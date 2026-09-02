---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h
title: native_interface.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:56c084ee6698b0e2e705f026b3da2fdc3827456a4e33b6d4d7c33acddf918c3f
---

## 概述

提供NativeModule接口的统一入口函数，用于初始化C-API环境、获取指定类型的Native模块接口集合，以及获取最新一次的报错信息。

**引用文件：** <arkui/native\_interface.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeNodeInterfaceSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeNodeInterfaceSample)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind) | ArkUI\_NativeAPIVariantKind | 定义Native接口集合类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [void\* OH\_ArkUI\_QueryModuleInterfaceByName(ArkUI\_NativeAPIVariantKind type, const char\* structName)](capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname) | 需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。 |
| [const char\* OH\_ArkUI\_NativeModule\_GetErrorMessage()](capi-native-interface-h.md#oh_arkui_nativemodule_geterrormessage) | 获取最新一次的报错信息，包括错误码、方法名称和错误原因。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)](capi-native-interface-h.md#oh_arkui_getmoduleinterface) | 初始化C-API环境，并基于结构体类型获取对应结构体指针。 |

## 枚举类型说明

### ArkUI\_NativeAPIVariantKind

```c
enum ArkUI_NativeAPIVariantKind
```

**描述：**

定义Native接口集合类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NATIVE\_NODE = 0 | UI组件相关接口类型，详见[native\_node.h](capi-native-node-h.md)中的[结构体](capi-native-node-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_DIALOG = 1 | 弹窗相关接口类型，详见[native\_dialog.h](capi-native-dialog-h.md)中的[结构体](capi-native-dialog-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_GESTURE = 2 | 手势相关接口类型，详见[native\_gesture.h](capi-native-gesture-h.md)中的[结构体](capi-native-gesture-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_ANIMATE = 3 | 动画相关接口类型，详见[native\_animate.h](capi-native-animate-h.md)中的[结构体](capi-native-animate-h.md#结构体)类型定义。 |
| ARKUI\_MULTI\_THREAD\_NATIVE\_NODE = 4 | 多线程UI组件相关接口类型，详见[native\_node.h](capi-native-node-h.md)中的[结构体](capi-native-node-h.md#结构体)类型定义。  **起始版本：** 22 |

## 函数说明

### OH\_ArkUI\_QueryModuleInterfaceByName()

```c
void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName)
```

**描述：**

需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind) type | ArkUI提供的Native接口集合大类，例如UI组件接口类：ARKUI\_NATIVE\_NODE，手势类：ARKUI\_NATIVE\_GESTURE。 |
| const char\* structName | Native接口结构体的名称，可通过查询对应头文件内的结构体定义获取，例如位于[native\_node.h](capi-native-node-h.md)中的"ArkUI\_NativeNodeAPI\_1"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 返回Native接口抽象指针，在转换为具体类型后进行使用。 |

### OH\_ArkUI\_GetModuleInterface()

```c
#define OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)                     \
do {                                                                                                 \
        void* anyNativeAPI = OH_ArkUI_QueryModuleInterfaceByName(nativeAPIVariantKind, #structType); \
        if (anyNativeAPI) {                                                                          \
            structPtr = (structType*)(anyNativeAPI);                                                 \
        }                                                                                            \
    } while (0)
```

**描述：**

初始化C-API环境，并基于结构体类型获取对应结构体指针。

适用于已确定Native接口集合类型和接口结构体类型，需要获取具体Native接口结构体指针以调用ArkUI Native C API的场景。此宏函数接收[ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind)类型枚举参数nativeAPIVariantKind、结构体类型参数structType、结构体指针变量structPtr；structPtr需与structType类型匹配。该宏调用[OH\_ArkUI\_QueryModuleInterfaceByName](capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname)初始化C-API环境并获取Native接口抽象指针，转换为structType\*类型后赋值给structPtr。

**起始版本：** 12

### OH\_ArkUI\_NativeModule\_GetErrorMessage()

```c
const char* OH_ArkUI_NativeModule_GetErrorMessage()
```

**描述：**

获取最新一次的报错信息，包括错误码、方法名称和错误原因。错误码相关信息请参考[ArkUI\_ErrorCode](capi-arkui-nativemodule-arkui-error-code-h.md#arkui_errorcode)。当其他接口返回错误码时，会保存对应的报错信息，通过此接口可获取当前存储的报错信息。返回的字符串是由系统创建的线程局部全局字符串，不得修改其内容。如需任何编辑，请自行创建字符串内容的副本。该接口返回的信息可能随版本演进而变化，仅用于输出以辅助分析与故障排查，不应作为逻辑判断依据。返回的报错信息无需手动释放。

**起始版本：** 26.0.0

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 最新一次的报错信息，包括错误码、方法名称和错误原因。 |
