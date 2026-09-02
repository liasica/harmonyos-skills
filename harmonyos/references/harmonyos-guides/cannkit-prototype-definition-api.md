---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-prototype-definition-api
title: 原型定义接口（REG_OP）
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > 原型定义接口（REG_OP）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30fadb46499a37bd22a390ffa2dca32fb41fd834c5e08cd796c971ed38ca3cc0
---

## 函数原型

函数原型定义示例如下。

```cpp
REG_OP(xxx)
    .INPUT(x1, type)
    .OPTIONAL_INPUT(x2, type)
    .DYNAMIC_INPUT(x3, type)
    .OUTPUT(y1, type)
    .DYNAMIC_OUTPUT(y3, type)
    .REQUIRED_ATTR(a, type)
    .ATTR(b, type, default_value)
    .GRAPH(z1)
    .DYNAMIC_GRAPH(z2)
    .OP_END_FACTORY_REG(xxx)
```

## 功能说明

定义算子的原型，包括算子的输入、输出、属性以及对应的数据类型。

进行如上算子原型定义后，即相当于向GE注册了该算子的原型，告知GE对应类型的算子应该具备哪些输入、输出与属性；同时相当于定义了一个op::xxx的Class，开发者可以include该原型头文件，然后实例化该Class进行IR模型构建，如下所示：

```cpp
conv = op::Conv2D()
conv.set_input_x(feature_map_data)
conv.set_input_filter(weight_data)
```

## 接口说明

