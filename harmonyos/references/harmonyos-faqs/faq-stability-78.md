---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-78
title: CppCrash-SIGABRT（进程终止）类崩溃问题排查
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > CppCrash-SIGABRT（进程终止）类崩溃问题排查
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95a7c96854a04f65cc0579d3f5d5215ff822075c7c359ff2c02d8db877969626
---

## 问题现象

应用发生了CppCrash崩溃，崩溃信号是Signal:SIGABRT。

## 背景知识

* SIGABRT进程终止信号，信号值6，通常为进程自身调用标准函数库的abort()函数，崩溃原因在调用abort()函数的代码。由程序检测到异常时触发，如线程创建失败，文件描述符使用异常等，大多数情况是各基础库（C库等）进行校验操作，校验失败会主动终止进程。
* abort函数是C语言标准库中用于异常终止进程的函数，通过发送SIGABRT信号强制终止当前进程。
* assert断言函数是C++标准库<cassert>中提供的，用于检查程序是否满足某些条件，不满足断言条件时，会执行\_\_assert\_fail函数打印失败信息并调用abort函数终止进程。
* [napi\_fatal\_error](../harmonyos-guides/use-napi-about-error.md#napi_fatal_error)函数用于引发致命错误以立即终止进程，谨慎使用，仅在遇到无法恢复的严重错误时才应该调用该函数。

| 序号 | 故障根因 | 分析工具 | 解决方案 |
| --- | --- | --- | --- |
| 1 | 断言检查失败 | hstack,debug | 检查代码运行时的断言条件是否符合预期，修复业务逻辑异常。 |
| 2 | 未处理抛出的异常 | hstack,debug | 在抛出异常的位置使用try-catch捕获并处理异常。 |
| 3 | 调用napi\_fatal\_error引发致命错误 | hstack,debug | 排查napi\_fatal\_error的调用逻辑是否符合预期。 |
| 4 | 主动调用abort函数 | hstack,debug | 排查abort函数的调用逻辑是否符合预期，修改业务逻辑避免调用。 |

## 场景一

### 问题定位

1. 获取CppCrash崩溃日志。

   开发态：DevEco Studio会自动收集到日志工具栏的FaultLog下，该工具有高亮关键信息、跳转到对应的代码行、以及结构化日志等方便开发者分析的功能，详情可见使用文档[FaultLog](../harmonyos-guides/ide-fault-log.md)。

   运维态：

   * 直接导出故障日志目录：必须先打开开发者模式，再执行命令hdc file recv /data/log/faultlog/faultlogger/ [本地目录]。
   * 使用HiAppEvent故障订阅接口：可记录应用运行过程中的故障，为应用开发者提供的事件打点机制，详见[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)和[崩溃事件介绍](../harmonyos-guides/hiappevent-watcher-crash-events.md)。
2. 分析LastFatalMessage最后一条Fatal级日志中的断言信息。

   断言失败的LastFatalMessage规格如下：

   ```txt
   LastFatalMessage:Assertion failed: <断言条件> (<代码文件所在路径>: <函数>: <代码行>)
   ```

   如下案例中断言条件denominator != 0，代码文件napi\_init.cpp，函数TestAssertFail，断言函数在文件第15行。

   ```txt
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c970000f82d from:63533:20020375
   LastFatalMessage:Assertion failed: denominator != 0 (D:/MyDemo/MyCppDemo/entry/src/main/cpp/napi_init.cpp: TestAssertFail: 15)
   Fault thread info:
   Tid:63533, Name:com.hx.example
   #00 pc 00000000001b0958 /system/lib/ld-musl-aarch64.so.1(raise+216)(52299a28d60f0bb4073bd788bc023a3a)
   #01 pc 000000000015c8d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(52299a28d60f0bb4073bd788bc023a3a)
   #02 pc 000000000015cb0c /system/lib/ld-musl-aarch64.so.1(__assert_fail+308)(52299a28d60f0bb4073bd788bc023a3a)
   #03 pc 00000000000073ac /data/storage/el1/bundle/libs/arm64/libentry.so(57435a076d9792172ded7a138ab63256deb9d8b5)
   #04 pc 0000000000006f14 /data/storage/el1/bundle/libs/arm64/libentry.so(57435a076d9792172ded7a138ab63256deb9d8b5)
   #05 pc 000000000005af1c /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+268)(c3fa3582b8743a7f433777d19d6f67c9)
   #06 pc 0000000000e12868 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #07 pc 0000000000458190 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8StwCopy+384)
   #08 at anonymous entry (entry/src/main/ets/pages/Index.ets:18:20)
   ```
3. 使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)定位到问题代码行，调试代码。

   检查断言条件中变量的值是否符合预期。

   ```
   static int TestAssertFail(int denominator) 
   {
       int numerator = 10;
       // 断言：分母不能为零
       assert(denominator != 0);
       return numerator / denominator;
   }
   ```

