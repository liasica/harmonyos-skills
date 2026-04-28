---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-mainwindowinfo
title: WindowManager_MainWindowInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_MainWindowInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:009d55a0b22e070dd590287da978b7f1184a8c9e800af3cc6e64b16a7b1d7a70
---

```
1. typedef struct {...} WindowManager_MainWindowInfo
```

## 概述

PhonePC/2in1TabletTVWearable

主窗口信息。

**起始版本：** 21

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint64\_t displayId | 主窗口所在的屏幕ID。 |
| int32\_t windowId | 主窗口ID。 |
| bool showing | 主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。 |
| const char\* label | 主窗口任务名称。 |
