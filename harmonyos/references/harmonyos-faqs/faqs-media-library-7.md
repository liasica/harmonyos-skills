---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-7
title: 保存视频失败
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 保存视频失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c948b8988180641b09162d702e778a935d64c1b898f0b8c886507db97dee55d0
---

## 问题现象

在应用内保存视频，保存过程中提示保存失败且图库里没有刚才拍摄的视频。

## 背景知识

* [fs.accessSync](../harmonyos-references/js-apis-file-fs.md#fileioaccesssync)：文件管理模块（@ohos.file.fs ）提供的接口，以同步方法检查文件或目录是否存在，或校验操作权限。
* [13900002](../harmonyos-references/errorcode-filemanagement.md#section13900002-没有这个文件或目录)错误码：文件管理错误码，错误原因：没有这个文件或目录。

## 问题定位

1. 在日志中查找错误码“13900002”，匹配到相关错误信息：

   ```shell
   path (/xxx/xxx.mp4) to realpath error: No such file or directory
   Common:{ThrowError:72} {ParseFileUri:<private>} ThrowError errCode:13900002 errMsg:no such file
   ```

   可以确认错误原因为“/xxx/xxx.mp4”这个文件不存在。
2. 查看保存视频相关代码，应用在保存视频前调用了fs.accessSync()方法校验临时视频文件是否存在。但是无论校验结果如何，应用都会调用photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest()方法保存视频。

   例如：

   ```shell
   // 虽然判断了视频文件是否存在，但是没有对不存在的情况做任何处理
   const isExist = fs.accessSync(this.videoPath);
   const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
   // 当视频文件不存在时，执行此处代码就会报错：“No such file or directory”
   const assetChangeRequest = photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(this.context, this.videoPath);
   await phAccessHelper.applyChanges(assetChangeRequest);
   ```

## 分析结论

1. 保存视频时路径不正确。
2. 视频路径不存在时没有相关异常处理逻辑。

## 修改建议

1. 排查视频文件路径的正确性，确保保存时传参的路径正确。
2. 当fs.accessSync()方法返回false（即文件不存在）时，应该执行对应的异常处理逻辑，而不是继续保存视频。参考代码：

   ```ts
   import fs from '@ohos.file.fs';
   import photoAccessHelper from '@ohos.file.photoAccessHelper';
   import { BusinessError } from '@ohos.base';
   import { PromptAction, UIContext } from '@kit.ArkUI';

   @Entry
   @Component
   struct VideoSavePage {
     private context: Context | undefined = this.getUIContext().getHostContext();
     private videoPath: string = `${this.context!.filesDir}/output.mp4`;
     uiContext: UIContext = this.getUIContext();
     promptAction: PromptAction = this.uiContext.getPromptAction();

     async saveVideo() {
       // 判断文件是否存在
       let isExist: boolean;
       try {
         isExist = fs.accessSync(this.videoPath); // 不存在会返回 false
       } catch (e) {
         isExist = false;
       }

       if (isExist) {
         try {
           const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(this.context);
           // 构造保存请求（视频）
           const assetChangeRequest =
             photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(this.context, this.videoPath);
           // 提交到相册
           await phAccessHelper.applyChanges(assetChangeRequest);

           this.promptAction.showToast({ message: '已保存到相册' });
         } catch (err) {
           const error = err as BusinessError;
           console.error(`保存失败：${error.code} ${error.message}`);
           this.promptAction.showToast({ message: '保存失败，请检查权限' });
         }
       } else {
         this.promptAction.showToast({ message: '视频文件不存在' });
       }
     }

     build() {
       Column({ space: 40 }) {
         Button('保存视频到相册')
           .onClick(() => this.saveVideo());
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```
