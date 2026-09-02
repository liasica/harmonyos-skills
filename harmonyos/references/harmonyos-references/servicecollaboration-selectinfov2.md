---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-selectinfov2
title: ServiceCollaboration_SelectInfoV2
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaboration_SelectInfoV2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b52d63d7287b9dcf4debb663c0a77d69b0ba37c9a474ed2facb42a99aa1f0081
---

## 概述

使用[HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。

**起始版本：** 6.1.0(23)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype) [serviceFilterType](servicecollaboration-selectinfov2.md#servicefiltertype) | 开发者期望的设备能力类型。 |
| char [deviceNetworkId](servicecollaboration-selectinfov2.md#devicenetworkid) [[COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicenetworkid_maxlength)] | 被选择的设备network Id。 |
| uint32\_t [maxSize](servicecollaboration-selectinfov2.md#maxsize) | 能被选中的最大图片数量。 |
| char uri[[SERVICE\_COLLABORATION\_URI\_MAXLENGTH](servicecollaboration-capi-module.md#service_collaboration_uri_maxlength)] | 应用沙箱目录uri路径。 |

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

能被选中的最大图片数量，默认50，取值范围为1到50。

### serviceFilterType

```c
ServiceCollaborationFilterType ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。

### uri

```c
char ServiceCollaboration_SelectInfo::uri[SERVICE_COLLABORATION_URI_MAXLENGTH]
```

**描述**

应用沙箱目录uri路径。
