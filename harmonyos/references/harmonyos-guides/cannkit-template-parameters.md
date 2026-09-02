---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-template-parameters
title: Matmul模板参数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > Matmul模板参数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:c2b6ec985bed68c8cc85480fc2a363406da676faabf09cde9c20744003186bfd
---

## 功能说明

创建Matmul对象时需要传入：

* A、B、C、Bias的参数类型信息，类型信息通过MatmulType来定义，包括：内存逻辑位置、数据格式、数据类型、是否转置、数据排布和是否使能L1复用。
* MatmulConfig信息（可选），用于配置Matmul模板信息以及相关的配置参数。不配置默认使能Norm模板。

  针对Kirin9020系列处理器、Kirin9030系列处理器，当前只支持使能默认的MDL模板。
* MatmulCallBack回调函数信息（可选），用于配置左右矩阵从GM拷贝到L1、计算结果从CO1拷贝到GM的自定义函数。
* MatmulPolicy信息（可选），预留参数。

## 实现原理

以输入矩阵A (GM, ND, half)、矩阵B(GM, ND, half)，输出矩阵C (GM, ND, float)，无Bias场景为例，其中(GM, ND, half)表示数据存放在GM上，数据格式为ND，数据类型为half，描述Matmul高阶API典型场景的内部算法框图，如下图所示。

**图1** Matmul算法框图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/OqVKFOvwRkKbRXppYZ-Vag/zh-cn_image_0000002706835352.png)

计算过程分为如下几步：

1. 数据从GM搬到A1：DataCopy每次从矩阵A，搬出一个stepM\*baseM\*stepKa\*baseK的矩阵块a1，循环多次完成矩阵A的搬运；数据从GM搬到B1：DataCopy每次从矩阵B，搬出一个stepKb\*baseK\*stepN\*baseN的矩阵块b1，循环多次完成矩阵B的搬运。
2. 数据从A1搬到A2：LoadData每次从矩阵块a1，搬出一个baseM \* baseK的矩阵块a0；数据从B1搬到B2，并完成转置：LoadData每次从矩阵块b1，搬出一个baseK \* baseN的矩阵块，并将其转置为baseN \* baseK的矩阵块b0。
3. 矩阵乘：每次完成一个矩阵块a0 \* b0的计算，得到baseM \* baseN的矩阵块co1。
4. 数据从矩阵块co1搬到矩阵块co2： DataCopy每次搬运一块baseM \* baseN的矩阵块co1到singleCoreM \* singleCoreN的矩阵块co2中。
5. 重复2-4步骤，完成矩阵块a1 \* b1的计算。
6. 数据从矩阵块co2搬到矩阵块C：DataCopy每次搬运一块singleCoreM \* singleCoreN的矩阵块co2到矩阵块C中。
7. 重复1-6步骤，完成矩阵A \* B = C的计算。

## 函数原型

```cpp
template <class A_TYPE, class B_TYPE, class C_TYPE, class BIAS_TYPE = C_TYPE, const MatmulConfig& MM_CFG = CFG_NORM, class MM_CB = MatmulCallBackFunc<nullptr, nullptr, nullptr>, MATMUL_POLICY_DEFAULT_OF(MatmulPolicy)> 
using Matmul = matmul::MatmulImpl<A_TYPE, B_TYPE, C_TYPE, BIAS_TYPE, MM_CFG, MM_CB, MATMUL_POLICY>;
```

* A\_TYPE、B\_TYPE、C\_TYPE类型信息通过[使用说明](cannkit-matmul-usage-description.md)表1来定义。
* MatmulConfig（可选），参数说明见表2。

  + 该参数可选取提供的模板默认值之一，当前提供的MatmulConfig模板取值范围为[CFG\_NORM、CFG\_MDL、CFG\_IBSHARE\_NORM、MM\_CFG\_BB]，分别对应默认的Norm、MDL、IBShare、BasicBlock模板。各模板的介绍请参考表3。
  + 该参数可以通过MatmulConfig章节中介绍的获取模板的接口，自定义模板参数配置。
  + 另外，MatmulConfig可拆分为表5、表6、表7、表8二级子Config，使用GetMMConfig接口，设置需要的二级子Config和表4，可以更加灵活的获取自定义的模板参数配置MatmulConfig。
