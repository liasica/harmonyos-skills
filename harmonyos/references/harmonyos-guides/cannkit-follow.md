---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-follow
title: Follow
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpParamDef > Follow
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f4185eb82f60f4e7f71715a39d77564546709f3594d6e256f3c724cca931719
---

## 函数功能

用于指定当前输入/输出的datatype/format/shape信息与之前定义过的某个输入一致。

## 函数原型

```cpp
OpParamDef &Follow(const char *paramName);
OpParamDef &Follow(const char *paramName, FollowType ftype);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| paramName | 输入 | 之前定义过的输入名。 |
| ftype | 输入 | ftype类型为枚举类FollowType，表示Follow的模式，取值如下。  - ALL，datatype/format/shape与paramName均保持一致。  - DTYPE，datatype与paramName保持一致。  - FORMAT，format与paramName保持一致。  - SHAPE，shape与paramName保持一致。 |

## 返回值

[OpParamDef](cannkit-paramtype.md)算子定义。

## 约束说明

* 所有Follow的数据源头仅支持为Input。
* 针对shape推导，仅支持输出参数Follow输入参数，不支持输入参数Follow另一个输入参数。
* 可以支持链式Follow，例如C Follow B，B Follow A，但此时Follow的模式不可中途变更（ftype需要保持一致）。
* 使用Follow接口通常比InferShape函数逻辑更加简单，能用Follow表达的逻辑，建议使用Follow接口，则无需再编写注册InferShape函数。
* InferShape推导函数和使用Follow接口去Follow shape不能混用，即不支持部分输出采用Infershape推导、部分输出采用Follow推导的情况。若开发者同时使用了InferShape函数和Follow接口，以开发者的InferShape函数为准，需要保证在InferShape函数中能够推导出所有的输出shape。

## 调用示例

输出“y1”Follow输入“x1”场景，此时“y1”的datatype、format以及shape都将会和“x1”保持一致。

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
    .Follow("x1")
    .OutputShapeDependOnCompute();
```
