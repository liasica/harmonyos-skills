---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-initialize-bucket
title: 初始化存储实例
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 初始化存储实例
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:1c8ac6829d47f52921bf815c47769ccfabdbbcadd899572ee02afffe5c286bb2
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[开通云存储服务](cloudfoundation-enable-storage.md)。

## 操作步骤

调用[cloudStorage.bucket](../harmonyos-references/cloudfoundation-cloudstorage.md#bucket)初始化一个存储实例。

1. 导入相关模块。

   ```typescript
   import { cloudStorage } from '@kit.CloudFoundationKit';
   ```
2. 使用以下任意一种方式初始化实例。

   * 使用默认实例

     ```typescript
     let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();
     ```
   * 使用指定的实例

     ```typescript
     let bucket: cloudStorage.StorageBucket = cloudStorage.bucket('bucket001-2wezr'); // 指定bucket001-2wezr实例
     ```

   **注意** 

   以“使用指定的实例”方式初始化云存储实例，请确保当前云侧存在该存储实例，否则后续操作将出现找不到存储实例的错误。在云侧创建新的存储实例，可参考[存储实例管理](../AppGallery-connect-Guides/agc-storage-manage-bucket-0000001281294006.md)。
