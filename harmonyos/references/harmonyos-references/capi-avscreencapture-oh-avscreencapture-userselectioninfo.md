---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-userselectioninfo
title: OH_AVScreenCapture_UserSelectionInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCapture_UserSelectionInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afdda6ba80e4de57186fa309cee639e82dbed9c2551aec1e16f7f29c8b5faa27
---

```c
typedef struct OH_AVScreenCapture_UserSelectionInfo OH_AVScreenCapture_UserSelectionInfo
```

## 概述

开发者可通过OH\_AVScreenCapture\_UserSelectionInfo获取用户在授权界面（选择界面）选择的参数（如捕获类型，捕获窗口等）。例如，在屏幕录制应用中，用户可以选择录制区域、录制音频源等参数后，使用该结构体获取用户的选择结果。

该结构体用于在屏幕录制授权流程中承载用户的选择结果，开发者可在授权完成后通过此结构体读取用户的授权选择信息。适用于应用需要根据用户授权选择来配置录屏行为的场景，帮助开发者灵活适配用户的录屏偏好。

**起始版本：** 20

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)
