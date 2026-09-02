---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/guidance-on-ndk-libc-interfaces-affected-by-permissions
title: NDK涉及的musl libc接口使用限制的说明
breadcrumb: API参考 > 标准库 > 附录 > NDK涉及的musl libc接口使用限制的说明
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0343e97252423a9f08b04b131ac15627c2f397b05c2c8975427c9f753c516022
---

## 概述

开发者使用DevEco Studio或者NDK进行应用开发时，可能涉及到使用musl libc的接口能力，因为musl libc的个别接口可能受多种系统和环境的限制而无法使用，此时可以通过本文档进行接口问题排查。

如果确认是下列原因导致接口调用报错，请通过“华为开发者联盟官网”->“支持”，[在线提单](https://developer.huawei.com/consumer/cn/support/)方式获取支持。

## Seccomp机制影响的musl接口

### 确定进程因为Seccomp机制终止的方法

* 查看进程faultlog日志，如果报错原因是signal:SIGSYS，且栈顶在ld-musl-{架构}.so.1库里，则进程终止可能是由Seccomp机制引起的。

  ```shell
  cat /data/log/faultlog/faultlogger/cppcrash-xxxx
  ```

  错误示例：

  ```txt
  Process name:com.example.myapplication
  Reason:Signal:SIGSYS(UNKNOWN)
  Fault thread Info:
  Tid:13893, Name:e.myapplication
  #00 pc 000a5d30 /system/lib/ld-musl-arm.so.1(sethostname+16)(584c9d0a0e9000497bb0d66799a9526a)
  #01 pc 00002f68 /data/storage/el1/bundle/libs/arm/libentry.so(test()+64)
  ```

### 常见可能受Seccomp机制影响的接口列表如下

| 头文件 | musl接口名称 |
| --- | --- |
| fcntl.h | name\_to\_handle\_at |
| fcntl.h | open\_by\_handle\_at |
| grp.h | initgroups |
| grp.h | setgroups |
| sched.h | setns |
| sched.h | unshare |
| sys/fanotify.h | fanotify\_init |
| sys/fanotify.h | fanotify\_mark |
| sys/fsuid.h | setfsgid |
| sys/fsuid.h | setfsuid |
| sys/klog.h | klogctl |
| sys/mount.h | mount |
| sys/mount.h | umount2 |
| sys/mount.h | umount |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/reboot.h | reboot |
| sys/sem.h | semctl |
| sys/sem.h | semget |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmat |
| sys/shm.h | shmctl |
| sys/shm.h | shmdt |
| sys/shm.h | shmget |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| sys/swap.h | swapoff |
| sys/swap.h | swapon |
| time.h | clock\_settime |
| sys/time.h | settimeofday |
| sys/timex.h | adjtimex |
| sys/timex.h | clock\_adjtime |
| unistd.h | acct |
| unistd.h | chroot |
| unistd.h | pause |
| unistd.h | setdomainname |
| unistd.h | setegid |
| unistd.h | setgid |
| unistd.h | sethostname |
| unistd.h | setregid |
| unistd.h | setresgid |
| unistd.h | setreuid |
| unistd.h | setuid |
| None | pivot\_root |
| None | init\_module |
| None | delete\_module |

## 内核没有对外开放影响的musl接口

| 头文件 | musl接口名称 |
| --- | --- |
| sys/fanotify.h | fanotify\_init |
| sys/fanotify.h | fanotify\_mark |
| unistd.h | acct |

## SELinux机制影响的musl接口

### 确定接口因为SELinux机制报错的方法

* 引入errno.h头文件，检查errno错误状态码，如果错误状态码是EACCES，则接口报错可能是由SELinux机制引起的。

### 常见可能受SELinux机制影响的接口列表如下

| 头文件 | musl接口名称 |
| --- | --- |
| net/if.h | if\_indextoname |
| net/if.h | if\_nametoindex |
| pty.h | forkpty |
| pty.h | openpty |
| semaphore.h | sem\_open |
| semaphore.h | sem\_unlink |
| stdlib.h | ptsname |
| stdlib.h | ptsname\_r |
| stdlib.h | posix\_openpt |
| stdlib.h | unlockpt |
| stdio.h | popen |
| stdio.h | pclose |
| sys/ioctl.h | ioctl |
| sys/mman.h | shm\_open |
| sys/mman.h | shm\_unlink |
| sys/mount.h | mount |
| sys/mount.h | umount |
| sys/mount.h | umount2 |
| sys/msg.h | msgctl |
| sys/msg.h | msgget |
| sys/msg.h | msgrcv |
| sys/msg.h | msgsnd |
| sys/sem.h | semget |
| sys/sem.h | semctl |
| sys/sem.h | semop |
| sys/sem.h | semtimedop |
| sys/shm.h | shmget |
| sys/shm.h | shmat |
| sys/shm.h | shmdt |
| sys/shm.h | shmctl |
| sys/stat.h | mkfifo |
| sys/stat.h | mkfifoat |
| sys/stat.h | mknod |
| sys/stat.h | mknodat |
| termios.h | tcgetattr |
| termios.h | tcsetattr |
| termios.h | tcsendbreak |
| termios.h | tcdrain |
| termios.h | tcflush |
| termios.h | tcflow |
| termios.h | tcgetsid |
| unistd.h | link |
| unistd.h | linkat |
| unistd.h | readlink |
| unistd.h | readlinkat |
| unistd.h | symlink |
| unistd.h | symlinkat |
| unistd.h | tcgetpgrp |
| unistd.h | tcsetpgrp |
| utmp.h | login\_tty |
| wordexp.h | wordexp |

参考：[third\_party\_musl 中与 SELinux 强相关的接口](guidance-on-ndk-libc-interfaces-affected-by-permissions.md#third_party_musl-中与-selinux-强相关的接口按实现路径归类)

## 沙箱机制影响的musl接口

沙箱机制可参考 [应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。

引入errno.h头文件，检查errno错误状态码，如果错误状态码是ENOENT，则接口报错可能是由沙箱机制引起的。

常见可能受沙箱机制影响的接口列表如下：

| 头文件 | musl接口名称 |
| --- | --- |
| fcntl.h | open |
| fcntl.h | openat |
| nl\_types.h | catopen |
| stdio.h | fopen |
| stdio.h | freopen |
| stdio.h | rename |
| stdio.h | renameat |
| stdio.h | renameat2 |
| stdio.h | tmpfile |
| stdio.h | tmpfile64 |

## 空实现或默认失败的musl接口

| 头文件 | musl接口名称 |
| --- | --- |
| netdb.h | getnetbyaddr |
| netdb.h | getnetbyname |
| stdio\_ext.h | \_\_fsetlocking |
| unistd.h | brk |
| utmp.h | getutent |
| utmp.h | pututline |
| utmp.h | setutent |
| utmp.h | pututline |
| utmp.h | utmpname |

## 需要特殊权限才能执行的musl接口

引入errno.h头文件，检查errno错误状态码，如果错误状态码是EPERM，则接口报错可能是由系统Capabilities安全机制引起的，也有可能是内核其他安全管控引起的。

常见可能受Capabilities机制影响的接口如下：

| 头文件 | musl接口名称 | Capabilities权限 |
| --- | --- | --- |
| None | pivot\_root | CAP\_SYS\_ADMIN |
| None | init\_module | CAP\_SYS\_MODULE |
| None | delete\_module | CAP\_SYS\_MODULE |
| fcntl.h | open\_by\_handle\_at | CAP\_DAC\_READ\_SEARCH |
| sys/klog.h | klogctl | CAP\_SYS\_ADMIN |
| sys/mount.h | mount | CAP\_SYS\_ADMIN |
| sys/mount.h | umount | CAP\_SYS\_ADMIN |
| sys/mount.h | umount2 | CAP\_SYS\_ADMIN |
| sys/reboot.h | reboot | CAP\_SYS\_BOOT |
| sys/swap.h | swapon | CAP\_SYS\_ADMIN |
| sys/swap.h | swapoff | CAP\_SYS\_ADMIN |
| sys/time.h | settimeofday | CAP\_SYS\_TIME |
| unistd.h | setdomainname | CAP\_SYS\_ADMIN |
| unistd.h | sethostname | CAP\_SYS\_ADMIN |
| unistd.h | chroot | CAP\_SYS\_CHROOT |

## third\_party\_musl 中与 SELinux 强相关的接口(按实现路径归类)

### pty/tty 与终端链路

| 头文件 | musl 接口名称 | 固定访问路径 |
| --- | --- | --- |
| pty.h | forkpty | 无；通过 openpty 间接访问 /dev/ptmx、/dev/pts/%d |
| pty.h | openpty | /dev/ptmx、/dev/pts/%d |
| stdlib.h | ptsname | 无；通过 ptsname\_r 间接得到 /dev/pts/%d |
| stdlib.h | ptsname\_r | /dev/pts/%d |
| stdlib.h | posix\_openpt | /dev/ptmx |
| stdlib.h | unlockpt | 无；对传入 fd 执行 ioctl(TIOCSPTLCK) |
| unistd.h | ctermid | 无；仅返回 /dev/tty 字符串 |
| unistd.h | ttyname\_r | /proc/self/fd/ |
| unistd.h | getpass | /dev/tty |
| utmp.h | login\_tty | 无；对传入 fd 执行 ioctl(TIOCSCTTY) |

说明：这类接口常关联 dev\_ptmx、devpts、tty\_device，在策略中通常不是“所有主体无差别放开”。

### 共享内存与命名信号量

| 头文件 | musl 接口名称 | 固定访问路径 |
| --- | --- | --- |
| sys/mman.h | shm\_open / shm\_unlink | /dev/shm/ |
| semaphore.h | sem\_open | /dev/shm/、/dev/shm/tmp-%d |
| semaphore.h | sem\_unlink | /dev/shm/ |

说明：/dev/shm 路径受系统侧 SELinux 管控。

### shell 执行与日志控制台

| 头文件 | musl 接口名称 | 固定访问路径 |
| --- | --- | --- |
| stdio.h | popen | /bin/sh |
| stdio.h | pclose | 无；等待并回收 popen 创建的子进程 |
| stdlib.h | system | /bin/sh |
| wordexp.h | wordexp | /bin/sh |
| syslog.h | syslog 相关接口 | /dev/log、/dev/console |
| fmtmsg.h | fmtmsg | /dev/console |

说明：/dev/log、/dev/console 的访问一般依赖主体域授权，不是默认全放行。

### 账号与敏感文件

| 头文件 | musl 接口名称 | 固定访问路径 |
| --- | --- | --- |
| shadow.h | getspnam\_r | /etc/tcb/%s/shadow、/etc/shadow |

说明：该类接口客体敏感度高，建议按最小权限单独审计。

### 无固定路径但存在 SELinux 管控点的接口

| 头文件 | musl 接口名称 | 可能受影响的原因 |
| --- | --- | --- |
| net/if.h | if\_indextoname | 通过 socket + ioctl(SIOCGIFNAME)，SELinux 管控 udp\_socket/unix\_dgram\_socket ioctl |
| net/if.h | if\_nametoindex | 通过 socket + ioctl(SIOCGIFINDEX)，SELinux 管控 udp\_socket/unix\_dgram\_socket ioctl |
| sys/mount.h | mount / umount / umount2 | 路径由参数传入，SELinux 管控 filesystem { mount unmount remount } 和挂载点 dir/file mounton |
| sys/msg.h | msgctl / msgget / msgrcv / msgsnd | System V 消息队列对象，SELinux 管控 msg/msgq |
| sys/sem.h | semget / semctl / semop / semtimedop | System V 信号量对象，SELinux 管控 sem |
| sys/shm.h | shmget / shmat / shmdt / shmctl | System V 共享内存对象，SELinux 管控 shm |
| sys/stat.h | mkfifo / mkfifoat | 路径由参数传入，SELinux 管控父目录 add\_name/create 和目标 fifo\_file |
| sys/stat.h | mknod / mknodat | 路径由参数传入，SELinux 管控父目录 add\_name/create 和目标 chr\_file/blk\_file/fifo\_file |
| sys/ioctl.h | ioctl | 通过 fd 访问目标客体，典型受 ioctl/allowxperm 管控 |
| termios.h | tcgetattr / tcsetattr | 通过 fd 执行 ioctl，典型客体是 tty\_device/devpts:chr\_file |
| termios.h | tcsendbreak / tcdrain / tcflush / tcflow / tcgetsid | 通过 fd 执行 ioctl，典型客体是 tty\_device/devpts:chr\_file |
| unistd.h | tcgetpgrp / tcsetpgrp | 通过 fd 执行 ioctl，典型客体是 tty\_device/devpts:chr\_file |
| unistd.h | link / linkat | 路径由参数传入，SELinux 管控 file link、父目录 add\_name |
| unistd.h | readlink / readlinkat | 路径由参数传入，SELinux 管控 lnk\_file read/getattr |
| unistd.h | symlink / symlinkat | 路径由参数传入，SELinux 管控 lnk\_file create、父目录 add\_name |

说明：以上接口没有在 musl 内部固定访问路径，是否触发 SELinux 拦截取决于调用主体、传入路径或 fd、内核对象标签及对应策略。
