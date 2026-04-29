---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-face-detector
title: 人脸检测
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 人脸检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:279d6cd74cbbf43c8ef79c5f10071ae1d722ea6ced42cdcfc42f763c60178e77
---

## 适用场景

检测图片中的人脸，返回高精度人脸矩形框坐标、人脸五官位置、人脸朝向、人脸置信度。可通过对人脸的定位，实现对人脸特定位置的美化修饰。广泛应用于各类人脸识别场景，如人脸聚类、美颜等场景中。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/PtTl3SN0Q4iw5DBHTzJxRA/zh-cn_image_0000002589245617.png?HW-CC-KV=V1&HW-CC-Date=20260429T054327Z&HW-CC-Expire=86400&HW-CC-Sign=29617660757828E9A1994E4939CF6296B60AEF073FFD774D9620AE091CD12F7E)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 人脸检测 | - 输入图像具有合适的成像质量（建议720p以上），224px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下（高度小于宽度的10倍），接近手机屏幕高宽比例为宜。  - 接口调用耗时较久，不适合在需要实时检测的场景下使用。  - 不支持同一用户启用多个线程。 |

## 世界坐标系

以下方图片指示坐标系辅助表示人脸朝向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/Ud8ktER3SSK-NKAbKYS1Kw/zh-cn_image_0000002558765808.png?HW-CC-KV=V1&HW-CC-Date=20260429T054327Z&HW-CC-Expire=86400&HW-CC-Sign=2073F1E3218785DFC9080C280374F049421E326409E3C3D279C310A5EE4F8BE4)

## 开发步骤

1. 在使用人脸检测时，将实现人脸检测相关的类添加至工程。

   ```
   1. import { faceDetector } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
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
   4. hilog.error(0x0000, 'faceDetector', "Failed to get uri.");
   5. }
   6. this.loadImage(uri)
   7. }

   9. private async openPhoto(): Promise<string> {
   10. return new Promise<string>((resolve) => {
   11. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   12. photoPicker.select({
   13. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   14. maxSelectNumber: 1
   15. }).then(res => {
   16. resolve(res.photoUris[0])
   17. }).catch((err: BusinessError) => {
   18. hilog.error(0x0000, 'faceDetector', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
   19. resolve('');
   20. })
   21. })
   22. }

   24. private loadImage(name: string) {
   25. setTimeout(async () => {
   26. let imageSource: image.ImageSource | undefined = undefined;
   27. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
   28. imageSource = image.createImageSource(fileSource.fd);
   29. this.chooseImage = await imageSource.createPixelMap();
   30. this.dataValues = "";
   31. }, 100
   32. )
   33. }
   ```
4. 实例化[VisionInfo](../harmonyos-references/core-vision-face-detector-api.md#visioninfo)对象，并传入待检测图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，实现人脸检测功能。

   ```
   1. // 初始化并调用人脸检测接口
   2. void faceDetector.init();
   3. let visionInfo: faceDetector.VisionInfo = {
   4. pixelMap: this.chooseImage,
   5. };
   6. let data:faceDetector.Face[] = await faceDetector.detect(visionInfo);
   ```
5. （可选）如果需要将结果展示在界面上，可以使用下列代码。

   ```
   1. let data:faceDetector.Face[] = await faceDetector.detect(visionInfo);
   2. if (data.length === 0) {
   3. this.dataValues = "No face is detected in the image. Select an image that contains a face.";
   4. } else {
   5. let faceString = JSON.stringify(data);
   6. hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
   7. this.dataValues = faceString;
   8. }
   ```

## 开发实例

### Index.ets

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. @State chooseImage: PixelMap | undefined = undefined
12. @State dataValues: string = ''

14. build() {
15. Column() {
16. Image(this.chooseImage)
17. .objectFit(ImageFit.Fill)
18. .height('60%')
19. Text(this.dataValues)
20. .copyOption(CopyOptions.LocalDevice)
21. .height('15%')
22. .margin(10)
23. .width('60%')
24. Button('选择图片')
25. .type(ButtonType.Capsule)
26. .fontColor(Color.White)
27. .alignSelf(ItemAlign.Center)
28. .width('80%')
29. .margin(10)
30. .onClick(() => {
31. // 拉起图库
32. void this.selectImage()
33. })
34. Button('人脸检测')
35. .type(ButtonType.Capsule)
36. .fontColor(Color.White)
37. .alignSelf(ItemAlign.Center)
38. .width('80%')
39. .margin(10)
40. .onClick(() => {
41. if(!this.chooseImage) {
42. hilog.error(0x0000, 'faceDetectorSample', "Failed to detect face.");
43. return;
44. }
45. // 调用人脸检测接口
46. void faceDetector.init();
47. let visionInfo: faceDetector.VisionInfo = {
48. pixelMap: this.chooseImage,
49. };
50. faceDetector.detect(visionInfo)
51. .then((data: faceDetector.Face[]) => {
52. if (data.length === 0) {
53. this.dataValues = "No face is detected in the image. Select an image that contains a face.";
54. } else {
55. let faceString = JSON.stringify(data);
56. hilog.info(0x0000, 'faceDetectorSample', "faceString data is " + faceString);
57. this.dataValues = faceString;
58. }
59. })
60. .catch((error: BusinessError) => {
61. hilog.error(0x0000, 'faceDetectorSample', `Face detection failed. Code: ${error.code}, message: ${error.message}`);
62. this.dataValues = `Error: ${error.message}`;
63. });
64. void faceDetector.release();
65. })
66. }
67. .width('100%')
68. .height('100%')
69. .justifyContent(FlexAlign.Center)
70. }

72. private async selectImage() {
73. let uri = await this.openPhoto()
74. if (uri === undefined) {
75. hilog.error(0x0000, 'faceDetectorSample', "Failed to get uri.");
76. }
77. this.loadImage(uri);
78. }

80. private async openPhoto(): Promise<string> {
81. return new Promise<string>((resolve) => {
82. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
83. photoPicker.select({
84. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
85. maxSelectNumber: 1
86. }).then(res => {
87. resolve(res.photoUris[0])
88. }).catch((err: BusinessError) => {
89. hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri.code: ${err.code}, message: ${err.message}`);
90. resolve('');
91. })
92. })
93. }

95. private loadImage(name: string) {
96. setTimeout(async () => {
97. let imageSource: image.ImageSource | undefined = undefined;
98. try {
99. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
100. imageSource = image.createImageSource(fileSource.fd);
101. this.chooseImage = await imageSource.createPixelMap();
102. this.dataValues = "";
103. await fileIo.close(fileSource);
104. } catch (error) {
105. hilog.error(0x0000, 'faceDetectorSample', `Failed to open file. Error: ${error}`);
106. }
107. }, 100
108. )
109. }
110. }
```
