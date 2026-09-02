---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-shadowoptions
title: OH_ArkUI_ShadowOptions
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_ShadowOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5366669f8645a9edeba5b52fc645ba23321fe9ff1edb9f0786dfc24c1e4c3b16
---

```c
typedef struct OH_ArkUI_ShadowOptions OH_ArkUI_ShadowOptions
```

## 概述

定义阴影选项，用于设置组件的阴影效果，包括阴影颜色、偏移量、模糊半径、阴影类型、是否填充等属性。

调用[OH\_ArkUI\_ShadowOptions\_Create](capi-native-type-visual-h.md#oh_arkui_shadowoptions_create)接口创建对应的阴影选项对象。

调用[OH\_ArkUI\_ShadowOptions\_Destroy](capi-native-type-visual-h.md#oh_arkui_shadowoptions_destroy)接口销毁阴影选项对象。

对象创建后，调用OH\_ArkUI\_ShadowOptions\_SetXXX系列接口设置生效的具体样式。例如调用[OH\_ArkUI\_ShadowOptions\_SetRadius](capi-native-type-visual-h.md#oh_arkui_shadowoptions_setradius)设置阴影模糊半径。若创建对象失败（返回空指针），调用SetXXX系列接口将不会生效。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type\_visual.h](capi-native-type-visual-h.md)
