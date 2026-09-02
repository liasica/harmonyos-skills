---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-content-embed-extension-h
title: content_embed_extension.h
breadcrumb: API参考 > 应用框架 > Content Embed Kit（内容嵌入服务） > C API > 头文件 > content_embed_extension.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0d4dcc4020d3927c12af7a947dc12a4c7c6d045e331bef5bed020efe66d430aa
---

## 概述

定义服务端应用OE Extension相关数据结构和操作接口。

**引用文件：** <ContentEmbedKit/content\_embed/content\_embed\_extension.h>

**库：** libcontent\_embed\_ndk.so

**系统能力：** SystemCapability.ContentEmbed.ObjectEditor

**起始版本：** 24

**相关模块：** [ContentEmbed](capi-contentembed.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ContentEmbed\_Document](capi-contentembed-contentembed-document.md) | ContentEmbed\_Document | 声明OE文档结构体类型。封装了被嵌入文档的元数据、内容和存储结构。 |
| [ContentEmbed\_ExtensionContext](capi-contentembed-contentembed-extensioncontext.md) | ContentEmbed\_ExtensionContext | 声明OE Extension上下文的结构体类型。 |
| [ContentEmbed\_ExtensionContext\*](capi-contentembed-contentembed-extensioncontext8h.md) | ContentEmbed\_ExtensionContextHandle | 声明OE Extension上下文对象指针类型。 |
| [ContentEmbed\_ExtensionInstance](capi-contentembed-contentembed-extensioninstance.md) | ContentEmbed\_ExtensionInstance | 声明OE Extension实例的结构体类型。管理扩展的生命周期、回调注册和客户端OE对象关联等核心功能。 |
| [ContentEmbed\_ExtensionInstance\*](capi-contentembed-contentembed-extensioninstance8h.md) | ContentEmbed\_ExtensionInstanceHandle | 声明OE Extension实例对象指针类型。 |
| [ContentEmbed\_Object](capi-contentembed-contentembed-object.md) | ContentEmbed\_Object | 声明ContentEmbed\_Object结构体类型。用于指向OE文档在服务端封装的文档嵌入和编辑的程序对象（简称服务端OE对象）。 |
| [ContentEmbed\_Object\*](capi-contentembed-contentembed-object8h.md) | ContentEmbed\_ObjectHandle | 声明ContentEmbed\_Object对象指针类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_GetContentEmbedContext(ContentEmbed\_ExtensionInstanceHandle ceInstance, ContentEmbed\_ExtensionContextHandle \*ceContext)](capi-content-embed-extension-h.md#oh_contentembed_extension_getcontentembedcontext) | - | 从OE Extension实例中获取其对应的OE Extension上下文对象。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_GetContext(ContentEmbed\_ExtensionContextHandle ceContext, AbilityRuntime\_ContextHandle \*context)](capi-content-embed-extension-h.md#oh_contentembed_extension_getcontext) | - | 从OE Extension上下文中获取AbilityRuntime上下文。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_GetExtensionInstance(AbilityRuntime\_ExtensionInstanceHandle baseInstance, ContentEmbed\_ExtensionInstanceHandle \*ceInstance)](capi-content-embed-extension-h.md#oh_contentembed_extension_getextensioninstance) | - | 从ExtensionAbility基类实例中获取对应的OE Extension实例。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnCreateFunc)(ContentEmbed\_ExtensionInstanceHandle instance, AbilityBase\_Want \*want)](capi-content-embed-extension-h.md#oh_contentembed_extension_oncreatefunc) | OH\_ContentEmbed\_Extension\_OnCreateFunc | OE Extension实例创建时的生命周期函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnCreateFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeroncreatefunc)注册到OE Extension实例。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnDestroyFunc)(ContentEmbed\_ExtensionInstanceHandle instance)](capi-content-embed-extension-h.md#oh_contentembed_extension_ondestroyfunc) | OH\_ContentEmbed\_Extension\_OnDestroyFunc | OE Extension实例销毁时的生命周期函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnDestroyFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondestroyfunc)注册到OE Extension实例。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnObjectAttachFunc)(ContentEmbed\_ExtensionInstanceHandle instance, ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectattachfunc) | OH\_ContentEmbed\_Extension\_OnObjectAttachFunc | 当客户端OE对象连接到OE Extension实例时触发此回调函数，用于执行服务端OE对象关联后的初始化操作。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectattachfunc)注册到OE Extension实例。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnObjectDetachFunc)(ContentEmbed\_ExtensionInstanceHandle instance, ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectdetachfunc) | OH\_ContentEmbed\_Extension\_OnObjectDetachFunc | 当客户端OE对象从OE Extension实例断开连接时触发此回调函数，用于执行服务端OE对象断开连接后的清理操作。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectdetachfunc)注册到OE Extension实例。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc)(ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_onwritetodatastreamfunc) | OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc | 当服务端OE对象写入OE文档数据流时的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnWriteToDataStreamFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronwritetodatastreamfunc)注册到服务端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc)(ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetsnapshotfunc) | OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc | 当客户端OE对象请求获取OE文档快照时的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetSnapshotFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetsnapshotfunc)注册到服务端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnDoEditFunc)(ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_ondoeditfunc) | OH\_ContentEmbed\_Extension\_OnDoEditFunc | 当客户端OE对象请求编辑OE文档时的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnDoEditFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondoeditfunc)注册到服务端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc)(ContentEmbed\_ObjectHandle object, bool \*isEditing, bool \*isModified)](capi-content-embed-extension-h.md#oh_contentembed_extension_ongeteditstatusfunc) | OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc | 当客户端OE对象请求OE文档编辑状态时的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetEditStatusFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongeteditstatusfunc)注册到服务端OE对象。 |
| [typedef void (\*OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc)(ContentEmbed\_ObjectHandle object, uint32\_t \*bitmask)](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetcapabilityfunc) | OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc | 当客户端OE对象查询OE Extension实例支持能力时的回调函数类型。  开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetCapabilityFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetcapabilityfunc)注册到服务端OE对象。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnCreateFunc(ContentEmbed\_ExtensionInstanceHandle instance, OH\_ContentEmbed\_Extension\_OnCreateFunc onCreateFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registeroncreatefunc) | - | 注册OE Extension实例创建时的生命周期函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnDestroyFunc(ContentEmbed\_ExtensionInstanceHandle instance, OH\_ContentEmbed\_Extension\_OnDestroyFunc onDestroyFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondestroyfunc) | - | 注册OE Extension实例销毁时的生命周期函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnObjectAttachFunc(ContentEmbed\_ExtensionInstanceHandle instance, OH\_ContentEmbed\_Extension\_OnObjectAttachFunc onObjectAttachFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectattachfunc) | - | 注册客户端OE对象连接时的回调函数。  可以通过调用[OH\_ContentEmbed\_Extension\_UnRegisterOnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectattachfunc)取消注册。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_UnRegisterOnObjectAttachFunc(ContentEmbed\_ExtensionInstanceHandle instance)](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectattachfunc) | - | 取消注册客户端OE对象连接时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnObjectDetachFunc(ContentEmbed\_ExtensionInstanceHandle instance, OH\_ContentEmbed\_Extension\_OnObjectDetachFunc onObjectDetachFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectdetachfunc) | - | 注册客户端OE对象断开连接时的回调函数。  可以通过调用[OH\_ContentEmbed\_Extension\_UnRegisterOnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectdetachfunc)取消注册。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_UnRegisterOnObjectDetachFunc(ContentEmbed\_ExtensionInstanceHandle instance)](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectdetachfunc) | - | 取消注册客户端OE对象断开连接时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnWriteToDataStreamFunc(ContentEmbed\_ObjectHandle object, OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc onWriteToDataStreamFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronwritetodatastreamfunc) | - | 注册服务端OE对象写入OE文档数据流时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnGetSnapshotFunc(ContentEmbed\_ObjectHandle object, OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc onGetSnapshotFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetsnapshotfunc) | - | 注册客户端OE对象请求获取OE文档快照时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnDoEditFunc(ContentEmbed\_ObjectHandle object, OH\_ContentEmbed\_Extension\_OnDoEditFunc onDoEditFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondoeditfunc) | - | 注册客户端OE对象请求编辑OE文档时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnGetEditStatusFunc(ContentEmbed\_ObjectHandle object, OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc onGetEditStatusFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongeteditstatusfunc) | - | 注册客户端OE对象请求OE文档编辑状态时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_RegisterOnGetCapabilityFunc(ContentEmbed\_ObjectHandle object, OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc onGetCapabilityFunc)](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetcapabilityfunc) | - | 注册客户端OE对象查询OE Extension实例支持能力时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_GetContentEmbedDocument(ContentEmbed\_ObjectHandle object, ContentEmbed\_Document \*\*ceDocument)](capi-content-embed-extension-h.md#oh_contentembed_extension_getcontentembeddocument) | - | 获取服务端OE对象关联的OE文档实例。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_CallbackToOnUpdate(ContentEmbed\_ObjectHandle object)](capi-content-embed-extension-h.md#oh_contentembed_extension_callbacktoonupdate) | - | 触发客户端OE对象注册的OE文档更新回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_CallbackToOnError(ContentEmbed\_ObjectHandle object, ContentEmbed\_ErrorCode code)](capi-content-embed-extension-h.md#oh_contentembed_extension_callbacktoonerror) | - | 触发客户端OE对象注册的OE文档错误回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_CallbackToOnEditingFinished(ContentEmbed\_ObjectHandle object, bool dataModified)](capi-content-embed-extension-h.md#oh_contentembed_extension_callbacktooneditingfinished) | - | 触发客户端OE对象注册的OE文档编辑完成回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_CallbackToOnExtensionStopped(ContentEmbed\_ExtensionInstanceHandle instance)](capi-content-embed-extension-h.md#oh_contentembed_extension_callbacktoonextensionstopped) | - | 触发OE Extension关联的所有客户端OE对象注册的OE Extension停止时的回调函数。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_SetSnapshot(ContentEmbed\_ObjectHandle object, OH\_PixelmapNative \*pixelMap)](capi-content-embed-extension-h.md#oh_contentembed_extension_setsnapshot) | - | 设置客户端OE对象关联的OE文档快照图像。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbility(ContentEmbed\_ExtensionContextHandle context, AbilityBase\_Want \*want)](capi-content-embed-extension-h.md#oh_contentembed_extension_contextstartselfuiability) | - | 通过OE Extension上下文启动自身的[UIAbility](js-apis-app-ability-uiability.md#uiability)。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbilityWithStartOptions(ContentEmbed\_ExtensionContextHandle context, AbilityBase\_Want \*want, AbilityRuntime\_StartOptions \*options)](capi-content-embed-extension-h.md#oh_contentembed_extension_contextstartselfuiabilitywithstartoptions) | - | 使用启动选项启动OE Extension上下文自身的[UIAbility](js-apis-app-ability-uiability.md#uiability)。 |
| [ContentEmbed\_ErrorCode OH\_ContentEmbed\_Extension\_ContextTerminateAbility(ContentEmbed\_ExtensionContextHandle context)](capi-content-embed-extension-h.md#oh_contentembed_extension_contextterminateability) | - | 销毁OE Extension。 |

## 函数说明

### OH\_ContentEmbed\_Extension\_GetContentEmbedContext()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedContext(ContentEmbed_ExtensionInstanceHandle ceInstance, ContentEmbed_ExtensionContextHandle *ceContext)
```

**描述**

从OE Extension实例中获取其对应的OE Extension上下文对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) ceInstance | OE Extension实例对象的指针。 |
| [ContentEmbed\_ExtensionContextHandle](capi-contentembed-contentembed-extensioncontext8h.md) \*ceContext | 输出参数。调用成功后，该指针指向OE Extension实例的上下文对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_GetContext()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContext(ContentEmbed_ExtensionContextHandle ceContext, AbilityRuntime_ContextHandle *context)
```

**描述**

从OE Extension上下文中获取AbilityRuntime上下文。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionContextHandle](capi-contentembed-contentembed-extensioncontext8h.md) ceContext | OE Extension上下文对象的指针。 |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) \*context | 输出参数。调用成功后，该指针指向[AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md)上下文对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_GetExtensionInstance()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetExtensionInstance(AbilityRuntime_ExtensionInstanceHandle baseInstance, ContentEmbed_ExtensionInstanceHandle *ceInstance)
```

**描述**

从ExtensionAbility基类实例中获取对应的OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ExtensionInstanceHandle](capi-abilityruntime-extensioninstance8h.md) baseInstance | [AbilityRuntime\_ExtensionInstanceHandle](capi-abilityruntime-extensioninstance8h.md)实例。 |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) \*ceInstance | 输出参数。调用成功后，该指针指向OE Extension实例对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_OnCreateFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnCreateFunc)(ContentEmbed_ExtensionInstanceHandle instance, AbilityBase_Want *want)
```

