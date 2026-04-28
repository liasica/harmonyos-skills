---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandler
title: JSVM_PropertyHandler
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_PropertyHandler
category: harmonyos-references
scraped_at: 2026-04-28T08:19:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bec1a0536b225e42cfeb009ff3cbeb204186b83a4e552aa24e775cc5075a4310
---

```
1. typedef struct {...} JSVM_PropertyHandler
```

## 概述

PhonePC/2in1TabletWearable

包含将class作为函数进行调用时所触发的回调函数的函数指针，以及访问实例对象属性时触发的回调函数的函数指针集。

**起始版本：** 18

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_PropertyHandlerCfg](api-jsvm-jsvm-propertyhandlerconfigurationstruct8h.md) propertyHandlerCfg | 访问实例对象属性触发相应的回调函数。 |
| [JSVM\_Callback](capi-jsvm-jsvm-callbackstruct8h.md) callAsFunctionCallback | 实例对象作为函数调用将触发此回调。 |
