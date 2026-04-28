---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-kernel-function
title: 核函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程模型 > 核函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00f9e1b001bb1c12b5bb2ac4c3ba5b99b8690ff4a092fb5daa0de726ea9e8752
---

从[SPMD模型](cannkit-spmd-model.md)可以得知，使用AscendC进行编程时，我们编写一份算子实现代码，算子被调用时，将启动N个运行实例，在N个核上运行。本节将介绍算子实现的入口函数。

核函数(Kernel Function)是AscendC算子设备侧实现的入口。在核函数中，需要为在一个核上执行的代码规定要进行的数据访问和计算操作，当核函数被调用时，多个核都执行相同的核函数代码，具有相同的参数，并行执行。

AscendC允许开发者使用核函数这种C/C++函数的语法扩展来管理设备端的运行代码，开发者在核函数中进行算子类对象的创建和其成员函数的调用，由此实现该算子的所有功能。核函数是主机端和设备端连接的桥梁，本章将具体介绍核函数的用法。

说明

Kirin9020/KirinX90系列处理器暂不支持通过<<<>>>调用核函数。

## 核函数定义

```
1. extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t* x, __gm__ uint8_t* y, __gm__ uint8_t* z)
```

以上是一个核函数声明的例子，编写核函数时需要遵循以下规则。

* **使用函数类型限定符**

  除了需要按照C/C++函数声明的方式定义核函数之外，还要为核函数加上额外的函数类型限定符，包含\_\_global\_\_和\_\_aicore\_\_。

  使用\_\_global\_\_函数类型限定符来标识它是一个核函数，可以被<<<>>>调用；使用\_\_aicore\_\_函数类型限定符来标识该核函数在设备端AI Core上执行：\_\_global\_\_ \_\_aicore\_\_ void kernel\_name(argument list)。

  编程中使用到的函数可以分为三类：核函数（device侧执行）、host侧执行函数、device侧执行函数（除核函数之外的）。三者的调用关系如下图所示：

  + host侧执行函数可以调用同类的host执行函数，也就是通用C/C++编程中的函数调用；也可以通过<<<>>>调用核函数。
  + device侧执行函数（除核函数之外的）可以调用同类的device侧执行函数。
  + 核函数可以调用device侧执行函数（除核函数之外的）。

  **图1** 核函数（device侧执行）、host侧执行函数、device侧执行函数（除核函数之外的）调用关系

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/SbBbmBehStSiGeoYkZXP2Q/zh-cn_image_0000002552799580.png?HW-CC-KV=V1&HW-CC-Date=20260427T235125Z&HW-CC-Expire=86400&HW-CC-Sign=C524877C9A3C0018BCFE9C341D93BEFDCA71154BB6083D67C229C7D9297EE25D)
* **使用变量类型限定符**

  指针入参变量需要增加变量类型限定符\_\_gm\_\_，表明该指针变量指向Global Memory上某处内存地址。
* **其他规则或建议**

  + 规则1：核函数必须具有void返回类型。
  + 规则2：仅支持入参为指针或C/C++内置数据类型(Primitive data types)，如：half\* s0、float\* s1、int32\_t c。
  + 建议：为了统一表达，建议使用GM\_ADDR宏来修饰入参，GM\_ADDR宏定义如下。

    ```
    1. #define GM_ADDR __gm__ uint8_t*
    ```

    使用GM\_ADDR修饰入参的样例如下。

    ```
    1. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
    ```

    这里统一使用uint8\_t类型的指针，在后续的使用中需要将其转化为实际的指针类型。

## 核函数调用

核函数的调用语句是C/C++函数调用语句的一种扩展。本节仅描述最基础的调用方式，实际进行算子开发时，开发者可以通过该方式调用，也可以通过接入AscendC框架的方式调用，更多细节请参考[工程化算子开发](cannkit-overview-of-engineering-operator.md)。

常见的函数调用方式是如下的形式：

```
1. function_name(argument list);
```

核函数使用内核调用符<<<...>>>这种语法形式，来规定核函数的执行配置：

```
1. kernel_name<<<blockDim, l2ctrl, stream>>>(argument list);
```

内核调用符仅可在NPU侧编译时调用，CPU侧编译无法识别该符号。

执行配置由以下blockDim, l2ctrl, stream参数决定：

### blockDim

规定了核函数将会在几个核上执行。每个执行该核函数的核会被分配一个逻辑ID，即block\_idx，可以在核函数的实现中调用[GetBlockIdx](cannkit-getblockidx.md)来获取block\_idx。

blockDim是逻辑核的概念，取值范围为[1, 65535]。为了充分利用硬件资源，一般设置为物理核的核数或其倍数。对于耦合架构和分离架构，blockDim在运行时的意义和设置规则有一些区别，具体说明如下。

* 耦合架构：由于其Vector、Cube单元是集成在一起的，blockDim用于设置启动多个AICore核实例执行，不区分Vector、Cube。AI Core的核数可以通过[GetCoreNumAic](cannkit-getcorenumaic.md)或者[GetCoreNumAiv](cannkit-getcorenumaiv.md)获取。
* 分离架构：

  + 针对仅包含Vector计算的算子，blockDim用于设置启动多少个Vector(AIV)实例执行，比如某款AI处理器上有40个Vector核，建议设置为40
  + 针对仅包含Cube计算的算子，blockDim用于设置启动多少个Cube(AIC)实例执行，比如某款AI处理器上有20个Cube核，建议设置为20。
  + 针对Vector/Cube融合计算的算子，启动时，按照AIV和AIC组合启动，blockDim用于设置启动多少个组合执行，比如某款AI处理器上有40个Vector核和20个Cube核，一个组合是2个Vector核和1个Cube核，建议设置为20，此时会启动20个组合，即40个Vector核和20个Cube核。

    说明

    该场景下，设置的blockDim逻辑核的核数不能超过物理核（2个Vector核和1个Cube核组合为1个物理核）的核数。
  + AIC/AIV的核数分别通过[GetCoreNumAic](cannkit-getcorenumaic.md)和[GetCoreNumAiv](cannkit-getcorenumaiv.md)接口获取。

### l2ctrl

保留参数，暂时设置为固定值nullptr，开发者无需关注。

### stream

类型为aclrtStream，stream用于维护一些异步操作的执行顺序，确保按照应用程序中的代码调用顺序在device上执行。

### 调用示例

如下名为add\_custom的核函数，实现两个矢量的相加，调用示例如下。

```
1. // blockDim设置为8表示在8个核上调用了add_custom核函数，每个核都会独立且并行地执行该核函数，该核函数的参数列表为x，y，z。
2. add_custom<<<8, nullptr, stream>>>(x, y, z);
```

核函数的调用是异步的，核函数的调用结束后，控制权立刻返回给host端，可以调用以下**aclrtSynchronizeStream**函数来强制主机端程序等待所有核函数执行完毕。

```
1. aclError aclrtSynchronizeStream(aclrtStream stream);
```

## 核函数示例

下面提供核函数实现的样例代码片段，完整样例请参考[矢量编程](cannkit-vector-programming.md)。

```
1. // 实现核函数
2. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
3. {
4. // 初始化算子类，算子类提供算子初始化和核心处理等方法
5. KernelAdd op;
6. // 初始化函数，获取该核函数需要处理的输入输出地址，同时完成必要的内存初始化工作
7. op.Init(x, y, z);
8. // 核心处理函数，完成算子的数据搬运与计算等核心逻辑
9. op.Process();
10. }
```
