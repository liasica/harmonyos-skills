---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfo
title: ServiceCollaboration_SelectInfo
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_SelectInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:09:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11aab8d4361231bccb663c62d59002ceca49516ca43091a102ebd2d404f51da9
---

## 概述

PhonePC/2in1TabletTV

使用[HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) [serviceFilterType](servicecollaboration-selectinfo.md#servicefiltertype) | 开发者期望的设备能力类型。 |
| char [deviceNetworkId](servicecollaboration-selectinfo.md#devicenetworkid) [[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicenetworkid_maxlength)] | 被选择的设备network Id。 |
| uint32\_t [maxSize](servicecollaboration-selectinfo.md#maxsize) | 被选择的设备能被选中的最大图片数量。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### deviceNetworkId

PhonePC/2in1TabletTV

```
1. char ServiceCollaboration_SelectInfo::deviceNetworkId[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH]
```

**描述**

被选择的设备network Id。

### maxSize

PhonePC/2in1TabletTV

```
1. uint32_t ServiceCollaboration_SelectInfo::maxSize
```

**描述**

能被选中的最大图片数量，默认50。

### serviceFilterType

PhonePC/2in1TabletTV

```
1. ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。
