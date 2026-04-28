---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmedia-source-h
title: avmedia_source.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avmedia_source.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:074b654d7810da61993322ebdda27858595cb04e905f3797efa4317172e8386d
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVMediaSource的结构体和枚举类型。

**引用文件：** <multimedia/player\_framework/avmedia\_source.h>

**库：** libavmedia\_source.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 23

**相关模块：** [avmedia\_source](capi-avmedia-source.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) | OH\_AVHttpHeader | 声明HTTP头部类型。 |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) | OH\_AVMediaSource | 声明媒体源类型。 |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) | OH\_AVMediaSourceLoadingRequest | 加载请求对象。应用通过该对象获取所请求资源的位置。 |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) | OH\_AVMediaSourceLoader | 声明媒体数据加载器类型，由应用实现。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVLoadingRequestError](capi-avmedia-source-h.md#avloadingrequesterror) | AVLoadingRequestError | 网络加载请求的错误码枚举。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVHttpHeader \*OH\_AVHttpHeader\_Create(void)](capi-avmedia-source-h.md#oh_avhttpheader_create) | - | 创建一个HTTP头部实例。 |
| [OH\_AVErrCode OH\_AVHttpHeader\_Destroy(OH\_AVHttpHeader \*header)](capi-avmedia-source-h.md#oh_avhttpheader_destroy) | - | 释放一个HTTP头部实例。 |
| [OH\_AVErrCode OH\_AVHttpHeader\_GetCount(OH\_AVHttpHeader \*header, uint32\_t \*count)](capi-avmedia-source-h.md#oh_avhttpheader_getcount) | - | 获取HTTP头部实例中的记录项数量。 |
| [OH\_AVErrCode OH\_AVHttpHeader\_AddRecord(OH\_AVHttpHeader \*header, const char \*key, const char \*value)](capi-avmedia-source-h.md#oh_avhttpheader_addrecord) | - | 向HTTP头部实例中添加一个键值对记录。 |
| [OH\_AVErrCode OH\_AVHttpHeader\_GetRecord(OH\_AVHttpHeader \*header, uint32\_t index, const char \*\*key, const char \*\*value)](capi-avmedia-source-h.md#oh_avhttpheader_getrecord) | - | 通过索引获取HTTP头部实例中的键值对记录。 |
| [OH\_AVMediaSource \*OH\_AVMediaSource\_CreateWithUrl(const char \*url, OH\_AVHttpHeader \*header)](capi-avmedia-source-h.md#oh_avmediasource_createwithurl) | - | 通过URL创建媒体源。 |
| [OH\_AVMediaSource \*OH\_AVMediaSource\_CreateWithDataSource(OH\_AVDataSource \*dataSource)](capi-avmedia-source-h.md#oh_avmediasource_createwithdatasource) | - | 通过OH\_AVDataSource创建媒体源。 |
| [OH\_AVMediaSource \*OH\_AVMediaSource\_CreateWithFd(int32\_t fd, int64\_t offset, int64\_t size)](capi-avmedia-source-h.md#oh_avmediasource_createwithfd) | - | 通过文件描述符（FileDescriptor）创建媒体源。 |
| [OH\_AVErrCode OH\_AVMediaSource\_Destroy(OH\_AVMediaSource \*source)](capi-avmedia-source-h.md#oh_avmediasource_destroy) | - | 释放media source实例。 |
| [OH\_AVErrCode OH\_AVMediaSource\_SetMimeType(OH\_AVMediaSource \*source, const char \*mimetype)](capi-avmedia-source-h.md#oh_avmediasource_setmimetype) | - | 设置媒体MIME类型以处理扩展媒体源。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoadingRequest\_GetUrl(OH\_AVMediaSourceLoadingRequest \*request, const char \*\*url)](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_geturl) | - | 获取请求的URL。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoadingRequest\_GetHttpHeader(OH\_AVMediaSourceLoadingRequest \*request, OH\_AVHttpHeader \*\*header)](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_gethttpheader) | - | 获取请求的HTTP头部。 |
| [int32\_t OH\_AVMediaSourceLoadingRequest\_RespondData(OH\_AVMediaSourceLoadingRequest \*request, int64\_t uuid, int64\_t offset, const uint8\_t \*data, uint64\_t dataSize)](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_responddata) | - | 用于向AVPlayer发送请求数据的接口。 |
| [void OH\_AVMediaSourceLoadingRequest\_RespondHeader(OH\_AVMediaSourceLoadingRequest \*request, int64\_t uuid, OH\_AVHttpHeader \*header, const char \*redirectUrl)](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_respondheader) | - | 应用用于向AVPlayer发送响应头部的接口，必须在首次调用[OH\_AVMediaSourceLoadingRequest\_RespondData](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_responddata)之前调用。 |
| [void OH\_AVMediaSourceLoadingRequest\_FinishLoading(OH\_AVMediaSourceLoadingRequest \*request, int64\_t uuid, AVLoadingRequestError error)](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_finishloading) | - | 通知播放器当前请求的状态。在推送完单个资源的所有数据后，应用应发送LOADING\_ERROR\_SUCCESS状态，以通知播放器资源推送已完成。 |
| [OH\_AVMediaSourceLoader \*OH\_AVMediaSourceLoader\_Create(void)](capi-avmedia-source-h.md#oh_avmediasourceloader_create) | - | 创建一个OH\_AVMediaSourceLoader实例。成功时返回OH\_AVMediaSourceLoader指针，失败时返回空指针。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoader\_Destroy(OH\_AVMediaSourceLoader \*loader)](capi-avmedia-source-h.md#oh_avmediasourceloader_destroy) | - | 释放OH\_AVMediaSourceLoader实例。 |
| [OH\_AVErrCode OH\_AVMediaSource\_SetMediaSourceLoader(OH\_AVMediaSource \*source, OH\_AVMediaSourceLoader \*loader)](capi-avmedia-source-h.md#oh_avmediasource_setmediasourceloader) | - | 为媒体源实例设置一个源加载器。 |
| [typedef int64\_t (\*OH\_AVMediaSourceLoaderOnSourceOpenedCallback)(OH\_AVMediaSourceLoadingRequest \*request, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourceopenedcallback) | OH\_AVMediaSourceLoaderOnSourceOpenedCallback | 定义由服务端调用的SourceOpenCallback函数。客户端应处理传入的请求，并返回所打开资源的唯一句柄。客户端必须在处理完请求后立即返回该句柄。 |
| [typedef void (\*OH\_AVMediaSourceLoaderOnSourceReadCallback)(int64\_t uuid, int64\_t requestedOffset, int64\_t requestedLength, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourcereadcallback) | OH\_AVMediaSourceLoaderOnSourceReadCallback | 定义由服务端调用的SourceReadCallback函数。客户端应记录读取请求，并在有足够数据时通过请求对象的[OH\_AVMediaSourceLoadingRequest\_RespondData](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_responddata)和[OH\_AVMediaSourceLoadingRequest\_RespondHeader](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_respondheader)方法推送数据。客户端必须在处理完请求后立即返回。 |
| [typedef void (\*OH\_AVMediaSourceLoaderOnSourceClosedCallback)(int64\_t uuid, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourceclosedcallback) | OH\_AVMediaSourceLoaderOnSourceClosedCallback | 定义由服务端调用的SourceCloseCallback函数。客户端应释放相关资源，并在处理完请求后立即返回。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoader\_SetSourceOpenCallback(OH\_AVMediaSourceLoader \*loader, OH\_AVMediaSourceLoaderOnSourceOpenedCallback callback, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloader_setsourceopencallback) | - | 为OH\_AVMediaSourceLoader设置打开回调函数。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoader\_SetSourceReadCallback(OH\_AVMediaSourceLoader \*loader, OH\_AVMediaSourceLoaderOnSourceReadCallback callback, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloader_setsourcereadcallback) | - | 为OH\_AVMediaSourceLoader设置读取回调函数。 |
| [OH\_AVErrCode OH\_AVMediaSourceLoader\_SetSourceCloseCallback(OH\_AVMediaSourceLoader \*loader, OH\_AVMediaSourceLoaderOnSourceClosedCallback callback, void \*userData)](capi-avmedia-source-h.md#oh_avmediasourceloader_setsourceclosecallback) | - | 为OH\_AVMediaSourceLoader设置关闭回调函数。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AVLoadingRequestError

PhonePC/2in1TabletTVWearable

```
1. enum AVLoadingRequestError
```

**描述**

网络加载请求的错误码枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AV\_LOADING\_ERROR\_SUCCESS = 0 | 资源成功下载。 |
| AV\_LOADING\_ERROR\_NOT\_READY = 1 | 资源未准备好，无法访问。 |
| AV\_LOADING\_ERROR\_NO\_RESOURCE = 2 | 资源URL不存在。 |
| AV\_LOADING\_ERROR\_INVALID\_HANDLE = 3 | 资源句柄的UUID无效。 |
| AV\_LOADING\_ERROR\_ACCESS\_DENIED = 4 | 客户端无权请求该资源。 |
| AV\_LOADING\_ERROR\_ACCESS\_TIMEOUT = 5 | 访问超时。 |
| AV\_LOADING\_ERROR\_AUTHORIZE\_FAILED = 6 | 授权失败。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVHttpHeader\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVHttpHeader *OH_AVHttpHeader_Create(void)
```

**描述**

创建一个HTTP头部实例。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVHttpHeader \*](capi-avmedia-source-oh-avhttpheader.md) | 成功时返回指向OH\_AVHttpHeader实例的指针，失败时返回空指针。 |

### OH\_AVHttpHeader\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVHttpHeader_Destroy(OH_AVHttpHeader *header)
```

**描述**

释放一个HTTP头部实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | 指向OH\_AVHttpHeader实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示header为空指针或实例销毁失败。 |

### OH\_AVHttpHeader\_GetCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVHttpHeader_GetCount(OH_AVHttpHeader *header, uint32_t *count)
```

**描述**

获取HTTP头部实例中的记录项数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | 指向OH\_AVHttpHeader实例的指针。 |
| uint32\_t \*count | 用于输出头部实例中记录项的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示header为空指针。 |

### OH\_AVHttpHeader\_AddRecord()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVHttpHeader_AddRecord(OH_AVHttpHeader *header, const char *key, const char *value)
```

**描述**

向HTTP头部实例中添加一个键值对记录。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | 指向OH\_AVHttpHeader实例的指针。 |
| const char \*key | 记录的键名。 |
| const char \*value | 记录的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示任一参数为空指针。 |

### OH\_AVHttpHeader\_GetRecord()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVHttpHeader_GetRecord(OH_AVHttpHeader *header, uint32_t index, const char **key, const char **value)
```

**描述**

通过索引获取HTTP头部实例中的键值对记录。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | 指向OH\_AVHttpHeader实例的指针。 |
| uint32\_t index | 记录在头部中的位置。 |
| const char \*\*key | 用于输出记录的键名。 |
| const char \*\*value | 用于输出记录的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示header为空指针或索引越界。 |

### OH\_AVMediaSource\_CreateWithUrl()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMediaSource *OH_AVMediaSource_CreateWithUrl(const char *url, OH_AVHttpHeader *header)
```

**描述**

通过URL创建媒体源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*url | 媒体源的URL。支持以下流媒体格式：HLS、HTTP-FLV、DASH和HTTPS。 |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | 附加到网络请求的HTTP头部。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVMediaSource \*](capi-avmedia-source-oh-avmediasource.md) | 成功时返回指向OH\_AVMediaSource实例的指针，失败时返回空指针。 |

### OH\_AVMediaSource\_CreateWithDataSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMediaSource *OH_AVMediaSource_CreateWithDataSource(OH_AVDataSource *dataSource)
```

**描述**

通过OH\_AVDataSource创建媒体源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVDataSource \*dataSource | 指向OH\_AVDataSource的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVMediaSource \*](capi-avmedia-source-oh-avmediasource.md) | 成功时返回指向OH\_AVMediaSource实例的指针，失败时返回空指针。 |

### OH\_AVMediaSource\_CreateWithFd()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMediaSource *OH_AVMediaSource_CreateWithFd(int32_t fd, int64_t offset, int64_t size)
```

**描述**

通过文件描述符（FileDescriptor）创建媒体源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t fd | 数据源的文件描述符。 |
| int64\_t offset | 开始读取的文件偏移量。 |
| int64\_t size | 文件大小（以字节为单位）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVMediaSource \*](capi-avmedia-source-oh-avmediasource.md) | 成功时返回指向OH\_AVMediaSource实例的指针，失败时返回空指针。 |

### OH\_AVMediaSource\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSource_Destroy(OH_AVMediaSource *source)
```

**描述**

释放media source实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) \*source | 指向OH\_AVMediaSource实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AVErrCode | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示source为空指针或释放失败。 |

### OH\_AVMediaSource\_SetMimeType()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSource_SetMimeType(OH_AVMediaSource *source, const char *mimetype)
```

**描述**

设置媒体MIME类型以处理扩展媒体源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) \*source | 指向OH\_AVMediaSource的指针。 |
| const char \*mimetype | 媒体源的MIME类型[AV\_MimeTypes](arkts-apis-media-e.md#avmimetypes12)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示source或mimetype为空指针。  AV\_ERR\_UNSUPPORTED\_FORMAT：表示不支持该mimetype。 |

### OH\_AVMediaSourceLoadingRequest\_GetUrl()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoadingRequest_GetUrl(OH_AVMediaSourceLoadingRequest *request, const char **url)
```

**描述**

获取请求的URL。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) \*request | OH\_AVMediaSourceLoadingRequest实例。 |
| const char \*\*url | 用于输出的URL字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示request为空指针或不存在URL。 |

### OH\_AVMediaSourceLoadingRequest\_GetHttpHeader()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoadingRequest_GetHttpHeader(OH_AVMediaSourceLoadingRequest *request, OH_AVHttpHeader **header)
```

**描述**

获取请求的HTTP头部。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) \*request | OH\_AVMediaSourceLoadingRequest实例。 |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*\*header | 用于HTTP请求的HTTP头部。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示request为空指针。 |

### OH\_AVMediaSourceLoadingRequest\_RespondData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_AVMediaSourceLoadingRequest_RespondData(OH_AVMediaSourceLoadingRequest *request, int64_t uuid, int64_t offset, const uint8_t *data, uint64_t dataSize)
```

**描述**

用于向AVPlayer发送请求数据的接口。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) \*request | 资源打开请求的参数。 |
| int64\_t uuid | 资源句柄的ID。 |
| int64\_t offset | 当前媒体数据相对于资源起始位置的偏移量。 |
| const uint8\_t \*data | 发送给播放器的媒体数据。 |
| uint64\_t dataSize | 发送给播放器的数据长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 当前读取操作接受的字节数。返回值小于零表示失败；  -2 表示播放器不再需要当前数据，客户端应停止当前读取过程；  -3 表示播放器缓冲区已满，客户端应等待下一次读取。 |

### OH\_AVMediaSourceLoadingRequest\_RespondHeader()

PhonePC/2in1TabletTVWearable

```
1. void OH_AVMediaSourceLoadingRequest_RespondHeader(OH_AVMediaSourceLoadingRequest *request, int64_t uuid, OH_AVHttpHeader *header, const char *redirectUrl)
```

**描述**

应用用于向AVPlayer发送响应头部的接口，必须在首次调用[OH\_AVMediaSourceLoadingRequest\_RespondData](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_responddata)之前调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) \*request | 资源打开请求的参数。 |
| int64\_t uuid | 资源句柄的ID。 |
| [OH\_AVHttpHeader](capi-avmedia-source-oh-avhttpheader.md) \*header | HTTP响应中的头部信息。  应用可将该头部字段与底层支持的字段进行交集处理后再传入，也可直接传入所有对应的头部信息。 |
| const char \*redirectUrl | HTTP响应中包含的重定向URL（如果存在）。 |

### OH\_AVMediaSourceLoadingRequest\_FinishLoading()

PhonePC/2in1TabletTVWearable

```
1. void OH_AVMediaSourceLoadingRequest_FinishLoading(OH_AVMediaSourceLoadingRequest *request, int64_t uuid, AVLoadingRequestError error)
```

**描述**

通知播放器当前请求的状态。在推送完单个资源的所有数据后，应用应发送LOADING\_ERROR\_SUCCESS状态，以通知播放器资源推送已完成。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoadingRequest](capi-avmedia-source-oh-avmediasourceloadingrequest.md) \*request | 资源打开请求的参数。 |
| int64\_t uuid | 资源句柄的ID。 |
| [AVLoadingRequestError](capi-avmedia-source-h.md#avloadingrequesterror) error | 错误状态。 |

### OH\_AVMediaSourceLoader\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMediaSourceLoader *OH_AVMediaSourceLoader_Create(void)
```

**描述**

创建一个OH\_AVMediaSourceLoader实例。成功时返回OH\_AVMediaSourceLoader指针，失败时返回空指针。

**起始版本：** 23

### OH\_AVMediaSourceLoader\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoader_Destroy(OH_AVMediaSourceLoader *loader)
```

**描述**

释放OH\_AVMediaSourceLoader实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) \*loader | 待释放的OH\_AVMediaSourceLoader实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示loader为空指针或释放失败。 |

### OH\_AVMediaSource\_SetMediaSourceLoader()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSource_SetMediaSourceLoader(OH_AVMediaSource *source, OH_AVMediaSourceLoader *loader)
```

**描述**

为媒体源实例设置一个源加载器。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) \*source | 需要网络代理的OH\_AVMediaSource。 |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) \*loader | OH\_AVMediaSourceLoader实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示source或loader为空指针，或操作失败。 |

### OH\_AVMediaSourceLoaderOnSourceOpenedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef int64_t (*OH_AVMediaSourceLoaderOnSourceOpenedCallback)(OH_AVMediaSourceLoadingRequest *request, void *userData)
```

**描述**

定义由服务端调用的SourceOpenCallback函数。客户端应处理传入的请求，并返回所打开资源的唯一句柄。客户端必须在处理完请求后立即返回该句柄。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVMediaSourceLoadingRequest \*request | 资源打开请求的参数，包含所请求资源的详细信息及数据推送方式。 |
| void \*userData | 用户在OH\_AVMediaSourceLoader\_SetSourceOpenCallback中设置的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 当前资源打开请求的句柄，该句柄对请求对象是唯一的。  大于0的值表示请求成功；  小于或等于0的值表示失败。 |

### OH\_AVMediaSourceLoaderOnSourceReadCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVMediaSourceLoaderOnSourceReadCallback)(int64_t uuid, int64_t requestedOffset, int64_t requestedLength, void *userData)
```

**描述**

定义由服务端调用的SourceReadCallback函数。客户端应记录读取请求，并在有足够数据时通过请求对象的[OH\_AVMediaSourceLoadingRequest\_RespondData](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_responddata)和[OH\_AVMediaSourceLoadingRequest\_RespondHeader](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_respondheader)方法推送数据。客户端必须在处理完请求后立即返回。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t uuid | 资源句柄的ID。 |
| int64\_t requestedOffset | 当前媒体数据相对于资源起始位置的偏移量。 |
| int64\_t requestedLength | 当前请求的数据长度。-1 表示已到达资源末尾，需通过[OH\_AVMediaSourceLoadingRequest\_FinishLoading](capi-avmedia-source-h.md#oh_avmediasourceloadingrequest_finishloading)方法通知播放器推送结束。 |
| void \*userData | 用户在OH\_AVMediaSourceLoader\_SetSourceReadCallback中设置的数据。 |

### OH\_AVMediaSourceLoaderOnSourceClosedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVMediaSourceLoaderOnSourceClosedCallback)(int64_t uuid, void *userData)
```

**描述**

定义由服务端调用的SourceCloseCallback函数。客户端应释放相关资源，并在处理完请求后立即返回。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t uuid | 资源句柄的ID。 |
| void \*userData | 用户在OH\_AVMediaSourceLoader\_SetSourceCloseCallback中设置的数据。 |

### OH\_AVMediaSourceLoader\_SetSourceOpenCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoader_SetSourceOpenCallback(OH_AVMediaSourceLoader *loader, OH_AVMediaSourceLoaderOnSourceOpenedCallback callback, void *userData)
```

**描述**

为OH\_AVMediaSourceLoader设置打开回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) \*loader | 要设置回调函数的OH\_AVMediaSourceLoader实例。 |
| [OH\_AVMediaSourceLoaderOnSourceOpenedCallback](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourceopenedcallback) callback | 要设置的打开回调函数。 |
| void \*userData | 回调函数中使用的用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示loader为空指针或操作失败。 |

### OH\_AVMediaSourceLoader\_SetSourceReadCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoader_SetSourceReadCallback(OH_AVMediaSourceLoader *loader, OH_AVMediaSourceLoaderOnSourceReadCallback callback, void *userData)
```

**描述**

为OH\_AVMediaSourceLoader设置读取回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) \*loader | 要设置回调函数的OH\_AVMediaSourceLoader实例。 |
| [OH\_AVMediaSourceLoaderOnSourceReadCallback](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourcereadcallback) callback | 要设置的读取回调函数。 |
| void \*userData | 回调函数中使用的用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示loader为空指针或操作失败。 |

### OH\_AVMediaSourceLoader\_SetSourceCloseCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMediaSourceLoader_SetSourceCloseCallback(OH_AVMediaSourceLoader *loader, OH_AVMediaSourceLoaderOnSourceClosedCallback callback, void *userData)
```

**描述**

为OH\_AVMediaSourceLoader设置关闭回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMediaSourceLoader](capi-avmedia-source-oh-avmediasourceloader.md) \*loader | 要设置回调函数的OH\_AVMediaSourceLoader实例。 |
| [OH\_AVMediaSourceLoaderOnSourceClosedCallback](capi-avmedia-source-h.md#oh_avmediasourceloaderonsourceclosedcallback) callback | 要设置的关闭回调函数。 |
| void \*userData | 回调函数中使用的用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示loader为空指针或操作失败。 |
