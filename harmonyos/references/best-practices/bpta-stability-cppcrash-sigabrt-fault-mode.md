---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-cppcrash-sigabrt-fault-mode
title: SIGABRT进程主动终止故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > CppCrash故障模式说明 > SIGABRT进程主动终止故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:7c1639cfdf6c0d823c954b61e9d0dae66364f1b23377e840972b14cae4fef1dd
---

## 根因描述

SIGABRT进程异常终止，通常为进程自身调用标准函数库的abort()函数导致，崩溃原因位于调用abort()函数的代码中。程序检测到异常时触发该终止，如线程创建失败、文件描述符使用异常等。基础库（如C库等）进行校验操作时，校验失败会主动终止进程。若内存被破坏间接导致abort，则定位困难；因为内存损坏可能发生在其他地方，但最终表现为abort()被调用。

## 问题分析思路

此类问题，通常有以下几种可能：

1、主动触发abort：业务代码、库函数、NAPI检测到异常，主动终止进程。

2、内存损坏：释放后使用、越界访问、生命周期不匹配。

3、资源不足或超规格：文件描述符超过限制、线程/内存分配失败。

4、库函数校验失败：C/C++标准库或系统库触发防护机制。

5、符号冲突导致异常捕获失败、类型转换异常、字符串转化异常等。

问题分析的步骤如下：

1. **确认类型**：查看崩溃日志文件中是否包含LastFatalMessage字段，该字段用于显示进程终止的原因，可根据其内容查阅相关文件或代码，确认崩溃原因。
2. **调用栈分析**：找到触发abort的调用栈，通常跳过libc.so等系统库栈帧，根据栈帧崩溃文件名，转到业务代码栈帧查看崩溃函数，同时结合该处历史崩溃情况，缩小分析范围。
3. **代码分析**：参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)，使用llvm-addr2line工具结合调用栈文件和地址偏移，定位到具体业务代码行。根据代码上下文，分析其中存在的逻辑问题，找到触发abort的原因，必要时沿栈帧多分析几层。
4. **更多日志**：结合崩溃日志文件中的其他信息，以及hilog、kmsg等日志，还原故障现场信息，进行定位。

## 关键字

关注CppCrash故障日志中是否有如下关键字：

* LastFatalMessage
* abort()
* SIGABRT

## 案例分析

### 案例一：主动abort触发故障

**问题现象**

业务代码调用后，应用退出并生成崩溃文件。

**问题分析**

1. 查看崩溃文件内容。

   **说明** 

   DevEco Studio成功连接手机时，可打开日志窗口找到FaultLog选项，点击即可查看崩溃日志。

   证据1：进程是触发SIGABRT退出，并打印了LastFatalMessage信息。

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317bef00002b7b from:11131:20020207
   LastFatalMessage:Assertion failed: pc != nullptr (.../entry/src/main/cpp/sigabort/sigabort.cpp: TriggerAssertAbort: 37)
   ```

   说明1：LastFatalMessage是进程退出前的最后一条fatal级别日志，对于SIGABRT类崩溃问题其一般能提供程序主动异常终止的原因，对定位该类问题有很大帮助。
2. 分析崩溃栈。ld-musl-aarch64.so.1中的栈帧，为触发abort的常见流程，可以跳过该部分到业务栈帧。

   证据2：

   ```screen
   Fault thread info:
   Tid:11131, Name:ppcrashanalysis
   #00 pc 00000000001d78dc /system/lib/ld-musl-aarch64.so.1(raise+228)(5c1c07696048fe989cb4fc766531ce2e)
   #01 pc 000000000017f000 /system/lib/ld-musl-aarch64.so.1(abort+20)(5c1c07696048fe989cb4fc766531ce2e)
   #02 pc 000000000017f258 /system/lib/ld-musl-aarch64.so.1(__assert_fail+344)(5c1c07696048fe989cb4fc766531ce2e)
   #03 pc 0000000000021e58 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerAssertAbort(napi_env__*, napi_callback_info__*)+108)(9292a79a3a85a8e682ac2c774db1d42ff07d1ac4)
   ```

   说明2：通常认为标准库、系统库较为稳定，因此优先分析崩溃栈帧中的业务部分调用栈。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号找到执行上下文。

   通常用法为 llvm-addr2line -Cfie libentry.so 0000000000021e58，即可定位到代码行号，so为带符号版本。

   证据3：从上往下跳过C库的调用栈，找到调用abort()函数的调用栈（#03层调用栈），从这里结合LastFatalMessage进行分析。

   ```cpp
   napi_value TriggerAssertAbort(napi_env env, napi_callback_info info)
   {
       void *pc = nullptr;
       if (env == nullptr) {
           pc = malloc(1024); // 1024 : size
       }
       assert(pc != nullptr);
       return {};
   }
   ```

   说明3：由于pc初始化为空，assert时，触发abort()。

**问题结论与总结**

应用主动调用abort()函数触发故障。

### 案例二：因资源不足导致线程创建失败进而崩溃

**问题现象**

应用崩溃闪退。

**问题分析**

1. 查看崩溃文件内容，关注LastFatalMessage字段信息。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c0100008557 from:34135:20020225
   LastFatalMessage:terminating due to uncaught exception of type std::__n1::system_error: thread constructor failed: Resource temporarily unavailable
   ```

   说明1：线程创建失败抛出异常。
