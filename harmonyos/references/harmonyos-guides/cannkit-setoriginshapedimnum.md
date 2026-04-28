---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoriginshapedimnum
title: SetOriginShapeDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetOriginShapeDimNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c053c70a61f85abcb9a84aef063eeb4c273ca1cff1fbf337a2cfc6e8ae62ee45
---

## 函数功能

设置原始shape的维度大小，即rank大小。

## 函数原型

```
1. graphStatus SetOriginShapeDimNum(const size_t dim_num);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dim\_num | 输入 | 原始shape的维度大小，即原始shape的rank。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
