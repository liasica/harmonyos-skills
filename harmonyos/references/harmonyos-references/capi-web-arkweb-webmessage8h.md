---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessage8h
title: ArkWeb_WebMessage*
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_WebMessage*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:80a6d0b9d0195427577257a51f2053eb87dae6056536e49f6ce59136dab29dcb
---

```c
typedef struct ArkWeb_WebMessage* ArkWeb_WebMessagePtr
```

## 概述

ArkWeb\_WebMessage是用于跨上下文消息通信的Web消息结构体，定义了消息的基本格式和数据承载能力。该结构体是Web消息通信的基础数据单元，支持在Native代码和Web页面之间传递字符串和二进制数据。

**使用场景：**

用于在Native端和Web页面之间进行消息通信，例如：

* Native端向Web页面发送控制指令或数据。
* Web页面向Native端发送用户操作结果或请求数据。
* 跨上下文的异步消息传递和数据同步。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_type.h](capi-arkweb-type-h.md)
