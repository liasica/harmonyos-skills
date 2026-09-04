---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-vector-calculation-sqrt
title: Sqrt
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 单目指令 > Sqrt
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:27+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:f6dcfa62014d5be5ad2bce29658b9a6719774fe709b4d3018f54a89399e72e87
---

## 函数功能

按元素做开方，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数：

![](https://media:401788444118723974)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T>
__aicore__ inline void Sqrt(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |

**表2** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  源操作数的数据类型需要与目的操作数保持一致。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float。 |
| calCount | 输入 | 输入数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。

## 调用示例

本样例中只展示Compute流程中的部分代码。本样例的srcLocal和dstLocal均为half类型，占16位bit。

如果开发者需要运行样例代码，请将该代码段拷贝并替换[样例模板](cannkit-vector-calculation-binocular-more.md#样例模板)中Compute函数的部分代码即可。

tensor前n个数据计算样例：

```cpp
AscendC::Sqrt(dstLocal, srcLocal, 512);
```

结果示例如下。

```text
输入数据(srcLocal): [1.0 2.0 3.0 4.0 ...]
输出数据(dstLocal):
[1.0 1.414 1.732 2.0...]
```
