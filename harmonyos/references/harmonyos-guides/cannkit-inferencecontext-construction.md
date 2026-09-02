---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferencecontext-construction
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ec3329583122f27b75888f1be4021a8c908c1376c171f49d481657385373faa
---

## 函数功能

InferenceContext对象的构造函数和析构函数。

## 函数原型

```cpp
~InferenceContext() = default;
InferenceContext(const InferenceContext &context) = delete;
InferenceContext(const InferenceContext &&context) = delete;
InferenceContext &operator=(const InferenceContext &context) = delete;
InferenceContext &operator=(const InferenceContext &&context) = delete;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| context | 输入 | InferenceContext内容，供初始化使用。 |

## 返回值

InferenceContext构造函数返回InferenceContext类型的对象。

## 异常处理

无

## 约束说明

无
