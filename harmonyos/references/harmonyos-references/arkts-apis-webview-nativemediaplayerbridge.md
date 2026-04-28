---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerbridge
title: Interface (NativeMediaPlayerBridge)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Interface (NativeMediaPlayerBridge)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:10+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:28d4f0eb066000b16149c079d0072e181586d663aa079a4825affd0294e066d7
---

[CreateNativeMediaPlayerCallback](arkts-apis-webview-t.md#createnativemediaplayercallback12)回调函数的返回值类型。接管网页媒体的播放器和ArkWeb内核之间的一个接口类。

ArkWeb内核通过该接口类的实例对象来控制应用创建的用来接管网页媒体的播放器。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Interface首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## updateRect12+

PhonePC/2in1TabletTVWearable

updateRect(x: number, y: number, width: number, height: number): void

更新surface位置信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | surface相对于Web组件的x坐标信息。 |
| y | number | 是 | surface相对于Web组件的y坐标信息。 |
| width | number | 是 | surface的宽度。  单位：像素。 |
| height | number | 是 | surface的高度。  单位：像素。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## play12+

PhonePC/2in1TabletTVWearable

play(): void

播放视频。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## pause12+

PhonePC/2in1TabletTVWearable

pause(): void

暂停播放。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## seek12+

PhonePC/2in1TabletTVWearable

seek(targetTime: number): void

播放跳转到某个时间点。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetTime | number | 是 | 播放跳转到的时间点。  单位：秒。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## setVolume12+

PhonePC/2in1TabletTVWearable

setVolume(volume: number): void

设置播放器音量值。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 播放器的音量。  取值范围：[0, 1.0]，其中0表示静音，1.0表示最大音量。 |

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## setMuted12+

PhonePC/2in1TabletTVWearable

setMuted(muted: boolean): void

设置静音状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| muted | boolean | 是 | 是否静音。  true表示静音，false表示未静音。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## setPlaybackRate12+

PhonePC/2in1TabletTVWearable

setPlaybackRate(playbackRate: number): void

设置播放速度。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| playbackRate | number | 是 | 播放倍率。  取值范围: [0, 10.0]，其中1表示原速播放。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## release12+

PhonePC/2in1TabletTVWearable

release(): void

销毁播放器。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## enterFullscreen12+

PhonePC/2in1TabletTVWearable

enterFullscreen(): void

播放器进入全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## exitFullscreen12+

PhonePC/2in1TabletTVWearable

exitFullscreen(): void

播放器退出全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## resumePlayer12+

PhonePC/2in1TabletTVWearable

resumePlayer?(): void

通知应用重建应用内播放器，并恢复应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。

## suspendPlayer12+

PhonePC/2in1TabletTVWearable

suspendPlayer?(type: SuspendType): void

通知应用销毁应用内播放器，并保存应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SuspendType](arkts-apis-webview-e.md#suspendtype12) | 是 | 播放器挂起类型。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。
