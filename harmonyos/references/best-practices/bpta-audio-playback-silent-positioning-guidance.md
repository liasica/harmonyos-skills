---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-playback-silent-positioning-guidance
title: 音频播放无声问题定位指导
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > 音频播放无声问题定位指导
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:5405ca493d682705bf7dbf9219d4e69e5d2881972b694d3da5b44c1ce7fc7861
---

## 概述

音频播放无声问题主要体现在以下几种场景：起播无声、异常中断无声、音量异常导致无声、前后台切换和长时任务异常导致无声等。本文通过[hilog日志采集](bpta-audio-playback-silent-positioning-guidance.md#section1220784418913)、[hilog日志分析](bpta-audio-playback-silent-positioning-guidance.md#section57673159105)，并结合[典型案例](bpta-audio-playback-silent-positioning-guidance.md#section6541633161814)帮助开发者定位音频播放无声问题。

音频渲染流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/FKPRUlwOQlCAhtp_cxNjqw/zh-cn_image_0000002703506142.png "点击放大")

* 应用（Application）：用户或上层软件发起音频播放请求的起点。
* AudioRenderer：应用层的音频渲染接口，负责将音频数据传递给下层模块。
* Client：音频客户端模块，负责与服务进程通信。
* Server：音频服务端模块，接收来自Client的音频数据。Server将音频数据分发至“音效、Mix混音”模块，进行音效处理和多路音频混合（Mixing）。
* AudioRendererSink：音频渲染接收端，接收处理后的音频数据，准备向下传递至硬件层。
* HDI/HDF：硬件驱动接口（Hardware Driver Interface）或硬件驱动框架（Hardware Driver Framework），负责将音频数据写入物理音频设备（如扬声器、耳机等）。

## hilog日志采集