**描述**

OE Extension实例创建时的生命周期函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnCreateFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeroncreatefunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | OE Extension实例对象的指针。 |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | [AbilityBase\_Want](capi-abilitybase-want.md)实例的指针。 |

### OH\_ContentEmbed\_Extension\_OnDestroyFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnDestroyFunc)(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

OE Extension实例销毁时的生命周期函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnDestroyFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondestroyfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | OE Extension实例对象的指针。 |

### OH\_ContentEmbed\_Extension\_OnObjectAttachFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnObjectAttachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象连接到OE Extension实例时触发此回调函数，用于执行服务端OE对象关联后的初始化操作。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectattachfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | OE Extension实例对象的指针。 |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

### OH\_ContentEmbed\_Extension\_OnObjectDetachFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnObjectDetachFunc)(ContentEmbed_ExtensionInstanceHandle instance, ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象从OE Extension实例断开连接时触发此回调函数，用于执行服务端OE对象断开连接后的清理操作。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronobjectdetachfunc)注册到OE Extension实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | OE Extension实例对象的指针。 |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

### OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnWriteToDataStreamFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当服务端OE对象写入OE文档数据流时的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnWriteToDataStreamFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registeronwritetodatastreamfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

### OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnGetSnapshotFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象请求获取OE文档快照时的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetSnapshotFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetsnapshotfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

