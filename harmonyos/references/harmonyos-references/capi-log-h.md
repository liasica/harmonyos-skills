---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-log-h
title: log.h
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 头文件 > log.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b66e1d87fcb11b8ef7980040e3acf0daed2c6dbe55dc5648a50d6c7008c4e00f
---

## 概述

PhonePC/2in1TabletTVWearable

HiLog模块日志接口定义，通过这些接口实现日志打印相关功能。用户输出日志时，先定义日志所属业务领域、日志TAG，然后按照类型、级别选择对应API，指定参数隐私标识输出日志内容。

业务领域：指定日志所对应的业务领域，用户自定义使用，用于标识业务的子系统、模块。16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。

日志TAG：字符串常量，用于标识调用所在的类或者业务。

日志级别：DEBUG、INFO、WARN、ERROR、FATAL。

参数格式：类printf的%方式，包括格式字符串（包括参数类型标识）和变参。

隐私参数标识：在格式字符串每个参数中%符号后类型前增加{public}、{private}标识。注意：每个参数未指定隐私标识时，缺省为隐私。

**引用文件：** <hilog/log.h>

**库：** libhilog\_ndk.z.so

**系统能力：** SystemCapability.HiviewDFX.HiLog

**起始版本：** 8

**相关模块：** [HiLog](capi-hilog.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [LogType](capi-log-h.md#logtype) | LogType | 日志类型。该枚举类型用于定义应用开发者可以使用的日志类型。当前有应用日志LOG\_APP。 |
| [LogLevel](capi-log-h.md#loglevel) | LogLevel | 日志级别。该枚举类型用于定义日志级别。各级别建议使用方式：  DEBUG：比INFO级别更详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。DEBUG级别的日志在正式发布版本中默认不会被打印，只有在调试版本或打开调试开关的情况下才会打印。  INFO：用来记录业务关键流程节点，可以还原业务的主要运行过程；用来记录非正常情况信息，但这些情况都是可以预期的(如无网络信号、登录失败等)。这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。  WARN：发生了较为严重的非预期情况，但是对用户影响不大，程序可以自动恢复或通过简单的操作就可以恢复的问题。  ERROR：程序或功能发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。  FATAL：重大致命异常，表明程序或功能即将崩溃，故障无法恢复。 |
| [PreferStrategy](capi-log-h.md#preferstrategy) | PreferStrategy | 偏好策略。在[OH\_LOG\_SetLogLevel](capi-log-h.md#oh_log_setloglevel)中使用。不同策略，实际生效的最低日志级别也不同。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_LOG\_DEBUG(type, ...) ((void)OH\_LOG\_Print((type), LOG\_DEBUG, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | DEBUG级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。  **起始版本：** 8 |
| OH\_LOG\_INFO(type, ...) ((void)OH\_LOG\_Print((type), LOG\_INFO, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | INFO级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。  **起始版本：** 8 |
| OH\_LOG\_WARN(type, ...) ((void)OH\_LOG\_Print((type), LOG\_WARN, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | WARN级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。  **起始版本：** 8 |
| OH\_LOG\_ERROR(type, ...) ((void)OH\_LOG\_Print((type), LOG\_ERROR, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | ERROR级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。  **起始版本：** 8 |
| OH\_LOG\_FATAL(type, ...) ((void)OH\_LOG\_Print((type), LOG\_FATAL, LOG\_DOMAIN, LOG\_TAG, \_\_VA\_ARGS\_\_)) | FATAL级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。  **起始版本：** 8 |
| LOG\_DOMAIN | 指定输出日志所对应的业务领域，默认值为0，取值范围为0x0~0xFFFF，超出此范围的domainID将导致日志无法打印。  **起始版本：** 8 |
| LOG\_TAG | 标识日志调用所在的类或业务行为，类型为字符串常量，默认值为NULL，最大长度为31个字节，超出后会截断，必须设置成非NULL字符串，否则日志将无法打印。不建议使用中文字符，可能出现乱码或对齐问题。  **起始版本：** 8 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [int OH\_LOG\_Print(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, ...)](capi-log-h.md#oh_log_print) | - | 写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参。 |
| [int OH\_LOG\_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*message)](capi-log-h.md#oh_log_printmsg) | - | 写日志接口。输出指定type、level、domain、tag的常量日志字符串。 |
| [int OH\_LOG\_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char \*tag, size\_t tagLen, const char \*message, size\_t messageLen)](capi-log-h.md#oh_log_printmsgbylen) | - | 写日志接口。输出指定domain、tag和日志级别的常量日志字符串，需要指定tag及字符串长度，和OH\_LOG\_PrintMsg区别是可以接受不带结束符的字符串。 |
| [int OH\_LOG\_VPrint(LogType type, LogLevel level, unsigned int domain, const char \*tag, const char \*fmt, va\_list ap)](capi-log-h.md#oh_log_vprint) | - | 写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参，变参为va\_list类型。 |
| [bool OH\_LOG\_IsLoggable(unsigned int domain, const char \*tag, LogLevel level)](capi-log-h.md#oh_log_isloggable) | - | 检查指定业务领域、TAG、级别的日志是否可以打印。 |
| [typedef void (\*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char \*tag, const char \*msg)](capi-log-h.md#logcallback) | LogCallback | 函数指针，开发者自定义回调函数内容，在回调函数中，可自行对hilog日志进行处理。 |
| [void OH\_LOG\_SetCallback(LogCallback callback)](capi-log-h.md#oh_log_setcallback) | - | 注册函数。调用此函数后，用户实现的回调函数可以接收当前进程的所有hilog日志。  请注意，无论是否调用该接口，它都不会更改当前进程的hilog日志的默认行为。 |
| [void OH\_LOG\_SetMinLogLevel(LogLevel level)](capi-log-h.md#oh_log_setminloglevel) | - | 设置应用日志打印的最低日志级别，用于拦截低级别日志打印。 |
| [void OH\_LOG\_SetLogLevel(LogLevel level, PreferStrategy prefer)](capi-log-h.md#oh_log_setloglevel) | - | 设置当前应用程序进程的最低日志级别。可以配置不同的偏好策略。 |

注意

如果设置的日志级别低于[全局日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)，OH\_LOG\_SetMinLogLevel()设置不生效。

debug版本应用下，OH\_LOG\_SetMinLogLevel()和OH\_LOG\_SetLogLevel()函数均不生效。

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### LogType

PhonePC/2in1TabletTVWearable

```
1. enum LogType
```

**描述**

日志类型。该枚举类型用于定义应用开发者可以使用的日志类型。当前有应用日志LOG\_APP。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| LOG\_APP = 0 | 应用日志 |

### LogLevel

PhonePC/2in1TabletTVWearable

```
1. enum LogLevel
```

**描述**

日志级别。该枚举类型用于定义日志级别。各级别建议使用方式：

DEBUG：比INFO级别更详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位分析问题。DEBUG级别的日志在正式发布版本中默认不会被打印，只有在调试版本或打开调试开关的情况下才会打印。

INFO：用来记录业务关键流程节点，可以还原业务的主要运行过程；用来记录非正常情况信息，但这些情况都是可以预期的(如无网络信号、登录失败等)。这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。

WARN：发生了较为严重的非预期情况，但是对用户影响不大，程序可以自动恢复或通过简单的操作就可以恢复的问题。

ERROR：程序或功能发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。

FATAL：重大致命异常，表明程序或功能即将崩溃，故障无法恢复。

**起始版本：** 8

| 枚举项 | 描述 |
| --- | --- |
| LOG\_DEBUG = 3 | DEBUG日志级别，使用OH\_LOG\_DEBUG接口打印。 |
| LOG\_INFO = 4 | INFO日志级别，使用OH\_LOG\_INFO接口打印。 |
| LOG\_WARN = 5 | WARN日志级别，使用OH\_LOG\_WARN接口打印。 |
| LOG\_ERROR = 6 | ERROR日志级别，使用OH\_LOG\_ERROR接口打印。 |
| LOG\_FATAL = 7 | FATAL日志级别，使用OH\_LOG\_FATAL接口打印。 |

### PreferStrategy

PhonePC/2in1TabletTVWearable

```
1. enum PreferStrategy
```

**描述**

偏好策略。在[OH\_LOG\_SetLogLevel](capi-log-h.md#oh_log_setloglevel)中使用。不同策略，实际生效的最低日志级别也不同。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| UNSET\_LOGLEVEL = 0 | 清除设置, 实际生效的最低日志级别是系统控制的最低级别。 |
| PREFER\_CLOSE\_LOG = 1 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较大值。 |
| PREFER\_OPEN\_LOG = 2 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较小值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_LOG\_Print()

PhonePC/2in1TabletTVWearable

```
1. int OH_LOG_Print(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, ...)
```

**描述**

写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogType](capi-log-h.md#logtype) type | 日志类型，三方应用日志类型为LOG\_APP。 |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |
| unsigned int domain | 日志业务领域，16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| const char \*fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 大于等于0表示成功；小于0表示失败。  失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。 |

### OH\_LOG\_PrintMsg()

PhonePC/2in1TabletTVWearable

```
1. int OH_LOG_PrintMsg(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *message)
```

**描述**

写日志接口。输出指定type、level、domain、tag的常量日志字符串。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogType](capi-log-h.md#logtype) type | 日志类型，三方应用日志类型为LOG\_APP。 |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |
| unsigned int domain | 日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| const char \*message | 常量日志字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 大于等于0表示成功；小于0表示失败。  失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。 |

### OH\_LOG\_PrintMsgByLen()

PhonePC/2in1TabletTVWearable

```
1. int OH_LOG_PrintMsgByLen(LogType type, LogLevel level, unsigned int domain, const char *tag, size_t tagLen, const char *message, size_t messageLen)
```

**描述**

写日志接口。输出指定domain、tag和日志级别的常量日志字符串，需要指定tag及字符串长度，和OH\_LOG\_PrintMsg区别是可以接受不带结束符的字符串。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogType](capi-log-h.md#logtype) type | 日志类型，三方应用日志类型为LOG\_APP。 |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |
| unsigned int domain | 日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| size\_t tagLen | tag长度。 |
| const char \*message | 常量日志字符串。 |
| size\_t messageLen | 常量字符串长度，小于3500。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 大于等于0表示成功；小于0表示失败。  失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。 |

### OH\_LOG\_VPrint()

PhonePC/2in1TabletTVWearable

```
1. int OH_LOG_VPrint(LogType type, LogLevel level, unsigned int domain, const char *tag, const char *fmt, va_list ap)
```

**描述**

写日志接口。指定日志类型、日志级别、业务领域、TAG，按照类printf格式类型和隐私指示确定需要输出的变参，变参为va\_list类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogType](capi-log-h.md#logtype) type | 日志类型，三方应用日志类型为LOG\_APP。 |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |
| unsigned int domain | 日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| const char \*fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中符号后类型前增加{public}、{private}标识。 |
| va\_list ap | va\_list类型，与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 大于等于0表示成功；小于0表示失败。  失败原因：LogLevel传入的级别低于当前允许打印的级别、domain超出范围、tag为空指针、以及CPU高负载、低内存、整机日志量过大等场景下日志写入socket失败。 |

### OH\_LOG\_IsLoggable()

PhonePC/2in1TabletTVWearable

```
1. bool OH_LOG_IsLoggable(unsigned int domain, const char *tag, LogLevel level)
```

**描述**

检查指定业务领域、TAG、级别的日志是否可以打印。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| unsigned int domain | 日志业务领域，16进制整数，范围0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果指定domain、tag、level日志可以打印则返回true；否则返回false。 |

### OH\_LOG\_DEBUG()

PhonePC/2in1TabletTVWearable

```
1. OH_LOG_DEBUG(type, ...)((void)OH_LOG_Print((type), LOG_DEBUG, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

DEBUG级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| type | 日志类型，三方应用日志类型为[LOG\_APP](capi-log-h.md#logtype)。 |
| fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**参考：**

[OH\_LOG\_Print](capi-log-h.md#oh_log_print)

### OH\_LOG\_INFO()

PhonePC/2in1TabletTVWearable

```
1. OH_LOG_INFO(type, ...)((void)OH_LOG_Print((type), LOG_INFO, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

INFO级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| type | 日志类型，三方应用日志类型为LOG\_APP。 |
| fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**参考：**

[OH\_LOG\_Print](capi-log-h.md#oh_log_print)

### OH\_LOG\_WARN()

PhonePC/2in1TabletTVWearable

```
1. OH_LOG_WARN(type, ...)((void)OH_LOG_Print((type), LOG_WARN, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

WARN级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| type | 日志类型，三方应用日志类型为[LOG\_APP](capi-log-h.md#logtype)。 |
| fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**参考：**

[OH\_LOG\_Print](capi-log-h.md#oh_log_print)

### OH\_LOG\_ERROR()

PhonePC/2in1TabletTVWearable

```
1. OH_LOG_ERROR(type, ...)((void)OH_LOG_Print((type), LOG_ERROR, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

ERROR级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| type | 日志类型，三方应用日志类型为[LOG\_APP](capi-log-h.md#logtype)。 |
| fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**参考：**

[OH\_LOG\_Print](capi-log-h.md#oh_log_print)

### OH\_LOG\_FATAL()

PhonePC/2in1TabletTVWearable

```
1. OH_LOG_FATAL(type, ...)((void)OH_LOG_Print((type), LOG_FATAL, LOG_DOMAIN, LOG_TAG, __VA_ARGS__))
```

**描述**

FATAL级别写日志，宏封装接口。使用时需要先定义LOG\_DOMAIN和LOG\_TAG，一般在源文件起始处统一定义一次。

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| type | 日志类型，三方应用日志类型为[LOG\_APP](capi-log-h.md#logtype)。 |
| fmt | 格式化字符串，基于类printf格式的增强，支持隐私参数标识，即在格式字符串每个参数中'%'符号后类型前增加{public}、{private}标识。 |
| ... | 与格式字符串里参数类型对应的参数列表，参数数目、参数类型必须与格式字符串中的标识一一对应。 |

**参考：**

[OH\_LOG\_Print](capi-log-h.md#oh_log_print)

### LogCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*LogCallback)(const LogType type, const LogLevel level, const unsigned int domain, const char *tag, const char *msg)
```

**描述**

函数指针，开发者自定义回调函数内容，在回调函数中，可自行对hilog日志进行处理。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const LogType](capi-log-h.md#logtype) type | 日志类型，三方应用日志类型为[LOG\_APP](capi-log-h.md#logtype)。 |
| [const LogLevel](capi-log-h.md#loglevel) level | 日志级别，日志级别包括LOG\_DEBUG、LOG\_INFO、LOG\_WARN、LOG\_ERROR、LOG\_FATAL。 |
| const unsigned int domain | 日志业务领域，16进制整数，范围为0x0~0xFFFF，超出范围则日志无法打印。 |
| const char \*tag | 日志TAG，字符串，标识调用所在的类或者业务。tag最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| const char \*msg | 日志内容，格式化之后的日志字符串。 |

### OH\_LOG\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_LOG_SetCallback(LogCallback callback)
```

**描述**

注册函数。调用此函数后，用户实现的回调函数可以接收当前进程的所有hilog日志。

请注意，无论是否调用该接口，它都不会更改当前进程的hilog日志的默认行为。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogCallback](capi-log-h.md#logcallback) callback | 用户实现的回调函数。如果不需要处理hilog日志，可以传输空指针。 |

### OH\_LOG\_SetMinLogLevel()

PhonePC/2in1TabletTVWearable

```
1. void OH_LOG_SetMinLogLevel(LogLevel level)
```

**描述**

设置应用日志打印的最低日志级别，用于拦截低级别日志打印。

注意：

1. 如果设置的日志级别低于[全局日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)，设置不生效。
2. debug版本应用下，此函数不生效。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别。 |

### OH\_LOG\_SetLogLevel()

PhonePC/2in1TabletTVWearable

```
1. void OH_LOG_SetLogLevel(LogLevel level, PreferStrategy prefer)
```

**描述**

设置当前应用程序进程的最低日志级别。

可通过prefer参数配置不同的偏好策略。如果选择策略PREFER\_CLOSE\_LOG，等同于调用OH\_LOG\_SetMinLogLevel。

注意：debug版本应用下，此函数不生效。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [LogLevel](capi-log-h.md#loglevel) level | 日志级别。 |
| [PreferStrategy](capi-log-h.md#preferstrategy) prefer | 偏好策略。 |
