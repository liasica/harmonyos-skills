---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-getdownloadurl
title: 获取云侧文件下载地址
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 获取云侧文件下载地址
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2b6a52aa9a5d23e9965b7d379f40a5c71447db050828701b71c0fd66597fc772
---

文件上传至云侧后，开发者可以获取云侧文件的下载地址，将下载地址放到网站中提供文件下载的体验。

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
2. 调用[StorageBucket.getDownloadURL](../harmonyos-references/cloudfoundation-cloudstorage.md#getdownloadurl)接口获取云侧文件的下载地址。

   ```typescript
   let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
   bucket.getDownloadURL(UI.uploadFileName).then((downloadURL: string) => {
     hilog.info(0x0000, 'Storage', `Succeeded in getting dwonLoadURL: ${downloadURL}`);
   }).catch((err: BusinessError) => {
     hilog.info(0x0000, 'Storage', `Failed to get DownloadURL code: ${err.code}, message: ${err.message}`);
   });
   ```
