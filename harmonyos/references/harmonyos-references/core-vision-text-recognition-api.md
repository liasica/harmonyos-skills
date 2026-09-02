---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-recognition-api
title: textRecognition（文字识别）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > textRecognition（文字识别）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:71959c6eee25c8c76db4e273b61147d5311504564ecbd24c132dd24316c8c2b4
---

通用文字识别服务提供图像信息转换为字符信息的能力。通过拍照、扫描等光学输入方式，把各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息，便于用户提取字符内容、屏幕坐标及外框。

目前本服务支持识别的语言有：简体中文、英文、日文、韩文、繁体中文五种语言。在使用文字识别服务时，建议图像清晰、文字无遮挡、背景简洁，以获得最佳识别效果，不适用于模糊不清或倾斜严重的图像。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
```

## TextRecognitionConfiguration

通用文本识别的配置项，用于配置是否支持朝向检测。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isDirectionDetectionSupported | boolean | 否 | 是 | 表示是否支持文字朝向检测。  true：表示支持朝向检测；false：表示不支持朝向检测。  默认是true，支持朝向检测。如果能判断当前图片是正向的，则可考虑将该属性设置为false，以提升性能。 |

## VisionInfo

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的[PixelMap](arkts-apis-image-pixelmap.md)类型的视觉信息。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 待识别的图片。对于图片的要求请参见[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## PixelPoint

指示像素点的位置。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 是 | 否 | 像素点横向x坐标。 |
| y | number | 是 | 否 | 像素点纵向y坐标。 |

## TextWord

描述一个单词的信息，包括内容，以及外框的坐标。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 单词的文本内容。 |
| cornerPoints | Array<[PixelPoint](core-vision-text-recognition-api.md#pixelpoint)> | 是 | 否 | 以顺时针返回的单词外框位置点列表，数组第一个元素表示左上角。 |

## TextLine

描述图像中的一行文本。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 文本行的文本内容。 |
| cornerPoints | Array<[PixelPoint](core-vision-text-recognition-api.md#pixelpoint)> | 是 | 否 | 以顺时针返回该文本行的外框位置点列表，数组第一个元素表示左上角。 |
| words | Array<[TextWord](core-vision-text-recognition-api.md#textword)> | 是 | 否 | 该行包含的单词信息。 |

## TextBlock

描述图像中的文本块。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 段落的文本内容。 |
| lines | Array<[TextLine](core-vision-text-recognition-api.md#textline)> | 是 | 否 | 该段落包含的文本行内容。 |

## TextRecognitionResult

文本识别的结果信息，包括文本内容和坐标信息。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 所识别的文本内容。 |
| blocks | Array<[TextBlock](core-vision-text-recognition-api.md#textblock)> | 是 | 否 | 文本内容中的具体段落信息。 |

## textRecognition.init

init(): Promise<boolean>

初始化文字识别服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseOCR() {
  // 初始化 OCR 服务
  const initResult = await textRecognition.init();
  hilog.info(0x0000, 'textRecognitionSample', `OCR service initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

    // 这里可以添加使用 OCR 服务的代码
    // 例如：await textRecognition.recognizeText(...);

    // 使用完毕后，释放 OCR 服务
    await textRecognition.release();
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
  } else {
    hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseOCR').onClick(() => {
        // 调用函数
        void initAndReleaseOCR();
      })
    }
  }
}
```

## textRecognition.release

release(): Promise<void>

释放文字识别服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initAndReleaseOCR() {
  // 初始化 OCR 服务
  const initResult = await textRecognition.init();
  hilog.info(0x0000, 'textRecognitionSample', `OCR service initialization result:${initResult}`);

  if (initResult) {
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

    // 这里可以添加使用 OCR 服务的代码
    // 例如：await textRecognition.recognizeText(...);

    // 使用完毕后，释放 OCR 服务
    await textRecognition.release();
    hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
  } else {
    hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initAndReleaseOCR').onClick(() => {
        // 调用函数
        void initAndReleaseOCR();
      })
    }
  }
}
```

## textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, callback: AsyncCallback<TextRecognitionResult>): void

