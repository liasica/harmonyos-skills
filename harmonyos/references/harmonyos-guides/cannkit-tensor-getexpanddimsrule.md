---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getexpanddimsrule
title: GetExpandDimsRule
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetExpandDimsRule
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bd508b79b4082771f907d82ed687ee33527cf1b04d781947efeaa16c40d5397a
---

## 函数功能

获取Tensor的补维规则。

## 函数原型

```cpp
graphStatus GetExpandDimsRule(AscendString &expand_dims_rule) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| expand\_dims\_rule | 输入 | 函数待返回的expand\_dims\_rule补维规则，采用字符串形式表示补维。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
