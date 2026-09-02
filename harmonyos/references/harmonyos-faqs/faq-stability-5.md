---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-5
title: 应用使用时卡死无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用使用时卡死无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:fb39f87568ceb075b552a17b60715df7e6dba5e5753fc8b7b15e16669827c2f9
---

## 问题现象

应用在使用过程中卡死无响应，随后出现闪退。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。

## 问题定位

### 场景一

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。

   观察栈顶可知应用进程发起了IPC通信，但对端进程长时间未返回结果，导致卡死。

   IPC栈帧下面的业务栈帧#07-#015，getPhotoList -> OpenFileByDatashare -> OpenFile，可知应用应该在读取媒体库中的photo资源。

   ```txt
   Tid:11654, Name:com.hx.example
   #00 pc 00000000001735b8 /system/lib/ld-musl-aarch64.so.1(ioctl+176)(e9ff207f4340aee156e36fdd8af0ab22)
   #01 pc 0000000000007600 /system/lib64/chipset-pub-sdk/libipc_common.z.so(OHOS::BinderConnector::WriteBinder(unsigned long, void*)+108)(bfa15156db8c2784e1ff199feedbdf3a)
   #02 pc 000000000005e730 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::TransactWithDriver(bool)+300)(380625b0d78357ec29232610b4b8bdcd)
   #03 pc 000000000005d39c /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::WaitForCompletion(OHOS::MessageParcel*, int*)+100)(380625b0d78357ec29232610b4b8bdcd)
   #04 pc 000000000005cb24 /system/lib64/platformsdk/libipc_core.z.so(OHOS::BinderInvoker::SendRequest(int, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+652)(380625b0d78357ec29232610b4b8bdcd)
   #05 pc 000000000003aee4 /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::SendRequestInner(bool, unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+148)(380625b0d78357ec29232610b4b8bdcd)
   #06 pc 000000000003b38c /system/lib64/platformsdk/libipc_core.z.so(OHOS::IPCObjectProxy::SendRequest(unsigned int, OHOS::MessageParcel&, OHOS::MessageParcel&, OHOS::MessageOption&)+472)(380625b0d78357ec29232610b4b8bdcd)
   #07 pc 0000000000041f7c /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::DataShareProxy::OpenFile(OHOS::Uri const&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+432)(ccc37cd431d6ae939fd621132f6ece39)
   #08 pc 00000000000217e4 /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::ExtSpecialController::OpenFile(OHOS::Uri const&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+160)(ccc37cd431d6ae939fd621132f6ece39)
   #09 pc 000000000003a654 /system/lib64/platformsdk/libdatashare_consumer.z.so(OHOS::DataShare::DataShareHelperImpl::OpenFile(OHOS::Uri&, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&)+80)(ccc37cd431d6ae939fd621132f6ece39)
   #10 pc 00000000000f4f3c /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::OpenFileByDatashare(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, unsigned int)+360)(09b47d0412ecc0b9dc858d032ed368d5)
   #11 pc 00000000000f43ac /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::OpenFileByUri(std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, unsigned int)+312)(09b47d0412ecc0b9dc858d032ed368d5)
   #12 pc 00000000000f3e5c /system/lib64/module/file/libfs.z.so(OHOS::FileManagement::ModuleFileIO::Open::Sync(napi_env__*, napi_callback_info__*) (.cfi)+676)(09b47d0412ecc0b9dc858d032ed368d5)
   #13 pc 000000000003df48 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+216)(73cfbb52b5b597a9083f1e565286dfef)
   #14 pc 00000000003f3b6c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #15 at getPhotoList (hsbackupmodule|hsbackupmodule|1.0.0|src/main/ets/localDataManager/MediaFilesHelper.ts:89:1)
   ```
3. 找到对端进程，搜索关键字BinderCatcher，从BinderCatcher中查看与当前故障进程通信的进程信息。

   观察到应用进程11654在和12198进程的12321线程通信。

   ```txt
   BinderCatcher --

   	11654:11654 to 12198:12321 code 2 wait:0.906698281 s frz_state:3, debug:11654:11654 to 12198:12321
   ```
