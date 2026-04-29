---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenumaiv
title: GetCoreNumAiv
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreNumAiv
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:69ed259155f63c271c7734ef4c1abf1b70266f2f45f6ce10e92311e4e2edc592
---

## 函数功能

获取当前硬件平台AI Core中Vector核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

## 函数原型

```
1. uint32_t GetCoreNumAiv(void) const;
```

## 参数说明

无

## 返回值

针对Kirin9020系列处理器，Cube、Vector分离架构，返回AI Core上的Vector核数。

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
