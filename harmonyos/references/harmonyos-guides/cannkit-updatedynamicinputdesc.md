---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updatedynamicinputdesc
title: UpdateDynamicInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > UpdateDynamicInputDesc
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:38+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:ea005c0ca9468be163904857cf6038ef19bd86ecdbb8f42256da0e4a75e7344f
---

## 函数功能

根据name和index的组合更新算子动态Input的TensorDesc。

## 函数原型

![](https://media:401788444115723939) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus UpdateDynamicInputDesc(const std::string &name, uint32_t index, const TensorDesc &tensor_desc);
graphStatus UpdateDynamicInputDesc(const char_t *name, uint32_t index, const TensorDesc &tensor_desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子动态Input的名称。 |
| index | 输入 | 算子动态Input编号，编号起始值从0开始。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 更新动态Input成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
