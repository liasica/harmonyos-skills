---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d06b59544a54ab7d10f31b6cdc1daa0bb53b12651936f8ec5462c0ef309c4af
---

## 函数功能

Operator构造函数和析构函数。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
Operator()
explicit Operator(const std::string &type);
explicit Operator(const char_t *type);
Operator(const std::string &name, const std::string &type);
Operator(const AscendString &name, const AscendString &type);
Operator(const char_t *name, const char_t *type);
virtual ~Operator() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| type | 输入 | 算子类型。 |
| name | 输入 | 算子名称。 |

## 返回值

Operator构造函数返回Operator类型的对象。

## 异常处理

无

## 约束说明

无
