---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-material-h
title: native_material.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_material.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1885e6edd3d90f2391fe6a19661fbb5677956fc1f86361b004b466ee931063d9
---

## 概述

提供ArkUI（方舟UI框架）在Native侧的沉浸式材质类型和API声明，用于实现半透明模糊背景、光感交互反馈等沉浸式UI效果。

**引用文件：** <arkui/native\_material.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**起始版本：** 26.0.0

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ImmersiveStyle](capi-native-material-h.md#arkui_immersivestyle) | ArkUI\_ImmersiveStyle | 沉浸式材质样式，取值范围见[ArkUI\_ImmersiveStyle](capi-native-material-h.md#arkui_immersivestyle)。传入无效样式将导致创建失败返回NULL。不同样式对应不同的材质参数，影响材质的薄厚程度和透明度。 |
| [ArkUI\_MaterialLevel](capi-native-material-h.md#arkui_materiallevel) | ArkUI\_MaterialLevel | 材质等级枚举，与设备的算力等级相关。使用[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)可获取当前设备的材质等级。 |

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_ImmersiveMaterial](capi-arkui-nativemodule-arkui-immersivematerial.md) | ArkUI\_ImmersiveMaterial | 定义Native侧的沉浸式材质对象。沉浸式材质根据设备算力等级分为不同等级。材质等级由[ArkUI\_MaterialLevel](capi-native-material-h.md#arkui_materiallevel)定义，可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取。在高算力和中算力设备上，会影响材质层的滤镜效果和阴影（[NODE\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_shadow)或[NODE\_CUSTOM\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_custom_shadow)）效果。在低算力设备上，会影响背景颜色[NODE\_BACKGROUND\_COLOR](capi-native-node-h-nodeattributetype-common.md#node_background_color)、边框颜色[NODE\_BORDER\_COLOR](capi-native-node-h-nodeattributetype-layoutattributes.md#node_border_color)、边框宽度[NODE\_BORDER\_WIDTH](capi-native-node-h-nodeattributetype-layoutattributes.md#node_border_width)和阴影（[NODE\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_shadow)或[NODE\_CUSTOM\_SHADOW](capi-native-node-h-nodeattributetype-animator.md#node_custom_shadow)）效果。 |
| [ArkUI\_ImmersiveMaterial\*](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) | ArkUI\_ImmersiveMaterialHandle | 定义指向沉浸式材质对象的指针，沉浸式材质用于实现沉浸式视觉效果。可以通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Create](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_create)创建沉浸式材质对象。可以通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_destroy)接口销毁沉浸式材质对象。待销毁的沉浸式材质对象应是通过OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Create创建的有效对象。 |
| [ArkUI\_LightEffectOptions](capi-arkui-nativemodule-arkui-lighteffectoptions.md) | ArkUI\_LightEffectOptions | 定义沉浸式材质的光感交互效果配置对象，用于配置沉浸式材质在用户交互时产生的光感响应效果。创建后需通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect)将配置对象设置到沉浸式材质对象上才能生效。创建时默认光感交互颜色为白色（0xffffffff）。 |
| [ArkUI\_LightEffectOptions\*](capi-arkui-nativemodule-arkui-lighteffectoptionshandle.md) | ArkUI\_LightEffectOptionsHandle | 定义指向光感交互效果配置对象的指针，开发者通过该指针可配置和管理沉浸式材质的光感交互效果参数。可以通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_create)创建光感交互效果配置对象。可以通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_destroy)接口销毁光感交互效果配置对象。待销毁的光感交互效果配置对象应是通过OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create创建的有效对象。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [bool OH\_ArkUI\_NativeModule\_GetSystemMaterialSupported()](capi-native-material-h.md#oh_arkui_nativemodule_getsystemmaterialsupported) | - | 检查当前设备是否支持系统材质（即设备系统内置的材质渲染能力）。如果返回true，则可以使用[NODE\_SYSTEM\_MATERIAL](capi-native-node-h-nodeattributetype-animator.md#node_system_material)属性，否则设置该属性将无效。该配置项由设备定义，不可修改。 |
| [ArkUI\_MaterialLevel OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel()](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel) | - | 获取全局材质等级，与设备的算力相关。该配置项由设备定义，不可修改。 |
| [ArkUI\_ImmersiveMaterialHandle OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Create(ArkUI\_ImmersiveStyle style)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_create) | - | 创建具有指定样式的沉浸式材质对象。创建的材质等级跟随全局材质等级，可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取。建议在使用前先调用[OH\_ArkUI\_NativeModule\_GetSystemMaterialSupported](capi-native-material-h.md#oh_arkui_nativemodule_getsystemmaterialsupported)检查设备是否支持系统材质，若设备不支持系统材质，通过[NODE\_SYSTEM\_MATERIAL](capi-native-node-h-nodeattributetype-animator.md#node_system_material)属性设置材质将无效。 |
| [void OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Destroy(ArkUI\_ImmersiveMaterialHandle material)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_destroy) | - | 销毁沉浸式材质对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetStyle(ArkUI\_ImmersiveMaterialHandle material, ArkUI\_ImmersiveStyle style)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setstyle) | - | 设置沉浸式材质对象的样式。该参数仅对高算力和中算力设备的滤镜和阴影显示效果有效，对低算力设备不生效但不会报错。在低算力设备上，材质会影响背景颜色、边框等属性，不受样式参数控制。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetStyle(ArkUI\_ImmersiveMaterialHandle material, ArkUI\_ImmersiveStyle\* style)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_getstyle) | - | 获取沉浸式材质对象的样式。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetMaterialColor(ArkUI\_ImmersiveMaterialHandle material, uint32\_t color)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setmaterialcolor) | - | 设置沉浸式材质对象的材质颜色。该参数对所有算力设备的滤镜和阴影显示效果有效。如果不设置，默认值为0，表示透明色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetMaterialColor(ArkUI\_ImmersiveMaterialHandle material, uint32\_t\* color)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_getmaterialcolor) | - | 获取沉浸式材质对象的材质颜色。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetApplyShadow(ArkUI\_ImmersiveMaterialHandle material, bool applyShadow)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setapplyshadow) | - | 设置沉浸式材质对象是否应用阴影。该参数对所有等级材质都生效。当该参数为true时，材质中的阴影效果生效，优先于阴影通用属性，适用于使用材质自带阴影的场景。当该参数为false时，阴影通用属性生效，材质无阴影效果，适用于需要使用自定义阴影效果替代材质阴影的场景。如果不设置，默认值为true。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetApplyShadow(ArkUI\_ImmersiveMaterialHandle material, bool\* applyShadow)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_getapplyshadow) | - | 获取沉浸式材质对象是否应用阴影。如果从未显式设置过该属性，将返回默认值true。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetInteractive(ArkUI\_ImmersiveMaterialHandle material, bool interactive)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setinteractive) | - | 设置沉浸式材质对象是否可交互形变。该参数对所有等级材质都生效。当该参数为true时，材质可交互形变。当该参数为false时，材质不可交互形变。如果不设置，遵循组件的行为。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetInteractive(ArkUI\_ImmersiveMaterialHandle material, bool\* interactive)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_getinteractive) | - | 获取沉浸式材质对象的可交互形变属性。如果从未设置过该属性，请先调用OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetInteractive设置该属性后再获取。，函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_LightEffectOptionsHandle OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create()](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_create) | - | 创建光感交互效果配置对象，用于配置沉浸式材质的触摸高亮反馈效果。默认颜色为白色（0xffffffff）。 |
| [void OH\_ArkUI\_NativeModule\_LightEffectOptions\_Destroy(ArkUI\_LightEffectOptionsHandle options)](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_destroy) | - | 销毁光感交互效果配置对象。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_LightEffectOptions\_SetColor(ArkUI\_LightEffectOptionsHandle options, uint32\_t color)](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_setcolor) | - | 设置光感交互效果的颜色。如果不设置，默认颜色为白色（0xffffffff）。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect(ArkUI\_ImmersiveMaterialHandle material, const ArkUI\_LightEffectOptionsHandle options)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect) | - | 设置沉浸式材质对象的光感交互效果。该参数对所有等级材质都生效。传入NULL的光感交互效果配置指针表示禁用光感交互效果，传入非NULL的光感交互效果配置指针表示使用该配置参数进行光感交互。非NULL的光感交互效果配置指针可通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_create)创建，并可通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_SetColor](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_setcolor)设置颜色。如果不调用该接口设置，光感交互效果遵循组件的行为。 |
| [ArkUI\_ErrorCode OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetLightEffectColor(ArkUI\_ImmersiveMaterialHandle material, uint32\_t\* color)](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_getlighteffectcolor) | - | 获取沉浸式材质对象的光感交互效果颜色。只有在调用[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect)成功设置非NULL的光感交互效果配置指针后，此接口才能成功获取颜色值。如果从未设置过光感交互效果或已禁用（传入NULL的光感交互效果配置指针），函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

