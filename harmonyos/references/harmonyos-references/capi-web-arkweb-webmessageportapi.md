---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi
title: ArkWeb_WebMessagePortAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_WebMessagePortAPI
category: harmonyos-references
scraped_at: 2026-09-02T15:01:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d9a35fb3207fbc0a4c9a78124bce8899026bcab0120031a788de83834c030a27
---

```c
typedef struct {...} ArkWeb_WebMessagePortAPI
```

## 概述

ArkWeb\_WebMessagePortAPI是Web消息端口相关Native API结构体。该结构体提供了消息端口的创建、关闭、消息发送和消息接收回调注册等功能。此API是postMessage桥接的核心组件，支持在Native代码和Web页面之间建立持久的双向通信通道。适用于需要在原生应用与Web页面之间进行数据交互的场景，解决了跨语言通信的难题，提升了应用的扩展能力和开发效率。

Web消息端口相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取，调用前建议通过[ARKWEB\_MEMBER\_MISSING](capi-arkweb-type-h.md#宏定义)校验函数指针的可用性，避免SDK与设备ROM不匹配导致崩溃。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t size | 结构体的大小（字节）。 |

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [ArkWeb\_ErrorCode (\*postMessage)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, const ArkWeb\_WebMessagePtr webMessage)](capi-web-arkweb-webmessageportapi.md#postmessage) | 发送消息到HTML。 |
| [void (\*close)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag)](capi-web-arkweb-webmessageportapi.md#close) | 关闭消息端口。 |
| [void (\*setMessageEventHandler)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, ArkWeb\_OnMessageEventHandler messageEventHandler, void\* userData)](capi-web-arkweb-webmessageportapi.md#setmessageeventhandler) | 设置接收HTML消息的回调。 |

## 成员函数说明

### postMessage()

```c
ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)
```

**描述：**

发送消息到HTML。在Native代码向Web页面传递数据、指令或配置信息时使用，例如表单数据同步、控制指令下发等。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称，用于标识要操作的Web组件。必须是与Web组件绑定的唯一标识符，如果未找到与webTag绑定的Web组件将返回初始化失败错误。 |
| const [ArkWeb\_WebMessagePtr](capi-web-arkweb-webmessage8h.md) webMessage | 需要发送的消息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 执行成功。  [ARKWEB\_INVALID\_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode) 参数无效。  **可能原因：**  - webMessagePort或webMessage参数为空。  - 参数类型不正确。  **解决措施：**  - 检查参数是否为空指针。  - 确认参数类型是否符合接口要求。  [ARKWEB\_INIT\_ERROR](capi-arkweb-error-code-h.md#arkweb_errorcode) 初始化失败，没有找到与webTag绑定的Web组件。  **可能原因：**  - Web组件未正确初始化。  - webTag参数与实际Web组件名称不匹配。  **解决措施：**  - 确认Web组件已完成初始化。  - 检查webTag参数是否与Web组件名称一致。 |

### close()

```c
void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)
```

**描述：**

关闭消息端口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |

### setMessageEventHandler()

```c
void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag,
        ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)
```

**描述：**

设置接收HTML消息的回调。在需要接收和处理来自Web页面的消息、请求或事件通知时使用。例如接收用户输入、状态更新通知等。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |
| [ArkWeb\_OnMessageEventHandler](capi-arkweb-type-h.md#arkweb_onmessageeventhandler) messageEventHandler | 处理消息的回调。 |
| void\* userData | 用户自定义数据，将在触发回调时传递给messageEventHandler回调函数。可用于携带上下文信息或额外的业务数据，由应用自行管理其生命周期。 |
