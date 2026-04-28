---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-file-format
title: 方舟字节码文件格式
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > 方舟字节码 > 方舟字节码文件格式
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c3d3e45461f5f304a2d10d11ef39f144c82a48aff7a35711425ce493a6e2d522
---

本文详细介绍了方舟字节码文件的格式，旨在帮助开发者深入理解字节码文件的组成结构，以指导字节码的分析和修改。

## 约束

本文内容基于方舟字节码版本号12.0.6.0（版本号为方舟编译器内部保留字段，开发者无需关注，仅供准确对照之用）。

## 字节码文件数据类型

方舟字节码使用了多种基础和复合数据类型，以下为常见类型的定义和说明。

### 整型

| **名称** | **说明** |
| --- | --- |
| uint8\_t | 8-bit无符号整数。 |
| uint16\_t | 16-bit无符号整数，采用小端字节序。 |
| uint32\_t | 32-bit无符号整数，采用小端字节序。 |
| uleb128 | leb128编码的无符号整数。 |
| sleb128 | leb128编码的有符号整数。 |

### 字符串

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| utf16\_length | uleb128 | 值为len << 1 | is\_ascii，其中len是字符串在UTF-16编码中的大小，is\_ascii标记该字符串是否仅包含ASCII字符。 |
| data | uint8\_t[] | 以'\0'结尾的MUTF-8编码字符序列。 |

### TaggedValue

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| tag | uint8\_t | 表示数据种类的标记。 |
| data | uint8\_t[] | 根据不同的标记，data是不同类型的数据或者为空。 |

## TypeDescriptor

