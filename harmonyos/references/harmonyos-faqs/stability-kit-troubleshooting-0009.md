---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/stability-kit-troubleshooting-0009
title: 应用卡死问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 故障排查 > 应用卡死问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:40+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a60129796f000e84324a1b8c53be4fdcacefd612cce82677bb2e7bafe0ce2c6e
---

## 问题现象

应用在使用时页面卡死闪退。

## 场景一

### 定位过程

1. 确认闪退类型，闪退问题首先排查是否出现JsCrash或者CppCrash，查看faultlogger目录，是否生成了形如jscrash-应用包名或者cppcrash-应用包名的故障日志。
2. 确认闪退原因。

   ```txt
       Reason:Error
       Error name:Error
       Error message:Init error. The WebviewController must be associated with a Web component
       Error code 17100001
   ```

   从故障日志中可以获取到故障原因和异常信息。

   * 根据日志中的Error Code：17100001可以在[WebView错误码](../harmonyos-references/errorcode-webview.md)中查询到相关解释。
   * 异常信息是Error message:Init error. The WebviewController must be associated with a Web component，WebviewController还没有和具体的Web组件关联，无法进行相应的操作。

### 分析结论

WebviewController还没有和具体的Web组件关联，无法进行相应的操作。

### 修改建议

建议将相应操作放在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)(内有示例代码)中，此回调当Controller成功绑定到Web组件时触发。

## 场景二

### 定位过程

1. 在faultlogger目录下查找Appfreeze-应用包名-应用UID-年月日时分秒文件，从Appfreeze日志文件中可以看出当前故障模块进程号PID，故障原因EVENTNAME和故障发生的时间点TIMESTAMP。

   ```txt
       EVENTNAME = THREAD_BLOCK_6S
       TIMESTAMP = 2025/04/28-23:21:11:452
       PID = 38709
       UID = 20020283
       TID = 38709
       PACKAGE_NAME = com.hx.example
       PROCESS_NAME = com.hx.example
       eventLog_action = t,cmd:c,cmd:cci,cmd:m,cmd:dam,tr,k:SysRqFile,hot
       eventLog_interval = 10
       MSG = 
       Fault time:2025/04/28-23:21:08
       App main thread is not response!
   ```
2. 排查主消息任务队列(EventHandler)是否有异常，日志中搜索"mainHandler dump is"，能得到两个结果，第一个是3s半周期检测的信息，第二个是6s故障上报的信息。

   查看两个队列的当前任务，如果相同说明该任务执行时间过长，导致了主线程卡死。

   ```txt
       mainHandler dump is:
        EventHandler dump begin curTime: 2025-04-28 11:22:13.469
        Event runner (Thread name = , Thread ID = 43116) is running
        Current Running: start at 2025-04-28 11:22:07.424, Event { send thread = 43116, send time = 2025-04-28 11:22:07.423, handle time = 2025-04-28 11:22:07.423, trigger time = 2025-04-28 11:22:07.424, task name = , caller = [native_safe_async_work.cpp(PostTask:419)] }
   ```
3. 排查主线程堆栈，日志搜索"Tid:应用进程号，Name:应用包名"。

   根据栈顶\_\_pthread\_mutex\_timedlock\_inner可知在等锁，等待获取锁的为libentry.so库，根据前缀/data/storage判断为应用so库。

   ```txt
       Tid:43116, Name:com.hx.example
       #00 pc 00000000001b9730 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+148)(cca90e1f13e1d967a51504163ea08b16)
       #01 pc 00000000001bf5e8 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+540)(cca90e1f13e1d967a51504163ea08b16)
       #02 pc 000000000009c7d4 /system/lib/ld-musl-aarch64.so.1(dl_iterate_phdr+48)(cca90e1f13e1d967a51504163ea08b16)
       #03 pc 0000000000143e70 /data/storage/el1/bundle/libs/arm64/libentry.so(d50b68584582b0dd7b02a7e0fe68133a672f2c92)
       #04 pc 00000000001424b0 /data/storage/el1/bundle/libs/arm64/libentry.so(unw_init_local+256)(d50b68584582b0dd7b02a7e0fe68133a672f2c92)
       #05 pc 000000000028fe4c /data/storage/el1/bundle/libs/arm64/libentry.so(_Unwind_Backtrace+64)(d50b68584582b0dd7b02a7e0fe68133a672f2c92)
       #06 pc 000000000506e8c4 /data/storage/el1/bundle/libs/arm64/libkn.so(b19a192f933c28a00907b018744e1d59d7a9d1a1)
       #07 pc 000000000506cafc /data/storage/el1/bundle/libs/arm64/libkn.so(b19a192f933c28a00907b018744e1d59d7a9d1a1)
       #08 pc 00000000050b9cbc /data/storage/el1/bundle/libs/arm64/libkn.so(b19a192f933c28a00907b018744e1d59d7a9d1a1)
   ```
