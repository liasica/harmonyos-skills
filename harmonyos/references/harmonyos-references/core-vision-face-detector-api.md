---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-face-detector-api
title: faceDetector（人脸检测）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > faceDetector（人脸检测）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9c9c32bdc8232d6750dba9a3766ff310e37468f38c588acdd4e6cc78ea0cc34
---

人脸检测支持2D人脸检测框的检测能力。检测给定图片中的人脸数量、人脸位置、特征点（左右眼中心、鼻子、左右嘴角）和姿态（pitch、roll、yaw）信息。人脸检测框按照大小排序。

与Vision Kit的活体检测的区别是：活体检测用于视频，人脸检测用于图片。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { faceDetector } from '@kit.CoreVisionKit';
```

## VisionInfo

PhonePC/2in1Tablet

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的PixelMap类型的视觉信息。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 待识别的图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## FaceRecognitionConfiguration

PhonePC/2in1Tablet

人脸遮挡检测的配置项。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| faceBlock | boolean | 是 | 否 | 是否开启人脸遮挡检测。  true：开启人脸遮挡检测；false：不开启人脸遮挡检测。默认为false。 |

## FaceBlock

PhonePC/2in1Tablet

人脸遮挡检测结果的枚举类。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | -1 | 人脸遮挡检测未开启。 |
| UNBLOCKED | 0 | 人脸无遮挡。 |
| BLOCKED | 1 | 人脸有遮挡。 |

## FacePoint

PhonePC/2in1Tablet

指示像素点的位置。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 是 | 否 | 像素点横向x坐标。 |
| y | number | 是 | 否 | 像素点纵向y坐标。 |

## FacePose

PhonePC/2in1Tablet

描述人脸在三维空间中的方向。坐标系可参考[世界坐标系](../harmonyos-guides/core-vision-face-detector.md#世界坐标系)。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| yaw | number | 是 | 否 | 头型航向，将物体绕Y轴旋转（localRotationY）。取值范围[-180,180]。 |
| pitch | number | 是 | 否 | 头型俯仰，将物体绕X轴旋转（localRotationX）。取值范围[-180,180]。 |
| roll | number | 是 | 否 | 头型横滚，将物体绕Z轴旋转（localRotationZ）。取值范围[-180,180]。 |

## FaceRectangle

PhonePC/2in1Tablet

表示人脸的矩形框。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 是 | 否 | 人脸矩形框左上角x坐标。 |
| top | number | 是 | 否 | 人脸矩形框左上角y坐标。 |
| width | number | 是 | 否 | 人脸框宽，单位：pixel。 |
| height | number | 是 | 否 | 人脸框高，单位：pixel。 |

## Face

PhonePC/2in1Tablet

表示人脸的信息列表。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| probability | number | 是 | 否 | 表示人脸检测结果的置信度，取值范围为(0,1)的浮点数，数值越大代表置信度越高。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| block | [FaceBlock](core-vision-face-detector-api.md#faceblock) | 是 | 是 | 人脸遮挡结果。  **起始版本**：5.0.2(14)。 |
| pose | [FacePose](core-vision-face-detector-api.md#facepose) | 是 | 否 | 人脸头型航向。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| rect | [FaceRectangle](core-vision-face-detector-api.md#facerectangle) | 是 | 否 | 人脸框列表。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| points | Array<[FacePoint](core-vision-face-detector-api.md#facepoint)> | 是 | 否 | 人脸五官位置数组，包括：左右眼中心、鼻子、左右嘴角。参数顺序为：左眼中心，右眼中心，鼻子，左嘴角，右嘴角。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |

## faceDetector.init

PhonePC/2in1Tablet

init(): Promise<boolean>

初始化人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseFaceDetector() {
5. // 初始化人脸检测服务
6. const initResult = await faceDetector.init();
7. hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

12. // 这里可以添加使用人脸检测服务的代码

14. // 使用完毕后，释放人脸检测服务
15. await faceDetector.release();
16. hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
17. } else {
18. hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseFaceDetector').onClick(() => {
29. // 调用函数
30. void initAndReleaseFaceDetector();
31. })
32. }
33. }
34. }
```

## faceDetector.init

PhonePC/2in1Tablet

init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>

