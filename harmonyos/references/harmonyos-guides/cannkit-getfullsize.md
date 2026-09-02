---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getfullsize
title: GetFullSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > GetFullSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:47d174cb7abbe6a25f65dbe82f3cb9ca55e6c1e7774b00449a94acf1cead1ef4
---

## 函数功能

获取补维后的dim数。

## 函数原型

```cpp
AxisIndex GetFullSize() const
```

## 参数说明

无

## 返回值

返回补维规则的长度，或者说是补维规则描述的维度。

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType type1("1001");
auto dim_num = type1.GetFullSize(); // dim_num=4
```
