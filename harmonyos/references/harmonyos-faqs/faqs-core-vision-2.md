---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-vision-2
title: 如何解决主体分割保存的图片背景非透明的问题
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础视觉（Core Vision） > 如何解决主体分割保存的图片背景非透明的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:3b763d1807e1bd3cafdce122333681f8048fa6caec6660276ea6fa78e214be95
---

## 问题现象

使用主体分割，保存分割得到的前景图到沙箱中，保存的是PNG格式，图片背景是黑色的，不是透明背景。

将图片进行主体分割出来后，获取到的内容图片保存到沙箱中：

```ts
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct Index {
  @State chooseImage: PixelMap | undefined = undefined;
  subjectSegImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';
  @State maxNum: string = '20';

  async aboutToAppear() {
    initSubjectSegmentation();
  }

  aboutToDisappear(): void {
    releaseSubjectSegmentation();
  }

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Contain)
        .height('30%')
        .accessibilityDescription('Image to be split')

      Scroll() {
        Text(this.dataValues)
          .copyOption(CopyOptions.LocalDevice)
          .margin(10)
          .width('100%')
      }
      .height('20%')

      Row() {
        Text('Maximum number of principals:')
          .fontSize(16)
        TextInput({ placeholder: 'Please enter the maximum number of entities', text: this.maxNum })
          .type(InputType.Number)
          .placeholderColor(Color.Gray)
          .fontSize(16)
          .backgroundColor(Color.White)
          .onChange((value: string) => {
            this.maxNum = value;
          })
      }
      .width('80%')
      .margin(10)

      Button('Select image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // Pull up the gallery.
          this.selectImage();
        })

      Button('Start subject segmentation')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(async () => {
          if (!this.chooseImage) {
            return;
          }
          let visionInfo: subjectSegmentation.VisionInfo = {
            pixelMap: this.chooseImage
          };
          let config: subjectSegmentation.SegmentationConfig = {
            maxCount: parseInt(this.maxNum),
            enableSubjectDetails: true,
            enableSubjectForegroundImage: true
          };
          // Call the image segmentation API.
          let data: subjectSegmentation.SegmentationResult =
            await subjectSegmentation.doSegmentation(visionInfo, config);
          this.subjectSegImage = data.fullSubject.foregroundImage;
          let outputString = `Subjects: ${data.subjectCount}\n`;
          outputString += `Maximum subjects: ${config.maxCount}\n`;
          outputString += `Show bounding box of each subject: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
          let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
          let segBoxString = `Global bounding box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
          outputString += segBoxString;

          if (config.enableSubjectDetails) {
            outputString += 'Individual bounding boxes:\n';
            if (data.subjectDetails) {
              for (let i = 0; i < data.subjectDetails.length; i++) {
                let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
                outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
              }
            }
          }

          this.dataValues = outputString;
        })

      SaveButton({ icon: SaveIconStyle.LINES, buttonType: ButtonType.Circle })
        .onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result == SaveButtonOnClickResult.SUCCESS) {
            if (!this.subjectSegImage) {
              return;
            }
            // 配置图片编码参数
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
            const imagePackerApi: image.ImagePacker = image.createImagePacker();
            // 将PixelMap编码为JPEG格式的二进制数据
            imagePackerApi.packToData(this.subjectSegImage, packOpts).then(async (buffer: ArrayBuffer) => {
              try {
                // 保存至相册中
                const context: Context = this.getUIContext().getHostContext() as Context;
                let helper = photoAccessHelper.getPhotoAccessHelper(context);
                let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpeg');
                let file = await fs.open(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                await fs.write(file.fd, buffer);
                await fs.close(file.fd);
              } catch (error) {
                console.error(`error is ${error}`);
              }
            }).catch((error: BusinessError) => {
              console.error(`Failed to pack the image. ${error.code} ${error.name} ${error.message}`);
            });
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto();
    if (uri === undefined) {
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<Array<string>> {
    return new Promise<Array<string>>((resolve, reject) => {
      let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      PhotoSelectOptions.maxSelectNumber = 1;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
        resolve(PhotoSelectResult.photoUris);
      }).catch((err: BusinessError) => {
        console.error(err.message);
        reject();
      });
    });
  }

  private loadImage(names: string[]) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined;
      let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
      imageSource = image.createImageSource(fileSource.fd);
      this.chooseImage = await imageSource.createPixelMap();
    }, 100
    );
  }
}

async function initSubjectSegmentation() {
  const initResult = await subjectSegmentation.init();
  console.info('subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
}

async function releaseSubjectSegmentation() {
  await subjectSegmentation.release();
}
```

## 背景知识

