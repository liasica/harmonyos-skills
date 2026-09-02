---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resourcemanager-resourcemanager-configuration
title: ResourceManager_Configuration
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > ResourceManager_Configuration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b42ec824580c8cff652a5b3a0af2bd626245c7372c1548707f66062884df1dfd
---

```c
typedef struct ResourceManager_Configuration {...} ResourceManager_Configuration
```

## 概述

设备状态的结构体。

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

**所在头文件：** [resmgr\_common.h](capi-resmgr-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [ResourceManager\_Direction](capi-resmgr-common-h.md#resourcemanager_direction) direction | 表示屏幕方向。 |
| char\* locale | 表示语言、文字、国家或地区，如zh\_Hans\_CN。 |
| [ResourceManager\_DeviceType](capi-resmgr-common-h.md#resourcemanager_devicetype) deviceType | 表示设备类型。 |
| [ScreenDensity](capi-resmgr-common-h.md#screendensity) screenDensity | 表示屏幕密度。 |
| [ResourceManager\_ColorMode](capi-resmgr-common-h.md#resourcemanager_colormode) colorMode | 表示颜色模式。 |
| uint32\_t mcc | 表示移动国家码。 |
| uint32\_t mnc | 表示移动网络码。 |
| uint32\_t reserved[20] | 保留属性。 |
