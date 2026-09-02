---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-28
title: 应用启动时一直闪退，无法打开
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用启动时一直闪退，无法打开
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5e0c34cc9da5d65864e007b3290ed7cd8028ac00ff470c175b25195585009117
---

## 问题现象

应用启动就会出现闪退，一直无法打开。

## 背景知识

* 近场通信(Near Field Communication，NFC)是一种短距高频的无线电技术，在13.56MHz频率运行，通信距离一般在10厘米范围内。
* [HCE](../harmonyos-guides/nfc-hce-guide.md)(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，电子设备上的应用程序模拟NFC卡片和NFC读卡器通信，实现NFC刷卡业务。
* [3100301 NFC卡模拟状态异常](../harmonyos-references/errorcode-nfc.md#section3100301-nfc卡模拟状态异常)：NFC服务执行卡模拟业务逻辑遇到错误。
* CppCrash进程崩溃检测基于操作系统信号机制，目前支持的崩溃信号参考[Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md)。
* CppCrash日志规格说明可以参考[日志规格](../harmonyos-guides/cppcrash-guidelines.md#日志规格)说明。

* JS Crash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JS Crash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。

## 问题定位

### 场景一

1. 在hilog日志中搜索关键字kill Reason，找到应用的进程号10300对应的终止记录，可以看到应用被终止的原因是OnRemoteDied。

   ```txt
   05-09 20:40:40.407   952  1197 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(RemoveProcess):463] remove process 20020043_应用包名_10300, processNum: 0
   05-09 20:40:40.407  1547 11114 I C01311/foundation/AppMS: [app_mgr_service_inner.cpp:2679]kill reason=OnRemoteDied, pid=10300
   05-09 20:40:40.407   623 13474 I C02C03/PARAM_WATCHER: [watcher_manager.cpp:504]Agent died 972 10300
   ```
2. 从kill Reason日志向上查找关键字OnRemoteDied，可以看到错误日志是hce on remote died，错误码是3100301。

   ```txt
   05-09 20:40:40.407 11311 11336 E C00301/nfc_service/Nfc_Core: [(UnRegAllCallback:92)]hce is null
   05-09 20:40:40.407   623 13474 W C057C2/param_watcher/IPCObjectProxy: SendObituary 513: handle:51 desc:*.IWatcher 2665647552
   05-09 20:40:40.407 11311 11336 I C00301/nfc_service/Nfc_Core: [(OnRemoteDied:35)]OnRemoteDied, UnRegAllCallback ret=3100301
   05-09 20:40:40.407 11311 11336 E C00301/nfc_service/Nfc_Core: [(RemoveHceDeathRecipient:335)]hce on remote died
   ```
3. 通过错误码可以判断应用注册HCE前未检测设备是否打开NFC。

### 场景二

1. 查看faultlogger目录下的CppCrash崩溃日志，故障原因是SIGABRT，进程异常终止，LastFatalMessage为Unexpected call: exit(-1)，发生了未预期的exit退出函数调用。

   ```txt
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317c0400007129 from:28969:20020228
   LastFatalMessage:[appspawn_server.c:57]Unexpected call: exit(-1)
   ```
2. 排查堆栈，栈顶是libappspawn\_helper.z.so中exit函数调用了abort函数终止了进程，而exit函数是下一个栈帧libjiagu.so中调用，需要梳理动态库中直接调用exit的业务场景，分析是否有必要直接exit。

   ```txt
   Fault thread info:
   Tid:29027, Name:com.hx.example
   #00 pc 000000000019ca00 /system/lib/ld-musl-aarch64.so.1(raise+228)(f77c0346c0084ebbadf721ea319f5f77)
   #01 pc 0000000000149b70 /system/lib/ld-musl-aarch64.so.1(abort+20)(f77c0346c0084ebbadf721ea319f5f77)
   #02 pc 0000000000001ca4 /system/lib64/libappspawn_helper.z.so(exit+144)(1f3a93bc50a79f539e4c02b5b88b2ee9)
   #03 pc 000000000001dd84 /data/storage/el1/bundle/libs/arm64/libjiagu.so(e2e257836d5f3479377e680f3812454d0cd87a0e)
   #04 pc 00000000001bdcac /system/lib/ld-musl-aarch64.so.1(start+236)(f77c0346c0084ebbadf721ea319f5f77)
   ```

### 场景三

1. 从faultlogger目录下获取到应用的SysFreeze和JS Crash故障日志，SysFreeze故障原因为LIFECYCLE\_TIMEOUT，搜索崩溃栈，关键字TID:进程ID(PID)，观察到半周期堆栈里有清晰的业务调用信息，阻塞堆栈中信息不完整，Failed to dump，原因是process is dumping当前进程已经在dump当中。

   ```txt
   // LIFECYCLE_HALF_TIMEOUT半周期检测堆栈
   Tid:42239, Name:com.hx.example
   #00 pc 000000000007ae88 /data/storage/el1/bundle/libs/arm64/libapplogrs.so
   #01 pc 000000000007ae74 /data/storage/el1/bundle/libs/arm64/libapplogrs.so
   #02 pc 0000000000e12868 /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+40)
   #03 pc 000000000038959c /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis1Imm8V8V8WithProf+1060)
   #04 at init (xxx|@dp/applog|1.2.16|src/main/ets/AppLogInstance.ts:114:1)
   #05 at initAppLog (xxx|@xxx/applog|1.0.0|src/main/ets/b60.ts:46:1)
   #06 at run (xxx|xxx|1.0.0|src/main/ets/y179/k58/g181.ts:11:1)
   #07 at runSyncTask (xxx|@hpaas/ez_launch_task|4.2.55|src/main/ets/LaunchTaskScheduler.ts:132:1)
   #08 at runTasks (xxx|@hpaas/ez_launch_task|4.2.55|src/main/ets/LaunchTaskScheduler.ts:50:1)
   #09 at confirmStage (xxx|@hpaas/ez_launch_task|4.2.55|src/main/ets/LaunchTaskScheduler.ts:42:1)
   #10 at onUIAbilityCreate (xxx|xxx|1.0.0|src/main/ets/y179/z179.ts:63:1)
   #11 at onCreate (xxx|xxx|1.0.0|src/main/ets/xxxability/DcarUIAbility.ts:77:1)
   // LIFECYCLE_TIMEOUT阻塞堆栈
   Failed to dump normal stacktrace for 42239
   Reason:
   normal stack:process is dumping
   Tid:42239, Name:com.hx.example
   #00 pc 000000000007ce1c /data/storage/el1/bundle/libs/arm64/libapplogrs.so
   #01 pc 0000000000e12868 /system/lib64/module/arkcompiler/stub.an
   #02 pc 000000000038959c /system/lib64/module/arkcompiler/stub.an
   ```
2. 从mainHandler主线程任务队列信息中观察到，当前执行任务并没有改变，并且两个堆栈中stub.an的指令地址相同，所以可以确定两个的堆栈业务是一致的，应用函数执行时间过长。

   ```txt
   // LIFECYCLE_HALF_TIMEOUT半周期检测堆栈
   mainHandler dump is:
   EventHandler dump begin curTime: 2025-11-08 14:13:52.248
   Event runner (Thread name = , Thread ID = 42239) is running
   Current Running: start at 2025-11-08 14:13:49.750, Event { send thread = 42281, send time = 2025-11-08 14:13:49.742, handle time = 2025-11-08 14:13:49.742, trigger time = 2025-11-08 14:13:49.750, task name = UIAbilityThread:AbilityTransaction, caller = [ui_ability_thread.cpp(ScheduleAbilityTransaction:339)] }
   // LIFECYCLE_TIMEOUT阻塞堆栈
   mainHandler dump is:
   EventHandler dump begin curTime: 2025-11-08 14:13:54.771
   Event runner (Thread name = , Thread ID = 42239) is running
   Current Running: start at 2025-11-08 14:13:49.749, Event { send thread = 42281, send time = 2025-11-08 14:13:49.742, handle time = 2025-11-08 14:13:49.742, trigger time = 2025-11-08 14:13:49.749, task name = UIAbilityThread:AbilityTransaction, caller = [ui_ability_thread.cpp(ScheduleAbilityTransaction:339)] }
   ```
3. SysFreeze阻塞堆栈的process is dumping与JS Crash崩溃有关，进程正是在dump jscrash的日志，随后进程因JS Crash终止，所以SysFreeze阻塞栈导出异常。

   ```txt
   11-08 14:13:52.381  1571 41366 I C02D11/foundation/DfxDumpCatcher: Receive DumpCatch request for cPid:(1571), pid(42239)
   11-08 14:13:52.381  1571 41366 I C02D11/foundation/DfxFaultLogger: FAULT_LOGGERD_CLIENT.RequestSdkDump :: pid: 42239, tid: 0, isJson: 1.
   11-08 14:13:52.383   575   575 I C02D11/DfxFaultLogger: FAULT_LOGGER_SERVER :: faultloggerd.sdkdump.server has processed request for pid: 1571, clientType: 1, and retCode 0
   11-08 14:13:52.546 42544 42544 I C02D11/DfxFaultLogger: Start main function of processdump
   11-08 14:13:52.718   575   575 I C02D11/DfxFaultLogger: FAULT_LOGGER_SERVER :: faultloggerd.crash.server receive request from pid: 42544, clientType: 2
   11-08 14:13:52.718 42544 42544 I C02D11/DfxFaultLogger: unwind key thread dump start
   11-08 14:13:52.718 42544 42544 I C02D11/DfxFaultLogger: GetKeyThreadStack, unwind tid(42239) start.
   11-08 14:13:52.718   575   575 I C02D11/DfxFaultLogger: FAULT_LOGGER_SERVER :: faultloggerd.crash.server has processed request for pid: 42544, clientType: 2, and retCode 0
   // ...
   11-08 14:13:54.965  1571 38090 I C02D11/foundation/DfxDumpCatcher: Receive DumpCatch request for cPid:(1571), pid(42239)
   11-08 14:13:54.965  1571 38090 I C02D11/foundation/DfxFaultLogger: FAULT_LOGGERD_CLIENT.RequestSdkDump :: pid: 42239, tid: 0, isJson: 1.
   11-08 14:13:54.966   575   575 I C02D11/DfxFaultLogger: FAULT_LOGGER_SERVER :: faultloggerd.sdkdump.server receive request from pid: 1571, clientType: 1
   11-08 14:13:54.966   575   575 I C02D11/DfxFaultLogger: Receive dump request for pid:42239 tid:0.
   11-08 14:13:54.966   575   575 E C02D11/DfxFaultLogger: FAULT_LOGGER_SERVICE :: pid(42239) is dumping, break.
   11-08 14:13:54.966   575   575 I C02D11/DfxFaultLogger: FAULT_LOGGER_SERVER :: faultloggerd.sdkdump.server has processed request for pid: 1571, clientType: 1, and retCode 5
   ```
4. 查看JS Crash日志，发现异常原因是主窗调用[getWindowProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)时，未能获取到窗口属性。

   ```txt
   Reason:Error
   Error name:Error
   Error message:[window][getWindowProperties]msg: get property info failed
   Error code:1300002
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at calcInitScreenSize (xxx|@xxx/utils|1.0.0|src/main/ets/x/y.ts:141:1)
       at initAndRegisterWindowSizeChange (xxx|@xxx/utils|1.0.0|src/main/ets/x/y.ts:159:1)
       at anonymous (xxx|xxx|1.0.0|src/main/ets/xxxability/DcarUIAbility.ts:179:1)
   ```
5. SysFreeze和JsCrash是同步发生，顺序应该是应用启动卡在onCreate->foregroundTimeout超时->sessionException->触发主窗口销毁->应用调用到getWindowProperties产生JS Crash问题。

   ```txt
   11-08 14:13:54.727  1571 34260 W C01336/foundation/AMS: [UALM1691]LIFECYCLE_TIMEOUT: uid: 20020200, pid: 42239, bundleName: com.hx.example, abilityName: DcarAbility, msg: ability:DcarAbility foreground timeout.
   11-08 14:13:54.769  1571 34260 I C01336/foundation/AMS: [UALM2175]scb call, NotifySCBToHandleException reason: handleForegroundTimeout
   11-08 14:13:54.772  3055  3055 I A04200/com.ohos.sceneboard/WINDOW: SCBSceneSession: on sessionException errorReason: handleForegroundTimeout, shouldSkipKillInStartup: false, needRemoveSession: false needClearCallerLink: true
   11-08 14:13:54.800  3055  3055 I A04200/com.ohos.sceneboard/WINDOW: SCBSpecificScenePanelViewModel --> onDestroyFloatWindowFromSceneSession
   11-08 14:13:54.806  3055  3400 I C04217/com.ohos.sceneboard/WMSAttribute: WindowDestroyNotifyVisibility: in, wid: 66, RSVisible: 0, WindowMode: 1
   11-08 14:13:55.849 42239 42239 W C03F00/com.hx.example/ArkCompiler: [default] [CallForNapi:3949] occur exception need return
   11-08 14:13:55.849 42239 42239 W C03F01/com.hx.example/NAPI: [napi_call_function] pending exception when js function called, print exception info: 
   11-08 14:13:55.849 42239 42239 E C03F00/com.hx.example/ArkCompiler: Error: [window][getWindowProperties]msg: get property info failed
   11-08 14:13:55.850  1571  1571 I C01336/foundation/AMS: [app_exit_reason_helper58]not record extension reason: 2097247
   11-08 14:13:55.850  1571  1571 E C01336/foundation/AMS: [app_exit_reason_helper71]abilityLists empty
   ```

## 分析结论

### 场景一

注册HCE前未检测设备是否打开NFC，接口抛出异常导致应用闪退。

### 场景二

应用主动调用exit()函数终止进程。

### 场景三

函数执行时间过长，导致主线程超时卡死。

## 修改建议

### 场景一

注册HCE前使用[nfcController.isNfcOpen](../harmonyos-references/js-apis-nfccontroller.md#nfccontrollerisnfcopen)先判断NFC状态，NFC未打开时，通过弹窗提示用户前往设置中心打开NFC。

### 场景二

程序正常运行过程中，直接调用exit或abort强制终止程序，可能会造成内存泄漏，不建议使用，而是应当抛出相关异常错误码。

### 场景三

参考文档[主线程耗时操作优化](../best-practices/bpta-time-optimization-of-the-main-thread.md)，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。
