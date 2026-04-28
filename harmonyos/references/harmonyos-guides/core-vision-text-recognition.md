---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-text-recognition
title: 通用文字识别
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 通用文字识别
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97f30a61e9afc7d5841d43f5029c069a2e613f7a30ee9cf47ad8bc6179caf4a6
---

## 适用场景

通用文字识别，是通过拍照、扫描等光学输入方式，将各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息的技术。

* 可以对文档翻拍、街景翻拍等图片进行文字检测和识别，也可以集成于其他应用中，提供文字检测、识别的功能，并根据识别结果提供翻译、搜索等相关服务。
* 可以处理来自相机、图库等多种来源的图像数据，提供一个自动检测文本、识别图像中文本位置以及文本内容功能的开放能力。
* 支持特定角度范围内的文本倾斜、拍摄角度倾斜、复杂光照条件以及复杂文本背景等场景的文字识别。

效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/2DBt8eKvRmehNdURIWMH-g/zh-cn_image_0000002583439351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235327Z&HW-CC-Expire=86400&HW-CC-Sign=E9E6366BE751BABA9DA9A414969E80A89D35011843ED8F7F5C0C37EA1C94524C)

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 文字识别 | - 支持的图片格式：JPEG、JPG、PNG。  - 支持的语言：简体中文、英文、日文、韩文、繁体中文。  - 文本长度：不超过10000字符。  - 支持文档印刷体识别，在识别手写字体方面能力有所欠缺。  - 输入图像具有合适成像的质量（建议720p以上），100px<高度<15210px，100px<宽度<10000px，高宽比例建议10:1以下（高度小于宽度的10倍），接近手机屏幕高宽比例为宜。  - 拍摄角度与文本所在平面垂直方向的夹角应小于30度。 |

## 开发步骤

1. 在使用通用文字识别时，将实现文字识别的相关的类添加至工程。

   ```
   1. import { textRecognition } from '@kit.CoreVisionKit'
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
   2. const initResult = await textRecognition.init();
   3. hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
   4. }

   6. async aboutToDisappear(): Promise<void> {
   7. await textRecognition.release();
   8. hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
   9. }

   11. private async selectImage() {
   12. let uri = await this.openPhoto();
   13. if (uri === undefined) {
   14. hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
   15. return;
   16. }
   17. this.loadImage(uri);
   18. }

   20. private async openPhoto(): Promise<string> {
   21. return new Promise<string>((resolve) => {
   22. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
   23. photoPicker.select({
   24. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
   25. maxSelectNumber: 1
   26. }).then((res: photoAccessHelper.PhotoSelectResult) => {
   27. resolve(res.photoUris[0]);
   28. }).catch((err: BusinessError) => {
   29. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
   30. resolve('');
   31. })
   32. })
   33. }

   35. private loadImage(name: string) {
   36. setTimeout(async () => {
   37. let imageSource: image.ImageSource | undefined = undefined;
   38. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
   39. imageSource = image.createImageSource(fileSource.fd);
   40. this.chooseImage = await imageSource.createPixelMap();
   41. }, 100)
   42. }
   ```
