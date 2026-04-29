---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-frameworkregistry-construction
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > FrameworkRegistry > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ddc42c8309e713202ff51e4e7e3557379bf765d28d81c2170307ab90a087e5f5
---

## 函数功能

FrameworkRegistry构造函数和析构函数。

## 函数原型

```
1. FrameworkRegistry(const FrameworkRegistry &) = delete;
2. FrameworkRegistry& operator = (const FrameworkRegistry &) = delete;
3. ~FrameworkRegistry();
4. static FrameworkRegistry& Instance();
```

## 参数说明

NA

## 返回值

Instance()返回FrameworkRegistry的单例对象。

## 异常处理

无

## 约束说明

无
