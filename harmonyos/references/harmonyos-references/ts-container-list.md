---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list
title: List
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > List
category: harmonyos-references
scraped_at: 2026-04-28T08:01:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de2c74d5ce82c0afdf0fcf277888405745996573ee6e199df57fe0677734c3af
---

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

List的懒加载是指组件按需加载可见区域可见的子组件。相比全量加载，使用懒加载可以提升应用启动速度，减少内存消耗。List和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)结合，懒加载能力存在差异：

* 当List和ForEach结合，会一次性创建所有的子节点，在需要的时候布局和渲染屏幕范围内的节点。当用户滑动时，划出屏幕范围的节点不会下树销毁，划入屏幕范围的节点会布局和渲染。
* 当List和LazyForEach结合，会一次性创建、布局、渲染屏幕范围的节点。当用户滑动时，划出屏幕范围的节点会下树销毁，划入屏幕范围的节点会创建、布局、渲染。
* 当List和带[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)的Repeat结合，它的懒加载行为和LazyForEach一致。当List和不带virtualScroll的Repeat结合，它的懒加载行为和ForEach一致。

如果可滚动组件嵌套List组件，并且滚动方向相同，List组件又没有设置主轴尺寸时，List组件会全量加载子组件，导致懒加载失效。该场景推荐使用List嵌套[ListItemGroup](ts-container-listitemgroup.md)组件以实现优化性能。

List的预加载是指除了加载显示区域内可见的子组件外，还支持空闲时隙提前加载部分显示区域外不可见的子组件。使用预加载可以减少滚动丢帧，提升流畅性。预加载需要结合懒加载才会生效。List支持通过[cachedCount](ts-container-list.md#cachedcount)设置预加载的数量。默认会预加载显示区域上下各一屏子节点（最大预加载16行子节点）。List和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)结合，预加载能力存在差异：

* 当List和ForEach结合，如果设置了cachedCount，除了会布局显示区域内子组件外，还会在空闲时隙预布局显示区域外cachedCount范围内的子节点。
* 当List和LazyForEach结合，如果设置了cachedCount，除了会创建和布局显示区域内子组件外，还会在空闲时隙预创建和预布局显示区域外cachedCount范围内的子节点。
* 当List和带[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)的Repeat结合，它的预加载行为和LazyForEach一致。当List和不带virtualScroll的Repeat结合，它的预加载行为和ForEach一致。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](ts-gesture-blocking-enhancement.md)进行处理。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持[ListItem](ts-container-listitem.md)、[ListItemGroup](ts-container-listitemgroup.md)子组件和自定义组件。自定义组件在List下使用时，建议使用ListItem或ListItemGroup作为自定义组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

说明

如果在处理大量子组件时遇到卡顿问题，请考虑采用懒加载、缓存列表项、动态预加载、组件复用和布局优化等方法来进行优化。最佳实践请参考[优化长列表加载慢丢帧问题](../best-practices/bpta-best-practices-long-list.md)。

从API version 21开始，List单个子组件的宽高最大为16777216px；API version 20及之前，List单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

List的子组件的索引值计算规则：

* 按子组件的顺序依次递增。
* if/else语句中，只有条件成立的分支内的子组件会参与索引值计算，条件不成立的分支内子组件不计算索引值。
* ForEach/LazyForEach/Repeat语句中，会计算展开所有子节点索引值。
* [if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)发生变化以后，会更新子节点索引值。
* ListItemGroup作为一个整体计算一个索引值，ListItemGroup内部的ListItem不计算索引值。
* List子组件visibility属性设置为Hidden或None依然会计算索引值。

## 接口

PhonePC/2in1TabletTVWearable