4. 观察hilog日志，查看具体阻塞原因。

   发现在22分7秒时，日志打印了请求任务返回结果，但直到22分16秒时，日志才打印taskpool:: Task PerformTask End，表示此线程任务结束，回收资源。

   说明主线程处理请求任务返回结果的时间长，也观察到日志信息网络请求结束计时，一共消耗：8661，结合当前运行任务native\_safe\_async\_work.cpp从22分7.424秒到22分13.469秒还未执行完成，判断是此任务在处理请求结果时，耗时过长，阻塞了主线程，导致触发了THREAD\_BLOCK\_6S。

   ```txt
       04-28 23:22:07.415 43116 43116 I A00000/com.hx.example/InputMethodManager: insertText, text: 工厂
       04-28 23:22:07.415 43116 43116 I A00000/com.hx.example/OhosTextInputService: OhosTextInputService.insertText text: 工厂
       04-28 23:22:07.415 43116 43116 I A00000/com.hx.example/OhosTextInputService: OhosTextInputService.updateState called: null -> TextFieldValue(text='xx工厂', selection=TextRange(4, 4), composition=null)
       04-28 23:22:07.421 43116 43116 I A03D00/com.hx.example/JSAPP: jceServiceConsumer request urlData:{"cmd":3,"subcmd":"CMD_POI_SUGGESTION_V02",...
       04-28 23:22:07.421 43116 43116 I A03D00/com.hx.example/JSAPP: jceServiceConsumer request params:{"strCity":"xx市","strKeyword":"xx工厂",...
       04-28 23:22:07.421 43116 43116 I A03D00/com.hx.example/JSAPP: TimeStatUtils jceServiceConsumer 网络请求 开始计时
       04-28 23:22:07.422 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController RouteSearch request start
       04-28 23:22:07.423 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController RouteSearch params 
       04-28 23:22:07.425 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController 网络请求开始
       // ...
       04-28 23:22:07.432 43116 43116 I A00000/com.hx.example/Konan_main: bie ming PoiRecordItem {"requestId":"5871877323626435705","id":"14374180825296894895",...
       04-28 23:22:07.434 43116 43116 I A00000/com.hx.example/Konan_main: bie ming PoiRecordItem {"requestId":"5871877323626435705","id":"7599096317080870545",...
       // ...
       04-28 23:22:07.601 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController 网络请求结束 一共耗时：176
       04-28 23:22:07.601 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController generateJCERespData：2032
       04-28 23:22:07.601 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController AES 解密 开始计时
       // ...
       04-28 23:22:07.636 43116 44052 I A03D00/com.hx.example/JSAPP: TimeStatUtils JceRequestController JSON数据转化为字符串 结束计时，一共消耗：5ms
       04-28 23:22:07.636 43116 44052 I A03D00/com.hx.example/JSAPP: JceRequestController request 成功...
       04-28 23:22:07.636 43116 44052 I A03D00/com.hx.example/JSAPP: TimeStatUtils jceServiceConsumer 请求任务返回结果
       // ...
       04-28 23:22:16.082 43116 43116 I C03F01/com.hx.example/NAPI: taskpool:: Task PerformTask End: 1284868352
       04-28 23:22:16.083 43116 43116 I A03D00/com.hx.example/JSAPP: RouteSearch TimeStatUtils jceServiceConsumer 网络请求 结束计时，一共消耗：8661 ThreadInfo: 43116 >> 43116
   ```

### 分析结论

当前运行任务执行时间过长，导致主线程阻塞，系统主动杀掉无响应应用。

### 修改建议

优化网络请求耗时，参考[网络诊断：Network分析](../harmonyos-guides/ide-profiler-network.md)，使用Profiler提供Network模板，分析请求各阶段耗时，进行对应优化。

如果优化困难，可以考虑提前将网络请求数据缓存，下次直接加载缓存数据，再通过发送网络请求二次刷新数据。

## 场景三

### 定位过程

1. 日志如下，应用出现Appfreeze，出现主线程阻塞THREAD\_BLOCK\_6异常。

   ```txt
       Version:6.9.2
       VersionCode:60902
       PreInstalled:No
       Foreground:Yes
       Pid:60292
       Uid:20020188
       Reason:THREAD_BLOCK_6S
       appfreeze: com.xxx.xxx.hos THREAD_BLOCK_6S at 20251117110638
       DisplayPowerInfo:powerState:AWAKE
   ```
2. 查看问题发生时间点主线程日志，应用创建了大量数据库连接后，系统出现文件描述符资源耗尽错误errno：24，怀疑存在数据库连接关闭异常，最终导致打开数据库chat\_customer.db失败阻塞。

   ```txt
       60292 60292 W C01650/com.xxx.xxx.hos/Rdb: ConnectionPool[Dump]: readers_ B_M_T_C[0,4,16244,0]:<6460,60292,10774><6461,60292,10773><6462,60292,10773><6463,60292,10773><6464,60292,10773><6465,60292,10772><6466,60292,10772><6467,60292,10772><6468,60292,10772><6469,60292,10772><6470,60292,10771><6471,60292,10771><6472,60292,10771><6473,60292,10771><6474,60292,10770>
       60292 60292 W C01650/com.xxx.xxx.hos/Rdb: ConnectionPool[Dump]: readers_ B_M_T_C[0,4,16244,0]:<6475,60292,10770><6476,60292,10770><6477,60292,10770><6478,60292,10770><6479,60292,10769><6480,60292,10769><6481,60292,10769><6482,60292,10769><6483,60292,10768><6484,60292,10768><6485,60292,10768><6486,60292,10768><6487,60292,10768><6488,60292,10767><6489,60292,10767>
       60292 60292 W C01650/com.xxx.xxx.hos/Rdb: ConnectionPool[Dump]: readers_ B_M_T_C[0,4,16244,0]:<6490,60292,10767><6491,60292,10767><6492,60292,10767><6493,60292,10766><6494,60292,10766><6495,60292,10766><6496,60292,10766><6497,60292,10765><6498,60292,10765><6499,60292,10765><6500,60292,10765><6501,60292,10765><6502,60292,10764><6503,60292,10764><6504,60292,10764>
       60292 60292 W C01650/com.xxx.xxx.hos/Rdb: ConnectionPool[Dump]: readers_ B_M_T_C[0,4,16244,0]:<6505,60292,10764><6506,60292,10763><6507,60292,10763><6508,60292,10763><6509,60292,10763><6510,60292,10763><6511,60292,10762><6512,60292,10762><6513,60292,10762><6514,60292,10762><6515,60292,10761><6516,60292,10761><6517,60292,10761><6518,60292,10761><6519,60292,10761>
       60292 60459 W C01719/com.xxx.xxx.hos/ffrt: 48:~WorkerThread:72 to exit, qos[3]
       60292 60292 W C01650/com.xxx.xxx.hos/LOGLIMIT: 927 line(s) dropped in a second!
       60292 60292 W C01650/com.xxx.xxx.hos/Rdb: Config[Log]: WARNING(540) Try open file readonly sysno 24 
       60292 60292 E C01650/com.xxx.xxx.hos/Rdb: Config[Log]: Error(14) errno is:24 cannot open file at line ***183 of [***3c0b.
       60292 60292 E C01650/com.xxx.xxx.hos/Rdb: Config[Log]: Error(14) errno is:24 os_unix.c:43183: (24) open(/***/el2/***/chat_customer.db.
       60292 60292 E C01650/com.xxx.xxx.hos/Rdb: SqliteConnection[OpenDatabase]: fail to open database errCode=14, dbPath=/***/el2/***/chat_customer.db, flags=65542, errno=24
   ```

