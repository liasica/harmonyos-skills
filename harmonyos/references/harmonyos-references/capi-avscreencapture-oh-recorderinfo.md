---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-recorderinfo
title: OH_RecorderInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_RecorderInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:03+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:1194302411cd5dae8238d12eb1382279e6805ea4571ee3278d41c8faf10dc57a
---

```
1. typedef struct OH_RecorderInfo {...} OH_RecorderInfo
```

## 概述

PhonePC/2in1TabletTV

录制文件信息。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| char\* url | 录制文件的URL。 |
| uint32\_t urlLen | 录制文件的URL的长度值。 |
| [OH\_ContainerFormatType](capi-native-avscreen-capture-base-h.md#oh_containerformattype) fileFormat | 录制文件的格式。 |