在设备/data/log/hilog/目录下，通过[hilogtool](../harmonyos-guides/hilog-tool.md)解析二进制日志文件。可以通过如下命令，或将命令集成为一个.bat格式的[自动化脚本](../harmonyos-guides/hilog-tool.md#自动化脚本)文件，实现日志文件的解析。

```screen
@set Ymd=%date:~0,4%_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
@set Ymd=%Ymd: =0%
@set Dir=LOG_%YMD%
md %Dir%
hdc file recv /data/log/hilog/ .\%Dir%\
hilogtool parse -i .\%Dir% -d .\%Dir%
pause
```

## hilog日志分析

在音频问题定位（如播放无声、卡顿、焦点冲突等）中，系统侧原生日志的domain ID用于快速过滤和定位音频框架层的关键事件。常见的音频相关系统侧原生日志domain ID包括：C02B12、C02B2B、C02B83、C02B87等。

这些domain ID对应的日志主要作用包括：

1. 追踪音频流状态：

   通过搜索关键词StreamClientState，可获取音频流的启停状态、ID及类型（如输出流或输入流）。
2. 定位焦点冲突与中断：

   通过搜索关键词ActivateAudioInterrupt，可分析音频流是否被抢占焦点，查看forceType（打断类型）和hintType（中断提示，如INTERRUPT\_HINT\_DUCK表示音频躲避/降低音量）。
3. 检测数据流异常：

   通过搜索关键词underrun，可发现音频框架Server模块数据读取异常，通常意味着应用未及时向框架发送数据 。
4. 监控实例初始化与释放：
   * 搜索StreamBuilder可确认音频流构造器创建是否成功。
   * 结合StreamClientState可分析AudioRenderer实例是否被异常释放（Release）。
5. 辅助其他场景分析：
   * 结合volume关键词分析音量设置。
   * 结合current foreground APP is分析前后台切换对音频的影响。
   * 结合TASK\_DETECTION分析后台长时任务取消导致的音频中断。

通过domain ID进行日志采集和解析（如使用[hilogtool](../harmonyos-guides/hilog-tool.md)），在采集到的日志中使用关键词过滤，开发者可以高效地从系统日志中筛选出与音频渲染、混音、中断策略相关的核心信息，从而定位无声、卡顿、焦点冲突等问题。

### 可能根因及关键日志解析

1. **AudioRenderer实例初始化失败。**

   搜索StreamBuilder关键词，可以获取创建构造器成功的日志。

   * type is 1表示AUDIOSTREAM\_TYPE\_RENDERER（输出音频流）。
   * type is 2表示AUDIOSTREAM\_TYPE\_CAPTURER（输入音频流）。

   ```screen
   .audio/OAudioStreamBuilder: [invalidDomain] [OHAudioStreamBuilder] OAudioStreamBuilder created, type is 2
   .audio/OAudioStreamBuilder: [invalidDomain] [Generate]Generate OHAudioCapturer
   .audio/OAudioCapturer: [invalidDomain] [OHAudioCapturer] OHAudioCapturer created!
   schedule_service/BinderInvoker: BinderInvoker 91: created invoker 677416768
   .audio/AudioCapturer: [Create]Capturer::Create sourceType: 0, uid: -1
   .audio/AudioCapturer: [SetParams]StreamClientState: Capturer::SetParams.
   ```

   ```screen
   .audio/OAudioStreamBuilder: [invalidDomain] [OAudioStreamBuilder] OAudioStreamBuilder created, type is 1
   .audio/OAudioStreamBuilder: [invalidDomain] [Generate]Generate OAudioRenderer
   schedule_service/TASK_DETECTION: [audio_detect.cpp (UpdateAudioRecord:76)] Get Audio info uid: 20020199, sessionId: 100924, State: 3, type: recorder
   .audio/OAudioRenderer: [invalidDomain] [OAudioRenderer] OAudioRenderer created!
   ```
2. **音频流状态异常。**

   搜索StreamClientState关键词，可以获取音频流的启停状态、ID、音频流类型（参考[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)）等。

   ```screen
   09-23 18:02:33.551 18585 20466 I C02B83/appName/AudioRenderer: [Create]StreamClientState for Renderer::Create. content: 0, usage: 10, flags: 0, uid: -1
   09-23 18:02:33.551 18585 20466 I C02B83/appName/AudioRenderer: [SetParams]StreamClientState for Renderer::SetParams.
   09-23 18:02:33.551   778  2567 I C02B87/audio_server/AudioRouterCenter: [fetchOutputDevices]streamUsage 10 clientUID -1 start fetch device
   09-23 18:02:33.551   778  2567 E C02B12/audio_server/ExtRouterManager: [invalidDomain][FetchOutputDevices]activeRouter is nullptr
   ```

   ```screen
   09-23 18:02:33.566 18585 20466 I C02B83/appName/AudioRenderer: [Start]StreamClientState for Renderer::Start: id: 100204, streamType: 14, interruptMode: 0
   09-23 18:02:33.566   778  2567 I C02B87/audio_server/AudioInterruptService: [ActivateAudioInterrupt]sessionId: 100204 pid: 18585 streamType: 14 usage: 10 source: -1
   ```
3. **焦点冲突导致中断。**

   搜索ActivateAudioInterrupt关键词，可以获取到音频流被抢断焦点的相关日志，附近有forceType、hintType等关键信息。

   * forceType：音频打断类型，用于表示打断是否已由系统强制执行。
   * hintType：音频中断提示，用于表示根据焦点策略对音频流执行的具体操作。

   详细请参考音频中断事件[InterruptEvent](../harmonyos-references/arkts-apis-audio-i.md#interruptevent9)。

   ```screen
   6\2\hilog\hilog.271.20240605-174147.txt (12 hits)
   -05 17:41:49.394 49093 49126 I C02B12/AudioRenderer: [Start]AudioRenderer::Start id: 100106
   -05 17:41:49.394  1209 23126 I C02B12/AudioFramework: [ActivateAudioInterrupt] sessionId: 100106 pid: 49093 streamType: 1 usage: 1 source: -1
   -05 17:41:49.395  1209 23126 I C02B12/AudioPolicyService: [SetAudioScene] SetAudioScene: 0
   -05 17:41:49.395  1209 23126 I C02B12/AudioPolicyService: [SetAudioScene] SetAudioScene: 0
   -05 17:41:49.396  1209  1369 I C02B12/AudioPolicyServerHandler: [HandleFocusInfoChangeEvent] HandleFocusInfoChangeEvent focusInfoList: 1
   -05 17:41:49.396   337 61659 W C02B12/AudioServer: [SetAudioScene] Capturer is not initialized.
   -05 17:41:49.396   337 61659 I C02B12/AudioRendererSinkInner: [SetAudioScene] SetAudioScene scene: 0, device: 2
   -05 17:41:49.396   337 61659 I C02B12/AudioRendererSinkInner: [SetAudioScene] SetAudioScene scene: 0, device: 2
   ......
   6\2\hilog\hilog.271.20240605-174147.txt (19 hits)
   -05 17:42:03.694 50587 50775 I CO2B12/AudioRenderer: [Start]AudioRenderer::Start id: 100108
   -05 17:42:03.694  1209 23126 I CO2B12/AudioFramework: [ActivateAudioInterrupt]sessionid: 100108 pid: 50587 streamType: 1 usage: 1 source: -1
   -05 17:42:03.694  1209 23126 I CO2B12/AudioFramework: [SendAudioInterruptEvent]OnInterrupt for active sessionId:100108, interruptType:3, By sessionId:100108
   -05 17:42:03.694  1209 23126 I CO2B12/AudioPolicyService: [SetAudioScene] SetAudioScene: 0
   -05 17:42:03.694  1209 23126 I CO2B12/AudioPolicyService: [SetAudioScene] SetAudioScene: 0
   -05 17:42:03.694   637 59606 W CO2B12/AudioServer: [SetAudioScene]Capturer is not initialized.
   -05 17:42:03.694   637 59606 I CO2B12/AudioServerSinkInk: [SetAudioScene]SetAudioScene scene: 0, device: 2
   -05 17:42:03.694   637 59606 I CO2B12/AudioServerSinkInk: [SetAudioScene]SetAudioScene scene: 0, device: 2
   -05 17:42:03.695  1209  1369 I CO2B12/AudioServerHandler: [HandleFocusInfoChangeEvent] focusInfoList: 0
   -05 17:42:03.695 49093 49271 I CO2B12/AudioRenderer: [OnInterrupt]forceType 0, interruptType: 3
   -05 17:42:03.695  1209  1369 I CO2B12/AudioPolicyServerHandler: [HandleFocusInfoChangeEvent]HandleFocusInfoChangeEvent focusInfoList: 1
   ```

   当后播音频流焦点申请失败（被拒绝后），搜索ActivateAudioInterrupt关键词，可发现request rejected信息。

   ```screen
   08-12 13:56:00.152 43923 44000 I C02B12/AudioInterruptService: [ActivateAudioInterrupt]sessionId: 100003 pid: 45948 streamType: 24 usage: 1
   08-12 13:56:00.153 43923 44000 I C02B12/AudioInterruptService: [ProcessFocusEntry]the incoming stream is rejected by sessionid:100043, pid: 49093
   08-12 13:56:00.153 43923 44000 I C02B12/AudioInterruptService: [ProcessFocusEntry]OnInterrupt for incoming sessionid: 100003, hintType: 3  
   08-12 13:56:00.153 43923 44000 E C02B12/AudioInterruptService: [ActivateAudioInterrupt]request rejected  
   08-12 13:56:00.153   983 46090 E C02BA0/CameraDaemon.ImageStream: T:0 ImageStreamRequest<371>: Enq img(6)/frame(54)/stream(1)/cnt(54)  
   08-12 13:56:00.153 45948 45985 E C02B12/AudioRenderer: [Start]ActivateAudioInterrupt failed
   ```
4. **数据流传输异常。**

   搜索standbyCheck或者0size is not enough关键词，可以发现数据传输异常问题。

   ```screen
   08-26 15:27:56.937  797  2128 I C02B83/audio_server/RendererInServer: [WriteData]sessionId: 100987 OHAudioBuffer 0size is not enough
   08-26 15:27:56.937  797  1010 I C02B83/audio_server/RendererInServer: [StandByCheck]sessionId:100987 standByCounter_:1 standByEnable_:false
   ```
5. **音频音量异常。**

   搜索volume关键词，可以获取音量设置信息。

   ```screen
   08-26 09:34:56.258   797  2128 I C02B8B/audio_server/AudioVolume: [comm]volume,sessionId:100967,volume:0.398108,volumeType:2,devClass:primary,volumeSystem:0.398108,volumeStream:1.000000,volumeApp:1.000000,isVKB:0,isMuted:F,doNotDisturbStatusVolume:1,mdmStatus:1.000000
   ```
6. **前后台切换异常。**

   搜索Application State change to关键词，可以发现应用是否有切换前后台操作。

   ```screen
   08-26 09:44:57.057   967 46258 I C01731/resource_schedule_service/SUSPEND_MSG: [a92ab245190df3d 0 0]20020294_com.example.audioRenderPlayPcm_12226, state:4
   08-26 09:44:57.057   967 46258 I C01724/resource_schedule_service/TASK_DETECTION: [a92ab245190df3d 0 0][OnAppStateChanged:639]Application State change to background, uid: 20020294, pid: 12226,bundleName: bundleName
   ```
7. **长时任务异常。**

   搜索TASK\_DETECTION关键词，可以发现是否取消了后台长时任务导致音频中断，信息为Cancel continuous task。

   ```screen
   08-09 09:38:27.395 913 17110 I C01724/TASK_DETECTION: backgroundModes: 2,3,
   08-09 09:38:27.395 913 17110 E C01724/TASK_DETECTION: [task_detection_manager.cpp(CheckUidStateInner:706)]new task 20020092_EntryAbility_6487 use nothing, Cancel continuous task
   08-09 09:38:27.396 1082 1224 I C01711/CONTINUOUS_TASK: [bg_continuous_task_mgr.cpp(HandleStopContinuousTask):934] StopContinuousTask taskType: 0, key 20020092_EntryAbility_6487
   ```

## 典型案例

### 焦点冲突导致后台音乐中断

**场景描述**

先播放音乐，再使用导航，发现导航声音会中断音乐播放。手动再次启动音乐播放，切回导航应用继续导航，发现音乐会再次中断播放。

**分析思路**

1. 搜索音频流状态StreamClientState和音量volume均未发现问题。
2. 由于该问题是不同应用之间音频流相互中断的现象，开发者可以着重分析焦点冲突情况。在日志中搜索关键词ActivateAudioInterrupt发现：

   ```screen
   02-17 07:42:04.140 1310 1310 I C02B12/AudioFramework: [audio_policy_server.cpp] [ActivateAudioInterrupt]ActivateAudioInterrupt: sessionID: 100032, streamType: 21, streamUsage: 13, sourceType: -1, pid: 58008
   ```

   ```screen
   02-17 07:42:04.142 1527 16329 I C02B12/AudioFramework: [audio_renderer.cpp] [OnInterrupt]forceType 0,hintType:4
   ```

上述是导航声音申请焦点的过程，其中streamUsage: 13（STREAM\_USAGE\_NAVIGATION = 13）表示导航场景音频输出流；hintType：4（INTERRUPT\_HINT\_DUCK = 4）表示提示音频躲避开始，降低音乐播放音量。

```screen
02-17 07:42:07.064 1310 47758 I C02B12/AudioFramework: [audio_policy_server.cpp] [ActivateAudioInterrupt]ActivateAudioInterrupt::sessionID: 89, streamType: 1, streamUsage: 1, sourceType: -1, pid: 58008
```

而pid = 58008进程，还中断了音乐类型（streamUsage: 1，STREAM\_USAGE\_MUSIC = 1）的音频流。后起的音频流，会导致当前播放的音乐类型的音频流停止，因此导致音乐播放中断。

### 音频数据流异常导致突然无声

**场景描述**

应用在播放视频过程中突然无声，过段时间后音频自动恢复。

**分析思路**

1. 搜索音频流状态StreamClientState和音量volume均未发现问题。
2. 日志中发现打印了StandbyCheck或者0size is not enough关键词，说明可能是应用这段时间没有送数据给音频框架。

   ```screen
   08-26 09:34:56.568   797  2128 I C02B83/audio_server/RendererInServer: [WriteData]sessionId: 100967 OHAudioBuffer 0size is not enough
   08-26 09:34:56.568  3079  3079 I A00F00/.../61012446: ResourcePackageBusinessHandler: resId:ai_suggestion_hmos_layout,domain:AIBusinessHMOS
   08-26 09:34:56.568  2964  2964 I A01B01/com.ohos.sceneboard/HOME: [a92ab342c086567 222d75c 397c514]BaseServiceStub: [PhoneDesktopProviderServiceStub]-onRemoteMessageRequest called code = 1, isSupportSegments = true, isRawDataBuffer = false
   08-26 09:34:56.568   797  1010 I C02B83/audio_server/RendererInServer: [StandByCheck]sessionId:100967 standByCounter_:0 standByEnable_:false
   ```
3. 针对数据读取异常的情况，可通过可视化PCM dump数据来进行佐证，发现应用给过来的数据有问题。如下图所示PCM音频数据中确实有一段无声：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/DLzlDMkGRbKv7Kxts_tIGg/zh-cn_image_0000002733345335.png "点击放大")

### AudioRenderer异常释放导致播放无声

**场景描述**

应用从视频页跳转至新视频页，再回退原视频页后，视频播放无声音。

**分析思路**

1. 搜索StreamClientState关键词，发现音频流1播放10秒暂停，切到音频流2后再切回1时，音频流1被Release导致视频播放时无声音。

   ```screen
   09-23 16:23:31.048 51758 51856 I C02B83/appName/AudioRenderer: [Create]StreamClientState for Renderer::Create. content: 2, usage: 1, flags: 0, uid: -1
   09-23 16:23:31.048 51758 51856 I C02B83/appName/AudioRenderer: [SetParams]StreamClientState for Renderer::SetParams
   09-23 16:23:31.061 51758 51860 I C02B83/appName/AudioRenderer: [Start]StreamClientState for Renderer::Start. id: 100191, streamType: 1, interruptMode: 0
   09-23 16:23:41.139 51758 51860 I C02B83/appName/AudioRenderer: [Pause]StreamClientState for Renderer::Pause. id: 100191
   09-23 16:23:41.157 51758 51951 I C02B83/appName/AudioRenderer: [Create]StreamClientState for Renderer::Create. content: 2, usage: 1, flags: 0, uid: -1
   09-23 16:23:41.157 51758 51951 I C02B83/appName/AudioRenderer: [SetParams]StreamClientState for Renderer::SetParams
   09-23 16:23:41.193 51758 51954 I C02B83/appName/AudioRenderer: [Start]StreamClientState for Renderer::Start. id: 100192, streamType: 1, interruptMode: 0
   09-23 16:23:50.860 51758 51758 I C02B83/appName/AudioRenderer: [Stop]StreamClientState for Renderer::Stop. id: 100192
   09-23 16:23:51.040 51758 51758 I C02B83/appName/AudioRenderer: [Release]StreamClientState for Renderer::Release. id: 100192
   09-23 16:23:51.043 51758 51758 I C02B83/appName/AudioRenderer: [Release]StreamClientState for Renderer::Release. id: 100191
   ```
2. 同时，可以通过trace日志进一步佐证AudioRenderer实例异常释放（可选操作）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/foIfwZq2RYCb7yjFsD07rQ/zh-cn_image_0000002703666060.png "点击放大")

