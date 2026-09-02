---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-slider-h
title: slider.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > slider.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cdd4a4aa1e78060d1054a6eb9a8108e3e276e42ed24630a91c71aa8734b910a9
---

## 概述

为NativeNode API提供Slider节点类型定义。

**引用文件：** <arkui/node\_attributes/slider.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeTypeSample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_SliderBlockStyle](capi-slider-h.md#arkui_sliderblockstyle) | ArkUI\_SliderBlockStyle | 定义滑块形状。 |
| [ArkUI\_SliderDirection](capi-slider-h.md#arkui_sliderdirection) | ArkUI\_SliderDirection | 定义滑动条滑动方向。 |
| [ArkUI\_SliderStyle](capi-slider-h.md#arkui_sliderstyle) | ArkUI\_SliderStyle | 定义滑块与滑轨显示样式。 |

## 枚举类型说明

### ArkUI\_SliderBlockStyle

```c
enum ArkUI_SliderBlockStyle
```

**描述：**

定义滑块形状。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_DEFAULT = 0 | 使用默认滑块（圆形）。 |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_IMAGE = 1 | 使用图片资源作为滑块。 |
| ARKUI\_SLIDER\_BLOCK\_STYLE\_SHAPE = 2 | 使用自定义形状作为滑块。 |

### ArkUI\_SliderDirection

```c
enum ArkUI_SliderDirection
```

**描述：**

定义滑动条滑动方向。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_DIRECTION\_VERTICAL = 0 | 方向为纵向。 |
| ARKUI\_SLIDER\_DIRECTION\_HORIZONTAL = 1 | 方向为横向。 |

### ArkUI\_SliderStyle

```c
enum ArkUI_SliderStyle
```

**描述：**

定义滑块与滑轨显示样式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_SLIDER\_STYLE\_OUT\_SET = 0 | 滑块在滑轨上。 |
| ARKUI\_SLIDER\_STYLE\_IN\_SET = 1 | 滑块在滑轨内。 |
| ARKUI\_SLIDER\_STYLE\_NONE = 2 | 无滑块。 |
