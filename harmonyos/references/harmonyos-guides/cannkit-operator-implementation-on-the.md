---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-implementation-on-the
title: Kernel侧算子实现
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 工程化算子开发 > 基于工程实现算子 > Kernel侧算子实现
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5f14a5860702e274fd65c7d03c496e76ef20a4a8fe72e9dfacc1586ca429413
---

在[算子实现](cannkit-operator-implementation-overview.md)章节已经介绍了kernel侧算子核心的实现方法，本章节侧重于介绍接入DDK框架时编程模式和API的使用。

## 自动生成kernel侧算子实现模板

在算子工程目录下的“op\_kernel/xxx.cpp”文件中实现算子的核函数。核函数的定义模板已通过msOpGen工具自动生成，样例如下所示。**这里参数的顺序按照“输入、输出、workspace、tiling”的顺序排布，开发者不要调整其顺序。**

```
1. #include "kernel_operator.h"
2. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling) {
3. GET_TILING_DATA(tiling_data, tiling);// 获取Tiling参数，详见下文介绍
4. // TODO: user kernel impl
5. }
```

**简要说明：**

算子原型定义中的输入和输出同名的情况下，自动生成的核函数中，输出参数增加ref后缀予以区分。示例如下。

```
1. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR x_ref, GM_ADDR workspace, GM_ADDR tiling) {
2. // ...
3. }
```

## GET\_TILING\_DATA获取Tiling参数

提供[GET\_TILING\_DATA](cannkit-get-tiling-data.md)，用于获取算子kernel入口函数传入的tiling信息，并填入注册的Tiling结构体中，此函数会以宏展开的方式进行编译。注意，对应的算子host实现中需要定义TilingData结构体，实现并注册计算TilingData的Tiling函数。具体请参考[Host侧Tiling实现](cannkit-tiling-implementation-on-the-host.md)。

核函数中调用[GET\_TILING\_DATA](cannkit-get-tiling-data.md)获取TilingData的样例如下。

```
1. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
2. {
3. GET_TILING_DATA(tilingData, tiling);
4. KernelAdd op;
5. op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum);
6. if (TILING_KEY_IS(1)) {
7. op.Process();
8. }
9. }
```

## 核函数内推导输入数据类型和格式

算子工程在核函数内提供了DTYPE\_<Arg>、ORIG\_DTYPE\_<Arg>、FORMAT\_<Arg>三种宏用于推导核函数入参的数据类型、原始数据类型和数据格式。其中<Arg>会自动大写。样例如下。

```
1. template<class T> func() {}
2. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
3. {
4. DTYPE_X temp;
5. func<DTYPE_Z>();
6. if (FORMAT_Y == FORMAT_ND) {
7. // ...
8. }
9. }
```

## 输出shape依赖计算的算子kernel侧实现

某些算子，比如NonZero（统计tensor中非零值的个数），计算完成前无法得知算子输出的shape信息，算子计算完成后才能获取。该类算子在原型定义时，需要使用[OutputShapeDependOnCompute](cannkit-outputshapedependoncompute.md)接口进行标识，同时在算子核函数中将实际输出shape写入到出参中，便于框架侧基于该信息进行输出内存的管理。

在核函数所有输出的最后增加一个GM\_ADDR类型的输出参数，并在核函数计算完成后，将输出shape信息写入到该出参中。shape信息的排布格式如下，大小为**n \* (8 + 1)**，每个元素的数据类型为**uint64\_t**。其中n表示待刷新shape信息的输出个数，每个输出的shape信息都通过第1个元素来保存实际的shape维度(dim)，后续的8个元素来保存具体每个维度的shape信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/kAJBeCrgTOymjoFhH1pv-A/zh-cn_image_0000002558606092.png?HW-CC-KV=V1&HW-CC-Date=20260429T054108Z&HW-CC-Expire=86400&HW-CC-Sign=D84B927D2D9C19515F132F9DC803834FE7B0FA39C3CF9F5A5171B1F766FF94AA)

说明

