---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-internal-associated-apis
title: 内部关联接口
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > 内部关联接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b94a44e7c3b3d3c8204f01ca9688b1e94c65389848efec9cef7b485afa86081
---

在进行算子原型注册、Tiling实现、shape推导过程中，使用到的外部开放接口中会调用到一些辅助数据结构和接口，称之为**内部关联接口**。开发者不会直接调用内部关联接口，此处仅作简单介绍。

## KernelContext类

本类是对底层数据结构KernelRunContext的包装，包含kernel执行时所需的算子输入、输出个数信息以及输入输出数据信息、compute\_node\_info和kernel\_extend\_info。

**表1** KernelContext类成员函数

| 接口名 | 接口功能 |
| --- | --- |
| GetInput | 获取输入的Chain指针。Chain是一个可以用来保存任意类型数据的类。 |
| GetInputNum | 获取kernel的输入数量。 |
| GetInputPointer | 获取输入数据的指针，本函数首先获取输入Chain，然后从输入Chain中获取指针。 |
| GetInputStrPointer | 获取输入字符串的指针，本函数首先获取输入Chain，然后从输入Chain中获取指针。 |
| GetInputValue | 获取输入数据的值，本函数首先获取输入Chain，然后从输入Chain中获取值。 |
| GetOutput | 获取输出的Chain指针。 |
| GetOutput2 | 获取输出的Chain指针。 |
| GetOutputNum | 获取kernel的输出数量。 |
| GetOutputPointer | 获取输出数据的指针，本函数首先获取输出Chain，然后从Chain中获取指针。 |
| GetContext | 获取底层的context结构体。 |
| GetKernelExtend | 获取kernel扩展信息的指针。 |
| GetComputeNodeExtend | 获取计算节点信息的指针。 |
| MutableInput | 获取输入的Chain指针。 |
| MutableInputPointer | 获取输入数据的指针，本函数首先获取输入Chain，然后从输入Chain中获取指针。 |
| IsInlineSize | 根据数据的长度判断一个数据是否会被inline存储，所谓inline存储是指此数据保存在context中时不需要单独分配内存。 |

## TilingParseContext类

用于TilingParse所需的信息保存在本类中，本类为编写算子的TilingParse函数时提供上下文信息，在TilingParse时可以从本类中获取所需的信息。

**表2** TilingParseContext类成员函数

| 接口名 | 接口功能 |
| --- | --- |
| GetCompiledJson | 获取算子编译产生的json字符串。 |
| GetCompiledInfo | 获取CompiledInfo实例。 |
| GetPlatformInfo | 获取fe::PlatFormInfos指针。 |

## Chain类

Chain是一个可以用来保存任意类型数据的类。通过其Set接口保存数据，通过GetPointer或者GetValue方法获取保存的数据。

**表3** Chain类成员函数

| 接口名 | 接口功能 |
| --- | --- |
| GetPointer | 获取指向Chain中保存数据的指针。 |
| GetValue | 获取Chain中保存的数据的值。 |
| Set | 将数据设置到Chain中。设置数据指针时，会尝试调用deleter将原有保存在Chain的数据删除。 |
| SetWithDefaultDeleter | 将数据设置到Chain中。设置数据指针时，会尝试调用deleter将原有保存在Chain的数据删除。 |
| HasDeleter | 判断当前Chain中保存的数据是否有deleter。 |

## ContinuousBuffer类

ContinuousBuffer类用于连续存储任意类型的数据，每个数据被转成uint8\_t数组进行存储，每个存储单元称为一个buffer。ContinuousBuffer使用两个属性来描述被存储的数据，分别是存储buffer的个数以及每个buffer对应的内存偏移量offsets\_。每个buffer在内存上是连续的。

**表4** ContinuousBuffer类成员函数

| 接口名 | 接口功能 |
| --- | --- |
| GetNum | 获取buffer的数量。 |
| GetTotalLength | 获取本实例的总长度。 |
| Get | 获取buffer指针、长度信息。 |

## KernelExtendInfo类