识别视觉信息内包含的文本。当识别完成时，回调函数会被自动调用并返回识别结果。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | 是 | 回调函数，当识别成功时，err为undefined，返回文字识别的结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run OCR, please try again. |
| 1001400002 | The OCR service is abnormal. |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function recognizeTextTest() {
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
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }

  // 将图片转换为PixelMap
  let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
  imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();
  if (!chooseImage) {
    return;
  }

  // 调用文本识别接口
  let visionInfo: textRecognition.VisionInfo = {
    pixelMap: chooseImage
  };
  textRecognition.recognizeText(visionInfo, (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
    if (error.code !== 0) {
      hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    // 识别成功，获取对应的结果
    let recognitionString = JSON.stringify(data);
    hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

    if (chooseImage && imageSource) {
      void chooseImage.release();
      void imageSource.release();
    }
  });
  if (fileSource) {
    await fileIo.close(fileSource);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('recognizeTextTest').onClick(() => {
        // 调用函数
        void recognizeTextTest();
      })
    }
  }
}
```

## textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, configuration ?: TextRecognitionConfiguration): Promise<TextRecognitionResult>

识别视觉信息内包含的文本。可以通过自定义配置项（如是否支持朝向检测）进行更详细的设置。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| configuration | [TextRecognitionConfiguration](core-vision-text-recognition-api.md#textrecognitionconfiguration) | 否 | 识别的配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | Promise对象，返回文字识别的结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run OCR, please try again. |
| 1001400002 | The OCR service is abnormal. |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function recognizeTextTest() {
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
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }

  // 将图片转换为PixelMap
  let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
  imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();
  if (!chooseImage) {
    return;
  }

  // 调用文本识别接口
  let visionInfo: textRecognition.VisionInfo = {
    pixelMap: chooseImage
  };
  let recognitionResult = await textRecognition.recognizeText(visionInfo);

  // 识别成功，获取对应的结果
  let recognitionString = JSON.stringify(recognitionResult);
  hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

  if (chooseImage && imageSource) {
    void chooseImage.release();
    void imageSource.release();
  }
  if (fileSource) {
    await fileIo.close(fileSource);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('recognizeTextTest').onClick(() => {
        // 调用函数
        void recognizeTextTest();
      })
    }
  }
}
```

## textRecognition.recognizeText

recognizeText(visionInfo: VisionInfo, configuration: TextRecognitionConfiguration, callback: AsyncCallback<TextRecognitionResult>): void

通过自定义配置项对识别能力进行更详细的设置，识别视觉信息内包含的文本。当识别完成时，回调函数会被自动调用并返回识别结果。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| configuration | [TextRecognitionConfiguration](core-vision-text-recognition-api.md#textrecognitionconfiguration) | 是 | 识别的配置项。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | 是 | 回调函数，当识别成功时err为undefined，返回文字识别的结果；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run OCR, please try again. |
| 1001400002 | The OCR service is abnormal. |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

async function recognizeTextTest() {
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
    hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
    return;
  }

  // 将图片转换为PixelMap
  let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
  imageSource = image.createImageSource(fileSource.fd);
  chooseImage = await imageSource.createPixelMap();
  if (!chooseImage) {
    return;
  }

  // 调用文本识别接口
  let visionInfo: textRecognition.VisionInfo = {
    pixelMap: chooseImage
  };
  let textConfiguration: textRecognition.TextRecognitionConfiguration = {
    isDirectionDetectionSupported: false
  };
  textRecognition.recognizeText(
    visionInfo,
    textConfiguration,
    (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
      if (error.code !== 0) {
        hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      // 识别成功，获取对应的结果
      let recognitionString = JSON.stringify(data);
      hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

      if (chooseImage && imageSource) {
        void chooseImage.release();
        void imageSource.release();
      }
    }
  );
  if (fileSource) {
    await fileIo.close(fileSource);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('recognizeTextTest').onClick(() => {
        // 调用函数
        void recognizeTextTest();
      })
    }
  }
}
```

## textRecognition.getSupportedLanguages

getSupportedLanguages(): Promise<Array<string>>

获取当前文本识别所支持的语言类型列表。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回所支持的[语言类型列表](core-vision-text-recognition-api.md#语言类型列表)。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1001400001 | Failed to run OCR, please try again. |
| 1001400002 | The OCR service is abnormal. |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {
  @State supportedLanguages: string[] = [];

  aboutToAppear() {
    // 获取支持的语言类型列表
    textRecognition.getSupportedLanguages().then((data: Array<string>) => {
      this.supportedLanguages = data;
      let languageString = data.join(', ');
      hilog.info(0x0000, 'OCRDemo', `Succeeded in obtaining the language: ${languageString}`);
    }, (err: BusinessError) => {
      hilog.error(0x0000, 'OCRDemo', `Failed to obtain the language. Code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Column() {
      Text(this.supportedLanguages.join(', '))
    }
  }
}
```

## textRecognition.getSupportedLanguages

getSupportedLanguages(callback: AsyncCallback<Array<string>>): void

获取当前文本识别所支持的语言类型列表。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 回调函数，当识别成功时err为undefined，返回所支持的[语言类型列表](core-vision-text-recognition-api.md#语言类型列表)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1001400001 | Failed to run OCR, please try again. |
| 1001400002 | The OCR service is abnormal. |

**示例：**

```typescript
import { textRecognition } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {
  @State supportedLanguages: string[] = [];

  aboutToAppear() {
    // 获取支持的语言类型列表
    textRecognition.getSupportedLanguages((error: BusinessError, data: Array<string>) => {
      if (!error) {
        this.supportedLanguages = data;
        hilog.info(0x0000, 'OCRDemo', `Succeeded in obtaining the language: ${data}`);
      } else {
        hilog.error(0x0000, 'OCRDemo', `Failed to obtain the language. Code: ${error.code}, message: ${error.message}`);
      }
    });
  }

  build() {
    Column() {
      Text(this.supportedLanguages.join(', '))
    }
  }
}
```

## 语言类型列表

| 语言（英） | 语言（中） |
| --- | --- |
| zh-CN | 简体中文 |
| en | 英文 |
| ja | 日文 |
| ko | 韩文 |
| zh-TW | 繁体中文 |
