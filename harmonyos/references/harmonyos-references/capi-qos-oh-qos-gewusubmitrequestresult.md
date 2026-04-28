---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos-oh-qos-gewusubmitrequestresult
title: OH_QoS_GewuSubmitRequestResult
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 结构体 > OH_QoS_GewuSubmitRequestResult
category: harmonyos-references
scraped_at: 2026-04-28T08:10:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2b14e064a8053de641bbf1b4af22373f9ff206bcc55f0b437bcf2c7efac88653
---

```
1. typedef struct { ... } OH_QoS_GewuSubmitRequestResult
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_QoS\_GewuSubmitRequest()接口的返回结果，成功时返回请求的 request，失败时 error 会置为对应的错误码 。

**起始版本：** 20

**相关模块：** [QoS](capi-qos.md)

**所在头文件：** [qos.h](capi-qos-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_QoS\_GewuRequest request | 创建出来的请求句柄 |
| [OH\_QoS\_GewuErrorCode](capi-qos-h.md#oh_qos_gewuerrorcode) error | 错误码。- 请求提交成功返回OH\_QOS\_GEWU\_OK。- 由于没有足够的内存而创建会话失败返回OH\_QOS\_GEWU\_NOMEM。 |
