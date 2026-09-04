---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer
title: SideBarContainer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 栅格与分栏 > SideBarContainer
category: harmonyos-references
scraped_at: 2026-09-05T06:17:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9b8828d2273d942612e72ad7ed053545caabd0370536484301c18ee068c27ac7
---

提供侧边栏可以显示和隐藏的容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区。支持侧边栏导航布局场景，通过控制按钮或手势切换侧边栏显隐，可提升应用导航效率。

**说明** 

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

可以包含子组件。

**说明** 

* 子组件类型：系统组件和自定义组件，不支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 子组件个数：必须且仅包含2个子组件。
* 子组件个数异常时：3个或以上子组件，显示第一个和第二个。1个子组件，显示侧边栏，内容区为空白。
* SideBarContainer走焦时，先在内容区走焦，再在侧边栏走焦。

## 接口

SideBarContainer( type?: SideBarContainerType )

创建侧边栏容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [SideBarContainerType](ts-container-sidebarcontainer.md#sidebarcontainertype枚举说明) | 否 | 设置侧边栏的显示类型。  默认值：SideBarContainerType.Embed |

## SideBarContainerType枚举说明

容器内侧边栏类型枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Embed | 0 | 侧边栏嵌入到组件内，和内容区并列显示。适用于需要同时展示侧边栏和内容区的场景。  整体容器大小不变时，显示侧边栏会导致内容区缩小，隐藏侧边栏会扩大内容区。  组件尺寸小于[minContentWidth](ts-container-sidebarcontainer.md#mincontentwidth10) + [minSideBarWidth](ts-container-sidebarcontainer.md#minsidebarwidth)，并且未设置showSideBar时，侧边栏自动隐藏。  设置了showSideBar属性时，以showSideBar属性设置的值为准。  未设置minSideBarWidth或minContentWidth时，采用对应接口的默认值进行计算。  组件在自动隐藏后，如果通过点击控制按钮唤出侧边栏，则侧边栏悬浮在内容区上显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Overlay | 1 | 侧边栏浮在内容区上面，不会影响内容区的大小。适用于需要临时展示侧边栏的场景。  组件尺寸小于minContentWidth时，内容区会被截断显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| AUTO10+ | 2 | 组件尺寸大于等于minSideBarWidth + minContentWidth时，采用Embed模式显示。  组件尺寸小于minSideBarWidth + minContentWidth时，采用Overlay模式显示。适用于需要响应式布局或多设备适配的场景。  未设置minSideBarWidth或minContentWidth时，会使用未设置接口的默认值进行计算，若计算的值小于600vp，则使用600vp作为模式切换的临界值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| DISPLACE | 3 | 侧边栏和内容区并列显示，内容区超出部分移出组件外。侧边栏展开时，内容区显示灰色蒙层（颜色为#33000000）并被禁用事件，点击内容区可收起侧边栏。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### showSideBar

showSideBar(value: boolean)

设置是否显示侧边栏。设置该属性值后会触发侧边栏的显示/隐藏动画。

当showSideBar属性未设置时，依据组件大小进行自动显示：小于minSideBarWidth + minContentWidth时默认不显示侧边栏，大于等于时默认显示侧边栏。

从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示侧边栏。  true：显示侧边栏  false：不显示侧边栏  默认值：true |

### controlButton

controlButton(value: ButtonStyle)

设置侧边栏控制按钮的属性。控制按钮用于切换侧边栏的显示和隐藏状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ButtonStyle](ts-container-sidebarcontainer.md#buttonstyle对象说明) | 是 | 侧边栏控制按钮的属性，用于配置控制按钮的位置、大小和图标。 |

### showControlButton

showControlButton(value: boolean)

设置是否显示控制按钮。控制按钮用于控制showSideBar属性的切换，点击可显示或隐藏侧边栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示控制按钮。  true：显示控制按钮  false：不显示控制按钮  默认值：true |

**说明** 

通过控制按钮切换侧边栏的显隐会触发侧边栏的显示/隐藏动画。

### sideBarWidth

sideBarWidth(value: number)

设置侧边栏的宽度。设置为小于0的值时按默认值显示。受minSideBarWidth和maxSideBarWidth限制，当设置的值不在限制范围内时，取最近的边界值。

从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 侧边栏的宽度。  默认值：240vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。  **说明：**  API version 10以下版本的默认值为200vp，API version 10及以上版本的默认值为240vp。 |

### sideBarWidth9+

sideBarWidth(value: Length)

设置侧边栏的宽度。设置为小于0的值时按默认值显示。受minSideBarWidth和maxSideBarWidth限制，当设置的值不在限制范围内时，取最近的边界值。与[sideBarWidth](ts-container-sidebarcontainer.md#sidebarwidth)相比，value参数新增了对百分比字符串和其他[像素单位](ts-pixel-units.md)的支持。

从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 侧边栏的宽度。  默认值：240vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。  **说明：**  API version 9的默认值为200vp，API version 10及以上版本的默认值为240vp。 |

### minSideBarWidth

minSideBarWidth(value: number)

设置侧边栏最小宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。

minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 侧边栏最小宽度。  默认值：API version 9及以下版本默认值为200vp，API version 10的默认值为240vp。  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |

### minSideBarWidth9+

minSideBarWidth(value: Length)

设置侧边栏最小宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。与[minSideBarWidth](ts-container-sidebarcontainer.md#minsidebarwidth)相比，value参数新增了对百分比字符串和其他[像素单位](ts-pixel-units.md)的支持。

minSideBarWidth优先于侧边栏子组件minWidth，minSideBarWidth未设置时默认值优先级高于侧边栏子组件minWidth。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 侧边栏最小宽度。  默认值：API version 9及以下版本默认值为200vp，API version 10的默认值为240vp。  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |

### maxSideBarWidth

maxSideBarWidth(value: number)

设置侧边栏最大宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。

maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置侧边栏最大宽度。  默认值：280vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。  值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。 |

### maxSideBarWidth9+

maxSideBarWidth(value: Length)

设置侧边栏最大宽度。设置为小于0的值时按默认值显示。值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。与[maxSideBarWidth](ts-container-sidebarcontainer.md#maxsidebarwidth)相比，value参数新增了对百分比字符串和其他[像素单位](ts-pixel-units.md)的支持。

maxSideBarWidth优先于侧边栏子组件maxWidth，maxSideBarWidth未设置时默认值优先级高于侧边栏子组件maxWidth。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 设置侧边栏最大宽度。  默认值：280vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。  值不能超过侧边栏容器本身宽度，超过则使用侧边栏容器本身宽度。 |

### autoHide9+

autoHide(value: boolean)

设置当侧边栏拖拽到小于最小宽度后，是否自动隐藏。受minSideBarWidth属性方法影响，minSideBarWidth属性方法未设置值使用默认值。自动隐藏后showSideBar属性值同步更新为false，并触发onChange事件。

拖拽过程中判断是否要自动隐藏。小于最小宽度时需要拖拽越界一定距离（具体距离由系统实现决定）后触发自动隐藏，具有阻尼效果，避免误操作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 侧边栏拖拽到小于最小宽度后，是否自动隐藏。  true：会自动隐藏  false：不会自动隐藏  默认值：true |

### sideBarPosition9+

sideBarPosition(value: SideBarPosition)

设置侧边栏显示位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SideBarPosition](ts-container-sidebarcontainer.md#sidebarposition9枚举说明) | 是 | 侧边栏显示位置。  默认值：SideBarPosition.Start |

### divider10+

divider(value: DividerStyle | null)

设置分割线的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DividerStyle](ts-container-sidebarcontainer.md#dividerstyle10对象说明) | null | 是 | 分割线的样式。  默认为DividerStyle：显示分割线。  - null或undefined：分割线样式保持默认值，不做任何改变。  **说明：**  API version 11及以下版本，null效果为不显示分割线。 |

### minContentWidth10+

minContentWidth(value: Dimension)

设置SideBarContainer组件内容区可显示的最小宽度。

设置为小于0，内容区显示的最小宽度为360vp，未设置该属性时，组件内容区的可缩小到0。

Embed场景下，增大组件尺寸时仅增大内容区的尺寸。

缩小组件尺寸时，先缩小内容区的尺寸至minContentWidth。继续缩小组件尺寸时，保持内容区宽度minContentWidth不变，优先缩小侧边栏的尺寸。

当缩小侧边栏的尺寸至minSideBarWidth后，继续缩小组件尺寸时，

* 如果[autoHide](ts-container-sidebarcontainer.md#autohide9)属性为false，则会保持侧边栏宽度[minSideBarWidth](ts-container-sidebarcontainer.md#minsidebarwidth)和内容区宽度minContentWidth不变，但内容区会被截断显示；
* 如果autoHide属性为true，则会优先隐藏侧边栏，然后继续缩小至内容区宽度minContentWidth后，内容区宽度保持不变，但内容区会被截断显示。

minContentWidth优先于侧边栏的[maxSideBarWidth](ts-container-sidebarcontainer.md#maxsidebarwidth)与sideBarWidth属性，minContentWidth未设置时默认值优先级低于设置的minSideBarWidth与maxSideBarWidth属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | SideBarContainer组件内容区可显示的最小宽度。  默认值：360vp  取值范围：[0, +∞)  设置为小于0时按默认值处理。 |

### showSideBarWithGesture

showSideBarWithGesture(value: boolean)

设置是否支持通过手势滑动来显示或隐藏侧边栏。未通过该接口设置时，不支持通过手势滑动显示或隐藏侧边栏。

**说明** 

* 手势滑动生效范围为侧边栏+内容区（不含分割线），滑动距离达到100vp时改变侧边栏显示或隐藏状态，最大可滑动距离等于侧边栏宽度。
* 当侧边栏位于容器左侧时：

  + 侧边栏隐藏时可向右滑动展开侧边栏。
  + 侧边栏显示时可向左滑动关闭侧边栏。
* 当侧边栏位于容器右侧时：

  + 侧边栏隐藏时可向左滑动展开侧边栏。
  + 侧边栏显示时可向右滑动关闭侧边栏。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置是否支持通过手势滑动显示或隐藏侧边栏。  true：支持手势滑动控制。  false：不支持手势滑动控制。  默认值：false |

## ButtonStyle对象说明

设置侧边栏控制按钮的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 是 | 设置侧边栏控制按钮距离容器左界限的间距。  默认值：16vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |
| top | number | 否 | 是 | 设置侧边栏控制按钮距离容器上界限的间距。  默认值：48vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |
| width | number | 否 | 是 | 设置侧边栏控制按钮的宽度。  默认值：  API version 9及之前版本：32vp  从API version 10开始：24vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |
| height | number | 否 | 是 | 设置侧边栏控制按钮的高度。  默认值：  API version 9及之前版本：32vp  从API version 10开始：24vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |
| icons | [ButtonIconOptions18+](ts-container-sidebarcontainer.md#buttoniconoptions18对象说明) | 否 | 是 | 设置侧边栏控制按钮的图标。  资源获取错误以及未设置该属性时，使用默认图标。 |

## ButtonIconOptions18+对象说明

设置侧边栏控制按钮的图标。

**说明** 

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| shown8+ | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 否 | 设置侧边栏显示时控制按钮的图标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| hidden8+ | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 否 | 设置侧边栏隐藏时控制按钮的图标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| switching8+ | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 是 | 设置侧边栏显示和隐藏状态切换时控制按钮的图标。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## SideBarPosition9+枚举说明

侧边栏显示位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Start | 0 | 侧边栏位于容器左侧。 |
| End | 1 | 侧边栏位于容器右侧。 |

## DividerStyle10+对象说明

设置分割线的样式。

**说明** 

针对侧边栏子组件设置[width](ts-universal-attributes-size.md#width)，[height](ts-universal-attributes-size.md#height)时，宽高都不生效。

针对侧边栏内容区设置[width](ts-universal-attributes-size.md#width)，[height](ts-universal-attributes-size.md#height)时，宽高都不生效，默认占满SideBarContainer的剩余空间。

当[showSideBar](ts-container-sidebarcontainer.md#showsidebar)属性未设置时，依据组件大小进行自动显示：

* 小于[minSideBarWidth](ts-container-sidebarcontainer.md#minsidebarwidth) + [minContentWidth](ts-container-sidebarcontainer.md#mincontentwidth10)：默认不显示侧边栏。
* 大于等于minSideBarWidth + minContentWidth：默认显示侧边栏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 否 | 分割线的线宽。  默认值：1vp  单位：vp  取值范围：[0, +∞)  异常值时取默认值。  **说明**：  分割线的宽度不支持百分比设置。优先级低于[通用属性height](ts-universal-attributes-size.md#height)，超过通用属性设置大小时，按照通用属性进行裁切。部分设备硬件中存在1像素取整后分割线不显示问题，建议使用2像素。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：#000000，3%，黑色。 |
| startMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏顶端的距离。  默认值：0  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |
| endMargin | [Length](ts-types.md#length) | 否 | 是 | 分割线与侧边栏底端的距离。  默认值：0  单位：vp  取值范围：[0, +∞)  异常值时取默认值。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

onChange(callback: (value: boolean) => void)

当侧边栏的状态在显示和隐藏之间切换时触发回调。

触发该事件的条件：

1. showSideBar属性值变换时。
2. showSideBar属性自适应行为变化时。
3. 分割线拖拽触发[autoHide](ts-container-sidebarcontainer.md#autohide9)时。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | true表示显示，false表示隐藏。 |

## 示例

该示例主要演示如何使用侧边栏组件及页面布局效果。

```ts
// xxx.ets
@Entry
@Component
struct SideBarContainerExample {
  // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
  normalIcon: Resource = $r('app.media.icon');
  selectedIcon: Resource = $r('app.media.icon');
  @State menuItems: number[] = [1, 2, 3];
  @State selectedItemId: number = 1;

  build() {
    SideBarContainer(SideBarContainerType.Embed) {
      Column() {
        ForEach(this.menuItems, (item: number) => {
          Column({ space: 5 }) {
            Image(this.selectedItemId === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
            Text('Index0' + item)
              .fontSize(25)
              .fontColor(this.selectedItemId === item ? '#0A59F7' : '#999')
              .fontFamily('source-sans-pro,cursive,sans-serif')
          }
          .onClick(() => {
            this.selectedItemId = item;
          })
        }, (item: number) => item.toString())
      }.width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .backgroundColor('#19000000')

      Column() {
        Text('SideBarContainer content text1').fontSize(25)
        Text('SideBarContainer content text2').fontSize(25)
      }
      .margin({ top: 50, left: 20, right: 30 })
    }
    .controlButton({
      icons: {
        // $r('app.media.drawer')需要替换为开发者所需的图像资源文件。
        hidden: $r('app.media.drawer'),
        shown: $r('app.media.drawer'),
        switching: $r('app.media.drawer')
      }
    })
    .sideBarWidth(150)
    .minSideBarWidth(50)
    .maxSideBarWidth(300)
    .minContentWidth(0)
    .onChange((value: boolean) => {
      console.info('status:' + value);
    })
    .divider({ strokeWidth: '1vp', color: Color.Gray, startMargin: '4vp', endMargin: '4vp' })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/4W5caoIJT7SClX4oA_RchQ/zh-cn_image_0000002742124907.png)
