---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input
title: input
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 模块 > input
category: harmonyos-references
scraped_at: 2026-09-02T14:52:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:293f29900b6f9ac29bd11a7d1b1c0b09b86c5de2bdf3787d7c553467fff32bb0
---

## 概述

提供多模态输入域的C接口，支持触控、按键、鼠标等多种输入设备的事件处理，统一接入多设备，提升开发效率与应用交互体验。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [oh\_axis\_type.h](capi-oh-axis-type-h.md) | 输入设备的轴事件结构和枚举，轴类型定义了输入设备在不同交互场景下的物理行为特征，系统通过轴类型来区分和传递不同的手势交互信息。 |
| [oh\_input\_manager.h](capi-oh-input-manager-h.md) | 提供输入事件注入、按键状态查询、设备热插拔监听、事件拦截、快捷键管理、鼠标光标管理、输入设备信息查询、注入权限管理等功能。 |
| [oh\_key\_code.h](capi-oh-key-code-h.md) | 按键设备的键值。 |
| [oh\_pointer\_style.h](capi-oh-pointer-style-h.md) | 鼠标光标的样式。 |