* MM\_CB（可选），用于支持不同的搬入搬出需求，实现定制化的搬入搬出功能，如非连续搬入或针对搬出设置不同的数据片段间隔等。MM\_CB中3个函数指针分别对应计算结果从CO1拷贝到GM、左矩阵从GM拷贝到L1、右矩阵从GM拷贝到L1的回调函数指针，各个功能回调函数接口定义及参数释义见表9。
* MATMUL\_POLICY\_DEFAULT\_OF(MatmulPolicy)（可选），当前为预留参数，无须配置。

  ```cpp
  #define MATMUL_POLICY_DEFAULT_OF(DEFAULT)      \
  template <const auto& = MM_CFG, typename ...> class MATMUL_POLICY = DEFAULT
  ```

## 参数说明

**表1** MatmulType参数说明

| 参数 | 说明 |
| --- | --- |
| POSITION | 内存逻辑位置  Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵可设置为TPosition::GM，TPosition::TSCM。  - B矩阵可设置为TPosition::GM，TPosition::TSCM。  - C矩阵可设置为TPosition::GM。 |
| CubeFormat | Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵在GM时，支持CubeFormat::ND。  - A矩阵在TSCM时，支持CubeFormat::NZ/CubeFormat::VECTOR。  - B矩阵在GM时，支持CubeFormat::ND/CubeFormat::NZ。  - B矩阵在TSCM时支持CubeFormat::NZ。  - C矩阵在GM时，支持CubeFormat::ND。 |
| TYPE | Kirin9020系列处理器、Kirin9030系列处理器：  - A矩阵可设置为half。  - B矩阵可设置为half。  - C矩阵可设置为half。 |
| ISTRANS | 是否开启使能矩阵转置的功能。当前不支持转置，只支持设为false。  false为不开启使能矩阵转置的功能，通过[SetTensorA](cannkit-settensora.md)和[SetTensorB](cannkit-settensorb.md)不能设置A、B矩阵是否转置。Matmul会认为A矩阵形状为[M, K]，B矩阵形状为[K, N]。  默认为false不使能转置。 |
| LAYOUT | 表征数据的排布。  NONE：默认值，表示不使用BatchMatmul，其他选项表示使用BatchMatmul。 |

**表2** MatmulConfig参数说明

