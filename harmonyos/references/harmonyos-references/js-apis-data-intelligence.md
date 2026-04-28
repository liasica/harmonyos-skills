---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-intelligence
title: @ohos.data.intelligence (智慧数据平台)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.intelligence (智慧数据平台)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e71962a0c77419daa1bc9da470d8c34f5fedc492dd06a74a3b0067ff867e2503
---

智慧数据平台（ArkData Intelligence Platform，AIP）提供端侧数据智慧化构建，使应用数据向量化，通过嵌入模型将非结构化的文本、图像等多模态数据，转换成具有语义的向量。

说明

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

考虑到数据向量化处理的计算量和资源占用较大，当前仅支持在2in1设备上使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { intelligence } from '@kit.ArkData';
```

## intelligence.getTextEmbeddingModel

PhonePC/2in1Tablet

getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>

获取文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ModelConfig](js-apis-data-intelligence.md#modelconfig) | 是 | 嵌入模型的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TextEmbedding](js-apis-data-intelligence.md#textembedding)> | Promise对象，返回文本嵌入模型对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let textConfig: intelligence.ModelConfig = {
4. version: intelligence.ModelVersion.BASIC_MODEL,
5. isNpuAvailable: false,
6. cachePath: "/data"
7. }
8. let textEmbedding: intelligence.TextEmbedding;

10. intelligence.getTextEmbeddingModel(textConfig)
11. .then((data: intelligence.TextEmbedding) => {
12. console.info("Succeeded in getting TextModel");
13. textEmbedding = data;
14. })
15. .catch((err: BusinessError) => {
16. console.error("Failed to get TextModel and code is " + err.code);
17. })
```

## intelligence.getImageEmbeddingModel

PhonePC/2in1Tablet

getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>

获取图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ModelConfig](js-apis-data-intelligence.md#modelconfig) | 是 | 嵌入模型的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageEmbedding](js-apis-data-intelligence.md#imageembedding)> | Promise对象，返回图像嵌入模型对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let imageConfig: intelligence.ModelConfig = {
4. version: intelligence.ModelVersion.BASIC_MODEL,
5. isNpuAvailable: false,
6. cachePath: "/data"
7. }
8. let imageEmbedding: intelligence.ImageEmbedding;

10. intelligence.getImageEmbeddingModel(imageConfig)
11. .then((data: intelligence.ImageEmbedding) => {
12. console.info("Succeeded in getting ImageModel");
13. imageEmbedding = data;
14. })
15. .catch((err: BusinessError) => {
16. console.error("Failed to get ImageModel and code is " + err.code);
17. })
```

## intelligence.splitText

PhonePC/2in1Tablet

splitText(text: string, config: SplitConfig): Promise<Array<string>>

获取文本的分块。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 用于分块的文本，可取任意值。 |
| config | [SplitConfig](js-apis-data-intelligence.md#splitconfig) | 是 | 文本分块的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回分块结果的数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let splitConfig: intelligence.SplitConfig = {
4. size: 10,
5. overlapRatio: 0.1
6. }
7. let splitText = 'text';

9. intelligence.splitText(splitText, splitConfig)
10. .then((data: Array<string>) => {
11. console.info("Succeeded in splitting Text");
12. })
13. .catch((err: BusinessError) => {
14. console.error("Failed to split Text and code is " + err.code);
15. })
```

## ModelConfig

PhonePC/2in1Tablet

