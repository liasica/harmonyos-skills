---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mindsporelite
title: @ohos.ai.mindSporeLite (端侧AI框架)
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > ArkTS API > @ohos.ai.mindSporeLite (端侧AI框架)
category: harmonyos-references
scraped_at: 2026-04-28T08:19:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:03e327121d08cc7855c2c85ad9126176e2bdb83afa9eb4f8df1dd2b124d8c1c1
---

MindSpore Lite是一个轻量化、高性能的端侧AI引擎，提供了标准的模型推理和训练接口，内置通用硬件高性能算子库，支持Neural Network Runtime Kit使能AI专用芯片加速推理，助力打造全场景智能应用。

本模块主要介绍MindSpore Lite AI引擎支持模型端侧推理/训练的相关能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。示例代码使用模型均为MindSpore端侧模型。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { mindSporeLite } from '@kit.MindSporeLiteKit';
```

## mindSporeLite.loadModelFromFile

PhonePC/2in1TabletTVWearable

loadModelFromFile(model: string, callback: Callback<Model>): void

从完整路径加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型的完整输入路径。字符串长度限制跟随文件系统。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. let modelFile: string = '/path/to/xxx.ms';
2. mindSporeLite.loadModelFromFile(modelFile, (mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. if (modelInputs == null) {
5. console.error('MS_LITE_ERR: getInputs failed.')
6. } else {
7. console.info(modelInputs[0].name);
8. }
9. })
```

## mindSporeLite.loadModelFromFile

PhonePC/2in1TabletTVWearable

loadModelFromFile(model: string, context: Context, callback: Callback<Model>): void

从完整路径加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型的完整输入路径。字符串长度限制跟随文件系统。 |
| context | [Context](js-apis-mindsporelite.md#context) | 是 | 运行环境的配置信息。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.target = ['cpu'];
3. let modelFile: string = '/path/to/xxx.ms';
4. mindSporeLite.loadModelFromFile(modelFile, context, (mindSporeLiteModel: mindSporeLite.Model) => {
5. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
6. if (modelInputs == null) {
7. console.error('MS_LITE_ERR: getInputs failed.')
8. } else {
9. console.info(modelInputs[0].name);
10. }
11. })
```

## mindSporeLite.loadModelFromFile

PhonePC/2in1TabletTVWearable

loadModelFromFile(model: string, context?: Context): Promise<Model>

从完整路径加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型的完整输入路径。字符串长度限制跟随文件系统。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. if (modelInputs == null) {
5. console.error('MS_LITE_ERR: getInputs failed.')
6. } else {
7. console.info(modelInputs[0].name);
8. }
9. })
```

## mindSporeLite.loadModelFromBuffer

PhonePC/2in1TabletTVWearable

loadModelFromBuffer(model: ArrayBuffer, callback: Callback<Model>): void

从内存加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | 包含模型的内存。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((buffer: Uint8Array) => {
11. let modelBuffer = buffer.buffer;
12. mindSporeLite.loadModelFromBuffer(modelBuffer, (mindSporeLiteModel: mindSporeLite.Model) => {
13. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
14. console.info('MS_LITE_LOG: ' + modelInputs[0].name);
15. })
16. })
17. .catch((error: BusinessError) => {
18. console.error("getRawFileContent promise error is " + error);
19. });
```

## mindSporeLite.loadModelFromBuffer

PhonePC/2in1TabletTVWearable

loadModelFromBuffer(model: ArrayBuffer, context: Context, callback: Callback<Model>): void

从内存加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | 包含模型的内存。 |
| context | [Context](js-apis-mindsporelite.md#context) | 是 | 运行环境的配置信息。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((buffer: Uint8Array) => {
11. let modelBuffer = buffer.buffer;
12. let context: mindSporeLite.Context = {};
13. context.target = ['cpu'];
14. mindSporeLite.loadModelFromBuffer(modelBuffer, context, (mindSporeLiteModel: mindSporeLite.Model) => {
15. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
16. console.info('MS_LITE_LOG: ' + modelInputs[0].name);
17. })
18. })
19. .catch((error: BusinessError) => {
20. console.error("getRawFileContent promise error is " + error);
21. });
```

## mindSporeLite.loadModelFromBuffer

PhonePC/2in1TabletTVWearable

loadModelFromBuffer(model: ArrayBuffer, context?: Context): Promise<Model>

从内存加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | 包含模型的内存。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((buffer: Uint8Array) => {
11. let modelBuffer = buffer.buffer;
12. mindSporeLite.loadModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
13. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
14. console.info('MS_LITE_LOG: ' + modelInputs[0].name);
15. })
16. })
17. .catch((error: BusinessError) => {
18. console.error("getRawFileContent promise error is " + error);
19. });
```

## mindSporeLite.loadModelFromFd

PhonePC/2in1TabletTVWearable

loadModelFromFd(model: number, callback: Callback<Model>): void

从文件描述符加载输入模型，用于CPU推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | number | 是 | 模型的文件描述符。跟随文件系统返回fd值传入。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. let modelFile = '/path/to/xxx.ms';
4. let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
5. mindSporeLite.loadModelFromFd(file.fd, (mindSporeLiteModel: mindSporeLite.Model) => {
6. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
7. if (modelInputs == null) {
8. console.error('MS_LITE_ERR: getInputs failed.')
9. } else {
10. console.info(modelInputs[0].name);
11. }
12. })
```

