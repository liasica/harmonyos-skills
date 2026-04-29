---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-fusionparseparamsfn-overload
title: FusionParseParamsFn（Overload）
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > FusionParseParamsFn（Overload）
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5cca3f555390121774736c0c848fa059a998430056ca6e28ce0573069095140f
---

## 函数功能

注册解析融合算子属性的函数，为[FusionParseParamsFn](cannkit-fusionparseparamsfn.md)的重载函数。

## 函数原型

```
1. OpRegistrationData &FusionParseParamsFn(const FusionParseParamByOpFunc &fusion_parse_param_fn)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| **fusion\_parse\_param\_fn** | 输入 | 解析融合算子属性的函数，请参见[回调函数FusionParseParamByOpFunc](cannkit-fusionparseparamsfn-overload.md#回调函数fusionparseparambyopfunc)。 |

## 回调函数FusionParseParamByOpFunc

开发者自定义并实现FusionParseParamByOpFunc类函数，完成原始模型中属性到适配AI处理器的模型中的属性映射，将结果填入Operator类中。

```
1. Status FusionParseParamByOpFunc(const std::vector<ge::Operator> &op_src,  ge::Operator &op_dest);
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| op\_src | 输入 | 一组scope内存储原始模型中算子属性的融合算子数据结构，  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |
| op\_dest | 输出 | 融合算子数据结构，保存融合算子信息。  关于Operator类，请参见[Operator](cannkit-operator-construction-and-destructor.md)。 |

## 调用示例

```
1. REGISTER_CUSTOM_OP(XXXXXX)
2. .FrameworkType(TENSORFLOW)
3. .FusionParseParamsFn(FusionParseParamsFn)
4. .OriginOpType(XXXXX)
5. .ImplyType(XXXXX);
```
