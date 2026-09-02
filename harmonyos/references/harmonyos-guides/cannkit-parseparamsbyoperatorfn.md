---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parseparamsbyoperatorfn
title: ParseParamsByOperatorFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > ParseParamsByOperatorFn
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c5d5fa7b9993120c7fb39fe710ebd15ee8d0b51bb7f4b667adc6b885915a3282
---

## 函数功能

注册解析开发者自定义算子属性的函数。

## 函数原型

```cpp
OpRegistrationData &ParseParamsByOperatorFn(const ParseParamByOpFunc &parse_param_by_op_fn)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| parse\_param\_by\_op\_fn | 输入 | 解析开发者自定义算子属性的函数，请参见[回调函数ParseParamByOpFunc](cannkit-parseparamsbyoperatorfn.md#回调函数parseparambyopfunc)。 |

## 回调函数ParseParamByOpFunc

开发者自定义并实现ParseParamByOpFunc类函数，完成原始模型中算子属性到适配AI处理器的模型中属性的映射，将结果填入Operator类中。

```cpp
Status ParseParamByOpFunc(const ge::Operator &op_origin, ge::Operator &op_dest)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_origin | 输入 | 框架定义的Operator类对象，包含解析出的原始模型中自定义算子属性信息，关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
| op\_dest | 输出 | 适配AI处理器的模型中的算子数据结构，保存算子信息。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |

## 约束说明

无

## 调用示例

原始TensorFlow算子与适配AI处理器的算子属性一一映射的场景：

```cpp
REGISTER_CUSTOM_OP("SoftplusGrad")
.FrameworkType(TENSORFLOW)
.OriginOpType("SoftplusGrad")
.ParseParamsByOperatorFn(AutoMappingByOpFn)
.ImplyType(ImplyType::TVM);
```

原始TensorFlow算子与适配AI处理器的算子属性无法一一映射的场景：

```cpp
Status ParseResizeArea(const ge::Operator &op_src, ge::Operator& op)
  {
    AutoMappingByOpFn(op_src, op);
 
    ge::TensorDesc input_tensor = op.GetInputDesc("images");
    input_tensor.SetOriginFormat(ge::FORMAT_NHWC);
    input_tensor.SetFormat(ge::FORMAT_NHWC);
    auto ret = op.UpdateInputDesc("images", input_tensor);
    if(ret != ge::GRAPH_SUCCESS){
        return FAILED;
    }
    ge::TensorDesc output_tensor = op.GetOutputDesc("y");
    output_tensor.SetOriginFormat(ge::FORMAT_NHWC);
    output_tensor.SetFormat(ge::FORMAT_NHWC);
    auto ret_output = op.UpdateOutputDesc("y", output_tensor);
    if(ret_output != ge::GRAPH_SUCCESS){
        return FAILED;
    }
    return SUCCESS;
  }
// register ResizeArea op to GE
REGISTER_CUSTOM_OP("ResizeArea")
  .FrameworkType(TENSORFLOW)
  .OriginOpType("ResizeArea")
  .ParseParamsByOperatorFn(ParseResizeArea)
  .ImplyType(ImplyType::AI_CPU);
```