TypeDescriptor是类（[Class](arkts-bytecode-file-format.md#class)）名称的格式，由'L'、'\_'、ClassName和';'组成：L\_ClassName;。其中，ClassName是类的全名，名称中的'.'会被替换为'/'。

## 字节码文件布局

字节码文件起始于[Header](arkts-bytecode-file-format.md#header)结构。文件中的所有结构均可以从Header出发，直接或间接地访问到。字节码文件中结构的引用方式包括偏移量和索引。偏移量是一个32位长度的值，表示当前结构的起始位置在字节码文件中相对于文件头的字节偏移量，从0开始计算。索引是一个16位长度的值，表示当前结构在索引区域中的位置，此机制将在[IndexSection](arkts-bytecode-file-format.md#indexsection)章节描述。

字节码文件中所有多字节数值类型（如u16、u32和i32等）均采用小端字节序（Little-endian）存储。

### Header

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| magic | uint8\_t[8] | 文件头魔数，值必须是'P' 'A' 'N' 'D' 'A' '\0' '\0' '\0'。 |
| checksum | uint32\_t | 字节码文件除文件头魔数和本校验字段之外的内容的adler32校验和。 |
| version | uint8\_t[4] | 字节码文件的版本号（[Version](arkts-bytecode-file-format.md#version)）。 |
| file\_size | uint32\_t | 字节码文件的大小，以字节为单位。 |
| foreign\_off | uint32\_t | 偏移量，指向外部区域。外部区域中仅包含类型为[ForeignClass](arkts-bytecode-file-format.md#foreignclass)或[ForeignMethod](arkts-bytecode-file-format.md#foreignmethod)的元素。foreign\_off指向该区域的第一个元素。 |
| foreign\_size | uint32\_t | 外部区域的大小，以字节为单位。 |
| num\_classes | uint32\_t | [ClassIndex](arkts-bytecode-file-format.md#classindex)结构中元素的数量，即文件中定义的[Class](arkts-bytecode-file-format.md#class)的数量。 |
| class\_idx\_off | uint32\_t | 偏移量，指向[ClassIndex](arkts-bytecode-file-format.md#classindex)。 |
| num\_lnps | uint32\_t | [LineNumberProgramIndex](arkts-bytecode-file-format.md#linenumberprogramindex)结构中元素的数量，即文件中定义的Line number program的数量。 |
| lnp\_idx\_off | uint32\_t | 偏移量，指向[LineNumberProgramIndex](arkts-bytecode-file-format.md#linenumberprogramindex)。 |
| reserved | uint32\_t | 方舟字节码文件内部使用的保留字段。 |
| num\_index\_regions | uint32\_t | [IndexSection](arkts-bytecode-file-format.md#indexsection)结构中元素的数量，即文件中[IndexHeader](arkts-bytecode-file-format.md#indexheader)的数量。 |
| index\_section\_off | uint32\_t | 偏移量，指向[IndexSection](arkts-bytecode-file-format.md#indexsection)。 |

### Version

字节码版本号由4个部分组成，格式为：主版本号.次版本号.特性版本号.编译版本号。

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| 主版本号 | uint8\_t | 标识整体架构调整引入的字节码文件格式变更。 |
| 次版本号 | uint8\_t | 标识局部架构调整或者重大特性调整引入的字节码文件格式变更。 |
| 特性版本号 | uint8\_t | 标识中小特性引入的字节码文件格式变更。 |
| 编译版本号 | uint8\_t | 标识缺陷修复引入的字节码文件格式变更。 |

### ForeignClass

描述字节码文件中的外部类。外部类在其他文件中声明，并在当前字节码文件中被引用。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| name | String | 外部类的名称，命名遵循[TypeDescriptor](arkts-bytecode-file-format.md#typedescriptor)语法。 |

### ForeignMethod

描述字节码文件中的外部方法。外部方法在其他文件中声明，并在当前字节码文件中被引用。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| class\_idx | uint16\_t | 一个指向该方法所从属的类的索引，指向一个在[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中的位置，该位置的值是一个指向[Class](arkts-bytecode-file-format.md#class)或[ForeignClass](arkts-bytecode-file-format.md#foreignclass)的偏移量。 |
| reserved | uint16\_t | 方舟字节码文件内部使用的保留字段。 |
| name\_off | uint32\_t | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示方法名称。 |
| index\_data | uleb128 | 方法的[MethodIndexData](arkts-bytecode-file-format.md#methodindexdata)数据。 |

注意

通过ForeignMethod的偏移量，可以找到偏移量所在的IndexHeader以解析class\_idx。

### ClassIndex

ClassIndex结构能通过名称快速定位到Class的定义。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| offsets | uint32\_t[] | 一个数组，数组中每个元素的值是一个指向[Class](arkts-bytecode-file-format.md#class)的偏移量。数组中的元素根据类的名称进行排序，名称遵循[TypeDescriptor](arkts-bytecode-file-format.md#typedescriptor)语法。数组长度由[Header](arkts-bytecode-file-format.md#header)中的num\_classes指定。 |

### Class

在字节码文件中，一个类可以表示方舟字节码的一个源代码文件或者一种内置的[Annotation](arkts-bytecode-file-format.md#annotation)。当表示源代码文件时，类的方法对应源代码文件中的函数，类的字段对应源文件中的内部信息；当表示内置的Annotation时，类中不包含字段与方法。源代码文件中的一个类在字节码文件中表示为一个对应其构造函数的方法。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| name | String | Class的名称，命名遵循[TypeDescriptor](arkts-bytecode-file-format.md#typedescriptor)语法。 |
| reserved | uint32\_t | 方舟字节码文件内部使用的保留字段。 |
| access\_flags | uleb128 | Class的访问标志，是[ClassAccessFlag](arkts-bytecode-file-format.md#classaccessflag)的组合。 |
| num\_fields | uleb128 | Class的字段的数量。 |
| num\_methods | uleb128 | Class的方法的数量。 |
| class\_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)类型，元素的标记是[ClassTag](arkts-bytecode-file-format.md#classtag)类型，数组中的元素按照标记递增排序（0x00标记除外）。 |
| fields | Field[] | Class的字段的数组，数组中每一个元素都是[Field](arkts-bytecode-file-format.md#field)类型。数组长度由num\_fields指定。 |
| methods | Method[] | Class的方法的数组，数组中每一个元素都是[Method](arkts-bytecode-file-format.md#method)类型。数组长度由num\_methods指定。 |

### ClassAccessFlag

| **名称** | **值** | **说明** |
| --- | --- | --- |
| ACC\_PUBLIC | 0x0001 | 默认属性，方舟字节码中的[Class](arkts-bytecode-file-format.md#class)均具备此标志。 |
| ACC\_ANNOTATION | 0x2000 | 声明该类为[Annotation](arkts-bytecode-file-format.md#annotation)类型。 |

### ClassTag

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **值** | **数量** | **格式** | **说明** |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)，是其所在class\_data的最后一项。 |
| SOURCE\_LANG | 0x02 | 0-1 | uint8\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data的值为0时，表示源码语言是ArkTS/TS/JS。 |
| SOURCE\_FILE | 0x07 | 0-1 | uint32\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data是一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示源文件的名称。 |

注意

ClassTag是class\_data中元素（[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)）所具备的标记，表头中的“数量”指的是在某一个[Class](arkts-bytecode-file-format.md#class)的class\_data中拥有此标记的元素出现的次数。

### Field

描述字节码文件中的字段。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| class\_idx | uint16\_t | 一个指向该字段从属的类的索引，指向一个在[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中的位置，该位置的值是[Type](arkts-bytecode-file-format.md#type)类型，是一个指向[Class](arkts-bytecode-file-format.md#class)的偏移量。 |
| type\_idx | uint16\_t | 一个指向定义该字段的类型的索引，指向一个在[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中的位置，该位置的值是[Type](arkts-bytecode-file-format.md#type)类型。 |
| name\_off | uint32\_t | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示字段的名称。 |
| reserved | uleb128 | 方舟字节码文件内部使用的保留字段。 |
| field\_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)类型，元素的标记是[FieldTag](arkts-bytecode-file-format.md#fieldtag)类型，数组中的元素按照标记递增排序（0x00标记除外）。 |

注意

通过Field的偏移量，可以找到偏移量所在的IndexHeader以解析class\_idx和type\_idx。

### FieldTag

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **值** | **数量** | **格式** | **说明** |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)，是其所在field\_data的最后一项。 |
| INT\_VALUE | 0x01 | 0-1 | sleb128 | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data的类型为boolean、byte、char、short 或 int。 |
| VALUE | 0x02 | 0-1 | uint32\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data的类型为[Value formats](arkts-bytecode-file-format.md#value-formats)中的FLOAT或ID。 |

注意

FieldTag是field\_data中元素（[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)）的标记。表头中的“数量”表示在某个[Field](arkts-bytecode-file-format.md#field)的field\_data中拥有此标记的元素出现的次数。

### Method

描述字节码文件中的方法。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| class\_idx | uint16\_t | 一个指向该方法所从属的类的索引，指向一个在[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中的位置，该位置的值是[Type](arkts-bytecode-file-format.md#type)类型，是一个指向[Class](arkts-bytecode-file-format.md#class)的偏移量。 |
| reserved | uint16\_t | 方舟字节码文件内部使用的保留字段。 |
| name\_off | uint32\_t | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示方法名称。 |
| index\_data | uleb128 | 方法的[MethodIndexData](arkts-bytecode-file-format.md#methodindexdata)数据。 |
| method\_data | TaggedValue[] | 不定长度的数组，数组中每个元素都是[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)类型，元素的标记是[MethodTag](arkts-bytecode-file-format.md#methodtag)类型，数组中的元素按照标记递增排序（0x00标记除外）。 |

注意

通过Method的偏移量，可以找到偏移量所在的IndexHeader以解析class\_idx。

### MethodIndexData

MethodIndexData是一个无符号32位整数，划分为3个部分。

| **位** | **名称** | **格式** | **说明** |
| --- | --- | --- | --- |
| 0 - 15 | header\_index | uint16\_t | 指向一个在[IndexSection](arkts-bytecode-file-format.md#indexsection)中的位置，该位置的值是[IndexHeader](arkts-bytecode-file-format.md#indexheader)。通过IndexHeader可以找到该方法引用的所有方法（[Method](arkts-bytecode-file-format.md#method)）、[字符串](arkts-bytecode-file-format.md#字符串)或字面量数组（[LiteralArray](arkts-bytecode-file-format.md#literalarray)）的偏移量。 |
| 16 - 23 | function\_kind | uint8\_t | 表示方法的函数类型（FunctionKind）。 |
| 24 - 31 | reserved | uint8\_t | 方舟字节码文件内部使用的保留字段。 |

**FunctionKind**

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FUNCTION | 0x1 | 普通函数。 |
| NC\_FUNCTION | 0x2 | 普通箭头函数。 |
| GENERATOR\_FUNCTION | 0x3 | 生成器函数。 |
| ASYNC\_FUNCTION | 0x4 | 异步函数。 |
| ASYNC\_GENERATOR\_FUNCTION | 0x5 | 异步生成器函数。 |
| ASYNC\_NC\_FUNCTION | 0x6 | 异步箭头函数。 |
| CONCURRENT\_FUNCTION | 0x7 | 并发函数。 |

### MethodTag

| **名称** | **值** | **数量** | **格式** | **说明** |
| --- | --- | --- | --- | --- |
| NOTHING | 0x00 | 1 | none | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)，是其所在method\_data的最后一项。 |
| CODE | 0x01 | 0-1 | uint32\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data是一个偏移量，指向[Code](arkts-bytecode-file-format.md#code)，表示方法的代码段。 |
| SOURCE\_LANG | 0x02 | 0-1 | uint8\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data为0时，表示源码语言是ArkTS/TS/JS。 |
| DEBUG\_INFO | 0x05 | 0-1 | uint32\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data是一个偏移量，指向[DebugInfo](arkts-bytecode-file-format.md#debuginfo)，表示方法的调试信息。 |
| ANNOTATION | 0x06 | >=0 | uint32\_t | 拥有此标记的[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)的data是一个偏移量，指向[Annotation](arkts-bytecode-file-format.md#annotation)， 表示方法的注解。 |

注意

MethodTag是method\_data中元素（[TaggedValue](arkts-bytecode-file-format.md#taggedvalue)）的标记。表头中的“数量”表示在某个[Method](arkts-bytecode-file-format.md#method)的method\_data中，具有此标记的元素出现的次数。

### Code

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| num\_vregs | uleb128 | 表示寄存器的数量，不包括存放入参和默认参数的寄存器。 |
| num\_args | uleb128 | 表示入参和默认参数的总数。 |
| code\_size | uleb128 | 表示所有指令的总大小，以字节为单位。 |
| tries\_size | uleb128 | try\_blocks数组的长度，表示[TryBlock](arkts-bytecode-file-format.md#tryblock)的数量。 |
| instructions | uint8\_t[] | 所有指令的数组。 |
| try\_blocks | TryBlock[] | 一个数组，数组中每个元素均为TryBlock类型。 |

### TryBlock

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| start\_pc | uleb128 | TryBlock的第一条指令距离其所在[Code](arkts-bytecode-file-format.md#code)的instructions的起始位置的偏移量。 |
| length | uleb128 | TryBlock的大小，以字节为单位。 |
| num\_catches | uleb128 | 与TryBlock关联的[CatchBlock](arkts-bytecode-file-format.md#catchblock)的数量，值为1。 |
| catch\_blocks | CatchBlock[] | 与TryBlock关联的CatchBlock的数组，数组中有且仅有一个可以捕获所有类型的异常的CatchBlock。 |

### CatchBlock

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| type\_idx | uleb128 | 值为0，表示此CatchBlock块捕获所有类型的异常。 |
| handler\_pc | uleb128 | 异常处理逻辑的第一条指令的程序计数器。 |
| code\_size | uleb128 | 此CatchBlock的大小，以字节为单位。 |

### Annotation

描述一个注解结构。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| class\_idx | uint16\_t | 一个指向当前Annotation所从属的类的索引，指向一个在[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中的位置，该位置的值是[Type](arkts-bytecode-file-format.md#type)类型，是一个指向[Class](arkts-bytecode-file-format.md#class)的偏移量。 |
| count | uint16\_t | elements数组的长度。 |
| elements | AnnotationElement[] | 一个数组，数组的每个元素都是[AnnotationElement](arkts-bytecode-file-format.md#annotationelement)类型。 |
| element\_types | uint8\_t[] | 一个数组，数组的每个元素都是[AnnotationElementTag](arkts-bytecode-file-format.md#annotationelementtag)类型，用于描述一个AnnotationElement。每个元素在element\_types数组中的位置和其对应的AnnotationElement在elements数组中的位置一致。 |

注意

通过Annotation的偏移量，可以找到偏移量所在的IndexHeader以解析class\_idx。

### AnnotationElementTag

| **名称** | **标记** |
| --- | --- |
| u1 | '1' |
| i8 | '2' |
| u8 | '3' |
| i16 | '4' |
| u16 | '5' |
| i32 | '6' |
| u32 | '7' |
| i64 | '8' |
| u64 | '9' |
| f32 | 'A' |
| f64 | 'B' |
| string | 'C' |
| method | 'E' |
| annotation | 'G' |
| literalarray | '#' |
| unknown | '0' |

### AnnotationElement

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| name\_off | uint32\_t | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示注解元素的名称。 |
| value | uint32\_t | 注解元素的值，若该值的宽度不超过32位，则此处存储值本身。否则，此处存储的值为指向[Value formats](arkts-bytecode-file-format.md#value-formats)格式的偏移量。 |

### Value formats

不同的值类型，有不同的值编码格式，包括INTEGER, LONG, FLOAT, DOUBLE, ID。

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| INTEGER | uint32\_t | 有符号的四字节整数值。 |
| LONG | uint64\_t | 有符号的八字节整数值。 |
| FLOAT | uint32\_t | 四字节位模式，向右零扩展，系统会将其解译为 IEEE754 32 位浮点值。 |
| DOUBLE | uint64\_t | 八字节位模式，向右零扩展，系统会将其解译为 IEEE754 64 位浮点值。 |
| ID | uint32\_t | 四字节位模式，表示文件中某个结构的偏移量。 |

### LineNumberProgramIndex

行号程序索引（LineNumberProgramIndex）的结构是一个数组，便于使用更紧凑的索引访问行号程序（Line number program）。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| offsets | uint32\_t[] | 一个数组，数组中每个元素的值是一个偏移量，指向一个行号程序。数组长度由[Header](arkts-bytecode-file-format.md#header)中的num\_lnps指定。 |

### DebugInfo

调试信息（DebugInfo）包含方法的程序计数器与源代码中的行列号之间的映射以及有关局部变量的信息。调试信息的格式由[DWARF调试信息格式第3版](https://dwarfstd.org/dwarf3std.html)（见第6.2项）的内容演变形成。基于状态机（State machine）的执行模型对行号程序（Line number program）进行解释，可得到映射和局部变量信息编码。为对不同方法的相同行号程序进行去重，程序中引用的所有常量都被移动到了常量池（Constant pool）中。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| line\_start | uleb128 | 状态机的行号寄存器的初始值。 |
| num\_parameters | uleb128 | 入参和默认参数的总数量。 |
| parameters | uleb128[] | 存储方法入参名称的数组，长度为num\_parameters。每个元素表示字符串的偏移量或0，0表示对应参数无名称。 |
| constant\_pool\_size | uleb128 | 常量池的大小，以字节为单位。 |
| constant\_pool | uleb128[] | 存放常量池数据的数组，数组长度是constant\_pool\_size。 |
| line\_number\_program\_idx | uleb128 | 一个索引，指向一个在[LineNumberProgramIndex](arkts-bytecode-file-format.md#linenumberprogramindex)中的位置，该位置的值是一个指向Line number program的偏移量。Line number program的长度可变，以END\_SEQUENCE操作码结束。 |

**Constant pool**

常量池（Constant pool）是DebugInfo中存放常量的结构。很多方法都具有相似的行号程序，其区别仅在于变量名、变量类型和文件名。为了对这类行号程序进行去重，程序中引用的所有常量都存储在常量池。在解释程序时，状态机维护一个指向常量池的指针。当状态机解释一条需要常量参数的指令时，会从内存常量池指针指向的位置读取值，然后递增指针。

**State machine**

状态机（State machine）的作用是产生[DebugInfo](arkts-bytecode-file-format.md#debuginfo)信息。状态机中有以下的寄存器：

| **名称** | **初始值** | **说明** |
| --- | --- | --- |
| address | 0 | 程序计数器（指向方法的某个指令），只能单调递增。 |
| line | [DebugInfo](arkts-bytecode-file-format.md#debuginfo)的属性line\_start的值 | 无符号整数，对应源码中的行号。所有的行都是从1开始编号，因此寄存器的值不能小于1。 |
| column | 0 | 无符号整数，对应源码中的列号。 |
| file | class\_data（参见[Class](arkts-bytecode-file-format.md#class)）中SOURCE\_FILE标记的值，或者0 | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示源文件的名称。如果没有文件名信息（[Class](arkts-bytecode-file-format.md#class)中没有SOURCE\_FILE标记），那么寄存器的值是0。 |
| source\_code | 0 | 一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示源文件的源码。如果没有源码信息，那么寄存器的值是0。 |
| constant\_pool\_ptr | [DebugInfo](arkts-bytecode-file-format.md#debuginfo)中常量池的起始地址 | 指向当前常量值的指针。 |

**Line number program**

一个行号程序（Line number program）由指令组成。每条指令都包含一个字节的操作码以及可选参数。根据操作码的不同，参数的值可能被编码在指令中（称为指令参数），或者需要从常量池中获取（称为常量池参数）。

| **操作码** | **值** | **指令参数** | **常量池参数** | **参数说明** | **说明** |
| --- | --- | --- | --- | --- | --- |
| END\_SEQUENCE | 0x00 | - | - | - | 标记行号程序的结束。 |
| ADVANCE\_PC | 0x01 | - | uleb128 addr\_diff | addr\_diff：address寄存器的值待增加的数值。 | address寄存器中的值加上addr\_diff，指向下一个地址，而不生成位置条目。 |
| ADVANCE\_LINE | 0x02 | - | sleb128 line\_diff | line\_diff：line寄存器的值待增加的数值。 | line寄存器中的值加上line\_diff，指向下一个行位置，而不生成位置条目。 |
| START\_LOCAL | 0x03 | sleb128 register\_num | uleb128 name\_idx  uleb128 type\_idx | register\_num：将包含局部变量的寄存器。  name\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示变量的名称。  type\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示变量的类型。 | 在当前地址中引入一个带有名称和类型的局部变量。将要包含这个变量的寄存器的编号被编码在指令中。如果寄存器的编号是-1，则表示这个寄存器是累加器寄存器。name\_idx和type\_idx的值可能为0，如果为0，则代表对应的信息不存在。 |
| START\_LOCAL\_EXTENDED | 0x04 | sleb128 register\_num | uleb128 name\_idx  uleb128 type\_idx  uleb128 sig\_idx | register\_num：将包含局部变量的寄存器。  name\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示变量的名称。  type\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示变量的类型。  sig\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示变量的签名。 | 在当前地址中引入一个带有名称、类型和签名的局部变量。将要包含这个变量的寄存器的编号被编码在指令中。如果寄存器的编号是-1，则表示这个寄存器是累加器寄存器。name\_idx、type\_idx和sig\_idx的值可能为0，如果为0，则代表对应的信息不存在。 |
| END\_LOCAL | 0x05 | sleb128 register\_num | - | register\_num：包含局部变量的寄存器。 | 在当前地址将指定寄存器中的局部变量标记为超出范围。寄存器的编号为-1，则表示这个寄存器是累加器寄存器。 |
| SET\_FILE | 0x09 | - | uleb128 name\_idx | name\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示文件的名称。 | 设置file寄存器的值。name\_idx的值可能为0，如果为0，则代表对应的信息不存在。 |
| SET\_SOURCE\_CODE | 0x0a | - | uleb128 source\_idx | source\_idx：一个偏移量，指向[字符串](arkts-bytecode-file-format.md#字符串)，表示文件的源码。 | 设置source\_code寄存器的值。source\_idx的值可能为0，如果为0，则代表对应的信息不存在。 |
| SET\_COLUMN | 0x0b | - | uleb128 column\_num | column\_num：待设置的列号。 | 设置column寄存器的值，并生成一个位置条目。 |
| 特殊操作码 | 0x0c..0xff | - | - | - | 使 line 和 address 寄存器指向下一个地址，并生成一个位置条目。详情参阅下文中的说明。 |

对于值在0x0c和0xff（含）之间的特殊操作码，状态机按照以下步骤将line和address寄存器移动一小部分，然后生成一个新的位置条目（参见[DWARF调试信息格式第3版](https://dwarfstd.org/dwarf3std.html)第6.2.5.1项 Special Opcodes）：

| **步骤序号** | **操作** | **说明** |
| --- | --- | --- |
| 1 | adjusted\_opcode = opcode - OPCODE\_BASE | 计算调整后的操作码。OPCODE\_BASE的值是0x0c，是第一个特殊操作码。 |
| 2 | address += adjusted\_opcode / LINE\_RANGE | 增加address寄存器中的值。LINE\_RANGE的值是15，用来计算行号信息的变化。 |
| 3 | line += LINE\_BASE + (adjusted\_opcode % LINE\_RANGE) | 增加line寄存器中的值。LINE\_BASE的值是-4，是最小的行号增量值；最大的行号增量值是LINE\_BASE + LINE\_RANGE - 1。 |
| 4 | - | 生成一个新的位置条目。 |

注意

特殊操作码计算方式：(line\_increment - LINE\_BASE) + (address\_increment \* LINE\_RANGE) + OPCODE\_BASE。

### IndexSection

通常情况下，字节码文件的各个结构使用32位偏移量来引用，当一个结构引用另一个结构时，需要在当前结构中记录被引用结构的32位偏移量。为了减小文件体积，字节码文件被分割成多个索引区域（Index region），每个索引区域内的结构使用16位索引。IndexSection结构描述了索引区域的集合。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| headers | IndexHeader[] | 一个数组，数组中每个元素是[IndexHeader](arkts-bytecode-file-format.md#indexheader)类型。数组中的元素根据区域的起始偏移量进行排序。数组长度由[Header](arkts-bytecode-file-format.md#header)中的num\_index\_regions指定。 |

### IndexHeader

每个IndexHeader结构描述一个索引区域。每个索引区域都有两类索引：指向[Type](arkts-bytecode-file-format.md#type)的索引和指向方法、字符串或者字面量数组的索引。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| start\_off | uint32\_t | 该区域的起始偏移量。 |
| end\_off | uint32\_t | 该区域的结束偏移量。 |
| class\_region\_idx\_size | uint32\_t | 该区域的[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)中元素的数量，最大值为65536。 |
| class\_region\_idx\_off | uint32\_t | 一个偏移量，指向[ClassRegionIndex](arkts-bytecode-file-format.md#classregionindex)。 |
| method\_string\_literal\_region\_idx\_size | uint32\_t | 该区域的[MethodStringLiteralRegionIndex](arkts-bytecode-file-format.md#methodstringliteralregionindex)中元素的数量，最大值为65536。 |
| method\_string\_literal\_region\_idx\_off | uint32\_t | 一个偏移量，指向[MethodStringLiteralRegionIndex](arkts-bytecode-file-format.md#methodstringliteralregionindex)。 |
| reserved | uint32\_t | 方舟字节码文件内部使用的保留字段。 |

### ClassRegionIndex

ClassRegionIndex结构的作用是允许通过更紧凑的索引，找到对应的[Type](arkts-bytecode-file-format.md#type)。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| types | Type[] | 一个数组，数组中每个元素都是[Type](arkts-bytecode-file-format.md#type)类型。数组长度由[IndexHeader](arkts-bytecode-file-format.md#indexheader)中的class\_region\_idx\_size指定。 |

### Type

表示一个基本类型编码或一个指向[Class](arkts-bytecode-file-format.md#class)的偏移量，是一个32位的值。

基本类型采用以下方式编码：

| **类型** | **编码** |
| --- | --- |
| u1 | 0x00 |
| i8 | 0x01 |
| u8 | 0x02 |
| i16 | 0x03 |
| u16 | 0x04 |
| i32 | 0x05 |
| u32 | 0x06 |
| f32 | 0x07 |
| f64 | 0x08 |
| i64 | 0x09 |
| u64 | 0x0a |
| any | 0x0c |

### MethodStringLiteralRegionIndex

MethodStringLiteralRegionIndex结构的作用是允许通过更紧凑的索引，找到对应的方法、字符串或者字面量数组。

* 对齐方式：4个字节。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| offsets | uint32\_t[] | 一个数组，数组中每个元素的值都是一个偏移量，指向方法、字符串或者字面量数组。数组长度由[IndexHeader](arkts-bytecode-file-format.md#indexheader)中的method\_string\_literal\_region\_idx\_size指定。 |

### LiteralArray

描述字节码文件中的字面量数组。

* 对齐方式：单字节对齐。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| num\_literals | uint32\_t | literals数组的长度。 |
| literals | Literal[] | 一个数组，数组的每个元素都是[Literal](arkts-bytecode-file-format.md#literal)类型。 |

### Literal

描述字节码文件中的字面量，根据字面量值的字节数的不同，有四种编码格式。分别是单字节编码、双字节编码、四字节编码和八字节编码。根据不同数值长度对应相应的编译格式，优化字节码文件大小。

* 对齐方式：每种格式都有对应的对齐规则。
* 格式：

| **名称** | **格式** | **说明** |
| --- | --- | --- |
| 单字节编码 | uint8\_t | 单字节的值，单字节对齐，存储用于简单类型的字面量，例如BOOL字面量。 |
| 双字节编码 | uint16\_t | 双字节的值，2个字节对齐，存储16位整型字面量。 |
| 四字节编码 | uint32\_t | 四字节的值，4个字节对齐，存储32位数值字面量，例如INTEGER整数型字面量，或FLOAT浮点型字面量。 |
| 八字节编码 | uint64\_t | 八字节的值，8个字节对齐，存储64位数值字面量，例如DOUBLE双精度浮点型字面量。 |
