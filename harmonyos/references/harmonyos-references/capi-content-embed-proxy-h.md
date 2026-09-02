---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-proxy-h
title: content_embed_proxy.h
breadcrumb: API参考 > 应用框架 > Content Embed Kit（内容嵌入服务） > C API > 头文件 > content_embed_proxy.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8aa98735393a3b57c37aa5e0d0f7ab4a4e08f8de740ad0d9dc06b48644162356
---

## 概述

为客户端应用提供服务端应用注册的OE Extension信息查询接口和与服务端OE Extension对象交互的数据结构及相关操作接口。

**引用文件：** <ContentEmbedKit/content\_embed/content\_embed\_proxy.h>

**库：** libcontent\_embed\_ndk.so

**系统能力：** SystemCapability.ContentEmbed.ObjectEditor

**起始版本：** 24

**相关模块：** [ContentEmbed](capi-contentembed.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ContentEmbed\_Info](capi-contentembed-contentembed-info.md) | ContentEmbed\_Info | 声明ContentEmbed\_Info结构体类型。包含客户端可获取的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)集合信息。 |
| [ContentEmbed\_Format](capi-contentembed-contentembed-format.md) | ContentEmbed\_Format | 声明ContentEmbed\_Format结构体类型。包含服务端应用OE Extension注册的OEID、显示名称、描述信息、图标和文件扩展名等信息。 |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) | ContentEmbed\_ExtensionProxy | 声明ContentEmbed\_ExtensionProxy结构体类型。用于指向OE文档在客户端封装的文档嵌入和编辑的程序对象（简称客户端OE对象）。 |
| [ContentEmbed\_Document](capi-contentembed-contentembed-document.md) | ContentEmbed\_Document | 声明OE文档结构体类型。封装了被嵌入的文档的元数据、内容和存储结构。 |
| [ContentEmbed\_Capability](capi-contentembed-contentembed-capability.md) | ContentEmbed\_Capability | 声明ContentEmbed\_Capability结构体类型。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| MAX\_NAME\_LENGTH (1 \* 1024) | 定义[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)中名称字段的最大字符数限制。  **起始版本：** 24 |
| MAX\_DESCRIPTION\_LENGTH (1 \* 1024) | 定义[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)中描述字段的最大字符数限制。  **起始版本：** 24 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_CreateContentEmbedInfo(ContentEmbed\_Info \*\*info)](capi-content-embed-proxy-h.md#oh_contentembed_createcontentembedinfo) | - | 创建[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。  开发者可通过[OH\_ContentEmbed\_DestroyContentEmbedInfo](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedinfo)销毁实例，以避免内存泄漏。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_DestroyContentEmbedInfo(ContentEmbed\_Info \*info)](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedinfo) | - | 销毁[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetContentEmbedInfo(const char \*locale, ContentEmbed\_Info \*info)](capi-content-embed-proxy-h.md#oh_contentembed_getcontentembedinfo) | - | 根据区域设置获取[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetFormatCountFromInfo(const ContentEmbed\_Info \*info, uint32\_t \*count)](capi-content-embed-proxy-h.md#oh_contentembed_getformatcountfrominfo) | - | 获取[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例中的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的数量。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetFormatFromInfo(const ContentEmbed\_Info \*info, uint32\_t index, ContentEmbed\_Format \*\*format)](capi-content-embed-proxy-h.md#oh_contentembed_getformatfrominfo) | - | 从[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例中获取指定索引位置的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_CreateContentEmbedFormat(ContentEmbed\_Format \*\*format)](capi-content-embed-proxy-h.md#oh_contentembed_createcontentembedformat) | - | 创建[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。  开发者可通过[OH\_ContentEmbed\_DestroyContentEmbedFormat](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedformat)销毁实例，以避免内存泄漏。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_DestroyContentEmbedFormat(ContentEmbed\_Format \*format)](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedformat) | - | 销毁[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetContentEmbedFormatByOEidAndLocale(const char \*oeid, const char \*locale, ContentEmbed\_Format \*format)](capi-content-embed-proxy-h.md#oh_contentembed_getcontentembedformatbyoeidandlocale) | - | 根据OEID和区域设置获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetOEidFromFormat(const ContentEmbed\_Format \*format, char \*oeid)](capi-content-embed-proxy-h.md#oh_contentembed_getoeidfromformat) | - | 获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的OEID。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetNameAndDescriptionFromFormat(const ContentEmbed\_Format \*format, char \*name, char \*description)](capi-content-embed-proxy-h.md#oh_contentembed_getnameanddescriptionfromformat) | - | 从[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例中获取其本地化的显示名称和描述信息。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_GetIconFromFormat(const ContentEmbed\_Format \*format, OH\_PixelmapNative \*\*icon)](capi-content-embed-proxy-h.md#oh_contentembed_geticonfromformat) | - | 获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的图标。 |
| [char\*\* OH\_ContentEmbed\_GetFileNameExtensionsFromFormat(const ContentEmbed\_Format \*format, unsigned int \*count)](capi-content-embed-proxy-h.md#oh_contentembed_getfilenameextensionsfromformat) | - | 获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的文件扩展名列表。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_CreateExtensionProxy(ContentEmbed\_Document \*document, ContentEmbed\_ExtensionProxy \*\*proxy, void \*contextPtr)](capi-content-embed-proxy-h.md#oh_contentembed_createextensionproxy) | - | 创建[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)实例。  开发者可通过[OH\_ContentEmbed\_DestroyExtensionProxy](capi-content-embed-proxy-h.md#oh_contentembed_destroyextensionproxy)销毁实例，以避免内存泄漏。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_DestroyExtensionProxy(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_destroyextensionproxy) | - | 销毁[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)实例。 |
| [typedef void (\*OH\_ContentEmbed\_ClientCallbackOnUpdateFunc)(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonupdatefunc) | OH\_ContentEmbed\_ClientCallbackOnUpdateFunc | OE文档更新时通知客户端的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnUpdateFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronupdatefunc)将此函数注册到客户端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_ClientCallbackOnErrorFunc)(ContentEmbed\_ExtensionProxy \*proxy, ContentEmbed\_ErrorCode error)](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonerrorfunc) | OH\_ContentEmbed\_ClientCallbackOnErrorFunc | OE文档错误时通知客户端的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnErrorFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronerrorfunc)将此函数注册到客户端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc)(ContentEmbed\_ExtensionProxy \*proxy, bool dataModified)](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackoneditingfinishedfunc) | OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc | OE文档编辑完成时通知客户端的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnEditingFinishedFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeroneditingfinishedfunc)将此函数注册到客户端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc)(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonextensionstoppedfunc) | OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc | OE Extension停止时回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnExtensionStoppedFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronextensionstoppedfunc)将此函数注册到客户端OE对象。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_RegisterOnUpdateFunc(ContentEmbed\_ExtensionProxy \*proxy, OH\_ContentEmbed\_ClientCallbackOnUpdateFunc onUpdateFunc)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronupdatefunc) | - | 向客户端OE对象注册OE文档更新时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_RegisterOnErrorFunc(ContentEmbed\_ExtensionProxy \*proxy, OH\_ContentEmbed\_ClientCallbackOnErrorFunc onErrorFunc)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronerrorfunc) | - | 向客户端OE对象注册OE文档触发错误时回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_RegisterOnEditingFinishedFunc(ContentEmbed\_ExtensionProxy \*proxy, OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc onEditingFinishedFunc)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeroneditingfinishedfunc) | - | 向客户端OE对象注册OE文档编辑完成时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_RegisterOnExtensionStoppedFunc(ContentEmbed\_ExtensionProxy \*proxy, OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc onExtensionStoppedFunc)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronextensionstoppedfunc) | - | 向客户端OE对象注册OE Extension停止时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_StartWork(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_startwork) | - | 连接服务端OE Extension，建立与OE Extension的通信通道。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_StopWork(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_stopwork) | - | 断开与OE Extension的通信通道。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_GetSnapshot(ContentEmbed\_ExtensionProxy \*proxy, OH\_PixelmapNative \*\*snapshot)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_getsnapshot) | - | 从客户端OE对象获取当前OE文档的快照图像，用于预览或缩略图显示。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_DoEdit(ContentEmbed\_ExtensionProxy \*proxy)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_doedit) | - | 客户端OE对象请求OE Extension实例进入编辑模式。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_GetEditStatus(ContentEmbed\_ExtensionProxy \*proxy, bool \*isEditing, bool \*isModified)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_geteditstatus) | - | 查询服务端OE Extension实例对OE文档的当前编辑状态和修改状态。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_GetCapability(ContentEmbed\_ExtensionProxy \*proxy, uint32\_t \*bitmask)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_getcapability) | - | 获取服务端OE Extension实例拥有的能力，以位掩码形式返回，各位的含义参见[ContentEmbed\_CapabilityCode](capi-content-embed-common-h.md#contentembed_capabilitycode)。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Proxy\_GetDocument(ContentEmbed\_ExtensionProxy \*proxy, ContentEmbed\_Document \*\*ceDocument)](capi-content-embed-proxy-h.md#oh_contentembed_proxy_getdocument) | - | 从客户端OE对象获取其关联的OE文档对象。  该OE文档对象通过[OH\_ContentEmbed\_CreateDocumentByOEid](capi-content-embed-document-h.md#oh_contentembed_createdocumentbyoeid)、[OH\_ContentEmbed\_CreateDocumentByFile](capi-content-embed-document-h.md#oh_contentembed_createdocumentbyfile)或[OH\_ContentEmbed\_LoadDocumentFromFile](capi-content-embed-document-h.md#oh_contentembed_loaddocumentfromfile)方式创建。  当该OE文档不再需要时，应调用[OH\_ContentEmbed\_DestroyDocument](capi-content-embed-document-h.md#oh_contentembed_destroydocument)将其销毁。 |

## 函数说明

### OH\_ContentEmbed\_CreateContentEmbedInfo()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedInfo(ContentEmbed_Info **info)
```

**描述**

创建[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。

开发者可通过[OH\_ContentEmbed\_DestroyContentEmbedInfo](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedinfo)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_Info](capi-contentembed-contentembed-info.md) \*\*info | 输出参数。该指针指向新创建的[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_DestroyContentEmbedInfo()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedInfo(ContentEmbed_Info *info)
```

**描述**

销毁[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_Info](capi-contentembed-contentembed-info.md) \*info | 指向[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetContentEmbedInfo()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedInfo(const char *locale, ContentEmbed_Info *info)
```

**描述**

根据区域设置获取[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例。

**需要权限：** ohos.permission.CONNECT\_OBJECTEDITOR\_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*locale | [表示区域ID的字符串](../harmonyos-guides/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成，例如"zh-Hans-CN"。当locale为空时，默认使用系统区域设置。 |
| [ContentEmbed\_Info](capi-contentembed-contentembed-info.md) \*info | 输出参数。该指针指向ContentEmbed\_Info对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_PERMISSION\_DENIED：表示权限校验失败。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务工作异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetFormatCountFromInfo()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatCountFromInfo(const ContentEmbed_Info *info, uint32_t *count)
```

**描述**

获取[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例中的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的数量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Info](capi-contentembed-contentembed-info.md) \*info | 指向[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)对象指针。 |
| uint32\_t \*count | 输出参数。存储[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetFormatFromInfo()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetFormatFromInfo(const ContentEmbed_Info *info, uint32_t index, ContentEmbed_Format **format)
```

**描述**

从[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)实例中获取指定索引位置的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Info](capi-contentembed-contentembed-info.md) \*info | 指向[ContentEmbed\_Info](capi-contentembed-contentembed-info.md)对象指针。 |
| uint32\_t index | 要获取的格式的索引，从0开始。 |
| [ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*\*format | 输出参数。该指针指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_CreateContentEmbedFormat()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_CreateContentEmbedFormat(ContentEmbed_Format **format)
```

**描述**

创建[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。

开发者可通过[OH\_ContentEmbed\_DestroyContentEmbedFormat](capi-content-embed-proxy-h.md#oh_contentembed_destroycontentembedformat)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*\*format | 输出参数。该指针指向新创建的[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_DestroyContentEmbedFormat()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyContentEmbedFormat(ContentEmbed_Format *format)
```

**描述**

销毁[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetContentEmbedFormatByOEidAndLocale()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetContentEmbedFormatByOEidAndLocale(const char *oeid, const char *locale, ContentEmbed_Format *format)
```

**描述**

根据OEID和区域设置获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例。

**需要权限：** ohos.permission.CONNECT\_OBJECTEDITOR\_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*oeid | 文档格式的唯一标识符字符串。 |
| const char \*locale | [表示区域ID的字符串](../harmonyos-guides/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成，例如"zh-Hans-CN"。当locale为空时，默认使用系统区域设置。 |
| [ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 输出参数。该指针指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_PERMISSION\_DENIED：表示权限校验失败。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务工作异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetOEidFromFormat()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetOEidFromFormat(const ContentEmbed_Format *format, char *oeid)
```

**描述**

获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的OEID。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象指针。 |
| char \*oeid | 输出参数。用于存储标识符OEID字符串的字符数组。建议数组长度为[MAX\_OEID\_LENGTH](capi-content-embed-common-h.md#宏定义)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetNameAndDescriptionFromFormat()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetNameAndDescriptionFromFormat(const ContentEmbed_Format *format, char *name, char *description)
```

**描述**

从[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例中获取其本地化的显示名称和描述信息。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象指针。 |
| char \*name | 输出参数。用于存储名称的字符数组。建议数组长度为[MAX\_NAME\_LENGTH](capi-content-embed-proxy-h.md#宏定义)。 |
| char \*description | 输出参数。用于存储描述信息的字符数组。建议数组长度为[MAX\_DESCRIPTION\_LENGTH](capi-content-embed-proxy-h.md#宏定义)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetIconFromFormat()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_GetIconFromFormat(const ContentEmbed_Format *format, OH_PixelmapNative **icon)
```

**描述**

获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的图标。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象指针。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md) \*\*icon | 输出参数。用于存储图标的[OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)实例指针。  开发者需要调用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)销毁，以避免内存泄漏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。 |

### OH\_ContentEmbed\_GetFileNameExtensionsFromFormat()

```c
char** OH_ContentEmbed_GetFileNameExtensionsFromFormat(const ContentEmbed_Format *format, unsigned int *count)
```

**描述**

获取[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)实例的文件扩展名列表。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const ContentEmbed\_Format](capi-contentembed-contentembed-format.md) \*format | 指向[ContentEmbed\_Format](capi-contentembed-contentembed-format.md)对象指针。 |
| unsigned int \*count | 输出参数。存储返回的文件扩展名数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char\*\* | 返回文件扩展名字符串数组的指针。 |

### OH\_ContentEmbed\_CreateExtensionProxy()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_CreateExtensionProxy(ContentEmbed_Document *document, ContentEmbed_ExtensionProxy **proxy, void *contextPtr)
```

**描述**

创建[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)实例。

开发者可通过[OH\_ContentEmbed\_DestroyExtensionProxy](capi-content-embed-proxy-h.md#oh_contentembed_destroyextensionproxy)销毁实例，以避免内存泄漏。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_Document](capi-contentembed-contentembed-document.md) \*document | 指向OE文档实例的指针。 |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*\*proxy | 输出参数。该指针指向新创建的[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象。 |
| void \*contextPtr | 上下文实例的指针，用于传递应用上下文信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_DestroyExtensionProxy()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_DestroyExtensionProxy(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

销毁[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_ClientCallbackOnUpdateFunc()

```c
typedef void (*OH_ContentEmbed_ClientCallbackOnUpdateFunc)(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

OE文档更新时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnUpdateFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronupdatefunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

### OH\_ContentEmbed\_ClientCallbackOnErrorFunc()

```c
typedef void (*OH_ContentEmbed_ClientCallbackOnErrorFunc)(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_ErrorCode error)
```

**描述**

OE文档错误时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnErrorFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronerrorfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) error | 表示发生的错误码，详细定义参见[ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode)。 |

### OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc()

```c
typedef void (*OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc)(ContentEmbed_ExtensionProxy *proxy, bool dataModified)
```

**描述**

OE文档编辑完成时通知客户端的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnEditingFinishedFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeroneditingfinishedfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| bool dataModified | 表示OE文档数据是否被修改。true表示OE文档已修改；false表示未修改。 |

### OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc()

```c
typedef void (*OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc)(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

OE Extension停止时回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Proxy\_RegisterOnExtensionStoppedFunc](capi-content-embed-proxy-h.md#oh_contentembed_proxy_registeronextensionstoppedfunc)将此函数注册到客户端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

### OH\_ContentEmbed\_Proxy\_RegisterOnUpdateFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnUpdateFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnUpdateFunc onUpdateFunc)
```

**描述**

向客户端OE对象注册OE文档更新时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [OH\_ContentEmbed\_ClientCallbackOnUpdateFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonupdatefunc) onUpdateFunc | 要注册的[OH\_ContentEmbed\_ClientCallbackOnUpdateFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonupdatefunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_RegisterOnErrorFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnErrorFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnErrorFunc onErrorFunc)
```

**描述**

向客户端OE对象注册OE文档触发错误时回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [OH\_ContentEmbed\_ClientCallbackOnErrorFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonerrorfunc) onErrorFunc | 要注册的[OH\_ContentEmbed\_ClientCallbackOnErrorFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonerrorfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_RegisterOnEditingFinishedFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnEditingFinishedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnEditingFinishedFunc onEditingFinishedFunc)
```

**描述**

向客户端OE对象注册OE文档编辑完成时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackoneditingfinishedfunc) onEditingFinishedFunc | 要注册的[OH\_ContentEmbed\_ClientCallbackOnEditingFinishedFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackoneditingfinishedfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_RegisterOnExtensionStoppedFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_RegisterOnExtensionStoppedFunc(ContentEmbed_ExtensionProxy *proxy, OH_ContentEmbed_ClientCallbackOnExtensionStoppedFunc onExtensionStoppedFunc)
```

**描述**

向客户端OE对象注册OE Extension停止时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonextensionstoppedfunc) onExtensionStoppedFunc | 要注册的[OH\_ContentEmbed\_ClientCallbackOnExtensionStoppedFunc](capi-content-embed-proxy-h.md#oh_contentembed_clientcallbackonextensionstoppedfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_StartWork()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StartWork(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

连接服务端OE Extension，建立与OE Extension的通信通道。

**需要权限：** ohos.permission.CONNECT\_OBJECTEDITOR\_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_PERMISSION\_DENIED：表示权限校验失败。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED：表示必要的客户端回调未注册。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。  CE\_ERR\_CONNECT\_LIMIT\_EXCEED：表示OE Extension连接数超出限制。  CE\_ERR\_FILE\_NOT\_GRANT：表示文件未被授权。  CE\_ERR\_DISK\_FULL：表示磁盘已满。 |

### OH\_ContentEmbed\_Proxy\_StopWork()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_StopWork(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

断开与OE Extension的通信通道。

**需要权限：** ohos.permission.CONNECT\_OBJECTEDITOR\_EXTENSION

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_PERMISSION\_DENIED：表示权限校验失败。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_GetSnapshot()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetSnapshot(ContentEmbed_ExtensionProxy *proxy, OH_PixelmapNative **snapshot)
```

**描述**

从客户端OE对象获取当前OE文档的快照图像，用于预览或缩略图显示。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md) \*\*snapshot | 输出参数。用于存储文档快照的[OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)实例指针。  开发者需要调用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)销毁，以避免内存泄漏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_EXTENSION\_ERROR：表示OE Extension发生错误。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。  CE\_ERR\_EXTENSION\_NOT\_SUPPORT：表示OE Extension不支持该能力。 |

### OH\_ContentEmbed\_Proxy\_DoEdit()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_DoEdit(ContentEmbed_ExtensionProxy *proxy)
```

**描述**

客户端OE对象请求OE Extension实例进入编辑模式。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_EXTENSION\_ERROR：表示OE Extension发生错误。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。  CE\_ERR\_EXTENSION\_NOT\_SUPPORT：表示OE Extension不支持该能力。 |

### OH\_ContentEmbed\_Proxy\_GetEditStatus()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetEditStatus(ContentEmbed_ExtensionProxy *proxy, bool *isEditing, bool *isModified)
```

**描述**

查询服务端OE Extension实例对OE文档的当前编辑状态和修改状态。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| bool \*isEditing | 输出参数。表示内容嵌入文档是否正在编辑。true表示正在编辑；false表示未在编辑。 |
| bool \*isModified | 输出参数。表示内容嵌入文档是否已被修改。true表示已修改；false表示未修改。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_EXTENSION\_ERROR：表示OE Extension发生错误。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_GetCapability()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetCapability(ContentEmbed_ExtensionProxy *proxy, uint32_t *bitmask)
```

**描述**

获取服务端OE Extension实例拥有的能力，以位掩码形式返回，各位的含义参见[ContentEmbed\_CapabilityCode](capi-content-embed-common-h.md#contentembed_capabilitycode)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| uint32\_t \*bitmask | 输出参数。表示服务端OE Extension实例拥有的能力，由[ContentEmbed\_CapabilityCode](capi-content-embed-common-h.md#contentembed_capabilitycode)中的值组合而成。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_EXTENSION\_ERROR：表示OE Extension发生错误。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Proxy\_GetDocument()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Proxy_GetDocument(ContentEmbed_ExtensionProxy *proxy, ContentEmbed_Document **ceDocument)
```

**描述**

从客户端OE对象获取其关联的OE文档对象。

该OE文档对象通过[OH\_ContentEmbed\_CreateDocumentByOEid](capi-content-embed-document-h.md#oh_contentembed_createdocumentbyoeid)、[OH\_ContentEmbed\_CreateDocumentByFile](capi-content-embed-document-h.md#oh_contentembed_createdocumentbyfile)或[OH\_ContentEmbed\_LoadDocumentFromFile](capi-content-embed-document-h.md#oh_contentembed_loaddocumentfromfile)方式创建。

当该OE文档不再需要时，应调用[OH\_ContentEmbed\_DestroyDocument](capi-content-embed-document-h.md#oh_contentembed_destroydocument)将其销毁。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md) \*proxy | 指向[ContentEmbed\_ExtensionProxy](capi-contentembed-contentembed-extensionproxy.md)对象的指针。 |
| [ContentEmbed\_Document](capi-contentembed-contentembed-document.md) \*\*ceDocument | 输出参数。用于存储OE文档实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |
