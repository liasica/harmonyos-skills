---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-face-detector-api
title: faceDetector（人脸检测）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > faceDetector（人脸检测）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f4cefa6d46e10a3ac3c94091947a17cfa82bd064b15ef6c77d03111b573704d2
---

人脸检测支持2D人脸检测框的检测能力。检测给定图片中的人脸数量、人脸位置、特征点（左右眼中心、鼻子、左右嘴角）和姿态（pitch、roll、yaw）信息。人脸检测框按照大小排序。

与[Vision Kit](vision-api.md)的活体检测的区别是：活体检测用于视频，人脸检测用于图片。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { faceDetector } from '@kit.CoreVisionKit';
```

## VisionInfo

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的[PixelMap](arkts-apis-image-pixelmap.md)类型的视觉信息。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 待识别的图片。对于图片的要求请参见[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## FaceRecognitionConfiguration

人脸遮挡检测的配置项。如果配置在初始化和检测期间指定，将启用额外的检测功能。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| faceBlock | boolean | 是 | 否 | 是否开启人脸遮挡检测。  true：开启人脸遮挡检测；false：不开启人脸遮挡检测。默认为false。 |

## FaceBlock

人脸遮挡检测结果的枚举类。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNINITIALIZED | -1 | 人脸遮挡检测未开启。 |
| UNBLOCKED | 0 | 人脸无遮挡。 |
| BLOCKED | 1 | 人脸有遮挡。 |

## FacePoint

指示像素点的位置。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 是 | 否 | 像素点横向x坐标。 |
| y | number | 是 | 否 | 像素点纵向y坐标。 |

## FacePose

描述人脸在三维空间中的方向。坐标系可参考[世界坐标系](../harmonyos-guides/core-vision-face-detector.md#世界坐标系)。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| yaw | number | 是 | 否 | 头型航向，将物体绕Y轴旋转（localRotationY）。取值范围[-180,180]。 |
| pitch | number | 是 | 否 | 头型俯仰，将物体绕X轴旋转（localRotationX）。取值范围[-180,180]。 |
| roll | number | 是 | 否 | 头型横滚，将物体绕Z轴旋转（localRotationZ）。取值范围[-180,180]。 |

## FaceRectangle

表示人脸的矩形框。描述人脸矩形框的位置和大小，包括左上角坐标、宽度和高度。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 是 | 否 | 人脸矩形框左上角x坐标。 |
| top | number | 是 | 否 | 人脸矩形框左上角y坐标。 |
| width | number | 是 | 否 | 人脸框宽，单位：px。 |
| height | number | 是 | 否 | 人脸框高，单位：px。 |

## Face

表示人脸检测的结果信息，包括人脸数量、坐标信息、人脸姿态和检测结果置信度。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| probability | number | 是 | 否 | 表示人脸检测结果的置信度，取值范围为0~1的浮点数，数值越大代表置信度越高。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| block | [FaceBlock](core-vision-face-detector-api.md#faceblock) | 是 | 是 | 人脸遮挡结果。默认值为FaceBlock.UNINITIALIZED，表示未开启人脸遮挡检测；若初始化时通过[FaceRecognitionConfiguration](core-vision-face-detector-api.md#facerecognitionconfiguration)将faceBlock设置为true开启了遮挡检测，则返回FaceBlock.UNBLOCKED（无遮挡）或FaceBlock.BLOCKED（有遮挡）。  **起始版本**：5.0.2(14)。 |
| pose | [FacePose](core-vision-face-detector-api.md#facepose) | 是 | 否 | 人脸头型航向。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| rect | [FaceRectangle](core-vision-face-detector-api.md#facerectangle) | 是 | 否 | 人脸框列表。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| points | Array<[FacePoint](core-vision-face-detector-api.md#facepoint)> | 是 | 否 | 人脸五官位置数组，包括：左右眼中心、鼻子、左右嘴角。参数顺序为：左眼中心，右眼中心，鼻子，左嘴角，右嘴角。  **元服务API**：从版本5.0.2(14)开始，该接口支持在元服务中使用。 |

## faceDetector.init

init(): Promise<boolean>

初始化人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```typescript
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // 初始化人脸检测服务
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
    }
  }
}
```

## faceDetector.init

init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>

初始化人脸遮挡检测分析器服务。同一个进程内只要有人脸检测服务开启了遮挡检测，在该人脸检测服务未release这段时间内，这个进程内的其他所有人脸检测服务都等同于开启了遮挡检测。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```typescript
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  let config: faceDetector.FaceRecognitionConfiguration = {
    faceBlock: true
  };
  // 初始化人脸遮挡检测服务
  const initResult = await faceDetector.init(config);
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
    }
  }
}
```

## faceDetector.release

release(): Promise<void>

释放人脸检测分析器服务。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```typescript
import { faceDetector } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseFaceDetector() {
  // 初始化人脸检测服务
  const initResult = await faceDetector.init();
  hilog.info(0x0000, 'faceDetectorSample', `Face detector initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector initialized successfully');

    // 这里可以添加使用人脸检测服务的代码

    // 使用完毕后，释放人脸检测服务
    await faceDetector.release();
    hilog.info(0x0000, 'faceDetectorSample', 'Face detector released successfully');
  } else {
    hilog.error(0x0000, 'faceDetectorSample', 'Failed to initialize face detector');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseFaceDetector').onClick(() => {
        // 调用函数
        void initAndReleaseFaceDetector();
      })
    }
  }
}
```

## faceDetector.detect

detect(visionInfo: VisionInfo): Promise<Array<Face>>

检测一张图片中的人脸信息，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Face.Detector

**模型约束：** 此接口仅可在Stage模型下使用。

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

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1008800001 | Failed to run face detector, please try again. |
| 1008800002 | The face detector service is abnormal. |

**示例：**

```typescript
import { faceDetector } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function faceDetectTest() {
  let imageSource: image.ImageSource | undefined = undefined;
  let chooseImage: PixelMap | undefined = undefined;

  // 通过图库选择一张图片
  let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  photoSelectOptions.maxSelectNumber = 1;
  let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let photoSelectResult = await photoPicker.select(photoSelectOptions);
  let uri = photoSelectResult.photoUris[0];
  if (uri === undefined) {
    hilog.info(0x0000, 'faceDetectorSample', 'uri is undefined');
    return;
  }

  // 将图片转换为PixelMap
  let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
  imageSource = image.createImageSource(file.fd);
  chooseImage = await imageSource.createPixelMap();
  hilog.info(0x0000, 'faceDetectorSample', 'chooseImage:', chooseImage);
  if (!chooseImage) {
    return;
  }

  // 调用人脸检测接口
  let visionInfo: faceDetector.VisionInfo = {
    pixelMap: chooseImage
  };
  let data: faceDetector.Face[] = await faceDetector.detect(visionInfo);
  if (data.length === 0) {
    hilog.info(0x0000, 'faceDetectorSample', 'No face is detected in the image.');
  } else {
    let faceString = JSON.stringify(data);
    hilog.info(0x0000, 'faceDetectorSample', 'faceString data is ' + faceString);
  }

  // 释放资源
  if (chooseImage && imageSource) {
    void chooseImage.release();
    void imageSource.release();
  }
  if (file) {
    await fileIo.close(file);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('faceDetectTest').onClick(() => {
        // 调用函数
        void faceDetectTest();
      })
    }
  }
}
```
