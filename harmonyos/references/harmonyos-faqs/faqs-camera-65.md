---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-65
title: 如何使用CameraPicker拍摄HEIF图
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何使用CameraPicker拍摄HEIF图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5e46217b303587415ed4fc752d2721a9401cc2446b5fdf734aa55e68958498ae
---

## 问题现象

如何使用CameraPicker来拍摄HEIF格式的图片？

## 背景知识

* [通过系统相机拍照和录像(CameraPicker)](../harmonyos-guides/camera-picker.md)：应用可调用CameraPicker拍摄照片或录制视频，无需申请相机权限。
* [ImagePacker.packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)：指定编码参数，将ImageSource直接编码进文件。使用callback异步回调。

## 解决方案

当前CameraPicker不支持拍摄HEIF格式的图片，但是可以通过ImagePacker.packToFile接口将Picker拍摄的图片重新编码成HEIF格式并保存。

样例代码如下：

```ts
import { common } from '@kit.AbilityKit';
import { camera, cameraPicker } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import fs from '@ohos.file.fs';
import { picker } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  getImageBaseName(imageName: string): string {
    const LAST_DOT_INDEX = imageName.lastIndexOf('.');
    if (LAST_DOT_INDEX > 0 && LAST_DOT_INDEX < imageName.length - 1) {
      return imageName.substring(0, LAST_DOT_INDEX);
    }
    return imageName;
  }

  copyFile(sourceUri: string, destinationPath: string) {
    let sourceFile: fs.File | null = null;
    let destFile: fs.File | null = null;

    try {
      sourceFile = fs.openSync(sourceUri, fs.OpenMode.READ_ONLY);
      destFile = fs.openSync(destinationPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      fs.copyFileSync(sourceFile.fd, destFile.fd);
    } catch (err) {
      hilog.error(0x0000, 'CopyFile', `Failed to copy file：${err.message}`);
    } finally {
      if (sourceFile) {
        try {
          fs.closeSync(sourceFile);
        } catch (closeError) {
          hilog.error(0x0000, 'ImageUtil', `close file error: ${closeError.message}`);
        }
      }

      if (destFile) {
        try {
          fs.closeSync(destFile);
        } catch (closeError) {
          hilog.error(0x0000, 'ImageUtil', `close file error: ${closeError.message}`);
        }
      }
    }
  }

  imageToImageSource(imagePath: string): image.ImageSource {
    let imageFile: fs.File | null = null;

    try {
      imageFile = fs.openSync(imagePath, fs.OpenMode.READ_ONLY);
      const STAT = fs.statSync(imagePath);
      const BUFFER = new ArrayBuffer(STAT.size);
      fs.readSync(imageFile.fd, BUFFER);

      const IMAGE_SOURCE = image.createImageSource(BUFFER);

      return IMAGE_SOURCE;
    } catch (error) {
      throw new Error('Failed to trans image.');
    } finally {
      if (imageFile) {
        try {
          fs.closeSync(imageFile);
        } catch (closeError) {
          hilog.error(0x0000, 'ImageUtil', `close file error: ${closeError.message}`);
        }
      }
    }
  }

  async imageFormatTrans(imageSource: image.ImageSource, targetPath: string): Promise<void> {
    if (!image.getImageSourceSupportedFormats().includes('image/heic')) {
      hilog.info(0x0000, 'ImageUtil', 'imageFormatTrans failed: heic not supported!');
      return;
    }
    let myFormat: string = 'image/heic';
    let myQuality: number = 98;

    let packOpts: image.PackingOption = {
      format: myFormat,
      quality: myQuality
    };
    let file: fs.File | null = null;
    const IMAGE_PACKER_API: image.ImagePacker = image.createImagePacker();

    try {
      file = fs.openSync(targetPath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);

      try {
        await IMAGE_PACKER_API.packToFile(imageSource, file.fd, packOpts);
        hilog.info(0x0000, 'ImageUtil', 'Succeeded in packing the image to file.');
      } catch (err) {
        hilog.error(0x0000, 'ImageUtil',
          `Failed to pack the image to file (inside packToFile). Code: ${err.code}, Message: ${err.message}`);
      }
    } catch (err) {
      hilog.error(0x0000, 'ImageUtil',
        `Failed to open file for writing. Code: ${err.code}, Message: ${err.message}`);
    } finally {
      if (file) {
        fs.closeSync(file);
      }
      IMAGE_PACKER_API.release((err: BusinessError) => {
        if (err) {
          hilog.error(0x0000, 'ImageUtil',
            `Failed to release image packaging.code ${err.code},message is ${err.message}`);
        } else {
          hilog.info(0x0000, 'ImageUtil', 'Succeeded in releasing image packaging.');
        }
      });
    }
  }

  saveToLocalFile(uiAbilityContext: common.UIAbilityContext, uiContext: UIContext, newFileName: string,
    sourcePath: string) {
    if (newFileName === '') {
      return;
    }
    let documentPicker = new picker.DocumentViewPicker(uiAbilityContext);
    let documentSaveOptions = new picker.DocumentSaveOptions();
    documentSaveOptions.newFileNames = [newFileName];
    documentPicker.save(documentSaveOptions).then((documentSaveResult: string[]) => {

      if (!documentSaveResult || documentSaveResult.length === 0 || !documentSaveResult[0]) {
        hilog.info(0x0000, 'saveToFile', 'User canceled the save operation.');
        return;
      }

      hilog.info(0x0000, 'saveToFile', 'DocumentViewPicker.save successfully, documentSaveResult uri: ' +
        JSON.stringify(documentSaveResult));
      documentSaveResult.forEach((path: string) => {
        this.copyFile(sourcePath, path);
      });

      uiContext.getPromptAction().showToast({
        message: `成功保存至本地`,
        duration: 1000
      });
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'saveToFile', 'DocumentViewPicker.save failed with err: ' + JSON.stringify(err));
    });
  }

  build() {
    Column() {
      Text('123')
      Button('点击拉起相机并拍照保存为 HEIF')
        .onClick(() => this.takePhotoAndSaveAsHEIF())
        .width('80%')
        .height(48)
        .fontSize(16)
        .fontWeight(500)
        .borderRadius(24)
        .backgroundColor('rgb(10, 89, 247)')
        .fontColor('white')
        .margin({ top: 100, bottom: 20 });

      Text('拍照后自动保存为 HEIF 格式')
        .fontSize(14)
        .fontColor('rgba(0, 0, 0, 0.6)')
        .textAlign(TextAlign.Center)
        .width('80%')
        .margin({ top: 16 });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }

  private async takePhotoAndSaveAsHEIF() {
    try {
      // 1. 拉起相机选择器
      const pickerProfile: cameraPicker.PickerProfile = {
        cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK,
      };

      const pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(
        this.context,
        [cameraPicker.PickerMediaType.PHOTO],
        pickerProfile
      );

      if (!pickerResult || !pickerResult.resultUri || pickerResult.resultUri.length === 0) {
        console.error('拍照失败：未获取到图像');
        return;
      }

      const originalUri = pickerResult.resultUri;
      const imageName = this.extractFileName(originalUri);
      const imageBaseName = this.getImageBaseName(imageName);
      const sandboxPath = this.context.filesDir + '/' + imageName;

      // 2. 复制原始图片到沙盒
      this.copyFile(originalUri, sandboxPath);

      // 3. 转换为 HEIF 格式
      const imageSource = this.imageToImageSource(sandboxPath);
      const targetPath = this.context.filesDir + '/' + imageBaseName + '.heic';

      await this.imageFormatTrans(imageSource, targetPath);

      // 4. 保存到本地
      this.saveToLocalFile(this.context, this.getUIContext(), imageBaseName + '.heic', targetPath);

      console.log('拍照并成功保存为 HEIF 格式：', targetPath);
    } catch (error) {
      let err = error as BusinessError;
      console.error('拍照或保存失败：', err.code, err.message);
    }
  }

  private extractFileName(uri: string): string {
    const index = uri.lastIndexOf('/') + 1;
    return decodeURIComponent(uri.slice(index));
  }
}
```

拍摄照片如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/SGHdAAJvSOmERP-ZVNPOiw/zh-cn_image_0000002628552486.png "点击放大")
