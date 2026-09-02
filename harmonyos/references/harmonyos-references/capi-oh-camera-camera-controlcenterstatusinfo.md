---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-controlcenterstatusinfo
title: Camera_ControlCenterStatusInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_ControlCenterStatusInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7cf291f8ba95745cd77e057adde3e553cf3b1043067d32caebadf366a0f445bd
---

```c
typedef struct Camera_ControlCenterStatusInfo {...} Camera_ControlCenterStatusInfo
```

## 概述

控制器效果激活状态信息。

**起始版本：** 20

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_ControlCenterEffectType](capi-camera-h.md#camera_controlcentereffecttype) effectType | 控制器效果类型。 |
| bool isActive | 控制器是否激活。true表示激活，false表示未激活。 |