2. 分析调用栈特征，跳过标准库进行分析。

   证据2：

   ```screen
   Fault thread info:
   Tid:52028, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 00000000000b088c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #03 pc 0000000000098cfc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #04 pc 00000000000af9f8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #05 pc 00000000000b2aa8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #06 pc 00000000000b2a24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #07 pc 000000000001c30c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerThreadNoMemoryAbort(napi_env__*, napi_callback_info__*)+148)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #08 pc 00000000000695fc /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+284)(f28a6a2c8c07c7d146adaaac012d68e9)
   ```

   说明2：通过栈帧初步可以判断#07为正常业务操作，触发异常。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号找到执行上下文。根据第#07栈帧找到代码如下。

   ```cpp
   napi_value TriggerThreadNoMemoryAbort(napi_env env, napi_callback_info info)
   {
       std::vector<std::thread> workerPool;
       while (true) {
           if (g_runningThreads.load() >= SPEC_THREAD_CEILING) {
               throw std::system_error(
                   std::make_error_code(std::errc::resource_unavailable_try_again),
                   "thread constructor failed");
           }
           workerPool.emplace_back(WorkerFunc);
       }
   }
   ```

   说明3：应用侧当判断正在运行线程数量超过SPEC\_THREAD\_CEILING时，主动抛出异常。
4. 排查业务分析在运行线程数量超过SPEC\_THREAD\_CEILING的最大值的原因。

**问题结论与总结**

应用创建线程超限触发异常。

**修复建议**

线程资源使用完成后，要及时回收释放相关资源。

### 案例三：库函数校验失败触发崩溃

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看崩溃文件内容，关注LastFatalMessage字段信息。

   证据1：可以看到是由于fd值超过1024才触发了崩溃。

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c0100006f7d from:28541:20020225
   LastFatalMessage:Musl Fortify runtime error: file descriptor 1540 >= FD_SETSIZE 1024
   ```

   说明1：musl库校验失败，触发崩溃。
2. 分析调用栈特征。识别为代码执行触发了句柄异常。

   证据2：

   ```screen
   Fault thread info:
   Tid:52731, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 000000000016df2c /system/lib/ld-musl-aarch64.so.1(__fortify_error+240)(70dc02a619c18db57e03f7ccbad15eb1)
   #03 pc 000000000016df74 /system/lib/ld-musl-aarch64.so.1(__fd_chk+68)(70dc02a619c18db57e03f7ccbad15eb1)
   #04 pc 000000000001be9c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerSelectOverflowAbort(napi_env__*, napi_callback_info__*)+372)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #05 pc 00000000000695fc /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+284)(f28a6a2c8c07c7d146adaaac012d68e9)
   ```

   说明2：C库主动调用abort()函数，需要回溯到对应业务侧代码上下文进行分析。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号找到执行上下文。

   ```screen
   #04 pc 000000000001be9c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerSelectOverflowAbort(napi_env__*, napi_callback_info__*)+372)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   找到崩溃代码行如下。

   ```cpp
   napi_value TriggerSelectOverflowAbort(napi_env env, napi_callback_info info)
   {
       std::vector<int> openFds;
       int highFd = -1;
       const int fdNum = 1500;
       for (int i = 0; i < fdNum; ++i) {
           int fd = open("/dev/null", O_RDONLY);
           if (fd < 0) {
               std::cerr << "[ERROR] Open file failed at iteration: " << i << std::endl;
               break;
           }
           openFds.push_back(fd);
           highFd = fd;
       }
       
       fd_set readFds;
       FD_ZERO(&readFds);
       FD_SET(highFd, &readFds);
       
       for (int fd : openFds) {
           close(fd);
       }
       return {};
   }
   ```
