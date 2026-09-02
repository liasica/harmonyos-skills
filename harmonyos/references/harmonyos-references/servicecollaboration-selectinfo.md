---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo
title: ServiceCollaboration_SelectInfo
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_SelectInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:034fe6e4c56706a52a1c92963c9b1592db2b848300f36425c6611b11cd1e173f
---

## 概述

使用[HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) [serviceFilterType](servicecollaboration-selectinfo.md#servicefiltertype) | 开发者期望的设备能力类型。 |
| char [deviceNetworkId](servicecollaboration-selectinfo.md#devicenetworkid) [[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicenetworkid_maxlength)] | 被选择的设备network Id。 |
| uint32\_t [maxSize](servicecollaboration-selectinfo.md#maxsize) | 能被选中的最大图片数量。 |

## 结构体成员变量说明

### deviceNetworkId

```c
char ServiceCollaboration_SelectInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

**描述**

被选择的设备network Id。

### maxSize

```c
uint32_t ServiceCollaboration_SelectInfo::maxSize
```

**描述**

能被选中的最大图片数量，默认50。

### serviceFilterType

```c
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。
