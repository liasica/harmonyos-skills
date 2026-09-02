---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-22
title: 如何从图库选择图片并上传到服务器
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何从图库选择图片并上传到服务器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e19675af1cbc6f4d7081761aafe88e73e2f1cdbb826b2e81b468e888644060d3
---

上传图片到服务器需要申请网络权限：ohos.permission.INTERNET。

从图库选择图片并上传到服务器，可参考以下示例代码。

```ts
import { request } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private openPhotoPicker() {
    // Obtain the application file path 
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let cacheDir = context.cacheDir;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select({
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
      maxSelectNumber: 1
    }, (_, result) => {
      if (result) {
        result.photoUris.forEach((uri) => {
          let file = fileIo.openSync(uri, fileIo.OpenMode.CREATE);
          // Copy the file to the cache directory
          fileIo.copyFileSync(file.fd, cacheDir + '/test.jpeg');
          this.uploadImage(['internal://cache/test.jpeg']);
        })
      }
    })
  }

  private uploadImage(paths: string[]) {
    let allFiles = Array<request.File>();
    let header = new Map<Object, string>();
    header.set('Content-Type', 'multipart/form-data');
    header.set('key2', 'value2');
    for (let i = 0; i < paths.length; i++) {
      allFiles[i] = {
        name: 'image' + i + '.jpeg',
        filename: 'image' + i + '.jpeg',
        uri: paths[i],
        type: 'image'
      }
    }
    let data: Array<request.RequestData> = [{ name: 'name', value: 'value' }];
    let uploadConfig: request.UploadConfig = {
      url: 'http://XXX&#34',
      header: header,
      method: 'POST',
      files: allFiles,
      data: data
    }
    try {
      request.uploadFile(this.getUIContext().getHostContext(), uploadConfig, (error, uploadTask) => {
        if (uploadTask) {
          uploadTask.on('progress', (uploadSize: number, totalSize: number) => {
            console.info('progress,uploadedSize:' + uploadSize + ',totalSize:' + totalSize);
          })
        } else {
          console.info('upload failure:' + error);
        }
      })
    } catch (error) {
      console.info('upload failure:' + error);
    }
  }

  build() {
    Column() {
      Button('选择图片上传')
        .width('100%')
        .onClick(() => {
          this.openPhotoPicker();
        })
    }
    .width('100%')
    .height('100%')
    .padding(16)
    .justifyContent(FlexAlign.End)
  }
}
```
