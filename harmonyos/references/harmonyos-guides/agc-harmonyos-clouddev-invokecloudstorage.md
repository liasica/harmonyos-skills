---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudstorage
title: 在端侧调用云存储
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发端侧工程 > 在端侧调用云侧代码 > 在端侧调用云存储
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:49+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:322cdf6dd5105937c07717b5f2e9c8376983a615bc99a8f539fa7f01c2d373c4
---

## 前提条件

* 请确保云存储服务已经开通。
* 使用云存储功能，需要获取用户凭据。请确保您已[配置AccessToken](../harmonyos-references/cloudfoundation-cloudcommon.md#getaccesstoken)。

## 操作步骤

1. 在代码文件中引入Cloud Foundation Kit。

   ```screen
   import { cloudStorage } from '@kit.CloudFoundationKit';
   import { BusinessError, request } from '@kit.BasicServicesKit';
   ```
2. 初始化云存储实例。

   ```screen
   const bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
   ```
3. 调用云存储接口，如uploadFile接口。“src/main/ets/pages/CloudStorage.ets”代码片段节选如下，更完整的接口信息请参考[Cloud Foundation Kit API参考-云存储模块](../harmonyos-references/cloudfoundation-cloudstorage.md)。

   ```typescript
   bucket.uploadFile(getContext(this), {
     localPath: cacheFilePath,
     cloudPath: cloudPath,
   }).then(task => {
     // add task event listener
     this.addEventListener(task, this.onUploadCompleted(cloudPath, cacheFilePath));
     // start task
     task.start();
   }).catch((err: BusinessError) => {
     hilog.error(HILOG_DOMAIN, TAG, 'uploadFile failed, error code: %{public}d, message: %{public}s',
       err.code, err.message);
     this.isUploading = false;
   });
   ```
