---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-transienttask-transienttask-delaysuspendinfo
title: TransientTask_DelaySuspendInfo
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 结构体 > TransientTask_DelaySuspendInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de34b8aa876922494b369006688bc934148f3cdccedaeed06e2d218883d19590
---

```c
typedef struct TransientTask_DelaySuspendInfo {...} TransientTask_DelaySuspendInfo
```

## 概述

定义短时任务返回信息结构体。用于返回当前短时任务的任务ID和剩余时间。

**起始版本：** 13

**相关模块：** [TransientTask](capi-transienttask.md)

**所在头文件：** [transient\_task\_type.h](capi-transient-task-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t requestId | 短时任务请求ID。 |
| int32\_t actualDelayTime | 剩余时间（单位：毫秒）。 |
