---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalar-binocular-adds
title: Adds
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 标量双目指令 > Adds
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:27+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:de56ace2dcf64cee3836bbadef081ed28e88c7e67f0ea1998d91c564a467a94c
---

## 功能说明

矢量内每个元素与标量求和，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数：

![](https://media:401788444116081943)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T, bool isSetMask = true> 
__aicore__ inline void Adds(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const T& scalarValue, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |
| scalarValue | scalarValue数据类型。 |
| isSetMask | 是否在接口内部设置mask模式和mask值。  - true，表示在接口内部设置。  - false，表示在接口外部设置。 |

**表2** 参数说明

| **参数名称** | **类型** | **说明** |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：Tensor（int16\_t、int32\_t、half、float）。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  数据类型需要与目的操作数保持一致。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：Tensor（int16\_t、int32\_t、half、float）。 |
| scalarValue | 输入 | 源操作数，数据类型需要与目的操作数中的元素类型保持一致  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：Tensor（int16\_t、int32\_t、half、float）。 |
| calCount | 输入 | 输入数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。

## 调用示例

本样例中只展示Compute流程中的部分代码。如果开发者需要运行样例代码，请将该代码段拷贝并替换标量双目指令样例模板[更多样例](cannkit-scalar-binocularinstructions.md)中的Compute函数即可。

tensor前n个数据计算样例：

```cpp
int16_t scalar = 2;
AscendC::Adds(dstLocal, srcLocal, scalar, 512);
```

结果示例如下。

```text
输入数据(src0Local): [1 2 3 ... 512]
输入数据(scalar): 2
输出数据(dstLocal): [3 4 5 ... 514]
```
