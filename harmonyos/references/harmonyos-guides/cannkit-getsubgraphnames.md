---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphnames
title: GetSubgraphNames
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraphNames
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:1117cfae5dcdf7241b0fe042c9db68bc3bad757873be99a89e90022ad75d8bc2
---

## 函数功能

获取一个算子的子图名称列表。

## 函数原型

![](https://media:401788444114462930) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::vector<std::string> GetSubgraphNames() const;
graphStatus GetSubgraphNames(std::vector<AscendString> &names) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| names | 输出 | 返回一个子图名称的列表。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
