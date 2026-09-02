---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-64
title: 应用切换前置摄像头卡住
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用切换前置摄像头卡住
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:359bab13e28531d80d80a9afae69f18667eaddb92b5eb58b0c1561a54bafb694
---

## 问题现象

拍照应用后置摄像头预览和拍照正常，切换前置摄像头时页面预览流卡住，无法正常拍照。

## 背景知识

* [getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)：查询相机设备在指定模式下支持的输出能力，同步返回结果。
* [CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)：相机输出能力项。

## 问题定位

1. 查看hilog日志，搜索'device/1'，'PreviewOutput'等关键词，可以看出预览流是创建成功的。

   ```txt
   19:49:33.602 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{AddInput():1228} AddInput is called
   19:49:33.602  1675  6467 I C02B01/camera_service/CAMERA: [dict]{AddInput():312} HCaptureSession::AddInput prepare execute
   19:49:33.602  1675  6467 I C02B01/camera_service/CAMERA: [dict]{operator()():325} HCaptureSession::AddInput device:device/1
   19:49:33.602 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{GetJSArgsForCameraOutput():1331} preview output adding..
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigureOutput():853} Enter Into CaptureSession::ConfigureOutput
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigureOutput():856} CaptureSession::ConfigureOutput outputType is:0
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigurePreviewOutput():716} CaptureSession::ConfigurePreviewOutput enter
   19:49:33.603   903  6731 I C01700/resource_schedule_service/RSS: [dict]report camera status completed
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ValidateOutputProfile():4789} CaptureSession::ValidateOutputProfile profile:w(480),h(480),f(1003) outputType:0
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{GetMode():2995} CaptureSession GetMode currentMode_ = 1, guestMode_ = 0
   19:49:33.603   903  8661 I C01703/resource_schedule_service/socperf: [dict][HandleCameraStateChange]: SocPerfPlugin: socperf->CAMERA_STATE_CHANGE: 0
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4809} CaptureSession::ValidateOutputProfile in mode(1): w(480),h(480),f(1003), profiles size is:22
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(480),h(480),f(1003)
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{AdaptOutputVideoHighFrameRate():948} Enter Into CaptureSession::AdaptOutputVideoHighFrameRate
   19:49:33.603 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{GetMode():2995} CaptureSession GetMode currentMode_ = 1, guestMode_ = 0
   19:49:33.604   903  8662 I C01703/resource_schedule_service/socperf: [dict][HandleCameraStateChange]: SocPerfPlugin: socperf->CAMERA_STATE_CHANGE: 0
   19:49:33.604  1675  6467 I C02B01/camera_service/CAMERA: [dict]{AddOutputStream():155} HStreamOperator::AddOutputStream streamId:81 streamType:2
   19:49:33.604  1675  6467 I C02B01/camera_service/CAMERA: [dict]{AddOutput():309} CaptureSession::AddOutput with with 2, rc = 0
   19:49:33.604  1675  6467 I C01401/camera_service/Bufferqueue: [dict]<consumer_surface.cpp:60-~ConsumerSurface>: ~ConsumerSurface, producer_ sptrCnt: 1, uniqueId: 87.
   19:49:33.604  1675  6467 I C02B01/camera_service/CAMERA: [dict]{AddOutput():443} CaptureSession::AddOutput with with 2, rc = 0
   19:49:33.604 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{AddOutput():923} CaptureSession::AddOutput StreamType = 2
   19:49:33.605 62122 62122 E C02B01/com.hm.example/CAMERA: [dict]{AddOutput():938} SetCameraApi!, errCode: 0
   ```
