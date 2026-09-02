---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tbufpool-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBufPool > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:889df92ee7a1ea87ce476024b8eea3c20a417f11aba5aa110379127ad1238ac1
---

## 函数功能

创建TBufPool对象时，初始化数据成员。

## 函数原型

```cpp
template <TPosition pos, uint32_t bufIDSize = 4> 
__aicore__ inline TBufPool();
```

## 参数说明

| 参数名称 | 含义 |
| --- | --- |
| pos | TBufPool逻辑位置，可以为VECIN、VECOUT、VECCALC、A1、B1、C1。关于TPosition的具体介绍请参考[TPosition](cannkit-tposition.md)。 |
| bufIDSize | TBufPool可分配Buffer数量，默认为4，不超过16。 |

## 约束说明

无
