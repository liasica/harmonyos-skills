---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-54
title: 无法在文件管理和图库中查看下载的图片
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 无法在文件管理和图库中查看下载的图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac02d4a334ed3706894b66e8bc87dd8fda74c912675ab05e9be55d1b710789dc
---

## 问题现象

图片显示下载完成，无法在文件管理和图库中查看下载的图片。

## 背景知识

* [request.downloadFile](../harmonyos-references/js-apis-request.md#requestdownloadfile9)：创建并启动一个下载任务，使用Promise异步回调，支持HTTP协议。
* [应用沙箱目录与应用沙箱路径](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)：应用沙箱是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。
* [用户文件概述](../harmonyos-guides/user-file-overview.md)：存放登录到该终端设备的用户所拥有的文件，包括用户私有的图片、视频、音频、文档等。

## 问题定位

1. 排查request.downloadFile接口是否已经将图片下载至应用沙箱目录，应用沙箱目录图片uri，参考路径：

   ```shell
   'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'
   ```
2. 排查是否使用文件拷贝相关函数将应用沙箱目录中的文件保存到用户文件目录。

## 分析结论

1. 图片已保存至应用沙箱目录。
2. 没有使用文件拷贝相关函数将应用沙箱目录中的文件保存到用户文件目录，导致无法在文件管理和图库中查看下载的图片。

## 修改建议

基于弹窗授权的方式保存到图库中，无需申请相册管理模块权限'ohos.permission.WRITE\_IMAGEVIDEO'，通过request.downloadFile保存网络图片到应用沙箱，再通过调用saveImageToAlbum将应用沙箱目录下的图片uri，保存至用户文件目录下。

```ts
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct PictureSave {
  uiContext = this.getUIContext();

  async savePng() {
    console.debug(`image => 保存网络图片到应用沙箱`);
    const context = this.uiContext?.getHostContext();
    let dirPath = context?.cacheDir;
    let fileName = 'temp2.jpg';

    // 防止沙箱重名导致下载失败
    if (fileIo.accessSync(`${dirPath}/${fileName}`)) {
      fileIo.rmdirSync(`${dirPath}/${fileName}`);
    }
    // 请将url替换成实际图片地址
    try {
      request.downloadFile(context, {
        enableMetered: true,
        url: 'www.example.com',
        filePath: `${dirPath}/${fileName}`
      }).then((downloadTask: request.DownloadTask) => {
        downloadTask.on('fail', (err: number) => {
          console.error(`Failed to download the task. Code: ${err}`);
        });
        downloadTask.on('complete', async () => {
          console.info('下载完成');
        });
      }
      )
        .catch((err: BusinessError) => {
          console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
        });

      this.saveImageToAlbum(`${dirPath}/${fileName}`);

    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  async saveImageToAlbum(path: string): Promise<boolean> {
    return new Promise(async (resolve: Function, reject: Function) => {
      try {
        const context = this.uiContext?.getHostContext();
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        let srcFileUri: Array<string> = [fileUri.getUriFromPath(path)];

        let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [
          {
            title: '保存图片',
            fileNameExtension: 'jpg',
            photoType: photoAccessHelper.PhotoType.IMAGE
          }
        ];
        let desFileUris: Array<string> =
          await phAccessHelper.showAssetsCreationDialog(srcFileUri, photoCreationConfigs);

        if (desFileUris.length > 0) {
          // 文件拷贝
          for (let index = 0; index < desFileUris.length; index++) {
            let srcFile = fs.openSync(srcFileUri[index], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            let destFile = fs.openSync(desFileUris[index], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            try {
              fs.copyFileSync(srcFile.fd, destFile.fd);
            } catch (error) {
              let err: BusinessError = error as BusinessError;
              console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
            } finally {
              fs.closeSync(srcFile);
              fs.closeSync(destFile);
            }
          }
          resolve(true);
        } else {
          resolve(false);
        }
      } catch (err) {
        reject(err);
      }
    });
  }

  build() {
    RelativeContainer() {
      Column() {
        Button('保存图片到相册')
          .onClick(() => {
            this.savePng();
          })

      }
      .height('100%')
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
    }
  }
}
```
