---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-options
title: NativeChildProcess_Options
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > NativeChildProcess_Options
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:59ed84df93a472478b15912c6262290e9067ddc5d2f1d1817a91b1fcfb027432
---

```c
typedef struct {...} NativeChildProcess_Options
```

## 概述

启动子进程的配置选项。

**起始版本：** 13

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NativeChildProcess\_IsolationMode](capi-native-child-process-h.md#nativechildprocess_isolationmode) isolationMode | 子进程所采用的隔离模式。 |
| int64\_t reserved | 预留字段，供未来扩展使用。 |
