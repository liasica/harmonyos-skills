---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07c3c780f831872a3676c62143f77f1454aa10bef2cacc4c73a2fa297885d5a7
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/cGsmPR0CQ8a1zuMb3SXDGA/zh-cn_image_0000002589245485.gif?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=74BF8F14B01B6A8D85A889D3ED3FCD9165CB9362332CCA208CA4C467B8E03E6F)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/cFVcug7NTpmxWQgtDlr0wg/zh-cn_image_0000002558606034.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=531D2060905586A03E3C5559D7E522A4393F6589D9E967C35FF7F809806C015A)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/7tgxfBCiRUWFlSyFoEIWxg/zh-cn_image_0000002589325561.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=9397576FB609F8EBD481371B3A6C8395C45B0E8F1E07997A8FAF5A519DD23D2C)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/AR4NU1rFQbScldMYhBLXpg/zh-cn_image_0000002589245499.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=491F0E52D03F192AED4F659015BDD5D1B6D902FD93FDCD4D2B23A317910C40E3)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Klt-FnXqR3aVnYyvoH8OOQ/zh-cn_image_0000002558765692.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=8BCBE2BF05ED97C075F779ED943C032F68F83010C291AD9D60D3B2786679462A)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/phO0u0ceRz-6ShW9QsXrxg/zh-cn_image_0000002558606036.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=2101303010481B476BF73A767A5C2CE5AE5E90EB1E1B73DA3CE2931D2B51309B)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/1zJtM8J0TFukQC4Zz4gd5w/zh-cn_image_0000002589325563.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=E269CC68E5EAE1E16E742F6ED1453E3EB061CBCF2BC20F67FD305672D7AFE52A)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/FihWI7dyQs2OCr5M2ynkIA/zh-cn_image_0000002589245501.png?HW-CC-KV=V1&HW-CC-Date=20260429T054038Z&HW-CC-Expire=86400&HW-CC-Sign=8A4D5EBBA1648D7488DA8DA31714EDC6A77A6A0982C4BCC8814886B08FB2AB92)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
