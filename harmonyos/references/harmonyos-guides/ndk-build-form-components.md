---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-form-components
title: 构建表单组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 构建表单组件
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fd1b6cc032580ed4aa913dfc80daa2f73dae89f96c00dbbdba18d34298304526
---

ArkUI NDK提供了多种表单组件，包括[按钮（Button）](arkts-common-components-button.md)、滑动条[Slider](../harmonyos-references/ts-basic-components-slider.md)、[切换按钮（Toggle）](arkts-common-components-switch.md)、多选框[Checkbox](../harmonyos-references/ts-basic-components-checkbox.md)、多选框群组[CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md)和[单选框（Radio）](arkts-common-components-radio-button.md)。这些组件是用户交互的基础元素，可以用于构建丰富的表单界面。

表单组件的相关接口定义在[native\_node.h](../harmonyos-references/capi-native-node-h.md)中。

本文提供表单组件NDK开发指导，查询之前需要先接入ArkTS页面，具体请参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

## Button按钮组件

Button组件用于创建可点击的按钮，支持多种按钮类型和样式设置。

### 创建Button组件

使用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建Button组件，节点类型为ARKUI\_NODE\_BUTTON。

```
std::shared_ptr<NativeModule::ArkUIBaseNode> CreateButtonExample()
{
    auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
    column->SetWidth(1, true);
    column->SetHeight(1, true);
    column->SetBackgroundColor(0x33ff0000);
    column->SetPadding(PARAM_20, false);
    auto button = std::make_shared<NativeModule::ArkUIButtonNode>();
    button->SetButtonLabel("This is a Button");
    button->SetMaxFontScale(1.0);
    auto circleBtn = std::make_shared<NativeModule::ArkUIButtonNode>();
    circleBtn->SetButtonLabel("Circle");
    circleBtn->SetButtonType(ARKUI_BUTTON_TYPE_CIRCLE);
    circleBtn->SetMargin(PARAM_20, false);
    column->AddChild(button);
    column->AddChild(circleBtn);
    // 返回Column，由调用方添加到Content中
    return column;
}
```

### 设置Button类型

