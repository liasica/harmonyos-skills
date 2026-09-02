---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-54
title: 如何实现解码Base64字符串格式图片为PixelMap并保存入系统图库
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现解码Base64字符串格式图片为PixelMap并保存入系统图库
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09b2572b841c4b640456049e39e4b4e8d8f6c119f0bdf2b5b72de0ef1d0b4099
---

## 问题现象

如何将Base64字符串格式的图片解码为PixelMap，并保存至系统图库中。

## 背景知识

* [ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)将所支持格式的图片文件解码成[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，以便在应用中显示或处理图片。
* [Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)类提供Base64编解码能力。[decode](../harmonyos-references/js-apis-util.md#decode9)接口可以将Base64字符串解码为原始的二进制数据。
* [showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)调用接口显示保存确认弹窗。如果用户同意保存，将返回一个已创建并授予保存权限的URI列表，应用可使用这些URI写入需要保存的图片和视频。

## 解决方案

* 解码Base64字符串格式图片为PixelMap：
  1. 使用[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)的[decode](../harmonyos-references/js-apis-util.md#decode9)接口解码Base64字符串获取图片的二进制数据。
  2. 通过保存图片数据的ArrayBuffer创建[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)，然后通过[createPixelMap](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)接口创建PixelMap。

  ```ts
  async base64Str2PixelMap() {
    let imageSource: image.ImageSource | undefined = undefined;
    try {
      // 判断是否以固定格式开头，如果不是则为非法base64字符串图片
      let headerReg = new RegExp('data:image/\\w+;base64,');
      let idx = this.imageStr.search(headerReg);
      if (idx !== 0) {
        console.error(`Invalid image base64 string`);
        return;
      }
      // 去除头部固定格式字符串
      let base64Str = this.imageStr.replace(headerReg, '');
      // 解码base64为图片二进制数据
      let base64Helper = new util.Base64Helper();
      let imgData = await base64Helper.decode(base64Str);
      // 通过图片二进制数据创建ImageSource，并解码为PixelMap
      imageSource = image.createImageSource(imgData.buffer.slice(0));
      this.pixelMap = await imageSource.createPixelMap();
    } catch (err) {
      console.error(`Failed to decode base64 string to pixelmap: ${JSON.stringify(err)}`);
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
    }
  }
  ```
* Base64字符串格式图片保存入系统图库：
  1. 使用[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)的[decode](../harmonyos-references/js-apis-util.md#decode9)接口解码Base64字符串获取图片的二进制数据。
  2. 保存图片数据入应用的沙箱目录下。
  3. 通过[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)保存沙箱目录下的图片入系统图库。

  ```ts
  async saveBase64StrImage() {
    // 匹配开头固定格式的字符串，若不存在，则为非法base64图片
    let headerReg = new RegExp('data:image/\\w+;base64,');
    let matchArr = this.imageStr.match(headerReg);
    if (!matchArr || matchArr.length === 0) {
      console.error(`Invalid image base64 string`);
      return;
    }
    // 去除头部固定格式的字符串
    let base64Str = this.imageStr.replace(headerReg, '');
    // 获得图片编码格式信息
    let fileNameExtension = matchArr[0].replace('data:image/', '').replace(';base64,', '');
    // 解码base64为图片二进制数据
    let base64Helper = new util.Base64Helper();
    let imgData = await base64Helper.decode(base64Str);
    // 写入沙箱文件
    let context = this.getUIContext().getHostContext() as Context;
    let srcFilePath = context.tempDir + `/temp_img.${fileNameExtension}`;
    let tmpFile: fileIo.File | undefined = undefined;
    try {
      tmpFile = fileIo.openSync(srcFilePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE);
      fileIo.writeSync(tmpFile.fd, imgData.buffer.slice(0));
    } catch (err) {
      console.error(`Failed to write image data to sandbox: ${JSON.stringify(err)}`);
      return;
    } finally {
      if (tmpFile) {
        fileIo.closeSync(tmpFile);
      }
    }

    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let srcFile: fileIo.File | undefined = undefined;
    let desFile: fileIo.File | undefined = undefined;
    try {
      srcFile = await fileIo.open(srcFilePath, fileIo.OpenMode.WRITE_ONLY);
      let srcFileUri = fileUri.getUriFromPath(srcFilePath);
      let srcFileUris: Array<string> = [
        srcFileUri,
      ];
      // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
      let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
        {
          fileNameExtension: fileNameExtension,
          photoType: photoAccessHelper.PhotoType.IMAGE,
        },
      ];
      // 基于弹窗授权的方式获取媒体库的目标uri。
      let desFileUris: Array<string> =
        await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
      // 将来源于应用沙箱的照片内容写入媒体库的目标uri。
      desFile = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
      srcFile = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
      await fileIo.copyFile(srcFile.fd, desFile.fd);
      console.info('create asset by dialog successfully');
    } catch (err) {
      console.error(`Error: ${JSON.stringify(err)}`);
    } finally {
      if (srcFile) {
        await fileIo.close(srcFile);
      }
      if (desFile) {
        await fileIo.close(desFile);
      }
    }
  }
  ```

完整示例参考如下：

```ts
import { Context } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';
import image from '@ohos.multimedia.image';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct Base64ImageDemo {
  @State imageStr: string = '';
  @State pixelMap: image.PixelMap | undefined = undefined;

  async image2Base64Str() {
    let imageSource: image.ImageSource | undefined = undefined;
    try {
      // 读取rawfile目录下的图片文件
      let context = this.getUIContext().getHostContext() as Context;
      let imgData = await context.resourceManager.getRawFileContent('img.png');
      // 获取图片mime type
      imageSource = image.createImageSource(imgData.buffer.slice(0));
      let info = await imageSource.getImageInfo();
      let mime = info.mimeType;
      // 编码图片数据为base64字符串
      let base64Helper = new util.Base64Helper();
      let base64Str = await base64Helper.encodeToString(imgData);
      this.imageStr = `data:${mime};base64,` + base64Str;
    } catch (err) {
      console.info(`Failed to encode image data to base64: ${JSON.stringify(err)}`);
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
    }
  }

  async base64Str2PixelMap() {
    let imageSource: image.ImageSource | undefined = undefined;
    try {
      // 判断是否以固定格式开头，如果不是则为非法base64字符串图片
      let headerReg = new RegExp('data:image/\\w+;base64,');
      let idx = this.imageStr.search(headerReg);
      if (idx !== 0) {
        console.error(`Invalid image base64 string`);
        return;
      }
      // 去除头部固定格式字符串
      let base64Str = this.imageStr.replace(headerReg, '');
      // 解码base64为图片二进制数据
      let base64Helper = new util.Base64Helper();
      let imgData = await base64Helper.decode(base64Str);
      // 通过图片二进制数据创建ImageSource，并解码为PixelMap
      imageSource = image.createImageSource(imgData.buffer.slice(0));
      this.pixelMap = await imageSource.createPixelMap();
    } catch (err) {
      console.error(`Failed to decode base64 string to pixelmap: ${JSON.stringify(err)}`);
    } finally {
      if (imageSource) {
        await imageSource.release();
      }
    }
  }

  async saveBase64StrImage() {
    // 匹配开头固定格式的字符串，若不存在，则为非法base64图片
    let headerReg = new RegExp('data:image/\\w+;base64,');
    let matchArr = this.imageStr.match(headerReg);
    if (!matchArr || matchArr.length === 0) {
      console.error(`Invalid image base64 string`);
      return;
    }
    // 去除头部固定格式的字符串
    let base64Str = this.imageStr.replace(headerReg, '');
    // 获得图片编码格式信息
    let fileNameExtension = matchArr[0].replace('data:image/', '').replace(';base64,', '');
    // 解码base64为图片二进制数据
    let base64Helper = new util.Base64Helper();
    let imgData = await base64Helper.decode(base64Str);
    // 写入沙箱文件
    let context = this.getUIContext().getHostContext() as Context;
    let srcFilePath = context.tempDir + `/temp_img.${fileNameExtension}`;
    let tmpFile: fileIo.File | undefined = undefined;
    try {
      tmpFile = fileIo.openSync(srcFilePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.CREATE);
      fileIo.writeSync(tmpFile.fd, imgData.buffer.slice(0));
    } catch (err) {
      console.error(`Failed to write image data to sandbox: ${JSON.stringify(err)}`);
      return;
    } finally {
      if (tmpFile) {
        fileIo.closeSync(tmpFile);
      }
    }

    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let srcFile: fileIo.File | undefined = undefined;
    let desFile: fileIo.File | undefined = undefined;
    try {
      srcFile = await fileIo.open(srcFilePath, fileIo.OpenMode.WRITE_ONLY);
      let srcFileUri = fileUri.getUriFromPath(srcFilePath);
      let srcFileUris: Array<string> = [
        srcFileUri,
      ];
      // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
      let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
        {
          fileNameExtension: fileNameExtension,
          photoType: photoAccessHelper.PhotoType.IMAGE,
        },
      ];
      // 基于弹窗授权的方式获取媒体库的目标uri。
      let desFileUris: Array<string> =
        await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
      // 将来源于应用沙箱的照片内容写入媒体库的目标uri。
      desFile = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
      srcFile = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
      await fileIo.copyFile(srcFile.fd, desFile.fd);
      console.info('create asset by dialog successfully');
    } catch (err) {
      console.error(`Error: ${JSON.stringify(err)}`);
    } finally {
      if (srcFile) {
        await fileIo.close(srcFile);
      }
      if (desFile) {
        await fileIo.close(desFile);
      }
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('Image2Base64')
        .fontSize(30)
        .onClick(async () => {
          await this.image2Base64Str();
        });

      Button('Base64Str2PixelMap')
        .fontSize(30)
        .onClick(async () => {
          await this.base64Str2PixelMap();
        });

      Button('SaveBase64StrImage')
        .fontSize(30)
        .onClick(async () => {
          await this.saveBase64StrImage();
        });

      Image(this.imageStr)
        .width('50%')
        .aspectRatio(1)
        .objectFit(ImageFit.Contain);

      Image(this.pixelMap)
        .width('50%')
        .aspectRatio(1)
        .objectFit(ImageFit.Contain);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