## mindSporeLite.loadModelFromFd

PhonePC/2in1TabletTVWearable

loadModelFromFd(model: number, context: Context, callback: Callback<Model>): void

从文件描述符加载输入模型用于推理。使用callback异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | number | 是 | 模型的文件描述符。跟随文件系统返回fd值传入。 |
| context | [Context](js-apis-mindsporelite.md#context) | 是 | 运行环境的配置信息。 |
| callback | Callback<[Model](js-apis-mindsporelite.md#model)> | 是 | 回调函数。返回模型对象。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. let modelFile = '/path/to/xxx.ms';
4. let context: mindSporeLite.Context = {};
5. context.target = ['cpu'];
6. let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
7. mindSporeLite.loadModelFromFd(file.fd, context, (mindSporeLiteModel: mindSporeLite.Model) => {
8. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
9. if (modelInputs == null) {
10. console.error('MS_LITE_ERR: getInputs failed.')
11. } else {
12. console.info(modelInputs[0].name);
13. }
14. })
```

## mindSporeLite.loadModelFromFd

PhonePC/2in1TabletTVWearable

loadModelFromFd(model: number, context?: Context): Promise<Model>

从文件描述符加载输入模型用于推理。使用Promise异步函数。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | number | 是 | 模型的文件描述符。跟随文件系统返回fd值传入。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. let modelFile = '/path/to/xxx.ms';
4. let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
5. mindSporeLite.loadModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
6. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
7. if (modelInputs == null) {
8. console.error('MS_LITE_ERR: getInputs failed.')
9. } else {
10. console.info(modelInputs[0].name);
11. }
12. })
```

## mindSporeLite.loadTrainModelFromFile12+

PhonePC/2in1TabletTVWearable

loadTrainModelFromFile(model: string, trainCfg?: TrainCfg, context?: Context): Promise<Model>

根据路径加载训练模型文件。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | string | 是 | 模型的完整输入路径。字符串长度限制跟随文件系统。 |
| trainCfg | [TrainCfg](js-apis-mindsporelite.md#traincfg12) | 否 | 模型训练配置。默认值为TrainCfg各属性默认值。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. if (modelInputs == null) {
5. console.error('MS_LITE_ERR: getInputs failed.')
6. } else {
7. console.info(modelInputs[0].name);
8. }
9. })
```

## mindSporeLite.loadTrainModelFromBuffer12+

PhonePC/2in1TabletTVWearable

loadTrainModelFromBuffer(model: ArrayBuffer, trainCfg?: TrainCfg, context?: Context): Promise<Model>

从内存缓冲区加载训练模型。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | ArrayBuffer | 是 | 包含训练模型的内存。 |
| trainCfg | [TrainCfg](js-apis-mindsporelite.md#traincfg12) | 否 | 模型训练配置。默认值为TrainCfg各属性默认值。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((buffer: Uint8Array) => {
11. let modelBuffer = buffer.buffer;
12. mindSporeLite.loadTrainModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
13. console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
14. })
15. })
16. .catch((error: BusinessError) => {
17. console.error("getRawFileContent promise error is " + error);
18. });
```