4. 找到对端进程堆栈，搜索关键字PeerBinder Stacktrace，排查对端进程的执行情况。

   对端进程pid:12198为媒体库数据管理进程，根据应用业务堆栈可知应用在同步读取媒体库资源，对端堆栈分析出是在正常执行相关逻辑，得出原因为此业务场景耗时较长，应用选择的同步方式造成主线程阻塞。

   ```txt
   PeerBinder Stacktrace --

   PeerBinder catcher stacktrace for pid : 12198
   Process name:com.ohos.medialibrary.medialibrarydata
   Tid:12198, Name:edialibrarydata
   // ...
   Tid:12321, Name:OS_IPC_1_12321
   #00 pc 000000000019d314 /system/lib/ld-musl-aarch64.so.1
   #01 pc 00000000001a1174 /system/lib/ld-musl-aarch64.so.1
   #02 pc 0000000000111898 /system/lib64/platformsdk/libimage_native.z.so
   #03 pc 0000000000111544 /system/lib64/platformsdk/libimage_native.z.so
   #04 pc 00000000000dbb9c /system/lib64/platformsdk/libimage_native.z.so
   #05 pc 00000000009330d4 /data/storage/el1/bundle/libs/arm64/libmedialibrary_data_extension.z.so
   // ...
   #23 pc 00000000000573ec /system/lib64/platformsdk/libipc_core.z.so
   #24 pc 00000000001bade8 /system/lib/ld-musl-aarch64.so.1
   #25 pc 00000000000a305c /system/lib/ld-musl-aarch64.so.1
   ```

### 场景二

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。

   观察到\_\_pthread\_cond\_timedwait主线程长时间等待互斥锁的释放。

   ```txt
   Tid:11600, Name: com.hx.example
   #00 pc 00000000001bb294 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(f63a7cd1d872195c667e79e5cf905476)
   #01 pc 00000000001bd3e8 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(f63a7cd1d872195c667e79e5cf905476)
   #02 pc 0000000000b0e5d4 /data/storage/el1/bundle/libs/arm64/libcutil.so(std::__n1::condition_variable::wait(std::__n1::unique_lock<std::__n1::mutex>&)+20)(c6a156572318e195d730824137ae3fe726196f11)
   #03 pc 0000000000fa1bd0 /data/storage/el1/bundle/libs/arm64/libcutil.so(tutil::threads::Semaphore::wait()+60)(c6a156572318e195d730824137ae3fe726196f11)
   #04 pc 0000000000c9df74 /data/storage/el1/bundle/libs/arm64/libcutil.so(tbusiness::device::DeviceRequestSyncImpl::sendPrivateSync(std::__n1::basic_string<char, std::__n1::char_traits<char>, std::__n1::allocator<char>> const&, tnet::gateway::RequestPriority, int)+560)(c6a156572318e195d730824137ae3fe726196f11)
   ```
3. 需要获取锁的so库解析代码后，排查代码上下文锁的使用情况。

### 场景三

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。

   观察到应用栈信息都卡死在应用的同一个函数中。

   ```txt
   Timestamp:2025-02-06 21:12:20:623
   Tid:29599, Name:com.hx.example
   #00 pc 00000000004e06d8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSThread::GetCurrentThreadId()+0)(034d9f294a567760a27036182ab1685c)
   #01 pc 00000000003940ac /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::CheckThread() const+140)(034d9f294a567760a27036182ab1685c)
   #02 pc 00000000005e99a0 /system/lib64/platformsdk/libark_jsruntime.so(panda::JSNApi::DisposeGlobalHandleAddr(panda::ecmascript::EcmaVM const*, unsigned long)+144)(034d9f294a567760a27036182ab1685c)
   #03 pc 0000000001f68564 /system/lib64/platformsdk/libace_compatible.z.so(void OHOS::Ace::Framework::JsiCallbackInfo::SetReturnValue<OHOS::Ace::Framework::JsiObject>(OHOS::Ace::Framework::JsiRef<OHOS::Ace::Framework::JsiObject>) const+120)(0cb3d87099daee94c9fce7a0ab8b6f3a)
   #04 pc 0000000001f9e25c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSCanvasRenderer::JsMeasureText(OHOS::Ace::Framework::JsiCallbackInfo const&)+588)(0cb3d87099daee94c9fce7a0ab8b6f3a)
   #05 pc 0000000001fb1c84 /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSRenderingContext>::InternalJSMemberFunctionCallback<OHOS::Ace::Framework::JSRenderingContext>(panda::JsiRuntimeCallInfo*)+224)(0cb3d87099daee94c9fce7a0ab8b6f3a)
   #06 pc 00000000005a9110 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+456)(034d9f294a567760a27036182ab1685c)
   #07 pc 000000000048d588 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #08 pc 000000000000be00 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8+312)
   #09 at calculateLineHeight (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:141:1)
   #10 at buildPosInfo (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:84:1)
   #11 at createAndStorePosInfo (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:69:1)
   #12 at anonymous (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:55:1)
   ```

   ```txt
   Timestamp:2025-02-06 21:12:23:575
   Tid:29599, Name:com.hx.example
   #00 pc 00000000000a3c2c /system/lib/ld-musl-aarch64.so.1(40aa37b764b946f897e55516b5d6eb9c)
   #01 pc 000000000074085c /system/lib64/platformsdk/libark_jsruntime.so(panda::os::thread::GetCurrentThreadId()+12)(034d9f294a567760a27036182ab1685c)
   #02 pc 00000000003940ac /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::CheckThread() const+140)(034d9f294a567760a27036182ab1685c)
   #03 pc 00000000005e99a0 /system/lib64/platformsdk/libark_jsruntime.so(panda::JSNApi::DisposeGlobalHandleAddr(panda::ecmascript::EcmaVM const*, unsigned long)+144)(034d9f294a567760a27036182ab1685c)
   #04 pc 0000000001f9e29c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSCanvasRenderer::JsMeasureText(OHOS::Ace::Framework::JsiCallbackInfo const&)+652)(0cb3d87099daee94c9fce7a0ab8b6f3a)
   #05 pc 0000000001fb1c84 /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSRenderingContext>::InternalJSMemberFunctionCallback<OHOS::Ace::Framework::JSRenderingContext>(panda::JsiRuntimeCallInfo*)+224)(0cb3d87099daee94c9fce7a0ab8b6f3a)
   #06 pc 00000000005a9110 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+456)(034d9f294a567760a27036182ab1685c)
   #07 pc 000000000048d588 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #08 pc 000000000000be00 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8+312)
   #09 at calculateLineHeight (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:141:1)
   #10 at buildPosInfo (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:84:1)
   #11 at createAndStorePosInfo (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:69:1)
   #12 at anonymous (app|recordstudio|1.0.0|src/main/ets/component/lyric/RecordLyricDrawManager.ts:55:1)
   ```
