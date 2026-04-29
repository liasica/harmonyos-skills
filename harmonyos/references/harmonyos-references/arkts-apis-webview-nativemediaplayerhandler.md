---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerhandler
title: Interface (NativeMediaPlayerHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Interface (NativeMediaPlayerHandler)
category: harmonyos-references
scraped_at: 2026-04-29T13:55:39+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:98a16aa98eb7a568e28f0f5a3fdee90260bb7c79f3987bd862bd94d9cc070df5
---

[CreateNativeMediaPlayerCallback](arkts-apis-webview-t.md#createnativemediaplayercallback12)回调函数的参数。应用通过该对象，将播放器的状态通知给 ArkWeb 内核。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Interface首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## handleStatusChanged12+

PhonePC/2in1TabletTVWearable

handleStatusChanged(status: PlaybackStatus): void

当播放器的播放状态发生变化时，调用该方法将播放状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| status | [PlaybackStatus](arkts-apis-webview-e.md#playbackstatus12) | 是 | 播放器的播放状态。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleVolumeChanged12+

PhonePC/2in1TabletTVWearable

handleVolumeChanged(volume: number): void

当播放器的音量发生变化时，调用该方法将音量通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 播放器的音量，取值范围：[0, 1.0]。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleMutedChanged12+

PhonePC/2in1TabletTVWearable

handleMutedChanged(muted: boolean): void

当播放器的静音状态发生变化时，调用该方法将静音状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muted | boolean | 是 | 当前播放器是否静音。  true表示当前播放器静音，false表示当前播放器未静音。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handlePlaybackRateChanged12+

PhonePC/2in1TabletTVWearable

handlePlaybackRateChanged(playbackRate: number): void

当播放器的播放速率发生变化时，调用该方法将播放速率通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| playbackRate | number | 是 | 播放速率，取值范围：[0, +∞) |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleDurationChanged12+

PhonePC/2in1TabletTVWearable

handleDurationChanged(duration: number): void

当播放器解析出媒体的总时长时，调用该方法将媒体的总时长通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 媒体的总时长。  单位：秒，取值范围：[0, +∞) |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleTimeUpdate12+

PhonePC/2in1TabletTVWearable

handleTimeUpdate(currentPlayTime: number): void

当媒体的播放进度发生变化时，调用该方法将媒体的播放进度通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentPlayTime | number | 是 | 当前播放时间。  单位：秒，取值范围：[0, duration] |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleBufferedEndTimeChanged12+

PhonePC/2in1TabletTVWearable

handleBufferedEndTimeChanged(bufferedEndTime: number): void

当媒体的缓冲时长发生变化时，调用该方法将媒体的缓冲时长通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bufferedEndTime | number | 是 | 媒体缓冲的时长。  单位：秒，取值范围：[0, duration] |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleEnded12+

PhonePC/2in1TabletTVWearable

handleEnded(): void

当媒体播放结束时，调用该方法将播放结束事件通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleNetworkStateChanged12+

PhonePC/2in1TabletTVWearable

handleNetworkStateChanged(state: NetworkState): void

当播放器的网络状态发生变化时，调用该方法将播放器的网络状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [NetworkState](arkts-apis-webview-e.md#networkstate12) | 是 | 播放器的网络状态。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleReadyStateChanged12+

PhonePC/2in1TabletTVWearable

handleReadyStateChanged(state: ReadyState): void

当播放器的缓存状态发生变化时，调用该方法将播放器的缓存状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [ReadyState](arkts-apis-webview-e.md#readystate12) | 是 | 播放器的缓存状态。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleFullscreenChanged12+

PhonePC/2in1TabletTVWearable

handleFullscreenChanged(fullscreen: boolean): void

当播放器的全屏状态发生变化时，调用该方法将播放器的全屏状态通知给 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullscreen | boolean | 是 | 是否全屏。  true表示全屏，false表示未全屏。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleSeeking12+

PhonePC/2in1TabletTVWearable

handleSeeking(): void

当播放器进入seek状态时，调用该方法将seek进入事件通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleSeekFinished12+

PhonePC/2in1TabletTVWearable

handleSeekFinished(): void

当播放器seek完成后，调用该方法将seek完成事件通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleError12+

PhonePC/2in1TabletTVWearable

handleError(error: MediaError, errorMessage: string): void

当播放器发生错误时，调用该方法将错误通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [MediaError](arkts-apis-webview-e.md#mediaerror12) | 是 | 错误类型。 |
| errorMessage | string | 是 | 错误的详细描述。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## handleVideoSizeChanged12+

PhonePC/2in1TabletTVWearable

handleVideoSizeChanged(width: number, height: number): void

当播放器解析出视频的尺寸时， 调用该方法将视频尺寸通知 ArkWeb 内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 视频的宽，单位：像素，取值范围：[0, +∞) |
| height | number | 是 | 视频的高，单位：像素，取值范围：[0, +∞) |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。
