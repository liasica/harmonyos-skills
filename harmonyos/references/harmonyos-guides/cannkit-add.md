---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-add
title: Add
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 双目指令 > Add
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:27+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:1f69ce4b3ee67763eb934542f7b6de700047ec456251d9f6700b2423bb507be7
---

## 功能说明

按元素求和，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数：

![](https://media:401788444116030942)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T> 
__aicore__ inline void Add(const LocalTensor<T>& dstLocal, const LocalTensor<T>& src0Local, const LocalTensor<T>& src1Local, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |

**表2** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float、int16\_t、int32\_t。 |
| src0Local、src1Local | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  两个源操作数的数据类型需要与目的操作数保持一致。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float、int16\_t、int32\_t。 |
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

本样例中只展示Compute流程中的部分代码。如果开发者需要运行样例代码，请将该代码段拷贝并替换双目指令样例模板[更多样例](cannkitvectorcalculation-binocularinstructions.md)中的Compute函数即可。

tensor前n个数据计算样例：

```cpp
AscendC::Add(dstLocal, src0Local, src1Local, 512);
```

结果示例如下。

```text
输入数据(src0Local): [1 2 3 ... 512]
输入数据(src1Local): [513 514 515 ... 1024]
输出数据(dstLocal): [514 516 518 ... 1536]
```
