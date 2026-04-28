---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-subgraphcountregister
title: SubgraphCountRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SubgraphCountRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65e259e3b4d4221f7938e7b5a50f7906a59727fe5fe5f8d81abba68a77a68a33
---

## 函数功能

子图注册。

## 函数原型

```
1. void SubgraphCountRegister(const char_t *ir_name, uint32_t count);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ir\_name | 输入 | 子图名称。 |
| count | 输入 | 动态个数子图场景（子图数量不固定），注册count个数的子图，子图名称是ir\_name\_0 ~ ir\_name\_n， n < count。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
