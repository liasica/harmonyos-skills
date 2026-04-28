---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-37
title: 模拟器上部分视频无法正常播放
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器上部分视频无法正常播放
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:49c558e7e96dc6ae87f72fff4f134cfb6f68ddd73e11b1285486df48901fb08f
---

**问题现象**

在模拟器播放视频时，可能会遇到视频有声音但无画面，或者播放卡顿的问题。

**解决措施**

由于模拟器仅支持RGBA格式的像素显示，请确保视频解码格式正确。模拟器仅支持软件解码，如果视频解码器依赖硬件解码，视频可能无法正常播放。
