---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Allocator > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9237ce396a6b7c3665d9b7d857bf7e1154277bd8c775a92198dfdf9507bb627f
---

## 函数功能

Allocator构造函数和析构函数。

## 函数原型

```cpp
Allocator() = default;
virtual ~Allocator() = default;
Allocator(const Allocator &) = delete;
Allocator &operator=(const Allocator &) = delete;
```

## 参数说明

无

## 返回值

无

## 异常处理

无

## 约束说明

虚基类需要开发者派生。
