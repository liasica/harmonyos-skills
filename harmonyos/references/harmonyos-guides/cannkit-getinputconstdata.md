---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputconstdata
title: GetInputConstData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetInputConstData
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56df308d12af6a7b9eb66724e646c88f493f5717a4806d5f936e5e3583a94437
---

## 函数功能

如果指定算子Input对应的节点为Const节点，可调用该接口获取Const节点的数据。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus GetInputConstData(const std::string &dst_name, Tensor &data) const;
2. graphStatus GetInputConstData(const char_t *dst_name, Tensor &data) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dst\_name | 输入 | 输入名称。 |
| data | 输出 | 返回Const节点的数据Tensor。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 如果指定算子Input对应的节点为Const节点且获取数据成功，返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
