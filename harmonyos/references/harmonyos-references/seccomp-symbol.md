---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/seccomp-symbol
title: Seccomp开放系统调用列表
breadcrumb: API参考 > 标准库 > 附录 > Seccomp开放系统调用列表
category: harmonyos-references
scraped_at: 2026-09-02T14:53:38+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:72d78a138d87940026c66d986bcf971a240059348b62d0123e9601ae6f449102
---

## 概述

Seccomp（Secure Computing Mode）是Linux内核提供的轻量级系统调用过滤机制。该机制自Linux 2.6.12版本首次引入以来，已从仅支持严格模式（Strict）的极简形态，演进为以Seccomp‑BPF（Berkeley Packet Filter）为核心的主流形态。

HarmonyOS采用Seccomp‑BPF模式，可通过BPF程序自定义系统调用过滤规则，精确限制进程可调用的系统调用范围，降低恶意代码利用内核漏洞带来的风险，提升进程、容器与应用的安全隔离性。

本文档聚焦在HarmonyOS环境下，Seccomp针对不同设备类型开放的系统调用列表，旨在帮助开发者：

1. 快速掌握不同设备在Seccomp下的系统调用管控差异。
2. 基于业务场景选择合适的接口调用，避免因系统调用限制导致功能异常。

## Seccomp机制简介

* 基本机制

  Seccomp策略以策略文件的形式存在。在编译构建阶段，相关脚本会先解析策略文件，生成包含BPF指令策略的源文件，再将其编译成策略动态库。在用户态进程启动过程中，通过Seccomp系统调用将BPF指令策略加载至内核。
* 基本特点

  + 子进程会继承父进程的Seccomp策略。
  + Seccomp策略在进程运行时加载到内核后，以单向链表形式存储于内存中，且内容不可修改。
  + 进程可多次设置Seccomp策略。进程执行系统调用时，内核会遍历单向链表中每个节点的策略并比较其返回值，最终取优先级最高的返回值。

## Seccomp机制导致进程终止的判定方法

查看进程faultlog日志，如果报错原因是signal:SIGSYS，且栈顶在ld-musl-{架构}.so.1库里，则进程终止可能是由Seccomp机制引起的。

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

## Seccomp符号列表

