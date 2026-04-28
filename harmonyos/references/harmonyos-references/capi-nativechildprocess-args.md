---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args
title: NativeChildProcess_Args
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_Args
category: harmonyos-references
scraped_at: 2026-04-28T07:59:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a02d1ecd71216e326cfb8b5d8d183d5afef4a0ac2ce7a99f0b88661903a4b79b
---

```
1. typedef struct {...} NativeChildProcess_Args
```

## 概述

PhonePC/2in1TabletTVWearable

传递给子进程的参数。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* entryParams | 入口参数，大小不能超过150KB。 |
| struct [NativeChildProcess\_FdList](capi-nativechildprocess-fdlist.md) fdList | 传递给子进程的文件描述符信息列表。 |
