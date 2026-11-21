---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1462e313e1a8991669c0de2e3b3bbc156fccc87fc756b150d0d268b453442dcc
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/e3vup-QFRNaDgIikTHLk7A/zh-cn_image_0000002792878308.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6267675CC99E2DDA60C4FF76084E251E29286487D3A74A17879C5CA9903CE91)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/wyd1WYfDRAm-8Hz7Hr-ifA/zh-cn_image_0000002821838227.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=9292FC5F4770FA65C78A0C353BED68C4B01577A8E297371403D11F9B03C3946B)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/rTjtHJ6HSFC-vTqvEfXwJg/zh-cn_image_0000002821758229.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=13F484EE643C24717EADF135C04403C59F0AFC70E4F483C313FD11836F67CDB8)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ZaoAvM1YSxWvkUsRJHuYxA/zh-cn_image_0000002793038292.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=72332A094C15BC9DD90ABC4B424BD8C7FC4B5B1B2246233FEDFA6CB1021B8C28)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/k6rd6Ig_SxSVZsJYTJyK0Q/zh-cn_image_0000002792878322.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C40B54B2174165FBE996C6F49D13ED191ED362A8E762EB1764FDCD2E0AFAA3F)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/cVZUMk4OSvqA80Z3GhtKjA/zh-cn_image_0000002821838229.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD4B150F417B01B2AAD5A7827C52FFFDB61197C20940190BAF1B992CCD1FEB2E)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/wJJoR83ATUmQo5HrIfWitA/zh-cn_image_0000002821758231.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=08F96F57851AAAC6F79150214F65DF299FC9060A39655D9F61F605665C142381)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/cmE9nL0kSR-_n22hhrapnQ/zh-cn_image_0000002793038294.png?HW-CC-KV=V1&HW-CC-Date=20261121T011240Z&HW-CC-Expire=31536000000&HW-CC-Sign=111D210543F46C8D4C735C2AE4932D23DDC56666FD15F61BB86798624AED0EE1)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
