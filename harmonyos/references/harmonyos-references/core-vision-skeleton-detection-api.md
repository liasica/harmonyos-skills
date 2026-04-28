---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-skeleton-detection-api
title: skeletonDetection（骨骼点检测）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > skeletonDetection（骨骼点检测）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9ce50662c823598b8270d6140600c3bd8a21ebdd11c18fe5f75257429ae9f21
---

骨骼点检测可以从图像中检测出人体的关键骨骼点，如头部、肩部、手肘、手腕、髋部、膝盖、脚踝等，并给出它们的位置坐标和置信度。同时，骨骼点检测是一项底层的AI能力，还可以与Core Vision Kit中其他AI能力如人脸识别、文字识别等组合使用，开发出更加智能化的应用。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { visionBase, skeletonDetection } from '@kit.CoreVisionKit';
```

## SkeletonPointType

PhonePC/2in1Tablet

骨骼点类型的枚举类。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NOSE | 0 | 鼻子。 |
| LEFT\_EYE | 1 | 左眼。 |
| RIGHT\_EYE | 2 | 右眼。 |
| LEFT\_EAR | 3 | 左耳。 |
| RIGHT\_EAR | 4 | 右耳。 |
| LEFT\_SHOULDER | 5 | 左肩。 |
| RIGHT\_SHOULDER | 6 | 右肩。 |
| LEFT\_ELBOW | 7 | 左肘。 |
| RIGHT\_ELBOW | 8 | 右肘。 |
| LEFT\_WRIST | 9 | 左腕。 |
| RIGHT\_WRIST | 10 | 右腕。 |
| LEFT\_HIP | 11 | 左髋。 |
| RIGHT\_HIP | 12 | 右髋。 |
| LEFT\_KNEE | 13 | 左膝。 |
| RIGHT\_KNEE | 14 | 右膝。 |
| LEFT\_ANKLE | 15 | 左脚踝。 |
| RIGHT\_ANKLE | 16 | 右脚踝。 |

## SkeletonPoint

PhonePC/2in1Tablet

详细的骨骼点信息。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| point | visionBase.[Point](core-vision-vision-base-api.md#point) | 否 | 否 | 骨骼点的图像坐标，即它在图像中的x和y位置。 |
| score | number | 否 | 否 | 骨骼点的置信度。取值范围是(0,1)。0表示置信度最低，1表示置信度最高，置信度越高，说明这个点的位置越可靠。 |
| type | [SkeletonPointType](core-vision-skeleton-detection-api.md#skeletonpointtype) | 否 | 否 | 骨骼点的类型，即它在人体骨骼模型中的位置。 |

## Skeleton

PhonePC/2in1Tablet

用于描述一个完整的人体骨骼检测结果。包括总体置信度和人体在图像中的大致位置，还详细列出了各个关键点的位置和类型。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| boundingBox | visionBase.[BoundingBox](core-vision-vision-base-api.md#boundingbox) | 否 | 否 | 骨骼的边界框，也就是所有骨骼点加一起的矩形框。 |
| score | number | 否 | 否 | 表示骨骼点的总体置信度,取值范围是(0,1)，0表示置信度最低，1表示置信度最高。反映了这个骨骼整体的可信程度。 |
| points | Array<[SkeletonPoint](core-vision-skeleton-detection-api.md#skeletonpoint)> | 否 | 否 | 返回包含骨骼点详情的对象数组。 |

## SkeletonDetectionResponse

PhonePC/2in1Tablet

用于表示一次骨骼点检测的完整结果。作为骨骼点检测的顶层输出，封装了一次检测的全部结果。继承自visionBase的[Response](core-vision-vision-base-api.md#response)。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| skeletons | Array<[Skeleton](core-vision-skeleton-detection-api.md#skeleton)> | 否 | 否 | 包含图片内所有人的人体骨骼点结果集合。 |

## SkeletonDetector

PhonePC/2in1Tablet

定义骨骼点检测的接口和基本结构。继承自[visionBase.Analyzer](core-vision-vision-base-api.md#analyzer)类。它有以下功能函数：

* private constructor()：这是一个私有构造函数，意味着不能直接通过 new 关键字实例化SkeletonDetector。必须通过 create() 静态方法来创建实例。
* static create(): Promise<SkeletonDetector>：这是一个静态方法，用于创建SkeletonDetector的实例。使用Promise异步回调。
* process(request: visionBase.Request): Promise<SkeletonDetectionResponse>：这是一个实例方法，用于处理骨骼点检测请求。使用Promise异步回调。
* destroy(): Promise<void>：这是一个实例方法，用于销毁骨骼点检测的进程，使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

| 名称 | 说明 |
| --- | --- |
| constructor | 强制开发者必须使用static create()方法来创建SkeletonDetector的实例。 |
| create | 初始化骨骼点检测接口。 |
| process | 骨骼点检测的实际执行接口。 |
| destroy | 骨骼点检测的销毁接口。 |

### create

PhonePC/2in1Tablet

static create(): Promise<SkeletonDetector>

骨骼点检测的初始化接口。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkeletonDetector](core-vision-skeleton-detection-api.md#skeletondetector)> | Promise对象，返回[SkeletonDetector](core-vision-skeleton-detection-api.md#skeletondetector)实例。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1011000001 | Failed to run, please try again. |
| 1011000002 | The service is abnormal. |

**示例：**

```
1. import { skeletonDetection } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function createAndDestroyDetector() {
5. const detector = await skeletonDetection.SkeletonDetector.create();
6. if (detector) {
7. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
8. } else {
9. hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
10. return;
11. }
12. // 使用 detector 进行一些操作
13. // ...

15. // 完成后销毁 detector
16. if (detector) {
17. await detector.destroy();
18. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
19. } else {
20. hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
21. }
22. }

