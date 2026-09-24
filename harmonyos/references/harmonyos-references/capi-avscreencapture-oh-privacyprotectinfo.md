---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-privacyprotectinfo
title: OH_PrivacyProtectInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_PrivacyProtectInfo
category: harmonyos-references
scraped_at: 2026-09-25T07:13:24+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:e5b87200bfae25bcb44130f8563a10546b5c5600cc18748d5153faa509677094
---

```c
typedef struct OH_PrivacyProtectInfo {...} OH_PrivacyProtectInfo
```

## 概述

隐私保护信息结构体。

用于在屏幕录制场景中对系统窗口和敏感应用进行隐私保护。systemWindowProtection控制系统窗口级别的隐私保护，sensitiveAppProtection控制敏感应用级别的隐私保护，两者都适用于需要在屏幕录制时保护用户隐私数据的场景。

**起始版本：** 24

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool systemWindowProtection | 是否开启系统窗口隐私保护。true表示开启隐私保护，false表示关闭隐私保护，默认值为true。系统窗口是指系统级应用（如输入法、通知等）的窗口。  **起始版本：** 24 |
| bool sensitiveAppProtection | 是否开启敏感应用的隐私保护。true表示开启隐私保护，false表示关闭隐私保护，默认值为true。敏感应用（如金融类应用）是指包含用户隐私数据的应用。  **起始版本：** 24 |
