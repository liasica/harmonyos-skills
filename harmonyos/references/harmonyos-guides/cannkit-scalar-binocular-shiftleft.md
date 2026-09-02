---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalar-binocular-shiftleft
title: ShiftLeft
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 标量双目指令 > ShiftLeft
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:406c833e045a7ca4cad61aaab67752aaa452ac4fb3a88e7e856e5fc535f32f03
---

## 功能说明

源操作数内每个元素做逻辑左移，逻辑左移的位数由输入参数scalar决定。

所谓逻辑左移，是指去掉最高位，最低位补0，例：二进制数 1010101010101010，逻辑左移一位结果为 0101010101010100。

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T, bool isSetMask = true> 
__aicore__ inline void ShiftLeft(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const T& scalarValue, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |
| U | scalarValue数据类型。 |
| isSetMask | 是否在接口内部设置mask模式和mask值。  - true，表示在接口内部设置。  - false，表示在接口外部设置。 |

**表2** 参数说明

| **参数名称** | **类型** | **说明** |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：  前n个tensor：uint16\_t、int16\_t、uint32\_t、int32\_t  不支持浮点类型（half、float32\_t）。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  数据类型需要与目的操作数保持一致。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：  前n个tensor：uint16\_t、int16\_t、uint32\_t、int32\_t  不支持浮点类型（half、float32\_t）。 |
| scalarValue | 输入 | 源操作数，数据类型需要与目的操作数Tensor中的元素数据类型保持一致。  - 当src为uint16\_t/int16\_t类型时，scalar取值范围：[0, 16]。  - 当src为uint32\_t/int32\_t类型时，scalar取值范围：[0, 32]。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：  前n个tensor：uint16\_t、int16\_t、uint32\_t、int32\_t  不支持浮点类型（half、float32\_t）。 |
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
AscendC::ShiftLeft(dstLocal, srcLocal, scalar, 512);
```

结果示例如下。

```text
输入数据(src0Local): [1 2 3 ... 512]
输入数据 scalar = 2
输出数据(dstLocal): [4 8 12 ... 2048]
```
