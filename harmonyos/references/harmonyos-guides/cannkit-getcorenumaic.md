---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenumaic
title: GetCoreNumAic
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreNumAic
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0729bfb2618c6c93d2faf2ddfea5b12065e86a363a79f41d694ed4c3d07e4a41
---

## 函数功能

获取当前硬件平台AI Core中Cube核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Cube核数；非分离架构返回AI Core的核数。

## 函数原型

```
1. uint32_t GetCoreNumAic(void) const;
```

## 参数说明

无

## 返回值

针对Kirin9020系列处理器，Cube、Vector分离架构，返回AI Core上的Cube核数。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. auto aicNum = ascendcPlatform.GetCoreNumAic();
4. auto aivNum = ascendcPlatform.GetCoreNumAiv();
5. // ...按照aivNum切分
6. context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
7. return ret;
8. }
```
