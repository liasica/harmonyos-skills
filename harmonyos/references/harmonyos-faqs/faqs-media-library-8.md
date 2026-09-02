---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-8
title: 保存图片时，预览图显示空白
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 保存图片时，预览图显示空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:614deb05176074c816f84781510ba049ae6bd14bfa3c10da3cf59be68a240c66
---

## 问题现象

保存图片时，显示的预览图是空白的。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/AMcYMjcCQ1Gu1DxKgGMG7Q/zh-cn_image_0000002629059030.png "点击放大")

## 背景知识

* [showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)：调用接口拉起保存确认弹窗。用户同意保存后，返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。如果用户拒绝保存，将返回空列表。
* [fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)：通过传入的路径path生成应用自己的uri；将path转uri时，路径中的中文及非数字字母的特殊字符将会被编译成对应的ASCII码，拼接在uri中。
* 沙箱是指用于网络编程的虚拟环境，可用于测试应用程序，其运行结果不会影响系统状态。[沙箱路径](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)是指应用程序在沙箱中的具体路径。

## 问题定位

排查代码中showAssetsCreationDialog传入的srcFileUris参数中是否为沙箱目录下的文件uri数组。排查是否使用getUriFromPath将沙箱文件路径转换为文件uri。如果srcFileUris参数中使用的uri为沙箱文件的路径而非文件uri，会导致界面预览空白。

## 分析结论

showAssetsCreationDialog方法中传入的uri数组使用了沙箱文件的路径，并非文件uri，导致保存图片时预览图空白。

## 修改建议

showAssetsCreationDialog参数srcFileUris为需保存到媒体库中的图片文件对应的媒体库uri，因此需要使用fileUri.getUriFromPath补全传入的路径，保存时即可预览图片。

```ts
import { common } from '@kit.AbilityKit';
import fs from '@ohos.file.fs';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@ohos.base';
import { JSON } from '@kit.ArkTS';
import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct SaveImage {
  build() {
    Column() {
      Button('保存图片')
        .onClick(async () => {
          try {
            await this.save(this.ResourceToSandBox());
          } catch (e) {
            console.error('[ERROR]', JSON.stringify(e as BusinessError));
          }
        });
    }
    .height('100%')
    .width('100%')
    .padding({ top: 50 });
  }

  // 将资源文件复制到沙箱目录下，返回沙箱目录下文件的uri
  ResourceToSandBox() {
    const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let fileName = 'startIcon.png';
    let filePath = context.tempDir + fileName; // 沙箱目录中图片文件的路径
    // 复制文件，以资源目录下的startIcon.png为例
    let arrayBuff = context.resourceManager.getMediaContentSync($r('app.media.startIcon').id).buffer;
    let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    fs.writeSync(file.fd, arrayBuff);
    fs.closeSync(file.fd);
    let dirUri = fileUri.getUriFromPath(filePath); // 通过传入的路径path生成uri
    return dirUri;
  }

  // 弹窗授权保存图片到相册，dirUri参数是本地沙箱路径中需要保存的图片文件的uri
  // 此处为示例，保存一张图片
  async save(dirUri: string) {
    let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [{
      fileNameExtension: 'png', // 此处图片文件的后缀是.png
      photoType: photoAccessHelper.PhotoType.IMAGE,
    }];
    let srcFileUris = [dirUri];
    let context = this.getUIContext().getHostContext();
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let desFileUris: Array<string> =
      await phAccessHelper.showAssetsCreationDialog([dirUri], photoCreationConfigs); // 使用弹窗授权保存图片到相册
    let srcFile = fs.openSync(srcFileUris[0], fs.OpenMode.READ_ONLY);
    let desFile = fs.openSync(desFileUris[0], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    fs.copyFileSync(srcFile.fd, desFile.fd);
    fs.closeSync(srcFile);
    fs.closeSync(desFile);
  }
}
```
