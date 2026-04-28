---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimsrule
title: GetExpandDimsRule
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetExpandDimsRule
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2738d8e74e30150737c36efc2fdefba1b0ce49c612fdb1d018715a7be2f08f4
---

## 函数功能

获取Tensor的补维规则。

## 函数原型

```
1. graphStatus GetExpandDimsRule(AscendString &expand_dims_rule) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| expand\_dims\_rule | 引用输入 | 获取到的补维规则，作为出参。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 获取成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
