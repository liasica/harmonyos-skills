---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokecloudstorage
title: 在端侧调用云存储
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:08+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:07a3e6ca1d7deeff268b14bbc3a3017d5bbdbb1118ed614e6e03de03cf812cca
---

## 前提条件

* 请确保云存储服务已经开通。
* 使用云存储功能，需要获取用户凭据。请确保您已[配置AccessToken](../harmonyos-references/cloudfoundation-cloudcommon.md#getaccesstoken)。

## 操作步骤

1. 在代码文件中引入Cloud Foundation Kit。

   ```
   1. import { cloudStorage } from '@kit.CloudFoundationKit';
   2. import { BusinessError, request } from '@kit.BasicServicesKit';
   ```
2. 初始化云存储实例。

   ```
   1. const bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
   ```
3. 调用云存储接口，如uploadFile接口。“src/main/ets/pages/CloudStorage.ets”代码片段节选如下，更完整的接口信息请参考[Cloud Foundation Kit API参考-云存储模块](../harmonyos-references/cloudfoundation-cloudstorage.md)。

   ```
   1. bucket.uploadFile(getContext(this), {
   2. localPath: cacheFilePath,
   3. cloudPath: cloudPath,
   4. }).then(task => {
   5. // add task event listener
   6. this.addEventListener(task, this.onUploadCompleted(cloudPath, cacheFilePath));
   7. // start task
   8. task.start();
   9. }).catch((err: BusinessError) => {
   10. hilog.error(HILOG_DOMAIN, TAG, 'uploadFile failed, error code: %{public}d, message: %{public}s',
   11. err.code, err.message);
   12. this.isUploading = false;
   13. });
   ```
