---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-subjectsegmentation-api
title: subjectSegmentation（主体分割）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > subjectSegmentation（主体分割）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:abbcebc64198357c7cb380dd653b93925bcfaba3cffa58993955c9b116253362
---

Core Vision Kit根据配置参数（如最多检测多少个物体、是否输出每个物体的详细信息等）可将一张普通的图片进行分割，分割后的信息包括图片整体的分割结果和每个显著物体的详细信息。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
```

## VisionInfo

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的PixelMap类型的视觉信息。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 待识别的图片。对于图片的要求请参见[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## SegmentationConfig

显著性分割的可选配置项，包括最多输出的主体个数、是否输出每个主体的详细分割信息，以及是否输出前景图的配置项。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| maxCount | number | 否 | 是 | 最多输出主体个数。取值范围为[1,20]个，以主体在原图中的面积占比降序排序，默认为6，超出范围则报错。 |
| enableSubjectDetails | boolean | 否 | 是 | 是否输出每个主体的前景信息（subjectDetails），默认为false，true代表输出每个主体的前景信息。 |
| enableSubjectForegroundImage | boolean | 否 | 是 | 是否输出前景图，默认为false，true代表输出前景图。 |

## Rectangle

显著性主体分割后的边界框。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 边界框左上角的x坐标。 |
| top | number | 否 | 否 | 边界框左上角的y坐标。 |
| height | number | 否 | 否 | 边界框高度，单位：px。 |
| width | number | 否 | 否 | 边界框宽度，单位：px。 |

## SubjectResult

分割后的详细结果。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| foregroundImage | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 显著性主体前景图。 |
| mattingList | Int32Array | 否 | 否 | 基于原图大小的一维数组，表示主体掩码。0-255取值范围。0代表背景，255代表主体，中间值代表是否是显著性主体的概率。 |
| subjectRectangle | [Rectangle](core-vision-subjectsegmentation-api.md#rectangle) | 否 | 否 | 主体的内切框。 |

## SegmentationResult

分割后的总输出结果，包括主体个数、整张图中所有主体的分割信息和每个主体的详细信息。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| subjectCount | number | 否 | 否 | 表示返回的主体个数，实际返回数量为画面中检测到的主体数量和maxCount中的较小值，受[SegmentationConfig](core-vision-subjectsegmentation-api.md#segmentationconfig)中maxCount参数的限制。 |
| fullSubject | [SubjectResult](core-vision-subjectsegmentation-api.md#subjectresult) | 否 | 否 | 默认输出的显著性主体合并信息。当画面主体数超过maxCount时，仅基于面积最大的maxCount个主体进行合并，与subjectDetails范围保持一致。 |
| subjectDetails | Array<[SubjectResult](core-vision-subjectsegmentation-api.md#subjectresult)> | 否 | 是 | 每个主体的详细信息列表，按主体面积降序排列，长度受maxCount限制。当enableSubjectDetails为true时返回，否则不返回，使用前需进行非空判断。 |

## subjectSegmentation.init

init(): Promise<boolean>

初始化主体分割服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseSubjectSegmentation() {
  // 初始化主体分割服务
  const initResult = await subjectSegmentation.init();
  hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

    // 这里可以添加使用主体分割服务的代码

    // 使用完毕后，释放主体分割服务
    await subjectSegmentation.release();
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
  } else {
    hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseSubjectSegmentation').onClick(() => {
        // 调用函数
        void initAndReleaseSubjectSegmentation();
      })
    }
  }
}
```

## subjectSegmentation.release

release(): Promise<void>