3. 结合代码排查函数内部逻辑是否合理。

### 场景四

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。

   观察到栈顶libhilog.so(WriteV)是打印日志操作，不是耗时业务。

   ```txt
   Tid:58538, Name:com.hx.example
   #00 pc 00000000001c9074 /system/lib/ld-musl-aarch64.so.1(writev+64)(e9ff207f4340aee156e36fdd8af0ab22)
   #01 pc 0000000000020054 /system/lib64/chipset-pub-sdk/libhilog.so(OHOS::HiviewDFX::Socket::WriteV(iovec const*, unsigned int)+44)(14405333e2409816091bcc89cce6534c)
   #02 pc 000000000001f1b0 /system/lib64/chipset-pub-sdk/libhilog.so(HilogWriteLogMessageBinary+60)(14405333e2409816091bcc89cce6534c)
   #03 pc 00000000000161a0 /system/lib64/chipset-pub-sdk/libhilog.so(HilogPrintBinary+1588)(14405333e2409816091bcc89cce6534c)
   #04 pc 000000000001583c /system/lib64/chipset-pub-sdk/libhilog.so(HiLogParamEncoded(LogType, LogLevel, unsigned int, char const*, char const*, std::__va_list, OHOS::HiviewDFX::HiLogEncode::OutBuffer&, DictFlag&)+1712)(14405333e2409816091bcc89cce6534c)
   #05 pc 0000000000016978 /system/lib64/chipset-pub-sdk/libhilog.so(HiLogPrintDictArgs(LogType, LogLevel, unsigned int, char const*, FmtId const*, char const*, std::__va_list)+440)(14405333e2409816091bcc89cce6534c)
   #06 pc 0000000000016a9c /system/lib64/chipset-pub-sdk/libhilog.so(HiLogPrintDictNew+128)(14405333e2409816091bcc89cce6534c)
   #07 pc 000000000000e4d0 /system/lib64/platformsdk/libconsole.z.so(napi_value__* OHOS::JsSysModule::Console::ConsoleLog<(OHOS::JsSysModule::LogLevel)1>(napi_env__*, napi_callback_info__*) (.cfi)+296)(c56dc4a0f51cef03c663b9e06c041e57)
   #08 pc 000000000003df48 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+216)(998b53857197a096e5ad930f65e67856)
   #09 pc 00000000003f3b6c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #10 at onCreate (entry/src/main/ets/entryability/EntryAbility.ets:13:7)
   #11 pc 00000000003a4e58 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+216)(76359649b760261c0213b7c12fecc049)
   ```
3. 查看hilog日志，搜索关键字catcher cmd: hilog -z 1000 -P ，分析业务执行情况。

   观察到应用中有大量重复打印，说明发生了死循环或重复调用。

   ```txt
   catcher cmd: hilog -z 1000 -P 
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 W A03D00/m.example.xxx/HiLog: write socket failed, 17 line(s) dropped!
   04-15 17:22:05.131 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.131 58538 58538 W A03D00/m.example.xxx/HiLog: write socket failed, 2 line(s) dropped!
   04-15 17:22:05.131 58538 58538 I A03D00/m.example.xxx/JSAPP: 阻塞
   ```

