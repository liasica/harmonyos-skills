---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-vector-calculation-relu
title: Relu
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 单目指令 > Relu
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:36+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:0e6f899c84c721963afa2cdb83a9c4650f1442439c5b88423977f08ea1667be0
---

## 函数功能

按元素做线性整流Relu，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/831ZYs8AQF-k1de3sD52Lg/zh-cn_image_0000002706675388.png)

## 函数原型

tensor前n个数据计算：

```cpp
template <typename T>
__aicore__ inline void Relu(const LocalTensor<T>& dstLocal, const LocalTensor<T>& srcLocal, const int32_t& calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数数据类型。 |

**表2** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float、int32\_t。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。  源操作数的数据类型需要与目的操作数保持一致。  Kirin9020系列处理器、Kirin9030系列处理器、KirinX90系列处理器，支持的数据类型为：half、float、int32\_t。 |
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
AscendC::Relu(dstLocal, srcLocal, 512);
```

结果示例如下。

```text
输入数据(srcLocal): [6.938 -8.86 -0.2263 ... 1.971 1.778]
输出数据(dstLocal):
[6.938 0 0 ... 1.971 1.778]
```
