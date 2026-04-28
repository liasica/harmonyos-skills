---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-setmetadata
title: 设置云侧文件的元数据
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 设置云侧文件的元数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:829a7f87e72bb56117b74e6dbef93d878d45e401cb0bf519e5c91f71f510222c
---

文件元数据包含云侧文件名、文件大小、文件类型等常用属性，也包括用户自定义的文件属性。

文件保存至云侧后，开发者可以设置文件的自定义属性。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

调用[StorageBucket.setMetadata](../harmonyos-references/cloudfoundation-cloudstorage.md#setmetadata)可以设置云侧文档的元数据信息。

```
1. import { cloudStorage } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

7. @Component
8. export struct testPage {
9. build() {
10. }

12. // 设置元数据
13. setMetaData() {
14. // 设置云存储默认实例中screenshot/screenshot_20250115_155321.jpg文件的元数据信息
15. storageBucket.setMetadata('screenshot/screenshot_20250115_155321.jpg', {
16. customMetadata: {
17. key1: "value1",
18. key2: "value2"
19. }
20. }).then((metadata: cloudStorage.Metadata) => {
21. hilog.info(0x0000, 'testTag', `Succeeded in setting metadata: ${JSON.stringify(metadata)}`);
22. }).catch((err: BusinessError) => {
23. hilog.error(0x0000, 'testTag', `Failed to set metadata, code: ${err.code}, message: ${err.message}`);
24. })
25. }
26. }
```
