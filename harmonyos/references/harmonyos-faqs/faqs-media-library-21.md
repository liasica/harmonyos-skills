---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-21
title: 编辑图片后上传图片，上传的图片仍为编辑前的图片
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 编辑图片后上传图片，上传的图片仍为编辑前的图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:78e8d739ddb214a68b1b39808a71e49cf76dd0c4d1613a17126f5ae628c08cfc
---

## 问题现象

选择一张图片上传，之后在相册中编辑该图片，再次上传该图片，上传后仍为编辑前的图片。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/y74_Z3IhQR6ZEPvBJ9O9Tw/zh-cn_image_0000002659258341.png "点击放大")

## 背景知识

* [PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)：图库选择器对象用于支持选择图片、视频等用户场景。使用前，需先创建PhotoViewPicker实例。
* [photoPicker.select](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md#select)：通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。

## 问题定位

排查代码中上传图片相关处理函数，确认应用在上传图片时会将图片缓存到应用沙箱中，且缓存文件的文件名为用户上传图片的文件名。并且应用通过判断上传图片名称和已缓存的图片名是否一致，来判断是否使用缓存。而用户编辑已选图片并不会改变图片名称，因此实际被上传的图片为沙箱的缓存图片，非编辑后的图片。

所用实现代码：

```ts
photoPicker.select(PhotoSelectOptions).then(async (PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
  const filePath = PhotoSelectResult.photoUris[0];
  const cacheDir = this.getUIContext().getHostContext()?.cacheDir;
  const fileName = filePath.split('.')[0].split('/').pop();
  const fileSuffix = filePath.split('.')[1];
  // 缓存的路径为图片名称，当图片编辑后图片名称不会改变但是实际图片已经更新了
  const cachePath = `${cacheDir}/${fileName}.${fileSuffix}`
  if (fileIo.accessSync(cachePath)) {
    // 该图片已被缓存，使用缓存地址
    this.tip = `使用已缓存图片：${cachePath}`;
  } else {
    // 该图片未缓存，缓存到应用沙箱目录
  }
});
```

## 分析结论

应用在首次上传时将图片进行了缓存，后续在相册中编辑图片后再上传时，由于应用仅通过文件名是否一致判断是否使用缓存，导致上传了缓存中编辑前的图片。

## 修改建议

修复判断图片是否已缓存的逻辑，使用文件名+最后一次修改时间作为缓存文件名：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct SimpleImageCacheDemo {
  @State tip: string = '';

  async pickImage() {
    try {
      let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      PhotoSelectOptions.maxSelectNumber = 5;
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then(async (PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
        const filePath = PhotoSelectResult.photoUris[0];
        const cacheDir = this.getUIContext().getHostContext()?.cacheDir;
        const fileName = filePath.split('.')[0].split('/').pop();
        const fileSuffix = filePath.split('.')[1];
        const file = await fileIo.open(filePath, fileIo.OpenMode.READ_ONLY);
        const stat = await fileIo.stat(file.fd);
        const cachePath = `${cacheDir}/${fileName}_${stat.mtime}.${fileSuffix}`;

        if (fileIo.accessSync(cachePath)) {
          // 该图片已被缓存，使用缓存地址
          this.tip = fileUri.getUriFromPath(cachePath);
        } else {
          // 该图片未缓存，缓存到应用沙箱目录
          const buffer = new ArrayBuffer(stat.size);
          await fileIo.read(file.fd, buffer, { offset: 0, length: stat.size });
          const destFd = await fileIo.open(cachePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
          fileIo.writeSync(destFd.fd, buffer);
          this.tip = fileUri.getUriFromPath(cachePath);
        }
      }).catch((err: BusinessError) => {
        console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('选择图片')
        .width('80%')
        .onClick(() => this.pickImage());
      Image(this.tip).height('80%').width('80%');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
