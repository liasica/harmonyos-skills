---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-xcomponent-h
title: xcomponent.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > xcomponent.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a6d605fc20e05b1b1f1f99f8582e013b55d326d43cb344404d23274eb9f2814
---

## 概述

XComponent组件枚举类型定义，用于描述XComponent的渲染类型，支持EGL/OpenGLES绘制及媒体数据写入场景，可满足开发者定制内容单独或与组件合成展示的渲染需求。

**引用文件：** <arkui/node\_attributes/xcomponent.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [xcomponent\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/XComponent3D)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_XComponentType](capi-xcomponent-h.md#arkui_xcomponenttype) | ArkUI\_XComponentType | 定义XComponent类型枚举值。 |

## 枚举类型说明

### ArkUI\_XComponentType

```c
enum ArkUI_XComponentType
```

**描述：**

定义XComponent类型枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_XCOMPONENT\_TYPE\_SURFACE = 0 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容单独显示在屏幕上。 |
| ARKUI\_XCOMPONENT\_TYPE\_TEXTURE = 2 | 用于EGL/OpenGLES和媒体数据写入，开发者定制绘制内容和XComponent组件内容合成后显示在屏幕上。 |
