---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settilingcond
title: SetTilingCond
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > SetTilingCond
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d910462e39b31835890b09577f73653f548f72909050c808180a1e79e281eb73
---

## 函数功能

设置tiling cond。

## 函数原型

```
1. ge::graphStatus SetTilingCond(int32_t tiling_cond);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| tiling\_cond | 输入 | 需要设置的tiling cond。 |

## 返回值

设置成功时返回“ge::GRAPH\_SUCCESS”。

关于graphStatus的定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

当前支持的Kirin9020和KirinX90系列处理器是分离架构。

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto ret = context->SetTilingCond(10);
3. // ...
4. }
```
