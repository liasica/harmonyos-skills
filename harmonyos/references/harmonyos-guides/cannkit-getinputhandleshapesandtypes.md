---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputhandleshapesandtypes
title: GetInputHandleShapesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetInputHandleShapesAndTypes
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d20627dcbd36493d00214b382ca00b00093607f569e554d7eabebf8ed89831a4
---

## 函数功能

在推理上下文中，获取算子输入句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。

## 函数原型

```cpp
const std::vector<std::vector<ShapeAndType>> &GetInputHandleShapesAndTypes() const
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
