---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-immersive-light-sense-enable
title: 开启沉浸光感
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 沉浸光感 > 沉浸光感开发指导 > 开启沉浸光感
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:01+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:d5b464792f6fd949c668a52ad332fa8d9b3a93018794a97a3db189ce4765c292
---

沉浸光感提供应用级开启和组件级开启两种方式，可按需选择。沉浸光感开启后，需要大量GPU资源，具体的适配指导请参考[沉浸光感功耗优化](arkts-immersive-light-sense-constraints.md)，其余开启后的常见问题请参考[沉浸光感常见问题](arkts-immersive-light-sense-faq.md)。

**说明** 

* 开启沉浸光感，要确保应用的[targetAPIVersion](app-configuration-file.md)不低于26.0.0。如需适配低版本，请参考[沉浸光感兼容性适配](arkts-immersive-light-sense-compatibility.md)。
* 沉浸光感开启后，

  弹窗类组件（AlertDialog、ActionSheet、CustomDialog、CalendarPickerDialog、DatePickerDialog、TimePickerDialog、TextPickerDialog、SelectionMenu、AlphabetIndexer弹窗、Text设置copyOption后长按或双击触发的文本菜单）和弹窗类接口（PromptAction、ArkUI\_NativeDialog、@ohos.promptAction (弹窗)、Popup控制、Tips控制、菜单控制、半模态转场）以及按钮与选择类组件（Slider、Toggle、Select）可在页面内全部区域生效。

  其他组件仅在Navigation/NavDestination标题栏或横向Tab中barPosition为BarPosition.End的底部TabBar中生效。在其他区域中设置沉浸光感效果不生效。
* 沉浸式系统材质反色、材质赋色、交互形变与点光源、阴影开关等个性化配置，具体请参见[沉浸式系统材质视效](arkts-immersive-light-sense-common-capability.md)。

## 沉浸光感开启方式对比

不同开启方式对比如下：

| 开启方式 | 支持的组件 | 说明 |
| --- | --- | --- |
| 应用级开启 | 组件清单详见[MaterialState](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)。 | 支持通过如下两种方式开启：  1. 通过[module.json5](module-configuration-file.md)统一配置，为支持沉浸光感的组件，批量开启或全局禁用沉浸光感，具体开启方法请参考表格下方内容。  2. module.json5未配置该字段时即为default模式，开发者的应用从API版本26.0.0之前升级至API版本26.0.0及以上，在未主动设置沉浸光感的情况下，组件默认开启沉浸光感，无需任何配置。 |
| 组件级开启 | 支持设置沉浸式系统材质的组件 | 支持通过如下三种方式开启：  1. 通过通用属性[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)设置。  2. 弹窗类组件通过options参数中的systemMaterial字段设置，例如Toast的[ShowToastOptions](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)、自定义弹窗的[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)等。  3. 组件专属接口设置，例如Select下拉菜单的[menuSystemMaterial](../harmonyos-references/ts-basic-components-select.md#menusystemmaterial)、Navigation标题栏的[systemMaterial](../harmonyos-references/ts-basic-components-navigation.md#navigationtitleoptions11)等。  各组件详细适配方法请参考[组件适配沉浸光感](arkts-immersive-light-sense-component-adaptation.md)。 |

应用级开启通过配置文件统一设置应用的沉浸光感开关。在[module.json5](module-configuration-file.md)中，将[metadata](module-configuration-file.md#metadata标签)参数的name字段配置为"ohos.arkui.UIMaterial.state"，value字段为default或enable时开启，字段为disable时关闭。该配置仅在entry类型的module中生效。

以下示例展示如何在[module.json5](module-configuration-file.md)中配置enable模式：

```json5
{
  "module": {
    "name": "entry",
    "type": "entry",
    // ...
    "metadata": [{
      "name": "ohos.arkui.UIMaterial.state",
      "value": "enable"
    }],
    // ...
  }
}
```

开发者可以通过[uiMaterial.getMaterialInfo()](../harmonyos-references/arkts-apis-uimaterial.md#uimaterialgetmaterialinfo)获取当前应用的沉浸式系统材质配置状态[MaterialState](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)，MaterialState中的[DEFAULT](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)、[ENABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)和[DISABLE](../harmonyos-references/arkts-apis-uimaterial.md#materialstate)，分别对应module.json5配置文件中default、enable和disable三个value值。

**说明** 

* 应用级开关设置为disable时，会全局禁用沉浸光感，应用级或组件级开启的设置均不生效。
* 组件级开启的优先级高于应用级开启，开发者通过组件的沉浸式系统材质接口可以直接覆盖应用级开关开启的组件效果，反之则不会覆盖。

## 关闭沉浸光感

关闭沉浸光感有以下几种方式：

1. 组件级关闭：组件级设置[uiMaterial.Material.empty](../harmonyos-references/arkts-apis-uimaterial.md#empty)。应用级开启和组件级开启两种接入方式均可通过该操作关闭。
2. 应用级关闭：应用级开关设置为disable，只针对应用级开启的组件。

此外，部分组件的沉浸式系统材质由多个独立接口控制。以Select为例，其下拉按钮的沉浸式系统材质通过[systemMaterial](../harmonyos-references/ts-universal-attributes-image-effect.md#systemmaterial)设置，下拉菜单的沉浸式系统材质通过独立的[menuSystemMaterial](../harmonyos-references/ts-basic-components-select.md#menusystemmaterial)接口设置，两者相互独立、可分别开启或关闭。

**说明** 

[uiMaterial.Material.empty](../harmonyos-references/arkts-apis-uimaterial.md#empty)与将systemMaterial属性设置为undefined含义不同：undefined表示恢复为组件默认的沉浸光感效果；uiMaterial.Material.empty是关闭沉浸光感效果。因此，要关闭一个默认开启沉浸光感的组件，应使用uiMaterial.Material.empty。
