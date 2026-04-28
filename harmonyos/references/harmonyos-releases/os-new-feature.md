---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature
title: 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:56+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7089adc0f60267389647d8749dc1806c18bf75714305f7f8ef7c4f53874ec74d
---

## Ability Kit

* 支持PC/2in1设备创建Native子进程，并传递参数到子进程。（[指南](../harmonyos-guides/capi-nativechildprocess-development-guideline.md)）
* 包管理新增定义ElementName的C API。（[API参考](../harmonyos-references/capi-native-bundle-oh-nativebundle-elementname.md)）
* 元能力新增C API，提供从ApplicationContext中获取cache路径、Area以及bundleName的能力。（[API参考](../harmonyos-references/capi-application-context-h.md)）

## ArkData

Preferences部件提供C API。（[指南](../harmonyos-guides/preferences-guidelines.md)、[API参考](../harmonyos-references/capi-preferences.md)）

## ArkUI

* RichEditor支持配置滚动条的显隐。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#barstate13)）
* 通过XComponent接入的三方平台支持无障碍能力。（[API参考](../harmonyos-references/capi-native-interface-accessibility-h.md)、[指南](../harmonyos-guides/ndk-accessibility-xcomponent.md)）
* 支持使用ComponentContent类型参数设置ListItemGroup的头部和尾部组件。（[API参考](../harmonyos-references/js-apis-arkui-componentcontent.md)）
* 新增支持获取和设置当前窗口是否禁用返回手势的功能，该功能仅在主窗口全屏模式下生效。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setgesturebackenabled13)）

## ArkWeb

* 支持获取资源响应数据和响应数据的准备状态。（[API参考](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md#getresponsedataex13)）
* 支持获取网页当前的滚动偏移量。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getscrolloffset13)）

## AVSession Kit

媒体播控模块提供C API。（[指南](../harmonyos-guides/using-ohavsession-developer.md)）

## Background Tasks Kit

* 短时任务提供C API。（[指南](../harmonyos-guides/native-transient-task.md)、[API参考](../harmonyos-references/capi-transienttask.md)）
* 新增音视频通话长时任务类型的定义。（[API参考](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)）

## Basic Services Kit

* 剪贴板模块提供C API。（[API参考](../harmonyos-references/capi-oh-pasteboard-h.md)）
* 打印服务模块新增C API。（[API参考](../harmonyos-references/capi-oh-print.md)）
* 电源管理模块新增C API。（[API参考](../harmonyos-references/capi-oh-batteryinfo.md)）

## Camera Kit

优化相机预览流的处理机制，增加对stride值的处理。详见[双路预览（ArkTS）](../harmonyos-guides/camera-dual-channel-preview.md)或[预览流二次处理（C/C++）](../harmonyos-guides/native-camera-preview-imagereceiver.md)。

## Connectivity Kit

* 支持通过C API获取蓝牙开关的状态。（[API参考](../harmonyos-references/capi-bluetooth.md)）
* 支持通过C API获取Wi-Fi开关的状态。（[API参考](../harmonyos-references/capi-wifi.md)）

## Core File Kit