### 分析结论

应用创建了大量数据库连接，系统出现文件描述符资源耗尽错误errno：24，怀疑存在数据库连接关闭异常。最终导致打开新的数据库（chat\_customer.db）链接失败阻塞。

### 修改建议

怀疑存在数据库连接池泄露，建议结合代码和场景对如下原因进行排查。

* 数据库连接未正确关闭；
* 资源管理不当；
* 连接池配置过大；
* 数据库连接超时设置不合理。

## 场景四

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是ReferenceError，引用错误类。
2. 分析上报的异常信息，大部分可在官方文档中检索到相关解释。
   * 异常信息是：Error message：@Component xxx missing @Provide property with name xxx.Fail to resolve @Consume xxx。

     ```txt
             Error name:ReferenceError
             Error message:@Component xxx missing @Provide property with name xxx. Fail to resolve @Consume xxx.
             Stacktrace:
                 at initializeConsume (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6699:1)
                 at Home (entry/src/main/ets/pages/Home.ets:6:1)
                 at anonymous (entry/src/main/ets/pages/Index.ets:154:26)
                 at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6815:1)
                 at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6842:1)
                 at anonymous (entry/src/main/ets/pages/Index.ets:154:26)
     ```
   * 异常信息是：Error message：VideoVerifyView：duplicate @Provide property with name xxx. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。

     ```txt
             Reason:ReferenceError
             Error name:ReferenceError
             Error message:VideoVerifyView: duplicate @Provide property with name xxx. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed.
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
   * 异常信息是：Error message:xxx is not initialized。

     ```txt
           Reason:ReferenceError
           Error name:ReferenceError
           Error message:PintuModel is not initialized
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (appentry|appentry|1.0.0|src/main/ets/pages/home/NewsPage.ts:174:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6813:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6840:1)
               at observedDeepRender (appentry|appentry|1.0.0|src/main/ets/pages/home/NewsPage.ts:172:1)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

* 异常信息是：Error message：@Component xxx missing @Provide property with name xxx.Fail to resolve @Consume xxx。

  初始化@Consume变量时，没有定义对应名称的@Provide变量，引用一个不存在的变量。
* 异常信息是：Error message：xxx：duplicate @Provide property with name xxx. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。

  名为xxx的@Provide属性重复。具有此名称的属性已有父组件存在。不允许重写@Provide组件。
* 异常信息是：Error message:xxx is not initialized。

  变量未初始化导致应用闪退。

### 修改建议

* 异常信息是：Error message：@Component xxx missing @Provide property with name xxx.Fail to resolve @Consume xxx。

  检查变量是否存在，若存在则在父组件中定义@Provide变量并赋值。
* 异常信息是：Error message：xxx：duplicate @Provide property with name xxx. Property with this name is provided by one of the ancestor Views already. @Provide override not allowed。

  删除/更改重复提供对应@Provide属性的代码。
* 异常信息是：Error message:xxx is not initialized。

  初始化对应的变量。

