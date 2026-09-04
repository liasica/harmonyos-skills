---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-platformascendc-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > 简介
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:762def88741fbcb227617cc974117810cf9dc199002fd07b02850d4623a6f389
---

## 函数功能

在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

![](https://media:401788444101532868) 

使用该功能需要包含"tiling/platform/platform\_ascendc.h"头文件。

## 函数原型

```cpp
PlatformAscendC() = delete
~PlatformAscendC() = default
explicit PlatformAscendC(fe::PlatFormInfos *platformInfo): platformInfo_(platformInfo) {}
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| platformInfo | 输入 | platformInfo结构体，通过[GetPlatformInfo](cannkit-getplatforminfo.md)接口可以获取。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t ub_size, l1_size;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
    auto aicNum = ascendcPlatform.GetCoreNumAic();
    auto aivNum = ascendcPlatform.GetCoreNumAiv();
    // ... 按照aivNum切分
    context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
    return ret;
}
```
