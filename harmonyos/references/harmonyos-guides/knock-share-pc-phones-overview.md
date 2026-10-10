---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-10-11T07:22:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4365e4c10210d70cc553ac716cec2fc6f09e3b717ce59846a95b2989c9404ab8
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/rfuOUx0nQkG_VY72HNRo-w/zh-cn_image_0000002784583763.gif)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/yBwix1OhSXew5gTgWXJ7dw/zh-cn_image_0000002784663955.png)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/qFnon4O1Sq-ds7jbDxqk9g/zh-cn_image_0000002755025022.png)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/9Cyk9CGwSVGCWsM6uKPOEQ/zh-cn_image_0000002755184910.png)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4JR-DrWtRkaqSv6qkRmhYQ/zh-cn_image_0000002784583777.png)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/tLCYu_qSRn6QGjA5SaIUYQ/zh-cn_image_0000002784663957.png)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/yw0vvau1SEaD9Vf0OZjLtg/zh-cn_image_0000002755025024.png)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4MN3HWpDTKCLTZI526EjMQ/zh-cn_image_0000002755184912.png)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