### 场景五

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到远小于检测时间，说明当前任务并未长时间阻塞主线程，需要关注待处理队列中任务的情况。

   ```txt
   mainHandler dump is:
    EventHandler dump begin curTime: 2025-11-14 09:14:49.947
    Event runner (Thread name = , Thread ID = 32144) is running
    Current Running: start at 2025-11-14 09:14:48.146, Event { send thread = 32225, send time = 2025-11-14 09:14:44.761, handle time = 2025-11-14 09:14:44.761, trigger time = 2025-11-14 09:14:48.146, task name = ArkUIAceContainerTouchEvent, caller = [task_runner_adapter_impl.cpp(PostTask:33)] }
   ```
2. 查看优先队列，搜索关键字Total event size，查看VIP、Immediate、High事件数量是否过多，这可能会让位于VIP队列中的watchdog任务未被及时调度执行，导致上报故障。观察到High队列任务数量25347，存在大量重复的任务。

   ```txt
   History event queue information:
   VIP priority event queue information:
   Total size of VIP events : 182
   Immediate priority event queue information:
   Total size of Immediate events : 0
   High priority event queue information:
   No.2 : Event { send thread = 32144, send time = 2025-11-14 09:14:44.155, handle time = 2025-11-14 09:14:44.155, task name = uv_io_cb, caller = [ohos_js_environment_impl.cpp(PostTaskToHandler:64)] }
   No.3 : Event { send thread = 32144, send time = 2025-11-14 09:14:44.155, handle time = 2025-11-14 09:14:44.155, task name = uv_io_cb, caller = [ohos_js_environment_impl.cpp(PostTaskToHandler:64)] }
   // ...
   Total size of High events : 25347
   Low priority event queue information:
   Total size of Low events : 97
   Idle priority event queue information:
   Total size of Idle events : 0
   Total event size : 25626
   ```
3. 查看堆栈日志，结合当前业务场景，分析此任务大量提交到任务队列中是否合理。

### 场景六

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。观察堆栈中的函数调用，loadDocumentNotPwd -> LoadDocument，可知当前操作应该为同步读取文档。

   ```txt
   Tid:53862, Name:com.hx.example
   #00 pc 00000000001c7dc0 /system/lib/ld-musl-aarch64.so.1(read+64)(6b9883f518515f73e093bce9a89a2548)
   #01 pc 000000000044e350 /system/lib64/platformsdk/libpdf_framework.so
   #02 pc 000000000074996c /system/lib64/platformsdk/libpdf_framework.so
   #03 pc 000000000074a860 /system/lib64/platformsdk/libpdf_framework.so
   #04 pc 0000000000748bac /system/lib64/platformsdk/libpdf_framework.so
   #05 pc 0000000000745d94 /system/lib64/platformsdk/libpdf_framework.so
   #06 pc 00000000007433fc /system/lib64/platformsdk/libpdf_framework.so
   #07 pc 0000000000741de0 /system/lib64/platformsdk/libpdf_framework.so
   #08 pc 000000000036da48 /system/lib64/platformsdk/libpdf_framework.so(CPDSDK_Document::Open(wchar_t const*, char const*, int)+304)
   #09 pc 00000000000444e4 /system/lib64/module/hms/officeservice/libpdfservice.z.so(PDFService::PDFDocument::LoadDocument(napi_env__*, napi_callback_info__*)+944)(6f17ff216baab47be0abbaf974f042c1)
   #10 pc 000000000003ec44 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+212)(edf034e044dbf26f955142c343577527)
   #11 pc 0000000000405b2c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #12 at loadDocumentNotPwd (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/biz/pdf/PdfDocumentBiz.ts:23:1)
   #13 at importPdfNotPwd (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/biz/pdf/PdfBiz.ts:24:1)
   #14 at anonymous (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/biz/pdf/PdfUtil.ts:12:1)
   #15 pc 00000000003a53c8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::InterpreterAssembly::Execute(panda::ecmascript::EcmaRuntimeCallInfo*)+216)(cdaf9033a0501974cfa94b73b57aabb3)
   #16 pc 00000000002711bc /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::builtins::BuiltinsPromise::PromiseConstructor(panda::ecmascript::EcmaRuntimeCallInfo*)+316)(cdaf9033a0501974cfa94b73b57aabb3)
   #17 pc 0000000000406cb8 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallNewAndDispatchNative+136)
   #18 at importPdf (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/biz/pdf/PdfUtil.ts:7:1)
   #19 at importPdfBySelectPdf (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/viewmodel/NoteListVM.ts:230:1)
   #20 at anonymous (@jnotes/main|@jnotes/main|1.0.0|src/main/ets/dialog/ImportPdfDialog.ts:431:1)
   ```
