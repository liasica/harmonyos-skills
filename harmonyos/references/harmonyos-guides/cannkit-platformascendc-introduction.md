---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-platformascendc-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > 简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6dda44741b2d941a0bae13d953d9a9ba57f725ace802b4165d8bb63a74252251
---

## 函数功能

在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

说明

使用该功能需要包含"tiling/platform/platform\_ascendc.h"头文件。

## 函数原型

```
1. PlatformAscendC() = delete
2. ~PlatformAscendC() = default
3. explicit PlatformAscendC(fe::PlatFormInfos *platformInfo): platformInfo_(platformInfo) {}
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

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. uint64_t ub_size, l1_size;
4. ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
5. ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
6. auto aicNum = ascendcPlatform.GetCoreNumAic();
7. auto aivNum = ascendcPlatform.GetCoreNumAiv();
8. // ... 按照aivNum切分
9. context->SetBlockDim(ascendcPlatform.CalcTschBlockDim(aivNum, aicNum, aivNum));
10. return ret;
11. }
```
