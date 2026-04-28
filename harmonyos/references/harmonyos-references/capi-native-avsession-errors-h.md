---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-errors-h
title: native_avsession_errors.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avsession_errors.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5568a79c7314d19f52593e0dc575eb826ed15a73073e6f4fabbe0123e0de39ef
---

## 概述

PhonePC/2in1TabletTVWearable

提供播控错误码的定义。

**引用文件：** <multimedia/av\_session/native\_avsession\_errors.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AVSession\_ErrCode | 播控错误码。 |
| [AVSessionCallback\_Result](capi-native-avsession-errors-h.md#avsessioncallback_result) | AVSessionCallback\_Result | 定义音视频会话回调结果枚举。 |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMetadata\_Result | 播控元数据错误码。 |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQueueItem\_Result | 播放列表中单项的错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AVSession\_ErrCode

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_ErrCode
```

**描述**

播控错误码。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AV\_SESSION\_ERR\_SUCCESS = 0 | 操作成功。 |
| AV\_SESSION\_ERR\_INVALID\_PARAMETER = 401 | 参数检查失败。 |
| AV\_SESSION\_ERR\_SERVICE\_EXCEPTION = 6600101 | 会话服务端异常。 |
| AV\_SESSION\_ERR\_CODE\_SESSION\_NOT\_EXIST = 6600102 | 会话不存在。 |
| AV\_SESSION\_ERR\_CODE\_COMMAND\_INVALID = 6600105 | 无效会话命令。 |
| AV\_SESSION\_ERR\_CODE\_SESSION\_INACTIVE = 6600106 | 会话未激活。 |
| AV\_SESSION\_ERR\_CODE\_MESSAGE\_OVERLOAD = 6600107 | 命令&消息过载。 |
| AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST = 6600109 | 远端会话不存在。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_UNSPECIFIED = 6611000 | 投播控制器出现未知错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_REMOTE\_ERROR = 6611001 | 远端设备出现未知错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_BEHIND\_LIVE\_WINDOW = 6611002 | 加载位置超过投播视频的总进度。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_TIMEOUT = 6611003 | 投播控制器加载超时。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_RUNTIME\_CHECK\_FAILED = 6611004 | 运行时检查失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PLAYER\_NOT\_WORKING = 6611100 | 跨设备数据传输被锁定。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_SEEK\_MODE\_UNSUPPORTED = 6611101 | 不支持当前进度条模式。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_ILLEGAL\_SEEK\_TARGET = 6611102 | 不支持跳转位置越界或异常跳转模式。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PLAY\_MODE\_UNSUPPORTED = 6611103 | 不支持当前播放模式。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PLAY\_SPEED\_UNSUPPORTED = 6611104 | 不支持当前播放速度。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DEVICE\_MISSING = 6611105 | 媒体接收设备已离线，操作执行失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_INVALID\_PARAM = 6611106 | 参数无效，如播放地址非法。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_NO\_MEMORY = 6611107 | 内存分配失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_OPERATION\_NOT\_ALLOWED = 6611108 | 不允许进行当前操作。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_UNSPECIFIED = 6612000 | 未知的输入/输出错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_FAILED = 6612001 | 网络连接失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_TIMEOUT = 6612002 | 网络超时。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_INVALID\_HTTP\_CONTENT\_TYPE = 6612003 | HTTP请求头中的Content-Type字段不合法。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_BAD\_HTTP\_STATUS = 6612004 | HTTP服务器返回异常的HTTP响应状态码。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_FILE\_NOT\_FOUND = 6612005 | 文件不存在。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_PERMISSION = 6612006 | 缺少执行IO（输入/输出）操作的权限。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_CLEARTEXT\_NOT\_PERMITTED = 6612007 | 网络安全配置不允许此操作。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_POSITION\_OUT\_OF\_RANGE = 6612008 | 读取数据超出数据范围。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_CONTENTS = 6612100 | 缺少可播放的媒体资源。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_ERROR = 6612101 | 媒体无法被读取，如存储介质沾灰、出现划痕。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_BUSY = 6612102 | 资源正在使用。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_EXPIRED = 6612103 | 内容使用有效期已过。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_USE\_FORBIDDEN = 6612104 | 不允许使用请求的内容。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NOT\_VERIFIED = 6612105 | 无法验证授权内容的使用权限。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_EXHAUSTED\_ALLOWED\_USES = 6612106 | 该媒体内容的按需请求使用次数，已触达系统最大允许使用次数上限。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_PACKET\_SENDING\_FAILED = 6612107 | 本端向远端发送资源包失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PARSING\_UNSPECIFIED = 6613000 | 媒体内容解析过程中出现未明确具体类型的错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_MALFORMED = 6613001 | 媒体容器格式码流解析错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_MALFORMED = 6613002 | 媒体清单解析错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_UNSUPPORTED = 6613003 | 提取文件失败，不支持该媒体容器格式。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_UNSUPPORTED = 6613004 | 媒体无法读取，如介质有灰尘、划痕。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_UNSPECIFIED = 6614000 | 未知的解码错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_INIT\_FAILED = 6614001 | 解码器初始化失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_QUERY\_FAILED = 6614002 | 解码器查询失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_FAILED = 6614003 | 解码媒体样本时失败。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_EXCEEDS\_CAPABILITIES = 6614004 | 内容请求使用次数达最大限制。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_UNSUPPORTED = 6614005 | 解码不支持的内容格式。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_UNSPECIFIED = 6615000 | 音频渲染器出现未明确具体类型的异常错误。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_INIT\_FAILED = 6615001 | 音频渲染器初始化异常。  **起始版本：** 23 |
| AV\_SESSION\_ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_WRITE\_FAILED = 6615002 | 音频渲染器写数据异常。  **起始版本：** 23 |

### AVSessionCallback\_Result

PhonePC/2in1TabletTVWearable

```
1. enum AVSessionCallback_Result
```

**描述**

定义音视频会话回调结果枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AVSESSION\_CALLBACK\_RESULT\_SUCCESS = 0 | 会话的回调结果为执行成功。 |
| AVSESSION\_CALLBACK\_RESULT\_FAILURE = -1 | 会话的回调结果为执行失败。 |

### AVMetadata\_Result

PhonePC/2in1TabletTVWearable

```
1. enum AVMetadata_Result
```

**描述**

播控元数据错误码。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AVMETADATA\_SUCCESS = 0 | 接口执行成功。 |
| AVMETADATA\_ERROR\_INVALID\_PARAM = 1 | 该函数是使用无效的输入参数执行的。 |
| AVMETADATA\_ERROR\_NO\_MEMORY = 2 | 内存分配失败。 |

### AVQueueItem\_Result

PhonePC/2in1TabletTVWearable

```
1. enum AVQueueItem_Result
```

**描述**

播放列表中单项的错误码。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AVQUEUEITEM\_SUCCESS = 0 | 接口执行成功。 |
| AVQUEUEITEM\_ERROR\_INVALID\_PARAM = 1 | 该函数是使用无效的输入参数执行的。 |
| AVQUEUEITEM\_ERROR\_NO\_MEMORY = 2 | 内存分配失败。 |
