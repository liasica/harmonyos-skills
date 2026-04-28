---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-4
title: 图片压缩API的quality参数与图片原始大小、压缩后大小的关系
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 图片压缩API的quality参数与图片原始大小、压缩后大小的关系
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:12c266f39e79a95a86dd80763f52f0caa753cc750516d7dc6ebf83fe1130bef7
---

对于有损压缩图片格式（如JPEG），质量参数会影响压缩后的图片大小。对于无损压缩图片格式（如PNG），质量参数不会影响压缩后的图片大小。而且，需要注意的是：减小quality只能使得压缩后的图片文件更小，而不会改变图片的尺寸。

quality参数应该如何选择？理想的图像质量设置取决于图像的细节、色彩和对比度，以及用户想要实现的用户体验。有些图像可以进一步压缩而不会出现明显的质量损失，而有些图像则很快就会出现伪影。一般来说：

* **quality设为90**可提供非常高质量的图像，同时显著减小原始文件的大小。
* **quality设为80**可以更大程度地减少文件大小，而质量几乎没有损失。
* **quality更低**可能会导致图像中出现明显的伪影，因此不建议quality低于80。

系统还提供了scale接口，可以根据输入的宽高缩放倍数对图片进行缩放，直接改变图片尺寸，达到图片压缩效果。在进行scale时，推荐宽高等比缩放，以免图片变形。在使用scale接口前，首先需要通过图片解码获取PixelMap，完成缩放后，重新压缩编码成图片文件。也可以在图片解码时指定desiredSize，直接解码成特定尺寸的PixelMap。

**参考链接**

[scale](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9)
