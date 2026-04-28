---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-windowmanager-windowmanager-windowsnapshotconfig
title: WindowManager_WindowSnapshotConfig
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_WindowSnapshotConfig
category: harmonyos-references
scraped_at: 2026-04-28T08:04:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0c41ea59b64e737865aa5e0eb4de8ed38c25d1df4bccd3b8152c65e3076b0005
---

```
1. typedef struct {...} WindowManager_WindowSnapshotConfig
```

## 概述

PhonePC/2in1TabletTVWearable

主窗口截图的配置项。

**起始版本：** 21

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool useCache | 是否使用主窗口的已有截图。默认值为true。 true表示使用主窗口的已有截图，若主窗口无保存的截图，则使用主窗口的最新截图。false表示使用主窗口的最新截图。 |
