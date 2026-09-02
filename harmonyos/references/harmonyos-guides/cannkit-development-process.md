---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-development-process
title: 开发流程
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子部署 > 算子入图（GE图）开发 > 开发流程
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:05+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:915d62b9620d8df677b2131556d6a71b0fa7c868e87b11b23596515d903bf0d5
---

该开发流程以[工程化算子开发](cannkit-overview-of-engineering-operator.md)为基础，除了需要提供[算子实现](cannkit-operator-prototype-definition.md)中的算子实现文件外，还需要额外交付算子入图的代码文件。本节仅提供算子入图代码文件的开发指导。

假设下图是我们需要使用的网络模型，开发者可能会想直接逐个算子调用，根据输入tensor得到输出tensor就可以完成网络的运行，但在图模式场景下，实际的网络模型生成过程中，会先进行tensor shape以及datatype的推导。这样可以让我们在图执行之前，就知道各tensor的数据类型和形状，提前校验其正确性；同时提前推导出算子的输出张量描述，包括张量的形状、数据类型及数据排布格式等信息，算子构图准备阶段就可以为所有的张量静态分配内存，避免动态内存分配带来的开销。

下面的网络模型经过shape和datatype推导之后，可以得到灰色底纹框中的推导信息。

**图1** shape与datatype推导示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/oeVWBWxBTXq-Zu2gQ6SvwA/zh-cn_image_0000002736314421.png)

除了tiling实现外，算子入图时需要额外提供的实现代码有以下几种：

* datatype推导：根据算子的输入datatype、算子逻辑及算子属性等信息，推理出算子的输出张量datatype。
* shape推导：根据算子的输入shape、算子逻辑及算子属性等信息，推理出算子的输出张量shape。
* 声明数据依赖：部分算子在InferShape时，需要依赖某个输入的具体值才可以进行，这类算子被称为“数据依赖算子”，对应的输入被称为“数据依赖输入”。该类算子在注册时，需要声明其数据依赖输入。

下表列出了不同类型的算子对上述实现代码的要求。

**表1** 不同的类型的算子对入图实现代码的要求

| 分类 | 对入图实现代码的要求 |
| --- | --- |
| 根据输入shape可以推导出输出shape。 | - shape推导  - datatype推导 |
| 依赖输入的value才能推导出输出shape，即数据依赖算子。 如Reshape算子，依赖shape输入的value才能推导出输出shape。 | - shape推导  - datatype推导  - 声明数据依赖 |

实际开发时通过固定的datatype和shape推导原型实现推导函数，然后再通过[SetInferShape](cannkit-setinfershape.md)、[SetInferDataType](cannkit-setinferdatatype.md)接口来关联对应的shape推导函数，样例如下。

```cpp
namespace ge {
static graphStatus InferShape(gert::InferShapeContext *context)
{
    // ...
    return GRAPH_SUCCESS;
}
 
static graphStatus InferDataType(gert::InferDataTypeContext *context)
{
    // ...
    return ge::GRAPH_SUCCESS;
}
} // namespace ge
 
 
namespace ops {
class AddCustom : public OpDef {
public:
    AddCustom(const char* name) : OpDef(name)
    {
        this->Input("x")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Input("y")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        this->Output("z")
            .ParamType(REQUIRED)
            .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
            .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
        // 根据开发者的算子调用方式决定需不需要注册 图模式调用方式下需要
        this->SetInferShape(ge::InferShape);
       this->SetInferDataType(ge::InferDataType);
        this->AICore()
            .SetTiling(optiling::TilingFunc);
        // 请替换为实际的Kirin AI处理器型号
        this->AICore().AddConfig("ascendxxx");
    }
};
OP_ADD(AddCustom);
} // namespace ops
```

## datatype推导

以AddCustom算子为例，InferDataType的实现如下所示。该样例中输出tensor的数据类型与输入tensor的数据类型相同，所以直接将任意一个输入tensor的数据类型赋给输出tensor即可。

```cpp
namespace ge {
static graphStatus InferDataType(gert::InferDataTypeContext* context)
{
    const auto inputDataType = context->GetInputDataType(0);
    context->SetOutputDataType(0, inputDataType);
    return ge::GRAPH_SUCCESS;
}
} // namespace ge
```

如下示例则给出了更灵活的datatype推导样例，当输入的数据类型为DT\_INT4时，其输出的数据类型为DT\_INT32。

