---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphbuilder
title: GetSubgraphBuilder
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetSubgraphBuilder
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d6a93ac265661f7409d2827a1abe36a6f273931daf76623ae1ef9547c1347529
---

## 函数功能

根据子图名称获取算子对应的子图构建的函数对象。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
SubgraphBuilder GetSubgraphBuilder(const std::string &name) const;
SubgraphBuilder GetSubgraphBuilder(const char_t *name) const;
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
