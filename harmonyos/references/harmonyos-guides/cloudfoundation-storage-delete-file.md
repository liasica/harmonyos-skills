---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-delete-file
title: 删除云侧文件
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 删除云侧文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f65bc9323a16cfa518b317ed41ed3109f45d39aaef429ac7118c7ecd0d4a3ff8
---

当云侧文件不需要时，开发者可以在应用客户端删除云侧的文件。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

调用[StorageBucket.deleteFile](../harmonyos-references/cloudfoundation-cloudstorage.md#deletefile)删除云侧的文件。

注意

删除操作不可逆，一旦执行，文件会被物理删除，不可找回。

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

12. // 删除云侧文件
13. deleteFile() {
14. // 删除云存储默认实例中screenshot/screenshot_20250115_155321.jpg文件
15. storageBucket.deleteFile('screenshot/screenshot_20250115_155321.jpg').then(() => {
16. hilog.info(0x0000, 'testTag', `Succeeded in deleting file.`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `Failed to delete file, code: ${err.code}, message: ${err.message}`);
19. })
20. }
21. }
```

说明

删除文件后，可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择项目，进入“云存储”界面查看文件列表。