## mindSporeLite.loadTrainModelFromFd12+

PhonePC/2in1TabletTVWearable

loadTrainModelFromFd(model: number, trainCfg?: TrainCfg, context?: Context): Promise<Model>

从文件描述符加载训练模型文件。使用Promise异步回调。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| model | number | 是 | 训练模型的文件描述符。跟随文件系统返回fd值传入。 |
| trainCfg | [TrainCfg](js-apis-mindsporelite.md#traincfg12) | 否 | 模型训练配置。默认值为TrainCfg各属性默认值。 |
| context | [Context](js-apis-mindsporelite.md#context) | 否 | 运行环境的配置信息。默认使用CpuDevice初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Model](js-apis-mindsporelite.md#model)> | Promise对象。返回Model对象。 |

**示例：**

```
1. import { fileIo } from '@kit.CoreFileKit';

3. let modelFile = '/path/to/xxx.ms';
4. let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ_ONLY);
5. mindSporeLite.loadTrainModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
6. console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
7. });
```

## mindSporeLite.getAllNNRTDeviceDescriptions12+

PhonePC/2in1TabletTVWearable

getAllNNRTDeviceDescriptions() : NNRTDeviceDescription[]

获取NNRt中的所有设备描述。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NNRTDeviceDescription](js-apis-mindsporelite.md#nnrtdevicedescription12)[] | NNRt设备描述信息数组。 |

**示例：**

```
1. let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
2. if (allDevices == null) {
3. console.error('MS_LITE_LOG: getAllNNRTDeviceDescriptions is NULL.');
4. }
```

## Context

PhonePC/2in1TabletTVWearable

定义运行环境的配置信息。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| target | string[] | 否 | 是 | 配置目标后端。可选'cpu'，'nnrt'，默认'cpu'。 |
| cpu | [CpuDevice](js-apis-mindsporelite.md#cpudevice) | 否 | 是 | CPU后端设备选项。只有当target包含'cpu'时，才能设置此属性。默认值为CpuDevice各属性默认值。 |
| nnrt | [NNRTDevice](js-apis-mindsporelite.md#nnrtdevice) | 否 | 是 | NNRt后端设备选项。只有当target包含'nnrt'时，才能设置此属性。默认值为NNRTDevice各属性默认值。 |

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.target = ['cpu','nnrt'];
```

## CpuDevice

PhonePC/2in1TabletTVWearable

CPU后端设备选项。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| threadNum | number | 否 | 是 | 设置运行时的线程数，默认值：2。 |
| threadAffinityMode | [ThreadAffinityMode](js-apis-mindsporelite.md#threadaffinitymode) | 否 | 是 | 设置运行时的CPU绑核策略模式，默认值为不绑核：mindSporeLite.ThreadAffinityMode.NO\_AFFINITIES。 |
| threadAffinityCoreList | number[] | 否 | 是 | 设置运行时的CPU绑核列表，设置绑核策略模式后使能，当绑核策略模式为mindSporeLite.ThreadAffinityMode.NO\_AFFINITIES时，绑核列表为空。列表中的数字代表核的序号。默认值：[]。 |
| precisionMode | string | 否 | 是 | 设置是否使能**Float16推理模式**，设置为'preferred\_fp16'代表使能半精度推理，其余设置情况均为不支持，默认设置'enforce\_fp32'表示不使能半精度推理。 |

**Float16推理模式**： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.cpu = {};
3. context.target = ['cpu'];
4. context.cpu.threadNum = 2;
5. context.cpu.threadAffinityMode = 0;
6. context.cpu.precisionMode = 'preferred_fp16';
7. context.cpu.threadAffinityCoreList = [0, 1, 2];
```

## ThreadAffinityMode

PhonePC/2in1TabletTVWearable

设置运行时的CPU绑核策略模式，有效值为0-2，0为默认不绑核，1为绑大核，2为绑中核。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_AFFINITIES | 0 | 不绑核。 |
| BIG\_CORES\_FIRST | 1 | 绑大核优先。 |
| LITTLE\_CORES\_FIRST | 2 | 绑中核优先。 |

## NNRTDevice

PhonePC/2in1TabletTVWearable

Neural Network Runtime表示神经网络运行时，简称NNRt。作为中间桥梁，连通上层 AI 推理框架和底层加速芯片，实现 AI 模型的跨芯片推理计算。MindSpore Lite 可配置NNRt后端。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceID12+ | bigint | 否 | 是 | NNRt设备ID。默认值为0。 |
| performanceMode12+ | [PerformanceMode](js-apis-mindsporelite.md#performancemode12) | 否 | 是 | NNRt设备的工作性能模式。默认值为PERFORMANCE\_NONE。 |
| priority12+ | [Priority](js-apis-mindsporelite.md#priority12) | 否 | 是 | NNRt推理任务优先级。默认值为PRIORITY\_MEDIUM。 |
| extensions12+ | [Extension](js-apis-mindsporelite.md#extension12)[] | 否 | 是 | NNRt设备的扩展配置。默认为空。 |

## PerformanceMode12+

PhonePC/2in1TabletTVWearable

NNRt设备的工作性能模式枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PERFORMANCE\_NONE | 0 | 无特殊设置。 |
| PERFORMANCE\_LOW | 1 | 低功耗模式。 |
| PERFORMANCE\_MEDIUM | 2 | 功耗-性能均衡模式。 |
| PERFORMANCE\_HIGH | 3 | 高性能模式。 |
| PERFORMANCE\_EXTREME | 4 | 极致性能模式。 |

## Priority12+

PhonePC/2in1TabletTVWearable

NNRt推理任务优先级枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIORITY\_NONE | 0 | 无优先级偏好。 |
| PRIORITY\_LOW | 1 | 低优先级任务。 |
| PRIORITY\_MEDIUM | 2 | 中优先级任务。 |
| PRIORITY\_HIGH | 3 | 高优先级任务。 |

## Extension12+

PhonePC/2in1TabletTVWearable

定义NNRt设备的扩展信息。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 扩展名称。 |
| value | ArrayBuffer | 否 | 否 | 包含扩展的内存。 |

## NNRTDeviceDescription12+

PhonePC/2in1TabletTVWearable

NNRt设备信息描述，包含设备ID，设备名称等信息。

**系统能力：** SystemCapability.AI.MindSporeLite

### deviceID12+

PhonePC/2in1TabletTVWearable

deviceID() : bigint

获取NNRt设备ID。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | NNRt设备ID。 |

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.target = ["nnrt"];
3. context.nnrt = {};
4. let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
5. if (allDevices == null) {
6. console.error('getAllNNRTDeviceDescriptions is NULL.');
7. } else {
8. for (let i: number = 0; i < allDevices.length; i++) {
9. console.info(allDevices[i].deviceID().toString());
10. }
11. }
```

### deviceType12+

PhonePC/2in1TabletTVWearable

deviceType() : NNRTDeviceType

获取NNRt设备类型。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NNRTDeviceType](js-apis-mindsporelite.md#nnrtdevicetype12) | NNRt设备类型。 |

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.target = ["nnrt"];
3. context.nnrt = {};
4. let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
5. if (allDevices == null) {
6. console.error('getAllNNRTDeviceDescriptions is NULL.');
7. } else {
8. for (let i: number = 0; i < allDevices.length; i++) {
9. console.info(allDevices[i].deviceType().toString());
10. }
11. }
```

### deviceName12+

PhonePC/2in1TabletTVWearable

deviceName() : string

获取NNRt设备名称。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | NNRt设备名称。 |

**示例：**

```
1. let context: mindSporeLite.Context = {};
2. context.target = ["nnrt"];
3. context.nnrt = {};
4. let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
5. if (allDevices == null) {
6. console.error('getAllNNRTDeviceDescriptions is NULL.');
7. } else {
8. for (let i: number = 0; i < allDevices.length; i++) {
9. console.info(allDevices[i].deviceName().toString());
10. }
11. }
```

## NNRTDeviceType12+

PhonePC/2in1TabletTVWearable

NNRt设备类型枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NNRTDEVICE\_OTHERS | 0 | 设备类型不属于以下3种，则属于其它。 |
| NNRTDEVICE\_CPU | 1 | CPU设备。 |
| NNRTDEVICE\_GPU | 2 | GPU设备。 |
| NNRTDEVICE\_ACCELERATOR | 3 | 特定的加速设备。 |

## TrainCfg12+

PhonePC/2in1TabletTVWearable

端侧训练相关参数的配置文件。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lossName | string[] | 否 | 是 | 损失函数的名称列表。默认值为["loss\_fct", "\_loss\_fn", "SigmoidCrossEntropy"]。 |
| optimizationLevel | [OptimizationLevel](js-apis-mindsporelite.md#optimizationlevel12) | 否 | 是 | 端侧训练的网络优化等级。默认值为O0。 |

**示例：**

```
1. let cfg: mindSporeLite.TrainCfg = {};
2. cfg.lossName = ["loss_fct", "_loss_fn", "SigmoidCrossEntropy"];
3. cfg.optimizationLevel = mindSporeLite.OptimizationLevel.O0;
```

## OptimizationLevel12+

PhonePC/2in1TabletTVWearable

端侧训练的网络优化等级枚举。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| O0 | 0 | 无优化等级。 |
| O2 | 2 | 将网络转换为float16，保持批量归一化层和损失函数为float32。 |
| O3 | 3 | 将网络转换为float16，包括批量归一化层。 |
| AUTO | 4 | 根据设备选择优化等级。 |

## QuantizationType12+

PhonePC/2in1TabletTVWearable

量化类型信息，有效值为0-2。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_QUANT | 0 | 不做量化。 |
| WEIGHT\_QUANT | 1 | 权重量化。 |
| FULL\_QUANT | 2 | 全量化。 |

## Model

PhonePC/2in1TabletTVWearable

模型实例。描述Model对象的属性和方法。

下例API示例中都需先使用[loadModelFromFile()](js-apis-mindsporelite.md#mindsporeliteloadmodelfromfile)、[loadModelFromBuffer()](js-apis-mindsporelite.md#mindsporeliteloadmodelfrombuffer)、[loadModelFromFd()](js-apis-mindsporelite.md#mindsporeliteloadmodelfromfd)中的任一方法获取到Model实例，再通过此实例调用对应方法。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| learningRate12+ | number | 否 | 是 | 训练模型的学习率。默认值从加载的模型中读取。 |
| trainMode12+ | boolean | 否 | 是 | 模型是否为训练模式。true表示训练模式，false表示非训练模式。如果是训练模型，trainMode默认是true；如果是推理模型，trainMode默认是false。 |

### getInputs

PhonePC/2in1TabletTVWearable

getInputs(): MSTensor[]

获取模型的输入用于推理。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 返回MSTensor对象。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. if (modelInputs == null) {
5. console.error('MS_LITE_ERR: getInputs failed.')
6. } else {
7. console.info(modelInputs[0].name);
8. }
9. })
```

### predict

PhonePC/2in1TabletTVWearable

predict(inputs: MSTensor[], callback: Callback<MSTensor[]>): void

执行推理模型。使用callback异步回调。需要确保调用时模型对象不被资源回收。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 是 | 模型的输入列表。MSTensor对象。 |
| callback | Callback<[MSTensor](js-apis-mindsporelite.md#mstensor)[]> | 是 | 回调函数。返回MSTensor对象。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let inputName = 'input_data.bin';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(inputName)
10. .then(async (buffer: Uint8Array) => {
11. let inputBuffer = buffer.buffer;
12. let modelFile: string = '/path/to/xxx.ms';
13. let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
14. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();

16. modelInputs[0].setData(inputBuffer);
17. mindSporeLiteModel.predict(modelInputs, (mindSporeLiteTensor: mindSporeLite.MSTensor[]) => {
18. let output = new Float32Array(mindSporeLiteTensor[0].getData());
19. for (let i = 0; i < output.length; i++) {
20. console.info('MS_LITE_LOG: ' + output[i].toString());
21. }
22. })
23. })
24. .catch((error: BusinessError) => {
25. console.error("getRawFileContent promise error is " + error);
26. });
```

### predict

PhonePC/2in1TabletTVWearable

predict(inputs: MSTensor[]): Promise<MSTensor[]>

执行推理模型，返回推理结果。使用Promise异步回调。需要确保调用时模型对象不被资源回收。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 是 | 模型的输入列表。MSTensor对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[MSTensor](js-apis-mindsporelite.md#mstensor)[]> | Promise对象。返回MSTensor对象列表。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let inputName = 'input_data.bin';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(inputName)
10. .then(async (buffer: Uint8Array) => {
11. let inputBuffer = buffer.buffer;
12. let modelFile = '/path/to/xxx.ms';
13. let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
14. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
15. modelInputs[0].setData(inputBuffer);
16. mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor: mindSporeLite.MSTensor[]) => {
17. let output = new Float32Array(mindSporeLiteTensor[0].getData());
18. for (let i = 0; i < output.length; i++) {
19. console.info(output[i].toString());
20. }
21. })
22. })
23. .catch((error: BusinessError) => {
24. console.error("getRawFileContent promise error is " + error);
25. });
```

### resize

PhonePC/2in1TabletTVWearable

resize(inputs: MSTensor[], dims: Array<Array<number>>): boolean

重新设置张量大小。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 是 | 模型的输入列表。 |
| dims | Array<Array<number>> | 是 | 需要修改的目标张量大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否设置成功的结果。true表示重新设置张量大小成功；false表示重新设置张量大小失败。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. let new_dim = new Array([1, 32, 32, 1]);
5. mindSporeLiteModel.resize(modelInputs, new_dim);
6. })
```

### runStep12+

PhonePC/2in1TabletTVWearable

runStep(inputs: MSTensor[]): boolean

单步训练模型，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputs | [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 是 | 模型的输入列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回单步训练模型是否成功的结果。true表示单步训练模型成功，false表示单步训练模型失败。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. mindSporeLiteModel.trainMode = true;
4. const modelInputs = mindSporeLiteModel.getInputs();
5. let ret = mindSporeLiteModel.runStep(modelInputs);
6. if (ret == false) {
7. console.error('MS_LITE_LOG: runStep failed.')
8. }
9. })
```

### getWeights12+

PhonePC/2in1TabletTVWearable

getWeights(): MSTensor[]

获取模型的所有权重，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 返回模型的权重张量。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((modelBuffer: Uint8Array) => {
11. mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
12. .then((mindSporeLiteModel: mindSporeLite.Model) => {
13. mindSporeLiteModel.trainMode = true;
14. const weights = mindSporeLiteModel.getWeights();
15. for (let i = 0; i < weights.length; i++) {
16. let printStr = weights[i].name + ", ";
17. printStr += weights[i].shape + ", ";
18. printStr += weights[i].dtype + ", ";
19. printStr += weights[i].dataSize + ", ";
20. printStr += weights[i].getData();
21. console.info("MS_LITE weights: ", printStr);
22. }
23. })
24. })
25. .catch((error: BusinessError) => {
26. console.error("getRawFileContent promise error is " + error);
27. });
```

### updateWeights12+

PhonePC/2in1TabletTVWearable

updateWeights(weights: MSTensor[]): boolean

更新模型的权重，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| weights | [MSTensor](js-apis-mindsporelite.md#mstensor)[] | 是 | 权重张量列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否更新权重成功的结果。true表示更新权重成功，false表示更新权重失败。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((modelBuffer: Uint8Array) => {
11. mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
12. .then((mindSporeLiteModel: mindSporeLite.Model) => {
13. mindSporeLiteModel.trainMode = true;
14. const weights = mindSporeLiteModel.getWeights();
15. let ret = mindSporeLiteModel.updateWeights(weights);
16. if (ret == false) {
17. console.error('MS_LITE_LOG: updateWeights failed.')
18. }
19. })
20. })
21. .catch((error: BusinessError) => {
22. console.error("getRawFileContent promise error is " + error);
23. });
```

### setupVirtualBatch12+

PhonePC/2in1TabletTVWearable

setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean

设置虚拟批次用于训练，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| virtualBatchMultiplier | number | 是 | 虚拟批次乘法器，当设置值小于1时，表示禁用虚拟batch。 |
| lr | number | 是 | 学习率。 |
| momentum | number | 是 | 动量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否设置虚拟批次成功的结果。true表示设置虚拟批次成功，false表示设置虚拟批次失败。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let modelFile = 'xxx.ms';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(modelFile)
10. .then((modelBuffer: Uint8Array) => {
11. mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
12. .then((mindSporeLiteModel: mindSporeLite.Model) => {
13. mindSporeLiteModel.trainMode = true;
14. let ret = mindSporeLiteModel.setupVirtualBatch(2, -1, -1);
15. if (ret == false) {
16. console.error('MS_LITE setupVirtualBatch failed.')
17. }
18. })
19. })
20. .catch((error: BusinessError) => {
21. console.error("getRawFileContent promise error is " + error);
22. });
```

### exportModel12+

PhonePC/2in1TabletTVWearable

exportModel(modelFile: string, quantizationType?: QuantizationType, exportInferenceOnly?: boolean, outputTensorName?: string[]): boolean

导出训练模型，仅用于端侧训练。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modelFile | string | 是 | 导出模型的文件路径。字符串长度限制跟随文件系统。 |
| quantizationType | [QuantizationType](js-apis-mindsporelite.md#quantizationtype12) | 否 | 量化类型，默认为NO\_QUANT。 |
| exportInferenceOnly | boolean | 否 | 是否只导出推理模型。true表示只导出推理模型，false表示导出训练和推理两个模型。默认为true。 |
| outputTensorName | string[] | 否 | 设置导出模型的输出张量的名称。默认为空字符串数组，表示全量导出。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否导出训练模型成功的结果。true表示导出训练模型成功，false表示导出训练模型失败。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. let newPath = '/newpath/to';
3. mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
4. mindSporeLiteModel.trainMode = true;
5. let ret = mindSporeLiteModel.exportModel(newPath + "/new_model.ms", mindSporeLite.QuantizationType.NO_QUANT, true);
6. if (ret == false) {
7. console.error('MS_LITE exportModel failed.')
8. }
9. })
```

### exportWeightsCollaborateWithMicro12+

PhonePC/2in1TabletTVWearable

exportWeightsCollaborateWithMicro(weightFile: string, isInference?: boolean, enableFp16?: boolean, changeableWeightsName?: string[]): boolean

导出供**micro推理**使用的模型权重，仅用于端侧训练。

**micro推理**：MindSpore Lite针对MCUs（MicroControllerUnits）部署硬件后端，提供了一种超轻量Micro AI部署解决方案，离线阶段直接将模型生成轻量化代码，不再需要在线解析模型和图编译。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| weightFile | string | 是 | 权重文件路径。字符串长度限制跟随文件系统。 |
| isInference | boolean | 否 | 是否从推理模型中导出权重。true表示从推理模型中导出权重，目前只支持true，默认为true。 |
| enableFp16 | boolean | 否 | 浮点权重是否以float16格式保存。true表示以float16格式保存，false表示不以float16格式保存。默认为false。 |
| changeableWeightsName | string[] | 否 | 设置可变权重的名称。默认为空字符串数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否导出供micro推理使用的模型权重成功的结果。true表示导出供micro推理使用的模型权重成功，false表示导出供micro推理使用的模型权重失败。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. let microWeight = '/path/to/xxx.bin';
3. mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
4. let ret = mindSporeLiteModel.exportWeightsCollaborateWithMicro(microWeight);
5. if (ret == false) {
6. console.error('MSLITE exportWeightsCollaborateWithMicro failed.')
7. }
8. })
```

## MSTensor

PhonePC/2in1TabletTVWearable

模型张量实例。描述MSTensor对象的属性和方法。它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。

下例API示例中都需先使用[getInputs()](js-apis-mindsporelite.md#getinputs)获取到MSTensor实例，再通过此实例调用对应方法。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 张量的名称。 |
| shape | number[] | 否 | 否 | 张量的维度数组。 |
| elementNum | number | 否 | 否 | 张量的维度数组的长度。 |
| dataSize | number | 否 | 否 | 张量的数据的长度。 |
| dtype | [DataType](js-apis-mindsporelite.md#datatype) | 否 | 否 | 张量的数据类型。 |
| format | [Format](js-apis-mindsporelite.md#format) | 否 | 否 | 张量的数据排布方式。 |

**示例：**

```
1. let modelFile = '/path/to/xxx.ms';
2. mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
3. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
4. console.info(modelInputs[0].name);
5. console.info(modelInputs[0].shape.toString());
6. console.info(modelInputs[0].elementNum.toString());
7. console.info(modelInputs[0].dtype.toString());
8. console.info(modelInputs[0].format.toString());
9. console.info(modelInputs[0].dataSize.toString());
10. })
```

### getData

PhonePC/2in1TabletTVWearable

getData(): ArrayBuffer

获取张量的数据。

**系统能力：** SystemCapability.AI.MindSporeLite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArrayBuffer | 返回张量的数据指针。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let inputName = 'input_data.bin';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(inputName)
10. .then(async (buffer: Uint8Array) => {
11. let inputBuffer = buffer.buffer;
12. let modelFile = '/path/to/xxx.ms';
13. let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
14. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
15. modelInputs[0].setData(inputBuffer);
16. mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor: mindSporeLite.MSTensor[]) => {
17. let output = new Float32Array(mindSporeLiteTensor[0].getData());
18. for (let i = 0; i < output.length; i++) {
19. console.info(output[i].toString());
20. }
21. })
22. })
23. .catch((error: BusinessError) => {
24. console.error("getRawFileContent promise error is " + error);
25. });
```

### setData

PhonePC/2in1TabletTVWearable

setData(inputArray: ArrayBuffer): void

设置张量的数据。

**系统能力：** SystemCapability.AI.MindSporeLite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputArray | ArrayBuffer | 是 | 张量的输入数据缓冲区。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { UIContext } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let inputName = 'input_data.bin';
6. let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
7. globalContext.getApplicationContext()
8. .resourceManager
9. .getRawFileContent(inputName)
10. .then(async (buffer: Uint8Array) => {
11. let inputBuffer = buffer.buffer;
12. let modelFile = '/path/to/xxx.ms';
13. let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
14. let modelInputs: mindSporeLite.MSTensor[] = mindSporeLiteModel.getInputs();
15. modelInputs[0].setData(inputBuffer);
16. })
17. .catch((error: BusinessError) => {
18. console.error("getRawFileContent promise error is " + error);
19. });
```

## DataType

PhonePC/2in1TabletTVWearable

张量的数据类型。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_UNKNOWN | 0 | 未知类型。 |
| NUMBER\_TYPE\_INT8 | 32 | 保持Int8的类型。 |
| NUMBER\_TYPE\_INT16 | 33 | 保持Int16的类型。 |
| NUMBER\_TYPE\_INT32 | 34 | 保持Int32的类型。 |
| NUMBER\_TYPE\_INT64 | 35 | 保持Int64的类型。 |
| NUMBER\_TYPE\_UINT8 | 37 | 保持UInt8的类型。 |
| NUMBER\_TYPE\_UINT16 | 38 | 保持UInt16的类型。 |
| NUMBER\_TYPE\_UINT32 | 39 | 保持UInt32的类型。 |
| NUMBER\_TYPE\_UINT64 | 40 | 保持UInt64的类型。 |
| NUMBER\_TYPE\_FLOAT16 | 42 | 保持Float16的类型。 |
| NUMBER\_TYPE\_FLOAT32 | 43 | 保持Float32的类型。 |
| NUMBER\_TYPE\_FLOAT64 | 44 | 保持Float64的类型。 |

## Format

PhonePC/2in1TabletTVWearable

张量的数据排布方式。

**系统能力：** SystemCapability.AI.MindSporeLite

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_FORMAT | -1 | 未知数据排布方式。 |
| NCHW | 0 | 数据排布方式为NCHW。 |
| NHWC | 1 | 数据排布方式为NHWC。 |
| NHWC4 | 2 | 数据排布方式为NHWC4。 |
| HWKC | 3 | 数据排布方式为HWKC。 |
| HWCK | 4 | 数据排布方式为HWCK。 |
| KCHW | 5 | 数据排布方式为KCHW。 |
