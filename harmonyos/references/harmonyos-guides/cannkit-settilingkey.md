---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settilingkey
title: SetTilingKey
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > SetTilingKey
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f2a1314ff624fdeee8e972226cf39ce63d24191b23bcb7fe49fa7e23037a3951
---

## 函数功能

设置TilingKey。

不同的kernel实现分支可以通过TilingKey来标识，host侧设置TilingKey后，可以选择对应的分支。例如，一个算子在不同的shape下，有不同的算法逻辑，kernel侧可以通过TilingKey来选择不同的算法逻辑，在host侧Tiling算法也有差异，host/kernel侧通过相同的TilingKey进行关联。

## 函数原型

```
1. ge::graphStatus SetTilingKey(const uint64_t tiling_key);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| tiling\_key | 输入 | 需要设置的tiling key。 |

## 返回值

成功时返回“ge::GRAPH\_SUCCESS”。

关于graphStatus定义，请参见[ge::graphStatus](cannkit-gegraphstatus.md)。

## 约束说明

tiling\_key的取值范围在uint64\_t数据类型范围内，但不可以取值为UINT64\_MAX。

## 调用示例

```
1. ge::graphStatus Tiling4XXX(TilingContext* context) {
2. auto ret = context->SetTilingKey(20);
3. // ...
4. }
```
