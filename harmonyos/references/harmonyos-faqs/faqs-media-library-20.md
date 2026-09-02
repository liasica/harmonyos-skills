---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-20
title: 生成的二维码图保存到本地图片失败
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 生成的二维码图保存到本地图片失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:08+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:2e2fd15d7ccb8ea00354ce9c09c3f6d74e8f3d5d2de70ea6093a4e6f08bd271b
---

## 问题现象

将字符串生成二维码保存本地后图片显示为空。

问题代码示例参考如下：

```screen
async createImageToSave() {
  let options: generateBarcode.CreateOptions = {
    scanType: scanCore.ScanType.QR_CODE,
    height: 400,
    width: 400
  }
  // 码图生成接口，成功返回PixelMap格式图片
  generateBarcode.createBarcode('华为', options).then((pixelMap: image.PixelMap) => {
    let buf = new ArrayBuffer(pixelMap.getPixelBytesNumber())
    pixelMap.readPixelsToBuffer(buf).then((value) => {
      console.info('二维码:' + buf.byteLength)
      CustomFileSaveManager.saveImageToPhoto(buf)
    })
  })
}
static async saveImageToPhoto(buffer: ArrayBuffer | string): Promise<void> {
  const context = getContext() as common.UIAbilityContext; // 获取getPhotoAccessHelper需要的context
  const helper = photoAccessHelper.getPhotoAccessHelper(context); // 获取相册管理模块的实例
  const uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg'); // 指定待创建的文件类型、后缀和创建选项，创建图片或视频资源
  const file = await fs.open(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  let r = await fs.write(file.fd, buffer);
  await fs.close(file.fd);
  showShortCenterToast('图片保存成功')
}
```

## 背景知识

* [generateBarcode](../harmonyos-references/scan-generatebarcode.md)：码图生成，通过[generateBarcode.createBarcode](../harmonyos-references/scan-generatebarcode.md)接口把文本生成码图。
* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，用于读取或写入图像数据以及获取图像信息。通过[readPixelsToBuffer](../harmonyos-references/arkts-apis-image-pixelmap.md#readpixelstobuffer7)读取PixelMap的图像像素数据。

## 问题定位

readPixelsToBuffer读取的是PixelMap的像素数据，不是图片的全部数据，导致保存到本地后图片显示为空。

## 分析结论

要通过[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)将图像重新编码获取全部ArrayBuffer数据。

## 修改建议

先用码图生成接口生成PixelMap格式图片，再通过[packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)接口获取PixelMap全部数据，写入文件保存即可得到一张图片。

**说明** 

码图生成暂不支持模拟器使用，调用会返回错误信息“Emulator is not supported.”。

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { generateBarcode, scanCore } from '@kit.ScanKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct BarcodeSavedToPhotoAlbum {
  @State pixel: image.PixelMap | undefined = undefined;
  private saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE,
    buttonType: ButtonType.Capsule
  };
  private context: Context = this.getUIContext().getHostContext()!;

  async savePixelMapToAlbum() {
    // 获取沙箱路径
    let filesDir = this.context.filesDir;
    let filePath = filesDir + '/codeChart.jpg';
    let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    let imagePackerApi = image.createImagePacker();
    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };

    // PixelMap编码到沙箱路径
    imagePackerApi.packToFile(this.pixel, file.fd, packOpts, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to pack the image to file.code ${err.code},message is ${err.message}`);
      } else {
        console.info('Succeeded in packing the image to file.');
        imagePackerApi.release((err: BusinessError) => {
          if (err) {
            console.error(`Failed to release the image source instance.code ${err.code},message is ${err.message}`);
          } else {
            console.info('Succeeded in releasing the image source instance.');
            fs.close(file.fd);
          }
        });
      }
    });

    // 保存资源到相册
    try {
      let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      // 需要确保fileUri对应的资源存在。
      let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
        photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context, filePath);
      await phAccessHelper.applyChanges(assetChangeRequest);
      console.info('createAsset successfully, uri: ' + assetChangeRequest.getAsset().uri);
    } catch (err) {
      console.error(`create asset failed with error: ${err.code}, ${err.message}`);
    }
    this.getUIContext().getPromptAction().showToast({ message: '已保存至相册！' });
  }

  async createImageToSave() {
    let options: generateBarcode.CreateOptions = {
      scanType: scanCore.ScanType.QR_CODE,
      height: 400,
      width: 400
    };
    // 码图生成接口，成功返回PixelMap格式图片
    // 注：暂不支持模拟器使用，调用会返回错误信息“Emulator is not supported.”
    generateBarcode.createBarcode("华为", options).then((pixelMap: image.PixelMap) => {
      this.pixel = pixelMap;
    }).catch((error: BusinessError) => {
      console.error('Failed to pack the image. And the error is: ' + error);
    });
  }

  build() {
    Row() {
      Column() {
        Image(this.pixel)
          .objectFit(ImageFit.None)
          .height('30%');

        Button("生成二维码")
          .onClick(() => {
            this.createImageToSave();
          });

        SaveButton(this.saveButtonOptions)
          .onClick(async (event, result: SaveButtonOnClickResult) => {
            if (result === SaveButtonOnClickResult.SUCCESS) {
              this.savePixelMapToAlbum();
              console.info(`${event}: Successfully saved PixelMap to album!`);
            }
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