| 参数 | 说明 | 支持模板：Norm, MDL, SpecialMDL, IBShare, BasicBlock |
| --- | --- | --- |
| doNorm | 使能Norm模板。参数取值如下。  - true：使能Norm模板  - false：不使能Norm模板  不指定模板的情况默认使能Norm模板。 | Norm |
| doMultiDataLoad | 使能MDL模板。参数取值如下。  - true：使能MDL模板  - false：不使能MDL模板 | MDL |
| doSpecialMDL | 使能SpecialMDL模板。参数取值如下。  - true：使能SpecialMDL模板  - false：不使能SpecialMDL模板  本质上也是MDL模板。MDL模板Matmul K方向不全载时（singleCoreK/baseK > stepKb），仅支持stepN设置为1，开启后支持stepN=2。 | SpecialMDL |
| doIBShareNorm | 使能IBShare模板。参数取值如下。  - false：不使能IBShare（默认值）  - true：使能IBShare  IBShare的功能是能够复用L1上相同的A矩阵或B矩阵数据，开启后在数据复用场景能够避免重复搬运数据到L1。 | IBShare |
| intrinsicsLimit | 当左矩阵或右矩阵在单核上内轴（即尾轴）大于等于65535时，是否使能循环执行数据的搬入。例如，左矩阵A[M, K]，单核上的内轴数据singleCoreK大于65535，配置该参数为true后，API内部通过循环执行数据的搬入。参数取值如下。  - false：当左矩阵或右矩阵在单核上内轴大于等于65535时，不使能循环执行数据的搬入（默认值）  - true：当左矩阵或右矩阵在单核上内轴大于等于65535时，使能数循环执行数据的搬入 | 所有模板 |
| batchLoop | 是否多Batch输入多Batch输出。参数取值如下。  - false：不使能多Batch（默认值）  - true：使能多Batch  仅对BatchMatmul有效。 | 所有模板 |
| isVecND2NZ | 使能通过vector进行ND2NZ。参数取值如下。  - false：不使能通过vector进行ND2NZ（默认值）  - true：使能通过vector进行ND2NZ  使能时需要设置SetLocalWorkspace。 | 所有模板 |
| enableInit | 是否启用Init函数，不使能Init函数能够提升常量传播效果，优化性能。默认使能。 | 所有模板 |
| bmmMode | Layout类型为NORMAL时，设置BatchMatmul输入A/B矩阵的多batch数据总和与L1 Buffer的大小关系。参数取值如下。  - BatchMode::BATCH\_LESS\_THAN\_L1：多batch数据总和<L1 Buffer Size。  - BatchMode::BATCH\_LARGE\_THAN\_L1：多batch数据总和>L1 Buffer Size。  - BatchMode::SINGLE\_LARGE\_THAN\_L1：单batch数据总和>L1 Buffer Size。 | Norm, IBShare |
| enUnitFlag | 使能unitflag功能，使计算与搬运流水并行，提高性能。Norm, IBShare下默认使能，MDL下默认不使能。参数取值如下。  - false：不使能unitflag功能  - true：使能unitflag功能 | MDL, Norm, IBShare |
| isPerTensor | A矩阵half类型输入且B矩阵int8类型输入场景，使能B矩阵量化时是否为per tensor，true为per tensor，false为per channel。 | MDL, SpecialMDL |
| hasAntiQuantOffset | A矩阵half类型输入且B矩阵int8类型输入场景，使能B矩阵量化时是否使用offset系数。 | MDL, SpecialMDL |
| doMTE2Preload | 在MTE2流水间隙较大，且M/N数值较大时可通过该参数开启对应M/N方向的预加载功能，开启后能减小MTE2间隙，提升性能。预加载功能仅在MDL模板有效。参数取值如下。  0：不开启（默认值）  1：开启M方向preload  2：开启N方向preload  注意，开启M/N预加载功能时需保证K全载，且M/N开启Double Buffer。 | MDL, SpecialMDL |
| isMsgReuse | SetSelfDefineData函数设置的回调函数中的dataPtr是否直接传递计算数据。参数取值如下。  - true：直接传递计算数据，仅限单个值  - false：传递GM上存储的数据地址信息 | Norm, MDL |
| enableUBReuse | 是否使能UB复用。参数取值如下。  - true：使能UB复用  - false：不使能UB复用 | MDL |
| enableL1CacheUB | 是否使能L1缓存UB计算块。参数取值如下。  - true：使能L1缓存UB计算块  - false：不使能L1缓存UB计算块  若要使能L1缓存UB计算块，必须在tiling实现中调用SetMatmulConfigParams接口配置相关信息。 | MDL |
| isDoubleCache | 开启IBShare模板后，在L1上是否同时缓存两块数据。注意，需要控制base块大小，防止两块缓存超过L1大小限制。参数取值如下。  - false：L1上同时缓存一块数据（默认值）  - true：使能L1上同时缓存两块数据 | IBShare |
| IterateOrder | Matmul做矩阵运算的循环迭代顺序，与[TCubeTiling结构体](cannkit-tcubetiling-structure.md)表1中的iterateOrder参数含义相同。当ScheduleType参数取值为ScheduleType::OUTER\_PRODUCT或1时，本参数生效。参数取值如下。  - ORDER\_M = 0, // 先往M轴方向偏移再往N轴方向偏移  - ORDER\_N, // 先往N轴方向偏移再往M轴方向偏移  - UNDEF, // 当前无效  **说明：** MDL模板使用时，若IterateOrder取值ORDER\_M，[TCubeTiling结构体](cannkit-tcubetiling-structure.md)表1中的stepN需要大于1，IterateOrder取值ORDER\_N时，TCubeTiling结构中的stepM需要大于1。 | Norm、MDL |
| ScheduleType | 配置Matmul数据搬运模式。参数取值如下。  - ScheduleType::INNER\_PRODUCT或0：默认模式，在K方向上做MTE1的循环搬运。  - ScheduleType::OUTER\_PRODUCT或1：在M或N方向上做MTE1的循环搬运。使能后，需要与IterateOrder参数配合使用。该配置当前只在Norm模板的Batch Matmul场景、MDL模板生效。  - 若IterateOrder取值ORDER\_M，则N方向循环搬运（在singleCoreN大于baseN场景可能有性能提升），即B矩阵的MTE1搬运并行。  - 若IterateOrder取值ORDER\_N，则M方向循环搬运（在singleCoreM大于baseM场景可能有性能提升），即A矩阵的MTE1搬运并行。  - 不能同时使能M方向和N方向循环搬运。  **说明：**  - singleCoreK>baseK的场景，不能使能ScheduleType::OUTER\_PRODUCT取值，需使用默认模式。  - MDL模板仅在调用IterateAll计算的场景支持配置ScheduleType::OUTER\_PRODUCT或1。 | Norm、MDL |
| isBiasBatch | 批量多Batch的Matmul场景，即BatchMatmul场景，Bias的大小是否带有Batch轴。参数取值如下。  - true：Bias带有Batch轴，Bias大小为Batch \* N（默认值）。  - false：Bias不带Batch轴，Bias大小为N，多Batch计算Matmul时，会复用Bias。 | Norm |
| doBasicBlock | 是否使能BasicBlock模板。模板参数取值如下。  - true：使能BasicBlock模板  - false：不使能BasicBlock模板  调用GetBasicConfig接口获取BasicBlock模板时，该参数被置为true。  **说明：**  - BasicBlock模板暂不支持输入为int8，int4数据类型的A、B矩阵，支持half/float/bfloat16\_t数据类型的A、B矩阵。  - BasicBlock模板暂不支持A矩阵的格式为标量数据Scalar或向量数据Vector。  - BasicBlock模板暂不支持ScheduleType::OUTER\_PRODUCT的数据搬运模式。 | BasicBlock |
| basicM | 相当于baseM。 | BasicBlock |
| basicN | 相当于baseN。 | BasicBlock |
| basicK | 相当于baseK。 | BasicBlock |
| doSpecialBasicBlock | 使能SpecialBasicBlock模板。参数取值如下。  - true：使能SpecialBasicBlock模板。  - false：不使能SpecialBasicBlock模板。  本质上也是BasicBlock模板，但消除了头开销scalar计算。 | 预留参数 |
| singleCoreM | 单核内M轴shape大小，以元素为单位。 | 预留参数 |
| singleCoreN | 单核内N轴shape大小，以元素为单位。 | 预留参数 |
| singleCoreK | 单核内K轴shape大小，以元素为单位。 | 预留参数 |
| stepM | 左矩阵在A1中缓存的bufferM方向上baseM的倍数。 | 预留参数 |
| stepN | 右矩阵在B1中缓存的bufferN方向上baseN的倍数。 | 预留参数 |
| baseMN | baseM\*baseN的大小。 | 预留参数 |
| singleCoreMN | singleCoreM\*singleCoreN的大小。 | 预留参数 |

