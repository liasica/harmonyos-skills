---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-fontconfigs
title: OH_ArkUI_FontConfigs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_FontConfigs
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:03379f9c496e182280141d56f2d289bb55f8f6021e2ef41168ba7966b8fc06a7
---

```c
typedef struct OH_ArkUI_FontConfigs OH_ArkUI_FontConfigs
```

## 概述

定义文本的字体配置，当前支持通过相关接口设置和获取字体粗细配置，适用于需要自定义字体粗细显示效果的场景。可以通过[OH\_ArkUI\_FontConfigs\_Create](capi-text-h.md#oh_arkui_fontconfigs_create)接口创建字体配置对象，通过[OH\_ArkUI\_FontConfigs\_Destroy](capi-text-h.md#oh_arkui_fontconfigs_destroy)接口销毁字体配置对象。配置创建后，可通过以下接口进行设置和查询：通过[OH\_ArkUI\_FontConfigs\_SetFontWeightConfigs](capi-text-h.md#oh_arkui_fontconfigs_setfontweightconfigs)接口设置字体粗细配置，通过[OH\_ArkUI\_FontConfigs\_GetFontWeightConfigs](capi-text-h.md#oh_arkui_fontconfigs_getfontweightconfigs)接口获取字体粗细配置。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [text.h](capi-text-h.md)