24. @Entry
25. @Component
26. struct Page {

28. build() {
29. Column(){
30. Button('createAndDestroyDetector').onClick(() => {
31. createAndDestroyDetector()
32. })
33. }
34. }
35. }
```

### destroy

PhonePC/2in1Tablet

destroy(): Promise<void>

销毁骨骼点检测能力。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { skeletonDetection } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function createAndDestroyDetector() {
5. const detector = await skeletonDetection.SkeletonDetector.create();
6. if (detector) {
7. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
8. } else {
9. hilog.error(0x0000,'skeletonDetectionSample','Failed to create Skeleton detector');
10. return;
11. }
12. // 使用 detector 进行一些操作
13. // ...

15. // 完成后销毁 detector
16. if (detector) {
17. await detector.destroy();
18. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
19. } else {
20. hilog.error(0x0000,'skeletonDetectionSample','Failed to destroy Skeleton detector');
21. }
22. }

24. @Entry
25. @Component
26. struct Page {

28. build() {
29. Column(){
30. Button('createAndDestroyDetector').onClick(() => {
31. createAndDestroyDetector()
32. })
33. }
34. }
35. }
```

### process

PhonePC/2in1Tablet

process(request: visionBase.Request): Promise<SkeletonDetectionResponse>

创建骨骼点检测实例并执行骨骼点检测。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | visionBase.[Request](core-vision-vision-base-api.md#request) | 是 | 图片实例。骨骼点检测接口仅支持传入一张图片，不支持传入多张图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkeletonDetectionResponse](core-vision-skeleton-detection-api.md#skeletondetectionresponse)> | 返回骨骼点识别的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1011000001 | Failed to run, please try again. |
| 1011000003 | Failed to run the model, please try again. |
| 1011000004 | Running the model timed out. Try again later. |

**示例：**

```
1. import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: image.PixelMap | undefined = undefined;

11. // 创建骨骼检测器
12. let detector: skeletonDetection.SkeletonDetector | undefined = undefined;

14. async function createDetector() {
15. detector = await skeletonDetection.SkeletonDetector.create();
16. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
17. }

19. @Entry
20. @Component
21. struct Page {

23. build() {
24. Column(){
25. Button('Button').onClick(() => {
26. // 将图片转换为PixelMap，可以通过图库获取
27. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
28. photoPicker.select({
29. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
30. maxSelectNumber: 1
31. }).then((res: photoAccessHelper.PhotoSelectResult) => {
32. let uri = res.photoUris[0];
33. if (uri === undefined) {
34. hilog.info(0x0000, 'skeletonDetectionSample', 'uri is undefined');
35. return
36. }
37. setTimeout(async () => {
38. let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
39. imageSource = image.createImageSource(file.fd);
40. chooseImage = await imageSource.createPixelMap();
41. hilog.info(0x0000, 'skeletonDetectionSample', 'chooseImage:', chooseImage);
42. if (!chooseImage) {
43. return
44. }

46. // 创建检测器
47. await createDetector();

49. if (!detector) {
50. hilog.error(0x0000, 'skeletonDetectionSample', 'Detector is not initialized');
51. return;
52. }

54. // 调用骨骼检测接口
55. let request: visionBase.Request = {
56. inputData: { pixelMap: chooseImage },
57. scene: visionBase.SceneMode.FOREGROUND
58. };

60. let response: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);

62. if (response.skeletons.length === 0) {
63. hilog.info(0x0000, 'skeletonDetectionSample', 'No skeletons detected in the image.');
64. } else {
65. hilog.info(0x0000, 'skeletonDetectionSample', `Detected ${response.skeletons.length} skeletons.`);
66. response.skeletons.forEach((skeleton, index) => {
67. hilog.info(0x0000, 'skeletonDetectionSample', `  Score: ${skeleton.score}`);
68. hilog.info(0x0000, 'skeletonDetectionSample', `  Number of points: ${skeleton.points.length}`);
69. skeleton.points.forEach(point => {
70. hilog.info(0x0000, 'skeletonDetectionSample', `    ${skeletonDetection.SkeletonPointType[point.type]}: (${point.point.x}, ${point.point.y}), Score: ${point.score}`);
71. });
72. });
73. }

75. // 清理资源
76. if (chooseImage && imageSource) {
77. void chooseImage.release();
78. void imageSource.release();
79. }
80. if (file) {
81. try {
82. await fileIo.close(file);
83. } catch (err) {
84. hilog.error(0x0000, 'skeletonDetectionSample', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
85. }
86. }
87. if (detector) {
88. await detector.destroy();
89. hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
90. }
91. }, 100);
92. }).catch((err: BusinessError) => {
93. hilog.error(0x0000, 'skeletonDetectionSample', `Failed to get photo image uri. Code: ${err.code}, message: ${err.message}`);
94. });
95. })
96. }
97. }
98. }
```
