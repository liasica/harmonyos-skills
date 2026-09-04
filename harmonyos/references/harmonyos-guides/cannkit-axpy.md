---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-axpy
title: Axpy
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 标量三目指令 > Axpy
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:27+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:42a3085b32b6482cb54772a0c9eff9caee2b69f73412c9671152cbe3ed2ddcc6
---

## 函数功能

源操作数(srcLocal)中每个元素与标量求积后和目的操作数(dstLocal)中的对应元素相加，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数：

![](https://media:401788444116138944)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T, typename U> 
__aicore__ inline void Axpy(const LocalTensor<T>& dstLocal, const LocalTensor<U>& srcLocal, const U& scalarValue, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 目的操作数数据类型。 |
| U | 源操作数数据类型。 |

**表2** 参数说明

| **参数名称** | **类型** | **说明** |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float | 支持mixed精度类型：dst为float，src为half |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float | 支持mixed精度类型：dst为float，src为half |
| scalarValue | 输入 | 源操作数，scalar标量。支持的数据类型为：half/float。scalarValue的数据类型需要和srcLocal保持一致。 |
| calCount | 输入 | 输入数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

该接口支持的精度组合如下。

* half精度组合：srcLocal数据类型=half；scalar数据类型=half；dstLocal数据类型=half；PAR=128。
* float精度组合：srcLocal数据类型=float；scalar数据类型=float；dstLocal数据类型=float；PAR=64。
* mixed精度组合：srcLocal数据类型=half；scalar数据类型=half；dstLocal数据类型=float；PAR=64。

## 调用示例

本样例中只展示Compute流程中的部分代码。如果开发者需要运行样例代码，请将该代码段拷贝并替换[更多样例](scalar-ternaryinstructions-more-examples.md)完整样例模板中Compute函数的部分代码即可。

tensor前n个数据计算样例：

```cpp
AscendC::Axpy(dstLocal, src0Local, (half)2.0, 512);// half精度组合
```
