---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinferencecontext
title: SetInferenceContext
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > SetInferenceContext
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a3aa54b6d4848789470a456c3466477d09026c9409f952c20a42df78ac15403
---

## 函数功能

向当前算子传递InferShape推导所需要的关联信息，比如前面算子的shape和DataType信息。

## 函数原型

```
1. void SetInferenceContext(const InferenceContextPtr &inference_context);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| inference\_context | 输入 | 当前operator的推理上下文。  InferenceContextPtr是指向InferenceContext类的指针的别名：  using InferenceContextPtr = std::shared\_ptr<InferenceContext>; |

## 返回值

无

## 异常处理

无

## 约束说明

无
