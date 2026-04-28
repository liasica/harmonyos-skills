---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-drop
title: 拖拽控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 拖拽控制
category: harmonyos-references
scraped_at: 2026-04-28T08:01:10+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0fe12771b0167d30d348fab23aee1cab2b698165fed2ccea48edde7da78d4e07
---

组件提供了一些属性和接口，可用于配置组件对拖拽事件的响应行为，或影响系统对拖拽事件的处理方式，包括是否允许被拖拽，自定义拖拽预览图的外观等。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

ArkUI框架对以下组件实现了默认的拖拽能力，支持对数据的拖出或拖入响应。开发者也可以通过实现通用拖拽事件来自定义拖拽响应。

* 默认支持拖出能力的组件（可从组件上拖出数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)、[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Hyperlink](ts-container-hyperlink.md)，开发者可通过设置这些组件的[draggable](ts-universal-attributes-drag-drop.md#draggable)属性来控制对默认拖拽能力的使用。
* 默认支持拖入能力的组件（目标组件可响应拖入数据）：[Search](ts-basic-components-search.md)、[TextInput](ts-basic-components-textinput.md)、[TextArea](ts-basic-components-textarea.md)、[RichEditor](ts-basic-components-richeditor.md)，开发者可通过设置这些组件的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)属性为null来禁用对默认拖入能力的支持。
* 不支持拖出能力的组件（不可从组件上拖出数据）：[ArcScrollBar](ts-basic-components-arcscrollbar.md)、[MultiNavigation](ohos-arkui-advanced-multinavigation.md)、[ToolBarItem](ts-basic-components-toolbaritem.md)、[ArcSlider](ohos-arkui-advanced-arcslider.md)、[Span](ts-basic-components-span.md)、[ImageSpan](ts-basic-components-imagespan.md)、[ContainerSpan](ts-basic-components-containerspan.md)、[SymbolSpan](ts-basic-components-symbolspan.md)、[ArcAlphabetIndexer](ts-container-arc-alphabet-indexer.md)、[OffscreenCanvas](ts-components-offscreencanvas.md)、[Menu](ts-basic-components-menu.md)、[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)、[PasteButton](ts-security-components-pastebutton.md)、[SaveButton](ts-security-components-savebutton.md)、[WithTheme](ts-container-with-theme.md)、[NavPushPathHelper](ohos-atomicservice-navpushpathhelper.md)、[ContentSlot](ts-components-contentslot.md)、[Chip](ohos-arkui-advanced-chip.md)、[ExceptionPrompt](ohos-arkui-advanced-exceptionprompt.md)、[Filter](ohos-arkui-advanced-filter.md)、[FormMenu](ohos-arkui-advanced-formmenu.md)、[Popup](ohos-arkui-advanced-popup.md)、[SelectionMenu](ohos-arkui-advanced-selectionmenu.md)、[SplitLayout](ohos-arkui-advanced-splitlayout.md)以及所有弹窗类组件。

Text、TextInput、TextArea、Hyperlink、Image、RichEditor和Web组件的draggable属性默认为true，默认支持拖出能力。

其他支持拖出能力的组件需要开发者将draggable属性设置为true，并在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)等接口中实现数据传输相关内容，才能正确处理拖拽。

说明

