---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-resourcemanager-resourcemanager-configuration
title: ResourceManager_Configuration
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > ResourceManager_Configuration
category: harmonyos-references
scraped_at: 2026-04-28T08:06:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:911e1a2aefe91149a442a30ba55486360b6260eed8fa37bbf41911d192b22694
---

```
1. typedef struct ResourceManager_Configuration {...} ResourceManager_Configuration
```

## 概述

PhonePC/2in1TabletTVWearable

设备状态的枚举。

**起始版本：** 12

**相关模块：** [resourcemanager](capi-resourcemanager.md)

**所在头文件：** [resmgr\_common.h](capi-resmgr-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| ResourceManager\_Direction direction | 表示屏幕方向。 |
| char\* locale | 表示语言文字国家地区，如zh-Hans-CN。 |
| ResourceManager\_DeviceType deviceType | 表示设备类型。 |
| ScreenDensity screenDensity | 表示屏幕密度。 |
| ResourceManager\_ColorMode colorMode | 表示颜色模式。 |
| uint32\_t mcc | 表示移动国家码。 |
| uint32\_t mnc | 表示移动网络码。 |
| uint32\_t reserved[20] | 保留属性。 |
