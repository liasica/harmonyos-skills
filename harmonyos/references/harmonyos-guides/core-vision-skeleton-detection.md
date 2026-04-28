---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-skeleton-detection
title: 骨骼点检测
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 骨骼点检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55e35b7c557178ae73a6c43acc206bc773f4555a6a07857d198736383315b571
---

## 适用场景

人体骨骼关键点检测，主要检测人体的一些关键点，通过关键点描述人体骨骼信息。具体应用主要集中在智能视频监控，病人监护系统，人机交互，虚拟现实，人体动画，智能家居，智能安防，运动员辅助训练等等。

支持17个关键点的识别，具体为鼻子，左右眼，左右耳，左右肩，左右肘、左右手腕、左右髋、左右膝、左右脚踝。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/tuAtW-vtT--7Mej4d4uizg/zh-cn_image_0000002583479309.png?HW-CC-KV=V1&HW-CC-Date=20260427T235328Z&HW-CC-Expire=86400&HW-CC-Sign=2EF5C169FEE0308BD228637EE242F0974346994B6AC91966FD0E17D671F01132)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 骨骼点检测 | - 输入图像具有合适成像的质量（建议720p以上），100px<高度<10000px，100px<宽度<10000px，高宽比例建议5:1以下（高度小于宽度的5倍），接近手机屏幕高宽比例为宜。 |

## 开发步骤

1. 在使用骨骼点检测时，将实现骨骼点检测相关的类添加至工程。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
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
   4. hilog.error(0x0000, 'skeletonDetectSample', "Failed to define uri.");
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
   17. hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
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
4. 实例化Request对象，并传入待检测图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，实现骨骼点检测功能。

   ```
   1. // 调用骨骼点识别接口
   2. let request: visionBase.Request = {
   3. inputData: { pixelMap: this.chooseImage }
   4. };
   5. let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
   ```
5. （可选）如果需要将结果展示在界面上，可以用下列代码。

   ```
   1. let data: skeletonDetection.SkeletonDetectionResponse = await (await skeletonDetection.SkeletonDetector.create()).process(request);
   2. let poseJson = JSON.stringify(data);
   3. hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
   4. this.dataValues = poseJson;
   ```

## 开发实例

### Index.ets

```
1. import { image } from '@kit.ImageKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
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

38. Button('开始骨骼点识别')
39. .type(ButtonType.Capsule)
40. .fontColor(Color.White)
41. .alignSelf(ItemAlign.Center)
42. .width('80%')
43. .margin(10)
44. .onClick(() => {
45. // 调用封装的异步处理函数
46. void this.handleSkeletonDetection();
47. })
48. }
49. .width('100%')
50. .height('100%')
51. .justifyContent(FlexAlign.Center)
52. }

54. // 封装骨骼点识别的异步逻辑
55. private async handleSkeletonDetection() {
56. if(!this.chooseImage) {
57. hilog.error(0x0000, 'skeletonDetectSample', `Failed to choose image.`);
58. return;
59. }
60. // 调用骨骼点识别接口
61. let request: visionBase.Request = {
62. inputData: { pixelMap: this.chooseImage }
63. };
64. try {
65. let data: skeletonDetection.SkeletonDetectionResponse =
66. await (await skeletonDetection.SkeletonDetector.create()).process(request);
67. let poseJson = JSON.stringify(data);
68. hilog.info(0x0000, 'skeletonDetectSample', `Succeeded in skeleton detection: ${poseJson}`);
69. this.dataValues = poseJson;
70. } catch (error) {
71. hilog.error(0x0000, 'skeletonDetectSample', `Failed to get result. Error: ${error}`);
72. }
73. }

75. private async selectImage() {
76. let uri = await this.openPhoto()
77. if (uri === undefined) {
78. hilog.error(0x0000, 'skeletonDetectSample', "Failed to define uri.");
79. }
80. this.loadImage(uri)
81. }

83. private async openPhoto(): Promise<string> {
84. return new Promise<string>((resolve, reject) => {
85. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
86. photoPicker.select({
87. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
88. }).then(res => {
89. resolve(res.photoUris[0])
90. }).catch((err: BusinessError) => {
91. hilog.error(0x0000, 'skeletonDetectSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
92. reject('')
93. })
94. })
95. }

97. private loadImage(name: string) {
98. setTimeout(async () => {
99. try {
100. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
101. this.imageSource = image.createImageSource(fileSource.fd);
102. this.chooseImage = await this.imageSource.createPixelMap();
103. await fileIo.close(fileSource);
104. } catch (error) {
105. hilog.error(0x0000, 'skeletonDetectSample', `Failed to open file. Error: ${error}`);
106. }
107. }, 100)
108. }
109. }
```
