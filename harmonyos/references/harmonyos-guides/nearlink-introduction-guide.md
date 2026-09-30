---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-introduction-guide
title: 星闪简介
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 星闪 > 星闪简介
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:6388b4dd85d70866352474cff72b042991571a34eaa84ee434375e6945a6b9ae
---

星闪（NearLink）提供一种低功耗、高速率的短距离通信服务，支持星闪设备之间的连接、数据交互。

星闪通信中设备分为中心设备与外围设备两种角色：中心设备主动发起扫描，发现并连接正在广播的外围设备；外围设备通过发送广播宣告自身，被中心设备发现并连接后，即可进行相应的数据传输。设备角色并非固定，同一设备可根据业务场景担任不同角色。

可能的使用场景有：

* 中心设备和外围设备（鼠标）通过星闪配对连接后，使用鼠标作为输入控制中心设备。
* 中心设备和外围设备（手写笔）通过星闪配对连接后，使用手写笔作为输入控制中心设备。

## 约束与限制

星闪服务适用于Phone、PC/2in1、TV、Tablet和Wearable设备。
