---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputhandleshapesandtypes
title: GetInputHandleShapesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetInputHandleShapesAndTypes
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e323b6d64ba8c9dd057b7e5fa6339fb8f42317febc506e224580901ee109faf2
---

## 函数功能

在推理上下文中，获取算子输入句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。

## 函数原型

```
1. const std::vector<std::vector<ShapeAndType>> &GetInputHandleShapesAndTypes() const
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| const std::vector<std::vector<ShapeAndType>> | 算子输入句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。 |

## 异常处理

无

## 约束说明

无
