---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-object-detection-api
title: objectDetection（多目标识别）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > objectDetection（多目标识别）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11fea0964fc0b4e917a3158f548ac0df72e4cc89fb7bf6615317a044cc44b3b6
---

多目标识别服务提供了从图像中识别多个目标的能力。通过拍照、录像等光学输入方式，把各种场景下的图像转化为数字图像信息，再利用AI底层能力对图像进行分析，从中定位并识别出多个感兴趣的目标对象，如人脸、动物、植物等，便于用户提取目标的类别、边框位置、置信度等信息。

目前本服务支持识别的目标类型包括：风景，动物，植物，建筑，人脸，表格，文本，人头，猫头，狗头，食物，汽车，人体，文档，卡证。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { visionBase, objectDetection } from '@kit.CoreVisionKit';
```

## VisionObject

PhonePC/2in1Tablet

视觉信息对象。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| boundingBox | visionBase.[BoundingBox](core-vision-vision-base-api.md#boundingbox) | 否 | 否 | visionObject的边界框。 |
| score | number | 否 | 否 | visionObject的置信度。范围为(0,1)。0表示置信度最低，1表示置信度最高。置信度越高，说明这个点的位置越可靠。 |
| labels | Array<number> | 否 | 否 | 识别物体的类型标签。  0：风景。  1：动物。  2：植物。  3：建筑。  5：人脸。  6：表格。  7：文本。  8：人头。  9：猫头。  10：狗头。  11：食物。  12：汽车。  13：人体。  21：文档。  22：卡证。 |
| id | number | 否 | 否 | visionObject的唯一标识符。ID为从0开始递增的整数编号。 |

## ObjectDetectionResponse

PhonePC/2in1Tablet

多目标检测的结果类。继承自visionBase基类的[Response](core-vision-vision-base-api.md#response)。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| objects | Array<[VisionObject](core-vision-object-detection-api.md#visionobject)> | 否 | 否 | 多目标检测结果。可以是单个对象或多个对象的数组。 |

## ObjectDetector

PhonePC/2in1Tablet

定义多目标识别的接口和基本结构。继承自[visionBase.Analyzer](core-vision-vision-base-api.md#analyzer)类。它有以下功能函数：

* private constructor()：这是一个私有构造函数，意味着不能直接通过new关键字实例化ObjectDetector，必须通过 create() 静态方法来创建实例。
* static create(): Promise<ObjectDetector>：这是一个静态方法，用于创建 ObjectDetector 的实例。使用Promise异步回调。
* process(request: visionBase.Request): Promise<ObjectDetectionResponse>：这是一个实例方法，用于处理多目标识别请求。使用Promise异步回调。
* destroy(): Promise<void>：这是一个实例方法，用于销毁多目标识别的进程。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

| 名称 | 说明 |
| --- | --- |
| constructor | 强制开发者必须使用static create()方法来创建ObjectDetector的实例。 |
| create | 初始化多目标识别接口。 |
| process | 多目标识别的实际执行接口。 |
| destroy | 多目标识别进程的销毁接口。 |

### create

PhonePC/2in1Tablet

static create(): Promise<ObjectDetector>

多目标识别的初始化接口。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ObjectDetector](core-vision-object-detection-api.md#objectdetector)> | Promise对象，返回ObjectDetector实例。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1011000001 | Failed to run, please try again. |
| 1011000002 | The service is abnormal. |

**示例：**

```
1. import { objectDetection } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function createAndDestroyDetector() {
5. const detector = await objectDetection.ObjectDetector.create();
6. if (detector) {
7. hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
8. } else {
9. hilog.error(0x0000,'objectDetectionSample','Failed to create object detector');
10. return;
11. }
12. // 使用 detector 进行一些操作
13. // ...

15. // 完成后销毁 detector
16. if (detector) {
17. await detector.destroy();
18. hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
19. } else {
20. hilog.error(0x0000,'objectDetectionSample','Failed to destroy object detector');
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

销毁多目标识别的进程。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { objectDetection } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function createAndDestroyDetector() {
5. const detector = await objectDetection.ObjectDetector.create();
6. if (detector) {
7. hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
8. } else {
9. hilog.error(0x0000,'objectDetectionSample','Failed to create object detector');
10. return;
11. }
12. // 使用 detector 进行一些操作
13. // ...

15. // 完成后销毁 detector
16. if (detector) {
17. await detector.destroy();
18. hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
19. } else {
20. hilog.error(0x0000,'objectDetectionSample','Failed to destroy object detector');
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

process(request: visionBase.Request): Promise<ObjectDetectionResponse>

创建多目标识别实例并执行多目标识别。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.ObjectDetection

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | visionBase.[Request](core-vision-vision-base-api.md#request) | 是 | 图片实例。多目标识别接口仅支持传入一张图片，不支持传入多张图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ObjectDetectionResponse](core-vision-object-detection-api.md#objectdetectionresponse)> | 返回多目标识别的结果。 |

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
1. import { objectDetection, visionBase } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: image.PixelMap | undefined = undefined;

11. // 创建对象检测器
12. let detector: objectDetection.ObjectDetector | undefined = undefined;

14. async function createDetector() {
15. detector = await objectDetection.ObjectDetector.create();
16. hilog.info(0x0000, 'objectDetectionSample', 'Object detector created successfully');
17. }

19. @Entry
20. @Component
21. struct Page {

23. build() {
24. Column(){
25. Button('Start').onClick(() => {
26. // 将图片转换为PixelMap，可以通过图库获取
27. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
28. photoPicker.select({
29. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
30. maxSelectNumber: 1
31. }).then((res: photoAccessHelper.PhotoSelectResult) => {
32. let uri = res.photoUris[0];
33. if (uri === undefined) {
34. hilog.info(0x0000, 'objectDetectionSample', 'uri is undefined');
35. return
36. }
37. setTimeout(async () => {
38. let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
39. imageSource = image.createImageSource(file.fd);
40. chooseImage = await imageSource.createPixelMap();
41. hilog.info(0x0000, 'objectDetectionSample', 'chooseImage:', chooseImage);
42. if (!chooseImage) {
43. return
44. }

46. // 创建检测器
47. await createDetector();

49. if (!detector) {
50. hilog.error(0x0000, 'objectDetectionSample', 'Detector is not initialized');
51. return;
52. }

54. // 调用对象检测接口
55. let request: visionBase.Request = {
56. inputData: { pixelMap: chooseImage },
57. scene: visionBase.SceneMode.FOREGROUND
58. };

60. let response: objectDetection.ObjectDetectionResponse = await detector.process(request);

62. if (response.objects.length === 0) {
63. hilog.info(0x0000, 'objectDetectionSample', 'No objects detected in the image.');
64. } else {
65. let objectString = JSON.stringify(response.objects);
66. hilog.info(0x0000, 'objectDetectionSample', 'Detected objects: ' + objectString);
67. }

69. // 清理资源
70. if (chooseImage && imageSource) {
71. void chooseImage.release();
72. void imageSource.release();
73. }
74. if (file) {
75. try {
76. await fileIo.close(file);
77. } catch (err) {
78. hilog.error(0x0000, 'objectDetectionSample', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
79. }
80. }
81. if (detector) {
82. await detector.destroy();
83. hilog.info(0x0000, 'objectDetectionSample', 'Object detector destroyed successfully');
84. }
85. }, 100);
86. }).catch((err: BusinessError) => {
87. hilog.error(0x0000, 'objectDetectionSample', `Failed to get photo image uri. Code: ${err.code}, message: ${err.message}`);
88. });
89. })
90. }
91. }
92. }
```
