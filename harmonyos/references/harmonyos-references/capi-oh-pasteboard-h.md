---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-h
title: oh_pasteboard.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > oh_pasteboard.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:794665534a19ca7b2e94aa0fa42506eb4f8ddf61360e70e20b4ce47636fa6150
---

## 概述

PhonePC/2in1TabletTVWearable

提供访问系统剪贴板的接口、数据结构、枚举类型。

**引用文件：** <database/pasteboard/oh\_pasteboard.h>

**库：** libpasteboard.so

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 13

**相关模块：** [Pasteboard](capi-pasteboard.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md) | Pasteboard\_ProgressInfo | 定义进度上报的数据结构。 |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md) | Pasteboard\_GetDataParams | 表示从剪贴板获取粘贴数据和进度时需要写入的参数。 |
| [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md) | OH\_PasteboardObserver | 定义剪贴板数据变更观察者。 |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md) | OH\_Pasteboard | 定义剪贴板对象，用以操作系统剪贴板。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN](capi-oh-pasteboard-h.md#pasteboard_mimetype_text_plain) "text/plain" | 纯文本类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_URI](capi-oh-pasteboard-h.md#pasteboard_mimetype_text_uri) "text/uri" | URI类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_HTML](capi-oh-pasteboard-h.md#pasteboard_mimetype_text_html) "text/html" | HTML类型。 |
| [PASTEBOARD\_MIMETYPE\_PIXELMAP](capi-oh-pasteboard-h.md#pasteboard_mimetype_pixelmap) "pixelMap" | pixelMap类型。 |
| [PASTEBOARD\_MIMETYPE\_TEXT\_WANT](capi-oh-pasteboard-h.md#pasteboard_mimetype_text_want) "text/want" | want类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Pasteboard\_NotifyType](capi-oh-pasteboard-h.md#pasteboard_notifytype) | Pasteboard\_NotifyType | 剪贴板的数据变更类型。 |
| [Pasteboard\_FileConflictOptions](capi-oh-pasteboard-h.md#pasteboard_fileconflictoptions) | Pasteboard\_FileConflictOptions | 定义文件拷贝冲突时的选项。 |
| [Pasteboard\_ProgressIndicator](capi-oh-pasteboard-h.md#pasteboard_progressindicator) | Pasteboard\_ProgressIndicator | 定义进度条指示选项，可选择是否采用系统默认进度显示。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_Pasteboard\_ProgressListener)(Pasteboard\_ProgressInfo\* progressInfo)](capi-oh-pasteboard-h.md#oh_pasteboard_progresslistener) | OH\_Pasteboard\_ProgressListener | 用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。 |
| [typedef void (\*Pasteboard\_Notify)(void\* context, Pasteboard\_NotifyType type)](capi-oh-pasteboard-h.md#pasteboard_notify) | Pasteboard\_Notify | 定义剪贴板内容变更时触发的回调函数。 |
| [typedef void (\*Pasteboard\_Finalize)(void\* context)](capi-oh-pasteboard-h.md#pasteboard_finalize) | Pasteboard\_Finalize | 定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。 |
| [OH\_PasteboardObserver\* OH\_PasteboardObserver\_Create()](capi-oh-pasteboard-h.md#oh_pasteboardobserver_create) | - | 创建一个剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)指针及实例对象。 |
| [int OH\_PasteboardObserver\_Destroy(OH\_PasteboardObserver\* observer)](capi-oh-pasteboard-h.md#oh_pasteboardobserver_destroy) | - | 销毁剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)指针指向的实例对象。 |
| [int OH\_PasteboardObserver\_SetData(OH\_PasteboardObserver\* observer, void\* context,const Pasteboard\_Notify callback, const Pasteboard\_Finalize finalize)](capi-oh-pasteboard-h.md#oh_pasteboardobserver_setdata) | - | 向剪贴板数据变更观察者设置回调函数。 |
| [OH\_Pasteboard\* OH\_Pasteboard\_Create()](capi-oh-pasteboard-h.md#oh_pasteboard_create) | - | 创建剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)指针及实例对象。 |
| [void OH\_Pasteboard\_Destroy(OH\_Pasteboard\* pasteboard)](capi-oh-pasteboard-h.md#oh_pasteboard_destroy) | - | 销毁剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例对象。 |
| [int OH\_Pasteboard\_Subscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](capi-oh-pasteboard-h.md#oh_pasteboard_subscribe) | - | 订阅剪贴板的数据变更事件。 |
| [int OH\_Pasteboard\_Unsubscribe(OH\_Pasteboard\* pasteboard, int type, const OH\_PasteboardObserver\* observer)](capi-oh-pasteboard-h.md#oh_pasteboard_unsubscribe) | - | 取消对剪贴板数据变更事件的订阅。 |
| [bool OH\_Pasteboard\_IsRemoteData(OH\_Pasteboard\* pasteboard)](capi-oh-pasteboard-h.md#oh_pasteboard_isremotedata) | - | 判断剪贴板中的数据是否来自远端设备。 |
| [int OH\_Pasteboard\_GetDataSource(OH\_Pasteboard\* pasteboard, char\* source, unsigned int len)](capi-oh-pasteboard-h.md#oh_pasteboard_getdatasource) | - | 获取剪贴板中数据的数据源。 |
| [bool OH\_Pasteboard\_HasType(OH\_Pasteboard\* pasteboard, const char\* type)](capi-oh-pasteboard-h.md#oh_pasteboard_hastype) | - | 判断剪贴板中是否有指定类型的数据。 |
| [bool OH\_Pasteboard\_HasData(OH\_Pasteboard\* pasteboard)](capi-oh-pasteboard-h.md#oh_pasteboard_hasdata) | - | 判断剪贴板中是否有数据。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetData(OH\_Pasteboard\* pasteboard, int\* status)](capi-oh-pasteboard-h.md#oh_pasteboard_getdata) | - | 获取剪贴板中的数据。 |
| [int OH\_Pasteboard\_SetData(OH\_Pasteboard\* pasteboard, OH\_UdmfData\* data)](capi-oh-pasteboard-h.md#oh_pasteboard_setdata) | - | 将统一数据对象数据写入剪贴板。 |
| [int OH\_Pasteboard\_ClearData(OH\_Pasteboard\* pasteboard)](capi-oh-pasteboard-h.md#oh_pasteboard_cleardata) | - | 清空剪贴板中的数据。 |
| [char \*\*OH\_Pasteboard\_GetMimeTypes(OH\_Pasteboard \*pasteboard, unsigned int \*count)](capi-oh-pasteboard-h.md#oh_pasteboard_getmimetypes) | - | 获取剪贴板中的MIME类型。 |
| [Pasteboard\_GetDataParams \*OH\_Pasteboard\_GetDataParams\_Create(void)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_create) | - | 创建剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)指针及实例对象。 |
| [void OH\_Pasteboard\_GetDataParams\_Destroy(Pasteboard\_GetDataParams\* params)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_destroy) | - | 销毁剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)指针指向的实例对象。 |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressIndicator(Pasteboard\_GetDataParams\* params,Pasteboard\_ProgressIndicator progressIndicator)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_setprogressindicator) | - | 向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置进度条指示选项，可选择是否采用系统默认进度显示。 |
| [void OH\_Pasteboard\_GetDataParams\_SetDestUri(Pasteboard\_GetDataParams\* params, const char\* destUri, uint32\_t destUriLen)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_setdesturi) | - | 向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。 |
| [void OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions(Pasteboard\_GetDataParams\* params,Pasteboard\_FileConflictOptions option)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_setfileconflictoptions) | - | 向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置文件冲突选项。 |
| [void OH\_Pasteboard\_GetDataParams\_SetProgressListener(Pasteboard\_GetDataParams\* params,const OH\_Pasteboard\_ProgressListener listener)](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_setprogresslistener) | - | 向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置进度上报回调函数。 |
| [int OH\_Pasteboard\_ProgressInfo\_GetProgress(Pasteboard\_ProgressInfo\* progressInfo)](capi-oh-pasteboard-h.md#oh_pasteboard_progressinfo_getprogress) | - | 从[Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md)获取粘贴进度。 |
| [void OH\_Pasteboard\_ProgressCancel(Pasteboard\_GetDataParams\* params)](capi-oh-pasteboard-h.md#oh_pasteboard_progresscancel) | - | 定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。 |
| [OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params,int\* status)](capi-oh-pasteboard-h.md#oh_pasteboard_getdatawithprogress) | - | 获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。 |
| [uint32\_t OH\_Pasteboard\_GetChangeCount(OH\_Pasteboard \*pasteboard)](capi-oh-pasteboard-h.md#oh_pasteboard_getchangecount) | - | 获取剪贴板内容的变化次数。 |
| [void OH\_Pasteboard\_SyncDelayedDataAsync(OH\_Pasteboard\* pasteboard, void (\*callback)(int errorCode))](capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync) | - | 通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH\_UdmfRecordProvider\_SetData](capi-udmf-h.md#oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](capi-oh-pasteboard-h.md#oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。 |

## 宏定义说明

PhonePC/2in1TabletTVWearable

### PASTEBOARD\_MIMETYPE\_TEXT\_PLAIN

PhonePC/2in1TabletTVWearable

```
1. #define PASTEBOARD_MIMETYPE_TEXT_PLAIN "text/plain"
```

**描述**

纯文本类型。

**起始版本：** 22

### PASTEBOARD\_MIMETYPE\_TEXT\_URI

PhonePC/2in1TabletTVWearable

```
1. #define PASTEBOARD_MIMETYPE_TEXT_URI "text/uri"
```

**描述**

URI类型。

**起始版本：** 22

### PASTEBOARD\_MIMETYPE\_TEXT\_HTML

PhonePC/2in1TabletTVWearable

```
1. #define PASTEBOARD_MIMETYPE_TEXT_HTML "text/html"
```

**描述**

HTML类型。

**起始版本：** 22

### PASTEBOARD\_MIMETYPE\_PIXELMAP

PhonePC/2in1TabletTVWearable

```
1. #define PASTEBOARD_MIMETYPE_PIXELMAP "pixelMap"
```

**描述**

pixelMap类型。

**起始版本：** 22

### PASTEBOARD\_MIMETYPE\_TEXT\_WANT

PhonePC/2in1TabletTVWearable

```
1. #define PASTEBOARD_MIMETYPE_TEXT_WANT "text/want"
```

**描述**

want类型。

**起始版本：** 22

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Pasteboard\_NotifyType

PhonePC/2in1TabletTVWearable

```
1. enum Pasteboard_NotifyType
```

**描述：**

剪贴板的数据变更类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| NOTIFY\_LOCAL\_DATA\_CHANGE = 1 | 本地设备剪贴板数据变更。 |
| NOTIFY\_REMOTE\_DATA\_CHANGE = 2 | 组网内的非本地设备剪贴板数据变更。 |

### Pasteboard\_FileConflictOptions

PhonePC/2in1TabletTVWearable

```
1. enum Pasteboard_FileConflictOptions
```

**描述：**

定义文件拷贝冲突时的选项。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| PASTEBOARD\_OVERWRITE = 0 | 目标路径存在同文件名时覆盖。 |
| PASTEBOARD\_SKIP = 1 | 目标路径存在同文件名时跳过。 |

### Pasteboard\_ProgressIndicator

PhonePC/2in1TabletTVWearable

```
1. enum Pasteboard_ProgressIndicator
```

**描述：**

定义进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| PASTEBOARD\_NONE = 0 | 不采用系统默认进度显示。 |
| PASTEBOARD\_DEFAULT = 1 | 采用系统默认进度显示。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Pasteboard\_ProgressListener()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_Pasteboard_ProgressListener)(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

用于在不使用系统默认进度显示时，通知应用拷贝粘贴任务进度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md)\* progressInfo | 定义进度上报的数据结构，且仅当进度指示选项[Pasteboard\_ProgressIndicator](capi-oh-pasteboard-h.md#pasteboard_progressindicator)设置为PASTEBOARD\_NONE时才会上报此信息。 |

### Pasteboard\_Notify()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Pasteboard_Notify)(void* context, Pasteboard_NotifyType type)
```

**描述：**

定义剪贴板内容变更时触发的回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 上下文信息，由函数[OH\_PasteboardObserver\_SetData](capi-oh-pasteboard-h.md#oh_pasteboardobserver_setdata)传入。 |
| [Pasteboard\_NotifyType](capi-oh-pasteboard-h.md#pasteboard_notifytype) type | 数据变更的类型。详见：[Pasteboard\_NotifyType](capi-oh-pasteboard-h.md#pasteboard_notifytype)。 |

### Pasteboard\_Finalize()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Pasteboard_Finalize)(void* context)
```

**描述：**

定义用于释放上下文的回调函数，剪贴板数据变更观察者对象销毁时触发。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* context | 要释放的上下文指针。 |

### OH\_PasteboardObserver\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_PasteboardObserver* OH_PasteboardObserver_Create()
```

**描述：**

创建一个剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)指针及实例对象。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)\* | 执行成功时返回一个指向剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)实例对象的指针，否则返回空指针。  当不再需要使用指针时，请使用[OH\_PasteboardObserver\_Destroy](capi-oh-pasteboard-h.md#oh_pasteboardobserver_destroy)销毁实例对象，否则会导致内存泄漏。 |

### OH\_PasteboardObserver\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. int OH_PasteboardObserver_Destroy(OH_PasteboardObserver* observer)
```

**描述：**

销毁剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)指针指向的实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_PasteboardObserver\_SetData()

PhonePC/2in1TabletTVWearable

```
1. int OH_PasteboardObserver_SetData(OH_PasteboardObserver* observer, void* context,const Pasteboard_Notify callback, const Pasteboard_Finalize finalize)
```

**描述：**

向剪贴板数据变更观察者设置回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)实例的指针。 |
| void\* context | 表示指向上下文数据的指针，将作为第一个参数传入[Pasteboard\_Notify](capi-oh-pasteboard-h.md#pasteboard_notify)。 |
| const [Pasteboard\_Notify](capi-oh-pasteboard-h.md#pasteboard_notify) callback | 表示数据变更回调函数。详见：[Pasteboard\_Notify](capi-oh-pasteboard-h.md#pasteboard_notify)。 |
| const [Pasteboard\_Finalize](capi-oh-pasteboard-h.md#pasteboard_finalize) finalize | 表示可选的回调函数，可以用于剪贴板数据变更观察者销毁时释放上下文数据。详见：[Pasteboard\_Finalize](capi-oh-pasteboard-h.md#pasteboard_finalize)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_Pasteboard* OH_Pasteboard_Create()
```

**描述：**

创建剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)指针及实例对象。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* | 执行成功则返回一个指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例对象的指针，否则返回nullptr。  当不再需要使用指针时，请使用[OH\_Pasteboard\_Destroy](capi-oh-pasteboard-h.md#oh_pasteboard_destroy)销毁实例对象，否则会导致内存泄漏。 |

### OH\_Pasteboard\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_Destroy(OH_Pasteboard* pasteboard)
```

**描述：**

销毁剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |

### OH\_Pasteboard\_Subscribe()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_Subscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

订阅剪贴板的数据变更事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| int type | 表示订阅的剪贴板数据变更类型，详见：[Pasteboard\_NotifyType](capi-oh-pasteboard-h.md#pasteboard_notifytype)。 |
| const [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_Unsubscribe()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_Unsubscribe(OH_Pasteboard* pasteboard, int type, const OH_PasteboardObserver* observer)
```

**描述：**

取消对剪贴板数据变更事件的订阅。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| int type | 表示订阅的剪贴板数据变更类型，详见：[Pasteboard\_NotifyType](capi-oh-pasteboard-h.md#pasteboard_notifytype)。 |
| const [OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)\* observer | 表示指向剪贴板数据变更观察者[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)实例的指针。它指定了剪贴板数据变更时触发的回调函数，详见：[OH\_PasteboardObserver](capi-pasteboard-oh-pasteboardobserver.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_IsRemoteData()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Pasteboard_IsRemoteData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中的数据是否来自远端设备。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回剪贴板中的数据是否来自远端设备。返回true表示剪贴板中的数据来自远端设备，返回false表示剪贴板中数据来自本端设备。 |

### OH\_Pasteboard\_GetDataSource()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_GetDataSource(OH_Pasteboard* pasteboard, char* source, unsigned int len)
```

**描述：**

获取剪贴板中数据的数据源。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| char\* source | 表示用于存放剪贴板数据源实例的指针，开发者需在调用接口前申请指针指向的内存。 |
| unsigned int len | 表示source指针对应的内存长度，当内存长度不足时调用接口会失败，建议长度：128字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_HasType()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Pasteboard_HasType(OH_Pasteboard* pasteboard, const char* type)
```

**描述：**

判断剪贴板中是否有指定类型的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| const char\* type | 表示要检查的数据类型。包含剪贴板基础数据类型与自定义数据类型，其中剪贴板基础数据类型有："text/plain"、"text/html"、"text/uri"、"text/want"和"pixelMap"，详见[宏定义](capi-oh-pasteboard-h.md#宏定义)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回剪贴板中是否有指定类型的数据。返回true表示剪贴板中包含指定类型的数据，返回false表示剪贴板中没有指定类型的数据。 |

### OH\_Pasteboard\_HasData()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Pasteboard_HasData(OH_Pasteboard* pasteboard)
```

**描述：**

判断剪贴板中是否有数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回剪贴板中是否有数据。返回true表示剪贴板中有数据，返回false表示剪贴板中没有数据。 |

### OH\_Pasteboard\_GetData()

PhonePC/2in1TabletTVWearable

```
1. OH_UdmfData* OH_Pasteboard_GetData(OH_Pasteboard* pasteboard, int* status)
```

**描述：**

获取剪贴板中的数据。

**起始版本：** 13

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| int\* status | 该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md)\* | 执行成功时返回统一数据对象[OH\_UdmfData](capi-udmf-oh-udmfdata.md)实例的指针。否则返回空指针。 |

### OH\_Pasteboard\_SetData()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_SetData(OH_Pasteboard* pasteboard, OH_UdmfData* data)
```

**描述：**

将统一数据对象数据写入剪贴板。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md)\* data | 表示指向统一数据对象[OH\_UdmfData](capi-udmf-oh-udmfdata.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_ClearData()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_ClearData(OH_Pasteboard* pasteboard)
```

**描述：**

清空剪贴板中的数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。  若返回ERR\_OK，表示执行成功。  若返回ERR\_INVALID\_PARAMETER，表示传入了无效参数。 |

### OH\_Pasteboard\_GetMimeTypes()

PhonePC/2in1TabletTVWearable

```
1. char **OH_Pasteboard_GetMimeTypes(OH_Pasteboard *pasteboard, unsigned int *count)
```

**描述：**

获取剪贴板中的MIME类型。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| unsigned int \*count | 该参数是输出参数，结果集中的类型数量会写入该变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char \*\* | 执行成功时返回剪贴板所有内容的MIME类型，否则返回nullptr。 |

### OH\_Pasteboard\_GetDataParams\_Create()

PhonePC/2in1TabletTVWearable

```
1. Pasteboard_GetDataParams *OH_Pasteboard_GetDataParams_Create(void)
```

**描述：**

创建剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)指针及实例对象。

**起始版本：** 15

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* | 执行成功时返回一个指向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)实例对象的指针，否则返回空指针。  当不再需要使用指针时，请使用[OH\_Pasteboard\_GetDataParams\_Destroy](capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_destroy)销毁实例对象，否则会导致内存泄漏。 |

### OH\_Pasteboard\_GetDataParams\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_GetDataParams_Destroy(Pasteboard_GetDataParams* params)
```

**描述：**

销毁剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)指针指向的实例对象。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md) \* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |

### OH\_Pasteboard\_GetDataParams\_SetProgressIndicator()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_GetDataParams_SetProgressIndicator(Pasteboard_GetDataParams* params,Pasteboard_ProgressIndicator progressIndicator)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置进度条指示选项，可选择是否采用系统默认进度显示。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| [Pasteboard\_ProgressIndicator](capi-oh-pasteboard-h.md#pasteboard_progressindicator) progressIndicator | 定义进度条指示选项。 |

### OH\_Pasteboard\_GetDataParams\_SetDestUri()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_GetDataParams_SetDestUri(Pasteboard_GetDataParams* params, const char* destUri, uint32_t destUriLen)
```

**描述：**

设置拷贝文件时目标路径。若不支持文件处理，则不需要设置此参数；若应用涉及复杂文件处理策略或需要区分文件多路径存储，建议不设置此参数，由应用自行完成文件copy处理。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| const char\* destUri | 定义拷贝文件目标路径。 |
| uint32\_t destUriLen | 定义拷贝文件目标路径长度。 |

### OH\_Pasteboard\_GetDataParams\_SetFileConflictOptions()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_GetDataParams_SetFileConflictOptions(Pasteboard_GetDataParams* params,Pasteboard_FileConflictOptions option)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置文件冲突选项。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| [Pasteboard\_FileConflictOptions](capi-oh-pasteboard-h.md#pasteboard_fileconflictoptions) option | 定义文件拷贝冲突时的选项，默认为PASTEBOARD\_OVERWRITE。 |

### OH\_Pasteboard\_GetDataParams\_SetProgressListener()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_GetDataParams_SetProgressListener(Pasteboard_GetDataParams* params,const OH_Pasteboard_ProgressListener listener)
```

**描述：**

向剪贴板[Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)设置进度上报回调函数。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| const [OH\_Pasteboard\_ProgressListener](capi-oh-pasteboard-h.md#oh_pasteboard_progresslistener) listener | 表示进度上报回调函数。 |

### OH\_Pasteboard\_ProgressInfo\_GetProgress()

PhonePC/2in1TabletTVWearable

```
1. int OH_Pasteboard_ProgressInfo_GetProgress(Pasteboard_ProgressInfo* progressInfo)
```

**描述：**

从[Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md)获取粘贴进度。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md)\* progressInfo | 表示指向剪贴板[Pasteboard\_ProgressInfo](capi-pasteboard-progressinfo.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回粘贴进度百分比。 |

### OH\_Pasteboard\_ProgressCancel()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_ProgressCancel(Pasteboard_GetDataParams* params)
```

**描述：**

定义取消函数，用于在获取粘贴数据时取消正在进行的粘贴动作。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |

### OH\_Pasteboard\_GetDataWithProgress()

PhonePC/2in1TabletTVWearable

```
1. OH_UdmfData* OH_Pasteboard_GetDataWithProgress(OH_Pasteboard* pasteboard, Pasteboard_GetDataParams* params,int* status)
```

**描述：**

获取剪贴板的数据以及粘贴进度，不支持对文件夹的拷贝。

**起始版本：** 15

**需要权限**：ohos.permission.READ\_PASTEBOARD，应用访问剪贴板内容需[申请访问剪贴板权限](../harmonyos-guides/get-pastedata-permission-guidelines.md)。[使用粘贴控件](../harmonyos-guides/pastebutton.md)访问剪贴板内容的应用，可以无需申请权限。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)\* pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| [Pasteboard\_GetDataParams](capi-pasteboard-getdataparams.md)\* params | 表示指向剪贴板OH\_Pasteboard\_GetDataParams的指针。 |
| int\* status | 该参数是输出参数，表示执行的错误码。错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_UdmfData](capi-udmf-oh-udmfdata.md)\* | 执行成功时返回统一数据对象OH\_UdmfData实例的指针。否则返回空指针。 |

### OH\_Pasteboard\_GetChangeCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Pasteboard_GetChangeCount(OH_Pasteboard *pasteboard)
```

**描述：**

获取剪贴板内容的变化次数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 执行成功时返回剪贴板内容的变化次数，否则返回0。  当剪贴板内容过期或调用OH\_Pasteboard\_ClearData等接口导致剪贴板内容为空时，内容变化次数不会因此改变。  系统重启或剪贴板服务异常重启时，剪贴板内容变化次数重新从0开始计数。对同一内容连续多次复制会被视作多次更改，每次复制均会导致内容变化次数增加。 |

### OH\_Pasteboard\_SyncDelayedDataAsync()

PhonePC/2in1TabletTVWearable

```
1. void OH_Pasteboard_SyncDelayedDataAsync(OH_Pasteboard* pasteboard, void (*callback)(int errorCode))
```

**描述：**

通知剪贴板从应用同步所有延迟数据，与延迟复制接口[OH\_UdmfRecordProvider\_SetData](capi-udmf-h.md#oh_udmfrecordprovider_setdata)搭配使用。当应用使用延迟复制功能复制时，仅将应用支持的数据类型写入剪贴板。应用应在退出时，重新调用[OH\_Pasteboard\_SetData](capi-oh-pasteboard-h.md#oh_pasteboard_setdata)接口主动提交所有复制数据或调用此接口通知剪贴板获取全量数据，等待数据同步完成再继续退出，否则可能导致其他应用粘贴获取不到数据。

注意

* 调用此接口会延长退出过程，建议应用直接设置数据到剪贴板，而不是调用延迟复制接口[OH\_UdmfRecordProvider\_SetData](capi-udmf-h.md#oh_udmfrecordprovider_setdata)和此接口。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md) \*pasteboard | 表示指向剪贴板[OH\_Pasteboard](capi-pasteboard-oh-pasteboard.md)实例的指针。 |
| void (\*callback)(int errorCode) | 数据同步完成后调用的回调函数指针，errorCode表示同步任务的结果，错误码定义详见[PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode)。 |
