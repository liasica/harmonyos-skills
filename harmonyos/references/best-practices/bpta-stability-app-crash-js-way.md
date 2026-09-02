---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-crash-js-way
title: JS Crash类问题分析方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 应用崩溃类问题分析 > JS Crash类问题分析方法
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:f0c5c216ba81df30c595fe44f1e372a7090521f67a624bd035e26dd30c42ab23
---

当未处理的JS异常导致应用意外退出时，应用会在抛出未处理的异常时崩溃并且会生成对应的JS Crash崩溃日志文件。开发者可通过错误日志查看引起崩溃的代码位置及分析应用崩溃的原因，可参看[JS Crash日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。

## 问题定位思路

### 获取日志

进程崩溃日志是一种故障日志，具体可参考[日志获取](../harmonyos-guides/jscrash-guidelines.md#日志获取)。

### 根因分析

分析JS Crash问题通过异常场景，结合错误信息和调用栈定位源码，从而得出基本的分析结论。调用栈的分析有以下几种情况：

**StackTrace 场景分类**

JS Crash故障日志中的StackTrace字段存放了JS Crash异常的调用栈信息，StackTrace的显示分为以下几种场景。

1. JS调用栈可直接通过超链接跳转到对应错误代码行，栈顶即为问题第一现场，如下样例所示。

   ```screen
   Device info:xxx
   Build info:xxx-xxx x.x.x.xxx(xxxx)
   Fingerprint:d1ad53b47ce339f2e21aec4b8ac5e8bda70dcb241bc684448ddf7eab7ff19860
   Timestamp:xxxx-xx-xx xx:xx:xx.xxx
   Module name:com.xxx.xxx
   Version:1.0.0
   VersionCode:1000000
   PreInstalled:No
   Foreground:Yes
   Pid:52148
   Uid:20020199
   Process Memory(kB): 147873(Rss)
   Device Memory(kB): Total 11679208, Free 577272, Available 5079040
   Page switch history:
     xx:xx:xx.xxx :enters foreground
   Reason:Error
   Error name:Error
   Error message:JSERROR
   Stacktrace:
       at anonymous entry (entry/src/main/ets/pages/Index.ets:18:11) //在DevEco Studio可直接点跳转到对应源码
   ```
2. 异常代码调用栈包含Cannot get SourceMap info, dump raw stack，表示SourceMap转换失败，仅展示ets栈对应编译产物的代码行号，需要通过SourceMap还原对应错误代码行。如下样例所示。

   ```screen
   Device info:xxx
   Build info:xxx-xxx x.x.x.xxx(xxxx)
   Fingerprint:a370fceb59011d96e41e97bda139b1851c911012ab8c386d1a2d63986d6d226d
   Module name:com.xxx.xxx
   Version:1.0.0
   VersionCode:1000000
   PreInstalled:No
   Foreground:Yes
   Pid:39185
   Uid:20020145
   Reason:Error
   Error name:Error
   Error message:JSERROR
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at anonymous (entry/src/main/ets/pages/Index.ts:49:49)
   ```
3. 异常代码调用栈包含SourceMap is not initialized yet，表示SourceMap没初始化完成就有异常产生的情况，一般是由于在系统侧进行SourceMap初始化和转换非常耗时导致的。ets栈对应编译产物的代码行号，需要通过SourceMap还原对应错误代码行。如下样例所示。

   ```screen
   Device info:xxx
   Build info:xxx-xxx x.x.x.xxx(xxxx)
   Fingerprint:377ef8529301363f373ce837d0bf83aacfc46112502143237e2f4026e86a0510
   Module name:com.xxx.xxx
   Version:1.0.0
   VersionCode:1000000
   PreInstalled:No
   Foreground:Yes
   Pid:6042
   Uid:20020145
   Reason:Error
   Error name:Error
   Error message:JSERROR
   Stacktrace:
   SourceMap is not initialized yet
   at anonymous (entry/src/main/ets/pages/Index.ts:49:49)
   ```
4. 异常代码调用栈栈顶libark\_jsruntime.so动态库的场景一般是业务调用NAPI函数后出现了异常。因为JS异常都是由虚拟机抛出，因此基于调用栈从上往下找，libace\_napi.z.so的下一帧一般是抛出异常的现场。在ARM64架构下，如果debug版本应用开启异步线程栈跟踪维测，当异步线程发生崩溃，故障日志不仅会包含当前调用栈，还会附带异步线程调用栈。这两个调用栈通过SubmitterStacktrace字符串分隔，SubmitterStacktrace下方即为异步线程调用栈。以下是一份具体的崩溃日志示例。

   ```screen
   Device info:xxx
   Build info:xxx-xxx x.x.x.xxx(xxxx)
   Fingerprint:89f2b64b24d642b0fc64e3a7cf68ca39fecaa580ff5736bb9d6706ea4cdf2c93
   Module name:com.xxx.xxx
   Version:1.0.0
   VersionCode:1000000
   PreInstalled:No
   Foreground:No
   Pid:14325
   Uid:20020145
   Reason:ReferenceError
   Error name:ReferenceError
   Reason:Error
   Error name:Error
   Error message:test error
   Error code:10
   Stacktrace:
   #00 pc 00000000004d9d4c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Backtrace(std::__h::basic_ostringstream<char, std::__h::char_traits<char>, std::__h::allocator<char>>&, bool)+92)(723d1618fe2567539bed3038ccfe92d8)
   #01 pc 000000000038ddcc /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JsStackInfo::BuildJsStackTrace(panda::ecmascript::JSThread*, bool, panda::ecmascript::JSHandle<panda::ecmascript::JSObject> const&, bool, unsigned int)+2952)(723d1618fe2567539bed3038ccfe92d8)
   #02 pc 000000000038c70c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::ErrorHelper::ErrorCommonConstructor(panda::ecmascript::EcmaRuntimeCallInfo*, panda::ecmascript::base::ErrorType const&)+1704)(723d1618fe2567539bed3038ccfe92d8)
   #03 pc 000000000038c03c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::builtins::BuiltinsError::ErrorConstructor(panda::ecmascript::EcmaRuntimeCallInfo*)+40)(723d1618fe2567539bed3038ccfe92d8)
   #04 pc 00000000001b5d90 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewJSError(panda::ecmascript::JSHandle<panda::ecmascript::GlobalEnv> const&, panda::ecmascript::base::ErrorType const&, panda::ecmascript::JSHandle<panda::ecmascript::EcmaString> const&, panda::ecmascript::StackCheck)+984)(723d1618fe2567539bed3038ccfe92d8)
   #05 pc 000000000093274c /system/lib64/platformsdk/libark_jsruntime.so(panda::Exception::Error(panda::ecmascript::EcmaVM const*, panda::Local<panda::StringRef>)+244)(723d1618fe2567539bed3038ccfe92d8)
   #06 pc 0000000000066398 /system/lib64/platformsdk/libace_napi.z.so(napi_throw_error+152)(c91850afe3629242ed12712b76be08f1)
   #07 pc 00000000000020fc /data/storage/el1/bundle/libs/arm64/libentry.so(02cecfd8fd280aeaa1af7b9d1227afeac0ec4356)   <- 异常抛出位置
   #08 pc 00000000000890c0 /system/lib64/platformsdk/libruntime.z.so(std::__h::__function::__func<OHOS::AbilityRuntime::OHOSJsEnvironmentImpl::PostTaskToHandler(char const*, void (*)(void*, int), void*, int, int)::$_0, std::__h::allocator<OHOS::AbilityRuntime::OHOSJsEnvironmentImpl::PostTaskToHandler(char const*, void (*)(void*, int), void*, int, int)::$_0>, void ()>::operator()() (.3ec3b6b3a88f13b2aa6c613a7afa022b)+128)(50df26f49d9c067da9cf79b804f136ec)
   ========SubmitterStacktrace========    <- 当异步线程发生崩溃后，把提交该异步任务的线程的栈也打印出来
   #00 pc 0000000000012cd0 /system/lib64/platformsdk/libuv.so(uv_queue_work+456)(e077582fac1bf7463ca5539c0a2b678a)
   #01 pc 0000000000001fd0 /data/storage/el1/bundle/libs/arm64/libentry.so(02cecfd8fd280aeaa1af7b9d1227afeac0ec4356)
   #02 pc 000000000004d69c /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+220)(c91850afe3629242ed12712b76be08f1)
   #03 pc 0000000000d08e90 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
   #04 pc 000000000036ae70 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+436)
   #05 at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:57:79)
   #06 pc 000000000029e144 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+540)(723d1618fe2567539bed3038ccfe92d8)
   #07 pc 0000000000327eac /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSFunction::Call(panda::ecmascript::EcmaRuntimeCallInfo*) (.419.extracted)+452)(723d1618fe2567539bed3038ccfe92d8)
   #08 pc 0000000000940c18 /system/lib64/platformsdk/libark_jsruntime.so(panda::FunctionRef::Call(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>, panda::Local<panda::JSValueRef> const*, int)+1988)(723d1618fe2567539bed3038ccfe92d8)
   #09 pc 00000000009ce8d8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiFunction::Call(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>, int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*, bool) const+700)(cdb4712f9d1d7fda83faae9d393a244e)
   #10 pc 0000000000972a38 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsFunction::ExecuteJS(int, OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiValue>*, bool)+384)(cdb4712f9d1d7fda83faae9d393a244e)
   #11 pc 0000000000e1f590 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsClickFunction::Execute(OHOS::Ace::GestureEvent&)+3396)(cdb4712f9d1d7fda83faae9d393a244e)
   #12 pc 0000000001079384 /system/lib64/platformsdk/libace_compatible.z.so(cdb4712f9d1d7fda83faae9d393a244e)
   #13 pc 00000000026e1b28 /system/lib64/platformsdk/libace_compatible.z.so(cdb4712f9d1d7fda83faae9d393a244e)
   #14 pc 0000000000f435a8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::ActTextOnClick(OHOS::Ace::GestureEvent&)+164)(cdb4712f9d1d7fda83faae9d393a244e)
   #15 pc 0000000002751134 /system/lib64/platformsdk/libace_compatible.z.so(cdb4712f9d1d7fda83faae9d393a244e)
   ```

**调用栈分析**

调用栈分析会有如下两种情况：

* 情况一：可跳转至引起错误的代码行

  如果FaultLog的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将被转换为超链接形式，在DevEco Studio中点击后跳转至对应代码行。
* 情况二：不可跳转至引起错误的代码行或者跳转代码位置不存在

  如出现Cannot get Source Map info, dump raw stack信息代表js栈转换ets行列号失败，在DevEco Studio中点击链接会跳转到不正确的代码位置或不存在的代码行位置。可参考：[堆栈轨迹分析](../harmonyos-guides/ide-release-app-stack-analysis.md)。
