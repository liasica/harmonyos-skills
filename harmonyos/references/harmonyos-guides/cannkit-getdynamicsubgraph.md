---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicsubgraph
title: GetDynamicSubgraph
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicSubgraph
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1c84a917bcf1404124093e16fc3292e0ef74d5f3a79eab60104d49f9aeb75c9
---

## 函数功能

根据子图名称和子图索引获取算子对应的动态输入子图。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. Graph GetDynamicSubgraph(const std::string &name, uint32_t index) const;
2. Graph GetDynamicSubgraph(const char_t *name, uint32_t index) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 子图名。 |
| index | 输入 | 同名子图的索引。 |

## 返回值

Graph对象。

## 异常处理

无

## 约束说明

无
