---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-math-prediction
title: 使用mathPrediction进行数理预测
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用mathPrediction进行数理预测
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:08+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:42b68f6d76db01b6c685f33be94dbe8e7825f0dabb412197ef31a8da8645fcce
---

从API版本26.0.0版本开始，FAST Kit提供mathPrediction数理预测模块，基于历史采样数据对序列数据进行建模和预测，适用于手势跟踪、动画曲线预测、运动轨迹预估等实时预测场景。

mathPrediction数理预测模块提供智能序列预测（predictIndex）能力：接收一组包含索引和时间戳的采样点数组，基于FAST Kit内置算法预测下一个时刻的索引值。其核心原理是利用时间序列分析技术，对输入的采样点进行趋势拟合与外推，从而实现对未来状态的预测。

## 场景介绍

mathPrediction数理预测模块适用于以下场景：

* **手势跟踪**：根据历史触摸点的位置和时间，预测下一帧触摸点的索引位置，减少触摸跟随延迟。
* **动画曲线预测**：基于动画曲线已有的关键帧索引-时间采样，预测后续帧的索引变化趋势，实现更平滑的动画过渡。
* **运动轨迹预估**：在游戏或交互应用中，根据物体的历史运动轨迹采样，预测其后续位置，提升响应速度。
* **滚动惯性预测**：在列表滚动场景中，根据历史滚动偏移量采样，预测减速阶段的最终停止位置。

## 开发步骤

1. 在调用predictIndex函数之前，必须确保mathPrediction模块已被正确导入，并且传入的IndexSample数组至少包含两个有效的采样点。
2. 导入[mathPrediction](../harmonyos-references/fast-kit-fast-math-prediction.md)模块。
3. 构造[IndexSample](../harmonyos-references/fast-kit-fast-math-prediction.md#indexsample)接口数组，添加至少2个采样点。
4. 调用[predictIndex](../harmonyos-references/fast-kit-fast-math-prediction.md#predictindex)函数进行预测。
5. 获取返回的预测结果。
6. 处理异常情况，例如当采样点少于2个时应抛出异常并记录日志。
7. 注意采样点的时间戳应为单调递增，否则可能导致预测结果不准确。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { mathPrediction } from '@kit.FASTKit';

const DOMAIN = 0x0000;

function mathPredictionTest(): void {
  // 构造至少包含两个采样点的数组，用于预测下一个索引值
  let samples: mathPrediction.IndexSample[] = [
    // 第一个采样点：初始索引为0，时间戳为0
    { index: 0, timestamp: 0 },
    // 第二个采样点：索引为10，时间戳为100
    { index: 10, timestamp: 100 },
    // 第三个采样点：索引为20，时间戳为200
    { index: 20, timestamp: 200 }
  ];
  try {
    // 调用预测函数获取下一个索引值
    const predicted = mathPrediction.predictIndex(samples);
    hilog.info(DOMAIN, 'testTag', 'PredictionFunction predicted=%{public}d', predicted);
  } catch (err) {
    // 捕获并记录预测失败时的错误码和错误信息
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(DOMAIN, 'testTag', 'PredictionFunction failed, code: %{public}d, message: %{public}s', code, message);
  }
}
```
