---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-math-tanh
title: Tanh
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 数学库 > Tanh
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:fbf05dfabe11d0ccbe2ab255a9d8c5b1e2af0d3ae6afde517977479d007b2325
---

## 功能说明

按元素做逻辑回归Tanh，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/xx03QYu8RNmdk8xpvQNUGw/zh-cn_image_0000002736434501.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/SG3rKVWcRQCCSz3M1fgIsA/zh-cn_image_0000002706835354.png)

## 函数原型

```cpp
template <typename T, bool isReuseSource = false>
__aicore__ inline void Tanh(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const uint32_t calCount)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数的数据类型。支持的数据类型为：half/float。 |
| isReuseSource | 是否允许修改源操作数。该参数预留，传入默认值false即可。 |

**表2** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstTensor | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。 |
| srcTensor | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。 |
| calCount | 输入 | 实际计算数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 输入输出操作数参与计算的数据长度要求32B对齐。

## 调用示例

```cpp
AscendC::TPipe pipe;
// calCount为实际计算数据元素个数
// 其它处理省略
AscendC::Tanh<T, false>(yLocal, xLocal, calCount);
```
