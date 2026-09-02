---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-2
title: 启动应用时发生闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 启动应用时发生闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:570b77218c510b1f0c4bd22c9ad0f4dd004c6cc9f15de9faaa33c36076ea04e5
---

## 问题现象

用户点击应用图标打开应用，打开过程中应用发生闪退。

## 背景知识

应用打开发生闪退，主要是发生了JS Crash异常或者CppCrash异常所导致。

该类异常的一般定位思路为：

1. 通过问题发生的时间，找到faultlogger目录对应的JS Crash日志文件。
2. 通过日志文件中以Reason:开头的行，找到对应的关键字，确定当前故障归属的具体场景。
3. 根据异常的关键字在下表中检索应用发生JS Crash/CppCrash的原因，完成定界。

* [JS Crash异常](../best-practices/bpta-stability-app-crash-js-way.md)根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。

  JS Crash日志包含异常原因及异常堆栈等关键定位信息：

  ```txt
  Build info:XXX-XXXX X.X.X.XX(XXXXXXXX) <- 版本信息
  Module name:com.example.myapplication <- 模块名
  Version:1.0.0 <- 版本号
  Pid:579 <- 进程号
  Uid:0 <- 用户ID
  Reason:TypeError <- 原因
  Error message:Cannot read property c of undefined <- 异常信息
  Cannot get SourceMap info, dump raw stack: <- 应用安装包为release包安装时不包含sourcemap文件，JS栈通过sourcemap行列号解析会失败
  Stacktrace:
      at onPageShow (entry/src/main/ets/pages/Index.ets:7:13)  <-异常代码调用栈
             ^                                      ^
           函数名异常代码文件行列号位置
  ```

  JS Crash常见场景及关键字检索表：

  | 异常场景 | 场景分类 | 检索关键字 |
  | --- | --- | --- |
  | 变量不是预期的类型，不能调用对应的属性 | TypeError | Error message:Cannot read property XXX of undefined |
  | 变量不是预期的类型，不能调用对应的方法 | TypeError | Error message:is not callable |
  | 变量不是一个有效的javascript对象 | TypeError | Error message:Receiver is not a JSObject |
  | 变量为只读属性，不能为只读属性赋值 | TypeError | Error message:Cannot assign to read only property |
  | 不能将undefined当作可迭代对象 | TypeError | Error message: undefined is not iterable (cannot read property Symbol(Symbol.iterator))" |
  | 未处理业务错误抛出的异常 | BusinessError | Reason:BusinessError |
  | 字符串的格式不符合JSON语法规范 | SyntaxError | Error message:Unexpected Text in JSON |
  | 没有定义对应key的@Provide变量 | ReferenceError | Error message：@Component XXX missing @Provide property with name XXX.Fail to resolve @ConsumeXXX |
  | 删除/更改重复提供对应@Provide属性 | ReferenceError | Error message：XXXX：duplicate @Provide property with name XXX |
  | 非法参数抛出异常 | Error | Invalid parameter |
  | 依赖注入容器里找不到 xxx 对应的实现绑定 | Error | Error message:No matching bindings found for serviceIdentifier: xxx |
