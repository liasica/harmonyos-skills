---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-get
title: Get
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVectorVector > Get
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6314fc3b9d491b0f6f48cadca21a9fd137d5cddfb1e6f6655a2e1ae451b9a820
---

## 函数功能

获取第index个元素的首地址。

## 函数原型

```cpp
const ContinuousVector *Get(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 元素index。 |

## 返回值

第index个元素的首地址。

## 约束说明

无

## 调用示例

```cpp
// 创建ContinuousVectorVector对象cvv
// ...
// 增加元素
// ...
auto cv = cvv->add(inner_vector_capacity);
// ...
// 获取第0个元素的首地址
auto cv1 = cvv->Get(0U);
```
