---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-getmetadata
title: 获取云侧文件的元数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 获取云侧文件的元数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b15a953518df9c0b71d4643a1d6948f6a9c945b676328c69ae81e8367f09ba5
---

文件元数据包含云侧文件名、文件大小、文件类型等常用属性，也包括用户自定义的文件属性。

文件上传至云侧后，开发者可以在下载文件前获取指定云侧文件的元数据，来决定是否下载此文件。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

调用[StorageBucket.getMetadata](../harmonyos-references/cloudfoundation-cloudstorage.md#getmetadata)获取指定云侧文件的元数据信息。

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

12. // 获取元数据
13. getMetaData() {
14. // 获取云存储默认实例中screenshot/screenshot_20250115_155321.jpg文件的元数据信息
15. storageBucket.getMetadata('screenshot/screenshot_20250115_155321.jpg').then((metadata: cloudStorage.Metadata) => {
16. hilog.info(0x0000, 'testTag', `Succeeded in getting metadata: ${JSON.stringify(metadata)}`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `Failed to get metadata, code: ${err.code}, message: ${err.message}`);
19. })
20. }
21. }
```
