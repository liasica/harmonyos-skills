---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensorc
title: GetTensorC
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > GetTensorC
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:29+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:4a3b58f0cf71b133f114ea88a48b2513c88a964d38e686f972885b330f516a04
---

## 功能说明

Iterate后，获取一块C矩阵片，可以直接输出到GM tensor中。

该接口和Iterate接口配合使用，用于在调用Iterate完成迭代计算后，获取一片baseM \* baseN大小的矩阵分片。

迭代获取C矩阵分片的过程分为同步和异步两种模式：

* **同步：** 执行完一次Iterate后执行一次GetTensorC，需要同步等待C矩阵分片获取完成。
* **异步：** 调用Iterate后，无需立即调用GetTensorC同步等待，可以先执行其他逻辑，待需要获取结果时再调用GetTensorC。异步方式可以减少同步等待，提高并行度，开发者对计算性能要求较高时，可以选用该方式。

## 函数原型

* 获取C矩阵，输出至GM

  ```cpp
  template <bool sync = true>
  __aicore__ inline void GetTensorC(const GlobalTensor<DstT>& gm, uint8_t enAtomic = 0, bool enSequentialWrite = false)
  ```

  + 支持同步模式
  + 支持异步模式
* 获取API接口返回的GM上的C矩阵，后续使用过程由开发者自行控制

  提供该接口支持返回API框架申请的GM上的C矩阵，由开发者自行控制后续使用过程。

  支持异步模式：

  以下接口中的doPad、height、width、srcGap、dstGap参数待废弃，使用过程中无需传入，保持默认值即可。

  ```cpp
  template <bool sync = true, bool doPad = false> 
  __aicore__ inline void GetTensorC(const LocalTensor<DstT>& c, uint8_t enAtomic = 0, bool enSequentialWrite = false, uint32_t height = 0, uint32_t width = 0, uint32_t srcGap = 0, uint32_t dstGap = 0)
  ```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| sync | 设置同步或者异步模式：同步模式设置为true，异步模式设置为false。 |

**表2** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| gm | 输出 | 取出C矩阵到GM，数据格式可以为ND或NZ。  Kirin9020系列处理器、Kirin9030系列处理器，支持的数据类型为：half。 |
| enAtomic | 输入 | 是否开启Atomic操作，默认值为0 **。**  参数取值：  0：不开启Atomic操作  1：开启AtomicAdd累加操作  2：开启AtomicMax求最大值操作  3：开启AtomicMin求最小值操作 |
| enSequentialWrite | 输入 | 是否开启连续写模式（连续写，写入[baseM, baseN]。非连续写，写入[singleCoreM, singleCoreN]中对应的位置），默认值false（非连续写模式）。  **说明：** 非连续写模式，内部会按照迭代顺序算好偏移，开发者不需要关注。如果开发者需要自己决定排布顺序，可以选择连续写模式，自行按照自己设定的偏移进行搬运操作。 |

**图1** 非连续写模式示意图

![](https://media:401788444119887989)

**图2** 连续写模式示意图

![](https://media:401788444119914990)

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

传入的C矩阵地址空间大小需要保证不小于baseM \* baseN。

## 调用示例

* 获取C矩阵，输出至GM，同步模式样例

  ```cpp
  while (mm.Iterate()) {
  mm.GetTensorC(gm);
  }
  ```
* 获取API接口返回的GM上的C矩阵，手动拷贝至UB，异步模式样例

  ```cpp
  // BaseM * BaseN = 128 *256
  mm.SetTensorA(gmA);
  mm.SetTensorB(gmB);
  mm.SetTail(singleM, singleN, singleK);
  mm.template Iterate<false>();
  // ...
  for (int i = 0; i < singleM / baseM * singleN / baseN; ++i) {
  // 获取每次计算的BaseM*BaseN的数据分配64*128大小的UB空间
  DataCopy(local, global[64 * 128 * i], 64 * 128); // 将GM的数据拷贝进UB中，进行后续的Vector操作
  // ... Vector 操作
  }
  ```
