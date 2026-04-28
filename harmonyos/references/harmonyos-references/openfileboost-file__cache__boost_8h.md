---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-file__cache__boost_8h
title: file_cache_boost.h
category: harmonyos-references
scraped_at: 2026-04-28T08:18:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f45a2ac5f2b6de455a631b2723c2e2c9c7c85104b990b800b6c7185110e7271a
---

## 概述

PC/2in1

声明通用文件缓存加速的API集合。

**引用文件：** <PreviewKit/file\_cache\_boost.h>

**库：** libfile\_cache\_boost.so

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 6.1.0(23)

**相关模块：** [Preview](openfileboost_preview.md)

## 汇总

PC/2in1

### 类型定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| typedef struct [CacheKey](openfileboost_preview.md#cachekey) [CacheKey](openfileboost_preview.md#cachekey) | 开发者传入的key相关数据结构的对外声明，开发者只需在序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)和反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)调用[WriteFunc](openfileboost_preview.md#writefunc)和[ReadFunc](openfileboost_preview.md#readfunc)时传入即可。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [ReadFunc](openfileboost_preview.md#readfunc)) (void \*buffer, size\_t \*bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [DeserializeFunc](openfileboost_preview.md#deserializefunc)进行反序列化的过程中调用此函数，可从缓存读取数据到缓冲区。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [WriteFunc](openfileboost_preview.md#writefunc)) (const void \*buffer, size\_t bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [SerializeFunc](openfileboost_preview.md#serializefunc)进行序列化的过程中调用此函数，将数据写入缓存。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [DeserializeFunc](openfileboost_preview.md#deserializefunc)) (void \*\*object, [ReadFunc](openfileboost_preview.md#readfunc) readFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行反序列化操作的回调函数定义。由开发者实现，用于将已序列化的数据恢复为原始数据。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [SerializeFunc](openfileboost_preview.md#serializefunc)) (const void \*object, [WriteFunc](openfileboost_preview.md#writefunc) writeFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行序列化操作的回调函数定义。由开发者实现，用于将复杂类型数据进行序列化操作。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) {  FILE\_CACHE\_BOOST\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM = 401,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_SUPPORTED = 801,  FILE\_CACHE\_BOOST\_ERROR\_NOMEM = 1017220001,  FILE\_CACHE\_BOOST\_ERROR\_INTERNAL\_ERROR = 1017220002, FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND = 1017220003, FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST = 1017220004, FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR = 1017220005,  FILE\_CACHE\_BOOST\_ERROR\_IO = 1017220006, FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED = 1017220007, FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED = 1017220008, FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT = 1017220009，  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED = 1017220010  } | 文件缓存加速相关的错误码定义。 |
| [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode) {  FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE = 1017221001，  FILE\_CACHE\_BOOST\_CALLBACK\_IO\_CANCELED = 1017221002  } | 回调函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)和[SerializeFunc](openfileboost_preview.md#serializefunc)的错误码定义，用于应用程序将回调函数的执行结果返回给系统。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_Init](openfileboost_preview.md) (const char \*path, size\_t pathLen, uint32\_t cacheUpperLimitMb, const char \*dbName, size\_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey) (const uint8\_t \*key, size\_t keyLen, const uint8\_t \*data, size\_t dataLen, uint32\_t weight) | 创建并添加一个缓存对象至文件缓存。  系统通过key管理缓存，建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当不再需要缓存时，推荐开发者主动调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。  开发者若想要对key对应的缓存内容做修改，需要先调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除之前的key，再重新创建和添加。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey) (const uint8\_t \*key, size\_t keyLen, uint8\_t \*\*data, size\_t \*dataLen) | 根据指定的key查询缓存对象。若缓存对象存在，则从磁盘中加载缓存对象的内容。调用该函数，系统会分配一段内存用于存储缓存数据，作为出参返回给开发者。开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| void [HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject) (uint8\_t \*data) | 释放调用[HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey)或[HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey)分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [SerializeFunc](openfileboost_preview.md#serializefunc) func, const void \*object, uint32\_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)对该象进行序列化处理，以便将其存储至磁盘并支持后续恢复。  例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [DeserializeFunc](openfileboost_preview.md#deserializefunc) func, void \*\*object) | 根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)将其还原为原始数据，从而获得完整的对象内容。  调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey) (const uint8\_t \*key, size\_t keyLen) | 根据指定的key删除对应的缓存对象。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_CancelOngoingIOByKey](openfileboost_preview.md#hms_filecacheboost_cancelongoingiobykey) (const uint8\_t \*key, size\_t keyLen) | 取消key对应的缓存对象当前正在进行的I/O操作。  当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。  若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。  例如当一个线程尝试删除数据对象的同时，有其他线程对其进行[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)操作，调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_ClearAllCache](openfileboost_preview.md#hms_filecacheboost_clearallcache) (void) | 清理所有的缓存对象。 该函数会释放通过[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)和[HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey)创建的所有缓存对象。 |
