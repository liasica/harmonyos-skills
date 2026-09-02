---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-8
title: 分享不显示缩略图的原因有哪些
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 分享不显示缩略图的原因有哪些
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d40dabd4dc7d852cd9d279b74565f0e9321e3c2dae7b675e4e123189e7b76c0f
---

## 问题现象

系统分享需要显示缩略图，调用[systemShare.SharedData](../harmonyos-references/share-system-share.md#shareddata)设置[SharedRecord](../harmonyos-references/share-system-share.md#sharedrecord)的thumbnail或thumbnailUri后仍无法显示缩略图的原因有哪些？

## 解决方案

若未设置缩略图（thumbnail或thumbnailUri）使用与分享内容类型匹配的图标作为缩略图。如果同时设置thumbnail和thumbnailUri，会优先使用thumbnail。

缩略图不显示的原因如下：

* thumbnail是否尺寸过大：限制图片大小：32KB以下。过大的图片可能导致want数据超限无法拉起分享，可使用[ImagePacker.packing](../harmonyos-references/arkts-apis-image-imagepacker.md#packing13)压缩图片质量。
* thumbnailUri不支持网络URL，如果是网络图片，可以下载到本地后再设置分享。
* thumbnailUri设置是否正确：使用应用文件uri，需要使用[getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)接口转换；使用用户文件uri，需要注意uri[授权持久化](../harmonyos-guides/file-persistpermission.md)。