**表3** 模板特性

| 模板 | 实现 | 优点 | 推荐使用场景 |
| --- | --- | --- | --- |
| Norm | 支持L1缓存多个基本块，MTE2分多次从GM搬运基本块到L1，每次搬运一份基本块，已搬的基本块不清空。（举例说明：depthA1=6，代表搬入6份A矩阵基本块到L1，1次搬运一份基本块，MTE2进行6次搬运） | 可以提前启动MTE1流水（因为搬1份基本块就可以做MTE1后面的运算） | 默认使能Norm模板 |
| MDL，SpecialMDL | 支持L1缓存多个基本块，MTE2从GM到L1的搬运为一次性"大包"搬运。（举例说明：depthA1=6，代表一次性搬入6份A矩阵基本块到L1，MTE2进行1次搬运） | 对于一般的大shape场景，可以减少MTE2的循环搬运，提升性能 | 大shape场景 |
| IBShare | MIX场景下，多个AIV的A矩阵或B矩阵GM地址相同的时候，通过共享L1 Buffer，减少MTE2搬运。 | 减少MTE2搬运，提升性能 | MIX场景多个AIV的A矩阵或B矩阵GM地址相同 |
| BasicBlock | 在无尾块的场景，base块大小确定的情况下，通过GetBasicConfig接口配置输入的基本块大小，固定MTE1每次搬运的矩阵大小及Mmad每次计算的矩阵大小，减少参数计算量。 | 减少MTE1矩阵搬运和Mmad矩阵计算过程中的参数计算开销 | 无尾块，base块(baseM, baseN)大小确定 |

