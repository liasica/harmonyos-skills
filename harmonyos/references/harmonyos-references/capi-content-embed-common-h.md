---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-common-h
title: content_embed_common.h
breadcrumb: API参考 > 应用框架 > Content Embed Kit（内容嵌入服务） > C API > 头文件 > content_embed_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6134123ca70f4d6524f9011b96a4b4e98bc76b04cb1dfb19ef3a445ec203c0d4
---

## 概述

提供内容嵌入模块的错误码定义和嵌入文档支持能力的类型枚举描述。

**引用文件：** <ContentEmbedKit/content\_embed/content\_embed\_common.h>

**库：** libcontent\_embed\_ndk.so

**系统能力：** SystemCapability.ContentEmbed.ObjectEditor

**起始版本：** 24

**相关模块：** [ContentEmbed](capi-contentembed.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | ContentEmbed\_ErrorCode | 提供内容嵌入模块的错误码定义。 |
| [ContentEmbed\_CapabilityCode](capi-content-embed-common-h.md#contentembed_capabilitycode) | ContentEmbed\_CapabilityCode | 嵌入文档对象支持的功能枚举，并支持通过位掩码组合多个能力值。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| MAX\_OEID\_LENGTH (1 \* 40) | 表示被嵌入文档的标识符OEID的最大字符串长度。  **起始版本：** 24 |

## 枚举类型说明

### ContentEmbed\_ErrorCode

```c
enum ContentEmbed_ErrorCode
```

**描述**

提供内容嵌入模块的错误码定义。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| CE\_ERR\_OK = 0 | 操作成功。  **起始版本：** 24 |
| CE\_PERMISSION\_DENIED = 201 | 权限校验失败。  **起始版本：** 24 |
| CE\_ERR\_PARAM\_INVALID = 401 | 参数不合法。  **起始版本：** 24 |
| CE\_ERR\_DEVICE\_NOT\_SUPPORTED = 801 | 当前设备不支持此功能。  **起始版本：** 24 |
| CE\_ERR\_NULL\_POINTER = 35300001 | 返回空指针，可能是内存分配失败或内部错误。  **起始版本：** 24 |
| CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED = 35300002 | 客户端未注册对应的回调函数。  **起始版本：** 24 |
| CE\_ERR\_EXTENSION\_ERROR = 35300003 | OE Extension发生未知错误。  **起始版本：** 24 |
| CE\_ERR\_SYSTEM\_ABNORMAL = 35300004 | 系统服务出现异常，可能是服务未启动、连接中断或权限不足。  **起始版本：** 24 |
| CE\_ERR\_STORAGE\_OPERATION\_FAILED = 35300005 | OE文档Storage对象相关操作失败。  **起始版本：** 24 |
| CE\_ERR\_STREAM\_OPERATION\_FAILED = 35300006 | OE文档Stream对象相关操作失败。  **起始版本：** 24 |
| CE\_ERR\_FILE\_OPERATION\_FAILED = 35300007 | 文件操作失败，可能是文件不存在、权限不足、路径错误或磁盘空间不足。  **起始版本：** 24 |
| CE\_ERR\_IN\_DLP\_SANDBOX = 35300008 | 当前应用正在DLP沙箱环境中运行，暂不支持调用相关功能。  **起始版本：** 24 |
| CE\_ERR\_IMAGE\_PACKER\_OPERATION\_FAILED = 35300009 | ImagePacker操作失败。  **起始版本：** 24 |
| CE\_ERR\_CLIENT\_CALLBACK\_FAILED = 35300010 | 客户端注册的回调函数在执行过程中发生异常。  **起始版本：** 24 |
| CE\_ERR\_EXTENSION\_ABNORMAL\_EXIT = 35300011 | OE Extension意外退出。  **起始版本：** 24 |
| CE\_ERR\_INVALID\_LINKING\_PATH = 35300012 | 链接到不允许被链接目录中的文件，如应用沙箱目录内的文件。  **起始版本：** 24 |
| CE\_ERR\_CONNECT\_LIMIT\_EXCEED = 35300013 | 当前OE Extension连接超出限制。  **起始版本：** 24 |
| CE\_ERR\_FILE\_NOT\_GRANT = 35300014 | 当前文件未授权。  **起始版本：** 24 |
| CE\_ERR\_DISK\_FULL = 35300015 | 当前磁盘空间不足。  **起始版本：** 24 |
| CE\_ERR\_EXTENSION\_NOT\_SUPPORT = 35300016 | 当前OE Extension不支持该能力。  **起始版本：** 24 |

### ContentEmbed\_CapabilityCode

```c
enum ContentEmbed_CapabilityCode
```

**描述**

嵌入文档对象支持的功能枚举，并支持通过位掩码组合多个能力值。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| CE\_CAPABILITY\_SUPPORT\_SNAPSHOT = 1 << 0 | 表示支持获取OE文档的快照图像。  **起始版本：** 24 |
| CE\_CAPABILITY\_SUPPORT\_DO\_EDIT = 1 << 1 | 表示支持对OE文档进行编辑操作。  **起始版本：** 24 |
