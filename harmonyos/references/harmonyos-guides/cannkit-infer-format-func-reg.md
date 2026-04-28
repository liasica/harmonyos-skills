---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infer-format-func-reg
title: INFER_FORMAT_FUNC_REG
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > INFER_FORMAT_FUNC_REG
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab637f2953c3a5279590e8f90becf0070c091e22fb5fb626f136a8dd93302ac2
---

## 函数功能

注册算子的InferFormat实现。

GE会在整图的Shape与Dtype推导前后分别调用一次整图的InferFormat，过程中会分别调用各个算子的InferFormat函数。如果算子没有注册InferFormat函数，GE将使用默认的推导函数，即输出的Format等于输入的Format。

## 函数原型

```
1. #define INFER_FORMAT_FUNC_REG(op_name, x) \
2. __INFER_FORMAT_FUNC_REG_IMPL__(op_name, INFER_FORMAT_FUNC(op_name, x), __COUNTER__)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| op\_name | 输入 | 算子类型。 |
| x | 输入 | inferFormat函数名，使用IMPLEMT\_INFERFORMAT\_FUNC中的func\_name |

## 返回值

无

## 约束说明

无

## 客户是否可用

是

## 调用示例

```
1. INFER_FORMAT_FUNC_REG(Transpose, TransposeInferFormat);
```
