---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-subject-segmentation
title: 主体分割
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 主体分割
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0a56d937aa4d6d53f1d363a23c335f7ff4e44bc05c4b08ed74410eec8b33d67f
---

## 适用场景

主体分割，可以检测出图片中区别于背景的前景物体或区域（即“显著主体”），并将其从背景中分离出来，适用于需要识别和提取图像主要信息的场景，广泛使用于前景目标检测和前景主体分离的场景。例如：

* 主体贴纸，从图片中提取显著性的主体，去掉背景。
* 背景替换，替换并提取出主体对象的背景。
* 显著性检测，快速定位图片中显著性区域。
* 辅助图片编辑，例如单独对主体进行美化处理。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/pxlXsdMkRZiSt8mDjOPsOQ/zh-cn_image_0000002589325679.png?HW-CC-KV=V1&HW-CC-Date=20260429T054327Z&HW-CC-Expire=86400&HW-CC-Sign=86301BF25FFC0D731EBDCE3F0913CC2B99B8AB944DEADC60D5B7A652E0AD519A)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 主体分割 | - 某个物体占比不小于原图大小的千分之五才会被认定为“主体”，才会支持分割。  - 不建议用于处理包含较多文字内容的图片分析场景。  - 输入图像具有合适成像的质量（建议720p以上），20px<高度<9000px，20px<宽度<9000px，高宽比例建议3:1以下（高度小于宽度的3倍），接近手机屏幕高宽比例为宜。 |

## 开发步骤

