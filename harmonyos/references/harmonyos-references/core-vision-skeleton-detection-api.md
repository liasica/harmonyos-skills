---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-skeleton-detection-api
title: skeletonDetection（骨骼点检测）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > skeletonDetection（骨骼点检测）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f780614dd4fef86b2ce1aea416ef4306213621ae7d466228ebd2771d12edebf2
---

骨骼点检测可以从图像中检测出人体的关键骨骼点，如头部、肩部、手肘、手腕、髋部、膝盖、脚踝等，并给出它们的位置坐标和置信度。同时，骨骼点检测是一项底层的AI能力，还可以与Core Vision Kit中其他AI能力如人脸识别、文字识别等组合使用，开发出更加智能化的应用。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { visionBase, skeletonDetection } from '@kit.CoreVisionKit';
```

## SkeletonPointType

骨骼点类型的枚举类。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

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

详细的骨骼点信息。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| point | visionBase.[Point](core-vision-vision-base-api.md#point) | 否 | 否 | 骨骼点的图像坐标，即它在图像中的x和y位置。 |
| score | number | 否 | 否 | 骨骼点的置信度。取值范围是0~1，0表示置信度最低，1表示置信度最高，置信度越高，说明这个点的位置越可靠。 |
| type | [SkeletonPointType](core-vision-skeleton-detection-api.md#skeletonpointtype) | 否 | 否 | 骨骼点的类型，即它在人体骨骼模型中的位置。 |

## Skeleton

用于描述一个完整的人体骨骼检测结果。包括总体置信度和人体在图像中的大致位置，还详细列出了各个关键点的位置和类型。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| boundingBox | visionBase.[BoundingBox](core-vision-vision-base-api.md#boundingbox) | 否 | 否 | 骨骼的边界框，也就是所有骨骼点加一起的矩形框。 |
| score | number | 否 | 否 | 反映了这个骨骼整体的可信程度，取值范围是0~1，0表示置信度最低，1表示置信度最高。 |
| points | Array<[SkeletonPoint](core-vision-skeleton-detection-api.md#skeletonpoint)> | 否 | 否 | 返回包含骨骼点详情的对象数组。 |

## SkeletonDetectionResponse

用于表示一次骨骼点检测的完整结果。作为骨骼点检测的顶层输出，封装了一次检测的全部结果。继承自visionBase的[Response](core-vision-vision-base-api.md#response)。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| skeletons | Array<[Skeleton](core-vision-skeleton-detection-api.md#skeleton)> | 否 | 否 | 包含图片内所有人的人体骨骼点结果集合。 |

## SkeletonDetector

定义骨骼点检测的接口和基本结构。继承自[visionBase.Analyzer](core-vision-vision-base-api.md#analyzer)类。它有以下功能函数：

* constructor()：私有构造函数，不能直接通过new关键字实例化SkeletonDetector，必须通过create()静态方法来创建实例。
* create(): Promise<SkeletonDetector>：静态方法，用于创建SkeletonDetector的实例。使用Promise异步回调。
* process(request: visionBase.Request): Promise<SkeletonDetectionResponse>：实例方法，用于处理骨骼点检测请求。使用Promise异步回调。
* destroy(): Promise<void>：实例方法，用于销毁骨骼点检测进程，使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

### create

static create(): Promise<SkeletonDetector>

骨骼点检测的初始化接口。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkeletonDetector](core-vision-skeleton-detection-api.md#skeletondetector)> | Promise对象，返回SkeletonDetector实例，用于执行骨骼点检测。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1011000001 | Failed to run, please try again. |
| 1011000002 | The service is abnormal. |

**示例：**

```typescript
import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  try {
    const detector = await skeletonDetection.SkeletonDetector.create();
    if (detector) {
      hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
    } else {
      hilog.error(0x0000, 'skeletonDetectionSample', 'Failed to create Skeleton detector');
      return;
    }
    // 使用 detector 进行一些操作
    // ...

    // 完成后销毁 detector
    if (detector) {
      await detector.destroy();
      hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
    } else {
      hilog.error(0x0000, 'skeletonDetectionSample', 'Failed to destroy Skeleton detector');
    }
  } catch (err) {
    hilog.error(0x0000, 'skeletonDetectionSample', `Skeleton detector error: ${err}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        void createAndDestroyDetector();
      })
    }
  }
}
```

### destroy

destroy(): Promise<void>

销毁骨骼点检测能力。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { skeletonDetection } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function createAndDestroyDetector() {
  try {
    const detector = await skeletonDetection.SkeletonDetector.create();
    if (detector) {
      hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');
    } else {
      hilog.error(0x0000, 'skeletonDetectionSample', 'Failed to create Skeleton detector');
      return;
    }
    // 使用 detector 进行一些操作
    // ...

    // 完成后销毁 detector
    if (detector) {
      await detector.destroy();
      hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
    } else {
      hilog.error(0x0000, 'skeletonDetectionSample', 'Failed to destroy Skeleton detector');
    }
  } catch (err) {
    hilog.error(0x0000, 'skeletonDetectionSample', `Skeleton detector error: ${err}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('createAndDestroyDetector').onClick(() => {
        void createAndDestroyDetector();
      })
    }
  }
}
```

### process

process(request: visionBase.Request): Promise<SkeletonDetectionResponse>

创建骨骼点检测实例并执行骨骼点检测。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SkeletonDetection

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | visionBase.[Request](core-vision-vision-base-api.md#request) | 是 | 图片实例。骨骼点检测接口仅支持传入一张图片，不支持传入多张图片。  详细内容请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SkeletonDetectionResponse](core-vision-skeleton-detection-api.md#skeletondetectionresponse)> | Promise对象，返回骨骼点识别的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |
| 1011000001 | Failed to run, please try again. |
| 1011000003 | Failed to run the model, please try again. |
| 1011000004 | Running the model timed out. Try again later. |

**示例：**

```typescript
import { skeletonDetection, visionBase } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function skeletonDetectTest() {
  try {
    let imageSource: image.ImageSource | undefined = undefined;
    let chooseImage: image.PixelMap | undefined = undefined;

    // 通过图库选择一张图片
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 1;
    let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
    let photoSelectResult = await photoPicker.select(photoSelectOptions);
    let uri = photoSelectResult.photoUris[0];
    if (uri === undefined) {
      hilog.info(0x0000, 'skeletonDetectionSample', 'uri is undefined');
      return;
    }

    // 将图片转换为PixelMap
    let file = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
    imageSource = image.createImageSource(file.fd);
    chooseImage = await imageSource.createPixelMap();
    hilog.info(0x0000, 'skeletonDetectionSample', 'chooseImage:', chooseImage);
    if (!chooseImage) {
      return;
    }

    // 创建检测器
    let detector = await skeletonDetection.SkeletonDetector.create();
    hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector created successfully');

    // 调用骨骼检测接口
    let request: visionBase.Request = {
      inputData: { pixelMap: chooseImage },
      scene: visionBase.SceneMode.FOREGROUND
    };
    let response: skeletonDetection.SkeletonDetectionResponse = await detector.process(request);

    if (response.skeletons.length === 0) {
      hilog.info(0x0000, 'skeletonDetectionSample', 'No skeletons detected in the image.');
    } else {
      hilog.info(0x0000, 'skeletonDetectionSample', `Detected ${response.skeletons.length} skeletons.`);
      response.skeletons.forEach((skeleton, index) => {
        hilog.info(0x0000, 'skeletonDetectionSample', `  Score: ${skeleton.score}`);
        hilog.info(0x0000, 'skeletonDetectionSample', `  Number of points: ${skeleton.points.length}`);
        skeleton.points.forEach(point => {
          hilog.info(0x0000, 'skeletonDetectionSample', `    ${skeletonDetection.SkeletonPointType[point.type]}: (${point.point.x}, ${point.point.y}), Score: ${point.score}`);
        });
      });
    }

    // 清理资源
    if (chooseImage && imageSource) {
      void chooseImage.release();
      void imageSource.release();
    }
    if (file) {
      await fileIo.close(file);
    }
    if (detector) {
      await detector.destroy();
      hilog.info(0x0000, 'skeletonDetectionSample', 'Skeleton detector destroyed successfully');
    }
  } catch (err) {
    hilog.error(0x0000, 'skeletonDetectionSample', `Skeleton detection error: ${err}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Button').onClick(() => {
        // 调用函数
        void skeletonDetectTest();
      })
    }
  }
}
```
