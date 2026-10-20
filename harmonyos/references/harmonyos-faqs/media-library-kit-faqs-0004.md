---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/media-library-kit-faqs-0004
title: 图库图片选择与上传常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 常见问题 > 图库图片选择与上传常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:45+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:02f6b9e457b7d4c194953ef76fdb556b097498298f6366d60305a7d8090980ae
---

**Q：使用PhotoPicker拉起图库选择器，应该如何去除拍照选项只保留视频和图片的选择，如下图所示。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/RJHbwVAlTyCDSOQBliByFA/zh-cn_image_0000002768292924.png "点击放大")

**A**：开发者可以通过以下步骤实现去除拍照选项的效果：

1. 使用[PhotoSelectOptions](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#photoselectoptions)对象：在调用select方法时，使用PhotoSelectOptions对象来配置选择选项。该对象允许你指定媒体文件类型和其他相关参数。
2. 设置isPhotoTakingSupported参数：在PhotoSelectOptions对象中，设置isPhotoTakingSupported参数为false。当使用PhotoPicker时，拍照功能将不会被启用。
3. 调用select方法：使用配置好的PhotoSelectOptions对象调用select方法。该方法会拉起PhotoPicker界面，由于拍照功能被禁用，只能选择图片或视频，而无法进行拍照。

更多图库选项设置可参考[BaseSelectOptions](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#baseselectoptions)。

**Q：如何从图库选择图片并上传到服务器？**

**A**：上传图片到服务器需要申请网络权限：ohos.permission.INTERNET。

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
