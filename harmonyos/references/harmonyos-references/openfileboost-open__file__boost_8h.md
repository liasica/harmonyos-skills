---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/openfileboost-open__file__boost_8h
title: open_file_boost.h
category: harmonyos-references
scraped_at: 2026-04-28T08:18:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:79f9fcbc14f58513fd161ea55959ba352031b67dc68ad2bb4dad893286313a6a
---

## 概述

PC/2in1

声明文件打开加速的API集合。

**引用文件：** <PreviewKit/open\_file\_boost.h>

**库：** libopen\_file\_boost.so

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.3(15)

**相关模块：** [Preview](openfileboost_preview.md)

## 汇总

PC/2in1

### 宏定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [MAX\_BUFFER\_LENGTH](openfileboost_preview.md#max_buffer_length) 1024 | 沙箱路径最大长度。 |

### 类型定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| typedef [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate)(\*[HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate)) (void) | 系统查询app状态的回调函数定义，该函数在调用[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)推荐文件之前先回调app。该函数用于系统向app查询当前是否允许推荐文件给app。如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。 |
| typedef [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode)(\*[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)) (void\* fileInfo) | 系统向应用推荐或取消推荐预加载文件的回调函数定义。 系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) {  OPEN\_FILE\_BOOST\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201,  OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401,  OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001,  OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002,  OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003,  OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004  } | 文件打开加速的错误码定义。 |
| [OpenFileBoost\_CbErrCode](openfileboost_preview.md#openfileboost_cberrcode) {  OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,  OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000  } | 回调函数[HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload)的错误码定义， 它用于app向系统返回回调函数执行结果。 |
| [OpenFileBoost\_AppState](openfileboost_preview.md#openfileboost_appstate) {  OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,  OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,  OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2  } | app状态，用于指示app当前是否允许系统推荐预加载文件。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getfdfrompreloadfileinfo) (void\* fileInfo, int32\_t\* fd) | 获取文件描述符信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](openfileboost_preview.md#hms_openfileboost_getsandboxpathfrompreloadfileinfo) (void\* fileInfo, char\* sandboxPath, int32\_t pathLen) | 获取沙箱路径信息。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_RegisterFilePreload](openfileboost_preview.md#hms_openfileboost_registerfilepreload) ([HMS\_OpenFileBoost\_QueryAppState](openfileboost_preview.md#hms_openfileboost_queryappstate) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](openfileboost_preview.md#hms_openfileboost_onfilepreload) cancelFilePreload) | 注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_UnregisterFilePreload](openfileboost_preview.md#hms_openfileboost_unregisterfilepreload) (void) | 取消注册预加载回调。 |
| [OpenFileBoost\_ErrCode](openfileboost_preview.md#openfileboost_errcode) [HMS\_OpenFileBoost\_NotifyPreloadHit](openfileboost_preview.md#hms_openfileboost_notifypreloadhit) (int32\_t fd, char\* sandboxPath, int32\_t pathLen) | 当用户打开预加载文件时，app调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。 |
