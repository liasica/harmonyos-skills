---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace
title: NativeDisplayManager_DisplayColorSpace
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayColorSpace
category: harmonyos-references
scraped_at: 2026-04-28T08:04:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b62a3fb61f36971c7fff2d5fdedd957c1109f595f170cb027ab0c77d4f75dede
---

```
1. typedef struct {...} NativeDisplayManager_DisplayColorSpace
```

## 概述

PhonePC/2in1TabletTVWearable

显示设备支持的所有色域类型。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t colorSpaceLength | 显示设备的色域长度。 |
| uint32\_t\* colorSpaces | 显示设备的色域数据。 |
