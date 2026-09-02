---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-10
title: CppCrash问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > CppCrash问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a7f81b7c49555c258e78b394ba2986bb43d8b2dd9f8d8e26a3242938868427fc
---

## 问题现象

应用在使用过程中或者在执行稳定性测试时，应用出现闪退或上报CppCrash异常。

## 背景知识

* CppCrash进程崩溃检测基于操作系统信号机制，目前支持的崩溃信号参考[Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md)。
* CppCrash日志规格可以参考[日志规格](../harmonyos-guides/cppcrash-guidelines.md#日志规格)说明。

## 问题定位

### 场景一

1. 从faultlogger目录下获取CppCrash故障日志。查看故障原因和异常信息Reason。
2. 故障信号是SIGSEGV。
   * 异常信息为空。从栈顶往下分析，跳过libace\_ndk.z.so等公共基础库，发生异常的so库解析崩溃堆栈后结合代码进行分析。

     ```screen
     Uid:20020197
     Process name:com.hx.example
     Process life time:2s
     Reason:Signal:SIGSEGV(SEGV_MAPERR)@0xffab14aa14a914c0 
     Fault thread info:
     Tid:62538, Name:com.hx.example
     #00 pc 00000000000296e4 /system/lib64/libace_ndk.z.so(ArkUI_AccessibilityProvider::SendAccessibilityAsyncEvent(ArkUI_AccessibilityEventInfo*, void (*)(int))+32)(42521ecd5a913b6984e2ff754dc45cf0)
     #01 pc 000000000020295c /data/storage/el1/bundle/libs/arm64/libflutter.so(cd0979aaa7458f05c7c4cfb0d8928c90c484e393) // 异常so库
     #02 pc 0000000000789730 /data/storage/el1/bundle/libs/arm64/libflutter.so(cd0979aaa7458f05c7c4cfb0d8928c90c484e393)
     #03 pc 0000000000221170 /data/storage/el1/bundle/libs/arm64/libflutter.so(cd0979aaa7458f05c7c4cfb0d8928c90c484e393)
     #04 pc 0000000000016db4 /system/lib64/platformsdk/libuv.so(uv__async_io+352)(25c5e130ae25e495771607adc70da044)
     #05 pc 000000000002880c /system/lib64/platformsdk/libuv.so(uv__io_poll+1012)(25c5e130ae25e495771607adc70da044)
     #06 pc 000000000001739c /system/lib64/platformsdk/libuv.so(uv_run+408)(25c5e130ae25e495771607adc70da044)
     ```
   * 异常信息是：Signal:SIGSEGV(SEGV\_MAPERR)@000000000000000000 probably caused by NULL pointer dereference。无效内存访问，需要栈顶so库解析崩溃栈后结合代码进行具体分析。

     ```screen
     Uid:20020157
     Process name:com.hx.example
     Process life time:2s
     Reason:Signal:SIGSEGV(SEGV_MAPERR)@000000000000000000  probably caused by NULL pointer dereference
     Fault thread info:
     Tid:18211, Name:1.ui
     #00 pc 0000000000000000 Not mapped
     #01 pc 0000000000429100 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
     #02 pc 000000000075b0bc /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
     #03 pc 00000000005af6e4 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
     #04 pc 0000000000568e24 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
     #05 pc 000000000056901c /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
     ```
   * 异常信息是：SIGSEGV(SEGV\_ACCERR)@0x0000000000000000 current thread stack low address = 0x0000000000000000, probably caused by stack-buffer-overflow，堆栈缓冲区溢出。堆栈中有大量重复调用，排查是否递归调用未能终止导致栈内存溢出，需要栈顶so库解析崩溃栈后结合代码进行具体分析。

     ```screen
     Uid:20020180
     Process name:com.hx.example
     Process life time:18446744073709077156s
     Reason:Signal:SIGSEGV(SEGV_ACCERR)@0x0000000000000000 current thread stack low address = 0x0000005b479ef000, probably caused by stack-buffer-overflow
     Fault thread info:
     Tid:1773, Name:Chrome_IOThread
     #00 pc 0000000003e15da8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(content::BrowserThread::CurrentlyOn(content::BrowserThread::ID)+4)(061948a4140de9d4f304c80724508f0147d74f83)
     #01 pc 0000000004e74c6c /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(ArkWeb_HttpBodyStream_::OnReadComplete(char*, int)+76)(061948a4140de9d4f304c80724508f0147d74f83)
     #02 pc 0000000002865b94 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::OnStreamReadAsync(scoped_refptr<net::WrappedIOBuffer>, scoped_refptr<CefPostDataStreamReadCallback>, int)+36)(061948a4140de9d4f304c80724508f0147d74f83)
     #03 pc 0000000002865b30 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::ReadAsync(void*, int, scoped_refptr<CefPostDataStreamReadCallback>)+388)(061948a4140de9d4f304c80724508f0147d74f83)
     #04 pc 0000000002865c28 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::Read(void*, int, scoped_refptr<CefPostDataStreamReadCallback>)+112)(061948a4140de9d4f304c80724508f0147d74f83)
     #05 pc 0000000004e745ac /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(ArkWeb_HttpBodyStream_::Read(void*, long) const+124)(061948a4140de9d4f304c80724508f0147d74f83)
     #06 pc 00000000000318b8 /data/storage/el1/bundle/libs/arm64/libwindvane.so(c7fcd317362718625bc274826f4e4217942fa164)
     // ...
     #247 pc 0000000004e74c84 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(ArkWeb_HttpBodyStream_::OnReadComplete(char*, int)+100)(061948a4140de9d4f304c80724508f0147d74f83)
     #248 pc 0000000002865b94 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::OnStreamReadAsync(scoped_refptr<net::WrappedIOBuffer>, scoped_refptr<CefPostDataStreamReadCallback>, int)+36)(061948a4140de9d4f304c80724508f0147d74f83)
     #249 pc 0000000002865b30 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::ReadAsync(void*, int, scoped_refptr<CefPostDataStreamReadCallback>)+388)(061948a4140de9d4f304c80724508f0147d74f83)
     #250 pc 0000000002865c28 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::Read(void*, int, scoped_refptr<CefPostDataStreamReadCallback>)+112)(061948a4140de9d4f304c80724508f0147d74f83)
     #251 pc 0000000004e745ac /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(ArkWeb_HttpBodyStream_::Read(void*, long) const+124)(061948a4140de9d4f304c80724508f0147d74f83)
     #252 pc 00000000000318b8 /data/storage/el1/bundle/libs/arm64/libwindvane.so(c7fcd317362718625bc274826f4e4217942fa164)
     #253 pc 0000000004e74c84 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(ArkWeb_HttpBodyStream_::OnReadComplete(char*, int)+100)(061948a4140de9d4f304c80724508f0147d74f83)
     #254 pc 0000000002865b94 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::OnStreamReadAsync(scoped_refptr<net::WrappedIOBuffer>, scoped_refptr<CefPostDataStreamReadCallback>, int)+36)(061948a4140de9d4f304c80724508f0147d74f83)
     #255 pc 0000000002865b30 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(CefPostDataStreamImpl::ReadAsync(void*, int, scoped_refptr<CefPostDataStreamReadCallback>)+388)(061948a4140de9d4f304c80724508f0147d74f83)
     ```

### 场景二

1. 从faultlogger目录下获取CppCrash故障日志。查看故障原因和异常信息Reason。
2. 故障信号是SIGABRT(SI\_TKILL)。
   * 异常信息为空。从崩溃堆栈中可以看出，libestarx\_sdk.so调用了abort函数退出进程。

     ```screen
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317be700007163 from:29027:20020199
        Fault thread info:
        Tid:29027, Name:XXXXXX
        #00 pc 0000000000199168 /system/lib/ld-musl-aarch64.so.1(raise+228)(2869c16473050fa2addbe1ee1a3d23c3)
        #01 pc 0000000000146464 /system/lib/ld-musl-aarch64.so.1(abort+20)(2869c16473050fa2addbe1ee1a3d23c3)
        #02 pc 00000000001182e0 /data/storage/el1/bundle/libs/arm64/libestarx_sdk.so(02a23a55c2e05b8f6f1993b0e68e0c2cc61294c7) <---- 调用abort的so库
        #03 pc 0000000000117d20 /data/storage/el1/bundle/libs/arm64/libestarx_sdk.so(02a23a55c2e05b8f6f1993b0e68e0c2cc61294c7)
     ```
   * 异常信息是：terminating due to uncaught exception of type XXXX。未处理抛出的异常，跳过ld-musl-aarch64.so和libc++.so等公共基础库，找到异常的抛出位置结合代码进行具体分析。

     ```screen
     Uid:20020169
     Process name:com.hx.example
     Process life time:18446744073709547675s
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317bc900000a02 from:2562:20020169
     LastFatalMessage:terminating due to uncaught exception of type std::__h::system_error: random_device got an unexpected error: Bad file descriptor
     Fault thread info:
     Tid:2562, Name:线程名
     #00 pc 0000000000199e1c /system/lib/ld-musl-aarch64.so.1(raise+228)(6b9883f518515f73e093bce9a89a2548)
     #01 pc 0000000000146f8c /system/lib/ld-musl-aarch64.so.1(abort+20)(6b9883f518515f73e093bce9a89a2548)
     #02 pc 00000000000adc34 /system/lib64/libc++.so(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #03 pc 00000000000971f8 /system/lib64/libc++.so(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #04 pc 00000000000acef8 /system/lib64/libc++.so(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #05 pc 00000000000afeb8 /system/lib64/libc++.so(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #06 pc 00000000000afe34 /system/lib64/libc++.so(__cxa_throw+124)(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #07 pc 00000000000d1aa4 /system/lib64/libc++.so(std::__h::__throw_system_error(int, char const*)+96)(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #08 pc 00000000000d277c /system/lib64/libc++.so(std::__h::random_device::operator()()+168)(7817a009937816a1f11f1e7673c1e796f9d24b58)
     #09 pc 0000000000015dec /system/lib64/libhuaweiid_native_base.z.so(HMS::HuaweiId::SystemUtil::get_random(unsigned int, unsigned int) (.cfi)+84)(ebd50acd72f8ae96c384ac230dfaab8a) <-- 异常抛出位置
     #10 pc 0000000000010acc /system/lib64/libhuaweiid_native_base.z.so(HMS::HuaweiId::HiAppEventUtils::GenerateTransId() (.cfi)+184)(ebd50acd72f8ae96c384ac230dfaab8a)
     #11 pc 0000000000010c08 /system/lib64/libhuaweiid_native_base.z.so(HMS::HuaweiId::HiAppEventUtils::BuildEventKey(int) (.cfi)+52)(ebd50acd72f8ae96c384ac230dfaab8a)
     #12 pc 0000000000029b98 /system/lib64/module/hms/core/libauthentication.z.so(HMS::HuaweiId::NapiAccountCapabilityScheduler::ExecuteCommonRequest(napi_env__*, napi_callback_info__*, bool)+1848)(1e1a51499a827de407d5f0af2731db35)
     #13 pc 000000000003ec44 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+212)(edf034e044dbf26f955142c343577527)
     #14 pc 0000000000405b2c /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
     #15 at getQuickLoginAnonymousPhone (XXXX|4.0.4|src/main/ets/quickLogin/QuickLoginService.ts:39:1)
     #16 at quickLoginInit (XXXX|4.0.4|src/main/ets/quickLogin/QuickLoginService.ts:18:1)
     #17 at QuickLogin (XXXX|2.2.2|src/main/ets/initialization/sdkinit/QuickLogin/index.ts:0:1)
     #18 at anonymous (XXXX|2.2.2|src/main/ets/entryability/BasicEntryAbility.ts:0:1)
     ```
   * 异常信息是：CFI check failed. Function Address:XXXX0IStandardAudioManagerListener。

     从崩溃堆栈中可以看出，libohaudio.so库的CFI check失败，从而调用abort函数退出。

     ```screen
     Process name:com.hx.example
     Process life time:167s
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317c1100009bc8 from:39880:20020241
     LastFatalMessage: CFI check failed. Function Address: 0x5c91535f00IStandardAudioManagerListener
     Fault thread info:
     Tid:41489, Name:OS_IPC_3_41489
     #00 pc 0000000000199c78 /system/lib/ld-musl-aarch64.so.1(raise+228)(48d27d8bf1dca4a4aebb6d87cc78e501)
     #01 pc 0000000000146ecc /system/lib/ld-musl-aarch64.so.1(abort+20)(48d27d8bf1dca4a4aebb6d87cc78e501)
     #02 pc 0000000000146eb4 /system/lib/ld-musl-aarch64.so.1(__cfi_fail_report+48)(48d27d8bf1dca4a4aebb6d87cc78e501)
     #03 pc 0000000000022098 /system/lib64/ndk/libohaudio.so(__cfi_check_fail+32)(00623ec2147353a07695f57818234421)
     #04 pc 00000000000260ec /system/lib64/ndk/libohaudio.so(__cfi_check+4332)(00623ec2147353a07695f57818234421)
     #05 pc 00000000000a08c0 /system/lib/ld-musl-aarch64.so.1(cfi_slowpath_common+540)(48d27d8bf1dca4a4aebb6d87cc78e501)
     #06 pc 000000000002dc80 /system/lib64/ndk/libohaudio.so(OHOS::AudioStandard::OHAudioRendererCallback::OnInterrupt(OHOS::AudioStandard::InterruptEvent const&)+64)(00623ec2147353a07695f57818234421)
     ```
   * 异常信息是：ecma\_vm cannot run in multi-thread! thread:XXXX currentThread:XXXX。

     JavaScript是单线程的，对JS对象的操作必须在创建该对象的原始线程上进行。

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
     #06 pc 000000000021a818 /data/storage/el1/bundle/libs/arm64/libssound.so
     ```
   * 异常信息是：resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit.hsp。

     从异常信息可以看出，应用崩溃和[Wallet Kit](../harmonyos-guides/wallet-introduction.md)有关。

     ```screen
     Process name:com.hx.example
     Process life time:18446744073709167786s
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317be4000082d8 from:33496:20020196
     LastFatalMessage:[default] [LoadJSPandaFile:108] resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit.hsp
     Fault thread info:
     Tid:33496, Name:com.hx.example
     #00 pc 000000000019c9c0 /system/lib/ld-musl-aarch64.so.1(raise+228)(9de0feb6aaed25d882950b087a420225)
     #01 pc 0000000000149b30 /system/lib/ld-musl-aarch64.so.1(abort+20)(9de0feb6aaed25d882950b087a420225)
     #02 pc 000000000042b2d4 /system/lib64/platformsdk/libark_jsruntime.so(92357ecadd291684f42e892cef654d36)
     #03 pc 0000000000594658 /system/lib64/platformsdk/libark_jsruntime.so(92357ecadd291684f42e892cef654d36)
     #04 pc 0000000000581c5c /system/lib64/platformsdk/libark_jsruntime.so(92357ecadd291684f42e892cef654d36)
     ```
   * 异常信息是：Assertion failed: xxx (xxx)。

     例如：Assertion failed: handle->flags & UV\_HANDLE\_CLOSING (/home/lwf/deps/libuv-1.51.0/src/unix/core.c: uv\_\_finish\_close: 314)，应用so库执行了函数uv\_\_finish\_close中的断言检查，断言条件handle->flags & UV\_HANDLE\_CLOSING失败，其作用是检测句柄（handle）是否关闭。

     ```screen
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317b5100007e2e from:32302:20020049
     LastFatalMessage:Assertion failed: handle->flags & UV_HANDLE_CLOSING (/home/lwf/deps/libuv-1.51.0/src/unix/core.c: uv__finish_close: 314)
     Fault thread info:
     Tid:32754, Name:com.hx.example
     #00 pc 00000000001b0958 /system/lib/ld-musl-aarch64.so.1(raise+216)(52299a28d60f0bb4073bd788bc023a3a)
     #01 pc 000000000015c8d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(52299a28d60f0bb4073bd788bc023a3a)
     #02 pc 000000000015cb0c /system/lib/ld-musl-aarch64.so.1(__assert_fail+308)(52299a28d60f0bb4073bd788bc023a3a)
     #03 pc 0000000001217544 /data/storage/el1/bundle/libs/arm64/librtcsdk.so(e28c80c93b52086a88022e4d43ce8a764cb7c719)
     #04 pc 0000000001213a98 /data/storage/el1/bundle/libs/arm64/librtcsdk.so(e28c80c93b52086a88022e4d43ce8a764cb7c719)
     #05 pc 00000000012138d0 /data/storage/el1/bundle/libs/arm64/librtcsdk.so(uv_run+560)(e28c80c93b52086a88022e4d43ce8a764cb7c719)
     #06 pc 00000000005d02a8 /data/storage/el1/bundle/libs/arm64/librtcsdk.so(e28c80c93b52086a88022e4d43ce8a764cb7c719)
     #07 pc 00000000005d9ee4 /data/storage/el1/bundle/libs/arm64/librtcsdk.so(e28c80c93b52086a88022e4d43ce8a764cb7c719)
     #08 pc 00000000001d0a2c /system/lib/ld-musl-aarch64.so.1(start+240)(52299a28d60f0bb4073bd788bc023a3a)
     ```
   * 异常信息是：[napi\_fatal\_error] FATAL ERROR: (null) init failed，致命错误，初始化失败。

     napi\_fatal\_error函数作用是在致命错误时终止进程，libbdmssdk.so主动调用该函数退出进程。

     ```screen
     Reason:Signal:SIGABRT(SI_TKILL)@0x01317bf60000994d from:39245:20020214
     LastFatalMessage:[napi_fatal_error] FATAL ERROR: (null) init failed
     Fault thread info:
     Tid:56980, Name:OS_TaskWorker
     #00 pc 00000000001b0958 /system/lib/ld-musl-aarch64.so.1(raise+216)(52299a28d60f0bb4073bd788bc023a3a)
     #01 pc 000000000015c8d8 /system/lib/ld-musl-aarch64.so.1(abort+24)(52299a28d60f0bb4073bd788bc023a3a)
     #02 pc 0000000000081b4c /system/lib64/platformsdk/libace_napi.z.so(napi_fatal_error+92)(487ddb26a8df0015506708d38263d5e7)
     #03 pc 0000000000164488 /data/storage/el1/bundle/libs/arm64/libbdmssdk.so(54d266e02a1a2a36a7e48520dcedd648fae3b8e4)
     #04 pc 00000000001bd0c0 /data/storage/el1/bundle/libs/arm64/libbdmssdk.so(54d266e02a1a2a36a7e48520dcedd648fae3b8e4)
     ```

### 场景三

1. 从faultlogger目录下获取CppCrash故障日志。查看故障原因和异常信息Reason。
2. 故障信号是SIGTRAP(TRAP\_BRKPT)。
   * 异常信息为空。

     ```screen
     Process name:com.hx.example
     Process life time:6374s
     Reason:Signal:SIGTRAP(TRAP_BRKPT)@0x0000005ce2b025a8 
     Fault thread info:
     Tid:61493, Name:Chrome_IOThread
     #00 pc 0000000004f825a8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #01 pc 0000000003340764 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #02 pc 00000000033421ac /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #03 pc 000000000333c53c /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #04 pc 000000000339d3dc /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #05 pc 000000000339eaf8 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     #06 pc 000000000339efb0 /data/storage/el1/bundle/arkwebcore/libs/arm64/libarkweb_engine.so(1c5060d089c8b433e6e7b62c61a1fe8c83459e22)
     ```
   * 异常信息是：Failed to unwind stack, try to get unreliable call stack from #02 by reparsing thread stack。

     表示业务代码运行时改写了原本保存函数调用信息的栈内存，导致无法成功回溯调用栈。因为调用栈可能不是一个完整的函数调用链路，需要结合业务代码分析其中的调用链路。详情参考[栈覆盖故障场景日志规格](../harmonyos-guides/cppcrash-guidelines.md#栈覆盖故障场景日志规格)。

     ```screen
     Process life time:21s
     Reason:Signal:SIGTRAP(TRAP_BRKPT)@0x0000005c90a9e294 
     LastFatalMessage: Failed to unwind stack, try to get unreliable call stack from #02 by reparsing thread stack.
     Fault thread info:
     Tid:31390, Name:com.hx.example
     #00 pc 0000000002bde294 /data/storage/el1/bundle/libs/arm64/libelectron.so(bab84122e801b4e410c279077891f501534d5a8d)
     #01 pc 0000000001ee17e4 /data/storage/el1/bundle/libs/arm64/libelectron.so(v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, v8::OOMDetails const&)+796)(bab84122e801b4e410c279077891f501534d5a8d)
     #02 pc 0000000000e18dc6 /data/storage/el1/bundle/libs/arm64/libelectron.so(bab84122e801b4e410c279077891f501534d5a8d)
     #03 pc 0000000001cef000 /data/storage/el1/bundle/libs/arm64/libelectron.so(bab84122e801b4e410c279077891f501534d5a8d)
     #04 pc 0000000000e3c413 /data/storage/el1/bundle/libs/arm64/libelectron.so(bab84122e801b4e410c279077891f501534d5a8d)
     #05 pc 00000000001b3990 /system/lib/ld-musl-aarch64.so.1(bab3669677bc77285aec30e8f1aae587)
     #06 pc 00000000001a938c /system/lib/ld-musl-aarch64.so.1(bab3669677bc77285aec30e8f1aae587)
     ```

### 场景四

1. 从faultlogger目录下获取CppCrash故障日志。查看故障原因和异常信息Reason。
2. 故障信号是SIGBUS，内存访问错误。

   ```screen
   Reason:Signal:SIGBUS(BUS_ADRALN)@0x6b6b79c57033cdae 
   Fault thread info:
   Tid:31380, Name:com.hx.example
   #00 pc 6b6b79c57033cdae Not mapped
   #01 pc 0000000000a60cfc /system/lib64/ndk/libjsvm.so(v8impl::(anonymous namespace)::FunctionCallbackWrapper::Invoke(v8::FunctionCallbackInfo<v8::Value> const&)+148)
   #02 pc 000000000076ac5c /system/lib64/ndk/libv8_shared.so(5b2ac1695b5376e6271d4d967cc3bda2dc6d7772)
   #03 pc 000000000076a810 /system/lib64/ndk/libv8_shared.so(5b2ac1695b5376e6271d4d967cc3bda2dc6d7772)
   #04 pc 000000000076a2a4 /system/lib64/ndk/libv8_shared.so(5b2ac1695b5376e6271d4d967cc3bda2dc6d7772)
   #05 pc 000000000060fda4 /system/lib64/ndk/libv8_shared.so(5b2ac1695b5376e6271d4d967cc3bda2dc6d7772)
   ```

## 分析结论

### 场景一

* 异常信息为空。

  无效内存访问导致闪退。
* 异常信息是：Signal:SIGSEGV(SEGV\_MAPERR)@000000000000000000 probably caused by NULL pointer dereference。

  无效内存访问，访问空指针。
* 异常信息是：SIGSEGV(SEGV\_ACCERR)@0x0000000000000000 current thread stack low address = 0x0000000000000000, probably caused by stack-buffer-overflow。

  递归调用未能终止导致栈内存溢出。

### 场景二

* 异常信息为空。

  so库主动调用abort函数退出进程。
* 异常信息是：terminating due to uncaught exception of type XXXX。

  未处理抛出的异常导致应用闪退。
* 异常信息是：CFI check failed. Function Address:XXXX0IStandardAudioManagerListener。

  应用没有初始化OH\_AudioRenderer\_Callbacks的所有回调函数。
* 异常信息是：ecma\_vm cannot run in multi-thread! thread:XXXX currentThread:XXXX。

  存在多线程安全问题导致应用闪退。
* 异常信息是：resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit.hsp。

  平板设备不支持[Wallet Kit](../harmonyos-guides/wallet-introduction.md)导致应用在平板上打开闪退。
* 异常信息是：Assertion failed: xxx (xxx)。

  断言失败错误，断言条件为false时，进程会直接终止。

  例：Assertion failed: handle->flags & UV\_HANDLE\_CLOSING (/home/lwf/deps/libuv-1.51.0/src/unix/core.c: uv\_\_finish\_close: 314)。断言handle->flags & UV\_HANDLE\_CLOSING失败，表示句柄flags是关闭状态，说明应用在句柄关闭时执行非法操作，例如重复调用关闭接口或访问已失效句柄。
* 异常信息是：[napi\_fatal\_error] FATAL ERROR: (null) init failed。

  应用进程初始化失败，主动调用napi\_fatal\_error函数退出进程。

### 场景三

* 异常信息为空。

  栈顶so库触发软件断点信号导致应用闪退。
* 异常信息是：Failed to unwind stack, try to get unreliable call stack from #02 by reparsing thread stack。

  栈顶so库触发软件断点信号导致应用闪退。

### 场景四

栈顶so库尝试访问未对齐的内存地址导致应用闪退。

## 修改建议

### 场景一

* 异常信息为空。

  如果发生异常的so库是flutter等三方库，可以尝试升级三方库版本解决。其他情况由异常so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
* 异常信息是：Signal:SIGSEGV(SEGV\_MAPERR)@000000000000000000 probably caused by NULL pointer dereference。

  栈顶so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析，排查是否访问了空指针，在访问变量前进行非空校验。
* 异常信息是：SIGSEGV(SEGV\_ACCERR)@0x0000000000000000 current thread stack low address = 0x0000000000000000, probably caused by stack-buffer-overflow。

  [使用Asan检测内存错误](../best-practices/bpta-stability-asan-detection.md)，修复引起内存错误的代码，参考文档[stack-buffer-overflow](../best-practices/bpta-stability-asan-detection.md#section1842052044614)。

### 场景二

* 异常信息为空。

  使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码分析调用abort函数是否正常。
* 异常信息是：terminating due to uncaught exception of type XXXX。

  使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析，在抛出异常的位置使用try-catch捕获并处理异常。
* 异常信息是：CFI check failed. Function Address:XXXX0IStandardAudioManagerListener。

  请确保OH\_AudioRenderer\_Callbacks的每一个回调都被自定义的回调方法或空指针初始化。详情参考[OH\_AudioRenderer\_Callbacks\_Struct](../harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct.md)。
* 异常信息是：ecma\_vm cannot run in multi-thread! thread:XXXX currentThread:XXXX。

  启用[方舟多线程检测](../best-practices/bpta-stability-ark-runtime-detection.md#section7199344111510)，运行或调试当前应用，当程序出现多线程安全问题时，会弹出Crash log信息。点击信息中的链接，可以跳转至引起多线程安全问题的代码处。
* 异常信息是：resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/com.huawei.hmos.walletkit/walletKit/walletKit.hsp。

  在使用钱包服务前需要判断当前设备是否支持NFC能力，将NFC能力加入[自定义syscap](../harmonyos-references/syscap.md)中。
* 异常信息是：Assertion failed: xxx (xxx)。

  检查代码运行时的断言条件，修复业务逻辑异常。

  例：Assertion failed: handle->flags & UV\_HANDLE\_CLOSING (/home/lwf/deps/libuv-1.51.0/src/unix/core.c: uv\_\_finish\_close: 314)。业务逻辑中避免调用正在关闭的句柄。
* 异常信息是：[napi\_fatal\_error] FATAL ERROR: (null) init failed。

  使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码分析调用napi\_fatal\_error函数原因并修改。

### 场景三

* 异常信息为空。

  栈顶so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
* 异常信息是：Failed to unwind stack, try to get unreliable call stack from #02 by reparsing thread stack。

  栈顶so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码分析具体的调用链路。

### 场景四

栈顶so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