4. 继续分析通过调用栈分析进程终止的原因。定位行号#03栈帧查看\_\_fd\_chk()函数的实现如下。

   证据3：

   ```cpp
   void __fd_chk(int fd)
   {
       if (fd < 0) {
           __fortify_error("file descriptor %d < 0", fd);
       }
       if (fd >= FD_SETSIZE) {
           __fortify_error("file descriptor %d >= FD_SETSIZE %d", fd, FD_SETSIZE);  ----  对应反汇编的结果
       }
   }
   ```

   查看FD\_SET\_SIZE定义如下。

   ```cpp
   #undef FD_SETSIZE
   #define FD_SETSIZE                      1024
   #endif
   ```

   可以看到\_\_fortify\_error会主动调用abort()函数导致进程退出。

   ```cpp
   void __fortify_error(const char* info, ...)
   {
       va_list ap;
       va_start(ap, info);
       fprintf(stderr, FORTIFY_RUNTIME_ERROR_PREFIX);
       vfprintf(stderr, info, ap);
       va_end(ap);
       abort();
   }
   ```
5. 查看崩溃进程的FD信息。

   进程的崩溃文件，会把进程打开的句柄信息一起写入，用于辅助FD相关问题定位。

   证据4：查看crash文件，fd数值确实超过了1024。结合LastFatalMessage信息，推断在执行FD\_SET()函数时因highFd的值大于1024导致进程主动终止退出。

   ```screen
   1531->/dev/null native object of unknown type 0
   1532->/dev/null native object of unknown type 0
   1533->/dev/null native object of unknown type 0
   1534->/dev/null native object of unknown type 0
   1535->/dev/null native object of unknown type 0
   1536->/dev/null native object of unknown type 0
   1537->/dev/null native object of unknown type 0
   1538->/dev/null native object of unknown type 0
   1539->/dev/null native object of unknown type 0
   1540->/dev/null native object of unknown type 0
   ```
6. 进一步分析业务发现为使用select()函数监听FD时校验FD数量超限触发进程主动终止。

**问题结论与总结**

libc中select()函数限制监控的FD不超过1024，超过会触发进程主动终止。

**修复建议**

根据使用场景，选择合适的系统API，可以使用poll()函数替换使用select()函数。

### 案例四：符号冲突导致异常捕获失败

**问题现象**

问题场景是在A库中抛出一个异常类型E，在B库中catch该类型异常E，未正确catch该指定类型异常E，导致崩溃。

**问题分析**

