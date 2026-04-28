---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascend-c-apis
title: AscendC API列表
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > AscendC API列表
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a75bcd9bdee9c9768928e4bec9a1533e6a19fbe13ac4320a1cffdc707908b4b
---

AscendC提供一组类库API，开发者使用标准C++语法和类库API进行编程。AscendC编程类库API示意图如下所示，分为：

* Kernel API：用于实现算子核函数的API接口。包括：

  + **基本数据结构：** Kernel API中使用到的基本数据结构，比如GlobalTensor和LocalTensor。
  + **基础API：** 实现对硬件能力的抽象，开放芯片的能力，保证完备性和兼容性。标注为ISASI（Instruction Set Architecture Special Interface，硬件体系结构相关的接口）类别的API，不能保证跨硬件版本兼容。
  + **高阶API：** 实现一些常用的计算算法，用于提高编程开发效率，通常会调用多种基础API实现。高阶API包括数学库、Matmul、Softmax等API。高阶API可以保证兼容性。
* Host API：

  + 高阶API配套的Tiling API：kernel侧高阶API配套的Tiling API，方便开发者获取kernel计算时所需的Tiling参数。
  + AscendC算子原型注册与管理API：用于AscendC算子原型定义和注册的API。
  + Tiling数据结构注册API：用于AscendC算子TilingData数据结构定义和注册的API。
  + 平台信息获取API：在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。平台信息获取API提供获取这些平台信息的功能。
* 算子调测API：用于算子调测的API，包括孪生调试，性能调测等。

  进行AscendC算子Host侧编程时，需要使用基础数据结构和API，请参考[gert命名空间](cannkit-anchorinstanceinfo-introduction.md)，完成算子开发后，需要使用Runtime API完成算子的调用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ZoNfU8o7RBCBQjFqaFNwYQ/zh-cn_image_0000002583439303.png?HW-CC-KV=V1&HW-CC-Date=20260427T235136Z&HW-CC-Expire=86400&HW-CC-Sign=3F89B150C7E29BB3B6E17FB57777FFAD3FC039D66848A06692208BF3738D18AB)

## Kernel API-基础API

**表1** 标量计算API列表

| 接口名 | 功能描述 |
| --- | --- |
| [ScalarGetCountOfValue](cannkit-scalargetcountofvalue.md) | 获取一个uint64\_t类型数字的二进制中0或者1的个数。 |
| [ScalarCountLeadingZero](cannkit-scalarcountleadingzero.md) | 计算一个uint64\_t类型数字前导0的个数（二进制从最高位到第一个1一共有多少个0）。 |
| [ScalarCast](cannkit-scalarcast.md) | 将一个scalar的类型转换为指定的类型。 |
| [CountBitsCntSameAsSignBit](cannkit-countbitscntsameassignbit.md) | 计算一个uint64\_t类型数字的二进制中，从最高数值位开始与符号位相同的连续比特位的个数。 |
| [ScalarGetSFFValue](cannkit-scalargetsffvalue.md) | 获取一个uint64\_t类型数字的二进制中第一个0或1出现的位置。 |

**表2** 矢量计算API列表

