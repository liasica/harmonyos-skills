---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-quickimagedatahandler
title: Interface (QuickImageDataHandler)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (QuickImageDataHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9ac5b7136f3f95ca0d0ebb6844205ca63bbd07aebac86f5307f3474371d00851
---

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 13开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared13+

PhonePC/2in1TabletTV

onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void

当请求的图片资源准备就绪时，系统会回调媒体资源就绪通知方法。如果资源准备出错，回调的data将为undefined。

map支持返回的信息：

| map键名 | 值说明 |
| --- | --- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 已就绪的图片资源数据。泛型，支持[Picture](arkts-apis-image-picture.md)数据类型。 |
| imageSource | image.ImageSource | 是 | 已就绪的图片资源数据。 |
| map13+ | Map<string, string> | 是 | 用于获取图片资源的额外信息，如图片质量。仅支持'quality'。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
4. onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
5. console.info('on image data prepared');
6. }
7. }
```