初始化人脸遮挡检测分析器服务。同一个进程内只要有人脸检测服务开启了遮挡检测，在该人脸检测服务未release这段时间内，这个进程内的其他所有人脸检测服务都等同于开启了遮挡检测。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faceRecognitionConfiguration | [FaceRecognitionConfiguration](core-vision-face-detector-api.md#facerecognitionconfiguration) | 是 | 人脸遮挡检测配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseFaceDetector() {
5. let config: faceDetector.FaceRecognitionConfiguration = {
6. faceBlock: true
7. }
8. // 初始化人脸遮挡检测服务
9. const initResult = await faceDetector.init(config);
10. hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

12. if (initResult) {
13. hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

15. // 这里可以添加使用人脸检测服务的代码

17. // 使用完毕后，释放人脸检测服务
18. await faceDetector.release();
19. hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
20. } else {
21. hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
22. }
23. }

25. @Entry
26. @Component
27. struct Page {

29. build() {
30. Column(){
31. Button('initAndReleaseFaceDetector').onClick(() => {
32. // 调用函数
33. void initAndReleaseFaceDetector();
34. })
35. }
36. }
37. }
```

## faceDetector.release

PhonePC/2in1Tablet

release(): Promise<void>

释放人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，释放接口无返回值。 |

**示例：**

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseFaceDetector() {
5. // 初始化人脸检测服务
6. const initResult = await faceDetector.init();
7. hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

12. // 这里可以添加使用人脸检测服务的代码

14. // 使用完毕后，释放人脸检测服务
15. await faceDetector.release();
16. hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
17. } else {
18. hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
19. }
20. }

22. @Entry
23. @Component
24. struct Page {

26. build() {
27. Column(){
28. Button('initAndReleaseFaceDetector').onClick(() => {
29. // 调用函数
30. void initAndReleaseFaceDetector();
31. })
32. }
33. }
34. }
```

## faceDetector.detect

PhonePC/2in1Tablet

detect(visionInfo: VisionInfo): Promise<Array<Face>>

检测一张图片中的人脸信息，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-face-detector-api.md#visioninfo) | 是 | 图片实例（包含人脸）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Face](core-vision-face-detector-api.md#face)>> | Promise对象，返回人脸检测的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1008800001 | Failed to run, please try again. |
| 1008800002 | The service is abnormal. |

**示例：**

```
1. import { faceDetector } from '@kit.CoreVisionKit';
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: PixelMap | undefined = undefined;

11. // 将图片转换为PixelMap，可以通过图库获取
12. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
13. photoPicker.select({
14. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
15. maxSelectNumber: 1
16. }).then((res: photoAccessHelper.PhotoSelectResult) => {
17. let uri = res.photoUris[0];
18. if (uri === undefined) {
19. hilog.info(0x0000, 'faceDetectorSample', 'uri is undefined');
20. return
21. }
22. setTimeout(async () => {
23. let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
24. imageSource = image.createImageSource(file.fd);
25. chooseImage = await imageSource.createPixelMap();
26. hilog.info(0x0000, 'faceDetectorSample', 'chooseImage:', chooseImage);
27. if (!chooseImage) {
28. return
29. }
30. // 调用人脸检测接口
31. let visionInfo: faceDetector.VisionInfo = {
32. pixelMap: chooseImage
33. };
34. let data: faceDetector.Face[] = await faceDetector.detect(visionInfo);
35. if (data.length === 0) {
36. hilog.info(0x0000, 'faceDetectorSample', 'No face is detected in the image.');
37. } else {
38. let faceString = JSON.stringify(data);
39. hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
40. }

42. if (chooseImage && imageSource) {
43. void chooseImage.release();
44. void imageSource.release();
45. }
46. if (file) {
47. try {
48. await fileIo.close(file);
49. } catch (err) {
50. hilog.error(0x0000, 'faceDetectorSample', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
51. }
52. }
53. }, 100);
54. }).catch((err: BusinessError) => {
55. hilog.error(0x0000, 'faceDetectorSample', `Failed to get photo image uri. code: ${err.code}, message: ${err.message}`);
56. });

58. @Entry
59. @Component
60. struct Page {

62. build() {
63. Column(){
64. }
65. }
66. }
```
