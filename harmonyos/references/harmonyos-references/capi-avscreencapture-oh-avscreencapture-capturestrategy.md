---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-capturestrategy
title: OH_AVScreenCapture_CaptureStrategy
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCapture_CaptureStrategy
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b213898f4a502edd9b0ab3baa83b9bf5c43785c3ce6b36f0b7d86177d8059afd
---

```c
typedef struct OH_AVScreenCapture_CaptureStrategy OH_AVScreenCapture_CaptureStrategy
```

## 概述

通过OH\_AVScreenCapture\_CaptureStrategy设置录屏策略。用于配置录屏行为，如录制内容范围、输出格式、性能参数等。支持配置录屏参数、调整录制质量、管理录制资源等。

录屏策略需在录屏启动之前通过OH\_AVScreenCapture\_SetCaptureStrategy接口设置，录屏启动后设置将不生效。

支持开发者根据业务需求灵活配置录屏捕获行为，适用于需要定制录屏策略的场景，可提升录屏功能的适用性和可控性。

**起始版本：** 20

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)
