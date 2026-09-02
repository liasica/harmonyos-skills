---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-fusionparseparamsfn
title: FusionParseParamsFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > FusionParseParamsFn
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c66911ecec8e23f2fb20e4b9f76a39f9db1af125d8d8f6d910b84b7c390e0e3
---

## 函数功能

注册解析融合算子属性的函数。

## 函数原型

```cpp
OpRegistrationData &FusionParseParamsFn(const FusionParseParamFunc &fusionParseParamFn)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| fusionParseParamFn | 输入 | 解析融合算子属性的函数，请参见[回调函数FusionParseParamFunc](cannkit-fusionparseparamsfn.md#回调函数fusionparseparamfunc)。 |

## 约束说明

对于融合算子插件，FusionParseParamsFn接口后续版本将会废弃，请使用[FusionParseParamsFn（Overload）](cannkit-fusionparseparamsfn-overload.md)接口进行融合算子属性的解析。

## 回调函数FusionParseParamFunc

开发者自定义并实现FusionParseParamFunc类函数，完成原始模型中属性到适配AI处理器的模型中属性的映射，将结果填入Operator类中。

```cpp
Status FusionParseParamFunc(const  vector<const google::protobuf::Message *> &v_op_origin, ge::Operator  &op_dest)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| v\_op\_origin | 输入 | 一组scope内的protobuf格式的数据结构（来源于原始模型的prototxt文件），包含算子属性信息。 |
| op\_dest | 输出 | 融合算子数据结构，保存融合算子信息。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
