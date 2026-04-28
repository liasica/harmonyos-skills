---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module
title: ServiceCollaboration
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 模块 > ServiceCollaboration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d951ee0be028505cb185ccf5dc924c41fe69a5c01ead65b5c7330c36c392fe0a
---

## 概述

PhonePC/2in1TabletTV

提供ServiceCollaboration跨设备互通的相关NDK接口。

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

## 汇总

PhonePC/2in1TabletTV

### 文件

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [service\_collaboration\_api.h](servicecollaboration-capi-h.md) | 跨设备互通的接口以及相关类型的定义。 |

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [ServiceCollaboration\_CollaborationDeviceInfo](servicecollaboration-collaborationdeviceinfo.md) | 跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。 |
| struct [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md) | 通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)获取的对端设备信息对象集合。 |
| struct [ServiceCollaboration\_SelectInfo](servicecollaboration-selectinfo.md) | 使用[HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)触发跨设备互通时，被选择的设备信息。 |
| struct [ServiceCollaborationCallback](servicecollaborationcallback.md) | 传给[HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)的回调方法。 |
| struct [ServiceCollaboration\_SelectInfoV2](servicecollaboration-selectinfov2.md) | 使用[HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。 |

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicenetworkid_maxlength) 65 | 设备network Id最大长度。 |
| [COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH](servicecollaboration-capi-module.md#collaborationdeviceinfo_devicename_maxlength) 128 | 设备名最大长度。 |
| [SERVICE\_COLLABORATION\_URI\_MAXLENGTH](servicecollaboration-capi-module.md#service_collaboration_uri_maxlength) 4096 | 传入沙箱目录uri的最大长度。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype) | 跨设备互通能力类型枚举。 |
| typedef enum [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype-1) [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype) | 回传数据类型。 |
| typedef enum [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1) [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode) | 错误码枚举。 |
| typedef struct [ServiceCollaboration\_CollaborationDeviceInfo](servicecollaboration-collaborationdeviceinfo.md) [ServiceCollaboration\_CollaborationDeviceInfo](servicecollaboration-capi-module.md#servicecollaboration_collaborationdeviceinfo) | 设备信息对象。 |
| typedef struct [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md) [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-capi-module.md#servicecollaboration_collaborationdeviceinfosets) | 设备信息对象集合。 |
| typedef struct [ServiceCollaboration\_SelectInfo](servicecollaboration-selectinfo.md) [ServiceCollaboration\_SelectInfo](servicecollaboration-capi-module.md#servicecollaboration_selectinfo) | 被选择的设备信息。 |
| typedef struct [ServiceCollaborationCallback](servicecollaborationcallback.md) [ServiceCollaborationCallback](servicecollaboration-capi-module.md#servicecollaborationcallback) | 回调跨设备互通状态信息。 |
| typedef struct [ServiceCollaboration\_SelectInfoV2](servicecollaboration-selectinfov2.md) [ServiceCollaboration\_SelectInfoV2](servicecollaboration-capi-module.md#servicecollaboration_selectinfov2) | 使用[HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。 |
| typedef enum [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) | 跨设备互通被调用端能力类型枚举 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) {  TAKE\_PHOTO = 1,  SCAN\_DOCUMENT = 2,  IMAGE\_PICKER = 3,  VIDEO\_PICKER = 5,  IMAGE\_VIDEO\_PICKER = 6  } | 跨设备互通能力类型的枚举。 |
| [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype-1){  IMAGE = 1,  VIDEO = 2  } | 回传数据类型。 |
| [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1){  LAST\_DATA\_BACK = 1001202000,  PEER\_CANCEL = 1001202001,  NETWORK\_ERROR = 1001202002,  PEER\_WIFI\_NOT\_OPEN = 1001202004,  LOCAL\_WIFI\_NOT\_OPEN = 1001202005,  DATA\_BACK\_START = 1001202006,  MIDDLE\_DATA\_BACK = 1001202007,  TIMEOUT\_AUTO\_CANCEL = 1001202008,  DATA\_READ\_FAILED = 1001202009,  LINK\_SHUTDOWN = 1001202011,  REMOTE\_HOTSPOT\_CONFLICT = 1001202013,  REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014,  SEND\_VIDEO\_SUCCESS = 1001202015,  MULTI\_VIDEO\_SENDING\_BACK = 1001202016,  STORE\_VIDEO\_FAIL = 1001202017  } | 错误码枚举。 |
| [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) {  PHONE = 1,  TABLET = 2,  PC\_2IN1 = 3  } | 设备类型枚举 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md)\* [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)(  uint32\_t fileterNum, [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) serviceFileterTypes[]) | 获取支持相关能力的设备列表。 |
| uint32\_t [HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)(  const [ServiceCollaboration\_SelectInfo](servicecollaboration-selectinfo.md)\* selectService, [ServiceCollaborationCallback](servicecollaborationcallback.md)\* callback) | 拉起跨设备互通回传图片的能力。 |
| int32\_t [HMS\_ServiceCollaboration\_StopCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration)(uint32\_t collaborationId) | 取消跨设备互通能力。 |
| int32\_t [HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)(  const [ServiceCollaboration\_SelectInfoV2](servicecollaboration-selectinfov2.md)\* selectService, [ServiceCollaborationCallback](servicecollaborationcallback.md)\* callback)  ) | 拉起跨设备互通回传图片和视频的能力。 |
| [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md)\*  [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfosV2](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfosv2) (  uint32\_t deviceFilterNum, [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype)  deviceFilterTypes[], uint32\_t serviceFilterNum,  [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) serviceFilterTypes[]) | 获取支持相关能力的指定设备列表。 |

## 宏定义说明

PhonePC/2in1TabletTV

### COLLABORATIONDEVICEINFO\_DEVICENETWORKID\_MAXLENGTH

PhonePC/2in1TabletTV

```
1. #define COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH   65
```

**描述**

设备network Id最大长度。

**起始版本：** 5.0.0(12)

### COLLABORATIONDEVICEINFO\_DEVICENAME\_MAXLENGTH

PhonePC/2in1TabletTV

```
1. #define COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH   128
```

**描述**

设备名最大长度。

**起始版本：** 5.0.0(12)

### SERVICE\_COLLABORATION\_URI\_MAXLENGTH

PhonePC/2in1TabletTV

```
1. #define SERVICE_COLLABORATION_URI_MAXLENGTH   4096
```

**描述**

应用沙箱目录uri的最大长度。

**起始版本：** 6.1.0(23)

## 类型定义说明

PhonePC/2in1TabletTV

### ServiceCollaboration\_CollaborationDeviceInfo

PhonePC/2in1TabletTV

```
1. typedef struct ServiceCollaboration_CollaborationDeviceInfo ServiceCollaboration_CollaborationDeviceInfo
```

**描述**

设备信息对象。

**起始版本：** 5.0.0(12)

### ServiceCollaboration\_CollaborationDeviceInfoSets

PhonePC/2in1TabletTV

```
1. typedef struct ServiceCollaboration_CollaborationDeviceInfoSets ServiceCollaboration_CollaborationDeviceInfoSets
```

**描述**

设备信息对象集合。

**起始版本：** 5.0.0(12)

### ServiceCollaboration\_SelectInfo

PhonePC/2in1TabletTV

```
1. typedef struct ServiceCollaboration_SelectInfo ServiceCollaboration_SelectInfo
```

**描述**

被选择的设备信息。

**起始版本：** 5.0.0(12)

### ServiceCollaborationCallback

PhonePC/2in1TabletTV

```
1. typedef struct ServiceCollaborationCallback ServiceCollaborationCallback
```

**描述**

回调跨设备互通状态信息。

**起始版本：** 5.0.0(12)

### ServiceCollaborationFilterType

PhonePC/2in1TabletTV

```
1. typedef enum ServiceCollaborationFilterType ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型的枚举。

**起始版本：** 5.0.0(12)

### ServiceCollaborationDataType

PhonePC/2in1TabletTV

```
1. typedef enum ServiceCollaborationDataType ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：** 5.0.0(12)

### ServiceCollaborationEventCode

PhonePC/2in1TabletTV

```
1. typedef enum ServiceCollaborationEventCode ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.0(12)

### ServiceCollaboration\_SelectInfoV2

PhonePC/2in1TabletTV

```
1. typedef struct ServiceCollaboration_SelectInfoV2 ServiceCollaboration_SelectInfoV2
```

**描述**

使用[HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)触发跨设备互通时，被选择的设备信息，支持选择具有图片和视频回传能力的设备。

**起始版本：** 6.1.0(23)

## 枚举定义说明

PhonePC/2in1TabletTV

### ServiceCollaborationFilterType

PhonePC/2in1TabletTV

```
1. enum ServiceCollaborationFilterType
```

**描述**

跨设备互通能力类型枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| TAKE\_PHOTO = 1 | 拍照。 |
| SCAN\_DOCUMENT = 2 | 扫描。 |
| IMAGE\_PICKER = 3 | 从图库中选择图片。 |
| VIDEO\_PICKER = 5 | 从图库中选择视频。  **起始版本：** 6.1.0(23) |
| IMAGE\_VIDEO\_PICKER = 6 | 从图库中选择图片与视频。  **起始版本：** 6.1.0(23) |

### CollaborationDeviceFilterType

PhonePC/2in1TabletTV

```
1. enum CollaborationDeviceFilterType
```

**描述**

跨设备互通设备类型枚举。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| PHONE | 手机。 |
| TABLET | 平板。 |
| PC\_2IN1 | PC/2in1。 |

### ServiceCollaborationDataType

PhonePC/2in1TabletTV

```
1. enum ServiceCollaborationDataType
```

**描述**

回传数据类型。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| IMAGE = 1 | 图片。 |
| VIDEO = 2 | 视频。  **起始版本：** 6.1.0(23) |

### ServiceCollaborationEventCode

PhonePC/2in1TabletTV

```
1. enum ServiceCollaborationEventCode
```

**描述**

错误码枚举。

**起始版本：** 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| LAST\_DATA\_BACK = 1001202000 | 已收到最后一个数据包。 |
| PEER\_CANCEL = 1001202001 | 对端取消。 |
| NETWORK\_ERROR = 1001202002 | 网络异常。 |
| PEER\_WIFI\_NOT\_OPEN = 1001202004 | 对端WLAN未开启。 |
| LOCAL\_WIFI\_NOT\_OPEN = 1001202005 | 本端WLAN未开启。 |
| DATA\_BACK\_START = 1001202006 | 开始回传数据。 |
| MIDDLE\_DATA\_BACK = 1001202007 | 收到中间数据。 |
| TIMEOUT\_AUTO\_CANCEL = 1001202008 | 接收数据超时取消。 |
| DATA\_READ\_FAILED = 1001202009 | 数据读取失败。 |
| LINK\_SHUTDOWN = 1001202011 | 链路断开。 |
| REMOTE\_HOTSPOT\_CONFLICT = 1001202013 | 由于对端开启热点产生了链路冲突。  **起始版本：** 5.1.0(18) |
| REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014 | 由于对端设备正在与其他设备进行互联而产生了链路冲突。  **起始版本：** 5.1.0(18) |
| SEND\_VIDEO\_SUCCESS = 1001202015 | 视频回传成功。  **起始版本：** 6.1.0(23) |
| MULTI\_VIDEO\_SENDING\_BACK = 1001202016 | 开始多个视频回传。  **起始版本：** 6.1.0(23) |
| STORE\_VIDEO\_FAIL = 1001202017 | 内存不足视频回传失败。  **起始版本：** 6.1.0(23) |

## 函数说明

PhonePC/2in1TabletTV

### HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos

PhonePC/2in1TabletTV

```
1. ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfos(
2. uint32_t fileterNum, ServiceCollaborationFilterType serviceFileterTypes[]);
```

**描述**

获取支持相关能力的设备列表。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| uint32\_t fileterNum | 服务能力类型总数。 |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) serviceFileterTypes[] | 具体需要的服务能力类型的数组。 |

**返回：**

返回[ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-capi-module.md#servicecollaboration_collaborationdeviceinfosets)，设备信息对象集合。

### HMS\_ServiceCollaboration\_GetCollaborationDeviceInfosV2

PhonePC/2in1TabletTV

```
1. ServiceCollaboration_CollaborationDeviceInfoSets* HMS_ServiceCollaboration_GetCollaborationDeviceInfosV2(
2. uint32_t deviceFilterNum, CollaborationDeviceFilterType deviceFilterTypes[], uint32_t serviceFilterNum, ServiceCollaborationFilterType serviceFilterTypes[]);
```

**描述**

获取支持相关能力的指定设备列表。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| uint32\_t deviceFilterNum | 设备类型总数。 |
| [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) deviceFilterTypes[] | 被调用端的设备类型的数组。 |
| uint32\_t serviceFilterNum | 服务能力类型总数。 |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) serviceFilterTypes[] | 服务能力类型的数组。 |

**返回：**

返回[ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-capi-module.md#servicecollaboration_collaborationdeviceinfosets)，设备信息对象集合。

### HMS\_ServiceCollaboration\_StartCollaboration

PhonePC/2in1TabletTV

```
1. uint32_t HMS_ServiceCollaboration_StartCollaboration(
2. const ServiceCollaboration_SelectInfo* selectService, ServiceCollaborationCallback* callback);
```

**描述**

拉起跨设备互通回传图片的能力。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| const [ServiceCollaboration\_SelectInfo](servicecollaboration-capi-module.md#servicecollaboration_selectinfo)\* selectService | 选择需要拉起的服务能力类型。 |
| [ServiceCollaborationCallback](servicecollaboration-capi-module.md#servicecollaborationcallback)\* callback | 回调，传递跨设备互通状态信息。 |

**返回：**

返回uint32\_t的collaborationId，本次跨设备互通唯一标识。

### HMS\_ServiceCollaboration\_StopCollaboration

PhonePC/2in1TabletTV

```
1. int32_t HMS_ServiceCollaboration_StopCollaboration(uint32_t collaborationId);
```

**描述**

取消跨设备互通能力。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| uint32\_t collaborationId | 跨设备互通唯一标识。 |

**返回：**

返回stop结果，0为成功。

### HMS\_ServiceCollaboration\_StartCollaborationV2

PhonePC/2in1TabletTV

```
1. uint32_t HMS_ServiceCollaboration_StartCollaborationV2(
2. const ServiceCollaboration_SelectInfoV2* selectService, ServiceCollaborationCallback* callback);
```

**描述**

拉起跨设备互通回传图片和视频的能力。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| const [ServiceCollaboration\_SelectInfoV2](servicecollaboration-capi-module.md#servicecollaboration_selectinfov2)\* selectService | 选择需要拉起的服务能力类型。 |
| [ServiceCollaborationCallback](servicecollaboration-capi-module.md#servicecollaborationcallback)\* callback | 回调，传递跨设备互通状态信息。 |

**返回：**

返回uint32\_t的collaborationId，本次跨设备互通唯一标识。
