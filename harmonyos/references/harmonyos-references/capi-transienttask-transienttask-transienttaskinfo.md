---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-transienttaskinfo
title: TransientTask_TransientTaskInfo
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 结构体 > TransientTask_TransientTaskInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bfbfd9a0075b5ccfdac395699be86e1dd21c61d51a24c508e31ca32e666831ec
---

```c
typedef struct TransientTask_TransientTaskInfo {...} TransientTask_TransientTaskInfo
```

## 概述

定义所有短时任务信息结构体。用于返回当日剩余总配额和已申请的所有短时任务信息。

**起始版本：** 20

**相关模块：** [TransientTask](capi-transienttask.md)

**所在头文件：** [transient\_task\_type.h](capi-transient-task-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t remainingQuota | 当日剩余总配额。单位：毫秒。 |
| [TransientTask\_DelaySuspendInfo](capi-transienttask-transienttask-delaysuspendinfo.md) transientTasks[[TRANSIENT\_TASK\_MAX\_NUM](capi-transient-task-type-h.md#宏定义)] | 已申请的所有短时任务信息。包括短时任务请求ID、剩余时间（单位：毫秒）。 |
