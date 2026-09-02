---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder-base-h
title: avtranscoder_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avtranscoder_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2d1f69ba81926a764189f75b6d27a0a502e77d69d76314213d9dd8ac316a763f
---

## 概述

定义了媒体AVTranscoder的结构体和枚举。

**引用文件：** <multimedia/player\_framework/avtranscoder\_base.h>

**库：** libavtranscoder.so

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**相关模块：** [AVTranscoder](capi-avtranscoder.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVTranscoder](capi-avtranscoder-oh-avtranscoder.md) | OH\_AVTranscoder | 初始化AVTranscoder。 |
| [OH\_AVTranscoder\_Config](capi-avtranscoder-oh-avtranscoder-config.md) | OH\_AVTranscoder\_Config | 初始化AVTranscoder\_Config。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVTranscoder\_State](capi-avtranscoder-base-h.md#oh_avtranscoder_state) | OH\_AVTranscoder\_State | 转码状态。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVTranscoder\_OnStateChange)(OH\_AVTranscoder \*transcoder, OH\_AVTranscoder\_State state, void \*userData)](capi-avtranscoder-base-h.md#oh_avtranscoder_onstatechange) | OH\_AVTranscoder\_OnStateChange | 转码过程的状态回调函数。 |
| [typedef void (\*OH\_AVTranscoder\_OnError)(OH\_AVTranscoder \*transcoder, int32\_t errorCode, const char \*errorMsg, void \*userData)](capi-avtranscoder-base-h.md#oh_avtranscoder_onerror) | OH\_AVTranscoder\_OnError | 转码过程中错误事件的回调函数。 |
| [typedef void (\*OH\_AVTranscoder\_OnProgressUpdate)(OH\_AVTranscoder \*transcoder, int32\_t progress, void \*userData)](capi-avtranscoder-base-h.md#oh_avtranscoder_onprogressupdate) | OH\_AVTranscoder\_OnProgressUpdate | 回调转码进度更新时调用。 |

## 枚举类型说明

### OH\_AVTranscoder\_State

```c
enum OH_AVTranscoder_State
```

**描述**

转码状态。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| AVTRANSCODER\_PREPARED = 1 | 准备 |
| AVTRANSCODER\_STARTED = 2 | 开始 |
| AVTRANSCODER\_PAUSED = 3 | 暂停 |
| AVTRANSCODER\_CANCELLED = 4 | 取消 |
| AVTRANSCODER\_COMPLETED = 5 | 完成 |

## 函数说明

### OH\_AVTranscoder\_OnStateChange()

```c
typedef void (*OH_AVTranscoder_OnStateChange)(OH_AVTranscoder *transcoder, OH_AVTranscoder_State state, void *userData)
```

**描述**

转码过程的状态回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVTranscoder](capi-avtranscoder-oh-avtranscoder.md) \*transcoder | OH\_AVTranscoder实例的指针。 |
| [OH\_AVTranscoder\_State](capi-avtranscoder-base-h.md#oh_avtranscoder_state) state | 转码状态，详细说明请参见[OH\_AVTranscoder\_State](capi-avtranscoder-base-h.md#oh_avtranscoder_state)。 |
| void \*userData | 用户特定数据的指针。 |

### OH\_AVTranscoder\_OnError()

```c
typedef void (*OH_AVTranscoder_OnError)(OH_AVTranscoder *transcoder, int32_t errorCode, const char *errorMsg,void *userData)
```

**描述**

转码过程中错误事件的回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVTranscoder](capi-avtranscoder-oh-avtranscoder.md) \*transcoder | OH\_AVTranscoder实例的指针。 |
| int32\_t errorCode | 错误码。  AV\_ERR\_NO\_MEMORY：无内存，取值为1。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不允许，取值为2。  AV\_ERR\_INVALID\_VAL：参数检查失败，取值为3。  AV\_ERR\_IO：IO错误，取值为4。  AV\_ERR\_INVALID\_STATE：当前状态不支持此操作，取值为8。  AV\_ERR\_UNSUPPORT：不支持的接口，取值为9。 |
| const char \*errorMsg | 错误消息。 |
| void \*userData | 用户特定数据的指针。 |

### OH\_AVTranscoder\_OnProgressUpdate()

```c
typedef void (*OH_AVTranscoder_OnProgressUpdate)(OH_AVTranscoder *transcoder, int32_t progress, void *userData)
```

**描述**

回调转码进度更新时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVTranscoder](capi-avtranscoder-oh-avtranscoder.md) \*transcoder | OH\_AVTranscoder实例的指针。 |
| int32\_t progress | 转码百分比进度。 |
| void \*userData | 用户特定数据的指针。 |
