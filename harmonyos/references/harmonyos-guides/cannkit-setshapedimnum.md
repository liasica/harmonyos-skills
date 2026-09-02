---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setshapedimnum
title: SetShapeDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetShapeDimNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a2c21f4fa72f30e86ec147b2a7280c33787b6f22a8db23713cdfa2c0aa52a68
---

## 函数功能

设置shape的维度大小，即rank大小。

## 函数原型

```cpp
graphStatus SetShapeDimNum(const size_t dim_num);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dim\_num | 输入 | shape的维度大小，即原始shape的rank。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
