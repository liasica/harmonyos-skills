---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vibrator-overview
title: 振动开发概述
breadcrumb: 指南 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > 振动 > 振动开发概述
category: harmonyos-guides
scraped_at: 2026-09-15T07:02:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bc51182238a3869af65cf2e5e097360fd6f3ff8f30a12db99c0f39762904be7d
---

通过最大化开放马达器件能力，振动器模块服务拓展了马达服务，实现了振动与交互融合设计，从而打造出细腻精致的一体化振动体验和差异化体验，提升用户交互效率、易用性以及用户体验，并增强品牌竞争力。

## 运作机制

Vibrator属于控制类小器件，主要包含以下四个模块：Vibrator API，Vibrator Framework，Vibrator Service和HDF层。

**图1** 控制类小器件中的Vibrator

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/o7o3n1TwQ7mAlgBvskv3IA/zh-cn_image_0000002723695560.png)

* Vibrator API：提供振动器基础的API，主要包含振动器的列表查询、振动效果查询、触发/关闭等接口。
* Vibrator Framework：实现振动器的框架层管理，实现与控制类小器件Service的通信。
* 控制类小器件 Service：实现控制器的服务管理。
* HDF层：适配不同设备。

## 约束与限制

在使用振动器时，开发者需要配置请求振动器的权限ohos.permission.VIBRATE，才能控制振动器振动。
