---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-undefined-behavior-fault-mode
title: 未定义异常访问故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 地址越界故障模式说明 > 未定义异常访问故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:c4795881d9fad2fcfdb7ef64d973a0535d77fe1324bad2c4123dd45cd61a7cbe
---

在程序运行过程中，部分操作虽然能够通过编译，但由于违反程序语言标准规定的行为约束，可能导致未定义行为。此类问题通常来源于程序对内存访问、数据运算以及类型转换规则的不正确使用。未定义行为发生后，程序执行结果不可预测，可能导致数据异常、程序崩溃或安全风险。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)（Undefined Behavior Sanitizer）检测能力后，系统可以在运行阶段对应用潜在的未定义行为进行检查，输出异常位置及具体原因，以辅助开发人员定位和修复问题。本文结合典型案例，介绍此类问题的日志特征与定位方法，具体包括：

* [变量指针未对齐访问](bpta-stability-undefined-behavior-fault-mode.md#section170195312394)
* [成员指针未对齐访问](bpta-stability-undefined-behavior-fault-mode.md#section22150364404)
* [数据类型转换异常](bpta-stability-undefined-behavior-fault-mode.md#section6602194144013)
* [整数溢出操作](bpta-stability-undefined-behavior-fault-mode.md#section1081712151410)
* [浮点数转换溢出](bpta-stability-undefined-behavior-fault-mode.md#section1299819239416)
* [除零操作](bpta-stability-undefined-behavior-fault-mode.md#section19102152994111)

## 变量指针未对齐访问

### 根因描述

程序在指针类型转换或地址偏移过程中，程序未保证转换后或偏移后的地址满足目标类型的对齐规则，导致后续访问数据时触发异常。由于不同数据类型具有不同的内存对齐要求，非法构造的指针可能导致处理器无法正确访问目标数据。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，应用运行时会对指针访问地址进行对齐检查，并报告该类未定义行为。

### 问题分析思路

变量指针未对齐访问通常由以下几种原因引起：

1. 指针地址偏移导致未对齐。
2. 手动计算变量地址错误导致未对齐。
3. 指针递增操作导致地址未对齐。
4. 使用非标准方式获取变量地址导致未对齐。

问题分析步骤如下：

1. 查看UBSan日志中的报错关键字段，确认故障类型，通过store/load to misaligned address关键字，初步判定该问题属指针未对齐异常。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。根据具体代码分析异常指针来源：是否存在指针偏移；是否存在错误类型转换；是否存在手动地址计算或内存管理。

### 关键字

关注故障日志中是否包含以下关键字：store/load to misaligned address。

### 案例分析

**案例：**不同类型之间错误转换

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据：日志中明确给出异常类型为store to misaligned address，表示程序向未满足对齐要求的地址写入数据。

   ```screen
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:75:5: runtime error: store to misaligned address 0x005ac0c94201 for type 'int32_t' (aka 'int'), which requires 4 byte alignment
   0x005ac0c94201: note: pointer points here
   00 00 00  00 00 00 00 00 00 00 00  b9 27 e0 66 81 d5 f9 4c  16 61 62 69 6c 69 74 79  4e 61 6d 65 00
   ^
   #0 0x5bc891245c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa1245c) (BuildId: e334d0e3b1e503fc1ab1d26b99c1c99b8f842133)
   #1 0x5aa4c8fad0  (/system/lib64/platformsdk/libace_napi.z.so+0x4fad0) (BuildId: 69af531e347ee63c838c4f14d23380da)
   #2 0x7e0f6fd8b8  (/system/lib64/module/arkcompiler/stub.an+0xe948b8)
   #3 0x7e0eceedc0  (/system/lib64/module/arkcompiler/stub.an+0x485dc0)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:75:5 in
   ==com.example.dfx_test==25143==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈获取详细代码位置。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/4fsfZNWBQvWgSTTyzQO-8A/zh-cn_image_0000002699892014.png)

   ubsanTest.cpp第75行代码触发异常，结合代码确认为执行\*pointer=42时触发的异常。对异常代码逐行解析如下：

   1. 代码第73行：buffer指针被强转为int8\_t\*类型。
   2. 代码第74行：buffer的类型为int8\_t\*，即buffer+1会向后移动1个int8\_t的大小（1字节）。而后又使用reinterpret\_cast强转为int32\_t\*类型，但reinterpret\_cast仅改变指针类型解释，不修正地址对齐问题，因此pointer指向了一个未对齐的地址。
   3. 代码第75行：代码尝试向未对齐的地址写入一个int32\_t值（4 字节），UBSan检测到该存储操作的目标地址不符合int32\_t的对齐规则，从而触发store to misaligned address错误。

**问题结论与总结**

变量指针未对齐访问是指程序在使用指针访问数据时，指针中保存的地址不满足目标数据类型的内存对齐要求，导致通过该指针进行读写操作时触发未定义行为。

**修复建议**

在进行对象访问或指针类型转换时，应确保内存地址满足目标类型的对齐要求，避免将未对齐的内存地址直接转换为对象指针并访问成员。对于原始内存数据解析场景，应采用安全的数据拷贝方式（如 memcpy()）将数据复制到满足对齐要求的对象中，再进行访问。

## 成员指针未对齐访问

### 根因描述

程序通过地址偏移或错误类型转换生成结构体指针，但未保证该指针地址满足结构体及其成员类型的内存对齐要求，导致后续通过该结构体指针访问成员时，产生未对齐成员访问，引发未定义行为。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，可在结构体成员访问阶段发现该类非法对齐访问并报告异常。

### 问题分析思路

成员指针未对齐访问通常由以下几种原因引起：

1. 结构体指针地址经过偏移后使用。
2. 手动计算地址生成结构体指针。
3. 动态内存地址经过二次偏移后作为结构体地址。
4. 将非结构体存储区域强制转换为结构体指针。

问题分析步骤如下：

1. 查看UBSan日志中的关键报错字段，确认故障类型。通过member access within misaligned address关键字，并结合for type 'struct x' 字段获取访问对象类型，其中 x 表示发生未对齐访问的结构体名称，初步确认为成员指针未对齐访问。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，即可定位到触发异常的代码位置，分析对象指针来源。

### 关键字

关注故障日志中是否包含以下关键字：member access within misaligned address。

### 案例分析

**案例：**结构体成员访问未对齐

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据：日志中明确给出异常类型为member access within misaligned address，表示程序在未满足对齐要求的地址上访问结构体成员。

   ```screen
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:351:14: runtime error: member access within misaligned address 0x005b9f5fbca1 for type 'struct IllegalOperandA', which requires 8 byte alignment
   0x005b9f5fbca1: note: pointer points here
    03 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  70 4a 55 9f 5b 00 00 00  01 80 6a 9f 00
                 ^ 
       #0 0x5b93d525dc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa125dc) (BuildId: d0cdf7247670257d496b145c8cc6daf67dbe496f)
       #1 0x5a75c71c80  (/system/lib64/platformsdk/libace_napi.z.so+0x71c80) (BuildId: 450a6d44bdb4f26d59104e95c83ef40c)
       #2 0x7f493aeb98  (/system/lib64/module/arkcompiler/stub.an+0xe86b98)
       #3 0x7f49251818  (/system/lib64/module/arkcompiler/stub.an+0xd29818)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:351:14 in 
   ==com.example.dfx_test==58600==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出，完成调用栈#0符号解析。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/JDIC3hSDSTyMcAJ5C7ytjw/zh-cn_image_0000002729611341.png "点击放大")

   ubsanTest.cpp第109行代码触发异常，结合代码确认为执行pointer->i32=7时触发的异常。对异常代码逐行解析如下：

   1. 代码第101~104行：定义结构体IllegalOperandA，结构体内部包含多个不同类型成员变量。由于不同成员类型具有不同对齐要求，结构体对象地址需要满足整体对齐规则。
   2. 代码第107行：buffer获得一块连续的原始内存空间。
   3. 代码第108行：对原始内存空间的地址进行了偏移操作，通过类型转换，将该地址转为结构体指针。
   4. 代码第109行：通过结构体指针访问成员，此时程序根据IllegalOperandA的内存布局，计算成员i32在结构体中的位置，并向对应地址写入数据。但此时pointer的地址不是满足结构体访问要求的合法地址，因此通过该地址访问结构体成员时，实际访问地址不满足成员变量的数据对齐要求，最终导致UBSan检测到异常。

**问题结论与总结**

程序在内存操作过程中未保证对象地址满足对应类型的对齐要求，将非对齐地址作为有效对象地址进行访问，导致对象成员访问时产生地址未对齐问题，存在未定义行为风险。

**修复建议**

在进行对象访问或指针类型转换时，应确保内存地址满足目标类型的对齐要求，避免将未满足对齐规则的内存地址直接转换为对象指针并访问结构体成员。对于原始内存数据解析场景，应避免直接通过强制类型转换访问未对齐数据，可采用安全的数据拷贝方式（如 memcpy()）将数据复制到满足对齐要求的目标对象中，再进行后续访问。

## 数据类型转换异常

### 根因描述

程序在进行数据类型转换时，未充分校验源数据与目标类型之间的兼容性，包括数据表示范围、类型存储规则等差异，直接将不满足目标类型要求的数据转换或解释为目标类型，导致目标类型无法正确表示或访问转换后的数据，引发未定义行为。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，可在类型转换及后续数据访问过程中发现该类非法转换并报告异常。

### 问题分析思路

数据类型转换异常通常由以下几种原因引起：

1. 将不符合目标类型表示范围的数据进行转换。
2. 将无效值转换为目标类型。
3. 不兼容类型之间的强制转换。
4. 指针类型错误转换后访问数据。

问题分析步骤如下：

1. 查看UBSan日志中的报错关键字段，确认故障类型。通过load of value x, which is not a valid value for type 'x'关键字，初步认为该故障类型为数据类型转换异常。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。分析指针来源，检查是否存在错误类型转换，分析实际存储数据与访问类型是否匹配。

### 关键字

关注故障日志中是否包含以下关键字：load of value。

### 案例分析

**案例：**非法类型转换导致的无效对象访问

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出异常为：load of value 2, which is not a valid value for type 'bool'（读取到的值为2，该值不是bool类型的有效值）。

   ```screen
   Module name:xxxx
   Version:1.0.1
   Pid:25400
   Uid:20020227
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:58:9: runtime error: load of value 2, which is not a valid value for type 'bool'
       #0 0x5b375522ac  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa122ac) (BuildId: 62aa1e682f1635fc5f284729dce3729f3df95231)
       #1 0x5a187cfad0  (/system/lib64/platformsdk/libace_napi.z.so+0x4fad0) (BuildId: 69af531e347ee63c838c4f14d23380da)
       #2 0x7e0883d8b8  (/system/lib64/module/arkcompiler/stub.an+0xe948b8)
       #3 0x7e07e2edc0  (/system/lib64/module/arkcompiler/stub.an+0x485dc0)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:58:9 in 
   ==com.example.dfx_test==25400==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出，完成调用栈#0符号解析。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/wjtXyYiWTx-3m6DT-LrKdA/zh-cn_image_0000002699732132.png "点击放大")

   ubsanTest.cpp第58行代码触发异常，结合代码确认为执行res+=2时触发的异常。对异常代码逐行解析如下：

   1. 代码第55行：创建了一个int类型的变量res。
   2. 代码第56行：将指向int类型对象的地址强制按照bool类型指针处理，但内存中的对象并没有发生变化。
   3. 代码第57行：执行条件判断语句时，发生一次内存读取，并按照bool类型解释数据，但bool只有两个合法状态0/1。
   4. 代码第58行：代码通过bool\*类型指针访问实际为int类型的对象，导致对象类型与访问类型不匹配，产生非法类型解释和未定义行为。

**问题结论与总结**

程序通过强制类型转换改变了对象的访问类型，导致按照错误的数据类型访问内存，读取到了非法bool值。

**修复建议**

明确数据类型，避免不安全的隐式类型转换。转换前检查数据范围，避免数值溢出。避免有符号类型和无符号类型混合运算。避免通过强制类型转换绕过类型安全检查。

## 整数溢出操作

### 根因描述

程序在执行整数运算过程中，未充分考虑操作数范围及计算结果可能超过目标整数类型的表示范围，导致运算结果超出当前数据类型可表示范围。由于有符号整数溢出属于未定义行为，可能导致计算结果异常或程序行为不可预测。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，可在整数运算执行过程中检测到超出类型表示范围的溢出操作并报告异常。

### 问题分析思路

整数溢出操作通常由以下几种原因引起：

1. 有符号整数加法超过表示范围。
2. 有符号整数减法低于表示范围。
3. 计算表达式中间结果发生溢出。
4. 循环计数变量递增导致溢出。

问题分析步骤如下：

1. 查看UBSan日志中的报错关键字段，确认故障类型。通过integer overflow关键字，初步确认该故障类型为整数溢出操作。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行，分析参与变量运算的数据类型及取值范围。

### 关键字

关注故障日志中是否包含以下关键字：signed integer overflow。

### 案例分析

**案例：**异常计算操作整数溢出，触发异常

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出异常为：signed integer overflow（有符号整数溢出）。

   ```screen
   Module name:xxxx
   Version:1.0.1
   Pid:33206
   Uid:20020227
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:48:24: runtime error: signed integer overflow: 2147483647 + 1 cannot be represented in type 'int'
       #0 0x5c82f121c4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa121c4) (BuildId: c352a4edab7061cee3f10c7db08f275a4e5cec7f)
       #1 0x5b5cc8fad0  (/system/lib64/platformsdk/libace_napi.z.so+0x4fad0) (BuildId: 69af531e347ee63c838c4f14d23380da)
       #2 0x7f80efb8b8  (/system/lib64/module/arkcompiler/stub.an+0xe948b8)
       #3 0x7f804ecdc0  (/system/lib64/module/arkcompiler/stub.an+0x485dc0)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:48:24 in 
   ==com.example.dfx_test==33206==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出，完成调用栈#0符号解析。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/djvXMymuRG6F1t577I5NFQ/zh-cn_image_0000002729491389.png)

   ubsanTest.cpp第48行代码触发异常，结合代码确认为执行int32\_t result=a+b时触发的异常。对异常代码逐行解析如下：

   1. 代码第46行：设置的int32\_t类型的变量a已经达到了最大值（2147483647）。
   2. 代码第48行：操作数达到类型最大值后继续累加（2147483647+1 > INT32\_MAX），导致整数运算结果超出类型表示范围。

**问题结论与总结**

程序在进行有符号整数运算时，未充分考虑变量的数据范围，导致计算结果超过设置变量类型可表示范围，引发 signed integer overflow 未定义行为。该问题可能导致计算结果异常，进而影响程序逻辑正确性。

**修复建议**

根据变量实际取值范围选择合适的数据类型，避免使用范围不足的整数类型存储计算结果；同时在执行加法、减法、乘法等运算前增加边界检查，确保运算结果不会超过数据类型可表示范围，避免发生整数溢出。

## 浮点数转换溢出

### 根因描述

程序在进行浮点数据类型转换时，未对源浮点数据的取值范围进行有效校验，直接将超出目标类型表示范围的浮点数据转换为目标类型。由于目标类型无法准确表示源数据，导致转换结果无效，引发浮点数转换溢出未定义行为。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，可在浮点转换过程中检测到超出目标类型表示范围的转换操作并报告异常。

### 问题分析思路

浮点数转换溢出通常由以下几种原因引起：

1. 浮点数转换为整数时超出整数表示范围。
2. 浮点数转换为范围更小的整数类型。
3. 浮点计算结果过大后再转换。

问题分析步骤如下：

1. 查看UBSan日志中的报错关键字段，确认故障类型，当日志出现xxx is outside the range of representable values of type 'x'信息时，其中xxx表示参与转换的实际数值，type 'x'表示目标数据类型，表明待转换数据超出了目标类型的表示范围，可初步判定为转换溢出异常。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行，分析存在的类型转换。

### 关键字

关注故障日志中是否包含以下关键字：outside the range。

### 案例分析

**案例：**浮点数转换溢出问题

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出异常为：outside the range （数值超出了表示的范围）。

   ```screen
   Module name:com.example.dfx_test
   Version:1.0.1
   Pid:43896
   Uid:20020227
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:39:30: runtime error: 1e+51 is outside the range of representable values of type 'int'
       #0 0x5bb04d20fc  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa120fc) (BuildId: 34c5b8971bd527fc753fc7de411e5e022390de79)
       #1 0x5a9164fad0  (/system/lib64/platformsdk/libace_napi.z.so+0x4fad0) (BuildId: 69af531e347ee63c838c4f14d23380da)
       #2 0x7e483ee8b8  (/system/lib64/module/arkcompiler/stub.an+0xe948b8)
       #3 0x7e479dfdc0  (/system/lib64/module/arkcompiler/stub.an+0x485dc0)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:39:30 in 
   ==com.example.dfx_test==43896==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出，完成调用栈#0符号解析。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/uYDCXPAxSma49kiEZzD0sw/zh-cn_image_0000002699892016.png)

   ubsanTest.cpp第39行代码触发异常，结合代码确认为执行int m=static\_cast<int>(n)时触发的异常。对异常代码逐行解析如下：

   1. 代码第38行：设置的变量n，存储的数值大小为1e+51。
   2. 代码第39行：int类型的数值范围是-2147483648~2147483647，而1e+51远超该范围，将其转换为int类型时触发异常。

**问题结论与总结**

程序在运行过程中，将一个超出目标类型表示范围的浮点数转换为目标类型时，UBSan检测到转换异常。

**修复建议**

在类型转换前检查源数据范围，确保转换后的值满足目标类型的表示范围。程序应避免未经校验的强制类型转换，并根据业务需求选择合适的数据类型。同时，对于外部输入的浮点数据，需要增加有效性检查，避免非法数值导致转换异常。

## 除零操作

### 根因描述

程序在执行除法运算时，未对除数的有效性进行检查，导致除数可能为零的情况下仍参与计算。由于除数为零不满足除法运算要求，导致程序执行非法除法操作，引发未定义行为。[开启UBSan](../harmonyos-guides/ide-ubsan.md#section19738384313)检测后，可在除法运算执行过程中检测到零除数并报告异常。

### 问题分析思路

除零操作通常由以下几种原因引起：

1. 直接使用常量0作为除数。
2. 条件判断遗漏导致除数为0。
3. 循环计算过程中除数变化为0。
4. 外部输入导致除数异常。
5. 算法计算过程中产生零除数。

问题分析步骤如下：

1. 查看UBSan日志中的报错关键字段，确认故障类型，其中包含信息：division by zero，可初步判定为除零异常。
2. 根据UBSan输出的调用栈信息，分析报错栈，确认触发异常位置，并通过llvm-addr2line（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）等解析工具，定位到具体代码行。查看除法表达式，分析除数为0的原因。

### 关键字

关注故障日志中是否包含以下关键字：division by zero。

### 案例分析

**案例：**异常计算操作除零，循环条件错误，触发异常

**问题现象**

应用运行过程中触发UBSan检测，生成UBSan故障日志。

**问题分析**

1. 查看日志内容，确认故障类型。

   证据1：日志中明确给出异常为：division by zero（执行除法操作时除数为0，导致除零异常）。

   ```screen
   Module name:xxxx
   Version:1.0.1
   Pid:24901
   Uid:20020227
   Reason:UBSAN
   D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:17:13: runtime error: division by zero
       #0 0x5ca7111fd8  (/data/storage/el1/bundle/libs/arm64/libentry.so+0xa11fd8) (BuildId: c352a4edab7061cee3f10c7db08f275a4e5cec7f)
       #1 0x5b7f4cfad0  (/system/lib64/platformsdk/libace_napi.z.so+0x4fad0) (BuildId: 69af531e347ee63c838c4f14d23380da)
       #2 0x7fae6ee8b8  (/system/lib64/module/arkcompiler/stub.an+0xe948b8)
       #3 0x7fadcdfdc0  (/system/lib64/module/arkcompiler/stub.an+0x485dc0)

   SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior D:/dfx_test/entry/src/main/cpp/common/xsan/ubsanTest.cpp:17:13 in 
   ==com.example.dfx_test==24901==Process memory map follows:
   ```
2. 获取带符号的so，通过llvm-addr2line工具（参考：[C++堆栈解析流程](../harmonyos-guides/ide-exception-stack-parsing-principle.md#section1735713501344)中对于llvm-addr2line的使用）解析栈得出，完成调用栈#0符号解析。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ryANmXQuQZWNQqyi3Ec07Q/zh-cn_image_0000002729611343.png)

   ubsanTest.cpp第17行代码触发异常，结合代码确认为执行sum/=i时触发的异常。对异常代码逐行解析如下：

   1. 代码第16行：循环条件中，变量i的初始值设置为0。
   2. 代码第17行：除数变量为0，导致发生除零操作。

**问题结论与总结**

除法运算前缺少对除数有效性的检查，未保证除数非零，导致非法触发操作。

**修复建议**

除法运算前增加除数校验，对可能为0的输入参数和计算结果进行边界校验，避免发生除零操作。
