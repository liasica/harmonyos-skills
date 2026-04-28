---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updatedynamicinputdesc
title: UpdateDynamicInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > UpdateDynamicInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de63aaaaefc5d580b368aebf7fb9e9485af5b9486c4bfafd04a37d6cf632c9a9
---

## 函数功能

根据name和index的组合更新算子动态Input的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus UpdateDynamicInputDesc(const std::string &name, uint32_t index, const TensorDesc &tensor_desc);
2. graphStatus UpdateDynamicInputDesc(const char_t *name, uint32_t index, const TensorDesc &tensor_desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子动态Input的名称。 |
| index | 输入 | 算子动态Input编号，编号起始值从1开始。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 更新动态Input成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
