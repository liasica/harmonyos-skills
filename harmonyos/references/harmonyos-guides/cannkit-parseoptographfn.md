---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parseoptographfn
title: ParseOpToGraphFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > ParseOpToGraphFn
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a7d0e96d7f474747e3968a523c8de3c6ec9cf599e68d5d65cf79cfc79808a0f
---

## 函数功能

注册实现算子一对多子图映射的函数，即将算子映射为多个算子。

## 函数原型

```
1. OpRegistrationData &ParseOpToGraphFn(const ParseOpToGraphFunc &parse_op_to_graph_fn)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| parse\_op\_to\_graph\_fn | 输入 | 实现算子一对多映射，进行子图构造的函数。  请参见[回调函数ParseOpToGraphFunc](cannkit-parseoptographfn.md#回调函数parseoptographfunc)。 |

## 约束说明

实现一对多子图映射时，插件注册时首先需要将原始框架中的算子映射成AI处理器中的PartitionedCall算子，并在[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)函数中使用“SetAttr”接口设置original\_type。

实现样例请参见[调用示例](cannkit-parseoptographfn.md#调用示例)。

## 回调函数ParseOpToGraphFunc

开发者自定义并实现ParseOpToGraphFunc函数，通过IR模型构建方式完成一对多子图的构造。

回调函数原型定义如下。

```
1. Status  ParseOpToGraphFunc(const ge::Operator &op, ge::Graph &graph)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op | 输入 | PartitionedCall算子数据结构，Operator类对象。 |
| graph | 输出 | 构造的子图。 |

子图输入输出关系构建方式如下。

* 输入：通过添加Data节点标识，Data节点的index属性表示原节点的第index个输入边。
* 输出：通过Graph::SetOutputs()接口设置，该接口的入参为**std::vector<std::pair<Operator, std::vector<size\_t>>>** ，输出边按照设置的输出顺序相连。

## 调用示例

以将Add算子转换成Addn+Abs为例。

实现Add算子到PartitionedCall算子的映射函数示例如下所示：

```
1. Status ParseParams(const ge::Operator &op_src, ge::Operator& op_dest)
2. {
3. // ...
4. op_dest.SetAttr("original_type", "ai.onnx::11::Add");
5. }
```

一对多子图构造函数实现示例如下所示：

```
1. static Status ParseOpToGraph(const Operator &op, Graph &graph) {
2. auto data_0 = op::Data().set_attr_index(0);
3. auto data_1 = op::Data().set_attr_index(1);
4. auto addn = op::AddN("addn_sum").create_dynamic_input_x(2)
5. .set_dynamic_input_x(0, data_0)
6. .set_dynamic_input_x(1, data_1)
7. .set_attr_N(2);
8. auto abs = op::Abs("abs_sum").set_input_x(addn);
9. std::vector<Operator> inputs{data_0, data_1};
10. std::vector<std::pair<Operator, std::vector<size_t>>> output_indexs;
11. output_indexs.emplace_back(abs, std::vector<std::size_t>{0});
12. graph.SetInputs(inputs).SetOutputs(output_indexs);
13. return domi::SUCCESS;
14. }
```

进行注册：

```
1. REGISTER_CUSTOM_OP("PartitionedCall")
2. .FrameworkType(xx)
3. .OriginOpType(xx)
4. .ParseParamsByOperatorFn(ParseParams)
5. .ParseOpToGraphFn(ParseOpToGraph)
6. .ImplyType(ImplyType::TVM);
```

图为将Add算子进行一对多子图映射后的示例。

**图1** 一对多转换示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/7w4byvmXT82Zs5lrBpYnZA/zh-cn_image_0000002589325663.png?HW-CC-KV=V1&HW-CC-Date=20260429T054219Z&HW-CC-Expire=86400&HW-CC-Sign=4EDB68B8CF977F8BE68E09BFC4D5859748F2A3CBFA4C50F310F35B87B806C03D)
