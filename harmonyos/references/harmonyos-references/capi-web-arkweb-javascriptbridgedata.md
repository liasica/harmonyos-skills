---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptbridgedata
title: ArkWeb_JavaScriptBridgeData
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptBridgeData
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26e25096e094b86cf84ee1cb37999b855e1f9957dacec1e2291cd36f0b2afade
---

```c
typedef struct {...} ArkWeb_JavaScriptBridgeData
```

## 概述

ArkWeb\_JavaScriptBridgeData是JavaScript桥接数据定义结构体，用于在Native代码和Web页面之间传递JavaScript桥接相关的数据。该结构体封装了桥接调用中的参数数据，是JavaScript桥接子系统中的基本数据单元，配合ArkWeb\_ControllerAPI中的JavaScript Proxy注册接口使用。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const uint8\_t\* buffer | 指向传输数据的指针。支持String和ArrayBuffer类型，其余类型会被JSON序列化后，以String类型传递。 |
| size\_t size | 传输数据的长度。建议根据实际数据大小合理设置，与buffer的大小保持一致，避免过大或过小导致的性能或数据问题。 |