管理嵌入模型的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version | [ModelVersion](js-apis-data-intelligence.md#modelversion) | 否 | 否 | 模型的版本。 |
| isNpuAvailable | boolean | 否 | 否 | 指示是否使用NPU加速向量化过程，true表示使用，false表示不使用。如果设备不支持NPU，调用加载模型会失败，并抛出错误码31300000。 |
| cachePath | string | 否 | 是 | 如果使用NPU进行加速，则需要本地路径进行模型缓存。格式为/xxx/xxx/xxx，xxx为路径地址，例如"/data"。长度上限为512个字符。默认值为""。 |

## ModelVersion

PhonePC/2in1Tablet

模型版本枚举。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC\_MODEL | 0 | 基本嵌入模型版本。 |

## Image

PhonePC/2in1TabletTVWearable

type Image = string

表示图片的URI地址，对应为string类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| string | 图片的URI地址。长度上限为512个字符。 |

## SplitConfig

PhonePC/2in1Tablet

管理文本分块的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| size | number | 否 | 否 | 分块的最大大小，取值为非负整数。 |
| overlapRatio | number | 否 | 否 | 相邻分块之间的重叠比率。范围为[0,1]，0表示重叠比率最低，1表示重叠比率最高。 |

## TextEmbedding

PhonePC/2in1Tablet

描述多模态嵌入模型的文本嵌入函数。

下列接口都需先使用[intelligence.getTextEmbeddingModel](js-apis-data-intelligence.md#intelligencegettextembeddingmodel)获取到TextEmbedding实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

### loadModel

PhonePC/2in1Tablet

loadModel(): Promise<void>

加载文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textEmbedding.loadModel()
4. .then(() => {
5. console.info("Succeeded in loading Model");
6. })
7. .catch((err: BusinessError) => {
8. console.error("Failed to load Model and code is " + err.code);
9. })
```

### releaseModel

PhonePC/2in1Tablet

releaseModel(): Promise<void>

释放文本嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textEmbedding.releaseModel()
4. .then(() => {
5. console.info("Succeeded in releasing Model");
6. })
7. .catch((err: BusinessError) => {
8. console.error("Failed to release Model and code is " + err.code);
9. })
```

### getEmbedding

PhonePC/2in1Tablet

getEmbedding(text: string): Promise<Array<number>>

获取给定文本的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](js-apis-data-intelligence.md#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 嵌入模型的输入文本。长度上限为512个字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回向量化结果的数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textEmbedding.loadModel();
4. let text = 'text';
5. textEmbedding.getEmbedding(text)
6. .then((data: Array<number>) => {
7. console.info("Succeeded in getting Embedding");
8. })
9. .catch((err: BusinessError) => {
10. console.error("Failed to get Embedding and code is " + err.code);
11. })
```

### getEmbedding

PhonePC/2in1Tablet

getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>

获取给定批次文本的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](js-apis-data-intelligence.md#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| batchTexts | Array<string> | 是 | 嵌入模型的文本输入批次。单个文本长度上限为512个字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<Array<number>>> | Promise对象，返回向量化结果的数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. textEmbedding.loadModel();
4. let batchTexts = ['text1', 'text2'];
5. textEmbedding.getEmbedding(batchTexts)
6. .then((data: Array<Array<number>>) => {
7. console.info("Succeeded in getting Embedding");
8. })
9. .catch((err: BusinessError) => {
10. console.error("Failed to get Embedding and code is " + err.code);
11. })
```

## ImageEmbedding

PhonePC/2in1Tablet

描述多模态嵌入模型的图像嵌入函数。

下列接口都需先使用[intelligence.getImageEmbeddingModel](js-apis-data-intelligence.md#intelligencegetimageembeddingmodel)获取到ImageEmbedding实例，再通过此实例调用对应接口。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

### loadModel

PhonePC/2in1Tablet

loadModel(): Promise<void>

加载图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. imageEmbedding.loadModel()
4. .then(() => {
5. console.info("Succeeded in loading Model");
6. })
7. .catch((err: BusinessError) => {
8. console.error("Failed to load Model and code is " + err.code);
9. })
```

### releaseModel

PhonePC/2in1Tablet

releaseModel(): Promise<void>

释放图像嵌入模型。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. imageEmbedding.releaseModel()
4. .then(() => {
5. console.info("Succeeded in releasing Model");
6. })
7. .catch((err: BusinessError) => {
8. console.error("Failed to release Model and code is " + err.code);
9. })
```

### getEmbedding

PhonePC/2in1Tablet

getEmbedding(image: Image): Promise<Array<number>>

获取给定图像的嵌入向量。使用Promise异步回调。

该接口需先调用[loadModel](js-apis-data-intelligence.md#loadmodel)加载嵌入模型，加载成功后调用getEmbedding。

**系统能力：** SystemCapability.DistributedDataManager.DataIntelligence.Core

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备类型中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [Image](js-apis-data-intelligence.md#image) | 是 | 嵌入模型的输入图像类型的URI地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回向量化结果的数组对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[智慧数据平台错误码](errorcode-intelligence.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. imageEmbedding.loadModel();
4. let image = 'file://<packageName>/data/storage/el2/base/haps/entry/files/xxx.jpg';
5. imageEmbedding.getEmbedding(image)
6. .then((data: Array<number>) => {
7. console.info("Succeeded in getting Embedding");
8. })
9. .catch((err: BusinessError) => {
10. console.error("Failed to get Embedding and code is " + err.code);
11. })
```
