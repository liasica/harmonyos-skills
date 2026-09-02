---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-iterateall
title: IterateAll
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > IterateAll
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:ef4f5062ab836749d631ebad952bfcd16b29e02b3411b59b4f675baa9b57cfe0
---

## 功能说明

调用一次IterateAll，会计算出singleCoreM \* singleCoreN大小的C矩阵。迭代顺序可通过tiling参数iterateOrder调整。

## 函数原型

```cpp
template <bool sync = true> __aicore__ inline void IterateAll(const GlobalTensor<DstT>& gm, uint8_t enAtomic = 0, bool enSequentialWrite = false, bool waitIterateAll = false, bool fakeMsg = false)
template <bool sync = true> __aicore__ inline void IterateAll(const LocalTensor<DstT>& ubCmatrix, uint8_t enAtomic = 0)
```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| sync | 获取C矩阵过程分为同步和异步两种模式：  - 同步：需要同步等待IterateAll执行结束。  - 异步：不需要同步等待IterateAll执行结束。  通过该参数设置同步或者异步模式：同步模式设置为true，异步模式设置为false，默认为同步模式。 |

**表2** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| gm | 输入 | C矩阵放置于Global Memory的地址。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。 |
| ubCmatrix | 输入 | C矩阵放置于Local Memory的地址。TPosition可设置为TPosition::TSCM。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。 |
| enAtomic | 输入 | 是否开启Atomic操作，默认值为0。  参数取值：  0：不开启Atomic操作  1：开启AtomicAdd累加操作  2：开启AtomicMax求最大值操作  3：开启AtomicMin求最小值操作 **。** |
| enSequentialWrite | 输入 | 是否开启连续写模式（连续写，写入[baseM, baseN]。非连续写，写入[singleCoreM、singleCoreN]中对应的位置），默认值false（非连续写模式）。 |
| waitIterateAll | 输入 | 仅在异步场景下使用，是否需要通过WaitIterateAll接口等待IterateAll执行结束。  true：需要通过WaitIterateAll接口等待IterateAll执行结束。  false：不需要通过WaitIterateAll接口等待IterateAll执行结束，开发者自行处理等待IterateAll执行结束的过程。 |
| fakeMsg | 输入 | 仅在IBShare（模板参数中开启了doIBShareNorm开关）场景使用。  IBShare用于保证复用L1上相同的A矩阵或B矩阵数据，要求AIV分核调用IterateAll的次数必须匹配，此时需要调用IterateAll并设置fakeMsg为true，不执行真正的计算，仅用来保证IterateAll调用成对出现。默认值为false，表示执行真正的计算。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

传入的C矩阵地址空间大小需要保证不小于singleM \* singleN。

## 调用示例

```cpp
REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);
mm.SetTensorA(gm_a);
mm.SetTensorB(gm_b);
mm.SetBias(gm_bias);
mm.IterateAll(gm_c); // 计算
```
