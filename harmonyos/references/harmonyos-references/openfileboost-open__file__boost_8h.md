---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-open__file__boost_8h
title: open_file_boost.h
breadcrumb: API参考 > 应用服务 > Preview Kit（文件预览服务） > C API > 头文件和结构体 > 头文件 > open_file_boost.h
category: harmonyos-references
scraped_at: 2026-09-02T15:03:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:be6a9b08620140af34c5e4478cc1aa0ee5ce3e087f2947ba044b1510f548ef2e
---

## 概述

声明文件打开加速的API集合。

**引用文件：** <PreviewKit/open\_file\_boost.h>

**库：** libopen\_file\_boost.so

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.3(15)

**相关模块：** [Preview](openfileboost_preview.md)

## 汇总

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [MAX\_BUFFER\_LENGTH](openfileboost_preview.md#max_buffer_length) 1024 | 沙箱路径最大长度。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate)(\*[HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate)) (void) | 系统查询App状态的回调函数定义，该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先回调App。该函数用于系统向App查询当前是否允许推荐文件给App。如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，App返回特定枚举值拒绝预加载。 |
| typedef [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode)(\*[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)) (void\* fileInfo) | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 系统预测用户可能打开的文件，并通过该回调函数通知App，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知App取消某些文件的预加载。 |
| typedef struct [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) | 文件扫描选项配置的不透明类型。 |
| typedef struct [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) | 文件扫描结果的不透明类型。 |
| typedef [FileScanBoost\_CbErrCode](openfileboost_preview.md#filescanboost_cberrcode)(\* [HMS\_Preview\_FileScanBoost\_OnFileScan](openfileboost_preview.md#hms_preview_filescanboost_onfilescan)) (int32\_t fd, const char \*path, uint32\_t pathLen) | 文件扫描回调通知的函数指针类型。 系统调用此回调来发送扫描任务。此回调方法与扫描任务执行是异步的， 应用程序应在收到扫描任务后立即返回回调返回值，而不应阻塞回调。 并且扫描任务完成后的最终结果应使用[HMS\_Preview\_FileScanBoost\_ReportScanResult](openfileboost_preview.md#hms_preview_filescanboost_reportscanresult)报告。 |
| typedef struct [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) | 应用支持预加载的文件信息，用于描述一组符合预加载条件的文件特征。 开发者可以使用[HMS\_Preview\_OpenFileBoost\_SupportFileCreate](openfileboost_preview.md#hms_preview_openfileboost_supportfilecreate)创建该结构体， 配置哪些类型的文件可以被系统预加载。 |
| typedef struct [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) | 应用支持预加载的文件信息和文件类型数量，用于向系统注册一批支持预加载的文件类型。 |
| typedef struct [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) | 应用向系统传递的文件操作信息。 开发者可传递文件路径和该文件的操作信息，操作信息包括：  打开："open"，  关闭："close"，  导入/加载："import"，  导出："export"，  TAB隐藏："tab\_hidden"，  TAB可见"tab\_visible"，  保存："save"，  新建："create"，  云上传："upload"，  云下载："download"，  共享："share"，  打印："print"，  另存为："save\_as"，  放映："play"。  开发者可以使用[HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfocreate)函数创建此结构体。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) {  OPEN\_FILE\_BOOST\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201,  OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401,  OPEN\_FILE\_BOOST\_CAPABILITY\_NOT\_SUPPORTED = 801,  OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001,  OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002,  OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003,  OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004  } | 文件打开加速的错误码定义。 |
| [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode) {  OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000  } | 回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义， 它用于App向系统返回回调函数执行结果。 |
| [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate) {  OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,  OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,  OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2,  OPEN\_FILE\_BOOST\_APP\_STATE\_EXCEL\_TRANSACTION = 3 } | App状态，用于指示App当前是否允许系统推荐预加载文件。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) {  FILE\_SCAN\_BOOST\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_ERROR\_PERMISSION\_NOT\_GRANTED = 201,  FILE\_SCAN\_BOOST\_ERROR\_INVALID\_PARAM = 401,  FILE\_SCAN\_BOOST\_ERROR\_CAPABILITY\_NOT\_SUPPORTED = 801,  FILE\_SCAN\_BOOST\_ERROR\_INTERNAL = 1017230001,  FILE\_SCAN\_BOOST\_ERROR\_NOT\_REGISTERED = 1017230002,  FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED = 1017230003,  FILE\_SCAN\_BOOST\_ERROR\_SERVICE\_UNAVAILABLE = 1017230004,  FILE\_SCAN\_BOOST\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017230005  } | 文件扫描加速功能返回的所有错误码的枚举。 |
| [FileScanBoost\_CbErrCode](openfileboost_preview.md#filescanboost_cberrcode) { FILE\_SCAN\_BOOST\_CALLBACK\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_INTERNAL = 1017240001,  FILE\_SCAN\_BOOST\_CALLBACK\_ERROR\_FORMAT\_NOT\_SUPPORTED = 1017240002 } | 文件扫描回调特定错误码的枚举。 |
| [FileScanBoost\_ScanState](openfileboost_preview.md#filescanboost_scanstate) { FILE\_SCAN\_BOOST\_SCAN\_STATE\_SUCCESS = 0,  FILE\_SCAN\_BOOST\_SCAN\_STATE\_PROCESS\_ERROR = 1,  FILE\_SCAN\_BOOST\_SCAN\_STATE\_FILE\_ERROR = 2 } | 文件扫描后扫描状态的枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo) (void\* fileInfo, int32\_t\* fd) | 获取文件描述符信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo) (void\* fileInfo, char\* sandboxPath, int32\_t pathLen) | 获取沙箱路径信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload) ([HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) cancelFilePreload) | 注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_UnregisterFilePreload](openfileboost_preview.md#hms_openfileboost_unregisterfilepreload) (void) | 取消注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_NotifyPreloadHit](openfileboost_preview.md#hms_openfileboost_notifypreloadhit) (int32\_t fd, char\* sandboxPath, int32\_t pathLen) | 当用户打开预加载文件时，App调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanOptionCreate](openfileboost_preview.md#hms_preview_filescanboost_scanoptioncreate) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*\*outOption) | 创建FileScanBoost\_ScanOption实例。 |
| void [HMS\_Preview\_FileScanBoost\_ScanOptionDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanoptiondestroy) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option) | 销毁FileScanBoost\_ScanOption实例。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanOptionAddSupportFile](openfileboost_preview.md#hms_preview_filescanboost_scanoptionaddsupportfile) ([FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option, const char \*suffix, uint32\_t suffixLen) | 向扫描选项添加支持的文件类型。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultCreate](openfileboost_preview.md#hms_preview_filescanboost_scanresultcreate) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*\*outResult) | 创建FileScanBoost\_ScanResult实例。 |
| void [HMS\_Preview\_FileScanBoost\_ScanResultDestroy](openfileboost_preview.md#hms_preview_filescanboost_scanresultdestroy) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result) | 销毁FileScanBoost\_ScanResult实例。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetState](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetstate) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, [FileScanBoost\_ScanState](openfileboost_preview.md#filescanboost_scanstate) state) | 在结果中设置扫描状态。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetMaxAtomicTime](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetmaxatomictime) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, int64\_t maxAtomicTime) | 在结果中设置最大原子时间。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ScanResultSetMemSize](openfileboost_preview.md#hms_preview_filescanboost_scanresultsetmemsize) ([FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result, int64\_t memSize) | 在结果中设置内存大小。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_RegisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_registerfilescan) ([HMS\_Preview\_FileScanBoost\_OnFileScan](openfileboost_preview.md#hms_preview_filescanboost_onfilescan) fileScanCb, [FileScanBoost\_ScanOption](openfileboost_preview.md#filescanboost_scanoption) \*option) | 使用扩展名过滤方式注册多文件类型的回调函数。 在上一次注册结果注销之前，请勿重复注册。 重复注册将返回错误码[FILE\_SCAN\_BOOST\_ERROR\_ALREADY\_REGISTERED](openfileboost_preview.md)， 且仅首次注册的信息生效。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_UnregisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_unregisterfilescan) (void) | 移除已注册的文件扫描回调函数。注意，注销意味着该应用程序所有未报告扫描结果的扫描任务均失效。 同时，在发起注销之前，应用程序需要清理未完成的扫描任务。 |
| [FileScanBoost\_ErrCode](openfileboost_preview.md#filescanboost_errcode) [HMS\_Preview\_FileScanBoost\_ReportScanResult](openfileboost_preview.md#hms_preview_filescanboost_reportscanresult) (const char \*path, uint32\_t pathLen, [FileScanBoost\_ScanResult](openfileboost_preview.md#filescanboost_scanresult) \*result) | 报告文件扫描操作的完成结果。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_SupportFileCreate](openfileboost_preview.md#hms_preview_openfileboost_supportfilecreate) (const char \*suffix, uint32\_t suffixLen, uint64\_t lowerLimitKb, uint64\_t upperLimitKb, [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*\*outSupportFile) | 创建[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_SupportFileDestroy](openfileboost_preview.md#hms_preview_openfileboost_supportfiledestroy) ([OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*supportFile) | 销毁[OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsCreate](openfileboost_preview.md#hms_preview_openfileboost_optionscreate) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*\*outOptions) | 创建一个空的[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)。 使用[HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile](openfileboost_preview.md#hms_preview_openfileboost_optionsaddsupportfile)添加文件。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsAddSupportFile](openfileboost_preview.md#hms_preview_openfileboost_optionsaddsupportfile) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options, const [OpenFileBoost\_SupportFile](openfileboost_preview.md#openfileboost_supportfile) \*supportFile) | 向[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)添加支持预加载的文件类型。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_OptionsDestroy](openfileboost_preview.md#hms_preview_openfileboost_optionsdestroy) ([OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options) | 销毁[OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_RegisterFilePreloadWithOption](openfileboost_preview.md#hms_preview_openfileboost_registerfilepreloadwithoption) (HMS\_OpenFileBoost\_QueryAppState queryAppState, HMS\_OpenFileBoost\_OnFilePreload filePreload, HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload, [OpenFileBoost\_Options](openfileboost_preview.md#openfileboost_options) \*options) | 注册预加载回调，允许应用传入支持预加载的文件信息。 |
| bool [HMS\_Preview\_FileBoost\_IsSupported](openfileboost_preview.md#hms_preview_fileboost_issupported) (void) | 查询当前设备是否支持文件打开加速功能。建议开发者在使用文件打开加速功能之前，先调用本接口检查当前设备是否支持文件打开加速功能。确认支持后再使用其他文件打开加速接口如[HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload)、[HMS\_Preview\_FileScanBoost\_RegisterFileScan](openfileboost_preview.md#hms_preview_filescanboost_registerfilescan)等。 |
| bool [HMS\_Preview\_OpenFileBoost\_IsEnabled](openfileboost_preview.md#hms_preview_openfileboost_isenabled) (void) | 查询应用加速特性是否使能。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_FileOperationInfoCreate](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfocreate) (const char \*path, uint32\_t pathLen, const char \*operation, uint32\_t operationLen, [OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*\*outFileOperationInfo) | 创建[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_FileOperationInfoDestroy](openfileboost_preview.md#hms_preview_openfileboost_fileoperationinfodestroy) ([OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*fileOperationInfo) | 销毁[OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo)。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_Preview\_OpenFileBoost\_NotifyFileOperation](openfileboost_preview.md#hms_preview_openfileboost_notifyfileoperation) ([OpenFileBoost\_FileOperationInfo](openfileboost_preview.md#openfileboost_fileoperationinfo) \*fileOperationInfo) | 当用户对文件进行操作时，App调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。 |
