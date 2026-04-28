---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h
title: native_interface.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_interface.h
category: harmonyos-references
scraped_at: 2026-04-28T08:03:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fdfa90869d3cb6497c28ceb7d9f0f127777d5c4ee65e3bf391fa7e51c7df06e6
---

## 概述

PhonePC/2in1TabletTVWearable

提供NativeModule接口的统一入口函数。

**引用文件：** <arkui/native\_interface.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeNodeInterfaceSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/NativeNodeInterfaceSample)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind) | ArkUI\_NativeAPIVariantKind | 定义Native接口集合类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void\* OH\_ArkUI\_QueryModuleInterfaceByName(ArkUI\_NativeAPIVariantKind type, const char\* structName)](capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname) | 需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_ArkUI\_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)](capi-native-interface-h.md#oh_arkui_getmoduleinterface) | 基于结构体类型获取对应结构体指针的宏函数。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### ArkUI\_NativeAPIVariantKind

PhonePC/2in1TabletTVWearable

```
1. enum ArkUI_NativeAPIVariantKind
```

**描述：**

定义Native接口集合类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NATIVE\_NODE = 0 | UI组件相关接口类型，详见[native\_node.h](capi-native-node-h.md)中的[结构体](capi-native-node-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_DIALOG = 1 | 弹窗相关接口类型，详见[native\_dialog.h](capi-native-dialog-h.md)中的[结构体](capi-native-dialog-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_GESTURE = 2 | 手势相关接口类型，详见[native\_gesture.h](capi-native-gesture-h.md)中的[结构体](capi-native-gesture-h.md#结构体)类型定义。 |
| ARKUI\_NATIVE\_ANIMATE = 3 | 动画相关接口类型。详见[native\_animate.h](capi-native-animate-h.md)中的[结构体](capi-native-animate-h.md#结构体)类型定义。 |
| ARKUI\_MULTI\_THREAD\_NATIVE\_NODE = 4 | 多线程UI组件相关接口类型，详见[native\_node.h](capi-native-node-h.md)中的[结构体](capi-native-node-h.md#结构体)类型定义。  **起始版本：** 22 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_ArkUI\_QueryModuleInterfaceByName()

PhonePC/2in1TabletTVWearable

```
1. void* OH_ArkUI_QueryModuleInterfaceByName(ArkUI_NativeAPIVariantKind type, const char* structName)
```

**描述：**

需调用该函数初始化C-API环境，并获取指定类型的Native模块接口集合。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind) type | ArkUI提供的native接口集合大类，例如UI组件接口类：ARKUI\_NATIVE\_NODE, 手势类：ARKUI\_NATIVE\_GESTURE。 |
| const char\* structName | native接口结构体的名称，通过查询对应头文件内结构体定义，例如位于[native\_node.h](capi-native-node-h.md)中的"ArkUI\_NativeNodeAPI\_1"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 返回native接口抽象指针，在转换为具体类型后进行使用。 |

### OH\_ArkUI\_GetModuleInterface()

PhonePC/2in1TabletTVWearable

```
1. #define OH_ArkUI_GetModuleInterface(nativeAPIVariantKind, structType, structPtr)                     \
2. do {                                                                                                 \
3. void* anyNativeAPI = OH_ArkUI_QueryModuleInterfaceByName(nativeAPIVariantKind, #structType); \
4. if (anyNativeAPI) {                                                                          \
5. structPtr = (structType*)(anyNativeAPI);                                                 \
6. }                                                                                            \
7. } while (0)
```

**描述：**

基于结构体类型获取对应结构体指针的宏函数。此宏函数接收[ArkUI\_NativeAPIVariantKind](capi-native-interface-h.md#arkui_nativeapivariantkind)类型枚举参数nativeAPIVariantKind、const char\*类型参数structType、structType\*类型参数structPtr，调用[OH\_ArkUI\_QueryModuleInterfaceByName](capi-native-interface-h.md#oh_arkui_querymoduleinterfacebyname)获取native接口抽象指针，转换为structType\*类型后赋值给structPtr。

**起始版本：** 12