## 枚举类型说明

### ArkUI\_ImmersiveStyle

```c
enum ArkUI_ImmersiveStyle
```

沉浸式材质样式枚举。不同样式对应不同的材质参数，影响材质的薄厚程度。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_IMMERSIVE\_STYLE\_ULTRA\_THIN = 0 | 超薄样式。材质层极薄，透明度效果极强。 |
| ARKUI\_IMMERSIVE\_STYLE\_THIN = 1 | 薄样式。材质层较薄，透明度效果强。 |
| ARKUI\_IMMERSIVE\_STYLE\_REGULAR = 2 | 常规样式。材质层厚度标准，视觉效果均衡。 |
| ARKUI\_IMMERSIVE\_STYLE\_THICK = 3 | 厚样式。模糊效果强。 |
| ARKUI\_IMMERSIVE\_STYLE\_ULTRA\_THICK = 4 | 超厚样式。材质层极厚，模糊效果极强。 |

### ArkUI\_MaterialLevel

```c
enum ArkUI_MaterialLevel
```

材质等级枚举，与设备的算力等级相关。

使用[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)可获取当前设备的材质等级。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_MATERIAL\_LEVEL\_EXQUISITE = 0 | 高算力设备材质等级。 |
| ARKUI\_MATERIAL\_LEVEL\_GENTLE = 1 | 中算力设备材质等级。 |
| ARKUI\_MATERIAL\_LEVEL\_SMOOTH = 2 | 低算力设备材质等级。 |

