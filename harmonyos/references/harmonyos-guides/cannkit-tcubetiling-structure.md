---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tcubetiling-structure
title: TCubeTiling结构体
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul Tiling > TCubeTiling结构体
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49f36ad281aad9574c00ebb71778a0b24774b5d3461060e6bd8c73404fa027a1
---

TCubeTiling结构体包含Matmul Tiling切分算法的相关参数，被传递给Matmul kernel侧，用于Matmul的切块、搬运和计算过程等。TCubeTiling结构体的参数说明见表1。

**表1** TCubeTiling结构说明

| 参数名称 | 数据类型 | 说明 |
| --- | --- | --- |
| usedCoreNum | int | 使用的AI处理器核数，请根据实际情况设置。取值范围为：[1, AI处理器最大核数]。该参数与shape相关参数的关系为：usedCoreNum = (M / singleCoreM) \* (N / singleCoreN)。 |
| M, N, Ka, Kb | int | A、B、C矩阵原始输入的shape大小，以元素为单位。M, Ka为A矩阵原始输入的Shape, Kb, N为B矩阵原始输入的Shape。  - 大小约束  - 若A矩阵为ND格式，不进行转置时，Ka取值范围为[1, 65535]，M无大小限制；进行转置时，M取值范围为[1, 65535]，Ka无大小限制。  - 若B矩阵为ND格式，不进行转置时，N取值范围为[1, 65535]，Kb无大小限制；进行转置时，Kb取值范围为[1, 65535]，N无大小限制。  - 对齐约束  - 若A矩阵以NZ格式输入，则M需要以16个元素对齐，K需要以C0\_size对齐；若B矩阵以NZ格式输入，则K需要以C0\_size对齐，N需要以16个元素对齐。  - 若A、B矩阵为ND格式，无对齐约束。  **说明：** NZ格式的输入，half/bfloat16\_t数据类型的C0\_size为16，float数据类型的C0\_size为8，int8\_t数据类型的C0\_size为32，int4\_t数据类型的C0\_size为64。 |
| singleCoreM, singleCoreN, singleCoreK | int | A、B、C矩阵单核内shape大小，以元素为单位。  singleCoreK = K，多核处理时不对K进行切分；singleCoreM <= M；singleCoreN <= N。  若A矩阵以NZ格式输入，则singleCoreM需要以16个元素对齐，singleCoreK需要以C0\_size \* fractal\_num对齐；若B矩阵以NZ格式输入，则singleCoreK需要以C0\_size \* fractal\_num对齐，singleCoreN需要以16个元素对齐。  NZ格式的输入，half/bfloat16\_t数据类型的C0\_size为16，float数据类型的C0\_size为8，int8\_t数据类型的C0\_size为32，int4\_t数据类型的C0\_size为64。 |
| baseM, baseN, baseK | int | A、B、C矩阵参与一次矩阵乘指令的shape大小，以元素为单位。  - baseM \* baseN \* sizeof(l0c\_dtype) <= L0C\_size，其中l0c\_dtype为int32\_t或者float数据类型  - baseM \* baseK \* sizeof(Input\_dtype) <= L0A\_size  - baseK \* baseN \* sizeof(Input\_dtype) <= L0B\_size  A、B、C矩阵参与一次矩阵乘的shape大小需要按分形对齐，其含义请参考Mmad中的数据格式说明。 |
| depthA1, depthB1 | int | A、B矩阵片全载A2/B2的份数，depthA1为baseM \* baseK的整数倍，depthB1为baseN \* baseK的整数倍。取值大于0。 |
| stepM， stepN，stepKa，stepKb | int | stepM为左矩阵在A1中缓存的bufferM方向上baseM的倍数。  stepN为右矩阵在B1中缓存的bufferN方向上baseN的倍数。  stepKa为左矩阵在A1中缓存的bufferKa方向上baseK的倍数。  stepKb为右矩阵在B1中缓存的bufferKb方向上baseK的倍数。  取值大于0。 |
| isBias | int | 是否使能Bias，0代表不使能Bias，1代表使能Bias。 |
| transLength | int | max(A1Length, B1Length, C1Length, BiasLength)。其中，A1Length, B1Length, C1Length, BiasLength分别表示A/B/C/Bias矩阵在计算过程中需要临时占用的UB空间大小。 |
| iterateOrder | int | 一次Iterate计算出[baseM, baseN]大小的C矩阵分片，Iterate完成后，Matmul会自动偏移下一次Iterate输出的C矩阵位置，iterateOrder表示自动偏移的顺序。参数取值如下。  - 0：先往M轴方向偏移再往N轴方向偏移  - 1：先往N轴方向偏移再往M轴方向偏移 |
| dbL0A, dbL0B,  dbL0C | int | MTE1是否开启double buffer。  dbL0A：左矩阵MTE1是否开启double buffer。dbL0B：右矩阵MTE1是否开启double buffer；dbL0C：Mmad是否开启double buffer。参数取值如下。  - 1：不开启double buffer  - 2：开启double buffer |
| shareMode | int | 该参数预留，开发者无需关注。 |
| shareL1Size | int | 该参数预留，开发者无需关注。 |
| shareL0CSize | int | 该参数预留，开发者无需关注。 |
| shareUbSize | int | 该参数预留，开发者无需关注。 |
| batchM | int | 该参数预留，开发者无需关注。 |
| batchN | int | 该参数预留，开发者无需关注。 |
| singleBatchM | int | 该参数预留，开发者无需关注。 |
| singleBatchN | int | 该参数预留，开发者无需关注。 |

