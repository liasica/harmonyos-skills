---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingbyopfndynamic
title: AutoMappingByOpFnDynamic
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > AutoMappingByOpFnDynamic
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8cbb8c889e85dab56a4c10856af7d656429f6e926ce23984aeca71055ae02598
---

## 函数功能

动态输入/输出算子的自动映射回调函数。

## 函数原型

```
1. Status AutoMappingByOpFnDynamic(const ge::Operator &op_src, ge::Operator &op, const std::vector<DynamicInputOutputInfo> &dynamic_name_attr_value)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_src | 输入 | 转换前原始模型中的算子，包含原始模型中算子的属性。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
| op | 输入 | 适配AI处理器的算子。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
| dynamic\_name\_attr\_value | 输入 | 描述动态输入输出实际个数，**DynamicInputOutputInfo**数据结构请参见[DynamicInputOutputInfo数据结构说明](cannkit-automappingbyopfndynamic.md#dynamicinputoutputinfo数据结构说明)。 |

## DynamicInputOutputInfo数据结构说明

```
1. constexpr int64_t kMaxNameLength = 1048576; // 1M
2. enum DynamicType : int16_t {
3. kInvalid = 0,
4. kInput = 1,
5. kOutput = 2
6. };
7. struct DynamicInputOutputInfo {
8. DynamicType type; // input/output
9. const char_t *port_name;
10. int64_t port_name_len;
11. const char_t *attr_name;
12. int64_t attr_name_len;
13. DynamicInputOutputInfo(const DynamicType type_instance, const char_t *const port_name_instance,
14. const int64_t port_name_len_instance, const char_t *const attr_name_instance,
15. const int64_t attr_name_len_instance)
16. : type(type_instance), port_name(port_name_instance), port_name_len(port_name_len_instance),
17. attr_name(attr_name_instance), attr_name_len(attr_name_len_instance) {}
18. DynamicInputOutputInfo() : DynamicInputOutputInfo(kInvalid, nullptr, 0L, nullptr, 0L) {}
19. };
```

| 参数 | 说明 |
| --- | --- |
| type | 指定是动态输入或输出。  0：无效值  1：输入  2：输出 |
| port\_name | 端口名字，输入或者输出的Name。 |
| port\_name\_len | 端口名字长度，最大长度为kMaxNameLength。 |
| attr\_name | 属性名字。 |
| attr\_name\_len | 属性名字长度，最大长度为kMaxNameLength。 |

## 调用示例

```
1. Status QueueDequeueUpToMapping(const  ge::Operator& op_src, ge::Operator& op) {
2. vector<DynamicInputOutputInfo> dynamic_name_attr_value;
3. string port_name = "components";
4. string attr_name = "component_types";
5. DynamicInputOutputInfo name_attr(kOutput, port_name.c_str(), port_name.size(), attr_name.c_str(), attr_name.size());
6. dynamic_name_attr_value.push_back(name_attr);
7. AutoMappingByOpFnDynamic(op_src, op, dynamic_name_attr_value);
8. return SUCCESS;
9. }

11. REGISTER_CUSTOM_OP("QueueDequeueUpTo")
12. .FrameworkType(TENSORFLOW)
13. .OriginOpType("QueueDequeueUpToV2")
14. .ParseParamsByOperatorFn(QueueDequeueUpToMapping)
15. .ImplyType(ImplyType::AI_CPU);
```
