---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-h
title: service_collaboration_api.h
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 头文件 > service_collaboration_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a69e547766d3207fb08b7cf5ea54169b8b25eb16067a4ae9e7efa9ba84b7ea5
---

## 概述

PhonePC/2in1TabletTV

函数export定义的接口。

**引用文件：** <service\_collaboration/service\_collaboration\_api.h>

**库：** libservice\_collaboration\_ndk.z.so

**系统能力：** SystemCapability.Collaboration.Service

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

## 汇总

PhonePC/2in1TabletTV

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
| [SERVICE\_COLLABORATION\_URI\_MAXLENGTH](servicecollaboration-capi-module.md#service_collaboration_uri_maxlength) 4096 | 传入应用沙箱目录uri的最大长度。 |

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
| typedef struct [ServiceCollaboration\_SelectInfoV2](servicecollaboration-selectinfov2.md) [ServiceCollaboration\_SelectInfoV2](servicecollaboration-capi-module.md#servicecollaboration_selectinfov2) | 被选择的设备信息。 |
| typedef struct [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) | 跨设备互通设备类型枚举 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) {  TAKE\_PHOTO = 1,  SCAN\_DOCUMENT = 2,  IMAGE\_PICKER = 3,  VIDEO\_PICKER = 5,  IMAGE\_VIDEO\_PICKER = 6  } | 跨设备互通能力类型的枚举。 |
| [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype-1){  IMAGE = 1,  VIDEO = 2  } | 回传数据类型。 |
| [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1){  LAST\_DATA\_BACK = 1001202000,  PEER\_CANCEL = 1001202001,  NETWORK\_ERROR = 1001202002,  PEER\_WIFI\_NOT\_OPEN = 1001202004,  LOCAL\_WIFI\_NOT\_OPEN = 1001202005,  DATA\_BACK\_START = 1001202006,  MIDDLE\_DATA\_BACK = 1001202007,  TIMEOUT\_AUTO\_CANCEL = 1001202008,  DATA\_READ\_FAILED = 1001202009,  LINK\_SHUTDOWN = 1001202011,  REMOTE\_HOTSPOT\_CONFLICT = 1001202013,  REMOTE\_DISTRIBUTED\_SERVICES\_CONFLICT = 1001202014,  SEND\_VIDEO\_SUCCESS = 1001202015,  MULTI\_VIDEO\_SENDING\_BACK = 1001202016,  STORE\_VIDEO\_FAIL = 1001202017  } | 错误码枚举。 |
| [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype) {  PHONE = 1,  TABLET = 2,  PC\_2IN1 = 3  } | 被调用端设备类型的枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md)\* [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfos)(  uint32\_t fileterNum, [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype-1) serviceFileterTypes[]); | 获取支持相关能力的设备列表。 |
| uint32\_t [HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)(  const [ServiceCollaboration\_SelectInfo](servicecollaboration-selectinfo.md)\* selectService, [ServiceCollaborationCallback](servicecollaborationcallback.md)\* callback) | 拉起跨设备互通回传图片的能力。 |
| int32\_t [HMS\_ServiceCollaboration\_StopCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_stopcollaboration)(uint32\_t collaborationId); | 取消跨设备互通能力。 |
| uint32\_t [HMS\_ServiceCollaboration\_StartCollaborationV2](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaborationv2)(  const [ServiceCollaboration\_SelectInfoV2](servicecollaboration-selectinfov2.md)\* selectService, [ServiceCollaborationCallback](servicecollaborationcallback.md)\* callback) | 拉起跨设备互通回传图片和视频的能力。 |
| [ServiceCollaboration\_CollaborationDeviceInfoSets](servicecollaboration-collaborationdeviceinfosets.md)\*  [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfosV2](servicecollaboration-capi-module.md#hms_servicecollaboration_getcollaborationdeviceinfosv2) (  uint32\_t deviceFilterNum, [CollaborationDeviceFilterType](servicecollaboration-capi-module.md#collaborationdevicefiltertype)  deviceFilterTypes[], uint32\_t serviceFilterNum,  [ServiceCollaborationFilterType](servicecollaboration-capi-module.md#servicecollaborationfiltertype) serviceFilterTypes[]) | 获取支持相关能力的指定设备列表。 |
