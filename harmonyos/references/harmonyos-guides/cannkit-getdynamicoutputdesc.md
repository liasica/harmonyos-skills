---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicoutputdesc
title: GetDynamicOutputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetDynamicOutputDesc
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:37+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:a6d2c8de441e48c6af5ff2d3926d2c9d578a8e101791fdfe51ef453cd0b6fb55
---

## 函数功能

根据name和index的组合获取算子动态Output的TensorDesc。

## 函数原型

![](https://media:401788444112215916) 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
TensorDesc GetDynamicOutputDesc(const std::string &name, uint32_t index) const;
TensorDesc GetDynamicOutputDesc(const char_t *name, uint32_t index) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子动态Output的名称。 |
| index | 输入 | 算子动态Output编号，编号起始值从0开始。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| [TensorDesc](cannkit-tensordesc-construction-and-destructor.md) | 获取TensorDesc成功，则返回算子动态Output的TensorDesc；获取失败，则返回TensorDesc默认构造的对象，其中，主要设置DataType为DT\_FLOAT（表示float类型），Format为FORMAT\_NCHW（表示NCHW）。 |

## 异常处理

无

## 约束说明

无
