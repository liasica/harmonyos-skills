---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-interfaces-dumpaccch
title: DumpAccChkPoint
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > DumpAccChkPoint
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:506883d6b371a074e6bf088bd15815811fe5401efefe15bb20fdfe1060861fe5
---

## 函数功能

基于算子工程开发的算子，可以使用该接口Dump指定Tensor的内容。同时支持打印自定义的附加信息（仅支持uint32\_t数据类型的信息），比如打印当前行号等。区别于[DumpTensor](cannkit-commissioning-interfaces-dumptensor.md)，使用该接口可以支持指定偏移位置的Tensor打印。

在算子kernel侧实现代码中需要打印偏移后Tensor数据的地方调用DumpAccChkPoint接口打印相关内容。样例如下。

```
1. AscendC::DumpAccChkPoint(srcLocal,5, 32, dataLen);
```

说明

DumpAccChkPoint接口打印功能会对算子实际运行的性能带来一定影响，通常在调测阶段使用。开发者可以按需通过如下方式关闭打印功能。

自定义算子工程：

修改算子工程op\_kernel目录下的CMakeLists.txt文件，首行增加编译选项-DASCENDC\_DUMP=0，关闭ASCENDC\_DUMP开关。

Dump时，每个block核的dump信息前会增加对应信息头DumpHead（32字节大小），用于记录核号和资源使用信息。每次Dump的Tensor数据前也会添加信息头DumpTensorHead（32字节大小），用于记录Tensor的相关信息。如下图所示，展示了多核打印场景下的打印信息结构。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/wu7nAhgARRa9IsJjZxLbvQ/zh-cn_image_0000002589325657.png?HW-CC-KV=V1&HW-CC-Date=20260429T054126Z&HW-CC-Expire=86400&HW-CC-Sign=426774E9EBF49EF84C9A7D5A1414E997675AAF23893F7D5B64117014A8FDA482)

**DumpHead的具体信息如下。**

* block\_id：当前运行的核号。
* total\_block\_num：此次dump的核数。
* block\_remain\_len：当前核剩余可用的dump的空间。
* block\_initial\_space：当前核初始分配的dump空间。
* magic：内存校验魔术字。

**DumpTensorHead的具体信息如下。**

* desc：开发者自定义附加信息。
* addr：Tensor的地址。
* data\_type：Tensor的数据类型。
* position：表示Tensor所在的物理存储位置，当前仅支持Unified Buffer/L1 Buffer/L0C Buffer/Global Memory。

打印结果的样例如下。

```
1. DumpHead: block_id=0, total_block_num=16, block_remain_len=1048448, block_initial_space=1048576, magic=5aa5bccd
2. DumpTensor: desc=5, addr=0, data_type=DT_FLOAT16, position=UB
3. [40, 82, 60, 11, 24, 55, 52, 60, 31, 86, 53, 61, 47, 54, 34, 62, 84, 29, 48, 95, 16, 0, 20, 77, 3, 55, 69, 73, 75, 40, 35, 13]
4. DumpHead: block_id=1, total_block_num=16, block_remain_len=1048448, block_initial_space=1048576, magic=5aa5bccd
5. DumpTensor: desc=5, addr=0, data_type=DT_FLOAT16, position=UB
6. [58, 84, 22, 54, 41, 93, 1, 45, 50, 9, 72, 81, 23, 96, 86, 45, 36, 9, 36, 34, 78, 7, 2, 29, 47, 26, 13, 24, 27, 55, 90, 5]
7. ...
8. DumpHead: block_id=7, total_block_num=16, block_remain_len=1048448, block_initial_space=1048576, magic=5aa5bccd
9. DumpTensor: desc=5, addr=0, data_type=DT_FLOAT16, position=UB
10. [28, 27, 79, 39, 86, 5, 23, 97, 89, 5, 65, 69, 59, 13, 49, 2, 34, 6, 52, 38, 4, 90, 11, 11, 61, 50, 71, 98, 19, 54, 54, 99]
```

## 函数原型

```
1. void DumpAccChkPoint(const GlobalTensor<T>& tensor, uint32_t index, uint32_t countOff, uint32_t dumpSize)
2. void DumpAccChkPoint(const LocalTensor<T>& tensor, uint32_t index, uint32_t countOff, uint32_t dumpSize)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| tensor | 输入 | 需要dump的Tensor。  待dump的tensor位于Unified Buffer/L1 Buffer/L0C Buffer时使用LocalTensor类型的tensor参数输入。  待dump的tensor位于Global Memory时使用GlobalTensor类型的tensor参数输入。 |
| index | 输入 | 开发者自定义附加信息（行号或其他自定义数字）。 |
| dumpSize | 输入 | 需要dump的元素个数。 |
| countOff | 输入 | 偏移元素个数。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

* **该功能仅在如下场景支持：** 通过[工程化算子开发](cannkit-overview-of-engineering-operator.md)方式调用算子。
* 当前仅支持打印存储位置为Unified Buffer/L1 Buffer/L0C Buffer/Global Memory的Tensor信息。
* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* 待dump的元素总长度需要32Byte对齐。
* 偏移量需保证32字节对齐，即：偏移元素个数 \* sizeof（T）需按32B对齐。
* 程序中调用[printf](cannkit-commissioning-interfaces-printf.md)接口使用的空间+[assert](cannkit-commissioning-interfaces-assert.md)接口使用的空间+调用DumpTensor及DumpAccChkPoint接口使用的空间+框架dump功能所使用的空间，每个核上不可超过1M。请开发者自行控制待打印的内容数据量，超出则不会打印。

## 调用示例

```
1. AscendC::DumpAccChkPoint(srcLocal, 7, 32 , 128);
```