**表4** MatmulConfigMode参数说明

| 参数 | 说明 |
| --- | --- |
| CONFIG\_NORM | 表示设置MatmulConfig默认值为Norm模板。 |
| CONFIG\_MDL | 表示设置MatmulConfig默认值为MDL模板。 |
| CONFIG\_SPECIALMDL | 表示设置MatmulConfig默认值为SpecialMDL模板。 |
| CONFIG\_IBSHARE | 表示设置MatmulConfig默认值为IBShare模板。 |

**表5** MatmulShapeParams参数说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| singleCoreM | uint32\_t | 单核内M轴shape大小，以元素为单位。 |
| singleCoreN | uint32\_t | 单核内N轴shape大小，以元素为单位。 |
| singleCoreK | uint32\_t | 单核内K轴shape大小，以元素为单位。 |
| basicM | uint32\_t | 相当于baseM。 |
| basicN | uint32\_t | 相当于baseN。 |
| basicK | uint32\_t | 相当于baseK。 |

**表6** MatmulQuantParams参数说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| isPerTensor | bool | A矩阵half类型输入且B矩阵int8类型输入场景，使能B矩阵量化时是否为per tensor，true为per tensor，false为per channel。 |
| hasAntiQuantOffset | bool | A矩阵half类型输入且B矩阵int8类型输入场景，使能B矩阵量化时是否使用offset系数，true为使用offset系数，false为不使用offset系数。 |

**表7** MatmulBatchParams参数说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| batchLoop | bool | 是否多Batch输入多Batch输出。参数取值如下。  - false：不使能多Batch（默认值）  - true：使能多Batch  仅对BatchMatmul有效。 |
| bmmMode | BatchMode | Layout类型为NORMAL时，设置BatchMatmul输入A/B矩阵的多batch数据总和与L1 Buffer的大小关系。参数取值如下。  - BatchMode::BATCH\_LESS\_THAN\_L1：多batch数据总和<L1 Buffer Size。  - BatchMode::BATCH\_LARGE\_THAN\_L1：多batch数据总和>L1 Buffer Size。  - BatchMode::SINGLE\_LARGE\_THAN\_L1：单batch数据总和>L1 Buffer Size。 |
| isBiasBatch | bool | 批量多Batch的Matmul场景，即BatchMatmul场景，Bias的大小是否带有Batch轴。参数取值如下。  - true：Bias带有Batch轴，Bias大小为Batch \* N（默认值）  - false：Bias不带Batch轴，Bias大小为N，多Batch计算Matmul时，会复用Bias。 |

