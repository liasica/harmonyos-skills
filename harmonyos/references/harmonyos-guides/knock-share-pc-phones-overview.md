---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-10-15T07:05:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b369c605f156649120ce9eadbec0a2b4ba56dd0fcb998338ccd1a5e3c1e35fd5
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_lZ0zvEySmqW0gIGPA9KvA/zh-cn_image_0000002791860085.gif)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3MGc0tpbT4KzblW21AbGMA/zh-cn_image_0000002762501222.png)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8gb0sLXCSuKDeZxnBkjkYg/zh-cn_image_0000002791739881.png)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/3jAW9TKvSOi56sh18MyHSw/zh-cn_image_0000002762341302.png)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ah3QG8DTRh6UZa7QbjjblA/zh-cn_image_0000002791860099.png)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4wi-GpInQNG02l-F_VwTPQ/zh-cn_image_0000002762501224.png)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/yJsNfeL5Q02C2PC5NJkYUA/zh-cn_image_0000002791739883.png)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/1LIyCZtuRhCpPgeupBLQDw/zh-cn_image_0000002762341304.png)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
