---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcastpicker
title: 音视频投播
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 应用接入播控自检 > 应用接入播控检查项详细说明 > 音视频投播
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2ad9d5c835918d5dc4199d9368066cc926632d005bcbff85222a2099dab7642d
---

针对音视频类应用，播控中心提供系统级设备切换、投播能力选择入口，提供音视频发声设备统一投播组件。应用通过接入统一投播组件，可以实现在应用内及系统播控中心，将应用音视频资源通过Cast+协议/DLNA协议投播到远端设备。应用需先按自检要求接入[基础播控](basic-playback-control.md)，才可正常接入音视频投播组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/YRiYu20YSzGExHT1EK9i3g/zh-cn_image_0000002589324933.png?HW-CC-KV=V1&HW-CC-Date=20260429T053450Z&HW-CC-Expire=86400&HW-CC-Sign=054030175098AD33230DEE9D23861C0D0A6EA224200BAB2B85312825AA71DC1A) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/RUstyj40RsqHOuyzD0GbFg/zh-cn_image_0000002589244869.png?HW-CC-KV=V1&HW-CC-Date=20260429T053450Z&HW-CC-Expire=86400&HW-CC-Sign=9FFECA8E3CACF00E05C2804AB8960898AB9858ECB931B25D1FB4F8B2556518AE)

## 基础投播能力

### Cast+协议音视频投播/DLNA协议音视频投播

注意

**自验证关注点：** 播放可投播的音视频资源，点击投播至3.1以上的华为智慧屏/DLNA协议的设备，查看投播功能是否正常可用，且在应用内及系统播控中心内能控制远端投播。

1. 界面是否正确显示Picker。

   如不显示，排查是否按自检要求正确适配了[基础播控](basic-playback-control.md)。
2. 双端设备联网后，是否可以在应用内及播控中心显示可投播设备列表。

   如不显示，排查是否设置了setExtras({requireAbilityList: ['url-cast']})，具体参考[投播开发指南](distributed-playback-guide.md)。
3. 点击可投播设备后，对端设备是否可以正常播放。

   如对端黑屏/不显示播放内容，应用自排查是否正确设置了资源链接，正确调用prepare及start接口，具体参考[投播开发指南](distributed-playback-guide.md)。
4. 投播后，在系统播控中心是否可正常控制远端投播的播放暂停、上下一集、进度控制、音量调节等。

   应用按照实际功能的有无，参照自检表注册必需的控制指令，例如on(type: 'playbackStateChange')来监听播控及远端设备的播放暂停指令，具体控制指令的开发参考[投播开发指南](distributed-playback-guide.md)。

### DRM数字加密视频投播

注意

**自验证关注点：** 播放可投播的DRM数字加密视频资源，点击投播至3.1以上的华为智慧屏，或支持DRM硬件解码的大屏设备，查看投播功能是否正常可用。

## 投播能力增强

### 镜像投屏自动切换资源投播

注意

**自验证关注点：** 在控制中心发起无线投屏后，在应用内播放可投播的音视频资源，查看是否自动切换为资源投播模式（Cast+协议音视频投播/DLNA协议音视频投播）。

用户通过“无线投屏”功能实现手机等设备和大屏等的镜像投屏，然后打开视频应用进入视频播放，此时应用需切换到资源投播。具体实现可参考[镜像投屏自动切换资源投播](distributed-playback-guide.md#镜像投屏自动切换资源投播)。
