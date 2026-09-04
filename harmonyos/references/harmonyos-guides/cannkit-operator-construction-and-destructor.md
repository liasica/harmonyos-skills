---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a98ca1b410af8d768046483edd0f6f1c0c0efb2e5fc41805b7e8b5cc77d968b7
---

## 函数功能

Operator构造函数和析构函数。

## 函数原型

![](https://media:401788444102259871) 

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
