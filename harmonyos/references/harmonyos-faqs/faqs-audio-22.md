---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-22
title: 使用AudioRenderer播放音频时，如何跳转到指定播放位置
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 使用AudioRenderer播放音频时，如何跳转到指定播放位置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1ab9a82d49fe597140b4eb77beca5b08e4425b4edb3ba01c9f09a425094b9fdf
---

**问题根因**

跳转播放是播放器功能之一，而AudioRenderer主要用于音频渲染播放，未提供跳转播放API接口。

**解决方案**

在AudioRenderer注册writeDataCallback时，通过跳转的时间戳，计算出新的offset位置，待下次read音频数据时，从该offset开始读取，就能跳转到指定位置播放了。
