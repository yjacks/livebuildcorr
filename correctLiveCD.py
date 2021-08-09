# 还没写

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
    os.system("mount -o loop " + iso_name + " iso_cp")
    os.system("cp -av iso_cp iso")
    os.system("cp -av iso_cp/.disk iso")
    os.system("umount iso_cp")


def DIY_live():
    os.mkdir("squashfs-root")
    os.system("unsquashfs iso/live/filesystem.squashfs squashfs-root")
    os.system("mount --bind /dev ~/squashfs-root/dev")
    os.system("mount -t proc proc ~/squashfs-root/proc")
    os.system("mount -t sysfs sys ~/squashfs-root/sys")
    os.system("cp /etc/resolv.conf ~/squashfs-root/etc/")
    os.system("cp /etc/apt/source.list ~/squashfs-root/etc/apt/")
    clearWindow()
    print("开始自定义")
    os.system("chroot squashfs-root")

    # 退出后

    os.system("umount squashfs-root/dev")
    os.system("umount squashfs-root/proc")
    os.system("umount squashfs-root/sys")
    os.system("mkdir squashfs-root/dev")
    os.system("mkdir squashfs-root/proc")
    os.system("mkdir squashfs-root/sys")
    os.system("rm iso/live/filesystem.squashfs")
    os.system("mksquashfs squashfs-root iso/live/filesystem.squashfs")
    print("LiveCD系统替换完成")


def isoBuild():
    os.system("chroot squashfs-root dpkg-query -W --showformat='${Package} ${Version}\n' \
    > iso/live/filesystem.manifest")
    os.system("cd ~/iso/ & find . -type f -print0 | xargs -0 md5sum > md5sum.txt")
    os.system("genisoimage -R -J -l -V 'liveSystem' -cache-inodes -b iso/isolinux/isolinux.bin \
    -c iso/isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o \
    ./live.iso ./iso")
    print("LiveCD生成完成")
