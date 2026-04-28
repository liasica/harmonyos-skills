---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayhdrformat
title: NativeDisplayManager_DisplayHdrFormat
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplayHdrFormat
category: harmonyos-references
scraped_at: 2026-04-28T08:04:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:567552196ecae875343d5a612bb016a34ea77ec1452db38bbc6c558bec56489e
---

```
1. typedef struct {...} NativeDisplayManager_DisplayHdrFormat
```

## 概述

PhonePC/2in1TabletTVWearable

显示设备支持的所有HDR格式。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t hdrFormatLength | 显示设备的HDR格式长度。 |
| uint32\_t\* hdrFormats | 显示设备的HDR格式数据。 |
