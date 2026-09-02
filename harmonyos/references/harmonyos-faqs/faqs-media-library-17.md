---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-17
title: 如何解析网络图片URI的后缀名并将其保存至相册
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何解析网络图片URI的后缀名并将其保存至相册
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ca470831172d66877215faba7c55c078981e703c2031b4df36d20cc3e994e008
---

## 问题现象

通过[photoAccessHelper.createAsset](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#createasset)申请一个uri，需要传入extension后缀名，但有些图片文件无法通过uri解析后缀，如何判断其文件类型并将其保存至相册？

## 背景知识

可以调用[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)拉起保存确认弹窗。用户同意保存后，返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。如果用户拒绝保存，将返回空列表。

## 解决方案

1. 需要在module.json5中配置网络权限[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)：

   ```ts
   {
     "name": "ohos.permission.INTERNET",
     "reason": "$string:reason_internet",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ]
     }
   }
   ```
2. 解析网络图片文件类型并保存至沙箱，再从沙箱中进行加载。

   ```ts
   import { http } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { fileIo, fileIo as fs, fileUri } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State filePath: string = '';
     context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
     type: string = '';

     loadImageWithUrl(url: string) {
       let responseCode = http.ResponseCode;
       let OutData: http.HttpResponse;
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let filesDir = context.filesDir;
       // 确保网络正常
       http.createHttp().request(url, {
         method: http.RequestMethod.GET,
         connectTimeout: 60000,
         readTimeout: 60000
       },
         async (error: BusinessError, data: http.HttpResponse) => {
           if (error) {
             console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
           } else {
             OutData = data;
             let code: http.ResponseCode | number = OutData.responseCode;
             let contentType: string = OutData.header['content-type'];

             let index = contentType.indexOf('/');
             let type: string = contentType.substring(index + 1);
             this.type = type;

             console.info('contentType=' + contentType);
             if (responseCode.OK === code) {
               let imageData: ArrayBuffer = OutData.result as ArrayBuffer;
               let file = fs.openSync(filesDir + '/test.' + type, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
               // 写入文件
               await fs.write(file.fd, imageData);
               // 关闭文件
               await fs.close(file.fd);

               try {
                 // 指定待保存到媒体库的位于应用沙箱的图片url
                 let srcFileUri = 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.' + type;

                 let srcFileUris: Array<string> = [
                   srcFileUri
                 ];
                 // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选
                 let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
                   {
                     title: 'test', // 可选
                     fileNameExtension: type,
                     photoType: photoAccessHelper.PhotoType.IMAGE,
                     subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // 可选
                   }
                 ];
                 // 基于弹窗授权的方式获取媒体库的目标uri
                 let desFileUris: Array<string> =
                   await this.phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
                 // 将来源于应用沙箱的照片内容写入媒体库的目标uri
                 let desFile: fileIo.File = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
                 let srcFile: fileIo.File = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
                 await fileIo.copyFile(srcFile.fd, desFile.fd);
                 fileIo.closeSync(srcFile);
                 fileIo.closeSync(desFile);

                 console.info('create asset by dialog successfully');
               } catch (err) {
                 console.error(`failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}`);
               }
             }
           }
         }
       );
     }

     build() {
       Row() {
         Column({ space: 10 }) {
           Image(this.filePath)
             .width('80%')
             .height(200)

           Button('显示').onClick(() => {
             let srcFileUri = 'file://com.example.myapplication/data/storage/el2/base/haps/entry/files/test.' + this.type;
             this.filePath = fileUri.getUriFromPath(srcFileUri);
           })

           // 开发者需手动替换成网络图片url
           Image('example.png')
             .width('80%')
             .height(200)

           // 开发者需手动替换成网络图片url
           Button('加载图片url').onClick(async () => {
             this.loadImageWithUrl('example.png');
           })
         }
         .width('100%')
       }
       .height('100%')
       .backgroundColor(0xF1F3F5)
     }
   }
   ```
