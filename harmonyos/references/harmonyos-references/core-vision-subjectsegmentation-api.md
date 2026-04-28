---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-subjectsegmentation-api
title: subjectSegmentation（主体分割）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > subjectSegmentation（主体分割）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3bef881c41cf1eaaeb094cf01d6cfdfb653a6337cd8d0a790267ef62d6b3ed7
---

Core Vision Kit根据配置参数（如最多检测多少个物体、是否输出每个物体的详细信息等）可将一张普通的图片进行分割，分割后的信息包括图片整体的分割结果和每个显著物体的详细信息。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
```

## VisionInfo

PhonePC/2in1Tablet

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的PixelMap类型的视觉信息。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 待识别的图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## SegmentationConfig

PhonePC/2in1Tablet

显著性分割的可选配置项，包括最多输出的主体个数、是否输出每个主体的详细分割信息，以及是否输出前景图的配置项。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxCount | number | 否 | 是 | 最多输出主体个数。取值范围为[1,20]，以主体在原图中的面积占比降序排序，默认为6。 |
| enableSubjectDetails | boolean | 否 | 是 | 是否输出每个主体的前景信息（subjectDetails），默认为false，true代表输出每个主体的前景信息。 |
| enableSubjectForegroundImage | boolean | 否 | 是 | 是否输出前景图，默认为false，true代表输出前景图。 |

## Rectangle

PhonePC/2in1Tablet

显著性主体分割后的边界框。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 边界框左上角的x坐标。 |
| top | number | 否 | 否 | 边界框左上角的y坐标。 |
| height | number | 否 | 否 | 边界框高度，单位为像素。 |
| width | number | 否 | 否 | 边界框宽度，单位为像素。 |

## SubjectResult

PhonePC/2in1Tablet

分割后的详细结果。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foregroundImage | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 显著性主体前景图。 |
| mattingList | Int32Array | 否 | 否 | 基于原图大小的一维数组，表示主体掩码。0-255取值范围。0代表背景，255代表主体，中间值代表是否是显著性主体的概率。 |
| subjectRectangle | [Rectangle](core-vision-subjectsegmentation-api.md#rectangle) | 否 | 否 | 主体的内切框。 |

## SegmentationResult

PhonePC/2in1Tablet

分割后的总输出结果，包括主体个数、整张图中所有主体的分割信息和每个主体的详细信息。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subjectCount | number | 否 | 否 | 表示主体个数，取决于[SegmentationConfig](core-vision-subjectsegmentation-api.md#segmentationconfig)中maxCount参数的限制。 |
| fullSubject | [SubjectResult](core-vision-subjectsegmentation-api.md#subjectresult) | 否 | 否 | 默认输出的整张图的所有显著性主体信息。 |
| subjectDetails | Array<[SubjectResult](core-vision-subjectsegmentation-api.md#subjectresult)> | 否 | 是 | 每个主体的显著性主体信息。 |

## subjectSegmentation.init

PhonePC/2in1Tablet

init(): Promise<boolean>

初始化主体分割服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseSubjectSegmentation() {
5. // 初始化主体分割服务
6. const initResult = await subjectSegmentation.init();
7. hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

12. // 这里可以添加使用主体分割服务的代码

14. // 使用完毕后，释放主体分割服务
15. await subjectSegmentation.release();
16. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
17. } else {
18. hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseSubjectSegmentation').onClick(() => {
29. // 调用函数
30. void initAndReleaseSubjectSegmentation();
31. })
32. }
33. }
34. }
```

## subjectSegmentation.release

PhonePC/2in1Tablet

release(): Promise<void>

释放主体分割服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，释放接口无返回值。 |

**示例：**

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseSubjectSegmentation() {
5. // 初始化主体分割服务
6. const initResult = await subjectSegmentation.init();
7. hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

12. // 这里可以添加使用主体分割服务的代码

14. // 使用完毕后，释放主体分割服务
15. await subjectSegmentation.release();
16. hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
17. } else {
18. hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseSubjectSegmentation').onClick(() => {
29. // 调用函数
30. void initAndReleaseSubjectSegmentation();
31. })
32. }
33. }
34. }
```

## subjectSegmentation.doSegmentation

PhonePC/2in1Tablet

doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>

创建显著性分割实例，并初始化引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-subjectsegmentation-api.md#visioninfo) | 是 | 图片实例。 |
| config | [SegmentationConfig](core-vision-subjectsegmentation-api.md#segmentationconfig) | 否 | 显著性分割的可选配置项，包括最大主体个数和是否输出每个主体的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SegmentationResult](core-vision-subjectsegmentation-api.md#segmentationresult)> | 返回显著性主体的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011000001 | Failed to run, please try again. |
| 1011000002 | The service is abnormal. |

**示例：**

```
1. import { subjectSegmentation } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. const TAG: string = 'ImageSegmentationSample';

10. async function subjectSegmentationTest() {
11. let chooseImage: image.PixelMap | undefined = undefined;
12. // 设置识别主体数量的上限
13. let maxNum: string = '20';

15. // Select an image from the gallery
16. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
17. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
18. PhotoSelectOptions.maxSelectNumber = 1;
19. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
20. let PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
21. let uris = PhotoSelectResult.photoUris;

23. if (uris.length !== 1) {
24. hilog.info(0x0000, TAG, 'Selected uris length is not 1');
25. return;
26. }

28. // Convert the selected image to PixelMap
29. let fileSource = await fileIo.open(uris[0], fileIo.OpenMode.READ_ONLY);
30. let imageSource = image.createImageSource(fileSource.fd);
31. chooseImage = await imageSource.createPixelMap();

33. if (!chooseImage) {
34. hilog.info(0x0000, TAG, 'chooseImage is undefined');
35. return;
36. }
37. if (fileSource) {
38. try {
39. await fileIo.close(fileSource);
40. } catch (err) {
41. hilog.error(0x0000, TAG, `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
42. }
43. }

45. // Call the image segmentation interface
46. let visionInfo: subjectSegmentation.VisionInfo = {
47. pixelMap: chooseImage
48. };
49. let config: subjectSegmentation.SegmentationConfig = {
50. maxCount: parseInt(maxNum),
51. enableSubjectDetails: true,
52. enableSubjectForegroundImage: true
53. };
54. let data: subjectSegmentation.SegmentationResult = await subjectSegmentation.doSegmentation(visionInfo, config);
55. let outputString = `Subject count: ${data.subjectCount}\n`;
56. outputString += `Max subject count: ${config.maxCount}\n`;
57. outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
58. let segBox : subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
59. let segBoxString = `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;
60. outputString += segBoxString;

62. if (config.enableSubjectDetails) {
63. outputString += 'Individual subject boxes:\n';
64. if (data.subjectDetails) {
65. for (let i = 0; i < data.subjectDetails.length; i++) {
66. let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
67. outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
68. }
69. }
70. }

72. hilog.info(0x0000, TAG, 'Segmentation result: ' + outputString);
73. }

77. @Entry
78. @Component
79. struct Page {

81. build() {
82. Column(){
83. Button('subjectSegmentationTest').onClick(() => {
84. subjectSegmentationTest().catch((err: BusinessError) => {
85. hilog.error(0x0000, TAG, `Failed to segment a photo. code: ${err.code}, message: ${err.message}`);
86. });
87. })
88. }
89. }
90. }
```
