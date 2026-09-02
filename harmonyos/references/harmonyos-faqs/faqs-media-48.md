---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-48
title: AVPlayer运行实例数量限制
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer运行实例数量限制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ebe4cbc2341c044bc9fd75275c3b027cddd8fdbeae69af58630e06a9615bf0f7
---

## 问题现象

AVPlayer音视频播放器创建实例是否有数量限制，创建多个AVPlayer同时运行，超过一定数量后会报错。

## 解决方案

通过[media.createAVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)接口创建AVPlayer实例本身并无数量限制，但是AVPlayer创建完成后，调用[prepare](../harmonyos-references/arkts-apis-media-avplayer.md#prepare9)接口准备播放音频/视频后，播放引擎处于工作状态（AVPlayer处于prepared/playing/paused/completed状态），会占用进程或系统硬件资源，当进程或系统硬件的资源被耗尽后，再次调用prepare准备播放会失败报错。

1. 当AVPlayer播放音频和低分辨率视频时，会占用进程的音频流资源，当进程的音频流资源被耗尽后，AVPlayer再次调用prepare进入工作状态时会报错。
2. 当AVPlayer播放高分辨率视频时，会占用系统硬件解码器资源，当硬件解码器资源被耗尽后，AVPlayer再次调用prepare进入工作状态时会报错。

## 总结

AVPlayer进入工作状态后会占用进程或系统硬件资源，当多个AVPlayer同时处于工作状态耗尽进程或系统硬件资源后，后续创建AVPlayer并运行会失败报错。因此，需要尽量复用AVPlayer实现音视频播放，不要同时运行过多AVPlayer实例。
