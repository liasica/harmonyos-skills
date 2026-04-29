---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datacopypad
title: DataCopyPad
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 数据搬运 > DataCopyPad
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:78d681932a1e80e09c572226e740cbca365c6820466b1cf82cf9de8ffadec3bd
---

## 功能说明

该接口提供数据非对齐搬运的功能，支持的数据传输通路如下。

* GM->VECIN/VECOUT
* VECIN/VECOUT->GM
* VECIN/VECOUT->TSCM

其中从GM->VECIN/VECOUT进行数据搬运时，可以根据开发者的需要自行填充数据。

## 函数原型

* dataCopyParams为DataCopyExtParams类型，相比于DataCopyParams类型，支持的操作数步长等参数取值范围更大

  + 通路：GM->VECIN/VECOUT

    ```
    1. template <typename T>
    2. __aicore__ inline  void DataCopyPad(const LocalTensor<T> &dstLocal, const GlobalTensor<T> &srcGlobal, const DataCopyExtParams &dataCopyParams, const DataCopyPadExtParams<T> &padParams)
    ```
  + 通路：VECIN/VECOUT->GM

    ```
    1. template <typename T>
    2. __aicore__ inline  void DataCopyPad(const GlobalTensor<T> &dstGlobal, const LocalTensor<T> &srcLocal, const DataCopyExtParams &dataCopyParams)
    ```
* dataCopyParams为DataCopyParams类型

  + 通路：GM->VECIN/VECOUT

    ```
    1. template<typename T>
    2. __aicore__ inline void DataCopyPad(const LocalTensor<T>& dstLocal, const GlobalTensor<T>& srcGlobal, const DataCopyParams& dataCopyParams, const DataCopyPadParams& padParams)
    ```
  + 通路：VECIN/VECOUT->GM

    ```
    1. template<typename T>
    2. __aicore__ inline void DataCopyPad(const GlobalTensor<T>& dstGlobal, const LocalTensor<T>& srcLocal,const DataCopyParams& dataCopyParams)
    ```

## 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T | 操作数以及paddingValue（待填充数据值）的数据类型。  Kirin9020系列处理器，支持的数据类型为：int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float  KirinX90系列处理器，支持的数据类型为：int8\_t/uint8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/half/float |

**表2** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal, dstGlobal | 输出 | 目的操作数，类型为LocalTensor或GlobalTensor。 |
| srcLocal, srcGlobal | 输入 | 源操作数，类型为LocalTensor或GlobalTensor。 |
| dataCopyParams | 输入 | 搬运参数。  - DataCopyExtParams类型，具体参数说明请参考表3。  - DataCopyParams类型，具体参数说明请参考表4。 |
| padParams | 输入 | 从GM->VECIN/VECOUT进行数据搬运时，可以根据开发者需要，在搬运数据左边或右边填充数据。padParams是用于控制数据填充过程的参数，DataCopyPadExtParams类型，具体参数请参考表5。 |
| nd2nzParams | 输入 | 从VECIN/VECOUT->TSCM进行数据搬运时，可以进行ND到NZ的数据格式转换。nd2nzParams是用于控制数据格式转换的参数，Nd2NzParams类型，具体参数为：ndNum、nValue、dValue、srcNdMatrixStride、srcDValue、dstNzC0Stride、dstNzNStride、dstNzMatrixStride。  **说明：** Nd2NzParams的ndNum仅支持设置为1。 |

**表3** DataCopyExtParams结构体参数定义

| 参数名称 | 含义 |
| --- | --- |
| blockCount | 指定该指令包含的连续传输数据块个数，数据类型为uint16\_t，取值范围：blockCount∈[1, 4095]。 |
| blockLen | 指定该指令每个连续传输数据块长度，**该指令支持非对齐搬运**，**每个连续传输数据块长度单位为Byte**。数据类型为uint32\_t，blockLen不要超出该数据类型的取值范围。 |
| srcStride | 源操作数，相邻连续数据块的间隔（前面一个数据块的尾与后面数据块的头的间隔），**如果源操作数的逻辑位置为VECIN/VECOUT，则单位为dataBlock(32Bytes), 如果源操作数的逻辑位置为GM,则单位为Byte**。数据类型为uint32\_t，srcStride不要超出该数据类型的取值范围。 |
| dstStride | 目的操作数，相邻连续数据块间的间隔（前面一个数据块的尾与后面数据块的头的间隔），**如果目的操作数的逻辑位置为VECIN/VECOUT，则单位为dataBlock(32Bytes)，如果目的操作数的逻辑位置为GM，则单位为Byte**。数据类型为uint32\_t，dstStride不要超出该数据类型的取值范围。 |
| rsv | 保留字段。 |

