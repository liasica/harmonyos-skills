---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-avscreencapture-contentfilter
title: OH_AVScreenCapture_ContentFilter
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVScreenCapture_ContentFilter
category: harmonyos-references
scraped_at: 2026-09-02T14:53:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:52a9872688577f7dd4f7307585ec1ba8ee291309de0bcd854d125168f3bee630
---

```c
typedef struct OH_AVScreenCapture_ContentFilter OH_AVScreenCapture_ContentFilter
```

## 概述

通过OH\_AVScreenCapture\_ContentFilter过滤音视频内容。开发者可以配置过滤规则，实现对屏幕录制内容中音视频流的筛选和控制，满足不同场景下的内容处理需求。

适用于隐私保护（如过滤敏感界面）、指定应用音视频排除等场景，可有效提升录屏内容的可控性。

**起始版本：** 12

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)
