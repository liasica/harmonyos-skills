---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow
title: WaterFlow
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > WaterFlow
category: harmonyos-references
scraped_at: 2026-04-28T08:01:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6fb6b72211e4774113797788ab2641e71dcf4a3fd45a672025a336e3a2d84a33
---

瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局。

说明

该组件从API version 9 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

WaterFlow组件支持展示瀑布流布局，不支持编辑模式和子元素拖动功能。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](ts-gesture-blocking-enhancement.md)进行处理。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持[FlowItem](ts-container-flowitem.md)子组件和自定义组件。自定义组件在WaterFlow下使用时，建议使用FlowItem作为自定义组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

说明

WaterFlow子组件的visibility属性设置为None时不显示，但该子组件周围的columnsGap、rowsGap、margin仍会生效。

在涉及大量子组件的情况下，建议采用懒加载、缓存数据、组件复用、固定宽高以及布局优化等方法，以提升性能和减少内存占用。最佳实践请参考[优化瀑布流加载慢丢帧问题](../best-practices/bpta-waterflow-performance-optimization.md)。

纵向布局时，WaterFlow会计算每一列中已放置子组件的累计高度，并将新子组件放入累计高度最小的那一列，以保持整体布局紧凑。

若多个列的高度相同，优先放入最左边的列。在RTL模式下，优先放入最右边的列。

从API version 21开始，WaterFlow单个子组件的宽高最大为16777216px；API version 20及之前，WaterFlow单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

## 接口

PhonePC/2in1TabletTVWearable

WaterFlow(options?: WaterFlowOptions)

