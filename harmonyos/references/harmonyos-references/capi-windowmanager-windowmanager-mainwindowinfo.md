---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-mainwindowinfo
title: WindowManager_MainWindowInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > WindowManager_MainWindowInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6ae019a2dcb9f02b2d2062a45c77322a7b9911037d155baf67a9eb6ac238dfbb
---

```c
typedef struct {...} WindowManager_MainWindowInfo
```

## 概述

主窗口信息。

**起始版本：** 21

**相关模块：** [WindowManager](capi-windowmanager.md)

**所在头文件：** [oh\_window\_comm.h](capi-oh-window-comm-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t displayId | 主窗口所在的屏幕ID。 |
| int32\_t windowId | 主窗口ID。 |
| bool showing | 主窗口的前后台状态。true表示主窗口在前台，false表示主窗口不在前台。 |
| const char\* label | 主窗口任务名称。 |
