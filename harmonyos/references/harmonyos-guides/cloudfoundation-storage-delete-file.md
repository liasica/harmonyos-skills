---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-delete-file
title: 删除云侧文件
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 删除云侧文件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:27361a218002d646c8c76c8d6c295752b0d9a90a64c34ea1021dafc65a6889c7
---

当云侧文件不需要时，开发者可以在应用客户端删除云侧的文件。

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
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[StorageBucket.deleteFile](../harmonyos-references/cloudfoundation-cloudstorage.md#deletefile)删除云侧的文件。

   **注意** 

   删除操作不可逆，一旦执行，文件会被物理删除，不可找回。

   ```typescript
   let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
   bucket.deleteFile(UI.uploadFileName).then(() => {
     hilog.info(0x0000, 'Storage', `Succeeded in deleting File`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'Storage', `Failed to delete file  code: ${err.code}, message: ${err.message}`);
   });
   ```

   **说明** 

   删除文件后，可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择项目，进入“云存储”界面查看文件列表。