开发者通过调用GetTiling接口获取TCubeTiling结构体，具体流程请参考[使用说明](cannkit-matmul-tiling-usage-description.md)。若开发者需要修改调整Tiling，请参考如下TCubeTiling参数约束和性能调优推荐取值，进行参数的设置。

* TCubeTiling参数约束

  TCubeTiling参数需要同时满足表1中的所有约束条件。若Matmul对象的MatmulConfig模板为MDL模板，除表1外，还同时需要满足表 MDL模板补充约束条件。

  **表2** TCubeTiling约束条件

  | 约束条件 | 说明 |
  | --- | --- |
  | usedCoreNum <= aiCoreCnt | 使用核数小于等于当前AI处理器的最大核数。 |
  | baseM \* baseK \* sizeof(A\_type) \* dbL0A< l0a\_size | A矩阵base块不超过l0a buffer大小。 |
  | baseN \* baseK \* sizeof(B\_type) \* dbL0B < l0b\_size | B矩阵base块不超过l0b buffer大小。 |
  | baseM \* baseN \* sizeof(int32\_t) \* dbL0C < l0c\_size | C矩阵base块不超过l0c buffer大小。 |
  | baseN \* sizeof(Bias\_type) < biasT\_size | Bias的base块不超过BiasTable buffer大小。 |
  | stepM \* stepKa \* db = depthA1  db这里表示为左矩阵MTE2是否开启double buffer，即L1是否开启double buffer，取值1（不开启double buffer）或2（开启double buffer） | depthA1的取值与stepM \* stepKa \* db相同。 |
  | stepN \* stepKb \* db = depthB1  db这里表示为右矩阵MTE2是否开启double buffer，即L1是否开启double buffer，取值1（不开启double buffer）或2（开启double buffer） | depthB1的取值与stepN \* stepKb \* db相同。 |
  | baseM \* baseK \* depthA1 \* sizeof(A\_type) + baseN \* baseK \* depthB1 \* sizeof(B\_type) <= L1\_size | A矩阵和B矩阵在L1缓存块满足L1 buffer大小限制。 |
  | baseM \* baseK, baseK \* baseN和baseM \* baseN按照NZ格式的分形对齐 | A矩阵、B矩阵、C矩阵的base块需要满足对齐约束：  baseM和baseN需要以16个元素对齐，baseK需要以C0\_size对齐。  **说明：** half/bfloat16\_t数据类型的C0\_size为16，float数据类型的C0\_size为8，int8\_t数据类型的C0\_size为32，int4\_t数据类型的C0\_size为64。 |

  **表3** MDL模板补充约束条件

  | 约束条件 | 说明 |
  | --- | --- |
  | Ka不全载时，即Ka / baseK > stepKa，stepM = 1 | K方向非全载时，M方向只能逐块搬运。 |
  | Kb不全载时，即Kb / baseK > stepKb，stepN = 1 | K方向非全载时，N方向只能逐块搬运。 |
  | kaStepIter\_ % kbStepIter\_ = 0或者kbStepIter\_ % kaStepIter\_ = 0  kaStepIter\_ = CeilDiv(tiling\_->singleCoreK\_, tiling\_->baseK \* tiling\_->stepKa)  kbStepIter\_ = CeilDiv(tiling\_->singleCoreK\_, tiling\_->baseK \* tiling\_->stepKb) | MDL模板K方向循环搬运要求Ka和Kb方向迭代次数为倍数关系。  kaStepIter\_ ：Ka方向循环搬运迭代次数。  kbStepIter\_ ：Kb方向循环搬运迭代次数。 |
* 性能调优推荐取值

  根据Tiling调优经验，部分TCubeTiling参数值或取值方式推荐如下。

  + base块推荐(baseM, baseN, baseK)：(128, 256, 64)
  + dbL0A / dbL0B = 2
  + depthA1 / (stepM \* stepKa) = 2
  + depthB1 / (stepN \* stepKb) = 2
  + 优先设置参数stepKa/stepKb，使得K方向全载，再考虑M方向或N方向全载。
