---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler
title: Interface (MediaAssetDataHandler)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (MediaAssetDataHandler)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:083b2f4463eb452415ce97a31ce508571058ccf86035626651ce6b27a9cb9e0e
---

媒体资源处理器接口，可通过实现onDataPrepared方法来自定义媒体资源处理逻辑。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onDataPrepared11+

onDataPrepared(data: T, map?: Map<string, string>): void

媒体资源就绪通知，系统在资源准备就绪时回调此方法。若资源准备出错，回调的data为undefined。资源请求与回调一一对应。

map支持返回的信息：

| map键名 | 值说明 |
| --- | --- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | T | 是 | 已就绪的图片/视频资源数据。  若资源准备出错，此参数为undefined。  支持ArrayBuffer、[ImageSource](arkts-apis-image-imagesource.md)、[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)和boolean四种数据类型。  当此参数类型为boolean时，true表示成功，false表示失败。 |
| map12+ | Map<string, string> | 否 | 用于获取图片资源的额外信息，如图片质量。当前仅支持'quality'。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ImageSource的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map.get('quality'));
  }
}

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对ArrayBuffer的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map.get('quality'));
  }
}

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // 自定义对MovingPhoto的处理逻辑。
    console.info('on image data prepared, photo quality is ' + map.get('quality'));
  }
}
```