* [CppCrash](../best-practices/bpta-quality-overview.md#section19523112309)应用崩溃指的是C/C++运行时崩溃，CppCrash进程崩溃检测基于操作系统信号机制。

  CppCrash常见场景及关键字检索表：

  | 异常场景 | 场景分类 | 检索关键字 |
  | --- | --- | --- |
  | 访问了无效内存引用 | SIGSEGV | Reason:Signal:SIGSEGV |
  | 进程异常终止 | SIGABRT | Reason:Signal:SIGABRT |
  | 非法指令异常 | SIGILL | Reason:Signal:SIGILL |

  SIGILL二级分类，解释如下：

  | 二级分类 | 信号字符串 | 解释 | 触发原因 |
  | --- | --- | --- | --- |
  | 1 | ILL\_ILLOPC | 非法操作码异常。 | 发生在执行不被CPU支持的指令时，或者在尝试执行特权指令时。 |
  | 2 | ILL\_ILLOPN | 非法操作数异常。 | 发生在指令使用了不正确的操作数，或者是操作数的类型不正确时。 |
  | 3 | ILL\_ILLADR | 非法地址异常。 | 发生在程序尝试访问无效的内存地址时，或者是在尝试执行未对齐的内存访问时。 |
  | 4 | ILL\_ILLTRP | 非法陷阱异常。 | 发生在程序尝试执行一个非法的陷阱指令时，或者是在尝试执行一个未定义的操作时。 |
  | 5 | ILL\_PRVOPC | 特权操作码异常。 | 发生在普通用户尝试执行特权指令时。 |
  | 6 | ILL\_PRVREG | 特权寄存器异常。 | 发生在普通用户尝试访问特权寄存器时。 |
  | 7 | ILL\_COPROC | 协处理器异常。 | 发生在程序尝试使用未定义的协处理器指令时。 |
  | 8 | ILL\_BADSTK | 无效的堆栈异常。 | 发生在程序尝试在无效的堆栈地址上执行操作时，或者是在堆栈溢出时。 |

## 场景一

### 问题定位

打开对应日志查看内容，确定故障原因是ReferenceError。

* 异常信息是：Error message：@Component XXX missing @Provide property with name XXX. Fail to resolve @Consume XXX。

  ```txt
  Error name:ReferenceError
  Error message:@Component XXX missing @Provide property with name XXX.
           Fail to resolve @ConsumeXXX.
  Stacktrace:
     at initializeConsume (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6699:1)
     at Home (entry/src/main/ets/pages/Home.ets:6:1)
     at anonymous (entry/src/main/ets/pages/Index.ets:154:26)
     at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6815:1)
     at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6842:1)
     at anonymous (entry/src/main/ets/pages/Index.ets:154:26)
  ```
* 异常信息是：Error message：VideoVerifyView：duplicate @Provide property with name XXX. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。

  ```txt
  Reason:ReferenceError
  Error name:ReferenceError
  Error message:VideoVerifyView: duplicate @Provide property with name XXX. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed.
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at addProvidedVar (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6673:1)
      at VideoVerifyView (app|app|1.0.0|src/main/ets/pages/scan/view/VideoVerifyView.ts:73:1)
      at anonymous (app|app|1.0.0|src/main/ets/pages/scan/VideoVerifyPage.ts:150:1)
      at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6815:1)
      at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6842:1)
      at anonymous (app|app|1.0.0|src/main/ets/pages/scan/VideoVerifyPage.ts:148:1)
      at ifElseBranchUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4300:1)
      at anonymous (app|app|1.0.0|src/main/ets/pages/scan/VideoVerifyPage.ts:146:1)
      at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6815:1)
      at UpdateElement (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6517:1)
      at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6744:1)
      at updateDirtyElements (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6739:1)
      at rerender (app|app|1.0.0|src/main/ets/pages/scan/VideoVerifyPage.ts:181:1)
  ```

### 分析结论

* 异常信息是：Error message：@Component XXX missing @Provide property with name XXX.Fail to resolve @ConsumeXXX。初始化@Consume变量XXX时，没有定义对应key的@Provide变量，引用一个不存在的变量，框架抛出JS ERROR。
* 异常信息是：Error message：XXXX：duplicate @Provide property with name XXX. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。名为XXX的@Provide属性重复。具有此名称的属性已有父组件存在。不允许重写@Provide组件。

### 修改建议

* 异常信息是：Error message：@Component XXX missing @Provide property with name XXX.Fail to resolve @ConsumeXXX。检查变量是否存在，若存在则在父组件中定义@Provide变量并赋值。
* 异常信息是：Error message：XXXX：duplicate @Provide property with name XXX. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。删除/更改重复提供对应@Provide属性的代码。

## 场景二

### 问题定位

故障原因是TypeError：

* 异常信息是Error message:Cannot read property XXX of undefined。

  ```txt
  Reason:TypeError
  Error name:TypeError
  Error message:Cannot read property loadPackage of undefined
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
  at initPageUrl (entry|entry|1.0.0|src/main/ets/h5common/page/H5Page.ts:3:1)
  ```
* 异常信息是Error message:is not callable。

  ```txt
  Reason:TypeError
  Error name:TypeError
  Error message:is not callable
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at forEachUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4352:1)
      at anonymous (entry|entry|1.0.0|src/main/ets/pages/Child/CaseRepeat.ts:478:1)
  ```
* 异常信息是Error message:Receiver is not a JSObject。

  ```txt
  Reason:TypeError
  Error name:TypeError
  Error message:Receiver is not a JSObject
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at anonymous (entry|entry|1.0.0|src/main/ets/view/webview/BasicWebView.ts:932:1)
      at anonymous (entry|entry|1.0.0|src/main/ets/view/webview/JsBridge.ts:100:1)
      at handlerReturnData (entry|entry|1.0.0|src/main/ets/view/webview/JsBridge.ts:35:1)
      at anonymous (entry|entry|1.0.0|src/main/ets/view/webview/BasicWebView.ts:1148:1)
      at (entry/src/main/ets/pages/base/WebViewTemplatePage.ets:183:7)
  ```
* 异常信息是Error message:Cannot assign to read only property。

  ```txt
  Reason:TypeError
  Error name:TypeError
  Error message:Cannot assign to read only property
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at onPageShow (entry|entry|1.0.0|src/main/ets/pages/Child/VaccSelect.ts:282:1)
  ```

从异常信息可以看出，变量不是预期的类型。

### 分析结论

* 异常信息是Error message:Cannot read property XXX of undefined。变量不是预期的类型，不能调用对应的属性。
* 异常信息是Error message:is not callable。变量不是预期的类型，不能调用对应的方法。
* 异常信息是Error message:Receiver is not a JSObject。变量不是一个有效的javascript对象。
* 异常信息是Error message:Cannot assign to read only property。变量为只读属性，无法为只读属性赋值。
* 异常信息是Error message:undefined is not iterable (cannot read property Symbol(Symbol.iterator))。不能将undefined当作可迭代对象。

### 修改建议

* 异常信息是Error message:Cannot read property XXX of undefined。在使用变量前进行校验，检查变量是否存在对应的属性。
* 异常信息是Error message:is not callable。检查变量或者this指针是否存在对应的方法。
* 异常信息是Error message:Receiver is not a JSObject。检查传入对象数据是否有误，并做严格的数据校验处理报错。
* 异常信息是Error message:Cannot assign to read only property。为变量赋值前校验是否为只读属性。
* 异常信息是Error message:undefined is not iterable (cannot read property Symbol(Symbol.iterator))。在迭代之前先保证变量是数组可迭代对象，再给默认值防错。

## 场景三

### 问题定位

故障原因是Error：

* 异常信息是：Invalid parameter。

  ```txt
  Reason:Error
  Error name:Error
  Error message:Invalid parameter
  Error code:
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at anonymous (phone|@ohos/fcpush|1.0.0|src/main/ets/push/InitPushSDK.ts:94:1)
  ```

### 分析结论

非法参数抛出异常，应用未处理异常导致闪退。

### 修改建议

对异常入参进行错误处理。

## 场景四

### 问题定位

故障原因是BusinessError：

* 故障信息是：e.message: Unexpected Text in JSON: Invalid Token, e.name:SyntaxError。应用捕获SyntaxError后通过BusinessError抛出业务错误。

  ```txt
  Reason:BusinessError
  Error name:BusinessError
  Error message:e.message: Unexpected Text in JSON: Invalid Token, e.name: SyntaxError
  Error code:
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
      at BusinessError (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_util_module/json/json_js.js:18:1)
      at parse (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_util_module/json/json_js.js:38:1)
      at anonymous (entry|entry|1.0.0|src/main/ets/pages/tab/home/funResultLayer.ts:1204:1)
      at anonymous (entry|entry|1.0.0|src/main/ets/pages/util/http.ts:379:1)
  ```

### 分析结论

未处理业务错误抛出的异常导致应用闪退。

### 修改建议

参考[堆栈轨迹分析](../harmonyos-guides/ide-release-app-stack-analysis.md)解析堆栈后结合具体代码进行分析，在异常抛出位置使用try-catch捕获并处理异常。

## 场景五

### 问题定位

故障原因是SyntaxError：

* 异常信息是Error message:Unexpected Text in JSON。这种错误通常发生在调用[JSON.parse](../harmonyos-references/js-apis-json.md#jsonparse)函数时，表示字符串的格式不符合JSON语法规范。

  ```txt
  Reason:SyntaxError
  Error name:SyntaxError
  Error message:Unexpected Text in JSON
  Stacktrace:
  Cannot get SourceMap info, dump raw stack:
     at innerJump (entry|entry|1.0.0|src/main/ets/pages/webview/YQWebView.ts:203:1)
     at innerJump (entry|base_webview|1.0.0|src/main/ets/webview/BaseJsCallNativeImpl.ts:190:1)
  ```

### 分析结论

字符串的格式不符合JSON语法规范。

### 修改建议

检查字符串是不是非JSON格式或者包含特殊字符。

## 场景六

### 问题定位

故障信号是SIGSEGV(SEGV\_MAPERR)：

* 异常信息是：Signal:SIGSEGV(SEGV\_MAPERR)@000000000000000000 probably caused by NULL pointer dereference。

  ```txt
  Uid:20020157
  Process name:应用包名
  Process life time:2s
  Reason:Signal:SIGSEGV(SEGV_MAPERR)@000000000000000000 probably caused by NULL pointer dereference
  Fault thread info:
  Tid:18211, Name:1.ui
  #00 pc 0000000000000000 Not mapped
  #01 pc 0000000000429100 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
  #02 pc 000000000075b0bc /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
  #03 pc 00000000005af6e4 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
  #04 pc 0000000000568e24 /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
  #05 pc 000000000056901c /data/storage/el1/bundle/libs/arm64/libsunloginclient.so(16409f4ecdc715f04b938e5ce840a0c704acac30)
  ```

### 分析结论

无效内存访问，访问空指针。

### 修改建议

栈顶so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析，排查是否访问了空指针，在访问变量前进行非空校验。

## 场景七

### 问题定位

故障信号是SIGABRT(SI\_TKILL)：

* 异常信息为空。从崩溃堆栈中可以看出，libestarx\_sdk.so调用了abort函数退出进程。

  ```txt
  Reason:Signal:SIGABRT(SI_TKILL)@0x01317be700007163 from:29027:20020199
  Fault thread info:
  Tid:29027, Name:XXXXXX
  #00 pc 0000000000199168 /system/lib/ld-musl-aarch64.so.1(raise+228)(2869c16473050fa2addbe1ee1a3d23c3)
  #01 pc 0000000000146464 /system/lib/ld-musl-aarch64.so.1(abort+20)(2869c16473050fa2addbe1ee1a3d23c3)
  #02 pc 00000000001182e0 /data/storage/el1/bundle/libs/arm64/libestarx_sdk.so(02a23a55c2e05b8f6f1993b0e68e0c2cc61294c7) <- 调用abort的so库
  #03 pc 0000000000117d20 /data/storage/el1/bundle/libs/arm64/libestarx_sdk.so(02a23a55c2e05b8f6f1993b0e68e0c2cc61294c7)
  ```
* 异常信息是：terminating due to uncaught exception of type XXXX。未处理抛出的异常，跳过ld-musl-aarch64.so和libc++.so等公共基础库，找到异常的抛出位置结合代码进行具体分析。

  ```txt
  Uid:20020169
  Process name:应用包名
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
  #09 pc 0000000000015dec /system/lib64/libhuaweiid_native_base.z.so(HMS::HuaweiId::SystemUtil::get_random(unsigned int, unsigned int) (.cfi)+84)(ebd50acd72f8ae96c384ac230dfaab8a) <- 异常抛出位置
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

### 分析结论

* 异常信息为空。so库主动调用abort函数退出进程。
* 异常信息是：terminating due to uncaught exception of type XXXX。未处理抛出的异常导致应用闪退。

### 修改建议

* 异常信息为空。使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码分析调用abort函数是否正常。
* 异常信息是：terminating due to uncaught exception of type XXXX。使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析，在抛出异常的位置使用try-catch捕获并处理异常。

## 场景八

### 问题定位

故障信号是SIGILL(ILL\_ILLOPC)：

* 异常信息是：Signal:SIGILL(ILL\_ILLOPC)@000000000000000000。

  ```txt
  Uid:20020930
  Process name:应用包名
  Process life time:18446744073709072495s
  Reason:Signal:SIGILL(ILL_ILLOPC)@000000000000000000 
  Fault thread info:
  Tid:29089, Name:线程名
  #00 pc 000000000003319c /data/storage/el1/bundle/libs/arm64/libmyjsi.so(1bd9227cd6d2583529a2f406bc718a0a69925f03)
  #01 pc 0000000000045344 /data/storage/el1/bundle/libs/arm64/libmyjsi.so(1bd9227cd6d2583529a2f406bc718a0a69925f03)
  #02 pc 0000000000bb1c60 /data/storage/el1/bundle/libs/arm64/libmyv8.so(v8::internal::MemoryAllocator::SetPermissionsOnExecutableMemoryChunk(v8::internal::VirtualMemory*, unsigned long, unsigned long, unsigned long)+192)(15166f2e78bd7f87)
  #03 pc 0000000000bb19a4 /data/storage/el1/bundle/libs/arm64/libmyv8.so(v8::internal::MemoryAllocator::AllocateAlignedMemory(unsigned long, unsigned long, unsigned long, v8::internal::Executability, void*, v8::internal::VirtualMemory*)+292)(15166f2e78bd7f87)
  #04 pc 0000000000bb1e6c /data/storage/el1/bundle/libs/arm64/libmyv8.so(v8::internal::MemoryAllocator::AllocateUninitializedChunk(v8::internal::BaseSpace*, unsigned long, v8::internal::Executability, v8::internal::PageSize)+152)(15166f2e78bd7f87)
  #05 pc 0000000000bb2778 /data/storage/el1/bundle/libs/arm64/libmyv8.so(v8::internal::MemoryAllocator::AllocatePage(v8::internal::MemoryAllocator::AllocationMode, v8::internal::Space*, v8::internal::Executability)+204)(15166f2e78bd7f87)
  ```

### 分析结论

非法操作码异常，需栈顶so库解析崩溃栈后结合代码进行具体分析。

### 修改建议

结合崩溃栈解析结果和具体代码排查是否执行不被CPU支持的指令，或者尝试执行特权指令。
