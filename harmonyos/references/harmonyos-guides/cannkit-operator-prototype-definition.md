---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-prototype-definition
title: 算子原型定义实现
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 基于工程实现算子 > 算子原型定义实现
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:22f44b2c87d93708c36521decb1454f048cf3754a5ba974330e22651ab965341
---

算子原型主要描述了算子的输入输出、属性等信息以及算子在AI处理器上相关实现信息，并关联[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)等函数。算子原型通过自定义的算子类来承载，该算子类继承自[OpDef](cannkit-input.md)。完成算子的原型定义等操作后，需要调用[原型注册接口(OP\_ADD)](cannkit-prototype-api-registration.md)接口，传入算子类型（自定义算子类的类名），进行算子原型注册。下面是一个简单的Add算子原型定义和注册的例子。

```
1. namespace ops {
2. class AddCustom : public OpDef {
3. public:
4. AddCustom(const char* name) : OpDef(name)
5. {
6. this->Input("x")
7. .ParamType(REQUIRED)
8. .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
9. .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
10. this->Input("y")
11. .ParamType(REQUIRED)
12. .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
13. .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
14. this->Output("z")
15. .ParamType(REQUIRED)
16. .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
17. .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
18. // 根据开发者的算子调用方式决定需不需要注册 单算子API调用方式下不需要
19. this->SetInferShape(ge::InferShape);
20. this->SetInferDataType(ge::InferDataType);
21. this->AICore()
22. .SetTiling(optiling::TilingFunc);
23. // 请替换为实际的Kirin AI处理器型号
24. this->AICore().AddConfig("kirin9020");
25. }
26. };
27. OP_ADD(AddCustom);
28. } // namespace ops
```

说明

注册算子类型后，框架会根据算子类型获取算子注册信息，同时在编译和运行时按照一定的规则匹配算子实现文件名称和kernel侧核函数名称。为了保证正确匹配，算子类型、算子实现文件名称和核函数名称需要遵循如下定义规则。通常情况下，开发者只需要保证创建算子工程时原型定义json文件中算子类型op的参数值为大驼峰命名方式即可，工程创建后自动生成的代码即满足该规则。在手动编写算子原型定义和算子实现文件时需要按照如下规则定义。

* 算子类型需要采用**大驼峰**的命名方式，即采用大写字符区分不同的语义。
* 算子实现文件名称、核函数名称需相同，均为算子类型转换为**下划线**命名方式后的值。下文描述了通过算子类型转换成算子实现文件名称和核函数名称的过程：

  + 首字符的大写字符转换为小写字符。例如：Abc -> abc。
  + 大写字符的前一个字符为小写字符或数字，则在大写字符前插一个下划线“\_”，并将该字符转换为小写字符。例如：AbcDef -> abc\_def。
  + 大写字符前一个字符为大写字符且后一个字符是小写字符，则在大写字符前插一个下划线“\_”，并将该字符转换为小写字符。例如：AbcAAc -> abc\_a\_ac。
  + 其他大写字符转换为小写字符，小写字符保持不变。

## 算子原型定义

算子原型定义描述了算子的输入输出、属性等信息。输入输出支持的datatype、format格式的数量需要一致，并保持一一对应的关系。

如下的代码片段呈现了Add算子输入x的描述信息。

```
1. this->Input("x")
2. .ParamType(REQUIRED)
3. .DataType({ge::DT_FLOAT16, ge::DT_FLOAT, ge::DT_INT32})
4. .Format({ge::FORMAT_ND, ge::FORMAT_ND, ge::FORMAT_ND});
```

**表1** 输入输出参数说明

| 原型定义 | 参数 | 具体描述 |
| --- | --- | --- |
| Input/Output | ParamType | 参数类型，Option取值为：OPTIONAL（可选）、REQUIRED（必选）、DYNAMIC（动态输入）。  - 类似于上文中的Add样例，其输入输出是必选的。  - 有些算子的输入或者输出个数是动态的，例如AddN，将N个输入Tensor累加到一起，输出一个Tensor；SplitV，将一个Tensor在某个轴上，拆分为N个Tensor输出。  - 有些算子的输入是可选的，例如BatchNorm算子，在训练的时候没有均值和方差输入，在推理的时候有均值和方差的输入。 |
| Input/Output | DataType | 算子输入输出支持的datatype。datatype的取值请参考[DataType](cannkit-ge-datatype.md)。 |
| Input/Output | Format | 算子输入输出支持的format。format的取值请参考[Format](cannkit-ge-format.md)。 |

