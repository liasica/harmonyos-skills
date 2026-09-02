---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-smart-gesture-shortcut
title: 智慧手势响应
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 智慧手势响应
category: harmonyos-references
scraped_at: 2026-09-02T14:51:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0589f5e23ea3d1e8441e5f8ac09b414bb52ee1aab22692308a44bc57057f6b8c
---

智慧手势响应用于配置组件是否响应智慧手势、是否展示并保留选中态以及响应优先级，适用于需要控制组件在智慧手势操作中是否可被选中或优先响应的场景，可提升智慧手势交互中目标组件响应的可控性。

**起始版本：** 26.0.0

## smartGestureShortcut

smartGestureShortcut(options?: SmartGestureShortcutOptions): T

设置组件智慧手势响应行为。该属性仅用于声明组件是否响应智慧手势，不会直接触发点击、滚动、翻页或返回等动作。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SmartGestureShortcutOptions](ts-universal-attributes-smart-gesture-shortcut.md#smartgestureshortcutoptions) | 否 | 组件智慧手势响应配置。  SmartGestureShortcutOptions中enabled用于配置组件是否响应智慧手势。  selectable用于设置组件被智慧手势操作选中后是否展示并保留选中态。  action用于设置智慧手势响应优先级，当前仅支持GestureShortcut.PRIMARY，会使组件在智慧手势支持的操作中作为首选响应目标，例如滑动、点击。  建议显式传入，避免因缺省配置导致预期不一致，缺省配置处理参考[SmartGestureShortcutOptions](ts-universal-attributes-smart-gesture-shortcut.md#smartgestureshortcutoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用属性方法。 |

**示例：**

参考智慧手势控制器[示例1（启用智慧手势并自定义动作处理）](arkts-apis-uicontext-smartgesturecontroller.md#示例1启用智慧手势并自定义动作处理)。

## SmartGestureShortcutOptions

智慧手势响应行为配置对象。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| action | [GestureShortcut](ts-appendix-enums.md#gestureshortcut) | 否 | 是 | 智慧手势响应优先级。当前仅支持GestureShortcut.PRIMARY，表示组件在智慧手势的滑动，点击等操作中作为首选响应目标。  默认值为GestureShortcut.PRIMARY。 |
| enabled | boolean | 否 | 是 | 当前组件是否响应智慧手势。  true表示组件响应智慧手势，false表示组件不响应智慧手势。  默认值为false。 |
| selectable | boolean | 否 | 是 | 组件被智慧手势操作选中后是否展示并保留选中态。  true表示显示选中框，false表示不显示选中框。  当enabled为true时，默认值为true；当enabled为false时，默认值为false。 |
