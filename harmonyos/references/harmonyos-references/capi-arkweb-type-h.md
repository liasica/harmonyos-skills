---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkweb-type-h
title: arkweb_type.h
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 头文件 > arkweb_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1de4b85ea14e3b14724e476b0d0b28192c26af189870e0a2f3c8cf375e753abb
---

## 概述

提供ArkWeb在Native侧的公共类型定义。

**引用文件：** <web/arkweb\_type.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md) | ArkWeb\_JavaScriptBridgeData | 定义JavaScript Bridge数据的基础结构。 |
| [ArkWeb\_WebMessage\*](capi-web-arkweb-webmessage8h.md) | ArkWeb\_WebMessagePtr | Post Message数据结构体指针。 |
| [ArkWeb\_JavaScriptValue\*](capi-web-arkweb-javascriptvalue8h.md) | ArkWeb\_JavaScriptValuePtr | JavaScript数据结构体指针。 |
| [ArkWeb\_WebMessagePort\*](capi-web-arkweb-webmessageport8h.md) | ArkWeb\_WebMessagePortPtr | Post Message端口结构体指针。 |
| [ArkWeb\_JavaScriptObject](capi-web-arkweb-javascriptobject.md) | ArkWeb\_JavaScriptObject | 注入的JavaScript结构体。 |
| [ArkWeb\_ProxyMethod](capi-web-arkweb-proxymethod.md) | ArkWeb\_ProxyMethod | 注入的Proxy方法通用结构体。 |
| [ArkWeb\_ProxyMethodWithResult](capi-web-arkweb-proxymethodwithresult.md) | ArkWeb\_ProxyMethodWithResult | 注入的Proxy方法通用结构体。 |
| [ArkWeb\_ProxyObject](capi-web-arkweb-proxyobject.md) | ArkWeb\_ProxyObject | 注入的Proxy对象通用结构体。 |
| [ArkWeb\_ProxyObjectWithResult](capi-web-arkweb-proxyobjectwithresult.md) | ArkWeb\_ProxyObjectWithResult | 注入的Proxy对象通用结构体。 |
| [ArkWeb\_ControllerAPI](capi-web-arkweb-controllerapi.md) | ArkWeb\_ControllerAPI | Controller相关的Native API结构体。在调用接口前建议通过ARKWEB\_MEMBER\_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致崩溃。Controller相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |
| [ArkWeb\_ComponentAPI](capi-web-arkweb-componentapi.md) | ArkWeb\_ComponentAPI | Component相关的Native API结构体。在调用接口前建议通过ARKWEB\_MEMBER\_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致崩溃。Component相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |
| [ArkWeb\_WebMessagePortAPI](capi-web-arkweb-webmessageportapi.md) | ArkWeb\_WebMessagePortAPI | Post Message相关的Native API结构体。在调用接口前建议通过ARKWEB\_MEMBER\_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致崩溃。WebMessagePort相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |
| [ArkWeb\_WebMessageAPI](capi-web-arkweb-webmessageapi.md) | ArkWeb\_WebMessageAPI | Post Message数据相关的Native API结构体。在调用接口前建议通过ARKWEB\_MEMBER\_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致崩溃。WebMessage相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |
| [ArkWeb\_CookieManagerAPI](capi-web-arkweb-cookiemanagerapi.md) | ArkWeb\_CookieManagerAPI | 定义了ArkWeb的CookieManager接口。在调用接口之前，建议使用ARKWEB\_MEMBER\_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。CookieManager相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |
| [ArkWeb\_JavaScriptValueAPI](capi-web-arkweb-javascriptvalueapi.md) | ArkWeb\_JavaScriptValueAPI | 定义了ArkWeb的JavaScriptValue接口。在调用接口之前，建议使用ARKWEB\_MEMBER\_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。JavaScriptValue相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkWeb\_WebMessageType](capi-arkweb-type-h.md#arkweb_webmessagetype) | ArkWeb\_WebMessageType | Post Message数据类型。 |
| [ArkWeb\_JavaScriptValueType](capi-arkweb-type-h.md#arkweb_javascriptvaluetype) | ArkWeb\_JavaScriptValueType | JavaScript数据类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*ArkWeb\_OnJavaScriptCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* data, void\* userData)](capi-arkweb-type-h.md#arkweb_onjavascriptcallback) | ArkWeb\_OnJavaScriptCallback | 注入的JavaScript执行完成的回调。 |
| [typedef void (\*ArkWeb\_OnJavaScriptProxyCallback)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)](capi-arkweb-type-h.md#arkweb_onjavascriptproxycallback) | ArkWeb\_OnJavaScriptProxyCallback | Proxy方法被执行的回调。 |
| [typedef ArkWeb\_JavaScriptValuePtr (\*ArkWeb\_OnJavaScriptProxyCallbackWithResult)(const char\* webTag, const ArkWeb\_JavaScriptBridgeData\* dataArray, size\_t arraySize, void\* userData)](capi-arkweb-type-h.md#arkweb_onjavascriptproxycallbackwithresult) | ArkWeb\_OnJavaScriptProxyCallbackWithResult | Proxy方法被执行的回调。 |
| [typedef void (\*ArkWeb\_OnComponentCallback)(const char\* webTag, void\* userData)](capi-arkweb-type-h.md#arkweb_oncomponentcallback) | ArkWeb\_OnComponentCallback | 组件事件通知相关的通用回调。 |
| [typedef void (\*ArkWeb\_OnScrollCallback)(const char\* webTag, void\* userData, double x, double y)](capi-arkweb-type-h.md#arkweb_onscrollcallback) | ArkWeb\_OnScrollCallback | Web组件滚动时的回调函数类型。 |
| [typedef void (\*ArkWeb\_OnMessageEventHandler)(const char\* webTag, const ArkWeb\_WebMessagePortPtr port, const ArkWeb\_WebMessagePtr message, void\* userData)](capi-arkweb-type-h.md#arkweb_onmessageeventhandler) | ArkWeb\_OnMessageEventHandler | 处理HTML发送过来的Post Message数据。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| ARKWEB\_MEMBER\_EXISTS(s, f) ((intptr\_t) & ((s)->f) - (intptr\_t)(s) + sizeof((s)->f) <= \*(size\_t \*)(s)) | 检查结构体中是否存在该成员变量。  **起始版本：** 12 |
| ARKWEB\_MEMBER\_MISSING(s, f) (!ARKWEB\_MEMBER\_EXISTS(s, f) || !((s)->f)) | 当前结构体存在该成员变量则返回false，否则返回true  **起始版本：** 12 |

## 枚举类型说明

### ArkWeb\_WebMessageType

```c
enum ArkWeb_WebMessageType
```

**描述**

Post Message数据类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_NONE = 0 | 错误数据。 |
| ARKWEB\_STRING | 字符串数据类型。 |
| ARKWEB\_BUFFER | 字节流数据类型。 |

### ArkWeb\_JavaScriptValueType

```c
enum ArkWeb_JavaScriptValueType
```

**描述**

JavaScript数据类型。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB\_JAVASCRIPT\_NONE = 0 | 错误数据。 |
| ARKWEB\_JAVASCRIPT\_STRING | 字符串数据类型。 |
| ARKWEB\_JAVASCRIPT\_BOOL | 布尔数据类型。 |

## 函数说明

### ArkWeb\_OnJavaScriptCallback()

```c
typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)
```

**描述**

注入的JavaScript执行完成的回调。用于获取JavaScript代码在Web组件中的执行结果，例如在需要根据JavaScript返回的数据更新原生UI或执行后续逻辑的场景中使用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md)\* data | JavaScriptBridge数据。 |
| void\* userData | 用户自定义的数据。 |

### ArkWeb\_OnJavaScriptProxyCallback()

```c
typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**描述**

Proxy方法被执行的回调。Proxy方法用于Native侧与JavaScript侧的对象交互和自定义操作。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md)\* dataArray | 数组数据。 |
| size\_t arraySize | 数组大小。 |
| void\* userData | 用户自定义的数据。 |

### ArkWeb\_OnJavaScriptProxyCallbackWithResult()

```c
typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**描述**

Proxy方法被执行的回调（有返回值）。用于在JavaScript调用注入的Proxy方法时接收通知并返回执行结果，适用于实现JavaScript与原生代码的桥接通信场景，例如拦截JavaScript调用、执行原生逻辑、计算结果并将结果返回给JavaScript。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_JavaScriptBridgeData](capi-web-arkweb-javascriptbridgedata.md)\* dataArray | 数组数据。 |
| size\_t arraySize | 数组大小。 |
| void\* userData | 用户自定义的数据。 |

### ArkWeb\_OnComponentCallback()

```c
typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)
```

**描述**

接收Web组件事件通知的回调。用于接收Web组件生命周期事件通知，例如页面加载完成、页面销毁、组件可见性变化等场景下的状态变更通知。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| void\* userData | 用户自定义的数据。 |

### ArkWeb\_OnScrollCallback()

```c
typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)
```

**描述**

Web组件滚动时的回调函数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| void\* userData | 用户自定义的数据。 |
| double x | X轴滚动偏移。单位：vp。 |
| double y | Y轴滚动偏移。单位：vp。 |

### ArkWeb\_OnMessageEventHandler()

```c
typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)
```

**描述**

处理HTML发送过来的Post Message数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) port | Post Message端口。 |
| const [ArkWeb\_WebMessagePtr](capi-web-arkweb-webmessage8h.md) message | Post Message数据。 |
| void\* userData | 用户自定义的数据。 |
