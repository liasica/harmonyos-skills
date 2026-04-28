---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxymethodwithresult
title: ArkWeb_ProxyMethodWithResult
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ProxyMethodWithResult
category: harmonyos-references
scraped_at: 2026-04-28T08:05:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:db468bd7bf8d6f37c723dfa1594164c1060950ab22c9510e8ec966d796c98d90
---

```
1. typedef struct {...} ArkWeb_ProxyMethodWithResult
```

## 概述

PhonePC/2in1TabletTVWearable

注入的Proxy方法通用结构体。

**起始版本：** 18

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* methodName | 注入的方法名。 |
| [ArkWeb\_OnJavaScriptProxyCallbackWithResult](capi-arkweb-type-h.md#arkweb_onjavascriptproxycallbackwithresult) callback | Proxy方法执行的回调。 |
| void\* userData | 需要在回调中携带的自定义数据。 |