1. 查看崩溃文件内容，关注LastFatalMessage字段信息。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317bca00009cd6 from:40150:20020170
   LastFatalMessage:terminating due to uncaught exception of type vip::VError: VError from A
   ```

   说明1：提示有未捕获异常，导致崩溃。
2. 查看异常栈帧。

   证据2：根据调用栈，可以看到在#08层栈中抛出异常，跳过中间系统栈帧。

   ```screen
   Fault thread info:
   Tid:53515, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 00000000000b088c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #03 pc 0000000000098cfc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #04 pc 00000000000af9f8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #05 pc 00000000000b2aa8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #06 pc 00000000000b2a24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #07 pc 0000000000001e40 /data/storage/el1/bundle/libs/arm64/libA.so(ThrowVError+52)(349a3ebe4027bdd63ef93adab5c4a9871b42ebb1)
   #08 pc 0000000000005858 /data/storage/el1/bundle/libs/arm64/libB.so(TestCatchVError+12)(848c923306593c6a5210c683bc464a59ab06783f)
   #09 pc 000000000001cd78 /data/storage/el1/bundle/libs/arm64/libentry.so(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #10 pc 000000000001cb10 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerExceptionAbort(napi_env__*, napi_callback_info__*)+156)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   找到#07帧对应代码如下。

   ```cpp
   extern "C" void ThrowVError()
   {
       throw(vip::VError());
   }
   ```

   向调用上层溯源#08帧抛出了异常的代码行如下。

   ```cpp
   extern "C" const char* TestCatchVError()
   {
       try {
           ThrowVError();
       } catch (vip::VError const& e) {
           return "vip::VError 被 vip::VError catch";
       }
       return "";
   }
   ```

   说明2：此处未按照预期捕获vip::VError，导致了程序崩溃。
3. 分析更多上下文。

   #09帧调用TestCatch()函数。

   ```screen
   auto testCatch = reinterpret_cast<ReturnType>(dlsym(handleB, "TestCatchVError"));

   OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, TAG,
                "%{public}s vip::VError exception catch info： %{public}s", "libB", testCatch());
   ```

   #10帧函数片段为。

   ```cpp
   OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, TAG, "##################################################################");
   OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, TAG, "dlopen libA.so RTLD_LOCAL -> dlopen libB.so RTLD_LOCAL");
   handleA = dlopen("libA.so", RTLD_NOW | RTLD_LOCAL);
   handleB = dlopen("libB.so", RTLD_NOW | RTLD_LOCAL);
   TestDlopen(handleA, handleB);
   dlclose(handleB);
   dlclose(handleA);
   ```

   说明：try catch底层机制当异常被抛出后，运行时会沿着调用栈向上查找catch子句。每个catch子句会检查抛出异常的std::type\_info与catch子句所期望的type\_info是否相同或是否具有派生关系，catch(...)是万能捕获，不进行任何类型检查。
4. 分析libA和libB中是否为同一故障。

   证据4：拿到vip::VError具体类型信息。

   ```cpp
   extern "C" const std::type_info* GetAVErrorTypeInfo()
   {
       return &typeid(vip::VError);
   }
   ```

   通过打印地址信息结果如下。

   ```screen
   com.examp...olexport  E     dlopen libA.so RTLD_LOCAL -> dlopen libB.so RTLD_LOCAL
   com.examp...olexport  E     libA  vip::VError sym info： addr=0x5be0c03038, from=libA.so
   com.examp...olexport  E     libB  vip::VError sym info： addr=0x5be0c42da8, from=libB.so
   ```

   继续分析代码Verror.h。

   ```cpp
   class VError : public std::exception {
   public:
       VError() = default;
       ~VError() override = default;
       const char* What() const noexcept
       {
           return "VError from A";
       }
   };
   ```

   这种构建模式下，libA.so和libB.so中都会包含VError异常的弱符号V。

   ```screen
   $ llvm-nm -CD libA.so | grep 'typeinfo for vip::VError'
   0000000000003038 V typeinfo for vip::VError
   $ llvm-nm -CD libB.so | grep 'typeinfo for vip::VError'
   0000000000002da8 V typeinfo for vip::VError
   ```

**问题结论与总结**

当两个库都包含VError的弱符号V，并使用RTLD\_LOCAL加载时，先加载A库再加载B库时，整个进程有两份type\_info对象，异常捕获失败。

先加载A库，其弱符号V（typeinfo）进入A库自身的局部符号表，但对外部不可见。再加载B库，由于B库依赖A库，但A库已加载，动态链接器不会重复加载。然而RTLD\_LOCAL参数使得B库无法访问A库的局部符号，且B库自身因头文件内联定义生成了自己的弱符号V，因此B库使用自己的副本。

**修复建议**

采用声明和定义分离的方式。