### 分析结论

断言失败错误，断言条件为false时，进程会直接终止。

### 修改建议

检查代码运行时的断言条件是否符合预期，修改业务逻辑避免断言失败。

## 场景二

### 问题定位

1. 获取CppCrash崩溃日志。

   开发态：DevEco Studio会自动收集到日志工具栏的FaultLog下，该工具有高亮关键信息、跳转到对应的代码行、以及结构化日志等方便开发者分析的功能，详情可见使用文档[FaultLog](../harmonyos-guides/ide-fault-log.md)。

   运维态：

   * 直接导出故障日志目录：必须先打开开发者模式，再执行命令hdc file recv /data/log/faultlog/faultlogger/ [本地目录]。
   * 使用HiAppEvent故障订阅接口：可记录应用运行过程中的故障，为应用开发者提供的事件打点机制，详见[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)和[崩溃事件介绍](../harmonyos-guides/hiappevent-watcher-crash-events.md)。
2. 分析LastFatalMessage最后一条Fatal级日志中的断言信息。

   未处理抛出的异常的LastFatalMessage规格如下：

   ```txt
   LastFatalMessage:terminating due to uncaught exception of type <异常类型>: <异常原因描述>
   ```

   如下案例中未捕获的异常类型为MyException，自定义异常类型，异常信息为param must be number。

   ```txt
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317bf500008459 from:33881:20020213
   LastFatalMessage:terminating due to uncaught exception of type MyException: param must be number
   Fault thread info:
   Tid:33881, Name:o.myapplication
   #00 pc 00000000001b0784 /system/lib/ld-musl-aarch64.so.1(raise+216)(a280d230b646de38cb5d2ab7d7a041f9)
   #01 pc 000000000015c7d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(a280d230b646de38cb5d2ab7d7a041f9)
   #02 pc 00000000000b0790 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(e6d9b1440a02d752fc87df97026a92954370db6f)
   #03 pc 0000000000098c00 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(e6d9b1440a02d752fc87df97026a92954370db6f)
   #04 pc 00000000000af8fc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(e6d9b1440a02d752fc87df97026a92954370db6f)
   #05 pc 00000000000b29ac /data/storage/el1/bundle/libs/arm64/libc++_shared.so(e6d9b1440a02d752fc87df97026a92954370db6f)
   #06 pc 00000000000b2928 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(e6d9b1440a02d752fc87df97026a92954370db6f)
   #07 pc 0000000000002090 /data/storage/el1/bundle/libs/arm64/libentry.so(942b45a8269d83bb9a50e6a973061a115e9b3290)
   #08 pc 0000000000054ccc /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+220)(9a6c64e04b99f8978e8b7e78192bf769)
   #09 pc 0000000000e29880 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #10 pc 000000000045f7c8 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+392)
   #11 at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:57:88)
   ```
