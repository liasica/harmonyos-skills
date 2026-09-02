---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdeviceinfo
title: ServiceCollaboration_CollaborationDeviceInfo
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_CollaborationDeviceInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50c162a25becfee47bfe563b38eea2b100ceae3ddac5daffb0c21d9189eec604
---

## 概述

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [deviceType](servicecollaboration-collaborationdeviceinfo.md#devicetype) | 对端设备类型。  Phone设备类型的值为0x14，Tablet设备类型的值为0x17。 |
| char [deviceNetworkId](servicecollaboration-collaborationdeviceinfo.md#devicenetworkid) [[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicenetworkid_maxlength)] | 对端设备network Id。 |
| char [deviceName](servicecollaboration-collaborationdeviceinfo.md#devicename) [[COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicename_maxlength)] | 对端设备名。 |
| uint32\_t [filterNum](servicecollaboration-collaborationdeviceinfo.md#filternum) | 对端设备支持的能力类型列表的大小。 |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) \* [serviceFilterTypes](servicecollaboration-collaborationdeviceinfo.md#servicefiltertypes) | 对端设备支持的能力类型列表。 |

## 结构体成员变量说明

### deviceName

```c
char ServiceCollaboration_CollaborationDeviceInfo::deviceName[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH]
```

**描述**

对端设备名。

### deviceNetworkId

```c
char ServiceCollaboration_CollaborationDeviceInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

**描述**

对端设备network Id。

### deviceType

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfo::deviceType
```

**描述**

对端设备类型。只有Phone或者Tablet。Phone设备类型的值为0x14，Tablet设备类型的值为0x17。

### filterNum

```c
uint32_t ServiceCollaboration_CollaborationDeviceInfo::filterNum
```

**描述**

对端设备支持的能力类型列表的大小。

### serviceFilterTypes

```c
ServiceCollaborationFilterType* ServiceCollaboration_CollaborationDeviceInfo::serviceFilterTypes
```

**描述**

对端设备支持的能力类型列表。