## 场景五

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是TypeError，类型错误类。
2. 分析上报的异常信息，大部分可在官方文档中检索到相关解释。
   * 异常信息是：Error message:Cannot read property xxx of undefined。(Cannot read property xxx of null和Cannot load property of null or undefined同此场景)

     ```txt
             Reason:TypeError
             Error name:TypeError
             Error message:Cannot read property loadPackage of undefined
             Stacktrace:
             Cannot get SourceMap info, dump raw stack:
               at initPageUrl (entry|entry|1.0.0|src/main/ets/h5common/page/H5Page.ts:3:1)
     ```
   * 异常信息是：Error message:is not callable。

     ```txt
           Reason:TypeError
           Error name:TypeError
           Error message:is not callable
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at forEachUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4352:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/pages/Child/CaseRepeat.ts:478:1)
     ```
   * 异常信息是：Error message:Receiver is not a JSObject。

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
   * 异常信息是：Error message:Can not get Prototype on non ECMA Object。

     ```txt
           Reason:TypeError
           Error name:TypeError
           Error message:Can not get Prototype on non ECMA Object
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (entry|entry|1.0.0|src/main/ets/com/jinbing/exampaper/module/capture/helper/ExamCameraOptHelper.ts:217:1)
     ```
   * 异常信息是：Error message:Cannot convert a illegal value to a Primitive。

     ```txt
           Reason:TypeError
           Error name:TypeError
           Error message:Cannot convert a illegal value to a Primitive
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (entry|order|1.0.0|src/main/ets/pages/source/list/OrderOften.ts:1280:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6817:1)
               at UpdateElement (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6519:1)
               at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6746:1)
               at updateDirtyElements (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6741:1)
               at rerender (entry|order|1.0.0|src/main/ets/pages/source/list/OrderOften.ts:1657:1)
     ```
   * 异常信息是：Error message:stack contains value, usually caused by circular structure。

     ```txt
           Reason:TypeError
           Error name:TypeError
           Error message:stack contains value, usually caused by circular structure
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (@xxx/bluetooth_har|@xxx/bluetooth_har|1.0.241127160422|src/main/ets/ble/Bluetooth.ts:220:75)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

* 异常信息是：Error message:Cannot read property xxx of undefined。

  变量不是预期的类型，不能调用对应的属性。
* 异常信息是：Error message:is not callable。

  变量不是预期的类型，不能调用对应的方法。
* 异常信息是：Error message:Receiver is not a JSObject。

  变量不是一个有效的javascript对象。
* 异常信息是：是Error message:Can not get Prototype on non ECMA Object。

  napi\_value超出NAPI框架的scope。
* 异常信息是：Error message:Cannot convert a illegal value to a Primitive。

  无法将非法值转换为原始类型。
* 异常信息是：Error message:stack contains value, usually caused by circular structure。

  对象存在循环引用，导致JSON序列化或深度拷贝时栈溢出。

### 修改建议

* 异常信息是：Error message:Cannot read property xxx of undefined。

  在使用变量前进行校验，检查变量是否存在对应的属性。
* 异常信息是：Error message:is not callable。

  检查变量或者this指针是否存在对应的方法。
* 异常信息是：Error message:Receiver is not a JSObject。

  检查传入对象数据是否有误，并做严格的数据校验处理报错。
* 异常信息是：Error message:Can not get Prototype on non ECMA Object。

  检查napi\_value的使用范围是否超出了napi\_handle\_scope的作用域范围。
* 异常信息是：Error message:Cannot convert a illegal value to a Primitive。

  确保对象中正确实现valueOf()或toString()方法，返回有效的原始值。
* 异常信息是：Error message:stack contains value, usually caused by circular structure。

  使用WeakSet检测和过滤循环引用，通过JSON.stringify()的replacer参数实现。

## 场景六

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是Error，自定义错误类。
2. 分析上报的异常信息，部分可在官方文档中检索到相关解释，部分为应用自行抛出的异常。
   * 异常信息是：xxx（应用代码自行抛出）。应用未处理直接抛出的异常。

     ```txt
             Reason:Error
             Error name:Error
             Error message:ApiError too_many_request: 你的请求过于频繁或服务器当前繁忙，请于一分钟后重试
             Error code:too_many_request
             Stacktrace:
             Cannot get SourceMap info, dump raw stack:
                 at ApiError (@xxx/network|@xxx/network|1.3.5|src/main/ets/ApiError.ts:4:9)
                 at intercept (@xxx/network|@xxx/network|1.3.5|src/main/ets/Request.ts:134:19)
     ```
   * 异常信息是：Invalid parameter/The parameter invalid/Invalid argument。非法参数抛出异常，需要结合栈顶代码进行具体分析。

     ```txt
             Reason:Error
             Error name:Error
             Error message:Invalid parameter
             Error code:
             Stacktrace:
             Cannot get SourceMap info, dump raw stack:
                 at anonymous (phone|@ohos/fcpush|1.0.0|src/main/ets/push/InitPushSDK.ts:94:1)
     ```
   * 异常信息是：No such file or directory。目录或文件不存在，需要结合栈顶代码进行具体分析。

     ```txt
           Uid:20020261
           Reason:Error
           Error name:Error
           Error message:No such file or directory
           Error code:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (entry|entry|1.0.0|src/main/ets/SecondaryPages/deCmpressPage.ts:102:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/SecondaryPages/deCmpressPage.ts:99:1)
               at (entry/src/main/ets/SecondaryPages/FileManagementPage2.ets:20:7)
     ```
   * 异常信息是：Init error. The WebviewController must be associated with a Web component，错误码是[17100001 WebviewController没有和具体的Web组件关联](../harmonyos-references/errorcode-webview.md#section17100001-webviewcontroller没有和具体的web组件关联)。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Init error. The WebviewController must be associated with a Web component
           Error code:17100001
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at handleBrowserBackOrExit (@xxx/madcore|@xxx/madcore|1.0.0-beta.2|src/main/ets/components/mpWebView/MpWebView.ts:339:1)
               at onWebPageClickBackItem (@xxx/madcore|@xxx/madcore|1.0.0-beta.2|src/main/ets/components/mpWebView/MpWebView.ts:335:1)
               at emitWebPageClickBackItem (@xxx/madcore|@xxx/madcore|1.0.0-beta.2|src/main/ets/components/mpWebView/MADPWebViewController.ts:31:1)
               at anonymous (@xxx/madcore|@xxx/madcore|1.0.0-beta.2|src/main/ets/pages/JsWebPage.ts:198:1)
     ```
   * 异常信息是：Invalid url，错误码是[17100002 Url格式错误](../harmonyos-references/errorcode-webview.md#section17100002-url格式错误)，无效的url。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Invalid url
           Error code:17100002
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (entry|entry|1.2.0|src/main/ets/page/webview/WebViewComponent.ts:1334:1)
               at anonymous (entry|entry|1.2.0|src/main/ets/page/webview/WebViewComponent.ts:1141:1)
     ```
   * 异常信息是：@Component xxx:ForEach id xxx: use of default id generator function not possible onprovided data structure. Need tospecify id generator function (ForEach 3rd parameter). Application Error!

     ForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '\\_\\_' + JSON.stringify(item);}，详情参考[键值生成规则](../harmonyos-guides/arkts-rendering-control-foreach.md#键值生成规则)。

     从异常信息可以看出默认的键值生成函数不能处理提供的数据结构，需要自定义键值生成函数。

     ```txt
           Error name:Error
           Error message:@Component xxx: ForEach id 104: use of default id generator function not possible on provided data structure. Need to specify id generator function (ForEach 3rd parameter). Application Error!
           Stacktrace:
               at idGenFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4341:1)
               at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4353:1)
     ```
   * 异常信息是：SQLite: Generic error。错误码是[14800021 SQLite：通用错误](../harmonyos-references/errorcode-data-rdb.md#section14800021-sqlite通用错误)。

     ```txt
           Reason:Error
           Error name:Error
           Error message:SQLite: Generic error.
           Error code:14800021
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (appentry|appentry|1.0.0|src/main/ets/common/utils/CoreDataUtil.ts:157:1)
     ```
   * 异常信息是：Column out of bounds。错误码是[14800013 列索引越界](../harmonyos-references/errorcode-data-rdb.md#section14800013-列索引越界)，列号超出范围。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Column out of bounds.
           Error code:14800013
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at queryFavoriteFile (entry|entry|1.0.0|src/main/ets/resourcesdatas/database/DJDbUtils.ts:87:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/resourcesdatas/database/DJDbUtils.ts:101:1)
     ```
   * 异常信息是：Invalid resource ID。错误码是[9001001 无效的资源id](../harmonyos-references/errorcode-resource-manager.md#section9001001-无效的资源id)，无效的资源ID。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Invalid resource ID
           Error code:9001001
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at tabName2key (home|home|1.0.0|src/main/ets/utils/ConvertUtils.ts:7:1)
               at getMenuListComp (home|home|1.0.0|src/main/ets/utils/MenuListCompUtils.ts:253:1)
               at anonymous (home|home|1.0.0|src/main/ets/components/dropdowntabs/DropdownTabs.ts:231:1)
               at setUpShowTabContents (home|home|1.0.0|src/main/ets/components/dropdowntabs/DropdownTabs.ts:230:1)
               at aboutToAppear (home|home|1.0.0|src/main/ets/components/dropdowntabs/DropdownTabs.ts:275:1)
               at (features/home/src/main/ets/view/Home.ets:293:11)
               at (products/phone/src/main/ets/pages/MainPage.ets:43:7)
     ```
   * 异常信息是：Internal error. UI execution context not found，错误码是100001，没有找到UI执行上下文。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Internal error. UI execution context not found.
           Error code:100001
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at gotoLoginPage (entry|entry|1.0.0|src/main/ets/viewmodel/login/QuickLoginManager.ts:474:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/h5common/plugin/JXPluginAlertInfo.ts:94:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/widget/dialog/CustomWindowDialog.ts:67:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/widget/dialog/CustomWindowDialog.ts:89:1)
     ```
   * 异常信息为Session not config，错误码是[7400103 会话未配置](../harmonyos-references/errorcode-camera.md#section7400103-会话未配置)。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Session not config.
           Error code:7400103
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at getFlashLight (entry|entry|1.0.0|src/main/ets/pages/model/CameraModel.ts:1664:1)
               at getFlashLight (entry|entry|1.0.0|src/main/ets/utils/TakePhotoOldUtil.ts:108:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/pages/MainPage.ts:7328:1)
     ```
   * 异常信息是：This window state is abnormal，窗口状态异常。

     ```txt
           Reason:Error
           Error name:Error
           Error message:This window state is abnormal.
           Error code:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at getMainWindowSync (/usr1/hmos_for_system/src/increment/sourcecode/foundation/window/window_manager/interfaces/kits/napi/window_runtime/window_stage_napi/window_stage.js:42:1)
               at setFullScreen (entry|entry|1.0.0|src/main/ets/entryability/EntryAbility.ts:39:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/entryability/EntryAbility.ts:21:1)
     ```
   * 异常信息是：Already closed，错误码为14800014，数据库或结果集已关闭。The RdbStore or ResultSet is already closed，RdbStore或者ResultSet对象已调用close接口关闭或者没有打开成功，相关接口无法使用。详情参考[14800014 目标实例已关闭](../harmonyos-references/errorcode-data-rdb.md#section14800014-目标实例已关闭)。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Already closed.
           Error code:14800014
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at firstNumber (phone|phone|1.0.0|src/main/ets/base/i5/s5.ts:269:1)
     ```
   * 异常信息是：Invalid relative path，错误码为9001005，无效的相对路径。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Invalid relative path
           Error code:9001005
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (phone|main|1.0.0|src/main/ets/pages/i15.ts:204:90)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8651:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8678:1)
               at anonymous (phone|main|1.0.0|src/main/ets/pages/i15.ts:197:30)
               at ifElseBranchUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:5049:1)
               at anonymous (phone|main|1.0.0|src/main/ets/pages/i15.ts:195:22)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8651:1)
               at UpdateElement (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8219:1)
               at anonymous (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8557:1)
               at updateDirtyElements (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:8552:1)
               at rerender (phone|main|1.0.0|src/main/ets/pages/i15.ts:529:14)
     ```
   * 异常信息是：Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status，当调用motion模块on、off、get接口时，服务异常，可能原因为1.系统错误，如空指针、容器相关异常；2.N-API调用异常，N-API状态无效。

     ```txt
           Reason:Error
           Error name:Error
           Error message:Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status.
           Error code:31500001
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at aboutToDisappear (entry|@xxx/home|1.0.0|src/main/ets/view/Home.ts:128:16)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