### OH\_ContentEmbed\_Extension\_OnDoEditFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnDoEditFunc)(ContentEmbed_ObjectHandle object)
```

**描述**

当客户端OE对象请求编辑OE文档时的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnDoEditFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerondoeditfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

### OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnGetEditStatusFunc)(ContentEmbed_ObjectHandle object, bool *isEditing, bool *isModified)
```

**描述**

当客户端OE对象请求OE文档编辑状态时的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetEditStatusFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongeteditstatusfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| bool \*isEditing | 输出参数。表示OE文档是否正在编辑，true表示正在编辑；false表示未编辑。 |
| bool \*isModified | 输出参数。表示OE文档是否已被修改，true表示已被修改；false表示未修改。 |

### OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc()

```c
typedef void (*OH_ContentEmbed_Extension_OnGetCapabilityFunc)(ContentEmbed_ObjectHandle object, uint32_t *bitmask)
```

**描述**

当客户端OE对象查询OE Extension实例支持能力时的回调函数类型。

开发者需要实现此函数并通过[OH\_ContentEmbed\_Extension\_RegisterOnGetCapabilityFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_registerongetcapabilityfunc)注册到服务端OE对象。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| uint32\_t \*bitmask | 输出参数，表示OE Extension实例支持的能力，由[ContentEmbed\_CapabilityCode](capi-content-embed-common-h.md#contentembed_capabilitycode)中的值组合而成。 |

### OH\_ContentEmbed\_Extension\_RegisterOnCreateFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnCreateFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnCreateFunc onCreateFunc)
```

**描述**

注册OE Extension实例创建时的生命周期函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |
| [OH\_ContentEmbed\_Extension\_OnCreateFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_oncreatefunc) onCreateFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnCreateFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_oncreatefunc)生命周期函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnDestroyFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDestroyFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnDestroyFunc onDestroyFunc)
```

**描述**

注册OE Extension实例销毁时的生命周期函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |
| [OH\_ContentEmbed\_Extension\_OnDestroyFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ondestroyfunc) onDestroyFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnDestroyFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ondestroyfunc)生命周期函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnObjectAttachFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectAttachFunc onObjectAttachFunc)
```

**描述**

注册客户端OE对象连接时的回调函数。

可以通过调用[OH\_ContentEmbed\_Extension\_UnRegisterOnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectattachfunc)取消注册。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |
| [OH\_ContentEmbed\_Extension\_OnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectattachfunc) onObjectAttachFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnObjectAttachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectattachfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_UnRegisterOnObjectAttachFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectAttachFunc(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

取消注册客户端OE对象连接时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnObjectDetachFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance, OH_ContentEmbed_Extension_OnObjectDetachFunc onObjectDetachFunc)
```

