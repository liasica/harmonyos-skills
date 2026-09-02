---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost_preview
title: Preview
breadcrumb: API参考 > 应用服务 > Preview Kit（文件预览服务） > C API > 模块 > Preview
category: harmonyos-references
scraped_at: 2026-09-02T15:03:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fe783d72a737f88deaa448c120d7de2eb80fdab4ba512942da85a0b6272997a4
---

## 概述

Preview Kit（文件预览服务）为应用提供便捷的文件快速预览服务，包括文件打开加速功能和通用文件缓存加速功能。

* 文件打开加速功能支持应用通过预加载机制提前加载文件，缩短用户打开文件时间，给用户提供流畅顺滑的爽感体验。
* 通用文件缓存加速功能支持应用通过缓存服务，将解码后的数据缓存到磁盘中，后续可直接获取缓存数据，省去解码过程，提升文件打开和浏览的性能。

详见[文件打开加速开发指南](../harmonyos-guides/preview-openfileboost.md)和[通用文件缓存加速开发指南](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 5.0.3(15)

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [open\_file\_boost.h](openfileboost-open__file__boost_8h.md) | 声明文件打开加速的API集合。 |
| [file\_cache\_boost.h](openfileboost-file__cache__boost_8h.md) | 声明用于通用文件缓存加速的API，以优化文件打开和文件浏览等场景中的性能。 |
| [preview\_kit.h](openfileboost-preview__kit_8h.md) | 声明Preview Kit所包含的所有头文件。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [MAX\_BUFFER\_LENGTH](openfileboost_preview.md#max_buffer_length) 1024 | 沙箱路径最大长度1024。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef  [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate)(\* [HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate)) (void) | 该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先调用，用于向App查询当前是否允许推荐文件给App。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，App返回特定枚举值拒绝预加载。 |
| typedef [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode)(\* [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)) (void \*fileInfo) | 系统预测用户可能打开的文件，并通过该回调函数通知App，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知App取消某些文件的预加载。 |
| typedef struct [CacheKey](openfileboost_preview.md#cachekey) [CacheKey](openfileboost_preview.md#cachekey) | 开发者传入的key相关数据结构的对外声明，开发者只需在序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)和反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)调用 [WriteFunc](openfileboost_preview.md#writefunc) 和[ReadFunc](openfileboost_preview.md#readfunc)时传入即可。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [ReadFunc](openfileboost_preview.md#readfunc)) (void \*buffer, size\_t \*bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [DeserializeFunc](openfileboost_preview.md#deserializefunc)进行反序列化的过程中调用此函数，可从缓存读取数据到缓冲区。 |
| typedef [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)(\* [WriteFunc](openfileboost_preview.md#writefunc)) (const void \*buffer, size\_t bufferLen, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | [SerializeFunc](openfileboost_preview.md#serializefunc)进行序列化的过程中调用此函数，将数据写入缓存。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [SerializeFunc](openfileboost_preview.md#serializefunc)) (const void \*object, [WriteFunc](openfileboost_preview.md#writefunc) writeFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行序列化操作的回调函数定义。由开发者实现，用于将复杂类型数据进行序列化操作。 |
| typedef [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)(\* [DeserializeFunc](openfileboost_preview.md#deserializefunc)) (void \*\*object, [ReadFunc](openfileboost_preview.md#readfunc) readFunc, struct [CacheKey](openfileboost_preview.md#cachekey) \*key) | 系统执行反序列化操作的回调函数定义。由开发者实现，用于将已序列化的数据恢复为原始数据。 |
| typedef struct [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) | 文件扫描选项配置的不透明类型。 |
| typedef struct [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) | 文件扫描结果的不透明类型。 |
| typedef [FileScanBoost\_CbErrCode](openfileboost_preview.md#filescanboost_cberrcode)(\* [HMS\_Preview\_FileScanBoost\_OnFileScan](openfileboost_preview.md#hms_preview_filescanboost_onfilescan)) (int32\_t fd, const char \*path, uint32\_t pathLen) | 文件扫描回调通知的函数指针类型。系统调用此回调来发送扫描任务。此回调方法与扫描任务执行是异步的，应用程序应在收到扫描任务后立即返回回调返回值，而不应阻塞回调。并且扫描任务完成后的最终结果应使用[HMS\_Preview\_FileScanBoost\_ReportScanResult](openfileboost_preview.md#hms_preview_filescanboost_reportscanresult)报告。 |
| typedef struct [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) | 应用支持预加载的文件信息，用于描述一组符合预加载条件的文件特征。 开发者可以使用[HMS\_Preview\_OpenFileBoost\_SupportFileCreate](openfileboost_preview.md#hms_preview_openfileboost_supportfilecreate)创建该结构体， 配置哪些类型的文件可以被系统预加载。 |
| typedef struct [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) | 应用支持预加载的文件信息和文件类型数量，用于向系统注册一批支持预加载的文件类型。 |
| typedef struct [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) | 应用向系统传递的文件操作信息。 开发者可传递文件路径和该文件的操作信息，操作信息包括但不限于： 打开："open"，关闭："close"，导入/加载："import"，导出："export"， TAB隐藏："tab\_hidden"，TAB可见"tab\_visible"， 保存："save"，新建："create"，云上传："upload"，云下载："download"，共享："share"， 打印："print"，另存为："save\_as"，放映："play"。 开发者可以使用[HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfocreate)函数创建此结构体。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) {  OPEN\_FILE\_BOOST\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201,  OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401,  OPEN\_FILE\_BOOST\_CAPABILITY\_NOT\_SUPPORTED = 801,  OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001,  OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002,  OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003,  OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004  } | 文件打开加速的错误码定义。 |
| [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode) {  OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000  } | 回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义，用于App向系统返回回调函数执行结果。 |
| [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate) {  OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,  OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,  OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2,  OPEN\_FILE\_BOOST\_APP\_STATE\_EXCEL\_TRANSACTION = 3  } | App状态，用于指示App当前允许、拒绝或永久拒绝系统推荐预加载文件。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) {  FILE\_CACHE\_BOOST\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM = 401,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_SUPPORTED = 801,  FILE\_CACHE\_BOOST\_ERROR\_NOMEM = 1017220001,  FILE\_CACHE\_BOOST\_ERROR\_INTERNAL\_ERROR = 1017220002,  FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND = 1017220003,  FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST = 1017220004,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR = 1017220005,  FILE\_CACHE\_BOOST\_ERROR\_IO = 1017220006,  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED = 1017220007,  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED = 1017220008,  FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT = 1017220009,  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED = 1017220010  } | 文件缓存加速相关的错误码定义。 |
| [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode) {  FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS = 0,  FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE = 1017221001,  FILE\_CACHE\_BOOST\_CALLBACK\_IO\_CANCELED = 1017221002  } | 回调函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)和[SerializeFunc](openfileboost_preview.md#serializefunc)的错误码定义，应用程序将回调函数的执行结果返回给系统。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) {  FILE\_SCAN\_BOOST\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_ERROR\_PERMISSION\_NOT\_GRANTED = 201,  FILE\_SCAN\_BOOST\_ERROR\_INVALID\_PARAM = 401,  FILE\_SCAN\_BOOST\_ERROR\_CAPABILITY\_NOT\_SUPPORTED = 801,  FILE\_SCAN\_BOOST\_ERROR\_INTERNAL = 1017230001,  FILE\_SCAN\_BOOST\_ERROR\_NOT\_REGISTERED = 1017230002,  FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED = 1017230003,  FILE\_SCAN\_BOOST\_ERROR\_SERVICE\_UNAVAILABLE = 1017230004,  FILE\_SCAN\_BOOST\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017230005  } | 文件扫描加速功能返回的所有错误码的枚举。 |
| [FileScanBoost\_CbErrCode](openfileboost_preview.md#filescanboost_cberrcode) {  FILE\_SCAN\_BOOST\_CALLBACK\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_INTERNAL = 1017240001,  FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017240002  } | 文件扫描回调特定错误码的枚举。 |
| [FileScanBoost\_ScanState](openfileboost_preview.md#filescanboost_scanstate) {  FILE\_SCAN\_BOOST\_SCAN\_STATE\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_SCAN\_STATE\_PROCESS\_ERROR = 1,  FILE\_SCAN\_BOOST\_SCAN\_STATE\_FILE\_ERROR = 2  } | 文件扫描后扫描状态的枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| bool [HMS\_Preview\_FileBoost\_IsSupported](openfileboost_preview.md#hms_preview_fileboost_issupported) (void) | 查询当前设备是否支持文件打开加速功能。建议使用本接口检查，确认设备支持文件打开加速功能后，再使用其他文件打开加速接口如[HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload)、[HMS\_Preview\_FileScanBoost\_RegisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_registerfilescan)等。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo) (void \*fileInfo, int32\_t \*fd) | 获取文件描述符信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo) (void \*fileInfo, char \*sandboxPath, int32\_t pathLen) | 获取沙箱路径信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload) ([HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) cancelFilePreload) | 应用使用本接口向系统注册文件预加载回调。  后续，系统预测用户可能打开的文件时，先调用queryAppState来向应用查询当前是否可以推荐预加载的文件。如果应用通过queryAppState返回允许推荐，则系统通过调用filePreload推荐一个文件，供应用进行预加载操作。  在某些特定情况下，例如系统可用内存不足、有其他文件更有可能被用户打开、或其他不适合文件保持预加载状态的条件发生，系统会通过调用cancelFilePreload来取消部分文件的预加载。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_UnregisterFilePreload](openfileboost_preview.md#hms_openfileboost_unregisterfilepreload) (void) | 取消注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_NotifyPreloadHit](openfileboost_preview.md#hms_openfileboost_notifypreloadhit) (int32\_t fd, char \*sandboxPath, int32\_t pathLen) | 当用户打开预加载文件时，App调用该接口通知系统预加载命中， 这将有助于提高预加载文件预测的准确性。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanOptionCreate](openfileboost_preview.md#hms_preview_filescanboost_scanoptioncreate) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*\*outOption) | 创建FileScanBoost\_ScanOption实例。 |
| void [HMS\_Preview\_FileScanBoost\_ScanOptionDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanoptiondestroy) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option) | 销毁FileScanBoost\_ScanOption实例。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanOptionAddSupportFile](openfileboost_preview.md#hms_preview_filescanboost_scanoptionaddsupportfile) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option, const char \*suffix, uint32\_t suffixLen) | 向扫描选项添加支持的文件类型。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultCreate](openfileboost_preview.md#hms_preview_filescanboost_scanresultcreate) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*\*outResult) | 创建FileScanBoost\_ScanResult实例。 |
| void [HMS\_Preview\_FileScanBoost\_ScanResultDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanresultdestroy) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result) | 销毁FileScanBoost\_ScanResult实例。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetState](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetstate) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, [FileScanBoost\_ScanState](openfileboost_preview.md#filescanboost_scanstate) state) | 在结果中设置扫描状态。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetMaxAtomicTime](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetmaxatomictime) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, int64\_t maxAtomicTime) | 在结果中设置最大原子时间。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetMemSize](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetmemsize) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, int64\_t memSize) | 在结果中设置内存大小。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_RegisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_registerfilescan) ([HMS\_Preview\_FileScanBoost\_OnFileScan](openfileboost_preview.md#hms_preview_filescanboost_onfilescan) fileScanCb, [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option) | 使用扩展名过滤方式注册多文件类型的回调函数。 在上一次注册结果注销之前，请勿重复注册。 重复注册将返回错误码FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED， 且仅首次注册的信息生效。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_UnregisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_unregisterfilescan) (void) | 移除已注册的文件扫描回调函数。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ReportScanResult](openfileboost_preview.md#hms_preview_filescanboost_reportscanresult) (const char \*path, uint32\_t pathLen, [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result) | 报告文件扫描操作的完成结果。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_SupportFileCreate](openfileboost_preview.md#hms_preview_openfileboost_supportfilecreate) (const char \*suffix, uint32\_t suffixLen, uint64\_t lowerLimitKb, uint64\_t upperLimitKb, [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*\*outSupportFile) | 创建[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_SupportFileDestroy](openfileboost_preview.md#hms_preview_openfileboost_supportfiledestroy) ([OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*supportFile) | 销毁[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsCreate](openfileboost_preview.md#hms_preview_openfileboost_optionscreate) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*\*outOptions) | 创建一个空的[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)。 使用[HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile](openfileboost_preview.md#hms_preview_openfileboost_optionsaddsupportfile)添加文件。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile](openfileboost_preview.md#hms_preview_openfileboost_optionsaddsupportfile) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options, const [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*supportFile) | 向[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)添加支持预加载的文件类型列表。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsDestroy](openfileboost_preview.md#hms_preview_openfileboost_optionsdestroy) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options) | 销毁[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_RegisterFilePreloadWithOption](openfileboost_preview.md#hms_preview_openfileboost_registerfilepreloadwithoption) (HMS\_OpenFileBoost\_QueryAppState queryAppState, HMS\_OpenFileBoost\_OnFilePreload filePreload, HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload, [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options) | 注册预加载回调，允许应用传入支持预加载的文件信息。 |
| bool [HMS\_Preview\_OpenFileBoost\_IsEnabled](openfileboost_preview.md#hms_preview_openfileboost_isenabled) (void) | 查询应用加速特性是否可用。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfocreate) (const char \*path, uint32\_t pathLen, const char \*operation, uint32\_t operationLen, [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*\*outFileOperationInfo) | 创建[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_FileOperationInfoDestroy](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfodestroy) ([OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*fileOperationInfo) | 销毁[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_NotifyFileOperation](openfileboost_preview.md#hms_preview_openfileboost_notifyfileoperation) ([OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*fileOperationInfo) | 当用户对文件进行操作时，App调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。 |
| bool [HMS\_Preview\_FileCacheBoost\_IsSupported](openfileboost_preview.md#hms_preview_filecacheboost_issupported) (void) | 查询当前设备是否支持文件缓存加速功能。建议使用本接口检查，确认设备支持文件缓存加速功能后，再使用其他文件缓存加速接口如[HMS\_FileCacheBoost\_Init](openfileboost_preview.md#hms_filecacheboost_init)等。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_Init](openfileboost_preview.md#hms_filecacheboost_init) (const char \*path, size\_t pathLen, uint32\_t cacheUpperLimitMb, const char \*dbName, size\_t dbNameLen) | 初始化缓存路径、缓存容量上限、数据库名称。系统保证了线程并发安全控制，如需支持多进程并发场景，建议各进程使用不同的数据库文件名以保证访问安全性。  缓存路径：开发者传入相对路径，缓存保存在应用沙箱目录下。  缓存容量上限：当系统检测到缓存总量超出设定上限后，将根据缓存淘汰策略进行容量管控，删除相应的缓存以释放空间。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey) (const uint8\_t \*key, size\_t keyLen, const uint8\_t \*data, size\_t dataLen, uint32\_t weight) | 创建并添加一个缓存对象至文件缓存。 该函数通过指定的唯一标识符 (key) 将数据缓存至文件缓存系统中，便于后续快速访问。建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当缓存不再需要时，推荐开发者主动调用 [HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。开发者若想要对key对应的缓存内容做修改，需要先调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除之前的key，再重新创建和添加。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey) (const uint8\_t \*key, size\_t keyLen, uint8\_t \*\*data, size\_t \*dataLen) | 根据指定的key查询缓存对象，若存在，则从磁盘中加载缓存对象的内容。调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| void [HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject) (uint8\_t \*data) | 释放调用[HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey)或[HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey)分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [SerializeFunc](openfileboost_preview.md#serializefunc) func, const void \*object, uint32\_t weight) | 创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)将该对象进行序列化处理，以便将其存储至磁盘并支持后续恢复。 例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey) (const uint8\_t \*key, size\_t keyLen, [DeserializeFunc](openfileboost_preview.md#deserializefunc) func, void \*\*object) | 根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)将其还原为原始数据，从而获得完整的对象内容。 调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey) (const uint8\_t \*key, size\_t keyLen) | 根据指定的key删除对应的缓存对象。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_CancelOngoingIOByKey](openfileboost_preview.md#hms_filecacheboost_cancelongoingiobykey) (const uint8\_t \*key, size\_t keyLen) | 取消key对应的缓存对象当前正在进行的I/O操作。当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。  当该函数返回 FILE\_CACHE\_BOOST\_SUCCESS，开发者可以立即释放数据对象；当返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED，表示当前没有正在执行的 key 需要被取消，开发者需要确认该 key 对应的动作执行完成或无需执行后再释放数据对象。  例如当一个线程尝试删除数据对象的同时，有其他线程对其进行[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)操作， 调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。 |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) [HMS\_FileCacheBoost\_ClearAllCache](openfileboost_preview.md#hms_filecacheboost_clearallcache) (void) | 清理所有的缓存对象。 该函数会释放通过[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)和[HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey)创建的所有缓存对象。 |

## 宏定义说明

### MAX\_BUFFER\_LENGTH

```cpp
#define MAX_BUFFER_LENGTH 1024
```

**描述**

沙箱路径最大长度。

**起始版本：** 5.0.3(15)

## 类型定义说明

### HMS\_OpenFileBoost\_OnFilePreload

```cpp
typedef OpenFileBoost_CbErrCode(*HMS_OpenFileBoost_OnFilePreload) (void *fileInfo)
```

**描述**

系统向应用推荐或取消推荐预加载文件的回调函数定义。系统预测用户可能打开的文件，并通过该回调函数通知App，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知App取消某些文件的预加载。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 预加载文件信息，App可以调用[HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo)获取对应的文件描述符信息，然后调用[HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo)获取对应的沙箱路径信息。App应该在当前回调上下文中同步解析预加载文件，以便系统可以评估本次预加载文件的资源消耗。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS。  如果失败则返回OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE。 |

### HMS\_OpenFileBoost\_QueryAppState

```cpp
typedef OpenFileBoost_AppState(*HMS_OpenFileBoost_QueryAppState) (void)
```

**描述**

系统查询App状态的回调函数定义，该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先回调App。该函数用于系统向App查询当前是否允许推荐文件给App。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，App返回特定枚举值拒绝预加载。

**起始版本：** 5.0.3(15)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate) | 如果App允许推荐文件，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD，系统接下来将调用 [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)去推荐文件进行预加载。  如果App拒绝此次推荐，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD。  如果App在本次注册期间不想再收到推荐，应该返回OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD，然后尽快调用HMS\_OpenFileBoost\_UnregisterFilePreloadCb来取消注册。 |

### FileScanBoost\_ScanOption

```cpp
typedef struct FileScanBoost_ScanOption FileScanBoost_ScanOption
```

**描述**

文件扫描选项配置的不透明类型。

**起始版本：** 26.0.0

### FileScanBoost\_ScanResult

```cpp
typedef struct FileScanBoost_ScanResult FileScanBoost_ScanResult
```

**描述**

文件扫描结果的不透明类型。

**起始版本：** 26.0.0

### HMS\_Preview\_FileScanBoost\_OnFileScan

```cpp
typedef FileScanBoost_CbErrCode(* HMS_Preview_FileScanBoost_OnFileScan) (int32_t fd, const char *path, uint32_t pathLen)
```

**描述**

文件扫描回调通知的函数指针类型。 系统调用此回调来发送扫描任务。此回调方法与扫描任务执行是异步的， 应用程序应在收到扫描任务后立即返回回调返回值，而不应阻塞回调。并且扫描任务完成后的最终结果应使用[HMS\_Preview\_FileScanBoost\_ReportScanResult](openfileboost_preview.md#hms_preview_filescanboost_reportscanresult)报告。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| fd | 被扫描文件的文件描述符。 |
| path | 文件路径字符串。 |
| pathLen | 文件路径字符串的长度。最大路径长度为PATH\_MAX。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_CbErrCode](openfileboost_preview.md#filescanboost_cberrcode) | 回调错误码。  应用接受扫描任务或者返回错误。  FILE\_SCAN\_BOOST\_CALLBACK\_SUCCESS表示接受扫描任务，否则表示不接受。 |

### OpenFileBoost\_FileOperationInfo

```cpp
typedef struct OpenFileBoost_FileOperationInfo OpenFileBoost_FileOperationInfo
```

**描述**

应用向系统传递的文件操作信息。 开发者可传递文件路径和该文件的操作信息，操作信息包括但不限于：

| **操作** | **字符串** |
| --- | --- |
| 打开 | "open" |
| 关闭 | "close" |
| 导入/加载 | "import" |
| 导出 | "export" |
| TAB隐藏 | "tab\_hidden" |
| TAB可见 | "tab\_visible" |
| 保存 | "save" |
| 新建 | "create" |
| 云上传 | "upload" |
| 云下载 | "download" |
| 共享 | "share" |
| 打印 | "print" |
| 另存为 | "save\_as" |
| 放映 | "play" |

**起始版本：** 26.0.0

### OpenFileBoost\_Options

```cpp
typedef struct OpenFileBoost_Options OpenFileBoost_Options
```

**描述**

应用支持预加载的文件信息和文件类型数量，用于向系统注册一批支持预加载的文件类型。

**起始版本：** 26.0.0

### OpenFileBoost\_SupportFile

```cpp
typedef struct OpenFileBoost_SupportFile OpenFileBoost_SupportFile
```

**描述**

应用支持预加载的文件信息，用于描述一组符合预加载条件的文件特征。 开发者可以使用[HMS\_Preview\_OpenFileBoost\_SupportFileCreate](openfileboost_preview.md#hms_preview_openfileboost_supportfilecreate)创建该结构体，配置哪些类型的文件可以被系统预加载。

**起始版本：** 26.0.0

### CacheKey

```cpp
typedef struct CacheKey CacheKey
```

**描述**

开发者在序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)和反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)调用[WriteFunc](openfileboost_preview.md#writefunc)和[ReadFunc](openfileboost_preview.md#readfunc)时，传入的key相关数据结构的对外声明。

**起始版本：** 6.1.0(23)

### SerializeFunc

```cpp
typedef FileCacheBoost_CbErrCode(*SerializeFunc) (const void *object, WriteFunc writeFunc, struct CacheKey *key)
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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode) | 函数执行结果。  函数执行成功则返回FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS。  函数执行失败则返回FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE。  其他错误详见[FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)。 |

### WriteFunc

```cpp
typedef FileCacheBoost_ErrCode(*WriteFunc) (const void *buffer, size_t bufferLen, struct CacheKey *key)
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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  如果函数执行成功，则返回FILE\_CACHE\_BOOST\_SUCCESS。  如果因数据对象内存被释放，导致写入缓存对象任务无法执行则返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### DeserializeFunc

```cpp
typedef FileCacheBoost_CbErrCode(*DeserializeFunc) (void **object, ReadFunc readFunc, struct CacheKey *key)
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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode) | 函数执行结果。  函数执行成功则返回FILE\_CACHE\_BOOST\_CALLBACK\_SUCCESS。  函数执行失败则返回FILE\_CACHE\_BOOST\_CALLBACK\_FAILURE。  其他错误详见[FileCacheBoost\_CbErrCode](openfileboost_preview.md#filecacheboost_cberrcode)。 |

### ReadFunc

```cpp
typedef FileCacheBoost_ErrCode(*ReadFunc) (void *buffer, size_t *bufferLen, struct CacheKey *key)
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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  如果函数执行成功，则返回FILE\_CACHE\_BOOST\_SUCCESS。  如果因数据对象内存被释放，导致读取缓存对象任务无法执行则返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

## 枚举类型说明

### OpenFileBoost\_AppState

```cpp
enum OpenFileBoost_AppState
```

**描述**

App状态，用于指示App当前是否允许系统推荐预加载文件。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0 | 当前允许推荐预加载文件。 |
| OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1 | 当前不允许推荐预加载文件。 |
| OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2 | 这次注册期间永远不允许推荐预加载文件。 |
| OPEN\_FILE\_BOOST\_APP\_STATE\_EXCEL\_TRANSACTION = 3 | 应用程序正在执行与excel文件相关的独占任务。**起始版本：** 26.0.0 |

### OpenFileBoost\_CbErrCode

```cpp
enum OpenFileBoost_CbErrCode
```

**描述**

回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义，它用于App向系统返回回调函数执行结果。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0 | 回调函数执行成功。 |
| OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000 | 回调函数执行失败。 |

### OpenFileBoost\_ErrCode

```cpp
enum OpenFileBoost_ErrCode
```

**描述**

文件打开加速的错误码定义。

**起始版本：** 5.0.3(15)

| 枚举值 | 描述 |
| --- | --- |
| OPEN\_FILE\_BOOST\_SUCCESS = 0 | 成功。 |
| OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201 | 未授权。 |
| OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401 | 无效输入参数。 |
| OPEN\_FILE\_BOOST\_CAPABILITY\_NOT\_SUPPORTED = 801 | 该设备不支持此API。**起始版本：** 26.0.0 |
| OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001 | 内部错误。 |
| OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002 | 传入的缓冲区的长度不足。 |
| OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003 | 服务不可用。 |
| OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004 | 内存不足。 |

### FileScanBoost\_CbErrCode

```cpp
enum FileScanBoost_CbErrCode
```

**描述**

文件扫描回调特定错误码的枚举。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| FILE\_SCAN\_BOOST\_CALLBACK\_SUCCESS = 0 | 回调成功完成。 |
| FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_INTERNAL = 1017240001 | 回调内部错误。 |
| FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017240002 | 不支持扫描此文件类型。 |

### FileScanBoost\_ErrCode

```cpp
enum FileScanBoost_ErrCode
```

**描述**

文件扫描加速功能返回的所有错误码的枚举。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| FILE\_SCAN\_BOOST\_SUCCESS = 0 | 操作成功完成。 |
| FILE\_SCAN\_BOOST\_ERROR\_PERMISSION\_NOT\_GRANTED = 201 | 未授予文件预加载权限。 |
| FILE\_SCAN\_BOOST\_ERROR\_INVALID\_PARAM = 401 | 提供的参数无效。 |
| FILE\_SCAN\_BOOST\_ERROR\_CAPABILITY\_NOT\_SUPPORTED = 801 | 该设备不支持此API。 |
| FILE\_SCAN\_BOOST\_ERROR\_INTERNAL = 1017230001 | 内部系统错误。 |
| FILE\_SCAN\_BOOST\_ERROR\_NOT\_REGISTERED = 1017230002 | 未注册扫描能力回调。 |
| FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED = 1017230003 | 扫描能力回调已注册。 |
| FILE\_SCAN\_BOOST\_ERROR\_SERVICE\_UNAVAILABLE = 1017230004 | 服务不可用。 |
| FILE\_SCAN\_BOOST\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017230005 | 文件格式不支持。 |

### FileScanBoost\_ScanState

```cpp
enum FileScanBoost_ScanState
```

**描述**

文件扫描后，扫描成功状态、扫描进程错误状态、扫描文件错误状态的枚举。

**起始版本：** 26.0.0

| 枚举值 | 描述 |
| --- | --- |
| FILE\_SCAN\_BOOST\_SCAN\_STATE\_SUCCESS = 0 | 扫描成功完成。 |
| FILE\_SCAN\_BOOST\_SCAN\_STATE\_PROCESS\_ERROR = 1 | 扫描操作发生错误。 |
| FILE\_SCAN\_BOOST\_SCAN\_STATE\_FILE\_ERROR = 2 | 文件无法预加载。 |

### FileCacheBoost\_CbErrCode

```cpp
enum FileCacheBoost_CbErrCode
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

```cpp
enum FileCacheBoost_ErrCode
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

### HMS\_Preview\_FileBoost\_IsSupported()

```cpp
bool HMS_Preview_FileBoost_IsSupported (void)
```

**描述**

查询当前设备是否支持文件打开加速功能。建议使用本接口检查，确认设备支持文件打开加速功能后，再使用其他文件打开加速接口如[HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload)、[HMS\_Preview\_FileScanBoost\_RegisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_registerfilescan)等。

**起始版本：** 26.0.0

**返回：**

如果当前设备支持文件打开加速功能，则返回true；否则返回false。

### HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo()

```cpp
OpenFileBoost_ErrCode HMS_OpenFileBoost_GetFdFromPreloadFileInfo (void * fileInfo, int32_t * fd)
```

**描述**

获取文件描述符信息。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 系统向App推荐的预加载文件信息。 |
| fd | 输出参数，预加载文件的文件描述符信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS。  如果失败将返回具体错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo()

```cpp
OpenFileBoost_ErrCode HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo (void * fileInfo, char * sandboxPath, int32_t pathLen)
```

**描述**

获取沙箱路径信息。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileInfo | 系统向App推荐的预加载文件信息。 |
| sandboxPath | 输出参数，预加载文件的沙箱路径信息，App应该传递一个指向一块有效内存区域的指针，系统将向其中填充沙箱路径信息。 |
| pathLen | 用于填充沙箱路径的内存区域的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS。  如果传入的内存缓冲区太小，系统将返回OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER。  其他错误详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_OpenFileBoost\_NotifyPreloadHit()

```cpp
OpenFileBoost_ErrCode HMS_OpenFileBoost_NotifyPreloadHit (int32_t fd, char * sandboxPath, int32_t pathLen)
```

**描述**

当用户打开预加载文件时，App调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| fd | 命中文件的文件描述符信息。 |
| sandboxPath | 命中文件的沙箱路径。 |
| pathLen | 沙箱路径的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS。  如果失败将返回具体错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_OpenFileBoost\_RegisterFilePreload()

```cpp
OpenFileBoost_ErrCode HMS_OpenFileBoost_RegisterFilePreload (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload)
```

**描述**

应用使用本接口向系统注册文件预加载回调。

后续，系统预测用户可能打开的文件时，先调用queryAppState来向应用查询当前是否可以推荐预加载的文件。如果应用通过queryAppState返回允许推荐，则系统通过调用filePreload推荐一个文件，供应用进行预加载操作。

在某些特定情况下，例如系统可用内存不足、有其他文件更有可能被用户打开、或其他不适合文件保持预加载状态的条件发生，系统会通过调用cancelFilePreload来取消部分文件的预加载。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 5.0.3(15)

**参数:**

| 名称 | 描述 |
| --- | --- |
| queryAppState | App状态查询回调函数，在通知预加载之前先调用该回调函数查询当前是否允许推荐预加载文件。 |
| filePreload | 文件预加载回调，系统预测用户可能打开的文件，并通过该回调函数通知调用者。 |
| cancelFilePreload | 取消文件预加载回调，比如系统可用内存不足时系统会通知调用方取消文件的预加载。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS。  如果失败将返回具体错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_OpenFileBoost\_UnregisterFilePreload()

```cpp
OpenFileBoost_ErrCode HMS_OpenFileBoost_UnregisterFilePreload (void)
```

**描述**

取消注册预加载回调。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 5.0.3(15)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果执行成功则返回OPEN\_FILE\_BOOST\_SUCCESS。  如果失败将返回具体错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_RegisterFileScan()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_RegisterFileScan (HMS_Preview_FileScanBoost_OnFileScan fileScanCb, FileScanBoost_ScanOption *option)
```

**描述**

使用扩展名过滤方式注册多文件类型的回调函数。在上一次注册结果注销之前，请勿重复注册。重复注册将返回错误码FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED，且仅首次注册的信息生效。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileScanCb | 要注册的回调函数。 |
| option | 指向包含支持文件类型的扫描选项实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ReportScanResult()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ReportScanResult (const char *path, uint32_t pathLen, FileScanBoost_ScanResult *result)
```

**描述**

完成扫描后，报告文件扫描操作的扫描结果。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| path | 被扫描的文件路径。 |
| pathLen | 文件路径字符串的长度。最大路径长度为PATH\_MAX。 |
| result | 指向包含状态和指标的扫描结果实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanOptionAddSupportFile()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionAddSupportFile (FileScanBoost_ScanOption *option, const char *suffix, uint32_t suffixLen)
```

**描述**

在注册扫描接口的扫描选项参数中添加支持的文件类型。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| option | 指向扫描选项实例的指针。 |
| suffix | 文件扩展名，例如 "xlsx"。 |
| suffixLen | 文件扩展名的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanOptionCreate()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionCreate (FileScanBoost_ScanOption **outOption)
```

**描述**

创建[FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption)实例。应用使用完毕后必须调用[HMS\_Preview\_FileScanBoost\_ScanOptionDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanoptiondestroy)来释放该实例。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| outOption | 指向接收所创建选项实例的指针。可参见[FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanOptionDestroy()

```cpp
void HMS_Preview_FileScanBoost_ScanOptionDestroy (FileScanBoost_ScanOption *option)
```

**描述**

销毁[FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption)实例。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| option | 指向要销毁的选项实例的指针。可参见[FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption)。 |

### HMS\_Preview\_FileScanBoost\_ScanResultCreate()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultCreate (FileScanBoost_ScanResult **outResult)
```

**描述**

创建[FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult)实例。应用使用完毕后必须调用[HMS\_Preview\_FileScanBoost\_ScanResultDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanresultdestroy)来释放该实例。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| outResult | 指向接收所创建结果实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。请参见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanResultDestroy()

```cpp
void HMS_Preview_FileScanBoost_ScanResultDestroy (FileScanBoost_ScanResult *result)
```

**描述**

销毁[FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult)实例。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 指向要销毁的结果实例的指针。 |

### HMS\_Preview\_FileScanBoost\_ScanResultSetMaxAtomicTime()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime (FileScanBoost_ScanResult *result, int64_t maxAtomicTime)
```

**描述**

在文件扫描结果中设置最大原子时间，单位为ms。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 指向扫描结果实例的指针。 |
| maxAtomicTime | 扫描该文件的最大原子时间，单位为ms。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanResultSetMemSize()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMemSize (FileScanBoost_ScanResult *result, int64_t memSize)
```

**描述**

在文件扫描结果中设置内存大小，单位为MB。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 指向扫描结果实例的指针。 |
| memSize | 扫描该文件消耗的内存，单位为MB。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_ScanResultSetState()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetState (FileScanBoost_ScanResult *result, FileScanBoost_ScanState state)
```

**描述**

在结果中设置扫描状态。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 指向扫描结果实例的指针。 |
| state | 扫描完成状态。扫描状态请参见[FileScanBoost\_ScanState](openfileboost_preview.md#filescanboost_scanstate)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_FileScanBoost\_UnregisterFileScan()

```cpp
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_UnregisterFileScan (void)
```

**描述**

移除已注册的文件扫描回调函数。注销文件扫描后，该应用程序所有未报告扫描结果的扫描任务均失效。同时，在发起注销之前，应用程序需要清理未完成的扫描任务。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) | 函数执行结果。  如果函数执行成功，返回FILE\_SCAN\_BOOST\_SUCCESS。  如果函数执行失败，返回具体错误码。详见[FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoCreate (const char *path, uint32_t pathLen, const char *operation, uint32_t operationLen, OpenFileBoost_FileOperationInfo **outFileOperationInfo)
```

**描述**

创建[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| path | 文件路径。 |
| pathLen | 文件路径的长度。最大长度限制为PATH\_MAX。 |
| operation | 文件操作信息。 |
| operationLen | 文件操作信息的长度。最大长度限制为NAME\_MAX。 |
| outFileOperationInfo | 用于接收创建的[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_FileOperationInfoDestroy()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoDestroy (OpenFileBoost_FileOperationInfo *fileOperationInfo)
```

**描述**

销毁[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileOperationInfo | 指向要销毁的[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_IsEnabled()

```cpp
bool HMS_Preview_OpenFileBoost_IsEnabled (void)
```

**描述**

查询应用加速特性是否可用。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果加速特性可用，则返回true；否则返回false。 |

### HMS\_Preview\_OpenFileBoost\_NotifyFileOperation()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_NotifyFileOperation (OpenFileBoost_FileOperationInfo *fileOperationInfo)
```

**描述**

当用户对文件进行操作时，App调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| fileOperationInfo | 应用向系统传递的文件操作信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsAddSupportFile (OpenFileBoost_Options *options, const OpenFileBoost_SupportFile *supportFile)
```

**描述**

向[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)添加支持预加载的文件类型列表。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)的指针。 |
| supportFile | 指向要添加的[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_OptionsCreate()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsCreate (OpenFileBoost_Options **outOptions)
```

**描述**

创建一个空的[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options), 再使用[HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile](openfileboost_preview.md#hms_preview_openfileboost_optionsaddsupportfile)添加支持的文件类型。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| outOptions | 用于接收创建的[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_OptionsDestroy()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsDestroy (OpenFileBoost_Options *options)
```

**描述**

销毁[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| options | 指向要销毁的[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_RegisterFilePreloadWithOption()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload, OpenFileBoost_Options *options)
```

**描述**

注册预加载回调，允许应用传入支持预加载的文件信息。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| queryAppState | App状态查询回调函数，在通知预加载之前先调用该回调函数查询当前是否允许推荐预加载文件。 |
| filePreload | 文件预加载回调，系统预测用户可能打开的文件，并通过该回调函数通知应用。 |
| cancelFilePreload | 取消文件预加载回调，比如系统可用内存不足时系统会通知调用方取消文件的预加载。 |
| options | 预加载支持文件配置选项，用于定义哪些类型的文件可以被预加载。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_SupportFileCreate()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileCreate (const char *suffix, uint32_t suffixLen, uint64_t lowerLimitKb, uint64_t upperLimitKb, OpenFileBoost_SupportFile **outSupportFile)
```

**描述**

创建[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| suffix | 文件后缀名。 |
| suffixLen | 文件后缀名的长度。 |
| lowerLimitKb | 文件大小下限(KB)。 |
| upperLimitKb | 文件大小上限(KB)。 |
| outSupportFile | 用于接收创建的[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_OpenFileBoost\_SupportFileDestroy()

```cpp
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileDestroy (OpenFileBoost_SupportFile *supportFile)
```

**描述**

销毁[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。使用示例详见[文件打开加速（C/C++）](../harmonyos-guides/preview-openfileboost.md)。

**起始版本：** 26.0.0

**参数:**

| 名称 | 描述 |
| --- | --- |
| supportFile | 指向要销毁的[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) | 函数执行结果。  如果函数执行成功，返回OPEN\_FILE\_BOOST\_SUCCESS。  如果函数执行失败，返回特定的错误码。详见[OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode)。 |

### HMS\_Preview\_FileCacheBoost\_IsSupported()

```cpp
bool HMS_Preview_FileCacheBoost_IsSupported (void)
```

**描述**

查询当前设备是否支持文件缓存加速功能。建议使用本接口检查，确认设备支持文件缓存加速功能后，再使用其他文件缓存加速接口如[HMS\_FileCacheBoost\_Init](openfileboost_preview.md#hms_filecacheboost_init)等。

**起始版本：** 26.0.0

**返回：**

如果当前设备支持文件缓存加速功能，则返回true；否则返回false。

### HMS\_FileCacheBoost\_Init()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_Init (const char * path, size_t pathLen, uint32_t cacheUpperLimitMb, const char * dbName, size_t dbNameLen)
```

**描述**

初始化缓存路径、缓存容量上限和数据库名称。该函数用于配置缓存文件的存储目录以及缓存最大容量。当系统检测到缓存总量超出设定上限后，将根据缓存淘汰策略进行容量管控，删除相应的缓存以释放空间。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_DIR：传入的路径无效，系统无法创建。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_AddObjectByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_AddObjectByKey (const uint8_t * key, size_t keyLen, const uint8_t * data, size_t dataLen, uint32_t weight)
```

**描述**

创建并添加一个缓存对象至文件缓存。 该函数通过指定的唯一标识符 (key) 将数据缓存至文件缓存系统中，便于后续快速访问。

建议开发者合理设计和管理key值，确保其在不同上下文中的唯一性和准确性。 当缓存不再需要时，推荐开发者主动调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除对应的缓存项，以避免资源浪费。 若不主动删除，系统将在缓存容量不足时，依据系统策略进行清除。

开发者若想要对key对应的缓存内容做修改，需要先调用[HMS\_FileCacheBoost\_RemoveObjectByKey](openfileboost_preview.md#hms_filecacheboost_removeobjectbykey)删除之前的key，再重新创建和添加。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST：key值已经存在。  FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放，导致创建缓存对象任务无法执行。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT：添加的缓存大小大于缓存容量上限。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_GetObjectByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_GetObjectByKey (const uint8_t * key, size_t keyLen, uint8_t ** data, size_t * dataLen )
```

**描述**

根据指定的key查询缓存对象，若存在，则从磁盘中加载缓存对象的内容。调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |
| data | 出参，缓存对象的内容。开发者需确保传入参数非空。 |
| dataLen | 缓存对象内容的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。  FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存被释放，导致获取缓存对象任务无法执行。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_FreeObject()

```cpp
void HMS_FileCacheBoost_FreeObject (uint8_t * data)
```

**描述**

释放调用[HMS\_FileCacheBoost\_GetObjectByKey](openfileboost_preview.md#hms_filecacheboost_getobjectbykey)或[HMS\_FileCacheBoost\_GetSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_getserialobjectbykey)分配的内存，建议开发者不再使用该内存时，及时调用此函数进行释放，避免造成内存泄漏。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| data | 需要释放的内存数据。 |

### HMS\_FileCacheBoost\_AddSerialObjectByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_AddSerialObjectByKey (const uint8_t * key, size_t keyLen, SerializeFunc func, const void * object, uint32_t weight )
```

**描述**

创建一个复杂类型对象的缓存项，通过传入自定义的序列化函数[SerializeFunc](openfileboost_preview.md#serializefunc)对该象进行序列化处理，以便将该对象存储至磁盘并支持后续恢复。

例如图像数据需要同时保存其元数据和像素数据，才能实现完整的缓存与读取过程。序列化和反序列化会占用内存，请开发者控制object大小，降低内存压力。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

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

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_KEY\_EXIST：key值已经存在。  FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放，导致创建缓存对象任务无法执行。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  FILE\_CACHE\_BOOST\_ERROR\_EXCEED\_LIMIT：添加的缓存大小大于缓存容量上限。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_GetSerialObjectByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_GetSerialObjectByKey (const uint8_t * key, size_t keyLen, DeserializeFunc func, void ** object )
```

**描述**

根据指定的key值获取复杂类型缓存对象，并通过传入的反序列化函数[DeserializeFunc](openfileboost_preview.md#deserializefunc)将其还原为原始数据，从而获得完整的对象内容。 调用该函数系统会分配一段内存用于存储缓存数据，作为出参返回给开发者，开发者需在使用完毕后调用[HMS\_FileCacheBoost\_FreeObject](openfileboost_preview.md#hms_filecacheboost_freeobject)显式释放该内存。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |
| func | 开发者实现的反序列化函数，于将已序列化的数据恢复为原始对象。 |
| object | 出参，缓存对象的内容。开发者需确保传入参数非空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。  FILE\_CACHE\_BOOST\_ERROR\_IO：发生I/O读写错误。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCELED：因数据对象内存缓存被释放，导致获取缓存对象任务无法执行。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_CancelOngoingIOByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_CancelOngoingIOByKey (const uint8_t * key, size_t keyLen )
```

**描述**

取消key对应的缓存对象当前正在进行的I/O操作。当开发者需要释放数据对象时，应调用本函数，防止有其他线程对该数据对象进行添加缓存对象或者获取缓存对象的操作。若该对象正处于缓存过程中，则操作将被中止；若已缓存完成，则此函数不做任何处理。

当该函数返回 FILE\_CACHE\_BOOST\_SUCCESS，开发者可以立即释放数据对象；当返回FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED，表示当前没有正在执行的 key 需要被取消，开发者需要确认该 key 对应的动作执行完成或无需执行后再释放数据对象。

例如当一个线程尝试删除数据对象的同时，有其他线程对其进行[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)操作，调用本函数可确保缓存对象的安全性，避免引发数据竞争问题。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：缓存完成和I/O取消成功，开发者可以立即释放数据对象。  FILE\_CACHE\_BOOST\_ERROR\_IO\_CANCEL\_FAILED：I/O取消失败，表示当前没有正在执行的key需要被取消，开发者需要确认该key对应的动作执行完成或无需执行后再释放数据对象。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入的参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_RemoveObjectByKey()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_RemoveObjectByKey (const uint8_t * key, size_t keyLen )
```

**描述**

根据指定的key删除对应的缓存对象。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**参数:**

| 名称 | 描述 |
| --- | --- |
| key | 缓存对象的key。 |
| keyLen | key的缓冲区长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_KEY\_NOT\_FOUND：key值不存在。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  FILE\_CACHE\_BOOST\_ERROR\_INVALID\_PARAM：传入参数无效。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |

### HMS\_FileCacheBoost\_ClearAllCache()

```cpp
FileCacheBoost_ErrCode HMS_FileCacheBoost_ClearAllCache (void )
```

**描述**

清理所有的缓存对象。该函数会释放通过[HMS\_FileCacheBoost\_AddObjectByKey](openfileboost_preview.md#hms_filecacheboost_addobjectbykey)和[HMS\_FileCacheBoost\_AddSerialObjectByKey](openfileboost_preview.md#hms_filecacheboost_addserialobjectbykey)创建的所有缓存对象。使用示例详见[通用文件缓存加速（C/C++）](../harmonyos-guides/preview-filecacheboost.md)。

**起始版本：** 6.1.0(23)

**返回：**

| 类型 | 说明 |
| --- | --- |
| [FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode) | 函数执行结果。  FILE\_CACHE\_BOOST\_SUCCESS：执行成功。  FILE\_CACHE\_BOOST\_ERROR\_NOT\_INITIALIZED：未初始化。  其他错误详见[FileCacheBoost\_ErrCode](openfileboost_preview.md#filecacheboost_errcode)。 |
