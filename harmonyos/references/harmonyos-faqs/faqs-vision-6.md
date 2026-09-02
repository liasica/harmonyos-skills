---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-6
title: 文档扫描后保存图片预览页面空白
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 文档扫描后保存图片预览页面空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:22d34ba43ae4ff34ac3e6b54df9ff040cf75f96728b0dda9700edc7ba1f7cdab
---

## 问题现象

文档扫描控件DocumentScanner扫描出图片后，使用相册管理模块弹窗showAssetsCreationDialog保存图片，预览页面空白。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/6dhNrk9YTE2EfbpCr0hcIw/zh-cn_image_0000002628554718.gif "点击放大")

## 背景知识

* 文档扫描控件[DocumentScanner](../harmonyos-references/vision-document-scanner.md)提供拍摄文档并转换为高清扫描件的服务。仅需使用手机拍摄文档，即可自动裁剪和优化，并支持jpeg图片、PDF格式保存和分享；同时支持拍摄拍照或图片识别表格，生成表格文档。
* 相册管理模块[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)调用接口拉起保存确认弹窗。用户同意保存后，返回已创建并授予保存权限的URI列表，该列表永久生效，应用可使用该URI写入图片/视频。

## 问题定位

* 文档扫描控件DocumentScanner问题：DocumentScanner控件在文档扫描结束后，仅在结果回调[DocumentScannerResultCallback](../harmonyos-references/vision-document-scanner.md#documentscannerresultcallback)中生成一个临时文档URI列表。
* 相册管理模块弹窗问题：查看接口showAssetsCreationDialog参数，发现入参的srcFileUris可能存在问题导致预览空白。

## 分析结论

当使用文档扫描控件DocumentScanner完成回调后得到URI列表，再调用接口showAssetsCreationDialog，由于showAssetsCreationDialog的入参srcFileUris需要使用[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)获取的沙箱路径URI或者[媒体文件URI](../harmonyos-guides/user-file-uri-intro.md#媒体文件uri)，才可以正常预览，但实际入参的srcFileUris是临时生成的，导致保存图片预览页面空白。

## 解决方案

使用文档扫描控件DocumentScanner完成回调后，将图片保存至沙箱目录下，后调用接口showAssetsCreationDialog保存图片，可以正常显示并保存图片至图库。

1. 根据业务场景将扫描得到的图片保存至沙箱目录下。

   ```ts
   saveListPicture(uris: string[]) {
     // 将图片保存至沙箱目录下
     let srcFile = fileIo.openSync(uris[0], fileIo.OpenMode.READ_ONLY);
     const destFileUri = fileUri.getUriFromPath(`${this.context.cacheDir}/${util.generateRandomUUID()}.jpg`);
     let destFile: fileIo.File = fileIo.openSync(destFileUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     fileIo.copyFileSync(srcFile.fd, destFile.fd);
     fileIo.closeSync(srcFile);
     fileIo.closeSync(destFile);
     hilog.info(0x0001, TAG, `文件路径：${destFileUri}`);

     this.saveImageToAsset(destFileUri, 'jpg').then(() => {
       promptAction.openToast({ message: '保存成功' });
     }).catch(() => {
       promptAction.openToast({ message: '保存失败' });
     });
   }
   ```
2. 使用fileUri.getUriFromPath获取保存到沙箱目录的文件URI作为参数，调用接口showAssetsCreationDialog保存图片。

   ```ts
   async saveImageToAsset(uri: string, nameExtension: string): Promise<void> {
     hilog.info(0x0001, TAG, `ShowAssetsCreationDialogDemo：${uri}`);
   try {
     let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
     // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri
     let srcFileUris: Array<string> = [uri];
     let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [{
       title: 'test',
       // 可选
       fileNameExtension: nameExtension,
       photoType: photoAccessHelper.PhotoType.IMAGE,
       // 可选，支持：普通图片、动态图片
       subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
     }];
     let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
     hilog.info(0x0001, TAG, `showAssetsCreationDialog success, data is：${desFileUris}`);
     if (desFileUris.length == 0) {
       // 用户拒绝保存
       throw (new Error('用户拒绝保存'));
     }
     this.createAssetByIo(uri, desFileUris[0]);
     return Promise.resolve();
   } catch (err) {
     hilog.error(0x0001, TAG, `showAssetsCreationDialog failed, errCode is：${err.code}` + `errMsg is：${err.message}`);
     return Promise.reject(err);
   }
   }

   createAssetByIo(sourceFilePath: string, targetFilePath: string) {
     try {
       hilog.info(0x0001, TAG, `文件路径：${this.context.filesDir}`);
       let srcFile: fileIo.File = fileIo.openSync(sourceFilePath, fileIo.OpenMode.READ_ONLY);
       let targetFile: fileIo.File = fileIo.openSync(targetFilePath, fileIo.OpenMode.READ_WRITE);
       fileIo.copyFileSync(srcFile.fd, targetFile.fd);
       fileIo.closeSync(srcFile);
       fileIo.closeSync(targetFile);
     } catch (error) {
       hilog.error(0x0001, TAG, `showAssetsCreationDialog failed, msg is：${error}`);
     }
   }
   ```

完整示例参考如下：

```ts
import {
  DocType,
  DocumentScanner,
  DocumentScannerConfig,
  SaveOption,
  FilterId,
  ShootingMode
} from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileUri } from '@kit.CoreFileKit';
import { util } from '@kit.ArkTS';
import { fileIo } from '@kit.CoreFileKit';
import { promptAction } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

const TAG: string = 'DocDemoPage';

@Entry
@Component
export struct DocDemoPage {
  @State docImageUris: string[] = [];
  private docScanConfig = new DocumentScannerConfig();
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear() {
    this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET];
    this.docScanConfig.isGallerySupported = true;
    this.docScanConfig.editTabs = [];
    this.docScanConfig.maxShotCount = 3;
    this.docScanConfig.defaultFilterId = FilterId.ORIGINAL;
    this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL;
    this.docScanConfig.isShareable = true;
    this.docScanConfig.originalUris = [];
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.Top }) {
        // 展示文档扫描结果
        List() {
          ForEach(this.docImageUris, (uri: string) => {
            ListItem() {
              Image(uri)
                .objectFit(ImageFit.Contain)
                .width(100)
                .height(100);
            };
          });
        }
        .listDirection(Axis.Vertical)
        .alignListItem(ListItemAlign.Center)
        .margin({
          top: 50
        })
        .width('80%')
        .height('80%');

        // 文档扫描
        DocumentScanner({
          scannerConfig: this.docScanConfig,
          onResult: (code: number, saveType: SaveOption, uris: string[]) => {
            hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`);
            if (code === -1) {
              promptAction.openToast({ message: 'failed' });
            } else {
              if (uris.length > 0) {
                this.saveListPicture(uris);
              }
            }
            uris.forEach(uriString => {
              hilog.info(0x0001, TAG, `uri: ${uriString}`);
            });
            this.docImageUris = uris;
          }
        })
          .size({ width: '100%', height: '100%' });
      }
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%');
  }

  saveListPicture(uris: string[]) {
    // 将图片保存至沙箱目录下
    let srcFile = fileIo.openSync(uris[0], fileIo.OpenMode.READ_ONLY);
    const destFileUri = fileUri.getUriFromPath(`${this.context.cacheDir}/${util.generateRandomUUID()}.jpg`);
    let destFile: fileIo.File = fileIo.openSync(destFileUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    fileIo.copyFileSync(srcFile.fd, destFile.fd);
    fileIo.closeSync(srcFile);
    fileIo.closeSync(destFile);
    hilog.info(0x0001, TAG, `文件路径：${destFileUri}`);

    this.saveImageToAsset(destFileUri, 'jpg').then(() => {
      promptAction.openToast({ message: '保存成功' });
    }).catch(() => {
      promptAction.openToast({ message: '保存失败' });
    });
  }

  async saveImageToAsset(uri: string, nameExtension: string): Promise<void> {
    hilog.info(0x0001, TAG, `ShowAssetsCreationDialogDemo：${uri}`);
    try {
      let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
      // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri
      let srcFileUris: Array<string> = [uri];
      let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [{
        title: 'test',
        // 可选
        fileNameExtension: nameExtension,
        photoType: photoAccessHelper.PhotoType.IMAGE,
        // 可选，支持：普通图片、动态图片
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      }];
      let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
      hilog.info(0x0001, TAG, `showAssetsCreationDialog success, data is：${desFileUris}`);
      if (desFileUris.length == 0) {
        // 用户拒绝保存
        throw (new Error('用户拒绝保存'));
      }
      this.createAssetByIo(uri, desFileUris[0]);
      return Promise.resolve();
    } catch (err) {
      hilog.error(0x0001, TAG, `showAssetsCreationDialog failed, errCode is：${err.code}` + `errMsg is：${err.message}`);
      return Promise.reject(err);
    }
  }

  createAssetByIo(sourceFilePath: string, targetFilePath: string) {
    try {
      hilog.info(0x0001, TAG, `文件路径：${this.context.filesDir}`);
      let srcFile: fileIo.File = fileIo.openSync(sourceFilePath, fileIo.OpenMode.READ_ONLY);
      let targetFile: fileIo.File = fileIo.openSync(targetFilePath, fileIo.OpenMode.READ_WRITE);
      fileIo.copyFileSync(srcFile.fd, targetFile.fd);
      fileIo.closeSync(srcFile);
      fileIo.closeSync(targetFile);
    } catch (error) {
      hilog.error(0x0001, TAG, `showAssetsCreationDialog failed, msg is：${error}`);
    }
  }
}
```

## 常见FAQ

Q：文本识别（TextRecognition）和文档扫描（DocumentScanner）是否有使用限制？

A：有，单个App每个月最多被调用10000次，超过将无法使用。

Q：let desFileUris: Array<string> = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs); desFileUris数组中的URI里面返回的是-3006。

A：photoCreationConfigs中的title值，不可以包含：([./:\*?"'`<>|{}[]])等这些特殊字符。