4. 实例化[VisionInfo](../harmonyos-references/core-vision-text-recognition-api.md#visioninfo)对象，并传入待检测图片的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   VisionInfo为待OCR检测识别的入参项，目前仅支持[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)类型的视觉信息。

   ```
   1. let visionInfo: textRecognition.VisionInfo = {
   2. pixelMap: this.chooseImage
   3. };
   ```
5. 配置通用文本识别的配置项[TextRecognitionConfiguration](../harmonyos-references/core-vision-text-recognition-api.md#textrecognitionconfiguration)，用于配置是否支持朝向检测。

   ```
   1. let textConfiguration: textRecognition.TextRecognitionConfiguration = {
   2. isDirectionDetectionSupported: false
   3. };
   ```
6. 调用textRecognition的[recognizeText](../harmonyos-references/core-vision-text-recognition-api.md#textrecognitionrecognizetext-1)接口，对识别到的结果进行处理。

   当调用成功时，获取文字识别的结果；调用失败时，将返回对应错误码。recognizeText接口提供了三种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](../harmonyos-references/core-vision-text-recognition-api.md)。

   ```
   1. textRecognition.recognizeText(visionInfo, textConfiguration)
   2. .then((data: textRecognition.TextRecognitionResult) => {
   3. // 识别成功，获取对应的结果
   4. let recognitionString = JSON.stringify(data);
   5. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);
   6. // 将结果更新到Text中显示
   7. this.dataValues = data.value;
   8. })
   9. .catch((error: BusinessError) => {
   10. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
   11. this.dataValues = `Error: ${error.message}`;
   12. });
   ```

## 开发实例

点击按钮，识别一张图片的文字内容，并通过日志打印。

### Index.ets

```
1. import { textRecognition } from '@kit.CoreVisionKit'
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct Index {
11. private imageSource: image.ImageSource | undefined = undefined;
12. @State chooseImage: PixelMap | undefined = undefined;
13. @State dataValues: string = '';

15. async aboutToAppear(): Promise<void> {
16. const initResult = await textRecognition.init();
17. hilog.info(0x0000, 'OCRDemo', `OCR service initialization result:${initResult}`);
18. }

20. async aboutToDisappear(): Promise<void> {
21. await textRecognition.release();
22. hilog.info(0x0000, 'OCRDemo', 'OCR service released successfully');
23. }

25. build() {
26. Column() {
27. Image(this.chooseImage)
28. .objectFit(ImageFit.Fill)
29. .height('60%')

31. Text(this.dataValues)
32. .copyOption(CopyOptions.LocalDevice)
33. .height('15%')
34. .margin(10)
35. .width('60%')

37. Button('选择图片')
38. .type(ButtonType.Capsule)
39. .fontColor(Color.White)
40. .alignSelf(ItemAlign.Center)
41. .width('80%')
42. .margin(10)
43. .onClick(() => {
44. // 拉起图库，获取图片资源
45. void this.selectImage();
46. })

48. Button('开始识别')
49. .type(ButtonType.Capsule)
50. .fontColor(Color.White)
51. .alignSelf(ItemAlign.Center)
52. .width('80%')
53. .margin(10)
54. .onClick(() => {
55. this.textRecognitionTest();
56. })
57. }
58. .width('100%')
59. .height('100%')
60. .justifyContent(FlexAlign.Center)
61. }

63. private textRecognitionTest() {
64. if (!this.chooseImage) {
65. return;
66. }
67. // 调用文本识别接口
68. let visionInfo: textRecognition.VisionInfo = {
69. pixelMap: this.chooseImage
70. };
71. let textConfiguration: textRecognition.TextRecognitionConfiguration = {
72. isDirectionDetectionSupported: false
73. };
74. textRecognition.recognizeText(visionInfo, textConfiguration)
75. .then((data: textRecognition.TextRecognitionResult) => {
76. // 识别成功，获取对应的结果
77. let recognitionString = JSON.stringify(data);
78. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);
79. // 将结果更新到Text中显示
80. this.dataValues = data.value;
81. })
82. .catch((error: BusinessError) => {
83. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
84. this.dataValues = `Error: ${error.message}`;
85. });
86. }

88. private async selectImage() {
89. let uri = await this.openPhoto();
90. if (uri === undefined) {
91. hilog.error(0x0000, 'OCRDemo', "Failed to get uri.");
92. return;
93. }
94. this.loadImage(uri);
95. }

97. private async openPhoto(): Promise<string> {
98. return new Promise<string>((resolve) => {
99. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
100. photoPicker.select({
101. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
102. maxSelectNumber: 1
103. }).then((res: photoAccessHelper.PhotoSelectResult) => {
104. resolve(res.photoUris[0]);
105. }).catch((err: BusinessError) => {
106. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
107. resolve('');
108. })
109. })
110. }

112. private loadImage(name: string) {
113. setTimeout(async () => {
114. try {
115. let fileSource = await fileIo.open(name, fileIo.OpenMode.READ_ONLY);
116. this.imageSource = image.createImageSource(fileSource.fd);
117. this.chooseImage = await this.imageSource.createPixelMap();
118. await fileIo.close(fileSource);
119. } catch (error) {
120. hilog.error(0x0000, 'OCRDemo', `Failed to open file. Error: ${error}`);
121. }
122. }, 100)
123. }
124. }
```