* 异常信息是：xxx（应用代码自行抛出）。应用未处理直接抛出的异常。

  业务代码逻辑问题，应用未处理异常直接抛出导致闪退。
* 异常信息是：Invalid parameter/The parameter invalid。

  非法参数抛出异常，应用未处理异常导致闪退。
* 异常信息是：No such file or directory。

  目录或文件不存在抛出异常，应用未处理异常导致闪退。
* 异常信息是：Init error. The WebviewController must be associated with a Web component。

  WebviewController还没有和具体的Web组件关联，无法进行相应的操作。
* 异常信息是：Invalid url。

  该URL对应的网页无效，或URL长度超过2048。
* 异常信息是：@Component xxx:ForEach id xxx: use of default id generator function not possible onprovided data structure. Need tospecify id generator function (ForEach 3rd parameter). Application Error!

  提供的数据结构不能被默认的键值生成函数处理。
* 异常信息是：SQLite: Generic error。

  执行SQL语句过程中出现错误。
* 异常信息是：Column out of bounds。

  当前列号超出范围[0, n - 1]，n = resultsetV9.columnCount。
* 异常信息是：Invalid resource ID。

  传入的是一个不存在的id值。
* 异常信息是：Internal error. UI execution context not found，错误码是100001。

  在上下文不明确的地方使用了全局Router变量。
