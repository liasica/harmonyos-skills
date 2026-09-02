---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-6
title: 应用点击某功能时卡死无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用点击某功能时卡死无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2f15324dc7bf8bef27226c698e1d8d2c3182737b79b4d19a418aab75b07dd85
---

## 问题现象

当用户点击某功能时，应用出现卡死或无响应的情况。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。

## 问题定位

1. 在faultlogger目录下查找appfreeze-应用包名-应用UID-年月日时分秒文件，从appfreeze日志文件中可以看出当前故障模块进程号，故障原因和故障发生的时间点。

   ```screen
   Device info:HUAWEI Mate 60 Pro
   Build info:ALN-AL80 5.0.0.120(C00E120R4P22log)
   Fingerprint:18aafb2df482759a871eb6e36316a0b0def9ee4531e2f1520f1b8142dfa23ff3
   Module name:com.hx.example
   Version:12.11.20
   VersionCode:108
   PreInstalled:No
   Foreground:Yes
   Pid:29060 // 故障模块进程号
   Uid:20020048
   Reason:APP_INPUT_BLOCK // 故障原因
   appfreeze: com.hx.example APP_INPUT_BLOCK at 20241219211304 // 故障发生的时间点
   ```
2. 查看主线程堆栈，可以看出主线程在等锁。

   ```screen
   EVENTNAME = APP_INPUT_BLOCK
   TIMESTAMP = 2024/12/19-21:13:04:402
   PID = 29060
   UID = 20020048
   TID = 29060
   PACKAGE_NAME = com.hx.example
   PROCESS_NAME = 进程名
   eventLog_action = t:input,t,cmd:c,cmd:dam,tr,k:SysRqFile
   eventLog_interval = 10
   MSG = 
   Fault time:2024/12/19-21:12:59
   User input does not respond!
   Timestamp:2024-12-19 21:13:00:264
   Tid:29060, Name:com.hx.example
   #00 pc 00000000001b6698 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(c05a4bdaf3657c3186f06e417c4fa802)
   #01 pc 00000000001bc6b0 /system/lib/ld-musl-aarch64.so.1(__pthread_mutex_timedlock_inner+592)(c05a4bdaf3657c3186f06e417c4fa802)
   #02 pc 00000000000c3ed8 /system/lib64/libc++.so(std::__h::mutex::lock()+8)(a2d45389edece3475c17a1d7fc9a76ec2b697825)
   #03 pc 0000000000022f48 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventQueueBase::GetEvent()+68)(bc66f21977d068489b7eb89fc0f782f1)
   ```
3. 搜索关键字"catcher cmd: hilog -z 1000 -P "，查看最近1000条流水日志。

   ```screen
   12-19 21:12:52.553 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.569 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.569|Func:--|Line:0|Module:KrnInit|Tag:ReactNative|Q:|Msg:notifyNativeGestureStarted view = [object Object] event = [object Object]
   12-19 21:12:52.569 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.570 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.586 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.586|Func:--|Line:0|Module:KrnInit|Tag:ReactNative|Q:|Msg:notifyNativeGestureStarted view = [object Object] event = [object Object]
   12-19 21:12:52.586 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.586 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.618 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.618|Func:--|Line:0|Module:KrnInit|Tag:ReactNative|Q:|Msg:notifyNativeGestureStarted view = [object Object] event = [object Object]
   12-19 21:12:52.618 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.618 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.623 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.623|Func:--|Line:0|Module:KrnInit|Tag:ReactNative|Q:|Msg:notifyNativeGestureStarted view = [object Object] event = [object Object]
   12-19 21:12:52.623 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.623 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.642 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.642|Func:--|Line:0|Module:KrnInit|Tag:ReactNative|Q:|Msg:notifyNativeGestureStarted view = [object Object] event = [object Object]
   12-19 21:12:52.642 29060 29060 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.642 29060 29060 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.679 29060 29246 I A06666/com.hx.example/[OBIWAN_LOG]: I|2024-12-19 21:12:52.679|Func:TaskEntry|Line:44|Module:Aemon|Tag:AnoleLog|Q:|Msg:[1] VideoDetectTask[1]: VideoDetectTask Monitor loop each 500ms.
   12-19 21:12:52.679 29060 29246 I A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.679 29060 29246 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.679 29060 29246 W A06666/com.hx.example/[OBIWAN_LOG]: W|2024-12-19 21:12:52.679|Func:TaskEntry|Line:85|Module:Aemon|Tag:AnoleLog|Q:|Msg:[1] VideoDetectTask[1]: DecoderBlockMonitor player state:3, do nothing.
   12-19 21:12:52.679 29060 29246 W A06666/com.hx.example/[OBIWAN_LOG]:  
   12-19 21:12:52.679 29060 29246 W A06666/com.hx.example/[KSCOBW_INNERLOG]: handleLogMessageData 在执行 
   12-19 21:12:52.679 29060 29246 I A06666/com.hx.example/[OBIWAN_LOG]: I|2024-12-19 21:12:52.679|Func:UpdateInfo|Line:922|Module:Aemon|Tag:AnoleLog|Q:|Msg:[1] CicaiMaxbufControl[0]: ::UpdateInfo
   12-19 21:12:52.679 29060 29246 I A06666/com.hx.example/[OBIWAN_LOG]:
   ```
4. 从流水日志可以看出应用在卡死阶段频繁地执行业务，导致用户输入得不到响应。

## 分析结论

频繁执行业务导致输入无响应。

## 修改建议

降低业务执行频次，或将其放到子线程执行，参考文档[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)。