1. 引用相关类添加至工程。

   ```
   1. import { subjectSegmentation } from '@kit.CoreVisionKit';
   2. import { image } from '@kit.ImageKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 准备预处理的图片资源，将图片转换为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，并添加初始化和释放方法。

   ```
   1. async aboutToAppear(): Promise<void> {
   2. const initResult = await subjectSegmentation.init();
   3. hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await subjectSegmentation.release();
   8. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
   9. }

   11. private async selectImage() {
   12. let uri = await this.openPhoto()
   13. if (uri === undefined) {
   14. hilog.error(0x0000, TAG, "uri is undefined");
   15. }
   16. this.loadImage(uri);
   17. }

   19. private async openPhoto(): Promise<Array<string>> {
   20. return new Promise<Array<string>>((resolve, reject) => {
   21. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   22. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
   23. PhotoSelectOptions.maxSelectNumber = 1;
   24. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   25. hilog.info(0x0000, TAG, 'PhotoViewPicker.select successfully, PhotoSelectResult uri: ');
   26. photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
   27. hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}`);
   28. resolve(PhotoSelectResult.photoUris)
   29. }).catch((err: BusinessError) => {
   30. hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
   31. reject();
   32. });
   33. })
   34. }

   36. private loadImage(names: string[]) {
   37. setTimeout(async () => {
   38. let imageSource: image.ImageSource | undefined = undefined
   39. let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY)
   40. imageSource = image.createImageSource(fileSource.fd)
   41. this.chooseImage = await imageSource.createPixelMap()
   42. }, 100
   43. )
   44. }
   ```
3. 实例化待分割的入参项[VisionInfo](../harmonyos-references/core-vision-subjectsegmentation-api.md#visioninfo)，并传入待检测图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   ```
   1. let visionInfo: subjectSegmentation.VisionInfo = {
   2. pixelMap: this.chooseImage,
   3. };
   ```
4. 配置通用文本识别的配置项[SegmentationConfig](../harmonyos-references/core-vision-subjectsegmentation-api.md#segmentationconfig)，包括最大分割主体个数、是否输出每个主体的分割信息，以及是否输出分割后的前景图。

   ```
   1. let config: subjectSegmentation.SegmentationConfig = {
   2. maxCount: parseInt(this.maxNum),
   3. enableSubjectDetails: true,
   4. enableSubjectForegroundImage: true,
   5. };
   ```
5. 调用subjectSegmentation的[subjectSegmentation.doSegmentation](../harmonyos-references/core-vision-subjectsegmentation-api.md#subjectsegmentationdosegmentation)接口，实现主体分割。

   ```
   1. let data: subjectSegmentation.SegmentationResult = await subjectSegmentation.doSegmentation(visionInfo, config);
   2. let outputString = `Subject count: ${data.subjectCount}\n`;
   3. outputString += `Max subject count: ${config.maxCount}\n`;
   4. outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
   5. let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
   6. let segBoxString = `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
   7. outputString += segBoxString;

   9. if (config.enableSubjectDetails) {
   10. outputString += 'Individual subject boxes:\n';
   11. if (data.subjectDetails) {
   12. for (let i = 0; i < data.subjectDetails.length; i++) {
   13. let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
   14. outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
   15. }
   16. }
   17. }
   ```

## 开发实例

### Index.ets

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. const TAG: string = "ImageSegmentationSample";

10. @Entry
11. @Component
12. struct Index {
13. @State chooseImage: PixelMap | undefined = undefined
14. @State dataValues: string = ''
15. @State segmentedImage: PixelMap | undefined = undefined
16. // 设置识别主体数量的上限
17. @State maxNum: string = '20'

20. build() {
21. Column() {
22. Image(this.chooseImage)
23. .objectFit(ImageFit.Fill)
24. .height('30%')
25. .accessibilityDescription("Image to be segmented")

27. Scroll() {
28. Text(this.dataValues)
29. .copyOption(CopyOptions.LocalDevice)
30. .margin(10)
31. .width('100%')
32. }
33. .height('20%')

35. Image(this.segmentedImage)
36. .objectFit(ImageFit.Fill)
37. .height('30%')
38. .accessibilityDescription("Segmented subject image")

40. Row() {
41. Text('Max subject count:')
42. .fontSize(16)
43. TextInput({ placeholder: 'Enter max subject count', text: this.maxNum })
44. .type(InputType.Number)
45. .placeholderColor(Color.Gray)
46. .fontSize(16)
47. .backgroundColor(Color.White)
48. .onChange((value: string) => {
49. this.maxNum = value
50. })
51. }
52. .width('80%')
53. .margin(10)

55. Button('Select Image')
56. .type(ButtonType.Capsule)
57. .fontColor(Color.White)
58. .alignSelf(ItemAlign.Center)
59. .width('80%')
60. .margin(10)
61. .onClick(() => {
62. void this.selectImage()
63. })

65. Button('Image Segmentation')
66. .type(ButtonType.Capsule)
67. .fontColor(Color.White)
68. .alignSelf(ItemAlign.Center)
69. .width('80%')
70. .margin(10)
71. .onClick(() => {
72. if (!this.chooseImage) {
73. hilog.error(0x0000, TAG, "imageSegmentation not have chooseImage");
74. return
75. }
76. let visionInfo: subjectSegmentation.VisionInfo = {
77. pixelMap: this.chooseImage,
78. };
79. let config: subjectSegmentation.SegmentationConfig = {
80. maxCount: parseInt(this.maxNum),
81. enableSubjectDetails: true,
82. enableSubjectForegroundImage: true,
83. };
84. subjectSegmentation.doSegmentation(visionInfo, config)
85. .then((data: subjectSegmentation.SegmentationResult) => {
86. let outputString = `Subject count: ${data.subjectCount}\n`;
87. outputString += `Max subject count: ${config.maxCount}\n`;
88. outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
89. let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
90. let segBoxString = `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
91. outputString += segBoxString;

93. if (config.enableSubjectDetails) {
94. outputString += 'Individual subject boxes:\n';
95. if (data.subjectDetails) {
96. for (let i = 0; i < data.subjectDetails.length; i++) {
97. let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
98. outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
99. }
100. }
101. }

103. hilog.info(0x0000, TAG, "Segmentation result: " + outputString);
104. this.dataValues = outputString;

106. if (data.fullSubject && data.fullSubject.foregroundImage) {
107. this.segmentedImage = data.fullSubject.foregroundImage;
108. } else {
109. hilog.warn(0x0000, TAG, "No foreground image in segmentation result");
110. }
111. })
112. .catch((error: BusinessError) => {
113. hilog.error(0x0000, TAG, `Image segmentation failed errCode: ${error.code}, errMessage: ${error.message}`);
114. this.dataValues = `Error: ${error.message}`;
115. this.segmentedImage = undefined;
116. });
117. })
118. }
119. .width('100%')
120. .height('80%')
121. .justifyContent(FlexAlign.Center)
122. }

124. private async selectImage() {
125. let uri = await this.openPhoto()
126. if (uri === undefined) {
127. hilog.error(0x0000, TAG, "uri is undefined");
128. }
129. this.loadImage(uri);
130. }

132. private async openPhoto(): Promise<Array<string>> {
133. return new Promise<Array<string>>((resolve, reject) => {
134. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
135. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
136. PhotoSelectOptions.maxSelectNumber = 1;
137. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
138. photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
139. hilog.info(0x0000, TAG, `PhotoViewPicker.select successfully, PhotoSelectResult uri: ${PhotoSelectResult.photoUris}`);
140. resolve(PhotoSelectResult.photoUris)
141. }).catch((err: BusinessError) => {
142. hilog.error(0x0000, TAG, `PhotoViewPicker.select failed with errCode: ${err.code}, errMessage: ${err.message}`);
143. reject();
144. });
145. })
146. }

148. private loadImage(names: string[]) {
149. setTimeout(async () => {
150. let imageSource: image.ImageSource | undefined = undefined
151. try {
152. let fileSource = await fileIo.open(names[0], fileIo.OpenMode.READ_ONLY)
153. imageSource = image.createImageSource(fileSource.fd)
154. this.chooseImage = await imageSource.createPixelMap()
155. await fileIo.close(fileSource);
156. } catch (error) {
157. hilog.error(0x0000, TAG, `Failed to open file. Error: ${error}`);
158. }
159. }, 100
160. )
161. }
162. }
```
