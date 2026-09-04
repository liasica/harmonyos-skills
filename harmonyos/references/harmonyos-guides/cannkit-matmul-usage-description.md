---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-usage-description
title: 使用说明
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > 使用说明
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:29+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:24b89f037441ac0420bc41d0607cc3db85de44a29214c09f34d5e532a6f3af70
---

AscendC提供一组Matmul高阶API，方便开发者快速实现Matmul矩阵乘法的运算操作。

Matmul的计算公式为：C = A \* B，其示意图如下。

* A、B为源操作数，A为左矩阵，形状为[M, K]；B为右矩阵，形状为[K, N]。
* C为目的操作数，存放矩阵乘结果的矩阵，形状为[M, N]。

**图1** Matmul矩阵乘示意图

![](https://media:401788444116681953)

![](https://media:401788444116709954) 

下文中提及的M轴方向，即为A矩阵纵向；K轴方向，即为A矩阵横向或B矩阵纵向；N轴方向，即为B矩阵横向。

实现Matmul矩阵乘运算的具体步骤如下。

1. 创建Matmul对象。示例如下。

   * CUBE\_ONLY（只有矩阵计算）场景下，需要设置ASCENDC\_CUBE\_ONLY代码宏。
   * 默认为MIX模式（包含矩阵计算和矢量计算），该场景下，不能设置ASCENDC\_CUBE\_ONLY代码宏。

   ```cpp
   // 纯cube模式（只有矩阵计算）场景下，需要设置该代码宏，并且必须在#include "lib/matmul_intf.h"之前设置
   // #define ASCENDC_CUBE_ONLY
   #include "lib/matmul_intf.h"
    
   typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
   typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
   typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
   typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
   matmul::Matmul<aType, bType, cType, biasType> mm;
   ```

   创建对象时需要传入A、B、C、Bias的参数类型信息， 类型信息通过MatmulType来定义，包括：内存逻辑位置、数据格式、数据类型。

   ```cpp
   template <AscendC::TPosition POSITION, CubeFormat FORMAT, typename TYPE, bool ISTRANS = false, LayoutMode LAYOUT = LayoutMode::NONE, bool IBSHARE = false> struct MatmulType {
       constexpr static AscendC::TPosition pos = POSITION;
       constexpr static CubeFormat format = FORMAT;
       using T = TYPE;
       constexpr static bool isTrans = ISTRANS;
       constexpr static LayoutMode layout = LAYOUT;
       constexpr static bool ibShare = IBSHARE;
   };
   ```

   **表1** MatmulType参数说明

   | 参数 | 说明 |
   | --- | --- |
   | POSITION | 内存逻辑位置  Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵可设置为TPosition::GM，TPosition::TSCM  - B矩阵可设置为TPosition::GM，TPosition::TSCM  - C矩阵可设置为TPosition::GM |
   | CubeFormat | Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵在GM时，支持CubeFormat::ND。  - A矩阵在TSCM时，支持CubeFormat::NZ/CubeFormat::VECTOR。  - B矩阵在GM时，支持CubeFormat::ND/CubeFormat::NZ。  - B矩阵在TSCM时支持CubeFormat::NZ。  - C矩阵在GM时，支持CubeFormat::ND。 |
   | TYPE | Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵可设置为half。  - B矩阵可设置为half。  - C矩阵可设置为half。 |
   | ISTRANS | 是否开启使能矩阵转置的功能。当前不支持转置，只支持设为false。  false为不开启使能矩阵转置的功能，通过[SetTensorA](cannkit-settensora.md)和[SetTensorB](cannkit-settensorb.md)不能设置A、B矩阵是否转置。Matmul会认为A矩阵形状为[M, K]，B矩阵形状为[K, N]。  默认为false不使能转置。 |
   | LAYOUT | 表征数据的排布。  NONE：默认值，表示不使用BatchMatmul，其他选项表示使用BatchMatmul。 |
2. 初始化操作。

   ```cpp
   REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);
   ```
3. 设置左矩阵A、右矩阵B、Bias。

   ```cpp
   mm.SetTensorA(gm_a); // 设置左矩阵A
   mm.SetTensorB(gm_b); // 设置右矩阵B
   mm.SetBias(gm_bias); // 设置Bias
    
   mm.SetLocalWorkspace(ubBuf);
   ```
4. 完成矩阵乘操作。

   * 调用Iterate完成单次迭代计算，叠加while循环完成单核全量数据的计算。Iterate方式，可以自行控制迭代次数，完成所需数据量的计算，方式比较灵活。

     ```cpp
     while (mm.Iterate()) {
          mm.GetTensorC(gm_c);
      }
     ```
   * 调用IterateAll完成单核上所有数据的计算。IterateAll方式，无需循环迭代，使用比较简单。

     ```cpp
     mm.IterateAll(gm_c);
     ```
5. 结束矩阵乘操作。

   ```cpp
   mm.End();
   ```
