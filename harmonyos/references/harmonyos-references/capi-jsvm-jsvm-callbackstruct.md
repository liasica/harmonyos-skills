---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct
title: JSVM_CallbackStruct
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CallbackStruct
category: harmonyos-references
scraped_at: 2026-04-28T08:19:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f87b33e63f2a4c2bbc8fe152df9b33359923b914b40b779963044a999500c623
---

```
1. typedef struct {...} JSVM_CallbackStruct
```

## 概述

PhonePC/2in1TabletWearable

用户提供的Native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| void\* data | 用户提供的Native回调函数的数据。 |

### 成员函数

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| [JSVM\_Value(JSVM\_CDECL\* callback)(JSVM\_Env env,JSVM\_CallbackInfo info)](capi-jsvm-jsvm-callbackstruct.md#callback) | 用户提供的Native回调函数的指针。 |

## 成员函数说明

PhonePC/2in1TabletWearable

### callback()

PhonePC/2in1TabletWearable

```
1. JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info)
```

**描述**

用户提供的Native回调函数的指针。
