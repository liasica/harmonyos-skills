---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-precision-conversion-instruction
title: 精度转换指令
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 矢量计算 > 精度转换指令
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:28+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:f736e239285fbb5b540b5c96739d4079dd18e314985368cdd401472295080f7d
---

## Cast

### 函数功能

根据源操作数和目的操作数Tensor的数据类型进行精度转换。

在了解精度转换规则之前，需要先了解浮点数的表示方式和二进制的舍入规则：

**浮点数的表示方式**：

* half共16bit，包括1bit符号位（S），5bit指数位（E）和10bit尾数位（M）。

  当E不全为0或不全为1时，表示的结果为：

  (-1)S \* 2E - 15 \* (1 + M)

  当E全为0时，表示的结果为：

  (-1)S \* 2-14 \* M

  当E全为1时，若M全为0，表示的结果为±inf（取决于符号位）；若M不全为0，表示的结果为nan。

  ![](https://media:401788444106734896)

  上图中S = 0，E = 15，M = 2-1 + 2-2，表示的结果为1.75。
* float共32bit，包括1bit符号位（S），8bit指数位（E）和23bit尾数位（M）。

  当E不全为0或不全为1时，表示的结果为：

  (-1)S \* 2E - 127 \* (1 + M)

  当E全为0时，表示的结果为：

  (-1)S \* 2-126 \* M

  当E全为1时，若M全为0，表示的结果为±inf（取决于符号位）；若M不全为0，表示的结果为nan。

  ![](https://media:401788444106759897)

  上图中S = 0，E = 127，M = 2-1 + 2-2，最终表示的结果为1.75 。
* bfloat16\_t共16bit，包括1bit符号位（S），8bit指数位（E）和7bit尾数位（M）。

  当E不全为0或不全为1时，表示的结果为：

  (-1)S \* 2E - 127 \* (1 + M)

  当E全为0时，表示的结果为：

  (-1)S \* 2-126 \* M

  当E全为1时，若M全为0，表示的结果为±inf（取决于符号位）；若M不全为0，表示的结果为nan。

  ![](https://media:401788444106781898)

  上图中S = 0，E = 127，M = 2-1 + 2-2，最终表示的结果为1.75。

**二进制的舍入规则和十进制类似，具体如下。**

![](https://media:401788444106807899)

* CAST\_RINT模式下，若待舍入部分的第一位为0，则不进位；若第一位为1且后续位不全为0，则进位；若第一位为1且后续位全为0，当M的最后一位为0则不进位，当M的最后一位为1则进位。
* CAST\_FLOOR模式下，若S为0，则不进位；若S为1，当待舍入部分全为0则不进位，否则，进位。
* CAST\_CEIL模式下，若S为1，则不进位；若S为0，当待舍入部分全为0则不进位；否则，进位。
* CAST\_ROUND模式下，若待舍入部分的第一位为0，则不进位；否则，进位。
* CAST\_TRUNC模式下，总是不进位。
* CAST\_ODD模式下，若待舍入部分全为0，则不进位；若待舍入部分不全为0，当M的最后一位为1则不进位，当M的最后一位为0则进位。

精度转换规则如下表所示：

**表1** 精度转换规则

| src类型 | dst类型 | 精度转换规则介绍 |
| --- | --- | --- |
| float | float | 将src按照round\_mode（精度转换处理模式，参见[参数说明](cannkit-precision-conversion-instruction.md#参数说明)中的round\_mode参数）取整，仍以float格式存入dst中。  示例：输入0.5，  CAST\_RINT模式输出0.0，CAST\_FLOOR模式输出0.0，CAST\_CEIL模式输出1.0，CAST\_ROUND模式输出1.0，CAST\_TRUNC模式输出0.0。 |
| float | half | 将src按照round\_mode取到half所能表示的数，以half格式（溢出默认按照饱和处理）存入dst中。  示例：输入0.5 + 2-12，写成float的表示形式：2-1 \* (1 + 2-11)，因此E = -1 + 127 = 126，M = 2-11。    half的指数位可以表示出2-1，E = -1 + 15 = 14，但half只有10 bit尾数位，因此灰色部分要进行舍入。  CAST\_RINT模式舍入得尾数0000000000，E = 14，M = 0，最终表示的结果为0.5。  CAST\_FLOOR模式舍入得尾数0000000000，E = 14，M = 0，最终表示的结果为0.5。  CAST\_CEIL模式舍入得尾数0000000001，E = 14，M = 2-10，最终表示的结果为0.5 + 2-11。  CAST\_ROUND模式舍入得尾数0000000001，E = 14，M = 2-10，最终表示的结果为0.5 + 2-11。  CAST\_TRUNC模式舍入得尾数0000000000，E = 14，M = 0，最终表示的结果为0.5。  CAST\_ODD模式舍入得尾数0000000001，E = 14，M = 2-10，最终表示的结果为0.5 + 2-11 。 |
| float | int64\_t | 将src按照round\_mode取整，以int64\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入222 + 0.5，  CAST\_RINT模式输出222，CAST\_FLOOR模式输出222，CAST\_CEIL模式输出222 + 1，CAST\_ROUND模式输出222 + 1，CAST\_TRUNC模式输出222。 |
| float | int32\_t | 将src按照round\_mode取整，以int32\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入222 + 0.5，  CAST\_RINT模式输出222，CAST\_FLOOR模式输出222 ，CAST\_CEIL模式输出222 + 1，CAST\_ROUND模式输出222 + 1，CAST\_TRUNC模式输出222。 |
| float | int16\_t | 将src按照round\_mode取整，以int16\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入222 + 0.5，  CAST\_RINT模式输出215 - 1（溢出处理），CAST\_FLOOR模式输出215 - 1（溢出处理），CAST\_CEIL模式输出215 - 1（溢出处理），CAST\_ROUND模式输出215 - 1（溢出处理），CAST\_TRUNC模式输出215 - 1（溢出处理）。 |
| float | bfloat16\_t | 将src按照round\_mode取到bfloat16\_t所能表示的数，以bfloat16\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入0.5+ 2-9 + 2-11 , 写成float的表示形式：2-1 \* (1 + 2-8 + 2-10)，因此E = -1 + 127 = 126，M = 2-8 + 2-10 。    bfloat16\_t的指数位位数和float的相同，有E = 126，但bfloat16\_t只有7bit尾数位，因此灰色部分要进行舍入。  CAST\_RINT模式舍入得尾数0000001，E = 126，M = 2-7，最终表示的结果为0.5 + 2-8。  CAST\_FLOOR模式舍入得尾数0000000，E = 126，M = 0，最终表示的结果为0.5。  CAST\_CEIL模式舍入得尾数0000001，E = 126，M = 2-7，最终表示的结果为0.5 + 2-8。  CAST\_ROUND模式舍入得尾数0000001，E = 126，M = 2-7，最终表示的结果为0.5 + 2-8。  CAST\_TRUNC模式舍入得尾数0000000，E = 126，M = 0，最终表示的结果为0.5。 |
| half | float | 将src以float格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入1.5 - 2-10，输出1.5 - 2-10。 |
| half | int32\_t | 将src按照round\_mode取整，以int32\_t格式存入dst中。  示例：输入-1.5，  CAST\_RINT模式输出-2，CAST\_FLOOR模式输出-2，CAST\_CEIL模式输出-1，CAST\_ROUND模式输出-2，CAST\_TRUNC模式输出-1。 |
| half | int16\_t | 将src按照round\_mode取整，以int16\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入27 - 0.5，  CAST\_RINT模式输出27，CAST\_FLOOR模式输出27 - 1，CAST\_CEIL模式输出27，CAST\_ROUND模式输出27，CAST\_TRUNC模式输出27 - 1。 |
| half | int8\_t | 将src按照round\_mode取整，以int8\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入27 - 0.5，  CAST\_RINT模式输出27 - 1（溢出处理），CAST\_FLOOR模式输出27 - 1，CAST\_CEIL模式输出27 - 1（溢出处理），CAST\_ROUND模式输出27 - 1（溢出处理），CAST\_TRUNC模式输出27 - 1。 |
| half | uint8\_t | 将src按照round\_mode取整，以uint8\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入1.75，  CAST\_RINT模式输出2，CAST\_FLOOR模式输出1，CAST\_CEIL模式输出2，CAST\_ROUND模式输出2，CAST\_TRUNC模式输出1。 |
| half | int4b\_t | 将src按照round\_mode取整，以int4b\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入1.5，  CAST\_RINT模式输出2，CAST\_FLOOR模式输出1，CAST\_CEIL模式输出2，CAST\_ROUND模式输出2，CAST\_TRUNC模式输出1。 |
| bfloat16\_t | float | 将src以float格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入1.5 - 2-6，输出1.5 - 2-6。 |
| bfloat16\_t | int32\_t | 将src按照round\_mode取整，以int32\_t格式（溢出默认按照饱和处理）存入dst中。  示例：输入26 + 0.5  CAST\_RINT模式输出26，CAST\_FLOOR模式输出26 ，CAST\_CEIL模式输出26 + 1，CAST\_ROUND模式输出26 + 1，CAST\_TRUNC模式输出26。 |
| int4b\_t | half | 将src以half格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入1，输出1.0。 |
| uint8\_t | half | 将src以half格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入1，输出1.0。 |
| int8\_t | half | 将src以half格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入-1，输出-1.0。 |
| int16\_t | half | 将src按照round\_mode取到half所能表示的数，以half格式存入dst中。  示例：输入212 + 2，写成half的表示形式：212 \* (1 + 2-11)，要求E = 12 + 15 = 27，M = 2-11：    由于half只有10bit尾数位，因此灰色部分要进行舍入。  CAST\_RINT模式舍入得尾数0000000000，E = 27，M = 0，最终表示的结果为212。  CAST\_FLOOR模式舍入得尾数0000000000，E = 27，M = 0，最终表示的结果为212。  CAST\_CEIL模式舍入得尾数0000000001，E = 27，M = 2-10，最终表示的结果为212 + 4。  CAST\_ROUND模式舍入得尾数0000000001，E = 27，M = 2-10，最终表示的结果为212 + 4。  CAST\_TRUNC模式舍入得尾数0000000000，E = 27，M = 0，最终表示的结果为212。 |
| int16\_t | float | 将src以float格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入215 - 1，输出215 - 1。 |
| int32\_t | float | 将src按照round\_mode取到float所能表示的数，以float格式存入dst中。  示例：输入225 + 3，写成float的表示形式：225 \* (1 + 2-24 + 2-25)，要求E = 25 + 127 = 152， M = 2-24 + 2-25。    由于float只有23bit尾数位，因此灰色部分要进行舍入。  CAST\_RINT模式舍入得尾数00000000000000000000001，E = 152，M = 2-23，最终表示的结果为225 + 4。  CAST\_FLOOR模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225。  CAST\_CEIL模式舍入得尾数00000000000000000000001，E = 152，M = 2-23，最终表示的结果为225 + 4。  CAST\_ROUND模式舍入得尾数00000000000000000000001，E = 152，M = 2-23，最终表示的结果为225 + 4。  CAST\_TRUNC模式舍入得尾数00000000000000000000000，E = 152，M = 0，最终表示的结果为225 。 |
| int32\_t | int64\_t | 将src以int64\_t格式存入dst中，不存在精度转换问题，无舍入模式。  示例：输入231 - 1，输出231 - 1。 |
| int32\_t | int16\_t | 将src以int16\_t格式（溢出默认按照饱和处理）存入dst中，不存在精度转换问题，无舍入模式。  示例：输入231 - 1，输出215 - 1。 |
| int64\_t | int32\_t | 将src以int32\_t格式（溢出默认按照饱和处理）存入dst中，不存在精度转换问题，无舍入模式。  示例：输入231，输出231 - 1。 |
| int64\_t | float | 将src按照round\_mode取到float所能表示的数，以float格式存入dst中。  示例：输入235 + 212 + 211，写成float的表示形式：235 \* (1 + 2-23 + 2-24)，要求E = 35 + 127 = 162，M = 2-23 + 2-24。    由于float只有23bit尾数位，因此灰色部分要进行舍入。  CAST\_RINT模式舍入得尾数00000000000000000000010，E = 162，M = 2-22，最终表示的结果为235 + 213。  CAST\_FLOOR模式舍入得尾数00000000000000000000001，E = 162，M = 2-23，最终表示的结果为225 + 212。  CAST\_CEIL模式舍入得尾数00000000000000000000010，E = 162，M = 2-22，最终表示的结果为225 + 213。  CAST\_ROUND模式舍入得尾数00000000000000000000010，E = 162，M = 2-22，最终表示的结果为225 + 213。  CAST\_TRUNC模式舍入得尾数00000000000000000000001，E = 162，M = 2-23，最终表示的结果为225 + 212。 |

### 函数原型

tensor前n个数据计算：

```cpp
template <typename T1, typename T2> 
  __aicore__ inline void Cast(const LocalTensor<T1>& dstLocal, const LocalTensor<T2>& srcLocal, const RoundMode& round_mode, const uint32_t calCount)
```

### 参数说明

**表2** 模板参数说明

| 参数名 | 描述 |
| --- | --- |
| T1 | 目的操作数数据类型。  - Kirin9020支持的数据类型见表4。  - Kirin9030支持的数据类型见表4。  - KirinX90支持的数据类型见表4。 |
| T2 | 源操作数数据类型。  - Kirin9020支持的数据类型见表4。  - Kirin9030支持的数据类型见表4。  - KirinX90支持的数据类型见表4。 |

**表3** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dstLocal | 输出 | 目的操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。 |
| srcLocal | 输入 | 源操作数。  类型为[LocalTensor](cannkit-localtensor.md)，支持的TPosition为VECIN、VECCALC、VECOUT。  LocalTensor的起始地址需要32字节对齐。 |
| round\_mode | 输入 | 精度转换处理模式，类型是RoundMode。  RoundMode为枚举类型，用以控制精度转换处理模式，具体取值为：CAST\_NONE、CAST\_RINT、CAST\_FLOOR、CAST\_CEIL、CAST\_ROUND、CAST\_TRUNC、CAST\_ODD。  CAST\_ROUND表示反向0取整，远离0，对正数x.y变成(x + 1)，对负数-x.y，变成-(x + 1)。 |
| calCount | 输入 | 输入数据元素个数。 |

**表4** Kirin系列产品Cast指令参数说明

| src数据类型 | dst数据类型 | 支持的roundMode |
| --- | --- | --- |
| float | half | 溢出部分按饱和处理。CAST\_RINT/CAST\_ODD/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC/CAST\_NONE |
| float | int16\_t | 溢出部分按饱和处理。  CAST\_RINT/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC |
| float | int32\_t | 溢出部分按饱和处理。  CAST\_RINT/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC/CAST\_NONE |
| float | float | CAST\_RINT/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC |
| half | int8\_t/uint8\_t | 溢出部分按饱和处理。  CAST\_RINT/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC/CAST\_NONE |
| half | int32\_t | CAST\_RINT/CAST\_ROUND/CAST\_FLOOR/CAST\_CEIL/CAST\_TRUNC |
| half | float | CAST\_NONE |
| half | int16\_t | CAST\_RINT |
| int16\_t | half/float | CAST\_NONE |
| int32\_t | float | CAST\_NONE |
| int32\_t | int16\_t | 溢出部分按饱和处理。CAST\_NONE |
| uint8\_t | half | CAST\_NONE |
| int8\_t | half | CAST\_NONE |

### 返回值

无

### 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

### 注意事项

* 操作数地址偏移对齐要求请参见[通用约束](cannkit-general-constraints.md)。
* dst与src的应为不同Tensor，或同一Tensor的同一元素，不支持同一Tensor的不同元素。
* src为float，dst为float时，取整模式表示向整数取整（仍为float类型），其他情况表示向dst数据类型所能表示的数字取整。

### 调用示例

本样例中只展示Compute流程中的部分代码。本样例的srcLocal为half类型，dstLocal为int32\_t类型，计算mask时以int32\_t为准。

如果开发者需要运行样例代码，请将该代码段拷贝并替换样例模板中Compute函数的部分代码即可。

tensor前n个数据计算样例：

```cpp
AscendC::Cast(dstLocal, srcLocal, AscendC::RoundMode::CAST_CEIL, 512);
```

结果示例如下。

```text
输入数据(srcLocal):
[29.5    83.6    16.75   45.1    40.62   69.06   47.6    96.5    72.7
 57.56   61.25   69.7    29.27   91.2    70.1    14.484   9.625  21.58
  9.336   3.125  63.72    9.9    17.28   73.2    75.7    29.81   98.8
 99.06   72.94    3.785  24.94   25.56   39.1    58.94   39.6    78.4
  5.43   25.48    9.58   60.8    77.56   29.7    70.3     6.312   4.047
 87.1    81.6    76.56   59.28   55.66   81.75   73.56   76.9    54.38
  7.254  37.84   11.08   77.6    83.6    89.2    93.06    2.96   76.56
 62.16   76.25   95.44   86.6    86.75   29.83   82.2    55.03   64.9
 56.44   12.89   87.06   39.34   72.25   43.06   63.4    51.72   63.9
  0.703  47.84   27.73   99.     89.     97.3     1.277  58.44   14.05
 78.9    98.5    28.55   44.8    41.03   40.75   74.2    74.06   10.51
 69.2    25.83   35.8    85.5    25.12   82.25   95.3    36.75   55.88
 90.9    57.47    7.13   18.1    40.97   31.     99.3    69.4    72.94
 62.44   63.7    80.     37.94   11.11   37.     39.72   87.94   31.72
 25.7    54.7    32.8    21.64   14.53   55.1     3.607  40.16   77.7
 15.15   77.44   43.25   85.75   67.3    30.33   67.56   60.72   58.16
 19.84   89.2    18.75   55.56   31.61    9.445   6.5    27.95   48.5
 37.16    7.805  37.72   69.6    36.2    92.56   24.72   41.56   48.44
 19.27   25.94   25.      8.836  55.75   77.8    25.84   46.16   71.7
 63.62   33.28    3.719  55.22   45.97   35.8    27.86   42.22    3.078
 92.06    0.805  51.97   76.4    32.03   74.56   28.1    91.2    35.38
  0.2009 74.25   87.5    92.75   76.25   51.28   22.9    34.4    28.23
 87.5    78.75   63.1    61.56   79.94    6.766  95.1    55.     56.75
 39.66   94.75   24.19   29.83   72.6    99.9    12.43   46.56   51.9
 92.3    42.66   91.8    95.8    35.2    13.08   60.7    22.22    6.055
  2.23   13.875  71.3    99.56   91.94   92.     96.06   97.5    68.75
  8.61    1.157  68.2    20.73   63.44   90.     38.78   64.4    88.9
 20.75   14.03   97.06   66.8    57.9    86.94   28.5     0.2279 51.8
 84.56   39.53   93.     15.66   15.23   71.75   11.44   45.28   57.38
 82.5    88.7     9.74   90.4    61.56   68.56   11.22   69.3    40.28
 24.78   84.44   23.92    8.4    20.88   48.2    17.42   59.84   93.2
  2.191  95.94   93.06   54.53   76.5    37.     41.7    82.7    69.5
 92.6     5.8    32.78   84.56   26.5    96.56    0.858  96.44   52.8
 90.9    30.52    2.656  32.03   35.72    8.125  21.94   84.5    66.7
 96.75   46.8     1.42   58.3    28.75   44.94   66.2    28.67   11.695
 41.75   67.25   26.75   17.72   35.9     5.72   55.88   94.7    80.8
 71.     86.06   36.78   81.06   56.8    61.34   11.42   74.     32.16
 14.695  78.6    56.1    64.4    61.75   50.88   39.6    79.94   71.25
 40.7     5.99   67.4    62.28   89.25   12.02   63.12   33.1    59.06
 28.2    19.22   59.66   51.6    53.28   97.8    42.25   82.     39.7
 50.6    95.06   20.64   26.62   54.9    55.     28.44   26.25   46.56
 87.06   98.44   49.34   37.2    97.4    34.3    83.4    57.4    94.
 29.31   79.44   19.72   54.9    50.25   58.75   92.5    17.3    17.88
 44.7     6.047  50.78   75.3    21.66   71.5    97.75   35.8    93.6
  4.367  31.02   66.5    48.25   34.     92.7    36.97   86.5    10.37
 82.     29.39   10.63   40.72   72.5    31.56   96.5    70.44    6.074
 37.34    7.58   21.72   44.97   77.6    14.22   18.62   47.97   54.6
 99.56   81.7    35.75   44.22   28.64   91.56    1.005  44.      8.125
 11.7    93.6    70.25   63.94   11.05   50.97   56.47   39.4    35.53
 84.     10.21   42.66   62.12   87.7    71.25   87.75   56.03   60.88
 31.81   68.1    91.1    67.3    53.6    96.06   43.75   27.86   46.6
 87.7    29.47    2.174  88.4    49.53   63.53   84.9    91.75   48.53
 91.94   88.44   58.3    88.44   23.11   91.56   71.4    59.66   93.44
 28.56   93.3    59.94   90.     18.95   52.8    70.3    58.     21.47
 93.7    45.03   84.25   34.06   23.86   38.4     5.566  41.5    35.1
 34.8    32.8    81.44   74.75   95.9    23.56    3.562  48.72   92.7
 43.88   83.75   69.06   85.8    22.84   63.78   90.94   52.78  ]
输出数据(dstLocal):
[ 30  84  17  46  41  70  48  97  73  58  62  70  30  92  71  15  10  22
  10   4  64  10  18  74  76  30  99 100  73   4  25  26  40  59  40  79
   6  26  10  61  78  30  71   7   5  88  82  77  60  56  82  74  77  55
   8  38  12  78  84  90  94   3  77  63  77  96  87  87  30  83  56  65
  57  13  88  40  73  44  64  52  64   1  48  28  99  89  98   2  59  15
  79  99  29  45  42  41  75  75  11  70  26  36  86  26  83  96  37  56
  91  58   8  19  41  31 100  70  73  63  64  80  38  12  37  40  88  32
  26  55  33  22  15  56   4  41  78  16  78  44  86  68  31  68  61  59
  20  90  19  56  32  10   7  28  49  38   8  38  70  37  93  25  42  49
  20  26  25   9  56  78  26  47  72  64  34   4  56  46  36  28  43   4
  93   1  52  77  33  75  29  92  36   1  75  88  93  77  52  23  35  29
  88  79  64  62  80   7  96  55  57  40  95  25  30  73 100  13  47  52
  93  43  92  96  36  14  61  23   7   3  14  72 100  92  92  97  98  69
   9   2  69  21  64  90  39  65  89  21  15  98  67  58  87  29   1  52
  85  40  93  16  16  72  12  46  58  83  89  10  91  62  69  12  70  41
  25  85  24   9  21  49  18  60  94   3  96  94  55  77  37  42  83  70
  93   6  33  85  27  97   1  97  53  91  31   3  33  36   9  22  85  67
  97  47   2  59  29  45  67  29  12  42  68  27  18  36   6  56  95  81
  71  87  37  82  57  62  12  74  33  15  79  57  65  62  51  40  80  72
  41   6  68  63  90  13  64  34  60  29  20  60  52  54  98  43  82  40
  51  96  21  27  55  55  29  27  47  88  99  50  38  98  35  84  58  94
  30  80  20  55  51  59  93  18  18  45   7  51  76  22  72  98  36  94
   5  32  67  49  34  93  37  87  11  82  30  11  41  73  32  97  71   7
  38   8  22  45  78  15  19  48  55 100  82  36  45  29  92   2  44   9
  12  94  71  64  12  51  57  40  36  84  11  43  63  88  72  88  57  61
  32  69  92  68  54  97  44  28  47  88  30   3  89  50  64  85  92  49
  92  89  59  89  24  92  72  60  94  29  94  60  90  19  53  71  58  22
  94  46  85  35  24  39   6  42  36  35  33  82  75  96  24   4  49  93
  44  84  70  86  23  64  91  53]
```

### 样例模板

为了方便开发者快速运行指令中的参考样例，本章节提供样例模板。

开发者可以将以下样例模板作为代码框架，只需将具体指令中的样例片段拷贝替换下文代码段中的加粗内容即可。

```cpp
#include "kernel_operator.h"
class KernelCast {
public:
    __aicore__ inline KernelCast() {}
    __aicore__ inline void Init(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
    {
        srcGlobal.SetGlobalBuffer((__gm__ half*)srcGm);
        dstGlobal.SetGlobalBuffer((__gm__ int32_t*)dstGm);
        pipe.InitBuffer(inQueueSrc, 1, 512 * sizeof(half));
        pipe.InitBuffer(outQueueDst, 1, 512 * sizeof(int32_t));
    }
    __aicore__ inline void Process()
    {
        CopyIn();
        Compute();
        CopyOut();
    }
private:
    __aicore__ inline void CopyIn()
    {
        AscendC::LocalTensor<half> srcLocal = inQueueSrc.AllocTensor<half>();
        AscendC::DataCopy(srcLocal, srcGlobal, 512);
        inQueueSrc.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<half> srcLocal = inQueueSrc.DeQue<half>();
        AscendC::LocalTensor<int32_t> dstLocal = outQueueDst.AllocTensor<int32_t>();
  
        **AscendC::Cast(dstLocal, srcLocal, AscendC::RoundMode::CAST_CEIL, 512);**
  
        outQueueDst.EnQue<int32_t>(dstLocal);
        inQueueSrc.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<int32_t> dstLocal = outQueueDst.DeQue<int32_t>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<half> srcGlobal;
    AscendC::GlobalTensor<int32_t> dstGlobal;
};
extern "C" __global__ __aicore__ void cast_simple_kernel(__gm__ uint8_t* srcGm, __gm__ uint8_t* dstGm)
{
    KernelCast op;
    op.Init(srcGm, dstGm);
    op.Process();
}
```
