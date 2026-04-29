---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorenum
title: GetCoreNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreNum
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad8825107e630596ef06d4b92c6cab30d725fc154da7f357817ace09ab43c070
---

## 函数功能

获取当前硬件平台的核数。若AI Core的架构为Cube、Vector分离架构，返回AI Core上的Vector核数；非分离架构返回AI Core的核数。

## 函数原型

```
1. uint32_t GetCoreNum(void) const;
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
3. auto coreNum = ascendcPlatform.GetCoreNum();
4. // ... 根据核数自行设计Tiling策略
5. context->SetBlockDim(coreNum);
6. return ret;
7. }
```
