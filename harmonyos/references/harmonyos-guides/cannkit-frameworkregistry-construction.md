---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworkregistry-construction
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > FrameworkRegistry > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:326d56b21983bbb8b095a72cea753eef1d09d67939d50890ed7eaa06c2c4e4c1
---

## 函数功能

FrameworkRegistry构造函数和析构函数。

## 函数原型

```cpp
FrameworkRegistry(const FrameworkRegistry &) = delete;
FrameworkRegistry& operator = (const FrameworkRegistry &) = delete;
~FrameworkRegistry();
static FrameworkRegistry& Instance();
```

## 参数说明

无

## 返回值

Instance()返回FrameworkRegistry的单例对象。

## 异常处理

无

## 约束说明

无
