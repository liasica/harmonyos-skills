---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-function-printf
title: printf/PRINTF功能
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > 更多功能 > printf/PRINTF功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f350955e9641feb1f74569fa749a05ffd9f23bc48cc9ecbc593070eb13d1d629
---

## 功能介绍

使用工具进行算子调测时，支持printf/PRINTF功能，可以打印Scalar数据。

说明

* CPU调测场景支持printf和PRINTF打印，其中printf采用C++自身打印功能，不受dump-mode参数控制。
* simulator调测场景支持printf和PRINTF打印，受dump mode参数控制。
* 固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

## 使用方法（命令行）

1. 在核函数代码中按需在目标位置加上printf或PRINTF语句，接口说明参见表1，以PRINTF打印为例：

   ```
   1. PRINTF("1 fmt string d %d\n", 6666);
   2. PRINTF("1 fmt string lf %lf\n", float(61.556));
   ```
2. simulator调测场景执行如下命令，使能Dump开关。

   ```
   1. ascendebug kernel --backend simulator --dump-mode normal ... {其他simulator调测参数}
   ```

   --dump-mode取normal，开启通用打印Scalar模式，其他参数参考[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)按需配置。
3. 查看屏显打印结果，示例如下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/XBVZzxYVRjOb-UZlHMuA8Q/zh-cn_image_0000002552959250.png?HW-CC-KV=V1&HW-CC-Date=20260427T235129Z&HW-CC-Expire=86400&HW-CC-Sign=DB7373F19BD294B95E3D6543B8860296D4C6AF564BFDF5B084A73C572378246C)

## 接口说明

printf/PRINTF接口说明如下。

* **函数原型：** template <class... Args>

  + void printf(**gm** const char\* fmt, Args&&... args);
  + void PRINTF(**gm** const char\* fmt, Args&&... args);
* **函数功能：** 打印Scalar数据。
* **参数(IN)：**

  + **fmt：** 格式控制字符串，包含两种类型的对象：普通字符和转换说明。
    - 普通字符将原样不动地打印输出。
    - 转换说明并不直接输出而是用于控制printf中参数的转换和打印。每个转换说明都由一个百分号字符（%）开始，以转换说明结束，从而说明输出数据的类型 。支持的转换类型包括：
      * %d / %i：输出十进制数，支持打印的数据类型：bool/int8\_t/int16\_t/int32\_t/int64\_t
      * %f：输出实数，支持打印的数据类型：float/half/bfloat16\_t
      * %x：输出十六进制整数，支持打印的数据类型：int8\_t/int16\_t/int32\_t/int64\_t/uint8\_t/uint16\_t/uint32\_t/uint64\_t
      * %s：输出字符串
      * %u：输出unsigned类型数据，支持打印的数据类型：bool/uint8\_t/uint16\_t/uint32\_t/uint64\_t
      * %p：输出指针地址
  + **args：** 附加参数，个数和类型可变的输出列表：根据不同的fmt字符串，函数可能需要一系列的附加参数，每个参数包含了一个要被插入的值，替换了fmt参数中指定的每个%标签。参数的个数应与%标签的个数相同。
* **参数(OUT)：** NA
* **返回值：** NA
* **使用约束：**

  + 不支持转义字符打印。
  + 当前支持的打印类型：
    - %d / %i：输出十进制数。
    - %f：输出实数。
    - %x：输出十六进制整数。
    - %s：输出字符串。
    - %u：输出unsigned类型数据。
    - %p：输出指针地址。
* **调用示例：**

  ```
  1. // 整型打印：
  2. printf("fmt string %d", 0x123);
  3. PRINTF("fmt string %d", 0x123);
  4. // 指针打印：
  5. int *a;
  6. printf("TEST %p", a);
  7. PRINTF("TEST %p", a);
  ```
