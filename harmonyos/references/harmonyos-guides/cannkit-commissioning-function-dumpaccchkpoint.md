---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-function-dumpaccchkpoint
title: DumpAccChkPoint功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > 更多功能 > DumpAccChkPoint功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0850970f183fe1cb8dc5a2b37d63b45a1abdcd0dd3bcc58fe47da836622e820
---

## 功能介绍

使用工具进行算子调测时，支持指定偏移位置的Tensor打印。**该功能与**[DumpTensor功能](cannkit-commissioning-function-dumptensor.md)**类似**，其使用更加灵活。

当Tensor数据较大时，可通过DumpAccChkPoint指定偏移位置，截取指定长度的元素值打印。

说明

* simulator调测场景下的Dump偏移位置Tensor，受dump mode参数控制。
* 固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

## 使用方法（命令行）

1. 在核函数代码中按需在需要打印Tensor偏移数据的地方调用DumpAccChkPoint接口，详情请参见接口说明，样例如下。

   ```
   1. DumpAccChkPoint(srcLocal, 5, 32, dataLen);
   ```
2. simulator调测场景执行如下命令，使能Dump开关。

   ```
   1. ascendebug kernel --backend simulator --dump-mode acc_chk ... {其他simulator调测参数}
   ```

   --dump-mode取acc\_chk，开启偏移位置打印Tensor模式，其他参数参考[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)按需配置。
3. 查看dump结果。

   Dump偏移位置Tensor数据存放在${root}/${work\_dir}/npu路径下，其目录结构、结果说明与[DumpTensor功能](cannkit-commissioning-function-dumptensor.md)类似。

## 接口说明

DumpAccChkPoint接口说明如下。

* **函数原型：**

  + void DumpAccChkPoint(const LocalTensor<T> &tensor, uint32\_t desc, uint32\_t offset, uint32\_t dumpNum)
  + void DumpAccChkPoint(const GlobalTensor<T> &tensor, uint32\_t desc, uint32\_t offset, uint32\_t dumpNum)
* **函数功能：** 支持指定偏移位置的Tensor打印。
* **参数(IN)：**

  + **tensor：** 开发者需要Dump的Tensor。多个DumpTensor调用时，不可重复。
    - 待dump的Tensor位于Unified Buffer/L1 Buffer/L0C Buffer时使用LocalTensor类型的Tensor参数输入。
    - 待dump的Tensor位于Global Memory时使用GlobalTensor类型的Tensor参数输入。
    - 当前支持的数据类型为uint8\_t、int8\_t、int16\_t、uint16\_t、int32\_t、uint32\_t、float、half。
  + **desc：** 开发者自定义附加信息（行号或其他自定义数字）。
  + **offset：** 偏移元素个数。
  + **dumpNum：** 需要Dump的元素个数。
* **参数(OUT)：** NA
* **返回值：** NA
* **使用约束：**

  + 当前接口仅支持位于Unified Buffer/L1 Buffer/L0C Buffer/Global Memory的数据Dump。
  + 偏移量需符合UB读取数据32B对齐的限制，即offset\*sizeof(T)需按32B对齐。
  + 每次Dump的大小(dataNum\*sizeof(T))需要32B对齐。
* **调用示例：**

  ```
  1. DumpAccChkPoint(srcLocal, 7, 32 , 128);
  ```
