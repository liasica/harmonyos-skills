---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-e
title: Enums
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:12:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98aa1664c18aa2b5b93c8c2086a95290570917d1c0a6fc3baa71c6d0558ea1a6
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ProtocolType11+

PhonePC/2in1TabletTV

远端设备支持的协议类型的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_LOCAL | 0 | 本地设备，包括设备本身的内置扬声器或音频插孔、A2DP 设备。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_CAST\_PLUS\_STREAM | 2 | Cast+的Stream模式。表示媒体正在其他设备上展示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_DLNA12+ | 4 | DLNA协议。表示媒体正在其他设备上展示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| TYPE\_CAST\_PLUS\_AUDIO20+ | 8 | PCM模式。表示媒体正在其他设备上展示。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## CastDisplayState12+

PhoneTablet

投播显示设备状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_OFF | 1 | 设备断开，扩展屏不再显示内容。 |
| STATE\_ON | 2 | 设备连接成功，扩展屏可用。 |

## CallerType22+

PhonePC/2in1TabletTVWearable

表示调用方来源类型的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_CAST | "cast" | 调用方来自投播。 |
| TYPE\_BLUETOOTH | "bluetooth" | 调用方来自蓝牙。 |
| TYPE\_APP | "app" | 调用方来自应用。 |
| TYPE\_NEARLINK | "nearlink" | 调用方来自星闪。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## ConnectionState10+

PhonePC/2in1TabletTVWearable

连接状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_CONNECTING | 0 | 设备连接中。 |
| STATE\_CONNECTED | 1 | 设备连接成功。 |
| STATE\_DISCONNECTED | 6 | 设备断开连接。 |

## CallState11+

PhonePC/2in1TabletTVWearable

表示通话状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALL\_STATE\_IDLE | 0 | 空闲状态。 |
| CALL\_STATE\_INCOMING | 1 | 来电。 |
| CALL\_STATE\_ACTIVE | 2 | 接通。 |
| CALL\_STATE\_DIALING | 3 | 响铃。 |
| CALL\_STATE\_WAITING | 4 | 等待接通。 |
| CALL\_STATE\_HOLDING | 5 | 保持。 |
| CALL\_STATE\_DISCONNECTING | 6 | 挂断。 |

## DisplayTag11+

PhonePC/2in1TabletTVWearable

枚举，表示当前媒体资源的金标，即应用媒体音源的特殊类型标识。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TAG\_AUDIO\_VIVID | 1 | AUDIO VIVID |

## DecoderType19+

PhonePC/2in1TabletTV

枚举，设备所支持的解码格式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | "video/avc" | VIDEO AVC |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | "video/hevc" | VIDEO HEVC |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | "audio/av3a" | AUDIO AV3A |

## ResolutionLevel19+

PhonePC/2in1TabletTV

枚举，设备所支持的分辨率。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RESOLUTION\_480P | 0 | 分辨率为480P(640\*480 dpi)。 |
| RESOLUTION\_720P | 1 | 分辨率为720P(1280\*720 dpi)。 |
| RESOLUTION\_1080P | 2 | 分辨率为1080P(1920\*1080 dpi)。 |
| RESOLUTION\_2K | 3 | 分辨率为2k(2560\*1440 dpi)。 |
| RESOLUTION\_4K | 4 | 分辨率为4k(4096\*3840 dpi)。 |

## AVCastCategory10+

PhonePC/2in1TabletTV

投播的类别枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CATEGORY\_LOCAL | 0 | 本地播放，默认播放设备，声音从本机或者连接的蓝牙耳机设备出声。 |
| CATEGORY\_REMOTE | 1 | 远端播放，远端播放设备，声音从其他设备发出声音或者画面。 |

## DeviceType10+

PhonePC/2in1TabletTVWearable

播放设备的类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_TYPE\_LOCAL | 0 | 本地播放类型。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| DEVICE\_TYPE\_BLUETOOTH | 10 | 蓝牙设备。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| DEVICE\_TYPE\_TV | 2 | 电视。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| DEVICE\_TYPE\_SMART\_SPEAKER | 3 | 音箱设备。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |

## LoopMode10+

PhonePC/2in1TabletTVWearable

