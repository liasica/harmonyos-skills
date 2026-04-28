---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e
title: Enums
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:13:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:750054ea0bf589afb858e522305f3cd4dfd31bd1fa9ce121fc948e351dc74ea2
---

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AVErrorCode9+

PhonePC/2in1TabletTVWearable

[Media错误码](errorcode-media.md)类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AVERR\_OK | 0 | 表示操作成功。 |
| AVERR\_NO\_PERMISSION | 201 | 表示无权限执行此操作。 |
| AVERR\_INVALID\_PARAMETER | 401 | 表示传入参数无效。 |
| AVERR\_UNSUPPORT\_CAPABILITY | 801 | 表示当前版本不支持该API能力。 |
| AVERR\_NO\_MEMORY | 5400101 | 表示系统内存不足或服务数量达到上限。 |
| AVERR\_OPERATE\_NOT\_PERMIT | 5400102 | 表示当前状态不允许或无权执行此操作。 |
| AVERR\_IO | 5400103 | 表示数据流异常信息。 |
| AVERR\_TIMEOUT | 5400104 | 表示系统或网络响应超时。 |
| AVERR\_SERVICE\_DIED | 5400105 | 表示服务进程死亡。 |
| AVERR\_UNSUPPORT\_FORMAT | 5400106 | 表示不支持当前媒体资源的格式。 |
| AVERR\_AUDIO\_INTERRUPTED11+ | 5400107 | 表示音频焦点被抢占。 |
| AVERR\_IO\_HOST\_NOT\_FOUND14+ | 5411001 | 表示解析或链接服务端地址错误。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_CONNECTION\_TIMEOUT14+ | 5411002 | 表示网络连接超时。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_NETWORK\_ABNORMAL14+ | 5411003 | 表示网络异常导致的数据或链路异常。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_NETWORK\_UNAVAILABLE14+ | 5411004 | 表示网络被禁用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_NO\_PERMISSION14+ | 5411005 | 表示无访问权限。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_REQUEST\_DENIED14+ | 5411006 | 表示客户端请求参数错误或超出处理能力。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_RESOURCE\_NOT\_FOUND14+ | 5411007 | 表示无可用网络资源。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_SSL\_CLIENT\_CERT\_NEEDED14+ | 5411008 | 表示服务端校验客户端证书失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_SSL\_CONNECTION\_FAILED14+ | 5411009 | 表示SSL连接失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_SSL\_SERVER\_CERT\_UNTRUSTED14+ | 5411010 | 表示客户端校验服务端证书失败。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_UNSUPPORTED\_REQUEST14+ | 5411011 | 表示网络协议的原因导致请求不受支持。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| AVERR\_SEEK\_CONTINUOUS\_UNSUPPORTED18+ | 5410002 | 表示不支持SEEK\_CONTINUOUS模式的seek。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| AVERR\_SUPER\_RESOLUTION\_UNSUPPORTED18+ | 5410003 | 表示不支持超分。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| AVERR\_SUPER\_RESOLUTION\_NOT\_ENABLED18+ | 5410004 | 表示未使能超分。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| AVERR\_PARAMETER\_OUT\_OF\_RANGE20+ | 5400108 | 表示参数超过取值范围。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| AVERR\_IO\_CLEARTEXT\_NOT\_PERMITTED23+ | 5411012 | 表示不允许HTTP明文访问。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## MediaType8+

PhonePC/2in1TabletTVWearable

媒体类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_TYPE\_UNSUPPORTED20+ | -1 | 表示未支持的类型。  **元服务API：** 从API version 20 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_AUD | 0 | 表示音频。  **元服务API：** 从API version 11 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_VID | 1 | 表示视频。  **元服务API：** 从API version 11 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_SUBTITLE12+ | 2 | 表示字幕。  **元服务API：** 从API version 12 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_ATTACHMENT20+ | 3 | 表示附件信息（如嵌入的外部文件）。  **元服务API：** 从API version 20 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_DATA20+ | 4 | 表示数据。  **元服务API：** 从API version 20 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_TIMED\_METADATA20+ | 5 | 表示带时间戳的元数据。  **元服务API：** 从API version 20 开始，该接口支持在元服务中使用。 |
| MEDIA\_TYPE\_AUXILIARY20+ | 6 | 表示辅助（轨道）信息。  **元服务API：** 从API version 20 开始，该接口支持在元服务中使用。 |

## CodecMimeType8+

PhonePC/2in1TabletTVWearable

