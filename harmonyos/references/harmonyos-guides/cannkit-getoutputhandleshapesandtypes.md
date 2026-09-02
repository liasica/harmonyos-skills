---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputhandleshapesandtypes
title: GetOutputHandleShapesAndTypes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetOutputHandleShapesAndTypes
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d435f0552f1f709b61f5c2c569f08d24334c050c3cc7f030fb10bb786080248
---

## 函数功能

在推理上下文中，获取算子输出句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。

## 函数原型

```cpp
const std::vector<std::vector<ShapeAndType>> &GetOutputHandleShapesAndTypes() const
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| const std::vector<std::vector<ShapeAndType>> | 算子输出句柄的[ShapeAndType](cannkit-shapeandtype-construction-and-destructor.md)。 |

## 异常处理

无

## 约束说明

无
