---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-24
title: 接入AVSession后播控中心没有显示
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 接入AVSession后播控中心没有显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a2987efd6bae65b7741438bfd492fd847d9665a16763b8344b91b8b62db02ea8
---

## 问题现象

音视频应用接入本地媒体会话（AVSession）后，在播控中心没有显示。

## 解决方案

播控中心的正常展示需要音视频应用正确接入媒体会话。‘

对于媒体类应用接入[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)场景：

* 媒体类应用创建AVSession时需要选择会话类型（[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)）为'audio'或者'video'。
* 在创建完成AVSession后，还必须要设元数据（[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)），并至少注册一个控制命令（播放、暂停等），播控中心才能正常显示。

对于通话类应用接入AVSession场景：

* 通话类应用创建AVSession时需要选择会话类型（AVSessionType）为“voice\_call”或“video\_call”。
* 在6.0之前通话类应用接入AVSession不会在播控中心展示。在6.0之后，当应用在应用市场上架为通讯类应用时，可以在播控中心显示正在通话中，且可以使用播控中心的投播组件进行通话设备切换。

音视频应用接入AVSession的流程可参考：[应用接入AVSession](../harmonyos-guides/avsession-access-scene.md)。