## 函数说明

### OH\_ArkUI\_NativeModule\_GetSystemMaterialSupported()

```c
bool OH_ArkUI_NativeModule_GetSystemMaterialSupported()
```

**描述：**

检查当前设备是否支持系统材质（即设备系统内置的材质渲染能力）。

如果返回true，则可以使用[NODE\_SYSTEM\_MATERIAL](capi-native-node-h-nodeattributetype-animator.md#node_system_material)属性，否则设置该属性将无效。该配置项由设备定义，不可修改。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回当前设备是否支持系统材质。true表示当前设备支持系统材质，false表示当前设备不支持系统材质。 |

### OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel()

```c
ArkUI_MaterialLevel OH_ArkUI_NativeModule_GetGlobalMaterialLevel()
```

**描述：**

获取全局材质等级，与设备的算力相关。该配置项由设备定义，不可修改。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_MaterialLevel](capi-native-material-h.md#arkui_materiallevel) | 返回设备的材质等级。  [ARKUI\_MATERIAL\_LEVEL\_EXQUISITE](capi-native-material-h.md#arkui_materiallevel)（0）：高算力设备材质等级。  [ARKUI\_MATERIAL\_LEVEL\_GENTLE](capi-native-material-h.md#arkui_materiallevel)（1）：中算力设备材质等级。  [ARKUI\_MATERIAL\_LEVEL\_SMOOTH](capi-native-material-h.md#arkui_materiallevel)（2）：低算力设备材质等级。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Create()

```c
ArkUI_ImmersiveMaterialHandle OH_ArkUI_NativeModule_ImmersiveMaterial_Create(ArkUI_ImmersiveStyle style)
```

**描述：**

创建具有指定样式的沉浸式材质对象。创建的材质等级跟随全局材质等级，可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveStyle](capi-native-material-h.md#arkui_immersivestyle) style | 材质样式。传入无效样式将导致设置失败，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)错误码。该样式仅对高算力和中算力设备的显示效果有效，对低算力设备不生效但不会报错。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) | 返回指向创建的沉浸式材质对象的指针。如果创建失败或材质样式无效，返回NULL。  返回的对象使用完后需要通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_destroy)释放。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_Destroy()

```c
void OH_ArkUI_NativeModule_ImmersiveMaterial_Destroy(ArkUI_ImmersiveMaterialHandle material)
```

**描述：**

销毁沉浸式材质对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetStyle()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_SetStyle(ArkUI_ImmersiveMaterialHandle material, ArkUI_ImmersiveStyle style)
```

**描述：**

设置沉浸式材质对象的样式。该参数仅对高算力和中算力设备的显示效果有效，对低算力设备不生效但不会报错。可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取当前设备的材质等级以判断该参数是否生效。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。  material为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| [ArkUI\_ImmersiveStyle](capi-native-material-h.md#arkui_immersivestyle) style | 材质样式。传入无效样式将导致设置失败，返回[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或style无效），请确保传入有效的material指针和有效的style枚举值。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetStyle()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_GetStyle(ArkUI_ImmersiveMaterialHandle material, ArkUI_ImmersiveStyle* style)
```

**描述：**

获取沉浸式材质对象的样式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| [ArkUI\_ImmersiveStyle](capi-native-material-h.md#arkui_immersivestyle)\* style | 指向用于接收材质样式的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或style为NULL），请确保material和style均为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetMaterialColor()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_SetMaterialColor(ArkUI_ImmersiveMaterialHandle material, uint32_t color)
```

**描述：**

设置沉浸式材质对象的材质颜色。该参数对所有算力设备的显示效果有效。可通过[OH\_ArkUI\_NativeModule\_GetGlobalMaterialLevel](capi-native-material-h.md#oh_arkui_nativemodule_getglobalmateriallevel)获取当前设备的材质等级以判断该参数是否生效。如果不设置，默认值为0，表示透明色。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。  material为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| uint32\_t color | 材质颜色，0xAARRGGBB格式，对所有算力设备的显示效果有效。传入0表示透明（默认值）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL），请确保material为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetMaterialColor()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_GetMaterialColor(ArkUI_ImmersiveMaterialHandle material, uint32_t* color)
```

**描述：**

获取沉浸式材质对象的材质颜色。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| uint32\_t\* color | 指向用于接收0xAARRGGBB格式的材质颜色的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或color为NULL），请确保material和color均为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetApplyShadow()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_SetApplyShadow(ArkUI_ImmersiveMaterialHandle material, bool applyShadow)
```

**描述：**

设置沉浸式材质对象是否应用阴影。该参数对所有等级材质都生效。

当该参数为true时，材质中的阴影效果生效，优先于阴影通用属性。当该参数为false时，阴影通用属性生效，材质无阴影效果。如果不设置，默认值为true。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| bool applyShadow | 是否添加材质效果的阴影。true表示材质阴影生效并优先于阴影通用属性，false表示不添加材质阴影、阴影通用属性生效。默认值为true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL），请确保material为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetApplyShadow()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_GetApplyShadow(ArkUI_ImmersiveMaterialHandle material, bool* applyShadow)
```

**描述：**

获取沉浸式材质对象是否应用阴影。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| bool\* applyShadow | 指向用于接收是否应用阴影的变量的指针。如果从未显式设置过该属性，该指针将接收默认值true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或applyShadow为NULL），请确保material和applyShadow均为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetInteractive()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_SetInteractive(ArkUI_ImmersiveMaterialHandle material, bool interactive)
```

**描述：**

设置沉浸式材质对象是否可交互形变。即材质在用户交互（如触摸、按压）时是否产生视觉形变响应。该参数对所有等级材质都生效。

当该参数为true时，材质可交互形变。当该参数为false时，材质不可交互形变。如果不设置，遵循组件的行为。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| bool interactive | 材质是否可交互形变。true表示材质可交互形变，false表示材质不可交互形变。如果不设置，遵循组件的行为。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL），请确保material为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetInteractive()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_GetInteractive(ArkUI_ImmersiveMaterialHandle material, bool* interactive)
```

**描述：**

获取沉浸式材质对象的可交互形变属性。建议先通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetInteractive](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setinteractive)设置该属性后再调用本接口获取，如果从未设置过该属性，函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。  material为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |
| bool\* interactive | 指向用于接收材质是否可交互形变的变量的指针。  interactive为NULL时，返回错误码[ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或interactive为NULL），请确保material和interactive均为有效指针。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 从未设置过该属性。请先调用OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetInteractive设置该属性后再获取。 |

### OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create()

```c
ArkUI_LightEffectOptionsHandle OH_ArkUI_NativeModule_LightEffectOptions_Create()
```

**描述：**

创建光感交互效果配置对象，用于配置沉浸式材质的触摸高亮反馈效果。默认颜色为白色（0xffffffff）。创建完成后，需通过[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect)将配置对象设置到沉浸式材质对象上才能生效。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_LightEffectOptionsHandle](capi-arkui-nativemodule-arkui-lighteffectoptionshandle.md) | 返回指向创建的光感交互效果配置对象的指针。返回的对象使用完后需要通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Destroy](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_destroy)释放。 |

