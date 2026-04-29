---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid
title: Grid
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > Grid
category: harmonyos-references
scraped_at: 2026-04-29T13:51:46+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:1c5f61dad74c742aadc46e3273b8e2c19f34095a26c0c9926733407deac0bbc5
---

网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](ts-gesture-blocking-enhancement.md)进行处理。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持[GridItem](ts-container-griditem.md)子组件和自定义组件。自定义组件在Grid下使用时，建议使用GridItem作为自定义组件的顶层组件，不建议给自定义组件设置属性和事件方法。

支持通过渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

说明

Grid子组件的索引值计算规则：

按子组件的顺序依次递增。

if/else语句中，只有条件成立分支内的子组件会参与索引值计算，条件不成立分支内的子组件不计算索引值。

ForEach/LazyForEach和Repeat语句中，会计算展开所有子组件索引值。

[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)发生变化以后，会更新子组件索引值。

Grid子组件的visibility属性设置为Hidden或None时依然会计算索引值。

Grid子组件的visibility属性设置为None时不显示，但依然会占用子组件对应的网格。

Grid子组件设置position属性，会占用子组件对应的网格，子组件将显示在相对Grid左上角偏移position的位置。该子组件不会随其对应网格滚动，在对应网格滑出Grid显示范围外后不显示。

当Grid子组件之间留有空隙时，会根据当前的展示区域尽可能填补空隙，因此GridItem可能会随着网格滚动而改变相对位置。

从API version 21开始，Grid单个子组件的宽高最大为16777216px；API version 20及之前，Grid单个子组件的宽高最大为1000000px。子组件超出该大小可能导致滚动或显示异常。

## 接口

PhonePC/2in1TabletTVWearable

Grid(scroller?: Scroller, layoutOptions?: GridLayoutOptions)

