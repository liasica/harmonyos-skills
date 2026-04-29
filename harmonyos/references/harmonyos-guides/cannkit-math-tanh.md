---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-math-tanh
title: Tanh
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 数学库 > Tanh
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0bbb85342e4dc1ce850bd94d6722dc6458e7065cc255124513918a4900e1a433
---

## 功能说明

按元素做逻辑回归Tanh，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/QAh0wttARAyigXacqdgxeA/zh-cn_image_0000002589245599.png?HW-CC-KV=V1&HW-CC-Date=20260429T054130Z&HW-CC-Expire=86400&HW-CC-Sign=46F7C218FC1EB2B4A608FCC0E2C621CCD916F51C7B26C59CD2BAFD1FFB085350)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/cA74xyxhRkW4FVq63yXfrQ/zh-cn_image_0000002558765790.png?HW-CC-KV=V1&HW-CC-Date=20260429T054130Z&HW-CC-Expire=86400&HW-CC-Sign=E921B2CE33BC1F96575B9E9143ED9E18C4B482511EB269DBCED6D91B36702179)

## 函数原型

```
1. template <typename T, bool isReuseSource = false>
2. __aicore__ inline void Tanh(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const uint32_t calCount)
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
| dstTensor | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。 |
| srcTensor | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。 |
| calCount | 输入 | 实际计算数据元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 输入输出操作数参与计算的数据长度要求32B对齐。

## 调用示例

```
1. AscendC::TPipe pipe;
2. // calCount为实际计算数据元素个数
3. // 其它处理省略
4. AscendC::Tanh<T, false>(yLocal, xLocal, calCount);
```