文件共享fileuri模块新增C API。（[指南](../harmonyos-guides/native-fileuri-guidelines.md)、[API参考](../harmonyos-references/capi-oh-file-uri-h.md#oh_fileuri_getfilename)）

## Device Security Kit

* 支持通过C API查询设备安全模式。（[API参考](../harmonyos-references/devicesecurity-capi-devicesecuritymode.md)）
* 支持通过C API为请求设置二进制数据接收回调。（[API参考](../harmonyos-references/remote-communication-overview.md#hms_rcp_setrequestonbinarydatarecvcallback)）

## Game Service Kit

游戏场景感知支持按需订阅设备状态变化和查询设备状态信息。（[API参考-订阅设备状态](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged-1)、[API参考-查询设备状态](../harmonyos-references/gameservice-gameperformance.md#gameperformancegetdeviceinfobyscope)）

## Image Kit

支持通过C API从PixelMap中读取ARGB格式的数据。（[API参考](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_getargbpixels)）

## Input Kit

多模输入能力新增一批C API。（[API参考](../harmonyos-references/capi-input.md)）

## Location Kit

地理位置模块提供C API。（[API参考](../harmonyos-references/capi-location.md)）

## Map Kit

支持设置地图经纬度范围和4个方向与边界之间的距离。（[API参考](../harmonyos-references/map-map-newlatlngbounds.md#newlatlngbounds-3)）

## Media Library Kit

PhotoViewPicker能力增强：

* PickerOptions新增是否支持滑动多选的选项和设置大图页checkbox的位置的选项。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)）
* 新增向picker发送退出大图的通知的API。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#exitphotobrowser13)）
* 新增设置大图页大图预览组件外其他UI元素是否可见的API。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#setphotobrowseruielementvisibility13)）
* 新增定义大图页大图预览组件外其他UI元素的API。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#photobrowseruielement13)）
* 支持PhotoPicker组件的删除通知等相关能力。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#itemsdeletedcallback13)）

## NearLink Kit

【新增Kit】NearLink Kit（星闪服务）提供一种低功耗、高速率的短距离通信服务，支持星闪设备之间的连接、数据交互。

中心设备可以通过扫描发现外围设备，并发起连接。外围设备可以通过发送广播的方式被中心设备发现，和中心设备连接之后可以进行相应的数据传输。

详细信息请参见[NearLink Kit开发指南](../harmonyos-guides/nearlink-introduction.md)。

## Notification Kit

通知服务新增C API。（[API参考](../harmonyos-references/capi-notification.md)）

## Payment Kit

新增数字人民币的接口。（[API参考](../harmonyos-references/payment-digitalcnyservice.md)）

## Remote Communication Kit

支持URPC场景下远程RPC调用能力。（[指南](../harmonyos-guides/remote-communication-urpccall.md)、[API参考](../harmonyos-references/remote-communication-urpcapi.md)）

## Scan Kit

在默认界面扫码界面，支持用户点击关闭“隐私横幅”。当重新打开应用的默认界面扫码将只显示安全访问提示，3s后消失。（[指南](../harmonyos-guides/scan-scanbarcode.md#业务流程)）

## Sensor Service Kit

传感器模块新增游戏及线性加速度传感器的C API，其中枚举类型Sensor\_Type新增SENSOR\_TYPE\_ACCELEROMETER参数（[API参考-Sensor\_Type](../harmonyos-references/capi-oh-sensor-type-h.md#sensor_type)），函数OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length)入参的传感器类型新增SENSOR\_TYPE\_LINEAR\_ACCELERATION（[API参考](../harmonyos-references/capi-oh-sensor-h.md#函数)）。

## Telephony Kit

蜂窝网络模块提供C API。（[API参考-蜂窝数据](../harmonyos-references/capi-telephony-data-h.md)、[API参考-网络搜索](../harmonyos-references/capi-telephony-radio-h.md)）

## Vision Kit

在AI识图场景下，支持设置图像分割菜单显示状态（[API参考](../harmonyos-references/vision-image-analyzer.md#setsubjectmenuvisibility)）以及开启与取消监听图片搜索事件（[API参考-开启](../harmonyos-references/vision-image-analyzer.md#ontype-objectsearchpanelvisibilitychange)、[API参考-取消](../harmonyos-references/vision-image-analyzer.md#offtype-objectsearchpanelvisibilitychange)）。

## XEngine Kit

支持时域AI超分能力，即利用相机抖动获取不同位置的采样信息，融合时域实现超采样率和超分辨率功能，并利用神经网络达到抗锯齿效果。（[指南](../harmonyos-guides/xengine-kit-ai-temporal-upscaling.md)）

## Audio Kit

新增支持麦克风状态检测的ArkTS和C API，可查询并监听在使用麦克风录音时，麦克风是否被堵塞。（[API参考](../harmonyos-references/capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_setmicblockstatuscallback)）
