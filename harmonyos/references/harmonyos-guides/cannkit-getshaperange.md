---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshaperange
title: GetShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetShapeRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45c7eb76b59a1f2b065e0ec2f63403b391cafce76b0dcbbbe1acd4db88ac831e
---

## 函数功能

获取设置的shape变化范围。

## 函数原型

```
1. graphStatus GetShapeRange(std::vector<std::pair<int64_t,int64_t>> &range) const;
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
