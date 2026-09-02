---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-embedded-component-h
title: embedded_component.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > embedded_component.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4c01beb0e93e101d518f92f75a66a4d51ad1eacc0fa0988708f6cb093389b73d
---

## 概述

声明EmbeddedComponent组件选项（ArkUI\_EmbeddedComponentOption）相关的结构体和方法。开发者可通过这些方法创建、销毁组件选项对象，并为EmbeddedComponent组件设置运行异常回调（onError）和正常退出回调（onTerminated）。适用于需要在应用中嵌入EmbeddedUIExtensionAbility组件并管理其生命周期、监听运行异常与正常退出事件的应用场景，帮助开发者灵活处理组件运行过程中的状态变化。

**引用文件：** <arkui/node\_attributes/embedded\_component.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [embedded\_component\_sample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/UIExtensionAndAccessibility)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md) | AbilityBase\_Want | 声明元能力Want结构。 |
| [ArkUI\_EmbeddedComponentOption](capi-arkui-nativemodule-arkui-embeddedcomponentoption.md) | ArkUI\_EmbeddedComponentOption | 为EmbeddedComponent定义参数EmbeddedComponentOption。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_EmbeddedComponentOption\* OH\_ArkUI\_EmbeddedComponentOption\_Create()](capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_create) | - | 创建EmbeddedComponent组件选项的对象。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_Dispose(ArkUI\_EmbeddedComponentOption\* option)](capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_dispose) | - | 销毁EmbeddedComponent组件选项的对象。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnError(ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, const char\* name, const char\* message))](capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_setonerror) | - | 设置EmbeddedComponent组件的onError回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。 |
| [void OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated(ArkUI\_EmbeddedComponentOption\* option, void (\*callback)(int32\_t code, AbilityBase\_Want\* want))](capi-embedded-component-h.md#oh_arkui_embeddedcomponentoption_setonterminated) | - | 设置EmbeddedComponent组件的onTerminated回调。EmbeddedComponent组件正常退出时触发本回调。 |

## 函数说明

### OH\_ArkUI\_EmbeddedComponentOption\_Create()

```c
ArkUI_EmbeddedComponentOption* OH_ArkUI_EmbeddedComponentOption_Create()
```

**描述：**

创建EmbeddedComponent组件选项的对象。返回的对象需要在不再使用时通过OH\_ArkUI\_EmbeddedComponentOption\_Dispose销毁。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](capi-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* | 返回指向EmbeddedComponent组件选项的对象的指针。 |

### OH\_ArkUI\_EmbeddedComponentOption\_Dispose()

```c
void OH_ArkUI_EmbeddedComponentOption_Dispose(ArkUI_EmbeddedComponentOption* option)
```

**描述：**

销毁EmbeddedComponent组件选项的对象。该对象必须由OH\_ArkUI\_EmbeddedComponentOption\_Create创建，销毁后不应再使用该对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](capi-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | 要销毁的EmbeddedComponent组件选项的对象的指针，不能为空，必须为OH\_ArkUI\_EmbeddedComponentOption\_Create()创建的有效对象。 |

### OH\_ArkUI\_EmbeddedComponentOption\_SetOnError()

```c
void OH_ArkUI_EmbeddedComponentOption_SetOnError(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, const char* name, const char* message))
```

**描述：**

设置EmbeddedComponent组件的[onError](ts-container-embedded-component.md#onerror)回调。EmbeddedComponent组件在运行过程中发生异常时触发本回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](capi-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | EmbeddedComponent组件选项的对象的指针。 |
| void (\*callback)(int32\_t code, const char\* name, const char\* message) | 开发者自定义回调函数。不设置该回调时，EmbeddedComponent组件在运行过程中发生异常时不触发回调。  - code：组件运行发生异常时返回的错误码信息。错误码的详细介绍请参考[UIExtension错误码](errorcode-uiextension.md)。  - name：组件运行发生异常时返回的名称信息。  - message：组件运行发生异常时返回的详细信息。 |

### OH\_ArkUI\_EmbeddedComponentOption\_SetOnTerminated()

```c
void OH_ArkUI_EmbeddedComponentOption_SetOnTerminated(ArkUI_EmbeddedComponentOption* option, void (*callback)(int32_t code, AbilityBase_Want* want))
```

**描述：**

设置EmbeddedComponent组件的[onTerminated](ts-container-embedded-component.md#onterminated)回调。EmbeddedComponent组件正常退出时触发本回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_EmbeddedComponentOption](capi-arkui-nativemodule-arkui-embeddedcomponentoption.md)\* option | EmbeddedComponent组件选项的对象的指针。 |
| void (\*callback)(int32\_t code, [AbilityBase\_Want](capi-arkui-nativemodule-abilitybase-want.md)\* want) | 开发者自定义回调函数。不设置该回调时，EmbeddedComponent组件正常退出时不触发回调。  - code：被拉起的[EmbeddedUIExtensionAbility](js-apis-app-ability-embeddeduiextensionability.md)退出时返回的结果码。若EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](js-apis-app-ability-uiextensioncontentsession.md#terminateselfwithresult)退出，结果码为EmbeddedUIExtensionAbility设置的值。若EmbeddedUIExtensionAbility通过调用[terminateSelf](js-apis-app-ability-uiextensioncontentsession.md#terminateself)退出，结果码为默认值"0"。  - want：被拉起的EmbeddedUIExtensionAbility退出时返回的数据。若EmbeddedUIExtensionAbility通过调用[terminateSelfWithResult](js-apis-app-ability-uiextensioncontentsession.md#terminateselfwithresult)退出，返回的数据为EmbeddedUIExtensionAbility设置的数据。若EmbeddedUIExtensionAbility通过调用[terminateSelf](js-apis-app-ability-uiextensioncontentsession.md#terminateself)退出，返回的数据为默认值。 |
