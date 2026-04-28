---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-upload-file
title: 上传指定文件至云侧
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 上传指定文件至云侧
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7cf09b978d2f4f9346fd80e74a55267bec3a7e95d70d8b355bde8c5c8cc79269
---

开发者可以快速将本地设备上的文件上传至云侧，上传完后，可以前往AppGallery Connect的“云存储”页面，查看上传的文档内容。

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 前提条件

已[初始化存储实例](cloudfoundation-storage-initialize-bucket.md)。

## 操作步骤

1. 选择待上传的文件，下方示例代码中使用[photoAccessHelper.PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)指定需要上传的文件。
2. 将待上传的文件复制到[context.cacheDir](../harmonyos-references/js-apis-inner-application-context.md#属性)目录下。

   说明

   由于StorageBucket.uploadFile接口传入参数localPath只能设置为context.cacheDir目录下的文件路径，所以上传前需要先将文件复制到context.cacheDir目录下。
3. 调用[StorageBucket.uploadFile](../harmonyos-references/cloudfoundation-cloudstorage.md#uploadfile)接口创建上传任务，监听上传任务的progress、completed、failed等事件。
4. 启动上传任务。

完整的示例代码如下：

```
1. import { cloudStorage } from '@kit.CloudFoundationKit';
2. import { BusinessError, request } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { photoAccessHelper } from '@kit.MediaLibraryKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { GlobalContext } from '../common/GlobalContext';

8. let storageBucket: cloudStorage.StorageBucket = cloudStorage.bucket();

10. @Component
11. export struct testPage {
12. build() {
13. }

15. // 上传指定文件至云侧
16. upload() {
17. this.selectPhoto().then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
18. let fileUri = photoSelectResult.photoUris[0];
19. hilog.info(0x0000, 'testTag', `pick file ${fileUri}`);
20. let fileName = fileUri.split('/').pop() as string;
21. hilog.info(0x0000, 'testTag', `file name ${fileName}`);
22. let cacheFile = GlobalContext.getContext().cacheDir + '/' + fileName;
23. hilog.info(0x0000, 'testTag', `cacheFile ${cacheFile}`);
24. // 将选中文件copy至cache目录下
25. this.copyFile(fileUri, cacheFile);
26. // 上传至云存储默认实例
27. this.uploadFile(cacheFile, `screenshot/${fileName}`);
28. }).catch((err: BusinessError) => {
29. hilog.error(0x0000, 'testTag', `Failed to upload file, code: ${err.code}, message: ${err.message}`);
30. })
31. }

33. /**
34. * @throws photoViewPicker select throws
35. */
36. selectPhoto(): Promise<photoAccessHelper.PhotoSelectResult> {
37. // 使用photoAccessHelper选择指定的文件
38. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
39. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // 过滤选择媒体文件类型为IMAGE
40. photoSelectOptions.maxSelectNumber = 1; // 选择媒体文件的最大数目
41. let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
42. return photoViewPicker.select(photoSelectOptions);
43. }

45. copyFile(srcPath: string, dstPath: string) {
46. try {
47. let srcFile = fileIo.openSync(srcPath);
48. let dstFile = fileIo.openSync(dstPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
49. fileIo.copyFileSync(srcFile.fd, dstFile.fd);
50. fileIo.closeSync(srcFile);
51. fileIo.closeSync(dstFile);
52. } catch (e) {
53. hilog.error(0x0000, 'testTag', `copy file failed ${e.message}`);
54. return;
55. }
56. }

58. uploadFile(localPath: string, cloudPath: string) {
59. storageBucket.uploadFile(GlobalContext.getContext(), {
60. localPath: localPath, // 本地文件路径（context.cacheDir目录下的文件路径）
61. cloudPath: cloudPath   // 云侧路径，支持传入“文件目录/文件名”（如“screenshot/demo.jpg”），或仅传入文件名。
62. }).then((task: request.agent.Task) => {
63. task.on('progress', (progress) => {
64. hilog.info(0x0000, 'testTag', `on progress ${JSON.stringify(progress)}`);
65. });
66. task.on('completed', (progress) => {
67. hilog.info(0x0000, 'testTag', `on completed ${JSON.stringify(progress)}`);
68. // 删除cache目录临时文件
69. fileIo.unlink(localPath).catch((err: BusinessError) => {
70. hilog.error(0x0000, 'testTag', `Failed to unlink, code: ${err.code}, message: ${err.message}.`);
71. });
72. });
73. task.on('failed', (progress) => {
74. hilog.info(0x0000, 'testTag', `on failed ${JSON.stringify(progress)}`);
75. // 删除cache目录临时文件
76. fileIo.unlink(localPath).catch((err: BusinessError) => {
77. hilog.error(0x0000, 'testTag', `Failed to unlink, code: ${err.code}, message: ${err.message}.`);
78. });
79. });
80. task.on('response', (response) => {
81. hilog.info(0x0000, 'testTag', `on response ${JSON.stringify(response)}`);
82. });

84. // start task
85. task.start((err: BusinessError) => {
86. if (err) {
87. hilog.error(0x0000, 'testTag',
88. `Failed to start a file upload task, code: ${err.code}, message: ${err.message}`);
89. } else {
90. hilog.info(0x0000, 'testTag', `Succeeded in starting a file upload task.`);
91. }
92. });
93. }).catch((err: BusinessError) => {
94. hilog.error(0x0000, 'testTag', `Failed to upload file, code: ${err.code}, message: ${err.message}`);
95. })
96. }
97. }
```

说明

上传完成，可以登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择项目，进入“云存储”界面查看文件列表。
