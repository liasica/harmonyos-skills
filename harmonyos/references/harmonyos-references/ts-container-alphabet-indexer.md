---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer
title: AlphabetIndexer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > AlphabetIndexer
category: harmonyos-references
scraped_at: 2026-04-29T13:52:20+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:8dfba3bad3d0ef8940067e3ab0c80bc2f9c6784c4ce8cb2da89122b78bf7d3a3
---

可以与容器组件联动用于按逻辑结构快速定位容器显示区域的组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

AlphabetIndexer(options: AlphabetIndexerOptions)

创建索引条组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AlphabetIndexerOptions](ts-container-alphabet-indexer.md#alphabetindexeroptions18对象说明) | 是 | 设置索引条组件参数。 |

## AlphabetIndexerOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于设置索引条参数。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| arrayValue7+ | Array<string> | 否 | 否 | 字符串数组，每个字符串代表一个索引项。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected7+ | number | 否 | 否 | 初始选中项索引值，若超出索引值范围，则取默认值0。与[selected](ts-container-alphabet-indexer.md#selected8)属性同时设置时，selected属性的优先级较高。  取值范围：[0, arrayValue.length-1]  该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

[width](ts-universal-attributes-size.md#width)属性设置"auto"时表示自适应宽度，宽度会随索引项最大宽度变化。

[padding](ts-universal-attributes-size.md#padding)属性默认为4vp。

文本最大的字体缩放倍数[maxFontScale](ts-basic-components-text.md#maxfontscale12)和最小的字体缩放倍数[minFontScale](ts-basic-components-text.md#minfontscale12)皆为1，不跟随系统字体大小调节变化。

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(value: ResourceColor)

设置未选中项文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 未选中项文本颜色。  默认值：0x99182431，显示为略带透明的棕色。 |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置选中项文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 选中项文本颜色。  默认值：0xFF007DFF，显示为蓝色。 |

### popupColor

PhonePC/2in1TabletTVWearable

popupColor(value: ResourceColor)

设置提示弹窗一级索引项文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 提示弹窗一级索引项文本颜色。  默认值：0xFF007DFF，显示为蓝色。 |

### selectedBackgroundColor

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(value: ResourceColor)

设置选中项背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 选中项背景颜色。  默认值：0x1A007DFF，显示为半透明的蓝绿色。 |

### popupBackground

PhonePC/2in1TabletTVWearable

popupBackground(value: ResourceColor)

设置提示弹窗背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 提示弹窗背景颜色。  弹窗的背景模糊材质效果会对背景色产生影响，可通过设置[popupBackgroundBlurStyle](ts-container-alphabet-indexer.md#popupbackgroundblurstyle12)属性值为NONE关闭背景模糊材质效果。  默认值：  API version 11及以前：0xFFFFFFFF，显示为白色。  API version 12及以后：#66808080，显示为半透明的灰色。 |

### usingPopup

PhonePC/2in1TabletTVWearable

usingPopup(value: boolean)

设置是否显示提示弹窗。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否显示提示弹窗。  默认值：false  true：显示提示弹窗。  false：不显示提示弹窗。 |

### selectedFont

PhonePC/2in1TabletTVWearable

selectedFont(value: Font)

设置选中项文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 选中项文本样式。  默认值：  API version 11及以前：  {  size:'12.0fp',  style:FontStyle.Normal,  weight:FontWeight.Regular,  family:'HarmonyOS Sans'  }  API version 12及以后：  {  size:'10.0vp',  style:FontStyle.Normal,  weight:FontWeight.Medium,  family:'HarmonyOS Sans'  } |

### popupFont

PhonePC/2in1TabletTVWearable

popupFont(value: Font)

设置提示弹窗一级索引文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 提示弹窗一级索引文本样式。  默认值：  {  size:'24.0vp',  style:FontStyle.Normal,  weight:FontWeight.Medium,  family:'HarmonyOS Sans'  } |

### font

PhonePC/2in1TabletTVWearable

font(value: Font)

设置未选中项文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 未选中索引项文本样式。  默认值：  API version 11及以前：  {  size:'12.0fp',  style:FontStyle.Normal,  weight:FontWeight.Regular,  family:'HarmonyOS Sans'  }  API version 12及以后：  {  size:'10.0vp',  style:FontStyle.Normal,  weight:FontWeight.Medium,  family:'HarmonyOS Sans'  } |

### itemSize

PhonePC/2in1TabletTVWearable

itemSize(value: string | number)

设置索引项区域大小。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | number | 是 | 索引项区域大小，索引项区域为正方形，即正方形边长。不支持设置为百分比。  实际取值会受到组件尺寸的约束，索引项宽度最大为组件宽度-左右[padding](ts-universal-attributes-size.md#padding)，索引项高度最大为（组件高度-上下[padding](ts-universal-attributes-size.md#padding)）/索引项个数。传入值小于等于0时，按照默认值处理。  默认值：16.0  单位：vp |

### alignStyle

PhonePC/2in1TabletTVWearable

alignStyle(value: IndexerAlign, offset?: Length)

设置索引条提示弹窗的对齐样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [IndexerAlign](ts-container-alphabet-indexer.md#indexeralign枚举说明) | 是 | 索引条提示弹窗的对齐样式，支持弹窗显示在索引条右侧和左侧。  默认值：IndexerAlign.END |
| offset10+ | [Length](ts-types.md#length) | 否 | 提示弹窗与索引条之间间距，大于等于0为有效值，在不设置或设置为小于0的情况下间距与popupPosition.x相同。与[popupPosition](ts-container-alphabet-indexer.md#popupposition8)同时设置时，水平方向上offset生效，竖直方向上popupPosition.y生效。 |

### selected8+

PhonePC/2in1TabletTVWearable

selected(index: number)

设置选中项索引值。

从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项索引值。  取值范围：[0, [arrayValue](ts-container-alphabet-indexer.md#alphabetindexeroptions18对象说明).length-1]  默认值：0 |

### popupPosition8+

PhonePC/2in1TabletTVWearable

popupPosition(value: Position)

设置弹出窗口相对于索引条上边框中点的位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | 是 | 弹出窗口相对于索引条上边框中点的位置。  默认值：{x: 60.0, y: 48.0} |

### popupSelectedColor10+

PhonePC/2in1TabletTVWearable

popupSelectedColor(value: ResourceColor)

设置提示弹窗二级索引选中项文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 提示弹窗二级索引选中项文本颜色。  默认值：#FF182431，显示为深暗蓝色。 |

### popupUnselectedColor10+

PhonePC/2in1TabletTVWearable

popupUnselectedColor(value: ResourceColor)

设置提示弹窗二级索引未选中项文本颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 提示弹窗二级索引未选中项文本颜色。  默认值：#FF182431，显示为深暗蓝色。 |

### popupItemFont10+

PhonePC/2in1TabletTVWearable

popupItemFont(value: Font)

设置提示弹窗二级索引项文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 提示弹窗二级索引项文本样式。  默认值：  {  size:24,  weight:FontWeight.Medium  } |

### popupItemBackgroundColor10+

PhonePC/2in1TabletTVWearable

popupItemBackgroundColor(value: ResourceColor)

设置提示弹窗二级索引项背景颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 提示弹窗二级索引项背景颜色。  默认值：  API version 11及以前：#FFFFFFFF，显示为白色。  API version 12及以后：#00000000，显示为透明色。 |

### autoCollapse11+

PhonePC/2in1TabletTVWearable

autoCollapse(value: boolean)

设置是否使用自适应折叠模式。

如果索引项第一项为“#”，当除去第一项后剩余索引项数量 <= 9时，选择全显示模式；9 < 剩余索引项数量 <= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式；剩余索引项数量 > 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。

如果索引项第一项不为“#”，当所有索引项数量 <= 9时，选择全显示模式；9 < 所有索引项数量 <= 13时，根据索引条高度自适应选择全显示模式或者短折叠模式；所有索引项数量 > 13时，根据索引条高度自适应选择短折叠模式或者长折叠模式。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否使用自适应折叠模式。  默认值：  API version 12之前：false  API version 12及之后：true  true：使用自适应折叠模式。  false：不使用自适应折叠模式。 |

### popupItemBorderRadius12+

PhonePC/2in1TabletTVWearable

popupItemBorderRadius(value: number)

设置提示弹窗索引项背板圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置提示弹窗索引项背板圆角半径。  默认值：24vp  不支持百分比，小于0时按照0设置。  提示弹窗背板圆角自适应变化（索引项圆角半径+4vp）。 |

### itemBorderRadius12+

PhonePC/2in1TabletTVWearable

itemBorderRadius(value: number)

设置索引项背板圆角半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置索引项背板圆角半径。  默认值：8vp  不支持百分比，小于0时按照0设置。  索引条背板圆角自适应变化（索引项圆角半径+4vp）。 |

### popupBackgroundBlurStyle12+

PhonePC/2in1TabletTVWearable

popupBackgroundBlurStyle(value: BlurStyle)

设置提示弹窗的背景模糊材质。未通过该接口设置时，默认为组件普通材质模糊，对应取值为BlurStyle中的COMPONENT\_REGULAR。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 是 | 设置提示弹窗的背景模糊材质。  弹窗的背景模糊材质效果会对背景色[popupBackground](ts-container-alphabet-indexer.md#popupbackground)产生影响，可通过设置属性值为NONE关闭背景模糊材质效果。 |

### popupTitleBackground12+

PhonePC/2in1TabletTVWearable

popupTitleBackground(value: ResourceColor)

设置提示弹窗一级索引项背景颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置提示弹窗一级索引项背景颜色。  默认值：  提示弹窗只有一个索引项：#00FFFFFF。  提示弹窗有多个索引项：#0c182431。 |

### enableHapticFeedback12+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(value: boolean)

设置是否开启触控反馈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否支持触控反馈。  true：支持触控反馈。  false：不支持触控反馈。  默认值：true  开启触控反馈时，需要在工程的[module.json5](../harmonyos-guides/module-configuration-file.md)中配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |

## IndexerAlign枚举说明

PhonePC/2in1TabletTVWearable

索引条提示弹窗的对齐样式枚举。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Left | 0 | 提示弹窗显示在索引条右侧。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Right | 1 | 提示弹窗显示在索引条左侧。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| START12+ | 2 | 在从左到右（LTR）场景下，提示弹窗显示在索引条右侧的位置。在RTL场景下，提示弹窗显示在索引条左侧的位置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| END12+ | 3 | 在从左到右（LTR）场景下，提示弹窗显示在索引条左侧的位置。在RTL场景下，提示弹窗显示在索引条右侧的位置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onSelected(deprecated)

PhonePC/2in1TabletTVWearable

onSelected(callback: (index: number) => void)

索引项选中事件，回调参数为当前选中项索引。

说明

从API version 7开始支持，从API version 8开始废弃，建议使用[onSelect](ts-container-alphabet-indexer.md#onselect8)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前选中的索引。 |

### onSelect8+

PhonePC/2in1TabletTVWearable

onSelect(callback: OnAlphabetIndexerSelectCallback)

索引项选中事件，回调参数为当前选中项索引。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerSelectCallback](ts-container-alphabet-indexer.md#onalphabetindexerselectcallback18) | 是 | 索引项选中事件。 |

### onRequestPopupData8+

PhonePC/2in1TabletTVWearable

onRequestPopupData(callback: OnAlphabetIndexerRequestPopupDataCallback)

设置提示弹窗二级索引项内容事件，回调参数为当前选中项索引，回调返回值为提示弹窗需显示的二级索引项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerRequestPopupDataCallback](ts-container-alphabet-indexer.md#onalphabetindexerrequestpopupdatacallback18) | 是 | 设置提示弹窗二级索引项内容事件。 |

### onPopupSelect8+

PhonePC/2in1TabletTVWearable

onPopupSelect(callback: OnAlphabetIndexerPopupSelectCallback)

提示弹窗二级索引选中事件，回调参数为当前选中二级索引项索引。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnAlphabetIndexerPopupSelectCallback](ts-container-alphabet-indexer.md#onalphabetindexerpopupselectcallback18) | 是 | 提示弹窗二级索引选中事件。 |

## OnAlphabetIndexerSelectCallback18+

PhonePC/2in1TabletTVWearable

type OnAlphabetIndexerSelectCallback = (index: number) => void

索引项被选中时触发的事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前选中索引项的索引。 |

## OnAlphabetIndexerPopupSelectCallback18+

PhonePC/2in1TabletTVWearable

type OnAlphabetIndexerPopupSelectCallback = (index: number) => void

提示弹窗二级索引项被选中时触发的事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前选中的提示弹窗二级索引项的索引。 |

## OnAlphabetIndexerRequestPopupDataCallback18+

PhonePC/2in1TabletTVWearable

type OnAlphabetIndexerRequestPopupDataCallback = (index: number) => Array<string>

[usingPopup](ts-container-alphabet-indexer.md#usingpopup)设置值为true，索引项被选中时触发的事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前选中索引项的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 索引项对应的提示弹窗二级索引字符串数组，此字符串数组在弹窗中竖排显示，字符串列表最多显示5个，超出部分可以滑动显示。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置提示弹窗显示文本内容）

通过[onRequestPopupData](ts-container-alphabet-indexer.md#onrequestpopupdata8)事件自定义提示弹窗显示文本内容。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlphabetIndexerSample {
5. private arrayA: string[] = ['安'];
6. private arrayB: string[] = ['卜', '白', '包', '毕', '丙'];
7. private arrayC: string[] = ['曹', '成', '陈', '催'];
8. private arrayL: string[] = ['刘', '李', '楼', '梁', '雷', '吕', '柳', '卢'];
9. private value: string[] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
10. 'H', 'I', 'J', 'K', 'L', 'M', 'N',
11. 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
12. 'V', 'W', 'X', 'Y', 'Z'];

14. build() {
15. Stack({ alignContent: Alignment.Start }) {
16. Row() {
17. List({ space: 20, initialIndex: 0 }) {
18. ForEach(this.arrayA, (item: string) => {
19. ListItem() {
20. Text(item)
21. .width('80%')
22. .height('5%')
23. .fontSize(30)
24. .textAlign(TextAlign.Center)
25. }
26. }, (item: string) => item)

28. ForEach(this.arrayB, (item: string) => {
29. ListItem() {
30. Text(item)
31. .width('80%')
32. .height('5%')
33. .fontSize(30)
34. .textAlign(TextAlign.Center)
35. }
36. }, (item: string) => item)

38. ForEach(this.arrayC, (item: string) => {
39. ListItem() {
40. Text(item)
41. .width('80%')
42. .height('5%')
43. .fontSize(30)
44. .textAlign(TextAlign.Center)
45. }
46. }, (item: string) => item)

48. ForEach(this.arrayL, (item: string) => {
49. ListItem() {
50. Text(item)
51. .width('80%')
52. .height('5%')
53. .fontSize(30)
54. .textAlign(TextAlign.Center)
55. }
56. }, (item: string) => item)
57. }
58. .width('50%')
59. .height('100%')

61. AlphabetIndexer({ arrayValue: this.value, selected: 0 })
62. .autoCollapse(false) // 关闭自适应折叠模式
63. .enableHapticFeedback(false) // 关闭触控反馈
64. .selectedColor(0xFFFFFF) // 选中项文本颜色
65. .popupColor(0xFFFAF0) // 提示弹窗一级索引文本颜色
66. .selectedBackgroundColor(0xCCCCCC) // 选中项背景颜色
67. .popupBackground(0xD2B48C) // 提示弹窗背景颜色
68. .usingPopup(true) // 索引项被选中时显示提示弹窗
69. .selectedFont({ size: 16, weight: FontWeight.Bolder }) // 选中项文本样式
70. .popupFont({ size: 30, weight: FontWeight.Bolder }) // 提示弹窗一级索引的文本样式
71. .itemSize(28) // 索引项的尺寸大小
72. .alignStyle(IndexerAlign.Left) // 提示弹窗在索引条右侧弹出
73. .popupItemBorderRadius(24) // 设置提示弹窗索引项背板圆角半径
74. .itemBorderRadius(14) // 设置索引项背板圆角半径
75. .popupBackgroundBlurStyle(BlurStyle.NONE) // 设置提示弹窗的背景模糊材质
76. .popupTitleBackground(0xCCCCCC) // 设置提示弹窗一级索引项背景颜色
77. .popupSelectedColor(0x00FF00) // 提示弹窗二级索引选中项文本颜色
78. .popupUnselectedColor(0x0000FF) // 提示弹窗二级索引未选中项文本颜色
79. .popupItemFont({ size: 30, style: FontStyle.Normal }) // 提示弹窗二级索引项文本样式
80. .popupItemBackgroundColor(0xCCCCCC) // 提示弹窗二级索引项背景颜色
81. .onSelect((index: number) => {
82. console.info(this.value[index] + ' Selected!');
83. })
84. .onRequestPopupData((index: number) => {
85. // 当选中A时，提示弹窗里面的二级索引文本列表显示A对应的列表arrayA，选中B、C、L时也同样
86. // 选中其余索引项时，提示弹窗二级索引文本列表为空，提示弹窗会只显示一级索引项
87. if (this.value[index] == 'A') {
88. return this.arrayA;
89. } else if (this.value[index] == 'B') {
90. return this.arrayB;
91. } else if (this.value[index] == 'C') {
92. return this.arrayC;
93. } else if (this.value[index] == 'L') {
94. return this.arrayL;
95. } else {
96. return [];
97. }
98. })
99. .onPopupSelect((index: number) => {
100. console.info('onPopupSelected:' + index);
101. })
102. }
103. .width('100%')
104. .height('100%')
105. }
106. }
107. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/WyBgvw3ERA6qaygpi5zBfw/zh-cn_image_0000002589326291.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055215Z&HW-CC-Expire=86400&HW-CC-Sign=DF2BD71D57B9012A956D29C3272C3E9200864E40E9CF2221345FBB76F76C7575)

### 示例2（开启自适应折叠模式）

通过[autoCollapse](ts-container-alphabet-indexer.md#autocollapse11)属性开启自适应折叠模式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlphabetIndexerSample {
5. private arrayA: string[] = ['安'];
6. private arrayB: string[] = ['卜', '白', '包', '毕', '丙'];
7. private arrayC: string[] = ['曹', '成', '陈', '催'];
8. private arrayJ: string[] = ['嘉', '贾'];
9. private value: string[] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
10. 'H', 'I', 'J', 'K', 'L', 'M', 'N',
11. 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
12. 'V', 'W', 'X', 'Y', 'Z'];
13. @State isNeedAutoCollapse: boolean = false;
14. @State indexerHeight: string = '75%';

16. build() {
17. Stack({ alignContent: Alignment.Start }) {
18. Row() {
19. List({ space: 20, initialIndex: 0 }) {
20. ForEach(this.arrayA, (item: string) => {
21. ListItem() {
22. Text(item)
23. .width('80%')
24. .height('5%')
25. .fontSize(30)
26. .textAlign(TextAlign.Center)
27. }
28. }, (item: string) => item)

30. ForEach(this.arrayB, (item: string) => {
31. ListItem() {
32. Text(item)
33. .width('80%')
34. .height('5%')
35. .fontSize(30)
36. .textAlign(TextAlign.Center)
37. }
38. }, (item: string) => item)

40. ForEach(this.arrayC, (item: string) => {
41. ListItem() {
42. Text(item)
43. .width('80%')
44. .height('5%')
45. .fontSize(30)
46. .textAlign(TextAlign.Center)
47. }
48. }, (item: string) => item)

50. ForEach(this.arrayJ, (item: string) => {
51. ListItem() {
52. Text(item)
53. .width('80%')
54. .height('5%')
55. .fontSize(30)
56. .textAlign(TextAlign.Center)
57. }
58. }, (item: string) => item)
59. }
60. .width('50%')
61. .height('100%')

63. Column() {
64. Column() {
65. AlphabetIndexer({ arrayValue: this.value, selected: 0 })
66. .autoCollapse(this.isNeedAutoCollapse) // 开启或关闭自适应折叠模式
67. .height(this.indexerHeight) // 索引条高度
68. .enableHapticFeedback(false) // 关闭触控反馈
69. .selectedColor(0xFFFFFF) // 选中项文本颜色
70. .popupColor(0xFFFAF0) // 提示弹窗一级索引文本颜色
71. .selectedBackgroundColor(0xCCCCCC) // 选中项背景颜色
72. .popupBackground(0xD2B48C) // 提示弹窗背景颜色
73. .usingPopup(true) // 索引项被选中时显示提示弹窗
74. .selectedFont({ size: 16, weight: FontWeight.Bolder }) // 选中项文本样式
75. .popupFont({ size: 30, weight: FontWeight.Bolder }) // 提示弹窗内容的文本样式
76. .itemSize(28) // 每一项的尺寸大小
77. .alignStyle(IndexerAlign.Right) // 提示弹窗在索引条左侧弹出
78. .popupTitleBackground("#D2B48C") // 设置提示弹窗一级索引项背景颜色
79. .popupSelectedColor(0x00FF00) // 提示弹窗二级索引选中项文本颜色
80. .popupUnselectedColor(0x0000FF) // 提示弹窗二级索引未选中项文本颜色
81. .popupItemFont({ size: 30, style: FontStyle.Normal }) // 提示弹窗二级索引项文本样式
82. .popupItemBackgroundColor(0xCCCCCC) // 提示弹窗二级索引项背景颜色
83. .onSelect((index: number) => {
84. console.info(this.value[index] + ' Selected!');
85. })
86. .onRequestPopupData((index: number) => {
87. // 当选中A时，提示弹窗里面的二级索引文本列表显示A对应的列表arrayA，选中B、C、J时也同样
88. // 选中其余索引项时，提示弹窗二级索引文本列表为空，提示弹窗会只显示一级索引项
89. if (this.value[index] == 'A') {
90. return this.arrayA;
91. } else if (this.value[index] == 'B') {
92. return this.arrayB;
93. } else if (this.value[index] == 'C') {
94. return this.arrayC;
95. } else if (this.value[index] == 'J') {
96. return this.arrayJ;
97. } else {
98. return [];
99. }
100. })
101. .onPopupSelect((index: number) => {
102. console.info('onPopupSelected:' + index);
103. })
104. }
105. .height('80%')
106. .justifyContent(FlexAlign.Center)

108. Column() {
109. Button('切换成折叠模式')
110. .margin('5vp')
111. .onClick(() => {
112. this.isNeedAutoCollapse = true;
113. })
114. Button('切换索引条高度到30%')
115. .margin('5vp')
116. .onClick(() => {
117. this.indexerHeight = '30%';
118. })
119. Button('切换索引条高度到70%')
120. .margin('5vp')
121. .onClick(() => {
122. this.indexerHeight = '70%';
123. })
124. }.height('20%')
125. }
126. .width('50%')
127. .justifyContent(FlexAlign.Center)
128. }
129. .width('100%')
130. .height(720)
131. }
132. }
133. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/3VccQO-0TfuVGlkcJcRFKQ/zh-cn_image_0000002589246233.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055215Z&HW-CC-Expire=86400&HW-CC-Sign=409809156A68F5224C07BFD15674FE272C8AEDBB36E1E6A464F1D029516A27C5)

### 示例3（设置提示弹窗背景模糊材质）

通过[popupBackgroundBlurStyle](ts-container-alphabet-indexer.md#popupbackgroundblurstyle12)属性实现提示弹窗的背景模糊效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AlphabetIndexerSample {
5. private arrayA: string[] = ['安'];
6. private arrayB: string[] = ['卜', '白', '包', '毕', '丙'];
7. private arrayC: string[] = ['曹', '成', '陈', '催'];
8. private arrayL: string[] = ['刘', '李', '楼', '梁', '雷', '吕', '柳', '卢'];
9. private value: string[] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
10. 'H', 'I', 'J', 'K', 'L', 'M', 'N',
11. 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
12. 'V', 'W', 'X', 'Y', 'Z'];
13. @State customBlurStyle: BlurStyle = BlurStyle.NONE;

15. build() {
16. Stack({ alignContent: Alignment.Start }) {
17. Row() {
18. List({ space: 20, initialIndex: 0 }) {
19. ForEach(this.arrayA, (item: string) => {
20. ListItem() {
21. Text(item)
22. .width('80%')
23. .height('5%')
24. .fontSize(30)
25. .textAlign(TextAlign.Center)
26. }
27. }, (item: string) => item)

29. ForEach(this.arrayB, (item: string) => {
30. ListItem() {
31. Text(item)
32. .width('80%')
33. .height('5%')
34. .fontSize(30)
35. .textAlign(TextAlign.Center)
36. }
37. }, (item: string) => item)

39. ForEach(this.arrayC, (item: string) => {
40. ListItem() {
41. Text(item)
42. .width('80%')
43. .height('5%')
44. .fontSize(30)
45. .textAlign(TextAlign.Center)
46. }
47. }, (item: string) => item)

49. ForEach(this.arrayL, (item: string) => {
50. ListItem() {
51. Text(item)
52. .width('80%')
53. .height('5%')
54. .fontSize(30)
55. .textAlign(TextAlign.Center)
56. }
57. }, (item: string) => item)
58. }
59. .width('30%')
60. .height('100%')

62. Column() {
63. Column() {
64. Text('切换模糊材质: ')
65. .fontSize(24)
66. .fontColor(0xcccccc)
67. .width('100%')
68. Button('COMPONENT_REGULAR')
69. .margin('5vp')
70. .width(200)
71. .onClick(() => {
72. this.customBlurStyle = BlurStyle.COMPONENT_REGULAR;
73. })
74. Button('BACKGROUND_THIN')
75. .margin('5vp')
76. .width(200)
77. .onClick(() => {
78. this.customBlurStyle = BlurStyle.BACKGROUND_THIN;
79. })
80. }.height('20%')

82. Column() {
83. AlphabetIndexer({ arrayValue: this.value, selected: 0 })
84. .usingPopup(true) // 索引项被选中时显示提示弹窗
85. .alignStyle(IndexerAlign.Left) // 提示弹窗在索引条右侧弹出
86. .popupItemBorderRadius(24) // 设置提示弹窗索引项背板圆角半径
87. .itemBorderRadius(14) // 设置索引项背板圆角半径
88. .popupBackgroundBlurStyle(this.customBlurStyle) // 设置提示弹窗的背景模糊材质
89. .popupTitleBackground(0xCCCCCC) // 设置提示弹窗一级索引项背景颜色
90. .onSelect((index: number) => {
91. console.info(this.value[index] + ' Selected!');
92. })
93. .onRequestPopupData((index: number) => {
94. // 当选中A时，提示弹窗里面的二级索引文本列表显示A对应的列表arrayA，选中B、C、L时也同样
95. // 选中其余索引项时，提示弹窗二级索引文本列表为空，提示弹窗会只显示一级索引项
96. if (this.value[index] == 'A') {
97. return this.arrayA;
98. } else if (this.value[index] == 'B') {
99. return this.arrayB;
100. } else if (this.value[index] == 'C') {
101. return this.arrayC;
102. } else if (this.value[index] == 'L') {
103. return this.arrayL;
104. } else {
105. return [];
106. }
107. })
108. .onPopupSelect((index: number) => {
109. console.info('onPopupSelected:' + index);
110. })
111. }
112. .height('80%')
113. }
114. .width('70%')
115. }
116. .width('100%')
117. .height('100%')
118. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
119. .backgroundImage($r("app.media.image"))
120. }
121. }
122. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/tF816-bqS4Gco8jr0MEQlA/zh-cn_image_0000002558766426.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055215Z&HW-CC-Expire=86400&HW-CC-Sign=364957F92C41BAC40511421F1C5F63B65A0099929E44DEC3DADF7804B32EA947)
