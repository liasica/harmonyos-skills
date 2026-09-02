---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphnames
title: GetSubgraphNames
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraphNames
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:1017d103e380ab31e3d1bdec99c48d2ebca63669a30b752a183665f852a586ef
---

## 函数功能

获取一个算子的子图名称列表。

## 函数原型

**说明** 

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
