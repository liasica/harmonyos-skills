---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-face-comparator
title: 人脸比对
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 人脸比对
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:864ba981ac113bdfd414da6de4e6dec77d697294c1aabc806ab108ba3134fc5f
---

## 适用场景

输入的两张比对图片是同一个人的照片时，系统返回的比对结果为"同一个人"，置信分数比较高；当两张比对图片不是同一个人的照片时，系统返回的比对结果为"非同一个人"，置信分数很低。可以用于APP中需要用到人脸比对功能的场景，比如娱乐类APP中比较两个人的相似度、与明星的相似度等。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/vmRLAX5WTWOMxynIkLza4g/zh-cn_image_0000002552799658.png?HW-CC-KV=V1&HW-CC-Date=20260427T235327Z&HW-CC-Expire=86400&HW-CC-Sign=374C079E46FA6E31A08E308D8C6765CF224BE6B1D9FE8B07EC7345105B690A3A)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 人脸比对 | - 当前功能只支持1v1人脸比对。  - 输入的两张图像都需要合适的成像质量（建议720p以上），224px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下（高度小于宽度的10倍），接近手机屏幕高宽比例为宜。 |

## 开发步骤

1. 在使用人脸比对时，将实现人脸比对相关的类添加至工程。

   ```
   1. import { faceComparator } from '@kit.CoreVisionKit';
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
3. 通过图库获取图片资源，将图片转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，并添加初始化和释放方法。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await faceComparator.init();
   3. hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await faceComparator.release();
   8. hilog.info(0x0000, TAG, 'Face comparator released successfully');
   9. }

   11. private async selectImage() {
   12. let uri = await this.openPhoto()
   13. if (uri === undefined) {
   14. hilog.error(0x0000, 'faceCompare', "Failed to get two image uris.");
   15. }
   16. this.loadImage(uri);
   17. }

   19. private async openPhoto(): Promise<string[]> {
   20. return new Promise<string[]>((resolve, reject) => {
   21. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   22. photoPicker.select({
   23. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   24. maxSelectNumber: 2
   25. }).then(res => {
   26. resolve(res.photoUris);
   27. }).catch((err: BusinessError) => {
   28. hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
   29. reject();
   30. });
   31. });
   32. }

   34. private loadImage(names: string[]) {
   35. setTimeout(async () => {
   36. let imageSource: image.ImageSource | undefined = undefined;
   37. let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
   38. imageSource = image.createImageSource(fileSource.fd);
   39. this.chooseImage = await imageSource.createPixelMap();
   40. fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
   41. imageSource = image.createImageSource(fileSource.fd);
   42. this.chooseImage1 = await imageSource.createPixelMap();
   43. }, 100
   44. )
   45. }
   ```