创建网格容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 可滚动组件的控制器。用于与可滚动组件进行绑定。  **说明：**  不允许和其他滚动类组件，如：[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)和[WaterFlow](ts-container-waterflow.md)绑定同一个滚动控制对象。 |
| layoutOptions10+ | [GridLayoutOptions](ts-container-grid.md#gridlayoutoptions10对象说明) | 否 | Grid布局选项。 |

## GridLayoutOptions10+对象说明

PhonePC/2in1TabletTVWearable

Grid布局选项。其中，irregularIndexes和onGetIrregularSizeByIndex可对仅设置rowsTemplate或columnsTemplate的Grid使用，可以指定一个index数组，并为其中的index对应的GridItem设置其占据的行数与列数，使用方法参见[示例3](ts-container-grid.md#示例3可滚动grid设置跨行跨列节点)；onGetRectByIndex可对同时设置rowsTemplate和columnsTemplate的Grid使用，为指定的index对应的GridItem设置位置和大小，使用方法参见[示例1](ts-container-grid.md#示例1固定行列grid)。

为提高Grid在跳转、列数变化等场景的性能，应该尽量使用GridLayoutOptions。即使Grid中没有任何特殊的跨行跨列节点，也可以通过使用'Grid(this.scroller, {regularSize: [1, 1]})'的方式提高跳转性能。参考[优化Grid组件加载慢丢帧问题](../best-practices/bpta-improve_grid_performance.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| regularSize | [number, number] | 否 | 否 | 大小规则的GridItem在Grid中占的行数和列数，只支持占1行1列即[1, 1]。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| irregularIndexes | number[] | 否 | 是 | 指定索引的GridItem在Grid中的大小是不规则的。当不设置onGetIrregularSizeByIndex时，irregularIndexes中GridItem的默认大小为垂直滚动Grid的一整行或水平滚动Grid的一整列。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onGetIrregularSizeByIndex | (index: number) => [number, number] | 否 | 是 | 配合irregularIndexes使用，设置不规则GridItem占用的行数和列数。开发者可为irregularIndexes中指明的index对应的GridItem设置占用的行数和列数。在API version 12之前，垂直滚动Grid不支持GridItem占多行，水平滚动Grid不支持GridItem占多列。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onGetRectByIndex11+ | (index: number) => [number, number,number,number] | 否 | 是 | 设置指定索引index对应的GridItem的位置及大小[rowStart,columnStart,rowSpan,columnSpan]。  其中rowStart为行起始位置，columnStart为列起始位置，无单位。  rowSpan为GridItem占用的行数，columnSpan为GridItem占用的列数，无单位。  rowStart和columnStart取大于等于0的自然数，若取负数时，rowStart和columnStart默认为0。  rowSpan和columnSpan取大于等于1的自然数，若取小数则向下取整，若小于1则按1计算。  **说明：**  第一种情况：某个GridItem发现给它指定的起始位置被占据了，则从起始位置[0,0]开始按顺序从左到右，从上到下寻找起始的放置位置。  第二种情况：如果起始位置没有被占据，但其他位置被占据了，无法显示全部的GridItem大小，则只会布局一部分。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)和[滚动组件通用属性](ts-container-scrollable-common.md#属性)外，还支持以下属性：

说明

Grid组件使用通用属性[clip12+](ts-universal-attributes-sharp-clipping.md#clip12)和通用属性[clip18+](ts-universal-attributes-sharp-clipping.md#clip18)时默认值都为true。

设置Grid的padding后，如果子组件部分位于Grid内容区且部分位于padding区域内，则会显示；如果子组件完全位于padding区域内，则不会显示。如下图所示，GridItem1显示，而GridItem2不显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/nMnnl5KqQSaGhERNh-AtTw/zh-cn_image_0000002589245951.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=F3DFF0B90EC8DD633D7A9559EB861899F378BA4A09495ADA37143555DC50E2B1)

### columnsTemplate

PhonePC/2in1TabletTVWearable

columnsTemplate(value: string)

设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如， '1fr 1fr 2fr' 是将父组件分3列，将父组件允许的宽分为4等份，第1列占1份，第2列占1份，第3列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用columnsGap作为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效列宽。

auto-fit模式和auto-stretch模式只支持track-size为一个有效列宽值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效列宽，如columnsTemplate('repeat(auto-fill, 20)')、columnsTemplate('repeat(auto-fill, 20 80px)')。

使用效果可以参考[示例8](ts-container-grid.md#示例8设置自适应列数)。

设置为'0fr'时，该列的列宽为0，不显示GridItem。设置为其他非法值时，GridItem显示为固定1列。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局列的数量或最小列宽值。 |

### columnsTemplate22+

PhonePC/2in1TabletTVWearable

columnsTemplate(value: string | ItemFillPolicy)

设置当前网格组件布局列的数量，不设置时默认1列。

当value设置为string类型时，使用方法参考[columnsTemplate(value: string)](ts-container-grid.md#columnstemplate)。

当value设置为ItemFillPolicy类型时，将根据Grid组件宽度对应[断点类型](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)确定列数。

例如，ItemFillPolicy.BREAKPOINT\_DEFAULT在组件宽度属于sm及更小的断点区间时显示2列，属于md断点区间时显示3列，属于lg及更大的断点区间时显示5列，且每列均为1fr。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [ItemFillPolicy](ts-types.md#itemfillpolicy22) | 是 | 当前网格组件布局列的数量。 |

### rowsTemplate

PhonePC/2in1TabletTVWearable

rowsTemplate(value: string)

设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。

例如， '1fr 1fr 2fr'是将父组件分3行，将父组件允许的高分为4等份，第1行占1份，第2行占1份，第3行占2份。

rowsTemplate('repeat(auto-fit, track-size)')是设置最小行高值为track-size，自动计算行数和实际行高。

rowsTemplate('repeat(auto-fill, track-size)')是设置固定行高值为track-size，自动计算行数。

rowsTemplate('repeat(auto-stretch, track-size)')是设置固定行高值为track-size，使用rowsGap为最小行间距，自动计算行数和实际行间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为行高，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效行高。

auto-fit模式和auto-stretch模式只支持track-size为一个有效行高值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效行高，如rowsTemplate('repeat(auto-fill, 20)')、rowsTemplate('repeat(auto-fill, 20 80px)')。

设置为'0fr'，则这一行的行高为0，这一行GridItem不显示。设置为其他非法值，按固定1行处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局行的数量或最小行高值。 |

说明

Grid组件根据rowsTemplate、columnsTemplate属性的设置情况，可分为以下三种布局模式：

1、rowsTemplate、columnsTemplate同时设置：

* Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。
* 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cellLength。
* Grid的宽高没有设置时，默认适应父组件尺寸。
* Grid网格列大小按照Grid自身内容区域大小减去所有行列Gap后按各个行列所占比重分配。
* GridItem默认填满网格大小。

2、rowsTemplate、columnsTemplate仅设置其中的一个：

* 元素按照设置的方向进行排布，超出Grid显示区域后，Grid可通过滚动的方式展示。
* 如果设置了columnsTemplate，Grid滚动方向为垂直方向，主轴方向为垂直方向，交叉轴方向为水平方向。
* 如果设置了rowsTemplate，Grid滚动方向为水平方向，主轴方向为水平方向，交叉轴方向为垂直方向。
* 此模式下以下属性不生效：layoutDirection、maxCount、minCount、cellLength。
* 网格交叉轴方向尺寸根据Grid自身内容区域交叉轴尺寸减去交叉轴方向所有Gap后按所占比重分配。
* 网格主轴方向尺寸取当前网格交叉轴方向所有GridItem主轴方向尺寸最大值。
* 此模式下GridItem交叉轴方向尺寸与网格一致，可以通过设置[constraintSize](ts-universal-attributes-size.md#constraintsize)中的maxWidth或maxHeight限制GridItem交叉轴方向尺寸小于网格。

3、rowsTemplate、columnsTemplate都不设置：

* 元素在layoutDirection方向上排布，列数由Grid的宽度、首个元素的宽度、minCount、maxCount、columnsGap共同决定。
* 行数由Grid高度、首个元素高度、cellLength、rowsGap共同决定。超出行列容纳范围的元素不显示，也不能通过滚动进行展示。
* 此模式下仅生效以下属性：layoutDirection、maxCount、minCount、cellLength、editMode、columnsGap、rowsGap。
* 当前layoutDirection设置为Row时，先从左到右排列，排满一行再排下一行。剩余高度不足时不再布局，整体内容顶部居中。
* 当前layoutDirection设置为Column时，先从上到下排列，排满一列再排下一列，剩余宽度不足时不再布局。整体内容顶部居中。
* 当前Grid下面没有GridItem时，Grid的宽高为0。

### columnsGap

PhonePC/2in1TabletTVWearable

columnsGap(value: Length)

设置列与列的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 列与列的间距。  默认值：0  取值范围：[0, +∞) |

### rowsGap

PhonePC/2in1TabletTVWearable

rowsGap(value: Length)

设置行与行的间距。设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 行与行的间距。  默认值：0  取值范围：[0, +∞) |

### scrollBar

PhonePC/2in1TabletTVWearable

scrollBar(value: BarState)

设置滚动条状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BarState](ts-appendix-enums.md#barstate) | 是 | 滚动条状态。  默认值：BarState.Auto  **说明：**  API version 9及以下版本默认值为BarState.Off，API version 10及以上版本的默认值为BarState.Auto。 |

### scrollBarColor

PhonePC/2in1TabletTVWearable

scrollBarColor(value: Color | number | string)

设置滚动条的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](ts-appendix-enums.md#color) | number | string | 是 | 滚动条的颜色。  默认值：'#182431'（40%不透明度）  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。  string为rgb或者argb格式颜色，示例：'#ffffff'。 |

### scrollBarColor22+

PhonePC/2in1TabletTVWearable

scrollBarColor(color: Color | number | string | Resource)

设置滚动条的颜色。与[scrollBarColor](ts-container-grid.md#scrollbarcolor)相比， 参数名改为color，并开始支持Resource类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource) | 是 | 滚动条的颜色。  默认值：'#182431'（40%不透明度）  number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

### scrollBarWidth

PhonePC/2in1TabletTVWearable

scrollBarWidth(value: number | string)

设置滚动条的宽度，不支持百分比设置。宽度设置后，滚动条正常状态和按压状态宽度均为滚动条的宽度值。如果滚动条的宽度超过Grid组件主轴方向的高度，则滚动条的宽度会变为默认值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 滚动条的宽度。  默认值：4  单位：vp  取值范围：设置为小于0的值时，按默认值处理。设置为0时，不显示滚动条。 |

### cachedCount

PhonePC/2in1TabletTVWearable

cachedCount(value: number)

设置预加载的GridItem的数量，只在[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和开启了[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)开关的[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)中生效。

设置缓存后会在Grid显示区域上下各缓存cachedCount\*列数个GridItem。

[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和开启了[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)开关的[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)超出显示和缓存范围的GridItem会被释放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 预加载的GridItem的数量。  默认值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。  通过状态变量单独更新value值时，Grid组件不会触发布局更新，缓存节点数量仅会在下次布局时更新。 |

### cachedCount14+

PhonePC/2in1TabletTVWearable

cachedCount(count: number, show: boolean)

设置预加载的GridItem数量，并配置是否显示预加载节点。

设置缓存后会在Grid显示区域上下各缓存cachedCount\*列数个GridItem。配合[裁剪](ts-universal-attributes-sharp-clipping.md#clip12)或[内容裁剪](ts-container-scrollable-common.md#clipcontent14)属性可以显示出预加载节点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 预加载的GridItem的数量。  默认值：垂直滚动时为一个屏幕内可显示的行数，水平滚动时为一个屏幕内可显示的列数，最大值为16。  取值范围：[0, +∞)，设置为小于0的值时，按1处理。  通过状态变量单独更新count值时，Grid组件不会触发布局更新，缓存节点数量仅会在下次布局时更新。 |
| show | boolean | 是 | 被预加载的GridItem是否需要显示。设置为true时显示预加载的GridItem，设置为false时不显示预加载的GridItem。  默认值：false |

### editMode8+

PhonePC/2in1TabletTVWearable

editMode(value: boolean)

设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部[GridItem](ts-container-griditem.md)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | Grid是否进入编辑模式。设置为true时当前Grid组件处于可编辑模式，设置为false时当前Grid组件处于不可编辑模式。  默认值：false |

### layoutDirection8+

PhonePC/2in1TabletTVWearable

layoutDirection(value: GridDirection)

设置布局的主轴方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GridDirection](ts-container-grid.md#griddirection8枚举说明) | 是 | 布局的主轴方向。  默认值：GridDirection.Row |

### maxCount8+

PhonePC/2in1TabletTVWearable

maxCount(value: number)

设置可显示的最大行数或列数。设置为小于1的值时，按默认值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最大列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最大行数。

当maxCount小于minCount时，maxCount和minCount都按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 可显示的最大行数或列数。  默认值：Infinity |

### minCount8+

PhonePC/2in1TabletTVWearable

minCount(value: number)

设置可显示的最小行数或列数。设置为小于1的值时，按默认值显示。

当layoutDirection是Row/RowReverse时，表示可显示的最小列数。

当layoutDirection是Column/ColumnReverse时，表示可显示的最小行数。

当minCount大于maxCount时，minCount和maxCount都按默认值处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 可显示的最小行数或列数。  默认值：1 |

### cellLength8+

PhonePC/2in1TabletTVWearable

cellLength(value: number)

设置一行的高度或者一列的宽度。

当layoutDirection是Row/RowReverse时，表示一行的高度。

当layoutDirection是Column/ColumnReverse时，表示一列的宽度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 一行的高度或者一列的宽度。  默认值：第一个元素的大小  单位：vp  取值范围：(0, +∞)，设置为小于等于0的值时，按默认值显示。 |

### multiSelectable8+

PhonePC/2in1TabletTVWearable

multiSelectable(value: boolean)

设置是否开启鼠标框选。开启框选后，可以配合GridItem的selected属性和onSelect事件获取GridItem的选中状态，还可以通过[多态样式](ts-universal-attributes-polymorphic-style.md)设置GridItem的选中态样式（GridItem默认无选中态样式）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启鼠标框选。  默认值：false  false：关闭框选。true：开启框选。 |

### supportAnimation8+

PhonePC/2in1TabletTVWearable

supportAnimation(value: boolean)

设置是否支持动画。当前支持GridItem拖拽动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。

仅在大小规则的Grid中支持拖拽动画，跨行或跨列场景不支持。

supportAnimation动画效果参考[示例5（Grid拖拽场景）](ts-container-grid.md#示例5grid拖拽场景)，其他动画效果需要应用自定义拖拽实现。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持动画。设置为true时支持GridItem拖拽动画，设置为false时不支持GridItem拖拽动画。  默认值：false |

### edgeEffect10+

PhonePC/2in1TabletTVWearable

edgeEffect(value: EdgeEffect, options?: EdgeEffectOptions)

设置边缘滑动效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [EdgeEffect](ts-appendix-enums.md#edgeeffect) | 是 | Grid组件的边缘滑动效果，支持弹簧效果和阴影效果。  默认值：EdgeEffect.None |
| options11+ | [EdgeEffectOptions](ts-container-scrollable-common.md#edgeeffectoptions11对象说明) | 否 | 组件内容大小小于组件自身时，是否开启滑动效果。设置为{ alwaysEnabled: true }会开启滑动效果，{ alwaysEnabled: false }不开启。  默认值：{ alwaysEnabled: false } |

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

设置嵌套滚动选项。设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。当组件内容大小小于组件自身，且[edgeEffect](ts-container-grid.md#edgeeffect10)的options为{ alwaysEnabled: false }时，组件自身滑动手势不会触发，嵌套滚动属性不会生效，如果其父滚动组件有滑动手势，则会触发父组件的滑动手势。

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

### alignItems12+

PhonePC/2in1TabletTVWearable

alignItems(alignment: Optional<GridItemAlignment>)

设置Grid中GridItem的对齐方式， 使用方法可以参考[示例9](ts-container-grid.md#示例9以当前行最高的griditem的高度为其他griditem的高度)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignment | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[GridItemAlignment](ts-container-grid.md#griditemalignment12枚举说明)> | 是 | 设置Grid中GridItem的对齐方式。  默认值：GridItemAlignment.DEFAULT |

### focusWrapMode20+

PhonePC/2in1TabletTVWearable

focusWrapMode(mode: Optional<FocusWrapMode>)

设置交叉轴方向键走焦模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[FocusWrapMode](ts-appendix-enums.md#focuswrapmode20)> | 是 | 交叉轴方向键走焦模式。  默认值：FocusWrapMode.DEFAULT  **说明：**  异常值按默认值处理，即交叉轴方向键不能换行。 |

### syncLoad20+

PhonePC/2in1TabletTVWearable

syncLoad(enable: boolean)

设置是否同步加载Grid区域内所有子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否同步加载Grid区域内所有子组件。  true表示同步加载，false表示异步加载。默认值：true。  **说明：**  设置为false时，在首次显示、不带动画scrollToIndex跳转场景，若当帧布局耗时超过50ms，会将Grid区域内尚未布局的子组件延后到下一帧进行布局。 |

### supportEmptyBranchInLazyLoading23+

PhonePC/2in1TabletTVWearable

supportEmptyBranchInLazyLoading(supported: boolean | undefined)

设置当前Grid组件是否支持在LazyForEach或Repeat中使用if/else渲染控制语法生成不包含任何子组件的空分支节点。未设置时不支持空分支节点。此属性初次赋值后不支持更新，所以赋值后无法在支持空分支、不支持空分支行为之间切换。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | undefined | 是 | 当前Grid组件是否支持在[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)或[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)中使用[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)渲染控制语法生成一个不含任何子节点的空分支节点。  true表示支持空分支节点；false表示不支持空分支节点。  值为undefined时，按false处理。 |

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

## GridItemAlignment12+枚举说明

PhonePC/2in1TabletTVWearable

GridItem的对齐方式枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 使用Grid的默认对齐方式。 |
| STRETCH | 1 | 以一行中的最高的GridItem作为其他GridItem的高度。 |

说明

1、只有可滚动的Grid中，设置STRETCH参数会生效，其他场景不生效。

2、在Grid的一行中，如果每个GridItem都是大小规律的（只占一行一列），设置STRETCH参数会生效，存在跨行或跨列的GridItem的场景不生效。

3、设置STRETCH后，只有不设置高度的GridItem才会以当前行中最高的GridItem作为自己的高度，设置过高度的GridItem高度不会变化。

4、设置STRETCH后，Grid布局时会有额外的布局流程，可能会带来额外的性能开销。

## GridDirection8+枚举说明

PhonePC/2in1TabletTVWearable

主轴布局方向枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Row | 0 | 主轴布局方向沿水平方向布局，即自左往右先填满一行，再去填下一行。 |
| Column | 1 | 主轴布局方向沿垂直方向布局，即自上往下先填满一列，再去填下一列。 |
| RowReverse | 2 | 主轴布局方向沿水平方向反向布局，即自右往左先填满一行，再去填下一行。 |
| ColumnReverse | 3 | 主轴布局方向沿垂直方向反向布局，即自下往上先填满一列，再去填下一列。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)和[滚动组件通用事件](ts-container-scrollable-common.md#事件)外，还支持以下事件：

### onScrollIndex

PhonePC/2in1TabletTVWearable

onScrollIndex(event: (first: number, last: number) => void)

当前网格显示的起始位置/终止位置的item发生变化时触发。网格初始化时会触发一次。Grid显示区域上第一个子组件/最后一个组件的索引值有变化就会触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的网格起始位置的索引值。 |
| last10+ | number | 是 | 当前显示的网格终止位置的索引值。 |

### onItemDragStart8+

PhonePC/2in1TabletTVWearable

onItemDragStart(event: OnItemDragStartCallback)

开始拖拽网格元素时触发。

手指长按GridItem时触发该事件。

由于拖拽检测也需要长按，且事件处理机制优先触发子组件事件，GridItem上绑定[LongPressGesture](ts-basic-gestures-longpressgesture.md#longpressgesture-1)时无法触发拖拽。如有长按和拖拽同时使用的需求可以使用通用拖拽事件。

拖拽浮起的网格元素可在应用窗口内移动，若需限制移动范围，可通过自定义手势实现，具体参考[示例16（实现GridItem自定义拖拽）](ts-container-grid.md#示例16实现griditem自定义拖拽)。

不支持拖动到Grid边缘时自动滚动，可使用通用拖拽实现，具体参考[示例17（通过拖拽事件实现griditem拖拽）](ts-container-grid.md#示例17通过拖拽事件实现griditem拖拽)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnItemDragStartCallback](ts-container-scrollable-common.md#onitemdragstartcallback23) | 是 | 网格元素拖拽开始时触发的回调。  API version 22及之前版本，该参数类型为(event: ItemDragInfo, itemIndex: number) => (() => any) | void，其中event和itemIndex参数含义参考[OnItemDragStartCallback](ts-container-scrollable-common.md#onitemdragstartcallback23)。 |

### onItemDragEnter8+

PhonePC/2in1TabletTVWearable

onItemDragEnter(event: (event: ItemDragInfo) => void)

拖拽进入网格元素范围内时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |

### onItemDragMove8+

PhonePC/2in1TabletTVWearable

onItemDragMove(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number) => void)

拖拽在网格元素范围内移动时触发。

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

拖拽离开网格元素时触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽离开的网格元素索引值。 |

### onItemDrop8+

PhonePC/2in1TabletTVWearable

onItemDrop(event: (event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => void)

绑定该事件的网格元素可作为拖拽释放目标，当GridItem停止拖拽时触发。

当拖拽释放位置在网格元素之内时，isSuccess会返回true；在网格元素之外时，isSuccess会返回false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ItemDragInfo](ts-container-scrollable-common.md#itemdraginfo对象说明) | 是 | 拖拽点的信息。 |
| itemIndex | number | 是 | 拖拽起始位置。 |
| insertIndex | number | 是 | 拖拽插入位置。 |
| isSuccess | boolean | 是 | 拖拽释放位置是否在设置了onItemDrop的网格元素之内。  true：表示拖拽释放位置在设置了onItemDrop的网格元素之内；false：表示拖拽释放位置在设置了onItemDrop的网格元素之外。 |

### onScrollBarUpdate10+

PhonePC/2in1TabletTVWearable

onScrollBarUpdate(event: (index: number, offset: number) => ComputedBarAttribute)

在Grid每帧布局结束时触发，可通过该回调设置滚动条的位置及长度。

该接口只用作设置Grid的滚动条位置，不建议开发者在此接口中做业务逻辑处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前显示的网格起始位置的索引值。 |
| offset | number | 是 | 当前显示的网格起始位置元素相对网格显示起始位置的偏移，单位vp。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ComputedBarAttribute](ts-container-grid.md#computedbarattribute10对象说明) | 滚动条的位置及长度。 |

### onReachStart10+

PhonePC/2in1TabletTVWearable

onReachStart(event: () => void)

网格到达起始位置时触发。

Grid初始化时会触发一次，Grid滚动到起始位置时触发一次。Grid边缘效果为弹簧效果时，划动经过起始位置时触发一次，回弹回起始位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格到达起始位置时触发的回调。 |

### onReachEnd10+

PhonePC/2in1TabletTVWearable

onReachEnd(event: () => void)

网格到达末尾位置时触发。不满一屏并且最后一个子组件末端在Grid内时触发。

Grid边缘效果为弹簧效果时，划动经过末尾位置时触发一次，回弹回末尾位置时再触发一次。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格到达末尾位置时触发的回调。 |

### onScrollFrameBegin10+

PhonePC/2in1TabletTVWearable

onScrollFrameBegin(event: OnScrollFrameBeginCallback)

该接口回调时，事件参数传入即将发生的滑动量，事件处理函数中可根据应用场景计算实际需要的滑动量并作为事件处理函数的返回值返回，网格将按照返回值的实际滑动量进行滑动。

满足以下任一条件时触发该事件：

1. 用户交互（如手指滑动、键鼠操作等）触发滚动。
2. Grid惯性滚动。
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

### onScrollStart10+

PhonePC/2in1TabletTVWearable

onScrollStart(event: () => void)

网格滑动开始时触发。手指拖动网格或网格的滚动条触发的滑动开始时，会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画开始时会触发该事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格滑动开始时触发的回调。 |

### onScrollStop10+

PhonePC/2in1TabletTVWearable

onScrollStop(event: () => void)

网格滑动停止时触发。手指拖动网格或网格的滚动条触发的滑动，手指离开屏幕后滑动停止时会触发该事件。使用[Scroller](ts-container-scroll.md#scroller)滑动控制器触发的带动画的滑动，动画停止会触发该事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 网格滑动停止时触发的回调。 |

### onScroll(deprecated)

PhonePC/2in1TabletTVWearable

onScroll(event: (scrollOffset: number, scrollState: [ScrollState](ts-container-list.md#scrollstate枚举说明)) => void)

网格滑动时触发。

说明

从API version 10开始支持，从API version 12开始废弃，建议使用[onDidScroll](ts-container-scrollable-common.md#ondidscroll12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scrollOffset | number | 是 | 相对于上一帧的偏移量，Grid的内容向上滚动时偏移量为正，向下滚动时偏移量为负。  单位vp。 |
| scrollState | [ScrollState](ts-container-list.md#scrollstate枚举说明) | 是 | 当前滑动状态。 |

## ComputedBarAttribute10+对象说明

PhonePC/2in1TabletTVWearable

滚动条位置和长度对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| totalOffset | number | 否 | 否 | Grid内容相对显示区域的总偏移，单位px。 |
| totalLength | number | 否 | 否 | Grid内容总长度，单位px。 |

## UIGridEvent19+

PhonePC/2in1TabletTVWearable

frameNode中[getEvent('Grid')](js-apis-arkui-framenode.md#geteventgrid19)方法的返回值，可用于给Grid节点设置滚动事件。

UIGridEvent继承于[UIScrollableCommonEvent](ts-container-scrollable-common.md#uiscrollablecommonevent19)。

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

setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void

设置[onScrollIndex](ts-container-grid.md#onscrollindex)事件的回调。

方法入参为undefined时，会重置事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnGridScrollIndexCallback](ts-container-grid.md#ongridscrollindexcallback19) | undefined | 是 | onScrollIndex事件的回调函数。 |

## OnGridScrollIndexCallback19+

PhonePC/2in1TabletTVWearable

type OnGridScrollIndexCallback = (first: number, last: number) => void

Grid组件可见区域item变化事件的回调类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| first | number | 是 | 当前显示的Grid起始位置的索引值。 |
| last | number | 是 | 当前显示的Grid终止位置的索引值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（固定行列Grid）

可以使用[GridLayoutOptions](ts-container-grid.md#gridlayoutoptions10对象说明)中的onGetRectByIndex指定GridItem的位置和大小。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridExample {
5. @State numbers1: string[] = ['0', '1', '2', '3', '4'];
6. @State numbers2: string[] = ['0', '1', '2', '3', '4', '5'];
7. layoutOptions3: GridLayoutOptions = {
8. regularSize: [1, 1],
9. onGetRectByIndex: (index: number) => {
10. if (index == 0) {
11. return [0, 0, 1, 1];
12. } else if (index == 1) {
13. return [0, 1, 2, 2];
14. } else if (index == 2) {
15. return [0, 3, 3, 3];
16. } else if (index == 3) {
17. return [3, 0, 3, 3];
18. } else if (index == 4) {
19. return [4, 3, 2, 2];
20. } else {
21. return [5, 5, 1, 1];
22. }
23. }
24. };

26. build() {
27. Column({ space: 5 }) {
28. Grid() {
29. ForEach(this.numbers1, (day: string) => {
30. ForEach(this.numbers1, (day: string) => {
31. GridItem() {
32. Text(day)
33. .fontSize(16)
34. .backgroundColor(0xF9CF93)
35. .width('100%')
36. .height('100%')
37. .textAlign(TextAlign.Center)
38. }
39. }, (day: string) => day)
40. }, (day: string) => day)
41. }
42. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
43. .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
44. .columnsGap(10)
45. .rowsGap(10)
46. .width('90%')
47. .backgroundColor(0xFAEEE0)
48. .height(300)

50. Text('GridLayoutOptions的使用：onGetRectByIndex。').fontColor(0x000000).fontSize(14).width('90%')

52. Grid(undefined, this.layoutOptions3) {
53. ForEach(this.numbers2, (day: string) => {
54. GridItem() {
55. Text(day)
56. .fontSize(16)
57. .backgroundColor(0xF9CF93)
58. .width('100%')
59. .height('100%')
60. .textAlign(TextAlign.Center)
61. }
62. .height('100%')
63. .width('100%')
64. }, (day: string) => day)
65. }
66. .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
67. .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
68. .columnsGap(10)
69. .rowsGap(10)
70. .width('90%')
71. .backgroundColor(0xFAEEE0)
72. .height(300)
73. }.width('100%').margin({ top: 5 })
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/BqBOBP48QjiQOsZCb0LnMg/zh-cn_image_0000002558766142.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=3446837A9B331E9B735E6CA6A31A7585F277CA67A2AF4B779A25ED712B6B9D20)

### 示例2（可滚动Grid和滚动事件）

可滚动Grid，包括所有滚动属性和事件。

GridDataSource实现了LazyForEach数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给Grid提供子组件。

```
1. // GridDataSource.ets
2. export class GridDataSource implements IDataSource {
3. private list: string[] = [];
4. private listeners: DataChangeListener[] = [];

6. constructor(list: string[]) {
7. this.list = list;
8. }

10. totalCount(): number {
11. return this.list.length;
12. }

14. getData(index: number): string {
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

31. // 通知控制器数据位置变化
32. notifyDataMove(from: number, to: number): void {
33. this.listeners.forEach(listener => {
34. listener.onDataMove(from, to);
35. })
36. }

38. // 重新加载所有数据
39. notifyDataReload(): void {
40. this.listeners.forEach(listener => {
41. listener.onDataReloaded();
42. })
43. }

45. // 交换元素位置
46. public swapItem(from: number, to: number): void {
47. let temp: string = this.list[from];
48. this.list[from] = this.list[to];
49. this.list[to] = temp;
50. this.notifyDataReload()
51. }
52. }
```

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource([]);
8. scroller: Scroller = new Scroller();
9. @State gridPosition: number = 0; // 0代表滚动到grid顶部，1代表中间值，2代表滚动到grid底部。

11. aboutToAppear() {
12. let list: string[] = [];
13. for (let i = 0; i < 5; i++) {
14. for (let j = 0; j < 5; j++) {
15. list.push(j.toString());
16. }
17. }
18. this.numbers = new GridDataSource(list);
19. }

21. build() {
22. Column({ space: 5 }) {
23. Text('Grid').fontColor(0x000000).fontSize(16).width('90%')
24. Grid(this.scroller) {
25. LazyForEach(this.numbers, (day: string) => {
26. GridItem() {
27. Text(day)
28. .fontSize(16)
29. .backgroundColor(0xF9CF93)
30. .width('100%')
31. .height(80)
32. .textAlign(TextAlign.Center)
33. }
34. }, (index: number) => index.toString())
35. }
36. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
37. .columnsGap(10)
38. .rowsGap(10)
39. .friction(0.6)
40. .enableScrollInteraction(true)
41. .supportAnimation(false)
42. .multiSelectable(false)
43. .edgeEffect(EdgeEffect.Spring)
44. .scrollBar(BarState.On)
45. .scrollBarColor(Color.Grey)
46. .scrollBarWidth(4)
47. .width('90%')
48. .backgroundColor(0xFAEEE0)
49. .height(300)
50. .onScrollIndex((first: number, last: number) => {
51. console.info(first.toString());
52. console.info(last.toString());
53. })
54. .onScrollBarUpdate((index: number, offset: number) => {
55. console.info('XXX' + 'Grid onScrollBarUpdate,index : ' + index.toString() + ',offset' + offset.toString());
56. return { totalOffset: (index / 5) * (80 + 10) - offset, totalLength: 80 * 5 + 10 * 4 };
57. })  // 只适用于当前示例代码数据源，如果数据源有变化，则需要修改该部分代码，或者删掉此属性
58. .onDidScroll((scrollOffset: number, scrollState: ScrollState) => {
59. console.info(scrollOffset.toString());
60. console.info(scrollState.toString());
61. })
62. .onScrollStart(() => {
63. console.info('XXX' + 'Grid onScrollStart');
64. })
65. .onScrollStop(() => {
66. console.info('XXX' + 'Grid onScrollStop');
67. })
68. .onReachStart(() => {
69. this.gridPosition = 0;
70. console.info('XXX' + 'Grid onReachStart');
71. })
72. .onReachEnd(() => {
73. this.gridPosition = 2;
74. console.info('XXX' + 'Grid onReachEnd');
75. })

77. Button('next page')
78. .onClick(() => { // 点击后滑到下一页
79. this.scroller.scrollPage({ next: true });
80. })
81. }.width('100%').margin({ top: 5 })
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/LjDytHOiRN6uDADrynbKzA/zh-cn_image_0000002558606484.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=EFD64923C412C59165DF74A9ED2DAF7E563570F5B9B226E2FE434991C817D2F6)

### 示例3（可滚动Grid设置跨行跨列节点）

[GridLayoutOptions](ts-container-grid.md#gridlayoutoptions10对象说明)的使用：irregularIndexes与onGetIrregularSizeByIndex。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource([]);
8. scroller: Scroller = new Scroller();
9. layoutOptions1: GridLayoutOptions = {
10. regularSize: [1, 1],        // 只支持[1, 1]
11. irregularIndexes: [0, 6],   // 索引为0和6的GridItem占用一行
12. };

14. layoutOptions2: GridLayoutOptions = {
15. regularSize: [1, 1],
16. irregularIndexes: [0, 7],   // 索引为0和7的GridItem占用的列数由onGetIrregularSizeByIndex指定
17. onGetIrregularSizeByIndex: (index: number) => {
18. if (index === 0) {
19. return [1, 5];
20. }
21. return [1, index % 6 + 1];
22. }
23. };

25. aboutToAppear() {
26. let list: string[] = [];
27. for (let i = 0; i < 5; i++) {
28. for (let j = 0; j < 5; j++) {
29. list.push(j.toString());
30. }
31. }
32. this.numbers = new GridDataSource(list);
33. }

35. build() {
36. Column({ space: 5 }) {
37. Text('Grid1').fontColor(0x000000).fontSize(16).width('90%')
38. Grid(this.scroller, this.layoutOptions1) {
39. LazyForEach(this.numbers, (day: string) => {
40. GridItem() {
41. Text(day)
42. .fontSize(16)
43. .backgroundColor(0xF9CF93)
44. .width('100%')
45. .height(80)
46. .textAlign(TextAlign.Center)
47. }.selectable(false)
48. }, (index: number) => index.toString())
49. }
50. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
51. .columnsGap(10)
52. .rowsGap(10)
53. .multiSelectable(true)
54. .scrollBar(BarState.Off)
55. .width('90%')
56. .backgroundColor(0xFAEEE0)
57. .height(300)

59. Text('Grid2').fontColor(0x000000).fontSize(16).width('90%')
60. // 不使用scroll，需要undefined占位
61. Grid(undefined, this.layoutOptions2) {
62. LazyForEach(this.numbers, (day: string) => {
63. GridItem() {
64. Text(day)
65. .fontSize(16)
66. .backgroundColor(0xF9CF93)
67. .width('100%')
68. .height(80)
69. .textAlign(TextAlign.Center)
70. }
71. }, (index: number) => index.toString())
72. }
73. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
74. .columnsGap(10)
75. .rowsGap(10)
76. .scrollBar(BarState.Off)
77. .width('90%')
78. .backgroundColor(0xFAEEE0)
79. .height(300)
80. }.width('100%').margin({ top: 5 })
81. }
82. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/eaNSS4dZQ3yidSuhKaZgCQ/zh-cn_image_0000002589326011.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=6563BDEAB0E500F10D7183E6491463E729138AA43EFCF8EDD6BFED1C9104CAB3)

### 示例4（Grid嵌套滚动）

[nestedScroll](ts-container-grid.md#nestedscroll10)和[onScrollFrameBegin](ts-container-grid.md#onscrollframebegin10)的使用。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';

3. @Entry
4. @Component
5. struct GridExample {
6. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
7. numbers: GridDataSource = new GridDataSource([]);
8. @State translateY: number = 0;
9. private scroller: Scroller = new Scroller();
10. private gridScroller: Scroller = new Scroller();
11. private touchDown: boolean = false;
12. private listTouchDown: boolean = false;
13. private scrolling: boolean = false;

15. aboutToAppear() {
16. let list: string[] = [];
17. for (let i = 0; i < 100; i++) {
18. list.push(i.toString());
19. }
20. this.numbers = new GridDataSource(list);
21. }

23. build() {
24. Stack() {
25. Column() {
26. Row() {
27. Text('Head')
28. }

30. Column() {
31. List({ scroller: this.scroller }) {
32. ListItem() {
33. Grid() {
34. GridItem() {
35. Text('GoodsTypeList1')
36. }
37. .backgroundColor(this.colors[0])
38. .columnStart(0)
39. .columnEnd(1)

41. GridItem() {
42. Text('GoodsTypeList2')
43. }
44. .backgroundColor(this.colors[1])
45. .columnStart(0)
46. .columnEnd(1)

48. GridItem() {
49. Text('GoodsTypeList3')
50. }
51. .backgroundColor(this.colors[2])
52. .columnStart(0)
53. .columnEnd(1)

55. GridItem() {
56. Text('GoodsTypeList4')
57. }
58. .backgroundColor(this.colors[3])
59. .columnStart(0)
60. .columnEnd(1)

62. GridItem() {
63. Text('GoodsTypeList5')
64. }
65. .backgroundColor(this.colors[4])
66. .columnStart(0)
67. .columnEnd(1)
68. }
69. .scrollBar(BarState.Off)
70. .columnsGap(15)
71. .rowsGap(10)
72. .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
73. .columnsTemplate('1fr')
74. .width('100%')
75. .height(200)
76. }

78. ListItem() {
79. Grid(this.gridScroller) {
80. LazyForEach(this.numbers, (item: string) => {
81. GridItem() {
82. Text(item)
83. .fontSize(16)
84. .backgroundColor(0xF9CF93)
85. .width('100%')
86. .height('100%')
87. .textAlign(TextAlign.Center)
88. }
89. .width('100%')
90. .height(40)
91. .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })
92. .borderRadius(10)
93. .translate({ x: 0, y: this.translateY })
94. }, (item: string) => item)
95. }
96. .columnsTemplate('1fr 1fr')
97. .friction(0.3)
98. .columnsGap(15)
99. .rowsGap(10)
100. .scrollBar(BarState.Off)
101. .width('100%')
102. .height('100%')
103. .layoutDirection(GridDirection.Column)
104. .nestedScroll({
105. scrollForward: NestedScrollMode.PARENT_FIRST,
106. scrollBackward: NestedScrollMode.SELF_FIRST
107. })
108. .onTouch((event: TouchEvent) => {
109. if (event.type == TouchType.Down) {
110. this.listTouchDown = true;
111. } else if (event.type == TouchType.Up) {
112. this.listTouchDown = false;
113. }
114. })
115. }
116. }
117. .scrollBar(BarState.Off)
118. .edgeEffect(EdgeEffect.None)
119. .onTouch((event: TouchEvent) => {
120. if (event.type == TouchType.Down) {
121. this.touchDown = true;
122. } else if (event.type == TouchType.Up) {
123. this.touchDown = false;
124. }
125. })
126. .onScrollFrameBegin((offset: number, state: ScrollState) => {
127. if (this.scrolling && offset > 0) {
128. let newOffset = this.scroller.currentOffset().yOffset;
129. if (newOffset >= 590) {
130. this.gridScroller.scrollBy(0, offset);
131. return { offsetRemain: 0 };
132. } else if (newOffset + offset > 590) {
133. this.gridScroller.scrollBy(0, newOffset + offset - 590);
134. return { offsetRemain: 590 - newOffset };
135. }
136. }
137. return { offsetRemain: offset };
138. })
139. .onScrollStart(() => {
140. if (this.touchDown && !this.listTouchDown) {
141. this.scrolling = true;
142. }
143. })
144. .onScrollStop(() => {
145. this.scrolling = false;
146. })
147. }
148. .width('100%')
149. .height('100%')
150. .padding({ left: 10, right: 10 })
151. }

153. Row() {
154. Text('Top')
155. .width(30)
156. .height(30)
157. .borderRadius(50)
158. }
159. .padding(5)
160. .borderRadius(50)
161. .backgroundColor('#ffffff')
162. .shadow({ radius: 10, color: '#909399', offsetX: 1, offsetY: 1 })
163. .margin({ right: 22, bottom: 15 })
164. .onClick(() => {
165. this.scroller.scrollTo({ xOffset: 0, yOffset: 0 });
166. this.gridScroller.scrollTo({ xOffset: 0, yOffset: 0 });
167. })
168. }
169. .align(Alignment.BottomEnd)
170. }
171. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/ZQ8U2BVMSOeNe51FbgN5bw/zh-cn_image_0000002589245953.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=C22462A43346C5F3042A8DF1DCC74B7BF84950C800D572DBCD8A89E6771E9733)

### 示例5（Grid拖拽场景）

1. 通过属性[editMode](ts-container-grid.md#editmode8)设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem。
2. 在[onItemDragStart](ts-container-grid.md#onitemdragstart8)回调中设置拖拽过程中显示的图片。
3. 在[onItemDrop](ts-container-grid.md#onitemdrop8)中获取拖拽起始位置，和拖拽插入位置，并在[onItemDrop](ts-container-grid.md#onitemdrop8)中完成交换数组位置逻辑。
4. 设置属性supportAnimation(true)支持动画。

说明

预览器窗口不支持显示拖拽跟手。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';

3. @Entry
4. @Component
5. struct GridExample {
6. numbers: GridDataSource = new GridDataSource([]);
7. scroller: Scroller = new Scroller();
8. @State text: string = 'drag';

10. @Builder pixelMapBuilder() { // 拖拽过程样式
11. Column() {
12. Text(this.text)
13. .fontSize(16)
14. .backgroundColor(0xF9CF93)
15. .width(80)
16. .height(80)
17. .textAlign(TextAlign.Center)
18. }
19. }

21. aboutToAppear() {
22. let list: string[] = [];
23. for (let i = 1; i <= 15; i++) {
24. list.push(i + '');
25. }
26. this.numbers = new GridDataSource(list);
27. }

29. changeIndex(index1: number, index2: number) { // 交换数组位置
30. this.numbers.swapItem(index1, index2);
31. }

33. build() {
34. Column({ space: 5 }) {
35. Grid(this.scroller) {
36. LazyForEach(this.numbers, (day: string) => {
37. GridItem() {
38. Text(day)
39. .fontSize(16)
40. .backgroundColor(0xF9CF93)
41. .width(80)
42. .height(80)
43. .textAlign(TextAlign.Center)
44. }
45. }, (day: string) => day)
46. }
47. .columnsTemplate('1fr 1fr 1fr')
48. .columnsGap(10)
49. .rowsGap(10)
50. .width('90%')
51. .backgroundColor(0xFAEEE0)
52. .height(300)
53. .editMode(true) // 设置Grid是否进入编辑模式，进入编辑模式可以拖拽Grid组件内部GridItem
54. .supportAnimation(true) // 设置支持动画
55. .onItemDragStart((event: ItemDragInfo, itemIndex: number) => { // 第一次拖拽此事件绑定的组件时，触发回调。
56. this.text = this.numbers.getData(itemIndex);
57. return this.pixelMapBuilder(); // 设置拖拽过程中显示的图片。
58. })
59. .onItemDrop((event: ItemDragInfo, itemIndex: number, insertIndex: number, isSuccess: boolean) => { // 绑定此事件的组件可作为拖拽释放目标，当在本组件范围内停止拖拽行为时，触发回调。
60. // isSuccess=false时，说明drop的位置在grid外部；insertIndex > length时，说明有新增元素的事件发生
61. if (!isSuccess || insertIndex >= this.numbers.totalCount()) {
62. return;
63. }
64. console.info('itemIndex:' + itemIndex + ', insertIndex:' + insertIndex); // itemIndex拖拽起始位置，insertIndex拖拽插入位置
65. this.changeIndex(itemIndex, insertIndex);
66. })
67. }.width('100%').margin({ top: 5 })
68. }
69. }
```

示例图：

网格子组件开始拖拽：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/_1JRR_-8Qm6CSH55BCvosQ/zh-cn_image_0000002558766144.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=351390EA9C739621B97BCEF3EAC9D761F0EBA3F514CA1C8D30AB6D6D2E095E77)

网格子组件拖拽过程中：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/MJPGRaBxT-eoH2OUFSqZmA/zh-cn_image_0000002558606486.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=3849D85679A5A53E151C561B330E2688CFAD9598BA734E4B460C53EF3D66D71F)

网格子组件1与子组件6拖拽交换位置后：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/LQlu3R3-REOYxkkkWN9BAA/zh-cn_image_0000002589326013.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=5797850EE0E67E87104B4A84293B79E26C48DE077FE5FEC963E2C819066CC60C)

拖拽动画：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/r-4IGiiPRui9v0kmD04hXw/zh-cn_image_0000002589245955.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=39CE0CC089E418D65CB782B7019744759DA56721BDF33771E1F6A71D9DF8A6A5)

### 示例6（自适应Grid）

[layoutDirection](ts-container-grid.md#layoutdirection8)、[maxCount](ts-container-grid.md#maxcount8)、[minCount](ts-container-grid.md#mincount8)、[cellLength](ts-container-grid.md#celllength8)的使用。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';

3. @Entry
4. @Component
5. struct GridExample {
6. numbers: GridDataSource = new GridDataSource([]);

8. aboutToAppear() {
9. let list: string[] = [];
10. for (let i = 1; i <= 30; i++) {
11. list.push(i + '');
12. }
13. this.numbers = new GridDataSource(list);
14. }

16. build() {
17. Scroll() {
18. Column({ space: 5 }) {
19. Blank()
20. Text('rowsTemplate、columnsTemplate都不设置时，layoutDirection、maxCount、minCount、cellLength才生效')
21. .fontSize(16).fontColor(0x000000).width('90%')
22. Grid() {
23. LazyForEach(this.numbers, (day: string) => {
24. GridItem() {
25. Text(day).fontSize(16).backgroundColor(0xF9CF93)
26. }.width(40).height(80).borderWidth(2).borderColor(Color.Red)
27. }, (day: string) => day)
28. }
29. .height(300)
30. .columnsGap(10)
31. .rowsGap(10)
32. .backgroundColor(0xFAEEE0)
33. .maxCount(6)
34. .minCount(2)
35. .cellLength(0)
36. .layoutDirection(GridDirection.Row)
37. }
38. .width('90%').margin({ top: 5, left: 5, right: 5 })
39. .align(Alignment.Center)
40. }
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/QCaTtSdEQDWSE_SdzbSwVg/zh-cn_image_0000002558766146.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=5CA7D418EA91447A846A555497A9BD42B56C8A4F731F4BD8DC7C8A49A47F7BE1)

### 示例7（双指缩放修改Grid列数）

双指缩放修改Grid列数。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource([]);
8. @State columns: number = 2;

10. aboutToAppear() {
11. let lastCount = AppStorage.get<number>('columnsCount');
12. if (typeof lastCount != 'undefined') {
13. this.columns = lastCount;
14. }

16. let list: string[] = [];
17. for (let i = 0; i < 20; i++) {
18. for (let j = 0; j < 20; j++) {
19. list.push(j.toString());
20. }
21. }
22. this.numbers = new GridDataSource(list);
23. }

25. build() {
26. Column({ space: 5 }) {
27. Row() {
28. Text('双指缩放改变列数')
29. .height('5%')
30. .margin({ top: 10, left: 20 })
31. }

33. Grid() {
34. LazyForEach(this.numbers, (day: string) => {
35. GridItem() {
36. Text(day)
37. .fontSize(16)
38. .backgroundColor(0xF9CF93)
39. .width('100%')
40. .height(80)
41. .textAlign(TextAlign.Center)
42. }
43. }, (index: number) => index.toString())
44. }
45. .columnsTemplate('1fr '.repeat(this.columns))
46. .columnsGap(10)
47. .rowsGap(10)
48. .width('90%')
49. .scrollBar(BarState.Off)
50. .backgroundColor(0xFAEEE0)
51. .height('100%')
52. .cachedCount(3)
53. // 切换列数item位置重排动画
54. .animation({
55. duration: 300,
56. curve: Curve.Smooth
57. })
58. .priorityGesture(
59. PinchGesture()
60. .onActionEnd((event: GestureEvent) => {
61. console.info('end scale:' + event.scale);
62. // 手指分开，减少列数以放大Item，触发阈值可以自定义，示例为2
63. if (event.scale > 2) {
64. this.columns--;
65. } else if (event.scale < 0.6) {
66. this.columns++;
67. }
68. // 可以根据设备屏幕宽度设定最大和最小列数，此处以最小1列最大4列为例
69. this.columns = Math.min(4, Math.max(1, this.columns));
70. AppStorage.setOrCreate<number>('columnsCount', this.columns);
71. })
72. )
73. }.width('100%').margin({ top: 5 })
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/YJGGi-p7TcW0p4d7DUQFaA/zh-cn_image_0000002558606488.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=40A33A05801F2710BA132E9AA90C267FBA0AAA5BA5D101E066C5F8EA1DB1E3F9)

### 示例8（设置自适应列数）

属性[columnsTemplate](ts-container-grid.md#columnstemplate)中auto-fill、auto-fit和auto-stretch的使用示例。

```
1. @Entry
2. @Component
3. struct GridColumnsTemplate {
4. data: number[] = [0, 1, 2, 3, 4, 5];
5. data1: number[] = [0, 1, 2, 3, 4, 5];
6. data2: number[] = [0, 1, 2, 3, 4, 5];

8. build() {
9. Column({ space: 10 }) {
10. Text('auto-fill 根据设定的列宽自动计算列数').width('90%')
11. Grid() {
12. ForEach(this.data, (item: number) => {
13. GridItem() {
14. Text('N' + item).height(80)
15. }
16. .backgroundColor(Color.Orange)
17. })
18. }
19. .width('90%')
20. .border({ width: 1, color: Color.Black })
21. .columnsTemplate('repeat(auto-fill, 70)')
22. .columnsGap(10)
23. .rowsGap(10)
24. .height(150)

26. Text('auto-fit 先根据设定的列宽计算列数，余下的空间会均分到每一列中').width('90%')
27. Grid() {
28. ForEach(this.data1, (item: number) => {
29. GridItem() {
30. Text('N' + item).height(80)
31. }
32. .backgroundColor(Color.Orange)
33. })
34. }
35. .width('90%')
36. .border({ width: 1, color: Color.Black })
37. .columnsTemplate('repeat(auto-fit, 70)')
38. .columnsGap(10)
39. .rowsGap(10)
40. .height(150)

42. Text('auto-stretch 先根据设定的列宽计算列数，余下的空间会均分到每个列间距中').width('90%')
43. Grid() {
44. ForEach(this.data2, (item: number) => {
45. GridItem() {
46. Text('N' + item).height(80)
47. }
48. .backgroundColor(Color.Orange)
49. })
50. }
51. .width('90%')
52. .border({ width: 1, color: Color.Black })
53. .columnsTemplate('repeat(auto-stretch, 70)')
54. .columnsGap(10)
55. .rowsGap(10)
56. .height(150)
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/rr2tNYwWTkqaoRrCXFhpOQ/zh-cn_image_0000002589326015.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=30ACEA1A1D348352E8EFA370D2D29224B84B713001357A67C17E63D9D28AB65B)

### 示例9（以当前行最高的GridItem的高度为其他GridItem的高度）

下面的Grid中包含两列，每列中的GridItem包括高度确定的两个Column和一个高度不确定的Text共三个子组件。

在默认情况下，左右两个GridItem的高度可能是不同的；在设置了Grid的[alignItems](ts-container-grid.md#alignitems12)属性为GridItemAlignment.STRETCH后，一行左右两个GridItem中原本高度较小的GridItem会以另一个高度较大的GridItem的高度作为自己的高度。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';

3. @Entry
4. @Component
5. struct Index {
6. data: GridDataSource = new GridDataSource([]);
7. @State items: number[] = [];

9. aboutToAppear(): void {
10. let list: string[] = [];
11. for (let i = 0; i < 100; i++) {
12. list.push(i.toString());
13. this.items.push(this.getSize());
14. }
15. this.data= new GridDataSource(list);
16. }

18. getSize() {
19. let ret = Math.floor(Math.random() * 5);
20. return Math.max(1, ret);
21. }

23. build() {
24. Column({ space: 10 }) {
25. Text('Grid alignItems示例代码')

27. Grid() {
28. LazyForEach(this.data, (item: number) => {
29. // GridItem和Column不设置高度，默认会自适应子组件大小，设置STRETCH的场景下，会变成与当前行最高节点同高。
30. // 若设置高度，则会保持已设置的高度，不会与当前行最高节点同高。
31. GridItem() {
32. Column() {
33. Column().height(100).backgroundColor('#D5D5D5').width('100%')
34. // 中间的Text设置flexGrow(1)来自适应填满父组件的空缺
35. Text('这是一段文字。'.repeat(this.items[item]))
36. .flexGrow(1).width('100%').align(Alignment.TopStart)
37. .backgroundColor('#F7F7F7')
38. Column().height(50).backgroundColor('#707070').width('100%')
39. }
40. }
41. .border({ color: Color.Black, width: 1 })
42. })
43. }
44. .columnsGap(10)
45. .rowsGap(5)
46. .columnsTemplate('1fr 1fr')
47. .width('80%')
48. .height('100%')
49. // Grid设置alignItems为STRETCH，以当前行最高的GridItem的高度为其他GridItem的高度。
50. .alignItems(GridItemAlignment.STRETCH)
51. .scrollBar(BarState.Off)
52. }
53. .height('100%')
54. .width('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/3OnhE9f5TE6Pf9XLtF3UBA/zh-cn_image_0000002589245957.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=AADF02B1C2C6C20FD1861A9C355A091F004C5132B61C323602B739643BE7E4AD)

### 示例10（设置边缘渐隐）

通过[fadingEdge](ts-container-scrollable-common.md#fadingedge14)属性来设置边缘渐隐效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. // 该示例实现了Grid组件开启边缘渐隐效果并设置边缘渐隐长度
3. import { LengthMetrics } from '@kit.ArkUI';
4. import { GridDataSource } from './GridDataSource';

6. @Entry
7. @Component
8. struct GridExample {
9. numbers: GridDataSource = new GridDataSource([]);
10. scroller: Scroller = new Scroller();

12. aboutToAppear() {
13. let list: string[] = [];
14. for (let i = 0; i <= 10; i++) {
15. for (let j = 0; j < 5; j++) {
16. list.push(j.toString());
17. }
18. }
19. this.numbers = new GridDataSource(list);
20. }

22. build() {
23. Column({ space: 5 }) {
24. Text('Grid').fontColor(0x000000).fontSize(16).width('90%')
25. Grid(this.scroller) {
26. LazyForEach(this.numbers, (day: string) => {
27. GridItem() {
28. Text(day)
29. .fontSize(16)
30. .backgroundColor(0xF9CF93)
31. .width('100%')
32. .height(80)
33. .textAlign(TextAlign.Center)
34. }
35. }, (index: number) => index.toString())
36. }
37. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
38. .columnsGap(10)
39. .rowsGap(20)
40. .height('90%')
41. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })

43. }.width('100%').margin({ top: 5 })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/p5EljF_ZSvqbh_dBhtVMWA/zh-cn_image_0000002558766148.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=79097CF597B1C50B9FF54859CAF83C940CD14691ADC4F5C87E53299A109E8A6A)

### 示例11（单边边缘效果）

该示例通过[edgeEffect](ts-container-grid.md#edgeeffect10)接口，实现了Grid组件设置单边边缘效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource([]);
8. scroller: Scroller = new Scroller();

10. aboutToAppear() {
11. let list: string[] = [];
12. for (let i = 0; i <= 10; i++) {
13. for (let j = 0; j < 5; j++) {
14. list.push(j.toString());
15. }
16. }
17. this.numbers = new GridDataSource(list);
18. }

20. build() {
21. Column({ space: 5 }) {
22. Grid(this.scroller) {
23. LazyForEach(this.numbers, (day: string) => {
24. GridItem() {
25. Text(day)
26. .fontSize(16)
27. .backgroundColor(0xF9CF93)
28. .width('100%')
29. .height(80)
30. .textAlign(TextAlign.Center)
31. }
32. }, (index: number) => index.toString())
33. }
34. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
35. .columnsGap(10)
36. .rowsGap(20)
37. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })
38. .width('90%')
39. .backgroundColor(0xDCDCDC)
40. .height('80%')

42. }.width('100%').margin({ top: 5 })
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Qq4tPU4wR0ysvJvCbKQu4Q/zh-cn_image_0000002558606490.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=751F372E0DAD2E3D1F5297877B05BE18EC1C6184700960D9F7C85811149BDDBB)

### 示例12（方向键走焦换行模式）

从API version 20开始，该示例通过[focusWrapMode](ts-container-grid.md#focuswrapmode20)接口，实现了Grid组件方向键走焦换行效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GridExample {
5. scroller: Scroller = new Scroller();
6. build() {
7. Column() {
8. Grid(this.scroller) {
9. GridItem() {
10. Text('A')
11. .focusable(true)
12. .fontSize(18)
13. .fontWeight(5)
14. .backgroundColor(0xF9CF93)
15. .width('100%')
16. .height(80)
17. .textAlign(TextAlign.Center)
18. }
19. GridItem() {
20. Text('B')
21. .focusable(true)
22. .fontSize(18)
23. .fontWeight(5)
24. .backgroundColor(0xF9CF93)
25. .width('100%')
26. .height(80)
27. .textAlign(TextAlign.Center)
28. }
29. GridItem() {
30. Text('C')
31. .focusable(true)
32. .fontSize(18)
33. .fontWeight(5)
34. .backgroundColor(0xF9CF93)
35. .width('100%')
36. .height(80)
37. .textAlign(TextAlign.Center)
38. }
39. GridItem() {
40. Text('D')
41. .focusable(true)
42. .fontSize(18)
43. .fontWeight(5)
44. .backgroundColor(0xF9CF93)
45. .width('100%')
46. .height(80)
47. .textAlign(TextAlign.Center)
48. }
49. GridItem() {
50. Text('E')
51. .focusable(true)
52. .fontSize(18)
53. .fontWeight(5)
54. .backgroundColor(0xF9CF93)
55. .width('100%')
56. .height(80)
57. .textAlign(TextAlign.Center)
58. }
59. GridItem() {
60. Text('F')
61. .focusable(true)
62. .fontSize(18)
63. .fontWeight(5)
64. .backgroundColor(0xF9CF93)
65. .width('100%')
66. .height(80)
67. .textAlign(TextAlign.Center)
68. }
69. }
70. .focusWrapMode(FocusWrapMode.WRAP_WITH_ARROW)
71. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
72. .columnsGap(10)
73. .rowsGap(20)
74. .backgroundColor(0xDCDCDC)
75. }.width('100%').margin({ top: 5 })
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/DnhelWi9RLCQ_EcsfUuUOw/zh-cn_image_0000002589326017.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=D63CB5CC8309000FD685F5B5B11804175BACE62630D805EE5C8A70741150F093)

### 示例13（设置滚动事件）

该示例通过FrameNode中的[getEvent('Grid')](js-apis-arkui-framenode.md#geteventgrid19)获取[UIGridEvent](ts-container-grid.md#uigridevent19)，并为Grid设置滚动事件回调，用于事件监听方因无法直接修改页面代码而无法使用声明式接口设置回调的场景。

从API version 19开始，新增UIGridEvent接口。

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
13. let gridEvent: UIGridEvent | undefined = typeNode.getEvent(frameNode, 'Grid');
14. gridEvent?.setOnWillScroll((scrollOffset: number, scrollState: ScrollState, scrollSource: ScrollSource) => {
15. console.info(`onWillScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}, scrollSource = ${scrollSource}`);
16. });
17. gridEvent?.setOnDidScroll((scrollOffset: number, scrollState: ScrollState) => {
18. console.info(`onDidScroll scrollOffset = ${scrollOffset}, scrollState = ${scrollState}`);
19. });
20. gridEvent?.setOnReachStart(() => {
21. console.info(`onReachStart`);
22. });
23. gridEvent?.setOnReachEnd(() => {
24. console.info(`onReachEnd`);
25. });
26. gridEvent?.setOnScrollStart(() => {
27. console.info(`onScrollStart`);
28. });
29. gridEvent?.setOnScrollStop(() => {
30. console.info(`onScrollStop`);
31. });
32. gridEvent?.setOnScrollFrameBegin((offset: number, state: ScrollState) => {
33. console.info(`onScrollFrameBegin offset = ${offset}, state = ${state}`);
34. return undefined;
35. });
36. gridEvent?.setOnScrollIndex((first: number, last: number) => {
37. console.info(`onScrollIndex start = ${first}, end = ${last}`);
38. });
39. }
40. }

42. @Entry
43. @Component
44. struct Index {
45. @State index: number = 0;
46. private myNodeController: MyNodeController = new MyNodeController();
47. @State numbers: string[] = [];

49. aboutToAppear() {
50. for (let i = 0; i < 5; i++) {
51. for (let j = 0; j < 5; j++) {
52. this.numbers.push(j.toString());
53. }
54. }
55. }

57. build() {
58. Column() {
59. Button('add CommonEvent to Grid')
60. .onClick(() => {
61. this.myNodeController!.addCommonEvent(this.myNodeController!.rootNode!.getParent()!.getPreviousSibling()!);
62. })
63. Grid() {
64. ForEach(this.numbers, (day: string, index: number) => {
65. GridItem() {
66. Text(day)
67. .fontSize(16)
68. .backgroundColor(0xF9CF93)
69. .width('100%')
70. .height(80)
71. .textAlign(TextAlign.Center)
72. }
73. }, (day: string, index: number) => index.toString() + day)
74. }
75. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
76. .columnsGap(10)
77. .rowsGap(10)
78. .enableScrollInteraction(true)
79. .width('90%')
80. .backgroundColor(0xFAEEE0)
81. .height(300)
82. NodeContainer(this.myNodeController)
83. }.width('100%')
84. }
85. }
```

### 示例14（滚动到指定位置）

该示例通过[scrollToIndex](ts-container-scroll.md#scrolltoindex)接口，实现了Grid组件滚动到指定位置。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';
2. @Entry
3. @Component
4. struct GridScrollToIndexSample {
5. numbers: GridDataSource = new GridDataSource([]);
6. scroller: Scroller = new Scroller();
7. aboutToAppear(): void {
8. let list: string[] = [];
9. for (let i = 0; i < 10; i++) {
10. for (let j = 0; j < 10; j++) {
11. list.push((i * 5 + j  + 1).toString());
12. }
13. }
14. this.numbers =  new GridDataSource(list);
15. }

17. build() {
18. Column({ space: 5 }) {
19. Button('scrollToIndex')
20. .onClick(() => { // 滚动到对应的位置
21. this.scroller.scrollToIndex(25, true, ScrollAlign.START);
22. })
23. Grid(this.scroller) {
24. LazyForEach(this.numbers, (day: string) => {
25. GridItem() {
26. Text(day)
27. .fontSize(16)
28. .backgroundColor(0xF9CF93)
29. .width('100%')
30. .height(80)
31. .textAlign(TextAlign.Center)
32. }
33. }, (index: number) => index.toString())
34. }
35. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
36. .columnsGap(10)
37. .rowsGap(10)
38. .friction(0.6)
39. .enableScrollInteraction(true)
40. .supportAnimation(false)
41. .multiSelectable(false)
42. .edgeEffect(EdgeEffect.Spring)
43. .scrollBar(BarState.On)
44. .scrollBarColor(Color.Grey)
45. .scrollBarWidth(4)
46. .width('90%')
47. .backgroundColor(0xFAEEE0)
48. .height(300)
49. }.width('100%').margin({ top: 5 })
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/yPxq1lOpQmWy41wXOUJRMw/zh-cn_image_0000002589245959.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=ADDC2FCA2ABF3DF2805A00D348BC9DD25FC8095652C0FC6BC67E6DE85DF906FA)

### 示例15（实现Grid滑动选择）

该示例通过[PanGesture](ts-basic-gestures-pangesture.md#pangesture-1)接口，实现了Grid组件一边滑动一边选择的效果。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';
3. import { display, curves } from '@kit.ArkUI';

5. enum SlideActionType {
6. START,
7. UPDATE,
8. END
9. }
10. // 热区
11. const HOT_AREA_LENGTH =
12. Math.round(display.getDefaultDisplaySync().densityDPI * 10 / 25.4 / display.getDefaultDisplaySync().densityPixels);
13. // 滚动曲线: 贝塞尔曲线
14. const SLIDE_SELECT_SPEED_CURVE = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
15. // 滚动速度: 最大速度
16. const AUTO_SPEED_MAX: number = Math.round(2400 / display.getDefaultDisplaySync().densityPixels);
17. @Entry
18. @Component
19. struct GridExample {
20. numbers: GridDataSource = new GridDataSource([]);
21. scroller: Scroller = new Scroller();
22. @State selectedIndexes: string[] = [];
23. // 滑动多选时，当前变更选中状态的item
24. @State updateIndex: number = -1;
25. @State lastUpdateIndex: number = -1;
26. @State updateTimer: number = new Date().valueOf();
27. // 是否可进行滑动多选
28. @State canSlideSelect: boolean = false;
29. @State isAutoScroll: boolean = false;
30. // 停止手势
31. @State stopGesture: boolean = false;
32. private scrollStartIndex: number = 0;
33. private scrollEndIndex: number = 0;
34. // 滑动的初始点位
35. @State startIndex: number = -1;
36. @State endIndex: number = -1;
37. // 滚动部位显示区域的高度
38. @State contentHeight: number = 0;
39. @State areaY: number = 0;
40. // 列表宽度
41. @State listWidth: number = 0;
42. @State oldCheckList: boolean[] = [];
43. // 滑动过程中是否将经过的点设为选中状态
44. @State setChecked: boolean = false;
45. aboutToAppear() {
46. let list: string[] = [];
47. for (let i = 0; i < 20; i++) {
48. for (let j = 0; j < 20; j++) {
49. list.push((20 * i + j + 1).toString());
50. }
51. }
52. this.numbers = new GridDataSource(list);
53. }
54. /**
55. * 获取当前点位
56. * @param finger
57. * @returns
58. */
59. getIndex(finger: FingerInfo): number {
60. // 初始化数据
61. let index = -1;
62. try {
63. index = this.scroller.getItemIndex(finger.localX, finger.localY);
64. if (index === -1) {
65. for (let i = this.scrollStartIndex; i <= this.scrollEndIndex; i++) {
66. const item = this.scroller.getItemRect(i);
67. if (finger.localY < item.y ||
68. finger.localY >= item.y && finger.localY <= item.y + item.height && finger.localX < item.x) {
69. break;
70. }
71. index = i;
72. }
73. }
74. } catch {
75. this.stopGesture = true;
76. return index;
77. }
78. return index;
79. }
80. slideActionStart(index: number): void {
81. if (index < 0) {
82. return;
83. }
84. console.debug('start index: ' + index.toString());
85. const targetIndex = index + 1;
86. this.setChecked = !this.selectedIndexes.includes(targetIndex.toString());
87. this.startIndex = index;
88. this.selectedIndexes.push(targetIndex.toString());
89. this.updateIndex = index;

91. }
92. slideActionUpdate(index: number): void {
93. if (!this.canSlideSelect) {
94. return;
95. }
96. if (this.startIndex === -1) {
97. // （初始接触点在空隙）时，重新配置滑动的初始数据
98. this.slideActionStart(index);
99. return;
100. }
101. if (index === -1) {
102. return;
103. }

105. this.lastUpdateIndex = this.updateIndex;
106. this.setItemChecked(index);
107. this.updateIndex = index;
108. }
109. setItemChecked(index: number):void {
110. const start = Math.min(this.startIndex, index);
111. const end = Math.max(this.startIndex, index);
112. for (let i = start; i < end+1;i++) {
113. const item = (i+1).toString();
114. if (this.setChecked) {
115. this.selectedIndexes.push(item);
116. } else {
117. if (this.selectedIndexes.includes(item)) {
118. this.selectedIndexes = this.selectedIndexes.filter(selectIndex => selectIndex != item);
119. }
120. }

122. }
123. }
124. /**
125. * 滑动结束
126. */
127. slideActionEnd(): void {
128. this.startIndex = -1;
129. this.updateIndex = -1;
130. this.scroller.scrollBy(0, 0);
131. this.isAutoScroll = false;
132. }
133. /**
134. * 自动滚动--
135. * @param finger
136. */
137. autoScroll(finger: FingerInfo): void {
138. // 不可多选
139. if (!this.canSlideSelect) {
140. return;
141. }
142. let pointY = finger.globalY - this.areaY;
143. if (pointY <= HOT_AREA_LENGTH) {
144. if (this.isAutoScroll && pointY <= 0) {
145. return;
146. }
147. const speedFlag = pointY > 0 ? SLIDE_SELECT_SPEED_CURVE
148. .interpolate(1 - pointY / HOT_AREA_LENGTH) : 1;
149. this.scroller.scrollEdge(Edge.Top, {
150. velocity: speedFlag * AUTO_SPEED_MAX
151. });
152. this.isAutoScroll = true;
153. } else if (pointY > this.contentHeight - HOT_AREA_LENGTH) {
154. if (this.isAutoScroll && pointY >= this.contentHeight) {
155. return;
156. }
157. const speedFlag = pointY < this.contentHeight ? SLIDE_SELECT_SPEED_CURVE
158. .interpolate(1 - (this.contentHeight - pointY) / HOT_AREA_LENGTH) : 1;
159. this.scroller.scrollEdge(Edge.Bottom, {
160. velocity: speedFlag * AUTO_SPEED_MAX
161. });
162. this.isAutoScroll = true;
163. } else {
164. if (this.isAutoScroll) {
165. this.scroller.scrollBy(0, 0);
166. this.isAutoScroll = false;
167. }
168. }
169. }

171. panGestureAction(type: SlideActionType, event: GestureEvent | undefined): void {
172. if (this.stopGesture || !event) {
173. return;
174. }
175. const finger = event!.fingerList[0];
176. const index = this.getIndex(finger);
177. switch (type) {
178. case SlideActionType.START: {
179. this.slideActionStart(index);
180. break;
181. }
182. case SlideActionType.UPDATE: {
183. this.slideActionUpdate(index);
184. this.autoScroll(finger);
185. break;
186. }
187. case SlideActionType.END: {
188. this.slideActionEnd();
189. break;
190. }
191. default: {
192. }
193. }
194. }
195. build() {
196. Column({ space: 5 }) {
197. Grid(this.scroller) {
198. LazyForEach(this.numbers, (day: string) => {
199. GridItem() {
200. Stack() {
201. Text(day)
202. .fontSize(16)
203. .backgroundColor(0xF9CF93)
204. .width('100%')
205. .height(80)
206. .textAlign(TextAlign.Center)
207. if (this.canSlideSelect) {
208. // $r('app.media.gouxuan')和$r('app.media.weigouxuan')需要替换为开发者所需的图像资源文件。
209. Image(this.selectedIndexes.includes(day) ? $r('app.media.gouxuan') :$r('app.media.weigouxuan'))
210. .width(30)
211. .height(30)
212. .position({right:5,top:5})
213. .draggable(false)
214. }

216. }
217. }
218. }, (index: number) => index.toString())
219. }
220. .columnsTemplate('1fr 1fr 1fr')
221. .columnsGap(10)
222. .rowsGap(10)
223. .friction(0.6)
224. .enableScrollInteraction(true)
225. .supportAnimation(false)
226. .multiSelectable(false)
227. .edgeEffect(EdgeEffect.Spring)
228. .scrollBar(BarState.On)
229. .scrollBarColor(Color.Grey)
230. .scrollBarWidth(4)
231. .width('90%')
232. .height('85%')
233. .draggable(!this.canSlideSelect)
234. .backgroundColor(0xFAEEE0)
235. .onAreaChange((oldVal, newVal) => {
236. this.listWidth = newVal.width as number;
237. this.areaY = newVal.globalPosition.y as number;
238. this.contentHeight = newVal.height as number;
239. })
240. .onScrollIndex((start, end) => {
241. this.scrollStartIndex = start;
242. this.scrollEndIndex = end;
243. })
244. .gesture(
245. // 手势滑动
246. PanGesture({ direction: PanDirection.Vertical })
247. .onActionStart((event: GestureEvent | undefined) => {
248. this.panGestureAction(SlideActionType.START, event);
249. })
250. .onActionUpdate((event: GestureEvent | undefined) => {
251. this.panGestureAction(SlideActionType.UPDATE, event);
252. })
253. .onActionEnd((event?: GestureEvent) => {
254. this.panGestureAction(SlideActionType.END, event);
255. }),
256. GestureMask.Normal
257. )
258. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
259. recognizers: Array<GestureRecognizer>) => {
260. if (this.canSlideSelect && current.isBuiltIn() &&
261. current.getType() == GestureControl.GestureType.PAN_GESTURE) {
262. return GestureJudgeResult.REJECT;
263. }
264. return GestureJudgeResult.CONTINUE;
265. })
266. Row() {
267. Button('开始编辑').onClick(()=>{
268. this.selectedIndexes = [];
269. this.canSlideSelect = true;
270. })
271. Button('结束编辑').onClick(()=>{
272. this.canSlideSelect = false;
273. this.selectedIndexes = [];
274. })
275. }
276. .margin({
277. bottom: 30
278. })
279. Text(`${this.selectedIndexes.join(',')}`)
280. }.width('100%').margin({ top: 5 })
281. }
282. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/ml893AMZSVC1B4ur0zHp8g/zh-cn_image_0000002558766150.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=B881E54D3EAB7B513C5BA85E7DC1183ABFA7251BE727D08E7402F87234DD3DFE)

### 示例16（实现GridItem自定义拖拽）

该示例通过[gesture](ts-gesture-settings.md#gesture)接口，实现了GridItem组件自定义拖拽效果。

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct GridItemExample {
6. @State numbers: number[] = [];
7. @State dragItem: number = -1;
8. @State scaleItem: number = -1;
9. @State item: number = -1;
10. private dragRefOffsetX: number = 0;
11. private dragRefOffsetY: number = 0;
12. @State offsetX: number = 0;
13. @State offsetY: number = 0;
14. private FIX_VP_X: number = 108;
15. private FIX_VP_Y: number = 120;

17. aboutToAppear() {
18. for (let i = 1; i <= 11; i++) {
19. this.numbers.push(i);
20. }
21. }

23. itemMove(index: number, newIndex: number): void {
24. console.info('index:' + index + ' newIndex:' + newIndex);
25. if (!this.isDraggable(newIndex)) {
26. return;
27. }
28. let tmp = this.numbers.splice(index, 1);
29. this.numbers.splice(newIndex, 0, tmp[0]);
30. }

32. // 向下滑
33. down(index: number): void {
34. // 指定固定GridItem不响应事件
35. if (!this.isDraggable(index + 3)) {
36. return;
37. }
38. this.offsetY -= this.FIX_VP_Y;
39. this.dragRefOffsetY += this.FIX_VP_Y;
40. this.itemMove(index, index + 3);
41. }

43. // 向下滑(右下角为空)
44. down2(index: number): void {
45. if (!this.isDraggable(index + 3)) {
46. return;
47. }
48. this.offsetY -= this.FIX_VP_Y;
49. this.dragRefOffsetY += this.FIX_VP_Y;
50. this.itemMove(index, index + 3);
51. }

53. // 向上滑
54. up(index: number): void {
55. if (!this.isDraggable(index - 3)) {
56. return;
57. }
58. this.offsetY += this.FIX_VP_Y;
59. this.dragRefOffsetY -= this.FIX_VP_Y;
60. this.itemMove(index, index - 3);
61. }

63. // 向左滑
64. left(index: number): void {
65. if (!this.isDraggable(index - 1)) {
66. return;
67. }
68. this.offsetX += this.FIX_VP_X;
69. this.dragRefOffsetX -= this.FIX_VP_X;
70. this.itemMove(index, index - 1);
71. }

73. // 向右滑
74. right(index: number): void {
75. if (!this.isDraggable(index + 1)) {
76. return;
77. }
78. this.offsetX -= this.FIX_VP_X;
79. this.dragRefOffsetX += this.FIX_VP_X;
80. this.itemMove(index, index + 1);
81. }

83. // 向右下滑
84. lowerRight(index: number): void {
85. if (!this.isDraggable(index + 4)) {
86. return;
87. }
88. this.offsetX -= this.FIX_VP_X;
89. this.dragRefOffsetX += this.FIX_VP_X;
90. this.offsetY -= this.FIX_VP_Y;
91. this.dragRefOffsetY += this.FIX_VP_Y;
92. this.itemMove(index, index + 4);
93. }

95. // 向右上滑
96. upperRight(index: number): void {
97. if (!this.isDraggable(index - 2)) {
98. return;
99. }
100. this.offsetX -= this.FIX_VP_X;
101. this.dragRefOffsetX += this.FIX_VP_X;
102. this.offsetY += this.FIX_VP_Y;
103. this.dragRefOffsetY -= this.FIX_VP_Y;
104. this.itemMove(index, index - 2);
105. }

107. // 向左下滑
108. lowerLeft(index: number): void {
109. if (!this.isDraggable(index + 2)) {
110. return;
111. }
112. this.offsetX += this.FIX_VP_X;
113. this.dragRefOffsetX -= this.FIX_VP_X;
114. this.offsetY -= this.FIX_VP_Y;
115. this.dragRefOffsetY += this.FIX_VP_Y;
116. this.itemMove(index, index + 2);
117. }

119. // 向左上滑
120. upperLeft(index: number): void {
121. if (!this.isDraggable(index - 4)) {
122. return;
123. }
124. this.offsetX += this.FIX_VP_X;
125. this.dragRefOffsetX -= this.FIX_VP_X;
126. this.offsetY += this.FIX_VP_Y;
127. this.dragRefOffsetY -= this.FIX_VP_Y;
128. this.itemMove(index, index - 4);
129. }

131. isDraggable(index: number): boolean {
132. console.info('index:' + index)
133. return index > 1;
134. }

136. build() {
137. Column() {
138. Grid() {
139. ForEach(this.numbers, (item: number) => {
140. GridItem() {
141. Text(item + '')
142. .fontSize(16)
143. .width('100%')
144. .textAlign(TextAlign.Center)
145. .height(100)
146. .borderRadius(10)
147. .backgroundColor(0xF9CF93)
148. .shadow(this.scaleItem == item ? {
149. radius: 70,
150. color: '#15000000',
151. offsetX: 0,
152. offsetY: 0
153. } :
154. {
155. radius: 0,
156. color: '#15000000',
157. offsetX: 0,
158. offsetY: 0
159. })
160. .animation({ curve: Curve.Sharp, duration: 300 })
161. }
162. // 指定固定GridItem不响应事件
163. .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
164. .scale({ x: this.scaleItem == item ? 1.05 : 1, y: this.scaleItem == item ? 1.05 : 1 })
165. .zIndex(this.dragItem == item ? 1 : 0)
166. .translate(this.dragItem == item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
167. .padding(10)
168. .gesture(
169. // 以下组合手势为顺序识别，当长按手势事件未正常触发时则不会触发拖动手势事件
170. GestureGroup(GestureMode.Sequence,
171. LongPressGesture({ repeat: true })
172. .onAction((event?: GestureEvent) => {
173. this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
174. this.scaleItem = item;
175. })
176. })
177. .onActionEnd(() => {
178. this.getUIContext()?.animateTo({ curve: Curve.Friction, duration: 300 }, () => {
179. this.scaleItem = -1;
180. })
181. }),
182. PanGesture({ fingers: 1, direction: null, distance: 0 })
183. .onActionStart(() => {
184. this.dragItem = item;
185. this.dragRefOffsetX = 0;
186. this.dragRefOffsetY = 0;
187. })
188. .onActionUpdate((event: GestureEvent) => {
189. this.offsetY = event.offsetY - this.dragRefOffsetY;
190. this.offsetX = event.offsetX - this.dragRefOffsetX;
191. this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
192. let index = this.numbers.indexOf(this.dragItem);
193. if (this.offsetY >= this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
194. ![8, 9, 10].includes(index)) {
195. // 向下滑
196. this.down(index);
197. } else if (this.offsetY <= -this.FIX_VP_Y / 2 && (this.offsetX <= 44 && this.offsetX >= -44) &&
198. ![0, 1, 2].includes(index)) {
199. // 向上滑
200. this.up(index);
201. } else if (this.offsetX >= this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
202. ![2, 5, 8, 10].includes(index)) {
203. // 向右滑
204. this.right(index);
205. } else if (this.offsetX <= -this.FIX_VP_X / 2 && (this.offsetY <= 50 && this.offsetY >= -50) &&
206. ![0, 3, 6, 9].includes(index)) {
207. // 向左滑
208. this.left(index);
209. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
210. ![2, 5, 7, 8, 9, 10].includes(index)) {
211. // 向右下滑
212. this.lowerRight(index);
213. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2 &&
214. ![0, 1, 2, 5, 8].includes(index)) {
215. // 向右上滑
216. this.upperRight(index);
217. } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
218. ![0, 3, 6, 9, 10].includes(index)) {
219. // 向左下滑
220. this.lowerLeft(index);
221. } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2 &&
222. ![0, 1, 2, 3, 6, 9].includes(index)) {
223. // 向左上滑
224. this.upperLeft(index);
225. } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2 &&
226. [7].includes(index)) {
227. // 向右下滑(右下角为空)
228. this.down2(index);
229. }
230. })
231. })
232. .onActionEnd(() => {
233. this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
234. this.dragItem = -1;
235. })
236. this.getUIContext()?.animateTo({
237. curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
238. }, () => {
239. this.scaleItem = -1;
240. })
241. })
242. )
243. .onCancel(() => {
244. this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
245. this.dragItem = -1;
246. })
247. this.getUIContext()?.animateTo({
248. curve: curves.interpolatingSpring(14, 1, 170, 17)
249. }, () => {
250. this.scaleItem = -1;
251. })
252. })
253. )
254. }, (item: number) => item.toString())
255. }
256. .width('90%')
257. .editMode(true)
258. .scrollBar(BarState.Off)
259. .columnsTemplate('1fr 1fr 1fr')
260. }.width('100%').height('100%').backgroundColor('#0D182431').padding({ top: 5 })
261. }
262. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/crlnY7uPR4qzGmw8OJQRBA/zh-cn_image_0000002558606492.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=E2BEEAA15F35226D4AEDA1A2574892AACD58CD9569F70133F02ECC1EB5D9A495)

### 示例17（通过拖拽事件实现GridItem拖拽）

该示例通过[拖拽事件](ts-universal-events-drag-drop.md)实现拖拽GridItem到Grid边缘时Grid自动滚动的功能。

GridDataSource说明及完整代码参考[示例2可滚动grid和滚动事件](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct Example {
7. numbers: GridDataSource = new GridDataSource([]);

9. aboutToAppear(): void {
10. let list: string[] = [];
11. for (let index = 0; index < 100; index++) {
12. list.push(index.toString());
13. }
14. this.numbers = new GridDataSource(list);
15. }

17. changeIndex(index1: number, index2: number) { // 交换数组位置
18. console.info(index1 + 'index2:' + index2);
19. this.numbers.swapItem(index1, index2);
20. }

22. build() {
23. Column({ space: 5 }) {
24. Grid() {
25. LazyForEach(this.numbers, (item: number, index: number) => {
26. GridItem() {
27. Text(item + '')
28. .fontSize(16)
29. .backgroundColor(0xF9CF93)
30. .width(80)
31. .height(80)
32. .textAlign(TextAlign.Center)
33. }
34. .width(90)
35. .height(90)
36. .selectable(true)
37. .selected(true)
38. .allowDrop([])
39. .onDragStart((event: DragEvent) => {
40. return { extraInfo: index + '' };
41. })
42. .onDragEnter((event: DragEvent, extraParams?: string) => {
43. console.info(index + '' + extraParams);
44. })
45. .onDragEnd((event: DragEvent, extraParams?: string) => {
46. console.info('onDragEnd' + index + '' + extraParams);
47. })
48. .onDrop((event?: DragEvent, extraParams?: string) => {
49. console.info('drop:' + item + '' + extraParams + JSON.stringify(event!));
50. this.changeIndex(parseInt(JSON.parse(extraParams!).extraInfo), index);
51. })
52. }, (item: string, index: number) => item + '+' + index)
53. }
54. .columnsGap(5)
55. .rowsGap(5)
56. .columnsTemplate('1fr 1fr 1fr')
57. .height(300)
58. }
59. .width('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/poSpVRV2QSaipGBuKVYixw/zh-cn_image_0000002589326019.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=17F02D59E13FC64DC2154D0D19C9B1737157A4D7DF6FED236317D4D93620F6E5)

### 示例18（Grid组件基于断点配置列数）

从API version 22开始，该示例展示了Grid组件支持基于断点配置列数效果。

```
1. // Index.ets
2. // xxx.ets
3. import { GridDataSource } from './GridDataSource';

5. @Entry
6. @Component
7. struct GridExample {
8. numbers: GridDataSource = new GridDataSource([]);

10. aboutToAppear() {
11. let list: string[] = [];
12. for (let i = 0; i < 5; i++) {
13. for (let j = 0; j < 5; j++) {
14. list.push(j.toString());
15. }
16. }
17. this.numbers = new GridDataSource(list);
18. }

20. build() {
21. Column({ space: 5 }) {
22. Grid(undefined) {
23. LazyForEach(this.numbers, (day: string) => {
24. GridItem() {
25. Text(day)
26. .fontSize(16)
27. .backgroundColor(0xF9CF93)
28. .width('100%')
29. .height(80)
30. .textAlign(TextAlign.Center)
31. }
32. }, (index: number) => index.toString())
33. }
34. .columnsTemplate({fillType:PresetFillType.BREAKPOINT_SM2MD3LG5})
35. .columnsGap(10)
36. .rowsGap(10)
37. .scrollBar(BarState.Off)
38. .width('100%')
39. .backgroundColor(0xFAEEE0)
40. .height(300)
41. }.width('100%').height('10%').justifyContent(FlexAlign.SpaceBetween)
42. }
43. }
```

Grid宽度属于sm及更小的断点区间时显示2列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/rg-6LddcQ_uvLeP28LXlnA/zh-cn_image_0000002589245961.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=916902D99682D0A0D2D0DB8FB653381F1A4D62633058365AD0A06404E8BE7E6D)

Grid宽度属于md断点区间时显示3列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/9VhgEbXARhSCJOsiUL5bVw/zh-cn_image_0000002558766152.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=0B91F1D440AD65922D0C989B64B33FAE91C5644712920EC16BE188D35DA983EC)

Grid宽度属于lg及更大的断点区间时显示5列。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/7xmhNRUCQsCTjamxPbyCFQ/zh-cn_image_0000002558606494.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=B03E742AD2A997867A80F6F6181383A4D3450B488BE32B45CC8984A686A4F268)

### 示例19（获取内容总大小）

从API version 22 开始，该示例实现了获取内容总大小的功能。

GridDataSource说明及完整代码参考[示例2（可滚动Grid和滚动事件）](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. import { GridDataSource } from './GridDataSource';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource([]);
8. scroller: Scroller = new Scroller();
9. @State contentWidth: number = -1;
10. @State contentHeight: number = -1;

12. aboutToAppear() {
13. let list: string[] = [];
14. for (let i = 0; i < 10; i++) {
15. for (let j = 0; j < 5; j++) {
16. list.push(j.toString());
17. }
18. }
19. this.numbers = new GridDataSource(list);
20. }

22. build() {
23. Column({ space: 5 }) {
24. Text('可滚动Grid和LazyForEach')
25. Row() {
26. // 点击按钮来调用contentSize函数获取内容尺寸
27. Button('GetContentSize')
28. .onClick(() => {
29. // Scroller未绑定组件时会抛异常，需要加上try catch保护
30. try {
31. // 通过调用contentSize函数获取内容尺寸的宽度值
32. this.contentWidth = this.scroller.contentSize().width;
33. // 通过调用contentSize函数获取内容尺寸的高度值
34. this.contentHeight = this.scroller.contentSize().height;
35. } catch (error) {
36. let err: BusinessError = error as BusinessError;
37. console.error(`Failed to get contentSize of the grid, code=${err.code}, message=${err.message}`);
38. }
39. })
40. // 将获取到的内容尺寸信息通过文本进行呈现
41. Text('Width：' + this.contentWidth + '，Height：' + this.contentHeight)
42. .fontColor(Color.Red)
43. .height(50)
44. }

46. Grid(this.scroller) {
47. LazyForEach(this.numbers, (day: string) => {
48. GridItem() {
49. Text(day)
50. .fontSize(16)
51. .backgroundColor(0xF9CF93)
52. .width('100%')
53. .height(80)
54. .textAlign(TextAlign.Center)
55. }
56. .margin(20)
57. }, (index: number) => index.toString())
58. }
59. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
60. .columnsGap(10)
61. .rowsGap(10)
62. .friction(0.6)
63. .enableScrollInteraction(true)
64. .supportAnimation(false)
65. .multiSelectable(false)
66. .edgeEffect(EdgeEffect.Spring)
67. .scrollBar(BarState.On)
68. .scrollBarColor(Color.Grey)
69. .scrollBarWidth(4)
70. .width('90%')
71. .backgroundColor(0xFAEEE0)
72. .height(300)
73. }.width('100%').margin({ top: 5 })
74. }
75. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/SKxIyvyPTwucBcRHjamRvQ/zh-cn_image_0000002589326021.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=27C3C6B1953FD5F8E82175DB8BFF7B61F909604603C7D12F657DBED5F2471CC6)

### 示例20（设置多选聚拢动画）

该示例通过打开Grid多选聚拢动画开关，实现了在GridItem上[长按弹出菜单](ts-universal-attributes-menu.md#bindcontextmenu8)时聚拢显示范围内被选中的GridItem。

从API version 23开始，Grid组件新增[编辑模式选项](ts-container-grid.md#editmodeoptions23)接口，可以设置多选聚拢动画开关。

GridDataSource说明及完整代码参考[示例2（可滚动Grid和滚动事件）](ts-container-grid.md#示例2可滚动grid和滚动事件)。

```
1. // xxx.ets
2. import { GridDataSource } from './GridDataSource';

4. @Entry
5. @Component
6. struct GridExample {
7. numbers: GridDataSource = new GridDataSource(['1', '2', '3', '4', '5', '6', '7', '8', '9']);
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
23. for (i = 0; i < 9; i++) {
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
47. Text('Grid')
48. Grid() {
49. LazyForEach(this.numbers, (day: string, index: number) => {
50. GridItem() {
51. Text(day)
52. .fontSize(16)
53. .backgroundColor(0xF9CF93)
54. .width('100%')
55. .height('100%')
56. .textAlign(TextAlign.Center)
57. }
58. .selected(this.isSelected[index])
59. // 设置多选显示效果
60. .stateStyles({
61. normal: this.normalStyles,
62. selected: this.selectStyles
63. })
64. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress,
65. { preview: MenuPreviewMode.IMAGE, hapticFeedbackMode: HapticFeedbackMode.ENABLED })
66. .onClick(() => {
67. this.isSelected[index] = !this.isSelected[index];
68. console.info(`item:${index}, this.isSelected[item]:${this.isSelected[index]}`)
69. if (this.isSelected[index]) {
70. ++this.selectedCount;
71. } else {
72. --this.selectedCount;
73. }
74. })
75. }, (day: string) => day)
76. }
77. .editModeOptions({
78. enableGatherSelectedItemsAnimation: true, onGetPreviewBadge: () => {
79. return this.selectedCount;
80. }
81. })
82. .columnsTemplate('1fr 1fr 1fr')
83. .rowsTemplate('1fr 1fr 1fr')
84. .columnsGap(10)
85. .rowsGap(10)
86. .width('90%')
87. .backgroundColor(0xFAEEE0)
88. .height(300)
89. }.width('100%').margin({ top: 5 })
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/b6AVIs98Rri-A5Fy_mW5vg/zh-cn_image_0000002589245963.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=399C2665862716DC2CC3438A80F118314E88E7076A49C1183D87A225A0B065B8)
