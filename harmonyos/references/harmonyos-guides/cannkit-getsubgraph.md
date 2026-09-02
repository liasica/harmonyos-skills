---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraph
title: GetSubgraph
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraph
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d546a833762e9da008d763b30824d9999d2c27817657e3eb246d92151f6e781
---

## 函数功能

根据子图名称获取算子对应的子图。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
Graph GetSubgraph(const std::string &name) const;
Graph GetSubgraph(const char_t *name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 子图名称。 |

## 返回值

Graph对象。

## 异常处理

无

## 约束说明

无
