---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo
title: AVSession_OutputDeviceInfo
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_OutputDeviceInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:12:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed97770ea3911876351dd4135d22d7f6543b64be81969dd1d24ef5de0e8f2bdd
---

```
1. struct AVSession_OutputDeviceInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

目标设备信息的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_deviceinfo.h](capi-native-deviceinfo-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 设备信息数组的大小。 |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*\*deviceInfos | 设备信息数组。 |
