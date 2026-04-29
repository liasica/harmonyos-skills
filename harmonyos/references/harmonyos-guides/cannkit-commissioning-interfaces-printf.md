---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-interfaces-printf
title: printf
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > printf
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a7b3b22ba7aab7f7ecc0b4c8b7519c568cf9aebff3d9fc53f4682268fcb55c8
---

## 函数功能

基于算子工程开发的算子，可以使用该接口实现CPU侧/NPU侧调试场景下的格式化输出功能。

在算子kernel侧实现代码中需要输出日志信息的地方调用printf接口打印相关内容。样例如下。

```
1. #include "kernel_operator.h"
2. AscendC::printf("fmt string %d\n", 0x123);
3. AscendC::PRINTF("fmt string %d\n", 0x123);
```

说明

printf(PRINTF)接口打印功能会对算子实际运行的性能带来一定影响，通常在调测阶段使用。开发者可以按需通过如下方式关闭打印功能。

自定义算子工程：

修改算子工程op\_kernel目录下的CMakeLists.txt文件，首行增加编译选项-DASCENDC\_DUMP=0，关闭ASCENDC\_DUMP开关。

**需要注意的是，关闭CPU侧的打印开关时，只对PRINTF接口生效，对printf不生效。**

printf打印结果示例如下。

```
1. fmt string 291
2. fmt string 291
```

根据算子执行方式的不同，printf的打印结果输出方式不同。动态图或者单算子直调场景下，待输出内容会被解析并打印在屏幕上。静态图场景下，整图算子需要全下沉到NPU侧执行，无法直接调用接口打印出单个算子的信息，因此需要在模型执行完毕后，将待输出内容落盘在dump文件中，dump文件需要通过工具解析为可读内容。

## 函数原型

```
1. void printf(__gm__ const char* fmt, Args&&... args)
2. void PRINTF(__gm__ const char* fmt, Args&&... args)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| fmt | 输入 | 格式控制字符串，包含两种类型的对象：普通字符和转换说明。  - 普通字符将原样不动地打印输出。  - 转换说明并不直接输出而是用于控制printf中参数的转换和打印。每个转换说明都由一个百分号字符（%）开始，以转换说明结束，从而说明输出数据的类型 。  支持的转换类型包括：  - %d / %i：输出十进制数，支持打印的数据类型：bool/int8\_t/int16\_t/int32\_t/int64\_t  - %f：输出实数，支持打印的数据类型：float/half/bfloat16\_t  - %x：输出十六进制整数，支持打印的数据类型：int8\_t/int16\_t/int32\_t/int64\_t/uint8\_t/uint16\_t/uint32\_t/uint64\_t  - %s：输出字符串  - %u：输出unsigned类型数据，支持打印的数据类型：bool/uint8\_t/uint16\_t/uint32\_t/uint64\_t  - %p：输出指针地址 |
| args | 输入 | 附加参数，个数和类型可变的输出列表：根据不同的fmt字符串，函数可能需要一系列的附加参数，每个参数包含了一个要被插入的值，替换了fmt参数中指定的每个%标签。参数的个数应与%标签的个数相同。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

* 本接口不支持打印除换行符之外的其他转义字符。
* 如果开发者需要包含标准库头文件stdio.h和cstdio，请在kernel\_operator.h头文件之前包含，避免printf符号冲突。
* 程序中调用printf/PRINTF接口使用的空间+调用[DumpTensor](cannkit-commissioning-interfaces-dumptensor.md)接口使用的空间+[DumpAccChkPoint](cannkit-commissioning-interfaces-dumpaccch.md)接口使用的空间+[assert](cannkit-commissioning-interfaces-assert.md)接口使用的空间+框架dump功能所使用的空间，每个核上不可超过1M。请开发者自行控制待打印的内容数据量，超出则不会打印。

## 调用示例

```
1. #include "kernel_operator.h"

3. // 整型打印：
4. AscendC::printf("fmt string %d\n", 0x123);
5. AscendC::PRINTF("fmt string %d\n", 0x123);

7. // 浮点型打印：
8. float a = 3.14;
9. AscendC::printf("fmt string %f\n", a);
10. AscendC::PRINTF("fmt string %f\n", a);

12. // 指针打印：
13. int *a;
14. AscendC::printf("TEST %p\n", a);
15. AscendC::PRINTF("TEST %p\n", a);
```

程序运行时打印效果如下。

```
1. fmt string 291
2. fmt string 291
3. TEST 0x12c08001a000
4. TEST 0x12c08001a000
```