3. 使用[HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)工具抓取该过程的Trace信息，观察该操作的执行耗时。

   当前任务运行时间Duration已达到7s，长时间占用主线程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/6j0tXs_XQGuWAKWQbIGr5w/zh-cn_image_0000002658555527.png "点击放大")

### 场景七

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到大于检测时间，说明当前任务执行超时。
2. 查看堆栈日志，排查耗时原因，搜索关键字Tid:应用pid, Name:应用包名，分析当前任务的执行情况。观察堆栈中的函数调用，writeToPersistentStorage -> JSPersistent::Set -> JsonStringifier::SerializeJSONProperty，可知当前栈顶操作是在执行JSON序列化，不是耗时操作或等锁情况。

   ```txt
   Tid:50688, Name:com.hx.example
   #00 pc 00000000003456d0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeKeys(panda::ecmascript::JSHandle<panda::ecmascript::JSObject> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, bool)+16676)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #01 pc 000000000034726c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+4976)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #02 pc 00000000003489c8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+10956)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #03 pc 0000000000347af0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+7156)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #04 pc 000000000034654c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+1616)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #05 pc 0000000000347af0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+7156)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #06 pc 0000000000429238 /system/lib64/platformsdk/libark_jsruntime.so(d44b73a6fb001d62b07fc7332e9c9cf7)
   #07 pc 0000000000631388 /system/lib64/platformsdk/libark_jsruntime.so(panda::JSON::Stringify(panda::ecmascript::EcmaVM const*, panda::Local<panda::JSValueRef>)+252)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #08 pc 0000000000f1e0fc /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JSPersistent::Set(OHOS::Ace::Framework::JsiCallbackInfo const&)+412)(2af4b0541833e1477286969581dd9596)
   #09 pc 000000000151d968 /system/lib64/platformsdk/libace_compatible.z.so(panda::Local<panda::JSValueRef> OHOS::Ace::Framework::JsiClass<OHOS::Ace::Framework::JSPersistent>::InternalJSMemberFunctionCallback<OHOS::Ace::Framework::JSPersistent>(panda::JsiRuntimeCallInfo*)+300)(2af4b0541833e1477286969581dd9596)
   #10 pc 0000000000631d84 /system/lib64/platformsdk/libark_jsruntime.so(panda::Callback::RegisterCallback(panda::ecmascript::EcmaRuntimeCallInfo*)+1952)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #11 pc 0000000000e12868 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #12 pc 0000000000458510 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis2Imm8V8V8V8StwCopy+392)
   #13 at writeToPersistentStorage (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:1951:1)
   #14 at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:1936:1)
   ```
