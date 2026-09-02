---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-27
title: 使用投播组件开发投播功能及注意事项
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 使用投播组件开发投播功能及注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cc269a97a32f810b9fe6fcbf9eb5e1a1c0d29e6d1abd528e5a91a2b379532fab
---

## 问题现象

应用可以通过统一投播组件AVCastPicker，在应用内及系统播控中心，将音视频资源通过Cast+协议/DLNA协议投播到远端设备或进行发声设备切换。使用中需要注意一些常见的注意事项。

## 背景知识

音视频投播：音视频投播包括[基础投播能力](../harmonyos-guides/avcastpicker.md#基础投播能力)和[投播能力增强](../harmonyos-guides/avcastpicker.md#投播能力增强)。

投播设备：参考[ProtocolType](../harmonyos-references/arkts-apis-avsession-e.md#protocoltype11)，本地设备，包括设备本身的内置扬声器或音频插孔、A2DP设备，为非投播设备，其余通过统一投播组件AVCastPicker连接到的设备为投播设备。

[媒体会话（AVSession）](../harmonyos-references/arkts-apis-avsession-avsession.md)：音视频管控服务，用于统一管理系统中接入播控中心的音视频行为。

[投播组件（AVCastPicker）](../harmonyos-references/ohos-multimedia-avcastpicker.md)：可嵌入应用UI界面的系统级投播组件。用户点击该组件后，系统将执行设备发现、连接和认证等流程，应用仅需通过接口获取投播中的相关回调信息。

[投播控制器（AVCastController）](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)：在投播建立后，由应用发起的用于控制远端播放的接口，包括播放、暂停、上一首/下一首切换和播放进度跳转等能力。

## 解决方案

1. 投播场景播控特性。

   参考[播控特性简介](../harmonyos-guides/distributed-playback-overview.md)，使用媒体播控开发投播功能，可以将音视频资源投放到其他投播设备上播放。

   HarmonyOS提供了统一的应用内音视频投播功能设计，通过使用系统提供的投播组件和接口，应用只需要设置对应的资源信息、监听投播中的相关状态，以及应用主动控制的行为（如：播放、暂停）。其他动作包括图标切换、设备的发现、连接、认证等，均由系统完成。
2. 投播组件开发。

   投播组件开发可参考[投播组件开发指导](../harmonyos-guides/distributed-playback-guide.md)，示例代码可参考：[音频投播](../best-practices/bpta-audio-cast.md)，[视频投播](../best-practices/bpta-vdeocast.md)。

   **说明** 

   PCM投播模式下，类似于通过蓝牙等方式连接音箱，无[playbackStateChange](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaybackstatechange10)回调且不依赖此回调同步本地端和远端的播放状态，远端播放状态跟随本地端。而Cast+的Stream模式或DLNA协议投播有[playbackStateChange](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaybackstatechange10)回调，据此同步本地端和远端的播放状态。
3. 扩展屏投播开发。

   参考[扩展屏投播开发指导](../harmonyos-guides/avsession-extended-screen.md)，可以通过[getAllCastDisplays(): Promise<Array>](../harmonyos-references/arkts-apis-avsession-avsession.md#getallcastdisplays12)获取当前系统中所有支持扩展屏投播的显示设备，手动或自动选择预期的扩展屏设备进行扩展屏投播。

   当采用控制中心的[系统无线投屏](https://consumer.huawei.com/cn/support/content/zh-cn16049615/)连接扩展屏时，需要注意：

   * 需要先通过无线投屏连接大屏设备，再通过[getAllCastDisplays(): Promise<Array>](../harmonyos-references/arkts-apis-avsession-avsession.md#getallcastdisplays12)获取当前系统中所有支持扩展屏投播的显示设备并选择对应的设备进行投屏。若无可用扩展屏设备，将会报错[GetAllCastDisplays]castDisplayNum is illegal。[on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void](../harmonyos-references/arkts-apis-avsession-avsession.md#oncastdisplaychange12)用于设置扩展屏投播显示设备变化的监听事件，仅当扩展投播设备变化时可以触发。
   * 扩展屏投播并使用投播组件AVCastPicker的投播，主要依赖于连接扩展屏设备和扩展屏投屏。

## 常见FAQ

Q：不同投播协议支持的投播设备是什么？

A：当前投播本地端支持的投播协议可参考[ProtocolType](../harmonyos-references/arkts-apis-avsession-e.md#protocoltype11)，本端设备支持HarmonyOS 5.0.0及以上版本的手机、平板设备。

不同协议的远端设备限制如下：

Cast+的Stream模式主要适用于HarmonyOS 5.0.0及以上版本的2in1设备、HarmonyOS 3.1及以上版本的华为智慧屏；PCM模式主要适用于投播到[HUAWEI HiPlay设备](https://consumer.huawei.com/cn/support/content/zh-cn16075324/)；DLNA协议为一种较为广泛支持的投播协议，适用于包括华为智慧屏在内的支持标准DLNA协议的设备，三方设备通过实现支持DLNA投播协议的对端播放器适配DLNA协议投播。

本地设备，包括设备本身的内置扬声器或音频插孔、A2DP设备，为非投播设备。

Q：使用投播组件开发投播功能时，APP会调用什么权限或者收集用户的位置信息吗？

A：参考[投播组件开发指导](../harmonyos-guides/distributed-playback-guide.md)，如果使用网络播放路径，需申请相关权限：ohos.permission.INTERNET，该权限与设备发现无关。

若需后台播放，需参考[长时任务使用场景](../harmonyos-guides/continuous-task.md#使用场景)申请对应类型的[长时任务](../harmonyos-guides/continuous-task.md)在后台保活，申请长时任务需要申请ohos.permission.KEEP\_BACKGROUND\_RUNNING权限，配置方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。

投播组件设备上报在系统窗口中，应用获取不到本地和远端设备信息，也不会采集位置信息。

Q：AVCastPicker可以自定义样式吗？

A：AVCastPicker组件可以通过[customPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)属性设置自定义图标样式。其他样式可以参考[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)进行设置。

Q：如何实现直播投播？

A：可以参考投播[开发步骤](../harmonyos-guides/distributed-playback-guide.md#开发步骤)，可以设置[mediaUri](../harmonyos-references/arkts-apis-avsession-i.md#avmediadescription10)来进行类似直播投播的效果。

Q：使用投播组件的时候，如何设置投屏资源的播放初始位置？

A：投屏资源的播放初始位置可以通过[startPosition](../harmonyos-references/arkts-apis-avsession-i.md#avmediadescription10)设置，startPosition表示投播当前进度。注意，直播场景下不应设置播放初始位置或应该设置为0，否则可能投播失败。

Q：视频流是加了referer防盗链可以投播吗？

A：目前不支持投播带有referer防盗链的网络视频。

Q：如何通过有线的方式将HarmonyOS设备屏幕投放到任意电脑上？

A：该场景符合[远程真机平台搭建](faqs-app-debugging-66.md)，开发者利用[HOScrcpy](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy)可以实现HarmonyOS NEXT设备投屏工具、远程真机平台等能力。

* [hosscrcpy-1.0.9-beta.jar](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy/releases)：该jar包工具主要提供HarmonyOS系统下基于视频流的投屏功能，帧率基本持平真机帧率，达到远程真机的效果，同时提供了设备反控的能力，方便开发者将其集成至自己的项目中，可通过[下载jar包](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy/releases)进行集成。
* 集成指导文档及demo请参考[远程真机工具](https://gitcode.com/OpenHarmonyToolkitsPlaza/HOScrcpy)。

Q：如何在连接投播设备后自动关闭AVCastPicker拉起的设备选择页面？

A：当通过[AVCastPicker组件](../harmonyos-references/ohos-multimedia-avcastpicker.md)拉起设备选择页面时，可以通过判断语句选择不加载AVCastPicker组件的方式，使设备选择页面立即消失。当用户选择设备并设备切换成功后触发[on('outputDeviceChange')](../harmonyos-references/arkts-apis-avsession-avsession.md#onoutputdevicechange10)监听，可据此判断是否已成功连接投播设备。

当使用[AVCastPickerHelper](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md)的[select](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)接口拉起设备选择页面时，无法控制自动关闭拉起的设备选择页面。

Q：HarmonyOS的平板设备是否支持作为投播的远端？

A：不支持通过Cast+的Stream模式投播到平板设备。DLNA协议模式可以通过在平板上安装已适配标准DLNA协议的应用用于模拟成DLNA大屏。

Q：使用DLNA协议投屏发现封面不展示是为什么？

A：设置封面依赖于投播对端对[mediaImage](../harmonyos-references/arkts-apis-avsession-i.md#avmediadescription10)或[albumCoverUri](../harmonyos-references/arkts-apis-avsession-i.md#avmediadescription10)的解析，大多三方对端设备不解析封面字段，故当前规格DLNA协议不支持封面展示。

## 总结

系统提供了音视频发声设备统一投播组件AVCastPicker，作为播控中心系统级设备切换、投播能力选择入口。应用可以通过接入统一投播组件，可以实现在应用内及系统播控中心，将音视频资源通过Cast+协议/DLNA协议投播到远端设备或进行发声设备切换。
