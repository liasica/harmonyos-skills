---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewusubmitrequestresult
title: OH_QoS_GewuSubmitRequestResult
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 结构体 > OH_QoS_GewuSubmitRequestResult
category: harmonyos-references
scraped_at: 2026-09-02T15:02:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bac63d1d133a0ebc40c1a3deb43ff47870f68153404ec711be833f3833275ebb
---

```c
typedef struct { ... } OH_QoS_GewuSubmitRequestResult
```

## 概述

OH\_QoS\_GewuSubmitRequest()接口的返回结果，用于获取格物服务（Gewu service，端侧AI推理加速服务）推理请求的提交状态和结果。请求提交成功时，request字段包含创建的请求句柄，可用于后续中止该请求；失败时，error字段保存错误码，便于开发者根据具体错误原因进行处理。该结构体适用于提交端侧AI推理请求后判断请求是否成功进入会话并获取请求句柄的场景。

**起始版本：** 20

**相关模块：** [QoS](capi-qos.md)

**所在头文件：** [qos.h](capi-qos-h.md)

## 汇总

### 成员变量

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| request | [OH\_QoS\_GewuRequest](capi-qos-h.md#oh_qos_gewurequest) | 请求提交成功后创建的请求句柄，可用于后续中止该请求。仅在error为OH\_QOS\_GEWU\_OK时有效，失败时该字段无效。 |
| error | [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) | 错误码。  - OH\_QOS\_GEWU\_OK：请求提交成功。  - OH\_QOS\_GEWU\_NOMEM：内存不足，表示没有足够的内存处理该请求，建议释放资源后重试。  - OH\_QOS\_GEWU\_INVAL：参数错误，表示传入的会话句柄、请求内容或回调等参数无效，请检查参数类型、格式和取值。  - OH\_QOS\_GEWU\_NOENT：找不到会话，表示指定的会话不存在或已被销毁，请确认会话是否已成功创建且仍然有效。  - OH\_QOS\_GEWU\_NOPERM：权限不足，表示调用者缺少接口所需权限，请检查应用权限配置。  - OH\_QOS\_GEWU\_NOSYS：找不到子系统，表示系统不支持相关功能或依赖子系统不可用，请确认系统版本和依赖库状态。  上述枚举值与数字的对应关系：OH\_QOS\_GEWU\_OK=0、OH\_QOS\_GEWU\_NOPERM=201、OH\_QOS\_GEWU\_NOMEM=203、OH\_QOS\_GEWU\_INVAL=401、OH\_QOS\_GEWU\_NOENT=502、OH\_QOS\_GEWU\_NOSYS=801。 |