```cpp
ge::graphStatus InferDataTypeForFoo(gert::InferDataTypeContext* context) {
 
    if (context->GetInputDataType(0) == DT_INT4) {
        context->SetOutputDataType(0, DT_INT32);
    }
    return ge::GRAPH_SUCCESS;
}
```

## shape推导

简单的shape推导逻辑可以使用[Follow](cannkit-follow.md)接口来表达，比如输出shape和输入shape相同的情况。示例如下。

输出“y1”Follow输入“x1”场景，指定Follow模式为SHAPE，此时“y1”的shape将会和“x1”保持一致。

```cpp
this->Input("x1")
    .ParamType(REQUIRED)
    .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
    .Format({ge::FORMAT_ND, ge::FORMAT_ND});
this->Input("x2")
    .ParamType(REQUIRED)
    .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
    .Format({ge::FORMAT_ND, ge::FORMAT_ND});
this->Output("y1")
    .ParamType(REQUIRED)
    .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
    .Format({ge::FORMAT_ND, ge::FORMAT_ND})
    .Follow("x1", FollowType::SHAPE);
```

无法在原型定义中通过Follow表达的情况需要开发者编写InferShape函数，其原型是确定的，接受一个[InferShapeContext](cannkit-infershapecontext-getinputshape.md)作为输入，从此context上可以获取到输入、输出的shape指针等内容。输入shape为const类型，因此InferShape时，输入shape是只读、不允许修改的。InferShape成功后，返回ge::GRAPH\_SUCCESS，其他返回值被认为推导失败。推导失败后，执行过程结束退出。

以Reshape算子为例，InferShape的实现如下所示。根据第1个输入（shape输入）的值，Reshape算子将第0个输入（x输入）的shape做变换，并输出到其第0个输出（y输出）上。Reshape的InferShape实现为：

```cpp
ge::graphStatus InferShapeForReshape(InferShapeContext *context) {
const gert::Shape *x_shape = context->GetInputShape(0); // 获取第0个输入的shape
const gert::Tensor *shape_tensor = context->GetInputTensor(1); // 获取第1个输入的tensor
gert::Shape *output_shape = context->GetOutputShape(0);
if (x_shape == nullptr || shape_tensor == nullptr || output_shape == nullptr) {
    // 防御式编程，不应该出现的场景，打印错误并返回失败
    return ge::GRAPH_FAILED;
}
 
auto reshape_size = static_cast<int32_t>(shape_tensor->GetShapeSize());
if (reshape_size < 1) {
    // 防御式编程，不应该出现的场景，打印错误并返回失败
    return ge::GRAPH_FAILED;
}
 
// 根据原型信息，Reshape的shape输入支持INT32与INT64两类，根据不同的类型进入对应的模板函数中做真正的shape变换操作
if (shape_tensor->GetDataType() == ge::DT_INT32) {
    int32_t *reshape_data = shape_tensor->GetData<int32_t>();
    return ReshapeInferShapeImpl<int32_t>(reshape_data, *x_shape, *output_shape, reshape_size);
} else {
    int64_t *reshape_data = shape_tensor->GetData<int64_t>();
    return ReshapeInferShapeImpl<int64_t>(reshape_data, *x_shape, *output_shape, reshape_size);
}
}
```

[InferShapeContext](cannkit-infershapecontext-getinputshape.md) public继承自[ExtendedKernelContext](cannkit-getinputdesc.md)，因此ExtendedKernelContext中提供的方法如获取算子type、name、属性等接口均可以在[InferShapeContext](cannkit-infershapecontext-getinputshape.md)实例中调用。

**说明** 

* InferShape推导函数和使用Follow接口去Follow shape不能混用，即不支持部分输出采用InferShape推导、部分输出采用Follow推导的情况。若开发者同时使用了InferShape函数和Follow接口，以开发者的InferShape函数为准，需要保证在InferShape函数中能够推导出所有的输出shape。
* 为了效率考虑，调用InferShape函数时，框架不会为输出shape做初始化，因此，在InferShape函数中，可以认为输出是**未初始化**的状态。如果在InferShape时，希望通过Append方式操作输出shape，需要先将输出shape的DimNum清零，以防止出现未定义行为。

## InferShape时获取属性、输入

在InferShape、Tiling时，可以通过context实例获取算子IR属性值，所谓IR属性，是指在IR注册时定义的属性，以TransData算子为例：

