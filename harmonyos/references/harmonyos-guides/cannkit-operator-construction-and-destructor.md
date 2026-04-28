---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a48ecae2e913233eef9c5482047bb6806f8370d40abe80938d2f987bc0959db9
---

## 函数功能

Operator构造函数和析构函数。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. Operator()
2. explicit Operator(const std::string &type);
3. explicit Operator(const char_t *type);
4. Operator(const std::string &name, const std::string &type);
5. Operator(const AscendString &name, const AscendString &type);
6. Operator(const char_t *name, const char_t *type);
7. virtual ~Operator() = default;
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
