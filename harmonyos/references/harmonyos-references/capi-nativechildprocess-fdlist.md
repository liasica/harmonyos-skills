---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist
title: NativeChildProcess_FdList
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_FdList
category: harmonyos-references
scraped_at: 2026-04-28T07:59:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4153784179c6421a7b58869db2a5dee335fb2042f8d470758162f687502aa280
---

```
1. typedef struct NativeChildProcess_FdList {...} NativeChildProcess_FdList
```

## 概述

PhonePC/2in1TabletTVWearable

传递给子进程的文件描述符信息列表，文件描述符记录个数不能超过16个。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| struct [NativeChildProcess\_Fd](capi-nativechildprocess-fd.md)\* head | 子进程文件描述符记录链表中的第一个记录。 |
