---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-knowledge
title: 基础知识
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 矩阵编程（高阶API） > 基础知识
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec5a09f3cda91b5d556abab23dd16fb33cb4290c24e7e78d2def95cb77741fca
---

说明

本节内容为使用高阶API进行矩阵乘法的编程指导。使用高阶API进行实际的矩阵编程时，需要通过[Matmul](cannkit-matmul-usage-description.md)查看确认接口支持的产品型号。

## 矩阵乘法概述

MatMul的计算公式为：C = A \* B + bias，其示意图如下。

* A、B为源操作数，A为左矩阵，形状为[M, K]；B为右矩阵，形状为[K, N]。
* C为目的操作数，存放矩阵乘结果的矩阵，形状为[M, N]。
* bias为矩阵乘偏置，形状为[1, N]。对A\*B结果矩阵的每一行都采用该bias进行偏置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/z7N_MdaJRf2ReEtai7aNAA/zh-cn_image_0000002589325613.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=4F9B9DD160A1DFABD6963E412008841D035B6FA11ACEAD7B6CBFD7D2686F699F)

## 矩阵乘法数据流

在了解矩阵乘法数据流之前，需要先回顾一下几个重要的存储**逻辑位置**的概念：

* 搬入数据的存放位置：A1，用于存放整块A矩阵，可类比CPU多级缓存中的二级缓存。
* 搬入数据的存放位置：B1，用于存放整块B矩阵，可类比CPU多级缓存中的二级缓存。
* 搬入数据的存放位置：A2，用于存放切分后的小块A矩阵，可类比CPU多级缓存中的一级缓存。
* 搬入数据的存放位置：B2，用于存放切分后的小块B矩阵，可类比CPU多级缓存中的一级缓存。
* 结果数据的存放位置：CO1，用于存放小块结果C矩阵，可理解为Cube Out。
* 结果数据的存放位置：CO2，用于存放整块结果C矩阵，可理解为Cube Out。
* 搬入数据的存放位置：VECCALC，一般在计算需要临时变量时使用此位置。

**矩阵乘法数据流**指矩阵乘的输入输出在各存储位置间的流向。逻辑位置的数据流向如下图所示（为了简化描述，没有列出bias）：

* A矩阵从输入位置到A2的数据流如下（输入位置可以是GM或者VECOUT）：GM->A2，GM->A1->A2；VECOUT->A1->A2。
* B矩阵从输入位置到B2的数据流如下（输入位置可以是GM或者VECOUT）：GM->B2，GM->B1->B2；VECOUT->B1->B2。
* 完成A2\*B2=CO1计算。
* CO1数据汇聚到CO2：CO1->CO2。
* 从CO2到输出位置（输出位置可以是GM或者VECIN）：CO2->GM/CO2->VECIN。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/yDvRRdgpR-yhjXGP7XPX4g/zh-cn_image_0000002589245553.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=AE16485BB414333B65B5A1E182EC7F80C435F4108EEBA9A24173E308E22FFEE8)

## 数据格式

在完成Matmul矩阵乘法时，涉及到两种分形格式ND和NZ。

* ND：普通格式，N维张量。
* NZ：为满足AICore中Cube计算单元高性能计算的需要，引入该特殊格式。

  ND –> NZ的变换过程为：

  (..., N，H, W )->pad->(..., N, H1\*H0, W1\*W0)->reshape->(..., N, H1, H0, W1, W0)->transpose->(..., N, W1, H1, H0, W0)

  如下图所示 （W，H）大小的矩阵被分为（H1\*W1）个分形，按照column major排布，形状如N字形；每个分形内部有（H0\*W0）个元素，按照row major排布，形状如z字形。所以这种数据格式称为NZ（大N小Z）格式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/iII1JFvLRS-KMRUREQIaUw/zh-cn_image_0000002558765744.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=C0E7FFD80CDFFB553802249926EF91109465C3441068AB3CA662D16F1C9E9608)

  下面我们再通过一个具体的例子来深入理解ND和NZ格式的数据排布区别。假设分形格式为2\*2，如下图所示4\*4的矩阵，ND和NZ格式存储两种情况下，数据在内存中的排布格式分别为：

  ND：0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

  NZ：0, 1, 4, 5, 8, 9, 12, 13, 2, 3, 6, 7, 10, 11, 14, 15

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/j2E25zEFQw6Mh7iLrdaLrg/zh-cn_image_0000002558606088.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=4E34CD5B8BE1612EE3116925F53B0A4EF769D20478DA8906A92A683C949C557C)

