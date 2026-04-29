---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-activation-sigmoid
title: Sigmoid
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 激活函数 > Sigmoid
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:24c482eb9e739ad7aac56ad59d0961dbb6cb6b5c6964ddd95554e43f7f2efc26
---

## 功能说明

按元素做逻辑回归Sigmoid，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/FH-nvyi6SYqJ3cLVkjTueQ/zh-cn_image_0000002589245601.png?HW-CC-KV=V1&HW-CC-Date=20260429T054131Z&HW-CC-Expire=86400&HW-CC-Sign=322290EF7DD7F22B0557A8CFF5CD1159CA25171937E1B72F944B947F42FD94BC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/9ihHQZOoSwuOOGQtUPFZUA/zh-cn_image_0000002558765792.png?HW-CC-KV=V1&HW-CC-Date=20260429T054131Z&HW-CC-Expire=86400&HW-CC-Sign=B2363E133347CC7D8FEE911EC8E97EC97907DF5D372DA0F721D9C7A0D7D1CA83)

## 函数原型

* 通过sharedTmpBuffer入参传入临时空间

  + 源操作数Tensor全部/部分参与计算

    ```
    1. template <typename T, bool isReuseSource = false>
    2. __aicore__ inline void Sigmoid(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const LocalTensor<uint8_t>& sharedTmpBuffer, const uint32_t calCount)
    ```
  + 源操作数Tensor全部参与计算

    ```
    1. template <typename T, bool isReuseSource = false>
    2. __aicore__ inline void Sigmoid(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const LocalTensor<uint8_t>& sharedTmpBuffer)
    ```
* 接口框架申请临时空间

  + 源操作数Tensor全部/部分参与计算

    ```
    1. template <typename T, bool isReuseSource = false>
    2. __aicore__ inline void Sigmoid(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const uint32_t calCount)
    ```
  + 源操作数Tensor全部参与计算

    ```
    1. template <typename T, bool isReuseSource = false>
    2. __aicore__ inline void Sigmoid(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor)
    ```

由于该接口的内部实现中涉及复杂的数学计算，需要额外的临时空间来存储计算过程中的中间变量。临时空间支持开发者通过sharedTmpBuffer入参传入和接口框架申请两种方式。

* 通过sharedTmpBuffer入参传入，使用该tensor作为临时空间进行处理，接口框架不再申请。该方式开发者可以自行管理sharedTmpBuffer内存空间，并在接口调用完成后，复用该部分内存，内存不会反复申请释放，灵活性较高，内存利用率也较高。
* 接口框架申请临时空间，开发者无需申请，但是需要预留临时空间的大小。

通过sharedTmpBuffer传入的情况，开发者需要为tensor申请空间；接口框架申请的方式，开发者需要预留临时空间。

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
| sharedTmpBuffer | 输入 | 临时缓存。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN/VECCALC/VECOUT。  用于Sigmoid内部复杂计算时存储中间变量，由开发者提供。 |
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
2. AscendC::TQue<AscendC::TPosition::VECCALC, 1> tmpQue;
3. pipe.InitBuffer(tmpQue, 1, bufferSize);  // bufferSize 通过Host侧tiling参数获取
4. AscendC::LocalTensor<uint8_t> sharedTmpBuffer = tmpQue.AllocTensor<uint8_t>();
5. // 输入shape信息为1024Bytes, 算子输入的数据类型为half, 实际计算个数为512Bytes
6. AscendC::Sigmoid(dstLocal, srcLocal, sharedTmpBuffer, 512);
```

结果示例如下：

```
1. 输入数据(srcLocal): [1.762616 7.9542747 ... 7.8306146 6.3167496]
2. 输出数据(dstLocal):  [0.853537 0.996489 ... 0.996027 0.998197]
```
