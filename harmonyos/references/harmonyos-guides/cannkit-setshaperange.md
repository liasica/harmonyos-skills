---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setshaperange
title: SetShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetShapeRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65bddbaae36d036139a5451595ddecc16321df9a29a725e0d23c5563fc5be535
---

## 函数功能

设置shape的变化范围。

## 函数原型

```
1. graphStatus SetShapeRange(const std::vector<std::pair<int64_t,int64_t>> &range);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| range | 输入 | shape代表的变化范围。vector中的每一个元素为一个pair，pair的第一个值为该维度上的dim最小值，第二个值为该维度上dim的最大值。举例如下。  该tensor的shape为{1, 1, -1, 2}，第三个轴的最大值为100，则range可设置为{{1, 1}, {1, 1}, {1, 100}, {2, 2}}。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 函数执行结果。若成功，则该值为GRAPH\_SUCCESS(即0)，其他值则为执行失败。 |

## 异常处理

无

## 约束说明

无
