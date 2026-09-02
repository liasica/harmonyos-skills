---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-span-h
title: image_span.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > image_span.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:51666c3b3554bd9b895f4ff1af520c3c15097183d7070f22603ab571923dc54a
---

## 概述

定义ImageSpan相关的枚举，用于在富文本中嵌入图片并控制图片与文本的对齐方式。支持多种对齐模式，适用于图文混排场景，可实现图片与文本的精确对齐，提升富文本的展示效果。

**引用文件：** <arkui/node\_attributes/image\_span.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [native\_type\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeType/native_type_sample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ImageSpanAlignment](capi-image-span-h.md#arkui_imagespanalignment) | ArkUI\_ImageSpanAlignment | 定义图片基于文本的对齐方式。 |

## 枚举类型说明

### ArkUI\_ImageSpanAlignment

```c
enum ArkUI_ImageSpanAlignment
```

**描述**

定义图片基于文本的对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BASELINE = 0 | 图片下边沿与文本基线对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_BOTTOM = 1 | 图片下边沿与文本下边沿对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_CENTER = 2 | 图片中间与文本中间对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_TOP = 3 | 图片上边沿与文本上边沿对齐。 |
| ARKUI\_IMAGE\_SPAN\_ALIGNMENT\_FOLLOW\_PARAGRAPH = 4 | 图片对齐方式跟随Text组件对齐方式。  **起始版本：** 20 |
