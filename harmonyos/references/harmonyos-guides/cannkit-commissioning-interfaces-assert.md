---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-interfaces-assert
title: assert
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 调测接口 > assert
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c1a72e60b522f1ea9efbc6bd4e792e198a3c8b3c040f51cdeb66fafc7e505f5
---

## 函数功能

基于算子工程开发的算子，可以使用该接口实现CPU/NPU域assert断言功能。算子执行中，如果assert内部条件判断不为真，则输出assert条件并将输入的信息格式化打印在屏幕上。

在算子kernel侧实现代码中需要增加断言的地方使用assert检查代码，并格式化输出一些调测信息。示例如下。

```
1. int assertFlag = 10;

3. assert(assertFlag == 10);
4. assert(assertFlag == 10, "The assertFlag value is 10.\n");
5. assert(assertFlag == 10, "The assertFlag value is %d.\n", assertFlag);
```

说明

assert接口打印功能会对算子实际运行的性能带来一定影响（每一条assert，系统会额外增加一条逻辑判断，具体性能影响取决于代码中assert的使用数量），通常在调测阶段使用。开发者可以按需通过如下方式关闭打印功能。

自定义算子工程：

修改算子工程op\_kernel目录下的CMakeLists.txt文件，首行增加编译选项-DASCENDC\_DUMP=0，关闭ASCENDC\_DUMP开关。

在assert条件被触发时，在断言信息前面会自动打印CANN\_VERSION\_STR值与CANN\_TIMESTAMP值。其中，CANN\_VERSION\_STR与CANN\_TIMESTAMP为宏定义，CANN\_VERSION\_STR代表CANN软件包的版本号信息，形式为字符串，CANN\_TIMESTAMP为CANN软件包发布时的时间戳，形式为数值(uint64\_t)。开发者也可在代码中直接使用这两个宏。assert打印信息示例如下。

```
1. [ASSERT][CANN_VERSION : XXX.XX][TimeStamp : 20240807140556417] /home/.../add_custom.cpp:44: Assertion `assertFlag != 10' The assertFlag value is 10.
```

## 函数原型

```
1. assert(expr)
2. assert(expr, __gm__ const char *fmt, Args&&... args)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| expr | 输入 | assert断言是否终止程序的条件。为true则程序继续执行，为false则终止程序。 |
| fmt | 输入 | 格式控制字符串，包含两种类型的对象：普通字符和转换说明。  - 普通字符将原样不动地打印输出。  - 转换说明并不直接输出而是用于控制printf中参数的转换和打印。每个转换说明都由一个百分号字符（%）开始，以转换说明结束，从而说明输出数据的类型 。  - 支持的转换类型包括：  - %d / %i：输出十进制数  - %f：输出实数  - %x：输出十六进制整数  - %s：输出字符串  - %u：输出unsigned类型数据  - %p：输出指针地址    当前支持的数据类型为uint8\_t/int8\_t/int16\_t/uint16\_t/int32\_t/uint32\_t/int64\_t/uint64\_t/float/half。 |
| args | 输入 | 附加参数，个数和类型可变的输出列表：根据不同的fmt字符串，函数可能需要一系列的附加参数，每个参数包含了一个要被插入的值，替换了fmt参数中指定的每个%标签。参数的个数应与%标签的个数相同。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

* **该功能仅在如下场景支持：** 通过[工程化算子开发](cannkit-overview-of-engineering-operator.md)方式调用算子。
* kernel开发不要包含系统的assert.h，会导致宏定义冲突。
* assert接口调用形式与C语言一致，不需要使用AscendC命名空间。
* 本接口不支持打印除换行符之外的其他转义字符。
* 程序中调用assert接口使用空间+调用[printf](cannkit-commissioning-interfaces-printf.md)接口使用的空间+调用[DumpTensor](cannkit-commissioning-interfaces-dumptensor.md)接口使用的空间+[DumpAccChkPoint](cannkit-commissioning-interfaces-dumpaccch.md)接口使用的空间+框架dump功能所使用的空间，每个核上不可超过1M。请开发者自行控制待打印的内容数据量，超出则不会打印。
* 程序中只调用assert接口，assert接口使用空间每个核上不可超过1k。请开发者自行控制待打印的内容数据量，超出则不会打印。

## 调用示例

```
1. int assertFlag = 10;

3. // 断言条件
4. assert(assertFlag == 10);

6. // 打印消息
7. assert(assertFlag == 10, "The assertFlag value is 10.\n");

9. // 格式化打印
10. assert(assertFlag == 10, "The assertFlag value is %d.\n", assertFlag);
11. assert(assertFlag != 10, "The assertFlag value is %d.\n", assertFlag);
```

程序运行时会触发assert，打印效果如下。

```
1. [ASSERT][CANN_VERSION : XXX.XX][TimeStamp : 20240807140556417] /home/.../add_custom.cpp:44: Assertion `assertFlag != 10' The assertFlag value is 10.
```