从上文的原型定义中可以看出，列出了输入输出所有datatype和format的组合，保持一一对应。使用如下接口，可以达到简化这种代码逻辑的目的。

通过[Follow](cannkit-follow.md)接口指定当前输入/输出的datatype/format/shape信息与之前定义过的某个输入一致。示例如下。输出“y1”Follow输入“x1”场景，此时“y1”的datatype、format以及shape都将会和“x1”保持一致。使用Follow接口指定shape一致时通常比[shape推导](cannkit-development-process.md#shape推导)函数逻辑更加简单，能用Follow表达的逻辑，建议使用Follow接口，则无需再编写注册InferShape函数。

```
1. this->Input("x1")
2. .ParamType(REQUIRED)
3. .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
4. .Format({ge::FORMAT_ND, ge::FORMAT_ND});
5. this->Input("x2")
6. .ParamType(REQUIRED)
7. .DataType({ge::DT_FLOAT, ge::DT_FLOAT})
8. .Format({ge::FORMAT_ND, ge::FORMAT_ND});
9. this->Output("y1")
10. .ParamType(REQUIRED)
11. .Follow("x1")
12. .OutputShapeDependOnCompute();
```

原型定义中还包括算子属性信息，如下的代码片段呈现了ReduceMax算子的属性reduceDim和isKeepDim的描述信息。

```
1. this->Attr("reduceDim")
2. .AttrType(REQUIRED)
3. .Int();
4. this->Attr("isKeepDim")
5. .AttrType(OPTIONAL)
6. .Int(1);
```

具体参数说明如下。

**表2** 属性参数说明

| 原型定义 | 注册方式 | 具体描述 |
| --- | --- | --- |
| Attr | AttrType | 设置算子属性类型，取值为：OPTIONAL（可选）、REQUIRED（必选）。 |
| Attr | Bool/Float/Int... | 设置算子属性数据类型为Bool/Float/Int...。具体说明请参考[OpAttrDef](cannkit-opattrdef.md)。 |

## AI处理器上相关实现信息

通过[AddConfig](cannkit-addconfig.md)注册算子支持的AI处理器型号以及相关的配置信息。AddConfig接口原型如下。

soc参数表示AI处理器型号，aicore\_config表示其他配置信息。

```
1. void AddConfig(const char *soc);
2. void AddConfig(const char *soc, OpAICoreConfig &aicore_config);
```

通过该接口注册AI处理器型号的样例如下，ascendxxx请替换为实际的AI处理器型号。

```
1. this->AICore().AddConfig("ascendxxx");
```

## 关联Tiling实现、Shape推导等函数

通过[SetInferShape](cannkit-setinfershape.md)、[SetInferDataType](cannkit-setinferdatatype.md)、[SetTiling](cannkit-settiling.md)接口来关联对应的shape推导函数和Tiling函数，样例如下。

```
1. this->SetInferShape(ge::InferShape);
2. this->SetInferDataType(ge::InferDataType);
3. this->AICore()
4. .SetTiling(optiling::TilingFunc);
```

## 多硬件平台注册差异化的算子原型

算子类继承基类OpDef，使用Input、Output、Attr等注册算子原型信息，硬件平台支持相同的算子原型的情况下，直接通过AICore().AddConfig添加支持的AI处理器型号即可；不同的硬件形态算子原型定义不同的情况，可以通过新增OpAICoreConfig的方式，针对不同的AI处理器型号注册差异化的算子原型。

差异化的算子原型生效规则如下。

* 对于算子类的输入输出原型信息，OpAICoreConfig未配置的会继承OpDef定义的原型，比如算子类中定义了输出y，OpAICoreConfig中没有定义输出y，OpAICoreConfig会继承y的原型定义。
* 对于算子类和新增OpAICoreConfig中定义的算子原型相同的情况，新增OpAICoreConfig中定义的算子原型信息会覆盖OpDef定义的原型信息，比如算子类中定义了输入x支持DT\_FLOAT16数据类型，新增OpAICoreConfig中也定义了输入x，但是支持DT\_FLOAT16、DT\_BF16数据类型，则以OpAICoreConfig新增定义为准。

如下样例中kirinxxx1、kirinxxx2（AI处理器型号）使用相同的算子原型，算子类通过继承基类OpDef，使用Input、Output、Attr等注册算子原型信息，再通过AICore().AddConfig添加支持的AI处理器型号；对于ascendxxx3支持的算子原型需要定制化处理，新增了DT\_BF16的类型，通过新增OpAICoreConfig的方式进行注册，x，y，z的定义会覆盖算子类中对应定义的原型信息。

```
1. namespace ops {
2. class MyAdd : public OpDef {
3. public:
4. MyAdd(const char* name) : OpDef(name)
5. {
6. // ascendxxx1 ascendxxx2 AI处理器型号原型定义
7. this->Input("x")
8. .ParamType(REQUIRED)
9. .DataType({ge::DT_FLOAT16})
10. .Format({ge::FORMAT_ND});
11. this->Input("y")
12. .ParamType(OPTIONAL)
13. .DataType({ge::DT_INT64})
14. .ValueDepend(REQUIRED)
15. .Format({ge::FORMAT_ND});
16. this->Output("z")
17. .ParamType(REQUIRED)
18. .DataType({ge::DT_FLOAT16})
19. .Format({ge::FORMAT_ND});
20. this->AICore()
21. .SetTiling(optiling::TilingFunc);
22. this->AICore().AddConfig("ascendxxx1");
23. this->AICore().AddConfig("ascendxxx2");
24. // ascendxxx3芯片定义OpAICoreConfig变量，定制化原型
25. OpAICoreConfig config;
26. config.Input("x")
27. .ParamType(REQUIRED)
28. .DataType({ge::DT_FLOAT16, ge::DT_BF16})
29. .Format({ge::FORMAT_ND, ge::FORMAT_ND});
30. config.Input("y")
31. .ParamType(REQUIRED)
32. .DataType({ge::DT_FLOAT16, ge::DT_BF16})
33. .Format({ge::FORMAT_ND, ge::FORMAT_ND});
34. config.Output("z")
35. .ParamType(REQUIRED)
36. .DataType({ge::DT_FLOAT16, ge::DT_BF16})
37. .Format({ge::FORMAT_ND, ge::FORMAT_ND});
38. this->AICore().AddConfig("kirin9020", config);
39. }
40. };
41. OP_ADD(MyAdd);
42. }
```

如下的样例中，只有几个参数原型信息在不同硬件平台不一致，开发者也可以通过OpAICoreConfig定制部分算子原型信息，复用OpDef定义的其他算子原型信息，达到部分原型信息硬件平台定制化的目的。

```
1. class AddCustom : public OpDef {
2. public:
3. AddCustom(const char* name) : OpDef(name)
4. {
5. this->Input("x").DataType({ ge::DT_FLOAT16 }).ParamType(OPTIONAL);
6. this->Output("y").DataType({ ge::DT_FLOAT16 });
7. OpAICoreConfig aicConfig1;
8. OpAICoreConfig aicConfig2;
9. aicConfig1.Input("x")
10. .ParamType(OPTIONAL)
11. .DataType({ ge::DT_FLOAT })
12. .Format({ ge::FORMAT_ND });
13. aicConfig2.Input("x")
14. .ParamType(REQUIRED)
15. .DataType({ ge::DT_INT32 })
16. .Format({ ge::FORMAT_ND });
17. this->AICore().AddConfig("kirinxxxx1", aicConfig1);
18. this->AICore().AddConfig("kirinxxxx2", aicConfig2);
19. }
20. };
```