| 分类 | 接口名 | 功能描述 | 当前是否支持孪生调试 |
| --- | --- | --- | --- |
| 单目指令 | [Exp](cannkit-vector-calculation-exp.md) | 按元素取自然指数。 | 是 |
| 单目指令 | [Ln](cannkit-vector-calculation-lnln.md) | 按元素取自然对数。 | 是 |
| 单目指令 | [Abs](cannkit-vector-calculation-abs.md) | 按元素取绝对值。 | 是 |
| 单目指令 | [Reciprocal](cannkit-reciprocal.md) | 按元素取倒数。 | 是 |
| 单目指令 | [Sqrt](cannkit-vector-calculation-sqrt.md) | 按元素做开方。 | 是 |
| 单目指令 | [Rsqrt](cannkit-rsqrt.md) | 按元素做开方后取倒数。 | 是 |
| 单目指令 | [Not](cannkit-vector-calculation-not.md) | 按元素做按位取反。 | 是 |
| 单目指令 | [Relu](cannkit-vector-calculation-relu.md) | 按元素做线性整流Relu。 | 是 |
| 双目指令 | [Add](cannkit-add.md) | 按元素求和。 | 是 |
| 双目指令 | [Sub](cannkit-cannkit-sub.md) | 按元素求差。 | 是 |
| 双目指令 | [Mul](cannkit-vector-calculation-binocular-mul.md) | 按元素求积。 | 是 |
| 双目指令 | [Div](cannkit-vector-calculation-binocular-div.md) | 按元素求商。 | 是 |
| 双目指令 | [Max](cannkit-vector-calculation-binocular-max.md) | 按元素求最大值。 | 是 |
| 双目指令 | [Min](cannkit-vector-calculation-binocular-min.md) | 按元素求最小值。 | 是 |
| 双目指令 | [And](cannkit-vector-calculation-binocular-and.md) | 针对每对元素执行按位与运算。 | 是 |
| 双目指令 | [Or](cannkit-vector-calculation-binocular-or.md) | 针对每对元素执行按位或运算。 | 是 |
| 标量双目指令 | [Adds](cannkit-scalar-binocular-adds.md) | 矢量内每个元素与标量求和。 | 是 |
| 标量双目指令 | [Muls](cannkit-scalar-binocular-muls.md) | 矢量内每个元素与标量求积。 | 是 |
| 标量双目指令 | [Maxs](cannkit-scalar-binocular-maxs.md) | 源操作数矢量内每个元素与标量相比，如果比标量大，则取源操作数值，比标量的值小，则取标量值。 | 是 |
| 标量双目指令 | [Mins](cannkit-scalar-binocular-mins.md) | 源操作数矢量内每个元素与标量相比，如果比标量大，则取标量值，比标量的值小，则取源操作数。 | 是 |
| 标量双目指令 | [ShiftLeft](cannkit-scalar-binocular-shiftleft.md) | 源操作数内每个元素做逻辑左移，逻辑左移的位数由输入参数scalar决定。 | 是 |
| 标量双目指令 | [ShiftRight](cannkit-scalar-binocular-shiftright.md) | 源操作数内每个元素做右移，右移的位数由输入参数scalar决定。 | 是 |
| 标量双目指令 | [LeakyRelu](cannkit-scalar-binocular-leakyrelu.md) | 按元素做带泄露线性整流Leaky ReLU。 | 否 |
| 标量三目指令 | [Axpy](cannkit-axpy.md) | 源操作数(srcLocal)中每个元素与标量求积后和目的操作数(dstLocal)中的对应元素相加。 | 否 |
| 精度转换指令 | [Cast](cannkit-precision-conversion-instruction.md#cast) | 根据源操作数和目的操作数Tensor的数据类型进行精度转换。 | 是 |
| 数据转换 | [Transpose](cannkit-transpose.md) | 可实现16\*16的二维矩阵数据块的转置。可实现[N,C,H,W]与[N,H,W,C]互相转换。 | 是 |
| 数据转换 | [TransDataTo5HD](cannkit-transdatato5hd.md) | 数据格式转换，一般用于将NCHW格式转换成NC1HWC0格式。特别的，也可以用于二维矩阵数据块的转置。 | 是 |
| 数据填充 | [Duplicate](cannkit-data-duplicate.md) | 将一个变量或一个立即数，复制多次并填充到向量。 | 是 |
| 数据填充 | [CreateVecIndex](cannkit-data-createvecindex.md) | 以firstValue为起始值创建向量索引。 | 是 |
| 数据分散/数据收集 | [Gather](cannkit-data-distribution-collection.md#gather) | 给定输入的张量和一个地址偏移张量，Gather指令根据偏移地址将输入张量按元素收集到结果张量中。 | 否 |

**表3** 数据搬运API列表

| 接口名 | 功能描述 |
| --- | --- |
| [DataCopy](cannkit-common-data-movement.md) | 数据搬运接口，包括普通数据搬运、随路格式转换。 |
| [DataCopyPad](cannkit-datacopypad.md) | 数据搬运接口，该接口提供数据非对齐搬运的功能。 |

**表4** 内存管理与同步控制API列表

| 接口名 | 功能描述 |
| --- | --- |
| [TPipe](cannkit-tpipe-constructor.md) | TPipe是用来管理全局内存等资源的框架。通过TPipe类提供的接口可以完成内存等资源的分配管理操作。 |
| [GetTPipePtr](cannkit-gettpipeptr.md) | 获取框架当前管理全局内存的TPipe指针，开发者获取指针后，可进行TPipe相关的操作。 |
| [TBufPool](cannkit-tbufpool-overview.md) | TPipe可以管理全局内存资源，而TBufPool可以手动管理或复用Unified Buffer/L1 Buffer物理内存，主要用于多个stage计算中Unified Buffer/L1 Buffer物理内存不足的场景。 |
| [TQue](cannkit-tque-overview.md) | 提供入队出队等接口，通过队列（Queue）完成任务间通信和同步。 |
| [TQueBind](cannkit-overview.md) | TQueBind绑定源逻辑位置和目的逻辑位置，根据源位置和目的位置，来确定内存分配的位置 、插入对应的同步事件，帮助开发者解决内存分配和管理、同步等问题。 |
| [TBuf](cannkit-tbuf-overview.md) | 使用AscendC编程的过程中，可能会用到一些临时变量。这些临时变量占用的内存可以使用TBuf数据结构来管理。 |
| [GetUserWorkspace](cannkit-getuserworkspace.md) | 获取开发者使用的workspace指针。 |
| [SetSysWorkSpace](cannkit-setsysworkspace.md) | 在进行融合算子编程时，由于框架通信机制需要使用到workspace，也就是系统workspace，所以在该场景下，开发者要调用该接口，设置系统workspace的指针。 |
| [GetSysWorkSpacePtr](cannkit-getsysworkspaceptr.md) | 获取系统workspace指针。 |

**表5** 系统变量访问API列表

| 接口名 | 功能描述 |
| --- | --- |
| [GetBlockNum](cannkit-getblocknum.md) | 获取当前任务配置的Block数，用于代码内部的多核逻辑控制等。 |
| [GetBlockIdx](cannkit-getblockidx.md) | 获取当前core的index，用于代码内部的多核逻辑控制及多核偏移量计算等。 |

**表6** 调测接口列表

| 接口名 | 功能描述 |
| --- | --- |
| [DumpTensor](cannkit-commissioning-interfaces-dumptensor.md) | 基于算子工程开发的算子，可以使用该接口Dump指定Tensor的内容。 |
| [printf](cannkit-commissioning-interfaces-printf.md) | 基于算子工程开发的算子，可以使用该接口实现CPU侧/NPU侧调试场景下的格式化输出功能。 |
| [assert](cannkit-commissioning-interfaces-assert.md) | 基于算子工程开发的算子，可以使用该接口实现CPU/NPU域assert断言功能。 |
| [DumpAccChkPoint](cannkit-commissioning-interfaces-dumpaccch.md) | 基于算子工程开发的算子，可以使用该接口Dump指定Tensor的内容。该接口可以支持指定偏移位置的Tensor打印。 |
| [Trap](cannkit-trap.md) | 当软件产生异常后，使用该指令使kernel中止运行。 |

**表7** 其他接口列表

| 分类 | 接口名 | 功能描述 |
| --- | --- | --- |
| Kernel Tiling | [GET\_TILING\_DATA](cannkit-get-tiling-data.md) | 用于获取算子kernel入口函数传入的tiling信息，并填入注册的Tiling结构体中，此函数会以宏展开的方式进行编译。如果开发者注册了多个TilingData结构体，使用该接口返回默认注册的结构体。 |
| Kernel Tiling | [GET\_TILING\_DATA\_WITH\_STRUCT](cannkit-get-tiling-data-with-struct.md) | 使用该接口指定结构体名称，可获取指定的tiling信息，并填入对应的Tiling结构体中，此函数会以宏展开的方式进行编译。与GET\_TILING\_DATA的区别是：GET\_TILING\_DATA只能获取默认注册的结构体，该接口可以根据指定的结构体名称获取对应的结构体，常用于针对不同的TilingKey注册了不同结构体的情况下。 |
| Kernel Tiling | [TILING\_KEY\_IS](cannkit-tiling-key-is.md) | 在核函数中判断本次执行时的tiling\_key是否等于某个key，从而标识tiling\_key==key的一条kernel分支。 |

## Kernel API-高阶API

**表8** Matmul API列表

| 接口名 | 功能描述 |
| --- | --- |
| [Matmul](cannkit-matmul-usage-description.md) | Matmul矩阵乘法的运算。 |

## Host API

**表9** Host API列表

| 分类 | 接口名 | 功能描述 |
| --- | --- | --- |
| 原型注册与管理 | [原型注册接口（OP\_ADD）](cannkit-prototype-api-registration.md) | 注册算子的原型定义。 |
| 原型注册与管理 | [OpDef](cannkit-input.md) | 用于算子原型定义。 |
| 原型注册与管理 | [OpParamDef](cannkit-paramtype.md) | 用于算子参数定义。 |
| 原型注册与管理 | [OpAttrDef](cannkit-opattrdef.md) | 用于算子属性定义。 |
| 原型注册与管理 | [OpAICoreDef](cannkit-settiling.md) | 用于定义AI处理器上相关实现信息，并关联Tiling实现、Shape推导等函数。 |
| Tiling数据结构注册 | [TilingData结构定义](cannkit-tilingdata-structure-definition.md) | 定义一个TilingData的类，添加所需的成员变量（TilingData字段），用于保存所需TilingData参数。完成该TilingData类的定义后，该类通过继承TilingDef类（用来存放、处理开发者自定义Tiling结构体成员变量的基类）提供TilingData字段设置、序列化和保存等接口。 |
| Tiling数据结构注册 | [TilingData结构注册](cannkit-tilingdata-structure-registration.md) | 注册定义的TilingData结构体并和自定义算子绑定。 |
| 平台信息获取 | [PlatformAscendC](cannkit-platformascendc-introduction.md) | 在实现Host侧的Tiling函数时，可能需要获取一些硬件平台的信息，来支撑Tiling的计算，比如获取硬件平台的核数等信息。PlatformAscendC类提供获取这些平台信息的功能。 |

## 算子调测API

**表10** 算子调测API列表

| 接口名 | 功能描述 |
| --- | --- |
| [GmAlloc](cannkit-gmalloc.md) | 进行核函数的CPU侧运行验证时，用于创建共享内存：在/tmp目录下创建一个共享文件，并返回该文件的映射指针。 |
| [GmFree](cannkit-gmfree.md) | 进行核函数的CPU侧运行验证时，用于释放通过GmAlloc申请的共享内存。 |
| [ICPU\_RUN\_KF](cannkit-icpu-run-kf.md) | 进行核函数的CPU侧运行验证时，CPU调测总入口，完成CPU侧的算子程序调用。 |
| [ICPU\_SET\_TILING\_KEY](cannkit-icpu-set-tiling-key.md) | 用于指定本次CPU调测使用的tilingKey。调测执行时，将只执行算子核函数中该tilingKey对应的分支。 |
