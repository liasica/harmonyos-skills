---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-picker
title: 使用滑动选择器 (Picker)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用选择类组件 > 使用滑动选择器 (Picker)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b317ae98d2ee9321352299748c7e9eaaa65a649e95afae2509f49fd141340a1f
---

## 概述

从API version 23开始，ArkUI开发框架在NDK接口提供了Picker容器组件。Picker容器组件用于实现用户自定义选项的选择操作，支持滚动选择、触感反馈、循环滚动等功能。Picker组件通过设置选择指示器样式，可以自定义选中项的显示效果，适用于日期选择、时间选择、文本选择等场景。从API版本26.0.0开始，可通过NODE\_PICKER\_DISPLAYED\_ITEM\_COUNT、NODE\_PICKER\_ITEM\_HEIGHT配置可见选项行数与每行行高，语义与ArkTS侧[UIPickerComponent](../harmonyos-references/ts-container-ui-picker-component.md)的[displayedItemCount](../harmonyos-references/ts-container-ui-picker-component.md#displayeditemcount)、[itemHeight](../harmonyos-references/ts-container-ui-picker-component.md#itemheight)一致；详细参数格式见[信息选择类组件相关属性](../harmonyos-references/capi-native-node-h-nodeattributetype-informationselection.md)。

[创建Picker](ndk-picker.md#创建picker)后，可以[设置Picker属性](ndk-picker.md#设置picker属性)，并[监听Picker事件](ndk-picker.md#监听picker事件)。

使用NDK接口构建UI界面以及NDK基本使用，可以参考[接入ArkTS页面](ndk-access-the-arkts-page.md)。

## 创建Picker

通过调用[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)()得到组件对象指针，节点类型为ARKUI\_NODE\_PICKER，并设置[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的相关属性，创建一个Picker容器组件。

### 基本创建方式

以下示例展示了创建Picker组件并设置基本属性的方法。

```
static ArkUI_NodeHandle CreatePicker(ArkUI_NativeNodeAPI_1 *api)
{
    ArkUI_NodeHandle picker = api->createNode(ARKUI_NODE_PICKER);
    if (picker == nullptr) {
        return nullptr;
    }
    if (g_state) {
        g_state->pickerNode = picker;
    }
    ArkUI_NumberValue widthValue = {.f32 = K_PICKER_WIDTH_RATIO};
    ArkUI_AttributeItem widthItem = {&widthValue, sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
    api->setAttribute(picker, NODE_WIDTH_PERCENT, &widthItem);
    UpdatePickerSelectedIndex();
    SetDisplayedItemCount(K_VISIBLE_COUNT);
    SetItemHeight(K_ITEM_HEIGHT);
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);
    if (g_state) {
        for (const auto &item : g_state->dataArray) {
            ArkUI_NodeHandle optionNode = CreatePickerOption(api, item);
            if (optionNode != nullptr) {
                api->addChild(picker, optionNode);
            }
        }
    }
    return picker;
}
```

### 封装为工具类

参考[示例](ndk-access-the-arkts-page.md#示例)中列表组件的实现方式，可以将Picker组件常用的属性设置封装到自定义的工具类中方便后续使用。

```c
class ContainerPickerCanLoopMaker : public BaseNode {
public:
    static ArkUI_NodeHandle CreateNativeNode();

    ContainerPickerCanLoopMaker()
        : BaseNode(NodeApiInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_PICKER)),
          nodeApi_(NodeApiInstance::GetInstance()->GetNativeNodeAPI())
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
    }

    ~ContainerPickerCanLoopMaker() override = default;

    // ========================================
    // 基础尺寸设置接口
    // ========================================
    void SetPickerSize(float width, float height) { SetSize(width, height); }

    void SetPickerSizePercent(float widthPercent, float heightPercent) { SetSizePercent(widthPercent, heightPercent); }

    void SetPickerWidthPercent(float widthPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_WIDTH_PERCENT, widthPercent);
    }

    void SetPickerHeightPercent(float heightPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_HEIGHT_PERCENT, heightPercent);
    }

    // ========================================
    // Picker特有属性设置接口
    // ========================================
    void SetSelectedIndex(uint32_t index)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue selectedIndexValue = {.u32 = index};
        ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                                 sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);
    }

    void SetCanLoop(bool canLoop)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
        ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);
    }

    void SetHapticFeedback(bool enabled)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
        ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                        sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);
    }

    void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                      .topLeftRadius = cornerRadius,
                                                      .topRightRadius = cornerRadius,
                                                      .bottomLeftRadius = cornerRadius,
                                                      .bottomRightRadius = cornerRadius};
        OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                      float endMargin = 20.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                                .dividerColor = dividerColor,
                                                .startMargin = startMargin,
                                                .endMargin = endMargin};
        OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    // ========================================
    // 公共辅助方法
    // ========================================
    ArkUI_NativeNodeAPI_1 *GetNodeAPI() const { return nodeApi_; }

protected:
    void OnNodeEvent(ArkUI_NodeEvent *event) override { BaseNode::OnNodeEvent(event); }

private:
    ArkUI_NativeNodeAPI_1 *nodeApi_ = nullptr;
};
```

## 设置Picker属性

### 设置默认选中项

通过设置[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_PICKER\_OPTION\_SELECTED\_INDEX属性，可以设置Picker组件的默认选中项索引。

```c
ArkUI_NumberValue selectedIndexValue = {.u32 = index};
ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                         sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);
```

### 设置触感反馈

通过设置NODE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK属性，可以控制Picker组件是否启用触感反馈。开启后，当用户滚动选择器时，如果系统硬件支持，会产生触感反馈。

使用[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)时可直接调用setAttribute。

```c
ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);
```

若使用上文封装的ContainerPickerCanLoopMaker，可调用已封装的接口。

```
picker->SetHapticFeedback(K_HAPTIC_FEEDBACK);
```

### 设置循环滚动

通过设置NODE\_PICKER\_CAN\_LOOP属性，可以控制Picker组件是否支持循环滚动。设置为true时，选择器可以无限循环滚动；设置为false时，滚动到首尾时会停止。

**说明** 

当子组件个数小于或等于可见选项行数（由NODE\_PICKER\_DISPLAYED\_ITEM\_COUNT设置，默认为7）时，无论设置为true还是false，都不会循环滚动。

使用[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)时可直接调用setAttribute。

```c
ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);
```

若使用上文封装的ContainerPickerCanLoopMaker，可调用已封装的接口。

```
picker->SetCanLoop(K_CAN_LOOP);
```

### 设置可见选项数量与选项行高

从API版本26.0.0开始，可通过[NODE\_PICKER\_DISPLAYED\_ITEM\_COUNT](../harmonyos-references/capi-native-node-h-nodeattributetype-informationselection.md#node_picker_displayed_item_count)设置可见选项行数，通过[NODE\_PICKER\_ITEM\_HEIGHT](../harmonyos-references/capi-native-node-h-nodeattributetype-informationselection.md#node_picker_item_height)设置每一行的高度（vp）。未设置时，默认分别为7行与40vp；取值范围、偶数行数规范及越界行为与[UIPickerComponent](../harmonyos-references/ts-container-ui-picker-component.md)的[displayedItemCount](../harmonyos-references/ts-container-ui-picker-component.md#displayeditemcount)、[itemHeight](../harmonyos-references/ts-container-ui-picker-component.md#itemheight)一致。立体滚轮样式下可视高度会受旋转影响，若增大行数或行高，请相应增大Picker容器高度。

使用[ArkUI\_NativeNodeAPI\_1](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md)时可直接调用setAttribute。

```
ArkUI_NumberValue itemCountValue = {.i32 = count};
ArkUI_AttributeItem itemCountItem = {&itemCountValue, sizeof(itemCountValue) / sizeof(ArkUI_NumberValue)};
g_state->api->setAttribute(g_state->pickerNode, NODE_PICKER_DISPLAYED_ITEM_COUNT, &itemCountItem);
```

```
ArkUI_NumberValue itemHeightValue = {.f32 = heightVp};
ArkUI_AttributeItem itemHeightItem = {&itemHeightValue, sizeof(itemHeightValue) / sizeof(ArkUI_NumberValue)};
g_state->api->setAttribute(g_state->pickerNode, NODE_PICKER_ITEM_HEIGHT, &itemHeightItem);
```

### 设置选择指示器样式

通过设置NODE\_PICKER\_SELECTION\_INDICATOR属性，可以自定义Picker组件的选择指示器样式。选择指示器包括背景样式和分割线样式两部分。

选择指示器的背景样式通过[ArkUI\_PickerIndicatorBackground](../harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatorbackground.md)结构体设置，包括背景颜色和圆角半径。

```c
void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                  .topLeftRadius = cornerRadius,
                                                  .topRightRadius = cornerRadius,
                                                  .bottomLeftRadius = cornerRadius,
                                                  .bottomRightRadius = cornerRadius};
    OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}
```

选择指示器的分割线样式通过[ArkUI\_PickerIndicatorDivider](../harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatordivider.md)结构体设置，包括线宽、颜色和边距。

```c
void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                  float endMargin = 20.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                            .dividerColor = dividerColor,
                                            .startMargin = startMargin,
                                            .endMargin = endMargin};
    OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}
```

将背景样式或分割线样式组合到[ArkUI\_PickerIndicatorStyle](../harmonyos-references/capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)结构体中，并设置给Picker组件。

若使用上文封装的ContainerPickerCanLoopMaker，可调用已封装的接口。

```
picker->SetSelectionIndicatorDivider(0xFF0000FF, 2.0f, 20.0f, 20.0f);
```

## 监听Picker事件

本示例通过[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册Picker组件的事件类型[ArkUI\_NodeEventType](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)，使用ArkUI\_NodeEventItem结构体为每个事件指定独立的回调函数。开发者无需额外注册全局回调函数，每个事件项直接绑定回调函数。Picker组件支持的事件如下：

| 枚举 | 说明 | 起始版本 |
| --- | --- | --- |
| NODE\_PICKER\_EVENT\_ON\_CHANGE | Picker组件中选择某项时触发的事件。 | 23 |
| NODE\_PICKER\_EVENT\_ON\_SCROLL\_STOP | Picker组件中选择某项且滚动停止时触发的事件。 | 23 |

### 监听选择变化事件

通过[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册NODE\_PICKER\_EVENT\_ON\_CHANGE事件，使用ArkUI\_NodeEventItem结构体指定回调函数，可以监听Picker组件的选择变化。事件回调中会返回选中项的索引值。

```
api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);
```

### 监听滚动停止事件

通过[registerNodeEvent](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#registernodeevent)注册NODE\_PICKER\_EVENT\_ON\_SCROLL\_STOP事件，使用ArkUI\_NodeEventItem结构体指定回调函数，可以监听Picker组件滚动停止时的选择变化。与NODE\_PICKER\_EVENT\_ON\_CHANGE事件相比，该事件只在滚动停止时触发，适合需要在滚动完成后再处理选择的场景。

```
api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);
```

## 完整示例

[Native\_Type\_Sample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)
