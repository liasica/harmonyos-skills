---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-initialize-bucket
title: 初始化存储实例
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 初始化存储实例
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9eed69c67609a48ea7a9d11561fea3bc2ef1bc7ad8c439ecc89c40a71abe046
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[开通云存储服务](cloudfoundation-enable-storage.md)。

## 操作步骤

调用[cloudStorage.bucket](../harmonyos-references/cloudfoundation-cloudstorage.md#bucket)初始化一个存储实例。支持使用两种方式初始化实例：

* 使用默认实例

  ```
  1. import { cloudStorage } from '@kit.CloudFoundationKit';

  3. let bucket: cloudStorage.StorageBucket = cloudStorage.bucket(); // 将启动异步任务查询云侧默认实例
  ```
* 使用指定的实例

  ```
  1. import { cloudStorage } from '@kit.CloudFoundationKit';

  3. let bucket: cloudStorage.StorageBucket = cloudStorage.bucket('bucket001-2wezr'); // 指定bucket001-2wezr实例
  ```

  注意

  以“使用指定的实例”方式初始化云存储实例，请确保当前云侧存在该存储实例，否则后续操作将出现找不到存储实例的错误。在云侧创建新的存储实例，可参考[存储实例管理](../AppGallery-connect-Guides/agc-storage-manage-bucket-0000001281294006.md)。