3. 使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)定位到问题代码行，调试代码。

   #07 TestTypeCheck(napi\_valuetype) at (D:/MyDemo/MyApplication3/entry/src/main/cpp/napi\_init.cpp:15) struct MyException : public std::exception

   排查抛出异常的业务逻辑是否符合预期，尽量用try-catch处理异常。

   ```
   struct MyException: public std::exception
   {
     const char * what () const throw ()
     {
       return "param must be number";
     }
   };

   static bool TestTypeCheck(napi_valuetype tp) 
   {
       if (tp != napi_number) {
           throw MyException();
       }
       return true;
   }
   ```

### 分析结论

未处理抛出的异常导致应用闪退。

### 修改建议

排查抛出异常的业务逻辑是否符合预期，尽量使用try-catch捕获并处理异常。

### 常见FAQ

Q：C++标准库中提供的常见异常有哪些？

A：见下表。

| 异常 | 描述 | 父类 |
| --- | --- | --- |
| std::exception | 所有标准 C++ 异常的父类。 | / |
| std::bad\_alloc | 动态内存分配失败。 | std::exception |
| std::bad\_cast | 类型转换失败。 | std::exception |
| std::bad\_typeid | 类型识别失败。 | std::exception |
| std::bad\_exception | 异常处理机制本身发生错误。 | std::exception |
| std::logic\_error | 程序逻辑异常。 | std::exception |
| std::domain\_error | 函数接收到其定义域之外的参数。 | std::logic\_error |
| std::invalid\_argument | 无效参数。 | std::logic\_error |
| std::length\_error | 长度错误。 | std::logic\_error |
| std::out\_of\_range | 访问超出有效范围的元素。 | std::logic\_error |
| std::runtime\_error | 运行时错误。 | std::exception |
| std::overflow\_error | 算术运算导致溢出。 | std::runtime\_error |
| std::range\_error | 函数返回值不在期望的范围内。 | std::runtime\_error |
| std::underflow\_error | 算术运算导致下溢。 | std::runtime\_error |

## 场景三

### 问题定位

1. 获取CppCrash崩溃日志。

   开发态：DevEco Studio会自动收集到日志工具栏的FaultLog下，该工具有高亮关键信息、跳转到对应的代码行、以及结构化日志等方便开发者分析的功能，详情可见使用文档[FaultLog](../harmonyos-guides/ide-fault-log.md)。

   运维态：

   * 直接导出故障日志目录：必须先打开开发者模式，再执行命令hdc file recv /data/log/faultlog/faultlogger/ [本地目录]。
   * 使用HiAppEvent故障订阅接口：可记录应用运行过程中的故障，为应用开发者提供的事件打点机制，详见[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)和[崩溃事件介绍](../harmonyos-guides/hiappevent-watcher-crash-events.md)。
2. 分析LastFatalMessage最后一条Fatal级日志中的断言信息。

   napi\_fatal\_error的LastFatalMessage规格如下：

   ```txt
   LastFatalMessage:[(<文件名>)(<napi_fatal_error>)] FATAL ERROR: <location参数：错误发生位置> <message参数：错误信息>
   // napi_fatal_error函数
   void napi_fatal_error(const char* location, size_t location_len, const char* message, size_t message_len);
   // 接收四个参数，一个位置信息，一个错误信息，两个长度参数。
   ```

   如下案例中location信息为(null)，代表传入的值为nullptr，错误信息为init failed。

   ```txt
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317bf400007342 from:29506:20020212
   LastFatalMessage:[napi_fatal_error] FATAL ERROR: (null) init failed

   Fault thread info:
   Tid:29506, Name:com.hx.example
   #00 pc 00000000001b0784 /system/lib/ld-musl-aarch64.so.1(raise+216)(a280d230b646de38cb5d2ab7d7a041f9)
   #01 pc 000000000015c7d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(a280d230b646de38cb5d2ab7d7a041f9)
   #02 pc 0000000000082f6c /system/lib64/platformsdk/libace_napi.z.so(napi_fatal_error+92)(9a6c64e04b99f8978e8b7e78192bf769)
   #03 pc 00000000000023c8 /data/storage/el1/bundle/libs/arm64/libentry.so(78ad9f0aa0391eabbe29a309c7c3016d845a867d)
   #04 pc 0000000000054ccc /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+220)(9a6c64e04b99f8978e8b7e78192bf769)
   #05 pc 0000000000e29880 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #06 pc 000000000045f0ec /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+368)
   #07 at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:39:19)
   ```