**表4** DataCopyParams结构体参数定义

| 参数名称 | 含义 |
| --- | --- |
| blockCount | 指定该指令包含的连续传输数据块个数，数据类型为uint16\_t，取值范围：blockCount∈[1, 4095]。 |
| blockLen | 指定该指令每个连续传输数据块长度，**该指令支持非对齐搬运**，**每个连续传输数据块长度单位为Byte**。数据类型为uint16\_t，blockLen不要超出该数据类型的取值范围。 |
| srcStride | 源操作数，相邻连续数据块的间隔（前面一个数据块的尾与后面数据块的头的间隔），**如果源操作数的逻辑位置为VECIN/VECOUT，则单位为dataBlock(32Bytes), 如果源操作数的逻辑位置为GM,则单位为Byte**。数据类型为uint16\_t，srcStride不要超出该数据类型的取值范围。 |
| dstStride | 目的操作数，相邻连续数据块间的间隔（前面一个数据块的尾与后面数据块的头的间隔），**如果目的操作数的逻辑位置为VECIN/VECOUT，则单位为dataBlock(32Bytes)，如果目的操作数的逻辑位置为GM，则单位为Byte**。数据类型为uint16\_t，dstStride不要超出该数据类型的取值范围。 |

**表5** DataCopyPadExtParams结构体参数定义

| 参数名称 | 含义 |
| --- | --- |
| isPad | 是否需要填充开发者自定义的数据，取值范围：true，false。  true：填充padding value。  false：表示开发者不需要指定填充值，会默认填充随机值。 |
| leftPadding | 连续搬运数据块左侧需要补充的数据范围，单位为元素个数。  **leftPadding、rightPadding的字节数均不能超过32Bytes。** |
| rightPadding | 连续搬运数据块右侧需要补充的数据范围，单位为元素个数。  **leftPadding、rightPadding的字节数均不能超过32Bytes。** |
| paddingValue | 左右两侧需要填充的数据值，需要保证在数据占用字节范围内。  数据类型和源操作数保持一致，T数据类型。  **当数据类型长度为64位时，该参数只能设置为0。** |

* **GM**->**VECIN/VECOUT**

  **参数解释**：

  + 当blockLen+leftPadding+rightPadding满足32字节对齐时，isPad为false，左右两侧填充的数据值会默认为随机值，否则为paddingValue。
  + 当blockLen+leftPadding+rightPadding不满足32字节对齐时，框架会填充一些假数据dummy，保证左右填充的数据和blockLen、假数据为32字节对齐。若leftPadding、rightPadding都为0：dummy会默认填充待搬运数据块的第一个元素值。若leftPadding/rightPadding不为0：isPad为false，左右两侧填充的数据值和dummy值均为随机值，否则为paddingValue。

  **配置示例1：**

  + blockLen为64，每个连续传输数据块包含64Bytes。srcStride为1，因为源操作数的逻辑位置为GM，srcStride的单位为Byte，也就是说源操作数相邻数据块之间间隔1Byte；dstStride为1，因为目的操作数的逻辑位置为VECIN/VECOUT，dstStride的单位为dataBlock(32Bytes)，也就是说目的操作数相邻数据块之间间隔1个dataBlock。
  + blockLen+leftPadding+rightPadding满足32字节对齐，isPad为false，左右两侧填充的数据值会默认为随机值，否则为paddingValue。此处示例中，leftPadding、rightPadding均为0，则不填充。
  + blockLen+leftPadding+rightPadding不满足32字节对齐时，框架会填充一些假数据dummy，保证左右填充的数据和blockLen、假数据为32字节对齐。leftPadding/rightPadding不为0：若isPad为false，左右两侧填充的数据值和dummy值均为随机值，否则为paddingValue。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/lXWvkPB_Qea-wYKF4bxzBw/zh-cn_image_0000002558765780.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=0A0BFEDE23B4E6F2E1EA089DEE2EC63972CDC644DAA83C10ED04137D9624547D)

  **配置示例2：**

  + blockLen为47，每个连续传输数据块包含47Bytes；srcStride为1，表示源操作数相邻数据块之间间隔1Byte；dstStride为1，表示目的操作数相邻数据块之间间隔1个dataBlock。
  + blockLen+leftPadding+rightPadding不满足32字节对齐，leftPadding、rightPadding均为0：dummy会默认填充待搬运数据块的第一个元素值。
  + blockLen+leftPadding+rightPadding不满足32字节对齐，leftPadding/rightPadding不为0：若isPad为false，左右两侧填充的数据值和dummy值均为随机值，否则为paddingValue。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ftOLqUqaSWGTGNDbnItE1Q/zh-cn_image_0000002558606124.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=5F4B9C23BD23CE185BF515D7827D1A0F816AAE8E5BB7D7405F0DB7B84C902359)
