---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-h
title: avplayer.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avplayer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa0bd61f4c7876fa8c35a7b63b70655512111f3cad6c4b7fbfa10dc7bcd29bb2
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVPlayer接口。使用AVPlayer提供的Native API播放媒体源。

**引用文件：** <multimedia/player\_framework/avplayer.h>

**库：** libavplayer.so

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**相关模块：** [AVPlayer](capi-avplayer.md)

**相关示例：** [AVPlayerNDKVideo](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerNDK)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [MediaKeySession](capi-avplayer-mediakeysession.md) | MediaKeySession | MediaKeySession类型。 |
| [DRM\_MediaKeySystemInfo](capi-avplayer-drm-mediakeysysteminfo.md) | DRM\_MediaKeySystemInfo | DRM\_MediaKeySystemInfo类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Player\_MediaKeySystemInfoCallback)(OH\_AVPlayer player, DRM\_MediaKeySystemInfo mediaKeySystemInfo)](capi-avplayer-h.md#player_mediakeysysteminfocallback) | Player\_MediaKeySystemInfoCallback | 播放器DRM信息更新时调用。 |
| [OH\_AVPlayer \*OH\_AVPlayer\_Create(void)](capi-avplayer-h.md#oh_avplayer_create) | - | 创建播放器。  推荐单个应用创建的音视频播放器实例（即音频、视频、音视频三类相加）不超过16个。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetURLSource(OH\_AVPlayer \*player, const char \*url)](capi-avplayer-h.md#oh_avplayer_seturlsource) | - | 设置播放器的播放源。对应的源可以是http url。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetFDSource(OH\_AVPlayer \*player, int32\_t fd, int64\_t offset, int64\_t size)](capi-avplayer-h.md#oh_avplayer_setfdsource) | - | 设置播放器的媒体文件描述符来源。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetDataSource(OH\_AVPlayer player, OH\_AVDataSourceExt datasrc, void\* userData)](capi-avplayer-h.md#oh_avplayer_setdatasource) | - | 设置播放器的媒体源，该媒体源的数据由应用程序提供。 |
| [OH\_AVErrCode OH\_AVPlayer\_Prepare(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_prepare) | - | 准备播放环境，异步缓存媒体数据。  此函数必须在SetSource之后调用。 |
| [OH\_AVErrCode OH\_AVPlayer\_Play(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_play) | - | 开始播放。  此函数必须在[OH\_AVPlayer\_Prepare](capi-avplayer-h.md#oh_avplayer_prepare)之后调用。  如果播放器状态为<Prepared>，调用此函数开始播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_Pause(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_pause) | - | 暂停播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_Stop(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_stop) | - | 停止播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_Reset(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_reset) | - | 将播放器恢复到初始状态。  函数调用完成后，调用SetSource添加播放源。调用[OH\_AVPlayer\_Prepare](capi-avplayer-h.md#oh_avplayer_prepare)后，再调用[OH\_AVPlayer\_Play](capi-avplayer-h.md#oh_avplayer_play)重新开始播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_Release(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_release) | - | 异步释放播放器资源。  异步释放可以提升性能，但不能确保播放画面的SurfaceBuffer已释放。调用者需要确保播放画面窗口的生命周期安全。 |
| [OH\_AVErrCode OH\_AVPlayer\_ReleaseSync(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_releasesync) | - | 同步释放播放器资源。  同步过程保证了播放画面的SurfaceBuffer释放，但该过程耗时较长，建议调用者自行设计异步机制。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVolume(OH\_AVPlayer \*player, float leftVolume, float rightVolume)](capi-avplayer-h.md#oh_avplayer_setvolume) | - | 设置播放器的音量。  可以在播放或暂停的过程中使用。0表示无声音，1为原始值。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetLoudnessGain(OH\_AVPlayer \*player, float loudnessGain)](capi-avplayer-h.md#oh_avplayer_setloudnessgain) | - | 设置播放器的响度。当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。  默认响度增益0.0dB。播放器流的usage参数必须是[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC，  [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE，[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK 之一。  音频渲染器的延迟模式必须是[OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL。  如果通过高分辨率管道播放，则不支持此操作。 |
| [OH\_AVErrCode OH\_AVPlayer\_Seek(OH\_AVPlayer \*player, int32\_t mSeconds, AVPlayerSeekMode mode)](capi-avplayer-h.md#oh_avplayer_seek) | - | 改变播放位置。  此函数可以在播放或暂停时使用。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetCurrentTime(OH\_AVPlayer \*player, int32\_t \*currentTime)](capi-avplayer-h.md#oh_avplayer_getcurrenttime) | - | 获取播放位置，精确到毫秒。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetVideoWidth(OH\_AVPlayer \*player, int32\_t \*videoWidth)](capi-avplayer-h.md#oh_avplayer_getvideowidth) | - | 获取视频宽度。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetVideoHeight(OH\_AVPlayer \*player, int32\_t \*videoHeight)](capi-avplayer-h.md#oh_avplayer_getvideoheight) | - | 获取视频高度。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed speed)](capi-avplayer-h.md#oh_avplayer_setplaybackspeed) | - | 根据指定的[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)，设置播放器的播放速率。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackRate(OH\_AVPlayer \*player, float rate)](capi-avplayer-h.md#oh_avplayer_setplaybackrate) | - | 在有效范围内，设置播放器的播放速率。  支持的状态：已准备/正在播放/已暂停/已完成。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetPlaybackSpeed(OH\_AVPlayer \*player, AVPlaybackSpeed \*speed)](capi-avplayer-h.md#oh_avplayer_getplaybackspeed) | - | 获取当前播放器的播放速率。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetPlaybackRate(OH\_AVPlayer \*player, float \*rate)](capi-avplayer-h.md#oh_avplayer_getplaybackrate) | - | 获取当前播放器播放速率。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioRendererInfo(OH\_AVPlayer \*player, OH\_AudioStream\_Usage streamUsage)](capi-avplayer-h.md#oh_avplayer_setaudiorendererinfo) | - | 设置player音频流类型。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVolumeMode(OH\_AVPlayer \*player, OH\_AudioStream\_VolumeMode volumeMode)](capi-avplayer-h.md#oh_avplayer_setvolumemode) | - | 设置player音频流音量模式。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioInterruptMode(OH\_AVPlayer \*player, OH\_AudioInterrupt\_Mode interruptMode)](capi-avplayer-h.md#oh_avplayer_setaudiointerruptmode) | - | 设置player音频流的打断模式。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetAudioEffectMode(OH\_AVPlayer \*player, OH\_AudioStream\_AudioEffectMode effectMode)](capi-avplayer-h.md#oh_avplayer_setaudioeffectmode) | - | 设置player音频流的音效模式。 |
| [OH\_AVErrCode OH\_AVPlayer\_SelectBitRate(OH\_AVPlayer \*player, uint32\_t bitRate)](capi-avplayer-h.md#oh_avplayer_selectbitrate) | - | 设置hls播放器使用的码率。仅对HLS协议网络流有效。  默认情况下，播放器会根据网络连接情况选择合适的码率和速度。  通过INFO\_TYPE\_BITRATE\_COLLECT上报有效码率链表，设置并选择指定的码率，选择小于且最接近的码率。准备好后，读取以查询当前选择的比特率。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVideoSurface(OH\_AVPlayer \*player, OHNativeWindow \*window)](capi-avplayer-h.md#oh_avplayer_setvideosurface) | - | 设置播放画面窗口。  此函数必须在SetSource之后，Prepare之前调用。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetDuration(OH\_AVPlayer \*player, int32\_t \*duration)](capi-avplayer-h.md#oh_avplayer_getduration) | - | 获取媒体文件的总时长，精确到毫秒。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetState(OH\_AVPlayer \*player, AVPlayerState \*state)](capi-avplayer-h.md#oh_avplayer_getstate) | - | 获取当前播放状态。 |
| [bool OH\_AVPlayer\_IsPlaying(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_isplaying) | - | 判断播放器是否在播放。 |
| [bool OH\_AVPlayer\_IsLooping(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_islooping) | - | 判断是否循环播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetLooping(OH\_AVPlayer \*player, bool loop)](capi-avplayer-h.md#oh_avplayer_setlooping) | - | 设置循环播放。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlayerCallback(OH\_AVPlayer \*player, AVPlayerCallback callback)](capi-avplayer-h.md#oh_avplayer_setplayercallback) | - | 设置播放器回调函数。  由于通过此方法设置的信息监听回调函数[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)和错误监听回调函数[OH\_AVPlayerOnError](capi-avplayer-base-h.md#oh_avplayeronerror)可以传递的信息有限，也不便于应用区分多个播放器实例。  从API version 12开始，应使用[OH\_AVPlayer\_SetOnInfoCallback](capi-avplayer-h.md#oh_avplayer_setoninfocallback)、[OH\_AVPlayer\_SetOnErrorCallback](capi-avplayer-h.md#oh_avplayer_setonerrorcallback)接口分别设置信息监听回调函数[OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)和错误监听回调函数[OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback)。(API12废弃) |
| [OH\_AVErrCode OH\_AVPlayer\_SelectTrack(OH\_AVPlayer \*player, int32\_t index)](capi-avplayer-h.md#oh_avplayer_selecttrack) | - | 选择音频或字幕轨道。  默认播放第一个带数据的音轨，不播放字幕轨道。  设置生效后，原音轨将失效。请设置字幕处于准备/播放/暂停/完成状态，并将音轨设置为准备状态。 |
| [OH\_AVErrCode OH\_AVPlayer\_DeselectTrack(OH\_AVPlayer \*player, int32\_t index)](capi-avplayer-h.md#oh_avplayer_deselecttrack) | - | 取消选择当前音频或字幕轨道。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetCurrentTrack(OH\_AVPlayer \*player, int32\_t trackType, int32\_t \*index)](capi-avplayer-h.md#oh_avplayer_getcurrenttrack) | - | 获取当前有效的轨道索引。请将状态设置为准备/正在播放/暂停/完成。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetMediaKeySystemInfoCallback(OH\_AVPlayer \*player, Player\_MediaKeySystemInfoCallback callback)](capi-avplayer-h.md#oh_avplayer_setmediakeysysteminfocallback) | - | 设置播放器媒体密钥系统信息回调的方法。 |
| [OH\_AVErrCode OH\_AVPlayer\_GetMediaKeySystemInfo(OH\_AVPlayer \*player, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](capi-avplayer-h.md#oh_avplayer_getmediakeysysteminfo) | - | 获取媒体密钥系统信息以创建媒体密钥会话。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetDecryptionConfig(OH\_AVPlayer \*player, MediaKeySession \*mediaKeySession, bool secureVideoPath)](capi-avplayer-h.md#oh_avplayer_setdecryptionconfig) | - | 设置解密信息。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetOnInfoCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnInfoCallback callback, void \*userData)](capi-avplayer-h.md#oh_avplayer_setoninfocallback) | - | 设置播放器消息回调监听函数。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetOnErrorCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnErrorCallback callback, void \*userData)](capi-avplayer-h.md#oh_avplayer_setonerrorcallback) | - | 设置播放器错误回调监听函数。 |
| [OH\_AVFormat \*OH\_AVPlayer\_GetMediaDescription(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_getmediadescription) | - | 获取播放器媒体源信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。  需要注意返回值OH\_AVFormat指针对象的生命周期需要用户手动释放。 |
| [OH\_AVFormat \*OH\_AVPlayer\_GetTrackDescription(OH\_AVPlayer \*player, uint32\_t index)](capi-avplayer-h.md#oh_avplayer_gettrackdescription) | - | 通过索引下标获取播放器媒体源轨道信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。  需要注意返回值OH\_AVFormat指针对象的生命周期需要用户手动释放。 |
| [OH\_AVErrCode OH\_AVPlayer\_AddFdSubtitleSource(OH\_AVPlayer \*player, int32\_t fd, int64\_t offset, int64\_t size)](capi-avplayer-h.md#oh_avplayer_addfdsubtitlesource) | - | 将由文件描述符表示的字幕资源添加到播放器。目前，外挂字幕必须在AVPlayer设置完视频资源的fdSrc之后再设置。 |
| [OH\_AVErrCode OH\_AVPlayer\_AddUrlSubtitleSource(OH\_AVPlayer \*player, const char \*url)](capi-avplayer-h.md#oh_avplayer_addurlsubtitlesource) | - | 将由URL表示的字幕资源添加到播放器。外挂字幕必须在AVPlayer设置完url之后再设置。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackRange(OH\_AVPlayer \*player, int32\_t mSecondsStart, int32\_t mSecondsEnd, bool closestRange)](capi-avplayer-h.md#oh_avplayer_setplaybackrange) | - | 设置播放起始位置和结束位置。设置后，仅播放音视频文件中指定范围内的内容。可在初始化、已准备、暂停、停止或完成状态下调用。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetMediaMuted(OH\_AVPlayer \*player, OH\_MediaType mediaType, bool muted)](capi-avplayer-h.md#oh_avplayer_setmediamuted) | - | 静音媒体流。此API仅可在AVPlayer处于已准备、播放、暂停或已完成状态时调用。 |
| [int32\_t OH\_AVPlayer\_GetPlaybackPosition(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_getplaybackposition) | - | 获取播放位置，精确到毫秒。此API仅可在AVPlayer处于已准备、播放中、暂停或完成状态时调用。 |
| [bool OH\_AVPlayer\_IsSeekContinuousSupported(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_isseekcontinuoussupported) | - | 检查媒体源是否支持连续跳转。在已准备、播放中、暂停或完成状态下调用时返回实际值；在其他状态下调用时返回 false。对于不支持[AV\_SEEK\_CONTINUOUS](capi-avplayer-base-h.md#avplayerseekmode)模式跳转操作的设备，返回false。 |
| [OH\_AVErrCode OH\_AVPlayer\_SelectTrackWithMode(OH\_AVPlayer \*player, int32\_t index, AVPlayerTrackSwitchMode mode)](capi-avplayer-h.md#oh_avplayer_selecttrackwithmode) | - | 在播放包含多个音视频轨道的资源时，使用指定的切换模式选择轨道。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetAmplitudeUpdateCallback(OH\_AVPlayer \*player, OH\_AVPlayerOnAmplitudeUpdateCallback callback, void \*userData)](capi-avplayer-h.md#oh_avplayer_setamplitudeupdatecallback) | - | 订阅最大音频电平值的更新事件，该值在播放音频资源时周期性上报。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetSeiReceivedCallback(OH\_AVPlayer \*player, const int32\_t \*payloadTypes, uint32\_t typeNum, OH\_AVPlayerOnSeiMessageReceivedCallback callback, void \*userData)](capi-avplayer-h.md#oh_avplayer_setseireceivedcallback) | - | 订阅接收到补充增强信息（SEI）消息的事件。仅适用于HTTP-FLV直播流，当视频流中存在SEI消息时触发。必须在调用prepare之前发起订阅。 |
| [uint32\_t OH\_AVSeiMessage\_GetSeiCount(OH\_AVSeiMessageArray \*message)](capi-avplayer-h.md#oh_avseimessage_getseicount) | - | 获取SEI消息数组中的消息项数量。 |
| [OH\_AVFormat \*OH\_AVSeiMessage\_GetSei(OH\_AVSeiMessageArray \*message, uint32\_t index)](capi-avplayer-h.md#oh_avseimessage_getsei) | - | 通过索引获取SEI消息数组中某一项的SEI。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetTargetVideoWindowSize(OH\_AVPlayer \*player, int32\_t width, int32\_t height)](capi-avplayer-h.md#oh_avplayer_settargetvideowindowsize) | - | 为超分辨率设置视频窗口大小。此API可在AVPlayer处于初始化、已准备、播放中、暂停、完成或停止状态时调用。输入参数值必须在320x320至1920x1080（像素）范围内。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetVideoSuperResolutionEnable(OH\_AVPlayer \*player, bool enabled)](capi-avplayer-h.md#oh_avplayer_setvideosuperresolutionenable) | - | 动态启用或禁用超分辨率。此API可在AVPlayer处于初始化、已准备、播放中、暂停、完成或停止状态时调用。必须在调用prepare之前在[OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md)中启用超分辨率功能。 |
| [OH\_AVPlaybackStrategy \*OH\_AVPlaybackStrategy\_Create(void)](capi-avplayer-h.md#oh_avplaybackstrategy_create) | - | 创建一个播放策略实例。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_Destroy(OH\_AVPlaybackStrategy \*strategy)](capi-avplayer-h.md#oh_avplaybackstrategy_destroy) | - | 释放一个播放策略实例。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredWidth(OH\_AVPlaybackStrategy \*strategy, int32\_t width)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredwidth) | - | 选择接近指定宽度的流。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredHeight(OH\_AVPlaybackStrategy \*strategy, int32\_t height)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredheight) | - | 选择接近指定高度的流。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredBufferDuration(OH\_AVPlaybackStrategy \*strategy, int32\_t ms)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredbufferduration) | - | 选择接近指定值的首选缓冲时长。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredHdr(OH\_AVPlaybackStrategy \*strategy, bool enabled)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredhdr) | - | 启用或禁用首选HDR模式。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredSubtitleLanguage(OH\_AVPlaybackStrategy \*strategy, const char \*lang)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredsubtitlelanguage) | - | 设置首选字幕语言。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredAudioLanguage(OH\_AVPlaybackStrategy \*strategy, const char \*lang)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredaudiolanguage) | - | 设置首选音频语言。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetMutedMediaType(OH\_AVPlaybackStrategy \*strategy, OH\_MediaType mediaType)](capi-avplayer-h.md#oh_avplaybackstrategy_setmutedmediatype) | - | 设置播放时要静音的媒体类型。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetShowFirstFrameOnPrepare(OH\_AVPlaybackStrategy \*strategy, bool enabled)](capi-avplayer-h.md#oh_avplaybackstrategy_setshowfirstframeonprepare) | - | 设置是否在prepare时显示首帧。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetThresholdForAutoQuickPlay(OH\_AVPlaybackStrategy \*strategy, double seconds)](capi-avplayer-h.md#oh_avplaybackstrategy_setthresholdforautoquickplay) | - | 设置自动快速播放的阈值。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetSuperResolutionEnable(OH\_AVPlaybackStrategy \*strategy, bool enabled)](capi-avplayer-h.md#oh_avplaybackstrategy_setsuperresolutionenable) | - | 启用或禁用超分辨率。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetPreferredBufferDurationForPlaying(OH\_AVPlaybackStrategy \*strategy, double seconds)](capi-avplayer-h.md#oh_avplaybackstrategy_setpreferredbufferdurationforplaying) | - | 设置播放时的首选缓冲时长（秒，double类型）。 |
| [OH\_AVErrCode OH\_AVPlaybackStrategy\_SetKeepDecodingOnMute(OH\_AVPlaybackStrategy \*strategy, bool enabled)](capi-avplayer-h.md#oh_avplaybackstrategy_setkeepdecodingonmute) | - | 设置静音时是否继续解码。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetPlaybackStrategy(OH\_AVPlayer \*player, OH\_AVPlaybackStrategy \*strategy)](capi-avplayer-h.md#oh_avplayer_setplaybackstrategy) | - | 将播放策略设置给avplayer。此API仅可在avplayer处于初始化状态时调用。 |
| [OH\_AVFormat\* OH\_AVPlayer\_GetPlaybackInfo(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_getplaybackinfo) | - | 获取当前播放器的统计信息。此API仅可在avplayer处于已准备、播放中或暂停状态时调用。 |
| [OH\_AVErrCode OH\_AVPlayer\_SetMediaSource(OH\_AVPlayer \*player, OH\_AVMediaSource \*source)](capi-avplayer-h.md#oh_avplayer_setmediasource) | - | 将OH\_AVMediaSource设置给播放器。 |
| [uint32\_t OH\_AVPlayer\_GetTrackCount(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_gettrackcount) | - | 获取播放器媒体源的轨道数量。 |
| [OH\_AVFormat \*OH\_AVPlayer\_GetTrackFormat(OH\_AVPlayer \*player, uint32\_t trackIndex)](capi-avplayer-h.md#oh_avplayer_gettrackformat) | - | 通过索引获取播放器轨道信息。 |
| [OH\_AVFormat \*OH\_AVPlayer\_GetPlaybackStatisticMetrics(OH\_AVPlayer \*player)](capi-avplayer-h.md#oh_avplayer_getplaybackstatisticmetrics) | - | 获取当前播放器的统计指标信息。设置完播放资源，并且当播放处于准备（prepared）/播放（playing）/暂停（paused）/完成（completed）/停止（stopped）状态时，可调用该接口。  需要注意返回值[OH\_AVFormat](capi-core-oh-avformat.md)指针对象的生命周期需要用户手动释放。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### Player\_MediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Player_MediaKeySystemInfoCallback)(OH_AVPlayer *player, DRM_MediaKeySystemInfo* mediaKeySystemInfo)
```

**描述**

播放器DRM信息更新时调用。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [DRM\_MediaKeySystemInfo](capi-avplayer-drm-mediakeysysteminfo.md)\* mediaKeySystemInfo | DRM信息。 |

### OH\_AVPlayer\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVPlayer *OH_AVPlayer_Create(void)
```

**描述**

创建播放器。

推荐单个应用创建的音视频播放器实例（即音频、视频、音视频三类相加）不超过16个。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \* | 如果创建成功返回指向OH\_AVPlayer实例的指针，否则返回空指针。  可能的失败原因：  1.PlayerFactory::CreatePlayer执行失败。  2.new PlayerObject执行失败。 |

### OH\_AVPlayer\_SetURLSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetURLSource(OH_AVPlayer *player, const char *url)
```

**描述**

设置播放器的播放源。对应的源可以是http url。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| const char \*url | 播放源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：设置成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，url为空或者player SetUrlSource执行失败。 |

### OH\_AVPlayer\_SetFDSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetFDSource(OH_AVPlayer *player, int32_t fd, int64_t offset, int64_t size)
```

**描述**

设置播放器的媒体文件描述符来源。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t fd | 媒体源的文件描述符。 |
| int64\_t offset | 媒体源在文件描述符中的偏移量。 |
| int64\_t size | 表示媒体源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：fd设置成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player SetFdSource执行失败。 |

### OH\_AVPlayer\_SetDataSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetDataSource(OH_AVPlayer *player, OH_AVDataSourceExt* datasrc, void* userData)
```

**描述**

设置播放器的媒体源，该媒体源的数据由应用程序提供。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVDataSourceExt](capi-codecbase-oh-avdatasourceext.md)\* datasrc | 指向自定义媒体数据的指针。 |
| void\* userData | 用户传入的句柄，用于回调中传入。userData若为空，不支持AVPlayer的多实例播放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：设置成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者输入datasrc为空指针。 |

### OH\_AVPlayer\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Prepare(OH_AVPlayer *player)
```

**描述**

准备播放环境，异步缓存媒体数据。

此函数必须在SetSource之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Prepare执行失败。 |

### OH\_AVPlayer\_Play()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Play(OH_AVPlayer *player)
```

**描述**

开始播放。

此函数必须在[OH\_AVPlayer\_Prepare](capi-avplayer-h.md#oh_avplayer_prepare)之后调用。

如果播放器状态为<Prepared>，调用此函数开始播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Play执行失败。 |

### OH\_AVPlayer\_Pause()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Pause(OH_AVPlayer *player)
```

**描述**

暂停播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Pause执行失败。 |

### OH\_AVPlayer\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Stop(OH_AVPlayer *player)
```

**描述**

停止播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Stop执行失败。 |

### OH\_AVPlayer\_Reset()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Reset(OH_AVPlayer *player)
```

**描述**

将播放器恢复到初始状态。

函数调用完成后，调用SetSource添加播放源。调用[OH\_AVPlayer\_Prepare](capi-avplayer-h.md#oh_avplayer_prepare)后，再调用[OH\_AVPlayer\_Play](capi-avplayer-h.md#oh_avplayer_play)重新开始播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Reset执行失败。 |

### OH\_AVPlayer\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Release(OH_AVPlayer *player)
```

**描述**

异步释放播放器资源。

异步释放可以提升性能，但不能确保播放画面的SurfaceBuffer已释放。调用者需要确保播放画面窗口的生命周期安全。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Release执行失败。 |

### OH\_AVPlayer\_ReleaseSync()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_ReleaseSync(OH_AVPlayer *player)
```

**描述**

同步释放播放器资源。

同步过程保证了播放画面的SurfaceBuffer释放，但该过程耗时较长，建议调用者自行设计异步机制。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player ReleaseSync执行失败。 |

### OH\_AVPlayer\_SetVolume()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetVolume(OH_AVPlayer *player, float leftVolume, float rightVolume)
```

**描述**

设置播放器的音量。

可以在播放或暂停的过程中使用。0表示无声音，1为原始值。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| float leftVolume | 要设置的左声道目标音量。 |
| float rightVolume | 要设置的右声道目标音量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置音量。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player SetVolume执行失败。 |

### OH\_AVPlayer\_SetLoudnessGain()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetLoudnessGain(OH_AVPlayer *player, float loudnessGain)
```

**描述**

设置播放器的响度。当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。

默认响度增益0.0dB。播放器流的usage参数必须是[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC，

[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE，[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK 之一。

音频渲染器的延迟模式必须是[OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL。

如果通过高分辨率管道播放，则不支持此操作。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| float loudnessGain | 设置播放器的响度值，单位为dB，响度范围为[-90.0, 24.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置响度。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者输入的loudnessGain是无效参数。  AV\_ERR\_INVALID\_STATE：函数在不正常的状态下调用，或者audioRendererInfo的usage参数不是  [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC，  [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE和  [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK之一。  AV\_ERR\_SERVICE\_DIED：系统错误。 |

### OH\_AVPlayer\_Seek()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_Seek(OH_AVPlayer *player, int32_t mSeconds, AVPlayerSeekMode mode)
```

**描述**

改变播放位置。

此函数可以在播放或暂停时使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t mSeconds | 播放目标位置，精确到毫秒。 |
| [AVPlayerSeekMode](capi-avplayer-base-h.md#avplayerseekmode) mode | 播放器的跳转模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player Seek执行失败。 |

### OH\_AVPlayer\_GetCurrentTime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetCurrentTime(OH_AVPlayer *player, int32_t *currentTime)
```

**描述**

获取播放位置，精确到毫秒。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t \*currentTime | 播放位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取当前播放位置。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player GetCurrentTime执行失败。 |

### OH\_AVPlayer\_GetVideoWidth()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetVideoWidth(OH_AVPlayer *player, int32_t *videoWidth)
```

**描述**

获取视频宽度。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t \*videoWidth | 视频宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取视频宽度。  AV\_ERR\_INVALID\_VAL：输入player为空指针。 |

### OH\_AVPlayer\_GetVideoHeight()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetVideoHeight(OH_AVPlayer *player, int32_t *videoHeight)
```

**描述**

获取视频高度。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t \*videoHeight | 视频高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取视频高度。  AV\_ERR\_INVALID\_VAL：输入player为空指针。 |

### OH\_AVPlayer\_SetPlaybackSpeed()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed speed)
```

**描述**

根据指定的[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)，设置播放器的播放速率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed) speed | 速率模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置播放速率。  AV\_ERR\_INVALID\_VAL：输入player为空指针。 |

### OH\_AVPlayer\_SetPlaybackRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetPlaybackRate(OH_AVPlayer *player, float rate)
```

**描述**

在有效范围内，设置播放器的播放速率。

支持的状态：已准备/正在播放/已暂停/已完成。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| float rate | 播放速率，有效范围是0.125~4。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置播放速率。  AV\_ERR\_OPERATE\_NOT\_PERMIT：如果在不支持的状态下调用或在直播期间调用。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者速率超出范围。 |

### OH\_AVPlayer\_GetPlaybackSpeed()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed *speed)
```

**描述**

获取当前播放器的播放速率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed) \*speed | 速率模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取播放速率。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player GetPlaybackSpeed执行失败。 |

### OH\_AVPlayer\_GetPlaybackRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetPlaybackRate(OH_AVPlayer *player, float *rate)
```

**描述**

获取当前播放器播放速率。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| float \*rate | 可以获得的播放速率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果成功获取当前播放器的播放速率，返回[AV\_ERR\_OK](capi-native-averrors-h.md#oh_averrcode)；  否则返回[native\_averrors.h](capi-native-averrors-h.md)中定义的错误码。 |

### OH\_AVPlayer\_SetAudioRendererInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetAudioRendererInfo(OH_AVPlayer *player, OH_AudioStream_Usage streamUsage)
```

**描述**

设置player音频流类型。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) streamUsage | player音频流设置的类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置音频流类型。  AV\_ERR\_INVALID\_VAL：输入player为空指针或者streamUsage值无效。 |

### OH\_AVPlayer\_SetVolumeMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetVolumeMode(OH_AVPlayer *player, OH_AudioStream_VolumeMode volumeMode)
```

**描述**

设置player音频流音量模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AudioStream\_VolumeMode](capi-native-audiostream-base-h.md#oh_audiostream_volumemode) volumeMode | 指定音频流音量模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置音频流音量模式。  AV\_ERR\_INVALID\_VAL： 输入player为空指针或者volumeMode值无效。  AV\_ERR\_INVALID\_STATE：函数在无效状态下调用，应先处于准备状态。  AV\_ERR\_SERVICE\_DIED：系统错误。 |

### OH\_AVPlayer\_SetAudioInterruptMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetAudioInterruptMode(OH_AVPlayer *player, OH_AudioInterrupt_Mode interruptMode)
```

**描述**

设置player音频流的打断模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AudioInterrupt\_Mode](capi-native-audiostream-base-h.md#oh_audiointerrupt_mode) interruptMode | player音频流使用的打断模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置音频流的打断模式。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者interruptMode值无效。 |

### OH\_AVPlayer\_SetAudioEffectMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetAudioEffectMode(OH_AVPlayer *player, OH_AudioStream_AudioEffectMode effectMode)
```

**描述**

设置player音频流的音效模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AudioStream\_AudioEffectMode](capi-native-audiostream-base-h.md#oh_audiostream_audioeffectmode) effectMode | player音频流使用的音效模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置音频流的音效模式。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者effectMode值无效。 |

### OH\_AVPlayer\_SelectBitRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SelectBitRate(OH_AVPlayer *player, uint32_t bitRate)
```

**描述**

设置hls播放器使用的码率。仅对HLS协议网络流有效。

默认情况下，播放器会根据网络连接情况选择合适的码率和速度。

通过INFO\_TYPE\_BITRATE\_COLLECT上报有效码率链表，设置并选择指定的码率，选择小于且最接近的码率。准备好后，读取以查询当前选择的比特率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| uint32\_t bitRate | 码率，单位为bps。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置码率。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player SelectBitRate执行失败。 |

### OH\_AVPlayer\_SetVideoSurface()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetVideoSurface(OH_AVPlayer *player, OHNativeWindow *window)
```

**描述**

设置播放画面窗口。

此函数必须在SetSource之后，Prepare之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OHNativeWindow](capi-codecbase-nativewindow.md) \*window | 指向OHNativeWindow实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置播放画面窗口。  AV\_ERR\_INVALID\_VAL：输入player为空指针，输入window为空指针或者player SetVideoSurface执行失败。 |

### OH\_AVPlayer\_GetDuration()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetDuration(OH_AVPlayer *player, int32_t *duration)
```

**描述**

获取媒体文件的总时长，精确到毫秒。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t \*duration | 媒体文件的总时长。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取媒体文件时长。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player GetDuration执行失败。 |

### OH\_AVPlayer\_GetState()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetState(OH_AVPlayer *player, AVPlayerState *state)
```

**描述**

获取当前播放状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlayerState](capi-avplayer-base-h.md#avplayerstate) \*state | 当前播放状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取当前播放状态。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player GetState执行失败。 |

### OH\_AVPlayer\_IsPlaying()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVPlayer_IsPlaying(OH_AVPlayer *player)
```

**描述**

判断播放器是否在播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果正在播放，则返回true；如果不在播放或者输入player为空指针则返回false。 |

### OH\_AVPlayer\_IsLooping()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVPlayer_IsLooping(OH_AVPlayer *player)
```

**描述**

判断是否循环播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果是循环播放，则返回true；如果不是循环播放或者输入player为空指针则返回false。 |

### OH\_AVPlayer\_SetLooping()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetLooping(OH_AVPlayer *player, bool loop)
```

**描述**

设置循环播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| bool loop | 循环播放开关。true表示开启循环播放，false表示关闭循环播放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置循环播放。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player SetLooping执行失败。 |

### OH\_AVPlayer\_SetPlayerCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetPlayerCallback(OH_AVPlayer *player, AVPlayerCallback callback)
```

**描述**

设置播放器回调函数。

由于通过此方法设置的信息监听回调函数[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)和错误监听回调函数[OH\_AVPlayerOnError](capi-avplayer-base-h.md#oh_avplayeronerror)可以传递的信息有限，也不便于应用区分多个播放器实例。

从API version 12开始，应使用[OH\_AVPlayer\_SetOnInfoCallback](capi-avplayer-h.md#oh_avplayer_setoninfocallback)、[OH\_AVPlayer\_SetOnErrorCallback](capi-avplayer-h.md#oh_avplayer_setonerrorcallback)接口分别设置信息监听回调函数[OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)和错误监听回调函数[OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback)。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH\_AVPlayer\_SetOnInfoCallback](capi-avplayer-h.md#oh_avplayer_setoninfocallback),[OH\_AVPlayer\_SetOnErrorCallback](capi-avplayer-h.md#oh_avplayer_setonerrorcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlayerCallback](capi-avplayer-avplayercallback.md) callback | 回调对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功设置播放器回调。  AV\_ERR\_INVALID\_VAL：输入player为空指针，callback.onInfo或onError为空，或者player SetPlayerCallback执行失败。 |

### OH\_AVPlayer\_SelectTrack()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SelectTrack(OH_AVPlayer *player, int32_t index)
```

**描述**

选择音频或字幕轨道。

默认播放第一个带数据的音轨，不播放字幕轨道。

设置生效后，原音轨将失效。请设置字幕处于准备/播放/暂停/完成状态，并将音轨设置为准备状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t index | 索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player SelectTrack执行失败。 |

### OH\_AVPlayer\_DeselectTrack()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_DeselectTrack(OH_AVPlayer *player, int32_t index)
```

**描述**

取消选择当前音频或字幕轨道。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t index | 索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player DeselectTrack执行失败。 |

### OH\_AVPlayer\_GetCurrentTrack()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetCurrentTrack(OH_AVPlayer *player, int32_t trackType, int32_t *index)
```

**描述**

获取当前有效的轨道索引。请将状态设置为准备/正在播放/暂停/完成。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t trackType | 媒体类型。0：音频，1：视频。 |
| int32\_t \*index | 索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：成功获取轨道索引。  AV\_ERR\_INVALID\_VAL：输入player为空指针，或者player GetCurrentTrack执行失败。 |

### OH\_AVPlayer\_SetMediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetMediaKeySystemInfoCallback(OH_AVPlayer *player, Player_MediaKeySystemInfoCallback callback)
```

**描述**

设置播放器媒体密钥系统信息回调的方法。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [Player\_MediaKeySystemInfoCallback](capi-avplayer-h.md#player_mediakeysysteminfocallback) callback | 对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针，callback为空指针，player SetDrmSystemInfoCallback，  SetDrmSystemInfoCallback或SetDrmSystemInfoCallback执行失败。 |

### OH\_AVPlayer\_GetMediaKeySystemInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_GetMediaKeySystemInfo(OH_AVPlayer *player, DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

获取媒体密钥系统信息以创建媒体密钥会话。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [DRM\_MediaKeySystemInfo](capi-avplayer-drm-mediakeysysteminfo.md) \*mediaKeySystemInfo | 媒体密钥系统信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针或者内存不足。 |

### OH\_AVPlayer\_SetDecryptionConfig()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetDecryptionConfig(OH_AVPlayer *player, MediaKeySession *mediaKeySession, bool secureVideoPath)
```

**描述**

设置解密信息。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [MediaKeySession](capi-avplayer-mediakeysession.md) \*mediaKeySession | 具有解密功能的媒体密钥会话实例。 |
| bool secureVideoPath | 是否需要安全解码器。true表示需要安全解码器，false表示不需要安全解码器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入player为空指针或者player SetDecryptionConfig执行失败。 |

### OH\_AVPlayer\_SetOnInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetOnInfoCallback(OH_AVPlayer *player, OH_AVPlayerOnInfoCallback callback, void *userData)
```

**描述**

设置播放器消息回调监听函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback) callback | 执行回调监听函数的指针，空指针表示取消设置播放器消息回调监听。 |
| void \*userData | 指向应用调用者设置的实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：内存分配失败。  AV\_ERR\_INVALID\_VAL： 输入player为空指针或者函数执行失败。 |

### OH\_AVPlayer\_SetOnErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetOnErrorCallback(OH_AVPlayer *player, OH_AVPlayerOnErrorCallback callback, void *userData)
```

**描述**

设置播放器错误回调监听函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback) callback | 执行回调监听函数的指针，空指针表示取消设置播放器错误回调监听。 |
| void \*userData | 指向应用调用者设置的实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：内存分配失败。  AV\_ERR\_INVALID\_VAL： 输入player为空指针或者函数执行失败。 |

### OH\_AVPlayer\_GetMediaDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVPlayer_GetMediaDescription(OH_AVPlayer *player)
```

**描述**

获取播放器媒体源信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

需要注意返回值OH\_AVFormat指针对象的生命周期需要用户手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 执行成功返回播放器媒体信息，否则返回nullptr。  可能故障原因：  1. 传入player指针不合法。  2. 设置的播放资源不合法。 |

### OH\_AVPlayer\_GetTrackDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVPlayer_GetTrackDescription(OH_AVPlayer *player, uint32_t index)
```

**描述**

通过索引下标获取播放器媒体源轨道信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

需要注意返回值OH\_AVFormat指针对象的生命周期需要用户手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| uint32\_t index | 轨道索引下标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 执行成功按索引下标返回轨道信息，否则返回nullptr。  可能故障原因：  1. 传入player指针不合法。  2. 设置的播放资源不合法。  3. 轨道索引下标超出播放源文件数组界限。 |

### OH\_AVPlayer\_AddFdSubtitleSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_AddFdSubtitleSource(OH_AVPlayer *player, int32_t fd, int64_t offset, int64_t size)
```

**描述**

将由文件描述符表示的字幕资源添加到播放器。目前，外挂字幕必须在AVPlayer设置完视频资源的fdSrc之后再设置。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t fd | 字幕源的文件描述符。 |
| int64\_t offset | 文件描述符中媒体源的偏移量。 |
| int64\_t size | 媒体源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。 |

### OH\_AVPlayer\_AddUrlSubtitleSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_AddUrlSubtitleSource(OH_AVPlayer *player, const char *url)
```

**描述**

将由URL表示的字幕资源添加到播放器。外挂字幕必须在AVPlayer设置完url之后再设置。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| const char \*url | 字幕源的URL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。 |

### OH\_AVPlayer\_SetPlaybackRange()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetPlaybackRange(OH_AVPlayer *player, int32_t mSecondsStart, int32_t mSecondsEnd, bool closestRange)
```

**描述**

设置播放起始位置和结束位置。设置后，仅播放音视频文件中指定范围内的内容。可在初始化、已准备、暂停、停止或完成状态下调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t mSecondsStart | 播放起始位置，应在[0, duration)范围内，-1 表示未设置起始位置，将从0开始播放。 |
| int32\_t mSecondsEnd | 播放结束位置，通常应在(startTimeMs, duration]范围内，-1 表示未设置结束位置，将在流末尾结束播放。 |
| bool closestRange | 是否同步到距离指定时间点最近的帧。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。 |

### OH\_AVPlayer\_SetMediaMuted()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetMediaMuted(OH_AVPlayer *player, OH_MediaType mediaType, bool muted)
```

**描述**

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype) mediaType | 指定的媒体类型，参见[native\_avcodec\_base.h](capi-native-avcodec-base-h.md)中的[OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype)。 |
| bool muted | true表示静音，false表示取消静音。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。 |

### OH\_AVPlayer\_GetPlaybackPosition()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_AVPlayer_GetPlaybackPosition(OH_AVPlayer *player)
```

**描述**

获取播放位置，精确到毫秒。此API仅可在AVPlayer处于已准备、播放中、暂停或完成状态时调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回以毫秒为单位的播放位置。  若player为空指针或无效，则返回-1。 |

### OH\_AVPlayer\_IsSeekContinuousSupported()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVPlayer_IsSeekContinuousSupported(OH_AVPlayer *player)
```

**描述**

检查媒体源是否支持连续跳转。在已准备、播放中、暂停或完成状态下调用时返回实际值；在其他状态下调用时返回 false。对于不支持[AV\_SEEK\_CONTINUOUS](capi-avplayer-base-h.md#avplayerseekmode)模式跳转操作的设备，返回false。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | @returns true表示支持连续跳转。  false表示不支持连续跳转或支持状态不确定。 |

### OH\_AVPlayer\_SelectTrackWithMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SelectTrackWithMode(OH_AVPlayer *player, int32_t index, AVPlayerTrackSwitchMode mode)
```

**描述**

在播放包含多个音视频轨道的资源时，使用指定的切换模式选择轨道。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t index | 所选轨道的索引。 |
| [AVPlayerTrackSwitchMode](capi-avplayer-base-h.md#avplayertrackswitchmode) mode | 切换模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。 |

### OH\_AVPlayer\_SetAmplitudeUpdateCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetAmplitudeUpdateCallback(OH_AVPlayer *player, OH_AVPlayerOnAmplitudeUpdateCallback callback, void *userData)
```

**描述**

订阅最大音频电平值的更新事件，该值在播放音频资源时周期性上报。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVPlayerOnAmplitudeUpdateCallback](capi-avplayer-base-h.md#oh_avplayeronamplitudeupdatecallback) callback | 回调函数指针，nullptr表示取消注册回调。 |
| void \*userData | 指向用户特定数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。 |

### OH\_AVPlayer\_SetSeiReceivedCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetSeiReceivedCallback(OH_AVPlayer *player, const int32_t *payloadTypes, uint32_t typeNum, OH_AVPlayerOnSeiMessageReceivedCallback callback, void *userData)
```

**描述**

订阅接收到补充增强信息（SEI）消息的事件。仅适用于HTTP-FLV直播流，当视频流中存在SEI消息时触发。必须在调用prepare之前发起订阅。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| const int32\_t \*payloadTypes | 负载类型数组。 |
| uint32\_t typeNum | 负载类型数组的大小。 |
| [OH\_AVPlayerOnSeiMessageReceivedCallback](capi-avplayer-base-h.md#oh_avplayeronseimessagereceivedcallback) callback | 回调函数指针，nullptr表示取消注册回调。 |
| void \*userData | 指向用户特定数据的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。 |

### OH\_AVSeiMessage\_GetSeiCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_AVSeiMessage_GetSeiCount(OH_AVSeiMessageArray *message)
```

**描述**

获取SEI消息数组中的消息项数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVSeiMessageArray \*message | 指向OH\_AVSeiMessageArray实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | SEI消息数组中的消息项数量。 |

### OH\_AVSeiMessage\_GetSei()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVSeiMessage_GetSei(OH_AVSeiMessageArray *message, uint32_t index)
```

**描述**

通过索引获取SEI消息数组中某一项的SEI。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVSeiMessageArray \*message | 指向OH\_AVSeiMessageArray实例的指针。 |
| uint32\_t index | 消息项的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 该消息项的SEI。 |

### OH\_AVPlayer\_SetTargetVideoWindowSize()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetTargetVideoWindowSize(OH_AVPlayer *player, int32_t width, int32_t height)
```

**描述**

为超分辨率设置视频窗口大小。此API可在AVPlayer处于初始化、已准备、播放中、暂停、完成或停止状态时调用。输入参数值必须在320x320至1920x1080（像素）范围内。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t width | 窗口宽度，取值范围[320-1920]，单位：像素。 |
| int32\_t height | 窗口高度，取值范围[320-1080]，单位：像素。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针或参数错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。  AV\_ERR\_SUPER\_RESOLUTION\_UNSUPPORTED：表示不支持超分辨率。  AV\_ERR\_SUPER\_RESOLUTION\_NOT\_ENABLED：表示未在[OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md)中启用超分辨率功能。 |

### OH\_AVPlayer\_SetVideoSuperResolutionEnable()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetVideoSuperResolutionEnable(OH_AVPlayer *player, bool enabled)
```

**描述**

动态启用或禁用超分辨率。此API可在AVPlayer处于初始化、已准备、播放中、暂停、完成或停止状态时调用。必须在调用prepare之前在[OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md)中启用超分辨率功能。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| bool enabled | true：启用超分辨率；false：禁用超分辨率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针或参数错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。  AV\_ERR\_SUPER\_RESOLUTION\_UNSUPPORTED：表示不支持超分辨率。  AV\_ERR\_SUPER\_RESOLUTION\_NOT\_ENABLED：表示未在[OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md)中启用超分辨率功能。 |

### OH\_AVPlaybackStrategy\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVPlaybackStrategy *OH_AVPlaybackStrategy_Create(void)
```

**描述**

创建一个播放策略实例。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVPlaybackStrategy \*](capi-avplayer-oh-avplaybackstrategy.md) | 一个播放策略实例，失败时返回空指针。 |

### OH\_AVPlaybackStrategy\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_Destroy(OH_AVPlaybackStrategy *strategy)
```

**描述**

释放一个播放策略实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | OH\_AVPlaybackStrategy实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredWidth()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredWidth(OH_AVPlaybackStrategy *strategy, int32_t width)
```

**描述**

选择接近指定宽度的流。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | avplayer使用的OH\_AVPlaybackStrategy。 |
| int32\_t width | avplayer启动时选择播放的首选宽度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredHeight()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredHeight(OH_AVPlaybackStrategy *strategy, int32_t height)
```

**描述**

选择接近指定高度的流。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | avplayer使用的OH\_AVPlaybackStrategy。 |
| int32\_t height | avplayer启动时选择播放的首选高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredBufferDuration()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredBufferDuration(OH_AVPlaybackStrategy *strategy, int32_t ms)
```

**描述**

选择接近指定值的首选缓冲时长。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | avplayer使用的OH\_AVPlaybackStrategy。 |
| int32\_t ms | avplayer启动时选择播放的首选缓冲时长。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredHdr()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredHdr(OH_AVPlaybackStrategy *strategy, bool enabled)
```

**描述**

启用或禁用首选HDR模式。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| bool enabled | true表示启用HDR，false表示禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredSubtitleLanguage()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredSubtitleLanguage(OH_AVPlaybackStrategy *strategy, const char *lang)
```

**描述**

设置首选字幕语言。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| const char \*lang | 字幕语言代码（例如"zh"）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredAudioLanguage()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredAudioLanguage(OH_AVPlaybackStrategy *strategy, const char *lang)
```

**描述**

设置首选音频语言。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| const char \*lang | 音频语言代码（例如"en"）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetMutedMediaType()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetMutedMediaType(OH_AVPlaybackStrategy *strategy, OH_MediaType mediaType)
```

**描述**

设置播放时要静音的媒体类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| [OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype) mediaType | 要静音的媒体类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetShowFirstFrameOnPrepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetShowFirstFrameOnPrepare(OH_AVPlaybackStrategy *strategy, bool enabled)
```

**描述**

设置是否在prepare时显示首帧。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| bool enabled | true表示显示，false表示不显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetThresholdForAutoQuickPlay()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetThresholdForAutoQuickPlay(OH_AVPlaybackStrategy *strategy, double seconds)
```

**描述**

设置自动快速播放的阈值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| double seconds | 自动快速播放的阈值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetSuperResolutionEnable()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetSuperResolutionEnable(OH_AVPlaybackStrategy *strategy, bool enabled)
```

**描述**

启用或禁用超分辨率。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| bool enabled | true表示启用，false表示禁用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetPreferredBufferDurationForPlaying()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetPreferredBufferDurationForPlaying(OH_AVPlaybackStrategy *strategy, double seconds)
```

**描述**

设置播放时的首选缓冲时长（秒，double类型）。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| double seconds | 缓冲时长（秒）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlaybackStrategy\_SetKeepDecodingOnMute()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlaybackStrategy_SetKeepDecodingOnMute(OH_AVPlaybackStrategy *strategy, bool enabled)
```

**描述**

设置静音时是否继续解码。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 指向OH\_AVPlaybackStrategy的指针。 |
| bool enabled | true表示继续解码，false表示静音时暂停解码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的strategy为空指针。 |

### OH\_AVPlayer\_SetPlaybackStrategy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetPlaybackStrategy(OH_AVPlayer *player, OH_AVPlaybackStrategy *strategy)
```

**描述**

将播放策略设置给avplayer。此API仅可在avplayer处于初始化状态时调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) \*strategy | 播放策略实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player为空指针。  AV\_ERR\_OPERATE\_NOT\_PERMIT：表示操作不允许。 |

### OH\_AVPlayer\_GetPlaybackInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat* OH_AVPlayer_GetPlaybackInfo(OH_AVPlayer *player)
```

**描述**

获取当前播放器的统计信息。此API仅可在avplayer处于已准备、播放中或暂停状态时调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat\*](capi-core-oh-avformat.md) | 返回指向OH\_AVFormat实例的指针。  若player为空指针或无效，则返回空指针。 |

### OH\_AVPlayer\_SetMediaSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVPlayer_SetMediaSource(OH_AVPlayer *player, OH_AVMediaSource *source)
```

**描述**

将OH\_AVMediaSource设置给播放器。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) \*source | 媒体源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：表示输入的player或者source为空指针，或player设置URL源失败。 |

### OH\_AVPlayer\_GetTrackCount()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_AVPlayer_GetTrackCount(OH_AVPlayer *player)
```

**描述**

获取播放器媒体源的轨道数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回轨道数量。 |

### OH\_AVPlayer\_GetTrackFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVPlayer_GetTrackFormat(OH_AVPlayer *player, uint32_t trackIndex)
```

**描述**

通过索引获取播放器轨道信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| uint32\_t trackIndex | 轨道数组索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 返回指向OH\_AVFormat实例的指针。  若player为空指针或无效，或trackIndex无效，则返回空指针。 |

### OH\_AVPlayer\_GetPlaybackStatisticMetrics()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVPlayer_GetPlaybackStatisticMetrics(OH_AVPlayer *player)
```

**描述**

获取当前播放器的统计指标信息。设置完播放资源，并且当播放处于准备（prepared）/播放（playing）/暂停（paused）/完成（completed）/停止（stopped）状态时，可调用该接口。

需要注意返回值[OH\_AVFormat](capi-core-oh-avformat.md)指针对象的生命周期需要用户手动释放。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 执行成功返回播放器的统计指标信息（键值详情请参考avplayer\_base.h中的[变量](capi-avplayer-base-h.md#变量)信息），否则返回nullptr。  可能的失败原因：传入player指针不合法。 |