## 数据分块(Tiling)

### 多核切分

为了实现多核并行，需要将矩阵数据进行切分，分配到不同的核上进行处理。切分策略如下图所示：

* 对于A矩阵，沿着M轴进行切分，切分成多份的singleCoreM，单核上处理SingleCoreM \* K大小的数据。
* 对于B矩阵，沿着N轴进行切分，切分成多份的singleCoreN，单核上处理K \* SingleCoreN大小的数据。
* 对于C矩阵，SingleCoreM \* K大小的A矩阵和K \* SingleCoreN大小的B矩阵相乘得到SingleCoreM \* SingleCoreN大小的C矩阵，即为单核上输出的C矩阵大小。

比如，下图中共有8个核参与计算，将A矩阵沿着M轴划分为4块，将B矩阵沿着N轴切分为两块，单核上仅处理某一分块（比如图中绿色部分为core3上参与计算的数据）：SingleCoreM \* K大小的A矩阵分块和SingleCoreN\* K大小的B矩阵分块相乘得到SingleCoreM \* SingleCoreN大小的C矩阵分块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/oGykcnCZQ0axO7PPhUdHMA/zh-cn_image_0000002589325615.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=B144F4902F00B9093E35B11BCAED532145223FFADD962F1565534D7CB0F97051)

### 核内切分

大多数情况下，Local Memory的存储，无法完整的容纳算子的输入与输出，需要每次搬运一部分输入进行计算然后搬出，再搬运下一部分输入进行计算，直到得到完整的最终结果，也就是需要做核内的输入切分。切分的策略如下所示：

* 对于A矩阵，沿M轴进行切分，切分成多份的baseM；沿K轴进行切分，切分成多份的baseK。
* 对于B矩阵，沿N轴进行切分，切分成多份的baseN，沿K轴进行切分，切分成多份的baseK。
* 对于C矩阵，A矩阵中baseM\*baseK大小的分块和B矩阵中baseK\*baseN大小的分块相乘并累加，得到C矩阵中对应位置baseM\*baseN大小的分块。比如，图中结果矩阵中的蓝色矩阵块5是通过如下的累加过程得到的：a\*a+b\*b+c\*c+d\*d+e\*e+f\*f。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/9zARE2mcRUi8YYEKpbBMbw/zh-cn_image_0000002589245555.png?HW-CC-KV=V1&HW-CC-Date=20260429T054106Z&HW-CC-Expire=86400&HW-CC-Sign=369C49A553DF1B67DEA5632FD2103B50FAB8B4108D3E06189B80DDD63DD8DDF7)

除了baseM, baseN, baseK外，还有一些常用的tiling参数，其含义如下。

* iterateOrder：一次Iterate迭代计算出[baseM, baseN]大小的C矩阵分片。Iterate完成后，Matmul会自动偏移下一次Iterate输出的C矩阵位置，iterateOrder表示自动偏移的顺序。

  + 0代表先往M轴方向偏移再往N轴方向偏移。
  + 1代表先往N轴方向偏移再往M轴方向偏移。
* depthA1，depthB1：A1、B1上存储的矩阵片全载A2/B2的份数，A2、B2存储大小分别是baseM \* baseK，baseN \* baseK。
* stepM，stepN：stepM为左矩阵在A1中缓存的buffer M方向上baseM的倍数。stepN为右矩阵在B1中缓存的buffer N方向上baseN的倍数。
* stepKa，stepKb：stepKa为左矩阵在A1中缓存的buffer K方向上baseK的倍数，stepKb为右矩阵在B1中缓存的buffer K方向上baseK的倍数。
