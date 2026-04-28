---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与手机碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f6dbf9534caf2abb194faf22a0720fe901cf5e27ea8b16c443aae01f5e6e4e0
---

Share Kit推出碰一碰分享，支持用户通过碰一碰发起跨端分享，可实现传输图片、共享Wi-Fi等。

## 场景介绍

* 宿主应用进入一个可以分享的界面，比如打开或者选中的一个文件、一条备忘录、一个联系人详情，或个人热点/Wi-Fi等。
* 宿主应用可以分享多个内容，如选中的多张图片等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Nmz6XQINQNOvaaOGanitzA/zh-cn_image_0000002583439221.gif?HW-CC-KV=V1&HW-CC-Date=20260427T235101Z&HW-CC-Expire=86400&HW-CC-Sign=3551750806D6F0906F6F62F1A8D72E7855E1FC8C34CCEC8BB0B21F5DEE543099)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/5t3aCkQtS12QNhxSyLO_Ng/zh-cn_image_0000002552959182.png?HW-CC-KV=V1&HW-CC-Date=20260427T235101Z&HW-CC-Expire=86400&HW-CC-Sign=C6D7C0D1A0B57C40E78007364EC5E74C13ED32B03D61BF85A658967ABB0F951E)

流程说明：

1. 宿主应用注册碰一碰分享事件，并与亮屏且解锁的对端设备碰一碰。
2. 宿主应用发现设备，调用碰一碰分享事件回调，在回调事件中构造分享数据并发送。
3. 目标设备接收并处理分享数据。
4. 宿主应用解除注册碰一碰分享事件。

## 使用约束

手机应用发起碰一碰分享时，双端设备需要在**亮屏、且解锁**的状态下并且都已开启华为分享服务（系统默认开启），设备顶部轻碰即可触发。如果用户已手动关闭华为分享服务开关，轻碰事件触发时，用户会接收到系统通知提示开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/tStYsE6hQ0a4C9cK1IxeWQ/zh-cn_image_0000002583479183.png?HW-CC-KV=V1&HW-CC-Date=20260427T235101Z&HW-CC-Expire=86400&HW-CC-Sign=76C215C5B93141B82B5969EA44DBCD330FA71264119289969E4104E7B31BCFC1)

Share Kit的处理机制：

* 任意一端设备不支持碰一碰能力时，轻碰无任何响应。
* 宿主应用无法获得分享结果，Share Kit会通过系统通知消息告知用户对端接收或拒绝。

## 环境要求

* 支持的手机系统：[HarmonyOS NEXT Release](../harmonyos-releases/overview-500.md#section62333015377)及以上版本，可使用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)判断系统能力是否支持。

  ```
  1. if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
  2. // 支持一碰分享的能力.
  3. }
  ```
* 集成开发环境：[DevEco Studio NEXT Beta1](../harmonyos-releases/overview-500.md#section1457031563711)及以上版本。
