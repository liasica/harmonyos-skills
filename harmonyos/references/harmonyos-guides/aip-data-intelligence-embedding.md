---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/aip-data-intelligence-embedding
title: 应用数据向量化 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据向量化 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52d64aa63a0340c7c5b5a2607ee29d2ec7f616aea5112634282cfab3c7f42bf2
---

## 场景介绍

在数字化向智能化演进的关键阶段，构建智慧化服务已成为应用开发者提升产品竞争力的必然选择。

当前，系统提供ArkData智慧数据平台（ArkData Intelligence Platform，AIP），提供端侧数据智慧化构建，使应用数据向量化，通过嵌入模型将非结构化的文本、图像等多模态数据，转换成具有语义的向量。

从API version 15开始，支持应用数据向量化。

## 基本概念

在智慧化数据构建过程中，涉及以下基本概念，请先了解相关含义。

### 向量化

向量化主要是指通过嵌入模型将高维非结构化数据（如文字、图像）映射为低维连续向量的嵌入技术。嵌入技术通过模型捕捉数据之间的语义关系，将抽象概念转化为可计算的数学表示，使计算机能够理解非结构化数据。目前，嵌入技术广泛应用于自然语言处理（语义搜索）、图像识别（特征提取）、推荐系统（用户/物品表征）等领域。

### 多模态嵌入模型

应用数据向量化，主要通过嵌入模型实现。当前支持多模态嵌入模型，能将文本和图像这两种不同数据模态转换到同一个向量空间，支持单模态（文搜文、图搜图）和跨模态（文搜图、图搜文）的语义表征能力。

### 文本分块

数据向量化时，文本数据长度受限，可通过AIP分块接口切分文本，高效实现数据向量化。

## 实现机制

应用可借助智慧数据平台能力，实现智慧化数据的构建，将应用数据转化为可计算的向量，相关能力均运行在应用进程内，数据不出应用，保证隐私安全。

## 运作机制

应用数据向量化，将应用原数据向量化并存储在向量数据库中。

## 约束限制

* 考虑到数据向量化处理的计算量和资源占用较大，当前仅支持在2in1设备上使用。
* 嵌入模型的推理过程可使用NPU加速。与NPU计算相比，纯CPU的计算在时延和功耗上都有较大差距，建议采用NPU加速。
* 模型推理单次可处理的文本长度上限为512个字符，支持中英文。
* 模型推理单次可处理的图像大小小于20MB。

## 接口说明

以下是智慧数据向量化功能的相关接口。更多接口及使用方式请见[智慧数据平台](../harmonyos-references/js-apis-data-intelligence.md)。

| 接口名称 | 描述 |
| --- | --- |
| getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding> | 获取文本嵌入模型。 |
| loadModel(): Promise<void> | 加载文本嵌入模型。 |
| splitText(text: string, config: SplitConfig): Promise<Array<string>> | 获取文本的分块。 |
| getEmbedding(text: string): Promise<Array<number>> | 获取给定文本的嵌入向量。 |
| getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>> | 获取给定批次文本的嵌入向量。 |
| releaseModel(): Promise<void> | 释放文本嵌入模型。 |
| getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding> | 获取图像嵌入模型。 |
| loadModel(): Promise<void> | 加载图像嵌入模型。 |
| getEmbedding(image: Image): Promise<Array<number>> | 获取给定图像的嵌入向量。 |
| releaseModel(): Promise<void> | 释放图像嵌入模型。 |

## 文本向量化开发步骤

