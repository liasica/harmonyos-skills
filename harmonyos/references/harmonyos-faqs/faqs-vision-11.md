---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-11
title: AI识图识别沙箱图片
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > AI识图识别沙箱图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b9d2c059e3f9350c59c539685a2066961756c34e61d37a9df4b262cbda143eb
---

## 问题现象

调试[AI识图](../harmonyos-guides/vision-imageanalyzer.md)时，使用沙箱图片发现图片不显示。

## 解决方案

AI识图可以在[Image](../harmonyos-references/ts-basic-components-image.md#image12-1)组件上配置，满足src类型即可，可参考以下代码：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import fs from '@ohos.file.fs';
import { common } from '@kit.AbilityKit';
import fileIo from '@ohos.file.fs';
import { visionImageAnalyzer } from '@kit.VisionKit';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct SavePixelMapToAlbum {
  @State imageUrl: string = '';
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE,
    buttonType: ButtonType.Capsule
  };
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
    new visionImageAnalyzer.VisionImageAnalyzerController();

  aboutToAppear(): void {
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange',
      (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
        console.info('DEMO_TAG', `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`);
      });
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info('DEMO_TAG', `textAnalysis result: ${JSON.stringify(text)}`);
    });
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info('DEMO_TAG', `selectedTextChange result: ${JSON.stringify(selectedText)}`);
    });
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info('DEMO_TAG', `subjectAnalysis result: ${JSON.stringify(subjects)}`);
    });
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info('DEMO_TAG', `selectedSubjectsChange result: ${JSON.stringify(subjects)}`);
    });
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error('DEMO_TAG', `analyzerFailed result: ${JSON.stringify(error)}`);
    });
  }

  async packToFile(pixelMap?: PixelMap): Promise<string> {
    // 获取应用文件路径
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filesDir: string = context.cacheDir;
    let picName = '/testing' + new Date().getTime() + '.jpg';
    // 新建并打开文件
    let file = fs.openSync(filesDir + picName, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    // 创建图像编码ImagePacker对象
    const imagePackerApi = image.createImagePacker();
    const options: image.PackingOption = { format: 'image/jpeg', quality: 98 };
    await imagePackerApi.packToFile(pixelMap, file.fd, options);
    return file.path;
  }

  build() {
    Row() {
      Column() {
        Image(this.imageUrl, {
          types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
          aiController: this.visionImageAnalyzerController
        }
        )
          .enableAnalyzer(true)
          .width(300)
          .height(300)
          .border({ width: 1 });
        Text('选择相册图片,并保存到沙盒路径');
        SaveButton(this.saveButtonOptions)
          .onClick(async (event, result: SaveButtonOnClickResult) => {
            if (result === SaveButtonOnClickResult.SUCCESS) {
              try {
                let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
                PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
                PhotoSelectOptions.maxSelectNumber = 5;
                let photoPicker = new photoAccessHelper.PhotoViewPicker();
                photoPicker.select(PhotoSelectOptions)
                  .then(async (PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
                    console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' +
                    JSON.stringify(PhotoSelectResult));
                    // 获取相册图片URI
                    let filePath = PhotoSelectResult.photoUris[0];
                    let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
                    // 通过传入文件描述符来创建图片源实例
                    let imageSource: image.ImageSource = image.createImageSource(file.fd);
                    let pixelMap: image.PixelMap = await imageSource.createPixelMap();
                    // 保存到沙盒路径
                    let url = await this.packToFile(pixelMap);
                    this.imageUrl = fileUri.getUriFromPath(url);
                  })
                  .catch((err: BusinessError) => {
                    console.error('PhotoViewPicker.select failed with err: ' + JSON.stringify(err));
                  });
              } catch (error) {
                let err: BusinessError = error as BusinessError;
                console.error('PhotoViewPicker failed with err: ' + JSON.stringify(err));
              }
            }
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
