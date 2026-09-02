---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-input-input-deviceinfo
title: Input_DeviceInfo
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 结构体 > Input_DeviceInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:52:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ae8080e79fae478913bae91e72c2997c268e9b7aaed986177d78b9d167ba168c
---

```c
typedef struct Input_DeviceInfo Input_DeviceInfo
```

## 概述

输入设备信息，用于描述输入设备的基本信息和能力特征，包括设备类型、设备ID等属性。开发者可以通过此结构体获取和管理输入设备的详细信息，便于设备识别和配置管理。

**起始版本：** 13

**相关模块：** [input](capi-input.md)

**所在头文件：** [oh\_input\_manager.h](capi-oh-input-manager-h.md)

**相关接口：**

| 名称 | 描述 |
| --- | --- |
| [OH\_Input\_CreateDeviceInfo](capi-oh-input-manager-h.md#oh_input_createdeviceinfo) | 创建输入设备信息的对象。通过调用[OH\_Input\_DestroyDeviceInfo](capi-oh-input-manager-h.md#oh_input_destroydeviceinfo)销毁输入设备信息的对象。 |
| [OH\_Input\_DestroyDeviceInfo](capi-oh-input-manager-h.md#oh_input_destroydeviceinfo) | 销毁输入设备信息的对象。 |
