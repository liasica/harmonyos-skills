---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-control-display-separation
title: xeg_control_display_separation.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_control_display_separation.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8f593d63272726411f2f798d1a418791714fc5e37c1186aac8dde3b6e53fe182
---

## 概述

XEngine控显分离API接口。

**引用文件**：<xengine/xeg\_control\_display\_separation.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 26.0.0

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

### 枚举

| 名称 | 描述 |
| --- | --- |
| [XEG\_ControlDisplaySeparationStatus](xengine-kit-xengine.md#xeg_controldisplayseparationstatus) { UNAVAILABLE = 0, AVAILABLE = 1} | 此枚举描述控显分离当前的状态信息。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum [XEG\_ControlDisplaySeparationStatus](xengine-kit-xengine.md#xeg_controldisplayseparationstatus) XEG\_ControlDisplaySeparationStatus | 此枚举描述控显分离当前的状态信息。 |
| typedef void(\*[PFN\_HMS\_XEG\_ControlDisplaySeparationStatusCallback](xengine-kit-xengine.md#pfn_hms_xeg_controldisplayseparationstatuscallback)) ([XEG\_ControlDisplaySeparationStatus](xengine-kit-xengine.md#xeg_controldisplayseparationstatus) status) | 控显分离特性监听函数的函数指针定义。 |
| typedef bool(\*[PFN\_HMS\_XEG\_SetControlDisplaySeparationStatusListener](xengine-kit-xengine.md#pfn_hms_xeg_setcontroldisplayseparationstatuslistener)) ([PFN\_HMS\_XEG\_ControlDisplaySeparationStatusCallback](xengine-kit-xengine.md#pfn_hms_xeg_controldisplayseparationstatuscallback) callback) | 设置控显分离特性全局唯一监听函数的函数指针定义。 |
| typedef void(\*[PFN\_HMS\_XEG\_RemoveControlDisplaySeparationStatusListener](xengine-kit-xengine.md#pfn_hms_xeg_removecontroldisplayseparationstatuslistener)) () | 移除控显分离特性全局唯一监听函数的函数指针定义。 |
| typedef bool(\*[PFN\_HMS\_XEG\_SetControlDisplaySeparationActive](xengine-kit-xengine.md#pfn_hms_xeg_setcontroldisplayseparationactive)) (bool flag) | 设置控显分离特性使能开关的函数指针定义。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| bool [HMS\_XEG\_SetControlDisplaySeparationStatusListener](xengine-kit-xengine.md#hms_xeg_setcontroldisplayseparationstatuslistener)([PFN\_HMS\_XEG\_ControlDisplaySeparationStatusCallback](xengine-kit-xengine.md#pfn_hms_xeg_controldisplayseparationstatuscallback) callback) | 设置控显分离特性全局唯一监听函数。 |
| void [HMS\_XEG\_RemoveControlDisplaySeparationStatusListener](xengine-kit-xengine.md#hms_xeg_removecontroldisplayseparationstatuslistener)() | 移除控显分离特性全局唯一监听函数。 |
| bool [HMS\_XEG\_SetControlDisplaySeparationActive](xengine-kit-xengine.md#hms_xeg_setcontroldisplayseparationactive)(bool flag) | 设置控显分离特性使能开关。 |
