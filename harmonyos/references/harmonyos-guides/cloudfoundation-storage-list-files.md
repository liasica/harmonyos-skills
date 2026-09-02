---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-list-files
title: 获取云侧文件列表
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 获取云侧文件列表
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:02de402b3e1971e3223e35a053b27cbbe33d13c633524eac8c2f2f9bc2239a36
---

开发者可以获取指定云侧目录下所有的文件信息，包括文件存储目录、文件名称等。

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
2. 调用[StorageBucket.list](../harmonyos-references/cloudfoundation-cloudstorage.md#list)获取云侧指定目录的文件列表。

   ```typescript
   bucket.list('', {
     maxResults: 1,
   }).then((result: Object) => {
     hilog.info(0x0000, 'Storage', `Succeeded in listing file  ${JSON.stringify(result)}`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'Storage', `Failed to list file  code: ${err.code}, message: ${err.message}`);
   });
   ```

   获取文件列表信息结构如下：

   ```typescript
   {
     directories: ["empty-dir1\/", "screenshot\/"],
     files: ["IMG_20240229_103118.jpg", "IMG_20240318_093732.jpg"]
   }
   ```
