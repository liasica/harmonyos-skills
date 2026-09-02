---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo
title: NativeDisplayManager_DisplaysInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplaysInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6da4bb06bd05b6321433c573808b8fc683b2aa058b383d0fe14160ee81c6a05c
---

```c
typedef struct {...} NativeDisplayManager_DisplaysInfo
```

## 概述

多显示设备的Display对象。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t displaysLength | 多显示设备Display对象的数组长度。 |
| [NativeDisplayManager\_DisplayInfo](capi-nativedisplaymanager-displayinfo.md)\* displaysInfo | 多显示设备Display对象的属性。 |