3. 观察整个堆栈，发现应用在大量更新视图数据，导致耗时过长。

   可以看到GestureRecognizer识别到手势事件后，应用开始更新StockGroups，与视图BottomToolBarView有关，在#40栈帧有viewPropertyHasChanged视图属性变化的处理函数，并且整个GroupList数据都在更新，当需要更新的数据越多，主线程耗时就越长，最终可能发生卡死。

   ```txt
   Tid:50688, Name:com.hx.example
   #00 pc 00000000003456d0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeKeys(panda::ecmascript::JSHandle<panda::ecmascript::JSObject> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, bool)+16676)(d44b73a6fb001d62b07fc7332e9c9cf7)
   #01 pc 000000000034726c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::base::JsonStringifier::SerializeJSONProperty(panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&, panda::ecmascript::JSHandle<panda::ecmascript::JSTaggedValue> const&)+4976)(d44b73a6fb001d62b07fc7332e9c9cf7)
   // ...
   #13 at writeToPersistentStorage (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:1951:1)
   // ...
   #17 at write (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:1934:1)
   #18 at syncPeerHasChanged (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:1981:1)
   // ...
   #36 at setCurrentGroupList (entry|entry|8.21.2266|src/main/ets/models/UserStockManager.ts:0:1)
   #37 at setStockGroups (entry|entry|8.21.2266|src/main/ets/pages/hq/view/ztBottomToolBarView.ts:0:1)
   // ...
   #40 at viewPropertyHasChanged (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8302:1)
   #41 at notifyPropertyHasChangedPU (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6303:1)
   #42 at onTrackedObjectPropertyCompatModeHasChangedPU (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6549:1)
   // ...
   #62 at addStock (entry|entry|8.21.2266|src/main/ets/models/UserStockManager.ts:0:1)
   #63 at updateGroup (entry|entry|8.21.2266|src/main/ets/models/UserStockManager.ts:0:1)
   #64 at processStock (entry|entry|8.21.2266|src/main/ets/pages/hq/view/ztBottomToolBarView.ts:0:1)
   #65 at itemClickEvent (entry|entry|8.21.2266|src/main/ets/pages/hq/view/ztBottomToolBarView.ts:0:1)
   #66 at onBottomClick (entry|entry|8.21.2266|src/main/ets/pages/hq/view/tztZFSelectBottomList.ts:0:1)
   #67 at anonymous (entry|entry|8.21.2266|src/main/ets/pages/hq/view/tztZFSelectBottomList.ts:0:1)
   #68 pc 00000000001e45f8 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::JSFunction::Call(panda::ecmascript::EcmaRuntimeCallInfo*)+764)(d44b73a6fb001d62b07fc7332e9c9cf7)
   // ...
   #75 pc 0000000002b6cbb8 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::TextPattern::ActTextOnClick(OHOS::Ace::GestureEvent&)+196)(2af4b0541833e1477286969581dd9596)
   // ...
   #90 pc 0000000000ae6ab4 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::NGGestureRecognizer::HandleEvent(OHOS::Ace::TouchEvent const&)+1844)(2af4b0541833e1477286969581dd9596)
   #91 pc 0000000000bd5438 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::ExclusiveRecognizer::DispatchEventToAllRecognizers(OHOS::Ace::TouchEvent const&)+772)(2af4b0541833e1477286969581dd9596)
   #92 pc 0000000000a6c7bc /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::EventManager::DispatchTouchEventToTouchTestResult(OHOS::Ace::TouchEvent const&, std::__h::list<OHOS::Ace::RefPtr<OHOS::Ace::TouchEventTarget>, std::__h::allocator<OHOS::Ace::RefPtr<OHOS::Ace::TouchEventTarget>>>, bool)+2296)(2af4b0541833e1477286969581dd9596)
   #93 pc 0000000000a6923c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::EventManager::DispatchTouchEvent(OHOS::Ace::TouchEvent const&, bool)+1212)(2af4b0541833e1477286969581dd9596)
   #94 pc 0000000000e3898c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::NG::PipelineContext::OnTouchEvent(OHOS::Ace::TouchEvent const&, OHOS::Ace::RefPtr<OHOS::Ace::NG::FrameNode> const&, bool)+3672)(2af4b0541833e1477286969581dd9596)
   // ...
   ```

### 场景八

1. 从faultlogger目录下获取到应用的AppFreeze，首先查看主线程任务队列的当前任务，搜索关键字mainHandler dump，观察到远小于检测时间，说明当前任务并未长时间阻塞主线程，需要关注待处理队列中任务的情况。

   ```txt
   mainHandler dump is:
    EventHandler dump begin curTime: 2026-01-07 15:38:35.435
    Event runner (Thread name = , Thread ID = 15805) is running
    Current Running: start at 2026-01-07 15:38:35.361, Event { send thread = 15805, send time = 2026-01-07 15:38:28.059, handle time = 2026-01-07 15:38:28.059, trigger time = 2026-01-07 15:38:35.362, task name = 26025, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_26025)] }
   ```
