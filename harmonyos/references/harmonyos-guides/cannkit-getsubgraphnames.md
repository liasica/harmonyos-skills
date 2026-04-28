---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphnames
title: GetSubgraphNames
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraphNames
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:526e0d9df988e02a2eef86b7eede50323bea826225bf06cff5516168fff0870c
---

## 函数功能

获取一个算子的子图名称列表。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. std::vector<std::string> GetSubgraphNames() const;
2. graphStatus GetSubgraphNames(std::vector<AscendString> &names) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| names | 输出 | 获取一个算子的子图名称列表。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | GRAPH\_FAILED：失败。  GRAPH\_SUCCESS：成功。 |

## 异常处理

无

## 约束说明

无
