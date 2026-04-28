---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nce-on-ndk-libc-interfaces-affected-by-permissions
title: NDK涉及的musl libc接口使用限制的说明
breadcrumb: API参考 > 标准库 > 附录 > NDK涉及的musl libc接口使用限制的说明
category: harmonyos-references
scraped_at: 2026-04-28T08:19:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad4d06a8dc83769cf58c166d2f3b79bb2bbc00eec68ad392e7d7fb1eb397e32a
---

## 概述

开发者使用DevEco Studio或者NDK进行应用开发时，可能涉及到使用musl libc的接口能力，因为musl libc的个别接口可能受多种系统和环境的限制而无法使用，此时可以通过本文档进行接口问题排查。

如果确认是下列原因导致接口调用报错，请通过“华为开发者联盟官网”->“支持”，[在线提单](https://developer.huawei.com/consumer/cn/support/)方式获取支持。

## Seccomp机制影响的musl接口

### 确定进程因为Seccomp机制终止的方法

* 查看进程faultlog日志，如果报错原因是signal:SIGSYS，且栈顶在ld-musl-{架构}.so.1库里，则进程终止可能是由Seccomp机制引起的。

  ```
  1. cat /data/log/faultlog/faultlogger/cppcrash-xxxx
  ```

  错误示例：

  ```
  1. Process name:com.example.myapplication
  2. Reason:Signal:SIGSYS(UNKNOWN)
  3. Fault thread Info:
  4. Tid:13893, Name:e.myapplication
  5. #00 pc 000a5d30 /system/lib/ld-musl-arm.so.1(sethostname+16)(584c9d0a0e9000497bb0d66799a9526a)
  6. #01 pc 00002f68 /data/storage/el1/bundle/libs/arm/libentry.so(test()+64)
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
