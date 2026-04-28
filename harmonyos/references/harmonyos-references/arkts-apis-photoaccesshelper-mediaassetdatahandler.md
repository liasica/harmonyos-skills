---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler
title: Interface (MediaAssetDataHandler)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (MediaAssetDataHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:72d634ccef736bc2e7a949f3ee467b67279ec1a6941f90c024bc3c3aa8ce68bf
---

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared11+

PhonePC/2in1TabletTV

onDataPrepared(data: T, map?: Map<string, string>): void

媒体资源就绪通知，系统在资源准备就绪时回调此方法。若资源准备出错，回调的data为undefined。资源请求与回调一一对应。

T支持ArrayBuffer，[ImageSource](arkts-apis-image-imagesource.md)，[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)和boolean四种数据类型。其中，ArrayBuffer表示图片/视频资源数据，[ImageSource](arkts-apis-image-imagesource.md)表示图片源，[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)表示动态照片对象，boolean表示图片/视频资源是否成功写入应用沙箱。

map支持返回的信息：

| map键名 | 值说明 |
| --- | --- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 已就绪的图片资源数据。泛型，支持ArrayBuffer, [ImageSource](arkts-apis-image-imagesource.md), [MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)和boolean四种数据类型。 |
| map12+ | Map<string, string> | 否 | 用于获取图片资源的额外信息，如图片质量。当前仅支持'quality'。 |

**示例：**

```
1. import { image } from '@kit.ImageKit';

3. class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
4. onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
5. if (data === undefined) {
6. console.error('Error occurred when preparing data');
7. return;
8. }
9. // 自定义对ImageSource的处理逻辑。
10. console.info('on image data prepared, photo quality is ' + map['quality']);
11. }
12. }

14. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
15. onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
16. if (data === undefined) {
17. console.error('Error occurred when preparing data');
18. return;
19. }
20. // 自定义对ArrayBuffer的处理逻辑。
21. console.info('on image data prepared, photo quality is ' + map['quality']);
22. }
23. }

25. class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
26. onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
27. if (data === undefined) {
28. console.error('Error occurred when preparing data');
29. return;
30. }
31. // 自定义对MovingPhoto的处理逻辑。
32. console.info('on image data prepared, photo quality is ' + map['quality']);
33. }
34. }
```