Text组件需配合[copyOption](ts-basic-components-text.md#copyoption9)一起使用，设置copyOptions为CopyOptions.InApp或者CopyOptions.LocalDevice。

## allowDrop

PhonePC/2in1TabletTVWearable

allowDrop(value: Array<UniformDataType> | null | Array<string>): T

设置该组件上允许落入的数据类型。如果未设置allowDrop，组件将默认接受所有数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[UniformDataType](ts-universal-attributes-drag-drop.md#uniformdatatype)> | null12+ | Array<string>23+ | 是 | 设置该组件上允许落入的数据类型。从API version 12开始，允许设置成null使该组件不接受所有的数据类型。从API version 23开始，支持设置自定义数据类型Array<string>，自定义数据类型为应用自行定义的数据类型字符串，字符串无明确格式要求，但不应与UniformDataType标准类型格式重复，建议以易记易区分为原则来定义。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## draggable

PhonePC/2in1TabletTVWearable

draggable(value: boolean): T

设置该组件是否允许拖拽。默认情况下，组件不允许拖拽。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置该组件是否允许进行拖拽。true表示允许拖拽，false表示不允许拖拽。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## dragPreview11+

PhonePC/2in1TabletTVWearable

dragPreview(value: CustomBuilder | DragItemInfo | string): T

设置组件浮起和拖拽过程中的预览图。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | string12+ | 是 | 设置组件浮起和拖拽过程中的预览图，仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)拖拽方式中有效。  当组件支持拖拽并同时设置[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)的预览图时，则长按浮起的预览图以[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)设置的预览图为准。开发者在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中返回的背板图优先级低于[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)设置的预览图，当设置了[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)预览图时，拖拽过程中的背板图使用[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)预览图。由于[CustomBuilder](ts-types.md#custombuilder8)需要离线渲染之后才能使用，因此存在一定的性能开销和时延，推荐优先使用 [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo)中的[PixelMap](arkts-apis-image-pixelmap.md)方式。  当传入类型为string的id时，则将id对应组件的截图作为预览图。如果id对应的组件无法查找到，或者id对应的组件[Visibility](ts-appendix-enums.md#visibility)属性设置成None/Hidden，则对组件自身进行截图作为拖拽预览图。目前截图不含有亮度、阴影、模糊和旋转等视觉效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## dragPreview15+

PhonePC/2in1TabletTVWearable

dragPreview(preview: CustomBuilder | DragItemInfo | string, config?: PreviewConfiguration):T

自定义组件拖拽过程中的预览图，仅用于设置浮起效果或者禁用浮起效果。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| preview | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | string | 是 | 设置组件浮起和拖拽过程中的预览图，仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)拖拽方式中有效。  当组件支持拖拽并同时设置[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)的预览图时，则长按浮起的预览图以[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)设置的预览图为准。开发者在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)中返回的背板图优先级低于[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)设置的预览图，当设置了[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)预览图时，拖拽过程中的背板图使用[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)预览图。由于[CustomBuilder](ts-types.md#custombuilder8)需要离线渲染之后才能使用，因此存在一定的性能开销和时延，推荐优先使用 [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo)中的[PixelMap](arkts-apis-image-pixelmap.md)方式。  当传入类型为string的id时，则将id对应组件的截图作为预览图。如果id对应的组件无法查找到，或者id对应的组件[Visibility](ts-appendix-enums.md#visibility)属性设置成None/Hidden，则对组件自身进行截图作为拖拽预览图。目前截图不含有亮度、阴影、模糊和旋转等视觉效果。 |
| config | [PreviewConfiguration](ts-universal-events-drag-drop.md#previewconfiguration15) | 否 | 对自定义拖拽过程中的预览图进行配置。  只对[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)中的预览生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## dragPreviewOptions11+

PhonePC/2in1TabletTVWearable

dragPreviewOptions(value: DragPreviewOptions, options?: DragInteractionOptions): T

设置拖拽过程中预览图处理模式，数量角标的显示以及预览图浮起的交互模式。不支持onItemDragStart拖拽方式。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11-1)11+ | 是 | 设置拖拽过程中预览图处理模式及数量角标的显示。 |
| options12+ | [DragInteractionOptions](ts-universal-attributes-drag-drop.md#draginteractionoptions12)12+ | 否 | 设置拖拽过程中预览图浮起的交互模式。  默认值：空 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## DragPreviewOptions11+

PhonePC/2in1TabletTVWearable

设置拖拽过程中预览图处理模式及数量角标的显示。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | [DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明) | Array<[DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明)>12+ | 否 | 是 | 表示拖拽过程中背板图处理模式。  默认值：DragPreviewMode.AUTO  当组件同时设置DragPreviewMode.AUTO和其它枚举值时，以DragPreviewMode.AUTO为准，其它枚举值设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| numberBadge12+ | boolean | number | 否 | 是 | 控制数量角标是否显示，或强制设置显示的数量。当设置数量角标时取值范围为[0，231-1]，超过取值范围时会按默认状态处理。当设置为浮点数时，只显示整数部分。  **说明：**  在多选拖拽场景，需通过该接口设置拖拽对象的数量。  默认值：true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| modifier12+ | [ImageModifier](ts-universal-attributes-drag-drop.md#imagemodifier12) | 否 | 是 | 用于配置拖拽背板图的样式Modifier对象，可使用图片组件所支持的属性和样式来配置背板图样式(参考示例6)，当前支持透明度，阴影，背景模糊度，圆角。文本拖拽只支持默认效果，不支持通过modifier进行自定义。  1.透明度  通过[opacity](ts-universal-attributes-opacity.md#opacity)设置不透明度，不透明度的取值范围为0-1。设置0或不设置时采用背板图透明度的默认值0.95，设置1或异常值时不透明。  2.阴影  通过[shadow](ts-universal-attributes-image-effect.md#shadow)设置阴影。  3.背景模糊度  通过[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect11)或[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)设置背景模糊度，如果两者同时设置，以后设置的属性为准。  4.圆角  通过[border](ts-universal-attributes-border.md#border)或[borderRadius](ts-universal-attributes-border.md#borderradius)设置圆角，当同时在mode和modifier中设置圆角，mode设置的圆角显示优先级低于modifier设置。  默认值：空，无法修改属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sizeChangeEffect19+ | [DraggingSizeChangeEffect](ts-universal-attributes-drag-drop.md#draggingsizechangeeffect19枚举说明)19+ | 否 | 是 | 用于选择长按浮起图与拖拽预览图过渡效果。  默认值：DraggingSizeChangeEffect.DEFAULT。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## DragPreviewMode11+枚举说明

PhonePC/2in1TabletTVWearable

设置拖拽预览图的显示模式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 1 | 系统根据拖拽场景自动改变跟手点位置，根据规则自动对拖拽背板图进行缩放变换等。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| DISABLE\_SCALE | 2 | 禁用系统对拖拽背板图的缩放行为。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| ENABLE\_DEFAULT\_SHADOW12+ | 3 | 启用非文本类组件默认阴影效果。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| ENABLE\_DEFAULT\_RADIUS12+ | 4 | 启用非文本类组件统一圆角效果，默认值12vp。当应用自身设置的圆角值大于默认值或modifier设置的圆角时，则显示应用自定义圆角效果。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| ENABLE\_DRAG\_ITEM\_GRAY\_EFFECT18+ | 5 | 启用支持原拖拽对象灰显（透明度）效果，对文本内容拖拽不生效。用户拖起时原对象显示灰显效果，释放时原对象恢复原有效果。开启默认灰显效果后，不建议在拖拽开始后自行修改透明度，如果开发者在拖拽发起后自行修改应用透明度，则灰显效果将被覆盖，且在结束拖拽时无法正确恢复原始透明度效果。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| ENABLE\_MULTI\_TILE\_EFFECT18+ | 6 | 启用支持多选对象鼠标拖拽不聚拢效果，各拖拽图显示在其原始位置的相对位置，当满足多选的情况下且isMultiSelectionEnabled为true时该参数才生效。不聚拢效果优先级高于[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)。不支持二次拖拽、圆角和缩放设置。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW19+ | 7 | 启用支持以拖拽预览图初始尺寸计算跟手点位置，长按浮起图和拖拽图不一致时使用。鼠标拖拽，设置DragPreviewMode.ENABLE\_MULTI\_TILE\_EFFECT时不生效。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |

## DraggingSizeChangeEffect19+枚举说明

PhonePC/2in1TabletTVWearable

当一个节点上同时设置长按浮起预览（参考[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)）与拖拽时，使用该字段设置长按浮起预览图与拖拽预览图过渡动效方式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 发起拖拽时直接从菜单预览图切换为最终尺寸的拖拽预览图。 |
| SIZE\_TRANSITION | 1 | 发起拖拽时，由菜单预览图直接切换为拖拽预览图，尺寸逐步从菜单预览图尺寸过渡到最终预览图尺寸，设置了[DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明)中的DISABLE\_SCALE枚举值时尺寸过渡不生效。这在长按浮起预览图与拖拽预览图相同时使用。 |
| SIZE\_CONTENT\_TRANSITION | 2 | 发起拖拽时，由菜单预览图逐步过渡切换为最终拖拽预览图，设置[DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明)中的DISABLE\_SCALE时尺寸过渡不生效。这常用于菜单预览图与拖拽预览图差异较大时使用，过渡效果包含内容透明度及尺寸变化。 |

## DragInteractionOptions12+

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isMultiSelectionEnabled | boolean | 否 | 是 | 表示拖拽过程中背板图是否支持多选聚拢效果。true表示支持多选聚拢效果，false表示不支持多选聚拢效果。该参数只在[Grid](ts-container-grid.md)和[List](ts-container-list.md)组件中的[GridItem](ts-container-griditem.md)组件和[ListItem](ts-container-listitem.md)组件生效。  当一个item组件设置为多选拖拽时，该组件的子组件不可拖拽。聚拢组件预览图设置的优先级为[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)中的string，dragPreview中的PixelMap，组件自截图，不支持dragPreview中的Builder形式。  不支持组件绑定[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)中参数存在isShown的模式。  默认值：false  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| defaultAnimationBeforeLifting | boolean | 否 | 是 | 表示是否启用长按浮起阶段组件自身的默认点按效果（缩小）。true表示启用默认点按效果，false表示不启用默认点按效果。  默认值：false  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| isLiftingDisabled15+ | boolean | 否 | 是 | 表示长按拖拽时，是否禁用浮起效果。true表示禁用浮起效果，false表示不禁用浮起效果。  如果设置为true，当组件支持拖拽并同时设置[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu8)时，仅弹出配置的自定义菜单预览。  默认值：false  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| enableEdgeAutoScroll18+ | boolean | 否 | 是 | 设置在拖拽至可滚动组件边缘时是否触发自动滚屏。true表示触发自动滚屏，false表示不触发自动滚屏。  默认值：true  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 表示拖拽时是否启用震动。true表示启用震动，false表示不启用震动。仅在存在蒙层的预览（通过[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)）场景生效。  **注意：** 仅当应用具备 ohos.permission.VIBRATE 权限，且用户启用了触感反馈时才会生效。  默认值：false  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |

## UniformDataType

PhonePC/2in1TabletTVWearable

type UniformDataType = UniformDataType

标准化数据类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [UniformDataType](js-apis-data-uniformtypedescriptor.md#uniformdatatype) | 标准化数据类型。 |

## ImageModifier12+

PhonePC/2in1TabletTVWearable

type ImageModifier = ImageModifier

图片组件modifier对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ImageModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 图片组件modifier对象。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（允许拖拽和落入）

示例1通过配置[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)设置组件是否可落入，通过配置[draggable](ts-universal-attributes-drag-drop.md#draggable)设置组件是否可拖拽。

```
1. // xxx.ets
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct ImageExample {
7. @State uri: string = "";
8. @State aBlockArr: string[] = [];
9. @State bBlockArr: string[] = [];
10. @State AVisible: Visibility = Visibility.Visible;
11. @State dragSuccess: Boolean = false;

13. build() {
14. Column() {
15. Text('Image拖拽')
16. .fontSize('30dp')
17. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
18. // $r('app.media.icon')需要替换为开发者所需的图像资源文件
19. Image($r('app.media.icon'))
20. .width(100)
21. .height(100)
22. .border({ width: 1 })
23. .visibility(this.AVisible)
24. .draggable(true)
25. .onDragEnd((event: DragEvent) => {
26. let ret = event.getResult();
27. if (ret == 0) {
28. console.info("enter ret == 0")
29. this.AVisible = Visibility.Hidden;
30. } else {
31. console.info("enter ret != 0")
32. this.AVisible = Visibility.Visible;
33. }
34. })
35. }
36. .margin({ bottom: 20 })

38. Row() {
39. Column() {
40. Text('不允许释放区域')
41. .fontSize('15dp')
42. .height('10%')
43. List() {
44. ForEach(this.aBlockArr, (item: string, index) => {
45. ListItem() {
46. Image(item)
47. .width(100)
48. .height(100)
49. .border({ width: 1 })
50. }
51. .margin({ left: 30, top: 30 })
52. }, (item: string) => item)
53. }
54. .height('90%')
55. .width('100%')
56. .allowDrop([uniformTypeDescriptor.UniformDataType.TEXT])
57. .onDrop((event?: DragEvent, extraParams?: string) => {
58. this.uri = JSON.parse(extraParams as string)?.extraInfo;
59. this.aBlockArr.splice(JSON.parse(extraParams as string)?.insertIndex, 0, this.uri);
60. console.info("ondrop not udmf data");
61. })
62. .border({ width: 1 })
63. }
64. .height("50%")
65. .width("45%")
66. .border({ width: 1 })
67. .margin({ left: 12 })

69. Column() {
70. Text('可释放区域')
71. .fontSize('15dp')
72. .height('10%')
73. List() {
74. ForEach(this.bBlockArr, (item: string, index) => {
75. ListItem() {
76. Image(item)
77. .width(100)
78. .height(100)
79. .border({ width: 1 })
80. }
81. .margin({ left: 30, top: 30 })
82. }, (item: string) => item)
83. }
84. .border({ width: 1 })
85. .height('90%')
86. .width('100%')
87. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
88. .onDrop((event?: DragEvent, extraParams?: string) => {
89. console.info("enter onDrop")
90. let dragData: UnifiedData = (event as DragEvent).getData() as UnifiedData;
91. if (dragData != undefined) {
92. let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
93. if (arr.length > 0) {
94. let image = arr[0] as unifiedDataChannel.Image;
95. this.uri = image.imageUri;
96. this.bBlockArr.splice(JSON.parse(extraParams as string)?.insertIndex, 0, this.uri);
97. } else {
98. console.info(`dragData arr is null`)
99. }
100. } else {
101. console.info(`dragData  is undefined`)
102. }
103. console.info("ondrop udmf data");
104. this.dragSuccess = true
105. })
106. }
107. .height("50%")
108. .width("45%")
109. .border({ width: 1 })
110. .margin({ left: 12 })
111. }
112. }.width('100%')
113. }
114. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/x6RrqgSRSL2nSWETjLDpKQ/zh-cn_image_0000002552959536.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=375081364DB01BC7933E2E0CA8D43E777526B9AE8F56D3E34141C18DF970C6E1)

### 示例2（设置预览图）

示例2通过配置[dragPreview](ts-universal-attributes-drag-drop.md#dragpreview11)设置拖拽过程的预览图。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DragPreviewDemo {
5. @Builder
6. dragPreviewBuilder() {
7. Column() {
8. Text("dragPreview")
9. .width(150)
10. .height(50)
11. .fontSize(20)
12. .borderRadius(10)
13. .textAlign(TextAlign.Center)
14. .fontColor(Color.Black)
15. .backgroundColor(Color.Pink)
16. }
17. }

19. @Builder
20. MenuBuilder() {
21. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
22. Text("menu item 1")
23. .fontSize(15)
24. .width(100)
25. .height(40)
26. .textAlign(TextAlign.Center)
27. .fontColor(Color.Black)
28. .backgroundColor(Color.Pink)
29. Divider()
30. .height(5)
31. Text("menu item 2")
32. .fontSize(15)
33. .width(100)
34. .height(40)
35. .textAlign(TextAlign.Center)
36. .fontColor(Color.Black)
37. .backgroundColor(Color.Pink)
38. }
39. .width(100)
40. }

42. build() {
43. Row() {
44. Column() {
45. // $r('app.media.image')需要替换为开发者所需的图像资源文件
46. Image($r('app.media.image'))
47. .width("30%")
48. .draggable(true)
49. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
50. .onDragStart(() => {
51. console.info("Image onDragStart")
52. })
53. .dragPreview(this.dragPreviewBuilder)
54. }
55. .width("100%")
56. }
57. .height("100%")
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/-r9ABkU_TFODf2Z9myaFdQ/zh-cn_image_0000002583479537.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=9B1C90D3A382D82E4B05F98A899C236EF70387437C3C984D581917D54F657571)

### 示例3（设置背板图样式）

示例3通过配置[dragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11)为ENABLE\_DEFAULT\_SHADOW、ENABLE\_DEFAULT\_RADIUS设置默认阴影和统一圆角效果。从API version 18开始，通过配置[dragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11)为ENABLE\_DRAG\_ITEM\_GRAY\_EFFECT设置灰显效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct dragPreviewOptionsDemo {
5. build() {
6. Row() {
7. Column() {
8. // $r('app.media.image')需要替换为开发者所需的图像资源文件
9. Image($r('app.media.image'))
10. .margin({ top: 10 })
11. .width("30%")
12. .draggable(true)
13. .dragPreviewOptions({ mode: DragPreviewMode.AUTO })
14. // $r('app.media.image')需要替换为开发者所需的图像资源文件
15. Image($r('app.media.image'))
16. .margin({ top: 10 })
17. .width("30%")
18. .border({
19. radius: {
20. topLeft: 1,
21. topRight: 2,
22. bottomLeft: 4,
23. bottomRight: 8
24. }
25. })
26. .draggable(true)
27. .onDragStart(() => {
28. console.info("Image onDragStart")
29. })
30. .dragPreviewOptions({
31. mode: [DragPreviewMode.ENABLE_DEFAULT_SHADOW, DragPreviewMode.ENABLE_DEFAULT_RADIUS,
32. DragPreviewMode.ENABLE_DRAG_ITEM_GRAY_EFFECT]
33. })
34. }
35. .width("100%")
36. .height("100%")
37. }
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/G-VjHOG9QbGrnziZGD-VoA/zh-cn_image_0000002552799888.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=E6B92A8C1BBDA224DCD76D5E794A3A141663D318160996CAB5236B8F42409E1A)

### 示例4（设置多选拖拽）

示例4通过配置[isMultiSelectionEnabled](ts-universal-attributes-drag-drop.md#draginteractionoptions12)实现Grid组件的多选拖拽效果。

```
1. @Entry
2. @Component
3. struct Example {
4. @State numbers: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

6. build() {
7. Column({ space: 5 }) {
8. Grid() {
9. ForEach(this.numbers, (item: number) => {
10. GridItem() {
11. Column()
12. .backgroundColor(Color.Blue)
13. .width('100%')
14. .height('100%')
15. }
16. .width(90)
17. .height(90)
18. .selectable(true)
19. .selected(true)
20. .dragPreviewOptions({}, { isMultiSelectionEnabled: true })
21. .onDragStart(() => {

23. })
24. }, (item: string) => item)
25. }
26. .columnsTemplate('1fr 1fr 1fr')
27. .rowsTemplate('1fr 1fr 1fr')
28. .height(300)
29. }
30. .width('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/-6qFgGEVSsKzoDO436HHLg/zh-cn_image_0000002583439583.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=A117CA1BF75DE9A19AEF0EE141404AD26834CED2CE30F1BC6F3CB672BF85085A)

### 示例5（设置默认点按效果）

示例5通过配置[defaultAnimationBeforeLifting](ts-universal-attributes-drag-drop.md#draginteractionoptions12)实现Grid组件的默认点按效果。

```
1. @Entry
2. @Component
3. struct Example {
4. @State numbers: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8]

6. build() {
7. Column({ space: 5 }) {
8. Grid() {
9. ForEach(this.numbers, (item: number) => {
10. GridItem() {
11. Column()
12. .backgroundColor(Color.Blue)
13. .width('100%')
14. .height('100%')
15. }
16. .width(90)
17. .height(90)
18. .selectable(true)
19. .selected(true)
20. .dragPreviewOptions({}, { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true })
21. .onDragStart(() => {

23. })
24. }, (item: string) => item)
25. }
26. .columnsTemplate('1fr 1fr 1fr')
27. .rowsTemplate('1fr 1fr 1fr')
28. .height(300)
29. }
30. .width('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/zalE58VtQC2qYMGtGoBtWg/zh-cn_image_0000002552959538.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=F38D76237C70C12580CBBE44A02D09350EB4F0302888433FAE3DF4DF7D2BAC8D)

### 示例6（自定义背板图样式）

示例6通过配置[ImageModifier](ts-universal-attributes-drag-drop.md#imagemodifier12)实现Image组件的自定义背板图样式。

```
1. // xxx.ets
2. import { ImageModifier } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct dragPreviewOptionsDemo {
7. @State myModifier: ImageAttribute = new ImageModifier().opacity(0.5)
8. @State vis: boolean = true
9. @State changeValue: string = ''
10. @State submitValue: string = ''
11. @State positionInfo: CaretOffset = { index: 0, x: 0, y: 0 }
12. controller: SearchController = new SearchController()
13. @State OpacityIndex: number = 0
14. @State OpacityList: (number | undefined | null)[] = [
15. 0.3, 0.5, 0.7, 1, -50, 0, 10, undefined, null
16. ]

18. build() {
19. Row() {
20. Column() {
21. Text(this.OpacityList[this.OpacityIndex] + "")
22. Button("Opacity")
23. .onClick(() => {
24. this.OpacityIndex++
25. if (this.OpacityIndex > this.OpacityList.length - 1) {
26. this.OpacityIndex = 0
27. }
28. })
29. // $r('app.media.image')需要替换为开发者所需的图像资源文件
30. Image($r('app.media.image'))
31. .margin({ top: 10 })
32. .width("100%")
33. .draggable(true)
34. .dragPreviewOptions({
35. modifier: this.myModifier.opacity(this.OpacityList[this.OpacityIndex]) as ImageModifier
36. })
37. }
38. .width("50%")
39. .height("50%")
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/tdG7sluySxm5kKAxYusa1w/zh-cn_image_0000002583479539.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=6EAF873CC3CC23B8812E8870F44E97F3D9BE7EED2E128E0F439F7BB08B35EB21)

### 示例7（图片拖拽设置）

示例7展示了不同图片（在线图片资源、本地图片资源和PixelMap）在拖拽时组件的设置。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

```
1. // xxx.ets
2. import { uniformTypeDescriptor, unifiedDataChannel } from '@kit.ArkData';
3. import { image } from '@kit.ImageKit';
4. import { request } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { buffer } from '@kit.ArkTS';
7. import { BusinessError } from '@kit.BasicServicesKit';

9. @Entry
10. @Component
11. struct ImageDrag {
12. @State targetImage1: string | PixelMap | null = null;
13. @State targetImage2: string | PixelMap | null = null;
14. @State targetImage3: string | PixelMap | null = null;
15. context: Context | undefined = this.getUIContext().getHostContext();
16. filesDir = this.context?.filesDir;

18. public async createPixelMap(pixelMap: unifiedDataChannel.SystemDefinedPixelMap): Promise<image.PixelMap | null> {
19. let mWidth: number = (pixelMap.details?.width ?? -1) as number;
20. let mHeight: number = (pixelMap.details?.height ?? -1) as number;
21. let mPixelFormat: image.PixelMapFormat =
22. (pixelMap.details?.['pixel-format'] ?? image.PixelMapFormat.UNKNOWN) as image.PixelMapFormat;
23. let mItemPixelMapData: Uint8Array = pixelMap.rawData;
24. const opts: image.InitializationOptions = {
25. editable: false, pixelFormat: mPixelFormat, size: {
26. height: mHeight,
27. width: mWidth
28. }
29. };
30. const buffer: ArrayBuffer = mItemPixelMapData.buffer.slice(mItemPixelMapData.byteOffset,
31. mItemPixelMapData.byteLength + mItemPixelMapData.byteOffset);
32. try {
33. let pixelMap: image.PixelMap = await image.createPixelMap(buffer, opts);
34. return pixelMap;
35. } catch (err) {
36. console.error('dragtest--> getPixelMap', err);
37. return null;
38. }
39. }

41. build() {
42. Column() {
43. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center }) {
44. // 在线图片资源拖出
45. Column() {
46. Text('Online Image').fontSize(14)
47. Image('https://www.example.com/xxx.png')// 请填写一个具体的网络图片地址
48. .objectFit(ImageFit.Contain)
49. .draggable(true)
50. .onDragStart(() => {
51. })
52. .width(100)
53. .height(100)
54. }
55. .border({
56. width: 2,
57. color: Color.Gray,
58. radius: 5,
59. style: BorderStyle.Dotted
60. })
61. .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)

63. // 本地图片资源拖出
64. Column() {
65. Text('Local Image').fontSize(14)
66. // $r('app.media.example')需要替换为开发者所需的图像资源文件
67. Image($r('app.media.example'))
68. .objectFit(ImageFit.Contain)
69. .draggable(true)
70. .onDragStart(() => {
71. })
72. .width(100)
73. .height(100)
74. }
75. .border({
76. width: 2,
77. color: Color.Gray,
78. radius: 5,
79. style: BorderStyle.Dotted
80. })
81. .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)

83. // PixelMap拖出
84. Column() {
85. Text('PixelMap').fontSize(14)
86. // $r('app.media.example')需要替换为开发者所需的图像资源文件
87. Image(this.context?.resourceManager.getDrawableDescriptor($r('app.media.example').id).getPixelMap())
88. .objectFit(ImageFit.Contain)
89. .draggable(true)
90. .onDragStart(() => {
91. })
92. .width(100)
93. .height(100)
94. }
95. .border({
96. width: 2,
97. color: Color.Gray,
98. radius: 5,
99. style: BorderStyle.Dotted
100. })
101. .alignItems(HorizontalAlign.Center).justifyContent(FlexAlign.Center)
102. }

104. // 落入数据类型为Image
105. Text('Data type is Image').fontSize(14).margin({ top: 10 })
106. Column() {
107. Image(this.targetImage1)
108. .objectFit(ImageFit.Contain)
109. .width('70%')
110. .height('70%')
111. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
112. .onDrop((event: DragEvent, extraParams: string) => {
113. if (extraParams === null || extraParams === undefined) {
114. return;
115. }
116. // 通过extraParams获取图片
117. let arr: Record<string, object> = JSON.parse(extraParams) as Record<string, object>;
118. let uri = arr['extraInfo'];
119. if (typeof uri == 'string') {
120. this.targetImage1 = uri;
121. try {
122. request.downloadFile(this.context, {
123. url: uri,
124. filePath: this.filesDir + '/example.png'
125. }).then((downloadTask: request.DownloadTask) => {
126. let file = fileIo.openSync(this.filesDir + '/example.png', fileIo.OpenMode.READ_WRITE);
127. let arrayBuffer = new ArrayBuffer(1024);
128. let readLen = fileIo.readSync(file.fd, arrayBuffer);
129. let buf = buffer.from(arrayBuffer, 0, readLen);
130. console.info(`The content of file: ${buf.toString()}`);
131. fileIo.closeSync(file);
132. })
133. } catch (error) {
134. }
135. }
136. })
137. }
138. .width('70%')
139. .height('25%')
140. .border({
141. width: 2,
142. color: Color.Gray,
143. radius: 5,
144. style: BorderStyle.Dotted
145. })
146. .alignItems(HorizontalAlign.Center)
147. .justifyContent(FlexAlign.Center)

149. Column() {
150. Image(this.targetImage2)
151. .objectFit(ImageFit.Contain)
152. .width('70%')
153. .height('70%')
154. .allowDrop([uniformTypeDescriptor.UniformDataType.IMAGE])
155. .onDrop((event: DragEvent, extraParams: string) => {
156. // 通过uniformTypeDescriptor获取图片
157. let data: UnifiedData = event.getData();
158. let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
159. if (records[0].getType() === uniformTypeDescriptor.UniformDataType.IMAGE) {
160. let image: unifiedDataChannel.Image = records[0] as unifiedDataChannel.Image;
161. this.targetImage2 = image.imageUri;
162. }
163. })
164. }
165. .width('70%')
166. .height('25%')
167. .border({
168. width: 2,
169. color: Color.Gray,
170. radius: 5,
171. style: BorderStyle.Dotted
172. })
173. .alignItems(HorizontalAlign.Center)
174. .justifyContent(FlexAlign.Center)

176. // 落入数据类型为PixelMap
177. Text('Data type is PixelMap').fontSize(14).margin({ top: 10 })
178. Column() {
179. Image(this.targetImage3)
180. .objectFit(ImageFit.Contain)
181. .width('70%')
182. .height('70%')
183. .allowDrop([uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP])
184. .onDrop(async (event: DragEvent, extraParams: string) => {
185. // 通过uniformTypeDescriptor获取图片
186. let data: UnifiedData = event.getData();
187. let records: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
188. if (records[0].getType() === uniformTypeDescriptor.UniformDataType.OPENHARMONY_PIXEL_MAP) {
189. let record: unifiedDataChannel.SystemDefinedPixelMap =
190. records[0] as unifiedDataChannel.SystemDefinedPixelMap;
191. this.targetImage3 = await this.createPixelMap(record);

193. // 落盘到本地
194. const imagePackerApi = image.createImagePacker();
195. let packOpts: image.PackingOption = { format: "image/jpeg", quality: 98 };
196. const path: string = this.context?.cacheDir + "/pixel_map.jpg";
197. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
198. imagePackerApi.packToFile(this.targetImage3, file.fd, packOpts).then(() => {
199. // 直接打包进文件
200. }).catch((error: BusinessError) => {
201. console.error('Failed to pack the image. And the error is: ' + error);
202. })
203. }
204. })
205. }
206. .width('70%')
207. .height('25%')
208. .border({
209. width: 2,
210. color: Color.Gray,
211. radius: 5,
212. style: BorderStyle.Dotted
213. })
214. .alignItems(HorizontalAlign.Center)
215. .justifyContent(FlexAlign.Center)

217. }.width('100%').height('100%')
218. }
219. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Ps_3rJrJSU-eEK4iomzofQ/zh-cn_image_0000002552799890.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=F869780FB478B95F248D31D9B01F73D52D3197A145350BC9F7A25D03117D0A72)

### 示例8（设置图片拖拽震动）

从API version 18开始，示例8通过设置[enableHapticFeedback](ts-universal-attributes-drag-drop.md#draginteractionoptions12)实现图片拖拽的震动效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DragPreviewDemo {
5. @Builder
6. MenuBuilder() {
7. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
8. Text("menu item 1")
9. .fontSize(15)
10. .width(100)
11. .height(40)
12. .textAlign(TextAlign.Center)
13. .fontColor(Color.Black)
14. .backgroundColor(Color.Pink)
15. Divider()
16. .height(5)
17. Text("menu item 2")
18. .fontSize(15)
19. .width(100)
20. .height(40)
21. .textAlign(TextAlign.Center)
22. .fontColor(Color.Black)
23. .backgroundColor(Color.Pink)
24. }
25. .width(100)
26. }

28. build() {
29. Row() {
30. Column() {
31. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
32. Image($r('app.media.app_icon'))
33. .width("30%")
34. .draggable(true)
35. .dragPreviewOptions({},
36. { isMultiSelectionEnabled: true, defaultAnimationBeforeLifting: true, enableHapticFeedback: true })
37. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
38. .onDragStart(() => {
39. console.info("Image onDragStart")
40. })
41. }
42. .width("100%")
43. }
44. .height("100%")
45. }
46. }
```

### 示例9（自定义预览图）

从API version 15开始，示例9通过配置[onlyForLifting](ts-universal-events-drag-drop.md#previewconfiguration15)实现自定义预览图，仅用于浮起效果以及配置[isLiftingDisabled](ts-universal-attributes-drag-drop.md#draginteractionoptions12)实现禁用浮起效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LiftingExampleDemo {
5. @Builder
6. dragPreviewBuilder() {
7. Column() {
8. Text("dragPreview builder")
9. .width(150)
10. .height(50)
11. .fontSize(20)
12. .borderRadius(10)
13. .textAlign(TextAlign.Center)
14. .fontColor(Color.Black)
15. .backgroundColor(Color.Green)
16. }
17. }

19. @Builder
20. MenuBuilder() {
21. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
22. Text("menu 1")
23. .fontSize(25)
24. .width(200)
25. .height(60)
26. .textAlign(TextAlign.Center)
27. .fontColor(Color.Black)
28. .backgroundColor(Color.Green)
29. Divider()
30. .height(5)
31. Text("menu 2")
32. .fontSize(25)
33. .width(200)
34. .height(60)
35. .textAlign(TextAlign.Center)
36. .fontColor(Color.Black)
37. .backgroundColor(Color.Green)
38. }
39. .width(100)
40. }

42. build() {
43. Column() {
44. Column() {
45. Text("禁用浮起效果")
46. .fontSize(30)
47. .height(30)
48. .backgroundColor('#FFFFFF')
49. .margin({ top: 30 })
50. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
51. Image($r('app.media.startIcon'))
52. .width("40%")
53. .draggable(true)
54. .margin({ top: 15 })
55. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
56. .onDragStart(() => {
57. })
58. .dragPreviewOptions({}, {
59. isLiftingDisabled: true
60. })
61. .dragPreview(this.dragPreviewBuilder, {
62. onlyForLifting: true,
63. delayCreating: true
64. })
65. }.width("100%")

67. Column() {
68. Text("仅用于浮起效果")
69. .fontSize(30)
70. .height(30)
71. .backgroundColor('#FFFFFF')
72. .margin({ top: 80 })
73. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
74. Image($r('app.media.startIcon'))
75. .width("40%")
76. .draggable(true)
77. .margin({ top: 15 })
78. .onDragStart(() => {
79. })
80. .dragPreviewOptions({}, {
81. isLiftingDisabled: false
82. })
83. .dragPreview(this.dragPreviewBuilder, {
84. onlyForLifting: true,
85. delayCreating: true
86. })
87. }.width("100%")
88. }.height("100%")
89. }
90. }
```

自定义预览图用于浮起效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/VrCFicbnSySbGViZxYGX6Q/zh-cn_image_0000002583439585.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=64ECB0D246EEAADB67323774A7C2E5414D88A0DEE9EA526EC286902BB9E530FA)

自定义预览图禁用浮起效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/DGQTz1o6S4qMSuGvtOR8aA/zh-cn_image_0000002552959540.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=F664F568AB4CDBD84A53A12EFA3B3C47DF5F8074331680E5DB8AD0BB8849B1DA)

### 示例10（以拖拽预览图初始尺寸计算跟手点位置）

从API version 19开始，示例10通过配置[DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明)为ENABLE\_TOUCH\_POINT\_CALCULATION\_BASED\_ON\_FINAL\_PREVIEW实现根据拖拽预览图的初始尺寸来计算拖拽过程中跟手点位置。当设置[DragPreviewMode](ts-universal-attributes-drag-drop.md#dragpreviewmode11枚举说明)为ENABLE\_MULTI\_TILE\_EFFECT时，该属性不生效。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
5. private iconStr: ResourceStr = $r("app.media.app_icon")

7. @Builder
8. MyPreview() {
9. // $r('app.media.image')需要替换为开发者所需的图像资源文件
10. Image($r('app.media.image'))
11. .width(100)
12. .height(100)
13. }

15. @Builder
16. MyMenuPreview() {
17. Column() {
18. // $r('app.media.image')需要替换为开发者所需的图像资源文件
19. Image($r('app.media.image'))
20. .width(100)
21. .height(100)
22. }
23. .backgroundColor(Color.Green)
24. .width(300)
25. .height(300)
26. }

28. @Builder
29. MyMenu() {
30. Menu() {
31. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
32. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
33. }
34. }

36. @Builder
37. SubMenu() {
38. Menu() {
39. MenuItem({ content: "复制", labelInfo: "Ctrl+C" })
40. MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })
41. }
42. }

44. build() {
45. NavDestination() {
46. Scroll() {
47. Column() {
48. Text("no ENABLE_TOUCH_POINT_CALCULATION_BASED_ON_FINAL_PREVIEW")
49. // $r('app.media.image')需要替换为开发者所需的图像资源文件
50. Image($r('app.media.image'))
51. .width(200)
52. .height(200)
53. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
54. preview: this.MyPreview
55. })
56. .dragPreview(this.MyMenuPreview)
57. .draggable(true)

59. Text("ENABLE_TOUCH_POINT_CALCULATION_BASED_ON_FINAL_PREVIEW")
60. // $r('app.media.image')需要替换为开发者所需的图像资源文件
61. Image($r('app.media.image'))
62. .width(200)
63. .height(200)
64. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
65. preview: this.MyPreview
66. })
67. .dragPreview(this.MyMenuPreview)
68. .draggable(true)
69. .dragPreviewOptions({
70. mode: [DragPreviewMode.ENABLE_TOUCH_POINT_CALCULATION_BASED_ON_FINAL_PREVIEW]
71. })
72. }.width('100%')
73. }
74. }
75. .height('100%')
76. .width('100%')
77. }
78. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/jN7SH5TJQYaW2JHB8w7fGw/zh-cn_image_0000002583479541.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=DC95780B8BA2E4767DA89E52F4A91FB4F76EEACF987AEF549B65EAD02B762BE4)

### 示例11（长按浮起预览图与拖拽预览图过渡动效）

从API version 19开始，示例11通过配置[DraggingSizeChangeEffect](ts-universal-attributes-drag-drop.md#draggingsizechangeeffect19枚举说明)实现不同拖拽过渡效果。

```
1. @Entry
2. @Component
3. struct Index {
4. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件
5. private iconStr: ResourceStr = $r("app.media.app_icon")

7. @Builder
8. MyPreview() {
9. // $r('app.media.image')需要替换为开发者所需的图像资源文件
10. Image($r('app.media.image'))
11. .width(200)
12. .height(200)
13. }

15. @Builder
16. MyMenuPreviewSame() {
17. Column() {
18. // $r('app.media.image')需要替换为开发者所需的图像资源文件
19. Image($r('app.media.image'))
20. .width(300)
21. .height(300)
22. }
23. }

25. @Builder
26. MyMenuPreview() {
27. Column() {
28. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
29. Image($r('app.media.startIcon'))
30. .width(300)
31. .height(300)
32. }
33. }

35. @Builder
36. MyMenu() {
37. Menu() {
38. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
39. MenuItem({ startIcon: this.iconStr, content: "菜单选项" })
40. }
41. }

43. @Builder
44. SubMenu() {
45. Menu() {
46. MenuItem({ content: "复制", labelInfo: "Ctrl+C" })
47. MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })
48. }
49. }

51. build() {
52. Column() {
53. Text("sizeChangeEffect: SIZE_TRANSITION，长按弹出菜单，拖拽移动后菜单预览图过渡到预览图，有缩放无叠加效果")
54. .margin({ top: 10 })
55. // $r('app.media.image')需要替换为开发者所需的图像资源文件
56. Image($r('app.media.image'))
57. .width(200)
58. .height(200)
59. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
60. preview: this.MyMenuPreviewSame
61. })
62. .dragPreview(this.MyPreview)
63. .dragPreviewOptions({
64. sizeChangeEffect: DraggingSizeChangeEffect.SIZE_TRANSITION
65. })
66. .draggable(true)

68. Text("sizeChangeEffect: SIZE_CONTENT_TRANSITION，长按弹出菜单，拖拽移动后菜单预览图和拖拽预览图两层叠加过渡")
69. .margin({ top: 10 })
70. // $r('app.media.image')需要替换为开发者所需的图像资源文件
71. Image($r('app.media.image'))
72. .width(200)
73. .height(200)
74. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
75. preview: this.MyMenuPreview
76. })
77. .dragPreview(this.MyPreview)
78. .dragPreviewOptions({
79. sizeChangeEffect: DraggingSizeChangeEffect.SIZE_CONTENT_TRANSITION
80. })
81. .draggable(true)
82. }
83. .height('100%')
84. .width('100%')
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/hf7N7xC8Q1-m2QYQkX15jQ/zh-cn_image_0000002552799892.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=585B831B54E3E22698461C75E8158E504CA2F1420196326FE0C351B3A88220F9)

### 示例12（设置自定义组件落入）

从API version 23开始，示例12通过组件的[onDragStart](ts-universal-events-drag-drop.md#ondragstart)接口传递其类型，并在目标组件的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)属性中设置允许该类型落入，即可实现自定义组件的拖拽落入功能。

```
1. import { unifiedDataChannel } from '@kit.ArkData';

3. @Entry
4. @Component
5. struct CustomExample {
6. // 用于存储已放置的组件信息
7. @State droppedItems: Array<string> = []

9. build() {
10. Column() {
11. // 标题
12. Text('自定义组件拖拽落入')
13. .fontSize(25)
14. .fontWeight(FontWeight.Bold)
15. .margin(10)

17. // 拖拽区域和放置区域的容器
18. Row() {
19. // 左侧 - 拖拽起始区域
20. Column() {
21. Text('拖拽源区域')
22. .fontSize(18)
23. .fontWeight(FontWeight.Medium)
24. .margin(10)

26. // 自定义组件 - 可拖拽
27. CustomCard({ title: '自定义卡片', color: Color.Blue })
28. .draggable(true)
29. .onDragStart((event: DragEvent) => {
30. // 构造符合UnifiedData类型的数据
31. let customCardData: Record<string, string> = {
32. 'uniformDataType': 'custom.card',
33. 'value': '自定义卡片'
34. }
35. let unifiedRecord = new unifiedDataChannel.UnifiedRecord('custom.card', customCardData);
36. let unifiedData = new unifiedDataChannel.UnifiedData(unifiedRecord);
37. event.setData(unifiedData);
38. })
39. }
40. .backgroundColor(Color.White)
41. .border({ color: '#ff0e0303', width: 1 })
42. .width('40%')
43. .height(300)

45. // 右侧 - 放置区域
46. Column() {
47. Text('放置区域')
48. .fontSize(18)
49. .fontWeight(FontWeight.Medium)
50. .margin(10)

52. // 放置区域内容
53. if (this.droppedItems.length === 0) {
54. Text('将组件拖到此处')
55. .fontSize(16)
56. .opacity(0.6)
57. } else {
58. // 显示已放置的组件
59. ForEach(this.droppedItems, (item: string) => {
60. CustomCard({ title: item, color: Color.Blue })
61. }, (item: string) => item)
62. }
63. }
64. .backgroundColor(Color.White)
65. .border({ color: '#ff0e0303', width: 1 })
66. .width('40%')
67. .height(300)
68. // 允许放置的类型 - 字符串数组形式
69. .allowDrop(['custom.card'])
70. .onDrop((event: DragEvent) => {
71. console.info('setData onDrop success');
72. let data = event.getData()
73. let arr: Array<unifiedDataChannel.UnifiedRecord> = data.getRecords();
74. if (arr.length > 0) {
75. if (arr[0].getTypes()[0] === 'custom.card') {
76. let customCardData = arr[0].getValue() as Record<string, string>;
77. this.droppedItems.push(customCardData.value)
78. }
79. }
80. })
81. }
82. .justifyContent(FlexAlign.SpaceAround)
83. .width('100%')
84. .height('70%')

86. // 操作说明
87. Text('操作说明：长按左侧卡片并拖拽到右侧区域')
88. .fontSize(14)
89. .opacity(0.7)
90. .margin(10)
91. }
92. .width('100%')
93. .height('65%')
94. .backgroundColor('#f8f9fa')
95. }
96. }

98. // 自定义卡片组件
99. @Component
100. struct CustomCard {
101. title: string = '默认标题'
102. color: Color = Color.Gray

104. build() {
105. Column() {
106. Text(this.title)
107. .fontSize(16)
108. .fontColor(Color.White)
109. .fontWeight(FontWeight.Medium)
110. .margin(5)

112. Text('这是一个自定义组件')
113. .fontColor(Color.White)
114. .fontSize(14)
115. .opacity(0.7)
116. }
117. .backgroundColor(this.color)
118. .borderRadius(12)
119. .width(120)
120. .height(100)
121. }
122. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/6_wybUJQSdSI9heJxXx1Bg/zh-cn_image_0000002583439587.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000109Z&HW-CC-Expire=86400&HW-CC-Sign=47B5851AE7FC9DCE4792AD11392321171D7C628A6C8EF0E2F42889BB61454134)
