---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition
title: 半模态转场
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 模态转场设置 > 半模态转场
category: harmonyos-references
scraped_at: 2026-04-29T13:51:31+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f12443cc08615f4204a2f9491a95893662231cc7773e85daa3c85b82af47ed6c
---

通过bindSheet属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

不支持路由跳转。

## bindSheet

PhonePC/2in1TabletTVWearable

bindSheet(isShow: boolean, builder: CustomBuilder, options?: SheetOptions): T

给组件绑定半模态页面，点击后显示模态页面。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isShow | boolean | 是 | 是否显示半模态页面。  true：显示半模态页面。  false：隐藏半模态页面。  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。 |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 配置半模态页面内容。 |
| options | [SheetOptions](ts-universal-attributes-sheet-transition.md#sheetoptions) | 否 | 配置半模态页面的可选属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

1. 在非双向绑定情况下，以拖拽方式关闭半模态页面不会改变isShow参数的值。
2. 为了使isShow参数值与半模态界面的状态同步，建议使用[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定isShow参数。从API version 18开始，该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。
3. 在半模态单挡位向上拖拽或是多挡位上滑换挡情况下，内容在拖拽结束或换挡结束后更新显示区域。
4. 半模态是一个严格和宿主节点绑定在一起的弹窗。若是想实现类似“页面显示的瞬间就弹出半模态”的效果，请确认宿主节点是否已挂载上树。若宿主节点还没上树就将isShow置为true，半模态将不生效。建议使用[onAppear](ts-universal-events-show-hide.md#onappear)函数，确保在宿主节点挂载后再显示半模态。

   尤其是 [SheetMode](ts-universal-attributes-sheet-transition.md#sheetmode12枚举说明) = EMBEDDED 时，除宿主节点外，还需确保对应的页面节点成功挂载。
5. 半模态页面的离场动效不支持打断，动效执行期间无法响应其他手势动作。目前离场动效使用[弹簧曲线](../harmonyos-guides/arkts-spring-curve.md)，该动画曲线存在视觉上并不明显的拖尾动画。因此，在半模态退出时，视觉上半模态页面已经消失，但此时动效可能还未结束，若想再次点击拉起半模态页面则不会响应。需要等动效完全结束后，才可以再次拉起。

## SheetOptions

PhonePC/2in1TabletTVWearable

继承自[BindOptions](ts-universal-attributes-sheet-transition.md#bindoptions)。

半模态页面内容选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| height | [SheetSize](ts-universal-attributes-sheet-transition.md#sheetsize枚举说明) | [Length](ts-types.md#length) | 否 | 是 | 半模态高度，默认是LARGE。  **说明：**  1. API version 14开始，底部弹窗横屏时，无状态栏则最大高度为距离屏幕顶部8vp，有状态栏则最大高度为距离状态栏8vp。  2. 底部弹窗时，当设置detents时，该属性设置无效。  3. 底部弹窗竖屏时，最大高度为距离状态栏8vp。  4. 居中弹窗和跟手弹窗设置类型为SheetSize.LARGE和SheetSize.MEDIUM无效，显示默认高度560vp。  5. 居中弹窗和跟手弹窗最小高度为320vp，最大高度为窗口短边的90%。  6. 居中弹窗和跟手弹窗当使用Length设置的高度时，高度大于最大高度，则显示最大高度，小于最小高度，则显示最小高度。  7. 如果半模态使用SheetSize.FIT\_CONTENT自适应模式，且类型设置为居中弹窗或跟手弹窗，API version 22及之前版本，高度大于最大高度时显示最大高度，高度小于最小高度时显示最小高度。从API version 23开始，高度大于最大高度时显示最大高度，高度小于最小高度时按照实际自适应高度生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| detents11+ | [([SheetSize](ts-universal-attributes-sheet-transition.md#sheetsize枚举说明) | [Length](ts-types.md#length)), ( [SheetSize](ts-universal-attributes-sheet-transition.md#sheetsize枚举说明) | [Length](ts-types.md#length))?, ([SheetSize](ts-universal-attributes-sheet-transition.md#sheetsize枚举说明) | [Length](ts-types.md#length))?] | 否 | 是 | 半模态页面的切换高度挡位。  **说明：**  从API version 12开始，底部弹窗横屏时该属性设置生效。  底部弹窗竖屏生效，元组中第一个高度为初始高度。  面板可跟手滑动切换挡位，松手后是否滑动至目标挡位有两个判断条件：速度和距离。速度超过阈值，则执行滑动至与手速方向一致的目标挡位；速度小于阈值，则引入距离判断条件，当位移距离>当前位置与目标位置的1/2，滑动至与手速方向一致的目标挡位，位移距离当前位置与目标位置的1/2，返回至当前挡位。速度阈值：1000，距离阈值：50%。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| preferType11+ | [SheetType](ts-universal-attributes-sheet-transition.md#sheettype11枚举说明) | 否 | 是 | 半模态页面的样式。  **说明：**  半模态在不同窗口所支持的显示类型：  1. 宽度 < 600vp：底部、全屏。默认底部样式。  2. 600vp <= 宽度 < 840vp：底部、居中、跟手、侧边、全屏。默认居中样式。  3. 宽度 >= 840vp：底部、居中、跟手、侧边、全屏。默认跟手样式。  4. API version 20开始，窗口宽度大于600vp时，preferType支持设置为SheetType.SIDE。  5. API version 20开始，preferType支持设置为SheetType.CONTENT\_COVER，支持设置为全屏模态样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| showClose11+ | boolean | [Resource](ts-types.md#resource) | 否 | 是 | 是否显示关闭图标。  2in1设备默认无按钮底板。  默认值：true。  true：显示关闭图标。  false：不显示关闭图标。  **说明：**  Resource需要为boolean类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dragBar | boolean | 否 | 是 | 是否显示控制条。  默认值：true  true：显示控制条。  false：不显示控制条。  **说明：**  半模态面板的detents属性设置多个不同高度并且设置生效时，默认显示控制条。否则不显示控制条。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| blurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 半模态面板的模糊背景。默认无模糊背景。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maskColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 半模态页面的背景蒙层颜色。  默认值：$r('sys.color.ohos\_id\_color\_mask\_thin')。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title11+ | [SheetTitleOptions](ts-universal-attributes-sheet-transition.md#sheettitleoptions11) | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 半模态面板的标题。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableOutsideInteractive11+ | boolean | 否 | 是 | 半模态页面显示时，其下层页面是否允许交互。  **说明：**  设置为true时允许交互，不显示蒙层；设置为false时不允许交互，显示蒙层；若不进行设置，默认底部弹窗与居中弹窗不允许交互，跟手弹窗允许交互。当设置为true时，maskColor设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shouldDismiss11+ | (sheetDismiss: [SheetDismiss](ts-universal-attributes-sheet-transition.md#sheetdismiss11)) => void | 否 | 是 | 半模态页面交互式关闭回调函数。  **说明：**  当用户执行下拉关闭、侧拉关闭、点击遮罩层关闭、点击关闭按钮的交互操作时，如果已注册回调函数，模态窗口将不会立即关闭。要关闭半模态，需在回调函数中调用shouldDismiss.dismiss()方法来实现。  如果不注册该回调函数，则用户执行下拉关闭、侧拉关闭、点击遮罩层关闭、点击关闭按钮的交互操作时，正常关闭半模态，无其他行为。  侧拉关闭又包含侧滑（左滑/右滑）、三键back、键盘ESC关闭。  建议在[二次确认](../harmonyos-guides/arkts-sheet-page.md#二次确认能力)场景使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDismiss12+ | [Callback](ts-types.md#callback12)<[DismissSheetAction](ts-universal-attributes-sheet-transition.md#dismisssheetaction12)> | 否 | 是 | 半模态页面的交互式关闭回调函数。允许开发者注册，以获取关闭操作的类型，并决定是否关闭半模态状态。  **说明：**  当用户执行下拉关闭、侧拉关闭、点击遮罩层关闭、点击关闭按钮的交互操作时，若已注册回调函数，则不会立即关闭页面，而是由开发者通过回调函数[DismissSheetAction](ts-universal-attributes-sheet-transition.md#dismisssheetaction12)中的reason参数判断关闭操作的类型，进而根据具体原因自主选择是否关闭半模态页面。  如果不注册该回调函数，则用户执行关闭操作时，正常关闭半模态，无其他行为。  侧拉关闭又包含侧滑（左滑/右滑）、三键back、键盘ESC关闭。  在onWillDismiss回调中，不能再做onWillDismiss拦截。  建议在[二次确认](../harmonyos-guides/arkts-sheet-page.md#二次确认能力)场景使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillSpringBackWhenDismiss12+ | [Callback](ts-types.md#callback12)<[SpringBackAction](ts-universal-attributes-sheet-transition.md#springbackaction12)> | 否 | 是 | 半模态页面交互式关闭前控制回弹函数。允许开发者注册，以控制半模态页面交互式关闭时的回弹效果。  **说明：**  当用户触发执行下拉关闭操作并同时注册该回调函数与shouldDismiss或onWillDismiss时，由开发者控制下滑关闭时是否回弹。在回调函数中可以通过调用springBack来实现回弹效果。也可以通过不调用springBack来取消回弹效果。  若不注册该回调函数，但注册shouldDismiss或onWillDismiss时，则默认在下拉关闭时，会触发回弹效果，回弹后再根据shouldDismiss或onWillDismiss内的回调行为决定半模态是否关闭。  如果不注册该回调函数，且未注册shouldDismiss或onWillDismiss时，默认在下滑关闭时，触发半模态关闭。  侧边弹窗样式则是在侧拉关闭场景生效springBack。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onHeightDidChange12+ | Callback<number> | 否 | 是 | 半模态页面高度变化回调函数。  **说明：**  底部弹窗时，只有挡位变化和拖拽跟手才返回每一帧高度，拉起半模态和避让软键盘只返回最后的高度，其他弹窗只在半模态拉起返回最后高度。  返回值为px。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDetentsDidChange12+ | Callback<number> | 否 | 是 | 半模态页面挡位变化回调函数。  **说明：**  底部弹窗时，挡位变化返回最后的高度。  返回值为px。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWidthDidChange12+ | Callback<number> | 否 | 是 | 半模态页面宽度变化回调函数。  **说明：**  宽度变化时返回最后的宽度。  返回值为px。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onTypeDidChange12+ | Callback<[SheetType](ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)> | 否 | 是 | 半模态页面形态变化回调函数。  **说明：**  形态变化时返回最后的形态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderWidth12+ | [Dimension](ts-types.md#dimension10) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 否 | 是 | 设置半模态页面的边框宽度。  可分别设置4个边框宽度。  默认值：0  百分比参数方式：以父元素半模态页面宽的百分比来设置半模态页面的边框宽度。  当半模态页面左边框和右边框大于半模态页面宽度，半模态页面上边框和下边框大于半模态页面高度，显示可能不符合预期。  **说明：**  底部弹窗时，底部边框宽度设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderColor12+ | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)12+ | 否 | 是 | 设置半模态页面的边框颜色。  默认值：Color.Black  如果使用borderColor属性，需要和borderWidth属性一起使用。  **说明：**  底部弹窗时，底部边框颜色设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| borderStyle12+ | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9) | 否 | 是 | 设置半模态页面的边框样式。  默认值：BorderStyle.Solid  如果使用borderStyle属性，需要和borderWidth属性一起使用。  **说明：**  底部弹窗时，底部边框样式设置无效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| width12+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置半模态页面的宽度。  百分比参数方式：以父元素宽的百分比来设置半模态页面的宽度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置半模态页面的阴影。  2in1设备默认值：ShadowStyle.OUTER\_FLOATING\_SM。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uiContext12+ | [UIContext](arkts-apis-uicontext-uicontext.md) | 否 | 是 | 在UIContext实例对应的窗口中显示半模态。  **说明：**  使用[openBindSheet](arkts-apis-uicontext-uicontext.md#openbindsheet12)启动的半模态页面，不支持设置、更新该属性。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mode12+ | [SheetMode](ts-universal-attributes-sheet-transition.md#sheetmode12枚举说明) | 否 | 是 | 设置半模态页面的显示层级。  默认值：SheetMode.OVERLAY  **说明：**  1. 半模态显示期间mode属性不支持动态切换，两种模式的显示层级完全不同，无法做到显示期间同一个半模态从一个层级变换到另一个层级。建议在使用时明确诉求固定mode值。  2. 设置SheetMode.EMBEDDED时不支持设置UIContext属性，两者对应的半模态显示层级效果互相冲突。  3. 使用[openBindSheet](arkts-apis-uicontext-uicontext.md#openbindsheet12)启动半模态页面，若未传入有效的targetId，则不支持设置为SheetMode.EMBEDDED，默认为SheetMode.OVERLAY。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| scrollSizeMode12+ | [ScrollSizeMode](ts-universal-attributes-sheet-transition.md#scrollsizemode12枚举说明) | 否 | 是 | 设置半模态面板滑动时，内容区域刷新时机。  默认值：ScrollSizeMode.FOLLOW\_DETENT  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| keyboardAvoidMode13+ | [SheetKeyboardAvoidMode](ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明) | 否 | 是 | 设置半模态激活输入法时对软键盘的避让方式。  **默认值：** TRANSLATE\_AND\_SCROLL  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。  默认值：false，默认不响应。  2in1设备默认值：true  true：响应悬停态。  false：不响应悬停态。  **说明：**  底部弹窗样式和跟手弹窗样式不响应悬停态。子窗模式不支持悬停态。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  2in1设备默认值：HoverModeAreaType.TOP\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| radius15+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 设置半模态页面圆角半径。  不建议设置4个圆角大小不相等，圆角大小相等时面板视觉体验最佳。  **默认值**：32vp  **说明：**  1. 根据设置的圆角半径值显示，如果未设置，则使用默认值。底部样式不显示半模态底部2个圆角，即使设置了底部2个圆角也不生效。  2. 分别设置4个方向的圆角半径后，如果某个方向的值异常，异常方向的圆角值重置为默认值，非异常方向的圆角值为已设置的值。统一设置4个方向的圆角时，如果设置的值异常，4个方向的圆角都重置为默认值。  3. 半径设置为百分比时，以半模态页面的宽度为基准。  4. 当圆角的半径大于半模态页面宽度一半时，圆角的半径取值为半模态页面宽度的一半。  5. 当半模态页面高度过小且圆角半径设置过大时，可能导致显示异常。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| detentSelection15+ | [SheetSize](ts-universal-attributes-sheet-transition.md#sheetsize枚举说明) | [Length](ts-types.md#length) | 否 | 是 | 支持非手势切换挡位。  **默认值：** detents[0]。  **说明：**  1. 该接口取值范围为detents数组范围，若设值非detents范围，该接口无效。  2. 当设置SheetSize.FIT\_CONTENT时，该接口无效。  3. 不建议手势切换挡位与该接口切换挡位同时生效使用。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| placement18+ | [Placement](ts-appendix-enums.md#placement8) | 否 | 是 | 设置半模态popup样式弹窗相对于目标的显示位置。  默认值：Placement.Bottom  **说明：**  1. popup样式弹窗在确保指定位置能容纳弹窗尺寸的前提下，优先依据设定的placement展示弹窗。若不可行，则遵循先垂直翻转，后尝试90°水平旋转的规则调整显示位置，以预设方向为下方为例，调整顺序依次为：下、上、右、左。  2. 如果设置的对齐方式导致组件布局超出窗口范围，将根据该对齐方式在水平或垂直方向上进行位移，直至组件完全显示在窗口内。  3. 如果在四个方向上均无法容纳当前的popup样式弹窗，处理方式遵循开发者设置的placementOnTarget属性：  1）若属性值为true，将依据设定的placement，向其镜像方向平移，直至弹窗能够完全显示。  2）若属性值为false，则在四个方向中，选择能够完全展示弹窗宽度且剩余高度最大的方向，通过调整半模态高度以适应当前方向，确保弹窗能够放下，同时保持预设placement对应的对齐方式不变。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| placementOnTarget18+ | boolean | 否 | 是 | 半模态popup样式弹窗在当前窗口下，四个方向均无法容纳该弹窗大小时，设置是否允许其覆盖在目标节点上。  默认值：true  true：允许其覆盖在目标节点上。  false：不允许其覆盖在目标节点上。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| effectEdge18+ | number | 否 | 是 | 设置半模态面板内容区边缘回弹效果，支持单边生效。  **默认值**：默认双边生效，即[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START | [EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END（即数值3）。  **说明：**  1. 仅上边缘生效：[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START。  2. 仅下边缘生效：[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END。  3. 双边生效：[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START | [EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END（即数值3）。  4. 双边不生效：[EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).START & [EffectEdge](ts-container-scrollable-common.md#effectedge18枚举说明).END（即数值0）。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| showInSubWindow19+ | boolean | 否 | 是 | 半模态是否在独立子窗中显示。  默认值：false  **说明：**  1. 若属性值为true，半模态可以在独立子窗口中展示，并且可以超过应用窗口范围。  2. 若属性值为false，半模态只能在应用窗口范围内展示。  3. 不建议在showInSubWindow为true的弹窗嵌套显示另一个showInSubWindow为true的弹窗，半模态可能会影响其他组件行为。  4. 不建议在showInSubWindow为true的弹窗中使用CalendarPicker、CalendarPickerDialog、DatePickerDialog、TextPickerDialog、TimePickerDialog等picker组件，半模态会影响上述组件行为。  5. 半模态显示期间该属性不支持动态切换。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| enableFloatingDragBar20+ | boolean | 否 | 是 | 控制条是否悬浮显示，true为悬浮显示，false为不悬浮显示。  默认值：false  **说明：**  悬浮效果只在控制条显示的场景生效，且控制条不占位。  title传入[CustomBuilder](ts-types.md#custombuilder8)时enableFloatingDragBar始终为false。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| modalTransition20+ | [ModalTransition](ts-universal-attributes-sheet-transition.md#modaltransition) | 否 | 是 | bindSheet全屏模态样式的系统转场方式。  默认值：ModalTransition.DEFAULT  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| radiusRenderStrategy23+ | [RenderStrategy](ts-appendix-enums.md#renderstrategy22) | 否 | 是 | 设置组件绘制圆角的模式。  默认值：RenderStrategy.FAST  **说明**: 当半模态设置模糊时，可通过设置为OFFSCREEN离屏模式解决半模态顶部或顶部圆角区域内显示效果异常问题。popup样式不支持设置组件绘制圆角模式。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## SheetSize枚举说明

PhonePC/2in1TabletTVWearable

指定半模态的高度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIUM | 0 | 指定半模态高度为半模态所在窗口的60%。  在TV设备上半模态高度为半模态所在窗口的50%。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| LARGE | 1 | 指定半模态高度几乎为半模态所在窗口的高度。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| FIT\_CONTENT11+ | 2 | 指定半模态高度为适应内容的高度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  **说明：**  1. FIT\_CONTENT是半模态容器高度去适应孩子builder根节点的布局。此场景下builder根节点的高度不能使用百分比，两者不能相互依赖彼此的布局。  2. 如果半模态使用SheetSize.FIT\_CONTENT自适应模式，且类型设置为居中弹窗或跟手弹窗，API version 22及之前版本，高度大于最大高度，则显示最大高度，高度小于最小高度，则显示最小高度。  API version 23开始，高度大于最大高度，则显示最大高度，高度小于最小高度，按照实际自适应高度生效。  其中居中弹窗和跟手弹窗最小高度为320vp，最大高度为窗口短边的90%。 |

## HoverModeAreaType14+

PhonePC/2in1TabletTVWearable

悬停态显示区域类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP\_SCREEN | 0 | 上半屏。 |
| BOTTOM\_SCREEN | 1 | 下半屏。 |

## BindOptions

PhonePC/2in1TabletTVWearable

半模态、全模态的公共配置接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 半模态页面的背板颜色。  默认值：Color.White。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | () => void | 否 | 是 | 半模态页面显示（动画开始前）回调函数。**元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onAppear | () => void | 否 | 是 | 半模态页面显示（动画结束后）回调函数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | () => void | 否 | 是 | 半模态页面回退（动画开始前）回调函数。  **说明：**  不允许在onWillDisappear函数中修改状态变量，可能会导致组件行为不稳定。**元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDisappear | () => void | 否 | 是 | 半模态页面回退（动画结束后）回调函数。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ModalTransition

PhonePC/2in1TabletTVWearable

全屏模态转场方式枚举类型，用于设置全屏模态转场类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 全屏模态上下切换动画。 |
| NONE | 1 | 全屏模态无转场动画。 |
| ALPHA | 2 | 全屏模态透明度渐变动画。 |

## SheetType11+枚举说明

PhonePC/2in1TabletTVWearable

半模态弹窗的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOTTOM | 0 | 底部弹窗。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CENTER | 1 | 居中弹窗。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| POPUP | 2 | 跟手弹窗。跟手弹窗面板不支持跟手滑动，下滑面板不关闭。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SIDE20+ | 3 | 侧边弹窗。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| CONTENT\_COVER20+ | 4 | 全屏弹窗。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

**半模态侧边弹窗样式：**

1. 侧边样式默认转场方向为从右向左，退出则是原地向右退出；镜像场景默认转场则是从左向右，退出则是原地向左退出。不支持自定义转场。
2. 无多挡位能力，不支持detents和detentSelection接口。同样也不支持控制条相关能力接口，如dragBar接口。
3. 底部弹窗样式可以在转场结束后向上滑动交互，但侧边弹窗样式不支持在转场结束后往左滑动交互，只支持往右滑动关闭。镜像场景则能力相反。
4. 不支持高度自定义，高度默认全屏。
5. 不支持指定其他显示层级接口，如showInSubWindow = true、mode = SheetMode.EMBEDDED。侧边弹窗的层级同SheetMode.OVERLAY，只支持在当前UIContext内顶层显示，在所有页面之上。和弹窗类组件显示在一个层级。
6. 无悬停态避让能力。
7. SIDE样式的半模态width的默认值规格：

   * [断点](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)为md的场景，默认宽度为窗口的1/2。
   * [断点](../harmonyos-guides/arkts-layout-development-grid-layout.md#栅格容器断点)大于md的场景，默认宽度400vp。

**侧边弹窗样式不支持的接口**

| 名称 | 说明 |
| --- | --- |
| height | 高度只支持全屏高度。 |
| detents | 无挡位能力。 |
| dragBar | 不支持DragBar。 |
| onDetentsDidChange | 无挡位能力。 |
| uiContext | 不支持指定显示层级。 |
| mode | 不支持指定显示层级。 |
| scrollSizeMode | 无挡位能力。 |
| enableHoverMode | 无悬停态避让能力。 |
| hoverModeArea | 无悬停态避让能力。 |
| detentSelection | 无挡位能力。 |
| placement | 只支持气泡样式。 |
| placementOnTarget | 只支持气泡样式。 |
| showInSubWindow | 不支持指定显示层级。 |

**bindSheet全屏模态样式说明：**

1. 全屏样式显示页面效果为铺满全屏，不支持边框、阴影、标题栏、关闭按钮、圆角等。
2. builder内容默认布局在安全区内。
3. 全屏样式支持系统转场方式[ModalTransition](ts-universal-attributes-sheet-transition.md#modaltransition)，默认值为ModalTransition.DEFAULT，不支持自定义转场。
4. 不支持挡位能力，不支持detents和detentSelection接口。
5. 不支持上下滑动，仅支持侧滑关闭。
6. 不支持宽高自定义，宽高默认为全屏。
7. 不支持指定其他显示层级接口，如showInSubWindow = true、mode = SheetMode.EMBEDDED。全屏弹窗的层级与SheetMode.OVERLAY相同，仅支持在当前UIContext内顶层显示，位于所有页面之上，与弹窗类组件显示在同一层级。
8. 默认不避让软键盘，需自定义避让软键盘。
9. 不支持蒙层效果。

**bindSheet全屏模态样式不支持的接口**

| 名称 | 说明 |
| --- | --- |
| height | 高度只支持全屏高度。 |
| width | 宽度只支持全屏宽度。 |
| detents | 无挡位能力。 |
| dragBar | 不支持拖动条。 |
| onDetentsDidChange | 无挡位能力。 |
| showClose | 不支持显示关闭按钮。 |
| title | 不支持显示标题栏。 |
| uiContext | 不支持指定显示层级。 |
| mode | 不支持指定显示层级。 |
| scrollSizeMode | 无挡位能力。 |
| keyboardAvoidMode | 无避让软键盘能力，需自定义避让。 |
| enableHoverMode | 无悬停态避让能力。 |
| hoverModeArea | 无悬停态避让能力。 |
| detentSelection | 无挡位能力。 |
| showInSubWindow | 不支持指定显示层级。 |
| radius | 不支持圆角。 |
| borderWidth | 不支持边框宽度。 |
| borderColor | 不支持边框颜色。 |
| borderStyle | 不支持边框样式。 |
| shadow | 不支持阴影。 |
| maskColor | 不支持蒙层颜色。 |
| enableOutsideInteractive | 不支持设置是否允许交互。 |
| effectEdge | 不支持边缘回弹效果。 |
| enableFloatingDragBar | 不支持浮动拖动条。 |
| onWillSpringBackWhenDismiss | 无回弹效果。 |

## SheetDismiss11+

PhonePC/2in1TabletTVWearable

控制半模态的关闭。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | () => void | 否 | 否 | 半模态面板关闭回调函数。开发者需要退出时调用，不需要退出时无需调用。 |

## SheetTitleOptions11+

PhonePC/2in1TabletTVWearable

半模态面板的标题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 半模态面板的主标题。 |
| subtitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 半模态面板的副标题。 |

## SheetMode12+枚举说明

PhonePC/2in1TabletTVWearable

半模态的显示层级模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OVERLAY | 0 | 设置半模态面板在当前UIContext内顶层显示，在所有页面之上。和弹窗类组件显示在一个层级。 |
| EMBEDDED | 1 | 设置半模态面板在当前页面内的顶层显示。  **说明：**  目前只支持挂载在Page或者NavDestination节点上，若有NavDestination优先挂载在NavDestination上。只支持在这两种页面内顶层显示。  该模式下新起的页面可以覆盖在半模态弹窗上，页面返回后该半模态依旧存在，半模态面板内容不丢失。  该模式下需确保目标页面节点如Page节点已挂载上树，再拉起半模态，否则半模态将无法挂载到对应的页面节点内。 |

## ScrollSizeMode12+枚举说明

PhonePC/2in1TabletTVWearable

半模态面板上下滑动时的内容更新方式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOW\_DETENT | 0 | 设置半模态面板跟手滑动结束后更新内容显示区域。 |
| CONTINUOUS | 1 | 设置半模态面板在滑动过程中持续更新内容显示区域。 |

## DismissSheetAction12+

PhonePC/2in1TabletTVWearable

半模态关闭前的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dismiss | [Callback](ts-types.md#callback12)<void> | 否 | 否 | 半模态页面关闭回调函数。开发者需要退出页面时调用。 |
| reason | [DismissReason](ts-universal-attributes-popup.md#dismissreason12枚举说明) | 否 | 否 | 返回本次半模态页面退出的操作类型。  **说明：**  DismissReason.SLIDE只生效半模态侧边弹窗形态，表示右滑退出。若镜像场景则表示左滑退出。  DismissReason.SLIDE\_DOWN生效半模态底部弹窗形态和居中弹窗形态，表示下滑退出。  半模态气泡弹窗形态无滑动退出能力。 |

## SpringBackAction12+

PhonePC/2in1TabletTVWearable

控制半模态关闭前的回弹。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| springBack | [Callback](ts-types.md#callback12)<void> | 否 | 否 | 半模态页面关闭前控制回弹函数，开发者需要半模态回弹时调用。 |

## SheetKeyboardAvoidMode13+枚举说明

PhonePC/2in1TabletTVWearable

半模态激活输入法时对软键盘的避让方式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 设置半模态不避让软键盘。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| TRANSLATE\_AND\_RESIZE | 1 | 设置半模态先上抬面板避让软键盘；  当上抬至最大高度仍不足以避让软键盘时，则通过压缩整体内容完成避让。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| RESIZE\_ONLY | 2 | 设置半模态通过压缩整体内容避让软键盘。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| TRANSLATE\_AND\_SCROLL | 3 | 设置半模态先上抬面板避让软键盘；  当上抬至最大高度仍不足以避让软键盘时，则通过滚动内容完成避让。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| POPUP\_SHEET20+ | 4 | 设置半模态popup样式弹窗避让软键盘。  1. 避让软键盘时，在popup样式弹窗当前显示位置无法容纳弹窗尺寸的前提下，遵循先垂直翻转避让，后尝试90°水平旋转避让的规则调整显示位置，以预设方向为下方为例，调整避让顺序依次为：下、上、右、左。  2. 如果设置的对齐方式导致组件布局超出窗口范围，将根据该对齐方式在水平或垂直方向上进行位移，直至组件完全显示在窗口内。  3. 避让软键盘时，如果在四个方向上均无法容纳当前的popup样式弹窗，处理方式遵循开发者设置的placementOnTarget属性：  （1）若属性值为true，将依据设定的placement，向其镜像方向平移，直至弹窗能够完全显示。  （2）若属性值为false，则在四个方向中，选择能够完全展示弹窗宽度且剩余高度最大的方向，通过调整半模态高度以适应当前方向，确保弹窗能够放下，同时保持预设placement对应的对齐方式不变。  4. 若此时半模态不是跟手样式，则不具备避让软键盘能力。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

说明

设置POPUP\_SHEET避让方式时，半模态只避让由面板内的文本框组件拉起的软键盘场景，其他场景半模态无需避让。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（不同高度的半模态弹窗）

该示例通过height设置不同高度的半模态弹窗。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SheetTransitionExample {
5. @State isShow: boolean = false;
6. @State sheetHeight: number = 300;

8. @Builder
9. myBuilder() {
10. Column() {
11. Button("change height")
12. .margin(10)
13. .fontSize(20)
14. .onClick(() => {
15. this.sheetHeight = 500;
16. })

18. Button("Set Illegal height")
19. .margin(10)
20. .fontSize(20)
21. .onClick(() => {
22. this.sheetHeight = -1;
23. })

25. Button("close modal 1")
26. .margin(10)
27. .fontSize(20)
28. .onClick(() => {
29. this.isShow = false;
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }

36. build() {
37. Column() {
38. Button("transition modal 1")
39. .onClick(() => {
40. this.isShow = true;
41. })
42. .fontSize(20)
43. .margin(10)
44. .bindSheet($$this.isShow, this.myBuilder(), {
45. height: this.sheetHeight,
46. backgroundColor: Color.Green,
47. onWillAppear: () => {
48. console.info("BindSheet onWillAppear.");
49. },
50. onAppear: () => {
51. console.info("BindSheet onAppear.");
52. },
53. onWillDisappear: () => {
54. console.info("BindSheet onWillDisappear.");
55. },
56. onDisappear: () => {
57. console.info("BindSheet onDisappear.");
58. }
59. })
60. }
61. .justifyContent(FlexAlign.Center)
62. .width('100%')
63. .height('100%')
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ohNCX2P6QQOUwnq1932HKA/zh-cn_image_0000002558766088.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=E90E2AB0C03705DA70C7133ECFF0CC3AAC5042CAC7AC55E450917C73A51BC4DC)

### 示例2（设置三个不同高度的挡位）

使用bindSheet的detents属性设置三个不同高度的挡位。

1. dragBar拖拽条只在多个挡位高度时生效；
2. 区别于height属性在不同时刻设置不同挡位的能力，多挡位能力有手势切换挡位高度的效果，且更适合固定高度区间的场景；
3. 若高度范围不确定，且可能存在大于3个不同高度的场景，不建议使用detents属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SheetTransitionExample {
5. @State isShow: boolean = false;

7. @Builder
8. myBuilder() {
9. Column() {
10. Button("content1")
11. .margin(10)
12. .fontSize(20)

14. Button("content2")
15. .margin(10)
16. .fontSize(20)
17. }
18. .width('100%')
19. }

21. build() {
22. Column() {
23. Button("transition modal 1")
24. .onClick(() => {
25. this.isShow = true;
26. })
27. .fontSize(20)
28. .margin(10)
29. .bindSheet($$this.isShow, this.myBuilder(), {
30. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
31. blurStyle: BlurStyle.Thick,
32. showClose: true,
33. title: { title: "title", subtitle: "subtitle" },
34. })
35. }
36. .justifyContent(FlexAlign.Start)
37. .width('100%')
38. .height('100%')
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/E7uB2212S1CTtcANciABbA/zh-cn_image_0000002558606430.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=6B0808F6A9900701AC5D9E6E9FCB0A22DCB0B02C5FA828F396C04C9AE8C65917)

### 示例3（使用边框宽度和颜色）

bindSheet属性的borderWidth、borderColor属性值使用LocalizedEdgeWidths类型和LocalizedEdgeColors类型。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SheetTransitionExample {
7. @State isShow: boolean = false;

9. @Builder
10. myBuilder() {
11. Column() {
12. Button("content1")
13. .margin(10)
14. .fontSize(20)

16. Button("content2")
17. .margin(10)
18. .fontSize(20)
19. }
20. .width('100%')
21. }

23. build() {
24. Column() {
25. Button("transition modal 1")
26. .onClick(() => {
27. this.isShow = true;
28. })
29. .fontSize(20)
30. .margin(10)
31. .bindSheet($$this.isShow, this.myBuilder(), {
32. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
33. backgroundColor: Color.Gray,
34. blurStyle: BlurStyle.Thick,
35. showClose: true,
36. title: { title: "title", subtitle: "subtitle" },
37. borderWidth: { top: LengthMetrics.vp(10), start: LengthMetrics.vp(10), end: LengthMetrics.vp(20) },
38. borderColor: { top: Color.Pink, start: Color.Blue, end: Color.Yellow },
39. })
40. }
41. .justifyContent(FlexAlign.Start)
42. .width('100%')
43. .height('100%')
44. }
45. }
```

从左至右显示语言模式示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/PuJftiycQGef1P1OkgpLgA/zh-cn_image_0000002589325957.png?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=269C9574C96CA10792332A1910F0BBC3C1F2A481F40F082BA031B60D89A99C30)

从右至左显示语言模式示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/H4Xd2BFzSledZpkVgfY07Q/zh-cn_image_0000002589245899.png?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=EDCEF43E9FDDCD9EE6E5EF121EC483BC3D341584B00B61C3AD682FFA8364980F)

### 示例4（使用关闭回调函数）

bindSheet注册onWillDismiss与onWillSpringBackWhenDismiss。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct bindSheetExample {
5. @State isShow: boolean = false;

7. @Builder
8. myBuilder() {
9. Column() {
10. Button("CONTEXT")
11. .margin(10)
12. .fontSize(20)
13. }
14. }

16. build() {
17. Column() {
18. Button("NoRegisterSpringback")
19. .onClick(() => {
20. this.isShow = true;
21. })
22. .fontSize(20)
23. .margin(10)
24. .bindSheet($$this.isShow, this.myBuilder(), {
25. height: SheetSize.MEDIUM,
26. blurStyle: BlurStyle.Thick,
27. showClose: true,
28. title: { title: "title", subtitle: "subtitle" },
29. preferType: SheetType.CENTER,

31. onWillDismiss: ((dismissSheetAction: DismissSheetAction) => {
32. if (dismissSheetAction.reason == DismissReason.SLIDE_DOWN) {
33. dismissSheetAction.dismiss(); // 注册dismiss行为
34. }
35. }),

37. onWillSpringBackWhenDismiss: ((SpringBackAction: SpringBackAction) => {
38. // 没有注册springBack，下拉半模态页面无回弹行为
39. // SpringBackAction.springBack();
40. }),
41. })
42. }
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/kZ8xD_SZS5ujUSTOE0a-NA/zh-cn_image_0000002558766090.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=F11FBD224B6F79C812406F28F5C40881489AC2142317D838F316190A9B19D5C8)

### 示例5（设置内容区刷新时机）

ScrollSizeMode.CONTINUOUS 持续更新内容适合detents多挡位切换场景。

建议在builder内减少UI加载耗时的操作，滑动时内容实时刷新对性能要求较高。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State isShow: boolean = false;

7. @Builder
8. myBuilder() {
9. Column() {
10. Column()
11. .backgroundColor(Color.Blue)
12. .height(200)
13. .width('100%')
14. Column()
15. .backgroundColor(Color.Green)
16. .height(200)
17. .width('100%')
18. }
19. }

21. build() {
22. Column() {
23. Button('BindSheet')
24. .onClick(() => {
25. this.isShow = true;
26. })
27. .bindSheet($$this.isShow, this.myBuilder(), {
28. detents: [300, 600, 900],
29. uiContext: this.getUIContext(),
30. mode: SheetMode.OVERLAY,
31. scrollSizeMode: ScrollSizeMode.CONTINUOUS,
32. backgroundColor: Color.Orange,
33. title: { title: 'Title', subtitle: 'Subtitle' }
34. })
35. }
36. .justifyContent(FlexAlign.Center)
37. .width('100%')
38. .height('100%')
39. }
40. }
```

跟手触发挡位切换时，松手才触发面板内容高度刷新

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/lOGh-HBaR4i84JIr_Nflrw/zh-cn_image_0000002558606432.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=AA7583AB228CECB25C1F7722C855F823B6C5B16C7774F7E09014E88099D5F377)

跟手触发挡位切换时，跟手时期就会触发面板内容高度刷新

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/KBdFUYRwRteZo_jR5iU8yQ/zh-cn_image_0000002589325959.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=C5A5BCB6D2F5143FB886AABE726A6AADDF3C87F06A1DD55C3D091A539B88B017)

### 示例6（设置压缩模态内容）

通过设置SheetKeyboardAvoidMode为RESIZE\_ONLY，当键盘高度变化时，根据高度变化实现滚动组件的滚动。

```
1. // xxx.ets
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct ListenKeyboardHeightChange {
8. @State isShow: boolean = false;
9. @State avoidMode: SheetKeyboardAvoidMode = SheetKeyboardAvoidMode.RESIZE_ONLY;
10. scroller = new Scroller();
11. private arr: number[] = [0, 1, 2, 3, 4, 5, 6];
12. windowClass: window.Window | undefined = undefined;

14. aboutToAppear(): void {
15. try {
16. window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
17. const errCode: number = err.code;
18. if (errCode) {
19. console.error(`Failed to obtain the top window, Cause code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. this.windowClass = data;
23. try {
24. if (this.windowClass !== undefined) {
25. console.info('success in listen height change');
26. this.windowClass.on('keyboardHeightChange', this.callback);
27. }
28. } catch (exception) {
29. console.error(`Failed to enable the listener for keyboard height changes, Cause code: ${exception.code}, message: ${exception.message}`);
30. }
31. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
32. });
33. } catch (exception) {
34. console.error(`Failed to obtain the top window, Cause code: ${exception.code}, message: ${exception.message}`);
35. }
36. }

38. callback = (height: number) => {
39. console.info('height change: ' + height);
40. if (height !== 0) {
41. this.scroller.scrollTo({
42. xOffset: 0, yOffset: height + this.scroller.currentOffset().yOffset,
43. animation: { duration: 1000, curve: Curve.Ease, canOverScroll: false }
44. });
45. }
46. }

48. @Builder
49. myBuilder() {
50. Scroll(this.scroller) {
51. Column() {
52. ForEach(this.arr, (item: number) => {
53. Row() {
54. Text(item.toString())
55. .width('80%')
56. .height(60)
57. .backgroundColor('#3366CC')
58. .borderRadius(15)
59. .fontSize(16)
60. .textAlign(TextAlign.Center)
61. .margin({ top: 5 })
62. }
63. }, (item: number) => item.toString())

65. TextInput().height('100')

67. Flex({ alignItems: ItemAlign.End }) {
68. Row() {
69. Button("click")
70. .margin(10)
71. .fontSize(20)
72. .width('45%')

74. Button("cancel")
75. .margin(10)
76. .fontSize(20)
77. .width('45%')
78. }.width('100%')
79. }.height(100)
80. }.margin({ right: 15, bottom: 50 })
81. }
82. .height('100%')
83. .scrollBar(BarState.On)
84. .scrollable(ScrollDirection.Vertical)
85. }

87. build() {
88. Column() {
89. Button("transition modal 1")
90. .onClick(() => {
91. this.isShow = true;
92. })
93. .fontSize(20)
94. .margin(10)
95. .bindSheet($$this.isShow, this.myBuilder(), {
96. height: 750,
97. backgroundColor: Color.Gray,
98. blurStyle: BlurStyle.Thick,
99. showClose: true,
100. title: { title: "title", subtitle: "subtitle" },
101. keyboardAvoidMode: SheetKeyboardAvoidMode.RESIZE_ONLY,
102. })
103. }
104. .justifyContent(FlexAlign.Start)
105. .width('100%')
106. .height('100%')
107. }
108. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ouKT22OORCSMzWXzENS0IA/zh-cn_image_0000002589245901.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=B3FBB8A86AEFAB60C608F0DA073361A07947DC3B5290410B399543895972F208)

### 示例7（镜像场景下如何设置圆角属性）

此示例为说明镜像场景而设置了不同的圆角半径，通常不建议开发者设置不同的值，会造成视觉体验不佳。

其中，从API version 15开始，半模态的radius属性值使用LocalizedBorderRadiuses类型。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SheetTransitionExample {
6. @State isShow: boolean = false;

8. @Builder
9. myBuilder() {
10. Column() {
11. Button("content1")
12. .margin(10)
13. .fontSize(20)

15. Button("content2")
16. .margin(10)
17. .fontSize(20)
18. }
19. .width('100%')
20. }

22. build() {
23. Column() {
24. Button("transition modal 1")
25. .onClick(() => {
26. this.isShow = true;
27. })
28. .fontSize(20)
29. .margin(10)
30. .bindSheet($$this.isShow, this.myBuilder(), {
31. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 200],
32. title: { title: "title", subtitle: "subtitle" },
33. radius: { topStart: LengthMetrics.vp(50), topEnd: LengthMetrics.vp(10) },
34. })
35. }
36. .justifyContent(FlexAlign.Start)
37. .width('100%')
38. .height('100%')
39. }
40. }
```

从左至右显示语言模式示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/IMgU-7CXQ2CBQiLx22506g/zh-cn_image_0000002558766092.png?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=8A40CEAA49CA3D450AB072DBD53FDD956D155886D5C8E36C2241642A62E69498)

从右至左显示语言模式示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/NrQ4IA39RluOCo9Anyi-zA/zh-cn_image_0000002558606434.png?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=3149669F75F22021CF7BCE71F0D41A81F94F1A535E0F8F75AB871C3919AB02BE)

### 示例8（半模态Side侧边样式）

从API version 20开始，此示例实现半模态侧边样式。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SheetSideExample {
6. @State isShowSide: boolean = false;
7. @State enableOutsideInteractive: boolean = false;
8. @State borderWidths: LocalizedEdgeWidths | undefined = undefined;
9. @State borderColors: Resource | undefined = undefined;
10. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];

12. @Builder
13. sideBuilder() {
14. Column() {
15. ForEach(this.arr, (item: number) => {
16. Row() {
17. Text(item.toString())
18. .width('90%')
19. .height(60)
20. .backgroundColor('#3366CC')
21. .borderRadius(15)
22. .fontSize(16)
23. .textAlign(TextAlign.Center)
24. .margin({ top: 5 })
25. }
26. }, (item: number) => item.toString())
27. TextInput()
28. .margin({ top: 5 })
29. Text('改变半模态交互模式')
30. .fontSize(22).fontColor(0xFFFFFF).fontWeight(FontWeight.Bold).textAlign(TextAlign.Center)
31. .width('100%').height(50).backgroundColor('#2ebd82')
32. Button("change enableOutsideInteractive = " + this.enableOutsideInteractive)
33. .margin({ top: 5 })
34. .onClick(() => {
35. this.enableOutsideInteractive = !this.enableOutsideInteractive;
36. if (this.enableOutsideInteractive) {
37. this.borderWidths = {start : LengthMetrics.vp(1)};
38. this.borderColors = $r('sys.color.comp_divider');
39. } else {
40. this.borderWidths = undefined;
41. this.borderColors = undefined;
42. }
43. })
44. }
45. .width('100%')
46. .height('auto')
47. }

50. build() {
51. Column({space:3}) {
52. Button("半模态弹窗-Side")
53. .onClick(() => {
54. this.isShowSide = true;
55. })
56. .fontSize(20)
57. .margin(10)
58. .bindSheet($$this.isShowSide, this.sideBuilder(), {
59. title: { title: "SideSheet", subtitle: "默认宽度" },
60. backgroundColor: Color.Grey,
61. onWillAppear: () => {
62. console.info("SideSheet onWillAppear.");
63. },
64. onAppear: () => {
65. console.info("SideSheet onAppear.");
66. },
67. onWillDisappear: () => {
68. console.info("SideSheet onWillDisappear.");
69. },
70. onDisappear: () => {
71. console.info("SideSheet onDisappear.");
72. },

74. preferType: SheetType.SIDE,  // SheetType.SIDE
75. blurStyle: BlurStyle.Regular,
76. maskColor: "#4bffc62d",  // 自定义蒙层颜色
77. enableOutsideInteractive: this.enableOutsideInteractive,

79. borderWidth: this.borderWidths,
80. borderColor: this.borderColors,

82. onHeightDidChange: (height: number) => {
83. console.info("SideSheet height change:" + height);
84. },
85. onTypeDidChange: (type: SheetType) => {
86. console.info("SideSheet type change:" + type);
87. },
88. })
89. }
90. .justifyContent(FlexAlign.Center)
91. .width('100%')
92. .height('100%')
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/95hBR_m6Rf6bPwvMHE2kbw/zh-cn_image_0000002589325961.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=D8B0014D356C59DD494493E4664E17F2C7311EED9947BAC16DEA8FFCF3AC03F5)

### 示例9（半模态ContentCover全屏样式）

从API version 20开始，此示例实现半模态的全屏显示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ContentCoverExample {
5. @State isShow: boolean = false

7. @Builder
8. myBuilder() {
9. Column() {
10. Button("Close Content Cover Sheet")
11. .margin(10)
12. .fontSize(20)
13. .onClick(() => {
14. this.isShow = false;
15. })
16. }
17. .width('100%')
18. .height('100%')
19. .justifyContent(FlexAlign.Center)
20. }

22. build() {
23. Column() {
24. Button("Show Content Cover Sheet")
25. .onClick(() => {
26. this.isShow = true
27. })
28. .fontSize(20)
29. .margin(10)
30. .bindSheet(this.isShow, this.myBuilder(), {
31. modalTransition: ModalTransition.DEFAULT,
32. preferType: SheetType.CONTENT_COVER,
33. backgroundColor: '#ffd5d5d5',
34. maskColor: '#ff707070',
35. onWillAppear: () => {
36. console.info("ContentCover onWillAppear.")
37. },
38. onAppear: () => {
39. console.info("ContentCover onAppear.")
40. },
41. onWillDisappear: () => {
42. console.info("ContentCover onWillDisappear.")
43. },
44. onDisappear: () => {
45. console.info("ContentCover onDisappear.")
46. },
47. })
48. }
49. .justifyContent(FlexAlign.Center)
50. .backgroundColor(Color.White)
51. .width('100%')
52. .height('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/-t1tG46mQryBlgYQ-Nbymw/zh-cn_image_0000002589245903.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055128Z&HW-CC-Expire=86400&HW-CC-Sign=486F35050998983F469B28F6519533F6BABEA6003E7F8F269DD13728C4FC384A)
