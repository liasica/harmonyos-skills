---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-lighteffectoptions
title: ArkUI_LightEffectOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_LightEffectOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95b07865fd91ddc4445fb6eac77f4788f40ac6cee08bb8654d351ca77880bcc7
---

```c
typedef struct ArkUI_LightEffectOptions ArkUI_LightEffectOptions
```

## 概述

定义沉浸式材质的光感交互效果配置对象，用于配置沉浸式材质在用户交互时产生的光感响应效果。详细设计逻辑请参见[native\_material.h](capi-native-material-h.md)。沉浸式材质是一种具有深度感和层次感的视觉材质风格，光感交互效果指用户与组件交互时产生的光影视觉反馈。创建后需通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect)将配置对象设置到沉浸式材质对象上才能生效。

未指定光感交互颜色时，默认光感交互颜色为白色（0xffffffff）。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_material.h](capi-native-material-h.md)
