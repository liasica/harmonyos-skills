---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapefuncregister
title: InferShapeFuncRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferShapeFuncRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0cb1b0f8566a41a4ecd88e94491997ebd06cb1bb282ae9d2dae96e9d9adc90ed
---

## 函数功能

InferShapeFuncRegister构造函数和析构函数。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. InferShapeFuncRegister (const std::string &operator_type, const InferShapeFunc &infer_shape_func);
2. InferShapeFuncRegister(const char *const operator_type, const InferShapeFunc &infer_shape_func);
3. ~ InferShapeFuncRegister()
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |
| infer\_shape\_func | 输入 | 算子InferShape函数。 |

## 返回值

InferShapeFuncRegister构造函数返回InferShapeFuncRegister类型的对象。

## 约束说明

算子InferShape函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
