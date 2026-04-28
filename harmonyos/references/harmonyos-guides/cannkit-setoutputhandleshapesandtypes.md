---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoutputhandleshapesandtypes
title: SetOutputHandleShapesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > SetOutputHandleShapesAndTypes
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d20afa1097677b5c72c980169089d029e747cfbe48f1452c5357e78d3b2e431e
---

## 函数功能

在推理上下文中，设置算子输出句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。

## 函数原型

```
1. void SetOutputHandleShapesAndTypes(const std::vector<std::vector<ShapeAndType>> &shapes_and_types)
2. void SetOutputHandleShapesAndTypes(std::vector<std::vector<ShapeAndType>> &&shapes_and_types)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| shapes\_and\_types | 输入 | 算子输出句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
