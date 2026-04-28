---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-getdownloadurl
title: 获取云侧文件下载地址
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 获取云侧文件下载地址
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5101684283c443d52c648c87c77419792a33b9fbd70d076107b97206c5a2658
---

文件上传至云侧后，开发者可以获取云侧文件的下载地址，将下载地址放到网站中提供文件下载的体验。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

* 已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。
* 已[上传指定文件至云侧](cloudfoundation-storage-upload-file.md)。

## 操作步骤

调用[StorageBucket.getDownloadURL](../harmonyos-references/cloudfoundation-cloudstorage.md#getdownloadurl)接口获取云侧文件的下载地址。

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

12. // 获取云侧文件下载地址
13. getUrl() {
14. // 获取云存储默认实例中screenshot/screenshot_20250115_155321.jpg文件的下载地址
15. storageBucket.getDownloadURL('screenshot/screenshot_20250115_155321.jpg').then((downloadURL: string) => {
16. hilog.info(0x0000, 'testTag', `Succeeded in getting download URL: ${downloadURL}`);
17. }).catch((err: BusinessError) => {
18. hilog.error(0x0000, 'testTag', `Failed to get download URL, code: ${err.code}, message: ${err.message}`);
19. })
20. }
21. }
```
