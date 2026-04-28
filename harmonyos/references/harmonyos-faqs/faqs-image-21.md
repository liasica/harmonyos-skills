---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-21
title: 如何保存网络图片到相册
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何保存网络图片到相册
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:33+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:0a1099b6caf58814d9e9fcc142cc129134cdfbcc6318645ff691a4344e09196f
---

可以使用安全控件中的保存控件，省去权限申请和权限请求等环节，获得临时授权，保存对应图片。需要申请的权限为：ohos.permission.INTERNET。参考代码如下：

```
1. import { http } from '@kit.NetworkKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { photoAccessHelper } from '@kit.MediaLibraryKit';
5. import { fileIo } from '@kit.CoreFileKit';

7. @Entry
8. @Component
9. struct SaveImage {
10. @State pixelMap: PixelMap | undefined = undefined;

12. loadImageWithUrl(url: string) {
13. let responseCode = http.ResponseCode;
14. let OutData: http.HttpResponse;
15. let imagePackerApi = image.createImagePacker();
16. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
17. // 确保网络正常
18. http.createHttp().request(url, {
19. method: http.RequestMethod.GET,
20. connectTimeout: 60000,
21. readTimeout: 60000
22. },
23. async (error: BusinessError, data: http.HttpResponse) => {
24. if (error) {
25. console.error(`http request failed with. Code: ${error.code}, message: ${error.message}`);
26. } else {
27. OutData = data;
28. let code: http.ResponseCode | number = OutData.responseCode;
29. if (responseCode.OK === code) {
30. let imageData: ArrayBuffer = OutData.result as ArrayBuffer;
31. let imageSource: image.ImageSource = image.createImageSource(imageData);

33. class tmp {
34. height: number = 100
35. width: number = 100
36. };

38. let options: Record<string, number | boolean | tmp> = {
39. 'alphaType': 0, // Transparency
40. 'editable': false, // Is it editable
41. 'pixelFormat': 3, // Pixel Format
42. 'scaleMode': 1, // Abbreviation
43. 'size': { height: 100, width: 100 }
44. }; // Create Image Size
45. imageSource.createPixelMap(options).then((pixelMap: PixelMap) => {
46. this.pixelMap = pixelMap;
47. this.pixelMap.getImageInfo().then((info: image.ImageInfo) => {
48. console.info('info.width = ' + info.size.width);
49. }).catch((err: BusinessError) => {
50. console.error('Failed ' + err);
51. })
52. imagePackerApi.packToData(pixelMap, packOpts).then(async (buffer: ArrayBuffer) => {
53. try {
54. const context = this.getUIContext().getHostContext()!;
55. let helper = photoAccessHelper.getPhotoAccessHelper(context);
56. let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
57. let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
58. // Write to file
59. await fileIo.write(file.fd, buffer);
60. this.getUIContext().getPromptAction().showToast({ message: '已保存至相册！' });
61. // Close the file
62. await fileIo.close(file.fd);
63. } catch (error) {
64. console.error('error is ' + JSON.stringify(error));
65. }
66. }).catch((error: BusinessError) => {
67. console.error('Failed to pack the image. And the error is: ' + error);
68. }).finally(()=>{
69. pixelMap.release();
70. })

72. })
73. }
74. }
75. }
76. )
77. }

79. build() {
80. Row() {
81. Column({ space: 10 }) {
82. Image('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png')
83. .width('80%')

85. SaveButton().onClick(async (event: ClickEvent, result: SaveButtonOnClickResult) => {
86. if (result === SaveButtonOnClickResult.SUCCESS) {
87. this.loadImageWithUrl('https://agc-storage-drcn.platform.dbankcloud.cn/v0/test-rqcjj/test.png');
88. } else {
89. this.getUIContext().getPromptAction().showToast({ message: '设置权限失败！' });
90. }
91. })
92. }
93. .width('100%')
94. }
95. .height('100%')
96. .backgroundColor(0xF1F3F5)
97. }
98. }
```

[SaveWebPictureToAlbum.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/SaveWebPictureToAlbum.ets#L21-L118)

**参考链接**

[使用保存控件](../harmonyos-guides/savebutton.md)

[存档图类型数据源](../harmonyos-guides/arkts-graphics-display.md#存档图类型数据源)
