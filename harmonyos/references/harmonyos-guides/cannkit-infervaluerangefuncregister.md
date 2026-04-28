---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infervaluerangefuncregister
title: InferValueRangeFuncRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferValueRangeFuncRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34f30cb699e96723e598580ef539be4a8ec2353bd48440dc6d4ad58fb6405f48
---

## 函数功能

InferValueRangeFuncRegister构造函数和析构函数。

## 函数原型

```
1. InferValueRangeFuncRegister(const char_t *const operator_type, const WHEN_CALL when_call,
2. const InferValueRangeFunc &infer_value_range_func);
3. InferValueRangeFuncRegister(const char_t *const operator_type);
4. ~InferValueRangeFuncRegister() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |
| when\_call | 输入 | infer函数的调用场景。 |
| infer\_value\_range\_func | 输入 | 算子inferValueRange函数。 |

## 返回值

InferValueRangeFuncRegister构造函数返回InferValueRangeFuncRegister类型的对象。

## 约束说明

算子InferValueRangeFuncRegister函数注册接口，此接口被其他头文件引用，一般不由算子开发者直接调用。
