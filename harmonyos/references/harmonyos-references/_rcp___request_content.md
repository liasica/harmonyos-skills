---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content
title: Rcp_RequestContent
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_RequestContent
category: harmonyos-references
scraped_at: 2026-04-28T08:09:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:860ca01e9f1727057b0d7bc7a1058ebdaa0c75bb886b5d8be99a852840388481
---

## 概述

PhonePC/2in1TabletTVWearable

请求的内容。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ContentType](remote-communication-overview.md#rcp_contenttype)[type](_rcp___request_content.md#type) | 表示union中使用的数据类型。 |
| union {  [Rcp\_Buffer](_rcp___buffer.md) [contentStr](_rcp___request_content.md#contentstr)  [Rcp\_Form](remote-communication-overview.md#rcp_form) \* [form](_rcp___request_content.md#form)  [Rcp\_MultipartForm](remote-communication-overview.md#rcp_multipartform) \* [multipartForm](_rcp___request_content.md#multipartform)  [Rcp\_GetDataCallback](remote-communication-overview.md#rcp_getdatacallback) [getDataCallback](_rcp___request_content.md#getdatacallback)  } | contentStr：文本。  form：表单。  multipartForm：多部分表单。  getDataCallback：使用回调函数获取数据。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### contentStr

PhonePC/2in1TabletTVWearable

```
1. Rcp_Buffer Rcp_RequestContent::contentStr
```

**描述**

字符串内容。

### form

PhonePC/2in1TabletTVWearable

```
1. Rcp_Form* Rcp_RequestContent::form
```

**描述**

表单内容。

### getDataCallback

PhonePC/2in1TabletTVWearable

```
1. Rcp_GetDataCallback Rcp_RequestContent::getDataCallback
```

**描述**

回调函数。

### multipartForm

PhonePC/2in1TabletTVWearable

```
1. Rcp_MultipartForm* Rcp_RequestContent::multipartForm
```

**描述**

多部分表单内容。

### type

PhonePC/2in1TabletTVWearable

```
1. Rcp_ContentType Rcp_RequestContent::type
```

**描述**

表示union中使用的数据类型。
