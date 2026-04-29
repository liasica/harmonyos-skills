---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/applinking-introduction
title: App Linking Kit简介
breadcrumb: 指南 > 应用服务 > App Linking Kit（应用链接服务） > App Linking Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7aa5f9806a10ba9e04b78e4568a28b753326c5c88148a9e4f32a4ad4a90de3d
---

App Linking Kit（应用链接服务）提供了一系列增强的链接特性。

* App Linking Kit支持[通过App Linking应用链接拉起指定应用](app-linking-startupapp.md)，实现应用间跳转。当应用已安装时，优先通过应用展示内容；若应用未安装，则通过系统浏览器展示网页版内容。

  在此基础之上，还可以实现直达应用市场能力、延迟链接能力这类有竞争力的特性，大大增强了App Linking的能力，使得链接跳转体验更佳，链接转化率更高。

  + [通过直达应用市场能力跳转至应用市场下载详情页](applinking-direct-to-ag.md)：当应用未安装时，App Linking的默认行为是通过系统浏览器打开链接对应的网页。通过App Linking Kit的直达应用市场能力，可以实现在应用未安装时直接跳转应用市场，省去了中转的步骤，使跳转体验更流畅。
  + [通过延迟链接跳转至应用详情页](applinking-deferredlink.md)：当用户点击应用推广链接时，若应用未安装，系统会将用户的点击信息自动缓存十分钟。当用户随后安装并启动应用时，仍可获取之前的点击参数，避免转化率损失，提升体验。
* App Linking Kit支持[通过聚合链接按指定方式跳转至应用](applinking-cross-platform.md)。当用户在HarmonyOS系统中点击聚合链接时，默认通过系统浏览器打开深度链接地址。通过聚合链接能力，可以引导用户跳转到HarmonyOS平台预览页、应用市场详情页、自定义网址、深度链接地址等页面。

## 适用场景

* 适用于应用的[扫码直达](scan-directservice.md)、社交分享、沉默唤醒、广告引流等场景。
* 适用于对安全性要求较高的场景，避免出现被其它应用仿冒的问题。
* 适用于对体验要求较高的应用，不管目标应用是否安装，用户点击该链接都可以正常访问。

## 典型案例

### 碰一碰视频分享

随着全场景智慧生活的不断演进，跨设备内容分享已成为用户的核心需求之一。传统分享方式普遍存在操作繁琐（需手动选择设备或应用）、依赖特定网络环境、传输效率低等问题，影响了用户体验。HarmonyOS提供的[Share Kit（分享服务）](share-introduction.md)结合App Linking Kit技术，能够实现内容的快速跨设备分享，直达目标应用，无需依赖第三方应用中转，提供高效、便捷、无缝的分享体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/1dGWHh8KR92bJzSCQR3Aag/zh-cn_image_0000002558765298.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053729Z&HW-CC-Expire=86400&HW-CC-Sign=7529C6533D435EAB5AAF84976325D303BC2D609D056491B3258A14A298BD7ECD)

### 游戏碰一碰快速组队

在《多乐中国象棋》这款组队竞技类游戏中，玩家只需轻轻碰触两台设备，即可实现秒速组队，省去了传统邀请流程中的繁琐操作，一步直达指定页面。与传统的通信软件邀请流程相比，操作步骤大幅减少。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/zGROEeaBQ7KLWvQqWMN1cg/zh-cn_image_0000002558605642.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053729Z&HW-CC-Expire=86400&HW-CC-Sign=BC9184E23404931EFC50A9F0C53470E621236D905C91F39AB2EB07F2B2176835)

### 通过扫码使服务快速触达用户

美团App结合App Linking技术，实现用户无需打开App，通过系统扫码即可直接解锁共享单车。在负一屏、控制中心、系统相机中均可解锁，相比打开App扫码，操作入口增加了3倍，一步扫码直达，操作效率提升了30%以上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/jiHwYkB2SNa1wKO0RshCWA/zh-cn_image_0000002589325169.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053729Z&HW-CC-Expire=86400&HW-CC-Sign=14C69D643F7369569C0C65FDAEB10579D83B0606A93BE4C51CB2652312C50F2A)

## 约束与限制

### 支持的设备

| 能力 | 支持设备 |
| --- | --- |
| 应用链接 | Phone、Tablet、PC/2in1、TV |
| 直达应用市场 | Phone、Tablet、PC/2in1 |
| 延迟链接 | Phone、Tablet、PC/2in1 |
| 聚合链接 | Phone、Tablet、PC/2in1 |

### 支持的国家/地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的签名方式

当前仅支持[手动签名](ide-signing.md#section297715173233)。

## 模拟器支持情况

本Kit暂不支持模拟器。
