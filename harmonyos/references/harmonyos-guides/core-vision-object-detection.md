---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-object-detection
title: 多目标识别
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 多目标识别
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:67c5345497e2b116bb290206cd630531ff7a86afbb9234c4516b7748f8663f93
---

## 适用场景

可同时检测出给定图片中的各种物体，包括风景、动物、植物、建筑、人脸、表格、文本等位置，并框选出物体。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/jINgs2teQM-kABvMsiZBjg/zh-cn_image_0000002589245619.png?HW-CC-KV=V1&HW-CC-Date=20260429T054327Z&HW-CC-Expire=86400&HW-CC-Sign=BBFF44B659DA233D146D159EA14373D19F7681545E6848EBEADFF82308E634F0)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 多目标识别 | - 输入图像具有合适成像的质量（建议720p以上），100px<高度<10000px，100px<宽度<10000px，高宽比例建议5:1以下（高度小于宽度的5倍），接近手机屏幕高宽比例为宜。  - 图片中的物体占比需要大于0.1%。 |

## 开发步骤

1. 在使用多目标识别时，将实现多目标识别相关的类添加至工程。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { objectDetection, visionBase } from '@kit.CoreVisionKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 简单配置页面的布局，并在Button组件添加点击事件，拉起图库，选择图片。

   ```
   1. Button('选择图片')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .alignSelf(ItemAlign.Center)
   5. .width('80%')
   6. .margin(10)
   7. .onClick(() => {
   8. // 拉起图库，获取图片资源
   9. void this.selectImage();
   10. })
   ```
3. 通过图库获取图片资源，将图片转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   ```
   1. private async selectImage() {
   2. let uri = await this.openPhoto()
   3. if (uri === undefined) {
   4. hilog.error(0x0000, 'objectDetectSample', "Failed to define uri.");
   5. }
   6. this.loadImage(uri)
   7. }

   9. private async openPhoto(): Promise<string> {
   10. return new Promise<string>((resolve, reject) => {
   11. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   12. photoPicker.select({
   13. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
   14. }).then(res => {
   15. resolve(res.photoUris[0])
   16. }).catch((err: BusinessError) => {
   17. hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
   18. reject('')
   19. })
   20. })
   21. }

   23. private loadImage(name: string) {
   24. setTimeout(async () => {
   25. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
   26. this.imageSource = image.createImageSource(fileSource.fd);
   27. this.chooseImage = await this.imageSource.createPixelMap();
   28. }, 100)
   29. }
   ```
4. 实例化Request对象，并传入待检测图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，调用多目标识别的实现多目标识别功能。

   ```
   1. // 调用多目标检测接口
   2. let request: visionBase.Request = {
   3. inputData: { pixelMap: this.chooseImage }
   4. };
   5. let data: objectDetection.ObjectDetectionResponse = await (await objectDetection.ObjectDetector.create()).process(request);
   ```
5. （可选）如果需要将结果展示在界面上，可以使用下列代码。

   ```
   1. let objectJson = JSON.stringify(data);
   2. hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection: ${objectJson}`);
   3. this.dataValues = objectJson;
   ```

## 开发实例

### Index.ets

```
1. import { image } from '@kit.ImageKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { objectDetection, visionBase } from '@kit.CoreVisionKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. private imageSource: image.ImageSource | undefined = undefined;
12. @State chooseImage: PixelMap | undefined = undefined
13. @State dataValues: string = ''

15. build() {
16. Column() {
17. Image(this.chooseImage)
18. .objectFit(ImageFit.Fill)
19. .height('60%')

21. Text(this.dataValues)
22. .copyOption(CopyOptions.LocalDevice)
23. .height('15%')
24. .margin(10)
25. .width('60%')

27. Button('选择图片')
28. .type(ButtonType.Capsule)
29. .fontColor(Color.White)
30. .alignSelf(ItemAlign.Center)
31. .width('80%')
32. .margin(10)
33. .onClick(() => {
34. // 拉起图库
35. void this.selectImage()
36. })

38. Button('开始多目标识别')
39. .type(ButtonType.Capsule)
40. .fontColor(Color.White)
41. .alignSelf(ItemAlign.Center)
42. .width('80%')
43. .margin(10)
44. .onClick(() => {
45. // 调用封装的异步识别函数
46. void this.handleMultiObjectDetection();
47. })
48. }
49. .width('100%')
50. .height('100%')
51. .justifyContent(FlexAlign.Center)
52. }

54. // 封装多目标识别的异步逻辑
55. private async handleMultiObjectDetection() {
56. if(!this.chooseImage) {
57. hilog.error(0x0000, 'objectDetectSample', `Failed to choose image.`);
58. return;
59. }
60. let request: visionBase.Request = {
61. inputData: { pixelMap: this.chooseImage }
62. };
63. try {
64. let data: objectDetection.ObjectDetectionResponse =
65. await (await objectDetection.ObjectDetector.create()).process(request);
66. let objectJson = JSON.stringify(data);
67. hilog.info(0x0000, 'objectDetectSample', `Succeeded in object detection: ${objectJson}`);
68. this.dataValues = objectJson;
69. } catch (error) {
70. hilog.error(0x0000, 'objectDetectSample', `Failed to get result. Error: ${error}`);
71. }
72. }

74. private async selectImage() {
75. try {
76. let uri = await this.openPhoto();
77. if (uri === undefined) {
78. hilog.error(0x0000, 'objectDetectSample', "Failed to define uri.");
79. return;
80. }
81. this.loadImage(uri);
82. } catch (err) {
83. hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
84. }
85. }

87. private async openPhoto(): Promise<string> {
88. return new Promise<string>((resolve, reject) => {
89. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
90. photoPicker.select({
91. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
92. }).then(res => {
93. resolve(res.photoUris[0]);
94. }).catch((err: BusinessError) => {
95. hilog.error(0x0000, 'objectDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
96. reject(err);
97. })
98. })
99. }

101. private loadImage(name: string) {
102. setTimeout(async () => {
103. try {
104. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
105. this.imageSource = image.createImageSource(fileSource.fd);
106. this.chooseImage = await this.imageSource.createPixelMap();
107. await fileIo.close(fileSource);
108. } catch (error) {
109. hilog.error(0x0000, 'objectDetectSample', `Failed to open file. Error: ${error}`);
110. }
111. }, 100)
112. }
113. }
```
