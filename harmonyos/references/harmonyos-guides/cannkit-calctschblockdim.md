---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-calctschblockdim
title: CalcTschBlockDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > CalcTschBlockDim
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5cf24a949f9cd2c85b2352eeec0ad35f580591a75072f987984c731e3c59dcb
---

## 函数功能

针对Cube、Vector分离架构，用于计算Cube、Vector融合算子的blockDim。针对Vector/Cube融合计算的算子，启动时，按照AIV和AIC组合启动，blockDim用于设置启动多少个组合执行，比如某款AI处理器上有40个Vector和20个Cube核。一个组合是2个Vector和1个Cube核，建议设置为20，此时会启动20个组合，即40个Vector和20个Cube核。使用该接口可以自动获取合适的blockDim值。

获取该值后，使用[SetBlockDim](cannkit-setblockdim.md)进行blockDim的设置。

## 函数原型

```
1. uint32_t CalcTschBlockDim(uint32_t sliceNum, uint32_t aicCoreNum, uint32_t aivCoreNum) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| sliceNum | 输入 | 数据切分的份数。 |
| aicCoreNum | 输入 | 如果算子实现使用了矩阵计算API，请传入[GetCoreNumAic](cannkit-getcorenumaic.md)返回的数量，否则传入0。 |
| aivCoreNum | 输入 | 如果算子实现使用了矢量计算API，请传入[GetCoreNumAiv](cannkit-getcorenumaiv.md)返回的数量，否则传入0。 |

## 返回值

返回用于底层任务调度的核数。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. auto aicNum = ascendcPlatform.GetCoreNumAic();
4. auto aivNum = ascendcPlatform.GetCoreNumAiv();
5. // ...按照aivNum切分数据，并进行计算
6. uint32_t sliceNum = aivNum;
7. context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(sliceNum, aicNum, aivNum));
8. return ge::GRAPH_SUCCESS;
9. }
```
