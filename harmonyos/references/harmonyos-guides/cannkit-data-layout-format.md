---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-data-layout-format
title: 数据排布格式
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > Tensor基础知识参考 > 数据排布格式
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:d4fd24c7d28962aa30220289a4d9fc627e7587d8d7ae71efcac8e3cf7571d587
---

Format为数据的物理排布格式，决定了如何解读数据的维度，比如1D，2D，3D，4D，5D等。

## NCHW和NHWC

在深度学习领域，多维数据通过多维数组存储，比如卷积神经网络的特征图(Feature Map)通常用四维数组保存，即4D，4D格式解释如下。

* N：Batch数量，例如图像的数目。
* H：Height，特征图高度，即垂直高度方向的像素个数。
* W：Width，特征图宽度，即水平宽度方向的像素个数。
* C：Channels，特征图通道，例如彩色RGB图像的Channels为3。

由于数据只能线性存储，因此这四个维度有对应的顺序。不同深度学习框架会按照不同的顺序存储特征图数据，比如Caffe，排列顺序为[Batch, Channels, Height, Width]，即NCHW。TensorFlow中，排列顺序为[Batch, Height, Width, Channels]，即NHWC。

如下图所示，以一张格式为RGB的图片为例，NCHW中，C排列在外层，实际存储的是“RRRRRRGGGGGGBBBBBB”，即同一通道的所有像素值顺序存储在一起；而NHWC中C排列在最内层，实际存储的则是“RGBRGBRGBRGBRGBRGB”，即多个通道的同一位置的像素值顺序存储在一起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/stKdK8QsRo2W6mswJvxV5A/zh-cn_image_0000002736434465.png)

尽管存储的数据相同，但不同的存储顺序会导致数据的访问特性不一致，因此即便进行同样的运算，相应的计算性能也会不同。

## NC1HWC0

Kirin AI处理器中，为了提高通用矩阵乘法(GEMM)运算数据块的访问效率，所有张量数据统一采用NC1HWC0的五维数据格式。其中C0与微架构强相关，等于AI Core中矩阵计算单元的大小。

C1=(C+C0-1)/C0。如果结果不整除，向上取整。

NHWC/NCHW -> NC1HWC0的转换过程为：将数据在C维度进行分割，变成C1份NHWC0/NC0HW，再将C1份NHWC0/NC0HW在内存中连续排列成NC1HWC0，其格式转换示意图如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/tY_sFkKBQ-6I2PIQANrvCw/zh-cn_image_0000002706835318.png)

* NHWC -> NC1HWC0的转换公式如下。

  ```cpp
  Tensor.reshape([N, H, W, C1, C0]).transpose([0, 3, 1, 2, 4])
  ```
* NCHW -> NC1HWC0的转换公式如下。

  ```cpp
  Tensor.reshape([N, C1, C0, H, W]).transpose([0, 1, 3, 4, 2])
  ```

## FRACTAL\_NZ

FRACTAL\_NZ是分形格式，如Feature Map的数据存储，在cube单元计算时，输出矩阵的数据格式为NW1H1H0W0。整个矩阵被分为（H1\*W1）个分形，按照column major排布，形状如N字形；每个分形内部有（H0\*W0）个元素，按照row major排布，形状如z字形。考虑到数据排布格式，将NW1H1H0W0数据格式称为Nz（大N小z）格式。其中，H0,W0表示一个分形的大小，示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/2-U-VLfSSlm_pxrsgJRwvQ/zh-cn_image_0000002736314423.png)

ND –> FRACTAL\_NZ的变换过程为：

```text
(..., N, H, W )->pad->(..., N, H1*H0, W1*W0)->reshape->(..., N, H1, H0, W1, W0)->transpose->(..., N, W1, H1, H0, W0)
```

## FRACTAL\_Z

FRACTAL\_Z是用于定义卷积权重的数据格式，由FT Matrix（FT：Filter，卷积核）变换得到。FRACTAL\_Z是送往Cube的最终数据格式，采用“C1HW,N1,N0,C0”的4维数据排布。

数据有两层Tiling，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/9dmMJak2S4CXTOWfPdHZuA/zh-cn_image_0000002706675380.png)

第一层与Cube的Size相关，数据按照列的方向连续（小n）；第二层与矩阵的Size相关，数据按照行的方向连续（大Z）。

例如：HWCN = (2, 2, 32, 32)，将其变成FRACTAL\_Z( C1HW, N1, N0, C0 ) = (8, 2, 16, 16)。

HWCN变换FRACTAL\_Z的过程为：

```cpp
Tensor.padding([ [0,0], [0,0], [0,(C0–C%C0)%C0], [0,(N0–N%N0)%N0] ]).reshape( [H, W, C1, C0, N1, N0]).transpose( [2, 0, 1, 4, 5, 3] ).reshape( [C1*H*W, N1, N0, C0])
```

NCHW变换FRACTAL\_Z的过程为：

```cpp
Tensor.padding([ [0,(N0–N%N0)%N0], [0,(C0–C%C0)%C0], [0,0], [0,0] ]).reshape( [N1, N0, C1, C0, H, W]).transpose( [2, 4, 5, 0, 1, 3] ).reshape( [C1*H*W, N1, N0, C0])
```