### OH\_ArkUI\_NativeModule\_LightEffectOptions\_Destroy()

```c
void OH_ArkUI_NativeModule_LightEffectOptions_Destroy(ArkUI_LightEffectOptionsHandle options)
```

**描述：**

销毁光感交互效果配置对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LightEffectOptionsHandle](capi-arkui-nativemodule-arkui-lighteffectoptionshandle.md) options | 指向光感交互效果配置对象的指针。 |

### OH\_ArkUI\_NativeModule\_LightEffectOptions\_SetColor()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_LightEffectOptions_SetColor(ArkUI_LightEffectOptionsHandle options, uint32_t color)
```

**描述：**

设置光感交互效果的颜色。如果不设置，默认颜色为白色（0xffffffff）。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_LightEffectOptionsHandle](capi-arkui-nativemodule-arkui-lighteffectoptionshandle.md) options | 指向光感交互效果配置对象的指针。 |
| uint32\_t color | 光感交互效果颜色，0xAARRGGBB格式。如果不设置，默认颜色为白色（0xffffffff）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（options为NULL），请确保options为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_SetLightEffect(ArkUI_ImmersiveMaterialHandle material, const ArkUI_LightEffectOptionsHandle options)
```

**描述：**

设置沉浸式材质对象的光感交互效果，即在材质表面呈现随用户交互动态变化的光效反射。该参数对所有等级材质都生效。

