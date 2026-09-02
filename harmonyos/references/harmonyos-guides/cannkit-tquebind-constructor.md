---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tquebind-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:084f175106f6295f834fcaf46826ac58f95cc3906aa91f9df0cc217f09f9445d
---

## 函数功能

创建TQueBind对象。

## 函数原型

```cpp
template <TPosition src, TPosition dst, int32_t depth, auto mask = 0> 
__aicore__ inline TQueBind();
```

## 参数说明

| 参数名称 | 含义 |
| --- | --- |
| src | 源逻辑位置，支持的TPosition可以为VECIN、VECOUT、A1、A2、B1、B2、CO1、CO2。关于TPosition的具体介绍请参考[TPosition](cannkit-tposition.md)。支持的src和dst组合请参考[简介](cannkit-overview.md)表1。 |
| dst | 目的逻辑位置，TPosition可以为VECIN、VECOUT、A1、A2、B1、B2、CO1、CO2。 |
| depth | TQue的深度，一般不超过4。 |
| mask | 如果开发者在某一个Que上，数据搬运的时候需要做转换，可以设置为0或1。一般不需要开发者配置，默认为0。  设置为0，代表数据格式从ND转换为NZ，目前仅支持TPosition为A1或B1。 |

## 约束说明

无