* [主体分割](../harmonyos-references/core-vision-subjectsegmentation-api.md)：Core Vision Kit根据配置参数（如最多检测多少个物体、是否输出每个物体的详细信息等）可将一张普通的图片进行分割，分割后的信息包括图片整体的分割结果和每个显著物体的详细信息。
* [PackingOption](../harmonyos-references/arkts-apis-image-i.md#packingoption)：图片编码选项。

* [PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)：图像像素类，用于读取或写入图像数据以及获取图像信息。
* JPEG（Joint Photographic Experts Group）：是面向连续色调静止图像的一种压缩标准。JPEG格式是最常用的图像文件格式，后缀名为.jpg或.jpeg。

* PNG（Portable Network Graphics）：便携式网络图形，是一种采用无损压缩算法的位图格式，支持索引、灰度、RGB三种颜色方案以及Alpha通道等特性。

## 问题定位

1. 检查是否复现问题。
2. 检查保存过程中，是否转换成了JPEG等不支持透明通道的格式，参考PackingOption说明。

## 分析结论

保存过程中，转换成了JPEG等不支持透明通道的格式（因为JPEG不支持透明通道，若使用带透明通道的数据编码JPEG格式，透明通道将变为黑色）。

## 修改建议

避免将获得的PixelMap转换成JPEG，可考虑转换成PNG等支持透明通道的格式，例如上方问题代码里就转换成了JPEG格式。可以修改为其他格式，如PNG，完整的示例代码：

```ts
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct Index {
  @State chooseImage: PixelMap | undefined = undefined;
  subjectSegImage: PixelMap | undefined = undefined;
  @State dataValues: string = '';
  @State maxNum: string = '20';

  async aboutToAppear() {
    initSubjectSegmentation();
  }

  aboutToDisappear(): void {
    releaseSubjectSegmentation();
  }

  build() {
    Column() {
      Image(this.chooseImage)
        .objectFit(ImageFit.Contain)
        .height('30%')
        .accessibilityDescription('Image to be split')

      Scroll() {
        Text(this.dataValues)
          .copyOption(CopyOptions.LocalDevice)
          .margin(10)
          .width('100%')
      }
      .height('20%')

      Row() {
        Text('Maximum number of principals:')
          .fontSize(16)
        TextInput({ placeholder: 'Please enter the maximum number of entities', text: this.maxNum })
          .type(InputType.Number)
          .placeholderColor(Color.Gray)
          .fontSize(16)
          .backgroundColor(Color.White)
          .onChange((value: string) => {
            this.maxNum = value;
          })
      }
      .width('80%')
      .margin(10)

      Button('Select image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          // Pull up the gallery.
          this.selectImage();
        })

      Button('Start subject segmentation')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(async () => {
          if (!this.chooseImage) {
            return;
          }
          let visionInfo: subjectSegmentation.VisionInfo = {
            pixelMap: this.chooseImage
          };
          let config: subjectSegmentation.SegmentationConfig = {
            maxCount: parseInt(this.maxNum),
            enableSubjectDetails: true,
            enableSubjectForegroundImage: true
          };
          // Call the image segmentation API.
          let data: subjectSegmentation.SegmentationResult =
            await subjectSegmentation.doSegmentation(visionInfo, config);
          this.subjectSegImage = data.fullSubject.foregroundImage;
          let outputString = `Subjects: ${data.subjectCount}\n`;
          outputString += `Maximum subjects: ${config.maxCount}\n`;
          outputString += `Show bounding box of each subject: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
          let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
          let segBoxString = `Global bounding box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
          outputString += segBoxString;

          if (config.enableSubjectDetails) {
            outputString += 'Individual bounding boxes:\n';
            if (data.subjectDetails) {
              for (let i = 0; i < data.subjectDetails.length; i++) {
                let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
                outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
              }
            }
          }

          this.dataValues = outputString;
        })

      SaveButton({ icon: SaveIconStyle.LINES, buttonType: ButtonType.Circle })
        .onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
          if (result == SaveButtonOnClickResult.SUCCESS) {
            if (!this.subjectSegImage) {
              return;
            }
            // 配置图片编码参数
            let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
            const imagePackerApi: image.ImagePacker = image.createImagePacker();
            // 将PixelMap编码为JPEG格式的二进制数据
            imagePackerApi.packToData(this.subjectSegImage, packOpts).then(async (buffer: ArrayBuffer) => {
              try {
                // 保存至相册中
                const context: Context = this.getUIContext().getHostContext() as Context;
                let helper = photoAccessHelper.getPhotoAccessHelper(context);
                let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpeg');
                let file = await fs.open(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                await fs.write(file.fd, buffer);
                await fs.close(file.fd);
              } catch (error) {
                console.error(`error is ${error}`);
              }
            }).catch((error: BusinessError) => {
              console.error(`Failed to pack the image. ${error.code} ${error.name} ${error.message}`);
            });
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async selectImage() {
    let uri = await this.openPhoto();
    if (uri === undefined) {
    }
    this.loadImage(uri);
  }

  private openPhoto(): Promise<Array<string>> {
    return new Promise<Array<string>>((resolve, reject) => {
      let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      PhotoSelectOptions.maxSelectNumber = 1;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
        resolve(PhotoSelectResult.photoUris);
      }).catch((err: BusinessError) => {
        console.error(err.message);
        reject();
      });
    });
  }

  private loadImage(names: string[]) {
    setTimeout(async () => {
      let imageSource: image.ImageSource | undefined = undefined;
      let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
      imageSource = image.createImageSource(fileSource.fd);
      this.chooseImage = await imageSource.createPixelMap();
    }, 100
    );
  }
}

async function initSubjectSegmentation() {
  const initResult = await subjectSegmentation.init();
  console.info('subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
}

async function releaseSubjectSegmentation() {
  await subjectSegmentation.release();
}
```
