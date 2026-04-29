---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4cffe3d8b6fb584d76c6855c27fa58e0dcd40fb980c6dae9a99152acddd2fe96
---

华为数字车钥匙依托华为钱包数字车钥匙业务集成方案，基于华为手机“芯-端-云”一体化的安全能力，且满足ICCE标准，可快速实现手机模拟车钥匙的功能。

相较于传统的车钥匙，华为数字车钥匙无需借助车钥匙实体，仅将车钥匙功能集成在移动智能终端设备中，基于SE、TEE等安全功能，使用蓝牙、NFC技术连接手机和车，即可实现车辆的开门、启动等功能。

说明

此方式当前仅支持中国境内（不包含中国香港、中国澳门、中国台湾）。

## 整体架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ioqhu-mcQOuLLjG-_mSd0Q/zh-cn_image_0000002589245507.png?HW-CC-KV=V1&HW-CC-Date=20260429T054043Z&HW-CC-Expire=86400&HW-CC-Sign=D3C7E5FDD1477D76A6C83A5432E9C77EEB6E86A300E671132154F3C26495CCB5)

### 按照参与各方的角色说明

| 角色 | 角色描述 |
| --- | --- |
| DK（Digital Key） | 数字钥匙 |
| 车钥匙Applet | 华为提供安全通道供车厂将密钥以及车厂独有的数据写入Applet实例。 |
| BLE | 低功耗蓝牙 |
| NFC | 近场通信 |

### 典型的交互流程

用户持手机在车主APP申请开通车钥匙：

DK业务管理服务将钥匙卡片信息通过钱包云服务器传递给华为钱包，同时写入到手机安全芯片的车钥匙Applet实例。

车辆和移动终端的通信方式：

* 车辆NFC模块（通常位于主驾后视镜，主驾B柱），使用NFC通道和终端设备安全芯片通信。
* 车辆BLE模块，通过蓝牙通道，使用终端设备上的华为钱包和终端设备的安全芯片通信。
