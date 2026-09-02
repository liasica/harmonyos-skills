---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-22
title: 删除媒体库资源的两种方法removeAssets和deleteAssets区别是什么
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 删除媒体库资源的两种方法removeAssets和deleteAssets区别是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:f336bc0ae7381fd0aafa60bd846f70154d931865b42b8d7fd82d47428d019c6c
---

## 问题现象

三方应用能否删除图库中的媒体资源，MediaAlbumChangeRequest.removeAssets和MediaAssetChangeRequest.deleteAssets两个方法的区别是什么？

## 解决方案

三方应用在[申请相册管理模块功能相关权限](../harmonyos-guides/photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)后，可以删除图库中的媒体资源，其中[MediaAssetChangeRequest.deleteAssets](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetchangerequest.md#deleteassets11)接口是删除图库中的媒体资源，会出现删除弹窗需要用户确认，而[MediaAlbumChangeRequest.removeAssets](../harmonyos-references/arkts-apis-photoaccesshelper-mediaalbumchangerequest.md#removeassets11)是指将媒体资源从指定相册中移除，需要和[PhotoAccessHelper.applyChanges](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口配合使用，无弹窗提示。上述两种方式执行后媒体资源均会进入回收站。