List(options?: [ListOptions](ts-container-list.md#listoptions18对象说明))

创建List列表容器。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ListOptions](ts-container-list.md#listoptions18对象说明) | 否 | 设置List组件参数。 |

## ListOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于设置List组件参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| initialIndex7+ | number | 否 | 是 | 设置当前List初次加载时显示区域起始位置的item索引值。  默认值：0  **说明：**  设置为负数或超过了当前List最后一个item的索引值时视为无效取值，无效取值按默认值显示。  从API version 14开始，如果在List组件创建完成后首次布局前（如List的[onAttach](ts-universal-events-show-hide.md#onattach12)事件中），调用Scroller滚动控制器中不带动画的scrollToIndex或scrollEdge方法，会覆盖initialIndex设置的值。  设置了initialIndex后，List从initialIndex对应的子组件开始布局，在这之前的子组件未参与布局，无法计算准确大小，因此通过[currentOffset](ts-container-scroll.md#currentoffset)接口获取到的List的滚动总偏移量通过估算得出，可能会有误差。可通过设置[childrenMainSize](ts-container-list.md#childrenmainsize12)确保List的滚动总偏移量的准确性。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| space7+ | number | string | 否 | 是 | 子组件主轴方向的间隔。  默认值：0  参数类型为number时单位为vp。  **说明：**  设置为负数或者大于等于List内容区长度时，按默认值显示。  space参数值小于List分割线宽度时，子组件主轴方向的间隔取分割线宽度。  List子组件的visibility属性设置为None时不显示，但该子组件上下的space还是会生效。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| scroller7+ | [Scroller](ts-container-scroll.md#scroller) | 否 | 是 | 可滚动组件的控制器。与List绑定后，可以通过它控制List的滚动。  **说明：**  不允许和其他滚动类组件，如：[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)绑定同一个滚动控制对象。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)和[滚动组件通用属性](ts-container-scrollable-common.md#属性)外，还支持以下属性：

说明

List组件通用属性[clip](ts-universal-attributes-sharp-clipping.md#clip12)的默认值为true。

### listDirection

PhonePC/2in1TabletTVWearable

listDirection(value: Axis)

设置List组件排列方向。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Axis](ts-appendix-enums.md#axis) | 是 | 组件的排列方向。  默认值：Axis.Vertical |

### divider

PhonePC/2in1TabletTVWearable

divider(value: [ListDividerOptions](ts-container-list.md#listdivideroptions18对象说明) | null)

设置ListItem分割线样式，默认无分割线。

List的分割线画在主轴方向两个子组件之间，第一个子组件上方和最后一个子组件下方不会绘制分割线。

多列模式下，ListItem与ListItem之间的分割线起始边距从每一列的交叉轴方向起始边开始计算，单列模式从List交叉轴方向起始边开始计算。

ListItem设置[多态样式](ts-universal-attributes-polymorphic-style.md)时，被按压的子组件上下的分割线不绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListDividerOptions](ts-container-list.md#listdivideroptions18对象说明) | null | 是 | ListItem分割线样式。  默认值：null |

### scrollBar

PhonePC/2in1TabletTVWearable

scrollBar(value: BarState)

设置滚动条状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](ts-appendix-enums.md#barstate) | 是 | 滚动条状态。  默认值：API version 9及以下版本默认值为BarState.Off，API version 10及以上版本的默认值为BarState.Auto。 |

### cachedCount

PhonePC/2in1TabletTVWearable

cachedCount(value: number)

设置列表中ListItem/ListItemGroup的预加载数量，懒加载场景只会预加载List显示区域外上下各cachedCount行的ListItem，非懒加载场景会全部加载。懒加载、非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。

List下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | ListItem/ListItemGroup的预加载数量。  默认值：根据屏幕内显示的节点个数设置，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。 |

### cachedCount14+

PhonePC/2in1TabletTVWearable

cachedCount(count: number, show: boolean)

设置列表中ListItem/ListItemGroup的预加载数量，并配置是否显示预加载节点。

List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。配合[裁剪](ts-universal-attributes-sharp-clipping.md#clip12)或[内容裁剪](ts-container-scrollable-common.md#clipcontent14)属性可以显示出预加载节点。

说明

通常建议设置cachedCount=n/2（n代表一屏显示的列表项数量），同时需考虑其他因素以实现体验和内存使用的平衡。最佳实践请参考[优化长列表加载慢丢帧问题-缓存列表项](../best-practices/bpta-best-practices-long-list.md#section11667144010222)。

**卡片能力：** 从API version 14开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载的ListItem的数量。  默认值：根据屏幕内显示的节点个数设置，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。 |
| show | boolean | 是 | 被预加载的ListItem是否需要显示。设置为true时显示预加载的ListItem，设置为false时不显示预加载的ListItem。  默认值：false |

### cachedCount22+

PhonePC/2in1TabletTVWearable

cachedCount(count: number | CacheCountInfo, show: boolean)

设置列表中ListItem/ListItemGroup的预加载数量，并配置是否显示预加载节点。

若cachedCount属性的第一个参数为number类型，在帧间空闲时隙会在显示区域外上下各预加载并布局count行ListItem。

若cachedCount属性的第一个参数为CacheCountInfo类型，当已缓存行数小于CacheCountInfo.minCount时，会在帧间空闲时隙预加载和布局。当已缓存行数大于CacheCountInfo.maxCount时，会将超出范围的节点销毁或回收复用。UI空闲时（无动画或用户操作），会在显示区域外上下各预加载CacheCountInfo.maxCount行ListItem。

在计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。配合[clip](ts-universal-attributes-sharp-clipping.md#clip12)或[clipContent](ts-container-scrollable-common.md#clipcontent14)属性可以显示出预加载节点。

默认行为：count参数默认为number类型，数值根据屏幕内显示的节点个数设置，最大值为16。预加载的ListItem默认不参与绘制。

说明

通常建议设置cachedCount=n/2（n代表一屏显示的列表项数量），同时需考虑其他因素以实现体验和内存使用的平衡。从API version 22开始，支持设置最大最小缓存数，可以将最大缓存数设置稍大，如设置为最小缓存数的两倍，利用UI线程空闲时间创建节点，减少滚动过程中预加载创建节点，提升滚动流畅性。最佳实践请参考[优化长列表加载慢丢帧问题-缓存列表项](../best-practices/bpta-best-practices-long-list.md#section11667144010222)。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | [CacheCountInfo](ts-types.md#cachecountinfo22对象说明) | 是 | 当参数类型为number时，表示预加载的ListItem的数量。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。  当参数类型为CacheCountInfo时，表示预加载的最大最小范围。 |
| show | boolean | 是 | 被预加载的ListItem是否需要显示。  true：显示预加载的ListItem。  false：不显示预加载的ListItem。 |

### edgeEffect

PhonePC/2in1TabletTVWearable

edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions)

设置边缘滑动效果。

说明

当List组件的内容区小于一屏时，默认没有回弹效果。若要启用回弹效果，可以通过设置edgeEffect属性的options参数为{ alwaysEnabled: true }来实现。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EdgeEffect](ts-appendix-enums.md#edgeeffect) | 是 | List组件的边缘滑动效果，支持弹簧效果和阴影效果。  默认值：EdgeEffect.Spring |
| options11+ | [EdgeEffectOptions](ts-container-scrollable-common.md#edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。  默认值：{ alwaysEnabled: false } |

### chainAnimation

PhonePC/2in1TabletTVWearable

chainAnimation(value: boolean)

设置当前List是否启用链式联动动效。

说明

* 链式联动效果是指在手指划动过程中，手指拖动的ListItem是主动对象，相邻的ListItem为从动对象，主动对象驱动从动对象联动，驱动效果遵循弹簧物理动效。
* 链式动效的驱动效果体现在ListItem之间的间距上。静止状态下的间距可以通过List组件space参数设置，如果不设置space参数并且启用了链式动效，该间距默认为20vp。
* 链式动效启用后，List的分割线不显示。
* 链式动效生效的前提是List处于单列模式并且边缘效果为EdgeEffect.Spring类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否启用链式联动动效。  默认值：false，不启用链式联动。true，启用链式联动。 |

### multiSelectable8+

PhonePC/2in1TabletTVWearable

multiSelectable(value: boolean)

设置是否开启鼠标框选。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启鼠标框选。  默认值：false，关闭框选。true，开启框选。 |

### lanes9+

PhonePC/2in1TabletTVWearable

lanes(value: number | LengthConstrain, gutter?: Dimension)

设置List组件的布局列数或行数（List垂直滚动时表示列数，水平滚动时表示行数）。

以列数作为示例，介绍设置规则如下：

* value为number类型时，根据number类型数值指定列数。
* value为LengthConstrain类型时，LengthConstrain中的minLength表示最小列宽，List组件会根据自身宽度在满足最小列宽情况下计算最大列数。同时，LengthConstrain会作为最大最小布局宽度约束传递给List的子组件，子组件没有设置宽度时会生效该最大最小布局约束。
* ListItemGroup在多列模式下也是独占一行，ListItemGroup中的ListItem按照List组件的lanes属性设置值来布局。
* value为LengthConstrain类型时，计算ListItemGroup中的列数时会按照ListItemGroup的自身宽度计算。因此ListItemGroup宽度与List宽度不一致时，ListItemGroup中的列数与List中的列数可能不一样。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [LengthConstrain](ts-types.md#lengthconstrain) | 是 | List组件的布局列数或行数。  默认值：1  取值范围：[1, +∞) |
| gutter10+ | [Dimension](ts-types.md#dimension10) | 否 | 列间距或行间距。  默认值：0  取值范围：[0, +∞)  **说明：**  gutter为列间距或行间距，当列数或行数大于1时生效。 |

### lanes22+

PhonePC/2in1TabletTVWearable

lanes(value: number | LengthConstrain | ItemFillPolicy, gutter?: Dimension)

设置List组件布局列的数量和列的间距，默认按固定一列显示。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [LengthConstrain](ts-types.md#lengthconstrain) | [ItemFillPolicy](ts-types.md#itemfillpolicy22) | 是 | 当前List组件布局列的数量。  设置为number类型时，根据number类型的数值确定列数，number类型取值范围：[1, +∞)。  设置为LengthConstrain类型时，根据LengthConstrain中的最大最小值确定列数。  设置为ItemFillPolicy类型时，根据List组件宽度对应[断点类型](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)确定列数，该类型只在List滚动方向为垂直方向时才生效。 |
| gutter | [Dimension](ts-types.md#dimension10) | 否 | 列间距。  默认值：0  取值范围：[0, +∞) |

### alignListItem9+

PhonePC/2in1TabletTVWearable

alignListItem(value: ListItemAlign)

设置List交叉轴方向宽度大于ListItem交叉轴宽度 \* lanes + (lanes - 1) \* gutter时，ListItem在List交叉轴方向的布局方式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListItemAlign](ts-container-list.md#listitemalign9枚举说明) | 是 | 交叉轴方向的布局方式。  默认值：ListItemAlign.Start |

### sticky9+

PhonePC/2in1TabletTVWearable

sticky(value: StickyStyle)

配合[ListItemGroup](ts-container-listitemgroup.md)组件使用，设置ListItemGroup中header是否要吸顶或footer是否要吸底。sticky属性可以设置为 StickyStyle.Header | StickyStyle.Footer 以同时支持header吸顶和footer吸底。从API version 20开始，sticky属性也可以设置为StickyStyle.BOTH，以同时支持header吸顶和footer吸底。

说明

由于浮点数计算精度，设置sticky后，在List滑动过程中小概率产生缝隙，可以通过[pixelRound](ts-universal-attributes-pixelroundforcomponent.md#pixelround)指定当前组件向下像素取整解决该问题。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [StickyStyle](ts-container-list.md#stickystyle9枚举说明) | 是 | ListItemGroup吸顶或吸底效果。  默认值：StickyStyle.None |

### scrollSnapAlign10+

PhonePC/2in1TabletTVWearable

scrollSnapAlign(value: ScrollSnapAlign)

设置列表项滚动结束对齐效果。

只支持item等高场景限位，不等高场景可能存在不准确的情况。对齐动画期间[onWillScroll](ts-container-scrollable-common.md#onwillscroll12)事件上报的滚动操作来源类型为ScrollSource.FLING。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollSnapAlign](ts-container-list.md#scrollsnapalign10枚举说明) | 是 | 列表项滚动结束对齐效果。  默认值：ScrollSnapAlign.NONE |

### scrollSnapAnimationSpeed22+

PhonePC/2in1TabletTVWearable

scrollSnapAnimationSpeed(speed: ScrollSnapAnimationSpeed)

设置列表项滚动限位动画速度。只在列表设置了滚动结束对齐效果后才生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [ScrollSnapAnimationSpeed](ts-container-list.md#scrollsnapanimationspeed22枚举说明) | 是 | 列表滚动限位动画速度。  默认值：ScrollSnapAnimationSpeed.NORMAL |

### enableScrollInteraction10+

PhonePC/2in1TabletTVWearable

enableScrollInteraction(value: boolean)

设置是否支持滚动手势。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持滚动手势。设置为true时可以通过手指或者鼠标滚动，设置为false时无法通过手指或者鼠标滚动，但不影响控制器[Scroller](ts-container-scroll.md#scroller)的滚动接口。  默认值：true |

说明

组件无法通过鼠标按下拖动操作进行滚动。

### nestedScroll10+

PhonePC/2in1TabletTVWearable

nestedScroll(value: NestedScrollOptions)

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。  默认值：{ scrollForward: NestedScrollMode.SELF\_ONLY, scrollBackward: NestedScrollMode.SELF\_ONLY } |

### friction10+

PhonePC/2in1TabletTVWearable

friction(value: number | Resource)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程。设置为小于等于0的值时，按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 摩擦系数。  默认值：非wearable设备为0.6，wearable设备为0.9。  从API version 11开始，非wearable设备默认值为0.7。  从API version 12开始，非wearable设备默认值为0.75。 |

### contentStartOffset11+

PhonePC/2in1TabletTVWearable

contentStartOffset(value: number)

设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区域起始偏移量。  默认值：0  单位：vp  **说明：**  设置为负数时，按默认值处理。 |

### contentStartOffset22+

PhonePC/2in1TabletTVWearable

contentStartOffset(offset: number | Resource)

设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。与[contentStartOffset11+](ts-container-list.md#contentstartoffset11)相比，参数名改为offset，并开始支持Resource类型。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](ts-types.md#resource) | 是 | 内容区域起始偏移量。  默认值：0  参数类型为number时单位为vp。  设置异常值如负数、非数字Resource时，按默认值处理。 |

### contentEndOffset11+

PhonePC/2in1TabletTVWearable

contentEndOffset(value: number)

设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内容区末尾偏移量。  默认值：0  单位：vp  **说明：**  设置为负数时，按默认值处理。 |

### contentEndOffset22+

PhonePC/2in1TabletTVWearable

contentEndOffset(offset: number | Resource)

设置内容区末尾偏移量。列表滚动到末尾位置时，列表内容与列表显示区域边界保留指定距离。与[contentEndOffset11+](ts-container-list.md#contentendoffset11)相比，参数名改为offset，并开始支持Resource类型。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | [Resource](ts-types.md#resource) | 是 | 内容区末尾偏移量。  默认值：0  参数类型为number时单位为vp。  设置异常值如负数、非数字Resource时，按默认值处理。 |

### childrenMainSize12+

PhonePC/2in1TabletTVWearable

childrenMainSize(value: ChildrenMainSize)

设置List组件的子组件在主轴方向的大小信息。

说明

* 该属性通过向List组件提供所有子组件在主轴方向的大小信息，确保在面对子组件主轴大小不一致、增删子组件、使用[scrollToIndex](ts-container-scroll.md#scrolltoindex)等场景时，List组件能够维护其滑动位置准确性。这样，[scrollTo](ts-container-scroll.md#scrollto)可以准确的跳转到指定位置，[currentOffset](ts-container-scroll.md#currentoffset)可以获取到当前准确的滑动位置，内置滚动条可以实现平滑移动无跳变。
* 当子组件是ListItemGroup时，需要根据ListItemGroup的列数、ListItemGroup中ListItem在主轴方向的间距以及ListItemGroup中header、footer和ListItem的大小，来准确计算出ListItemGroup在主轴方向的整体大小，并传递给List组件。
* 如果子组件有ListItemGroup，必须为每一个ListItemGroup设置[childrenMainSize](ts-container-listitemgroup.md#childrenmainsize12)属性。List组件和每一个ListItemGroup组件都要通过childrenMainSize属性接口一对一绑定一个ChildrenMainSize对象。
* 多列场景使用LazyForEach生成子组件时，需确保LazyForEach全部生成ListItemGroup组件或者全部生成ListItem组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ChildrenMainSize](ts-container-scrollable-common.md#childrenmainsize12对象说明) | 是 | 该对象用来维护子组件在主轴方向的大小信息。 |

### maintainVisibleContentPosition12+

PhonePC/2in1TabletTVWearable

maintainVisibleContentPosition(enabled: boolean)

设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置显示区域上方插入或删除数据时是否要保持可见内容位置不变。  默认值：false，显示区域上方插入或删除数据时可见内容位置会跟随变化。 true：显示区域上方插入或删除数据时可见内容位置不变。 |

说明

* 只有使用LazyForEach在显示区域外插入或删除数据时，属性设置为true才能保持可见内容位置不变。使用ForEach插入或删除数据、使用LazyForEach重新加载数据时，即使maintainVisibleContentPosition属性设置为true，可见区内容位置也会跟随变化。
* 从API version 20开始，使用[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)在懒加载场景下，显示区域外插入或删除数据时，属性设置为true也能保持可见内容位置不变。
* maintainVisibleContentPosition属性设置为true后，在显示区域上方插入或删除数据，会触发[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)、onScrollIndex事件。
* maintainVisibleContentPosition属性设置为true后，在多列场景下，一次插入或删除整行数据，可以保持可见内容位置不变，如果不是插入或删除整行数据，可见内容位置还是会发生变化。

### stackFromEnd19+

PhonePC/2in1TabletTVWearable

stackFromEnd(enabled: boolean)

设置List组件是否从末尾开始布局。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置List组件是否从末尾开始布局。  默认值：false，List从顶部开始布局。 true：List组件从末尾开始布局。 |

说明

* stackFromEnd属性设置为true后，当List内容小于List组件高度时，内容底部对齐。
* stackFromEnd属性设置为true后，显示区域内有ListItem变高，或有插入ListItem，内容上方的ListItem往上移动。
* stackFromEnd属性设置为true后，[ListOptions](ts-container-list.md#listoptions18对象说明)中initialIndex参数默认值为总item个数-1。

### focusWrapMode20+

PhonePC/2in1TabletTVWearable

focusWrapMode(mode: Optional<FocusWrapMode>)

设置方向键走焦模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[FocusWrapMode](ts-appendix-enums.md#focuswrapmode20)> | 是 | 交叉轴方向键走焦模式。  默认值：FocusWrapMode.DEFAULT  **说明：**  异常值按默认值处理，即交叉轴方向键不能换行。 |

### syncLoad20+

PhonePC/2in1TabletTVWearable

syncLoad(enable: boolean)

设置是否同步加载List区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否同步加载List区域内所有子组件。  true表示同步加载，false表示异步加载。默认值：true。  **说明：**  设置为false时，在首次显示、不带动画scrollToIndex跳转场景，若当帧布局耗时超过50ms，会将List区域内尚未布局的子组件延后到下一帧进行布局。 |

### editModeOptions23+

PhonePC/2in1TabletTVWearable

editModeOptions(options?: EditModeOptions)

配置编辑模式选项参数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EditModeOptions](ts-container-scrollable-common.md#editmodeoptions23对象说明) | 否 | 编辑模式选项。 |

### editMode(deprecated)

PhonePC/2in1TabletTVWearable

editMode(value: boolean)

设置当前List组件是否处于可编辑模式。可参考[示例3](ts-container-list.md#示例3设置编辑模式)实现删除选中的list项。

说明

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当前List组件是否处于可编辑模式。  默认值：false，当前List组件不处于可编辑模式。 |

### supportEmptyBranchInLazyLoading23+

PhonePC/2in1TabletTVWearable

supportEmptyBranchInLazyLoading(supported: boolean | undefined)

设置当前List组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持空分支行为之间切换。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | undefined | 是 | 当前List组件是否支持在[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)或[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)中使用[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)渲染控制语法生成一个不含任何子节点的空分支节点。  true表示支持空分支节点；false表示不支持空分支节点。  值为undefined时，按false处理。 |

## ListItemAlign9+枚举说明

PhonePC/2in1TabletTVWearable

设置子组件在List交叉轴方向的对齐方式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Start | 0 | ListItem在List中，交叉轴方向首部对齐。 |
| Center | 1 | ListItem在List中，交叉轴方向居中对齐。 |
| End | 2 | ListItem在List中，交叉轴方向尾部对齐。 |

## StickyStyle9+枚举说明

PhonePC/2in1TabletTVWearable

ListItemGroup吸顶或吸底效果枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | ListItemGroup的header不吸顶，footer不吸底。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Header | 1 | ListItemGroup的header吸顶，footer不吸底。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Footer | 2 | ListItemGroup的footer吸底，header不吸顶。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BOTH20+ | 3 | ListItemGroup的header吸顶，footer吸底。  **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ScrollSnapAlign10+枚举说明

PhonePC/2in1TabletTVWearable

设置列表项滚动结束对齐效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 默认无项目滚动对齐效果。 |
| START | 1 | 视图中的第一项将在列表的开头对齐。  **说明：**  当列表位移至末端，需要将末端的item完整显示，可能出现开头不对齐的情况。 |
| CENTER | 2 | 视图中的中间项将在列表中心对齐。  **说明：**  顶端和末尾的item都可以在列表中心对齐，列表显示可能露出空白。 |
| END | 3 | 视图中的最后一项将在列表末尾对齐。  **说明：**  当列表位移至顶端，需要将顶端的item完整显示，可能出现末尾不对齐的情况。 |

## ScrollSnapAnimationSpeed22+枚举说明

PhonePC/2in1TabletTVWearable

设置列表项滚动限位动画速度。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 默认列表限位动画速度，通常用于列表项尺寸较大，划一下滚动一个列表项场景。 |
| SLOW | 1 | 列表限位动画速度较慢，通常用于列表项尺寸较小，划一下滚动多个列表项场景。 |

## CloseSwipeActionOptions11+对象说明

PhonePC/2in1TabletTVWearable

收起[EXPANDED](ts-container-listitem.md#swipeactionstate11枚举说明)状态[ListItem](ts-container-listitem.md)回调事件集合，用于设置收起动画完成后回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onFinish | ()=>void | 否 | 是 | 在收起动画完成后触发。 |

## ListDividerOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于设置List或ListItemGroup组件的分割线样式。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth7+ | [Length](ts-types.md#length) | 否 | 否 | 分割线的线宽。  单位：vp  **说明：**  设置为负数，百分比，或者大于等于List内容区长度时，按0处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| color7+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线颜色。  默认值：0x08000000  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| startMargin7+ | [Length](ts-types.md#length) | 否 | 是 | 分割线与列表侧边起始端的距离。  默认值：0  单位：vp  **说明：**  设置为负数或者百分比时，按默认值处理。  endMargin + startMargin 超过列宽度后startMargin和endMargin均会被置0。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| endMargin7+ | [Length](ts-types.md#length) | 否 | 是 | 分割线与列表侧边结束端的距离。  默认值：0  单位：vp  **说明：**  设置为负数或者百分比时，按默认值处理。  endMargin + startMargin 超过列宽度后startMargin和endMargin均会被置0。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)和[滚动组件通用事件](ts-container-scrollable-common.md#事件)外，还支持以下事件：

### onScrollIndex

PhonePC/2in1TabletTVWearable

onScrollIndex(event: (start: number, end: number, center: number) => void)

有子组件划入或划出List显示区域时触发。计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

List的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollIndex事件。

触发该事件的条件：列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

从API version 10开始，List显示区域中间位置子组件变化时也会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | List显示区域内第一个子组件的索引值 |
| end | number | 是 | List显示区域内最后一个子组件的索引值。 |
| center10+ | number | 是 | List显示区域内中间位置子组件的索引值。 |

### onReachStart

PhonePC/2in1TabletTVWearable

onReachStart(event: () => void)

列表到达起始位置时触发。

List初始化时如果initialIndex为0会触发一次，List滚动到起始位置时触发一次。List边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表到达起始位置时触发的回调。 |

### onReachEnd

PhonePC/2in1TabletTVWearable

onReachEnd(event: () => void)

列表到达末尾位置时触发事件。当最后一个子组件因滚动或内容/布局变化出现在列表视窗中时，触发此回调。

当子组件未撑满列表，无须滚动即可直接在列表内完整展示时，首次加载也会触发此事件。

List边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表到达末尾位置时触发的回调。 |

### onScrollFrameBegin9+

PhonePC/2in1TabletTVWearable

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，列表将按照返回值的实际滑动量进行滑动。

当listDirection的值为Axis.Vertical时，返回垂直方向滑动量，当listDirection的值为Axis.Horizontal时，返回水平方向滑动量。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. List惯性滚动。
3. 调用[fling](ts-container-scroll.md#fling12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](ts-container-scroll.md#fling12)接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](ts-container-scroll.md#onscrollframebegincallback18) | 是 | 每帧滚动开始回调函数。 |

### onScrollStart9+

PhonePC/2in1TabletTVWearable

onScrollStart(event: () => void)

列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表滑动开始时触发的回调。 |

### onScrollStop

PhonePC/2in1TabletTVWearable

onScrollStop(event: () => void)

列表滑动停止时触发。手拖动列表或列表的滚动条触发的滑动，手离开屏幕后滑动停止时会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 列表滑动停止时触发的回调。 |

### onItemMove

PhonePC/2in1TabletTVWearable

onItemMove(event: (from: number, to: number) => boolean)

列表元素发生移动时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 | 移动前索引值。 |
| to | number | 是 | 移动后索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经移动。返回值为true时列表元素发生移动，返回值为false时列表元素没有移动。 |

### onItemDragStart8+

PhonePC/2in1TabletTVWearable

onItemDragStart(event: OnItemDragStartCallback)

开始拖拽列表元素时触发。

不支持拖动到List边缘时触发List的自动滚动，可以使用ForEach、LazyForEach、Repeat的[onMove](ts-universal-attributes-drag-sorting.md#onmove)接口实现该效果，参考[示例12（使用OnMove进行拖拽）](ts-container-list.md#示例12使用onmove进行拖拽)。但需注意[onMove](ts-universal-attributes-drag-sorting.md#onmove)接口不支持跨ListItemGroup拖拽。

说明

从API version 14开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnItemDragStartCallback](ts-container-scrollable-common.md#onitemdragstartcallback23) | 是 | 列表元素拖拽开始时触发的回调。  API version 22及之前版本，该参数类型为(event: ItemDragInfo, itemIndex: number) => (() => any) | void，其中event和itemIndex参数含义参考[OnItemDragStartCallback](ts-container-scrollable-common.md#onitemdragstartcallback23)。 |

### onItemDragEnter8+

PhonePC/2in1TabletTVWearable

onItemDragEnter(event: (event: ItemDragInfo) => void)

拖拽列表元素进入列表范围内时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |

### onItemDragMove8+

PhonePC/2in1TabletTVWearable

onItemDragMove(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number) => void)

拖拽列表元素在列表范围内移动时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |

### onItemDragLeave8+

PhonePC/2in1TabletTVWearable

onItemDragLeave(event: (event: ItemDragInfo, itemIndex: number) => void)

拖拽列表元素离开列表范围时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽离开的列表元素索引值。 |

### onItemDrop8+

PhonePC/2in1TabletTVWearable

onItemDrop(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => void)

绑定该事件的列表可作为拖拽释放目标，当在列表范围内停止拖拽时触发。

跨List拖拽时，当拖拽释放的位置绑定了onItemDrop时isSuccess为true，否则为false。List内部拖拽时，isSuccess为onItemMove事件的返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |
| isSuccess | boolean | 是 | 是否成功释放。返回值为true时列表元素成功释放，返回值为false时列表元素没有成功释放。 |

### onScrollVisibleContentChange12+

PhonePC/2in1TabletTVWearable

onScrollVisibleContentChange(handler: OnScrollVisibleContentChangeCallback)

有子组件划入或划出List显示区域时触发。计算触发条件时，每一个ListItem、ListItemGroup中的header或footer都算一个子组件。

List的边缘效果为弹簧效果时，在List划动到边缘继续划动和松手回弹过程不会触发onScrollVisibleContentChange事件。

触发该事件的条件：列表初始化时会触发一次，List显示区域内第一个子组件的索引值或最后一个子组件的索引值有变化时会触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [OnScrollVisibleContentChangeCallback](ts-container-list.md#onscrollvisiblecontentchangecallback12) | 是 | 当前显示内容发生改变的时候触发回调。 |

### onItemDelete(deprecated)

PhonePC/2in1TabletTVWearable

onItemDelete(event: (index: number) => boolean)

当List组件在编辑模式时，点击ListItem右边出现的删除按钮时触发。

说明

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 被删除的列表项的索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否已经删除。 |

### onScroll(deprecated)

PhonePC/2in1TabletTVWearable

onScroll(event: (scrollOffset: number, scrollState: [ScrollState](ts-container-list.md#scrollstate枚举说明)) => void)

列表滑动时触发。

说明

从API version 7开始支持，从API version 12开始废弃，建议使用[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，List的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滑动状态。 |

## ScrollState枚举说明

PhonePC/2in1TabletTVWearable

滑动状态枚举。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Idle | 0 | 空闲状态。滚动状态回归空闲时触发，控制器提供的无动画方法控制滚动时触发。 |
| Scroll | 1 | 滚动状态。手指拖动List，拖动滚动条和滚动鼠标滚轮时触发。 |
| Fling | 2 | 惯性滚动状态。动画控制的滚动都会触发。包括快速划动松手后的惯性滚动，  划动到边缘回弹的滚动，快速拖动内置滚动条松手后的惯性滚动，  使用滚动控制器提供的带动画的方法控制的滚动。 |

## ListScroller11+

PhonePC/2in1TabletTVWearable

List组件的滚动控制器，通过它控制List组件的滚动，仅支持一对一绑定到List组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

ListScroller继承自[Scroller](ts-container-scroll.md#scroller)，具有[Scroller](ts-container-scroll.md#scroller)的全部方法。

### 导入对象

```
1. listScroller: ListScroller = new ListScroller();
```

### getItemRectInGroup11+

PhonePC/2in1TabletTVWearable

getItemRectInGroup(index: number, indexInGroup: number): RectResult

获取[ListItemGroup](ts-container-listitemgroup.md)中的[ListItem](ts-container-listitem.md)的大小和相对于List的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | ListItemGroup在List中的索引值。 |
| indexInGroup | number | 是 | ListItem在ListItemGroup中的索引值。 |

说明

* index必须是当前显示区域显示的子组件的索引值，否则视index为非法值。
* 索引值为index的子组件必须是ListItemGroup，否则视index为非法值。
* indexInGroup必须是当前显示区域内ListItemGroup中显示的ListItem的索引值，否则视indexInGroup为非法值。
* index或者indexInGroup为非法值时返回的大小和位置均为0。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectResult](ts-universal-attributes-on-child-touch-test.md#rectresult) | ListItemGroup中的ListItem的大小和相对于List的位置。  单位：vp。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### getVisibleListContentInfo14+

PhonePC/2in1TabletTVWearable

getVisibleListContentInfo(x: number, y: number): VisibleListContentInfo

根据坐标获取子组件的索引信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | x轴坐标，单位为vp。 |
| y | number | 是 | y轴坐标，单位为vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisibleListContentInfo](ts-container-list.md#visiblelistcontentinfo12对象说明) | 入参坐标处的子组件的索引信息。 |

说明

* 入参坐标(x, y)的基准点是List组件的位置。
* 如果该坐标位置处于ListItem范围内，且该ListItem父组件是List，则返回值对象成员index为该ListItem在List中的索引值，itemGroupArea返回undefined，itemIndexInGroup返回undefined。
* 如果该坐标位置处于ListItem范围内，且该ListItem父组件是ListItemGroup，则返回值对象成员index为该ListItemGroup在List中的索引值，itemGroupArea返回ListItemGroupArea.IN\_LIST\_ITEM\_AREA，itemIndexInGroup返回该ListItem在ListItemGroup中的索引值。
* 如果该坐标位置不处于ListItem范围内，但是处于ListItemGroup的header或者footer范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回undefined。如果坐标位置处于header范围，itemGroupArea返回ListItemGroupArea.IN\_HEADER\_AREA。如果坐标位置处于footer范围，itemGroupArea返回ListItemGroupArea.IN\_FOOTER\_AREA。
* 如果该坐标位置既不处于ListItem范围内，也不处于ListItemGroup的header或者footer范围内，但是处于ListItemGroup的范围内，则返回值对象成员index为该ListItemGroup在List中的索引值，itemIndexInGroup返回undefined，itemGroupArea返回ListItemGroupArea.NONE。
* 如果该坐标位置既不处于ListItem范围内，也不处于ListItemGroup的范围内，则返回值对象成员index为-1，itemIndexInGroup返回undefined，itemGroupArea返回undefined。

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### scrollToItemInGroup11+

PhonePC/2in1TabletTVWearable

scrollToItemInGroup(index: number, indexInGroup: number, smooth?: boolean, align?: ScrollAlign): void

滑动到指定的ListItemGroup中指定的ListItem。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 要滑动到的目标元素所在的ListItemGroup在当前容器中的索引值。  **说明：**  index值设置成负值或者大于当前容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| indexInGroup | number | 是 | 要滑动到的目标元素在index指定的ListItemGroup中的索引值。  **说明：**  indexInGroup值设置成负值或者大于index指定的ListItemGroup容器子组件的最大索引值，视为异常值，本次跳转不生效。 |
| smooth | boolean | 否 | 设置该次滑动是否有动效，true表示有动效，false表示没有动效。  默认值：false  **说明：**  开启动效时，会对经过的所有item进行加载和布局计算，当大量加载item时会导致性能问题。 |
| align | [ScrollAlign](ts-container-scroll.md#scrollalign10枚举说明) | 否 | 指定滑动到的元素与当前容器的对齐方式。  默认值：ScrollAlign.START。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

### closeAllSwipeActions11+

PhonePC/2in1TabletTVWearable

closeAllSwipeActions(options?: CloseSwipeActionOptions): void

将[EXPANDED](ts-container-listitem.md#swipeactionstate11枚举说明)状态的[ListItem](ts-container-listitem.md)收起，并设置回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CloseSwipeActionOptions](ts-container-list.md#closeswipeactionoptions11对象说明) | 否 | 收起[EXPANDED](ts-container-listitem.md#swipeactionstate11枚举说明)状态的[ListItem](ts-container-listitem.md)的回调事件集合。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[滚动类组件错误码](errorcode-scroll.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100004 | Controller not bound to a component. |

说明

* ListScroller必须绑定到List组件上。

## OnScrollVisibleContentChangeCallback12+

PhonePC/2in1TabletTVWearable

type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void

有子组件划入或划出List显示区域时触发。

List从有子组件变成空的List时，上报的start和end参数会保留上次有子组件时的值。

start和end的index同时返回0，代表List内只有一个子组件。

说明

从API version 14开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | [VisibleListContentInfo](ts-container-list.md#visiblelistcontentinfo12对象说明) | 是 | 1. 通过该参数获取List显示区域第一个子组件在List中的索引值。  2. 如果当前List显示区域第一个子组件是ListItemGroup，可以获取当前List显示区域第一个组件属于该ListItemGroup的哪一区域。  3. 如果当前List显示区域第一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。 |
| end | [VisibleListContentInfo](ts-container-list.md#visiblelistcontentinfo12对象说明) | 是 | 1. 通过该参数获取List显示区域最后一个子组件在List中的索引值。  2. 如果当前List显示区域最后一个子组件是ListItemGroup，可以获取当前List显示区域最后一个组件属于该ListItemGroup的哪一区域。  3. 如果当前List显示区域最后一个组件是ListItemGroup内的ListItem，可以获取该ListItem在ListItemGroup内的索引值。 |

## VisibleListContentInfo12+对象说明

PhonePC/2in1TabletTVWearable

用于表示List可见内容区子组件的详细信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 表示ListItem或ListItemGroup在List中的索引值。 |
| itemGroupArea | [ListItemGroupArea](ts-container-list.md#listitemgrouparea12枚举说明) | 否 | 是 | 表示处于ListItemGroup的哪一个区域。 |
| itemIndexInGroup | number | 否 | 是 | 表示ListItem在ListItemGroup中的索引值。 |

## ListItemGroupArea12+枚举说明

PhonePC/2in1TabletTVWearable

枚举了ListItemGroup各个区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | ListItemGroup内部ListItem区域、header区域以及footer区域以外的区域。 |
| IN\_LIST\_ITEM\_AREA | 1 | ListItemGroup内部ListItem区域。 |
| IN\_HEADER\_AREA | 2 | ListItemGroup内部header区域。 |
| IN\_FOOTER\_AREA | 3 | ListItemGroup内部footer区域。 |

## UIListEvent19+

PhonePC/2in1TabletTVWearable

frameNode中[getEvent('List')](js-apis-arkui-framenode.md#geteventlist19)方法的返回值，可用于给List节点设置滚动事件。

UIListEvent继承于[UIScrollableCommonEvent](ts-container-scrollable-common.md#uiscrollablecommonevent19)。

### setOnWillScroll19+

PhonePC/2in1TabletTVWearable

setOnWillScroll(callback: OnWillScrollCallback | undefined): void

设置[onWillScroll](ts-container-scrollable-common.md#onwillscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnWillScrollCallback](ts-container-scrollable-common.md#onwillscrollcallback12) | undefined | 是 | onWillScroll事件的回调函数。 |

### setOnDidScroll19+

PhonePC/2in1TabletTVWearable

setOnDidScroll(callback: OnScrollCallback | undefined): void

设置[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnScrollCallback](ts-container-scrollable-common.md#onscrollcallback12) | undefined | 是 | onDidScroll事件的回调函数。 |

### setOnScrollIndex19+

PhonePC/2in1TabletTVWearable

setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void

设置[onScrollIndex](ts-container-list.md#onscrollindex)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnListScrollIndexCallback](ts-container-list.md#onlistscrollindexcallback19) | undefined | 是 | onScrollIndex事件的回调函数。 |

### setOnScrollVisibleContentChange19+

PhonePC/2in1TabletTVWearable

setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void

设置[onScrollVisibleContentChange](ts-container-list.md#onscrollvisiblecontentchange12)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnScrollVisibleContentChangeCallback](ts-container-list.md#onscrollvisiblecontentchangecallback12) | undefined | 是 | onScrollVisibleContentChange事件的回调函数。 |

## OnListScrollIndexCallback19+

PhonePC/2in1TabletTVWearable

type OnListScrollIndexCallback = (start: number, end: number, center: number) => void

List组件可见区域item变化事件的回调类型。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | List显示区域内第一个子组件的索引值。 |
| end | number | 是 | List显示区域内最后一个子组件的索引值。 |
| center | number | 是 | List显示区域内中间位置子组件的索引值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（添加滚动事件）

该示例实现了设置纵向列表，并在当前显示界面发生改变时回调索引。

ListDataSource实现了LazyForEach数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给List提供子组件。

```
1. // ListDataSource.ets
2. export class ListDataSource implements IDataSource {
3. private list: number[] = [];
4. private listeners: DataChangeListener[] = [];

6. constructor(list: number[]) {
7. this.list = list;
8. }

10. totalCount(): number {
11. return this.list.length;
12. }

14. getData(index: number): number {
15. return this.list[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. this.listeners.push(listener);
21. }
22. }

24. unregisterDataChangeListener(listener: DataChangeListener): void {
25. const pos = this.listeners.indexOf(listener);
26. if (pos >= 0) {
27. this.listeners.splice(pos, 1);
28. }
29. }

31. // 通知LazyForEach组件需要重载所有子组件
32. notifyDataReload(): void {
33. this.listeners.forEach(listener => {
34. listener.onDataReloaded();
35. });
36. }

38. // 通知控制器数据删除
39. notifyDataDelete(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataDelete(index);
42. });
43. }

45. // 通知控制器添加数据
46. notifyDataAdd(index: number): void {
47. this.listeners.forEach(listener => {
48. listener.onDataAdd(index);
49. });
50. }

52. // 在指定索引位置删除一个元素
53. public deleteItem(index: number): void {
54. this.list.splice(index, 1);
55. this.notifyDataDelete(index);
56. }

58. // 在指定索引位置插入一个元素
59. public insertItem(index: number, data: number): void {
60. this.list.splice(index, 0, data);
61. this.notifyDataAdd(index);
62. }

64. public reloadData(): void {
65. this.notifyDataReload();
66. }
67. }
```

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

9. build() {
10. Column() {
11. List({ space: 20, initialIndex: 0 }) {
12. LazyForEach(this.arr, (item: number) => {
13. ListItem() {
14. Text('' + item)
15. .width('100%').height(100).fontSize(16)
16. .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
17. }
18. }, (item: number) => item.toString())
19. }
20. .listDirection(Axis.Vertical) // 排列方向
21. .scrollBar(BarState.Off)
22. .friction(0.6)
23. .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 }) // 每行之间的分界线
24. .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
25. .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
26. console.info('first' + firstIndex);
27. console.info('last' + lastIndex);
28. console.info('center' + centerIndex);
29. })
30. .onScrollVisibleContentChange((start: VisibleListContentInfo, end: VisibleListContentInfo) => {
31. console.info(' start index: ' + start.index +
32. ' start item group area: ' + start.itemGroupArea +
33. ' start index in group: ' + start.itemIndexInGroup);
34. console.info(' end index: ' + end.index +
35. ' end item group area: ' + end.itemGroupArea +
36. ' end index in group: ' + end.itemIndexInGroup);
37. })
38. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
39. console.info(`onScroll scrollState = ScrollState` + scrollState + `, scrollOffset = ` + scrollOffset);
40. })
41. .width('90%')
42. }
43. .width('100%')
44. .height('100%')
45. .backgroundColor(0xDCDCDC)
46. .padding({ top: 5 })
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Bj1qx4BrTlq34DjfqJCq1w/zh-cn_image_0000002583479605.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=32DC6E6883983C0516040458EE23278104AAF7633C4A7DA3A21CDAB56DA084B9)

### 示例2（设置子元素对齐）

该示例展示了不同ListItemAlign枚举值下，List组件交叉轴方向子元素对齐效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListLanesExample {
7. arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]);
8. @State alignListItem: ListItemAlign = ListItemAlign.Start;

10. build() {
11. Column() {
12. List({ space: 20, initialIndex: 0 }) {
13. LazyForEach(this.arr, (item: string) => {
14. ListItem() {
15. Text('' + item)
16. .width('100%')
17. .height(100)
18. .fontSize(16)
19. .textAlign(TextAlign.Center)
20. .borderRadius(10)
21. .backgroundColor(0xFFFFFF)
22. }
23. .border({ width: 2, color: Color.Green })
24. }, (item: string) => item)
25. }
26. .height(300)
27. .width('90%')
28. .friction(0.6)
29. .border({ width: 3, color: Color.Red })
30. .lanes({ minLength: 40, maxLength: 40 })
31. .alignListItem(this.alignListItem)
32. .scrollBar(BarState.Off)

34. Button('点击更改alignListItem:' + this.alignListItem).onClick(() => {
35. if (this.alignListItem == ListItemAlign.Start) {
36. this.alignListItem = ListItemAlign.Center;
37. } else if (this.alignListItem == ListItemAlign.Center) {
38. this.alignListItem = ListItemAlign.End;
39. } else {
40. this.alignListItem = ListItemAlign.Start;
41. }
42. })
43. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/GZ9JHGb8RWGJJ-bWgtz3bw/zh-cn_image_0000002552799956.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=537F01C9AFA5A96B2461CB38DD27A8A0334FA2ACC0F0FCE6D3A5A3E5D633AA1E)

### 示例3（设置编辑模式）

该示例展示了如何设置当前List组件是否处于可编辑模式。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
8. @State editFlag: boolean = false;

10. build() {
11. Stack({ alignContent: Alignment.TopStart }) {
12. Column() {
13. List({ space: 20, initialIndex: 0 }) {
14. LazyForEach(this.arr, (item: number, index?: number) => {
15. ListItem() {
16. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
17. Text('' + item)
18. .width('100%')
19. .height(80)
20. .fontSize(20)
21. .textAlign(TextAlign.Center)
22. .borderRadius(10)
23. .backgroundColor(0xFFFFFF)
24. .flexShrink(1)
25. if (this.editFlag) {
26. Button() {
27. Text('delete').fontSize(16)
28. }.width('30%').height(40)
29. .onClick(() => {
30. if (index != undefined) {
31. console.info(this.arr.getData(index) + 'Delete');
32. this.arr.deleteItem(index);
33. this.arr.reloadData();
34. console.info(JSON.stringify(this.arr));
35. this.editFlag = false;
36. }
37. }).stateEffect(true)
38. }
39. }
40. }
41. }, (item: number, index: number) => item.toString() + index.toString())
42. }.width('90%')
43. .scrollBar(BarState.Off)
44. .friction(0.6)
45. }.width('100%')

47. Button('edit list')
48. .onClick(() => {
49. this.editFlag = !this.editFlag;
50. }).margin({ top: 5, left: 20 })
51. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/-wZrdSPeS3OMbXLJAWrX3Q/zh-cn_image_0000002583439651.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=AD691E868DF92CF01DFD6C11B90B5A1E12BB5418486AD6E74C75A9A2D7E10F33)

### 示例4（设置限位对齐）

该示例展示了List组件设置居中限位的实现效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource=new ListDataSource([]);
8. private scrollerForList: Scroller = new Scroller();

10. aboutToAppear() {
11. let list: number[] = [];
12. for (let i = 0; i < 20; i++) {
13. list.push(i);
14. }
15. this.arr = new ListDataSource(list);
16. }

18. build() {
19. Column() {
20. Row() {
21. List({ space: 20, initialIndex: 3, scroller: this.scrollerForList }) {
22. LazyForEach(this.arr, (item: number) => {
23. ListItem() {
24. Text('' + item)
25. .width('100%').height(100).fontSize(16)
26. .textAlign(TextAlign.Center)
27. }
28. .borderRadius(10).backgroundColor(0xFFFFFF)
29. .width('60%')
30. .height('80%')
31. }, (item: number) => JSON.stringify(item))
32. }
33. .chainAnimation(true)
34. .edgeEffect(EdgeEffect.Spring)
35. .listDirection(Axis.Horizontal)
36. .height('100%')
37. .width('100%')
38. .scrollSnapAlign(ScrollSnapAlign.CENTER)
39. .borderRadius(10)
40. .backgroundColor(0xDCDCDC)
41. }
42. .width('100%')
43. .height('100%')
44. .backgroundColor(0xDCDCDC)
45. .padding({ top: 10 })
46. }
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/DkUMoBWgQLmgIxlyZJ-PqA/zh-cn_image_0000002552959606.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=06AE07B97D38DF517B741E62C51F238F107AD9BF2F1E58CD4FF1A8BAFC21F272)

### 示例5（跳转准确）

该示例通过设置[childrenMainSize](ts-container-list.md#childrenmainsize12)属性，实现了List在子组件高度不一致时调用scrollTo接口也可以跳转准确。

如果配合状态管理V2使用，详情见：[List与makeObserved](../harmonyos-guides/arkts-v1-v2-migration-inner-object.md#滚动组件)。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([]);
8. private scroller: ListScroller = new ListScroller();
9. @State listSpace: number = 10;
10. @State listChildrenSize: ChildrenMainSize = new ChildrenMainSize(100);
11. aboutToAppear(){
12. // 初始化数据源。
13. let list: number[] = [];
14. for (let i = 0; i < 10; i++) {
15. list.push(i);
16. }
17. this.arr = new ListDataSource(list);
18. // 前5个item的主轴大小不是默认大小100，因此需要通过ChildrenMainSize通知List。
19. this.listChildrenSize.splice(0, 5, [300, 300, 300, 300, 300]);
20. }

22. build() {
23. Column() {
24. List({ space: this.listSpace, initialIndex: 4, scroller: this.scroller }) {
25. LazyForEach(this.arr, (item: number) => {
26. ListItem() {
27. Text('item-' + item)
28. .height( item < 5 ? 300 : this.listChildrenSize.childDefaultSize)
29. .width('90%')
30. .fontSize(16)
31. .textAlign(TextAlign.Center)
32. .borderRadius(10)
33. .backgroundColor(0xFFFFFF)
34. }
35. }, (item: string) => item)
36. }
37. .backgroundColor(Color.Gray)
38. .layoutWeight(1)
39. .scrollBar(BarState.On)
40. .childrenMainSize(this.listChildrenSize)
41. .alignListItem(ListItemAlign.Center)
42. Row({ space: 18 }) {
43. Button() { Text('item size + 50') }.onClick(()=>{
44. this.listChildrenSize.childDefaultSize += 50;
45. }).height('50%').width('30%').backgroundColor(0xADD8E6)
46. Button() { Text('item size - 50') }.onClick(()=>{
47. if (this.listChildrenSize.childDefaultSize === 0) {
48. return;
49. }
50. this.listChildrenSize.childDefaultSize -= 50;
51. }).height('50%').width('30%').backgroundColor(0xADD8E6)
52. Button() { Text('scrollTo (0, 310)') }.onClick(()=>{
53. // 310: 跳转到item 1顶部与List顶部平齐的位置。
54. // 如果不设置childrenMainSize，item高度不一致时scrollTo会不准确。
55. this.scroller.scrollTo({ xOffset: 0, yOffset: 310 })
56. }).height('50%').width('30%').backgroundColor(0xADD8E6)
57. }.height('20%')
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/iAYuYT_4SfWFmCJrGIDM1g/zh-cn_image_0000002583479607.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=AAFBA44468F2FB934E4790F1AE56DCB9B29A81DD08A3CA945E2DB863DCE50296)

### 示例6（获得子组件索引信息）

该示例展示了含有group时，获得List组件的Item索引相关信息。

```
1. // xxx.ets
2. class TimeTableDataSource implements IDataSource {
3. private list: TimeTable[] = [];

5. constructor(list: TimeTable[]) {
6. this.list = list;
7. }

9. totalCount(): number {
10. return this.list.length;
11. }

13. getData(index: number): TimeTable {
14. return this.list[index];
15. }

17. registerDataChangeListener(listener: DataChangeListener): void {
18. }

20. unregisterDataChangeListener(listener: DataChangeListener): void {
21. }
22. }

24. class ProjectsDataSource implements IDataSource {
25. private list: string[] = [];

27. constructor(list: string[]) {
28. this.list = list;
29. }

31. totalCount(): number {
32. return this.list.length;
33. }

35. getData(index: number): string {
36. return this.list[index];
37. }

39. registerDataChangeListener(listener: DataChangeListener): void {
40. }

42. unregisterDataChangeListener(listener: DataChangeListener): void {
43. }
44. }

46. @Entry
47. @Component
48. struct ListItemGroupExample {
49. private timeTable: TimeTable[] = [
50. {
51. title: '星期一',
52. projects: ['语文', '数学', '英语']
53. },
54. {
55. title: '星期二',
56. projects: ['物理', '化学', '生物']
57. },
58. {
59. title: '星期三',
60. projects: ['历史', '地理', '政治']
61. },
62. {
63. title: '星期四',
64. projects: ['美术', '音乐', '体育']
65. }
66. ];
67. private scroller: ListScroller = new ListScroller();
68. @State listIndexInfo: VisibleListContentInfo = { index: -1 };
69. @State mess:string = 'null';
70. @State itemBackgroundColorArr: boolean[] = [false];
71. @Builder
72. itemHead(text: string) {
73. Text(text)
74. .fontSize(20)
75. .backgroundColor(0xAABBCC)
76. .width('100%')
77. .padding(10)
78. }

80. @Builder
81. itemFoot(num: number) {
82. Text('共' + num + '节课')
83. .fontSize(16)
84. .backgroundColor(0xAABBCC)
85. .width('100%')
86. .padding(5)
87. }

89. build() {
90. Column() {
91. List({ space: 20, scroller: this.scroller}) {
92. LazyForEach(new TimeTableDataSource(this.timeTable), (item: TimeTable, index: number) => {
93. ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
94. LazyForEach(new ProjectsDataSource(item.projects), (project: string, subIndex: number) => {
95. ListItem() {
96. Text(project)
97. .width('100%')
98. .height(100)
99. .fontSize(20)
100. .textAlign(TextAlign.Center)
101. .backgroundColor(this.itemBackgroundColorArr[index * 3 +subIndex] ? 0x68B4FF: 0xFFFFFF)
102. }
103. }, (item: string) => item)
104. }
105. .divider({ strokeWidth: 1, color: Color.Blue }) // 每行之间的分界线
106. },(item: string) => item)
107. }
108. .width('90%')
109. .sticky(StickyStyle.Header | StickyStyle.Footer)
110. .scrollBar(BarState.Off)
111. .gesture(
112. PanGesture()
113. .onActionUpdate((event: GestureEvent) => {
114. if (event.fingerList[0] != undefined && event.fingerList[0].localX != undefined && event.fingerList[0].localY != undefined) {
115. this.listIndexInfo  = this.scroller.getVisibleListContentInfo(event.fingerList[0].localX, event.fingerList[0].localY);
116. let itemIndex:string = 'undefined';
117. if (this.listIndexInfo.itemIndexInGroup != undefined ) {
118. itemIndex = this.listIndexInfo.itemIndexInGroup.toString();
119. if (this.listIndexInfo.index != undefined && this.listIndexInfo.index >= 0 &&
120. this.listIndexInfo.itemIndexInGroup >= 0 ) {
121. this.itemBackgroundColorArr[this.listIndexInfo.index * 3 + this.listIndexInfo.itemIndexInGroup] = true;
122. }
123. }
124. this.mess = 'index:' + this.listIndexInfo.index.toString() + ' itemIndex:' + itemIndex;
125. }
126. }))
127. .gesture(
128. TapGesture({ count: 1 })
129. .onAction((event: GestureEvent) => {
130. if (event) {
131. this.itemBackgroundColorArr.splice(0,this.itemBackgroundColorArr.length);
132. }
133. })
134. )
135. Text('您当前位置Item索引为'+ this.mess)
136. .fontColor(Color.Red)
137. .height(50)
138. }.width('100%').height('90%').backgroundColor(0xDCDCDC).padding({ top: 5 })
139. }
140. }

142. interface TimeTable {
143. title: string;
144. projects: string[];
145. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/szq0UOf1QvW-HRFTooH5MQ/zh-cn_image_0000002552799958.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=EA804874EB7A4D40A2CC27C7CC1E5602B374178C2EBDC6585DC38564F48587B3)

### 示例7（设置边缘渐隐）

该示例实现了List组件开启边缘渐隐效果并设置边缘渐隐长度。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. import { LengthMetrics } from '@kit.ArkUI'
2. import { ListDataSource } from './ListDataSource';
3. @Entry
4. @Component
5. struct ListExample {
6. private arr: ListDataSource=new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
7. scrollerForList: Scroller = new Scroller();

9. build() {
10. Column() {

12. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
13. LazyForEach(this.arr, (item: number) => {
14. ListItem() {
15. Text('' + item)
16. .width('100%').height(100).fontSize(16)
17. .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
18. }
19. }, (item: number) => item.toString())
20. }
21. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
22. }
23. .width('100%')
24. .height('100%')
25. .backgroundColor(0xDCDCDC)
26. .padding({ top: 5 })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/aoFqMEA7RyK0Klq7Ipc5rg/zh-cn_image_0000002583439653.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=46846020E38761791BEBFB7748F1B959DA920DABD6D25050D8816DAF41A2604B)

### 示例8（单边边缘效果）

该示例通过edgeEffect接口，实现了List组件设置单边边缘效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
8. scrollerForList: Scroller = new Scroller();
9. build() {
10. Column() {
11. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
12. LazyForEach(this.arr, (item: number) => {
13. ListItem() {
14. Text('' + item)
15. .width('100%').height(100).fontSize(16)
16. .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
17. }
18. }, (item: string) => item)
19. }
20. .edgeEffect(EdgeEffect.Spring, {alwaysEnabled: true, effectEdge: EffectEdge.START})
21. .width('90%').height('90%')
22. }
23. .width('100%')
24. .height('100%')
25. .backgroundColor(0xDCDCDC)
26. .padding({ top: 5 })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/oFA6QNOiRXGEJAfETWymWg/zh-cn_image_0000002552959608.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=87A664B834713A5AB4662CE9E8ACBB5DBAF0FD4BE7A0649AD69CC1ADE202CFAC)

### 示例9（设置折行走焦）

从API version 20开始，该示例通过[focusWrapMode](ts-container-list.md#focuswrapmode20)接口，实现了List组件方向键走焦换行效果。

```
1. @Entry
2. @Component
3. struct ListExample {
4. @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
5. build() {
6. Stack({ alignContent: Alignment.TopStart }) {
7. Column() {
8. List({ space: 40, initialIndex: 0 }) {
9. ForEach(this.arr, (item: number, index?: number) => {
10. ListItem() {
11. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
12. Text('' + item)
13. .width(150)
14. .height(93)
15. .fontSize(30)
16. .textAlign(TextAlign.Center)
17. .borderRadius(10)
18. .backgroundColor(0xFFFFFF)
19. .flexShrink(1)
20. .focusable(true)
21. .offset({ left: 5 })
22. }
23. }
24. }, (item: string, index?: number) => item)
25. }
26. .lanes(2)
27. .contentStartOffset(20)
28. .contentEndOffset(20)
29. .width('100%')
30. .scrollBar(BarState.Off)
31. .friction(0.6)
32. .focusWrapMode(FocusWrapMode.WRAP_WITH_ARROW)
33. .alignListItem(ListItemAlign.Center)
34. .offset({ left: 20 })
35. }.width('90%')
36. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/e4E1ho8iRZejLjNdSn3_Fw/zh-cn_image_0000002583479609.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=D12254806F5BA563848BDBAC6381BAE8CAD4A08091686F415660FD76126A7525)

### 示例10（设置显示区域外插入数据时，保持显示内容不变）

该示例通过maintainVisibleContentPosition接口，实现了上滑无限加载历史消息场景。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. import { ListDataSource } from './ListDataSource';

3. @Entry
4. @Component
5. struct ListExample {
6. private arr: ListDataSource = new ListDataSource([990, 991, 992, 993, 994, 995, 996, 997, 998, 999]);
7. build() {
8. Column() {
9. List({ space: 20, initialIndex: 9 }) {
10. LazyForEach(this.arr, (item: number) => {
11. ListItem() {
12. Text('message:' + item)
13. .width('100%').height(100)
14. .fontSize(16)
15. .textAlign(TextAlign.Center)
16. .borderRadius(10)
17. .backgroundColor(0xFFFFFF)
18. }
19. }, (item: number) => item.toString())
20. }
21. .maintainVisibleContentPosition(true)
22. .onScrollIndex((start:number)=>{
23. if (start < 5) {
24. for (let i = 0; i < 10; i++) {
25. this.arr.insertItem(0, this.arr.getData(0) - 1);
26. }
27. }
28. })
29. }
30. .width('100%')
31. .height('100%')
32. .backgroundColor(0xDCDCDC)
33. .padding(12)
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/FTs7p9naQzG6oEeJWJSDIQ/zh-cn_image_0000002552799960.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=39A881D51667B3E7548E141A061A5384478ACD0E1C08929BCB0AF2758D2D26FB)

### 示例11（设置滚动条的边距）

从API version 20开始，该示例展示了通过[scrollBarMargin](ts-container-scrollable-common.md#scrollbarmargin20)属性设置滚动条边距并避让[contentStartOffset](ts-container-list.md#contentstartoffset11)、[contentEndOffset](ts-container-list.md#contentendoffset11)区域的效果。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ListScrollBarMarginExample {
7. @State arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

9. build() {
10. Column() {
11. List({ space: 40, initialIndex: 0 }) {
12. ForEach(this.arr, (item: number, index?: number) => {
13. ListItem() {
14. Text('' + item)
15. .width('100%')
16. .height(100)
17. .fontSize(16)
18. .textAlign(TextAlign.Center)
19. .borderRadius(10)
20. .backgroundColor(0xFFFFFF)
21. }
22. }, (item: string, index?: number) => item)
23. }
24. .contentStartOffset(20)
25. .contentEndOffset(20)
26. .scrollBar(BarState.On)
27. .scrollBarMargin({ start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) })
28. .width('90%')
29. }
30. .width('100%')
31. .height('100%')
32. .backgroundColor(0xDCDCDC)
33. .padding({ top: 5 })
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/MULYGqpGSsioqTiln58cPQ/zh-cn_image_0000002583439655.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=C52B54D5F05A18D98045CDE1E3D57428A3A03E3D509AB098F80BF58C2ECE78C2)

### 示例12（使用OnMove进行拖拽）

从API version 12开始，该示例展示了使用ForEach的[onMove](ts-universal-attributes-drag-sorting.md#onmove)接口进行拖拽排序的效果，支持拖动到List边缘时触发List的自动滚动。

```
1. @Entry
2. @Component
3. struct ForEachSort {
4. @State arr: Array<string> = [];

6. build() {
7. Row() {
8. List() {
9. ForEach(this.arr, (item: string) => {
10. ListItem() {
11. Text(item.toString())
12. .fontSize(16)
13. .textAlign(TextAlign.Center)
14. .size({ height: 100, width: '100%' })
15. }.margin(10)
16. .borderRadius(10)
17. .backgroundColor('#FFFFFFFF')
18. }, (item: string) => item)
19. .onMove((from: number, to: number) => {
20. let tmp = this.arr.splice(from, 1);
21. this.arr.splice(to, 0, tmp[0]);
22. })
23. }
24. .width('100%')
25. .height('100%')
26. .backgroundColor('#FFDCDCDC')
27. }
28. }

30. aboutToAppear(): void {
31. for (let i = 0; i < 100; i++) {
32. this.arr.push(i.toString());
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ooX6z0hOSt2_KkGS8xxCGA/zh-cn_image_0000002552959610.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=6143123A23CB2585A67C11E3CD72D8274B09DFDC401E7F64C11B48D494ECE1E0)

### 示例13（基于断点配置lanes）

从API version 22开始，该示例展示了List组件支持基于断点配置lanes效果。

ListDataSource说明及完整代码参考[示例1添加滚动事件](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]);
8. scrollerForList: Scroller = new Scroller();

10. build() {
11. Column() {
12. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
13. LazyForEach(this.arr, (item: number) => {
14. ListItem() {
15. Text('' + item)
16. .width('100%').height(100).fontSize(16)
17. .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
18. }
19. }, (item: string) => item)
20. }
21. .lanes({ fillType: PresetFillType.BREAKPOINT_SM2MD3LG5}, 10)
22. .width('90%').height(600)
23. }
24. .width('100%')
25. .height('100%')
26. .backgroundColor(0xDCDCDC)
27. .padding({ top: 5 })
28. }
29. }
```

List宽度属于sm及更小的断点区间时显示2列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ZaR-CHPbR_Smv24NFyE27A/zh-cn_image_0000002583479611.png?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=1919EC3AA3108DA31FAC04C4C860195FC4E0F4BE607B085A9F51BEAE41903C23)

List宽度属于md断点区间时显示3列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/1DPfsrEkQ4-hmazw8A0e2w/zh-cn_image_0000002552799962.png?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=E9CF471A84124BE5E9ECC0518BC67566711FECE2A4C4B9926C8B5696ED345F7B)

List宽度属于lg及更大的断点区间时显示5列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/v6fUJfp9RDyYaSWV7IImFg/zh-cn_image_0000002583439657.png?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=10C2004EC80AFDF23975E62218CD808113C8672F908B9CAFC44BD396406C09EB)

### 示例14（获取内容总大小）

从API version 22 开始，该示例实现了List组件获取内容总大小的功能。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
8. scrollerForList: Scroller = new Scroller()
9. @State contentWidth: number = -1;
10. @State contentHeight: number = -1;

12. build() {
13. Column() {
14. List({ space: 20, initialIndex: 0, scroller: this.scrollerForList }) {
15. ForEach(this.arr, (item: number) => {
16. ListItem() {
17. Text('' + item)
18. .width('100%')
19. .height(100)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .borderRadius(10)
23. .backgroundColor(0xFFFFFF)
24. }
25. }, (item: string) => item)
26. }
27. .width('90%').height('90%')

29. // 点击按钮来调用contentSize函数获取内容尺寸
30. Button('GetContentSize')
31. .onClick(() => {
32. // Scroller未绑定组件时会抛异常，需要加上try catch保护
33. try {
34. // 通过调用contentSize函数获取内容尺寸的宽度值
35. this.contentWidth = this.scrollerForList.contentSize().width;
36. // 通过调用contentSize函数获取内容尺寸的高度值
37. this.contentHeight = this.scrollerForList.contentSize().height;
38. } catch (error) {
39. let err: BusinessError = error as BusinessError;
40. console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
41. }
42. })
43. // 将获取到的内容尺寸信息通过文本进行呈现
44. Text('Width：' + this.contentWidth + '，Height：' + this.contentHeight)
45. .fontColor(Color.Red)
46. .height(50)
47. }
48. .width('100%')
49. .height('100%')
50. .backgroundColor(0xDCDCDC)
51. .padding({ top: 5 })
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/jKKGZY6bQkqvP4hNlukKkQ/zh-cn_image_0000002552959612.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=376E86A341BC35B6E27F4C4059B53E6BE0D548FAB48421C2F922B1853FB811AC)

### 示例15（在两个列表之间实现拖拽功能）

该示例通过OnItemDragStart等事件实现了ListItem在两个List组件间的拖拽效果。

```
1. // xxx.ets
2. @ObservedV2
3. class ListData {
4. @Trace public title: string = '';
5. @Trace public data: string[] = [];

7. constructor(title: string, data: string[]) {
8. this.title = title;
9. this.data = data;
10. }
11. }

13. class DraggingData {
14. public data?: string;
15. }

17. @ComponentV2
18. struct DraggableList {
19. @Require @Param data: string[];
20. @Require @Param draggingData: DraggingData;

22. @Builder
23. ItemBuilder(data: string, size: SizeOptions, event: ItemDragInfo): void {
24. Stack() {
25. Text(data)
26. }
27. .backgroundColor(Color.White)
28. .borderRadius(4)
29. .size(size)
30. }

32. viewWidth: number = 0;
33. lastInsertIndex: number = 0;
34. scroller: Scroller = new Scroller();

36. build() {
37. List({ scroller: this.scroller }) {
38. ForEach(this.data, (item: string) => {
39. ListItem() {
40. Text(item)
41. }
42. .width('100%')
43. .height('10%')
44. .margin(10)
45. .backgroundColor(Color.White)
46. .borderRadius(4)
47. .aspectRatio(1)
48. }, (item: string) => item)
49. }
50. .width('50%')
51. .layoutWeight(1)
52. .padding(10)
53. .onItemDragStart((event: ItemDragInfo, itemIndex: number) => {
54. let rect = this.scroller.getItemRect(itemIndex);
55. let size: SizeOptions = {
56. width: rect.width,
57. height: rect.height
58. };
59. this.lastInsertIndex = itemIndex;
60. this.draggingData.data = this.data[itemIndex];
61. this.data.splice(itemIndex, 1);

63. return this.ItemBuilder(this.draggingData.data, size, event);
64. })
65. .onItemDragEnter((event: ItemDragInfo) => {
66. console.info('Item drag enter at position:', event.x, event.y);
67. })
68. .onItemDragMove((event: ItemDragInfo, itemIndex: number, insertIndex: number) => {
69. if (this.lastInsertIndex != insertIndex){
70. console.info('insertIndex change from ', this.lastInsertIndex, 'to', insertIndex);
71. this.lastInsertIndex = insertIndex;
72. }
73. })
74. .onItemDragLeave((event: ItemDragInfo, itemIndex: number) => {
75. console.info('Item ' + itemIndex + ' drag leave at position:', event.x, event.y);
76. })
77. .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => {
78. if (!isSuccess) {
79. this.draggingData.data = undefined;
80. return;
81. }
82. if (insertIndex >= 0) {
83. this.data.splice(insertIndex, 0, this.draggingData.data!);
84. }
85. this.draggingData.data = undefined;
86. })
87. .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
88. this.viewWidth = newValue.width as number;
89. })
90. }
91. }

93. @Entry
94. @ComponentV2
95. struct Index {
96. @Local data: ListData[] = [
97. new ListData('A', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']),
98. new ListData('B', ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']),
99. ]
100. @Local draggingData: DraggingData = new DraggingData();

102. build() {
103. Stack() {
104. Row() {
105. DraggableList({ data: this.data[0].data, draggingData: this.draggingData })
106. DraggableList({ data: this.data[1].data, draggingData: this.draggingData })
107. }
108. }
109. .backgroundColor('#FFDCDCDC')
110. }
111. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ylRgN7fKSFugz9JeT2QWpw/zh-cn_image_0000002583479613.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=E8A81556244BD7D29EFBF23D3C79623EFB6DA98AE678E8647FADB6FC75C71418)

### 示例16（实现ListItemGroup中点击项的居中效果）

该示例使用[scrollToItemInGroup](ts-container-list.md#scrolltoitemingroup11)接口，实现了点击[ListItemGroup](ts-container-listitemgroup.md)中的[ListItem](ts-container-listitem.md)时将其居中的效果。

```
1. import { util } from '@kit.ArkTS';

3. class Contact {
4. key: string = util.generateRandomUUID(true);
5. name: string;
6. icon: Resource;

8. constructor(name: string, icon: Resource) {
9. this.name = name;
10. this.icon = icon;
11. }
12. }

14. class ContactsGroup {
15. title: string = '';
16. contacts: Array<object> | null = null;
17. key: string = '';
18. }

20. @Entry
21. @Component
22. struct ContactsList {
23. private scroller: ListScroller = new ListScroller();
24. private contactsGroups: ContactsGroup[] = [
25. {
26. title: 'A',
27. contacts: [
28. new Contact('艾佳', $r('app.media.icon')),  // $r('app.media.icon')需要替换为开发者所需的图像资源文件
29. new Contact('安安', $r('app.media.icon')),
30. new Contact('Angela', $r('app.media.icon'))
31. // ...
32. ],
33. key: util.generateRandomUUID(true)
34. } as ContactsGroup,
35. {
36. title: 'B',
37. contacts: [
38. new Contact('白叶', $r('app.media.icon')),
39. new Contact('伯明', $r('app.media.icon'))
40. // ...
41. ],
42. key: util.generateRandomUUID(true)
43. } as ContactsGroup,
44. // ...
45. ]

47. @Builder
48. itemHead(text: string) {
49. Text(text)
50. .fontSize(20)
51. .backgroundColor('#fff1f3f5')
52. .width('100%')
53. .padding(5)
54. }

56. build() {
57. List({ scroller: this.scroller }) {
58. ForEach(this.contactsGroups, (item: ContactsGroup, index: number) => {
59. ListItemGroup({ header: this.itemHead(item.title) }) {
60. ForEach(item.contacts, (contact: Contact, subIndex: number) => {
61. ListItem() {
62. Row() {
63. Image(contact.icon)
64. .width(40)
65. .height(40)
66. .margin(10)
67. Text(contact.name).fontSize(20)
68. }
69. .width('100%')
70. .justifyContent(FlexAlign.Start)
71. .margin(10)
72. }
73. .gesture(
74. TapGesture({ count: 1 })
75. .onAction((event: GestureEvent) => {
76. if (event) {
77. const itemRect = this.scroller.getItemRectInGroup(index, subIndex);
78. console.info('第', index + 1, '个ListItemGroup的第', subIndex + 1, '个ListItem的 x:', itemRect.x,
79. ' y:', itemRect.y, ' width:', itemRect.width, ' height:', itemRect.height)
80. this.scroller.scrollToItemInGroup(index, subIndex, true, ScrollAlign.CENTER);
81. }
82. })
83. )
84. }, (contact: Contact) => JSON.stringify(contact))
85. }
86. .divider({ strokeWidth: 4 })
87. .width('100%')
88. }, (item: ContactsGroup) => JSON.stringify(item))
89. }
90. .onScrollFrameBegin((offset: number, state: ScrollState) => {
91. console.info('List scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
92. return { offsetRemain: offset };
93. })
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/aH52KkR0Ss-xroCYFV57Mw/zh-cn_image_0000002552799964.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=582A4D4334D170368CADC4C297280A1AE83A0353615369DD16D7FCB9AE861366)

### 示例17（设置多选聚拢动画）

该示例通过打开List多选聚拢动画开关，实现了在ListItem上[长按弹出菜单](ts-universal-attributes-menu.md#bindcontextmenu8)时聚拢显示范围内被选中的ListItem。

从API version 23开始，List组件新增[编辑模式选项](ts-container-list.md#editmodeoptions23)接口，可以设置多选聚拢动画开关。

ListDataSource说明及完整代码参考[示例1（添加滚动事件）](ts-container-list.md#示例1添加滚动事件)。

```
1. // xxx.ets
2. import { ListDataSource } from './ListDataSource';

4. @Entry
5. @Component
6. struct ListExample {
7. private arr: ListDataSource = new ListDataSource([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
8. @State isSelected: boolean[] = [];
9. selectedCount: number = 0;

11. @Styles
12. normalStyles(): void {
13. .opacity(1.0)
14. }

16. @Styles
17. selectStyles(): void {
18. .opacity(0.4)
19. }

21. onPageShow(): void {
22. let i: number = 0;
23. for (i = 0; i < 10; i++) {
24. this.isSelected.push(false);
25. }
26. }

28. @Builder
29. MenuBuilder() {
30. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
31. Text('menu item 1')
32. .fontSize(18)
33. .width(120)
34. .height(50)
35. .textAlign(TextAlign.Center)
36. Divider().height(10)
37. Text('menu item 2')
38. .fontSize(18)
39. .width(120)
40. .height(50)
41. .textAlign(TextAlign.Center)
42. }.width(100)
43. }

45. build() {
46. Column({ space: 5 }) {
47. List({ space: 10 }) {
48. LazyForEach(this.arr, (item: number) => {
49. ListItem() {
50. Text(item.toString())
51. .fontSize(16)
52. .backgroundColor(Color.White)
53. .width('100%')
54. .height(50)
55. .textAlign(TextAlign.Center)
56. }
57. .selected(this.isSelected[item])
58. // 设置多选显示效果
59. .stateStyles({
60. normal: this.normalStyles,
61. selected: this.selectStyles
62. })
63. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress,
64. { preview: MenuPreviewMode.IMAGE, hapticFeedbackMode: HapticFeedbackMode.ENABLED })
65. .onClick(() => {
66. this.isSelected[item] = !this.isSelected[item];
67. console.info(`item:${item}, this.isSelected[item]:${this.isSelected[item]}`)
68. if (this.isSelected[item]) {
69. ++this.selectedCount;
70. } else {
71. --this.selectedCount;
72. }
73. })
74. }, (item: number) => item.toString())
75. }
76. .editModeOptions({
77. enableGatherSelectedItemsAnimation: true, onGetPreviewBadge: () => {
78. return this.selectedCount;
79. }
80. })
81. .width('90%')
82. .height(300)
83. .scrollBar(BarState.Off)
84. }.width('100%').margin({ top: 5 }).backgroundColor('#FFDCDCDC')
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/SNLifOmmQ2Wxlsc1etoWbA/zh-cn_image_0000002583439659.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000126Z&HW-CC-Expire=86400&HW-CC-Sign=44547368F97821C8C8D28E61960031B397FE30C1B404F92D268EFD6864E301C3)
