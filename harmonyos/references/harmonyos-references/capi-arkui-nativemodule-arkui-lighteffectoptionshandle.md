---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-lighteffectoptionshandle
title: ArkUI_LightEffectOptions*
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_LightEffectOptions*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d54f0256d6869a14bf60ae7cc920f16fccf19b794b8afb12edebb37b7bd88b36
---

```c
typedef ArkUI_LightEffectOptions* ArkUI_LightEffectOptionsHandle
```

## 概述

定义指向光感交互效果配置对象的指针，开发者通过该指针可配置和管理沉浸式材质的光感交互效果参数。

必须通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_create)创建光感交互效果配置对象，使用完毕后必须调用[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_destroy)接口销毁配置对象以释放资源，销毁后继续使用该指针会导致未定义行为。两者必须配对使用。未调用Destroy销毁对象会导致资源泄漏。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_material.h](capi-native-material-h.md)