* **VECIN/VECOUT**->**GM**

  当每个连续传输数据块长度blockLen为32字节对齐时，下图呈现了需要传入的DataCopyParams示例，blockLen为64，每个连续传输数据块包含64Bytes；srcStride为1，因为源操作数的逻辑位置为VECIN/VECOUT，srcStride的单位为dataBlock(32Bytes)，也就是说源操作数相邻数据块之间间隔1个dataBlock；dstStride为1，因为目的操作数的逻辑位置为GM，dstStride的单位为Byte，也就是说目的操作数相邻数据块之间间隔1Byte。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/aaaILJCnQgO-EBNBNTKAXg/zh-cn_image_0000002589325651.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=172ACED466C5A3EEBC089774EFF3E6A10E842445D22AE1A947E8C2AB1E31B59C)

  当每个连续传输数据块长度blockLen不满足32字节对齐，由于Unified Buffer要求32字节对齐，框架在搬出时会自动补充一些假数据来保证对齐，但在当搬到GM时会自动将填充的假数据丢弃掉。下图呈现了该场景下需要传入的DataCopyParams示例和假数据补齐的原理。blockLen为47，每个连续传输数据块包含47Bytes，不满足32字节对齐；srcStride为1，表示源操作数相邻数据块之间间隔1个dataBlock；dstStride为1，表示目的操作数相邻数据块之间间隔1Byte。框架在搬出时会自动补充17Bytes的假数据来保证对齐，搬到GM时再自动将填充的假数据丢弃掉。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/UPiPvQBVSKC6Mq4JRho9KQ/zh-cn_image_0000002589245591.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=41BD59BB33E1685F72012C1A02694E7CD69EFAF1DDFD73FAAFE34232CC65F4EC)
* **VECIN/VECOUT->TSCM**

  内部实现涉及AIC和AIV之间的通信，实际搬运路径为VECIN/VECOUT->GM->TSCM，**发送通信消息会有开销，性能会受到影响**。

  如下图所示，展示了从VECIN/VECOUT搬运到GM，再搬运到TSCM的过程：示例中数据类型为half，单个datablock（32B）含有16个half元素，源操作数中的 A1~A6、B1~B6、C1~C6为需要进行搬运的数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/3kAATfaDTWWtvB-wz6jLFg/zh-cn_image_0000002558765782.png?HW-CC-KV=V1&HW-CC-Date=20260429T054124Z&HW-CC-Expire=86400&HW-CC-Sign=2DE8F8115077D81556732C2E97056C8D69EE60048010966BE6FB028862ED00FF)

  从VECIN/VECOUT->GM的搬运，数据存储格式没有发生转变，依然是ND。

  + **blockCount**为需要搬运的连续传输数据块个数，设置为3。
  + **blockLen**为一个连续传输数据块的大小(单位为Byte)，设置为6 \* 32 = 192。
  + **srcStride**为源操作数相邻连续数据块的间隔（前面一个数据块的尾与后面数据块的头的间隔），源操作数逻辑位置为VECIN/VECOUT，其单位为datablock, 两个连续传输数据块（A1~A6、B1~B6）中间相隔1个A7，因此srcStride设置为1。
  + **dstStride**为目的操作数，相邻连续数据块间的间隔（前面一个数据块的尾与后面数据块的头的间隔），目的操作数逻辑位置为GM，其单位为Byte，两个连续传输数据块（A1~A6、B1~B6）中间相隔2个空白的datablock，因此dstStride设置为64Byte。

  从GM->TSCM的搬运，数据存储格式由ND转换为NZ。

  + **ndNum**固定为1，即A1~A6、B1~B6、C1~C6视作一整个ndMatrix。
  + **nValue**为ndMatrix的行数，即为3行。
  + **dValue**为ndMatrix中一行包含的元素个数，即为6 \* 16 = 96个元素。
  + **srcNdMatrixStride**为相邻ndMatrix之间的距离，因为仅涉及1个ndMatrix，所以可填为0。
  + **srcDValue**表明ndMatrix的第x行和第x+1行所相隔的元素个数，如A1~B1的距离，即为8个datablock，8 \* 16 = 128个元素。
  + **dstNzC0Stride**为src同一行的相邻datablock在NZ矩阵中相隔datablock数，如A1~A2的距离，即为7个datablock (A1 + 空白 + B1 + 空白 + C1 + 空白 \* 2)。
  + **dstNzNStride**为src中ndMatrix的相邻行在NZ矩阵中相隔多少个datablock，如A1~B1的距离，即为2个datablock (A1 + 空白) 。
  + **dstNzMatrixStride**为相邻NZ矩阵之间的元素个数，因为仅涉及1个NZ矩阵，所以可以填为1。

