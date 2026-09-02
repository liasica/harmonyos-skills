---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-tiling-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul Tiling > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:009d7a4d55f33f3491bec3fd87179a1b26ce484d69404330cad506fe0a641b03
---

## 功能说明

用于创建一个Matmul单核Tiling对象，或者多核Tiling对象，或者BatchMatmul Tiling对象。

## 函数原型

* 带参构造函数，需要传入硬件平台信息，推荐使用这类构造函数来获得更好的兼容性。

  + 使用PlatformAscendC类传入信息

    ```cpp
    explicit MatmulApiTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)
    explicit MultiCoreMatmulTiling(const platform_ascendc::PlatformAscendC& ascendcPlatform)
    explicit BatchMatmulTiling(const platform_ascendc::PlatformAscendC &ascendcPlatform)
    ```
  + 使用PlatformInfo传入信息

    当platform\_ascendc::PlatformAscendC无法在Tiling运行时获取时，需要开发者自己构造PlatformInfo结构体，透传给MatmulApiTiling构造函数。

    ```cpp
    explicit MatmulApiTiling(const PlatformInfo& platform)
    explicit MultiCoreMatmulTiling(const PlatformInfo &platform)
    ```
* 无参构造函数

  支持如下产品型号：

  Kirin9020系列处理器

  Kirin9030系列处理器

  ```cpp
  MatmulApiTiling()
  MultiCoreMatmulTiling()
  BatchMatmulTiling()
  ```
* 基类构造函数

  MatmulApiTiling、MultiCoreMatmulTiling和BatchMatmulTiling都继承自基类MatmulApiTilingBase，其构造函数如下。

  ```cpp
  MatmulApiTilingBase()
  explicit MatmulApiTilingBase(const platform_ascendc::PlatformAscendC& ascendcPlatform)
  explicit MatmulApiTilingBase(const PlatformInfo& platform)
  ```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| ascendcPlatform | 输入 | 传入硬件平台的信息，PlatformAscendC定义请参见[PlatformAscendC类简介](cannkit-platformascendc-introduction.md)。 |
| platform | 输入 | 传入硬件版本以及AI Core中各个硬件单元提供的内存大小。PlatformInfo构造时通过[PlatformAscendC类简介](cannkit-platformascendc-introduction.md)获取。  PlatformInfo结构定义参数如下，socVersion通过[GetSocVersion](cannkit-getsocversion.md)获取并透传，各类硬件存储空间大小通过[GetCoreMemSize](cannkit-getcorememsize.md)获取并透传。  - platform\_ascendc::SocVersion socVersion;  - uint64\_t l1Size = 0;  - uint64\_t l0CSize = 0;  - uint64\_t ubSize = 0;  - uint64\_t l0ASize = 0;  - uint64\_t l0BSize = 0;  不推荐通过直接填值构造PlatformInfo的方式调用构造函数，例如PlatformInfo(, 1024, 1024, ..); |

在实现Host侧的Tiling函数时，platform\_ascendc::PlatformAscendC用于获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。

和platform\_ascendc::PlatformAscendC不同的是，PlatformInfo则用于获取芯片版本以及AI Core中各个硬件单元提供的内存大小等只针对单个AI Core的信息。

## 注意事项

无

## 使用样例

* 无参构造函数

  ```cpp
  // 单核Tiling
  matmul_tiling::MatmulApiTiling tiling;
  tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = tiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败

  // 多核Tiling
  matmul_tiling::MultiCoreMatmulTiling tiling;
  tiling.SetDim(1);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = tiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败

  // BatchMatmul Tiling
  matmul_tiling::BatchMatmulTiling bmmTiling;
  bmmTiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = bmmTiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败
  ```
* 带参构造函数

  ```cpp
  // 单核Tiling
  auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
  tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = tiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败

  // 多核Tiling
  auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
  tiling.SetDim(1);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = tiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败

  // BatchMatmul Tiling
  auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  matmul_tiling::BatchMatmulTiling bmmTiling(ascendcPlatform);
  bmmTiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  // ...
  optiling::TCubeTiling tilingData;
  int ret = bmmTiling.GetTiling(tilingData); // 若返回值ret为-1，表示Tiling参数生成失败
  ```
