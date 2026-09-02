---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist
title: NativeChildProcess_FdList
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_FdList
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fa14bac9f7f89c5002cf437063f01e346d57690a1fe2a8f6529a3c743eea3727
---

```c
typedef struct NativeChildProcess_FdList {...} NativeChildProcess_FdList
```

## 概述

传递给子进程的文件描述符信息列表，文件描述符记录个数不能超过16个，超过限制将导致创建子进程失败。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [NativeChildProcess\_Fd](capi-nativechildprocess-fd.md)\* head | 子进程文件描述符记录链表中的第一个记录。 |
