---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-i
title: Interfaces (其他)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e97c5cb6e7cce7a95ef5c139e3d70d45b234219c6abea80b4edd55fb482622b1
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AVCastControlCommand10+

PhonePC/2in1TabletTV

投播控制器接受的命令的对象描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| command | [AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10) | 否 | 否 | 命令。每种命令对应的参数不同，具体的对应关系可查阅[AVCastControlCommandType](arkts-apis-avsession-t.md#avcastcontrolcommandtype10)。 |
| parameter | [media.PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8) | number | string | [LoopMode](arkts-apis-avsession-e.md#loopmode10) | 否 | 是 | 命令对应的参数。 |

## CastDisplayInfo12+

PhoneTablet

扩展屏投播显示设备相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 投播显示设备的ID，该参数应为整数。 |
| name | string | 否 | 否 | 投播显示设备的名称。 |
| state | [CastDisplayState](arkts-apis-avsession-e.md#castdisplaystate12) | 否 | 否 | 投播显示设备状态。 |
| width | number | 否 | 否 | 投播显示设备的屏幕宽度，单位为px，该参数应为整数。 |
| height | number | 否 | 否 | 投播显示设备的屏幕高度，单位为px，该参数应为整数。 |

## AVMetadata10+

PhonePC/2in1TabletTVWearable

媒体元数据的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| assetId | string | 否 | 否 | 媒体ID。媒体信息的唯一标识，由应用自定义。  - 该属性发生变化则其他元数据属性都将被刷新。  - 若该属性维持不变，且不设置相应的媒体元数据信息，那么将不会更新对应的媒体元数据信息。  - 当该属性设为空值时，调用[setAVMetadata](arkts-apis-avsession-avsession.md#setavmetadata10)方法将失败，返回错误码6600101。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 标题。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| artist | string | 否 | 是 | 艺术家。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| author | string | 否 | 是 | 专辑作者。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| avQueueName12+ | string | 否 | 是 | 歌单（歌曲列表）名称。 |
| avQueueId11+ | string | 否 | 是 | 歌单（歌曲列表）唯一标识Id。 |
| avQueueImage11+ | [image.PixelMap](arkts-apis-image-pixelmap.md) | string | 否 | 是 | 歌单（歌曲列表）封面图。  图片的像素数据或者图片路径地址（本地路径或网络路径）。应用通过setAVMetadata设置图片数据。  - 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。  - 设置为url图片路径，获取的为url图片路径。 |
| album | string | 否 | 是 | 专辑名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| writer | string | 否 | 是 | 词作者。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| composer | string | 否 | 是 | 作曲者。 |
| duration | number | 否 | 是 | 媒体时长，单位毫秒（ms）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mediaImage | [image.PixelMap](arkts-apis-image-pixelmap.md) | string | 否 | 是 | 图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过setAVMetadata设置图片数据。  - 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。  - 设置为url图片路径，获取的为url图片路径。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bundleIcon18+ | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 是 | 应用图标图片的像素数据。只读类型，不从应用侧设置。 |
| publishDate | Date | 否 | 是 | 发行日期。 |
| subtitle | string | 否 | 是 | 子标题。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| description | string | 否 | 是 | 媒体描述。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lyric | string | 否 | 是 | 媒体歌词内容。应用需将歌词内容拼接为一个字符串传入。  字符串长度需小于40960字节。  **说明：** 系统支持简单版的LRC格式（Simple LRC format）的歌词文本内容。当传入的歌词内容不规范（例如：出现重复的时间戳等），将导致解析失败，并在系统中显示异常。 |
| singleLyricText17+ | string | 否 | 是 | 单条媒体歌词内容。应用需将歌词内容拼接为一个字符串传入（不包含时间戳）。  字符串长度小于40960字节。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| previousAssetId | string | 否 | 是 | 上一首媒体ID。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| nextAssetId | string | 否 | 是 | 下一首媒体ID。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| filter11+ | number | 否 | 是 | 当前session支持的协议，默认为TYPE\_CAST\_PLUS\_STREAM。具体取值参考[ProtocolType](arkts-apis-avsession-e.md#protocoltype11)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| drmSchemes12+ | Array<string> | 否 | 是 | 当前session支持的DRM方案，取值为DRM方案uuid。 |
| skipIntervals11+ | [SkipIntervals](arkts-apis-avsession-e.md#skipintervals11) | 否 | 是 | 快进快退支持的时间间隔。默认为SECONDS\_15，即15秒。 |
| displayTags11+ | number | 否 | 是 | 媒体资源的金标类型，取值参考[DisplayTag](arkts-apis-avsession-e.md#displaytag11)。 |

## AVMediaDescription10+

PhonePC/2in1TabletTVWearable

播放列表媒体元数据的相关属性。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| assetId | string | 否 | 否 | 播放列表媒体ID。媒体信息的唯一标识，由应用自定义。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 播放列表媒体标题。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| subtitle | string | 否 | 是 | 播放列表媒体子标题。  在使用了cast+协议的音频投播场景下，不支持使用该属性。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| description | string | 否 | 是 | 播放列表媒体描述的文本。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mediaImage | [image.PixelMap](arkts-apis-image-pixelmap.md) | string | 否 | 是 | 设置播放列表媒体图片像素数据。  在使用了cast+协议的音视频投播场景下，该字段用于给对端设备设置媒体专辑封面。  当入参为string类型时：  - 只支持使用网络URI设置封面，不支持本地URI。  - 其作用与albumCoverUri属性功能相同，且优先级高于albumCoverUri。  从API version 23开始，支持入参为image.PixelMap类型给对端设备设置媒体信息。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| extras | {[key: string]: Object;} | 否 | 是 | 播放列表媒体额外字段。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| mediaUri | string | 否 | 是 | 播放列表媒体URI。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mediaType | string | 否 | 是 | 播放列表媒体类型。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mediaSize | number | 否 | 是 | 播放列表媒体的大小。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| albumTitle | string | 否 | 是 | 播放列表媒体专辑标题。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| albumCoverUri | string | 否 | 是 | 播放列表媒体专辑封面URI。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lyricContent | string | 否 | 是 | 播放列表媒体歌词内容。  字符串长度需小于40960字节。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lyricUri | string | 否 | 是 | 播放列表媒体歌词URI。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| artist | string | 否 | 是 | 播放列表媒体专辑作者。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| fdSrc | [media.AVFileDescriptor](arkts-apis-media-i.md#avfiledescriptor9) | 否 | 是 | 播放列表媒体本地文件的句柄。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dataSrc12+ | [media.AVDataSrcDescriptor](arkts-apis-media-i.md#avdatasrcdescriptor10) | 否 | 是 | 播放列表数据源描述。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| pcmSrc20+ | boolean | 否 | 是 | 播放列表是否使用PCM数据源。true表示使用PCM数据源，false表示不使用PCM数据源。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| drmScheme12+ | string | 否 | 是 | 播放列表媒体支持的DRM方案，由uuid表示。  **系统能力：** SystemCapability.Multimedia.AVSession.Core |
| duration | number | 否 | 是 | 播放列表媒体播放时长。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| startPosition | number | 否 | 是 | 播放列表媒体起始播放位置。音视频投播场景中，在投播资源时，此字段应置空或赋值为0。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| creditsPosition | number | 否 | 是 | 播放列表媒体的片尾播放位置。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| appName | string | 否 | 是 | 播放列表提供的应用的名字。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| displayTags11+ | number | 否 | 是 | 媒体资源的金标类型，取值参考[DisplayTag](arkts-apis-avsession-e.md#displaytag11)。  在使用了cast+协议的音频投播场景下，不支持使用该属性。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| launchClientData20+ | string | 否 | 是 | 投播过程中应用程序向接收方发送的自定义数据。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## AVQueueItem10+

PhonePC/2in1TabletTVWearable

播放列表中单项的相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemId | number | 否 | 否 | 播放列表中单项的ID。 |
| description | [AVMediaDescription](arkts-apis-avsession-i.md#avmediadescription10) | 否 | 是 | 播放列表中单项的媒体元数据。 |

## AVPlaybackState10+

PhonePC/2in1TabletTVWearable

媒体播放状态的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [PlaybackState](arkts-apis-avsession-e.md#playbackstate10) | 否 | 是 | 播放状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| speed | number | 否 | 是 | 播放倍速。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| position | [PlaybackPosition](arkts-apis-avsession-i.md#playbackposition10) | 否 | 是 | 播放位置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| bufferedTime | number | 否 | 是 | 缓冲时间。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| loopMode | [LoopMode](arkts-apis-avsession-e.md#loopmode10) | 否 | 是 | 循环模式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isFavorite | boolean | 否 | 是 | 表示是否收藏。true表示收藏，false表示不收藏。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| activeItemId | number | 否 | 是 | 正在播放的媒体Id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| volume | number | 否 | 是 | 正在播放的媒体音量。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxVolume11+ | number | 否 | 是 | 最大音量。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| muted11+ | boolean | 否 | 是 | 当前是否是静音状态。true表示是，false表示不是。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| duration11+ | number | 否 | 是 | 当前媒体资源的时长。 |
| videoWidth11+ | number | 否 | 是 | 媒体资源的视频宽度，单位为像素（px）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| videoHeight11+ | number | 否 | 是 | 媒体资源的视频高度，单位为像素（px）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| extras | {[key: string]: Object;} | 否 | 是 | 自定义媒体数据。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## PlaybackPosition10+

PhonePC/2in1TabletTVWearable

媒体播放位置的相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| elapsedTime | number | 否 | 否 | 已用时间，单位毫秒（ms）。 |
| updateTime | number | 否 | 否 | 更新时间，单位毫秒（ms）。 |

## CallMetadata11+

PhonePC/2in1TabletTVWearable

通话会话元数据相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 来电人姓名（别名）。 |
| phoneNumber | string | 否 | 是 | 来电电话号码。 |
| avatar | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 来电人头像。 |

## AVCallState11+

PhonePC/2in1TabletTVWearable

通话状态相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [CallState](arkts-apis-avsession-e.md#callstate11) | 否 | 否 | 当前通话状态。 |
| muted | boolean | 否 | 否 | 表示通话mic是否静音。 true表示是静音，false表示不是静音。 |

## DeviceInfo10+

PhonePC/2in1TabletTVWearable

播放设备的相关信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| castCategory | [AVCastCategory](arkts-apis-avsession-e.md#avcastcategory10) | 否 | 否 | 投播的类别。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| deviceId | string | 否 | 否 | 播放设备的ID。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| deviceName | string | 否 | 否 | 播放设备的名称。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| deviceType | [DeviceType](arkts-apis-avsession-e.md#devicetype10) | 否 | 否 | 播放设备的类型。  **系统能力：** SystemCapability.Multimedia.AVSession.Core  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| supportedProtocols11+ | number | 否 | 是 | 播放设备支持的协议。  默认为TYPE\_LOCAL,具体取值来自[ProtocolType](arkts-apis-avsession-e.md#protocoltype11)，可以是protocolType中的某个协议或者多个协议的组合。  设备仅支持一种协议，返回对应枚举值；设备支持多种协议，返回对应枚举值之和。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| supportedDrmCapabilities12+ | Array<string> | 否 | 是 | 播放设备支持的DRM能力。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| manufacturer13+ | string | 否 | 是 | 播放设备生产厂家。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| modelName13+ | string | 否 | 是 | 播放设备型号名称。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| audioCapabilities20+ | [AudioCapabilities](arkts-apis-avsession-i.md#audiocapabilities20) | 否 | 是 | 播放设备支持的音频能力。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| supportedPullClients20+ | Array<number> | 否 | 是 | 支持拉端客户端的ID集合（只有支持4K投播的设备会返回此字段）。  **系统能力：** SystemCapability.Multimedia.AVSession.AVCast  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## OutputDeviceInfo10+

PhonePC/2in1TabletTVWearable

播放设备的相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| devices | Array<[DeviceInfo](arkts-apis-avsession-i.md#deviceinfo10)> | 否 | 否 | 播放设备的集合。 |

## AVControlCommand10+

PhonePC/2in1TabletTVWearable

会话接受的命令的对象描述。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| command | [AVControlCommandType](arkts-apis-avsession-t.md#avcontrolcommandtype10) | 否 | 否 | 命令（不同命令对应不同参数）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| parameter | [LoopMode](arkts-apis-avsession-e.md#loopmode10) | string | number | 否 | 是 | 命令对应的参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| commandInfo22+ | [CommandInfo](arkts-apis-avsession-i.md#commandinfo22) | 否 | 是 | 命令信息。 |

## AVCastPickerOptions14+

PhonePC/2in1TabletTV

拉起的投播组件包含的配置属性。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionType | [AVSessionType](arkts-apis-avsession-t.md#avsessiontype10) | 否 | 是 | 会话类型，默认值为audio。  当前仅支持的会话类型有audio和video。如果传入voice\_call或video\_call，将默认按照传入audio处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| pickerStyle22+ | [AVCastPickerStyle](js-apis-avcastpickerparam.md#avcastpickerstyle12) | 否 | 是 | 设置组件样式。 |
| menuPosition22+ | [MenuPosition](arkts-apis-avsession-i.md#menuposition-22) | 否 | 是 | 当pickerStyle设置为STYLE\_MENU时，可以设置弹出菜单的位置。 |

## AudioCapabilities20+

PhonePC/2in1TabletTV

表示投播设备支持的音频能力。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| streamInfos | Array<[audio.AudioStreamInfo](arkts-apis-audio-i.md#audiostreaminfo8)> | 是 | 否 | 音频能力参数的列表。 |

## CommandInfo22+

PhonePC/2in1TabletTVWearable

定义要发送到会话的命令信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| callerBundleName | string | 否 | 是 | 调用方应用包名。 |
| callerModuleName | string | 否 | 是 | 调用方应用模块名。 |
| callerDeviceId | string | 否 | 是 | 调用方设备ID。 |
| callerType | [CallerType](arkts-apis-avsession-e.md#callertype22) | 否 | 是 | 调用方来源。 |

## MenuPosition 22+

PhonePC/2in1TabletTV

定义可弹出菜单的组件的位置。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 组件在X轴上的位置坐标。单位为vp。 |
| y | number | 否 | 否 | 组件在y轴上的位置坐标。单位为vp。 |
| width | number | 否 | 否 | 组件宽度。单位为vp。 |
| height | number | 否 | 否 | 组件高度。单位为vp。 |

## AVSessionDescriptor 23+

PhonePC/2in1TabletTVWearable

会话的相关描述信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sessionId | string | 否 | 否 | 会话ID。 |
| type | [AVSessionType](arkts-apis-avsession-t.md#avsessiontype10) | 否 | 否 | 会话类型。 |
| sessionTag | string | 否 | 否 | 会话的自定义名称。 |
| elementName | [ElementName](js-apis-bundle-elementname.md) | 否 | 否 | 会话所属应用的信息（包含bundleName、abilityName等）。 |
| isActive | boolean | 否 | 否 | 会话是否被激活。  true：已被激活。  false：没有被激活。 |
| isTopSession | boolean | 否 | 否 | 会话是否为最新的会话。  true：是最新的会话。  false：不是最新的会话。 |

## DesktopLyricState23+

PhonePC/2in1TabletTVWearable

桌面歌词状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLocked | boolean | 否 | 否 | 桌面歌词位置是否锁定。true表示已锁定，false表示未锁定。若已锁定，桌面显示歌词后，固定当前位置，不可被拖拽。 |
