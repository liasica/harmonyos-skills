---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback
title: ArkUI_ContextCallback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ContextCallback
category: harmonyos-references
scraped_at: 2026-04-28T08:04:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e2e075b4b389751b45c54ad75c8eacbf093a4438d6231f977101493586179eae
---

```
1. typedef struct {...} ArkUI_ContextCallback
```

## 概述

PhonePC/2in1TabletTVWearable

事件回调类型。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| void\* userData | 自定义类型，开发者自定义类型的数据，在回调时作为参数传入。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*callback)(void\* userData)](capi-arkui-nativemodule-arkui-contextcallback.md#callback) | 事件回调。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### callback()

PhonePC/2in1TabletTVWearable

```
1. void (*callback)(void* userData)
```

**描述：**

事件回调。
