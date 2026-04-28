---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdim
title: GetDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > GetDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87e0255dc6d2446371949113e7bd91729633497cccb011fbcb28af1034bab55c
---

## 函数功能

获取对应idx轴的dim值。

## 函数原型

```
1. int64_t GetDim(const size_t idx) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| idx | 输入 | dim的index，调用者需要保证index合法。 |

## 返回值

dim值，在idx>=kMaxDimNum时，返回kInvalidDimValue。

## 约束说明

调用者需要保证index合法，即idx<kMaxDimNum。

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. auto dim0 = shape0.GetDim(0); // 3
3. auto invalid_dim = shape0.GetDim(kMaxDimNum); // kInvalidDimValue
```
