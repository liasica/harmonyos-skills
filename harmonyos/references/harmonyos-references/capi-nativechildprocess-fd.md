---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd
title: NativeChildProcess_Fd
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_Fd
category: harmonyos-references
scraped_at: 2026-04-28T07:59:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42ba70dcbf1214f3f1f39bd8f0329e59f19bc34f29a556c16b28ed8edccdbdf6
---

```
1. typedef struct {...} NativeChildProcess_Fd
```

## 概述

PhonePC/2in1TabletTVWearable

传递给子进程的文件描述符信息。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* fdName | 文件描述符的键，最大长度为20字符。 |
| int32\_t fd | 文件描述符的值。 |
| struct [NativeChildProcess\_Fd](capi-nativechildprocess-fd.md)\* next | 下一个文件描述记录指针。 |
