from globalProject import *

iso_name = ""


def liveBuild():
    with open("a.sh", "w") as w:
        w.write("cd " + configDir + "/live\n")
        w.write("lb build")
    os.system("sh a.sh")
    a = os.popen("ls " + configDir + "/live *.iso")
    i = a.read()
    a.close()
    global iso_name
    iso_name = i[i.rfind("/") + 1:-1]


def mountIso():
    os.mkdir("iso_cp")
    os.mkdir("iso")
    os.system("mount -o loop " +"live/"+ iso_name + " iso_cp")
    os.system("cp -av iso_cp/* iso")
    os.system("cp -av iso_cp/.disk iso")
    os.system("umount iso_cp")


def DIY_live():
    os.mkdir("s-q")
    os.mkdir("squashfs-root")
    os.system("mount ./iso/live/filesystem.squashfs ./s-q")
    os.system("cp -av ./s-q/* squashfs-root")
    os.system("umount ./s-q")
    #os.system("mkdir squashfs-root/dev")
    #os.system("mkdir squashfs-root/proc")
    #os.system("mkdir squashfs-root/sys")
    os.system("mount --bind /dev squashfs-root/dev")
    os.system("mount -t proc proc squashfs-root/proc")
    os.system("mount -t sysfs sys squashfs-root/sys")
    os.system("cp /etc/resolv.conf squashfs-root/etc/")
    os.system("cp /etc/apt/sources.list ~/squashfs-root/etc/apt/")
    # clearWindow()
    print("开始自定义")
    os.system("chroot squashfs-root")

    # 退出后

    os.system("umount squashfs-root/dev")
    os.system("umount squashfs-root/proc")
    os.system("umount squashfs-root/sys")
    os.system("rm iso/live/filesystem.squashfs")
    os.system("mksquashfs squashfs-root iso/live/filesystem.squashfs")
    print("LiveCD系统替换完成")


def isoBuild():
    with open("b.sh","w") as w:
        w.write("chroot squashfs-root dpkg-query -W --showformat='${Package} ${Version}\\n'> iso/live/filesystem.manifest\n")
        w.write("cd iso/ & find . -type f -print0 | xargs -0 md5sum > md5sum.txt\n")
        w.write("genisoimage -R -J -l -V 'liveSystem' -cache-inodes -b isolinux/isolinux.bin \
        -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o \
        ./live.iso ./iso")
    os.system("sh b.sh")
    print("LiveCD生成完成")
