# 公用变量
import os


def clearWindow():
    os.system("clear")


configDir = ""
readFilesList = ["binary",
                 "bootstrap",
                 "chroot",
                 "common",
                 "source"]
selectTypeKeyBinary = {"引导选项": [
    "LB_BINARY_FILESYSTEM",
    "LB_APT_INDICES",
    "LB_BOOTAPPEND_LIVE",
    "LB_BOOTAPPEND_INSTALL",
    "LB_BOOTAPPEND_LIVE_FAILSAFE",
    "LB_BOOTLOADERS"],
    "校验选项": ["LB_CHECKSUMS"],
    "DebianInstaller选项(建议不选)": ["LB_BUILD_WITH_CHROOT",
                                "LB_DEBIAN_INSTALLER",
                                "LB_DEBIAN_INSTALLER_DISTRIBUTION",
                                "LB_DEBIAN_INSTALLER_PRESEEDFILE",
                                "LB_DEBIAN_INSTALLER_GUI"],
    "引导选项(自身)": ["LB_GRUB_SPLASH",
                 "LB_HDD_LABEL",
                 "LB_HDD_SIZE",
                 "LB_HDD_PARTITION_START"],
    "名称选项": ["LB_ISO_APPLICATION",
             "LB_ISO_PREPARER",
             "LB_ISO_PUBLISHER",
             "LB_ISO_VOLUME"],
    "杂项": ["LB_JFFS2_ERASEBLOCK",
           "LB_MEMTEST",
           "LB_LOADLIN",
           "LB_WIN32_LOADER",
           "LB_NET_ROOT_FILESYSTEM",
           "LB_NET_ROOT_MOUNTOPTIONS",
           "LB_NET_ROOT_PATH",
           "LB_NET_ROOT_SERVER",
           "LB_NET_COW_FILESYSTEM",
           "LB_NET_COW_MOUNTOPTIONS",
           "LB_NET_COW_PATH",
           "LB_NET_COW_SERVER",
           "LB_NET_TARBALL",
           "LB_ONIE",
           "LB_ONIE_KERNEL_CMDLINE",
           "LB_FIRMWARE_BINARY",
           "LB_FIRMWARE_CHROOT",
           "LB_SWAP_FILE_PATH",
           "LB_SWAP_FILE_SIZE",
           "LB_UEFI_SECURE_BOOT"
           ]}
selectTypeKeyBootstrap = {"版本选项": ["LB_DISTRIBUTION", "LB_PARENT_DISTRIBUTION"],
                          "镜像源选项": [
                              "LB_PARENT_DEBIAN_INSTALLER_DISTRIBUTION"
                              "LB_PARENT_MIRROR_BOOTSTRAP"
                              "LB_PARENT_MIRROR_CHROOT"
                              "LB_PARENT_MIRROR_CHROOT_SECURITY"
                              "LB_PARENT_MIRROR_BINARY"
                              "LB_PARENT_MIRROR_BINARY_SECURITY"
                              "LB_PARENT_MIRROR_DEBIAN_INSTALLER"
                              "LB_MIRROR_BOOTSTRAP"
                              "LB_MIRROR_CHROOT"
                              "LB_MIRROR_CHROOT_SECURITY"
                              "LB_MIRROR_BINARY"
                              "LB_MIRROR_BINARY_SECURITY"
                              "LB_MIRROR_DEBIAN_INSTALLER"
                          ],
                          "杂项": [
                              "LB_BOOTSTRAP_QEMU_ARCHITECTURES",
                              "LB_BOOTSTRAP_QEMU_EXCLUDE",
                              "LB_BOOTSTRAP_QEMU_STATIC"
                          ]
                          }
selectTypeKeyBuild = {"架构及版本选项": [""" 
    [Image]
    Architecture: amd64
    Archive - Areas: main
    Distribution: stretch
    Mirror - Bootstrap: http://deb.debian.org/debian/

    [FIXME]
    Configuration - Version: 1:20190311
    Name: live - image
    Type: iso - hybrid
    """
                                  ]}
selectTypeKeyChroot = {"本体选项":
                           ["LB_CHROOT_FILESYSTEM",
                            "LB_UNION_FILESYSTEM",
                            "LB_INTERACTIVE",
                            "LB_KEYRING_PACKAGES",
                            "LB_LINUX_FLAVOURS",
                            "LB_LINUX_PACKAGES",
                            "LB_SECURITY",
                            "LB_UPDATES",
                            "LB_BACKPORTS"]
                       }
selectTypeKeyCommon = {"APT选项": ["LB_APT",
                                 "LB_APT_FTP_PROXY",
                                 "LB_APT_HTTP_PROXY",
                                 "LB_APT_PIPELINE",
                                 "LB_APT_RECOMMENDS",
                                 "LB_APT_SECURE",
                                 "LB_APT_SOURCE_ARCHIVES"
                                 ],
                       "杂项": ["LB_CACHE",
                              "LB_CACHE_INDICES",
                              "LB_CACHE_PACKAGES",
                              "LB_CACHE_STAGES",
                              "LB_DEBCONF_FRONTEND",
                              "LB_DEBCONF_PRIORITY",
                              ],
                       "默认程序选项": ["LB_INITRAMFS",
                                  "LB_INITRAMFS_COMPRESSION",
                                  "LB_INITSYSTEM",
                                  "LB_FDISK",
                                  "LB_LOSETUP",
                                  "LB_MODE",
                                  "LB_SYSTEM",
                                  "LB_TASKSEL"],
                       "APT杂项": ["APT_OPTIONS",
                                 "APTITUDE_OPTIONS",
                                 "DEBOOTSTRAP_OPTIONS",
                                 "DEBOOTSTRAP_SCRIPT",
                                 "GZIP_OPTIONS",
                                 "ISOHYBRID_OPTIONS"]}
selectTypeKeySource = {"杂项": ["LB_SOURCE",
                              "LB_SOURCE_IMAGES"]
                       }
selectTypeKeysNames = [
    selectTypeKeyBinary,
    selectTypeKeyBootstrap,
    selectTypeKeyBuild,
    selectTypeKeyChroot,
    selectTypeKeyCommon,
    selectTypeKeySource
]
selectTypeKeys = dict(zip(readFilesList, selectTypeKeysNames))
