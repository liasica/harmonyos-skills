---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton
title: ArcButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > ArcButton
category: harmonyos-references
scraped_at: 2026-04-29T13:52:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:afcc82561d8d0a468e3bed3bd3c78cf6ef8802855c9d1e738816ea3c67f51fc1
---

弧形按钮组件提供强调、普通、警告等样式按钮，推荐用于圆形屏幕的设备。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {
2. ArcButton,
3. ArcButtonOptions,
4. ArcButtonStatus,
5. ArcButtonStyleMode,
6. ArcButtonPosition,
7. }  from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## 事件

PhonePC/2in1TabletTVWearable

通用事件支持[点击事件](ts-universal-events-click.md)和[触摸事件](ts-universal-events-touch.md)。

## ArcButton

PhonePC/2in1TabletTVWearable

ArcButton({ options: ArcButtonOptions })

创建ArcButton实例，入参是弧形按钮配置选项。

**装饰器类型：** @Component

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数**：

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [ArcButtonOptions](ohos-arkui-advanced-arcbutton.md#arcbuttonoptions) | 是 | @Require | 定义ArcButton组件的文本、背景色、阴影等参数。 |

## ArcButtonOptions

PhonePC/2in1TabletTVWearable

定义ArcButton的默认样式或自定义样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [ArcButtonPosition](ohos-arkui-advanced-arcbutton.md#arcbuttonposition) | 否 | 否 | 上下弧形按钮类型属性。  默认值：ArcButtonPosition.BOTTOM\_EDGE。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| styleMode | [ArcButtonStyleMode](ohos-arkui-advanced-arcbutton.md#arcbuttonstylemode) | 否 | 否 | 弧形按钮样式模式。该样式不支持与[ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23)样式同时使用。  默认值：ArcButtonStyleMode.EMPHASIZED\_LIGHT。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| status | [ArcButtonStatus](ohos-arkui-advanced-arcbutton.md#arcbuttonstatus) | 否 | 否 | 弧形按钮状态。  默认值：ArcButtonStatus.NORMAL。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 弧形按钮显示文本。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 否 | 弧形按钮背景模糊能力。  默认值：BlurStyle.NONE。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 否 | 弧形按钮背景颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.Black。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| shadowColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 否 | 弧形按钮阴影颜色。  默认值：Color.Black。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| shadowEnabled | boolean | 否 | 否 | 弧形按钮阴影开关。  默认值：false  值为true时，显示阴影。值为false时，不显示阴影。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontSize | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 否 | 弧形按钮文本大小。  默认值：19fp。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 否 | 弧形按钮文本颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.White。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| pressedFontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 否 | 弧形按钮按下文本颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.White。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 否 | 弧形按钮文本样式。  默认值：FontStyle.Normal。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontFamily | string | [Resource](ts-types.md#resource) | 否 | 否 | 弧形按钮字体名。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontMargin | [LocalizedMargin](ts-types.md#localizedmargin12) | 否 | 否 | 弧形按钮文本边距。  默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| progressConfig23+ | [ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23) | 否 | 是 | ArcButton进度条参数。不设置该属性时ArcButton组件表现为按钮样式（[示例1](ohos-arkui-advanced-arcbutton.md#示例1-设置弧形按钮)），设置后表现为进度条样式（[示例2](ohos-arkui-advanced-arcbutton.md#示例2-设置设备进度条按钮)），进度条样式不受[ArcButtonStyleMode](ohos-arkui-advanced-arcbutton.md#arcbuttonstylemode)属性设置影响。  默认值：[ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23) 的各项子属性均取其默认值。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| onTouch | [Callback](ts-types.md#voidcallback12)< [TouchEvent](ts-universal-events-touch.md#touchevent对象说明)> | 否 | 是 | 弧形按钮手指触摸动作触发该回调。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onClick | [Callback](ts-types.md#voidcallback12)<[ClickEvent](ts-universal-events-click.md#clickevent) > | 否 | 是 | 弧形按钮点击动作触发该回调。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options: CommonArcButtonOptions)

弧形按钮的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CommonArcButtonOptions](ohos-arkui-advanced-arcbutton.md#commonarcbuttonoptions) | 是 | 定义ArcButton组件的文本、背景色、阴影等参数。 |

## CommonArcButtonOptions

PhonePC/2in1TabletTVWearable

ArcButton的默认样式或自定义样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [ArcButtonPosition](ohos-arkui-advanced-arcbutton.md#arcbuttonposition) | 否 | 是 | 上下弧形按钮类型属性。  默认值：ArcButtonPosition.BOTTOM\_EDGE。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| styleMode | [ArcButtonStyleMode](ohos-arkui-advanced-arcbutton.md#arcbuttonstylemode) | 否 | 是 | 弧形按钮样式模式。该样式不支持与[ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23)样式同时使用。  默认值：ArcButtonStyleMode.EMPHASIZED\_LIGHT。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| status | [ArcButtonStatus](ohos-arkui-advanced-arcbutton.md#arcbuttonstatus) | 否 | 是 | 弧形按钮状态。  默认值：ArcButtonStatus.NORMAL。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弧形按钮显示文本。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弧形按钮背景模糊能力。  默认值：BlurStyle.NONE。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 弧形按钮背景颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.Black。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| shadowColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 弧形按钮阴影颜色。  默认值：Color.Black。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| shadowEnabled | boolean | 否 | 是 | 弧形按钮阴影开关。  默认值：false  值为true时，显示阴影。值为false时，不显示阴影。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontSize | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 弧形按钮文本大小。  默认值：19fp。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 弧形按钮文本颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.White。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| pressedFontColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 弧形按钮按下文本颜色。  ArcButtonStyleMode需要设置为CUSTOM。  默认值：Color.White。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontStyle | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 弧形按钮文本样式。  默认值：FontStyle.Normal。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontFamily | string | [Resource](ts-types.md#resource) | 否 | 是 | 弧形按钮字体名。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| fontMargin | [LocalizedMargin](ts-types.md#localizedmargin12) | 否 | 是 | 弧形按钮文本边距。  默认值：{start:24vp, top: 10vp,end: 24vp, bottom:16vp }。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| progressConfig23+ | [ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23) | 否 | 是 | ArcButton进度条参数。不设置该属性时ArcButton组件表现为按钮样式（[示例1](ohos-arkui-advanced-arcbutton.md#示例1-设置弧形按钮)），设置后表现为进度条样式（[示例2](ohos-arkui-advanced-arcbutton.md#示例2-设置设备进度条按钮)），进度条样式不受[ArcButtonStyleMode](ohos-arkui-advanced-arcbutton.md#arcbuttonstylemode)属性设置影响。  默认值：[ArcButtonProgressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonprogressconfig23) 的各项子属性均取其默认值。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| onTouch | [Callback](ts-types.md#voidcallback12)< [TouchEvent](ts-universal-events-touch.md#touchevent对象说明)> | 否 | 是 | 弧形按钮手指触摸动作触发该回调。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onClick | [Callback](ts-types.md#voidcallback12)<[ClickEvent](ts-universal-events-click.md#clickevent) > | 否 | 是 | 弧形按钮点击动作触发该回调。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ArcButtonProgressConfig23+

PhonePC/2in1TabletTVWearable

ArcButton内进度条的参数配置。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 进度条当前值。设置小于0的数值时置为0，设置大于total的数值时置为total。  默认值：0  取值范围：[0, total] |
| total | number | 否 | 是 | 进度的最大值。  默认值：100  取值范围：[0, 2147483647]，设置0或超出取值范围取默认值为100。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 进度条前景色。如果组件设置了背景色（[backgroundColor](ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)），进度条前景色默认值取组件背景色。进度条前景色不受按钮样式（[ArcButtonStyleMode](ohos-arkui-advanced-arcbutton.md#arcbuttonstylemode)）设置影响。进度条背景色仅依赖进度条前景色设置，取进度条前景色的25%透明度。  默认值："#1F71FF"，显示为蓝色。 |

## ArcButtonPosition

PhonePC/2in1TabletTVWearable

定义ArcButton可设置的弧形按钮的类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP\_EDGE | 0 | 上弧形按钮，位于圆形屏幕上方。 |
| BOTTOM\_EDGE | 1 | 底部弧形按钮，位于圆形屏幕底部。 |

## ArcButtonStyleMode

PhonePC/2in1TabletTVWearable

定义ArcButton可设置弧形按钮样式模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EMPHASIZED\_LIGHT | 0 | 强调样式，亮色，表现为蓝色背景、白色文字。 |
| EMPHASIZED\_DARK | 1 | 警告样式，暗色，表现为红色背景、白色文字。 |
| NORMAL\_LIGHT | 2 | 常规样式，亮色，表现为深蓝色背景、蓝色文字。 |
| NORMAL\_DARK | 3 | 常规样式，暗色，表现为深灰色背景、蓝色文字。 |
| CUSTOM | 4 | 自定义按钮颜色和字体颜色。 |

## ArcButtonStatus

PhonePC/2in1TabletTVWearable

定义ArcButton可设置的弧形按钮状态。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 正常状态。 |
| PRESSED | 1 | 按压状态。 |
| DISABLED | 2 | 禁用状态。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1 (设置弧形按钮)

该示例展示了ArcButton的基本用法。从API version 18开始，新增ArcButton。示例配置如下：

1.topOptions定义了上弧形按钮，按钮文本为ButtonTop，字体大小为15fp，按钮状态为正常状态，按钮样式为亮色强调，启用阴影。

2.bottomOptions定义了底部弧形按钮，按钮文本为ButtonBottom，字体大小为15fp，按钮样式为亮色强调，启用阴影，设置了按钮的点击事件。

该示例推荐在Wearable设备下运行以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，需在src/main目录下的工程配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)内配置wearable。

```
1. // module.json5
2. {
3. "module": {
4. // ...
5. "deviceTypes": [
6. "wearable",
7. "phone"
8. ]
9. // ...
10. }
11. }
```

```
1. // xxx.ets
2. import {
3. LengthMetrics,
4. LengthUnit,
5. ArcButton,
6. ArcButtonOptions,
7. ArcButtonStatus,
8. ArcButtonStyleMode,
9. ArcButtonPosition,
10. }  from '@kit.ArkUI';

12. @Entry
13. @ComponentV2
14. struct Index {
15. @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
16. @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

18. aboutToAppear() {
19. this.topOptions = new ArcButtonOptions({
20. label: 'ButtonTop',
21. status: ArcButtonStatus.NORMAL,
22. position: ArcButtonPosition.TOP_EDGE,
23. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
24. fontSize: new LengthMetrics(15, LengthUnit.FP),
25. shadowEnabled: true
26. })

28. this.bottomOptions = new ArcButtonOptions({
29. label: 'ButtonBottom',
30. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
31. fontSize: new LengthMetrics(15, LengthUnit.FP),
32. shadowEnabled: true,
33. onClick: () => {
34. console.info('click from ArcButton.');
35. }
36. })
37. }

39. build() {
40. Stack() {
41. Stack() {
42. Circle({ width: 233, height: 233 })
43. .strokeWidth(0.1)
44. .fill(Color.White)

46. Column() {
47. ArcButton({ options: this.topOptions })
48. Blank()
49. ArcButton({ options: this.bottomOptions })

51. }.width('100%')
52. .height('100%')
53. }.width(233)
54. .height(233)
55. }.width('100%')
56. .height('100%')
57. .alignContent(Alignment.Center)
58. .backgroundColor(Color.Gray)
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/p-yz4_bvTlmWJul0vIkLJA/zh-cn_image_0000002589246063.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=48BD1D7FC3209766FA1E69C7F08FB17555D0E8933E12B08506D96AF395A24B9C)

### 示例2 (设置设备进度条按钮)

该示例展示了ArcButton组件进度条样式的基本用法。从API version 23开始，新增[progressConfig](ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)接口。示例配置如下：

1.topOptions定义了上弧形按钮。按钮文本为Add，字体大小为15fp，按钮状态为正常状态，按钮样式为亮色强调，启用阴影。按钮设置了点击事件，点击按钮将增加进度条的进度。

2.bottomOptions定义了底部弧形按钮，按钮文本为进度条百分比，字体大小为15fp，按钮状态为进度条状态，按钮样式为默认样式，启用阴影。

该示例推荐在Wearable设备下运行以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，需在src/main目录下的工程配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)内配置wearable。

```
1. // module.json5
2. {
3. "module": {
4. // ...
5. "deviceTypes": [
6. "wearable",
7. "phone"
8. ]
9. // ...
10. }
11. }
```

```
1. // xxx.ets
2. import {
3. LengthMetrics,
4. LengthUnit,
5. ArcButton,
6. ArcButtonOptions,
7. ArcButtonStatus,
8. ArcButtonStyleMode,
9. ArcButtonPosition,
10. }  from '@kit.ArkUI';

12. @Entry
13. @ComponentV2
14. struct Index {
15. @Local topOptions: ArcButtonOptions = new ArcButtonOptions({});
16. @Local bottomOptions: ArcButtonOptions = new ArcButtonOptions({});

18. aboutToAppear() {
19. this.topOptions = new ArcButtonOptions({
20. label: 'Add',
21. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
22. position: ArcButtonPosition.TOP_EDGE,
23. fontSize: new LengthMetrics(15, LengthUnit.FP),
24. shadowEnabled: true,
25. onClick: () => {
26. if(this.bottomOptions.progressConfig && this.bottomOptions.progressConfig.value < 100) {
27. this.bottomOptions.progressConfig.value = this.bottomOptions.progressConfig.value + 5
28. this.bottomOptions.label = this.bottomOptions.progressConfig.value + "%"
29. }
30. }
31. })

33. this.bottomOptions = new ArcButtonOptions({
34. label: '0%',
35. status: ArcButtonStatus.NORMAL,
36. fontSize: new LengthMetrics(15, LengthUnit.FP),
37. shadowEnabled: true,
38. progressConfig: {value:0, total:100},
39. })
40. }

42. build() {
43. Stack() {
44. Stack() {
45. Circle({ width: 233, height: 233 })
46. .strokeWidth(0.1)
47. .fill(Color.White)

49. Column() {
50. ArcButton({ options: this.topOptions })
51. Blank()
52. ArcButton({ options: this.bottomOptions })

54. }.width('100%')
55. .height('100%')
56. }.width(233)
57. .height(233)
58. }.width('100%')
59. .height('100%')
60. .alignContent(Alignment.Center)
61. .backgroundColor(Color.Gray)
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/2RrbqhiGQYm2S4XLeLDUaQ/zh-cn_image_0000002558766254.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=C24D0F5F0565460E9776A17062E7C87DFB8A21CD5E1ACC92F64B3E6FA056BA9F)
