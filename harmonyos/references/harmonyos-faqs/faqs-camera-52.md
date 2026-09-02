---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-52
title: 配置参数异常排查须知
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 配置参数异常排查须知
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8256ab844ed1cfb5ba7ed3ac76803eac468ab640026aa4c3e080f0649caac7a3
---

## 问题现象

在使用Camera Kit开发过程中，可能会高频碰到7400101、7400110这两类与配置参数有关的错误，本文将以设置帧率的接口为例讲述这两类错误的排查方案以及可能的原因。

## 背景知识

* [7400101 无效入参](../harmonyos-references/errorcode-camera.md#section7400101-无效入参)：调用接口时，传入的参数无效。
* [7400110 与当前配置存在冲突](../harmonyos-references/errorcode-camera.md#section7400110-与当前配置存在冲突)：由于当前提交的配置与设备所支持的配置存在不兼容。

## 问题定位

* 场景一：7400101定位过程。

  在拍照界面，当使用setFrameRate()方法使Preview的帧率在固定帧率12和30之间切换时，偶有发生7400101的报错。通过日志搜索关键词“7400101”：

  ```txt
  01-25 14:46:42.324   4258-4258     A0FF00/com.exa....customcamera  com.examp...omcamera  I     [camera-log] PreviewManager: setFrameRate: activeFrameRate: [12, 12].
  01-25 14:46:42.324   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab2bc524f137 0 0]qosId not exist, qosId = 103!
  01-25 14:46:42.324   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab2bc524f137 0 0]ConvertValueToNew failed, qosId = 103!
  01-25 14:46:42.324   4258-4258     C02B01/com.exa...camera/CAMERA  com.examp...omcamera  E     {SetFrameRate():494} PreviewOutput::SetFrameRate The frame rate does not need to be set.
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab3bc524f3bd 0 0]qosId not exist, qosId = 104!
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab3bc524f3bd 0 0]ConvertValueToNew failed, qosId = 104!
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab3bc524f3bd 0 0]qosId not exist, qosId = 105!
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab3bc524f3bd 0 0]ConvertValueToNew failed, qosId = 105!
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab3bc524f3bd 0 0]qosId not exist, qosId = 103!
  01-25 14:46:42.325   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab3bc524f3bd 0 0]ConvertValueToNew failed, qosId = 103!
  01-25 14:46:42.333   4258-4258     C02B01/com.exa...camera/CAMERA  com.examp...omcamera  E     {SetFrameRate():1055} PreviewOutputNapi::SetFrameRate! 7400101
  01-25 14:46:42.333   4258-4258     A0FF00/com.exa....customcamera  com.examp...omcamera  E     [camera-log] PreviewManager: setFrameRate [12, 12] error {"code":"7400101"}
  ```

  从这段日志可以看出，在尝试将固定帧率设置为12时出现了7400101报错。但是实际上当预览帧率在12和30之间切换时是有成功的案例的，于是通过“setFrameRate”关键词继续向上排查日志，找到成功设置的日志：

  ```txt
  01-25 14:46:37.967   4258-4258     A0FF00/com.exa....customcamera  com.examp...omcamera  I     [camera-log] PreviewManager: setFrameRate: activeFrameRate: [30, 30].
  01-25 14:46:37.967   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab6bc4dec0de 0 0]ConvertValueToNew failed, qosId = 105!
  01-25 14:46:37.967   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab6bc4dec0de 0 0]qosId not exist, qosId = 103!
  01-25 14:46:37.967   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab6bc4dec0de 0 0]ConvertValueToNew failed, qosId = 103!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab7bc4dec32c 0 0]qosId not exist, qosId = 104!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab7bc4dec32c 0 0]ConvertValueToNew failed, qosId = 104!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab7bc4dec32c 0 0]qosId not exist, qosId = 105!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab7bc4dec32c 0 0]ConvertValueToNew failed, qosId = 105!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       I     [a92ab7bc4dec32c 0 0]qosId not exist, qosId = 103!
  01-25 14:46:37.968   1324-1338     C01708/perfgenius_host/PF_      perfgenius_host       W     [a92ab7bc4dec32c 0 0]ConvertValueToNew failed, qosId = 103!
  01-25 14:46:37.968   1818-5040     C02B01/camera_service/CAMERA    camera_service        I     {GetClientBundle():330} bundle name is com.example.customcamera 
  01-25 14:46:37.968   983-53898     C02BB3/CameraD...n/IPS_PRESTAB  CameraDaemon          I     PreviewStablization.cpp:898 PostProcess mType=0x40000: mPreRet=0 index=244 frameNum=245 costtime=2ms, warpRet=0 warpType=2 tnrType=0 dropFlag=0 mIsNeedRecording=1 mIsAlgoStarted=1 mCurVideoStatus=0 outFrame=157018 mInFrameList.size=0 mOutFrameList.size=0 residuaryRotateRadian 0.000000 roi=[48, 36, 1824, 1368]
  01-25 14:46:37.968   1818-5040     C02B01/camera_service/CAMERA    camera_service        I     {SetFrameRate():939} HStreamRepeat::SetFramRate stream:616, with settingCapture ID:345
  01-25 14:46:37.968   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [DytoneSyncAIVPreProcess.1171] [dytoneSync process] AIV----aiv NPU proc---END!
  01-25 14:46:37.968   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [ProcessDytoneSync.459 ] [dytoneSync process] NPU----MODEL--INFER---begin!
  01-25 14:46:37.968   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [ProcessDytoneSync.466 ] [dytoneSync process] NPU AND CPU----MODEL--INFER---END!
  01-25 14:46:37.968   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [XStyleProcess.969 ] [dytoneSync process] ALL SYNC ONLY IS OVER!
  01-25 14:46:37.968   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [XStyleProcess.1017] [xstyle process] pXStyle->Process frame=245 bypass
  01-25 14:46:37.969   983-5031      A02BA9/CameraD...ONE_V20241126  CameraDaemon          I     [MergeLut.281 ] [xstyle process] MergeLut end
  01-25 14:46:37.969   983-5021      C02BC1/CameraD...oomController  CameraDaemon          E     T:0 UpdateZoomList:334 not update CAMERA_OHOS_SMOOTH_ZOOM_RATIOS, dim:0!
  01-25 14:46:37.969   983-5021      C02BC1/CameraD...rorController  CameraDaemon          E     T:0 UpdateStreamMirrorSetting:45 capability not mirror support, exit
  01-25 14:46:37.969   983-5021      C02BC1/CameraD...rorController  CameraDaemon          E     T:0 UpdateStreamMirrorSetting:45 capability not mirror support, exit
  01-25 14:46:37.969   4258-4258     C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {AddFunctionToMap():5485} The automatic switching device is not enabled.
  01-25 14:46:37.969   4258-4258     A0FF00/com.exa....customcamera  com.examp...omcamera  I     [camera-log] PreviewManager: ======lalala setFrameRate [12, 12]
  ```

  对比这两段日志，从第一段失败的日志可以发现，在设置帧率为12之前，实际生效的帧率已经是12了；而第二段日志显示，在设置帧率为12之前，实际生效的帧率为30，所以再次调用setFrameRate(12, 12)时就不会报错。
* 场景二：7400110排查过程。

  在视频录制模式中，使用setFrameRate(30, 30)接口把预览帧率设置为固定帧率30，发生报错7400110。在日志中搜索关键词“7400110”，得到如下信息：

  ```txt
  01-25 14:11:32.437   41803-41803   A0FF00/com.exa....customcamera  com.examp...omcamera  I     [camera-log] PreviewManager: setFrameRate: activeFrameRate: [0, 0].
  01-25 14:11:32.437   41803-41803   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  W     {CheckFrameRateRangeWithCurrentFps():783} CaptureSession::CheckFrameRateRangeWithCurrentFps check is not pass!
  01-25 14:11:32.437   41803-41803   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  E     {canSetFrameRateRange():853} PreviewOutput::canSetFrameRateRange Can not set frame rate range with wrong state of output
  01-25 14:11:32.437   41803-41803   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  E     {SetFrameRate():1055} PreviewOutputNapi::SetFrameRate! 7400110
  01-25 14:11:32.437   41803-41803   A0FF00/com.exa....customcamera  com.examp...omcamera  E     [camera-log] PreviewManager: setFrameRate [30, 30] error {"code":"7400110"}
  ```

  从日志中二三两行可以发现，报错的主要原因是设置的帧率超过了OutPut可设置帧率的范围。于是通过Debug查看当前PreviewOutput支持的帧率范围，结果如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/lIL6YJ41RNqt6HJBS2lvsw/zh-cn_image_0000002658911799.png "点击放大")

  从图中可知，在当前视频拍摄模式下，Preview支持的帧率列表为[1,30]的非固定帧率和[60,60]的固定帧率，但是代码中设置的帧率为[30,30]的固定帧率，该帧率并不在当前Preview支持的帧率列表之中，因此报错7400110。

## 分析结论

* 场景一：7400101定位结果。

  通过setFrameRate()接口设置了一个无效的重复帧率值，导致报错7400101。
* 场景二：7400110定位结果。

  设置的帧率不在当前Preview支持的帧率列表之中。

## 修改建议

* 场景一：7400101修改建议。

  避免无效调用，可以先通过getActiveFrameRate()方法查询当前生效的帧率设置，如果相同则直接跳过，仅当不同时再实际调用setFrameRate()接口去设置帧率。
* 场景二：7400110修改建议。

  先通过getSupportedFrameRates()方法查询当前OutPut支持的帧率范围，然后从中选择当前业务需要的帧率去设置。

## 总结

在使用参数设置的接口之前，需要查看相关的接口文档，通过查询接口了解该参数的限制和条件，避免设置的参数超出当前设备支持的范围。
