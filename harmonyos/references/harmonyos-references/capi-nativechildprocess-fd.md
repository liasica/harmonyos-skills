---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd
title: NativeChildProcess_Fd
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_Fd
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4586543e027d5f9faf75b01c71ab84005b2574a21d97a2d575a2fe3a7c80a674
---

```c
typedef struct {...} NativeChildProcess_Fd
```

## 概述

传递给子进程的文件描述符信息。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* fdName | 文件描述符的键，最大长度为20字符。 |
| int32\_t fd | 文件描述符的值。 |
| struct [NativeChildProcess\_Fd](capi-nativechildprocess-fd.md)\* next | 指向下一个文件描述符结构体的指针。 |