4. 实现人脸比对功能。实例化[VisionInfo](../harmonyos-references/core-vision-facecomparator-api.md#visioninfo)对象，传入两张图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，调用[faceComparator.compareFaces](../harmonyos-references/core-vision-facecomparator-api.md#facecomparatorcomparefaces)方法进行人脸比对。

   ```
   1. // 调用人脸比对接口
   2. let visionInfo: faceComparator.VisionInfo = {
   3. pixelMap: this.chooseImage,
   4. };
   5. let visionInfo1: faceComparator.VisionInfo = {
   6. pixelMap: this.chooseImage1,
   7. };
   8. let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
   ```
5. （可选）如果需要将结果展示在界面上，可以用下列代码。

   ```
   1. let data:faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
   2. let faceString = "degree of similarity: "+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
   3. hilog.info(0x0000, 'testTag', "faceString data is " + faceString);
   4. this.dataValues = faceString;
   ```

## 开发实例

### Index.ets

```
1. import { faceComparator } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. const TAG: string = "FaceCompareSample";

10. @Entry
11. @Component
12. struct Index {
13. @State chooseImage: PixelMap | undefined = undefined
14. @State chooseImage1: PixelMap | undefined = undefined
15. @State dataValues: string = ''

17. async aboutToAppear(): Promise<void> {
18. const initResult = await faceComparator.init();
19. hilog.info(0x0000, TAG, `Face comparator initialization result:${initResult}`);
20. }

22. async aboutToDisappear(): Promise<void> {
23. await faceComparator.release();
24. hilog.info(0x0000, TAG, 'Face comparator released successfully');
25. }

27. build() {
28. Column() {
29. Image(this.chooseImage)
30. .objectFit(ImageFit.Fill)
31. .height('30%')
32. .accessibilityDescription("默认图片1")
33. Image(this.chooseImage1)
34. .objectFit(ImageFit.Fill)
35. .height('30%')
36. .accessibilityDescription("默认图片2")
37. Text(this.dataValues)
38. .copyOption(CopyOptions.LocalDevice)
39. .height('15%')
40. .margin(10)
41. .width('60%')
42. Button('选择图片')
43. .type(ButtonType.Capsule)
44. .fontColor(Color.White)
45. .alignSelf(ItemAlign.Center)
46. .width('80%')
47. .margin(10)
48. .onClick(() => {
49. // 拉起图库
50. void this.selectImage()
51. })
52. Button('人脸比对')
53. .type(ButtonType.Capsule)
54. .fontColor(Color.White)
55. .alignSelf(ItemAlign.Center)
56. .width('80%')
57. .margin(10)
58. .onClick(() => {
59. if(!this.chooseImage || !this.chooseImage1) {
60. hilog.error(0x0000, TAG, "Failed to choose image");
61. return;
62. }
63. // 调用人脸比对接口
64. let visionInfo: faceComparator.VisionInfo = {
65. pixelMap: this.chooseImage,
66. };
67. let visionInfo1: faceComparator.VisionInfo = {
68. pixelMap: this.chooseImage1,
69. };
70. faceComparator.compareFaces(visionInfo, visionInfo1)
71. .then((data: faceComparator.FaceCompareResult) => {
72. let faceString = "degree of similarity: "+ this.toPercentage(data.similarity)+((data.isSamePerson)?". is":". no")+ " same person";
73. hilog.info(0x0000, TAG, "faceString data is " + faceString);
74. this.dataValues = faceString;
75. })
76. .catch((error: BusinessError) => {
77. hilog.error(0x0000, TAG, `Face comparison failed. Code: ${error.code}, message: ${error.message}`);
78. this.dataValues = `Error: ${error.message}`;
79. });
80. })
81. }
82. .width('100%')
83. .height('100%')
84. .justifyContent(FlexAlign.Center)
85. }

87. private toPercentage(num: number): string {
88. return `${(num * 100).toFixed(2)}%`;
89. }

91. private async selectImage() {
92. let uri = await this.openPhoto()
93. if (uri === undefined) {
94. hilog.error(0x0000, TAG, "Failed to get two image uris.");
95. }
96. this.loadImage(uri);
97. }

99. private async openPhoto(): Promise<string[]> {
100. return new Promise<string[]>((resolve, reject) => {
101. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
102. photoPicker.select({
103. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
104. maxSelectNumber: 2
105. }).then(res => {
106. resolve(res.photoUris);
107. }).catch((err: BusinessError) => {
108. hilog.error(0x0000, TAG, `Failed to get photo image uris. code: ${err.code}, message: ${err.message}`);
109. reject();
110. });
111. });
112. }

114. private loadImage(names: string[]) {
115. setTimeout(async () => {
116. let imageSource: image.ImageSource | undefined = undefined;
117. let fileSource: fileIo.File
118. try {
119. fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY);
120. imageSource = image.createImageSource(fileSource.fd);
121. this.chooseImage = await imageSource.createPixelMap();
122. } catch (error) {
123. hilog.error(0x0000, TAG, `Failed to open file. Error: ${error}`);
124. }
125. try {
126. fileSource = await fileIo.open(names[1], fileIo.OpenMode.READ_ONLY);
127. imageSource = image.createImageSource(fileSource.fd);
128. this.chooseImage1 = await imageSource.createPixelMap();
129. await fileIo.close(fileSource);
130. } catch (error) {
131. hilog.error(0x0000, TAG, `Failed to open the second file. Error: ${error}`);
132. }
133. }, 100
134. )
135. }
136. }
```
