---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorc
title: operator[]
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > operator[]
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:60f16909ca84c11291b3c2f106673d60b7d703834f25898f77780ecb5d782572
---

## 函数功能

获取指定index轴的dim值。

## 函数原型

```cpp
const int64_t &operator[](size_t idx) const
int64_t &operator[](size_t idx)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| idx | 输入 | dim的index，调用者需要保证index合法。 |

## 返回值

* const int64\_t &operator[](size\_t idx) const：dim值，在idx>=kMaxDimNum时，行为未定义。
* int64\_t &operator[](size\_t idx)：dim值，在idx>=kMaxDimNum时，行为未定义。

## 约束说明

调用者需要保证index合法，即idx<kMaxDimNum。

## 调用示例

```cpp
Shape shape0({3, 256, 256});
auto dim0 = shape0[0]; // 0轴的维度大小为3
auto dim1 = shape0[1]; // 1轴的维度大小为256
auto dim2 = shape0[2]; // 2轴的维度大小为256
auto invalid_dim = shape0[kMaxDimNum]; // 行为未定义
```