**描述**

注册客户端OE对象断开连接时的回调函数。

可以通过调用[OH\_ContentEmbed\_Extension\_UnRegisterOnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_unregisteronobjectdetachfunc)取消注册。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |
| [OH\_ContentEmbed\_Extension\_OnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectdetachfunc) onObjectDetachFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnObjectDetachFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onobjectdetachfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_UnRegisterOnObjectDetachFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_UnRegisterOnObjectDetachFunc(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

取消注册客户端OE对象断开连接时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnWriteToDataStreamFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnWriteToDataStreamFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnWriteToDataStreamFunc onWriteToDataStreamFunc)
```

**描述**

注册服务端OE对象写入OE文档数据流时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onwritetodatastreamfunc) onWriteToDataStreamFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnWriteToDataStreamFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_onwritetodatastreamfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnGetSnapshotFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetSnapshotFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetSnapshotFunc onGetSnapshotFunc)
```

**描述**

注册客户端OE对象请求获取OE文档快照时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetsnapshotfunc) onGetSnapshotFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnGetSnapshotFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetsnapshotfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnDoEditFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnDoEditFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnDoEditFunc onDoEditFunc)
```

**描述**

注册客户端OE对象请求编辑OE文档时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_ContentEmbed\_Extension\_OnDoEditFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ondoeditfunc) onDoEditFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnDoEditFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ondoeditfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnGetEditStatusFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetEditStatusFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetEditStatusFunc onGetEditStatusFunc)
```

