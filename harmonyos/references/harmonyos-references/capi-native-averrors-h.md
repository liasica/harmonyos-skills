---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-averrors-h
title: native_averrors.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_averrors.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:060f2d0919bd511ea70d79e0fd0553d52f6c6050c6b4de846cc0ebb260ca2058
---

## 概述

PhonePC/2in1TabletTVWearable

媒体框架错误码。

**引用文件：** <multimedia/player\_framework/native\_averrors.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：** [Core](capi-core.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | OH\_AVErrCode | 媒体框架错误码。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVErrCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVErrCode
```

**描述**

媒体框架错误码。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| AV\_ERR\_OK = 0 | 操作成功。 |
| AV\_ERR\_NO\_MEMORY = 1 | 无内存。 |
| AV\_ERR\_OPERATE\_NOT\_PERMIT = 2 | 操作不允许。 |
| AV\_ERR\_INVALID\_VAL = 3 | 无效值。 |
| AV\_ERR\_IO = 4 | IO错误。 |
| AV\_ERR\_TIMEOUT = 5 | 超时错误。 |
| AV\_ERR\_UNKNOWN = 6 | 未知错误。 |
| AV\_ERR\_SERVICE\_DIED = 7 | 服务死亡。 |
| AV\_ERR\_INVALID\_STATE = 8 | 当前状态不支持此操作。 |
| AV\_ERR\_UNSUPPORT = 9 | 未支持的接口。 |
| AV\_ERR\_INPUT\_DATA\_ERROR = 10 | 输入数据错误。  **起始版本：** 12 |
| AV\_ERR\_UNSUPPORTED\_FORMAT = 11 | 不支持的格式。  **起始版本：** 18 |
| AV\_ERR\_EXTEND\_START = 100 | 扩展错误码初始值。 |
| AV\_ERR\_DRM\_BASE = 200 | DRM起始错误码。  **起始版本：** 12 |
| AV\_ERR\_DRM\_DECRYPT\_FAILED = 201 | DRM解密失败。  **起始版本：** 12 |
| AV\_ERR\_VIDEO\_BASE = 300 | 视频起始错误码。  **起始版本：** 12 |
| AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION = 301 | 视频不支持色彩空间转换。  **起始版本：** 12 |
| AV\_ERR\_IO\_CANNOT\_FIND\_HOST = 5411001 | 无法找到主机，可能服务器地址错误。  **起始版本：** 14 |
| AV\_ERR\_IO\_CONNECTION\_TIMEOUT = 5411002 | 网络连接超时。  **起始版本：** 14 |
| AV\_ERR\_IO\_NETWORK\_ABNORMAL = 5411003 | 网络异常导致连接失败。  **起始版本：** 14 |
| AV\_ERR\_IO\_NETWORK\_UNAVAILABLE = 5411004 | 网络不可用导致连接失败。  **起始版本：** 14 |
| AV\_ERR\_IO\_NO\_PERMISSION = 5411005 | 无网络访问权限。  **起始版本：** 14 |
| AV\_ERR\_IO\_NETWORK\_ACCESS\_DENIED = 5411006 | 客户端请求参数错误或超出处理能力。  **起始版本：** 14 |
| AV\_ERR\_IO\_RESOURCE\_NOT\_FOUND = 5411007 | 无法找到可用网络资源。  **起始版本：** 14 |
| AV\_ERR\_IO\_SSL\_CLIENT\_CERT\_NEEDED = 5411008 | 由于未携带客户端证书、证书无效或过期导致服务器验证失败。  **起始版本：** 14 |
| AV\_ERR\_IO\_SSL\_CONNECT\_FAIL = 5411009 | 由于未携带服务器证书、证书无效或过期导致客户端验证失败。  **起始版本：** 14 |
| AV\_ERR\_IO\_SSL\_SERVER\_CERT\_UNTRUSTED = 5411010 | SSL服务器证书不受信任。  **起始版本：** 14 |
| AV\_ERR\_IO\_UNSUPPORTED\_REQUEST = 5411011 | 网络协议不支持该请求。  **起始版本：** 14 |
| AV\_ERR\_IO\_CLEARTEXT\_NOT\_PERMITTED = 5411012 | 不允许HTTP明文访问。  **起始版本：** 23 |
| AV\_ERR\_STREAM\_CHANGED = 5410005 | 同步模式下流格式发生变更。可以通过调用接口[OH\_VideoEncoder\_GetOutputDescription](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputdescription)（视频编码）、[OH\_VideoDecoder\_GetOutputDescription](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputdescription)（视频解码）、[OH\_AudioCodec\_GetOutputDescription](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputdescription)（音频编解码）来获取更新后流的配置信息。  **起始版本：** 20 |
| AV\_ERR\_TRY\_AGAIN\_LATER = 5410006 | 同步模式下临时缓冲区查询失败，建议等待短暂间隔后重试操作。  **起始版本：** 20 |
| AV\_ERR\_SUPER\_RESOLUTION\_UNSUPPORTED = 5410003 | 该媒体源或者当前设备不支持超分。  **起始版本：** 23 |
| AV\_ERR\_SUPER\_RESOLUTION\_NOT\_ENABLED = 5410004 | 未使能超分。  **起始版本：** 23 |
