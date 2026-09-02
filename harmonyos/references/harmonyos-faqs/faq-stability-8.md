---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-8
title: 应用在启动加载时，卡死无响应后闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在启动加载时，卡死无响应后闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:070a1774be02f37f8f3744c5bc059dd43421b6cfc0fefc5c2d74eafcb0941d73
---

## 问题现象

冷启动应用，卡在LOGO页面加载，卡死无响应，然后异常闪退。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* LIFECYCLE\_TIMEOUT生命周期切换超时是指UIAbility生命周期切换超时。通过获取不同生命周期切换的过程，在生命周期切换开始的位置向watchdog线程插入超时任务，在生命周期切换完成之后移除超时任务，固定时间内未成功移除将上报故障。
* LIFECYCLE\_TIMEOUT的sysfreeze日志中，除了故障时的阻塞信息block，还有半周期检测信息warning，日志根据时间先打印warning的信息，后打印block信息，半周期检测的EVENTNAME为LIFECYCLE\_HALF\_TIMEOUT。

## 问题定位

1. 应用在启动阶段卡死或前后台切换时卡死，首先排查是否发生了LIFECYCLE\_TIMEOUT故障，查看faultlogger目录下，有无生成sysfreeze-应用包名的故障日志。
2. 观察sysfreeze日志的基本信息，故障位置是EntryAbility的Foreground生命周期超时EntryAbility foreground timeout.，故障原因Reason为LIFECYCLE\_TIMEOUT，故障模块进程号Pid为58538，故障上报时间在22分4秒，根据Foreground生命周期超时检测阈值为5s，由此也可以推断故障开始时间在21分59秒。

   ```shell
   Foreground:Yes
   Pid:58538
   Uid:20020182
   Reason:LIFECYCLE_TIMEOUT
   sysfreeze: com.example.xxx LIFECYCLE_TIMEOUT at 20250415172204
   DisplayPowerInfo:powerState:AWAKE
   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
   DOMAIN:AAFWK
   STRINGID:LIFECYCLE_TIMEOUT
   TIMESTAMP:2025/04/15-17:22:04:290
   PID:58538
   UID:20020182
   PACKAGE_NAME:com.example.xxx
   PROCESS_NAME:com.example.xxx
   *******************************************
   start time: 2025/04/15-17:22:01:711
   DOMAIN = AAFWK
   EVENTNAME = LIFECYCLE_HALF_TIMEOUT
   TIMESTAMP = 2025/04/15-17:22:01:703
   PID = 58538
   UID = 20020182
   TID = 58538
   PACKAGE_NAME = com.example.xxx
   PROCESS_NAME = com.example.xxx
   eventLog_action = pb:1:r,t
   eventLog_interval = 10
   MSG = 
   Fault time:2025/04/15-17:22:01
   ability:EntryAbility foreground timeout.
   ```

3. 排查主消息任务队列(EventHandler)是否有异常，日志中搜索"mainHandler dump is"，能得到两个结果，其中前面的是半周期检测时的信息。

   查看当前任务已运行时长，排查是否阻塞：dump begin curTime - trigger time，得出block时长5s，大于等于故障检测时长5s。且发现warning和block在执行的当前任务相同，证明此任务阻塞了的当前线程。

   * warning：LIFECYCLE\_HALF\_TIMEOUT。

     ```shell
     mainHandler dump is:
      EventHandler dump begin curTime: 2025-04-15 05:22:01.531
      Event runner (Thread name = , Thread ID = 58538) is running
      Current Running: start at 2025-04-15 05:21:59.031, Event { send thread = 58680, send time = 2025-04-15 05:21:59.031, handle time = 2025-04-15 05:21:59.031, trigger time = 2025-04-15 05:21:59.031, task name = UIAbilityThread:AbilityTransaction, caller = [ui_ability_thread.cpp(ScheduleAbilityTransaction:345)] }
     ```
   * block：LIFECYCLE\_TIMEOUT。

     ```shell
     mainHandler dump is:
      EventHandler dump begin curTime: 2025-04-15 05:22:04.031
      Event runner (Thread name = , Thread ID = 58538) is running
      Current Running: start at 2025-04-15 05:21:59.030, Event { send thread = 58680, send time = 2025-04-15 05:21:59.030, handle time = 2025-04-15 05:21:59.030, trigger time = 2025-04-15 05:21:59.030, task name = UIAbilityThread:AbilityTransaction, caller = [ui_ability_thread.cpp(ScheduleAbilityTransaction:345)] }
     ```

4. 排查主线程堆栈，日志搜索"Tid:应用进程号，Name:应用包名"，可以搜到如下两个堆栈。观察到两个堆栈一致，说明主线程发生了卡死，问题出在栈顶libhilog.so库。
   * warning栈：LIFECYCLE\_HALF\_TIMEOUT。

     ```shell
     Tid:58538, Name:xxx
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
   * block栈：LIFECYCLE\_TIMEOUT。

     ```shell
     Tid:58538, Name:xxx
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
5. 排查sysfreeze日志中抓取的hilog日志信息，搜索"catcher cmd: hilog -z 1000 -P"。

   发现应用一直在循环输出打印相同的内容，说明发生了死循环或重复调用，导致应用超时，启动失败。

   ```shell
   catcher cmd: hilog -z 1000 -P 
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.130 58538 58538 W A03D00/com.example.xxx/HiLog: write socket failed, 17 line(s) dropped!
   04-15 17:22:05.131 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   04-15 17:22:05.131 58538 58538 W A03D00/com.example.xxx/HiLog: write socket failed, 2 line(s) dropped!
   04-15 17:22:05.131 58538 58538 I A03D00/com.example.xxx/JSAPP: 阻塞
   ```

## 分析结论

应用在Foreground生命周期中，执行了死循环或耗时操作，导致卡死闪退。

## 修改建议

* 尽量减少生命周期函数的加载内容，不要在其中做耗时操作，如果非必要，尽量采用异步加载。
* 请求云侧数据需要验证充分，充分考虑有网、弱网、无网的场景。
