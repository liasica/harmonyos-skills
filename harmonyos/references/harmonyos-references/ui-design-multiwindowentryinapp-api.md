---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-multiwindowentryinapp-api
title: MultiWindowEntryInAPP
breadcrumb: API参考 > 应用框架 > UI Design Kit（UI设计套件） > ArkTS组件 > MultiWindowEntryInAPP
category: harmonyos-references
scraped_at: 2026-04-29T13:57:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:191755c4c26e89beb05c6ec837268b012e1ce35e4dbe731c350307fe41351c0b
---

说明

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

* 双折叠：展开态。
* 三折叠：双屏态，三屏态的横屏态。
* 平板：横屏态。

对于不支持的设备形态，该组件不可交互，不响应点击事件。

MultiWindowEntryInAPP组件承载单应用多窗口并行逻辑的实现，应用开发者结合本应用业务特点，通过MultiWindowEntryInAPP实现一个应用多个窗口任务并行场景的开发。

**设备行为差异：** 该组件在Phone、Tablet设备中上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：** 6.0.0(20)

## 导入模块

PhonePC/2in1TabletTV

说明

* MultiWindowEntryInAPPAttribute是用于配置MultiWindowEntryInAPP组件属性的关键接口。6.0.1(21)及之前版本，导入MultiWindowEntryInAPP组件后需要开发者手动导入MultiWindowEntryInAPPAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入MultiWindowEntryInAPP组件后，会自动导入MultiWindowEntryInAPPAttribute，无需开发者手动导入。
* 如果开发者手动导入MultiWindowEntryInAPPAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```
1. import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```
1. import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions } from '@kit.UIDesignKit';
```

## 子组件

PhonePC/2in1TabletTV

无

## 接口

PhonePC/2in1TabletTV

MultiWindowEntryInAPP(params: MultiWindowEntryInAPPParams)

创建应用内多窗组件接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [MultiWindowEntryInAPPParams](ui-design-multiwindowentryinapp-api.md#multiwindowentryinappparams) | 是 | 应用内多窗组件参数。 |

## MultiWindowEntryInAPPParams

PhonePC/2in1TabletTV

MultiWindowEntryInAPP组件参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 否 | 否 | 要启动窗口的参数，有以下要求：  1. 必填字段：abilityName, moduleName和bundleName；  2. 应用限制：所有指定的名称（abilityName, moduleName 和bundleName）必须属于当前应用；  3. 跨应用限制：多窗口功能不支持跨应用的能力。 |
| isShowSubtitle | boolean | 否 | 是 | 是否显示组件文本标题。  true：显示默认文本标题。  false：不显示默认文本标题。  默认值：false。 |
| multiWindowEntryInAPPStyle | [MultiWindowEntryInAPPStyle](ui-design-multiwindowentryinapp-api.md#multiwindowentryinappstyle) | 否 | 是 | 组件风格参数。 |

## MultiWindowEntryInAPPStyle

PhonePC/2in1TabletTV

MultiWindowEntryInAPP组件风格参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconOptions | [MultiWindowEntryInAPPIconOptions](ui-design-multiwindowentryinapp-api.md#multiwindowentryinappiconoptions) | 否 | 是 | 组件图标参数。 |
| subtitleOptions | [MultiWindowEntryInAPPSubtitleOptions](ui-design-multiwindowentryinapp-api.md#multiwindowentryinappsubtitleoptions) | 否 | 是 | 组件文本标题参数。 |

## MultiWindowEntryInAPPIconOptions

PhonePC/2in1TabletTV

MultiWindowEntryInAPP组件图标参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iconColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件图标颜色。  默认值：$r('sys.color.font\_primary')。 |
| iconWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 组件图标粗细。  默认值：400。  **说明**：  - number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  - string类型仅支持number类型取值的字符串形式，例如“400”，以及“Bold”、“Bolder”、“Lighter”、“Regular” 、“Medium”分别对应FontWeight中相应的枚举值。 |
| iconSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 组件图标尺寸。  默认值：24\*24 vp。  **说明**：暂不支持百分比。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 组件背景颜色。  默认值：$r('sys.color.comp\_background\_tertiary')。 |

## MultiWindowEntryInAPPSubtitleOptions

PhonePC/2in1TabletTV

MultiWindowEntryInAPP组件标题文本参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| modifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 组件文本标题修改器。 |

## 属性

PhonePC/2in1TabletTV

支持大部分[通用属性](ts-component-general-attributes.md)。

说明

width、height、size属性暂不支持百分比。

该组件暂不支持accessibilityDescription、accessibilityText属性。

## 事件

PhonePC/2in1TabletTV

支持大部分[通用事件](ts-component-general-events.md)。

说明

该组件暂不支持onClick事件，如要监听点击请使用onTouch事件。

## 示例

PhonePC/2in1TabletTV

集成应用内多窗组件，用户点击按钮后可与应用内的其他UIAbility组成分屏或进入全景多窗。

```
1. // 从6.0.2(22)版本开始，无需手动导入MultiWindowEntryInAPPAttribute。具体请参考MultiWindowEntryInAPP的导入模块说明。
2. import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
3. import { Want } from '@kit.AbilityKit';
4. import { TextModifier } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct MultiWindowEntryInAPPTest {
9. @State textModifier: TextModifier = new TextModifier();
10. private want: Want = {
11. // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
12. bundleName: "com.example.myapplication",
13. moduleName: "entry",
14. abilityName: "FuncAbility",
15. };

17. build() {
18. Row() {
19. MultiWindowEntryInAPP({
20. want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
21. iconOptions: {
22. iconSize: 24,
23. iconColor: $r('sys.color.font_primary'),
24. iconWeight: FontWeight.Normal,
25. backgroundColor: $r('sys.color.comp_background_tertiary')
26. },
27. subtitleOptions: {
28. modifier: this.textModifier.fontColor(Color.Black)
29. }
30. }
31. })
32. .size({ width: 48, height: 48 })
33. .position({ x: 400, y: 30 })
34. }
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/xXetDIE4RHOhw76UbJSufQ/zh-cn_image_0000002558607398.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055712Z&HW-CC-Expire=86400&HW-CC-Sign=40848F45CFA13108F4BB4CC2B5FC5DAF8D4F5EC71783C2038ECD0FED425672D0)
