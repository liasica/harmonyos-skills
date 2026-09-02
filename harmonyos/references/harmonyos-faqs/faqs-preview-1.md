---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-preview-1
title: Preview Kit预览文件失败
breadcrumb: FAQ > 应用服务开发 > 通用文件预览服务（Preview Kit） > Preview Kit预览文件失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:b1e3803b05fafd7be8af9c9e937a0c34b1f70b9c9d0144163cc0764bb796e5a2
---

## 问题现象

使用Preview Kit预览视频MP4格式文件，一直显示“正在加载”，无法打开。

## 背景知识

[Preview Kit](../harmonyos-guides/preview-introduction.md)：为应用提供便捷的文件快速预览和文件打开加速能力，打开加速提供了预加载机制提前加载文件，缩短用户打开文件时间，给用户提供流畅顺滑的预览体验。Preview Kit能够对图片、视频、音频、文本、html进行预览查看，满足绝大多数办公开发的需求，具体可以参考[文件预览支持的文件类型](../harmonyos-guides/preview-introduction.md#文件预览支持的文件类型)。

## 问题定位

1. 排查文件的uri，Preview Kit的openPreview在传入预览信息时，仅支持uri格式，不支持传入文件的沙箱路径。

   ```txt
   07-09 11:00:20.810 24281 24281 I C04500/com.xxx.xxx/chromium: [nodict][nweb_download_handler_delegate.cc:106] web_download_item params, nweb_id:3,id:6,guid:62b1d5fc-4bfe-4685-90f6-15fc74a468a2,suggested:xxxx.mp4,current_speed:0,percent_complete:82,total_bytes:282842028,received_bytes:232516236,full_path:/data/storage/el2/base/cache/web/xxxx (3).mp4,state:0,received_slices:(0,78388928,0)(94280676,87829180,0)(188561352,66298128,0),last_modified:Wed, 11 Sep 2024 00:47:09 GMT,etag:"66e0e88d-10dbd3ac"
   07-09 11:00:20.810 24281 24281 I C04500/com.xxx.xxx/chromium: [nodict][nweb_download_item.h:69] ~NWebDownloadItem() is called
   07-09 11:00:20.811 24281 24281 I A03D00/com.xxx.xxx/JSAPP: download update guid: 62b1d5fc-4bfe-4685-90f6-15fc74a468a2
   07-09 11:00:20.811 24281 24281 I A03D00/com.xxx.xxx/JSAPP: download update guid: 82
   07-09 11:00:20.811 24281 24281 I A03D00/com.xxx.xxx/JSAPP: download update speed: 0
   07-09 11:00:20.838   862 32771 W C01719/resource_schedule_service/ffrt: 5365472:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:20.839   862 32766 W C01719/resource_schedule_service/ffrt: 5365474:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:20.919   862 32731 W C01719/resource_schedule_service/ffrt: 5365479:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:20.919   862 32724 W C01719/resource_schedule_service/ffrt: 5365482:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:20.919   862 32731 I C057C6/resource_schedule_service/BinderInvoker: ~BinderInvoker 97: destroyed invoker 3359663360
   07-09 11:00:20.920   862 32724 I C057C6/resource_schedule_service/BinderInvoker: ~BinderInvoker 97: destroyed invoker 3359681280
   07-09 11:00:20.974   634 31973 I C02D15/hiview/XPower: [task_198]#ffrt [WifiHandler] [126] timeout [9881]. queue size:1
   07-09 11:00:20.974   634 31835 W C02DA0/hiview/NativeLeakSample: HandleAllPssCollection: isFirstCollect is false, no HandleAllPssCollection
   07-09 11:00:20.988   862 32725 W C01719/resource_schedule_service/ffrt: 5365486:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:20.988   862 32725 I C057C6/resource_schedule_service/BinderInvoker: ~BinderInvoker 97: destroyed invoker 1174865792
   07-09 11:00:21.027   862 32726 W C01719/resource_schedule_service/ffrt: 5365490:~WorkerThread:65 WorkerThread enter destruction
   07-09 11:00:21.027   862 32726 I C057C6/resource_schedule_service/BinderInvoker: ~BinderInvoker 97: destroyed invoker 3359674880
   07-09 11:00:21.029  1396  2481 W C01120/foundation/BMS: uid 20020179 is not existed
   07-09 11:00:21.030   634 32807 E P02D15/hiview/XPower: [task_46]#Failed to get packages: 8521233 for uid: 20020179
   07-09 11:00:21.031   634 32807 E P02D15/hiview/XPower: [task_46]#Failed to get packages by uid=20020179, pid=0, ret: -6
   07-09 11:00:21.031   634 32807 E C02D15/hiview/XPower: [task_46]#Failed to find package for uid:20020179
   07-09 11:00:21.034  1396  2481 W C01120/foundation/BMS: uid 20020291 is not existed
   ```
2. 根据日志定位，发现拉起方传递的mimeType是Word的mimeType，所以预览把它当做Word文档打开，导致加载异常。

   ```txt
   07-09 11:01:00.040 32157 32157 E A0FF01/com.huawei.hmos.hipreview/[HiPreview]: MenuAbilityUtil: the mimeType of the file named <private> fails to be verified.
   07-09 11:01:00.040 32157 32157 E A0FF01/com.huawei.hmos.hipreview/[HiPreview]:      the expected mimeType is ["video/mp4"], but the actual mimeType is application/msword.
   07-09 11:01:00.040 32157 32157 E C02D08/com.huawei.hmos.hipreview/NAPI_HISYSEVENT_ADAPTER: js function line number parsed failed.
   07-09 11:01:00.041  3208  3208 W C0391F/com.ohos.sceneboard/AceImage: [(100000:100000:scope)] Image LoadFail, source = <private>, reason: empty sourceFailed to create image loader, Image source type not supported
   07-09 11:01:00.041  3208  3208 W C0391F/com.ohos.sceneboard/AceImage: [(100000:100000:scope)] Image LoadFail, source = <private>, reason: empty sourceFailed to create image loader, Image source type not supported
   ```

## 分析结论

由于预览把视频MP4文件当做Word文档打开，导致预览文件加载出现异常。

## 修改建议

1. 可以不传mimeType，此时Preview Kit会根据后缀判断是什么类型的文件，进行打开。
2. 或者传入正确的视频文件的mimeType类型，再预览文件。

   ```ts
   import { filePreview } from '@kit.PreviewKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileUri } from '@kit.CoreFileKit';
   import fs from '@ohos.file.fs';

   @Entry
   @Component
   struct PreviewKit {
     context: Context = this.getUIContext().getHostContext() as Context;

     build() {
       Column() {
         Button('预览文件')
           .onClick(() => {
             // 先将待预览的文件写入沙箱中
             let uiContext = this.getUIContext().getHostContext() as Context;
             let resMgr = uiContext.resourceManager;
             // 请将需要预览的文件放在工程目录的/resources/base/media/下，此处以video.mp4为例，请按需修改文件名
             const resource = resMgr.getMediaContentSync($r('app.media.video').id);
             // 应用沙箱中的文件，此处以video.mp4为例，请按需修改文件名
             const targetPath = uiContext.filesDir + '/' + 'video.mp4';
             // 创建写入流
             const file = fs.openSync(targetPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
             let stream = fs.fdopenStreamSync(file.fd, 'r+');
             // 写入文件
             try {
               stream.writeSync(resource.buffer);
             } finally {
               stream.closeSync();
             }
             // 将沙箱文件路径转成uri形式，防止预览失败
             let uri = fileUri.getUriFromPath(targetPath);
             console.log('Preview-kit ' + uiContext.filesDir);
             // 传入支持的文件类型且文件存在时会返回true
             filePreview.canPreview(uiContext, uri).then((result) => {
               console.info(`Preview-kit Succeeded in obtaining the result of whether it can be previewed. result = ${result}`);
             }).catch((err: BusinessError) => {
               console.error(`Preview-kit Failed to obtain the result of whether it can be previewed, err.code = ${err.code}, err.message = ${err.message}`);
             });

             let displayInfo: filePreview.DisplayInfo = {
               x: 100,
               y: 100,
               width: 800,
               height: 800
             };
             let fileInfo: filePreview.PreviewInfo = {
               title: 'video.mp4',
               uri: uri,
               mimeType: 'video/mp4'
             };
             // 打开文件预览
             filePreview.openPreview(uiContext, fileInfo, displayInfo)
               .then(() => {
                 console.info('Preview-kit Succeeded in opening preview');
               }).catch((err: BusinessError) => {
               console.error(`Preview-kit Failed to open preview, err.code = ${err.code}, err.message = ${err.message}`);
             });
           })
           .margin(10)
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
