---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata
title: ArkWeb_JavaScriptBridgeData
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptBridgeData
category: harmonyos-references
scraped_at: 2026-04-28T08:05:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9388bd019409e86c40c18581d72ab3e582c3aa95cb090018a81d284e179c38dc
---

```
1. typedef struct {...} ArkWeb_JavaScriptBridgeData
```

## 概述

PhonePC/2in1TabletTVWearable

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const uint8\_t\* buffer | 指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。 |
| size\_t size | 传输数据的长度。 |
