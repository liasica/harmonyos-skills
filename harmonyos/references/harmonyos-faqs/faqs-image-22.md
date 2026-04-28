---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-22
title: 如何从图库选择图片并上传到服务器
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何从图库选择图片并上传到服务器
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:29+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:ece7ea78ada6ce9b5ad419660b0b172b21ce745f0e38d74face44f84cb34f83a
---

上传图片到服务器需要申请网络权限：ohos.permission.INTERNET。

从图库选择图片并上传到服务器，可参考以下示例代码。

```
1. import { request } from '@kit.BasicServicesKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';
4. import { common } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. private openPhotoPicker() {
10. // Obtain the application file path
11. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
12. let cacheDir = context.cacheDir;
13. let photoPicker = new photoAccessHelper.PhotoViewPicker();
14. photoPicker.select({
15. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
16. maxSelectNumber: 1
17. }, (_, result) => {
18. if (result) {
19. result.photoUris.forEach((uri) => {
20. let file = fileIo.openSync(uri, fileIo.OpenMode.CREATE);
21. // Copy the file to the cache directory
22. fileIo.copyFileSync(file.fd, cacheDir + '/test.jpeg');
23. this.uploadImage(['internal://cache/test.jpeg']);
24. })
25. }
26. })
27. }

29. private uploadImage(paths: string[]) {
30. let allFiles = Array<request.File>();
31. let header = new Map<Object, string>();
32. header.set('Content-Type', 'multipart/form-data');
33. header.set('key2', 'value2');
34. for (let i = 0; i < paths.length; i++) {
35. allFiles[i] = {
36. name: 'image' + i + '.jpeg',
37. filename: 'image' + i + '.jpeg',
38. uri: paths[i],
39. type: 'image'
40. }
41. }
42. let data: Array<request.RequestData> = [{ name: 'name', value: 'value' }];
43. let uploadConfig: request.UploadConfig = {
44. url: 'http://XXX&#34',
45. header: header,
46. method: 'POST',
47. files: allFiles,
48. data: data
49. }
50. try {
51. request.uploadFile(this.getUIContext().getHostContext(), uploadConfig, (error, uploadTask) => {
52. if (uploadTask) {
53. uploadTask.on('progress', (uploadSize: number, totalSize: number) => {
54. console.info('progress,uploadedSize:' + uploadSize + ',totalSize:' + totalSize);
55. })
56. } else {
57. console.info('upload failure:' + error);
58. }
59. })
60. } catch (error) {
61. console.info('upload failure:' + error);
62. }
63. }

65. build() {
66. Column() {
67. Button('选择图片上传')
68. .width('100%')
69. .onClick(() => {
70. this.openPhotoPicker();
71. })
72. }
73. .width('100%')
74. .height('100%')
75. .padding(16)
76. .justifyContent(FlexAlign.End)
77. }
78. }
```

[ImageUpload.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/ImageUpload.ets#L21-L99)