### 案例五：类型转换异常触发崩溃

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看LastFatalMessage信息，分析调用栈特征。可以看到是由于std::bad\_cast才触发了异常。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c0100009f25 from:40741:20020225
   LastFatalMessage:terminating due to uncaught exception of type std::bad_cast: std::bad_cast
   ```
2. 分析调用栈特征。可注意到触发了\_\_cxa\_bad\_cast异常。

   证据2：

   ```screen
   Fault thread info:
   Tid:54874, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 00000000000b088c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #03 pc 0000000000098cfc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #04 pc 00000000000af9f8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #05 pc 00000000000b2aa8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #06 pc 00000000000b2a24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #07 pc 0000000000098b88 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_bad_cast+48)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #08 pc 000000000001c5e8 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBadCastAbort(napi_env__*, napi_callback_info__*)+104)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   说明2：C库主动调用abort()函数，需要找到对应业务侧代码进行定位。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。

   找到业务栈帧：#08 pc 000000000001c5e8 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerBadCastAbort(napi\_env\_\_\*, napi\_callback\_info\_\_\*)+104)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)。

   证据3：找到崩溃行号。

   ```cpp
   napi_value TriggerBadCastAbort(napi_env env, napi_callback_info info)
   {
       DerivedA instanceA;
       Base& baseRef = instanceA;
       DerivedB& invalidBRef = dynamic_cast<DerivedB&>(baseRef);
       return {};
   }
   ```

   说明3：说明baseRef转成DerivedB时，触发了异常。

**问题结论与总结**

对象向下转型时，如果对象不是目标类型，dynamic\_cast会抛出bad\_cast异常触发崩溃。

**修复建议**

慎用或者不用类型转换。

### 案例六：数组越界触发崩溃

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看LastFatalMessage信息，分析调用栈特征。可以看到是由于std::out\_of\_range: vector才触发了异常。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c010000bfad from:49069:20020225
   LastFatalMessage:terminating due to uncaught exception of type std::out_of_range: vector
   ```
2. 分析调用栈特征。可注意到触发了std::out\_of\_range异常。

   证据2：

   ```screen
   Fault thread info:
   Tid:55630, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 00000000000b088c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #03 pc 0000000000098cfc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #04 pc 00000000000af9f8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #05 pc 00000000000b2aa8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #06 pc 00000000000b2a24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #07 pc 00000000000228f0 /data/storage/el1/bundle/libs/arm64/libentry.so(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #08 pc 00000000000228b0 /data/storage/el1/bundle/libs/arm64/libentry.so(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #09 pc 000000000001c8e0 /data/storage/el1/bundle/libs/arm64/libentry.so(std::__n1::vector<int, std::__n1::allocator<int>>::at(unsigned long)+64)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   #10 pc 000000000001c714 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerVectorExceptionAbort(napi_env__*, napi_callback_info__*)+88)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   说明2：C库主动调用abort()函数，需要找到对应业务侧代码进行定位。
3. 基于崩溃栈定位行号。

   根据#10 pc 000000000001c714 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerVectorExceptionAbort(napi\_env\_\_\*, napi\_callback\_info\_\_\*)+88)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)找到崩溃行号。

   证据3：

   ```cpp
   napi_value TriggerVectorExceptionAbort(napi_env env, napi_callback_info info)
   {
       std::vector<int> vec = {1, 2, 3};
       int val = vec.at(10);
   }
   ```

   说明3：使用at()函数访问数组元素时，触发异常。

**问题结论与总结**

因数组访问越界导致C库越界检查触发的SIGABRT类崩溃。

**修复建议**

数组通过下标访问时需要严格校验下标的合法性。

