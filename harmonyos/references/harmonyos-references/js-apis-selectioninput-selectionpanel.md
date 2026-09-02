---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-selectioninput-selectionpanel
title: "@ohos.selectionInput.SelectionPanel (划词面板)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 数据文件处理 > @ohos.selectionInput.SelectionPanel (划词面板)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7406a47afab843b555a00632cf45f467916c9ae5c2b08c240c3317d0d4ca3530
---

划词面板是用户选中文本后弹出的操作面板，适用于需要为选中文本提供翻译、搜索等快捷操作功能的场景，帮助开发者快速集成划词操作能力，提升用户交互体验。面板采用两级架构设计：菜单面板（MENU\_PANEL）为一级面板，展示当前应用可提供的功能入口（如翻译、搜索等）；主面板（MAIN\_PANEL）为二级面板，在用户点击菜单面板中的功能按钮后弹出，展示具体的功能结果。本模块提供划词面板的属性信息和类型，开发者可通过[PanelInfo](js-apis-selectioninput-selectionpanel.md#panelinfo)设定面板的位置和尺寸，通过[PanelType](js-apis-selectioninput-selectionpanel.md#paneltype)指定面板类型。划词面板的创建与显示接口请参见[createPanel](js-apis-selectioninput-selectionmanager.md#createpanel)、[show](js-apis-selectioninput-selectionmanager.md#show)。

**说明** 

* 本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该功能。

## 导入模块

```ts
import { PanelInfo, PanelType } from '@kit.BasicServicesKit';
```

## PanelInfo

划词面板属性信息，包含面板类型、位置和宽高。开发者通过panelType指定面板类型（菜单面板或主面板），通过x、y设定面板左上角坐标，通过width、height设定面板尺寸，各项属性共同定义面板的呈现形态。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| panelType | [PanelType](js-apis-selectioninput-selectionpanel.md#paneltype) | 否 | 否 | 划词面板类型枚举，有两种面板可供选择，详见[PanelType](js-apis-selectioninput-selectionpanel.md#paneltype)。 |
| x | number | 否 | 否 | 划词面板左上角的x轴坐标，单位为px。以主屏幕左上角为原点，x轴正方向向右。取值范围[0, +∞)，传入负数时面板无法正常创建。 |
| y | number | 否 | 否 | 划词面板左上角的y轴坐标，单位为px。以主屏幕左上角为原点，y轴正方向向下。取值范围[0, +∞)，传入负数时面板无法正常创建。 |
| width | number | 否 | 否 | 划词面板宽度，单位为px。取值范围(0, +∞)，传入0或负数时面板无法正常创建。 |
| height | number | 否 | 否 | 划词面板高度，单位为px。取值范围(0, +∞)，传入0或负数时面板无法正常创建。 |

## PanelType

划词面板类型枚举，定义面板的两级架构：菜单面板（一级）和主面板（二级）。

**系统能力：** SystemCapability.SelectionInput.Selection

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MENU\_PANEL | 1 | 菜单面板为一级面板，显示当前应用可以提供的功能，如翻译、搜索等。 |
| MAIN\_PANEL | 2 | 主面板为二级面板，当用户点击菜单面板中的功能按钮时弹出，展示具体的翻译或搜索结果等内容。 |
