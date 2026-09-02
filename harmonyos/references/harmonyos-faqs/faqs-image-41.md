---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-41
title: 如何将图片转为base64后再解码显示
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将图片转为base64后再解码显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:937cc733f247fb187d2c66670b5a106161b7d83a08c48e485d8a971ce375ba12
---

## 问题现象

业务诉求：将图片转成Base64后存入数据库，再从数据库中读取解码后进行图片展示，期望提供从选择图片到转换为Base64编码，再从Base64解码后显示图片的示例。

## 背景知识

* 从图库选择图片可以使用[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)来实现。
* ImageKit的[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)接口提供了创建PixelMap的能力。
* Base64Helper工具函数提供了[encodeToString](../harmonyos-references/js-apis-util.md#encodetostring9)：将ArrayBuffer转换成string文本，以及[decodeSync](../harmonyos-references/js-apis-util.md#decodesync9)：通过输入参数解码后输出ArrayBuffer对象的能力。

## 解决方案

* 从选择图片到转换为Base64编码可参考以下流程：

  1.从图库选择图片得到图片数组的uris，结合fileIo和ImageKit将uris转换为ImageSource后，通过createPixelMap接口获取到图片的PixelMap。

  2.将PixelMap转换为ArrayBuffer后，再通过Base64Helper的encodeToString接口即可转换为Base64编码的字符串。
* 从Base64编码再转换为图片显示可参考以下流程：

  1.通过Base64Helper.decodeSync函数将PixelMap转换为ArrayBuffer。

  2.通过image.createPixelMap还原成图片PixelMap。

  PixelMap的对象，可以通过ArkUI的Image组件直接展示，可参考如下完整代码示例：

  ```ts
  import { photoAccessHelper } from '@kit.MediaLibraryKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { image } from '@kit.ImageKit';
  import util from '@ohos.util';

  @Entry
  @Component
  struct Index {
    @State originalPixelMap: image.PixelMap | null = null;
    @State imageBase64Str: string = '';
    @State targetPixelMap: image.PixelMap | null = null;

    // 从相册选择图片并进行预览
    selectPhoto() {
      try {
        let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
        photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
        photoSelectOptions.maxSelectNumber = 1;
        let photoPicker = new photoAccessHelper.PhotoViewPicker();
        photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
          let result = JSON.stringify(photoSelectResult);
          console.info(`PhotoViewPicker.select successfully, PhotoSelectResult uri: ${result}`);
          let uri = photoSelectResult.photoUris[0];
          // 获取到图片或者视频文件的URI后进行文件读取等操作
          let file: fs.File | null = null;
          try {
            file = fs.openSync(uri, fs.OpenMode.READ_ONLY);
            const imageSourceApi = image.createImageSource(file.fd);
            this.originalPixelMap = imageSourceApi.createPixelMapSync();
            let num = this.originalPixelMap.getPixelBytesNumber();
            let readBuffer: ArrayBuffer = new ArrayBuffer(num);
            this.originalPixelMap.readPixelsToBufferSync(readBuffer);
            let utilBase64Helper = new util.Base64Helper();
            // 获取到图片Base64字符串
            this.imageBase64Str = utilBase64Helper.encodeToStringSync(new Uint8Array(readBuffer));
            imageSourceApi.release();
            this.base64ToPixmap();
          } catch (e) {
            let err: BusinessError = e as BusinessError;
            console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
          } finally {
            // 释放资源
            if (file !== null) {
              fs.closeSync(file.fd);
            }
          }
        }).catch((err: BusinessError) => {
          console.error(`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}`);
        });
      } catch (error) {
        let err: BusinessError = error as BusinessError;
        console.error(`PhotoViewPicker failed with err: ${err.code}, ${err.message}`);
      }
    }

    // 将Base64编码的字符串转换为PixelMap
    base64ToPixmap() {
      try {
        let utilBase64Helper = new util.Base64Helper();
        let pixelFormat = this.originalPixelMap?.getImageInfoSync().pixelFormat;
        let height = this.originalPixelMap?.getImageInfoSync().size.height as number;
        let width = this.originalPixelMap?.getImageInfoSync().size.width as number;
        let opts: image.InitializationOptions =
          { editable: true, srcPixelFormat: pixelFormat, size: { height: height, width: width } };
        let imageUint8 = utilBase64Helper.decodeSync(this.imageBase64Str).buffer;
        this.targetPixelMap = image.createPixelMapSync(imageUint8, opts);
      } catch (e) {
        console.error(`base64ToPixmap failed with err: ${e.code}, ${e.message}`);
      }
    }

    build() {
      Column({ space: 10 }) {
        Button('获取展示Base64图片')
          .onClick(() => {
            this.selectPhoto();
          });
        Text('原始图片');
        Image(this.originalPixelMap == null ? $r('app.media.startIcon') : this.originalPixelMap)
          .width('200vp');

        Text('Base64图片');
        Image(this.targetPixelMap == null ? $r('app.media.startIcon') : this.targetPixelMap)
          .width('200vp');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

## 总结

* PixelMap文件转Base64。
  1. 通过Image模块的createImageSource方法从ArrayBuffer中构造出ImageSource实例，然后通过ImageSource的createPixelMap方法创建一个PixelMap实例。
  2. 将PixelMap编码成Uint8Array数据可以通过util.Base64Helper()，Base64Helper类提供Base64编解码和Base64URL编解码功能，使用encodeSync方法通过输入参数编码后输出Uint8Array对象。
  3. 将Uint8Array数据转换成Base64类型HarmonyOS的util工具函数提供了Base64Helper类，Base64Helper类中的encodeToStringSync方法可以将Uint8Array转换为Base64编码。如果要保证Base64编码后的结果仍能够解码成原始的图片文件，请直接使用Base64Helper类进行二进制数据转换操作，避免增加图片编解码相关操作。
* Base64转PixelMap。
  1. 将Base64类型数据解析成ArrayBuffer类型，同样可以通过Base64Helper类中的decodeSync方法将Base64数据解析成Uint8Array类型数据，然后将Uint8Array类型数据转换成ArrayBuffer数据可以直接访问Uint8Array的buffer属性。
  2. 创建InitializationOptions对象用于配置新PixelMap，并使用image.createPixelMapSync使用解码后的数据创建新的PixelMap。