| **接口名称** | **接口说明** | 衍生接口（可用于IR模型构建） |
| --- | --- | --- |
| REG\_OP(x) | 定义一个算子原型，算子类型为x。 | [REG\_OP](cannkit-prototype-definition-derivative-api.md#reg_op) |
| .INPUT(x, type) | 定义输入名称（x）和类型(type)。  类型为TensorType类型，例如：  - TensorType{DT\_FLOAT}  - TensorType({DT\_FLOAT, DT\_INT8})  - TensorType::ALL()  关于TensorType类，请参见[TensorType](cannkit-tensortype.md)。 | [INPUT](cannkit-prototype-definition-derivative-api.md#input) |
| .OPTIONAL\_INPUT(x, type) | 定义可选输入的名称（x）和类型（type）。  类型为TensorType类型，例如：  - TensorType{DT\_FLOAT}  - TensorType({DT\_FLOAT, DT\_INT8})  - TensorType::ALL()  关于TensorType类，请参见[TensorType](cannkit-tensortype.md)。 | [OPTIONAL\_INPUT](cannkit-prototype-definition-derivative-api.md#optional_input) |
| .DYNAMIC\_INPUT(x, type) | 定义动态输入的名称（x）和类型（type）。  类型为TensorType类型，例如：  - TensorType{DT\_FLOAT}  - TensorType({DT\_FLOAT, DT\_INT8})  - TensorType::ALL()  关于TensorType类，请参见[TensorType](cannkit-tensortype.md)。 | [DYNAMIC\_INPUT](cannkit-prototype-definition-derivative-api.md#dynamic_input) |
| .OUTPUT(x, type) | 定义输出的名称（x）和类型（type）。  类型为TensorType类型，例如：  - TensorType{DT\_FLOAT}  - TensorType({DT\_FLOAT, DT\_INT8})  - TensorType::ALL()  关于TensorType类，请参见[TensorType](cannkit-tensortype.md)。 | [OUTPUT](cannkit-prototype-definition-derivative-api.md#output) |
| .DYNAMIC\_OUTPUT(x, type) | 定义动态输出的名称（x）和类型（type）。  类型为TensorType类型，例如：  - TensorType{DT\_FLOAT}  - TensorType({DT\_FLOAT, DT\_INT8})  - TensorType::ALL()  关于TensorType类，请参见[TensorType](cannkit-tensortype.md)。 | [DYNAMIC\_OUTPUT](cannkit-prototype-definition-derivative-api.md#dynamic_output) |
| .REQUIRED\_ATTR(x, type) | 定义必备属性的名称（x）和类型（type）。  type的可选值包括：  - Int，属性类型为int64\_t  - Float, 属性类型为float  - String，属性类型为string  - Bool，属性类型为bool  - Tensor，属性类型为Tensor  - Type，属性为Type枚举定义  - NamedAttrs，属性类型为NamedAttrs  - AscendString，属性类型为AscendString  - ListInt，属性类型为vector<int64\_t>, int64\_t列表  - ListFloat, 属性类型为vector<float>, float列表  - ListString，属性类型为vector<string>，string列表  - ListBool，属性类型为vector<bool>，bool列表  - ListTensor，属性类型为vector<Tensor>，Tensor列表  - Bytes，属性类型为Buffer  - ListType，属性类型为vector<Type>，Type列表  - ListListInt，属性类型为vector<vector<int64\_t>>，2维列表  - ListAscendString，属性类型为vector<AscendString>，AscendString列表  - ListNamedAttrs，属性类型为vector<NamedAttrs>，NamedAttrs列表 | [REQUIRED\_ATTR](cannkit-prototype-definition-derivative-api.md#required_attr) |
| .ATTR(x, type, default\_value) | 定义可选属性的名称、类型以及默认值。  当开发者不设置算子对象的属性时，会使用此处设置的默认值。  type的可选值包括：  - Int，属性类型为int64\_t  - Float, 属性类型为float  - String，属性类型为string  - Bool，属性类型为bool  - Tensor，属性类型为Tensor  - Type，属性为Type枚举定义  - NamedAttrs，属性类型为NamedAttrs  - AscendString，属性类型为AscendString  - ListInt，属性类型为vector<int64\_t>, int64\_t列表  - ListFloat, 属性类型为vector<float>, float列表  - ListString，属性类型为vector<string>，string列表  - ListBool，属性类型为vector<bool>，bool列表  - ListTensor，属性类型为vector<Tensor>，Tensor列表  - Bytes，属性类型为Buffer  - ListType，属性类型为vector<Type>，Type列表  - ListListInt，属性类型为vector<vector<int64\_t>>，2维列表  - ListAscendString，属性类型为vector<AscendString>，AscendString列表  - ListNamedAttrs，属性类型为vector<NamedAttrs>，NamedAttrs列表  定义示例：  - .ATTR(mode, Int, 1)  - .ATTR(pad, ListInt, {0, 0, 0, 0}) | [ATTR](cannkit-prototype-definition-derivative-api.md#attr) |
| .GRAPH(z1) | 注册算子中包含的子图信息，输入z1为子图名称。  例如If算子注册的子图为：  .GRAPH(then\_branch) .GRAPH(else\_branch)  对于同一个算子，注册的算子子图名称需要保持唯一。 | [GRAPH](cannkit-prototype-definition-derivative-api.md#graph) |
| .DYNAMIC\_GRAPH(z2) | 注册动态算子子图信息，输入z2为子图名称。  例如Case算子注册的子图为：  .DYNAMIC\_GRAPH(branches)  对于同一个算子，注册的算子子图名称需要保持唯一。 | [DYNAMIC\_GRAPH](cannkit-prototype-definition-derivative-api.md#dynamic_graph) |
| .INFER\_SHAPE\_AND\_TYPE() | 该接口为历史遗留兼容性接口，当前版本开发者无需使用。 | - |
| .OP\_END\_FACTORY\_REG(x) | 与REG\_OP配对，结束算子原型定义。  算子类型（x）与REG\_OP(x)中的类型相同。 | - |

OpReg类中的OpReg &N()接口的功能是为了开发者进行算子注册的时候，使用.\*\*的方式调用OpReg类的接口，例如.INPUT(x, type)、.OUTPUT(x, type)，无其他含义。

## 返回值

无

## 约束说明

* REG\_OP的算子类型必须全局唯一。
* 同一个算子的输入名称之间不能重复。
* 同一个算子的输出名称之间不能重复。
* 同一个算子的属性名称之间不能重复。

## 调用示例

动态输入的算子原型定义示例：

```cpp
REG_OP(AddN)
    .DYNAMIC_INPUT(x, TensorType::NumberType())
    .OUTPUT(y, TensorType::NumberType())
    .REQUIRED_ATTR(N, Int)
    .OP_END_FACTORY_REG(AddN)
```

多输入的算子原型定义示例：

```cpp
REG_OP(GreaterEqual)
    .INPUT(x1, TensorType::RealNumberType())
    .INPUT(x2, TensorType::RealNumberType())
    .OUTPUT(y, TensorType({DT_BOOL}))
    .OP_END_FACTORY_REG(GreaterEqual)
```

注册子图的算子原型定义示例：

```cpp
REG_OP(If)
    .INPUT(cond, TensorType::ALL())
    .DYNAMIC_INPUT(input, TensorType::ALL())
    .DYNAMIC_OUTPUT(output, TensorType::ALL())
    .GRAPH(then_branch)
    .GRAPH(else_branch)
    .OP_END_FACTORY_REG(If)
```