```cpp
namespace ops {
class TransData : public OpDef {
public:
    explicit TransData(const char *name) : OpDef(name)
    {
        this->Input("src")
             // ...
        this->Output("dst")
             // ...
        this->Attr("src_format")
            .AttrType(REQUIRED)
            .String();
        this->Attr("dst_format")
            .AttrType(REQUIRED)
            .String();
        this->Attr("group")
            .AttrType(OPTIONAL)
           .Int(1);
        // ...
    }
};
OP_ADD(TransData);
} // namespace ops
```

其原型定义中声明了src\_format、dst\_format、group三个属性，可以通过如下方式获取算子属性：

```cpp
ge::graphStatus ExampleGetTransDataAttr(TilingContext *context) {
  // 获取所有属性
  const RuntimeAttrs *attrs = context->GetAttrs();
  ASSERT_NOT_NULL(attrs);
   
  // 按照在原型定义中的顺序，使用index获取属性，index从0开始计数
  const char *src_format = attrs->GetAttrPointer<char>(0); // 获取src_format，src_format是第一个属性，因此index为0
  const char *dst_format = attrs->GetAttrPointer<char>(1); // 获取dst_format，dst_format是第二个属性，因此index为1
  const int64_t group = attrs->GetAttrPointer<int64_t>(2); // 获取group，group是第三个属性，因此index为2
   
  return ge::GRAPH_SUCCESS;
}
```

## 数据依赖

一般来说，具备输入shape后，算子可以通过InferShape推导出输出shape。然而部分算子在InferShape时，需要依赖某个输入的具体值才可以进行，这类算子被称为“数据依赖算子”，对应的输入被称为“数据依赖输入”。以Reshape算子为例，其依据shape输入的描述，对输入的shape做调整，因此Reshape算子依赖shape输入的值。这类算子需要在原型定义时通过[ValueDepend](cannkit-valuedepend.md)接口声明对应的输入为数据依赖输入项。

```cpp
namespace ops {
class Reshape : public OpDef {
public:
    explicit Reshape(const char *name) : OpDef(name)
    {
        // ...
        this->Input("shape")
             .ParamType(REQUIRED)
             // ...
             .ValueDepend(REQUIRED) // 声明 ReShape算子的shape输入为数据依赖输入
        // ...
    }
};
OP_ADD(Reshape);
} // namespace ops
```

根据第1个输入（shape输入）的值，Reshape算子将第0个输入（x输入）的shape做变换，并输出到其第0个输出（y输出）上。Reshape的InferShape实现为：

```cpp
ge::graphStatus InferShapeForReshape(InferShapeContext *context) {
const gert::Shape *x_shape = context->GetInputShape(0); // 获取第0个输入的shape
const gert::Tensor *shape_tensor = context->GetInputTensor(1); // 获取第1个输入的tensor
gert::Shape *output_shape = context->GetOutputShape(0);
if (x_shape == nullptr || shape_tensor == nullptr || output_shape == nullptr) {
    // 防御式编程，不应该出现的场景，打印错误并返回失败
    return ge::GRAPH_FAILED;
}
 
auto reshape_size = static_cast<int32_t>(shape_tensor->GetShapeSize());
if (reshape_size < 1) {
    // 防御式编程，不应该出现的场景，打印错误并返回失败
    return ge::GRAPH_FAILED;
}
 
// 根据原型信息，Reshape的shape输入支持INT32与INT64两类，根据不同的类型进入对应的模板函数中做真正的shape变换操作
if (shape_tensor->GetDataType() == ge::DT_INT32) {
    int32_t *reshape_data = shape_tensor->GetData<int32_t>();
    return ReshapeInferShapeImpl<int32_t>(reshape_data, *x_shape, *output_shape, reshape_size);
} else {
    int64_t *reshape_data = shape_tensor->GetData<int64_t>();
    return ReshapeInferShapeImpl<int64_t>(reshape_data, *x_shape, *output_shape, reshape_size);
}
}
```

**说明** 

* 只有声明过数据依赖的输入，才可以在InferShape时调用GetInputTensor等获取tensor的接口获取其对应的tensor数据。若对一个未声明数据依赖的输入调用GetInputTensor等获取tensor的接口，只能在tensor中获取到正确的shape、format、datatype信息，无法获取到真实的tensor数据地址（获取到的地址为nullptr）。
* 从tensor中获取tensor\_data时(GetData<int32\_t>或GetData<int64\_t>)，使用者需要保证获取的数据类型是正确的，否则行为是未定义的。
