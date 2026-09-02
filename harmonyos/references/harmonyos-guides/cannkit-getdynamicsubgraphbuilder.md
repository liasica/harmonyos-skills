---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicsubgraphbuilder
title: GetDynamicSubgraphBuilder
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicSubgraphBuilder
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f514dc889606409b0ead3cfbf4d413ca3c9d20cb79e9f8cd207dd21732648ba5
---

## 函数功能

根据子图名称和子图索引获取算子对应的动态输入子图的构建函数对象。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
SubgraphBuilder GetDynamicSubgraphBuilder(const std::string &name, uint32_t index) const;
SubgraphBuilder GetDynamicSubgraphBuilder(const char_t *name, uint32_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 子图名。 |
| index | 输入 | 同名子图的索引。 |

## 返回值

SubgraphBuilder对象。

## 异常处理

无

## 约束说明

无
