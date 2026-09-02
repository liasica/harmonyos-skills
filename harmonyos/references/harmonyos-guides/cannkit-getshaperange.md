---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshaperange
title: GetShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetShapeRange
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e2c1458b5b2434eec471ab946745b82e1a252c5bdd151a6e812a66b04fa6155a
---

## 函数功能

获取设置的shape变化范围。

## 函数原型

```cpp
graphStatus GetShapeRange(std::vector<std::pair<int64_t,int64_t>> &range) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| range | 输出 | 设置过的shape变化范围。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 函数执行结果。若成功，则该值为GRAPH\_SUCCESS(即0)，其他值则为执行失败。 |

## 异常处理

无

## 约束说明

无
