---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2
title: ArkUI_NativeDialogAPI_2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NativeDialogAPI_2
category: harmonyos-references
scraped_at: 2026-04-28T08:04:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5edc9f11ff9e24a2b7b5f780749bb3a76debe527c7adfe5e33d80ab0556a8c66
---

```
1. typedef struct {...} ArkUI_NativeDialogAPI_2
```

## 概述

PhonePC/2in1TabletTVWearable

ArkUI提供的Native侧自定义弹窗接口集合。

**起始版本：** 15

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_dialog.h](capi-native-dialog-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogAPI\_1](capi-arkui-nativemodule-arkui-nativedialogapi-1.md) nativeDialogAPI1 | ArkUI提供的Native侧自定义弹窗接口集合，范围是[ArkUI\_NativeDialogAPI\_1](capi-arkui-nativemodule-arkui-nativedialogapi-1.md)。  **起始版本：** 15 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*setKeyboardAvoidDistance)(ArkUI\_NativeDialogHandle handle, float distance, ArkUI\_LengthMetricUnit unit)](capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setkeyboardavoiddistance) | 弹窗避让键盘后，和键盘之间距离。 |
| [int32\_t (\*setLevelMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_LevelMode levelMode)](capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setlevelmode) | 设置弹窗的显示层级。 |
| [int32\_t (\*setLevelUniqueId)(ArkUI\_NativeDialogHandle handle, int32\_t uniqueId)](capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setleveluniqueid) | 设置弹窗显示层级页面下的节点id。 |
| [int32\_t (\*setImmersiveMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_ImmersiveMode immersiveMode)](capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setimmersivemode) | 设置嵌入式弹窗蒙层的显示区域。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### setKeyboardAvoidDistance()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setKeyboardAvoidDistance)(ArkUI_NativeDialogHandle handle, float distance, ArkUI_LengthMetricUnit unit)
```

**描述：**

弹窗避让键盘后，和键盘之间距离。

说明

setKeyboardAvoidDistance方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| float distance | 避让键盘的距离，单位为vp。 |
| [ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit) unit | 避让距离的单位，参数类型[ArkUI\_LengthMetricUnit](capi-native-type-h.md#arkui_lengthmetricunit)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](capi-native-type-h.md#arkui_errorcode) 接口初始化错误。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setLevelMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setLevelMode)(ArkUI_NativeDialogHandle handle, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

说明

setLevelMode方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode) levelMode | 显示层级的枚举值， 类型为[ArkUI\_LevelMode](capi-native-dialog-h.md#arkui_levelmode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setLevelUniqueId()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setLevelUniqueId)(ArkUI_NativeDialogHandle handle, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

说明

setLevelUniqueId方法需要在调用[setLevelMode](capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setlevelmode)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| int32\_t uniqueId | 指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |

### setImmersiveMode()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*setImmersiveMode)(ArkUI_NativeDialogHandle handle, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

说明

setImmersiveMode方法需要在调用[show](capi-arkui-nativemodule-arkui-nativedialogapi-1.md#show)方法之前调用。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeDialogHandle](capi-arkui-nativemodule-arkui-nativedialog8h.md) handle | 指向自定义弹窗控制器的指针。 |
| [ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode) immersiveMode | 显示区域类型的枚举值， 类型为[ArkUI\_ImmersiveMode](capi-native-dialog-h.md#arkui_immersivemode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 错误码。  [ARKUI\_ERROR\_CODE\_NO\_ERROR](capi-native-type-h.md#arkui_errorcode) 成功。  [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](capi-native-type-h.md#arkui_errorcode) 函数参数异常。 |
