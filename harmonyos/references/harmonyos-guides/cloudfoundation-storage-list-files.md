---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-list-files
title: 获取云侧文件列表
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 获取云侧文件列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47d5971794007245114547f14aef69abcefcc4952dec5e7db2ac7da03ea06c2f
---

开发者可以获取指定云侧目录下所有的文件信息，包括文件存储目录、文件名称等。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

调用[StorageBucket.list](../harmonyos-references/cloudfoundation-cloudstorage.md#list)可以获取云侧指定目录的文件列表。

完整示例代码如下：

```
1. import { cloudStorage } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

7. @Component
8. export struct testPage {
9. build() {
10. }

12. // 获取文件列表
13. getList() {
14. // 获取云存储默认实例中根路径下的文件列表
15. storageBucket.list('').then((result: cloudStorage.ListResults) => {
16. hilog.info(0x0000, 'testTag', `Succeeded in listing files, result: ${JSON.stringify(result)}`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `Failed to list files, code: ${err.code}, message: ${err.message}`);
19. })
20. }
21. }
```

获取文件列表信息结构如下：

```
1. {
2. directories: ["empty-dir1\/", "screenshot\/"],
3. files: ["IMG_20240229_103118.jpg", "IMG_20240318_093732.jpg"]
4. }
```
