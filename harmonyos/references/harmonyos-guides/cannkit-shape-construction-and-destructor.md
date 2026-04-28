---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Shape > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b7143762495f2cd7961f4697afa4189a7579ad6e36ad113d988bc45a232c017
---

## 函数功能

Shape构造函数和析构函数。

## 函数原型

```
1. Shape();
2. ~Shape() = default;
3. explicit Shape(const std::vector<int64_t> &dims);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dims | 输入 | Shape的取值内容。  Shape表征张量数据的维度大小，用std::vector<int64\_t>表征每一个维度的具体大小。 |

## 返回值

Shape构造函数返回Shape类型的对象。

## 异常处理

无

## 约束说明

无
