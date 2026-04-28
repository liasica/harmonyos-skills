---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo
title: NativeDisplayManager_DisplaysInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > NativeDisplayManager_DisplaysInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:04:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:631805f0befbbe5204c316dc2c7c25658d72ab9ae82cc60a97deb3f742ad8555
---

```
1. typedef struct {...} NativeDisplayManager_DisplaysInfo
```

## 概述

PhonePC/2in1TabletTVWearable

多显示设备的Display对象。

**起始版本：** 14

**相关模块：** [OH\_DisplayManager](capi-oh-displaymanager.md)

**所在头文件：** [oh\_display\_info.h](capi-oh-display-info-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t displaysLength | 多显示设备Display对象的长度。 |
| [NativeDisplayManager\_DisplayInfo](capi-nativedisplaymanager-displayinfo.md)\* displaysInfo | 多显示设备Display对象的属性。 |
