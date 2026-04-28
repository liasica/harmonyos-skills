---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Allocator > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e8cb6353f60dcd52951d089ab2c75663bc34388262d5266b727abffe0dbc5f7
---

## 函数功能

Allocator构造函数和析构函数。

## 函数原型

```
1. Allocator() = default;
2. virtual ~Allocator() = default;
3. Allocator(const Allocator &) = delete;
4. Allocator &operator=(const Allocator &) = delete;
```

## 参数说明

无

## 返回值

无

## 异常处理

无

## 约束说明

虚基类需要开发者派生。