**表8** MatmulFuncParams参数说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| intrinsicsLimit | bool | 进行芯片指令搬运地址偏移量校验，影响性能。参数取值如下。  - false：不进行芯片指令搬运地址偏移量校验（默认值）  - true：进行芯片指令搬运地址偏移量校验 |
| enVecND2NZ | bool | 使能通过vector进行ND2NZ。参数取值如下。  - false：不使能通过vector进行ND2NZ（默认值）  - true：使能通过vector进行ND2NZ  使能时需要设置SetLocalWorkspace。 |
| doMTE2Preload | uint32\_t | 在MTE2流水间隙较大，且M/N数值较大时可通过该参数开启对应M/N方向的预加载功能，开启后能减小MTE2间隙，提升性能。预加载功能仅在MDL模板有效。参数取值如下。  0：不开启（默认值）  1：开启M方向preload  2：开启N方向preload  注意，开启M/N预加载功能时需保证K全载，且M/N开启Double Buffer。 |
| enableReuse | bool | SetSelfDefineData函数设置的回调函数中的dataPtr是否直接传递计算数据。参数取值如下。  - true：直接传递计算数据，仅限单个值  - false：传递GM上存储的数据地址信息 |
| enableUBReuse | bool | 是否使能UB复用。参数取值如下。  - true：使能UB复用  - false：不使能UB复用 |
| enableL1CacheUB | bool | 是否使能L1缓存UB计算块。参数取值如下。  - true：使能L1缓存UB计算块  - false：不使能L1缓存UB计算块  若要使能L1缓存UB计算块，必须在tiling实现中调用SetMatmulConfigParams接口配置相关信息。 |
| iterateOrder | IterateOrder | Matmul做矩阵运算的循环迭代顺序，与[TCubeTiling结构体](cannkit-tcubetiling-structure.md)表1中的iterateOrder参数含义相同。当ScheduleType参数取值为ScheduleType::OUTER\_PRODUCT或1时，本参数生效。参数取值如下。  - ORDER\_M = 0, // 先往M轴方向偏移再往N轴方向偏移  - ORDER\_N, // 先往N轴方向偏移再往M轴方向偏移  - UNDEF, // 当前无效  **说明：** MDL模板使用时，若IterateOrder取值ORDER\_M，[TCubeTiling结构体](cannkit-tcubetiling-structure.md)表1中的stepN需要大于1，IterateOrder取值ORDER\_N时，TCubeTiling结构中的stepM需要大于1。 |
| scheduleType | ScheduleType | 配置Matmul数据搬运模式。参数取值如下。  - ScheduleType::INNER\_PRODUCT或0：默认模式，在K方向上做MTE1的循环搬运。  - ScheduleType::OUTER\_PRODUCT或1：在M或N方向上做MTE1的循环搬运。使能后，需要与IterateOrder参数配合使用。该配置当前只在Norm模板的Batch Matmul场景、MDL模板生效。  - 若IterateOrder取值ORDER\_M，则N方向循环搬运（在singleCoreN大于baseN场景可能有性能提升），即B矩阵的MTE1搬运并行。  - 若IterateOrder取值ORDER\_N，则M方向循环搬运（在singleCoreM大于baseM场景可能有性能提升），即A矩阵的MTE1搬运并行。  - 不能同时使能M方向和N方向循环搬运。  **说明：**  - singleCoreK>baseK的场景，不能使能ScheduleType::OUTER\_PRODUCT取值，需使用默认模式。  - MDL模板仅在调用IterateAll计算的场景支持配置ScheduleType::OUTER\_PRODUCT或1。 |
| enableDoubleCache | bool | 开启IBShare模板后，在L1上是否同时缓存两块数据。注意，需要控制base块大小，防止两块缓存超过L1大小限制。参数取值如下。  - false：L1上同时缓存一块数据（默认值）。  - true：使能L1上同时缓存两块数据。 |

**表9** MatmulCallBackFunc回调函数接口及参数说明