3. 使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)定位到问题代码行，调试代码。

   #03 FatalError(napi\_env\_\_\*, napi\_callback\_info\_\_\*) at (D:/MyDemo/MyCppDemo/entry/src/main/cpp/napi\_init.cpp:31)

   排查napi\_fatal\_error的调用逻辑是否符合预期。

   ```
   static napi_value FatalError(napi_env env, napi_callback_info info)
   {
       // 请注意，使用napi_fatal_error函数会导致应用进程直接终止，因此应该谨慎使用，仅在遇到无法恢复的严重错误时才应该调用该函数
       // 模拟一个致命错误条件
       bool errorCondition = true;
       if (errorCondition) {
           // 创建一个致命错误信息
           napi_fatal_error(nullptr, NAPI_AUTO_LENGTH, "init failed", NAPI_AUTO_LENGTH);
       }
       return nullptr;
   }
   ```

### 分析结论

进程主动调用napi\_fatal\_error引发致命错误导致应用闪退。

### 修改建议

排查napi\_fatal\_error的调用逻辑是否符合预期，修改业务逻辑避免调用。

## 场景四

### 问题定位

1. 获取CppCrash崩溃日志。

   开发态：DevEco Studio会自动收集到日志工具栏的FaultLog下，该工具有高亮关键信息、跳转到对应的代码行、以及结构化日志等方便开发者分析的功能，详情可见使用文档[FaultLog](../harmonyos-guides/ide-fault-log.md)。

   运维态：

   * 直接导出故障日志目录：必须先打开开发者模式，再执行命令hdc file recv /data/log/faultlog/faultlogger/ [本地目录]。
   * 使用HiAppEvent故障订阅接口：可记录应用运行过程中的故障，为应用开发者提供的事件打点机制，详见[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)和[崩溃事件介绍](../harmonyos-guides/hiappevent-watcher-crash-events.md)。
2. 从堆栈中观察到libcppcrash.so调用了abort函数。

   ```txt
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317b5200002d1c from:11548:20020050
   Fault thread info:
   Tid:11548, Name:.demo.dfxSample
   #00 pc 00000000001b0784 /system/lib/ld-musl-aarch64.so.1(raise+216)(a280d230b646de38cb5d2ab7d7a041f9)
   #01 pc 000000000015c7d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(a280d230b646de38cb5d2ab7d7a041f9)
   #02 pc 00000000000023c0 /data/storage/el1/bundle/libs/arm64/libcppcrash.so(5444004dfa6dd0d412948ee3459bc7bacaed9e0d)
   #03 pc 0000000000054ccc /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+220)(9a6c64e04b99f8978e8b7e78192bf769)
   #04 pc 0000000000e29880 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #05 pc 000000000045e474 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallarg0Imm8StwCopy+316)
   #06 at anonymous (entry|cppcrash|1.0.0|src/main/ets/components/signalSIGABRT/CppCrashSIGABRTPage.ts:58:17)
   ```
3. 使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)定位到问题代码行，调试代码。

   #02 AbortError(napi\_env\_\_\*, napi\_callback\_info\_\_\*) at (D:\MyDemo\DFXSampleDemo\feature\cppcrash\src\main\cpp\SIGABRTCrash\AbortExit.cpp:15)

   排查abort函数的调用逻辑是否符合预期。

   ```
   napi_value AbortExit::AbortError(napi_env env, napi_callback_info info)
   {
       // 模拟一个致命错误条件
       bool errorCondition = true;
       if (errorCondition) {
           abort();
       }
       return nullptr;
   }
   ```

### 分析结论

进程主动调用abort函数导致应用闪退。

### 修改建议

排查abort函数的调用逻辑是否符合预期，修改业务逻辑避免调用。