* 异常信息是：Session not config。

  会话未配置之前即执行了需要会话配置的操作，导致应用闪退。
* 异常信息是：This window state is abnormal。

  操作窗口时，该窗口未创建或已被销毁。
* 异常信息是：Already closed，错误码为14800014，数据库或结果集已关闭。

  RdbStore或者ResultSet对象已调用close接口关闭或者没有打开成功，相关接口无法使用。
* 异常信息是：Invalid relative path。

  传入的相对路径有误。
* 异常信息是：Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status。

  动态感知服务状态异常，应用未捕获异常导致闪退。

### 修改建议

* 异常信息是：xxx（应用代码自行抛出）。

  应用未处理直接抛出的异常。避免出现异常场景或者使用try-catch捕获并处理异常。
* 异常信息是：Invalid parameter/The parameter invalid。

  修改异常入参，传递正确参数。
* 异常信息是：No such file or directory。

  检查目录或文件路径或者使用try-catch捕获并处理异常。
* 异常信息是：Init error. The WebviewController must be associated with a Web component。

  请检查WebviewController对象是否已与Web组件关联，可以通过onControllerAttached()接口进行检查。
* 异常信息是：Invalid url。

  请检查输入的url是否正确且url长度不超过2048。
* 异常信息是：@Component xxx:ForEach id xxx: use of default id generator function not possible onprovided data structure. Need tospecify id generator function (ForEach 3rd parameter). Application Error!

  确保提供的数据结构能被默认的键值生成函数处理或者自定义键值生成函数。
* 异常信息是：SQLite: Generic error。

  分析错误的SQL语句，找出错误点。
* 异常信息是：Column out of bounds。

  检查结果集当前列号是否超出范围。
