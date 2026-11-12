---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:564908596abfaabd889c8c48a08d577485dc0eb113ee930184b9386386a96042
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/AGocrn2xQJC1DB_ddwfM0Q/zh-cn_image_0000002786520520.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=71DDE5649FD83C1C4AB3E2BE7C70FE1CC1FDBDA8E0E109B961E26C36315EF5A9)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/JfyoPmOvQDq5U-ycAlM5fA/zh-cn_image_0000002786360604.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=25C9ECDF2B14B5C61605D55B8E3D1DC1F2C5DB99146F2389778E6BBE3AAFDFF6)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/UYuLt_yBRwmrGL3UTOFsdg/zh-cn_image_0000002815560025.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD9E0CF3EAFC9472DCA72BCFA5E9770114A36B54C63B5A9CDF8A4CEE2A6EE9F0)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/qEbDJWB6QGGV7YcMCloN7w/zh-cn_image_0000002815400109.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=24CB46A0001AE744BACBC5781BBB460C369DD9E78CBAEAFC6447B02AA545857A)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/QAXqxVdYTQO3pxt6ar_RKw/zh-cn_image_0000002786520534.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A843F68CCF6DDEB764E4A9B5569F7BDD371F342883A026A4C376339D6451686)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/CORnFpSeSLmcTzzOQb_q2w/zh-cn_image_0000002786360606.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=11E4020153AAA2F2D59E13968AEA47C15E4CC762D6D55FE1B90D781EA6CE02E3)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/8VWQ0gBrT_id4i33ZfxpzQ/zh-cn_image_0000002815560027.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E82D86BDF83A83DCB89FD27C3BB5A2ED284D8CA3FF06607C3BFC71701806A1B)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KovIHC-hR5KgbFDMaTWEsw/zh-cn_image_0000002815400111.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA90D250935B842C24DF3039971C12BBD0BD24058440D204E8C4E4526CC5CBC8)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