创建瀑布流容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WaterFlowOptions](ts-container-waterflow.md#waterflowoptions对象说明) | 否 | 瀑布流组件参数。 |

## WaterFlowOptions对象说明

PhonePC/2in1TabletTVWearable

瀑布流组件参数对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| footer | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置WaterFlow尾部组件，用于在瀑布流末尾显示自定义内容（如加载提示、底部标识等）。不设置时不显示尾部组件。  **说明：**  使用方法参见[示例1](ts-container-waterflow.md#示例1使用基本瀑布流)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| footerContent18+ | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 设置WaterFlow尾部组件。  该参数的优先级高于参数footer，即同时设置footer和footerContent时，以footerContent设置的组件为准。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 是 | 可滚动组件的控制器，与可滚动组件绑定。  **说明：**  不允许和其他滚动类组件，如：[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)绑定同一个滚动控制对象。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| sections12+ | [WaterFlowSections](ts-container-waterflow.md#waterflowsections12) | 否 | 是 | 设置FlowItem分组，实现同一个瀑布流组件内部各分组使用不同列数混合布局。适用于需要在不同区域使用不同列数布局的场景。不设置时使用统一列数布局。  **说明：**  1. 使用分组混合布局时会忽略[columnsTemplate](ts-container-waterflow.md#columnstemplate)和[rowsTemplate](ts-container-waterflow.md#rowstemplate)属性。  2. 使用分组混合布局时不支持单独设置footer，可以使用最后一个分组作为尾部组件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| layoutMode12+ | [WaterFlowLayoutMode](ts-container-waterflow.md#waterflowlayoutmode12枚举说明) | 否 | 是 | 设置WaterFlow的布局模式，根据使用场景选择更切合的模式。  **说明：**  默认值：[ALWAYS\_TOP\_DOWN](ts-container-waterflow.md#waterflowlayoutmode12枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## WaterFlowSections12+

PhonePC/2in1TabletTVWearable

瀑布流分组信息。

说明

使用splice、push、update修改分组信息后需要保证所有分组子节点总数与瀑布流实际子节点总数一致，否则会出现瀑布流因为不能正常布局而无法滑动的问题。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

创建一个瀑布流分组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### splice12+

PhonePC/2in1TabletTVWearable

splice(start: number, deleteCount?: number, sections?: Array<SectionOptions>): boolean

移除或者替换已存在的分组和/或添加新分组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 | 从0开始计算的索引，会转换为整数，表示要开始改变分组的位置。  **说明：**  1. 如果索引是负数，则从末尾开始计算，使用start + WaterFlowSections.length()。  2. 如果 start < -WaterFlowSections.length()，则使用0。  3. 如果 start >= WaterFlowSections.length()，则在最后添加新分组。 |
| deleteCount | number | 否 | 表示要从start开始删除的分组数量。  **说明：**  1. 如果省略了deleteCount，或者其值大于或等于由start指定的位置到WaterFlowSections末尾的分组数量，那么从start到WaterFlowSections末尾的所有分组将被删除。  2. 如果deleteCount是0或者负数，则不会删除任何分组。 |
| sections | Array<[SectionOptions](ts-container-waterflow.md#sectionoptions12对象说明)> | 否 | 表示要从start开始加入的分组。如果不指定，splice()将只从瀑布流中删除分组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分组修改成功返回true；修改失败（要加入的分组中有任意分组的itemsCount不是非负数）返回false。 |

### push12+

PhonePC/2in1TabletTVWearable

push(section: SectionOptions): boolean

将指定分组添加到瀑布流末尾。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| section | [SectionOptions](ts-container-waterflow.md#sectionoptions12对象说明) | 是 | 添加到瀑布流末尾的分组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分组添加成功返回true，添加失败（新分组的itemsCount不是非负数）返回false。 |

### update12+

PhonePC/2in1TabletTVWearable

update(sectionIndex: number, section: SectionOptions): boolean

修改指定索引分组的配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sectionIndex | number | 是 | 从0开始计算的索引，会转换为整数，表示要修改的分组的位置。  **说明：**  1. 如果索引是负数，则从末尾开始计算，使用sectionIndex + WaterFlowSections.length()。  2. 如果sectionIndex < -WaterFlowSections.length()，则使用0。  3. 如果sectionIndex >= WaterFlowSections.length()，则在最后添加新分组。 |
| section | [SectionOptions](ts-container-waterflow.md#sectionoptions12对象说明) | 是 | 新的分组信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 分组是否更新成功，新分组的itemsCount不是非负数时返回false。 |

### values12+

PhonePC/2in1TabletTVWearable

values(): Array<SectionOptions>

获取瀑布流中所有分组配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SectionOptions](ts-container-waterflow.md#sectionoptions12对象说明)> | 瀑布流中所有分组配置信息。 |

### length12+

PhonePC/2in1TabletTVWearable

length(): number

获取瀑布流中分组数量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 瀑布流中分组数量。 |

## SectionOptions12+对象说明

PhonePC/2in1TabletTVWearable

FlowItem分组配置信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| itemsCount | number | 否 | 否 | 分组中FlowItem数量，必须是非负数。若splice、push、update方法收到的分组中有分组的itemsCount小于0，则不会执行该方法。 避免使用itemsCount为0的分组，这可能导致布局计算异常。 |
| crossCount | number | 否 | 是 | 纵向布局时为列数，横向布局时为行数，默认值：1。小于1的按默认值处理。 |
| columnsGap | [Dimension](ts-types.md#dimension10) | 否 | 是 | 该分组的列间距，不设置该参数时默认使用瀑布流的[columnsGap](ts-container-waterflow.md#columnsgap)，设置非法值时使用0vp。 |
| rowsGap | [Dimension](ts-types.md#dimension10) | 否 | 是 | 该分组的行间距，不设置该参数时默认使用瀑布流的[rowsGap](ts-container-waterflow.md#rowsgap)，设置非法值时使用0vp。 |
| margin | [Margin](ts-types.md#margin) | [Dimension](ts-types.md#dimension10) | 否 | 是 | 该分组的外边距参数为Length类型时，四个方向外边距同时生效。  默认值：0  单位：vp  margin设置百分比时，上下左右外边距均以瀑布流的width作为基础值。 |
| onGetItemMainSizeByIndex | [GetItemMainSizeByIndex](ts-container-waterflow.md#getitemmainsizebyindex12) | 否 | 是 | 瀑布流组件布局过程中获取指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。  **说明：**  1. 同时使用onGetItemMainSizeByIndex和FlowItem的宽高属性时，主轴大小以onGetItemMainSizeByIndex返回结果为准，onGetItemMainSizeByIndex会覆盖FlowItem的主轴长度。  2. 使用onGetItemMainSizeByIndex可以提高瀑布流跳转到指定位置或index时的效率，避免混用设置onGetItemMainSizeByIndex和未设置的分组，会导致布局异常。  3. onGetItemMainSizeByIndex返回负数时FlowItem高度为0。 |

## GetItemMainSizeByIndex12+

PhonePC/2in1TabletTVWearable

type GetItemMainSizeByIndex = (index: number) => number

根据index获取指定Item的主轴大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | FlowItem在WaterFlow中的索引。  取值范围：[0, 子节点总数-1] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 指定index的FlowItem的主轴大小，纵向瀑布流时为高度，横向瀑布流时为宽度，单位vp。 |

## WaterFlowLayoutMode12+枚举说明

PhonePC/2in1TabletTVWearable

瀑布流组件布局模式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALWAYS\_TOP\_DOWN | 0 | 默认的从上到下的布局模式。视窗内的FlowItem依赖视窗上方所有FlowItem的布局信息。因此跳转或切换列数时，需要计算出上方所有的FlowItem的布局信息。 |
| SLIDING\_WINDOW | 1 | 移动窗口式的布局模式。只考虑视窗内的布局信息，对视窗上方的FlowItem没有依赖关系，因此向后跳转或切换列数时只需要布局视窗内的FlowItem。建议优先采用该模式，尤其在应用需要支持屏幕旋转或动态切换列数的场景下。  **说明：**  1. 无动画跳转到较远的位置时，会以目标位置为基准，向前或向后布局FlowItem。这之后如果滑回跳转前的位置，内容的布局效果可能和之前不一致。 这个效果会导致跳转后回滑到顶部时，顶部节点可能不对齐。所以该布局模式下会在滑动到顶部后自动调整布局，保证顶部对齐。在有多个分组的情况下，会在滑动结束时调整在视窗内的分组。  2. [scroller](ts-container-waterflow.md#waterflowoptions对象说明)的[currentOffset](ts-container-scroll.md#currentoffset)或[offset](ts-container-scroll.md#offset23)接口返回的总偏移量在触发跳转或数据更新后不准确，在回滑到顶部时会重新校准，从API version 23开始，新增offset接口。  3. 如果在同一帧内调用跳转（如无动画的[scrollToIndex](ts-container-scroll.md#scrolltoindex)、[scrollEdge](ts-container-scroll.md#scrolledge)）和输入偏移量（如滑动手势或滚动动画），两者都会生效。  4. 调用无动画的[scrollToIndex](ts-container-scroll.md#scrolltoindex)进行跳转，如果跳转到较远位置（超过视窗内的FlowItem数量的位置）时，移动窗口模式对总偏移量进行估算。  5. 仅在API version 18及以上版本中支持滚动条[scrollBar](ts-container-scrollable-common.md#scrollbar11)显示。低于此版本时，设置滚动条将不显示。 |

| 对比维度 | ALWAYS\_TOP\_DOWN (默认) | SLIDING\_WINDOW |
| --- | --- | --- |
| 适用场景 | 固定列数、简单瀑布流 | 动态列数、大数据量、屏幕旋转 |
| 布局策略 | 从顶部开始完整布局 | 滑动窗口式布局 |
| 性能特点 | 依赖上方所有 FlowItem | 只考虑视窗内布局 |
| 跳转效率 | 需要计算上方所有布局 | 快速跳转，无需完整计算 |
| 列数切换 | 需要重新计算全部布局 | 只重新布局视窗内容 |
| 屏幕旋转 | 支持，但性能较差 | 支持，性能好 |
| 滚动条显示 | 始终支持 | API 18+ 支持 |
| 布局一致性 | 始终保持一致 | 跳转后可能不一致 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)和[滚动组件通用属性](ts-container-scrollable-common.md#属性)外，还支持以下属性：

说明

WaterFlow组件使用通用属性[clip12+](ts-universal-attributes-sharp-clipping.md#clip12)和通用属性[clip18+](ts-universal-attributes-sharp-clipping.md#clip18)时默认值都为true。

WaterFlow组件内容裁剪模式[ContentClipMode14+枚举说明](ts-container-scrollable-common.md#contentclipmode14枚举说明)为ContentClipMode.CONTENT\_ONLY，padding区域会被裁剪不显示。

### columnsTemplate

PhonePC/2in1TabletTVWearable

columnsTemplate(value: string)

设置当前瀑布流组件布局列的数量，不设置时默认1列。

例如，'1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。

可使用columnsTemplate('repeat(auto-fill,track-size)')根据给定的列宽track-size自动计算列数，其中repeat、auto-fill为关键字，track-size为可设置的宽度，支持的单位包括px、vp、%或有效数字，默认单位为vp，使用方法参见[示例2](ts-container-waterflow.md#示例2自动计算列数)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前瀑布流组件布局列的数量。  默认值：'1fr' |

### columnsTemplate22+

PhonePC/2in1TabletTVWearable

columnsTemplate(value: string | ItemFillPolicy)

设置当前瀑布流组件布局列的数量，不设置时默认1列。

当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](ts-container-waterflow.md#columnstemplate)。

当value设置为ItemFillPolicy类型时，将根据WaterFlow组件宽度对应[断点类型](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)确定列数。

例如，ItemFillPolicy.BREAKPOINT\_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [ItemFillPolicy](ts-types.md#itemfillpolicy22) | 是 | 当前瀑布流组件布局列的数量。 |

### rowsTemplate

PhonePC/2in1TabletTVWearable

rowsTemplate(value: string)

设置当前瀑布流组件布局行的数量，不设置时默认1行。

例如，'1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。

可使用rowsTemplate('repeat(auto-fill,track-size)')根据给定的行高track-size自动计算行数，其中repeat、auto-fill为关键字，track-size为可设置的高度，支持的单位包括px、vp、%或有效数字，默认单位为vp。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前瀑布流组件布局行的数量。  默认值：'1fr' |

### itemConstraintSize

PhonePC/2in1TabletTVWearable

itemConstraintSize(value: ConstraintSizeOptions)

设置约束尺寸，子组件布局时，进行尺寸范围限制。使用方法参考[示例1](ts-container-waterflow.md#示例1使用基本瀑布流)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 约束尺寸。设置小于0的值，参数不生效。  **说明：**  1.同时设置itemConstraintSize和FlowItem的[constraintSize](ts-universal-attributes-size.md#constraintsize)属性时，minWidth/minHeight会取其中的最大值，maxWidth/maxHeight会取其中的最小值，调整后的值作为FlowItem的constraintSize处理。  2.只设置itemConstraintSize时，相当于对WaterFlow所有子组件设置了相同的constraintSize。  3.itemConstraintSize通过以上两种方式转换成FlowItem的constraintSize后的生效规则与通用属性[constraintSize](ts-universal-attributes-size.md#constraintsize)相同。 |

### columnsGap

PhonePC/2in1TabletTVWearable

columnsGap(value: Length)

设置列与列的间距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 列与列的间距。  默认值：0  取值范围：[0, +∞)，小于0时按0处理。 |

### rowsGap

PhonePC/2in1TabletTVWearable

rowsGap(value: Length)

设置行与行的间距。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 行与行的间距。  默认值：0  取值范围：[0, +∞)，小于0时按0处理。 |

### layoutDirection

PhonePC/2in1TabletTVWearable

layoutDirection(value: FlexDirection)

设置布局的主轴方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FlexDirection](ts-appendix-enums.md#flexdirection) | 是 | 布局的主轴方向。  默认值：FlexDirection.Column |

layoutDirection优先级高于rowsTemplate和columnsTemplate。根据layoutDirection设置情况，分为以下三种设置模式：

* layoutDirection设置纵向布局（FlexDirection.Column 或 FlexDirection.ColumnReverse）

  此时columnsTemplate有效（如果未设置，取默认值）。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件纵向布局，辅轴均分成横向2列。
* layoutDirection设置横向布局（FlexDirection.Row 或 FlexDirection.RowReverse）

  此时rowsTemplate有效（如果未设置，取默认值）。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件横向布局，辅轴均分成纵向3列。
* layoutDirection未设置布局方向

  布局方向为layoutDirection的默认值：FlexDirection.Column，此时columnsTemplate有效。例如columnsTemplate设置为'1fr 1fr'、rowsTemplate设置为'1fr 1fr 1fr'时，瀑布流组件纵向布局，辅轴均分成横向2列。

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

设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。使用方法参考[嵌套滚动实现方式二](ts-container-scroll.md#示例3嵌套滚动实现方式二)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](ts-container-scrollable-common.md#nestedscrolloptions10对象说明) | 是 | 嵌套滚动选项。 |

### friction10+

PhonePC/2in1TabletTVWearable

friction(value: number | Resource)

设置摩擦系数，手动划动滚动区域时生效，仅影响惯性滚动过程，对惯性滚动过程中的链式效果有间接影响。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 摩擦系数。  默认值：非可穿戴设备为0.6，可穿戴设备为0.9。  从API version 11开始，非可穿戴设备默认值为0.7。  从API version 12开始，非可穿戴设备默认值为0.75。  取值范围：(0, +∞)，设置为小于等于0的值时，按默认值处理。 |

### cachedCount11+

PhonePC/2in1TabletTVWearable

cachedCount(value: number)

设置预加载的FlowItem数量。

只在[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和开启了[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)开关的[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预加载的FlowItem的数量。  默认值：根据屏幕内显示的节点个数设置，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。 |

### cachedCount14+

PhonePC/2in1TabletTVWearable

cachedCount(count: number, show: boolean)

设置预加载的FlowItem数量，并配置是否显示预加载节点。

配合[clip](ts-universal-attributes-sharp-clipping.md#clip12)或[clipContent](ts-container-scrollable-common.md#clipcontent14)属性可以显示出预加载节点。

只在[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和开启了virtualScroll开关的[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)中生效，超出显示及缓存范围的FlowItem会被释放。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载的FlowItem的数量。  默认值：根据屏幕内显示的节点个数设置，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。 |
| show | boolean | 是 | 被预加载的FlowItem是否需要显示。设置为true时显示预加载的FlowItem，设置为false时不显示预加载的FlowItem。  默认值：false |

### syncLoad20+

PhonePC/2in1TabletTVWearable

syncLoad(enable: boolean)

设置是否同步加载WaterFlow区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否同步加载WaterFlow区域内所有子组件。  true表示同步加载，false表示异步加载。  默认值：true。  **说明：**  设置为false时，在首次显示、不带动画[scrollToIndex](ts-container-scroll.md#scrolltoindex)跳转场景，若当帧布局耗时超过50ms，会将WaterFlow区域内尚未布局的子组件延后到下一帧进行布局。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)和[滚动组件通用事件](ts-container-scrollable-common.md#事件)外，还支持以下事件：

### onReachStart

PhonePC/2in1TabletTVWearable

onReachStart(event: () => void)

瀑布流内容到达起始位置时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 瀑布流内容到达起始位置时触发的回调。 |

### onReachEnd

PhonePC/2in1TabletTVWearable

onReachEnd(event: () => void)

瀑布流内容到达末尾位置时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 瀑布流内容到达末尾位置时触发的回调。 |

### onScrollFrameBegin10+

PhonePC/2in1TabletTVWearable

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，瀑布流将按照返回值的实际滑动量进行滑动。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. WaterFlow惯性滚动。
3. 调用[fling](ts-container-scroll.md#fling12)接口触发滚动。

不触发该事件的条件：

1. 调用除[fling](ts-container-scroll.md#fling12)接口外的其他滚动控制接口。
2. 越界回弹。
3. 拖动滚动条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](ts-container-scroll.md#onscrollframebegincallback18) | 是 | 每帧滚动开始回调函数。 |

### onScrollIndex11+

PhonePC/2in1TabletTVWearable

onScrollIndex(event: (first: number, last: number) => void)

当前瀑布流显示的起始位置/终止位置的子组件发生变化时触发。瀑布流初始化时会触发一次。

瀑布流显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的瀑布流起始位置的索引值。  取值范围：[0, 子节点总数-1] |
| last | number | 是 | 当前显示的瀑布流终止位置的索引值。  取值范围：[0, 子节点总数-1] |

通过last参数可以判断是否“继续加载数据”，参考[示例3使用分组](ts-container-waterflow.md#示例3使用分组)中“即将触底时提前增加数据”的处理逻辑。

当WaterFlow列表为空时，使用不同的WaterFlowOptions参数会导致onScrollIndex事件的返回值有所不同。具体差异请参见下表：

| layoutMode | sections | first | last |
| --- | --- | --- | --- |
| ALWAYS\_TOP\_DOWN | 无 | 0 | 0 |
| ALWAYS\_TOP\_DOWN | 有 | 0 | -1 |
| SLIDING\_WINDOW | 可选 | 1000000 | -1 |

## UIWaterFlowEvent19+

PhonePC/2in1TabletTVWearable

frameNode中[getEvent('WaterFlow')](js-apis-arkui-framenode.md#geteventwaterflow19)方法的返回值，可用于给WaterFlow节点设置滚动事件。

UIWaterFlowEvent继承于[UIScrollableCommonEvent](ts-container-scrollable-common.md#uiscrollablecommonevent19)。

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

setOnScrollIndex(callback: OnWaterFlowScrollIndexCallback | undefined): void

设置[onScrollIndex](ts-container-waterflow.md#onscrollindex11)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnWaterFlowScrollIndexCallback](ts-container-waterflow.md#onwaterflowscrollindexcallback19) | undefined | 是 | onScrollIndex事件的回调函数。 |

## OnWaterFlowScrollIndexCallback19+

PhonePC/2in1TabletTVWearable

type OnWaterFlowScrollIndexCallback = (first: number, last: number) => void

WaterFlow组件可见区域item变化事件的回调类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的瀑布流起始位置的索引值。 |
| last | number | 是 | 当前显示的瀑布流终止位置的索引值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用基本瀑布流）

该示例展示了WaterFlow组件数据加载处理、属性设置和事件回调等基本使用场景。

WaterFlowDataSource实现了LazyForEach数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给WaterFlow提供子组件。

```
1. // WaterFlowDataSource.ets

3. // 实现IDataSource接口的对象，用于瀑布流组件加载数据
4. export class WaterFlowDataSource implements IDataSource {
5. private dataArray: number[] = [];
6. private listeners: DataChangeListener[] = [];

8. constructor() {
9. for (let i = 0; i < 100; i++) {
10. this.dataArray.push(i);
11. }
12. }

14. // 获取索引对应的数据
15. public getData(index: number): number {
16. return this.dataArray[index];
17. }

19. // 通知控制器数据重新加载
20. notifyDataReload(): void {
21. this.listeners.forEach(listener => {
22. listener.onDataReloaded();
23. })
24. }

26. // 通知控制器数据增加
27. notifyDataAdd(index: number): void {
28. this.listeners.forEach(listener => {
29. listener.onDataAdd(index);
30. })
31. }

33. // 通知控制器数据变化
34. notifyDataChange(index: number): void {
35. this.listeners.forEach(listener => {
36. listener.onDataChange(index);
37. })
38. }

40. // 通知控制器数据删除
41. notifyDataDelete(index: number): void {
42. this.listeners.forEach(listener => {
43. listener.onDataDelete(index);
44. })
45. }

47. // 通知控制器数据位置变化
48. notifyDataMove(from: number, to: number): void {
49. this.listeners.forEach(listener => {
50. listener.onDataMove(from, to);
51. })
52. }

54. // 通知控制器数据批量修改
55. notifyDatasetChange(operations: DataOperation[]): void {
56. this.listeners.forEach(listener => {
57. listener.onDatasetChange(operations);
58. })
59. }

61. // 获取数据总数
62. public totalCount(): number {
63. return this.dataArray.length;
64. }

66. // 注册改变数据的控制器
67. registerDataChangeListener(listener: DataChangeListener): void {
68. if (this.listeners.indexOf(listener) < 0) {
69. this.listeners.push(listener);
70. }
71. }

73. // 注销改变数据的控制器
74. unregisterDataChangeListener(listener: DataChangeListener): void {
75. const pos = this.listeners.indexOf(listener);
76. if (pos >= 0) {
77. this.listeners.splice(pos, 1);
78. }
79. }

81. // 增加数据
82. public add1stItem(): void {
83. this.dataArray.splice(0, 0, this.dataArray.length);
84. this.notifyDataAdd(0);
85. }

87. // 在数据尾部增加一个元素
88. public addLastItem(): void {
89. this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
90. this.notifyDataAdd(this.dataArray.length - 1);
91. }

93. // 在指定索引位置增加一个元素
94. public addItem(index: number): void {
95. this.dataArray.splice(index, 0, this.dataArray.length);
96. this.notifyDataAdd(index);
97. }

99. // 删除第一个元素
100. public delete1stItem(): void {
101. this.dataArray.splice(0, 1);
102. this.notifyDataDelete(0);
103. }

105. // 删除第二个元素
106. public delete2ndItem(): void {
107. this.dataArray.splice(1, 1);
108. this.notifyDataDelete(1);
109. }

111. // 删除最后一个元素
112. public deleteLastItem(): void {
113. this.dataArray.splice(-1, 1);
114. this.notifyDataDelete(this.dataArray.length);
115. }

117. // 在指定索引位置删除一个元素
118. public deleteItem(index: number): void {
119. this.dataArray.splice(index, 1);
120. this.notifyDataDelete(index);
121. }

123. // 重新加载数据
124. public reload(): void {
125. this.dataArray.splice(1, 1);
126. this.dataArray.splice(3, 2);
127. this.notifyDataReload();
128. }

130. // 在数据尾部增加count个元素
131. public addNewItems(count: number): void {
132. let len = this.dataArray.length;
133. for (let i = 0; i < count; i++) {
134. this.dataArray.push(this.dataArray[len - 1] + i + 1);
135. this.notifyDataAdd(this.dataArray.length - 1);
136. }
137. }

139. // 刷新所有元素
140. public refreshItems(): void {
141. let newDataArray: number[] = [];
142. for (let i = 0; i < 100; i++) {
143. newDataArray.push(this.dataArray[0] + i + 1000);
144. }
145. this.dataArray = newDataArray;
146. this.notifyDataReload();
147. }
148. }
```

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. enum FooterState {
5. Loading = 0,
6. End = 1
7. }

9. @Entry
10. @Component
11. struct WaterFlowDemo {
12. @State minSize: number = 80;
13. @State maxSize: number = 180;
14. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
15. @State footerState: FooterState = FooterState.Loading;
16. scroller: Scroller = new Scroller();
17. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
18. private itemWidthArray: number[] = [];
19. private itemHeightArray: number[] = [];

21. // 计算FlowItem宽/高
22. getSize() {
23. let ret = Math.floor(Math.random() * this.maxSize);
24. return (ret > this.minSize ? ret : this.minSize);
25. }

27. // 设置FlowItem的宽/高数组
28. setItemSizeArray() {
29. for (let i = 0; i < 100; i++) {
30. this.itemWidthArray.push(this.getSize());
31. this.itemHeightArray.push(this.getSize());
32. }
33. }

35. // 组件生命周期：在组件即将出现时初始化尺寸数组
36. aboutToAppear() {
37. this.setItemSizeArray();
38. }

40. @Builder
41. itemFoot() {
42. // 注意：不要直接用IfElse节点作为footer的根节点
43. // 必须在外面使用(Column/Row/Stack等)容器包裹，确保布局正确
44. Column() {
45. if (this.footerState == FooterState.Loading) {
46. Text(`加载中...`)
47. .fontSize(10)
48. .backgroundColor(Color.Red)
49. .width(50)
50. .height(50)
51. .align(Alignment.Center)
52. .margin({ top: 2 })
53. } else if (this.footerState == FooterState.End) {
54. Text(`到底啦...`)
55. .fontSize(10)
56. .backgroundColor(Color.Red)
57. .width(50)
58. .height(50)
59. .align(Alignment.Center)
60. .margin({ top: 2 })
61. } else {
62. Text(`Footer`)
63. .fontSize(10)
64. .backgroundColor(Color.Red)
65. .width(50)
66. .height(50)
67. .align(Alignment.Center)
68. .margin({ top: 2 })
69. }
70. }
71. }

73. build() {
74. Column({ space: 2 }) {
75. WaterFlow({ footer: this.itemFoot() }) {
76. LazyForEach(this.dataSource, (item: number) => {
77. FlowItem() {
78. Column() {
79. Text('N' + item).fontSize(12).height('16')
80. // 注意：需要确保对应的jpg文件存在才会正常显示
81. Image('res/waterFlowTest(' + item % 5 + ').jpg')
82. .objectFit(ImageFit.Fill)
83. .width('100%')
84. .layoutWeight(1)
85. }
86. }
87. .width('100%')
88. .height(this.itemHeightArray[item % 100])
89. .backgroundColor(this.colors[item % this.colors.length])
90. }, (item: string) => item)
91. }
92. .columnsTemplate('1fr 1fr')    // 设置2列等宽布局
93. .columnsGap(10)
94. .rowsGap(5)
95. .backgroundColor(0xFAEEE0)
96. .width('100%')
97. .height('100%')
98. .itemConstraintSize({minWidth:80,maxWidth:180,minHeight:80,maxHeight:180})
99. // 触底加载数据：滚动到底部时触发分页加载
100. .onReachEnd(() => {
101. console.info('onReachEnd')

103. // 模拟分页加载：当数据超过200条时停止加载
104. if (this.dataSource.totalCount() > 200) {
105. this.footerState = FooterState.End;
106. return;
107. }
108. setTimeout(() => {
109. for (let i = 0; i < 100; i++) {
110. this.dataSource.addLastItem();
111. }
112. }, 1000)
113. })
114. .onReachStart(() => {
115. // 滚动到顶部时触发
116. console.info('waterFlow reach start');
117. })
118. .onScrollStart(() => {
119. // 开始滚动时触发
120. console.info('waterFlow scroll start');
121. })
122. .onScrollStop(() => {
123. // 停止滚动时触发
124. console.info('waterFlow scroll stop');
125. })
126. .onScrollFrameBegin((offset: number, state: ScrollState) => {
127. // 滚动帧开始时触发：可以控制滚动行为
128. // offset：滚动偏移量，state：滚动状态
129. console.info('waterFlow scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
130. return { offsetRemain: offset };  // 返回开发者期望的实际滚动偏移量
131. })
132. }
133. }
134. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/FS_y3DioS0qLBaD8iYFqmw/zh-cn_image_0000002583439691.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=B186ADF6EC0BB9DB2070FCA3B560F8B2C98D1081BF249E123DF23BF885A23B34)

### 示例2（自动计算列数）

该示例通过auto-fill实现了自动计算列数的效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. @State minSize: number = 80;
8. @State maxSize: number = 180;
9. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
10. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
11. private itemWidthArray: number[] = [];
12. private itemHeightArray: number[] = [];

14. // 计算FlowItem宽/高
15. getSize() {
16. let ret = Math.floor(Math.random() * this.maxSize);
17. return (ret > this.minSize ? ret : this.minSize);
18. }

20. // 设置FlowItem宽/高数组
21. setItemSizeArray() {
22. for (let i = 0; i < 100; i++) {
23. this.itemWidthArray.push(this.getSize());
24. this.itemHeightArray.push(this.getSize());
25. }
26. }

28. // 组件生命周期：在组件即将出现时初始化尺寸数组
29. aboutToAppear() {
30. this.setItemSizeArray();
31. }

33. build() {
34. Column({ space: 2 }) {
35. WaterFlow() {
36. LazyForEach(this.dataSource, (item: number) => {
37. FlowItem() {
38. Column() {
39. Text('N' + item).fontSize(12).height('16')
40. // 存在对应的jpg文件才会显示图片
41. Image('res/waterFlowTest(' + item % 5 + ').jpg')
42. }
43. }
44. .width('100%')
45. .height(this.itemHeightArray[item % 100])
46. .backgroundColor(this.colors[item % this.colors.length])
47. }, (item: string) => item)
48. }
49. // auto-fill自动计算列数
50. // 'repeat(auto-fill,80)' 表示：根据容器宽度自动计算能放下多少个80px宽的列
51. // 例如：容器宽度400px，则自动计算为5列（400÷80=5）
52. .columnsTemplate('repeat(auto-fill,80)')
53. .columnsGap(10)
54. .rowsGap(5)
55. .padding({left:5})
56. .backgroundColor(0xFAEEE0)
57. .width('100%')
58. .height('100%')
59. }
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Iop1IktzSPSRfUyKCeCEFg/zh-cn_image_0000002552959646.png?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=A5EA9323B99C1D65E50BFC84219F8568EB74F1AB4C01E21443CA43C38C6E5298)

### 示例3（使用分组）

该示例展示了分组的初始化以及splice、push、update、values、length等接口的不同效果。

如果配合状态管理V2使用，详情见：[WaterFlow与makeObserved](../harmonyos-guides/arkts-v1-v2-migration-inner-object.md#滚动组件)。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. // 可复用组件：优化性能，减少组件创建销毁开销
5. @Reusable
6. @Component
7. struct ReusableFlowItem {
8. @State item: number = 0;

10. // 组件复用生命周期：从复用缓存中取出时调用
11. // 用于更新组件状态，显示新的内容
12. aboutToReuse(params: Record<string, number>) {
13. this.item = params.item;
14. console.info('Reuse item:' + this.item);
15. }

17. // 组件生命周期：初始化尺寸数组和分组配置
18. aboutToAppear() {
19. console.info('new item:' + this.item);
20. }

22. build() {
23. Column() {
24. // 注意：需要确保对应的jpg文件存在才会正常显示
25. Image('res/waterFlowTest(' + this.item % 5 + ').jpg')
26. .overlay('N' + this.item, { align: Alignment.Top })
27. .objectFit(ImageFit.Fill)
28. .width('100%')
29. .layoutWeight(1)
30. }
31. }
32. }

34. @Entry
35. @Component
36. struct WaterFlowDemo {
37. minSize: number = 80;
38. maxSize: number = 180;
39. colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
40. scroller: Scroller = new Scroller();
41. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
42. dataCount: number = this.dataSource.totalCount();
43. private itemWidthArray: number[] = [];
44. private itemHeightArray: number[] = [];
45. // 分组管理：WaterFlow的核心特性，支持不同区域使用不同列数
46. @State sections: WaterFlowSections = new WaterFlowSections();
47. // 分组边距配置：统一的外边距设置
48. sectionMargin: Margin = { top: 10, left: 5, bottom: 10, right: 5 };

50. oneColumnSection: SectionOptions = {
51. itemsCount: 4,                     // 该分组包含4个FlowItem
52. crossCount: 1,                     // 使用1列布局
53. columnsGap: '5vp',
54. rowsGap: 10,
55. margin: this.sectionMargin,
56. // 回调函数：动态设置每个item的高度
57. onGetItemMainSizeByIndex: (index: number) => {
58. return this.itemHeightArray[index % 100];
59. }
60. };

62. // 第二种分组：双列布局，适合展示列表内容
63. twoColumnSection: SectionOptions = {
64. itemsCount: 2,                     // 该分组包含2个FlowItem
65. crossCount: 2,                     // 使用2列布局
66. // 回调函数：固定高度100px
67. onGetItemMainSizeByIndex: (index: number) => {
68. return 100;
69. }
70. };

72. // 最后一个分组：用于处理剩余数据
73. lastSection: SectionOptions = {
74. itemsCount: 20,                    // 该分组包含20个FlowItem
75. crossCount: 2,                     // 使用2列布局
76. // 回调函数：使用随机高度
77. onGetItemMainSizeByIndex: (index: number) => {
78. return this.itemHeightArray[index % 100];
79. }
80. };

82. // 计算FlowItem高度
83. getSize() {
84. let ret = Math.floor(Math.random() * this.maxSize);
85. return (ret > this.minSize ? ret : this.minSize);
86. }

88. // 设置FlowItem的高度数组
89. setItemSizeArray() {
90. for (let i = 0; i < 100; i++) {
91. this.itemHeightArray.push(this.getSize());
92. }
93. }

95. // 组件生命周期：初始化数据和恢复上次的列数设置
96. aboutToAppear() {
97. this.setItemSizeArray();

99. // 初始化瀑布流分组信息：交替使用单列和双列布局
100. let sectionOptions: SectionOptions[] = [];
101. let count = 0;                     // 已分配的FlowItem数量计数
102. let oneOrTwo = 0;                  // 用于交替选择分组类型

104. while (count < this.dataCount) {
105. // 剩余数据不足20个时，使用最后一个分组处理
106. if (this.dataCount - count < 20) {
107. this.lastSection.itemsCount = this.dataCount - count;
108. sectionOptions.push(this.lastSection);
109. break;
110. }

112. // 交替使用单列和双列布局
113. if (oneOrTwo++ % 2 == 0) {
114. sectionOptions.push(this.oneColumnSection);
115. count += this.oneColumnSection.itemsCount;
116. } else {
117. sectionOptions.push(this.twoColumnSection);
118. count += this.twoColumnSection.itemsCount;
119. }
120. }

122. // 将配置好的分组添加到WaterFlow中
123. this.sections.splice(0, 0, sectionOptions);
124. }

126. build() {
127. Column({ space: 2 }) {
128. Row() {
129. Button('splice')
130. .height('5%')
131. .onClick(() => {
132. // 重要：必须保证LazyForEach中数据数量和新分组itemsCount累计总数保持一致
133. let totalCount: number = this.dataSource.totalCount();
134. let newSection: SectionOptions = {
135. itemsCount: totalCount,
136. crossCount: 2,
137. onGetItemMainSizeByIndex: (index: number) => {
138. return this.itemHeightArray[index % 100];
139. }
140. };
141. let oldLength: number = this.sections.length();
142. this.sections.splice(0, oldLength, [newSection]);  // 替换所有分组
143. })
144. .margin({ top: 10, left: 20 })

146. Button('update')
147. .height('5%')
148. .onClick(() => {
149. // 在第一个分组中增加4个FlowItem
150. // 重要：必须保证数据源和分组itemsCount同步更新
151. const sections: Array<SectionOptions> = this.sections.values();
152. let newSection: SectionOptions = sections[0];

154. // 先在数据源中添加4个新数据
155. this.dataSource.addItem(this.oneColumnSection.itemsCount);
156. this.dataSource.addItem(this.oneColumnSection.itemsCount + 1);
157. this.dataSource.addItem(this.oneColumnSection.itemsCount + 2);
158. this.dataSource.addItem(this.oneColumnSection.itemsCount + 3);

160. // 然后更新分组的itemsCount
161. newSection.itemsCount += 4;
162. const result: boolean = this.sections.update(0, newSection);
163. console.info('update:' + result);
164. })
165. .margin({ top: 10, left: 20 })

167. Button('delete')
168. .height('5%')
169. .onClick(() => {
170. // 在第一个分组中减少4个FlowItem
171. // 重要：必须保证数据源和分组itemsCount同步更新
172. const sections: Array<SectionOptions> = this.sections.values();
173. let newSection: SectionOptions = sections[0];

175. // 检查是否有足够的item可以删除
176. if (newSection.itemsCount < 4) {
177. return;
178. }

180. // 先从数据源中删除4条数据
181. this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 1);
182. this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 2);
183. this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 3);
184. this.dataSource.deleteItem(this.oneColumnSection.itemsCount - 4);

186. // 更新分组的itemsCount
187. newSection.itemsCount -= 4;
188. this.sections.update(0, newSection);
189. })
190. .margin({ top: 10, left: 20 })

192. Button('values')
193. .height('5%')
194. .onClick(() => {
195. const sections: Array<SectionOptions> = this.sections.values();
196. for (const value of sections) {
197. console.info(JSON.stringify(value));
198. }
199. console.info('count:' + this.sections.length());
200. })
201. .margin({ top: 10, left: 20 })
202. }.margin({ bottom: 20 })

204. WaterFlow({ scroller: this.scroller, sections: this.sections }) {
205. LazyForEach(this.dataSource, (item: number) => {
206. FlowItem() {
207. // 使用可复用组件，提升性能
208. ReusableFlowItem({ item: item })
209. }
210. .width('100%')
211. // 注意：同时设置onGetItemMainSizeByIndex和height属性时，
212. // 主轴大小以onGetItemMainSizeByIndex返回结果为准
213. .height(this.itemHeightArray[item % 100])
214. .backgroundColor(this.colors[item % this.colors.length])
215. }, (item: string) => item)
216. }
217. .columnsTemplate('1fr 1fr')
218. .columnsGap(10)
219. .rowsGap(5)
220. .backgroundColor(0xFAEEE0)
221. .width('100%')
222. .height('100%')
223. .layoutWeight(1)
224. .onScrollIndex((first: number, last: number) => {
225. // 滚动监听：即将触底时提前加载更多数据
226. if (last + 20 >= this.dataSource.totalCount()) {
227. // 添加100个新数据到数据源
228. for (let i = 0; i < 100; i++) {
229. this.dataSource.addLastItem();
230. }

232. // 重要：更新数据源后必须同步更新sections
233. // 修改最后一个section的FlowItem数量
234. const sections: Array<SectionOptions> = this.sections.values();
235. let newSection: SectionOptions = sections[this.sections.length() - 1];
236. newSection.itemsCount += 100;
237. this.sections.update(-1, newSection);  // -1表示最后一个分组
238. }
239. })
240. }
241. }
242. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Yk8B1FyPQPCLXrFGSfbk3A/zh-cn_image_0000002583479647.png?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=C78B6F749F59E6F55574EA4F55FCBD629858EDEF3E1D430C5216F69628AAA53A)

### 示例4（双指缩放改变列数）

该示例通过[priorityGesture](ts-gesture-settings.md#prioritygesture)和[PinchGesture](ts-basic-gestures-pinchgesture.md)实现了双指缩放改变列数效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';
3. import { image } from '@kit.ImageKit';

5. // 可复用组件：优化性能，减少组件创建销毁开销
6. @Reusable
7. @Component
8. struct ReusableFlowItem {
9. @State item: number = 0;

11. // 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
12. aboutToReuse(params: Record<string, number>) {
13. this.item = params.item;
14. }

16. build() {
17. Column() {
18. Text('N' + this.item).fontSize(12).height('16')
19. // 注意：需要确保对应的jpg文件存在才会正常显示
20. Image('res/waterFlow(' + this.item % 5 + ').jpg')
21. .objectFit(ImageFit.Fill)
22. .width('100%')
23. .layoutWeight(1)
24. }
25. }
26. }

28. @Entry
29. @Component
30. struct WaterFlowDemo {
31. minSize: number = 80;
32. maxSize: number = 180;
33. colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
34. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
35. private itemWidthArray: number[] = [];
36. private itemHeightArray: number[] = [];
37. @State columns: number = 2;
38. @State waterFlowScale: number = 1;
39. @State imageScale: number = 1;
40. @State waterFlowOpacity: number = 1;
41. @State waterFlowSnapshot: image.PixelMap | undefined = undefined;
42. private columnChanged: boolean = false;
43. private oldColumn: number = this.columns;
44. private pinchTime: number = 0;

46. // 计算FlowItem宽/高
47. getSize() {
48. let ret = Math.floor(Math.random() * this.maxSize);
49. return (ret > this.minSize ? ret : this.minSize);
50. }

52. // 设置FlowItem的宽/高数组
53. setItemSizeArray() {
54. for (let i = 0; i < 100; i++) {
55. this.itemWidthArray.push(this.getSize());
56. this.itemHeightArray.push(this.getSize());
57. }
58. }

60. // 组件生命周期：初始化数据和恢复上次的列数设置
61. aboutToAppear() {
62. // 读取上次最后切换到的列数
63. let lastCount = AppStorage.get<number>('columnsCount');
64. if (typeof lastCount != 'undefined') {
65. this.columns = lastCount;
66. }
67. this.setItemSizeArray();
68. }

70. // 根据缩放阈值改变列数，触发WaterFlow重新布局
71. changeColumns(scale: number) {
72. if (scale > (this.columns / (this.columns - 0.5)) && this.columns > 1) {
73. this.columns--;
74. this.columnChanged = true;
75. } else if (scale < 1 && this.columns < 4) {
76. this.columns++;
77. this.columnChanged = true;
78. }
79. }

81. build() {
82. Column({ space: 2 }) {
83. Row() {
84. Text('双指缩放改变列数')
85. .height('5%')
86. .margin({ top: 10, left: 20 })
87. }

89. Stack() {
90. // 用于展示缩放前的WaterFlow截图
91. Image(this.waterFlowSnapshot)
92. .width('100%')
93. .height('100%')
94. .scale({
95. x: this.imageScale,
96. y: this.imageScale,
97. centerX: 0,
98. centerY: 0
99. })

101. WaterFlow() {
102. LazyForEach(this.dataSource, (item: number) => {
103. FlowItem() {
104. // 使用可复用组件，提升性能
105. ReusableFlowItem({ item: item })
106. }
107. .width('100%')
108. .aspectRatio(this.itemHeightArray[item % 100] / this.itemWidthArray[item%100])
109. .backgroundColor(this.colors[item % this.colors.length])
110. }, (item: string) => item)
111. }
112. .id('waterflow') // 设置id用于截图
113. .columnsTemplate('1fr '.repeat(this.columns))  // 动态生成列模板，如：'1fr 1fr 1fr'表示3列等宽
114. .backgroundColor(0xFAEEE0)
115. .width('100%')
116. .height('100%')
117. .layoutWeight(1)
118. .opacity(this.waterFlowOpacity)
119. .scale({
120. x: this.waterFlowScale,
121. y: this.waterFlowScale,
122. centerX: 0,
123. centerY: 0
124. })
125. .priorityGesture(
126. PinchGesture()
127. .onActionStart((event: GestureEvent) => {
128. // 双指捏合手势识别成功时截图
129. this.pinchTime = event.timestamp;
130. this.columnChanged = false;
131. this.oldColumn = this.columns;
132. this.getUIContext().getComponentSnapshot().get('waterflow', (error: Error, pixmap: image.PixelMap) => {
133. if (error) {
134. console.info('error:' + JSON.stringify(error));
135. return;
136. }
137. this.waterFlowSnapshot = pixmap;
138. })
139. })
140. .onActionUpdate((event: GestureEvent) => {
141. // 手势更新：处理缩放逻辑和视觉效果
142. // 边界限制：防止超出列数范围时继续缩放
143. if ((this.oldColumn === 1 && event.scale > 1) || (this.oldColumn === 4 && event.scale < 1)) {
144. return;
145. }

147. // 节流处理：避免过于频繁的更新，提升性能
148. if (event.timestamp - this.pinchTime < 10000000) {
149. return;
150. }
151. this.pinchTime = event.timestamp;

153. this.waterFlowScale = event.scale;
154. this.imageScale = event.scale;
155. // 根据缩放比例设置WaterFlow透明度
156. this.waterFlowOpacity = (this.waterFlowScale > 1) ? (this.waterFlowScale - 1) : (1 - this.waterFlowScale);
157. this.waterFlowOpacity *= 3;
158. if (!this.columnChanged) {
159. this.changeColumns(event.scale);
160. }

162. // 列数改变后的缩放比例调整：避免出现空白区域
163. if (this.columnChanged) {
164. this.waterFlowScale = this.imageScale * this.columns / this.oldColumn;

166. // 限制缩放范围，确保视觉效果自然
167. if (event.scale < 1) {
168. this.waterFlowScale = this.waterFlowScale > 1 ? this.waterFlowScale : 1;
169. } else {
170. this.waterFlowScale = this.waterFlowScale < 1 ? this.waterFlowScale : 1;
171. }
172. }
173. })
174. .onActionEnd((event: GestureEvent) => {
175. // 手势结束：执行归位动画并保存状态
176. // 执行归位动画：平滑过渡到正常状态
177. this.getUIContext()?.animateTo({ duration: 300 }, () => {
178. this.waterFlowScale = 1;
179. this.waterFlowOpacity = 1;
180. })

182. // 持久化保存当前列数：下次启动时恢复
183. AppStorage.setOrCreate<number>('columnsCount', this.columns);
184. })
185. )
186. }
187. }
188. }
189. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/lNU28ZfORoyImUuCjkRWRA/zh-cn_image_0000002552799998.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=0FA0823B612080858A46B0DE5539A0B71019C7A24B4CF5D83D054918CB11559F)

### 示例5（设置边缘渐隐效果）

该示例通过[fadingEdge](ts-container-scrollable-common.md#fadingedge14)实现了WaterFlow组件开启边缘渐隐效果，并通过fadingEdgeLength参数设置边缘渐隐长度。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { WaterFlowDataSource } from './WaterFlowDataSource';

5. @Entry
6. @Component
7. struct WaterFlowDemo {
8. @State minSize: number = 80;
9. @State maxSize: number = 180;
10. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
11. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
12. scroller: Scroller = new Scroller();
13. private itemWidthArray: number[] = [];
14. private itemHeightArray: number[] = [];

16. // 计算FlowItem宽/高
17. getSize() {
18. let ret = Math.floor(Math.random() * this.maxSize);
19. return (ret > this.minSize ? ret : this.minSize);
20. }

22. // 设置FlowItem宽/高数组
23. setItemSizeArray() {
24. for (let i = 0; i < 100; i++) {
25. this.itemWidthArray.push(this.getSize());
26. this.itemHeightArray.push(this.getSize());
27. }
28. }

30. // 组件生命周期：在组件即将出现时初始化尺寸数组
31. aboutToAppear() {
32. this.setItemSizeArray();
33. }

35. build() {
36. Column({ space: 2 }) {
37. WaterFlow({ scroller: this.scroller }) {
38. LazyForEach(this.dataSource, (item: number) => {
39. FlowItem() {
40. Column() {
41. Text('N' + item).fontSize(12).height('16')
42. }
43. }
44. .width('100%')
45. .height(this.itemHeightArray[item % 100])
46. .backgroundColor(this.colors[item % 5])
47. }, (item: string) => item)
48. }
49. // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
50. .columnsTemplate('repeat(auto-fill,80)')
51. .columnsGap(10)
52. .rowsGap(5)
53. .height('90%')
54. .scrollBar(BarState.On)
55. // 边缘渐隐效果：在滚动边缘创建渐隐过渡效果
56. // true：启用渐隐效果
57. // fadingEdgeLength: LengthMetrics.vp(80)：渐隐区域长度为80vp
58. // 效果：在瀑布流顶部和底部边缘会有80vp的渐隐过渡区域
59. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/yBbBO2ZbSH6uLmVqvbjbqA/zh-cn_image_0000002583439693.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=DB0B5FA95318DA3189E4B0B8DC6699F94DE55761B846C33930D626E56F3A1E3E)

### 示例6（单边边缘效果）

该示例通过[edgeEffect](ts-container-scrollable-common.md#edgeeffect11)接口，实现了WaterFlow组件设置单边边缘效果。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. @State minSize: number = 80;
8. @State maxSize: number = 180;
9. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
10. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
11. scroller: Scroller = new Scroller();
12. private itemWidthArray: number[] = [];
13. private itemHeightArray: number[] = [];

15. // 计算FlowItem宽/高
16. getSize() {
17. let ret = Math.floor(Math.random() * this.maxSize);
18. return (ret > this.minSize ? ret : this.minSize);
19. }

21. // 设置FlowItem宽/高数组
22. setItemSizeArray() {
23. for (let i = 0; i < 100; i++) {
24. this.itemWidthArray.push(this.getSize());
25. this.itemHeightArray.push(this.getSize());
26. }
27. }

29. // 组件生命周期：在组件即将出现时初始化尺寸数组
30. aboutToAppear() {
31. this.setItemSizeArray();
32. }

34. build() {
35. Column({ space: 2 }) {
36. WaterFlow({ scroller: this.scroller }) {
37. LazyForEach(this.dataSource, (item: number) => {
38. FlowItem() {
39. Column() {
40. Text('N' + item).fontSize(12).height('16')
41. }
42. }
43. .width('100%')
44. .height(this.itemHeightArray[item % 100])
45. .backgroundColor(this.colors[item % 5])
46. }, (item: number) => item.toString())
47. }
48. // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
49. .columnsTemplate('repeat(auto-fill,80)')
50. .columnsGap(10)
51. .rowsGap(5)
52. .height('90%')
53. // 单边边缘效果：设置弹簧效果，仅在顶部生效
54. // EdgeEffect.Spring：弹簧回弹效果，滑动到边界时会有弹性回弹
55. // alwaysEnabled: true：始终启用边缘效果，即使内容不足以滚动
56. // effectEdge: EffectEdge.START：仅在起始边缘（顶部）生效
57. // 效果：只有向上滑动到顶部时才会有弹簧回弹效果，向下滑动到底部不会有效果
58. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })

60. }
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/JmFePQlzQj6ymjsaTUhdMw/zh-cn_image_0000002552959648.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=6E8BA8CE00BA51FF574294DCC8286F70BB806ABDC160E14ABF0B4029CB51F62D)

### 示例7（WaterFlow组件设置和改变尾部组件）

从API version 18开始，该示例通过[WaterFlowOptions对象说明](ts-container-waterflow.md#waterflowoptions对象说明)的footerContent接口，实现了WaterFlow组件设置尾部组件。通过[ComponentContent](js-apis-arkui-componentcontent.md)的update函数更新尾部组件。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { ComponentContent, UIContext } from '@kit.ArkUI';
3. import { WaterFlowDataSource } from './WaterFlowDataSource';

5. class Params {
6. text: string = '';

8. constructor(text: string) {
9. this.text = text;
10. }
11. }

13. // Builder函数：构建尾部组件的UI结构
14. @Builder
15. function buildText(params: Params) {
16. Column() {
17. Text(params.text)
18. .fontSize(20)
19. .fontWeight(FontWeight.Bold)
20. .margin(20)
21. }
22. }

24. @Entry
25. @Component
26. struct Index {
27. @State message1: string = '已经到底了';
28. @State message2: string = '加载更多';
29. @State colors: number[] = [0xD5D5D5, 0x7F7F7F, 0xF7F7F7];
30. @State minSize: number = 80;
31. @State maxSize: number = 180;

33. // UI上下文：用于创建ComponentContent
34. context: UIContext = this.getUIContext();

36. // 动态尾部组件：使用ComponentContent创建可更新的尾部组件
37. // ComponentContent<Params>：泛型指定参数类型
38. // wrapBuilder<[Params]>(buildText)：包装Builder函数
39. // new Params(this.message1)：初始参数，显示'已经到底了'
40. footerContent: ComponentContent<Params> = new ComponentContent<Params>(
41. this.context,
42. wrapBuilder<[Params]>(buildText),
43. new Params(this.message1)
44. );

46. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
47. private itemWidthArray: number[] = [];
48. private itemHeightArray: number[] = [];

50. // 计算FlowItem宽/高
51. getSize() {
52. let ret = Math.floor(Math.random() * this.maxSize);
53. return (ret > this.minSize ? ret : this.minSize);
54. }

56. // 设置FlowItem宽/高数组
57. setItemSizeArray() {
58. for (let i = 0; i < 100; i++) {
59. this.itemWidthArray.push(this.getSize());
60. this.itemHeightArray.push(this.getSize());
61. }
62. }

64. // 组件生命周期：在组件即将出现时初始化尺寸数组
65. aboutToAppear() {
66. this.setItemSizeArray();
67. }

69. build() {
70. Row() {
71. Column() {
72. Button('更新footer').width('90%').margin(20)
73. .onClick((event?: ClickEvent) => {
74. // 调用ComponentContent的update方法更新尾部组件
75. // 传入新的Params对象，文本内容从'已经到底了'变为'加载更多'
76. this.footerContent.update(new Params(this.message2));
77. })
78. WaterFlow({ footerContent: this.footerContent }) {
79. LazyForEach(this.dataSource, (item: number) => {
80. FlowItem() {
81. Column() {
82. Text('N' + item).fontSize(12).height('16')
83. }
84. .width('100%')
85. .height(this.itemHeightArray[item % 100])
86. .backgroundColor(this.colors[item % 3])
87. .justifyContent(FlexAlign.Center)
88. .alignItems(HorizontalAlign.Center)
89. }
90. }, (item: number) => item.toString())
91. }
92. .columnsTemplate('1fr')
93. .height('90%')
94. }
95. .width('100%')
96. .height('100%')
97. }
98. .height('100%')
99. }
100. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/67XacB7BQXe0QFzf6BVBOw/zh-cn_image_0000002583479649.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=5C343BAD403BE89F43CAD3CD73B73EE79C11A97C9F02624729F61A2ACA3440AB)

### 示例8（WaterFlow组件实现下拉刷新）

该示例通过[Refresh](ts-container-refresh.md)组件和WaterFlow组件，实现了下拉刷新瀑布流组件数据源。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. @State minSize: number = 80;
8. @State maxSize: number = 180;
9. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
10. @State isRefreshing: boolean = false;
11. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
12. scroller: Scroller = new Scroller();
13. private itemWidthArray: number[] = [];
14. private itemHeightArray: number[] = [];

16. // 计算FlowItem宽/高
17. getSize() {
18. let ret = Math.floor(Math.random() * this.maxSize);
19. return (ret > this.minSize ? ret : this.minSize);
20. }

22. // 设置FlowItem宽/高数组
23. setItemSizeArray() {
24. for (let i = 0; i < 100; i++) {
25. this.itemWidthArray.push(this.getSize());
26. this.itemHeightArray.push(this.getSize());
27. }
28. }

30. // 组件生命周期：在组件即将出现时初始化尺寸数组
31. aboutToAppear() {
32. this.setItemSizeArray();
33. }

35. build() {
36. Column({ space: 2 }) {
37. // refreshing: $$this.isRefreshing：双向绑定刷新状态
38. Refresh({ refreshing: $$this.isRefreshing }) {
39. WaterFlow({ scroller: this.scroller }) {
40. LazyForEach(this.dataSource, (item: number) => {
41. FlowItem() {
42. Column() {
43. Text('N' + item).fontSize(12).height('16')
44. }
45. }
46. .width('100%')
47. .height(this.itemHeightArray[item % 100])
48. .backgroundColor(this.colors[item % this.colors.length])
49. }, (item: number) => item.toString())
50. }
51. // auto-fill自动计算列数：根据容器宽度自动计算能放下多少个80px宽的列
52. .columnsTemplate('repeat(auto-fill,80)')
53. .columnsGap(10)
54. .rowsGap(5)
55. .height('90%')
56. // 边缘效果：弹簧回弹效果
57. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
58. .onReachEnd(() => {
59. // 触底加载更多数据：滚动到底部时触发
60. setTimeout(() => {
61. this.dataSource.addNewItems(100);
62. }, 1000)
63. })
64. }
65. .onStateChange((refreshStatus: RefreshStatus) => {
66. // 刷新状态变化监听：处理不同的刷新状态
67. if (refreshStatus === RefreshStatus.Done) {
68. // 刷新完成时：调用数据源的刷新方法，更新所有数据
69. this.dataSource.refreshItems();
70. }
71. })
72. .onRefreshing(() => {
73. // 正在刷新时的回调：模拟刷新过程
74. setTimeout(() => {
75. this.isRefreshing = false;
76. }, 1000)
77. })
78. }
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/cP51EweVToGhOyF5BethuQ/zh-cn_image_0000002552800000.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=4BD38D72ECA6EE78D11EB86A1BEF2E434B89432944506CE11182820D087643A9)

### 示例9（WaterFlow组件基于断点配置列数）

从API version 22开始，该示例展示了WaterFlow组件支持基于断点配置列数效果。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. minSize: number = 80;
8. maxSize: number = 180;
9. colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
10. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
11. private itemHeightArray: number[] = [];

13. // 计算FlowItem宽/高
14. getSize() {
15. let ret = Math.floor(Math.random() * this.maxSize);
16. return (ret > this.minSize ? ret : this.minSize);
17. }

19. // 设置FlowItem的宽/高数组
20. setItemSizeArray() {
21. for (let i = 0; i < 100; i++) {
22. this.itemHeightArray.push(this.getSize());
23. }
24. }

26. // 组件生命周期：在组件即将出现时初始化尺寸数组
27. aboutToAppear() {
28. this.setItemSizeArray();
29. }

31. build() {
32. Column({ space: 2 }) {
33. WaterFlow() {
34. LazyForEach(this.dataSource, (item: number) => {
35. FlowItem() {
36. Column() {
37. Text('N' + item).fontSize(12).height('16')
38. // 注意：需要确保对应的jpg文件存在才会正常显示
39. Image('res/waterFlowTest(' + item % 5 + ').jpg')
40. .objectFit(ImageFit.Fill)
41. .width('100%')
42. .layoutWeight(1)
43. }
44. }
45. .width('100%')
46. .height(this.itemHeightArray[item % 100])
47. .backgroundColor(this.colors[item % this.colors.length])
48. }, (item: string) => item)
49. }
50. .key('waterFlow')
51. // 设置WaterFlow按断点决定列数
52. .columnsTemplate({fillType:PresetFillType.BREAKPOINT_SM2MD3LG5})
53. .columnsGap(10)
54. .rowsGap(5)
55. .backgroundColor(0xFAEEE0)
56. .margin('20vp')
57. .width('100%')
58. .height('30%')
59. }
60. }
61. }
```

WaterFlow宽度属于sm及更小的断点区间时显示2列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/i2rjCnUvSgOJ47YvHAnoSQ/zh-cn_image_0000002583439695.png?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=49EE4FFBA098488C337646FF473655DBCC59AC51F3D7510E13B8756B4868B69E)

WaterFlow宽度属于md断点区间时显示3列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/4oNoN8kHSNSRh21N6S9V3g/zh-cn_image_0000002552959650.png?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=CEC1EAD4C4CB443A0E258E8F52BFDCC0E37399818A678942FB0312DA57DA02DD)

WaterFlow宽度属于lg及更大的断点区间时显示5列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/po_APs-bTO2-wVf3mFzFgg/zh-cn_image_0000002583479651.png?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=B2E66CF184DE6DE109B1565E2F18F019498C0B39DB0DBB85C9C23326869074B1)

### 示例10（WaterFlow组件实现获取内容高度）

从API version 22 开始，该示例通过WaterFlow组件，实现了获取内容高度。

WaterFlowDataSource说明及完整代码参考[示例1使用基本瀑布流](ts-container-waterflow.md#示例1使用基本瀑布流)。

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WaterFlowContentSizeDemo {
8. @State minSize: number = 80;
9. @State maxSize: number = 180;
10. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
11. @State contentWidth: number = -1;
12. @State contentHeight: number = -1;
13. scroller: Scroller = new Scroller();
14. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
15. private itemWidthArray: number[] = [];
16. private itemHeightArray: number[] = [];

18. // 计算FlowItem宽/高
19. getSize() {
20. let ret = Math.floor(Math.random() * this.maxSize);
21. return (ret > this.minSize ? ret : this.minSize);
22. }

24. // 设置FlowItem的宽/高数组
25. setItemSizeArray() {
26. for (let i = 0; i < 100; i++) {
27. this.itemWidthArray.push(this.getSize());
28. this.itemHeightArray.push(this.getSize());
29. }
30. }

32. // 组件生命周期：在组件即将出现时初始化尺寸数组
33. aboutToAppear() {
34. this.setItemSizeArray();
35. }

37. @Builder
38. itemFoot() {
39. Column() {
40. Text(`到底啦...`)
41. .fontSize(10)
42. .backgroundColor(Color.Red)
43. .width(50)
44. .height(50)
45. .align(Alignment.Center)
46. .margin({ top: 2 })
47. }
48. }

50. build() {
51. Column({ space: 2 }) {
52. // 点击按钮来调用contentSize函数获取内容尺寸
53. Button('GetContentSize')
54. .onClick(() => {
55. // Scroller未绑定组件时会抛异常，需要加上try catch保护
56. try {
57. // 通过调用contentSize函数获取内容尺寸的宽度值
58. this.contentWidth = this.scroller.contentSize().width;
59. // 通过调用contentSize函数获取内容尺寸的高度值
60. this.contentHeight = this.scroller.contentSize().height;
61. } catch (error) {
62. let err: BusinessError = error as BusinessError;
63. console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
64. }
65. }).margin(5)
66. // 将获取到的内容尺寸信息通过文本进行呈现
67. Text('Width:' + this.contentWidth)
68. .fontColor(Color.Red)
69. .height(30)
70. Text('Height:' + this.contentHeight)
71. .fontColor(Color.Red)
72. .height(30)

74. WaterFlow({ scroller: this.scroller, footer: this.itemFoot() }) {
75. LazyForEach(this.dataSource, (item: number) => {
76. FlowItem() {
77. Column() {
78. Text('N' + item).fontSize(12).height('16')
79. }
80. }
81. .width('100%')
82. .height(this.itemHeightArray[item % 100])
83. .backgroundColor(this.colors[item % this.colors.length])
84. }, (item: string) => item)
85. }
86. .columnsTemplate('1fr 1fr') // 设置2列等宽布局
87. .columnsGap(10)
88. .rowsGap(5)
89. .backgroundColor(0xFAEEE0)
90. .width('100%')
91. .height('80%')
92. }
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/gCskqZJvRau1bZobt0cNsw/zh-cn_image_0000002552800002.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000130Z&HW-CC-Expire=86400&HW-CC-Sign=E318E49D2A558F85D173E5D49E558434513174A863178663FBE4FACB6370B4B8)

### 示例11（设置滚动事件）

该示例通过FrameNode中的[getEvent('WaterFlow')](js-apis-arkui-framenode.md#geteventwaterflow19)获取[UIWaterFlowEvent](ts-container-waterflow.md#uiwaterflowevent19)，并为WaterFlow设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UIWaterFlowEvent接口。

```
1. import { NodeController, FrameNode, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. public rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);
8. this.rootNode.commonAttribute.width(100);
9. return this.rootNode;
10. }

12. addCommonEvent(frameNode: FrameNode) {
13. // 获取WaterFlow事件
14. let waterFlowEvent: UIWaterFlowEvent | undefined = typeNode.getEvent(frameNode, 'WaterFlow');

16. // 设置OnWillScroll事件
17. waterFlowEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
18. console.info('onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}');
19. });

21. // 设置OnDidScroll事件
22. waterFlowEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
23. console.info('onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}');
24. });

26. // 设置OnReachStart事件
27. waterFlowEvent?.setOnReachStart(() => {
28. console.info('onReachStart');
29. });

31. // 设置OnReachEnd事件
32. waterFlowEvent?.setOnReachEnd(() => {
33. console.info('onReachEnd');
34. });

36. // 设置OnScrollStart事件
37. waterFlowEvent?.setOnScrollStart(() => {
38. console.info('onScrollStart');
39. });

41. // 设置OnScrollStop事件
42. waterFlowEvent?.setOnScrollStop(() => {
43. console.info('onScrollStop');
44. });

46. // 设置OnScrollFrameBegin事件
47. waterFlowEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
48. console.info('onScrollFrameBegin offset = ${offset}, state = ${state}');
49. return undefined;
50. });

52. // 设置OnScrollIndex事件
53. waterFlowEvent?.setOnScrollIndex((first: number, last: number) => {
54. console.info('onScrollIndex start = ${first}, end = ${last}');
55. });
56. }
57. }

59. @Entry
60. @Component
61. struct Index {
62. @State index: number = 0;
63. private myNodeController: MyNodeController = new MyNodeController();
64. @State numbers: string[] = [];
65. @State heights: number[] = [];

67. aboutToAppear() {
68. for (let i = 0; i < 30; i++) {
69. this.numbers.push('${i+1}');
70. this.heights.push(70 + Math.floor(Math.random() * 60));
71. }
72. }

74. build() {
75. Column() {
76. Button('add CommonEvent to WaterFlow')
77. .onClick(() => {
78. this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!)
79. })
80. WaterFlow() {
81. ForEach(this.numbers, (day: string, index: number) => {
82. FlowItem() {
83. Text(day)
84. .fontSize(16)
85. .backgroundColor(0xF9CF93)
86. .width('100%')
87. .height(this.heights[index])
88. .textAlign(TextAlign.Center)
89. }
90. .width('100%')
91. }, (day: string, index: number) => index.toString() + day)
92. }
93. .columnsTemplate('1fr 1fr')
94. .columnsGap(10)
95. .rowsGap(10)
96. .enableScrollInteraction(true)
97. .width('90%')
98. .backgroundColor(0xFAEEE0)
99. .height(300)
100. NodeContainer(this.myNodeController)
101. }.width('100%')
102. }
103. }
```