| 回调函数功能 | 回调函数接口 | 参数说明 |
| --- | --- | --- |
| 可自定义设置不同的搬出数据片段数目等参数，实现将Matmul计算结果从CO1搬出到GM的功能 | void DataCopyOut(const **gm** void \*gm, const LocalTensor<int8\_t> &co1Local, const void \*dataCopyOutParams, const uint64\_t tilingPtr, const uint64\_t dataPtr) | gm：输出的GM地址。  co1Local：CO1上的计算结果。  dataCopyOutParams：  Matmul定义的DataCopyOutParams结构体指针，供开发者参考使用。  - uint16\_t cBurstNum：传输数据片段数目  - uint16\_t burstLen：连续传输数据片段长度  - int16\_t srcStride：源tensor相邻连续数据片段间隔  - uint32\_t dstStride：目的tensor相邻连续数据片段间隔  - uint16\_t oriNSize：NZ转ND时，源tensorN方向大小  - bool enUnitFlag：是否使能UnitFlag  - uint64\_t quantScalar：量化场景下量化Scalar的值  - uint64\_t cbufWorkspaceAddr：量化场景下量化Tensor地址  tilingPtr：开发者使用SetUserDefInfo设置的tiling参数地址。  dataPtr：开发者使用SetSelfDefineData设置的计算数据地址。 |
| 可自定义左矩阵搬入首地址、搬运块位置、搬运块大小，实现左矩阵从GM搬入L1的功能 | void CopyA1(const LocalTensor<int8\_t> &aMatrix, const **gm** void \*gm, int row, int col, int useM, int useK, const uint64\_t tilingPtr, const uint64\_t dataPtr) | aMatrix：目标L1Buffer地址。  gm：左矩阵GM首地址。  row、col：搬运块左上角坐标在左矩阵中的位置。  useM、useK：搬运块M、K方向大小。  tilingPtr：开发者使用SetUserDefInfo设置的tiling参数地址。  dataPtr：开发者使用SetSelfDefineData设置的计算数据地址。 |
| 可自定义右矩阵搬入首地址、搬运块位置、搬运块大小，实现右矩阵从GM搬入L1的功能 | void CopyB1(const LocalTensor<int8\_t> &bMatrix, const **gm** void \*gm, int row, int col, int useK, int useN, const uint64\_t tilingPtr, const uint64\_t dataPtr) | bMatrix：目标L1Buffer地址。  gm：右矩阵GM首地址。  row、col：搬运块左上角坐标在右矩阵中的位置。  useK、useN：搬运块K、N方向大小。  tilingPtr：开发者使用SetUserDefInfo设置的tiling参数地址。  dataPtr：开发者使用SetSelfDefineData设置的计算数据地址。 |

**表10** MatmulApiStaticTiling常量化Tiling参数说明

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| M, N, Ka, Kb,  singleCoreM, singleCoreN, singleCoreK,  baseM, baseN, baseK,  depthA1, depthB1,  stepM,stepN,stepKa,stepKb,  isBias,  transLength,  iterateOrder,  dbL0A, dbL0B,  dbL0C,  shareMode,  shareL1Size,  shareL0CSize,  shareUbSize,  batchM,  batchN,  singleBatchM,  singleBatchN | int | 与TCubeTiling结构体结构体中各同名参数含义一致。本结构体中的参数是常量化后的常数值。 |
| cfg | [参数说明](cannkit-template-parameters.md#参数说明)下的表2 | Matmul模板的参数配置。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 调用示例

```cpp
// 开发者自定义回调函数
void DataCopyOut(const __gm__ void *gm, const LocalTensor<int8_t> &co1Local, const void *dataCopyOutParams, const uint64_t tilingPtr, const uint64_t dataPtr);
void CopyA1(const AscendC::LocalTensor<int8_t> &aMatrix, const __gm__ void *gm, int row, int col, int useM, int useK, const uint64_t tilingPtr, const uint64_t dataPtr);
void CopyB1(const AscendC::LocalTensor<int8_t> &bMatrix, const __gm__ void *gm, int row, int col, int useK, int useN, const uint64_t tilingPtr, const uint64_t dataPtr);
 
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
matmul::Matmul<aType, bType, cType, biasType, CFG_MDL> mm1;
matmul::MatmulConfig mmConfig{false, true, false, 128, 128, 64};
mmConfig.enUnitFlag = false;
matmul::Matmul<aType, bType, cType, biasType, mmConfig> mm2;
matmul::Matmul<aType, bType, cType, biasType, CFG_NORM, matmul::MatmulCallBackFunc<DataCopyOut, CopyA1, CopyB1>> mm3;
```