表示媒体播放循环模式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOOP\_MODE\_SEQUENCE | 0 | 顺序播放。 |
| LOOP\_MODE\_SINGLE | 1 | 单曲循环。 |
| LOOP\_MODE\_LIST | 2 | 表单循环。 |
| LOOP\_MODE\_SHUFFLE | 3 | 随机播放。 |
| LOOP\_MODE\_CUSTOM11+ | 4 | 自定义播放。 |

## PlaybackState10+

PhonePC/2in1TabletTVWearable

表示媒体播放状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYBACK\_STATE\_INITIAL | 0 | 初始状态。 |
| PLAYBACK\_STATE\_PREPARE | 1 | 播放准备状态。 |
| PLAYBACK\_STATE\_PLAY | 2 | 正在播放。 |
| PLAYBACK\_STATE\_PAUSE | 3 | 暂停。 |
| PLAYBACK\_STATE\_FAST\_FORWARD | 4 | 快进。 |
| PLAYBACK\_STATE\_REWIND | 5 | 快退。 |
| PLAYBACK\_STATE\_STOP | 6 | 停止。 |
| PLAYBACK\_STATE\_COMPLETED | 7 | 播放完成。 |
| PLAYBACK\_STATE\_RELEASED | 8 | 释放。 |
| PLAYBACK\_STATE\_ERROR | 9 | 错误。 |
| PLAYBACK\_STATE\_IDLE11+ | 10 | 空闲。 |
| PLAYBACK\_STATE\_BUFFERING11+ | 11 | 缓冲。 |

## AVSessionErrorCode10+

PhonePC/2in1TabletTVWearable

