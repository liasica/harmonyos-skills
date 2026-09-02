---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-22
title: 使用AudioRenderer播放音频时，如何跳转到指定播放位置
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 使用AudioRenderer播放音频时，如何跳转到指定播放位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:852c9a6f581253a0588d471729fad8cfc8beec413fccd312bde4b49cec464905
---

## 问题根因

跳转播放是播放器功能之一，而AudioRenderer主要用于音频渲染播放，未提供跳转播放API接口。

## 解决方案

在AudioRenderer注册writeDataCallback时，通过跳转的时间戳，计算出新的offset位置，待下次read音频数据时，从该offset开始读取，就能跳转到指定位置播放了。
