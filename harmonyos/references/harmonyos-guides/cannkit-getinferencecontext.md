---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinferencecontext
title: GetInferenceContext
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetInferenceContext
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4a17a43247b13d2aca780c576a165bde2b0951b0da207a71d33dff5d6b598e2a
---

## 函数功能

获取当前算子传递InferShape推导所需要的关联信息，比如前面算子的shape和DataType信息。

## 函数原型

```
1. InferenceContextPtr GetInferenceContext() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| InferenceContextPtr | 返回当前operator的推理上下文。  InferenceContextPtr是指向InferenceContext类的指针的别名：  using InferenceContextPtr = std::shared\_ptr<InferenceContext> |

## 异常处理

无

## 约束说明

无