## 返回值

无

## 支持的型号

Kirin9020系列处理器。

KirinX90系列处理器

## 约束说明

leftPadding、rightPadding的字节数均不能超过32Bytes。

## 调用示例

本示例实现了GM->VECIN->GM的非对齐搬运过程。

```
1. #include "kernel_operator.h"

3. class TestDataCopyPad {
4. public:
5. __aicore__ inline TestDataCopyPad() {}
6. __aicore__ inline void Init(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
7. {
8. srcGlobal.SetGlobalBuffer((__gm__ half *)srcGm);
9. dstGlobal.SetGlobalBuffer((__gm__ half *)dstGm);
10. pipe.InitBuffer(inQueueSrc, 1, 32 * sizeof(half));
11. pipe.InitBuffer(outQueueDst, 1, 32 * sizeof(half));
12. }
13. __aicore__ inline void Process()
14. {
15. CopyIn();
16. Compute();
17. CopyOut();
18. }
19. private:
20. __aicore__ inline void CopyIn()
21. {
22. AscendC::LocalTensor<half> srcLocal = inQueueSrc.AllocTensor<half>();
23. AscendC::DataCopyExtParams copyParams{1, 20 * sizeof(half), 0, 0, 0}; // 结构体DataCopyExtParams最后一个参数是rsv保留位
24. AscendC::DataCopyPadExtParams<half> padParams{true, 0, 2, 0};
25. AscendC::DataCopyPad(srcLocal, srcGlobal, copyParams, padParams); // 从GM->VECIN搬运40Bytes
26. inQueueSrc.EnQue<half>(srcLocal);
27. }
28. __aicore__ inline void Compute()
29. {
30. AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
31. AscendC::LocalTensor<half> dstLocal = outQueueDst.AllocTensor<half>();
32. AscendC::Adds(dstLocal, srcLocal, scalar, 20);
33. outQueueDst.EnQue(dstLocal);
34. inQueueSrc.FreeTensor(srcLocal);
35. }
36. __aicore__ inline void CopyOut()
37. {
38. AscendC::LocalTensor<half> dstLocal = outQueueDst.DeQue<half>();
39. AscendC::DataCopyExtParams copyParams{1, 20 * sizeof(half), 0, 0, 0};
40. AscendC::DataCopyPad(dstGlobal, dstLocal, copyParams); // 从VECIN->GM搬运40Bytes
41. outQueueDst.FreeTensor(dstLocal);
42. }
43. private:
44. AscendC::TPipe pipe;
45. AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
46. AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
47. AscendC::GlobalTensor<half> srcGlobal;
48. AscendC::GlobalTensor<half> dstGlobal;
49. AscendC::DataCopyPadExtParams<half> padParams;
50. AscendC::DataCopyExtParams copyParams;
51. half scalar = 0;
52. };

54. extern "C" __global__ __aicore__ void kernel_data_copy_pad_kernel(__gm__ uint8_t* src_gm, __gm__ uint8_t* dst_gm)
55. {
56. TestDataCopyPad op;
57. op.Init(src_gm, dst_gm);
58. op.Process();
59. }
```

结果示例：

```
1. 输入数据(src0Global): [1 2 3 ... 32]
2. 输出数据(dstGlobal):[1 2 3 ... 20]
```
