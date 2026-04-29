---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/distributed-playback-overview
title: 播控特性简介
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 分布式媒体会话 > 使用投播组件 > 播控特性简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:043f094111deb58ddba517cf4dbb2763861e0b80038c957d29d180464485ff04
---

使用媒体播控，可以简单高效地将音视频投放到其他HarmonyOS设备上播放，如在手机上播放的音视频，可以投到2in1设备上继续播放。

HarmonyOS提供了统一的应用内音视频投播功能设计，通过使用系统提供的投播组件和接口，应用只需要设置对应的资源信息、监听投播中的相关状态，以及应用主动控制的行为（如：播放、暂停）。其他动作包括图标切换、设备的发现、连接、认证等，均由系统完成。

## 基本概念

* **媒体会话（[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)）**

  音视频管控服务，用于对系统中所有音视频行为进行统一的管理。

  本地播放时，应用需要向媒体会话提供播放的媒体信息（如正在播放的歌曲、歌曲的播放状态等），并接收和响应播控中心发出的控制命令（如暂停、下一首等）。具体请参考[本地媒体会话](local-avsession-overview.md)。

  投播时，通过AVSession，应用可以进行投播能力的设置和查询，并创建投播控制器。

  应用可以在启动内容显示（比如：视频播放）时，获取支持投播的扩展屏设备并注册监听，当存在扩展屏时，可在扩展屏上全屏绘制要投播的内容。
* **投播组件（[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)）**

  系统级的投播组件，可嵌入应用界面的UI组件。当用户点击该组件后，系统将进行设备发现、连接、认证等流程，应用仅需要通过接口获取投播中相关的回调信息。
* **投播控制器（[AVCastController](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)）**

  在投播后，由应用发起的用于控制远端播放的接口，包括播放、暂停、调节音量、设置播放模式、设置播放速度等能力。
* **后台长时任务**

  应用实现后台播放，需申请后台长时任务，避免应用在投播后被系统后台清理或冻结。具体参考[长时任务](continuous-task.md)。

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/urGSMGaKS0-Yo-tKToqpFQ/zh-cn_image_0000002558765054.png?HW-CC-KV=V1&HW-CC-Date=20260429T053448Z&HW-CC-Expire=86400&HW-CC-Sign=A9638CD45B8FE588797562EB10CA5A41F7E526845FC4374965B89464D73ACE4A)

* **发现和连接设备**

  用户在应用界面上点击AVCastPicker组件，触发系统发现可用于投播的设备。用户在设备列表中选择对应设备后，系统连接对应设备。应用无需关注设备的发现连接过程，仅需关注设备在远端是否可用。

  应用需要接入AVSession，才可以使用系统提供的统一投播能力，由系统进行设备发现和管理。
* **进入远端投播**

  应用通过AVSession监听设备的连接情况，监听到设备已连接后，可通过AVSession获取一个AVCastController对象用于发送控制命令（如播放、暂停、下一首等）。

  应用在进入远端投播时，应停止本地的播放器，避免本端和远端设备同时播放的情况。同时，建议应用重新绘制应用界面，比如界面变更为一个遥控器，来控制远端播放。
* **在本端控制播放**

  在本端（包括应用内和播控中心）控制播放时，控制命令将通过AVCastController发送，系统将完成数据传输和信息同步，然后更新远端系统预置播放器的状态。
* **在远端控制播放**

  用户同样可以在远端直接控制播放，会直接修改远端播放器的状态。
* **远端播放器状态回调**

  当远端播放器状态变更后，会触发回调，将状态信息返回到本端。应用可以通过AVCastController监听到远端播放器的状态变化。