会话发生错误时的错误码。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERR\_CODE\_SERVICE\_EXCEPTION | 6600101 | 会话服务端异常。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_SESSION\_NOT\_EXIST | 6600102 | 会话不存在。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_CONTROLLER\_NOT\_EXIST | 6600103 | 会话控制器不存在。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_REMOTE\_CONNECTION\_ERR | 6600104 | 远端会话连接失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_COMMAND\_INVALID | 6600105 | 无效会话命令。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_SESSION\_INACTIVE | 6600106 | 会话未激活。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_MESSAGE\_OVERLOAD | 6600107 | 命令&消息过载。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_DEVICE\_CONNECTION\_FAILED | 6600108 | 设备连接失败。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST | 6600109 | 远端会话不存在。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_ENABLED23+ | 6600110 | 应用程序的桌面歌词功能未开启。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_DESKTOP\_LYRIC\_NOT\_SUPPORTED23+ | 6600111 | 当前设备不支持桌面歌词功能。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| ERR\_CODE\_CAST\_CONTROL\_UNSPECIFIED13+ | 6611000 | 未被定义的投播错误码。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_REMOTE\_ERROR13+ | 6611001 | 远端播放器中发生不明错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_BEHIND\_LIVE\_WINDOW13+ | 6611002 | 播放出现延迟。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_TIMEOUT13+ | 6611003 | 投播控制进程超时。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_RUNTIME\_CHECK\_FAILED13+ | 6611004 | 运行时检查失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PLAYER\_NOT\_WORKING13+ | 6611100 | 跨设备数据传输被锁定。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_SEEK\_MODE\_UNSUPPORTED13+ | 6611101 | 不支持指定的查找模式。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_ILLEGAL\_SEEK\_TARGET13+ | 6611102 | 要搜索的位置超出媒体的范围，或者不支持当前搜索模式。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PLAY\_MODE\_UNSUPPORTED13+ | 6611103 | 不支持指定的播放模式。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PLAY\_SPEED\_UNSUPPORTED13+ | 6611104 | 不支持指定的播放速度。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DEVICE\_MISSING13+ | 6611105 | 操作失败，因为媒体源设备或媒体接收器设备已被销毁。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_INVALID\_PARAM13+ | 6611106 | 该参数无效。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_NO\_MEMORY13+ | 6611107 | 内存分配失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_OPERATION\_NOT\_ALLOWED13+ | 6611108 | 不被允许的操作。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_UNSPECIFIED13+ | 6612000 | 未指定的输入/输出错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_FAILED13+ | 6612001 | 网络连接失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_CONNECTION\_TIMEOUT13+ | 6612002 | 网络连接超时。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_INVALID\_HTTP\_CONTENT\_TYPE 13+ | 6612003 | 无效的"Content-Type"。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_BAD\_HTTP\_STATUS13+ | 6612004 | HTTP服务器返回一个意外的HTTP响应状态码。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_FILE\_NOT\_FOUND13+ | 6612005 | 文件不存在。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_PERMISSION13+ | 6612006 | 不允许执行输入/输出的IO操作。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CLEARTEXT\_NOT\_PERMITTED13+ | 6612007 | 应用的网络安全配置不允许访问明文HTTP流量。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_POSITION\_OUT\_OF\_RANGE13+ | 6612008 | 从数据绑定中读取数据。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NO\_CONTENTS13+ | 6612100 | 媒体中没有可播放的内容。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_READ\_ERROR13+ | 6612101 | 媒体无法读取。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_BUSY13+ | 6612102 | 该资源正在使用中。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_CONTENT\_EXPIRED13+ | 6612103 | 输入/输出的IO请求内容已过期。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_USE\_FORBIDDEN13+ | 6612104 | 不允许播放请求内容。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NOT\_VERIFIED13+ | 6612105 | 无法验证所允许的内容。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_EXHAUSTED\_ALLOWED\_USES13+ | 6612106 | 此内容已达到允许的最大使用次数。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_IO\_NETWORK\_PACKET\_SENDING\_FAILED13+ | 6612107 | 从源设备发送数据包到接收设备时出现错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_UNSPECIFIED13+ | 6613000 | 未指定的内容解析错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_MALFORMED13+ | 6613001 | 媒体容器比特流的格式解析错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_MALFORMED13+ | 6613002 | 媒体清单解析错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_CONTAINER\_UNSUPPORTED13+ | 6613003 | 文件的媒体容器格式/媒体容器特性不被支持。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_PARSING\_MANIFEST\_UNSUPPORTED13+ | 6613004 | 媒体清单中不支持的特性。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_UNSPECIFIED13+ | 6614000 | 未指定的解码错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_INIT\_FAILED13+ | 6614001 | 解码器初始化失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_QUERY\_FAILED13+ | 6614002 | 解码器查询失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FAILED13+ | 6614003 | 媒体样本解码失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_EXCEEDS\_CAPABILITIES13+ | 6614004 | 设备的能力无法解码当前格式。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DECODING\_FORMAT\_UNSUPPORTED13+ | 6614005 | 不支持的解码格式。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_UNSPECIFIED13+ | 6615000 | 未指定的音频渲染器错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_INIT\_FAILED 13+ | 6615001 | 音频渲染器初始化失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_AUDIO\_RENDERER\_WRITE\_FAILED13+ | 6615002 | 音频渲染器写入数据失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_UNSPECIFIED13+ | 6616000 | 未指定的DRM相关错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_SCHEME\_UNSUPPORTED13+ | 6616001 | 设备不支持所选择的DRM保护方案。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_PROVISIONING\_FAILED13+ | 6616002 | 设备配置失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_CONTENT\_ERROR13+ | 6616003 | 受DRM保护的内容无法播放。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_LICENSE\_ACQUISITION\_FAILED13+ | 6616004 | 获取许可证失败。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_DISALLOWED\_OPERATION13+ | 6616005 | 许可证策略不允许该操作。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_SYSTEM\_ERROR13+ | 6616006 | DRM系统中发生错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_DEVICE\_REVOKED13+ | 6616007 | 设备已撤销DRM权限。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_LICENSE\_EXPIRED13+ | 6616008 | 加载中的DRM许可证已过期。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |
| ERR\_CODE\_CAST\_CONTROL\_DRM\_PROVIDE\_KEY\_RESPONSE\_ERROR13+ | 6616100 | DRM处理密钥响应时发生错误。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast |

## SkipIntervals11+

PhonePC/2in1TabletTVWearable

表示session支持的快进快退时间间隔的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SECONDS\_10 | 10 | 时间为10秒。 |
| SECONDS\_15 | 15 | 时间为15秒。 |
| SECONDS\_30 | 30 | 时间为30秒。 |