1. 导入模块。

   ```
   1. import { intelligence } from '@kit.ArkData';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取文本嵌入模型。

   调用getTextEmbeddingModel方法，获取文本嵌入模型。示例代码如下所示：

   ```
   1. let textConfig:intelligence.ModelConfig = {
   2. version:intelligence.ModelVersion.BASIC_MODEL,
   3. isNpuAvailable:false,
   4. cachePath:"/data"
   5. }
   6. let textEmbedding:intelligence.TextEmbedding;
   ```

   ```
   1. intelligence.getTextEmbeddingModel(textConfig)
   2. .then((data:intelligence.TextEmbedding) => {
   3. console.info('Succeeded in getting TextModel');
   4. textEmbedding = data;
   5. // ...
   6. })
   7. .catch((err:BusinessError) => {
   8. console.error('Failed to get TextModel and code is ' + err.code);
   9. // ...
   10. })
   ```
3. 加载文本嵌入模型。

   调用loadModel方法，加载文本嵌入模型。示例代码如下所示：

   ```
   1. textEmbedding.loadModel()
   2. .then(() => {
   3. console.info('Succeeded in loading Model');
   4. // ...
   5. })
   6. .catch((err:BusinessError) => {
   7. console.error('Failed to load Model and code is ' + err.code);
   8. // ...
   9. })
   ```
4. 获取文本的分块。当数据长度超过限定时，使用splitText()接口将其分块，然后再进行数据向量化。

   调用splitText方法，获取文本的分块结果。示例代码如下所示：

   ```
   1. let splitConfig:intelligence.SplitConfig = {
   2. size:10,
   3. overlapRatio:0.1
   4. }
   5. let splitText = 'text';

   7. intelligence.splitText(splitText, splitConfig)
   8. .then((data:Array<string>) => {
   9. console.info('Succeeded in splitting Text');
   10. // ...
   11. })
   12. .catch((err:BusinessError) => {
   13. console.error('Failed to split Text and code is ' + err.code);
   14. // ...
   15. })
   ```
5. 获取给定文本的嵌入向量。给定的文本数据可以是单个文本或文本集合。

   调用getEmbedding方法，获取给定单个文本或文本集合的嵌入向量。示例代码如下所示：

   ```
   1. let text = 'text';
   2. textEmbedding.getEmbedding(text)
   3. .then((data:Array<number>) => {
   4. console.info('Succeeded in getting Embedding');
   5. // ...
   6. })
   7. .catch((err:BusinessError) => {
   8. console.error('Failed to get Embedding and code is ' + err.code);
   9. // ...
   10. })

   12. let batchTexts = ['text1','text2'];
   13. textEmbedding.getEmbedding(batchTexts)
   14. .then((data:Array<Array<number>>) => {
   15. console.info('Succeeded in getting Embedding');
   16. // ...
   17. })
   18. .catch((err:BusinessError) => {
   19. console.error('Failed to get Embedding and code is ' + err.code);
   20. // ...
   21. })
   ```
6. 释放文本嵌入模型。

   调用releaseModel方法，释放文本嵌入模型。示例代码如下所示：

   ```
   1. textEmbedding.releaseModel()
   2. .then(() => {
   3. console.info('Succeeded in releasing Model');
   4. // ...
   5. })
   6. .catch((err:BusinessError) => {
   7. console.error('Failed to release Model and code is ' + err.code);
   8. // ...
   9. })
   ```

## 图像向量化开发步骤

1. 导入模块。

   ```
   1. import { intelligence } from '@kit.ArkData';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 获取图像嵌入模型。

   调用getImageEmbeddingModel方法，获取图像嵌入模型。示例代码如下所示：

   ```
   1. let imageConfig:intelligence.ModelConfig = {
   2. version:intelligence.ModelVersion.BASIC_MODEL,
   3. isNpuAvailable:false,
   4. cachePath:"/data"
   5. }
   6. let imageEmbedding:intelligence.ImageEmbedding;
   ```

   ```
   1. intelligence.getImageEmbeddingModel(imageConfig)
   2. .then((data:intelligence.ImageEmbedding) => {
   3. console.info('Succeeded in getting ImageModel');
   4. imageEmbedding = data;
   5. // ...
   6. })
   7. .catch((err:BusinessError) => {
   8. console.error('Failed to get ImageModel and code is ' + err.code);
   9. // ...
   10. })
   ```
3. 加载图像嵌入模型。

   调用loadModel方法，加载图像嵌入模型。示例代码如下所示：

   ```
   1. imageEmbedding.loadModel()
   2. .then(() => {
   3. console.info('Succeeded in loading Model');
   4. // ...
   5. })
   6. .catch((err:BusinessError) => {
   7. console.error('Failed to load Model and code is ' + err.code);
   8. // ...
   9. })
   ```
4. 获取给定图像的嵌入向量。

   调用getEmbedding方法，获取给定图像的嵌入向量。示例代码如下所示：

   ```
   1. let image = 'file://<packageName>/data/storage/el2/base/haps/entry/files/xxx.jpg';
   2. imageEmbedding.getEmbedding(image)
   3. .then((data:Array<number>) => {
   4. console.info('Succeeded in getting Embedding');
   5. // ...
   6. })
   7. .catch((err:BusinessError) => {
   8. console.error('Failed to get Embedding and code is ' + err.code);
   9. // ...
   10. })
   ```
5. 释放图像嵌入模型。

   调用releaseModel方法，释放图像嵌入模型。示例代码如下所示：

   ```
   1. imageEmbedding.releaseModel()
   2. .then(() => {
   3. console.info('Succeeded in releasing Model');
   4. // ...
   5. })
   6. .catch((err:BusinessError) => {
   7. console.error('Failed to release Model and code is ' + err.code);
   8. // ...
   9. })
   ```