Codec MIME类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO\_H263 | 'video/h263' | 表示视频/h263类型。 |
| VIDEO\_AVC | 'video/avc' | 表示视频/avc类型。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| VIDEO\_MPEG2 | 'video/mpeg2' | 表示视频/mpeg2类型。 |
| VIDEO\_MPEG4 | 'video/mp4v-es' | 表示视频/mpeg4类型。 |
| VIDEO\_VP8 | 'video/x-vnd.on2.vp8' | 表示视频/vp8类型。 |
| VIDEO\_HEVC11+ | 'video/hevc' | 表示视频/H265类型。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| AUDIO\_AAC | 'audio/mp4a-latm' | 表示音频/mp4a-latm类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| AUDIO\_VORBIS | 'audio/vorbis' | 表示音频/vorbis类型。 |
| AUDIO\_FLAC | 'audio/flac' | 表示音频/flac类型。 |
| AUDIO\_MP312+ | 'audio/mpeg' | 表示音频/mpeg类型。 |
| AUDIO\_G711MU12+ | 'audio/g711mu' | 表示音频/G711-mulaw类型。 |
| AUDIO\_AMR\_NB18+ | 'audio/3gpp' | 表示音频/amr-nb类型。 |
| AUDIO\_AMR\_WB18+ | 'audio/amr-wb' | 表示音频/amr-wb类型。 |

## AacProfile22+

PhonePC/2in1TabletTVWearable

高级音频编码（AAC）类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AAC\_LC | 0 | 表示AAC Low-Complexity类型。 |
| AAC\_HE | 1 | 表示AAC High-Efficiency类型。 |
| AAC\_HE\_V2 | 2 | 表示AAC High-Efficiency version 2类型。 |

## MediaDescriptionKey8+

PhonePC/2in1TabletTVWearable

