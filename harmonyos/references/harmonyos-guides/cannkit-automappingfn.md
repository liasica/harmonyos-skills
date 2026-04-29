---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingfn
title: AutoMappingFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > AutoMappingFn
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c88c5ad57d83223ee6626034c1d8f3b44c70f91699a48cf21c82fe2657ea1ad
---

## 函数功能

自动映射回调函数。

## 函数原型

```
1. Status AutoMappingFn(const google::protobuf::Message *op_src, ge::Operator &op)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_src | 输入 | 转换前原始模型中的算子，包含原始模型中算子的属性。 |
| op | 输入 | 适配AI处理器的算子。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |

## 约束说明

若原始TensorFlow算子与适配AI处理器的算子属性无法一一映射，AutoMappingFn函数无法应用于回调函数[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)中，此种场景下，请在回调函数中使用[AutoMappingByOpFn](cannkit-automappingbyopfn.md)接口进行可以映射成功的属性的自动解析，使用示例请参见[调用示例](cannkit-automappingbyopfn.md#调用示例)。