* 输出的顺序和原型定义中输出的顺序保持一致。
* 对于uint64\_t的输出数据类型（对于tensor而言），需要将dim的uint32\_t的高位设置为1，表示以uint64\_t类型解析该tensor。

* 如下示例中，算子中有一个输出依赖计算得出，输出tensor的数据类型为uint32\_t，计算完成后，得到输出的shape为（32, 64），出参shape\_out用于存放该shape信息，值为（2, 32, 64）。代码示例如下。

  ```
  1. extern "C" __global__ __aicore__ void xxx_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR shape_out, GM_ADDR workspace, GM_ADDR tiling) {
  2. // ...
  3. constexpr uint32_t SHAPEOUT_SIZE = 9;
  4. // 输出数据为2维([32, 64])，tensor类型为uint32_t
  5. GlobalTensor<uint64_t> shapeoutGlobal_uint32;
  6. shapeoutGlobal_uint32.SetGlobalBuffer((__gm__ uint64_t*)shape_out, SHAPEOUT_SIZE);
  7. shapeoutGlobal_uint32.SetValue(0, 2);
  8. shapeoutGlobal_uint32.SetValue(1, 32);
  9. shapeoutGlobal_uint32.SetValue(2, 64);
  10. // ...
  11. }
  ```
* 如下示例中，算子中有一个输出依赖计算得出，输出tensor的数据类型为uint64\_t，计算完成后，得到输出的shape为（32, 64），出参shape\_out用于存放该shape信息，值为（0x0000000010000000 | 2, 32, 64）。代码示例如下。

  ```
  1. extern "C" __global__ __aicore__ void xxx_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR shape_out, GM_ADDR workspace, GM_ADDR tiling) {
  2. // ...
  3. constexpr uint32_t SHAPEOUT_SIZE = 9;
  4. // 输出数据为4维([1, 64, 128, 128])，tensor类型为uint64_t
  5. GlobalTensor<uint64_t> shapeoutGlobal_uint64;
  6. shapeoutGlobal_uint64.SetGlobalBuffer((__gm__ uint64_t*)shape_out, SHAPEOUT_SIZE);
  7. shapeoutGlobal_uint64.SetValue(0, 0x0000000010000000 | 4);
  8. shapeoutGlobal_uint64.SetValue(1, 1);
  9. shapeoutGlobal_uint64.SetValue(2, 64);
  10. shapeoutGlobal_uint64.SetValue(3, 128);
  11. shapeoutGlobal_uint64.SetValue(4, 128);
  12. // ...
  13. }
  ```
* 如下示例中，算子中有两个输出依赖计算得出，输出tensor的数据类型为uint64\_t，计算完成后，得到输出的shape为（16, 32）和 （1, 16, 16, 32），出参shape\_out用于存放该shape信息。示例如下。

  ```
  1. extern "C" __global__ __aicore__ void xxx_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR shape_out, GM_ADDR workspace, GM_ADDR tiling) {
  2. // ...
  3. // 有两个输出需要刷新shape，一个维度为2维[16, 32]，一个维度为4维[1, 16, 16, 32]
  4. // tensor类型为uint64_t
  5. constexpr uint32_t SHAPEOUT_SIZE_2 = 18;
  6. GlobalTensor<uint64_t> shapeoutGlobal_uint64_2;
  7. shapeoutGlobal_uint64_2.SetGlobalBuffer((__gm__ uint64_t*)shape_out, SHAPEOUT_SIZE_2 );
  8. shapeoutGlobal_uint64_2.SetValue(0, 0x0000000010000000 | 2);
  9. shapeoutGlobal_uint64_2.SetValue(1, 16);
  10. shapeoutGlobal_uint64_2.SetValue(2, 32);
  11. // index[3]~index[8]数据为占位
  12. shapeoutGlobal_uint64_2.SetValue(9, 0x0000000010000000 | 4);
  13. shapeoutGlobal_uint64_2.SetValue(10, 1);
  14. shapeoutGlobal_uint64_2.SetValue(11, 16);
  15. shapeoutGlobal_uint64_2.SetValue(12, 16);
  16. shapeoutGlobal_uint64_2.SetValue(13, 32);
  17. // ...
  18. }
  ```
