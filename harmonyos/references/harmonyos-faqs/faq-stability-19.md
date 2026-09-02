---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-19
title: 后台播放音乐或者录音时，应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 后台播放音乐或者录音时，应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:efb6300680789d13ee03a4c82ef279180ad4249d37c02ed573ef93600f9c372c
---

## 问题现象

应用在播放音乐或者录音时，退出到后台，过了一段时间应用闪退。

## 背景知识

* PROCESS\_KILL是因为各种原因（如应用内存超限、运行锁异常等）导致应用被操作系统强制停止。
* 当前支持的PROCESS\_KILL问题种类可以参考[分析PROCESS KILL问题](../app/agc-help-apms-appterminate-0000002577580566.md)。

## 场景一

### 问题定位

在hilog日志中搜索关键字kill Reason，从日志中可以看出终止原因是ILLEGAL\_AUDIO\_RENDERER\_BY\_SUSPEND，后台非法播放音频。

```txt
11-20 08:11:21.059   921 29517 W C01713/resource_schedule_service/SUSPEND_MANAGER: [(ReportKillAppEvent):267] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=30627, processName=com.hx.example, msg=Kill Reason:ILLEGAL_AUDIO_RENDERER_BY_SUSPEND
11-20 08:11:21.060   921 29517 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(IsKillAppWhenIllegalUseAudio):239] Application 20020177_com.hx.example_[30627,31442,] current has media and not apply background_task or Resource::AUDIO
11-20 08:11:21.060   921 29517 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(KillApplicationByUid):171] kill running application, app name is com.hx.example, uid is 20020177
```

### 分析结论

后台非法播放音频导致应用被系统终止。

### 修改建议

参考[后台播放](../harmonyos-guides/avsession-background-scene.md)申请长时任务播放音频，禁止不操作或写入静音数据等恶意行为。

## 场景二

### 问题定位

在hilog日志中搜索关键字kill Reason，从日志中可以看出终止原因是ILLEGAL\_AUDIO\_CAPTURER\_BY\_SUSPEND，错误信息是current has media and not apply background\_task or Resource::AUDIO，表示应用当前正在使用媒体资源，但没有申请background\_task或Resource::AUDIO权限。

```txt
04-24 20:51:29.264   998  2232 W C01713/resource_schedule_service/SUSPEND_MANAGER: [(ReportKillAppEvent):277] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=64424, processName=com.hx.example, msg=Kill Reason:ILLEGAL_AUDIO_CAPTURER_BY_SUSPEND, foreground=0
04-24 20:51:29.264  3674  3674 I A01B05/com.ohos.sceneboard/AOD: AodSettingsModule --> Check isInTimeRange, currentTime: 1745499089264, startTime: 1745449200000, endTime: 1745506800000
04-24 20:51:29.264   998  2232 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(IsKillAppWhenIllegalUseAudio):248] Application 20020222_com.hx.example_[64424] current has media and not apply background_task or Resource::AUDIO
04-24 20:51:29.264   998  2232 I C01713/resource_schedule_service/SUSPEND_MANAGER: [(KillApplicationByUid):178] kill running application, app name is com.hx.example, uid is 20020222
```

### 分析结论

后台非法录音导致应用被系统终止。

### 修改建议

应用退出到后台时停止录音或者申请录制[长时任务](../harmonyos-guides/continuous-task.md)。

## 场景三

### 问题定位

在hilog日志中搜索关键字kill Reason，从日志中可以看出终止原因是Power Save Clean。而且能搜到不止一个应用被省电终止，播放音频的应用只是其中之一。

```txt
02-05 12:47:03.045  1527  2449 I C01336/foundation/AMS: [app_exit_reason_data_manager.cpp:272]value: {"ability_list":[],"exit_msg":"Kill Reason:Power Save Clean","reason":6,"time_stamp":1738730823045}
02-05 12:47:03.045  1527  2449 I C01630/foundation/DistributedDB: Write timestamp:3170987308230454770 timestamp:3170987308230454770, flag:2 modifyTime:17387308230454780 createTime:17387308230454780
02-05 12:47:03.046  1527  2449 I C01336/foundation/AMS: [app_exit_reason_data_manager.cpp:220]current bundle name: com.hx.example, tokenId:<private>, reason: 6,  exitMsg: Kill Reason:Power Save Clean, abilityName:EntryAbility isSetReason:1
02-05 12:47:03.046  1527  2449 I C01630/foundation/DistributedDB: Write timestamp:3170987308230464410 timestamp:3170987308230464410, flag:3 modifyTime:17387308230464411 createTime:17387308230464411
```

### 分析结论

设备因电量低，开启了省电策略，导致后台应用被终止。

### 修改建议

在设备低电量时及时充电，或保持充足电量。
