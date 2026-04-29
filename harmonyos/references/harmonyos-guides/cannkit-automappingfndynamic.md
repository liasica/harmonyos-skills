---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingfndynamic
title: AutoMappingFnDynamic
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > AutoMappingFnDynamic
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d81ebaace658c5a63b9201f6dfdb3077fca523a2de630020239a67c9c88eb649
---

## 函数功能

动态输入/输出算子的自动映射回调函数。

## 函数原型

```
1. Status AutoMappingFnDynamic(const google::protobuf::Message *op_src, ge::Operator &op, std::map<std::string, std::pair<std::string, std::string>> dynamic_name_attr_value, int32_t in_pos = -1, int32_t out_pos = -1)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_src | 输入 | 转换前原始模型中的算子，包含原始模型中算子的属性。 |
| op | 输入 | 适配AI处理器的算子。 |
| dynamic\_name\_attr\_value | 输入 | 描述动态输入输出实际个数，key表示动态端口是输入还是输出，key的取值：  - in：代表算子的输入。  - out：代表算子的输出。 |
| in\_pos | 输入 | 动态输入的端口id。 |
| out\_pos | 输入 | 动态输出的端口id。 |

## 约束说明

若原始TensorFlow算子与适配AI处理器的算子属性无法一一映射，AutoMappingFnDynamic函数无法应用于回调函数[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)中，此种场景下，请在回调函数中使用[AutoMappingByOpFnDynamic](cannkit-automappingbyopfndynamic.md)接口进行可以映射成功的属性的自动解析，使用示例请参见[调用示例](cannkit-automappingbyopfndynamic.md#调用示例)。

## 调用示例

动态输入的代码示例：

```
1. // register MapStage op to GE
2. Status MapStageMapping(const google::protobuf::Message* op_src, ge::Operator& op) {
3. map<string, pair<string, string>> value;
4. value["in"] = pair<string, string>("values", "fake_dtypes");
5. AutoMappingFnDynamic(op_src, op, value);
6. return SUCCESS;
7. }

9. REGISTER_CUSTOM_OP("MapStage")
10. .FrameworkType(TENSORFLOW)
11. .OriginOpType("MapStage")
12. .ParseParamsFn(MapStageMapping)
13. .ImplyType(ImplyType::AI_CPU);
```

动态输出的代码示例：

```
1. Status AutoMappingFnSplit(const google::protobuf::Message* op_src, ge::Operator& op) {
2. map<string, pair<string, string>> value;
3. value["out"] = pair<string, string>("y", "num_split");
4. AutoMappingFnDynamic(op_src, op, value);
5. return SUCCESS;
6. }

8. REGISTER_CUSTOM_OP("Split")
9. .FrameworkType(TENSORFLOW)
10. .OriginOpType("Split")
11. .ParseParamsFn(AutoMappingFnSplit)
12. .ImplyType(ImplyType::TVM);
```
