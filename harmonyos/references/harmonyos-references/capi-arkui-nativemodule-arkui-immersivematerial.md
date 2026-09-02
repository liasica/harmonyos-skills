---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-immersivematerial
title: ArkUI_ImmersiveMaterial
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ImmersiveMaterial
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:316a6ffce827678d144286746a3c008067ce6ff99a1f86aead31fb1216dbc1f9
---

```c
typedef struct ArkUI_ImmersiveMaterial ArkUI_ImmersiveMaterial
```

## 概述

定义Native侧的沉浸式材质对象，根据设备算力等级提供适配的视觉效果。

沉浸式材质的等级根据设备算力等级而不同。

材质等级由[ArkUI\_MaterialLevel](capi-native-material-h.md#arkui_materiallevel)定义，可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取。

在高算力和中算力设备上，会影响沉浸式材质渲染层的滤镜效果和阴影（[NODE\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_shadow)或[NODE\_CUSTOM\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_custom_shadow)）效果。在低算力设备上，会影响背景颜色[NODE\_BACKGROUND\_COLOR](capi-native-node-h-nodeattributetype-common.md#node_background_color)、边框颜色[NODE\_BORDER\_COLOR](capi-native-node-h-nodeattributetype-layoutattributes.md#node_border_color)、边框宽度[NODE\_BORDER\_WIDTH](capi-native-node-h-nodeattributetype-layoutattributes.md#node_border_width)和阴影（[NODE\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_shadow)或[NODE\_CUSTOM\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_custom_shadow)）效果。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_material.h](capi-native-material-h.md)