**描述**

注册客户端OE对象请求OE文档编辑状态时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongeteditstatusfunc) onGetEditStatusFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnGetEditStatusFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongeteditstatusfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_RegisterOnGetCapabilityFunc()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_RegisterOnGetCapabilityFunc(ContentEmbed_ObjectHandle object, OH_ContentEmbed_Extension_OnGetCapabilityFunc onGetCapabilityFunc)
```

**描述**

注册客户端OE对象查询OE Extension实例支持能力时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetcapabilityfunc) onGetCapabilityFunc | 要注册的[OH\_ContentEmbed\_Extension\_OnGetCapabilityFunc](capi-content-embed-extension-h.md#oh_contentembed_extension_ongetcapabilityfunc)回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_GetContentEmbedDocument()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_GetContentEmbedDocument(ContentEmbed_ObjectHandle object, ContentEmbed_Document **ceDocument)
```

**描述**

获取服务端OE对象关联的OE文档实例。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [ContentEmbed\_Document](capi-contentembed-contentembed-document.md) \*\*ceDocument | 输出参数。调用成功后，该指针指向关联的OE文档实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_CallbackToOnUpdate()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnUpdate(ContentEmbed_ObjectHandle object)
```

**描述**

触发客户端OE对象注册的OE文档更新回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED：表示客户端回调未注册。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_CLIENT\_CALLBACK\_FAILED：表示客户端回调执行失败。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_CallbackToOnError()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnError(ContentEmbed_ObjectHandle object, ContentEmbed_ErrorCode code)
```

