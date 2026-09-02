---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-subgraphcountregister
title: SubgraphCountRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SubgraphCountRegister
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:045170df5c52cfd8a5e06c4333b4f545147b97da48b75591bd0d3e937aa9d8a2
---

## 函数功能

子图注册。

## 函数原型

```cpp
void SubgraphCountRegister(const char_t *ir_name, uint32_t count);
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
