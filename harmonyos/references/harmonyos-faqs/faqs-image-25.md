---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-25
title: 图片加载失败
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 图片加载失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05a07fdc7cb5357b7037999918019a0a9f485e3e552334aa83b77d97ae71836a
---

## 问题现象

应用内因图片加载失败导致图片出现空白、黑屏、错误提示等现象。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)：Image为图片组件，常用于在应用中显示图片。
* [EXIF](../harmonyos-guides/image-tool.md)（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前仅支持JPEG、PNG、HEIF格式图片。
* Image Kit错误码[62980123](../harmonyos-references/errorcode-image.md#section62980123-图片不支持exif解码)：图片不支持EXIF解码。其他Image Kit错误码参考[Image Kit错误码](../harmonyos-references/errorcode-image.md)。

## 问题定位

* 场景一：

  根据问题发生时间点，找到对应日志。发现在图片未显示时，日志中显示图片资源为空导致解码超时。

  ```txt
  09-08 09:43:44.081 C0391F/AceImage: [image_loader.cpp(CreateImageLoader)-(100000:100000:sCope)] Image source type   not supported!arcType:sourceInfo: empty source
  09-08 09:43:44.081 CO391F/AceImage: [image loading_context.cpp(FailCallback)-(100000:100000:sCope)] Image LoadFail,   source = <private>,reason:Failed to load image data
  09-08 09:43:44.081 CO391F/AceImage: [image loading_context.cpp(FailCallback)-(100000:100000:sCope)] Image LoadFail,   source = <private>,reason:emptysourceFailed image loader, Image source type not supported
  09-08 09:43:44.081 CO2B05/HEIF HW DECODER: [heif hw decoder.cpp](ReceiveOutputBufferLoop 574] output time out
  ```
* 场景二：

  根据问题发生时间点，在日志中查找Image Kit错误码“62980123”。

  找到相关错误日志：

  ```txt
  getImageProperty failed, code is 62980123, message is The image does not support EXIF decoding.
  ```

## 分析结论

* 场景一：服务器数据异常，图片资源未正确获取，导致图片解码失败，未能正确显示图片。
* 场景二：获取图片指定属性键的值失败，图片不支持EXIF解码。

## 修改建议

* 场景一：

  检查服务器数据，并对图片显示进行判空处理，当数据为空时，可以显示默认图片，或对图片的alt属性进行设置，配置加载时的占位图。可参考[官方案例](../harmonyos-references/ts-basic-components-image.md#示例2下载与显示静态网络图片)。
* 场景二：

  应用调用getImageProperty接口时需要捕获异常，并对异常情况进行相应处理。

  ```ts
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { photoAccessHelper } from '@kit.MediaLibraryKit';
  import { image } from '@kit.ImageKit';

  let selectUris: string[];

  @Entry
  @Component
  struct ImageUploadDemo {
    build() {
      Row() {
        Column() {
          Button('打开相册')
            .onClick(() => {
              const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
              photoViewPicker.select().then(async (photoSelectResult) => {
                selectUris = photoSelectResult.photoUris;
                console.info('photoViewPicker.select to file succeed and uris are:' + selectUris);
              }).catch((err: BusinessError) => {
                console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
              });
            });

          Button('creatPixelMap')
            .margin({ top: 10 })
            .onClick(() => {
              let file = fs.openSync(selectUris[0], fs.OpenMode.READ_ONLY);
              const imageSource: image.ImageSource = image.createImageSource(file.fd);
              imageSource.getImageProperty(image.PropertyKey.IMAGE_WIDTH).then(() => {
                // getImageProperty调用成功，继续处理上传业务逻辑
              }).catch(() => {
                // getImageProperty失败时捕获异常，并进行相应处理
              });
            });
        }
        .justifyContent(FlexAlign.Center).alignItems(HorizontalAlign.Center)
        .height('100%')
        .width('100%');
      };
    }
  }
  ```
