---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:850256d5ed2370aab7dea721d77f26bbf89af418b4e92b0f63d18b3205cadcce
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/P1it9LtlQDuNxtgkfNBMhg/zh-cn_image_0000002552959176.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=54F9C334261B1A2D65696F7B085B58C5D5794D127B6CBD782E7A5E59F44425D9)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mUMGTMc_Qn2-DvenjlJAdA/zh-cn_image_0000002552799540.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=73D5F8DD08A529309B038A88952C17ECAC54772FD6A74879AFCBA4CA7D4C5F7E)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/m6HDF1ydQP6R4arKxz_3ww/zh-cn_image_0000002583439235.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=B5B7BD3CE6BCA2621C2473364CAB2C0856197467C5943518C90548792496DC20)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/e3-z4DZWT3mBU4Hx0QB4bg/zh-cn_image_0000002552959190.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=CE688AB4A860733DAE8656F301C644517359F2D3A389C9548764EB18A3C5CD93)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Vtp2xzGBQUCOyRD8G5q20w/zh-cn_image_0000002583479191.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=9D50F481771637B66847F4E1E1F95805AD347242443BCB3C09E456DE6ACD8EC3)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/QU2feIIWQOyTiMcvNQokSA/zh-cn_image_0000002552799542.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=964087C2680464E5049087B36EEF8E3E5A0E96F9C4B1DFF0F68D4D1EE94A10A7)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/gdALnEThQdy19F6e71ddhg/zh-cn_image_0000002583439237.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=0DF5093E929D921EAB5885939D56DB60DF1750233C8371F51C8041055FCB7CD2)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/kjdbwvpSTUG4PY9jvUUZkA/zh-cn_image_0000002552959192.png?HW-CC-KV=V1&HW-CC-Date=20260427T235102Z&HW-CC-Expire=86400&HW-CC-Sign=27A0E9E01F81AF641CCD9AE7D464934C00EB99A8260941B3ED9768265A171D8A)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
