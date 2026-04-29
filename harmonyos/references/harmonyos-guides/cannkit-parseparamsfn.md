---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parseparamsfn
title: ParseParamsFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > ParseParamsFn
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6c6c7c9439dc0840a6014148f3c9a5f543145b9335a12c14d107203319074b7f
---

## 函数功能

注册解析算子属性的函数。

## 函数原型

```
1. OpRegistrationData &ParseParamsFn(const ParseParamFunc &parseParamFn)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| parseParamFn | 输入 | 解析算子属性的函数ParseParamFunc，请参见[回调函数ParseParamFunc](cannkit-parseparamsfn.md#回调函数parseparamfunc)。  针对TensorFlow框架，若原始TensorFlow框架算子属性与适配AI处理器的模型中算子属性一一对应（属性个数与顺序一致），可直接使用[AutoMappingFn](cannkit-automappingfn.md)函数自动实现映射。 |

## 约束说明

对于自定义算子插件，ParseParamsFn后续版本将会废弃，请使用[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)接口进行算子属性的解析。

若开发者已使用ParseParamsFn接口进行了算子插件的开发，请执行如下操作进行新接口适配：

1. 请重新使用[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)接口进行算子插件的开发。
2. 请基于新版本自定义算子样例工程的编译脚本重新进行自定义算子工程的编译。

## 回调函数ParseParamFunc

开发者自定义并实现FusionParseParamFunc类函数，完成原始模型中算子属性到适配AI处理器的模型中算子属性映射，将结果填入Operator类中。

```
1. Status ParseParamFunc(const Message *op_origin, ge::Operator &op_dest)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_origin | 输入 | protobuf格式的数据结构（来源于原始模型的prototxt文件），包含算子属性信息。 |
| op\_dest | 输出 | 适配AI处理器的模型的算子数据结构，保存算子信息。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
