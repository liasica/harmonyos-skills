---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaborationcallback
title: ServiceCollaborationCallback
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > C API > 头文件和结构体 > 结构体 > ServiceCollaborationCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:09:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1cf807de9ead8e599b1f7a935e2e798c886f1b583af8e366701871a3f3f97925
---

## 概述

PhonePC/2in1TabletTV

传给[HMS\_ServiceCollaboration\_StartCollaboration](servicecollaboration-capi-module.md#hms_servicecollaboration_startcollaboration)的回调方法。

**起始版本：** 5.0.0(12)

**相关模块：** [ServiceCollaboration](servicecollaboration-capi-module.md)

**所在头文件：** [service\_collaboration\_api.h](servicecollaboration-capi-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t(\* [OnEvent](servicecollaborationcallback.md#onevent) )([ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code, uint32\_t extraCode) | 在跨设备互通服务状态变化时被调用。 |
| int32\_t(\* [OnDataCallback](servicecollaborationcallback.md#ondatacallback) )([ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code, [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype-1) dataType, uint32\_t dataSize, char \*data) | 在跨设备互通服务数据返回时被调用。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### OnDataCallback

PhonePC/2in1TabletTV

```
1. int32_t(* ServiceCollaborationCallback::OnDataCallback) (ServiceCollaborationEventCode code, ServiceCollaborationDataType dataType, uint32_t dataSize, char *data)
```

**描述**

在跨设备互通服务数据返回时被调用。

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code | 错误码。 |
| [ServiceCollaborationDataType](servicecollaboration-capi-module.md#servicecollaborationdatatype-1) dataType | 回传数据类型。 |
| uint32\_t dataSize | 数据大小，单位是字节。 |
| char \*data | 数据。 |

### OnEvent

PhonePC/2in1TabletTV

```
1. int32_t(* ServiceCollaborationCallback::OnEvent) (ServiceCollaborationEventCode code, uint32_t extraCode)
```

**描述**

在跨设备互通服务状态变化时被调用。

**参数：**

| 名称 | 描述 |
| --- | --- |
| [ServiceCollaborationEventCode](servicecollaboration-capi-module.md#servicecollaborationeventcode-1) code | 错误码。 |
| uint32\_t extraCode | 拓展状态码，携带错误码未提供的额外信息。 |