媒体信息描述枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MD\_KEY\_TRACK\_INDEX | 'track\_index' | 表示轨道序号，其对应键值类型为number。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_TRACK\_TYPE | 'track\_type' | 表示轨道类型，其对应键值类型为number，参考[MediaType](arkts-apis-media-e.md#mediatype8)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_CODEC\_MIME | 'codec\_mime' | 表示codec\_mime类型，其对应键值类型为string。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_DURATION | 'duration' | 表示媒体时长，其对应键值类型为number，单位为毫秒（ms）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_BITRATE | 'bitrate' | 表示比特率，其对应键值类型为number，单位为比特率（bps），值为undefined或0表示异常。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_WIDTH | 'width' | 表示视频宽度，其对应键值类型为number，单位为像素（px）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_HEIGHT | 'height' | 表示视频高度，其对应键值类型为number，单位为像素（px）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_FRAME\_RATE | 'frame\_rate' | 表示视频帧率，其对应键值类型为number，单位为每100秒的帧数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_AUD\_CHANNEL\_COUNT | 'channel\_count' | 表示声道数，其对应键值类型为number。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_AUD\_SAMPLE\_RATE | 'sample\_rate' | 表示采样率，其对应键值类型为number，单位为赫兹（Hz）。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| MD\_KEY\_AUD\_SAMPLE\_DEPTH12+ | 'sample\_depth' | 表示位深，其对应键值类型为number，单位为位（bit）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MD\_KEY\_LANGUAGE12+ | 'language' | 表示字幕语言，其对应键值类型为string。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MD\_KEY\_TRACK\_NAME12+ | 'track\_name' | 表示track名称，其对应键值类型为string。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MD\_KEY\_HDR\_TYPE12+ | 'hdr\_type' | 表示视频轨类型，其对应键值类型为string。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MD\_KEY\_ORIGINAL\_WIDTH21+ | 'original\_width' | 表示视频原始宽度，其对应键值类型为number，单位为像素（px）。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| MD\_KEY\_ORIGINAL\_HEIGHT21+ | 'original\_height' | 表示视频原始高度，其对应键值类型为number，单位为像素（px）。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |
| MD\_KEY\_MIME\_TYPE23+ | 'mime\_type' | 表示轨道的mime\_type类型，其对应键值类型为string。对于音视频轨道，该值与MD\_KEY\_CODEC\_MIME相同。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| MD\_KEY\_REFERENCE\_TRACK\_IDS23+ | 'ref\_track\_ids' | 表示此轨道与其他轨道的引用关系，其对应键值类型为string，以逗号分隔。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |
| MD\_KEY\_TRACK\_REFERENCE\_TYPE23+ | 'track\_ref\_type' | 表示此轨道作为辅助轨的辅助类型，其对应键值类型为string。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## FetchResult23+

PhonePC/2in1TabletTVWearable

表示批量获取缩略图操作结果的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FETCH\_FAILED | 0 | 从视频中获取该缩略图失败。 |
| FETCH\_SUCCEEDED | 1 | 从视频中获取该缩略图成功。 |
| FETCH\_CANCELED | 2 | 从视频中获取该缩略图操作被取消。 |

## PlaybackInfoKey12+

PhonePC/2in1TabletTVWearable

播放信息描述枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SERVER\_IP\_ADDRESS | 'server\_ip\_address' | 表示服务器IP地址，其对应键值类型为string。 |
| AVG\_DOWNLOAD\_RATE | 'average\_download\_rate' | 表示平均下载速率，其对应键值类型为number，单位为比特率（bps）。 |
| DOWNLOAD\_RATE | 'download\_rate' | 表示1s的下载速率，其对应键值类型为number，单位为比特率（bps）。 |
| IS\_DOWNLOADING | 'is\_downloading' | 表示下载状态，1表示在下载状态，0表示非下载状态（下载完成），其对应键值类型为number。 |
| BUFFER\_DURATION | 'buffer\_duration' | 表示缓存数据的可播放时长，其对应键值类型为number，单位为秒（s）。 |

## PlaybackMetricsKey23+

PhonePC/2in1TabletTVWearable

表示播放器指标信息的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PREPARE\_DURATION | 'prepare\_duration' | 表示准备时长，单位为毫秒（ms）。 |
| RESOURCE\_CONNECTION\_DURATION | 'resource\_connection\_duration' | 表示资源建链时长，单位为毫秒（ms）。 |
| FIRST\_FRAME\_DECAPSULATION\_DURATION | 'first\_frame\_decapsulation\_duration' | 表示第一帧的解封装时长，单位为毫秒（ms）。 |
| TOTAL\_PLAYING\_TIME | 'total\_playback\_time' | 表示总的播放时长，单位为毫秒（ms）。 |
| DOWNLOAD\_REQUESTS\_COUNT | 'loading\_requests\_count' | 表示总的请求次数。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| TOTAL\_DOWNLOAD\_TIME | 'total\_loading\_time' | 表示总的加载时长，单位为毫秒（ms）。 |
| TOTAL\_DOWNLOAD\_SIZE | 'total\_loading\_bytes' | 表示总的加载大小，单位为字节（Byte）。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| STALLING\_COUNT | 'stalling\_count' | 表示总的卡顿次数。 |
| TOTAL\_STALLING\_TIME | 'total\_stalling\_time' | 表示总的卡顿时长，单位为毫秒（ms）。 |

## BufferingInfoType8+

PhonePC/2in1TabletTVWearable

缓存事件类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BUFFERING\_START | 1 | 表示开始缓冲。当上报BUFFERING\_START时，播放器会暂停播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BUFFERING\_END | 2 | 表示结束缓冲。当上报BUFFERING\_END时，播放器会恢复播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BUFFERING\_PERCENT | 3 | 表示缓冲百分比。可参考该事件感知缓冲进度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CACHED\_DURATION | 4 | 表示已缓冲数据预估可播放时长，单位为毫秒（ms）。缓冲区中的数据变化量大于500ms，上报一次。可参考该事件做进度条。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## SoundInterruptMode23+

PhonePC/2in1TabletTVWearable

表示在SoundPool中，同一ID的音频在播放时的打断模式的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_INTERRUPT | 0 | 表示同一ID的音频，如果前者尚未播放完成，后者不会打断前者的播放，二者并行播放。 |
| SAME\_SOUND\_INTERRUPT | 1 | 表示同一ID的音频，如果前者尚未播放完成，后者在播放前会先打断前者的播放。 |

## StateChangeReason9+

PhonePC/2in1TabletTVWearable

表示播放或录制实例状态机切换原因的枚举，伴随state一起上报。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER | 1 | 表示用户行为造成的状态切换，由用户或客户端主动调用接口产生。 |
| BACKGROUND | 2 | 表示后台系统行为造成的状态切换，比如应用未注册播控中心权限，退到后台时被系统强制暂停或停止。 |

## SeekMode8+

PhonePC/2in1TabletTVWearable

视频播放的Seek模式枚举，可通过seek方法作为参数传递下去。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEEK\_NEXT\_SYNC | 0 | 表示跳转到指定时间点的下一个关键帧，建议向后快进的时候用这个枚举值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SEEK\_PREV\_SYNC | 1 | 表示跳转到指定时间点的上一个关键帧，建议向前快进的时候用这个枚举值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SEEK\_CLOSEST12+ | 2 | 表示跳转到距离指定时间点最近的帧，建议精准跳转进度的时候用这个枚举值。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SEEK\_CONTINUOUS18+ | 3 | 该模式提供了一种画面平滑流畅变化的Seek体验，应用可以结合进度条控件持续调用Seek方法，AVPlayer根据Seek调用持续流畅地更新画面。  应用可以调用[isSeekContinuousSupported](arkts-apis-media-avplayer.md#isseekcontinuoussupported18)方法根据返回结果感知视频源是否支持该模式Seek。  对于不支持该Seek模式的视频源调用该模式Seek时，会上报AVERR\_SEEK\_CONTINUOUS\_UNSUPPORTED错误(参考[AVErrorCode](arkts-apis-media-e.md#averrorcode9))，同时画面更新的流畅性会降低。  该Seek模式不会触发[on('seekDone')](arkts-apis-media-avplayer.md#onseekdone9)事件。  当应用需要退出该模式下的Seek时，需要调用seek(-1, SeekMode.SEEK\_CONTINUOUS)来结束该模式下的Seek。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## SwitchMode12+

PhonePC/2in1TabletTVWearable

视频播放的selectTrack模式枚举，可通过selectTrack方法作为参数传递下去，当前仅DASH协议视频轨支持该扩展参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SMOOTH | 0 | 表示切换后视频平滑播放，该模式切换存在延迟，不会立即生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SEGMENT | 1 | 表示切换后从当前分片开始位置播放，该模式立即切换，会有重复播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CLOSEST | 2 | 表示从距离当前播放时间点最近的帧开始播放，该模式立即切换，切换后会卡住3到5s，然后恢复播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## PlaybackSpeed8+

PhonePC/2in1TabletTVWearable

视频播放的倍速枚举，可通过setSpeed方法作为参数传递下去。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPEED\_FORWARD\_0\_75\_X | 0 | 表示视频播放正常播速的0.75倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_1\_00\_X | 1 | 表示视频播放正常播速。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_1\_25\_X | 2 | 表示视频播放正常播速的1.25倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_1\_75\_X | 3 | 表示视频播放正常播速的1.75倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_2\_00\_X | 4 | 表示视频播放正常播速的2.00倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_50\_X12+ | 5 | 表示视频播放正常播速的0.50倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_1\_50\_X12+ | 6 | 表示视频播放正常播速的1.50倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_3\_00\_X13+ | 7 | 表示视频播放正常播速的3.00倍。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_25\_X12+ | 8 | 表示视频播放正常播速的0.25倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_125\_X12+ | 9 | 表示视频播放正常播速的0.125倍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## VideoScaleType9+

PhonePC/2in1TabletTVWearable

枚举，视频缩放模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO\_SCALE\_TYPE\_FIT | 0 | 默认比例类型，视频拉伸至与窗口等大。 |
| VIDEO\_SCALE\_TYPE\_FIT\_CROP | 1 | 保持视频宽高比缩放至最短边填满窗口，长边超出窗口部分被裁剪。 |
| VIDEO\_SCALE\_TYPE\_SCALED\_ASPECT20+ | 2 | 保持视频宽高比缩放至长边填满窗口，短边居中对齐，未填满部分留黑。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## AudioSourceType9+

PhonePC/2in1TabletTVWearable

表示视频录制中音频源类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_SOURCE\_TYPE\_DEFAULT | 0 | 默认的音频输入源类型。 |
| AUDIO\_SOURCE\_TYPE\_MIC | 1 | 表示MIC的音频输入源。  **元服务API：** 从API version 12 开始，该接口支持在元服务中使用。 |
| AUDIO\_SOURCE\_TYPE\_VOICE\_RECOGNITION12+ | 2 | 表示语音识别场景的音频源。 |
| AUDIO\_SOURCE\_TYPE\_VOICE\_COMMUNICATION12+ | 7 | 表示语音通话场景的音频源。 |
| AUDIO\_SOURCE\_TYPE\_VOICE\_MESSAGE12+ | 10 | 表示短语音消息的音频源。 |
| AUDIO\_SOURCE\_TYPE\_CAMCORDER12+ | 13 | 表示相机录像的音频源。 |

## VideoSourceType9+

PhonePC/2in1TabletTVWearable

表示视频录制中视频源类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV | 0 | 输入surface中携带的是raw data。 |
| VIDEO\_SOURCE\_TYPE\_SURFACE\_ES | 1 | 输入surface中携带的是ES data。 |

## ContainerFormatType8+

PhonePC/2in1TabletTVWearable

表示容器格式类型的枚举，缩写为CFT。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CFT\_MPEG\_4 | 'mp4' | 视频的容器格式，MP4。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| CFT\_MPEG\_4A | 'm4a' | 音频的容器格式，M4A。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CFT\_MP312+ | 'mp3' | 音频的容器格式，MP3。 |
| CFT\_WAV12+ | 'wav' | 音频的容器格式，WAV。 |
| CFT\_AMR18+ | 'amr' | 音频的容器格式，AMR。 |
| CFT\_AAC20+ | 'aac' | 音频的容器格式，AAC。默认为ADTS帧头格式。 |

## FileGenerationMode12+

PhonePC/2in1TabletTVWearable

表示创建媒体文件模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APP\_CREATE | 0 | 由应用自行在沙箱创建媒体文件。 |
| AUTO\_CREATE\_CAMERA\_SCENE | 1 | 由系统创建媒体文件，当前仅在相机录制场景下生效，会忽略应用设置的url。 |

## HdrType12+

PhonePC/2in1TabletTVWearable

表示视频HDR类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AV\_HDR\_TYPE\_NONE | 0 | 表示无HDR类型。 |
| AV\_HDR\_TYPE\_VIVID | 1 | 表示为HDR VIVID类型。 |

## AVImageQueryOptions12+

PhonePC/2in1TabletTVWearable

需要获取的缩略图时间点与视频帧的对应关系。

在获取视频缩略图时，传入的时间点与实际取得的视频帧所在时间点不一定相等，需要指定传入的时间点与实际取得的视频帧的时间关系。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AV\_IMAGE\_QUERY\_NEXT\_SYNC | 0 | 表示选取传入时间点或之后的关键帧。 |
| AV\_IMAGE\_QUERY\_PREVIOUS\_SYNC | 1 | 表示选取传入时间点或之前的关键帧。 |
| AV\_IMAGE\_QUERY\_CLOSEST\_SYNC | 2 | 表示选取离传入时间点最近的关键帧。 |
| AV\_IMAGE\_QUERY\_CLOSEST | 3 | 表示选取离传入时间点最近的帧，该帧不一定是关键帧。 |

## LoadingRequestError18+

PhonePC/2in1TabletTVWearable

枚举，数据加载过程中状态变化的原因。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOADING\_ERROR\_SUCCESS | 0 | 由客户端返回，表示已经推送到资源末尾。 |
| LOADING\_ERROR\_NOT\_READY | 1 | 由客户端返回，表示资源尚未准备好可供访问。 |
| LOADING\_ERROR\_NO\_RESOURCE | 2 | 由客户端返回，表示请求的资源URL不存在。 |
| LOADING\_ERROR\_INVAID\_HANDLE | 3 | 由客户端返回，表示请求的资源句柄uuid无效。 |
| LOADING\_ERROR\_ACCESS\_DENIED | 4 | 由客户端返回，表示客户端没有权限请求该资源。 |
| LOADING\_ERROR\_ACCESS\_TIMEOUT | 5 | 由客户端返回，表示访问资源过程超时。 |
| LOADING\_ERROR\_AUTHORIZE\_FAILED | 6 | 由客户端返回，表示授权失败。 |

## AVMimeTypes12+

PhonePC/2in1TabletTVWearable

媒体MIME类型，通过[setMimeType](arkts-apis-media-mediasource.md#setmimetype12)设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APPLICATION\_M3U8 | application/m3u8 | 表示m3u8本地文件。 |

## AVScreenCaptureRecordPreset12+

PhonePC/2in1TabletTV

进行屏幕录制时的编码、封装格式参数的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCREEN\_RECORD\_PRESET\_H264\_AAC\_MP4 | 0 | 使用视频H264编码，音频AAC编码，MP4封装格式。 |
| SCREEN\_RECORD\_PRESET\_H265\_AAC\_MP4 | 1 | 使用视频H265编码，音频AAC编码，MP4封装格式。 |

## AVScreenCaptureStateCode12+

PhonePC/2in1TabletTV

屏幕录制的状态回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCREENCAPTURE\_STATE\_STARTED | 0 | 录屏已开始。 |
| SCREENCAPTURE\_STATE\_CANCELED | 1 | 录屏被取消。 |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER | 2 | 录屏被用户手动停止。 |
| SCREENCAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER | 3 | 录屏被其他录屏打断。 |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_CALL | 4 | 录屏被来电打断。 |
| SCREENCAPTURE\_STATE\_MIC\_UNAVAILABLE | 5 | 录屏无法使用麦克风收音。 |
| SCREENCAPTURE\_STATE\_MIC\_MUTED\_BY\_USER | 6 | 麦克风被用户关闭。 |
| SCREENCAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER | 7 | 麦克风被用户打开。 |
| SCREENCAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE | 8 | 录屏进入隐私页面。 |
| SCREENCAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE | 9 | 录屏退出隐私页面。 |
| SCREENCAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES | 10 | 系统用户切换，录屏中断。 |

## AVScreenCaptureFillMode18+

PhonePC/2in1TabletTV

进行屏幕录制时视频填充模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRESERVE\_ASPECT\_RATIO | 0 | 保持与原始图像相同的宽高比例，即与物理屏幕宽高比例一致。 |
| SCALE\_TO\_FILL | 1 | 进行图像拉伸填充，适配设置的宽度和高度。 |

## PickerMode22+

PhonePC/2in1TabletTV

表示屏幕录制Picker模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_ONLY | 0 | 仅显示窗口列表。 |
| SCREEN\_ONLY | 1 | 仅显示屏幕列表。 |
| SCREEN\_AND\_WINDOW | 2 | 同时显示屏幕列表和窗口列表。 |

## AVMetricsEventType23+

PhonePC/2in1TabletTVWearable

表示媒体服务支持的指标事件的枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AV\_METRICS\_EVENT\_STALLING | 1 | 表示播放卡顿的指标事件。 |

## AudioEncoder(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)替代。

表示音频编码格式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认编码格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AAC替代。 |
| AMR\_NB | 1 | AMR-NB(Adaptive Multi Rate-Narrow Band Speech Codec) 编码格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AMR\_NB替代。 |
| AMR\_WB | 2 | AMR-WB(Adaptive Multi Rate-Wide Band Speech Codec) 编码格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AMR\_WB替代。 |
| AAC\_LC | 3 | AAC-LC（Advanced Audio Coding Low Complexity）编码格式。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AAC替代。 |
| HE\_AAC | 4 | HE\_AAC（High-Efficiency Advanced Audio Coding）编码格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AAC替代。 |

## AudioOutputFormat(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 6开始支持，从API version 8 开始废弃，建议使用[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)替代。

表示音频封装格式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认封装格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议根据具体情况选择[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)中的一项替代。 |
| MPEG\_4 | 2 | 封装为MPEG-4格式。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)中的CFT\_MPEG\_4替代。 |
| AMR\_NB | 3 | 封装为AMR\_NB格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)中的CFT\_AMR，编码格式使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AMR\_NB替代。 |
| AMR\_WB | 4 | 封装为AMR\_WB格式。  仅做接口定义，暂不支持使用。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)中的CFT\_AMR，编码格式使用[CodecMimeType](arkts-apis-media-e.md#codecmimetype8)中的AUDIO\_AMR\_WB替代。 |
| AAC\_ADTS | 6 | 封装为ADTS（Audio Data Transport Stream）格式，是AAC音频的传输流格式。  **说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](arkts-apis-media-e.md#containerformattype8)中的CFT\_AAC替代。 |

## MediaErrorCode(deprecated)

PhonePC/2in1TabletTVWearable

媒体服务错误类型枚举。

说明

从API version 8开始支持，从API version 11开始废弃，建议使用[AVErrorCode](arkts-apis-media-e.md#averrorcode9)替代。

**系统能力：** SystemCapability.Multimedia.Media.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MSERR\_OK | 0 | 表示操作成功。 |
| MSERR\_NO\_MEMORY | 1 | 表示申请内存失败，系统可能无可用内存。 |
| MSERR\_OPERATION\_NOT\_PERMIT | 2 | 表示无权限执行此操作。 |
| MSERR\_INVALID\_VAL | 3 | 表示传入入参无效。 |
| MSERR\_IO | 4 | 表示发生IO错误。 |
| MSERR\_TIMEOUT | 5 | 表示操作超时。 |
| MSERR\_UNKNOWN | 6 | 表示未知错误。 |
| MSERR\_SERVICE\_DIED | 7 | 表示服务端失效。 |
| MSERR\_INVALID\_STATE | 8 | 表示在当前状态下，不允许执行此操作。 |
| MSERR\_UNSUPPORTED | 9 | 表示在当前版本下，不支持此操作。 |
