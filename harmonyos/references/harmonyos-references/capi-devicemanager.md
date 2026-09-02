---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-devicemanager
title: DeviceManager
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > C API > 模块 > DeviceManager
category: harmonyos-references
scraped_at: 2026-09-02T14:52:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d49a599623d002b14cfb5f614878615386433254a6e73f62230489bb5c58e995
---

## 概述

分布式设备管理模块，用于获取可信设备和本地设备的基本信息。可信设备指已通过设备认证建立信任关系的设备，基本信息包括设备名称、设备类型、设备标识、设备状态等。该模块提供设备发现、设备绑定、设备信息查询、设备状态监听等功能，适用于分布式跨设备协同、设备互联等场景，实现业务协同与数据共享。

开发者可通过该模块提供的接口获取设备信息，完成分布式设备管理相关的开发任务。模块设计逻辑和使用说明，请参见[分布式设备管理开发指导](../harmonyos-guides/devicemanager-guidelines.md)。

**起始版本：** 20

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [oh\_device\_manager.h](capi-oh-device-manager-h.md) | 提供访问可信设备和本地设备信息的接口。引用文件：<distributedhardware/device\_manager/oh\_device\_manager.h> |
| [oh\_device\_manager\_err\_code.h](capi-oh-device-manager-err-code-h.md) | 声明设备管理模块错误码信息。引用文件：<distributedhardware/device\_manager/oh\_device\_manager\_err\_code.h> |
