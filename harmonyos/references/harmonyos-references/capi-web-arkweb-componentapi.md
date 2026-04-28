---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-componentapi
title: ArkWeb_ComponentAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ComponentAPI
category: harmonyos-references
scraped_at: 2026-04-28T08:05:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c3d89751fc53b7378f05d292f73265517aa3d723d76a2366d48936c7a35d8a6b
---

```
1. typedef struct {...} ArkWeb_ComponentAPI
```

## 概述

PhonePC/2in1TabletTVWearable

Component相关的Native API结构体。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| size\_t size | 结构体的大小。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*onControllerAttached)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](capi-web-arkweb-componentapi.md#oncontrollerattached) | 当Controller成功绑定到Web组件时触发该回调。 |
| [void (\*onPageBegin)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](capi-web-arkweb-componentapi.md#onpagebegin) | 网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。 |
| [void (\*onPageEnd)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](capi-web-arkweb-componentapi.md#onpageend) | 网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。 |
| [void (\*onDestroy)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](capi-web-arkweb-componentapi.md#ondestroy) | 当前Web组件销毁时触发该回调。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### onControllerAttached()

PhonePC/2in1TabletTVWearable

```
1. void (*onControllerAttached)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

当Controller成功绑定到Web组件时触发该回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| ArkWeb\_OnComponentCallback callback | onControllerAttached的回调函数。 |
| void\* userData | 用户自定义数据。 |

### onPageBegin()

PhonePC/2in1TabletTVWearable

```
1. void (*onPageBegin)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

网页开始加载时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| ArkWeb\_OnComponentCallback callback | onPageBegin的回调函数。 |
| void\* userData | 用户自定义数据。 |

### onPageEnd()

PhonePC/2in1TabletTVWearable

```
1. void (*onPageEnd)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| ArkWeb\_OnComponentCallback callback | onPageEnd的回调函数。 |
| void\* userData | 用户自定义数据。 |

### onDestroy()

PhonePC/2in1TabletTVWearable

```
1. void (*onDestroy)(const char* webTag, ArkWeb_OnComponentCallback callback, void* userData)
```

**描述：**

当前Web组件销毁时触发该回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| ArkWeb\_OnComponentCallback callback | onDestroy的回调函数。 |
| void\* userData | 用户自定义数据。 |
