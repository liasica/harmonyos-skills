---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/playback-control-access-checklist
title: 应用接入播控自检表
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 应用接入播控自检 > 应用接入播控自检表
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc9b278f96950c29c2f38817c2ba9d6fba7566a74f8da537b74e99c294bb5f3f
---

如接入AVSession，请按照下表根据应用的业务场景接入，应用上架前请根据此表格自检，以确保应用的体验。

如果应用包含在后台/锁屏状态下播放音频等业务场景，开发者需要规范[接入AVSession](avsession-access-scene.md)；如应用仅需在前台播放音视频，开发者可选择不接入AVSession。

## 基础播控-播放信息

应用按类型区分，需要正确接入所有必接项（√ ），部分功能不强制接入（-），应用可以根据实际需要选择性接入。

说明

对于必接项，应用按照实际功能的有无进行判断，若本身具备接入条件则需要接入；如本身没有该功能，可不接入。

| 功能 | **音乐类/听书类** | **视频类** | **直播类** | **浏览器类** | **新闻阅读类** | **Voip类** |
| --- | --- | --- | --- | --- | --- | --- |
| [媒体封面](basic-playback-control.md#媒体封面) | √ | √ | √ | √ | √ | - |
| [主标题](basic-playback-control.md#主标题) | √ | √ | √ | √ | √ | - |
| [进度与时间](basic-playback-control.md#进度与时间) | √ | √ | - | √ | √ | - |
| [副标题](basic-playback-control.md#副标题) | √ | √ | √ | √ | √ | - |
| [滚动歌词](basic-playback-control.md#滚动歌词) | √ | - | - | - | - | - |
| [媒体音源特殊标识](basic-playback-control.md#媒体音源特殊标识) | - | - | - | - | - | - |

## 基础播控-播放控制

应用按类型区分，需要正确接入所有必接项（√ ），部分功能不强制接入（-），应用可以根据实际需要选择性接入。

说明

对于必接项，应用按照实际功能的有无进行判断，若本身具备接入条件则需要接入；如本身没有该功能，可不接入。

| 功能 | **音乐类/听书类** | **视频类** | **直播类** | **浏览器类** | **新闻阅读类** | **Voip类** |
| --- | --- | --- | --- | --- | --- | --- |
| [播放/暂停](basic-playback-control.md#播放暂停) | √ | √ | √ | √ | √ | - |
| [上下一首/集](basic-playback-control.md#上下一首集) | √ | √ | - | - | - | - |
| [按钮置灰](basic-playback-control.md#按钮置灰) | √ | √ | √ | √ | √ | - |
| [点击播控卡片跳转应用指定页面](basic-playback-control.md#点击播控卡片跳转应用指定页面) | √ | √ | √ | √ | √ | - |
| [收藏](basic-playback-control.md#收藏) | √ | - | - | - | - | - |
| [循环模式](basic-playback-control.md#循环模式) | √ | - | - | - | - | - |
| [快进/快退](basic-playback-control.md#快进快退) | - | √ | - | - | - | - |

## 音视频投播

应用按类型区分，需要正确接入所有必接项（√ ），部分功能不强制接入（-），应用可以根据实际需要选择性接入。

说明

对于必接项，应用按照实际功能的有无进行判断，若本身具备接入条件则需要接入；如本身没有该功能，可不接入。

| 功能 | **音乐类/听书类** | **视频类** | **直播类** | **浏览器类** | **新闻阅读类** | **Voip类** |
| --- | --- | --- | --- | --- | --- | --- |
| [通话设备切换组件](using-switch-call-devices.md) | - | - | - | - | - | √ |
| [Cast+协议音视频投播](avcastpicker.md#cast协议音视频投播dlna协议音视频投播) | √ | √ | - | - | - | - |
| [DRM数字加密视频投播](avcastpicker.md#drm数字加密视频投播) | - | - | - | - | - | - |
| [DLNA协议音视频投播](avcastpicker.md#cast协议音视频投播dlna协议音视频投播) | √ | √ | - | - | - | - |
| [镜像投屏自动切换资源投播](avcastpicker.md#镜像投屏自动切换资源投播) | - | - | - | - | - | - |
| [应用内投播组件](distributed-playback-guide.md)（半模态） | √ | √ | - | - | - | - |

## 播控增强

应用按类型区分，需要正确接入所有必接项（√ ），部分功能不强制接入（-），应用可以根据实际需要选择性接入。

说明

对于必接项，应用按照实际功能的有无进行判断，若本身具备接入条件则需要接入；如本身没有该功能，可不接入。

| **功能** | **音乐类/听书类** | **视频类** | **直播类** | **浏览器类** | **新闻阅读类** | **Voip类** |
| --- | --- | --- | --- | --- | --- | --- |
| [播放按钮一键冷启动播放](quick-playback.md#播放按钮一键冷启动播放) | √ | - | - | - | - | - |
| [历史歌单](quick-playback.md#历史歌单歌单推荐) | √ | - | - | - | - | - |
| [歌单推荐](quick-playback.md#历史歌单歌单推荐) | √ | - | - | - | - | - |
| [统一音量组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md) | - | √ | - | - | - | - |

## 示例代码

* [基础播控与播控增强](https://gitcode.com/HarmonyOS_Samples/media-provider)（示例工程）
* [通话设备切换组件](https://gitcode.com/HarmonyOS_Samples/avcastpicker-for-call)（示例工程）