传入NULL的光感交互效果配置指针表示禁用光感交互效果，适用于纯展示性材质表面场景；传入非NULL的光感交互效果配置指针表示使用该配置参数进行光感交互，适用于需要增强触摸视觉反馈的交互式组件场景。如果不调用该接口设置，光感交互效果遵循组件的行为。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| const [ArkUI\_LightEffectOptionsHandle](capi-arkui-nativemodule-arkui-lighteffectoptionshandle.md) options | 指向光感交互效果配置对象的指针。传入NULL禁用光感交互效果，传入非NULL启用。非NULL指针需通过[OH\_ArkUI\_NativeModule\_LightEffectOptions\_Create](capi-native-material-h.md#oh_arkui_nativemodule_lighteffectoptions_create)创建。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL），请确保material为有效指针。 |

### OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_GetLightEffectColor()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_ImmersiveMaterial_GetLightEffectColor(ArkUI_ImmersiveMaterialHandle material, uint32_t* color)
```

**描述：**

获取沉浸式材质对象的光感交互效果颜色。

只有在调用[OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect](capi-native-material-h.md#oh_arkui_nativemodule_immersivematerial_setlighteffect)成功设置非NULL的光感交互效果配置指针后，此接口才能成功获取颜色值。如果从未设置过光感交互效果或已禁用（传入NULL的光感交互效果配置指针），函数将返回[ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_ImmersiveMaterialHandle](capi-arkui-nativemodule-arkui-immersivematerialhandle.md) material | 指向沉浸式材质对象的指针。 |
| uint32\_t\* color | 指向用于接收0xAARRGGBB格式的光感交互效果颜色的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) | [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 操作成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 参数异常（material为NULL或color为NULL），请确保material和color均为有效指针。  [ARKUI\_ERROR\_CODE\_PARAM\_ERROR](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode) 光感交互效果从未设置或已禁用，请先调用OH\_ArkUI\_NativeModule\_ImmersiveMaterial\_SetLightEffect设置非NULL的光感交互效果配置指针后再获取颜色。 |
