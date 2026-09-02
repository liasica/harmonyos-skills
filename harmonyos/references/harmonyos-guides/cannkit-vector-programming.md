---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-vector-programming
title: 矢量编程
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 矢量编程
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:04+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:863dc0cc1f7ffcf8bf4a590f8fb9d5e882ca4028d4a0c7f57a004f91e9be84af
---

## 算子实现流程概述

基于AscendC方式实现矢量算子的流程如图1所示。

**图1** 矢量算子实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/pjk3D2xqTymCqsbPnp2H7g/zh-cn_image_0000002736314409.png)

* 算子分析：分析算子的数学表达式、输入、输出以及计算逻辑的实现，明确需要调用的AscendC接口。
* 核函数定义：定义AscendC算子入口函数。
* 根据矢量编程范式实现算子类：完成核函数的内部实现。

下文以ElemWise(Add)算子为例，对上述步骤进行详细介绍。本样例中介绍的算子完整代码参见[add\_custom.cpp](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_add_custom_cpp/blob/master/FrameworkLaunch/AddCustom/op_kernel/add_custom.cpp)。

### 算子分析

在开发算子代码之前需要分析算子的数学表达式、输入、输出以及计算逻辑的实现，明确需要调用的AscendC接口。

1. 明确算子的数学表达式及计算逻辑。

   Add算子的数学表达式为：

   ```cpp
   z = x + y
   ```

   计算逻辑是：AscendC提供的[矢量计算](cannkit-vector-calculation-exp.md)接口的操作元素都为LocalTensor，输入数据需要先搬运进片上存储，然后使用计算接口完成两个输入参数相加，得到最终结果，再搬出到外部存储上。AscendC Add算子的计算逻辑如下图所示。

   **图2** 算子计算逻辑

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/VW2AMo5cQci9JkjuNSpXRQ/zh-cn_image_0000002706675366.png)
2. 明确输入和输出。

   * Add算子有两个输入：x与y，输出为z。
   * 本样例中算子的输入支持的数据类型为half(float16)，算子输出的数据类型与输入数据类型相同。
   * 算子输入支持shape(8，2048)，输出shape与输入shape相同。
   * 算子输入支持的format为：ND。
3. 确定核函数名称和参数。

   * 开发者可以自定义核函数名称，本样例中核函数命名为add\_custom。
   * 根据对算子输入输出的分析，确定核函数有3个参数x，y，z；x，y为输入在Global Memory上的内存地址，z为输出在Global Memory上的内存地址。
4. 确定算子实现所需接口。

   * 实现涉及外部存储和内部存储间的数据搬运，查看AscendC API参考中的数据搬移接口，需要使用[DataCopy](cannkit-common-data-movement.md)来实现数据搬移。
   * 本样例只涉及矢量计算的加法操作，通过查看AscendC API参考中的[矢量计算](cannkit-vector-calculation-exp.md)接口定义，初步分析可使用双目指令[Add](cannkit-add.md)接口实现x+y。
   * 计算中使用到的Tensor数据结构，使用Queue队列进行管理，会使用到[EnQue](cannkit-tque-enque.md)、[DeQue](cannkit-tque-deque.md)等接口。

   通过以上分析，得到AscendC Add算子的设计规格如下。

   * **算子类型(OpType)：** Add
   * **算子输入输出：**
     + **name:** x（输入）、y（输入）、z（输出）
     + **shape:** (8, 2048)
     + **data type:** half
     + **format:** ND
   * **核函数名称：** add\_custom
   * **使用的主要接口：** DataCopy：数据搬移接口；Add：矢量双目指令接口；EnQue、DeQue等接口：Queue队列管理接口。
   * **算子实现文件名称：** add\_custom.cpp

### 核函数定义

