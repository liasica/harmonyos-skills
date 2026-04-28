---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageportapi
title: ArkWeb_WebMessagePortAPI
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_WebMessagePortAPI
category: harmonyos-references
scraped_at: 2026-04-28T08:05:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4607b4b05eabbee51c2de1283576652b4d4d0faf381aeb729951c1ba4c6f7573
---

```
1. typedef struct {...} ArkWeb_WebMessagePortAPI
```

## 概述

PhonePC/2in1TabletTVWearable

Post Message相关的Native API结构体。在调用接口前建议通过[ARKWEB\_MEMBER\_MISSING](capi-arkweb-type-h.md#宏定义)校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessagePort相关接口需在UI线程中调用OH\_ArkWeb\_GetNativeAPI方法获取。

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
| [ArkWeb\_ErrorCode (\*postMessage)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, const ArkWeb\_WebMessagePtr webMessage)](capi-web-arkweb-webmessageportapi.md#postmessage) | 发送消息到HTML。 |
| [void (\*close)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag)](capi-web-arkweb-webmessageportapi.md#close) | 关闭消息端口。 |
| [void (\*setMessageEventHandler)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, ArkWeb\_OnMessageEventHandler messageEventHandler, void\* userData)](capi-web-arkweb-webmessageportapi.md#setmessageeventhandler) | 设置接收HTML消息的回调。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### postMessage()

PhonePC/2in1TabletTVWearable

```
1. ArkWeb_ErrorCode (*postMessage)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag, const ArkWeb_WebMessagePtr webMessage)
```

**描述：**

发送消息到HTML。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |
| const [ArkWeb\_WebMessagePtr](capi-web-arkweb-webmessage8h.md) webMessage | 需要发送的消息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkWeb\_ErrorCode](capi-arkweb-error-code-h.md#arkweb_errorcode) | [ARKWEB\_SUCCESS](capi-arkweb-error-code-h.md#arkweb_errorcode) 执行成功。  [ARKWEB\_INVALID\_PARAM](capi-arkweb-error-code-h.md#arkweb_errorcode) 参数无效。  [ARKWEB\_INIT\_ERROR](capi-arkweb-error-code-h.md#arkweb_errorcode) 初始化失败，没有找到与webTag绑定的Web组件。 |

### close()

PhonePC/2in1TabletTVWearable

```
1. void (*close)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag)
```

**描述：**

关闭消息端口。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |

### setMessageEventHandler()

PhonePC/2in1TabletTVWearable

```
1. void (*setMessageEventHandler)(const ArkWeb_WebMessagePortPtr webMessagePort, const char* webTag,
2. ArkWeb_OnMessageEventHandler messageEventHandler, void* userData)
```

**描述：**

设置接收HTML消息的回调。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [ArkWeb\_WebMessagePortPtr](capi-web-arkweb-webmessageport8h.md) webMessagePort | Post Message端口结构体指针。 |
| const char\* webTag | Web组件名称。 |
| [ArkWeb\_OnMessageEventHandler](capi-arkweb-type-h.md#arkweb_onmessageeventhandler) messageEventHandler | 处理消息的回调。 |
| void\* userData | 用户自定义数据。 |