### 焦点冲突导致设备切换后无声

**场景描述**

音视频会议场景，在拉远端音频流时会有打开扬声器动作，但发现听不到远端用户的声音。

**分析思路**

针对设备切换异常的现象，可以搜索AudioScene关键词查看设备切换过程。同时搜索StreamClientState关键词和ActivateAudioInterrupt关键词综合分析。分析发现拉取的远端音频流（sessionID：100003，pid：45948，streamType：24，usage：17）与当前音频流（sessionID：100043，pid：43239，streamType：24，usage：17）产生了冲突。pid：43239应用拒绝了远端音频流的焦点申请，进而导致打开扬声器后无声音。

日志如下：

```screen
D:\temp\20240815\3_扬声器打开-reject 日志\hilog.616.20240812-135450 (13 hits)
Line 2212: 08-12 13:54:51.636 43308 43308 I C02B12/NapiAudioManager: [GetAudioSceneSync]GetRenderRateSync
Line 4169: 08-12 13:54:52.215 43923 43995 I C02B12/AudioInterruptService: [ActivateAudioInterrupt] sessionid: 100043 pid: 43239 streamType: 24 usage: 17 source: -1
Line 4175: 08-12 13:54:52.215 43923 43995 I C02B12/AudioPolicyService: [SetAudioScene] Set audio scene start 3
Line 4187: 08-12 13:54:52.215 43923 43944 I C02B12/AudioPolicyServerHandler: [HandleFocusInfoChangeEvent] HandleFocusInfoChangeEvent focusInfoList :1
Line 4239: 08-12 13:54:52.221 43923 43995 W C02B12/AudioServer: [SetAudioScene] Capturer is not initialized.
Line 4240: 08-12 13:54:52.221 43923 43995 I C02B12/AudioRendererSinkInner: [SetAudioScene] SetAudioScene scene: 3, device: 2
......
```

