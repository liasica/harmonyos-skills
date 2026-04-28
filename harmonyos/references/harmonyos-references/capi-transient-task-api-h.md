---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transient-task-api-h
title: transient_task_api.h
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 头文件 > transient_task_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:38+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:da5d5632d424834477c5a2c8f60e24c94348a2f916f060a64b96bea7eaae2341
---

## 概述

PhonePC/2in1TabletTVWearable

提供短时任务申请、查询、取消功能。

**引用文件：** <transient\_task/transient\_task\_api.h>

**库：** libtransient\_task.so

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**相关模块：** [TransientTask](capi-transienttask.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char\* reason, TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)](capi-transient-task-api-h.md#oh_backgroundtaskmanager_requestsuspenddelay) | 申请短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)](capi-transient-task-api-h.md#oh_backgroundtaskmanager_getremainingdelaytime) | 获取本次短时任务的剩余时间。 |
| [int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)](capi-transient-task-api-h.md#oh_backgroundtaskmanager_cancelsuspenddelay) | 取消短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo \*transientTaskInfo)](capi-transient-task-api-h.md#oh_backgroundtaskmanager_gettransienttaskinfo) | 获取所有短时任务信息，如当日剩余总配额等。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_BackgroundTaskManager\_RequestSuspendDelay()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_BackgroundTaskManager_RequestSuspendDelay(const char* reason, TransientTask_Callback callback, TransientTask_DelaySuspendInfo *info)
```

**描述**

申请短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* reason | 申请短时任务的原因。 |
| [TransientTask\_Callback](capi-transient-task-type-h.md#transienttask_callback) callback | 短时任务即将超时的回调，一般在超时前6秒，通过此回调通知应用。 |
| [TransientTask\_DelaySuspendInfo](capi-transienttask-transienttask-delaysuspendinfo.md) \*info | 返回短时任务信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回0，表示申请成功。  返回401，表示入参错误。  返回9800002，表示Parcel读写操作失败。  返回9800003，表示IPC通信失败。  返回9800004，表示系统服务失败。  返回9900001，表示短时任务客户端信息校验失败。  返回9900002，表示短时任务服务端校验失败。  错误码的具体信息请参考[TransientTask\_ErrorCode](capi-transient-task-type-h.md#transienttask_errorcode)。 |

### OH\_BackgroundTaskManager\_GetRemainingDelayTime()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_BackgroundTaskManager_GetRemainingDelayTime(int32_t requestId, int32_t *delayTime)
```

**描述**

获取本次短时任务的剩余时间。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t requestId | 短时任务的请求ID。 |
| int32\_t \*delayTime | 短时任务的剩余时间，单位：毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回0，表示查询成功。  返回401，表示入参错误。  返回9800002，表示Parcel读写操作失败。  返回9800003，表示IPC通信失败。  返回9800004，表示系统服务失败。  返回9900001，表示短时任务客户端信息校验失败。  返回9900002，表示短时任务服务端校验失败。  错误码的具体信息请参考[TransientTask\_ErrorCode](capi-transient-task-type-h.md#transienttask_errorcode)。 |

### OH\_BackgroundTaskManager\_CancelSuspendDelay()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_BackgroundTaskManager_CancelSuspendDelay(int32_t requestId)
```

**描述**

取消短时任务。

**系统能力：** SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t requestId | 短时任务的请求ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回0，表示取消成功。  返回401，表示入参错误。  返回9800002，表示Parcel读写操作失败。  返回9800003，表示IPC通信失败。  返回9800004，表示系统服务失败。  返回9900001，表示短时任务客户端信息校验失败。  返回9900002，表示短时任务服务端校验失败。  错误码的具体信息请参考[TransientTask\_ErrorCode](capi-transient-task-type-h.md#transienttask_errorcode)。 |

### OH\_BackgroundTaskManager\_GetTransientTaskInfo()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_BackgroundTaskManager_GetTransientTaskInfo(TransientTask_TransientTaskInfo *transientTaskInfo)
```

**描述**

获取所有短时任务信息，如当日剩余总配额等。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TransientTask\_TransientTaskInfo](capi-transienttask-transienttask-transienttaskinfo.md)  \*transientTaskInfo | 所有短时任务信息，具体请参考[TransientTask\_TransientTaskInfo](capi-transienttask-transienttask-transienttaskinfo.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回0，表示获取成功。  返回9900001，表示短时任务客户端信息校验失败。  返回9900003，表示Parcel读写操作失败。  返回9900004，表示系统服务失败。  错误码的具体信息请参考[TransientTask\_ErrorCode](capi-transient-task-type-h.md#transienttask_errorcode)。 |