本类是用于保存的kernel运行时的额外信息，包括kernel的名字、类型、用于profiling注册的kernel type的index以及计算节点名的index。

**表5** KernelExtendInfo类成员函数

| 接口名 | 接口功能 |
| --- | --- |
| GetKernelName | 获取kernel name。 |
| SetKernelName | 设置kernel name。 |
| GetKernelType | 获取kernel type。一个算子可以对应多个kernel，也就对应多个kernel type。 |
| SetKernelType | 设置kernel type。 |
| SetKernelTypeIdx | 设置kernel\_type\_idx\_，用于profiling。profiling时设置的kernel type字符串对应的idx，用idx代替kernel type字符串作为标识，提升速度。 |
| SetNodeNameIdx | 设置compute\_node\_name\_idx\_，用于profiling。profiling时，用idx代替node name字符串作为标识，提升速度。 |
| GetNodeNameIdx | 获取compute\_node\_name\_idx\_，用于profiling。 |
| GetKernelTypeIdx | 获取kernel\_type\_idx\_，用于profiling。 |

## TensorOperateType

```
1. enum TensorOperateType {
2. kGetTensorAddress,  // < 获取Tensor的地址
3. kFreeTensor,        // < 释放Tensor
4. kPlusShareCount,    // < 共享Tensor
5. kTensorOperateType
6. };
```

## StructSizeInfoBase类

StructSizeInfoBase类用来存放、获取AscendC高阶API和开发者自定义的tiling结构体大小，通过单例实现一个结构体信息库。

**表6** StructSizeInfoBase类成员函数

| 函数名称 | 含义 |
| --- | --- |
| GetInstance | 获取StructSizeInfoBase类的单例。 |
| SetStructSize | 设置高阶API/开发者自定义tiling结构大小。 |
| GetStructSize | 获取高阶API/开发者自定义tiling结构大小。 |

## TilingDataStructBase类

TilingDataStructBase的类，用于记录Tiling结构体构造过程信息。提供以下接口：

**表7** TilingDataStructBase类成员函数

| 函数名称 | 含义 |
| --- | --- |
| GetInstance | 获取TilingDataStructBase类的单例。 |
| RecordTilingStruct | 用于框架检查不同算子注册同名不同结构tiling结构体情况，若出现则会打印warning信息。 |

## 数值计算校验相关接口

框架内部使用的数值计算校验相关接口。

**表8** 接口说明

| 函数名称 | 含义 |
| --- | --- |
| MulOverflow | 判断乘法数值运算是否溢出。其中溢出的判断条件为乘积后的数值大于ret类型TRet所能表示的最大值。 |
| AddOverflow | 判断加法数值运算是否溢出。其中溢出的判断条件为相加后的数值大于ret类型TRet所能表示的最大值。 |
| Compat | 判断入参的数值是否超过指定类型T所能表示的数值范围。 |

## OpExecuteContext类

本类用于保存图模式下调用单算子执行API场景下的上下文。

**表9** OpExecuteContext类成员函数

| 函数名称含义 | 含义 |
| --- | --- |
| GetInputTensor | 获取指定索引输入的Tensor。 |
| GetOptionalInputTensor | 获取指定索引的可选输入的Tensor。 |
| GetDynamicInputTensor | 获取指定索引的动态个数输入的Tensor。 |
| GetRequiredInputTensor | 获取指定索引的必选输入的Tensor。 |
| GetOutputTensor | 获取指定索引输出的Tensor。 |
| GetDynamicOutputTensor | 获取指定索引的动态个数输出的Tensor。 |
| GetRequiredOutputTensor | 获取指定索引的必选输出的Tensor。 |
| GetStream | 获取下发算子的流信息。 |
| GetOpExecuteFunc | 获取多kernel算子的执行回调函数。 |
| MallocWorkspace | 分配workspace内存。 |
| FreeWorkspace | 释放workspace内存。 |
| GetDeterministic | 获取确定性计算配置选项。 |
| GetAllowHf32 | 获取allow\_hf32配置选项。 |
| GetPrecisionMode | 获取精度模式配置选项。 |
