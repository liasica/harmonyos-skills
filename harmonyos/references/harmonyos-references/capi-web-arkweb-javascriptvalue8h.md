---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalue8h
title: ArkWeb_JavaScriptValue*
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_JavaScriptValue*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1421b4333cdb2fedc1123929e329c2d764560ebca21ce156515a0183138b3d75
---

```c
typedef struct ArkWeb_JavaScriptValue* ArkWeb_JavaScriptValuePtr
```

## 概述

ArkWeb\_JavaScriptValue是用于在Native代码中封装JavaScript值的结构体，提供了JavaScript值的基本创建和操作能力。该结构体支持将Native数据转换为JavaScript可识别的格式，解决Native与JavaScript双向数据传递的类型安全与格式兼容问题，是JavaScript桥接通信中的数据传递基础类型，有助于减少手动转换成本、提升桥接通信效率并增强可维护性。

**起始版本：** 18

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)
