---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-download-file
title: 下载云侧文件至本地
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 下载云侧文件至本地
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:92ea5bf99d4c66464ad237d88319268c55f2453385c3b59b67da77566d15c50b
---

文件上传至云侧后，开发者可以将云侧文件下载到本地设备中。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

1. 导入相关模块。

   ```typescript
   import { cloudStorage } from '@kit.CloudFoundationKit';
   // ...
   import { request } from '@kit.BasicServicesKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { GlobalContext } from '../common/GlobalContext';
   ```
2. 下载文件。

   1. 调用[StorageBucket.downloadFile](../harmonyos-references/cloudfoundation-cloudstorage.md#downloadfile)接口创建下载任务，监听下载任务的progress、completed、failed等事件。
   2. 启动下载任务。

      **说明** 

      下载成功后，文件将保存在[context.cacheDir](../harmonyos-references/js-apis-inner-application-context.md#属性)目录下。

   完整示例代码如下：

   ```typescript
   cloudStorage.bucket().downloadFile(GlobalContext.getContext(), {
     localPath: `./${Date.now()}_` + UI.uploadFileName,
     cloudPath: UI.uploadFileName
   })
     .then((task: request.agent.Task) => {
       task.on('progress', (progress) => {
         hilog.info(0x0000, 'Storage', `on progress ${JSON.stringify(progress)} `);
       });
       task.on('completed', (progress) => {
         hilog.info(0x0000, 'Storage', `on completed ${JSON.stringify(progress)} `);
         UI.listDir(GlobalContext.getContext().cacheDir);
       });
       task.on('failed', (progress) => {
         hilog.info(0x0000, 'Storage', `on failed ${JSON.stringify(progress)} `);
       });
       task.start((err: BusinessError) => {
         if (err) {
           hilog.error(0x0000, 'Storage',
             `Failed to start the downloadFileWithTask task, code: ${err.code}, message: ${err.message}`);
         } else {
           hilog.info(0x0000, 'Storage', `Succeeded in starting a downloadFileWithTask task. result: ${task.tid}`);
         }
       });
     }).catch((error: BusinessError) => {
     hilog.error(0x0000, 'Storage', `Failed to downloadFile code: ${error.code}, message: ${error.message}`);
   });
   ```

   **说明** 

   如果本地已存在同名文件，下载文件将出现异常，可以通过设置[DownloadParams.overwrite](../harmonyos-references/cloudfoundation-cloudstorage.md#downloadparams)来决定是否覆盖本地文件。