**描述**

触发客户端OE对象注册的OE文档错误回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) code | 表示错误码，详细定义参见[ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED：表示客户端回调未注册。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_CLIENT\_CALLBACK\_FAILED：表示客户端回调执行失败。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_CallbackToOnEditingFinished()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnEditingFinished(ContentEmbed_ObjectHandle object, bool dataModified)
```

**描述**

触发客户端OE对象注册的OE文档编辑完成回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| bool dataModified | 表示文档数据是否已被修改。true表示有修改，false表示无修改。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED：表示客户端回调未注册。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_CLIENT\_CALLBACK\_FAILED：表示客户端回调执行失败。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_CallbackToOnExtensionStopped()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_CallbackToOnExtensionStopped(ContentEmbed_ExtensionInstanceHandle instance)
```

**描述**

触发OE Extension关联的所有客户端OE对象注册的OE Extension停止时的回调函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionInstanceHandle](capi-contentembed-contentembed-extensioninstance8h.md) instance | 指向OE Extension实例对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_CLIENT\_CALLBACK\_NOT\_REGISTERED：表示客户端回调未注册。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_CLIENT\_CALLBACK\_FAILED：表示客户端回调执行失败。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_SetSnapshot()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_SetSnapshot(ContentEmbed_ObjectHandle object, OH_PixelmapNative *pixelMap)
```

**描述**

设置客户端OE对象关联的OE文档快照图像。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md) object | [ContentEmbed\_ObjectHandle](capi-contentembed-contentembed-object8h.md)实例。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md) \*pixelMap | 文档快照的像素图对象，详细信息参考[OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。  CE\_ERR\_IMAGE\_PACKER\_OPERATION\_FAILED：表示图像操作失败。 |

### OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbility()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbility(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want)
```

**描述**

通过OE Extension上下文启动自身的[UIAbility](js-apis-app-ability-uiability.md#uiability)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionContextHandle](capi-contentembed-contentembed-extensioncontext8h.md) context | 指向OE Extension上下文对象的指针。 |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动UIAbility时传递的参数，详细信息参考[AbilityBase\_Want](capi-abilitybase-want.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_ContextStartSelfUIAbilityWithStartOptions()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextStartSelfUIAbilityWithStartOptions(ContentEmbed_ExtensionContextHandle context, AbilityBase_Want *want, AbilityRuntime_StartOptions *options)
```

**描述**

使用启动选项启动OE Extension上下文自身的[UIAbility](js-apis-app-ability-uiability.md#uiability)。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionContextHandle](capi-contentembed-contentembed-extensioncontext8h.md) context | 指向OE Extension上下文对象的指针。 |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动UIAbility时传递的参数，详细信息参考[AbilityBase\_Want](capi-abilitybase-want.md)。 |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*options | 启动UIAbility时的附加选项，详细信息参考[AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |

### OH\_ContentEmbed\_Extension\_ContextTerminateAbility()

```c
ContentEmbed_ErrorCode OH_ContentEmbed_Extension_ContextTerminateAbility(ContentEmbed_ExtensionContextHandle context)
```

**描述**

销毁OE Extension。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ContentEmbed\_ExtensionContextHandle](capi-contentembed-contentembed-extensioncontext8h.md) context | 指向OE Extension上下文对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ContentEmbed\_ErrorCode](capi-content-embed-common-h.md#contentembed_errorcode) | 返回特定的错误码：  CE\_ERR\_OK：表示操作成功。  CE\_ERR\_PARAM\_INVALID：表示参数检查失败。  CE\_ERR\_NULL\_POINTER：表示返回空指针。  CE\_ERR\_SYSTEM\_ABNORMAL：表示系统服务异常。  CE\_ERR\_DEVICE\_NOT\_SUPPORTED：表示设备不支持。  CE\_ERR\_IN\_DLP\_SANDBOX：表示应用在DLP沙箱中，不支持此操作。 |
