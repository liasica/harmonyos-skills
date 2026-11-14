---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/knock-share-pc-phones-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 碰一碰分享 > 手机与PC/2in1碰一碰分享 > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b8098c6a88df5389c32a21e11ba03ddfc6f9aa3bd8222e5a9c39ff252de52b8
---

## 场景介绍

Share Kit支持Phone和PC/2in1之间的碰一碰分享。利用PC/2in1设备的屏幕感知能力，识别Phone轻碰屏幕的动作及位置，实现PC/2in1窗口级的交互。

**从6.1.0(23)版本开始，支持Phone与Tablet设备之间的碰一碰分享。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/i_t9XoXOScS5M3GN3gZdFQ/zh-cn_image_0000002788468268.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE3E1977DE9787C9E8CDDAFBB363703509E50E2291A1CF5FCB3F07EFB55F1E58)

## 业务流程

* PC/2in1设备作为数据接收端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/68whRrlZSmqv1p6F6gnLQw/zh-cn_image_0000002817507769.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=065D90C5AD251FE70EE88EB53104ED1657CABAABB9A73A406F03FDB9D81B17DA)
* PC/2in1设备作为数据发送端

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/B9__zQjlTyKeih0byiClKg/zh-cn_image_0000002788308338.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=25C8364381AA403ADA8AEF99F4646384187161A5922E81995349D2E03FDD3733)

## 双向分享限制

从6.0.0(20) Beta5版本开始，手机与PC/2in1设备之间不支持双向分享。遵循以下机制：

* 当手机前台有可分享内容时，无论PC/2in1设备前台窗口是否有可分享内容，优先将手机作为发送端，PC/2in1设备作为接收端。
* 当手机前台无可分享内容且PC/2in1设备前台窗口有可分享内容时，PC/2in1设备作为发送端，手机作为接收端。
* 当手机前台和PC/2in1设备前台窗口均无可分享内容时，遵循无内容分享逻辑。

对于6.0.0(20) Beta3及之前的版本，当手机前台和PC/2in1设备前台窗口均有可分享内容时，支持双向分享（发送分享内容的同时也可接收到分享内容）。

## 使用约束

* 手机与PC/2in1设备间碰一碰分享需登录相同的华为账号。
* 仅支持直板手机或折叠手机直板态与PC/2in1屏幕碰一碰分享。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/VmVfzWljSjG8ACOdLMOr3w/zh-cn_image_0000002817427701.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=4362F2B2DDE2E6D836F8D56FFF6BE43BB61F6F0968E381932AE3AB2CB8D90478)
* 轻碰屏幕交互约束：

  + 手机与PC/2in1屏幕俯视夹角应≤5°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/5LPsVx5eTXmpSrzEZFC_vQ/zh-cn_image_0000002788468282.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBFC698184801EBC233061D2A5104EB33533F7B437247FDB4E10C27B36421015)
  + 手机与PC/2in1屏幕侧视夹角应＞35°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/JHuaKy-KQFGiUDr8joMBQQ/zh-cn_image_0000002817507771.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=95FB5FEDFF29123992A37CDC12F82AD973C7DA75521DD34E724EE7965449BD24)
  + 手机与PC/2in1屏幕正视夹角应≤25°。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/e7CLMqRrS9GBfRswYJqvTA/zh-cn_image_0000002788308340.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B8FF34943627E33C8F0F79C9C5C39D8677A38AE788E19C9E266677573503CE8)
  + 手机不能超出PC/2in1设备屏幕。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/FKBQ4EJJRD23e4nmT9DBNg/zh-cn_image_0000002817427703.png?HW-CC-KV=V1&HW-CC-Date=20261114T004648Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3346A658B867EAEA633ABB44B859F1E641CF171CBCB64BBA69DD763AA72E4B5)
* 支持官方手机保护壳，不支持过厚的手机外壳。

## 环境要求

* 支持的PC/2in1系统：[HarmonyOS 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。
* 集成开发环境：[DevEco Studio 6.0.0 Beta1](../harmonyos-releases/overview-600.md#section1836613212578)及以上版本。

## 代码示例

* PC/2in1作为发送端接入参考：[发送分享数据](knock-share-between-phones-content.md#发送分享数据)
* PC/2in1作为接收端接入参考：[分享内容直达应用界面](knock-share-pc-phones-sandbox.md)
