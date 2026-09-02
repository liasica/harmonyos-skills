---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-37
title: Video组件是否可以设置User-Agent
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > Video组件是否可以设置User-Agent
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0ad06f963f0b3c9779da1030ed51c184aa8c859f139c84e4fc4cd34be9062762
---

## 问题现象

在视频播放Video组件中，是否支持自定义设置用户代理User-Agent属性？

## 解决方案

不可以，[Video组件目前只能显示固定网络地址的视频](../harmonyos-guides/arkts-common-components-video-player.md#加载网络视频)，不能进行添加请求头等复杂操作。目前AVPlayer可以设置User-Agent，[通过创建mediaSource实例对象，设置媒体来源，定制HTTP请求，以键值对的形式设置User-Agent、Cookie、Referer等字段。](../harmonyos-guides/playback-url-setting-method.md#流媒体播放场景下设置url)另外，三方库[@ohos/ijkplayer](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fijkplayer)也可以设置User-Agent。