Button组件支持通过设置NODE\_BUTTON\_TYPE属性实现不同的按钮类型，包括普通按钮、胶囊按钮、圆形按钮和圆角矩形按钮。按钮类型对应枚举请参考[ArkUI\_ButtonType](../harmonyos-references/capi-button-h.md#arkui_buttontype)。

下述示例将按钮类型设置为ARKUI\_BUTTON\_TYPE\_CIRCLE圆形按钮。

```
auto circleBtn = std::make_shared<NativeModule::ArkUIButtonNode>();
circleBtn->SetButtonLabel("Circle");
circleBtn->SetButtonType(ARKUI_BUTTON_TYPE_CIRCLE);
circleBtn->SetMargin(PARAM_20, false);
```

### Button属性

Button独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_BUTTON\_LABEL | 设置按钮文本标签。 |
| NODE\_BUTTON\_TYPE | 设置按钮类型。 |
| NODE\_BUTTON\_MIN\_FONT\_SCALE | 设置最小字体缩放比例。从API version 18开始支持。 |
| NODE\_BUTTON\_MAX\_FONT\_SCALE | 设置最大字体缩放比例。从API version 18开始支持。 |

## Slider滑动条组件

Slider组件用于创建滑动条，用户可以通过拖动滑块来选择数值。

### 创建Slider组件

使用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建Slider组件，节点类型为ARKUI\_NODE\_SLIDER。

```
std::shared_ptr<NativeModule::ArkUIBaseNode> CreateSliderExample()
{
    auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
    column->SetWidth(1, true);
    column->SetHeight(1, true);
    column->SetBackgroundColor(0x33ff0000);
    column->SetPadding(PARAM_20, false);
    auto sliderInSet = std::make_shared<NativeModule::ArkUISliderNode>();
    sliderInSet->SetSliderValue(PARAM_50);
    sliderInSet->SetSliderStep(PARAM_10);
    sliderInSet->SetSliderStyle(ARKUI_SLIDER_STYLE_IN_SET);
    sliderInSet->SetBlockColor(0xFF00FF00);
    sliderInSet->SetTrackColor(0xFFFFFF00);
    auto sliderOutSet = std::make_shared<NativeModule::ArkUISliderNode>();
    sliderOutSet->SetSliderValue(PARAM_50);
    sliderOutSet->SetSliderStep(PARAM_10);
    sliderOutSet->SetSliderStyle(ARKUI_SLIDER_STYLE_OUT_SET);
    sliderOutSet->SetMargin(PARAM_20, false);
    sliderOutSet->SetSliderDirection(ARKUI_SLIDER_DIRECTION_VERTICAL);
    sliderOutSet->SetIsReverse(true);
    sliderOutSet->SetIsShowSteps(true);
    column->AddChild(sliderInSet);
    column->AddChild(sliderOutSet);
    return column;
}
```

### 设置Slider样式

Slider支持两种样式，通过[ARKUI\_SliderStyle](../harmonyos-references/capi-slider-h.md#arkui_sliderstyle)枚举定义：

* ARKUI\_SLIDER\_STYLE\_OUT\_SET：滑块在滑动条外（默认值）。
* ARKUI\_SLIDER\_STYLE\_IN\_SET：滑块在滑动条内。

如下示例代码创建了ARKUI\_SLIDER\_STYLE\_IN\_SET样式的Slider组件并设置了滑块和滑轨颜色。

```
auto sliderInSet = std::make_shared<NativeModule::ArkUISliderNode>();
sliderInSet->SetSliderValue(PARAM_50);
sliderInSet->SetSliderStep(PARAM_10);
sliderInSet->SetSliderStyle(ARKUI_SLIDER_STYLE_IN_SET);
sliderInSet->SetBlockColor(0xFF00FF00);
sliderInSet->SetTrackColor(0xFFFFFF00);
```

### 设置Slider方向和步长

Slider支持设置滑动方向（水平或垂直）、是否反向以及是否显示步长刻度。

```
auto sliderOutSet = std::make_shared<NativeModule::ArkUISliderNode>();
sliderOutSet->SetSliderValue(PARAM_50);
sliderOutSet->SetSliderStep(PARAM_10);
sliderOutSet->SetSliderStyle(ARKUI_SLIDER_STYLE_OUT_SET);
sliderOutSet->SetMargin(PARAM_20, false);
sliderOutSet->SetSliderDirection(ARKUI_SLIDER_DIRECTION_VERTICAL);
sliderOutSet->SetIsReverse(true);
sliderOutSet->SetIsShowSteps(true);
```

### Slider属性

Slider独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_SLIDER\_VALUE | 设置当前进度值。 |
| NODE\_SLIDER\_MIN\_VALUE | 设置最小值。 |
| NODE\_SLIDER\_MAX\_VALUE | 设置最大值。 |
| NODE\_SLIDER\_STEP | 设置滑动步长。 |
| NODE\_SLIDER\_DIRECTION | 设置滑动条方向。 |
| NODE\_SLIDER\_REVERSE | 设置是否反向。 |
| NODE\_SLIDER\_STYLE | 设置滑动条样式。 |
| NODE\_SLIDER\_BLOCK\_COLOR | 设置滑块颜色。 |
| NODE\_SLIDER\_TRACK\_COLOR | 设置轨道颜色。 |
| NODE\_SLIDER\_SELECTED\_COLOR | 设置已选择部分颜色。 |
| NODE\_SLIDER\_SHOW\_STEPS | 设置是否显示步长刻度。 |

## Toggle开关组件

Toggle组件用于创建开关，用户可以在开和关两种状态之间切换。

### 创建Toggle组件

使用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建Toggle组件，节点类型为ARKUI\_NODE\_TOGGLE。

```
std::shared_ptr<NativeModule::ArkUIBaseNode> CreateToggleExample()
{
    auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
    column->SetWidth(1, true);
    column->SetHeight(1, true);
    column->SetBackgroundColor(0x33ff0000);
    column->SetPadding(PARAM_20, false);
    auto toggle = std::make_shared<NativeModule::ArkUIToggleNode>();
    toggle->SetSelectedColor(0xFFFF0000);
    toggle->SetUnSelectedColor(0xFF0000FF);
    toggle->SetSwitchPointColor(0xFF00FF00);
    column->AddChild(toggle);

    return column;
}
```

### 设置Toggle样式

可以设置Toggle开启状态背景色、关闭状态背景色以及滑块颜色。

```
toggle->SetSelectedColor(0xFFFF0000);
toggle->SetUnSelectedColor(0xFF0000FF);
toggle->SetSwitchPointColor(0xFF00FF00);
```

### Toggle属性

Toggle独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_TOGGLE\_VALUE | 设置开关状态。 |
| NODE\_TOGGLE\_SELECTED\_COLOR | 设置开启状态背景色。 |
| NODE\_TOGGLE\_UNSELECTED\_COLOR | 设置关闭状态背景色。 |
| NODE\_TOGGLE\_SWITCH\_POINT\_COLOR | 设置滑块颜色。 |

## Checkbox多选框组件

Checkbox组件用于创建多选框，用户可以选中或取消选中。CheckboxGroup用于管理多个多选框，实现全选等操作。

### 创建Checkbox组件

使用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建Checkbox组件，节点类型为ARKUI\_NODE\_CHECKBOX。

```
std::shared_ptr<NativeModule::ArkUIBaseNode> CreateCheckboxExample()
{
    auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
    column->SetWidth(1, true);
    column->SetHeight(1, true);
    column->SetBackgroundColor(0x33ff0000);
    column->SetPadding(PARAM_20, false);
    auto checkbox1 = std::make_shared<NativeModule::ArkUICheckboxNode>();
    auto checkbox2 = std::make_shared<NativeModule::ArkUICheckboxNode>();
    auto checkbox3 = std::make_shared<NativeModule::ArkUICheckboxNode>();
    auto checkboxGroup = std::make_shared<NativeModule::ArkUICheckboxGroupNode>();
    checkboxGroup->SetCheckboxGroupName("check_group");
    checkbox1->SetCheckboxGroup("check_group");
    checkbox1->SetSelectColor(0xFFFF0000);
    checkbox2->SetCheckboxGroup("check_group");
    checkbox2->SetUnSelectColor(0xFFFF0000);
    checkbox3->SetCheckboxGroup("check_group");
    checkbox3->SetCheckboxShape(ArkUI_CHECKBOX_SHAPE_ROUNDED_SQUARE);
    checkbox1->SetCheckboxName("check_group1");
    checkbox2->SetCheckboxName("check_group2");
    checkbox3->SetCheckboxName("check_group3");

    column->AddChild(checkboxGroup);
    column->AddChild(checkbox1);
    column->AddChild(checkbox2);
    column->AddChild(checkbox3);

    // 返回Column，由调用方添加到Content中
    return column;
}
```

### 创建CheckboxGroup

CheckboxGroup用于管理同一组内的多个多选框，节点类型为ARKUI\_NODE\_CHECKBOX\_GROUP。

```
auto checkboxGroup = std::make_shared<NativeModule::ArkUICheckboxGroupNode>();
checkboxGroup->SetCheckboxGroupName("check_group");
```

### 设置Checkbox属性

可以设置多选框的选中颜色、未选中颜色、形状以及所属组名。

```
checkbox1->SetCheckboxGroup("check_group");
checkbox1->SetSelectColor(0xFFFF0000);
checkbox2->SetCheckboxGroup("check_group");
checkbox2->SetUnSelectColor(0xFFFF0000);
checkbox3->SetCheckboxGroup("check_group");
checkbox3->SetCheckboxShape(ArkUI_CHECKBOX_SHAPE_ROUNDED_SQUARE);
checkbox1->SetCheckboxName("check_group1");
checkbox2->SetCheckboxName("check_group2");
checkbox3->SetCheckboxName("check_group3");
```

### Checkbox属性

Checkbox独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_CHECKBOX\_SELECT | 设置是否选中。 |
| NODE\_CHECKBOX\_SELECT\_COLOR | 设置选中状态颜色。 |
| NODE\_CHECKBOX\_UNSELECT\_COLOR | 设置未选中状态颜色。 |
| NODE\_CHECKBOX\_MARK | 设置勾选标记样式。 |
| NODE\_CHECKBOX\_SHAPE | 设置多选框形状。 |
| NODE\_CHECKBOX\_NAME | 设置多选框名称。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP | 设置多选框组名称，用于CheckboxGroup管理。从API version 15开始支持。 |

### CheckboxGroup属性

CheckboxGroup独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_CHECKBOX\_GROUP\_NAME | 设置多选框群组名称。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SELECT\_ALL | 设置是否全选。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SELECTED\_COLOR | 设置选中状态颜色。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_UNSELECTED\_COLOR | 设置未选中状态颜色。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_MARK | 设置勾选标记样式。从API version 15开始支持。 |
| NODE\_CHECKBOX\_GROUP\_SHAPE | 设置多选框形状。从API version 15开始支持。 |

## Radio单选按钮组件

Radio组件用于创建单选按钮，同一组内的单选按钮只能选中一个。

### 创建Radio组件

使用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建Radio组件，节点类型为ARKUI\_NODE\_RADIO。

```
std::shared_ptr<NativeModule::ArkUIBaseNode> CreateRadioExample()
{
    auto column = std::make_shared<NativeModule::ArkUIColumnNode>();
    column->SetWidth(1, true);
    column->SetHeight(1, true);
    column->SetBackgroundColor(0x33ff0000);
    column->SetPadding(PARAM_20, false);
    auto radio1 = std::make_shared<NativeModule::ArkUIRadioNode>();
    auto radio2 = std::make_shared<NativeModule::ArkUIRadioNode>();
    auto radio3 = std::make_shared<NativeModule::ArkUIRadioNode>();
    radio1->SetIsOn(true);
    radio1->SetRadioGroup("radio_group");
    radio2->SetRadioGroup("radio_group");
    radio3->SetRadioGroup("radio_group");
    radio3->SetRadioStyle(0xFFFF0000, 0xFF00FF00, 0xFF00FFFF);

    column->AddChild(radio1);
    column->AddChild(radio2);
    column->AddChild(radio3);

    return column;
}
```

### 设置Radio组

同一组内的Radio组件只能选中一个，通过设置相同的组名实现互斥。

```
radio1->SetIsOn(true);
radio1->SetRadioGroup("radio_group");
radio2->SetRadioGroup("radio_group");
radio3->SetRadioGroup("radio_group");
```

### 设置Radio样式

可以设置单选按钮的样式，包括未选中状态颜色、选中状态内部圆环颜色和选中状态外环颜色。

```
radio3->SetRadioStyle(0xFFFF0000, 0xFF00FF00, 0xFF00FFFF);
```

### Radio属性

Radio独有属性如下，具体说明请参考[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的枚举定义。

| 属性 | 说明 |
| --- | --- |
| NODE\_RADIO\_CHECKED | 设置是否选中。 |
| NODE\_RADIO\_STYLE | 设置单选框选中状态和非选中状态的样式（包括开启状态底板颜色、关闭状态描边颜色、开启状态内部圆饼颜色）。 |
| NODE\_RADIO\_VALUE | 设置单选按钮值。 |
| NODE\_RADIO\_GROUP | 设置所属组名，同一组内的Radio互斥。 |
