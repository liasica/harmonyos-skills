---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativebridge-hms-nativebridge-ongoinginfo
title: HMS_NativeBridge_OnGoingInfo
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > C API > 结构体 > HMS_NativeBridge_OnGoingInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:56:12+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b2a38a8c94bb60a39337432a7cbfbcbb8098b6c38cda4db8025c275d718cff84
---

```c
typedef struct {...} HMS_NativeBridge_OnGoingInfo
```

## 概述

控制小图标显示状态的信息结构体。

**起始版本：** 26.0.1

**相关模块：** [NativeBridge](capi-nativebridge.md)

**所在头文件：** [wear\_engine\_slim.h](capi-wear-engine-slim-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool showStatus | 后台运行的应用是否以小图标形式在前台显示。true表示显示，false表示隐藏/不显示。  **起始版本：** 26.0.1 |
| const char \*packName | 应用的包名。  **起始版本：** 26.0.1 |
| int32\_t showTime | 小图标在前台显示时长，单位为分钟。  **起始版本：** 26.0.1 |
| const char \*iconPath | 小图标的路径。  **起始版本：** 26.0.1 |
| [HMS\_NativeBridge\_InstallerCallback](capi-wear-engine-slim-h.md#hms_nativebridge_installercallback) callBack | 回调函数，用于通知调用方小图标显示时长已到期，即将隐藏。  **起始版本：** 26.0.1 |
