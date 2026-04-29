---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-tiling-usage-description
title: 使用说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul Tiling > 使用说明
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2db0f5f94111c98a631825e120e5733992211c7df13c7817d2dd6ce9ebe61316
---

AscendC提供一组Matmul Tiling API，方便开发者获取Matmul kernel计算时所需的Tiling参数。开发者只需要传入A/B/C矩阵等信息，调用API接口，即可获取到Init中TCubeTiling结构体中的相关参数。

Matmul Tiling API分为Matmul单核Tiling接口、多核Tiling接口和BatchMatmul Tiling接口。获取Tiling参数的流程如下。

1. 创建一个单核Tiling对象，或多核Tiling对象，或BatchMatmul Tiling对象。
2. 设置A、B、C、Bias的参数类型信息，M、N、Ka、Kb形状信息等。
3. 调用GetTiling接口，获取Tiling信息。

使用Matmul单核Tiling接口、多核Tiling接口和BatchMatmul Tiling接口获取Tiling参数的样例如下。

* Matmul单核Tiling

  ```
  1. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  2. matmul_tiling::MatmulApiTiling tiling(ascendcPlatform);
  3. tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  4. tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  5. tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  6. tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  7. tiling.SetShape(1024, 1024, 1024);
  8. tiling.SetOrgShape(1024, 1024, 1024); // 或Ka,Kb不等长，如tiling.SetOrgShape(1024, 1024, 1024, 1280)
  9. tiling.SetBias(true);
  10. tiling.SetBufferSpace(-1, -1, -1);  // 设定允许使用的空间，缺省使用该AI处理器所有空间
  11. optiling::TCubeTiling tilingData;
  12. int ret = tiling.GetTiling(tilingData);    // if ret = -1, get tiling failed
  ```
* 多核Tiling

  ```
  1. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  2. matmul_tiling::MultiCoreMatmulTiling tiling(ascendcPlatform);
  3. tiling.SetDim(1);
  4. tiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  5. tiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  6. tiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  7. tiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  8. tiling.SetShape(1024, 1024, 1024);
  9. tiling.SetSingleShape(1024, 1024, 1024);
  10. tiling.SetOrgShape(1024, 1024, 1024);
  11. tiling.SetBias(true);
  12. tiling.SetBufferSpace(-1, -1, -1);  // 设定允许使用的空间，缺省使用该AI处理器所有空间
  13. optiling::TCubeTiling tilingData;
  14. int ret = tiling.GetTiling(tilingData);    // if ret = -1, get tiling failed
  ```
* BatchMatmul Tiling

  ```
  1. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
  2. matmul_tiling::BatchMatmulTiling bmmTiling(ascendcPlatform);
  3. bmmTiling.SetDim(1);
  4. bmmTiling.SetAType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  5. bmmTiling.SetBType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT16);
  6. bmmTiling.SetCType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  7. bmmTiling.SetBiasType(matmul_tiling::TPosition::GM, matmul_tiling::CubeFormat::ND, matmul_tiling::DataType::DT_FLOAT);
  8. bmmTiling.SetBias(true);
  9. bmmTiling.SetShape(1024, 1024, 1024);
  10. bmmTiling.SetSingleShape(1024, 1024, 1024);
  11. bmmTiling.SetOrgShape(1024, 1024, 1024);
  12. bmmTiling.SetBufferSpace(-1, -1, -1);  // 设定允许使用的空间，缺省使用该AI处理器所有空间
  13. optiling::TCubeTiling tilingData;
  14. int ret = bmmTiling.GetTiling(tilingData);    // if ret = -1, get tiling failed
  ```

接口列表如下。

**表1** MatmulApiTiling/MultiCoreMatmulTiling/BatchMatmulTiling共有接口列表

| 接口 | 功能 |
| --- | --- |
| SetAType | 设置A矩阵的位置，数据格式，数据类型，是否转置等信息。 |
| SetBType | 设置B矩阵的位置，数据格式，数据类型，是否转置等信息。 |
| SetCType | 设置C矩阵的位置，数据格式，数据类型等信息。 |
| SetBiasType | 设置Bias的位置，数据格式，数据类型等信息。 |
| SetShape | 设置Matmul单次计算的形状singleM、singleN、singleK，单位为元素个数。 |
| SetOrgShape | 设置Matmul计算时的原始完整的形状M、N、Ka、Kb，单位为元素个数。 |
| SetBias | 设置Bias是否参与运算。 |
| SetFixSplit | 设置固定的baseM、baseN、baseK，单位为元素个数。 |
| SetBufferSpace | 设置Matmul计算时可用的L1/L0C/UB空间大小，单位为字节。 |
| SetTraverse | 设置遍历方式，M轴优先还是N轴优先。 |
| SetMadType | 设置是否使能HF32模式。**当前版本暂不支持。** |
| SetSplitRange | 设置baseM/baseN/baseK的最大值和最小值。 |
| SetDoubleBuffer | 设置A/B/C/Bias是否使能double buffer功能，以及是否需要做ND2NZ或者NZ2ND的转换。**该接口为预留接口，当前版本暂不支持。** |
| GetBaseM | 获取baseM值。 |
| GetBaseN | 获取baseN值。 |
| GetBaseK | 获取baseK值。 |
| GetTiling | 获取Tiling参数。 |

**表2** MultiCoreMatmulTiling其他接口

| 接口 | 功能 |
| --- | --- |
| SetDim | 设置多核Matmul时，可以参与运算的核数。 |
| SetSingleRange | 设置singleCoreM/singleCoreN/singleCoreK的最大值与最小值。 |
| SetSingleShape | 设置Matmul单核计算的形状singleCoreM、singleCoreN、singleCoreK，单位为元素个数。 |
| GetSingleShape | 获取计算后的singleCoreM/singleCoreN/singleCoreK。 |
| SetAlignSplit | 设置多核切分时singleCoreM/singleCoreN/singleCoreK的对齐值 |
| GetCoreNum | 获得多核切分后，使用的blockDim。 |
| SetSplitK | 多核场景，使能切K轴。 |

**表3** BatchMatmulTiling其他接口

| 接口 | 功能 |
| --- | --- |
| GetCoreNum | 获得多核切分后，使用的blockDim。 |
