---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferformatfuncregister
title: InferFormatFuncRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferFormatFuncRegister
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:496098d636f054412846b450f966b5924034b5b96fdd9fdf80286138dced1275
---

## 函数功能

InferFormatFuncRegister构造函数和析构函数。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
InferFormatFuncRegister(const std::string &operator_type, const InferFormatFunc &infer_format_func);
InferFormatFuncRegister(const char_t *const operator_type, const InferFormatFunc &infer_format_func);
~InferFormatFuncRegister() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |
| infer\_format\_func | 输入 | 算子InferFormat函数。 |

## 返回值

InferFormatFuncRegister构造函数返回InferFormatFuncRegister类型的对象。

## 约束说明

算子InferFormat函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