根据[核函数定义](cannkit-kernel-function.md#核函数定义)中介绍的规则进行核函数的定义。

1. 函数原型定义

   本样例中，函数名为add\_custom（核函数名称可自定义），根据[算子分析](cannkit-vector-programming.md#算子分析)中对算子输入输出的分析，确定有3个参数x，y，z，其中x，y为输入内存，z为输出内存。根据[核函数定义](cannkit-kernel-function.md#核函数定义)核函数的规则介绍，函数原型定义如下所示：使用\_\_global\_\_函数类型限定符来标识它是一个核函数；使用\_\_aicore\_\_函数类型限定符来标识该核函数在设备端aicore上执行；为方便起见，统一使用GM\_ADDR宏修饰入参，GM\_ADDR宏定义请参考[核函数](cannkit-kernel-function.md)。

   ```cpp
   extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
   {
   }
   ```
2. 调用算子类的Init和Process函数。

   算子类的Init函数，完成内存初始化相关工作，Process函数完成算子实现的核心逻辑，具体介绍参见[算子类实现](cannkit-vector-programming.md#算子类实现)。

   ```cpp
   extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
   {
       KernelAdd op;
       op.Init(x, y, z);
       op.Process();
   }
   ```

### 算子类实现

根据上一节介绍，核函数中会调用算子类的Init和Process函数，本节具体讲解如何基于编程范式实现算子类。

根据矢量编程范式对Add算子的实现流程进行设计的思路如下，矢量编程范式请参考[Vector编程范式](cannkit-programming-paradigm.md#vector编程范式)，设计完成后得到的Add算子实现流程图参见图3：

* Add算子的实现流程分为3个基本任务：CopyIn，Compute，CopyOut。CopyIn任务负责将Global Memory上的输入Tensor xGm和yGm搬运至Local Memory，分别存储在xLocal，yLocal，Compute任务负责对xLocal，yLocal执行加法操作，计算结果存储在zLocal中，CopyOut任务负责将输出数据从zLocal搬运至Global Memory上的输出Tensor zGm中。
* CopyIn，Compute任务间通过VECIN队列inQueueX，inQueueY进行通信和同步，Compute，CopyOut任务间通过VECOUT队列outQueueZ进行通信和同步。
* 任务间交互使用到的内存、临时变量使用到的内存统一使用pipe内存管理对象进行管理。

**图3** Add算子实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/1-xMe1SPT4G84HIofYorKQ/zh-cn_image_0000002736434453.png)

算子类中主要实现上述流程，包含对外开放的初始化Init函数和核心处理函数Process，Process函数中会对上图中的三个基本任务进行调用；同时包括一些算子实现中会用到的私有成员，比如上图中的Global Tensor和VECIN、VECOUT队列等。KernelAdd算子类具体成员如下。

```cpp
class KernelAdd {
public:
    __aicore__ inline KernelAdd() {}
    // 初始化函数，用于初始化内存
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z){}
    // 核心处理函数，实现算子逻辑，调用私有成员函数CopyIn、Compute和CopyOut，完成矢量算子的三阶段流水线执行
    __aicore__ inline void Process(){}
  
private:
    // CopyIn函数，完成CopyIn阶段的处理，由Process函数调用
    __aicore__ inline void CopyIn(int32_t progress){}
    // Compute函数，完成Compute阶段的处理，由Process函数调用
    __aicore__ inline void Compute(int32_t progress){}
    // CopyOut函数，完成CopyOut阶段的处理，由Process函数调用
    __aicore__ inline void CopyOut(int32_t progress){}
 
private:
    AscendC::TPipe pipe; // 管道内存管理对象
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueX, inQueueY; // 输入数据队列管理对象，队列位置为VECIN
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueZ; // 输出数据队列管理对象，队列位置为VECOUT
    AscendC::GlobalTensor<half> xGm; // 输入输出全局内存地址管理对象，xGm和yGm为输入，zGm为输出
    AscendC::GlobalTensor<half> yGm;
    AscendC::GlobalTensor<half> zGm;
};
```

初始化函数主要完成以下内容：

* 设置输入输出Global Tensor的Global Memory内存地址。

  本样例中使用多核并行计算，即把数据进行分片，分配到多个核上进行处理。AscendC核函数是在一个核上的处理函数，所以只处理部分数据，需要在初始化函数中获取该核函数需要处理的输入输出在Global Memory上的内存偏移地址，并将该偏移地址设置在Global Tensor中。

  以获取输入x在Global Memory上的内存偏移地址为例：

  ```cpp
  xGm.SetGlobalBuffer((__gm__ half*)x + BLOCK_LENGTH * GetBlockIdx(), BLOCK_LENGTH);
  ```

  本样例中的分配方案是：数据整体长度TOTAL\_LENGTH为8 \* 2048，平均分配到8个核上运行，每个核上处理的数据大小BLOCK\_LENGTH为2048字节。x + BLOCK\_LENGTH \* GetBlockIdx()即为单核处理程序中x在Global Memory上的内存偏移地址，获取偏移地址后，使用[GlobalTensor](cannkit-globaltensor.md)类的接口设定该核上Global Memory的起始地址以及长度。具体示意图请参考图4。

  **图4** 多核并行处理示意图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/VPm7ZpvpS3Kn-hzV83F-Ag/zh-cn_image_0000002706835306.png)
* 通过Pipe内存管理对象为输入输出Queue分配内存。

  比如，为输入x的Queue分配内存，可以通过如下代码段实现：

  ```cpp
  pipe.InitBuffer(inQueueX, BUFFER_NUM, TILE_LENGTH * sizeof(half))
  ```

  对于单核上的处理数据，可以进行数据切块(Tiling)，在本示例中，将数据切分成8块（并不意味着8块就是性能最优）仅作为参考。切分后的每个数据块再次切分成2块，即可开启double buffer，实现流水线之间的并行。

  这样单核上的数据（2048个数）被切分成16块，每块TILE\_LENGTH(128)个数据。上文代码表示Pipe为inQueueX分配了两块大小为TILE\_LENGTH \* sizeof(half)个字节的内存块，每个内存块能容纳TILE\_LENGTH(128)个half类型数据。数据切分示意图如图5所示。

  **图5** 单核数据切分示意图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/-n1wNazKSuqcvm9WC-s69g/zh-cn_image_0000002736314411.png)

Kirin9020/Kirin9030/KirinX90系列处理器支持的核数为1，具体的初始化函数代码如下。

```cpp
constexpr int32_t TOTAL_LENGTH = 8 * 2048; // 数据总长度
constexpr int32_t USE_CORE_NUM = 1; // 使用的核心数量
constexpr int32_t BLOCK_LENGTH = TOTAL_LENGTH / USE_CORE_NUM; // 每个核心计算的数据长度
constexpr int32_t TILE_NUM = 8; // 将数据拆分为8个图块（tile）供每个核心处理
constexpr int32_t BUFFER_NUM = 2; // 每个队列中的张量数量（用于双缓冲）
constexpr int32_t TILE_LENGTH = BLOCK_LENGTH / TILE_NUM / BUFFER_NUM; // 每个图块长度（由于双缓冲机制，需拆分为2部分）
__aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z)
{
    // 获取当前核心的起始索引，实现核心并行
    xGm.SetGlobalBuffer((__gm__ half*)x + BLOCK_LENGTH * AscendC::GetBlockIdx(), BLOCK_LENGTH);
    yGm.SetGlobalBuffer((__gm__ half*)y + BLOCK_LENGTH * AscendC::GetBlockIdx(), BLOCK_LENGTH);
    zGm.SetGlobalBuffer((__gm__ half*)z + BLOCK_LENGTH * AscendC::GetBlockIdx(), BLOCK_LENGTH);
    // 初始化管道（Pipe）缓冲区到队列，单位是字节
    pipe.InitBuffer(inQueueX, BUFFER_NUM, TILE_LENGTH * sizeof(half));
    pipe.InitBuffer(inQueueY, BUFFER_NUM, TILE_LENGTH * sizeof(half));
    pipe.InitBuffer(outQueueZ, BUFFER_NUM, TILE_LENGTH * sizeof(half));
}
```

基于矢量编程范式，将核函数的实现分为3个基本任务：CopyIn，Compute，CopyOut。Process函数中通过如下方式调用这三个函数。

```cpp
    __aicore__ inline void Process()
    {
        // 由于使用了双缓冲区，循环次数需要加倍。
        constexpr int32_t loopCount = TILE_NUM * BUFFER_NUM;
        // 平铺策略，流水线并行
        for (int32_t i = 0; i < loopCount; i++) {
            CopyIn(i);
            Compute(i);
            CopyOut(i);
        }
    }
```

根据编程范式上面的算法分析，将整个计算拆分成三个Stage，开发者单独编写每个Stage的代码，三阶段流程示意图参见图3，具体流程如下。

1. CopyIn函数实现。

   1. 使用[DataCopy](cannkit-common-data-movement.md)接口将GlobalTensor数据拷贝到LocalTensor。
   2. 使用[EnQue](cannkit-tque-enque.md)将LocalTensor放入VecIn的Queue中。

   ```cpp
   __aicore__ inline void CopyIn(int32_t progress)
       {
           // 从队列内存中分配张量
           AscendC::LocalTensor<half> xLocal = inQueueX.AllocTensor<half>();
           AscendC::LocalTensor<half> yLocal = inQueueY.AllocTensor<half>();
           // 将progress_th tile从全局张量复制到局部张量
           AscendC::DataCopy(xLocal, xGm[progress * TILE_LENGTH], TILE_LENGTH);
           AscendC::DataCopy(yLocal, yGm[progress * TILE_LENGTH], TILE_LENGTH);
           // 将输入张量入队到VECIN队列
           inQueueX.EnQue(xLocal);
           inQueueY.EnQue(yLocal);
       }
   ```
2. Compute函数实现。

   1. 使用[DeQue](cannkit-tque-deque.md)从VecIn中取出LocalTensor。
   2. 使用[Add](cannkit-add.md)接口完成矢量计算。
   3. 使用[EnQue](cannkit-tque-enque.md)将计算结果LocalTensor放入到VecOut的Queue中。
   4. 使用[FreeTensor](cannkit-tque-freetensor.md)释放不再使用的LocalTensor。

   ```cpp
   __aicore__ inline void Compute(int32_t progress)
   {
       // 从VECIN队列中取出输入张量。
       AscendC::LocalTensor<half> xLocal = inQueueX.DeQue<half>();
       AscendC::LocalTensor<half> yLocal = inQueueY.DeQue<half>();
       AscendC::LocalTensor<half> zLocal = outQueueZ.AllocTensor<half>();
       // 调用Add指令进行计算
       AscendC::Add(zLocal, xLocal, yLocal, TILE_LENGTH);
       // 将输出张量加入VECOUT队列
       outQueueZ.EnQue<half>(zLocal);
       // 免费输入张量，可重复使用
       inQueueX.FreeTensor(xLocal);
       inQueueY.FreeTensor(yLocal);
   }
   ```
3. CopyOut函数实现。

   1. 使用[DeQue](cannkit-tque-deque.md)接口从VecOut的Queue中取出LocalTensor。
   2. 使用[DataCopy](cannkit-common-data-movement.md)接口将LocalTensor拷贝到GlobalTensor上。
   3. 使用[FreeTensor](cannkit-tque-freetensor.md)将不再使用的LocalTensor进行回收。

   ```cpp
    __aicore__ inline void CopyOut(int32_t progress)
   {
       // 从VECOUT队列中取出输出张量。
       AscendC::LocalTensor<half> zLocal = outQueueZ.DeQue<half>();
       // 将局部张量中的progress_th块复制到全局张量
       AscendC::DataCopy(zGm[progress * TILE_LENGTH], zLocal, TILE_LENGTH);
       // 可自由输出张量以供重用
       outQueueZ.FreeTensor(zLocal);
   }
   ```

### 运行验证

核函数即算子kernel程序开发完成后，即可编写host侧的核函数调用程序，实现从host侧的APP程序调用算子，进行运行验证。
