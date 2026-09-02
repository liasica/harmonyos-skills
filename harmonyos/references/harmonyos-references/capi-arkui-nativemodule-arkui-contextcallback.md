---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback
title: ArkUI_ContextCallback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ContextCallback
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eaf8c59380c4dd268cbe2616cf06f8f3df8b4da871879cba9436380b6a1109c6
---

```c
typedef struct {...} ArkUI_ContextCallback
```

## 概述

事件回调类型，用于定义回调函数及其用户自定义数据。使用该类型的接口触发回调时，会调用callback，并将userData作为参数传入。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void\* userData | 用户自定义数据，在回调时作为参数传入。 |

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [void (\*callback)(void\* userData)](capi-arkui-nativemodule-arkui-contextcallback.md#callback) | 事件触发时执行的回调函数，调用时会传入userData指向的用户自定义数据。 |

## 成员函数说明

### callback()

```c
void (*callback)(void* userData)
```

**描述：**

事件触发时执行的回调函数，无返回值。触发该回调时，会将userData指向的用户自定义数据作为参数传入，用于执行自定义处理逻辑。具体触发时机由使用该类型的接口定义。
