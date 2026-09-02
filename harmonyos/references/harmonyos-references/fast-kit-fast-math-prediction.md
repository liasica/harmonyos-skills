---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-math-prediction
title: "@hms.fast.mathPrediction (数理预测)"
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > ArkTS API > @hms.fast.mathPrediction (数理预测)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8824389aa4d852d62e4487140c6b4eca1885adc5f219a5aa43d536b1a4183c3c
---

本模块提供基于历史采样数据对序列数据进行建模和预测的能力，适用于手势跟踪、动画曲线预测、运动轨迹预估等实时预测场景。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { mathPrediction } from '@kit.FASTKit';
```

## predictIndex

predictIndex(samples: IndexSample[]): number

基于历史采样数据预测下一帧的索引值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| samples | [IndexSample](fast-kit-fast-math-prediction.md#indexsample)[] | 是 | 最近帧的采样点数组，按时间戳从早到晚排序。该参数用于提供历史数据以进行趋势分析和预测。例如，在手势跟踪中，它表示用户手部在连续时间点的位置变化；在动画曲线预测中，它代表关键帧的索引序列。必须包含至少2个数据点，否则抛出错误码1023100001。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 预测的下一帧索引值（四舍五入为整数），表示基于历史采样数据推断出的下一个预期索引位置，可用于后续的数据处理或动画渲染。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](fast-kit-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1023100001 | Array length invalid. |

**示例：**

```typescript
import { mathPrediction } from '@kit.FASTKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义历史采样点数组，包含至少两个数据点用于预测
let samples: mathPrediction.IndexSample[] = [
  // 第一个采样点：索引为0，时间戳为0
  { index: 0, timestamp: 0 },
  // 第二个采样点：索引为10，时间戳为100
  { index: 10, timestamp: 100 },
  // 第三个采样点：索引为20，时间戳为200
  { index: 20, timestamp: 200 }
];

try {
  // 调用 predictIndex 方法进行索引预测
  let predicted = mathPrediction.predictIndex(samples);
  // 输出预测结果
  console.info(`predicted index: ${predicted}`);
} catch (err) {
  // 获取错误码和错误信息
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  // 记录预测失败的日志
  console.error(`predictIndex failed, code: ${code}, message: ${message}`);
}
```

## IndexSample

索引采样点，描述某一时刻的索引状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 采样点id（例如帧索引），取值范围为所有整数。 |
| timestamp | number | 否 | 否 | 采样点的时间戳，取值范围为所有整数，单位：毫秒。 |
