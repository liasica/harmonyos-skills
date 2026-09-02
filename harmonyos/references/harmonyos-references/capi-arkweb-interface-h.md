---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-interface-h
title: arkweb_interface.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > arkweb_interface.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a802c81e667b060a0076a684322231332282ffbad171151c4c3a06cf74b9dfe
---

## 概述

arkweb\_interface.h是ArkWeb在Native侧（C/C++）的核心入口头文件：它定义了基础Native API类型[ArkWeb\_AnyNativeAPI](capi-web-arkweb-anynativeapi.md)与API类型枚举[ArkWeb\_NativeAPIVariantKind](capi-arkweb-interface-h.md#arkweb_nativeapivariantkind)，并提供[OH\_ArkWeb\_GetNativeAPI](capi-arkweb-interface-h.md#oh_arkweb_getnativeapi)接口用于按需获取Controller、Component、CookieManager等具体Native API结构体，同时提供[OH\_ArkWeb\_RegisterScrollCallback](capi-arkweb-interface-h.md#oh_arkweb_registerscrollcallback)用于注册Web组件滚动事件回调；当开发者需要在Native代码中控制Web组件行为（如执行JavaScript、管理Cookie、监听组件生命周期或滚动事件）时，应首先通过本头文件获取对应的Native API，而页面渲染显示等能力仍需由ArkTS侧的Web组件提供。

**引用文件：** <web/arkweb\_interface.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_AnyNativeAPI](capi-web-arkweb-anynativeapi.md) | ArkWeb\_AnyNativeAPI | 定义基础Native API类型。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_NativeAPIVariantKind](capi-arkweb-interface-h.md#arkweb_nativeapivariantkind) | ArkWeb\_NativeAPIVariantKind | 定义Native API的类型枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkWeb\_AnyNativeAPI\* OH\_ArkWeb\_GetNativeAPI(ArkWeb\_NativeAPIVariantKind type)](capi-arkweb-interface-h.md#oh_arkweb_getnativeapi) | 根据传入的API类型，获取对应的Native API结构体。 |
| [bool OH\_ArkWeb\_RegisterScrollCallback(const char\* webTag, ArkWeb\_OnScrollCallback callback, void\* userData)](capi-arkweb-interface-h.md#oh_arkweb_registerscrollcallback) | 注册组件滚动时的回调函数。 |

## 枚举类型说明

### ArkWeb\_NativeAPIVariantKind

```c
enum ArkWeb_NativeAPIVariantKind
```

**描述：**

定义Native API的类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_NATIVE\_COMPONENT | Component相关API类型。 |
| ARKWEB\_NATIVE\_CONTROLLER | Controller相关API类型。 |
| ARKWEB\_NATIVE\_WEB\_MESSAGE\_PORT | WebMessagePort相关API类型。 |
| ARKWEB\_NATIVE\_WEB\_MESSAGE | WebMessage相关API类型。 |
| ARKWEB\_NATIVE\_COOKIE\_MANAGER | CookieManager相关API类型。 |
| ARKWEB\_NATIVE\_JAVASCRIPT\_VALUE | JavaScriptValue相关API类型。  **起始版本：** 18 |

## 函数说明

### OH\_ArkWeb\_GetNativeAPI()

```c
ArkWeb_AnyNativeAPI* OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind type)
```

**描述：**

根据传入的API类型，获取对应的Native API结构体。用于在Native代码中获取Controller以控制Web组件行为、获取CookieManager以管理Cookie、获取WebMessagePort以实现消息通信、获取JavaScriptValue以操作JavaScript对象等场景。该接口可能返回空指针，开发者在使用返回值前必须进行判空处理，避免空指针解引用导致应用崩溃。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkWeb\_NativeAPIVariantKind](capi-arkweb-interface-h.md#arkweb_nativeapivariantkind) type | ArkWeb支持的Native API类型，不同API类型可能需要不同系统版本支持，详见枚举类型说明。  返回值使用说明：返回的指针由系统管理，无需开发者手动释放；多次调用相同参数可能返回同一指针；返回的Native API结构体在Web组件生命周期内有效；使用时请确保线程安全。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_AnyNativeAPI](capi-web-arkweb-anynativeapi.md)\* | 根据传入的API类型，返回对应的Native API结构体指针，结构体第一个成员为当前结构体的大小，可用于访问Controller、Component、CookieManager等具体的Native API功能。若传入的API类型在当前系统版本不支持（如ARKWEB\_NATIVE\_JAVASCRIPT\_VALUE在18以下版本不可用），则返回NULL。 |

### OH\_ArkWeb\_RegisterScrollCallback()

```c
bool OH_ArkWeb_RegisterScrollCallback(const char* webTag, ArkWeb_OnScrollCallback callback, void* userData)
```

**描述：**

注册组件滚动时的回调函数。用于监测用户滚动行为以实现懒加载、检测滚动位置以实现回到顶部功能、记录用户浏览行为用于数据分析、实现滚动时的视觉特效等场景。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件的名称。 |
| [ArkWeb\_OnScrollCallback](capi-arkweb-type-h.md#arkweb_onscrollcallback) callback | 页面滚动时的回调函数。 |
| void\* userData | 用户自定义的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果回调设置成功，则返回true，否则返回false。 |
