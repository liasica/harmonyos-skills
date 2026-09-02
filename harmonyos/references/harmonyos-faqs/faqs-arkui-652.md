---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-652
title: Video播放系统图库视频
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Video播放系统图库视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fce5ef422b680f856960070f4d7d27d4c0d87f20ab3916357b77423908f86e0
---

## 问题现象

如何使用Video组件播放用户系统图库中的视频文件。

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md)：Video组件用于播放视频文件并控制其播放状态，支持加载本地视频和网络视频。
* [PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)：PhotoViewPicker用于拉起系统图库，让用户选取图库中的图片、视频的场景。

## 解决方案

创建[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)实例，调用[select](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md#select)接口拉起图库界面供用户进行视频文件的选择，文件选择成功后，会返回视频文件的uri，可以通过Video组件播放该uri对应的相册视频。

参考代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State videoUri: string = '';
  private controller: VideoController = new VideoController();

  build() {
    Column({ space: 20 }) {
      Video({
        src: this.videoUri,
        controller: this.controller,
      })
        .width('100%')
        .aspectRatio(1)
        .loop(false)
        .autoPlay(true)
        .controls(false)
        .objectFit(ImageFit.Contain)
        .onError(() => {
          console.error(`video error.`);
        })
        .onStop(() => {
          console.info(`video stopped.`);
        })
        .onUpdate(() => {
          console.info(`video update.`);
        })
        .onPrepared(() => {
          console.info(`video prepared.`);
        });

      Button('Select Video')
        .padding(5)
        .fontSize(30)
        .onClick(() => {
          let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
          photoSelectOptions.maxSelectNumber = 1;
          let uris: Array<string> = [];
          let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
          photoViewPicker.select(photoSelectOptions)
            .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
              uris = photoSelectResult.photoUris;
              if (uris.length > 0) {
                this.videoUri = uris[0];
                console.info(`Video URI: ${this.videoUri}`);
              }
            })
            .catch((err: BusinessError) => {
              console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
            });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
