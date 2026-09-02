---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo
title: Class (NativeMediaPlayerSurfaceInfo)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (NativeMediaPlayerSurfaceInfo)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0293d835e69c985c0164ed790653755b5cd44653658a2d72126b2a59782a91b9
---

NativeMediaPlayerSurfaceInfo 使用[enableNativeMediaPlayer](arkts-basic-components-web-attributes.md#enablenativemediaplayer12)来进行同层渲染的 surface 信息配置。该类允许应用接管网页媒体播放功能，通过配置 surface 的 id 和位置信息，实现网页媒体内容与应用界面的同层渲染融合，提升媒体播放体验。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id12+ | string | 否 | 否 | surface的id，用于同层渲染的NativeImage的surfaceId。  详见[NativeEmbedDataInfo](arkts-basic-components-web-i.md#nativeembeddatainfo11)。 |
| rect12+ | [RectEvent](arkts-apis-webview-i.md#rectevent12) | 否 | 否 | surface的位置信息，用于指定同层渲染时surface的显示位置和尺寸。 |
