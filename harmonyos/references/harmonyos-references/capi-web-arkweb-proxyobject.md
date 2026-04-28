---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-proxyobject
title: ArkWeb_ProxyObject
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ProxyObject
category: harmonyos-references
scraped_at: 2026-04-28T08:05:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f39605fc6ea656e42d4193f9e21204cc559d8a13fcf920e7d1fb592ec25888c4
---

```
1. typedef struct {...} ArkWeb_ProxyObject
```

## 概述

PhonePC/2in1TabletTVWearable

注入的Proxy对象通用结构体。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char\* objName | 注入的对象名。 |
| const [ArkWeb\_ProxyMethod](capi-web-arkweb-proxymethod.md)\* methodList | 注入的对象携带的方法结构体数组。 |
| size\_t size | 方法结构体数组的长度。 |
