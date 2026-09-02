---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-26
title: 应用在6.0版本系统上启动时发生闪退，5.0版本启动正常
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在6.0版本系统上启动时发生闪退，5.0版本启动正常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9087b09bbdc89f6d8fa02514e2a16a41b91bf4e8c1196d3ee84d300ce49372ae
---

## 问题现象

应用在6.0的系统版本上启动闪退，在5.0的系统版本上启动正常。

## 背景知识

1. ptrace(process trace)允许一个进程观察和控制另一个进程的执行。
2. ptrace反调试的核心是通过设置进程的追踪者(tracer)为自身进程，从而阻止其他调试器附加，因为系统限制每个进程只能有一个调试器附加。
3. 在6.0的系统版本上，[限制ptrace接口仅可在开发者调试模式下使用](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040675033)。
4. SIGABRT信号表示进程异常终止，通常为进程自身调用标准函数库的abort()函数。

## 问题定位

1. 查看faultlogger目录下的崩溃日志，异常信号是SIGABRT，从堆栈信息可以看出应用是因为libohosdrisklib.so库调用exit函数退出的。

   ```shell
   Process name:应用包名
   Process life time:8s
   Process Memory(kB): 266919(Rss)
   Device Memory(kB): Total 11690364, Free 999636, Available 3753984
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317d0d000024d2 from:9426:20020493
   LastFatalMessage:[appspawn_server.c:61]Unexpected call: exit(0)
   Fault thread info:
   Tid:9579, Name:应用包名后缀
   #00 pc 00000000001a2f14 /system/lib/ld-musl-aarch64.so.1(raise+216)(028acccfd609e1a349b61b0ca661fd38)
   #01 pc 000000000014f3f8 /system/lib/ld-musl-aarch64.so.1(abort+24)(028acccfd609e1a349b61b0ca661fd38)
   #02 pc 0000000000001a7c /system/lib64/libappspawn_helper.z.so(exit+144)(517365fff3f2e99f1a9275002b0b78f6)
   #03 pc 000000000000a36c /data/storage/el1/bundle/libs/arm64/libohosdrisklib.so(79bf68877a79cc39c06b698819ea6b3ebf2cd7bd)
   #04 pc 00000000001c2fc0 /system/lib/ld-musl-aarch64.so.1(start+240)(028acccfd609e1a349b61b0ca661fd38)
   ```
2. 使用5.0系统版本的设备进行测试，应用能正常启动，不会发生闪退。
3. 排查故障so库是否调用了ptrace接口，ptrace接口在6.0的系统版本上仅可在开发者调试模式下使用。

## 分析结论

6.0的系统版本为了保障安全隐私限制了ptrace接口使用，导致应用启动闪退。

## 修改建议

在6.0系统版本中，不再需要通过ptrace接口将当前进程设为自身的追踪者，从而阻止其他进程调试当前进程，因此可以移除对ptrace接口的使用。
