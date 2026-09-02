---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tbuf-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBuf > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e5f3be7aa7c644e7fa929f2a5acfa5528b34c65c03d5275c7b3ba1dcd563e752
---

## 函数功能

创建TBuf对象时，初始化数据成员。

## 函数原型

```cpp
template <TPosition pos> 
__aicore__ inline TBuf();
```

## 参数说明

| 参数名称 | 含义 |
| --- | --- |
| pos | TBuf所在的逻辑位置，取值为VECCALC。关于TPosition的具体介绍请参考[TPosition](cannkit-tposition.md)。 |

## 约束说明

无
