---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfosets
title: ServiceCollaboration_CollaborationDeviceInfoSets
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_CollaborationDeviceInfoSets
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:adb5c5da827c04cfc292434e279c1d28de70d08c57cc1a84a76048242e58a9d5
---

## 概述

通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [size](servicecollaboration-collaborationdeviceinfosets.md#size) | 对端设备信息对象集合的大小。 |
| [ServiceCollaboration\_CollaborationDeviceInfo](servicecollaboration-collaborationdeviceinfo.md) \* [deviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md#deviceinfosets) | 对端设备信息对象集合。 |

## 结构体成员变量说明

### deviceInfoSets

```c
ServiceCollaboration_CollaborationDeviceInfo* ServiceCollaboration_CollaborationDeviceInfoSets::deviceInfoSets
```

**描述**

对端设备信息对象集合。

### size

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfoSets::size
```

**描述**

对端设备信息对象集合的大小。
