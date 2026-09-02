---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-concurrentinfo
title: Camera_ConcurrentInfo
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > C API > 结构体 > Camera_ConcurrentInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26285645ba07eeff96e2d28480d57300ac2f80a7f72291975f609450e9750e98
---

```c
typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```

## 概述

相机并发能力信息。

**起始版本：** 18

**相关模块：** [OH\_Camera](capi-oh-camera.md)

**所在头文件：** [camera.h](capi-camera-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera\_Device](capi-oh-camera-camera-device.md) camera | 相机实例。 |
| [Camera\_ConcurrentType](capi-camera-h.md#camera_concurrenttype) type | 相机并发状态。 |
| [Camera\_SceneMode](capi-camera-h.md#camera_scenemode)\* sceneModes | 相机并发支持的模式。 |
| [Camera\_OutputCapability](capi-oh-camera-camera-outputcapability.md)\* outputCapabilities | 相机输出能力集。 |
| uint32\_t modeAndCapabilitySize | 相机输出能力集大小。 |
