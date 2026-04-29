---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-between-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与手机碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:371782f9e69f7bb6981d0da53537e61982644687ac719e15e0c3625a3847a5b1
---

Share Kit推出碰一碰分享，支持用户通过碰一碰发起跨端分享，可实现传输图片、共享Wi-Fi等。

## 场景介绍

* 宿主应用进入一个可以分享的界面，比如打开或者选中的一个文件、一条备忘录、一个联系人详情，或个人热点/Wi-Fi等。
* 宿主应用可以分享多个内容，如选中的多张图片等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/rnDUOUaBRqWZZyBdsb6b6w/zh-cn_image_0000002589325547.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=7AACC36DC634C24937D9E5B27C32613E928A711C5DC358FE289F4EF76B029AD0)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/dH7Y9D94SRSztXpvQQ3hiw/zh-cn_image_0000002589245491.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=51D576CFCA29765047D6466AD8C1C8DF61E78CC35E65B35F64E1577719BFD245)

流程说明：

1. 宿主应用注册碰一碰分享事件，并与亮屏且解锁的对端设备碰一碰。
2. 宿主应用发现设备，调用碰一碰分享事件回调，在回调事件中构造分享数据并发送。
3. 目标设备接收并处理分享数据。
4. 宿主应用解除注册碰一碰分享事件。

## 使用约束

手机应用发起碰一碰分享时，双端设备需要在**亮屏、且解锁**的状态下并且都已开启华为分享服务（系统默认开启），设备顶部轻碰即可触发。如果用户已手动关闭华为分享服务开关，轻碰事件触发时，用户会接收到系统通知提示开启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/vSkB56y5SP6tgPH5a2wMNg/zh-cn_image_0000002558765684.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=CD62B807CBBFE99933E06B15315732FAC25B8ED7ADC2B9337AF188C484ECD06F)

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