```screen
D:\temp\20240815\3_扬声器打开-reject 日志\hilog.617.20240812-135501 (6 hits)
Line 11723: 08-12 13:55:05.267 44194 44194 I C02B12/NapiAudioManager: [GetAudioSceneSync]GetRenderRateSync
Line 11824: 08-12 13:55:05.277 43923 43946 I C02B12/AudioRendererSinkInner: [SetAudioScene] SetAudioScene scene: 3, device: 1
Line 11824: 08-12 13:55:05.277 43923 43946 I C02B12/AudioRendererSinkInner: [SetAudioScene] SetAudioScene scene: 3, device: 1
Line 12859: 08-12 13:55:05.514 44194 44194 I C02B12/NapiAudioManager: [GetAudioSceneSync]GetRenderRateSync
Line 12895: 08-12 13:55:05.517 44194 44194 I C02B12/NapiAudioManager: [GetAudioSceneSync]GetRenderRateSync
Line 12933: 08-12 13:55:05.522 44194 44194 I C02B12/NapiAudioManager: [GetAudioSceneSync]GetRenderRateSync
```

```screen
D:\temp\20240815\3_扬声器打开-reject 日志\hilog.618.20240812-135546 (23 hits)
......
Line 15423: 08-12 13:56:00.152 45948 45985 I C02B12/AudioRenderer: [Start] StreamClientState for Renderer::Start. id: 100003, streamType: 24, interruptMode: 0
Line 15424: 08-12 13:56:00.152 43923 44000 I C02B12/AudioInterruptService: [ActivateAudioInterrupt] sessionid: 100003 pid: 45948 streamType: 24 usage: 17 source: -1
Line 15425: 08-12 13:56:00.153 43923 44000 I C02B12/AudioInterruptService: [ProcessFocusEntry] the incoming stream is rejected by sessionid:100043, pid:43239
Line 15426: 08-12 13:56:00.153 43923 44000 I C02B12/AudioInterruptService: [ProcessFocusEntry]OnInterrupt for incoming sessionid: 100003, hintType: 3
Line 15427: 08-12 13:56:00.153 43923 44000 E C02B12/AudioInterruptService: [ActivateAudioInterrupt] request rejected
Line 15429: 08-12 13:56:00.153 45948 45985 E C02B12/AudioInterruptService: [ActivateAudioInterrupt] Failed
```