释放主体分割服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseSubjectSegmentation() {
  // 初始化主体分割服务
  const initResult = await subjectSegmentation.init();
  hilog.info(0x0000, 'subjectSegmentationSample', `Subject segmentation initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation initialized successfully');

    // 这里可以添加使用主体分割服务的代码

    // 使用完毕后，释放主体分割服务
    await subjectSegmentation.release();
    hilog.info(0x0000, 'subjectSegmentationSample', 'Subject segmentation released successfully');
  } else {
    hilog.error(0x0000, 'subjectSegmentationSample', 'Failed to initialize subject segmentation');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseSubjectSegmentation').onClick(() => {
        // 调用函数
        void initAndReleaseSubjectSegmentation();
      })
    }
  }
}
```

## subjectSegmentation.doSegmentation

doSegmentation(visionInfo: VisionInfo, config?: SegmentationConfig): Promise<SegmentationResult>

创建显著性分割实例，并初始化引擎。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.SubjectSegmentation

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-subjectsegmentation-api.md#visioninfo) | 是 | 图片实例。 |
| config | [SegmentationConfig](core-vision-subjectsegmentation-api.md#segmentationconfig) | 否 | 显著性分割的可选配置项，包括最大主体个数和是否输出每个主体的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SegmentationResult](core-vision-subjectsegmentation-api.md#segmentationresult)> | Promise对象，返回显著性主体的结果。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1011000001 | Failed to run, please try again. |
| 1011000002 | The service is abnormal. |

**示例：**

```typescript
import { subjectSegmentation } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const TAG: string = 'ImageSegmentationSample';

async function subjectSegmentationTest() {
  let chooseImage: image.PixelMap | undefined = undefined;
  // 设置识别主体数量的上限
  let maxNum: string = '20';

  // 通过图库选择一张图片
  let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
  photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
  photoSelectOptions.maxSelectNumber = 1;
  let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
  let photoSelectResult = await photoPicker.select(photoSelectOptions);
  let uris = photoSelectResult.photoUris;

  if (uris.length !== 1) {
    hilog.info(0x0000, TAG, 'Selected uris length is not 1');
    return;
  }

  // 将选择的图片转换为PixelMap
  let fileSource = await fileIo.open(uris[0], fileIo.OpenMode.READ_ONLY);
  let imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();

  if (!chooseImage) {
    hilog.info(0x0000, TAG, 'chooseImage is undefined');
    return;
  }
  if (fileSource) {
    await fileIo.close(fileSource);
  }

  // 调用主体分割接口
  let visionInfo: subjectSegmentation.VisionInfo = {
    pixelMap: chooseImage
  };
  let config: subjectSegmentation.SegmentationConfig = {
    maxCount: parseInt(maxNum),
    enableSubjectDetails: true,
    enableSubjectForegroundImage: true
  };
  let data: subjectSegmentation.SegmentationResult = await subjectSegmentation.doSegmentation(visionInfo, config);

  // 拼装分割结果信息
  let outputString = `Subject count: ${data.subjectCount}\n`;
  outputString += `Max subject count: ${config.maxCount}\n`;
  outputString += `Enable subject details: ${config.enableSubjectDetails ? 'Yes' : 'No'}\n\n`;
  let segBox: subjectSegmentation.Rectangle = data.fullSubject.subjectRectangle;
  outputString += `Full subject box:\nLeft: ${segBox.left}, Top: ${segBox.top}, Width: ${segBox.width}, Height: ${segBox.height}\n\n`;

  // 拼装每个主体的详细分割信息
  if (config.enableSubjectDetails && data.subjectDetails) {
    outputString += 'Individual subject boxes:\n';
    for (let i = 0; i < data.subjectDetails.length; i++) {
      let detailSegBox: subjectSegmentation.Rectangle = data.subjectDetails[i].subjectRectangle;
      outputString += `Subject ${i + 1}:\nLeft: ${detailSegBox.left}, Top: ${detailSegBox.top}, Width: ${detailSegBox.width}, Height: ${detailSegBox.height}\n\n`;
    }
  }

  hilog.info(0x0000, TAG, 'Segmentation result: ' + outputString);
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('subjectSegmentationTest').onClick(() => {
        // 调用函数
        void subjectSegmentationTest();
      })
    }
  }
}
```
