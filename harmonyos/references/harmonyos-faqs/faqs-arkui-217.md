---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-217
title: Image组件是否有缓存机制
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image组件是否有缓存机制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f0905c7f8de174350b6a13946995b422cb1348443846afc3267df57840bae24e
---

1. Image的缓存策略

Image模块提供了三级Cache机制，解码后内存图片缓存、解码前数据缓存、物理磁盘缓存。在加载图片时会逐级查找，如果在Cache中找到之前加载过的图片则提前返回对应的结果。

2. Image组件如何配置打开和关闭缓存

* 内存图片缓存：通过[setImageCacheCount](../harmonyos-references/js-apis-system-app.md#setimagecachecount7)接口打开缓存，如果希望每次联网都获取最新资源，可以不设置（默认为0），不进行缓存。。
* 磁盘缓存：磁盘缓存是默认开启的，默认值为100M，可以将[setImageFileCacheSize](../harmonyos-references/js-apis-system-app.md#setimagefilecachesize7)的值设置为0关闭磁盘缓存。
* 解码前数据缓存：通过[setImageRawDataCacheSize](../harmonyos-references/js-apis-system-app.md#setimagerawdatacachesize7)设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。

setImageCacheCount、setImageRawDataCacheSize和setImageFileCacheSize这三个图片缓存接口灵活性不足，后续不再演进，对于复杂情况，建议使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。
