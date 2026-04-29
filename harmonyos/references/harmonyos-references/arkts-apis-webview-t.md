---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-t
title: Types
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Types
category: harmonyos-references
scraped_at: 2026-04-29T13:55:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:80ce2f398cd5ecc66a6c990dd9945f6d4bdab7b00d92f39933049d03faaf754d
---

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 示例效果请以真机运行为准。

## WebMessage

PhonePC/2in1TabletTVWearable

type WebMessage = ArrayBuffer | string

用于描述[WebMessagePort](arkts-apis-webview-webmessageport.md)所支持的数据类型。

**系统能力：** SystemCapability.Web.Webview.Core

| 类型 | 说明 |
| --- | --- |
| string | 字符串类型数据。 |
| ArrayBuffer | 二进制类型数据。 |

## OnProxyConfigChangeCallback15+

PhonePC/2in1TabletTVWearable

type OnProxyConfigChangeCallback = () => void

回调函数，回调成功表示代理设置成功。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

完整示例代码参考[removeProxyOverride](arkts-apis-webview-proxycontroller.md#removeproxyoverride15)。

## CreateNativeMediaPlayerCallback12+

PhonePC/2in1TabletTVWearable

type CreateNativeMediaPlayerCallback = (handler: NativeMediaPlayerHandler, mediaInfo: MediaInfo) => NativeMediaPlayerBridge

[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)方法的参数。一个回调函数，创建一个播放器，用于接管网页中的媒体播放。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [NativeMediaPlayerHandler](arkts-apis-webview-nativemediaplayerhandler.md) | 是 | 通过该对象，将播放器的状态报告给 ArkWeb 内核。 |
| mediaInfo | [MediaInfo](arkts-apis-webview-i.md#mediainfo12) | 是 | 网页媒体的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NativeMediaPlayerBridge](arkts-apis-webview-nativemediaplayerbridge.md) | 接管网页媒体的播放器和 ArkWeb 内核之间的一个接口类。  应用需要实现该接口类。  ArkWeb 内核通过该接口类的对象来控制应用创建的用来接管网页媒体的播放器。  如果应用返回了 null，则表示应用不接管这个媒体的播放，由 ArkWeb 内核来播放该媒体。 |

**示例：**

完整示例代码参考[onCreateNativeMediaPlayer](arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)。
