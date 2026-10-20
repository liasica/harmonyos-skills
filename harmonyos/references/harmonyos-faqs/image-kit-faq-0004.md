---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/image-kit-faq-0004
title: 如何读取相册中的图片
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 常见问题 > 如何读取相册中的图片
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:23d54e5f135b710aeedf61ba712b7d7ab6d344e4eedc8ab55c498af6b8253f08
---

**Q：如何读取相册中的图片？**

**A**：使用photoAccessHelper.PhotoSelectOptions接口读取相册中的图片。

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  @State getAlbum: string = '显示相册中的图片';
  @State pixel: image.PixelMap | undefined = undefined;
  @State albumPath: string = '';
  @State photoSize: number = 0;

  async getPictureFromAlbum() {
    // Pull up the album and select the pictures
    let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    PhotoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
    this.albumPath = photoSelectResult.photoUris[0];

    // Read the image as a buffer
    const file = fileIo.openSync(this.albumPath, fileIo.OpenMode.READ_ONLY);
    this.photoSize = fileIo.statSync(file.fd).size;
    console.info('Photo Size: ' + this.photoSize);
    let buffer = new ArrayBuffer(this.photoSize);
    fileIo.readSync(file.fd, buffer);
    fileIo.closeSync(file);

    // Decoding into PixelMap
    const imageSource = image.createImageSource(buffer);
    console.log('imageSource: ' + JSON.stringify(imageSource));
    this.pixel = await imageSource.createPixelMap({});
  }

  build() {
    Row() {
      Column() {
        Image(this.pixel)
          .width('100%')
          .aspectRatio(1)
        Button('显示照片')
          .onClick(() => {
            this.getPictureFromAlbum();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
