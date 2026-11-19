---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c26a2e2219a684daa0c4867b89e9a4e22d12704f8394fa29941ccc004e0610f
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/mcossPRYQcy_acaSA0oOzQ/zh-cn_image_0000002791566654.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=35D9FB80E28E73F8AB2EC262914AB733B87BFD681FFD2215F4B1497B84830BAC)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/vow6CyebSCOgR-RlRj6LRw/zh-cn_image_0000002820526619.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=F16051B6352D726E45C300AACE8E680532BE624C53CC192EC72D7E7175E21710)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/IoVco_2FRWafo7YDg_GKKQ/zh-cn_image_0000002820406619.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=A453094D08A913E68005D0E080407427FC6881B117E94641BD155DF002868AE7)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/vF4-O7s6RziDK8smoZWy5A/zh-cn_image_0000002791726640.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=21678A5BAF50359F19B67D43CA78F0BE7B8EDAC66B0E6FF59B98522C261AB515)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/7jJyrrkIRJigohB6c1T7vA/zh-cn_image_0000002791566668.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=81B0584A819311EB42AB039FA6229FBF1389028358DEB2C7C6B53AA06E3E4947)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/NL3MOhJDTeeqBBLl5wiIXw/zh-cn_image_0000002820526621.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=49A2735A2FB4A53BD417117CAD7C8E2D77CEE8D5685D3490F9BEE8C501378B12)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/vXD50bymQCGQUiVMc56bYg/zh-cn_image_0000002820406621.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=0902533E6E0469BBC486566E7D5F5A9DB3E1857231E69A7D9A05AF402D0D4440)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/jg4J0XIcRJKG0qRgjHxkCw/zh-cn_image_0000002791726642.png?HW-CC-KV=V1&HW-CC-Date=20261119T014913Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BD7C6252BEE8CD4648475DAC4AE3EB9C7ADF43B60C265E96AE357C9683F35B5)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
