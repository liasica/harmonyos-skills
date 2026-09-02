---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-immersivematerialhandle
title: ArkUI_ImmersiveMaterial*
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ImmersiveMaterial*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e54ab27bbcbf6478a6afe3b5ab76a7d678022645da474f3ec69bfb71730a9bd4
---

```c
typedef struct ArkUI_ImmersiveMaterial* ArkUI_ImmersiveMaterialHandle
```

## 概述

定义指向沉浸式材质对象的指针，沉浸式材质用于实现沉浸式视觉效果对象。

可以通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Create](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_create)创建沉浸式材质对象，创建后必须在使用完毕时调用[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_destroy)销毁沉浸式材质对象以释放资源，避免内存泄漏。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_material.h](capi-native-material-h.md)
