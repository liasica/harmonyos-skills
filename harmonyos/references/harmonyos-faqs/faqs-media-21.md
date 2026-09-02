---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-21
title: 媒体文件存在多个格式后缀
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 媒体文件存在多个格式后缀
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:107c21a1b8c3dc205ae8b5dde0ebf57186c8b488dd2f186675b6b1c691339cc4
---

## 问题现象

媒体文件保存至媒体库后，文件名中存在多个后缀名。

## 背景知识

* 保存图片、视频等用户文件到图库时，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，应用可以通过[安全保存控件](../harmonyos-guides/savebutton.md)或[授权弹窗](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)的方式，将用户指定的媒体资源保存到图库中。
* [showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)可以拉起保存确认弹窗，通过用户授权将媒体文件保存至媒体库中。
* [安全保存控件](../harmonyos-guides/savebutton.md)：保存控件允许用户通过点击按钮临时获取存储权限，无需权限弹框确认。集成保存控件后，当用户点击该控件时，应用会获得10秒内访问媒体库特权接口的授权。这适用于任何需要将文件保存到媒体库的应用场景，例如保存图片或视频等。

## 问题定位

1. 通过搜索文件名查看日志，发现文件处于应用沙箱下时格式正确，但是处于媒体库时名称已发生变化，增加了一层后缀。

   ```txt
   11-30 12:36:23.606  3564  3564 E A01010/com.example.hm: 文件大小：7.8MB, 路径：/data/storage/el2/base/haps/phone/files/2024-11-30_12:36:09.mp4
   ```

   ```txt
   11-30 12:37:10.046  3564  3564 I A03D00/com.example.hm: [picker] document save option: {"newFileNames":["2024-11-30_12_36_09.mp4.mp4"]}
   ```
2. 通过搜索photoAccessHelper关键词发现应用通过showAssetsCreationDialog方法将文本从应用沙箱保存至媒体库中。

   ```txt
   11-30 12:36:26.592 40535  5115 I A03D00/com.huawei.hmos.photos/JSAPP: photoAccessHelper  getPhotoAccessHelper inner add createDeleteRequest and showAssetsCreationDialog
   ```
3. 排查代码是否在photoCreationConfigs的title参数中添加了文件后缀。

   ```ts
   let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
     {
       title: 'test.mp4', // 可选。
       fileNameExtension: 'mp4',
       photoType: photoAccessHelper.PhotoType.IMAGE,
       subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // 可选。
     }
   ];
   ```

## 分析结论

应用使用showAssetsCreationDialog将媒体文件保存到媒体库时，错误填写了showAssetsCreationDialog的title参数，传入了文件的格式导致最终保存的媒体文件出现多个格式。

## 修改建议

参考如下代码，在创建photoCreationConfigs时，传入的title参数仅包含媒体文件名称即可，不需要传入文件格式后缀。

```ts
// 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选
let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
  {
    title: 'test',
    fileNameExtension: 'mp4',
    photoType: photoAccessHelper.PhotoType.VIDEO,
    subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
  }
];
// 基于弹窗授权的方式获取媒体库的目标uri
let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
```

完整示例参考如下：

```ts
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { http } from '@kit.NetworkKit';
import { util } from '@kit.ArkTS';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct CreationDialogIndexPage {
  // videoSrc需要替换成应用自己的链接，否则后续无法成功运行
  @State videoSrc: string = 'XXX.XXX.XXX';
  @State imageBuffer: ArrayBuffer | undefined = undefined;
  public context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_FILE,
    buttonType: ButtonType.Capsule
  };
  private controller: VideoController | undefined;

  aboutToAppear(): void {
    // 每一个httpRequest对应一个HTTP请求任务，不可复用
    let httpRequest = http.createHttp();
    let options: http.HttpRequestOptions = {
      method: http.RequestMethod.GET,
      readTimeout: 60000,
      connectTimeout: 60000,
      maxLimit: 100 * 1024 * 1024,
      expectDataType: http.HttpDataType.ARRAY_BUFFER
    };

    httpRequest
      .request(this.videoSrc, options,
        async (error: BusinessError, data: http.HttpResponse) => {
          if (error) {
            this.getUIContext().getPromptAction().showToast({
              message: '文件下载失败，请检查网络',
              duration: 5000
            });
          }
          // 判断网络获取到的资源是否为ArrayBuffer类型
          if (data.result instanceof ArrayBuffer) {
            this.imageBuffer = data.result as ArrayBuffer;

          }
        }
      );
  }

  async dialogSave(imageBuffer: ArrayBuffer) {
    try {
      //下载后的数据保存到Cache目录下
      const newFileName = util.generateRandomUUID() + '.mp4';
      const newFilePath = this.context.cacheDir + '/' + newFileName;
      const srcFileUri = fileUri.getUriFromPath(newFilePath);
      let file: fs.File = await fs.open(srcFileUri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      await fs.write(file.fd, imageBuffer);
      await fs.close(file);
      console.info('文件路径：' + srcFileUri);
      let srcFileUris: Array<string> = [
        srcFileUri
      ];
      // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选
      let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
        {
          title: 'test',
          fileNameExtension: 'mp4',
          photoType: photoAccessHelper.PhotoType.VIDEO,
          subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
        }
      ];
      // 基于弹窗授权的方式获取媒体库的目标uri
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
      let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
      // 将来源于应用沙箱的照片内容写入媒体库的目标uri
      let desFile: fs.File = await fs.open(desFileUris[0], fs.OpenMode.WRITE_ONLY);
      let srcFile: fs.File = await fs.open(srcFileUri, fs.OpenMode.READ_ONLY);
      await fs.copyFile(srcFile.fd, desFile.fd);
      fs.closeSync(srcFile);
      fs.closeSync(desFile);
      console.info('create asset by dialog successfully');
    } catch (err) {
      console.error(`failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`);
    }
  }

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height(300);

      Button(this.imageBuffer ? '弹窗授权保存文件' : '等待文件下载')
        .fontSize(14)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          if (this.imageBuffer) {
            this.dialogSave(this.imageBuffer);
          }
        })
        .enabled(this.imageBuffer != null)
        .height('5%')
        .width('50%');

    }.width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceEvenly);
  }
}
```
