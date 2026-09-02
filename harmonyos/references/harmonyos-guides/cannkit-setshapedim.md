---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setshapedim
title: SetShapeDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetShapeDim
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6fd0b6e62e862eff58bce3b5d60b90d363e2c27a8a737c4fae86d0afa77efa4
---

## 函数功能

设置shape第idx维度。

## 函数原型

```cpp
graphStatus SetShapeDim(const size_t idx, const int64_t dim_value);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| idx | 输入 | 维度的索引，索引从0开始。 |
| dim\_value | 输入 | 需设置的值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
