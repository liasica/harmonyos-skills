---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview
title: Preview
breadcrumb: API参考 > 应用服务 > Preview Kit（文件预览服务） > C API > 模块 > Preview
category: harmonyos-references
scraped_at: 2026-04-28T08:18:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9671b9f731e7e8db4c34bffae1c4a19953c25027ff25dfede4b5749b1f866899
---

## 概述

PC/2in1

Preview Kit（文件预览服务）为应用提供便捷的文件快速预览服务。应用可以通过Preview Kit提供的预览API，快速启动预览界面，实现对各类文件的预览。

其中C API接口主要提供了文件打开加速功能和通用文件缓存加速功能。

* 文件打开加速功能支持应用通过预加载机制提前加载文件，缩短用户打开文件时间，给用户提供流畅顺滑的爽感体验。
* 通用文件缓存加速功能支持应用通过缓存服务，将解码后的数据缓存到磁盘中，后续可直接获取缓存数据，省去解码过程，提升文件打开和浏览的性能。

详见[文件打开加速开发指南](../harmonyos-guides/preview-openfileboost.md)和[通用文件缓存加速开发指南](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 5.0.3(15)

## 汇总

PC/2in1

### 文件

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [open\_file\_boost.h](openfileboost-open__file__boost_8h.md) | 声明文件打开加速的API集合。 |
| [file\_cache\_boost.h](openfileboost-file__cache__boost_8h.md) | 声明用于通用文件缓存加速的API，以优化文件打开和文件浏览等场景中的性能。 |
| [preview\_kit.h](openfileboost-preview__kit_8h.md) | 声明Preview Kit所包含的所有头文件。 |

### 宏定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [MAX\_BUFFER\_LENGTH](openfileboost_preview.md#max_buffer_length) 1024 | 沙箱路径最大长度1024。 |

### 类型定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| typedef  [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate)(\* [HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate)) (void) | 该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先调用，用于向app查询当前是否允许推荐文件给app。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。 |
| typedef [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode)(\* [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)) (void \*fileInfo) | 系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。 |
| typedef struct [CacheKey](openfileboost_preview.md#cachekey) [CacheKey](openfileboost_preview.md#cachekey) | 开发者传入的key相关数据结构的对外声明，开发者只需在序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)和反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)调用 [WriteFunc](openfileboost_preview.md#writefunc) 和[ReadFunc](openfileboost_preview.md#readfunc)时传入即可。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [ReadFunc](openfileboost_preview.md#readfunc)) (void \*buffer, size\_t \*bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [DeserializeFunc](openfileboost_preview.md#deserializefunc)进行反序列化的过程中调用此函数，可从缓存读取数据到缓冲区。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [WriteFunc](openfileboost_preview.md#writefunc)) (const void \*buffer, size\_t bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [SerializeFunc](openfileboost_preview.md#serializefunc)进行序列化的过程中调用此函数，将数据写入缓存。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [SerializeFunc](openfileboost_preview.md#serializefunc)) (const void \*object, [WriteFunc](openfileboost_preview.md#writefunc) writeFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行序列化操作的回调函数定义。由开发者实现，用于将复杂类型数据进行序列化操作。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [DeserializeFunc](openfileboost_preview.md#deserializefunc)) (void \*\*object, [ReadFunc](openfileboost_preview.md#readfunc) readFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行反序列化操作的回调函数定义。由开发者实现，用于将已序列化的数据恢复为原始数据。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) {  OPEN\_FILE\_BOOST\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201,  OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401,  OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001,  OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002,  OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003,  OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004  } | 文件打开加速的错误码定义。 |
| [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode) { OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000  } | 回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义，用于app向系统返回回调函数执行结果。 |
| [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate) { OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,  OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,  OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2  } | app状态，用于指示app当前允许、拒绝或永久拒绝系统推荐预加载文件。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) {  FILE\_CACHE\_BOOST\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM = 401,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_SUPPORTED = 801,  FILE\_CACHE\_BOOST\_ERROR\_NOMEM = 1017220001,  FILE\_CACHE\_BOOST\_ERROR\_INTERNAL\_ERROR = 1017220002,  FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND = 1017220003,  FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST = 1017220004,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR = 1017220005,  FILE\_CACHE\_BOOST\_ERROR\_IO = 1017220006,  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED = 1017220007,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED = 1017220008,  FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT = 1017220009，  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED = 1017220010  } | 文件缓存加速相关的错误码定义。 |
| [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode) { FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE = 1017221001，  FILE\_CACHE\_BOOST\_CALLBACK\_IO\_CANCELED = 1017221002  } | 回调函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)和[SerializeFunc](openfileboost_preview.md#serializefunc)的错误码定义，用于应用程序将回调函数的执行结果返回给系统。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo) (void \*fileInfo, int32\_t \*fd) | 获取文件描述符信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo) (void \*fileInfo, char \*sandboxPath, int32\_t pathLen) | 获取沙箱路径信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload) ([HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) cancelFilePreload) | 注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_UnregisterFilePreload](openfileboost_preview.md#hms_openfileboost_unregisterfilepreload) (void) | 取消注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_NotifyPreloadHit](openfileboost_preview.md#hms_openfileboost_notifypreloadhit) (int32\_t fd, char \*sandboxPath, int32\_t pathLen) | 当用户打开预加载文件时, app调用该接口通知系统预加载命中, 这将有助于提高预加载文件预测的准确性。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_Init](openfileboost_preview.md#hms_filecacheboost_init) (const char \*path, size\_t pathLen, uint32\_t cacheUpperLimitMb, const char \*dbName, size\_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。  缓存路径：开发者传入相对路径，缓存保存在应用沙箱目录下。  缓存容量上限：当系统检测到缓存总量超出设定上限后，将根据缓存淘汰策略进行容量管控，删除相应的缓存以释放空间。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey) (const uint8\_t \*key, size\_t keyLen, const uint8\_t \*data, size\_t dataLen, uint32\_t weight) | 创建并添加一个缓存对象至文件缓存。 该函数通过指定的唯一标识符 (key) 将数据缓存至文件缓存系统中，便于后续快速访问。建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当缓存不再需要时，推荐开发者主动调用 [HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。开发者若想要对key对应的缓存内容做修改，需要先调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除之前的key，再重新创建和添加。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey) (const uint8\_t \*key, size\_t keyLen, uint8\_t \*\*data, size\_t \*dataLen) | 根据指定的key查询缓存对象，若存在，则从磁盘中加载缓存对象的内容。调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| void [HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject) (uint8\_t \*data) | 释放调用[HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey)或[HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey)分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [SerializeFunc](openfileboost_preview.md#serializefunc) func, const void \*object, uint32\_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)对该象进行序列化处理，以便将其存储至磁盘并支持后续恢复。 例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [DeserializeFunc](openfileboost_preview.md#deserializefunc) func, void \*\*object) | 根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)将其还原为原始数据，从而获得完整的对象内容。 调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey) (const uint8\_t \*key, size\_t keyLen) | 根据指定的key删除对应的缓存对象。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_CancelOngoingIOByKey](openfileboost_preview.md#hms_filecacheboost_cancelongoingiobykey) (const uint8\_t \*key, size\_t keyLen) | 取消key对应的缓存对象当前正在进行的I/O操作。当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。  当该函数返回 FILE\_CACHE\_BOOST\_SUCCESS，开发者可以立即释放数据对象；当返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED，表示当前没有正在执行的 key 需要被取消，开发者需要确认该 key 对应的动作执行完成或无需执行后再释放数据对象。  例如当一个线程尝试删除数据对象的同时，有其他线程对其进行[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)操作， 调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_ClearAllCache](openfileboost_preview.md#hms_filecacheboost_clearallcache) (void) | 清理所有的缓存对象。 该函数会释放通过[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)和[HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey)创建的所有缓存对象 |

## 宏定义说明

PC/2in1

### MAX\_BUFFER\_LENGTH

PC/2in1

```
1. #define MAX_BUFFER_LENGTH   1024
```

**描述**

沙箱路径最大长度。

**起始版本：** 5.0.3(15)

## 类型定义说明

PC/2in1

### HMS\_OpenFileBoost\_OnFilePreload

PC/2in1

```
1. typedef OpenFileBoost_CbErrCode(*HMS_OpenFileBoost_OnFilePreload) (void *fileInfo)
```

**描述**

系统向应用推荐或取消推荐预加载文件的回调函数定义。系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 预加载文件信息，app可以调用[HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo)获取对应的文件描述符信息，然后调用[HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo)获取对应的沙箱路径信息。app应该在当前回调上下文中同步解析预加载文件，以便系统可以评估本次预加载文件的资源消耗。 |

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS，如果失败则返回 OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE。

### HMS\_OpenFileBoost\_QueryAppState

PC/2in1

```
1. typedef OpenFileBoost_AppState(*HMS_OpenFileBoost_QueryAppState) (void)
```

**描述**

系统查询app状态的回调函数定义，该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先回调app。该函数用于系统向app查询当前是否允许推荐文件给app。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。

**起始版本：** 5.0.3(15)

**返回：**

如果app允许推荐文件，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD，系统接下来将调用 [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)去推荐文件进行预加载。 如果app拒绝此次推荐，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD。如果app在本次注册期间不想再收到推荐，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD，然后尽快调用HMS\_OpenFileBoost\_UnregisterFilePreloadCb来取消注册。

### CacheKey

PC/2in1

```
1. typedef struct CacheKey CacheKey
```

**描述**

开发者在序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)和反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)调用[WriteFunc](openfileboost_preview.md#writefunc)和[ReadFunc](openfileboost_preview.md#readfunc)时，传入的key相关数据结构的对外声明。

**起始版本：** 6.1.0(23)

### SerializeFunc

PC/2in1

```
1. typedef FileCacheBoost_CbErrCode(*SerializeFunc) (const void *object, WriteFunc writeFunc, struct CacheKey *key)
```

**描述**

序列化函数，定义了系统执行序列化操作时的回调接口。由开发者实现，用于将复杂类型数据进行序列化操作。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| object | 待序列化的对象。 |
| writeFunc | 将序列化数据写入缓存的回调函数，参数类型可参见[WriteFunc](openfileboost_preview.md#writefunc)。 |
| key | 序列化对象的key。 |

**返回：**

函数执行成功则返回FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS，函数执行失败则返回FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE，其他错误详见[FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)。

### WriteFunc

PC/2in1

```
1. typedef FileCacheBoost_ErrCode(*WriteFunc) (const void *buffer, size_t bufferLen, struct CacheKey *key)
```

**描述**

[SerializeFunc](openfileboost_preview.md#serializefunc) 进行序列化的过程中调用此函数，将数据写入缓存。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 待写入数据。 |
| bufferLen | 待写入数据的长度。 |
| key | 待写入缓存对象的key。 |

**返回：**

如果函数执行成功，则返回FILE\_CACHE\_BOOST\_SUCCESS，如果因数据对象内存被释放，导致写入缓存对象任务无法执行则返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED，其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### DeserializeFunc

PC/2in1

```
1. typedef FileCacheBoost_CbErrCode(*DeserializeFunc) (void **object, ReadFunc readFunc, struct CacheKey *key)
```

**描述**

反序列化函数，定义了系统执行反序列化操作时的回调接口。由开发者实现，用于将已序列化的数据恢复为原始数据。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| object | 反序列化后生成的数据。 |
| readFunc | 从缓存中读取序列化数据的回调函数，参数类型可参见[ReadFunc](openfileboost_preview.md#readfunc)。 |
| key | 待反序列化对象的key。 |

**返回：**

函数执行成功则返回FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS，函数执行失败则返回FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE，其他错误详见[FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)。

### ReadFunc

PC/2in1

```
1. typedef FileCacheBoost_ErrCode(*ReadFunc) (void *buffer, size_t *bufferLen, struct CacheKey *key)
```

**描述**

[DeserializeFunc](openfileboost_preview.md#deserializefunc)进行反序列化的过程中调用此函数，可从缓存读取数据到缓冲区。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| buffer | 存储读取数据的缓冲区。 |
| bufferLen | 作为入参表示期望读取的数据长度，作为出参表示实际读取的数据长度。 |
| key | 当前正在读取的缓存对象。 |

**返回：**

如果函数执行成功，则返回FILE\_CACHE\_BOOST\_SUCCESS，如果因数据对象内存被释放，导致读取缓存对象任务无法执行则返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED，其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

## 枚举类型说明

PC/2in1

### OpenFileBoost\_AppState

PC/2in1

```
1. enum OpenFileBoost_AppState
```

**描述**

app状态，用于指示app当前是否允许系统推荐预加载文件。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD | 当前允许推荐预加载文件。 |
| OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD | 当前不允许推荐预加载文件。 |
| OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD | 这次注册期间永远不允许推荐预加载文件。 |

### OpenFileBoost\_CbErrCode

PC/2in1

```
1. enum OpenFileBoost_CbErrCode
```

**描述**

回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义，它用于app向系统返回回调函数执行结果。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS | 回调函数执行成功。 |
| OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE | 回调函数执行失败。 |

### OpenFileBoost\_ErrCode

PC/2in1

```
1. enum OpenFileBoost_ErrCode
```

**描述**

文件打开加速的错误码定义。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_SUCCESS | 成功。 |
| OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED | 未授权。 |
| OPEN\_FILE\_BOOST\_INVALID\_PARAM | 无效输入参数。 |
| OPEN\_FILE\_BOOST\_INTERNAL\_ERROR | 内部错误。 |
| OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER | 传入的缓冲区的长度不足。 |
| OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE | 服务不可用。 |
| OPEN\_FILE\_BOOST\_NO\_MEMORY | 内存不足。 |

### FileCacheBoost\_CbErrCode

PC/2in1

```
1. enum FileCacheBoost_CbErrCode
```

**描述**

回调函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)和[SerializeFunc](openfileboost_preview.md#serializefunc)的错误码定义，应用程序将回调函数的执行结果返回给系统。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS = 0 | 回调函数执行成功。 |
| FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE = 1017221001 | 回调函数执行失败。 |
| FILE\_CACHE\_BOOST\_CALLBACK\_IO\_CANCELED = 1017221002 | I/O取消错误。 |

### FileCacheBoost\_ErrCode

PC/2in1

```
1. enum FileCacheBoost_ErrCode
```

**描述**

文件缓存加速相关的错误码定义。

**起始版本：** 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| FILE\_CACHE\_BOOST\_SUCCESS = 0 | 成功。 |
| FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM = 401 | 无效输入参数。 |
| FILE\_CACHE\_BOOST\_ERROR\_NOT\_SUPPORTED = 801 | 该设备不支持此API。 |
| FILE\_CACHE\_BOOST\_ERROR\_NOMEM = 1017220001 | 内存不足。 |
| FILE\_CACHE\_BOOST\_ERROR\_INTERNAL\_ERROR = 1017220002 | 内部错误。 |
| FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND = 1017220003 | 缓存key不存在。 |
| FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST = 1017220004 | 缓存key已存在。 |
| FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR = 1017220005 | 路径初始化错误。 |
| FILE\_CACHE\_BOOST\_ERROR\_IO = 1017220006 | I/O读写错误。 |
| FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED = 1017220007 | I/O 被取消。 |
| FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED = 1017220008 | 未初始化。 |
| FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT = 1017220009 | 单个缓存大小超出限制。 |
| FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED = 1017220010 | I/O 取消失败。 |

## 函数说明

PC/2in1

### HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo()

PC/2in1

```
1. OpenFileBoost_ErrCode HMS_OpenFileBoost_GetFdFromPreloadFileInfo (void * fileInfo, int32_t * fd)
```

**描述**

获取文件描述符信息。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 系统向app推荐的预加载文件信息。 |
| fd | 输出参数，预加载文件的文件描述符信息。 |

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。

### HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo()

PC/2in1

```
1. OpenFileBoost_ErrCode HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo (void * fileInfo, char * sandboxPath, int32_t pathLen)
```

**描述**

获取沙箱路径信息。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 系统向app推荐的预加载文件信息。 |
| sandboxPath | 输出参数，预加载文件的沙箱路径信息，app应该传递一个指向一块有效内存区域的指针，系统将向其中填充沙箱路径信息。 |
| pathLen | 用于填充沙箱路径的内存区域的长度。 |

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS，如果传入的内存缓冲区太小，系统将返回OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER，其他错误详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。

### HMS\_OpenFileBoost\_NotifyPreloadHit()

PC/2in1

```
1. OpenFileBoost_ErrCode HMS_OpenFileBoost_NotifyPreloadHit (int32_t fd, char * sandboxPath, int32_t pathLen)
```

**描述**

当用户打开预加载文件时，app调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fd | 命中文件的文件描述符信息。 |
| sandboxPath | 命中文件的沙箱路径。 |
| pathLen | 沙箱路径的长度 |

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。

### HMS\_OpenFileBoost\_RegisterFilePreload()

PC/2in1

```
1. OpenFileBoost_ErrCode HMS_OpenFileBoost_RegisterFilePreload (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload)
```

**描述**

注册预加载回调。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| queryAppState | app状态查询回调函数，在通知预加载之前先调用该回调函数查询当前是否允许推荐预加载文件。 |
| filePreload | 文件预加载回调，系统预测用户可能打开的文件，并通过该回调函数通知调用者。 |
| cancelFilePreload | 取消文件预加载回调，比如系统可用内存不足时系统会通知调用方取消文件的预加载。 |

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。

### HMS\_OpenFileBoost\_UnregisterFilePreload()

PC/2in1

```
1. OpenFileBoost_ErrCode HMS_OpenFileBoost_UnregisterFilePreload (void)
```

**描述**

取消注册预加载回调。

**起始版本：** 5.0.3(15)

**返回：**

函数执行结果，如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。

### HMS\_FileCacheBoost\_Init()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_Init (const char * path, size_t pathLen, uint32_t cacheUpperLimitMb, const char * dbName, size_t dbNameLen)
```

**描述**

初始化缓存路径、缓存容量上限和数据库名称。该函数用于配置缓存文件的存储目录以及缓存最大容量。当系统检测到缓存总量超出设定上限后，将根据缓存淘汰策略进行容量管控，删除相应的缓存以释放空间。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| path | 存储缓存文件的路径。开发者传入相对路径即可，系统会创建完整路径，传入的路径须有效。 |
| pathLen | 缓存路径的缓冲区长度。 |
| cacheUpperLimitMb | 缓存容量上限值（单位为MB）。若缓存使用量超过该限制，系统将触发缓存淘汰机制。 若用户设置的缓存容量大于系统预设的默认上限，则系统将使用默认上限为作为缓存容量上限值。 |
| dbName | 数据库文件名，该数据库用于缓存元数据管理。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。 |
| dbNameLen | 数据库名称的缓冲区长度。 |

**返回：**

函数执行结果:

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR：传入的路径无效，系统无法创建。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_AddObjectByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_AddObjectByKey (const uint8_t * key, size_t keyLen, const uint8_t * data, size_t dataLen, uint32_t weight)
```

**描述**

创建并添加一个缓存对象至文件缓存。 该函数通过指定的唯一标识符 (key) 将数据缓存至文件缓存系统中，便于后续快速访问。

建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当缓存不再需要时，推荐开发者主动调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。

开发者若想要对key对应的缓存内容做修改，需要先调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除之前的key，再重新创建和添加。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的唯一标识符。该值通常可由文件的特征值生成，例如图片的SHA-256 、MD4哈希值等。当图片内容未发生变化时，再次打开可获取到对应缓存。当图片内容发生变化时，key值应同步更新，原缓存内容失效。 |
| keyLen | key的缓冲区长度。 |
| data | 待缓存数据。 |
| dataLen | 缓存数据的缓冲区长度。 |
| weight | 缓存对象的权重值，用于反映其重要性或优先级。若开发者希望某个缓存对象优先保留，应为其分配较高的权重。  有效取值范围为0-10000，如果输入的权重超过10000，系统会将其设置为10000。  例如开发者可传入数据解码耗时作为权重，当缓存空间达到上限时，系统将参考该权重计算缓存的淘汰顺序。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST：key 值已经存在。

FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。

FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放，导致创建缓存对象任务无法执行。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT：添加的缓存大小大于缓存容量上限。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见 [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_GetObjectByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_GetObjectByKey (const uint8_t * key, size_t keyLen, uint8_t ** data, size_t * dataLen )
```

**描述**

根据指定的key查询缓存对象，若存在，则从磁盘中加载缓存对象的内容。调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |
| data | 出参，缓存对象的内容。开发者需确保传入参数非空。 |
| dataLen | 缓存对象内容的长度。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。

FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存被释放，导致获取缓存对象任务无法执行。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见 [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_FreeObject()

PC/2in1

```
1. void HMS_FileCacheBoost_FreeObject (uint8_t * data)
```

**描述**

释放调用[HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey)或[HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey)分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| data | 需要释放的内存数据。 |

### HMS\_FileCacheBoost\_AddSerialObjectByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_AddSerialObjectByKey (const uint8_t * key, size_t keyLen, SerializeFunc func, const void * object, uint32_t weight )
```

**描述**

创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)对该象进行序列化处理，以便将该对象存储至磁盘并支持后续恢复。

例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的长度。 |
| func | 开发者实现的序列化函数，用于将复杂类型数据进行序列化处理。 |
| object | 待缓存的复杂类型对象。 |
| weight | 缓存对象的权重值，用于反映其重要性或优先级，有效取值范围为0-10000，如果输入的权重超过10000，系统会将其设置为10000。 例如开发者可传入数据解码耗时作为权重，当缓存空间达到上限时，系统将参考该权重计算缓存的淘汰顺序。 若开发者希望某个缓存对象优先保留，应为其分配较高的权重。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST：key值已经存在。

FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。

FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放， 导致创建缓存对象任务无法执行。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT：添加的缓存大小大于缓存容量上限。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见 [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_GetSerialObjectByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_GetSerialObjectByKey (const uint8_t * key, size_t keyLen, DeserializeFunc func, void ** object )
```

**描述**

根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)将其还原为原始数据，从而获得完整的对象内容。 调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |
| func | 开发者实现的反序列化函数，于将已序列化的数据恢复为原始对象。 |
| object | 出参，缓存对象的内容。开发者需确保传入参数非空。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。

FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放，导致获取缓存对象任务无法执行。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见 [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_CancelOngoingIOByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_CancelOngoingIOByKey (const uint8_t * key, size_t keyLen )
```

**描述**

取消key对应的缓存对象当前正在进行的I/O操作。当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。

当该函数返回 FILE\_CACHE\_BOOST\_SUCCESS，开发者可以立即释放数据对象；当返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED，表示当前没有正在执行的 key 需要被取消，开发者需要确认该 key 对应的动作执行完成或无需执行后再释放数据对象。

例如当一个线程尝试删除数据对象的同时，有其他线程对其进行[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)操作， 调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：缓存完成和I/O取消成功，开发者可以立即释放数据对象。

FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED：I/O取消失败，表示当前没有正在执行的key需要被取消，开发者需要确认该key对应的动作执行完成或无需执行后再释放数据对象。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。

其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_RemoveObjectByKey()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_RemoveObjectByKey (const uint8_t * key, size_t keyLen )
```

**描述**

根据指定的key删除对应的缓存对象。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入参数无效。

其他错误详见 [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。

### HMS\_FileCacheBoost\_ClearAllCache()

PC/2in1

```
1. FileCacheBoost_ErrCode HMS_FileCacheBoost_ClearAllCache (void )
```

**描述**

清理所有的缓存对象。 该函数会释放通过[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)和[HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey)创建的所有缓存对象。

**起始版本：** 6.1.0(23)

**返回：**

函数执行结果：

FILE\_CACHE\_BOOST\_SUCCESS：执行成功。

FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。

其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。