### 案例七：NAPI触发异常

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看LastFatalMessage信息，分析调用栈特征。可以看到是由于NAPI接口调用失败触发了异常。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c010000d2cb from:53963:20020225
   LastFatalMessage:[napi_fatal_error] FATAL ERROR: NativeModule::TriggerOfficialFatalAbort Critical resource error! Triggering intentional Abort.
   ```
2. 分析调用栈特征。可注意到触发了napi\_fatal\_error异常。

   证据2：

   ```screen
   Fault thread info:
   Tid:57078, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 000000000008e38c /system/lib64/platformsdk/libace_napi.z.so(napi_fatal_error+92)(f28a6a2c8c07c7d146adaaac012d68e9)
   #03 pc 000000000001c92c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerNapiFatalAbort(napi_env__*, napi_callback_info__*)+44)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   说明2：NAPI接口内部检测到异常，调用napi\_fatal\_error触发abort。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。

   溯源#03 pc 000000000001c92c /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerNapiFatalAbort(napi\_env\_\_\*, napi\_callback\_info\_\_\*)+44)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a) 崩溃行号。

   证据3：

   ```cpp
   napi_value TriggerNapiFatalAbort(napi_env env, napi_callback_info info)
   {
         napi_fatal_error("NativeModule::TriggerNapiFatalAbort", NAPI_AUTO_LENGTH,
                          "Critical resource error! Triggering intentional Abort.",
                          NAPI_AUTO_LENGTH);
       return {};
   }
   ```

   说明3：NAPI调用失败后，框架主动终止进程。

**问题结论与总结**

NAPI接口调用失败时，框架会主动调用abort终止进程。

**修复建议**

检查NAPI接口调用参数，确保参数合法有效。

### 案例八：字符串转化异常

**问题现象**

应用崩溃退出。

**问题分析**

1. 查看LastFatalMessage信息，分析调用栈特征。可以看到是由于std::stoi转换失败才触发了异常。

   证据1：

   ```screen
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c010000e4d2 from:58578:20020225
   LastFatalMessage:terminating due to uncaught exception of type std::out_of_range: stoi: out of range
   ```
2. 分析调用栈特征。可注意到触发了stoi异常。

   证据2：

   ```screen
   Fault thread info:
   Tid:57660, Name:ppcrashanalysis
   #00 pc 00000000001c1300 /system/lib/ld-musl-aarch64.so.1(raise+216)(70dc02a619c18db57e03f7ccbad15eb1)
   #01 pc 000000000016b204 /system/lib/ld-musl-aarch64.so.1(abort+24)(70dc02a619c18db57e03f7ccbad15eb1)
   #02 pc 00000000000b088c /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #03 pc 0000000000098cfc /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #04 pc 00000000000af9f8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #05 pc 00000000000b2aa8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #06 pc 00000000000b2a24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #07 pc 00000000000d2e60 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #08 pc 00000000000cfa24 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(std::__n1::stoi(std::__n1::basic_string<char, std::__n1::char_traits<char>, std::__n1::allocator<char>> const&, unsigned long*, int)+236)(d2aeda5d2b106eca7953ec5f8909f164a1df0abb)
   #09 pc 000000000001c974 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerStrCastNumAbort(napi_env__*, napi_callback_info__*)+68)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a)
   ```

   说明2：stoi转换失败后，主动调用abort()函数终止进程。
3. 参考[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)使用llvm-addr2line工具定位行号。

   溯源#09 pc 000000000001c974 /data/storage/el1/bundle/libs/arm64/libentry.so(TriggerStrCastNumAbort(napi\_env\_\_\*, napi\_callback\_info\_\_\*)+68)(6f0c5bd0722b8e63a18fcd4150b89c84a85c927a) 崩溃行号。

   证据3：

   ```screen
   napi_value TriggerStrCastNumAbort(napi_env env, napi_callback_info info)
   {
       std::string numStr = "99999999999999999999999";
       int parsedValue = std::stoi(numStr);
       return {};
   }
   ```

   说明3：std::stoi()在转换失败时会抛出异常，异常未捕获导致主动调用abort()函数进程崩溃。

**问题结论与总结**

字符串转换时，数据太大，std::stoi转换失败时抛出异常，异常未捕获导致进程终止。

**修复建议**

使用异常安全的字符串转换方法，或在转换前进行参数校验。

## 常见易错代码预防建议

### 资源类API接口，需要成对使用，避免造成资源泄漏

资源分配失败，会导致应用闪退等未定义行为。

### 在主动调用abort前，先写入fatal信息

应用提前写入abort信息后，可以在崩溃文件中直接展示出来，可参考[hilog.fatal()](../harmonyos-references/js-apis-hilog.md#hilogfatal)和[OH\_LOG\_FATAL()](../harmonyos-references/capi-log-h.md#oh_log_fatal)使用指导。