* 异常信息是：Invalid resource ID。

  排查是否为以下场景：HAR开启混淆、中间码HAR、字节码HAR、跨HAP/HSP包。这四种场景推荐使用[getStringByName()](../harmonyos-references/js-apis-resource-manager.md#getstringbyname9)等方法通过名称获取资源。检查传入参数的资源id是否已有。
* 异常信息是：Internal error. UI execution context not found，错误码是100001。

  方法一（推荐）：使用[Navigation组件](../harmonyos-guides/arkts-navigation-navigation.md)作为应用路由框架。

  方法二（不推荐）：通过使用[Class (UIContext)](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Class (Router)](../harmonyos-references/arkts-apis-uicontext-router.md)对象，再通过该对象调用对应方法。可参考[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)中的示例。
* 异常信息是：Session not config。

  在调用需要会话配置的操作之前需要先调用[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11-1)接口配置会话。
* 异常信息是：This window state is abnormal。

  在对窗口进行操作前，检查该窗口是否存在，确保其已创建且未被销毁，再进行相关操作。
* 异常信息是：Already closed，错误码为14800014，数据库或结果集已关闭。

  重新打开RdbStore或者重新查询获取得到ResultSet，确保使用相关接口时，对象未close。
* 异常信息是：Invalid relative path。

  检查传入的相对路径是否符合预期，确保相对路径正确。
* 异常信息是：Service exception. Possible causes: 1. A system error, such as null pointer, container-related exception; 2. N-API invocation exception, invalid N-API status。

  检查motion接口的调用逻辑，排查on和off接口的参数和调用时序。

## 场景七

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是BusinessError，业务错误类。
2. 分析上报的异常信息，部分可在官方文档中检索到相关解释，部分为应用捕获后通过BusinessError抛出的异常。
   * 异常信息是：e.message: Unexpected Text in JSON: Invalid Token, e.name: SyntaxError。应用捕获SyntaxError后通过BusinessError抛出业务错误。

     ```txt
           Uid:20020303
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
   * 异常信息是：Parameter error. xxx，参数类型错误。

     The type of Parameter must be string。传入的参数类型必须是字符串。

     ```txt
           Reason:BusinessError
           Error name:BusinessError
           Error message:Parameter error. The type of Parameter must be string.
           Error code:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at c10 (@xx/push|@xx/push|1.2.0|src/main/ets/l/q.ts:1:1)
               at i17 (@xx/push|@xx/push|1.2.0|src/main/ets/u/a1/w2.ts:1:1)
               at i17 (@xx/push|@xx/push|1.2.0|src/main/ets/u/a1/c1.ts:1:1)
               at l3 (@xx/push|@xx/push|1.2.0|src/main/ets/u/a1/c1.ts:0:1)
               at setAlias (@xx/push|@xx/push|1.2.0|src/main/ets/e/g1/h1.ts:0:1)
               at setAlias (entry|entry|1.0.0|src/main/ets/common/jpush/JPushManager.ts:42:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/common/jpush/JPushManager.ts:19:1)
     ```
   * 异常信息是：Error message:unterminated entity ref。未正确转义特殊字符。

     ```txt
           Reason:BusinessError
           Error name:BusinessError
           Error message:unterminated entity ref
           Error code:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at BusinessError (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/xml/js_xml.js:19:1)
               at parse (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/xml/js_xml.js:209:1)
               at getSpecifiedText (app|utils|1.0.0|src/main/ets/utils/Strings.ts:50:1)
               at anonymous (app|main|1.0.0|src/main/ets/components/SearchImageComponent.ts:546:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6814:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6841:1)
               at h3 (app|main|1.0.0|src/main/ets/components/SearchImageComponent.ts:521:1)
     ```
   * 异常信息是：Syntax Error. Invalid Url string，错误码为10200002，非法URL字符串，parseURL传入的URL参数不符合规范。

     ```txt
           Reason:BusinessError
           Error name:BusinessError
           Error message:Syntax Error. Invalid Url string
           Error code:10200002
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at BusinessError (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/url/js_url.js:22:1)
               at parseURL (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/url/js_url.js:548:1)
               at skipToNewsDetail (entry|entry|1.0.0|src/main/ets/common/utils/SkipToNewsDetailUtils.ts:113:33)
               at anonymous (entry|entry|1.0.0|src/main/ets/pages/mine/new_mine/components/FunctionSectionCard.ts:40:64)
     ```
   * 异常信息是：Syntax Error. Invalid Uri string: xxx，非法的URI字符串。Syntax Error. Invalid Uri string: The path does not conform to the rule，此URI路径不符合规范。Syntax Error. Invalid Uri string: The #It can't be the first，#字符无法作为URI的首个字符。

     ```txt
           Reason:BusinessError
           Error name:BusinessError
           Error message:Syntax Error. Invalid Uri string: The path does not conform to the rule
           Error code:10200002
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at BusinessError (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/uri/js_uri.js:6:1)
               at URI (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/uri/js_uri.js:19:1)
               at anonymous (flutter_inappwebview_ohos|flutter_inappwebview_ohos|1.0.0|src/main/ets/components/plugin/webview/in_app_webview/InAppWebViewClient.ts:310:26)
               at anonymous (flutter_inappwebview_ohos|flutter_inappwebview_ohos|1.0.0|src/main/ets/components/plugin/webview/in_app_webview/OhosWebView.ts:208:24)
               at (../../../../../../../../../../Users/heybox/.pub-cache/git/flutter_inappwebview-87d6095fde480b06c8c9c498685945807ce453cf/flutter_inappwebview_ohos/ohos/src/main/ets/components/plugin/webview/in_app_webview/OhosWebView.ets:205:3)
     ```

     ```txt
           Reason:BusinessError
           Error name:BusinessError
           Error message:Syntax Error. Invalid Uri string: The #It can't be the first
           Error code:10200002
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at BusinessError (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/uri/js_uri.js:6:1)
               at URI (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/commonlibrary/ets_utils/js_api_module/uri/js_uri.js:19:1)
               at parseURI (appentry|appentry|1.0.0|src/main/ets/common/utils/UrlUtil.ts:282:1)
               at push (appentry|appentry|1.0.0|src/main/ets/common/utils/UrlUtil.ts:491:1)
               at anonymous (appentry|appentry|1.0.0|src/main/ets/components/IconNavigatorCOM.ts:201:1)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

* 异常信息是：e.message: Unexpected Text in JSON: Invalid Token, e.name: SyntaxError。应用捕获SyntaxError后通过BusinessError抛出业务错误。

  未处理业务错误抛出的异常导致应用闪退。
* 异常信息是：Parameter error. xxx。

  参数类型错误抛出异常，应用未处理异常导致应用闪退。
* 异常信息是：Error message:unterminated entity ref。

  未正确转义特殊字符。未正确转义XML/HTML中的特殊字符导致应用闪退。
* 异常信息是：Syntax Error. Invalid Url string。

  URL字符串格式异常导致闪退。
* 异常信息是：Syntax Error. Invalid Uri string: xxx。

  URI字符串非法导致闪退。

### 修改建议

* 异常信息是：e.message: Unexpected Text in JSON: Invalid Token, e.name: SyntaxError。应用捕获SyntaxError后通过BusinessError抛出业务错误。

  参考[堆栈轨迹分析](../harmonyos-guides/ide-release-app-stack-analysis.md)解析堆栈后结合具体代码进行分析，在异常抛出位置使用try-catch捕获并处理异常。
* 异常信息是：Parameter error. xxx。

  参考[堆栈轨迹分析](../harmonyos-guides/ide-release-app-stack-analysis.md)解析堆栈后结合具体代码进行分析，传入正确的参数类型。
* 异常信息是：Error message:unterminated entity ref。未正确转义特殊字符。

  检查解析的XML/HTML中是否包含特殊字符，对特殊字符进行转义，例如：&字符需要转义成&。
* 异常信息是：Syntax Error. Invalid Url string。

  检查URL格式是否则正确，可参考接口文档[parseURL](../harmonyos-references/js-apis-url.md#parseurl9)中的示例。
* 异常信息是：Syntax Error. Invalid Uri string: xxx。

  检查传入的URI格式是否符合规范，可参考接口文档[@ohos.uri (URI字符串解析)](../harmonyos-references/js-apis-uri.md)。

## 场景八

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是SyntaxError，语法错误类。
2. 分析上报的异常信息，大部分可在官方文档中检索到相关解释。
   * 异常信息是：Error message:Unexpected Text in JSON。这种错误通常发生在调用[JSON.parse](../harmonyos-references/js-apis-json.md#jsonparse)函数时，表示在解析JSON数据时遇到了无效的字符或格式错误。

     ```txt
           Reason:SyntaxError
           Error name:SyntaxError
           Error message:Unexpected Text in JSON: Invalid Token
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at innerJump (entry|entry|1.0.0|src/main/ets/pages/webview/YQWebView.ts:203:1)
               at innerJump (entry|base_webview|1.0.0|src/main/ets/webview/BaseJsCallNativeImpl.ts:190:1)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

字符串的格式不符合JSON语法规范。

### 修改建议

在解析JSON数据之前，检查内容是否为有效的JSON格式，避免直接解析非JSON数据或者包含特殊字符。

## 场景九

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是RangeError，边界错误类。
2. 分析上报的异常信息，大部分可在官方文档中检索到相关解释。
   * 异常信息是：Invalid array length。

     ```txt
           Uid:20020237
           Reason:RangeError
           Error name:RangeError
           Error message:Invalid array length
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at anonymous (entry|@ohos/home|1.0.0|src/main/ets/pages/medal/MyMedal/provider/MedalLikeProvider.ts:180:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:7168:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:7195:1)
               at initialRender (entry|@ohos/home|1.0.0|src/main/ets/pages/medal/MyMedal/provider/MedalLikeProvider.ts:176:1)
               at initialRenderView (/usr1/hmos_for_system/src/increment/sourcecode/out/generic_generic_arm_64only/general_all_phone_standard/obj/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/stateMgmt.js:6831:1)
               at anonymous (entry|@ohos/home|1.0.0|src/main/ets/pages/medal/MyMedal/provider/MedalProgressProvider.ts:131:1)
     ```
   * 异常信息是：Stack overflow，从故障堆栈可以看到，应用在递归调用同一个函数，直到栈空间溢出。

     ```txt
           Reason:RangeError
           Error name:RangeError
           Error message:Stack overflow!
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
               at backspaceImproved (phone|@xxxx/message|1.0.0|src/main/ets/utils/MsgRichEditorTools.ts:226:1)
               at anonymous (phone|@xxxx/message|1.0.0|src/main/ets/components/ChatInput.ts:252:1)
     ```
3. 根据堆栈对应错误代码行，排查是否存在上述问题。

### 分析结论

* 异常信息是：Invalid array length。

  数组长度为负数或超长。
* 异常信息是：Stack overflow。

  函数递归调用导致栈空间溢出。

### 修改建议

* 异常信息是：Invalid array length。

  调整数组长度。
* 异常信息是：Stack overflow。

  检查递归调用是否合理，如果合理，请将递归函数重写为循环形式避免栈空间溢出。

## 场景十

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是OutOfMemoryError，堆内存不够类。
   * 故障信息为OutOfMemory when trying to allocate 278544 bytes function name: SharedHeap::AllocateHugeObject，AllocateHugeObject内存分配函数，在尝试分配278544字节内存时，超出了大对象空间阈值。

     ```txt
           Reason:OutOfMemoryError
           Lifetime: 0.000000s
           Js-Engine: ark
           Error message: OutOfMemory when trying to allocate 278544 bytes function name: SharedHeap::AllocateHugeObject
           Cannot get SourceMap info, dump raw stack:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at info (entry/build/default/cache/default/default@CompileArkTS/esmodule/release/common/src/main/ets/utils/Logger.ts:10:10)
               at anonymous (entry/build/default/cache/default/default@CompileArkTS/esmodule/release/common/src/main/ets/utils/persistence/KvStore.ts:90:90)
     ```
   * 故障信息为OutOfMemory when trying to allocate 40 bytes function name: Heap::AllocateYoungOrHugeObject，AllocateYoungOrHugeObject内存分配函数，在尝试分配仅40字节内存时，超出了年轻代或大对象空间阈值。

     ```txt
           Reason:OutOfMemoryError
           page: pages/Index.js
           Error message: OutOfMemory when trying to allocate 40 bytes function name: Heap::AllocateYoungOrHugeObject
           Cannot get SourceMap info, dump raw stack:
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at ObservedPropertyObjectPU (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:0:1)
               at SynchedPropertyOneWayPU (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:5434:1)
               at SynchedPropertyObjectOneWayPU (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:0:1)
               at LgPortrait (@xxx/lego-widget-core|@xxx/lego-widget-core|5.44.1-20250829.141541|src/main/ets/components/display/LgPortrait.ts:30:26)
               at anonymous (entry|@xxx/chat|0.1.0|src/main/ets/pages/conversation/ConversationItem.ts:65:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6817:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6844:1)
               at anonymous (entry|@xxx/chat|0.1.0|src/main/ets/pages/conversation/ConversationItem.ts:63:1)
               at ifElseBranchUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4300:1)
               at anonymous (entry|@xxx/chat|0.1.0|src/main/ets/pages/conversation/ConversationItem.ts:61:1)
               at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6817:1)
               at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:6844:1)
               at ConversationItemBuilder (entry|@xxx/chat|0.1.0|src/main/ets/pages/conversation/ConversationItem.ts:21:1)
               at deepRenderFunction (entry|@xxx/chat|0.1.0|src/main/ets/pages/conversation/ConversationPage.ts:658:1)
     ```
2. 应用分配内存时出现堆内存溢出，老年代和大对象空间初始化时均设定为Heap剩余未分配空间的大小，默认手机设备主线程OldSpaceSize上限接近350MB。应用分配的内存超过了350M导致出现OOM。详情可见[Heap结构及其配置参数](../harmonyos-guides/gc-introduction.md#heap)。
3. 找到稳定复现场景，通过[Snapshot分析模板](../harmonyos-guides/ide-insight-session-snapshot.md)拍摄内存快照，对比操作前后的内存快照，找到泄漏对象。

### 分析结论

应用内存溢出，分配的内存超过空间上限。

### 修改建议

* 如果内存溢出的堆栈一致，说明调用栈是个高频调用并且可能存在内存泄漏，结合具体代码进行分析。
* 如果内存溢出的堆栈不一致，通过[Snapshot分析模板](../harmonyos-guides/ide-insight-session-snapshot.md)分析泄漏对象，修复内存溢出问题。

## 场景十一

### 定位过程

1. 从faultlogger目录下获取到应用的JS Crash故障日志，故障类型是URIError，URI错误类。
2. 分析上报的异常信息，大部分可在官方文档中检索到相关解释。
   * 异常信息是：DecodeURI: invalid character：xxx。在调用DecodeURI函数时发现URL无效抛出异常。

     ```txt
           Reason:URIError
           Error name:URIError
           Error message:DecodeURI: invalid character: xxx
           Stacktrace:
           Cannot get SourceMap info, dump raw stack:
               at downFile (entry|entry|1.0.0|src/main/ets/util/FileDownloadUtil.ts:8:1)
               at startReadFile (entry|entry|1.0.0|src/main/ets/components/TDWebview.ts:745:1)
               at readClick (entry|entry|1.0.0|src/main/ets/components/TDWebview.ts:186:1)
               at anonymous (entry|entry|1.0.0|src/main/ets/components/TDWebview.ts:1433:1)
     ```

### 分析结论

URL无效，DecodeURI函数抛出异常导致应用闪退。

### 修改建议

检查URL，确保使用的URL真实有效，使用try-catch捕获并处理异常。