2. 查看历史任务队列，搜索关键字History event queue information，观察到存在多个短耗时任务，一直占用主线程，导致位于高优先队列的watchdog任务未被及时调度执行，上报AppFreeze。

   ```txt
   History event queue information:
   No. 0 : Event { send thread = 16272, send time = 2026-01-07 15:38:25.936, handle time = 2026-01-07 15:38:25.936, trigger time = 2026-01-07 15:38:26.370, completeTime time = 2026-01-07 15:38:26.790, priority = Low, task name = 25779, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25779)] }
   No. 2 : Event { send thread = 16272, send time = 2026-01-07 15:38:25.936, handle time = 2026-01-07 15:38:25.936, trigger time = 2026-01-07 15:38:26.791, completeTime time = 2026-01-07 15:38:27.450, priority = Low, task name = 25780, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25780)] }
   No. 15 : Event { send thread = 16272, send time = 2026-01-07 15:38:25.938, handle time = 2026-01-07 15:38:25.938, trigger time = 2026-01-07 15:38:27.457, completeTime time = 2026-01-07 15:38:28.473, priority = Low, task name = 25781, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25781)] }
   No. 16 : Event { send thread = 16059, send time = 2026-01-07 15:38:27.026, handle time = 2026-01-07 15:38:27.026, trigger time = 2026-01-07 15:38:28.473, completeTime time = 2026-01-07 15:38:28.475, priority = VIP, task name = MMI::OnPointerEvent, caller = [input_manager_impl.cpp(OnPointerEvent:655)] }
   No. 17 : Event { send thread = 15805, send time = 2026-01-07 15:38:27.457, handle time = 2026-01-07 15:38:27.505, trigger time = 2026-01-07 15:38:28.475, completeTime time = 2026-01-07 15:38:28.475, priority = VIP, task name = BarrierEvent, caller = [event_queue.cpp(PostTaskForVsync:210)] }
   No. 18 : Event { send thread = 15805, send time = 2026-01-07 15:38:26.370, handle time = 2026-01-07 15:38:26.370, trigger time = 2026-01-07 15:38:28.475, completeTime time = 2026-01-07 15:38:29.735, priority = Low, task name = 25836, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25836)] }
   No. 19 : Event { send thread = 15805, send time = 2026-01-07 15:38:26.370, handle time = 2026-01-07 15:38:26.370, trigger time = 2026-01-07 15:38:29.735, completeTime time = 2026-01-07 15:38:30.812, priority = Low, task name = 25837, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25837)] }
   No. 20 : Event { send thread = 15805, send time = 2026-01-07 15:38:26.371, handle time = 2026-01-07 15:38:26.371, trigger time = 2026-01-07 15:38:30.812, completeTime time = 2026-01-07 15:38:31.614, priority = Low, task name = 25838, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25838)] }
   No. 21 : Event { send thread = 15805, send time = 2026-01-07 15:38:26.389, handle time = 2026-01-07 15:38:26.389, trigger time = 2026-01-07 15:38:31.614, completeTime time = 2026-01-07 15:38:32.501, priority = Low, task name = 25839, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25839)] }
   No. 22 : Event { send thread = 15805, send time = 2026-01-07 15:38:26.841, handle time = 2026-01-07 15:38:26.841, trigger time = 2026-01-07 15:38:32.501, completeTime time = 2026-01-07 15:38:33.786, priority = Low, task name = 25880, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25880)] }
   No. 23 : Event { send thread = 15805, send time = 2026-01-07 15:38:27.457, handle time = 2026-01-07 15:38:27.457, trigger time = 2026-01-07 15:38:33.786, completeTime time = 2026-01-07 15:38:34.651, priority = Low, task name = 25975, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25975)] }
   No. 24 : Event { send thread = 15805, send time = 2026-01-07 15:38:28.058, handle time = 2026-01-07 15:38:28.058, trigger time = 2026-01-07 15:38:34.651, completeTime time = 2026-01-07 15:38:35.071, priority = Low, task name = 26023, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_26023)] }
   No. 25 : Event { send thread = 15805, send time = 2026-01-07 15:38:28.058, handle time = 2026-01-07 15:38:28.058, trigger time = 2026-01-07 15:38:35.071, completeTime time = 2026-01-07 15:38:35.361, priority = Low, task name = 26024, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_26024)] }
   No. 26 : Event { send thread = 15805, send time = 2026-01-07 15:38:28.060, handle time = 2026-01-07 15:38:28.060, trigger time = 2026-01-07 15:38:35.362, completeTime time = , priority = Low, task name = 26025, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_26025)] }
   No. 27 : Event { send thread = 16272, send time = 2026-01-07 15:38:25.936, handle time = 2026-01-07 15:38:25.936, trigger time = 2026-01-07 15:38:26.146, completeTime time = 2026-01-07 15:38:26.369, priority = Low, task name = 25778, caller = [event_handler.cpp(PostTaskByFFRT:682sq_main_queue_8_25778)] }
   No. 28 : Event { send thread = 16015, send time = 2026-01-07 15:38:26.210, handle time = 2026-01-07 15:38:26.210, trigger time = 2026-01-07 15:38:26.369, completeTime time = 2026-01-07 15:38:26.369, priority = VIP, task name = 25769, caller = [watchdog.cpp(Timer:249)] }
   // 高优先队列
   No. 12 : Event { send thread = 16015, send time = 2026-01-07 15:38:29.209, handle time = 2026-01-07 15:38:29.209, id = 1, caller = [watchdog.cpp(Timer:249)] }
   No. 23 : Event { send thread = 16015, send time = 2026-01-07 15:38:32.209, handle time = 2026-01-07 15:38:32.210, id = 1, caller = [watchdog.cpp(Timer:249)] }
   ```
