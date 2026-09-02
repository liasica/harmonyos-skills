---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-14
title: 在使用发音跟读功能时，应用出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 在使用发音跟读功能时，应用出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a222dd8ad6e32fc8595ac80c18fec32a6fb0cf5df02f6c31d1804ae769286c10
---

## 问题现象

应用的发音跟读功能使用时，出现闪退现象。

## 背景知识

* JavaScript是单线程的，对JS对象的操作必须在创建该JS对象的原始线程上进行，违反规则会导致多线程安全问题。
* 多线程安全问题检测原理可以参考[原理介绍](../best-practices/bpta-stability-ark-runtime-detection.md#section18515155816101)。
* 常见的[多线程安全问题](../best-practices/bpta-stability-ark-runtime-detection.md#section19357830121120)主要包括两类：非JS线程使用N-API接口和N-API接口使用其他线程的env。

## 问题定位

1. 查看faultlogger目录下的崩溃日志，故障原因是SIGABRT，进程异常终止，异常信息是ecma\_vm cannot run in multi-thread!，说明应用存在多线程安全问题。

   其中，thread:51212表示创建并拥有这个JavaScript环境的线程ID。currentThread:51605表示当前正在尝试操作这个JavaScript环境的线程ID。当前线程号为51605，而使用的JavaScript线程是由51212线程创建的，这表明虚拟机环境（vm/env）被跨线程使用，从而导致了多线程安全问题。

   ```screen
   Process name:com.hx.example
   Process life time:18446744073709544401s
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c000000c80c from:51212:20020224
   LastFatalMessage:[default] [CheckThread:465] Fatal: ecma_vm cannot run in multi-thread! thread:51212 currentThread:51605
   Fault thread info:
   Tid:51605, Name:com.hx.example
   #00 pc 000000000019a39c /system/lib/ld-musl-aarch64.so.1(raise+228)(ec494483f83e03f6f9e11c6a09ebdfed)
   #01 pc 000000000014750c /system/lib/ld-musl-aarch64.so.1(abort+20)(ec494483f83e03f6f9e11c6a09ebdfed)
   #02 pc 0000000000393380 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::CheckThread() const+1152)(138af8e6daf940060b31f75783edac70)
   #03 pc 00000000005cc410 /system/lib64/platformsdk/libark_jsruntime.so(panda::StringRef::NewFromUtf8(panda::ecmascript::EcmaVM const*, char const*, int)+68)(138af8e6daf940060b31f75783edac70)
   #04 pc 00000000000569f0 /system/lib64/platformsdk/libace_napi.z.so(napi_create_string_utf8+92)(d1d6ae93d149a5e76895580028b70a7c)
   #05 pc 000000000000820c /data/storage/el1/bundle/libs/arm64/libsingsound.so(1db4efb2d35f579ad7cafd7164aef54788f7f840)
   ```
2. 开启方舟多线程检测，具体方法可以参考[启用方舟多线程检测](../best-practices/bpta-stability-ark-runtime-detection.md#section7199344111510)。
3. 运行或调试当前应用，当程序出现多线程安全问题时，会弹出Crash log信息。点击信息中的链接，可以跳转至引起多线程安全问题的代码处。

## 分析结论

存在多线程安全问题，导致应用闪退。

## 修改建议

[启用方舟多线程检测](../best-practices/bpta-stability-ark-runtime-detection.md#section7199344111510)，通过崩溃日志直接跳转到引起多线程安全问题的代码行。
