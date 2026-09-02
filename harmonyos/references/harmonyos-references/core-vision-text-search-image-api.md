---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-search-image-api
title: textSearchImage（通过文本搜索图片）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > textSearchImage（通过文本搜索图片）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e6349224dd9f1afcb56658ce90cd2df651f47fd6bba0814341198e691ada5022
---

文本搜索图片提供基于文本描述的图片检索能力。通过输入文本关键词，从已插入的图片库中搜索匹配的图像结果，返回图片沙箱路径、作用域和相似度信息。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
```

## ImageObject

搜索完成后返回的图片信息对象，包含图片沙箱路径、图片作用域和相似度（图像与搜索文本之间对比）。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| imagePath | string | 是 | 否 | 图片沙箱路径。 |
| scope | string | 是 | 否 | 图片作用域。 |
| similarity | number | 是 | 否 | 图像和相关文本的相似度，取值范围为[-1, 1]，数值越大相似度越高，反之则相似度越低。 |

## textSearchImage.init

init(): Promise<boolean>

初始化文本搜索图片分析器服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示初始化成功，返回false表示初始化失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100002 | Service abnormal. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

async function initTextSearchImage() {
  try {
    const initResult = await textSearchImage.init();
    hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
    if (initResult) {
      hilog.info(0x0000, 'textSearchImageSample', 'Text search image initialized successfully');
    } else {
      hilog.error(0x0000, 'textSearchImageSample', 'Failed to initialize text search image');
    }
  } catch (error) {
    hilog.error(0x0000, 'textSearchImageSample', `Init failed. Code: ${error.code}, message: ${error.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('initTextSearchImage').onClick(() => {
        void initTextSearchImage();
      })
    }
  }
}
```

## textSearchImage.insertImage

insertImage(imagePath: string, scope: string): Promise<boolean>

在数据库中插入图片特征。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imagePath | string | 是 | 图片沙箱路径，允许的长度范围[1,128]，支持字母、数字、符号。对于图像尺寸的要求，详细内容请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |
| scope | string | 是 | 图片作用域，允许的长度范围[1,32]，支持字母或数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示插入成功，返回false表示插入失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100001 | Invalid image path. |
| 1013100002 | Service abnormal. |
| 1013100003 | The capability has been updated. Please use the function [clearData](core-vision-text-search-image-api.md#textsearchimagecleardata), and after completing it, use this function again. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function insertImage(context: common.UIAbilityContext) {
  // 正确获取应用级别的沙箱路径
  const applicationContext = context.getApplicationContext();
  const filesDir = applicationContext.filesDir;
  
  // 请确保该路径下确实存在对应的图片文件
  const imagePath = filesDir + '/haps/entry/files/image.jpg';
  const scope = 'default_scope';

  try {
    const result = await textSearchImage.insertImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
  }
}

@Entry
@Component
struct Page {
  build() {
    Column() {
      Button('insertImage')
        .onClick(() => {
          const context = getContext(this) as common.UIAbilityContext;
          void insertImage(context);
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## textSearchImage.search

search(query: string, scope: string, topKey?: number): Promise<Array<ImageObject>>

返回匹配搜索条件的图片集合。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 查询词，允许的长度范围[1,100]，不支持纯数字和纯字母，支持中文，拼接数字，字母或者符号。 |
| scope | string | 是 | 图片作用域，允许的长度范围[1,32]，支持字母或数字。 |
| topKey | number | 否 | 在满足匹配条件的前提下，自定义返回图片数量的上限，默认值为100。取值范围为[0, 100]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ImageObject](core-vision-text-search-image-api.md#imageobject)>> | Promise对象，返回匹配的图片结果列表。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100002 | Service abnormal. |
| 1013100003 | The capability has been updated. Please use the function [clearData](core-vision-text-search-image-api.md#textsearchimagecleardata), and after completing it, use this function again. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function searchImages() {
  const query = 'landscape';
  const scope = 'default_scope';
  const topKey = 100;
  
  try {
    const results = await textSearchImage.search(query, scope, topKey);
    hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
    results.forEach((imageObject, index) => {
      hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
    });
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('searchImages').onClick(() => {
        void searchImages();
      })
    }
  }
}
```

## textSearchImage.deleteImage

deleteImage(imagePath: string, scope: string): Promise<boolean>

从数据库中删除该图片记录。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imagePath | string | 是 | 图片沙箱路径，允许的长度范围[1,128]，支持字母、数字、符号。 |
| scope | string | 是 | 图片作用域，允许的长度范围[1,32]，支持字母或数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示删除成功，返回false表示删除失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100002 | Service abnormal. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function deleteImage(context: common.UIAbilityContext) {
  // 正确获取应用级别的沙箱路径
  const applicationContext = context.getApplicationContext();
  const filesDir = applicationContext.filesDir;

  // 请确保该路径下确实存在对应的图片文件
  const imagePath = filesDir + '/haps/entry/files/image.jpg';
  const scope = 'default_scope';

  try {
    const result = await textSearchImage.deleteImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
  }
}

@Entry
@Component
struct Page {
  build() {
    Column() {
      Button('deleteImage').onClick(() => {
        const context = getContext(this) as common.UIAbilityContext;
        void deleteImage(context);
      })
    }
  }
}
```

## textSearchImage.clearData

clearData(): Promise<boolean>

清除数据库中所有数据，建议在模型能力更新后执行。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示清除数据成功，返回false表示清除数据失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100002 | Service abnormal. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function clearAllData() {
  try {
    const result = await textSearchImage.clearData();
    hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('clearAllData').onClick(() => {
        void clearAllData();
      })
    }
  }
}
```

## textSearchImage.release

release(): Promise<boolean>

释放文本搜索图片分析器服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示释放成功，返回false表示释放失败。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](errorcode-core-vision.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1013100002 | Service abnormal. |

**示例：**

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function releaseTextSearchImage() {
  try {
    const result = await textSearchImage.release();
    hilog.info(0x0000, 'textSearchImageSample', `Release result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Release failed. Code: ${err.code}, message: ${err.message}`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('releaseTextSearchImage').onClick(() => {
        void releaseTextSearchImage();
      })
    }
  }
}
```
