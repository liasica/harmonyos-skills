---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-5
title: 图片编解码支持的格式有哪些
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 图片编解码支持的格式有哪些
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0c89e70b3afbdcc6ee6275c0a88ddb1d58ba37e902f55f99cbd17b191efef746
---

* 图片解码

指将所支持格式的图片文件解码成PixelMap，以便在应用或系统中进行图片显示或图片处理。当前支持解码的图片格式包括JPEG、PNG、GIF、RAW、WebP、BMP、HEIC（API12起）。

* 图片编码

指将PixelMap编码成不同格式的图片文件，用于后续处理，如保存、传输等。当前支持编码的图片格式包括JPEG、WebP、PNG、HEIC（API12起）、GIF（API18起，需要使用PackToDataFromPixelmapSequence或PackToFileFromPixelmapSequence接口进行编码）。

**参考链接**

[使用ImageSource完成图片解码](../harmonyos-guides/image-decoding.md)

[使用ImagePacker完成图片编码](../harmonyos-guides/image-encoding.md)

[图片编码（C/C++）](../harmonyos-guides/image-encoding-native.md)
