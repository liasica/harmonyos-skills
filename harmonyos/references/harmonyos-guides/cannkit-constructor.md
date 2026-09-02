---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > RuntimeAttrs > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3dd05f4b2abf192256d90dbe71c09717b8107fe7000323a3caaa3109b984a770
---

## 函数功能

RuntimeAttrs类的构造函数。

## 函数原型

```cpp
RuntimeAttrs() = delete;
RuntimeAttrs(const RuntimeAttrs &) = delete;
RuntimeAttrs(RuntimeAttrs &&) = delete;
RuntimeAttrs &operator=(const RuntimeAttrs &) = delete;
RuntimeAttrs &operator=(RuntimeAttrs &&) = delete;
```

## 参数说明

无

## 返回值

无

## 约束说明

POD类型，当前不允许通过调用构造函数显式构造，可通过显式申请内存构造。