| 系统调用 | 支持架构 | 支持设备 | 备注 |
| --- | --- | --- | --- |
| mbind | all | PC | - |
| mmap | arm64 | 全平台设备 | - |
| mmap | riscv64 | 全平台设备 | - |
| mmap2 | arm | 全平台设备 | - |
| munmap | all | 全平台设备 | - |
| mremap | all | 全平台设备 | - |
| mprotect | all | 全平台设备 | - |
| msync | all | 全平台设备 | - |
| mlock | all | 全平台设备 | - |
| munlock | all | 全平台设备 | - |
| mlockall | all | 全平台设备 | - |
| munlockall | all | 全平台设备 | - |
| mincore | all | 全平台设备 | - |
| madvise | all | 全平台设备 | - |
| mlock2 | all | 全平台设备 | - |
| membarrier | all | 全平台设备 | - |
| brk | all | 全平台设备 | - |
| remap\_file\_pages | arm | 全平台设备 | - |
| fork | arm | 全平台设备 | - |
| vfork | arm | 全平台设备 | - |
| exit | all | 全平台设备 | - |
| exit\_group | all | 全平台设备 | - |
| waitid | all | 全平台设备 | - |
| wait4 | all | 全平台设备 | - |
| set\_tid\_address | all | 全平台设备 | - |
| setpgid | all | 全平台设备 | - |
| getpgid | all | 全平台设备 | - |
| getsid | all | 全平台设备 | - |
| setsid | all | 全平台设备 | - |
| getpid | all | 全平台设备 | - |
| getppid | all | 全平台设备 | - |
| gettid | all | 全平台设备 | - |
| uname | all | 全平台设备 | - |
| personality | all | 全平台设备 | - |
| execve | all | 全平台设备 | - |
| execveat | all | 全平台设备 | - |
| clone | all | 全平台设备 | 仅允许不包含以下命名空间标志的调用：  CLONE\_NEWNS、  CLONE\_NEWPID、  CLONE\_NEWNETCLONE\_NEWCGROUP、  CLONE\_NEWUTS、  CLONE\_NEWIPC、  CLONE\_NEWUSER  符合条件返回ALLOW，否则返回TRAP。 |
| io\_setup | all | 全平台设备 | - |
| io\_destroy | all | 全平台设备 | - |
| io\_submit | all | 全平台设备 | - |
| io\_cancel | all | 全平台设备 | - |
| io\_getevents | all | 全平台设备 | - |
| openat | all | 全平台设备 | - |
| open | arm | 全平台设备 | - |
| close | all | 全平台设备 | - |
| creat | arm | 全平台设备 | - |
| read | all | 全平台设备 | - |
| write | all | 全平台设备 | - |
| readv | all | 全平台设备 | - |
| writev | all | 全平台设备 | - |
| pread64 | all | 全平台设备 | - |
| pwrite64 | all | 全平台设备 | - |
| preadv | all | 全平台设备 | - |
| pwritev | all | 全平台设备 | - |
| preadv2 | all | 全平台设备 | - |
| pwritev2 | all | 全平台设备 | - |
| lseek | all | 全平台设备 | - |
| \_llseek | arm | 全平台设备 | - |
| truncate | all | 全平台设备 | - |
| ftruncate | arm64 | 全平台设备 | - |
| ftruncate | riscv64 | 全平台设备 | - |
| truncate64 | arm | 全平台设备 | - |
| ftruncate64 | arm | 全平台设备 | - |
| fallocate | all | 全平台设备 | - |
| fcntl | all | 全平台设备 | - |
| fcntl64 | arm | 全平台设备 | - |
| flock | all | 全平台设备 | - |
| mknodat | all | 全平台设备 | - |
| mkdirat | all | 全平台设备 | - |
| mkdir | arm | 全平台设备 | - |
| rmdir | arm | 全平台设备 | - |
| unlinkat | all | 全平台设备 | - |
| unlink | arm | 全平台设备 | - |
| symlinkat | all | 全平台设备 | - |
| symlink | arm | 全平台设备 | - |
| linkat | all | 全平台设备 | - |
| link | arm | 全平台设备 | - |
| renameat | arm | 全平台设备 | - |
| renameat | arm64 | 全平台设备 | - |
| rename | arm | 全平台设备 | - |
| renameat2 | all | 全平台设备 | - |
| chdir | all | 全平台设备 | - |
| fchdir | all | 全平台设备 | - |
| faccessat | all | 全平台设备 | - |
| access | arm | 全平台设备 | - |
| faccessat2 | all | 全平台设备 | - |
| getcwd | all | 全平台设备 | - |
| getdents64 | all | 全平台设备 | - |
| getdents | arm | 全平台设备 | - |
| readlinkat | all | 全平台设备 | - |
| readlink | arm | 全平台设备 | - |
| newfstatat | arm64 | 全平台设备 | - |
| newfstatat | riscv64 | 全平台设备 | - |
| fstatat64 | arm | 全平台设备 | - |
| fstat | arm64 | 全平台设备 | - |
| fstat | riscv64 | 全平台设备 | - |
| stat64 | arm | 全平台设备 | - |
| lstat64 | arm | 全平台设备 | - |
| fstat64 | arm | 全平台设备 | - |
| statfs | arm64 | 全平台设备 | - |
| statfs | riscv64 | 全平台设备 | - |
| statfs64 | arm | 全平台设备 | - |
| fstatfs | arm64 | 全平台设备 | - |
| fstatfs | riscv64 | 全平台设备 | - |
| fstatfs64 | arm | 全平台设备 | - |
| sync | all | 全平台设备 | - |
| fsync | all | 全平台设备 | - |
| fdatasync | all | 全平台设备 | - |
| syncfs | all | 全平台设备 | - |
| sync\_file\_range | arm64 | 全平台设备 | - |
| sync\_file\_range | riscv64 | 全平台设备 | - |
| sync\_file\_range2 | arm | 全平台设备 | - |
| utimensat | all | 全平台设备 | - |
| utimensat\_time64 | arm | 全平台设备 | - |
| pipe2 | all | 全平台设备 | - |
| pipe | arm | 全平台设备 | - |
| dup | all | 全平台设备 | - |
| dup3 | all | 全平台设备 | - |
| dup2 | arm | 全平台设备 | - |
| sendfile | all | 全平台设备 | - |
| sendfile64 | arm | 全平台设备 | - |
| copy\_file\_range | all | 全平台设备 | - |
| vmsplice | all | 全平台设备 | - |
| splice | all | 全平台设备 | - |
| tee | all | 全平台设备 | - |
| readahead | all | 全平台设备 | - |
| fadvise64 | arm64 | 全平台设备 | - |
| fadvise64 | riscv64 | 全平台设备 | - |
| fadvise64\_64 | arm | 全平台设备 | - |
| quotactl | all | 全平台设备 | - |
| pivot\_root | riscv64 | 全平台设备 | - |
| statx | all | 全平台设备 | - |
| setxattr | all | 全平台设备 | - |
| lsetxattr | all | 全平台设备 | - |
| fsetxattr | all | 全平台设备 | - |
| getxattr | all | 全平台设备 | - |
| lgetxattr | all | 全平台设备 | - |
| fgetxattr | all | 全平台设备 | - |
| listxattr | all | 全平台设备 | - |
| llistxattr | all | 全平台设备 | - |
| flistxattr | all | 全平台设备 | - |
| removexattr | all | 全平台设备 | - |
| lremovexattr | all | 全平台设备 | - |
| fremovexattr | all | 全平台设备 | - |
| fchownat | all | 全平台设备 | - |
| fchown | arm64 | 全平台设备 | - |
| fchown | riscv64 | 全平台设备 | - |
| fchown32 | arm | 全平台设备 | - |
| lchown32 | arm | 全平台设备 | - |
| chown32 | arm | 全平台设备 | - |
| getuid | all | 全平台设备 | - |
| getuid32 | arm | 全平台设备 | - |
| geteuid | arm64 | 全平台设备 | - |
| geteuid | riscv64 | 全平台设备 | - |
| geteuid32 | arm | 全平台设备 | - |
| getgid | arm64 | 全平台设备 | - |
| getgid | riscv64 | 全平台设备 | - |
| getgid32 | arm | 全平台设备 | - |
| getegid | arm64 | 全平台设备 | - |
| getegid | riscv64 | 全平台设备 | - |
| getegid32 | arm | 全平台设备 | - |
| setresuid | arm64 | 全平台设备 | - |
| setresuid | riscv64 | 全平台设备 | - |
| setresuid32 | arm | 全平台设备 | - |
| getresuid | arm64 | 全平台设备 | - |
| getresuid | riscv64 | 全平台设备 | - |
| getresuid32 | arm | 全平台设备 | - |
| getresgid | arm64 | 全平台设备 | - |
| getresgid | riscv64 | 全平台设备 | - |
| getresgid32 | arm | 全平台设备 | - |
| getgroups | arm64 | 全平台设备 | - |
| getgroups | riscv64 | 全平台设备 | - |
| getgroups32 | arm | 全平台设备 | - |
| setpriority | all | 全平台设备 | - |
| getpriority | all | 全平台设备 | - |
| capget | all | 全平台设备 | - |
| capset | all | 全平台设备 | - |
| umask | all | 全平台设备 | - |
| getrlimit | arm64 | 全平台设备 | - |
| getrlimit | riscv64 | 全平台设备 | - |
| ugetrlimit | arm | 全平台设备 | - |
| setrlimit | all | 全平台设备 | - |
| prlimit64 | all | 全平台设备 | - |
| fchmod | all | 全平台设备 | - |
| fchmodat | all | 全平台设备 | - |
| chmod | arm | 全平台设备 | - |
| kill | all | 全平台设备 | - |
| tkill | all | 全平台设备 | - |
| tgkill | all | 全平台设备 | - |
| sigaltstack | all | 全平台设备 | - |
| rt\_sigsuspend | all | 全平台设备 | - |
| rt\_sigaction | all | 全平台设备 | - |
| sigaction | arm | 全平台设备 | - |
| rt\_sigprocmask | all | 全平台设备 | - |
| rt\_sigpending | all | 全平台设备 | - |
| rt\_sigtimedwait | all | 全平台设备 | - |
| rt\_sigtimedwait\_time64 | arm | 全平台设备 | - |
| rt\_sigqueueinfo | all | 全平台设备 | - |
| rt\_sigreturn | all | 全平台设备 | - |
| sigreturn | arm | 全平台设备 | - |
| signalfd4 | all | 全平台设备 | - |
| timerfd\_create | all | 全平台设备 | - |
| timerfd\_settime | all | 全平台设备 | - |
| timerfd\_gettime | all | 全平台设备 | - |
| timerfd\_gettime64 | arm | 全平台设备 | - |
| timerfd\_settime64 | arm | 全平台设备 | - |
| timer\_create | all | 全平台设备 | - |
| timer\_gettime | all | 全平台设备 | - |
| timer\_gettime64 | arm | 全平台设备 | - |
| timer\_getoverrun | all | 全平台设备 | - |
| timer\_settime | all | 全平台设备 | - |
| timer\_settime64 | arm | 全平台设备 | - |
| timer\_delete | all | 全平台设备 | - |
| clock\_gettime | all | 全平台设备 | - |
| clock\_gettime64 | arm | 全平台设备 | - |
| clock\_settime64 | arm | 全平台设备 | - |
| clock\_getres | all | 全平台设备 | - |
| clock\_getres\_time64 | arm | 全平台设备 | - |
| clock\_nanosleep | all | 全平台设备 | - |
| clock\_nanosleep\_time64 | arm | 全平台设备 | - |
| clock\_adjtime64 | arm | 全平台设备 | - |
| getitimer | all | 全平台设备 | - |
| setitimer | all | 全平台设备 | - |
| nanosleep | all | 全平台设备 | - |
| futex | all | 全平台设备 | - |
| futex\_time64 | arm | 全平台设备 | - |
| rt\_tgsigqueueinfo | all | 全平台设备 | - |
| semtimedop\_time64 | arm | 全平台设备 | - |
| pidfd\_send\_signal | all | 全平台设备 | - |
| shmget | all | PC | - |
| socket | all | 全平台设备 | - |
| socketpair | all | 全平台设备 | - |
| bind | all | 全平台设备 | - |
| listen | all | 全平台设备 | - |
| accept | all | 全平台设备 | - |
| accept4 | all | 全平台设备 | - |
| connect | all | 全平台设备 | - |
| getsockname | all | 全平台设备 | - |
| getpeername | all | 全平台设备 | - |
| sendto | all | 全平台设备 | - |
| recvfrom | all | 全平台设备 | - |
| setsockopt | all | 全平台设备 | - |
| getsockopt | all | 全平台设备 | - |
| shutdown | all | 全平台设备 | - |
| sendmsg | all | 全平台设备 | - |
| recvmsg | all | 全平台设备 | - |
| recvmmsg | all | 全平台设备 | - |
| recvmmsg\_time64 | arm | 全平台设备 | - |
| sendmmsg | all | 全平台设备 | - |
| sched\_setparam | all | 全平台设备 | - |
| sched\_setscheduler | all | 全平台设备 | - |
| sched\_getscheduler | all | 全平台设备 | - |
| sched\_getparam | all | 全平台设备 | - |
| sched\_setaffinity | all | 全平台设备 | - |
| sched\_getaffinity | all | 全平台设备 | - |
| sched\_yield | all | 全平台设备 | - |
| sched\_get\_priority\_max | all | 全平台设备 | - |
| sched\_get\_priority\_min | all | 全平台设备 | - |
| sched\_rr\_get\_interval | all | 全平台设备 | - |
| sched\_rr\_get\_interval\_time64 | arm | 全平台设备 | - |
| sched\_setattr | all | 全平台设备 | - |
| sched\_getattr | all | 全平台设备 | - |
| ioprio\_set | arm64 | 全平台设备 | - |
| ioprio\_set | riscv64 | 全平台设备 | - |
| ioprio\_get | arm64 | 全平台设备 | - |
| ioprio\_get | riscv64 | 全平台设备 | - |
| perf\_event\_open | all | 全平台设备 | - |
| getcpu | all | 全平台设备 | - |
| getrusage | all | 全平台设备 | - |
| times | all | 全平台设备 | - |
| process\_vm\_readv | all | 全平台设备 | - |
| process\_vm\_writev | all | 全平台设备 | - |
| process\_madvise | all | 全平台设备 | - |
| ioctl | all | 全平台设备 | - |
| inotify\_init1 | all | 全平台设备 | - |
| inotify\_init | arm | 全平台设备 | - |
| inotify\_add\_watch | all | 全平台设备 | - |
| inotify\_rm\_watch | all | 全平台设备 | - |
| eventfd2 | all | 全平台设备 | - |
| eventfd | arm | 全平台设备 | - |
| epoll\_create1 | all | 全平台设备 | - |
| epoll\_create | arm | 全平台设备 | - |
| epoll\_ctl | all | 全平台设备 | - |
| epoll\_pwait | all | 全平台设备 | - |
| epoll\_wait | arm | 全平台设备 | - |
| pselect6 | all | 全平台设备 | - |
| pselect6\_time64 | arm | 全平台设备 | - |
| \_newselect | arm | 全平台设备 | - |
| ppoll | all | 全平台设备 | - |
| ppoll\_time64 | arm | 全平台设备 | - |
| poll | arm | 全平台设备 | - |
| ptrace | all | 全平台设备 | - |
| restart\_syscall | all | 全平台设备 | - |
| prctl | all | 全平台设备 | - |
| seccomp | all | 全平台设备 | - |
| getrandom | all | 全平台设备 | - |
| memfd\_create | all | 全平台设备 | - |
| userfaultfd | all | 全平台设备 | - |
| gettimeofday | all | 全平台设备 | - |
| sysinfo | all | 全平台设备 | - |
| pidfd\_open | all | 全平台设备 | - |
| pidfd\_getfd | all | 全平台设备 | - |
| set\_robust\_list | all | 全平台设备 | - |
| cacheflush | arm | 全平台设备 | - |
| set\_tls | arm | 全平台设备 | - |
