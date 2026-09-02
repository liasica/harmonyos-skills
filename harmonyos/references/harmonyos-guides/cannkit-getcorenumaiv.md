---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenumaiv
title: GetCoreNumAiv
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreNumAiv
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:b2eb10df989c1a363aaa478046dd2525f27040f0a99053b5bae5537ec6d8af8a
---

## 函数功能

获取当前硬件平台AI Core中Vector核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

## 函数原型

```cpp
uint32_t GetCoreNumAiv(void) const;
```

## 参数说明

无

## 返回值

若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

目前涉及分离架构的处理器包括：Kirin9020系列处理器、Kirin9030系列处理器。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    auto aicNum = ascendcPlatform.GetCoreNumAic();
    auto aivNum = ascendcPlatform.GetCoreNumAiv();
    // ...按照aivNum切分
    context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
    return ret;
}
```
