---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-facecomparator-api
title: faceComparator（人脸比对）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > faceComparator（人脸比对）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e6d5ae2f23b5ea572f11173e7336235bf98ff8bb9db1ba73e8899950681ca40
---

识别人脸，对人像进行高精度比对，给出置信度分数，判断对象是否为同一个人。人脸比对技术可应用于实现对图库照片的智能分类管理等场景中。基于领先的端侧智能图像识别算法，对人脸识别准确度高，让应用体验更好。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { faceComparator } from '@kit.CoreVisionKit';
```

## VisionInfo

PhonePC/2in1Tablet

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的PixelMap类型的视觉信息。

**系统能力：** SystemCapability.AI.Face.Comparator

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 待识别的图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## FaceCompareResult

PhonePC/2in1Tablet

人脸比对的结果。

**系统能力：** SystemCapability.AI.Face.Comparator

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isSamePerson | boolean | 是 | 否 | 是否是同一个人，true代表为同一个人，false不是同一个人。 |
| similarity | number | 是 | 否 | 相似度，取值范围是(0,1)的浮点数。值越大说明相似程度越高。 |

## faceComparator.init

PhonePC/2in1Tablet

init(): Promise<boolean>

初始化人脸比对分析器服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Face.Comparator

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```
1. import { faceComparator } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseFaceComparator() {
5. // 初始化人脸比较服务
6. const initResult = await faceComparator.init();
7. hilog.info(0x0000, 'faceComparatorSample', `Face comparator initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

12. // 这里可以添加使用人脸比较服务的代码

14. // 使用完毕后，释放人脸比较服务
15. await faceComparator.release();
16. hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
17. } else {
18. hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseFaceComparator').onClick(() => {
29. // 调用函数
30. void initAndReleaseFaceComparator();
31. })
32. }
33. }
34. }
```

## faceComparator.release

PhonePC/2in1Tablet

release(): Promise<void>

释放人脸比对分析器服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Face.Comparator

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，释放接口无返回值。 |

**示例：**

```
1. import { faceComparator } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseFaceComparator() {
5. // 初始化人脸比较服务
6. const initResult = await faceComparator.init();
7. hilog.info(0x0000, 'faceComparatorSample', `Face comparator initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'faceComparatorSample', 'Face comparator initialized successfully');

12. // 这里可以添加使用人脸比较服务的代码

14. // 使用完毕后，释放人脸比较服务
15. await faceComparator.release();
16. hilog.info(0x0000, 'faceComparatorSample', 'Face comparator released successfully');
17. } else {
18. hilog.error(0x0000, 'faceComparatorSample', 'Failed to initialize face comparator');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseFaceComparator').onClick(() => {
29. // 调用函数
30. void initAndReleaseFaceComparator();
31. })
32. }
33. }
34. }
```

## faceComparator.compareFaces

PhonePC/2in1Tablet

compareFaces(visionInfo1: VisionInfo, visionInfo2: VisionInfo): Promise<FaceCompareResult>

创建人脸比对实例，使用Promise异步回调。

**系统能力：** SystemCapability.AI.Face.Comparator

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo1 | [VisionInfo](core-vision-facecomparator-api.md#visioninfo) | 是 | 第一张包含人脸的图片。 |
| visionInfo2 | [VisionInfo](core-vision-facecomparator-api.md#visioninfo) | 是 | 第二张包含人脸的图片。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FaceCompareResult](core-vision-facecomparator-api.md#facecompareresult)> | Promise对象，返回人脸比对的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1008400001 | Failed to run, please try again. |
| 1008400002 | The service is abnormal. |

**示例：**

```
1. import { faceComparator } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. async function faceCompareTest() {
9. let chooseImage: PixelMap | undefined = undefined;
10. let chooseImage1: PixelMap | undefined = undefined;

12. // 从图库中选择两张图片
13. let PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
14. PhotoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
15. PhotoSelectOptions.maxSelectNumber = 2;
16. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
17. let PhotoSelectResult = await photoPicker.select(PhotoSelectOptions);
18. let uris = PhotoSelectResult.photoUris;

20. if (uris.length !== 2) {
21. hilog.info(0x0000, 'testTag', 'selected uris length is not 2');
22. return;
23. }

25. // 将选择的图片转换为PixelMap
26. let fileSource = await fileIo.open(uris[0], fileIo.OpenMode.READ_ONLY);
27. let imageSource = image.createImageSource(fileSource.fd);
28. chooseImage = await imageSource.createPixelMap();

30. fileSource = await fileIo.open(uris[1], fileIo.OpenMode.READ_ONLY);
31. imageSource = image.createImageSource(fileSource.fd);
32. chooseImage1 = await imageSource.createPixelMap();

34. if (!chooseImage || !chooseImage1) {
35. hilog.info(0x0000, 'testTag', 'chooseImage or chooseImage1 is undefined');
36. return;
37. }

39. // 调用人脸比对接口
40. let visionInfo: faceComparator.VisionInfo = {
41. pixelMap: chooseImage
42. };
43. let visionInfo1: faceComparator.VisionInfo = {
44. pixelMap: chooseImage1
45. };

47. let data: faceComparator.FaceCompareResult = await faceComparator.compareFaces(visionInfo, visionInfo1);
48. let similarity = (data.similarity * 100).toFixed(2);
49. let isSamePerson = data.isSamePerson ? 'is' : 'is not';
50. let faceString = `Similarity: ${similarity}%. ${isSamePerson} the same person`;
51. hilog.info(0x0000, 'testTag', 'faceString data is ' + faceString);

53. // 释放资源
54. if (chooseImage && chooseImage1) {
55. void chooseImage.release();
56. chooseImage1.release();
57. }
58. if (fileSource) {
59. try {
60. await fileIo.close(fileSource);
61. } catch (err) {
62. hilog.error(0x0000, 'testTag', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
63. }
64. }
65. }

67. @Entry
68. @Component
69. struct Page {

71. build() {
72. Column(){
73. Button('faceCompareTest').onClick(() => {
74. faceCompareTest().catch((err: BusinessError) => {
75. hilog.error(0x0000, 'faceCompareSample', `Failed to compare faces. Code: ${err.code}, message: ${err.message}`);
76. });
77. })
78. }
79. }
80. }
```
