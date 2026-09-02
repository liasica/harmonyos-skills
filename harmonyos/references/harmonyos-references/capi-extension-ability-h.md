---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-extension-ability-h
title: extension_ability.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > extension_ability.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d9b970a2d8740d62a6c195e58e323204c15f7e46063b080b71820afe6f1ba305
---

## 概述

提供ExtensionAbility回调函数类型声明和入口函数名称声明。

**引用文件：** <AbilityKit/ability\_runtime/extension\_ability.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 24

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_ExtensionInstance](capi-abilityruntime-extensioninstance.md) | - | 定义AbilityRuntime\_ExtensionInstance结构体类型。 |
| [AbilityRuntime\_ExtensionInstance\*](capi-abilityruntime-extensioninstance8h.md) | AbilityRuntime\_ExtensionInstanceHandle | 定义AbilityRuntime\_ExtensionInstance对象指针。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void AbilityRuntime\_Extension\_CreateFunc(AbilityRuntime\_ExtensionInstanceHandle handle, const char \*abilityName);](capi-extension-ability-h.md#abilityruntime_extension_createfunc) | AbilityRuntime\_Extension\_CreateFunc | ExtensionAbility中必须实现的回调函数类型，用于实例化ExtensionAbility。 |

### 变量

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_OnNativeExtensionCreate](capi-extension-ability-h.md#oh_abilityruntime_onnativeextensioncreate) | [AbilityRuntime\_Extension\_CreateFunc](capi-extension-ability-h.md#abilityruntime_extension_createfunc) | ExtensionAbility入口函数名称声明。开发者需要实现一个类型为[AbilityRuntime\_Extension\_CreateFunc](capi-extension-ability-h.md#abilityruntime_extension_createfunc)的函数，并将其命名为OH\_AbilityRuntime\_OnNativeExtensionCreate。系统会自动查找并调用此函数来完成ExtensionAbility实例的初始化。  **起始版本：** 24 |

## 函数说明

### AbilityRuntime\_Extension\_CreateFunc()

```c
typedef void AbilityRuntime_Extension_CreateFunc(AbilityRuntime_ExtensionInstanceHandle handle, const char *abilityName)
```

**描述**

ExtensionAbility创建回调函数类型。ExtensionAbility中必须实现的回调函数类型，用于实例化ExtensionAbility。

**起始版本：** 24

**参数：**

| 参数名 | 描述 |
| --- | --- |
| [AbilityRuntime\_ExtensionInstanceHandle](capi-abilityruntime-extensioninstance8h.md) handle | 回调函数传入AbilityRuntime\_ExtensionInstanceHandle实例。 |
| const char \*abilityName | 回调函数传入的ExtensionAbility的名称。 |

## 变量说明

### OH\_AbilityRuntime\_OnNativeExtensionCreate

```c
AbilityRuntime_Extension_CreateFunc OH_AbilityRuntime_OnNativeExtensionCreate
```

**描述**

ExtensionAbility入口函数名称声明。开发者需要实现一个类型为[AbilityRuntime\_Extension\_CreateFunc](capi-extension-ability-h.md#abilityruntime_extension_createfunc)的函数，并将其命名为OH\_AbilityRuntime\_OnNativeExtensionCreate。系统会自动查找并调用此函数来完成ExtensionAbility实例的初始化。

**起始版本：** 24

**示例代码：**

```c
#include <AbilityKit/ability_runtime/extension_ability.h>

extern "C" void OH_AbilityRuntime_OnNativeExtensionCreate(AbilityRuntime_ExtensionInstance *instance,
                                                          const char *abilityName) {
    if (!instance) {
        // 记录错误日志以及其他业务处理
        return;
    }
    // ExtensionAbility 初始化工作
}
```
