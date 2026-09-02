---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-47
title: 应用内如何直接展示本应用保存到图库的图片和视频
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 应用内如何直接展示本应用保存到图库的图片和视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77e261e7ea000172296b4d304aa25385331e1c748c98fafb009f6050ddae7313
---

## 问题现象

应用使用受限权限ohos.permission.READ\_IMAGEVIDEO可以筛选出保存在媒体库的图片和视频资源进行展示，是否有非受限权限的处理方案？

## 背景知识

* [ohos.permission.READ\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionread_imagevideo)受限权限允许读取用户公共目录的图片或视频文件，可申请此权限的特殊场景与功能：应用需要克隆、备份或同步图片/视频类文件。
* 应用可以使用安全控件或授权弹窗的方式，将用户指定的媒体资源保存到图库中，使用方式请参考：[保存媒体库资源](../harmonyos-guides/photoaccesshelper-savebutton.md)。
* 相册管理模块photoAccessHelper下的[getAssets](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#getassets)接口可以获取图库中的图片和视频资源。

## 解决方案

应用保存到图库的图片和视频，应用默认对这些资源具备读的权限，应用只需获取这些资源对应的媒体uri，通过[video](../harmonyos-references/ts-media-components-video.md)组件加载展示，就可以实现应用内展示图库中自己保存的资源的诉求，无需申请受限权限，获取应用保存到图库的媒体uri可通过如下方案。

1. 安全控件保存资源到图库。

   应用使用安全控件[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)保存资源到图库，调用photoAccessHelper.createAsset创建媒体资源时获取的就是媒体uri，如下面示例中的photoUri。

   ```ts
   SaveButton(this.saveButtonOptions) // 创建安全控件按钮
     .onClick(async (event, result: SaveButtonOnClickResult) => {
       if (result == SaveButtonOnClickResult.SUCCESS) {
         try {
           // 1、使用安全控件创建文件
           let phAccessHelper: photoAccessHelper.PhotoAccessHelper =
             photoAccessHelper.getPhotoAccessHelper(this.context);
           let options: photoAccessHelper.CreateOptions = {
             title: Date.now().toString()
           };
           let photoUri: string =
             await phAccessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
           console.info('CameraDemo createAsset successfully, photoUri: ' + photoUri);
           // 2.1、方式一：通过文件管理写入文件
           let file = fs.openSync(photoUri, fs.OpenMode.WRITE_ONLY);
           fs.writeSync(file.fd, this.imageBuffer); //图片的buffer数据
           fs.closeSync(file);
         } catch (error) {
           let err = error as BusinessError;
           console.error(`CameraDemo savePicture error: ${JSON.stringify(err)}`);
         }
       } else {
         console.error('CameraDemo SaveButtonOnClickResult createAsset failed.');
       }
     });
   ```
2. 弹窗授权保存资源到图库。

   应用使用弹窗授权[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)方式保存资源到图库，调用phAccessHelper.showAssetsCreationDialog保存媒体资源时获取的就是媒体uri，如下面示例中的desFileUris。

   ```ts
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
   ```
3. 通过getAssets接口查询获取媒体uri。

   应用通过相册管理模块photoAccessHelper下的getAssets查询接口，会查询出应用有读权限的图片和视频，也就是查询到应用本身保存到图库的这些资源，从而获取到这些资源的媒体uri。

   ```ts
   async getAssetsUri(): Promise<void> {
     let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
     let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
     let fetchOption: photoAccessHelper.FetchOptions = {
       fetchColumns: [photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT,
         photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION],
       predicates: predicates
     };
     let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
     await phAccessHelper.getAssets(fetchOption);
     // 得到uri对应的PhotoAsset对象，读取文件的部分信息
     const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
     // 获取到的媒体uri
     this.videoSrc = asset.uri;
   }
   ```

完整示例参考如下：

```ts
import fs from '@ohos.file.fs';
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
import photoAccessHelper from '@ohos.file.photoAccessHelper';
import http from '@ohos.net.http';
import fileIo from '@ohos.file.fs';
import { util } from '@kit.ArkTS';
import { fileUri } from '@kit.CoreFileKit';
import { dataSharePredicates } from '@kit.ArkData';

@Entry
@Component
struct Index {
  private controller: VideoController | undefined;
  @State videoSrc: string = '';
  // url需要替换成应用自己的链接，否则后续无法成功运行
  public url: string = 'XXXX';
  @State imageBuffer: ArrayBuffer | undefined = undefined;
  public context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_FILE,
    buttonType: ButtonType.Capsule
  };

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
      .request(this.url, options,
        async (error: BusinessError, data: http.HttpResponse) => {
          if (error) {
            console.error('httpRequest failed.');
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

  /**
   *通过getAssets接口查询应用自身保存到图库的资源，无需申请受限权限
   */
  async getAssetsUri(): Promise<void> {
    let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [photoAccessHelper.PhotoKeys.WIDTH, photoAccessHelper.PhotoKeys.HEIGHT,
        photoAccessHelper.PhotoKeys.TITLE, photoAccessHelper.PhotoKeys.DURATION],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await phAccessHelper.getAssets(fetchOption);
    // 得到uri对应的PhotoAsset对象，读取文件的部分信息
    const asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    // 获取到的媒体uri
    this.videoSrc = asset.uri;
  }

  build() {
    Column() {
      Text(' ').fontSize(20);
      Text('方案一：安全控件获取uri');
      SaveButton(this.saveButtonOptions) // 创建安全控件按钮
        .onClick(async (event, result: SaveButtonOnClickResult) => {
          if (result == SaveButtonOnClickResult.SUCCESS) {
            try {
              // 1、使用安全控件创建文件
              let phAccessHelper: photoAccessHelper.PhotoAccessHelper =
                photoAccessHelper.getPhotoAccessHelper(this.context);
              let options: photoAccessHelper.CreateOptions = {
                title: Date.now().toString()
              };
              let photoUri: string =
                await phAccessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
              console.info('CameraDemo createAsset successfully, photoUri: ' + photoUri);
              // 2.1、方式一：通过文件管理写入文件
              let file = fs.openSync(photoUri, fs.OpenMode.WRITE_ONLY);
              fs.writeSync(file.fd, this.imageBuffer); //图片的buffer数据
              fs.closeSync(file);
            } catch (error) {
              let err = error as BusinessError;
              console.error(`CameraDemo savePicture error: ${JSON.stringify(err)}`);
            }
          } else {
            console.error('CameraDemo SaveButtonOnClickResult createAsset failed.');
          }
        });

      Text(' ').fontSize(20);
      Text('方案二：弹窗授权获取uri');
      Button('弹窗授权获取uri')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          if (this.imageBuffer) {
            this.dialogSave(this.imageBuffer);
          }
        })
        .height('5%')
        .width('50%');

      Text(' ').fontSize(20);
      Text('方案三：直接查询媒体uri');
      Button('直接查询媒体uri')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.getAssetsUri();
        })
        .height('5%')
        .width('50%');

      Video({
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .height(300);
    };
  }
}
```