2. 搜索'PhotoOutput'，日志如下，可以看出创建的拍照输出流的分辨率是'w(640),h(360)'，但是前置摄像头支持的拍照配置信息集合中没有符合该分辨率的配置。然后日志打印了'CanAddOutput check failed!'，创建拍照输出流失败。

   ```txt
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{AddOutput():1365} AddOutput is called
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{GetJSArgsForCameraOutput():1335} photo output adding..
   19:49:33.605  1550  9854 I C01202/foundation/Ces: [dict][common_event_control_manager.cpp(NotifyUnorderedEventLocked:250)]Notify usual.event.CAMERA_STATUS end(2, 2, 0, 0)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigureOutput():853} Enter Into CaptureSession::ConfigureOutput
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigureOutput():856} CaptureSession::ConfigureOutput outputType is:1
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ConfigurePhotoOutput():800} CaptureSession::ConfigurePhotoOutput enter
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{ValidateOutputProfile():4789} CaptureSession::ValidateOutputProfile profile:w(640),h(360),f(2000) outputType:1
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{GetMode():2995} CaptureSession GetMode currentMode_ = 1, guestMode_ = 0
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4809} CaptureSession::ValidateOutputProfile in mode(1): w(640),h(360),f(2000), profiles size is:22
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(640),h(480),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(640),h(640),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(720),h(720),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(960),h(720),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(1080),h(1080),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(1280),h(720),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(1440),h(1080),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(1920),h(1080),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2160),h(2160),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2304),h(2304),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2384),h(1080),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2560),h(1080),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2688),h(1216),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2816),h(2112),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(2880),h(2160),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(3072),h(2304),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(3120),h(3120),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(3264),h(2448),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(3840),h(1648),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(3840),h(2160),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(4160),h(1888),f(2000)
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{operator()():4813} CaptureSession::ValidateOutputProfile outType iterator profile::w(4160),h(3120),f(2000)
   19:49:33.605 62122 62122 E C02B01/com.hm.example/CAMERA: [dict]{operator()():4816} CaptureSession::ValidateOutputProfile fail!
   19:49:33.605 62122 62122 E C02B01/com.hm.example/CAMERA: [dict]{AddOutput():910} CanAddOutput check failed!
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{InvokeJSAsyncMethod():54} CameraInputNapi::Open, InvokeJSAsyncMethod napi_resolve_deferred
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{InvokeJSAsyncMethod():59} CameraInputNapi::Open, InvokeJSAsyncMethod end deferred
   19:49:33.605 62122 62122 I C02B01/com.hm.example/CAMERA: [dict]{InvokeJSAsyncMethod():72} CameraInputNapi::Open, InvokeJSAsyncMethod inner end
   19:49:33.605  1001 11170 I C01F0B/telephony/TelephonyExtCommon: [dict]OnReceiveEvent enter, event : usual.event.CAMERA_STATUS
   19:49:33.605  1001 11170 I C01F0B/telephony/TelephonyExtCommon: [dict]HandleCameraStatus, cameraId=device/1, cameraState=0
   19:49:33.607   625 51511 I C02D15/hiview/XPower: [dict][task_136]#CameraPower: m_lastBatteryGasGauge 790
   19:49:33.608   903  9078 I C02948/resource_schedule_service/ThermalAware: [dict][cam_collector.cpp] CameraPower: bundleName: com.hm.example, cameraId: 1, wholePower: 0, owner: 1
   19:49:33.609   903  9073 I C02948/resource_schedule_service/ThermalAware: [dict][thermal_scenario_cluster.cpp] camowner change to 1 pkg: com.hm.example
   19:49:33.609  1477  1796 I C02942/powermgr/ThermalSvc: [dict]tag camowner, val 1, isImmed 1
   19:49:33.610   986 10700 I C02BA1/CameraDaemon/CameraBufferMonitor: [dict]T:19 DelMonitorApva<313>: [CBA]totalSize(338116Kb), size(36868Kb), stride(37748768), usage(0x400820), cma tag(0), format(769), requestor(SMARTISP_AIAF_WORKSPACE)
   19:49:33.610   986 10700 W C02160/CameraDaemon/RUNTIME: [dict]rtCloseClient:35 Direct Device close start.
   19:49:33.610   986 10700 W C02160/CameraDaemon/RUNTIME: [dict]rtCloseClient:38 Direct Device close success.
   19:49:33.610   986 10700 W C02160/CameraDaemon/RUNTIME: [dict]Exit:94 client cnt_ 2
   ```

## 分析结论

应用需要创建的拍照输出流的分辨率是'w(640),h(360)'，但是前置摄像头支持的拍照配置信息集合中没有符合该分辨率的配置，所以创建拍照输出流失败，导致切换前置摄像头卡住。

## 修改建议

不同的设备前置摄像头支持的拍照配置信息可能不一样，应用需要根据设备的实际情况选择适合的分辨率配置创建拍照输出流。示例代码可以参考官网文档[拍照](../harmonyos-guides/camera-shooting.md)章节的[开发步骤](../harmonyos-guides/camera-shooting.md#开发步骤)第二步创建拍照输出流。
