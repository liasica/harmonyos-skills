---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-25
title: 短时间内保存多个资源如何避免重复弹窗
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 短时间内保存多个资源如何避免重复弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:45921d3064f822ee1cec742721aa8731c687281fa7099d0ac4d788df07ec2e5c
---

## 问题现象

某些场景下因为客观因素无法使用安全控件，使用系统弹窗保存方案会频繁弹窗授权影响用户体验。需要一种在一次性授权后，一段时间内将多张图片保存至相册，无需每次弹窗确认的方案，实现短时间内的无感保存能力。

## 背景知识

1. [ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionshort_term_write_imagevideo)为受限开放权限，允许应用保存图片、视频到用户公共目录。应用获取此权限后，最长可获得30分钟的短时授权，来保存图片/视频。申请权限参考：[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md#section156171230179)。
2. 应用首次调用[createAssetWithShortTermPermission](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#createassetwithshorttermpermission12)方法后拉起保存确认弹框。在用户"同意"后的5分钟之内，同一个应用再次调用接口，支持无需弹框确认自动返回已授权的uri给应用，支持应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹框进行确认授权。

## 解决方案

申请SHORT\_TERM\_WRITE\_IMAGEVIDEO权限后，将图片保存至沙箱路径，使用createAssetWithShortTermPermission接口拉起保存确认弹框，在用户同意保存后返回已创建并授予保存权限的uri，将此uri保存至相册。

1. 申请SHORT\_TERM\_WRITE\_IMAGEVIDEO权限，并在module.json5配置文件的requestPermissions标签中配置相关权限，具体可参考[声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。
2. 将图片资源保存至沙箱路径，代码示例如下：

   ```ts
   getPath() {
     let contexts = this.getUIContext().getHostContext() as common.UIAbilityContext;
     // test.jpg仅供参考使用，实际场景请使用真实的rawfile文件名。
     let array = contexts.resourceManager.getRawFileContentSync('test.jpg');
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let filesDir = context.cacheDir;
     let filePath = filesDir + '/test.png';
     let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     fileIo.writeSync(file.fd, array.buffer);
     fileIo.closeSync(file);
     return filePath;
   }
   ```
3. 使用createAssetWithShortTermPermission接口提供给应用拉起保存确认弹框，在用户同意保存后返回已创建并授予保存权限的uri，并将此uri保存至相册，代码示例如下：

   ```ts
   async shortTermSaveImage(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
     console.info('createAssetWithShortTermPermissionDemo.');
     let filePath = this.getPath();
     try {
       let photoCreationConfig: photoAccessHelper.PhotoCreationConfig = {
         fileNameExtension: 'jpg',
         photoType: photoAccessHelper.PhotoType.IMAGE,
         subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
       };

       let resultUri: string = await phAccessHelper.createAssetWithShortTermPermission(photoCreationConfig);
       let resultFile: fileIo.File = fileIo.openSync(resultUri, fileIo.OpenMode.READ_WRITE);
       // 使用getUriFromPath方法把传入的路径path生成应用自己的uri
       let dirUri = fileUri.getUriFromPath(filePath);
       let srcFile: fileIo.File = fileIo.openSync(dirUri, fileIo.OpenMode.READ_ONLY);
       let bufSize: number = 2000000;
       let readSize: number = 0;
       let buf = new ArrayBuffer(bufSize);
       let readLen = fileIo.readSync(srcFile.fd, buf, {
         offset: readSize,
         length: bufSize
       });
       if (readLen > 0) {
         readSize += readLen;
         fileIo.writeSync(resultFile.fd, buf, { length: readLen });
       }
       fileIo.closeSync(srcFile);
       fileIo.closeSync(resultFile);
       this.promptAction.openToast({
         message: '已保存至相册',
         duration: 3000,
       });
     } catch (err) {
       console.error(`createAssetWithShortTermPermission failed, errCode is ${err.code} errMsg is ${err.message}`);
       this.promptAction.openToast({
         message: '保存失败',
         duration: 3000,
       });
     }
   }
   ```

完整示例代码如下：

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  // 将图片资源保存到沙箱路径，此处示例为保存本地资源
  getPath() {
    let contexts = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // test.jpg仅供参考使用，实际场景请使用真实的rawfile文件名。
    let array = contexts.resourceManager.getRawFileContentSync('test.jpg');
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filesDir = context.cacheDir;
    let filePath = filesDir + '/test.png';
    let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    fileIo.writeSync(file.fd, array.buffer);
    fileIo.closeSync(file);
    return filePath;
  }

  async shortTermSaveImage(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
    console.info('createAssetWithShortTermPermissionDemo.');
    let filePath = this.getPath();
    try {
      let photoCreationConfig: photoAccessHelper.PhotoCreationConfig = {
        fileNameExtension: 'jpg',
        photoType: photoAccessHelper.PhotoType.IMAGE,
        subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
      };

      let resultUri: string = await phAccessHelper.createAssetWithShortTermPermission(photoCreationConfig);
      let resultFile: fileIo.File = fileIo.openSync(resultUri, fileIo.OpenMode.READ_WRITE);
      // 使用getUriFromPath方法把传入的路径path生成应用自己的uri
      let dirUri = fileUri.getUriFromPath(filePath);
      let srcFile: fileIo.File = fileIo.openSync(dirUri, fileIo.OpenMode.READ_ONLY);
      let bufSize: number = 2000000;
      let readSize: number = 0;
      let buf = new ArrayBuffer(bufSize);
      let readLen = fileIo.readSync(srcFile.fd, buf, {
        offset: readSize,
        length: bufSize
      });
      if (readLen > 0) {
        readSize += readLen;
        fileIo.writeSync(resultFile.fd, buf, { length: readLen });
      }
      fileIo.closeSync(srcFile);
      fileIo.closeSync(resultFile);
      this.promptAction.openToast({
        message: '已保存至相册',
        duration: 3000,
      });
    } catch (err) {
      console.error(`createAssetWithShortTermPermission failed, errCode is ${err.code} errMsg is ${err.message}`);
      this.promptAction.openToast({
        message: '保存失败',
        duration: 3000,
      });
    }
  }

  build() {
    Column({ space: 10 }) {
      // test.jpg仅供参考使用，开发者可替换为实际使用图片
      Image($rawfile('test.jpg')).width(150);
      Button('短时权限保存照片').onClick(() => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        this.shortTermSaveImage(phAccessHelper);
      });

    }
    .height('100%')
    .width('100%');
  }
}
```