3. 查看堆栈日志，搜索关键字Tid:应用pid, Name:应用包名，使用[堆栈解析工具（hstack）](../harmonyos-guides/ide-command-line-hstack.md)解析到对应代码，排查此业务频繁执行是否合理，并分析当前任务短耗时情况是否正常。

   ```txt
   Tid:15805, Name:com.hx.example
   #00 pc 000000000014dcc0 /system/lib/ld-musl-aarch64.so.1(memcpy+0)(aa868b6787bcddfd90eb4e8cb2aaea84)
   #01 pc 0000000000023044 /data/storage/el1/bundle/libs/arm64/libcrash_reporter.so(0621db87af80730734b6140844c7443776429244)
   #02 pc 0000000002d4cef8 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.WingsFramework.so(WEQueryFeedback::GetCellValue(int, std::__n1::basic_string<char, std::__n1::char_traits<char>, std::__n1::allocator<char>> const&, WEDataValue&)+288)(44dfbfdfc434361fa7a5538c607cc83fb513a236)
   #03 pc 0000000002ce6708 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.WingsFramework.so(WEDataSource::UpdateAllData(WEQueryFeedback&)+508)(44dfbfdfc434361fa7a5538c607cc83fb513a236)
   #04 pc 0000000002ce2608 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.WingsFramework.so(WEDataSource::SynchronizeData(WEQueryFeedback&)+1112)(44dfbfdfc434361fa7a5538c607cc83fb513a236)
   #05 pc 0000000002cc4968 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.WingsFramework.so(WEDataProvider::SychronizeData(wedb::IQueryEngine*)+356)(44dfbfdfc434361fa7a5538c607cc83fb513a236)
   #06 pc 0000000002cc46e8 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.WingsFramework.so(WEDataProvider::onDataChanged(wedb::IQueryEngine*)+428)(44dfbfdfc434361fa7a5538c607cc83fb513a236)
   #07 pc 0000000000056174 /data/storage/el1/bundle/libs/arm64/libWind.Cosmos.DataClient.so(wedb::CQueryEngine::OnDataChanged()+1392)(539aa42b7bbd13db543337890cdd7151424e516f)
   ```

## 分析结论

### 场景一

应用进程IPC通信超时，对端进程业务所需耗时过长，但应用使用同步方式导致主线程阻塞。

### 场景二

锁使用异常导致应用进程等锁卡死。

### 场景三

函数执行时间过长，导致主线程阻塞。

### 场景四

应用业务死循环或重复调用，导致耗时过长阻塞主线程。

### 场景五

高优先级任务过多导致应用卡死。

### 场景六

大文件导入业务执行时间过长，主线程阻塞导致卡死闪退。

### 场景七

应用视图数据更新过多，状态变量的更新会导致视图的重新渲染，如果更新的内容越多，遍历和渲染的时间会相应增加，导致主线程耗时过长。

### 场景八

多个短耗时任务一直占用主线程，导致卡死无响应。

## 修改建议

### 场景一

参考文档[主线程耗时操作优化](../best-practices/bpta-time-optimization-of-the-main-thread.md)，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。

### 场景二

lock()和unlock()需要成对使用，以确保锁得到正确的管理，在异常分支提前返回时释放互斥锁，修复方式可参考案例[ThreadBlock类问题案例-未正确使用锁](../best-practices/bpta-scenario-stability-app-freeze.md#section7412134135816)。

### 场景三

参考文档[主线程耗时操作优化](../best-practices/bpta-time-optimization-of-the-main-thread.md)，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。

### 场景四

确保循环条件正常，避免死循环。

降低业务执行频次，或将其放到子线程执行，参考文档[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)。

### 场景五

调整代码逻辑，减少高优先级任务数量，或分散任务，避免在一段时间内集中执行。

### 场景六

参考文档[主线程耗时操作优化](../best-practices/bpta-time-optimization-of-the-main-thread.md)，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。

### 场景七

控制页面渲染的逻辑，考虑大量组件、频繁刷新等场景，简化布局、异步处理、批量更新，避免组件渲染时间过长，详情参考[性能优化](../best-practices/bpta-performance-optimization.md)。

### 场景八

优化耗时，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。

控制执行次数，当遇到用户高频事件输入时，根据业务场景，可以选择节流、防抖或限制次数的方式进行优化：

* 限制执行次数，通过计数变量限制业务执行次数。
* 节流，固定时间间隔内只允许触发一次操作，忽略中间频繁触发。
* 防抖，事件停止触发后延迟一段时间再执行操作，仅响应最后一次触发。

## 常见FAQ

Q：THREAD\_BLOCK\_6S是检测的是否只有主线程？还是任意一个线程阻塞都会导致THREAD\_BLOCK\_6S问题并闪退？

A：只检测主线程，原理可以参考下[THREAD\_BLOCK\_6S 应用主线程卡死超时](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)。

Q：使用async函数处理页面按键响应，是否是新启动的线程，是否纳入了THREAD\_BLOCK\_6S检测？

A：async不会启动新的线程，所以耗时很长时，可能会导致THREAD\_BLOCK\_6S。

Q：后台的耗时处理应该使用什么方案才能避免THREAD\_BLOCK\_6S闪退？

A：可以根据场景参考下：1.[使用多线程能力](../best-practices/bpta-concurrency-capability.md#section1912142113263)。2.[长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)。
