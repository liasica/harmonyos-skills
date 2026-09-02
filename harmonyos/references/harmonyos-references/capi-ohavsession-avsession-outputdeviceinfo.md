---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohavsession-avsession-outputdeviceinfo
title: AVSession_OutputDeviceInfo
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 结构体 > AVSession_OutputDeviceInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4193a53ccd1edced6b899c792d605ceb075b070ea0e8a724554d020b4e41f0ef
---

```c
typedef struct AVSession_OutputDeviceInfo {...} AVSession_OutputDeviceInfo
```

## 概述

输出设备信息的定义。

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

**所在头文件：** [native\_deviceinfo.h](capi-native-deviceinfo-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 设备信息数组的大小，表示deviceInfos数组的元素数量。 |
| [AVSession\_DeviceInfo](capi-ohavsession-avsession-deviceinfo.md) \*\*deviceInfos | 指向设备信息数组的指针，数组长度由size字段指定。 |
