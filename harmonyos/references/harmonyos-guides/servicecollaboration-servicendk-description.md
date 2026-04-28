---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-servicendk-description
title: 跨设备互通NDK特性概述
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > 跨设备互通NDK（C） > 跨设备互通NDK特性概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:498a70cad945bf44dfbe6203c8c0ac8bafa41a7112df61ded088f2cb7cdb3216
---

跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，TV、平板或2in1设备可以调用手机的相机、扫描、图库等功能。

说明

本章节以拍照为例展开介绍，扫描、图库功能的使用与拍照类似。

用户在TV、平板或2in1设备上使用富文本类编辑应用（如：备忘录、邮件、笔记等）时，想要拍摄一些照片作为素材，但是当前设备拍摄不太方便。通过跨设备互通-拍照，用户可以在当前设备的应用中指定平板或手机设备，并打开平板或手机的相机来拍摄所需的素材。通过手机或者平板设备拍摄，移动更便利、取景更灵巧、相机能力也更强大。拍摄的照片将实现快速回传到TV、平板或2in1设备的应用中，帮助用户高效完成图文并茂的文档设计。

如果同一组网下有多台手机或平板设备，用户可以选择不同的设备进行拍摄。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/b13TDM0RQAWCUktpu7X5hw/zh-cn_image_0000002583438477.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234409Z&HW-CC-Expire=86400&HW-CC-Sign=844836ACB2F68DE35C9FAA0042A3E12414183277D24607EA5E87A5560DA4EEEA)

## 运作机制

基于分布式协同框架面向跨设备拍照的业务场景，为您提供了 [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)（设备列表接口）、[HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)（跨端拍照、扫描、拉起图库选择图片）或[HMS\_ServiceCollaboration\_StartCollaborationV2](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)（跨端拍照、扫描、拉起图库选择图片和视频）和 [HMS\_ServiceCollaboration\_StopCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration)（终止跨设备互通）四个接口。只需要调用这四个接口，即可完成跨设备互通，无需关注分布式场景下数据传输、指令控制等具体细节。

1. **系统分布式协同框架跨设备自动建链**

   a. 通过系统的分布式协同框架，同账号下的本端设备（2in1设备/平板）与远端设备（手机/平板）自动建立连接。系统将自动完成设备的发现、连接、认证等流程，通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)接口提供可用的具有相机、扫描和图库能力的远端设备信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/b_F-TINdT8Wzr4FaSZvLvg/zh-cn_image_0000002552958436.png?HW-CC-KV=V1&HW-CC-Date=20260427T234409Z&HW-CC-Expire=86400&HW-CC-Sign=5F4F4828A56845A3260416E3CE4CEEF4ED9D0B06F7FFC379D0743359A4C3C3D4)

   b. 通过[HMS\_ServiceCollaboration\_StartCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)或者[HMS\_ServiceCollaboration\_StartCollaborationV2](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)拉起对应跨设备互通能力，通过[HMS\_ServiceCollaboration\_StopCollaboration](../harmonyos-references/servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration)终止跨设备互通能力。分布式协同框架会将远端拍摄状态信息实时回传到应用侧，应用侧会根据错误码做相关提示。

   拍摄状态可能为：对端设备拍摄中、图片导入中、协同失败、本端WLAN未开启、双端WLAN或者蓝牙未开启。具体拍摄状态提示可由应用选择绘制，对应提示信息参考[ServiceCollaborationEventCode](../harmonyos-references/servicecollaboration-capi-module.md#servicecollaborationeventcode-1)。

   | 对端设备拍摄中 | 图片导入中 | 协同失败 | 本端WLAN未开启 | 双端WLAN或者蓝牙未开启 |
   | --- | --- | --- | --- | --- |
   |  |  |  |  |  |
2. **用户使用远端设备拍照**

   1. 用户使用远端设备完成拍照并确认，照片将回传到本端设备的应用，完成整个流程。
   2. 远端设备将自动退出相机界面，回到初始状态。
