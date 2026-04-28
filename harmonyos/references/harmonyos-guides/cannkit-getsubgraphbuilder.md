---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphbuilder
title: GetSubgraphBuilder
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraphBuilder
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eb16fb2fc2f2c958e7ba0d253556008800a2e839888fca52e0c173f8f8fb0d64
---

## 函数功能

根据子图名称获取算子对应的子图构建的函数对象。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. SubgraphBuilder GetSubgraphBuilder(const std::string &name) const;
2. SubgraphBuilder GetSubgraphBuilder(const char_t *name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 子图名称。 |

## 返回值

SubgraphBuilder对象。

## 异常处理

无

## 约束说明

无
