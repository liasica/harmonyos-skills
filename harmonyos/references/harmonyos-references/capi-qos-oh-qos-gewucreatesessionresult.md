---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewucreatesessionresult
title: OH_QoS_GewuCreateSessionResult
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 结构体 > OH_QoS_GewuCreateSessionResult
category: harmonyos-references
scraped_at: 2026-09-02T15:02:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:41f21cc662f6ed8c69cff13b68955f4acda36db7e13a1842d87b49b9f2a59d26
---

```c
typedef struct { ... } OH_QoS_GewuCreateSessionResult
```

## 概述

OH\_QoS\_GewuCreateSession()接口的返回结果，用于封装格物会话创建操作的执行状态。该结构体支持统一处理会话创建成功和失败两种场景：创建会话成功时，session字段包含创建的会话句柄；失败时，error字段保存错误码，便于开发者定位和处理异常。

**起始版本：** 20

**相关模块：** [QoS](capi-qos.md)

**所在头文件：** [qos.h](capi-qos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_QoS\_GewuSession](capi-qos-h.md#oh_qos_gewusession) session | 创建会话成功后返回的会话句柄。仅在error为OH\_QOS\_GEWU\_OK时有效。 |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) error | 错误码。  - OH\_QOS\_GEWU\_OK：创建会话成功。  - OH\_QOS\_GEWU\_NOMEM：内存不足，表示没有足够的内存创建会话，建议释放系统资源后重新创建会话。  - OH\_QOS\_GEWU\_INVAL：参数错误，表示输入参数不符合接口要求，请检查attributes中的字段类型、格式和取值。  - OH\_QOS\_GEWU\_NOPERM：权限不足，表示调用者缺少接口所需权限，请检查应用权限配置。  - OH\_QOS\_GEWU\_EXIST：会话已存在，表示重复创建已存在的会话，请确认会话创建流程。  - OH\_QOS\_GEWU\_NOSYS：找不到子系统，表示系统不支持相关功能或依赖子系统不可用，请确认系统版本和依赖库状态。  上述枚举值与数字的对应关系：OH\_QOS\_GEWU\_OK=0、OH\_QOS\_GEWU\_NOPERM=201、OH\_QOS\_GEWU\_NOMEM=203、OH\_QOS\_GEWU\_INVAL=401、OH\_QOS\_GEWU\_EXIST=501、OH\_QOS\_GEWU\_NOSYS=801。 |
