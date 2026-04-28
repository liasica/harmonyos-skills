---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress
title: Progress
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > Progress
category: harmonyos-references
scraped_at: 2026-04-28T08:02:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9aa237271462447763fba16096a33972c69da8fe40221c3bb8889f8f6d8cd6f
---

进度条组件，用于显示内容加载或操作处理等进度。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Progress(options: ProgressOptions)

创建进度条组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ProgressOptions](ts-basic-components-progress.md#progressoptions对象说明) | 是 | 按进度条类型不同，设置不同属性的进度条组件参数。 |

## ProgressOptions对象说明

PhonePC/2in1TabletTVWearable

进度条选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 指定当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。  默认值：0  取值范围：[0, total]  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| total | number | 否 | 是 | 指定进度总长。设置小于等于0的数值时置为100。  默认值：100  取值范围：[0, 2147483647]  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| type8+ | [ProgressType](ts-basic-components-progress.md#progresstype8枚举说明) | 否 | 是 | 指定进度条类型。  默认值：ProgressType.Linear  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **说明：** 不同的type需分别对应相应的[style](ts-basic-components-progress.md#style8)属性设置，详细映射关系参考[ProgressStyleMap](ts-basic-components-progress.md#progressstylemap10对象说明)。 |
| style(deprecated) | [ProgressStyle](ts-basic-components-progress.md#progressstyle枚举说明) | 否 | 是 | 指定进度条样式。  该参数从API version8开始废弃，建议使用type替代。  默认值：ProgressStyle.Linear |

## ProgressType8+枚举说明

PhonePC/2in1TabletTVWearable

进度条类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Linear | 0 | 线性样式。从API version 9开始，当高度大于宽度时，自适应垂直显示。 |
| Ring | 1 | 环形无刻度样式，环形圆环逐渐显示直至完全填充。 |
| Eclipse | 2 | 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。 |
| ScaleRing | 3 | 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。从API version 9开始，刻度外圈出现重叠时自动转换为环形无刻度进度条。 |
| Capsule | 4 | 胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同，中段的进度展示效果与Linear相同。当高度大于宽度时，自适应垂直显示。 |

## ProgressStyle枚举说明

PhonePC/2in1TabletTVWearable

进度条样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Linear | 0 | 线性样式。 |
| Ring8+ | 1 | 环形圆环逐渐显示直至完全填充。 |
| Eclipse | 2 | 圆形样式，显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。 |
| ScaleRing8+ | 3 | 环形有刻度样式，显示类似时钟刻度形式的进度展示效果。 |
| Capsule8+ | 4 | 胶囊样式，头尾两端圆弧处的进度展示效果与Eclipse相同，中段的进度展示效果与Linear相同。当高度大于宽度时，自适应垂直显示。 |

## ProgressStyleMap10+对象说明

PhonePC/2in1TabletTVWearable

进度条类型和样式的映射表。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 |
| --- | --- |
| ProgressType.Linear | [LinearStyleOptions10+](ts-basic-components-progress.md#linearstyleoptions10) | [ProgressStyleOptions](ts-basic-components-progress.md#progressstyleoptions8) |
| ProgressType.Ring | [RingStyleOptions10+](ts-basic-components-progress.md#ringstyleoptions10) | [ProgressStyleOptions](ts-basic-components-progress.md#progressstyleoptions8) |
| ProgressType.Eclipse | [EclipseStyleOptions10+](ts-basic-components-progress.md#eclipsestyleoptions10) | [ProgressStyleOptions](ts-basic-components-progress.md#progressstyleoptions8) |
| ProgressType.ScaleRing | [ScaleRingStyleOptions10+](ts-basic-components-progress.md#scaleringstyleoptions10) | [ProgressStyleOptions](ts-basic-components-progress.md#progressstyleoptions8) |
| ProgressType.Capsule | [CapsuleStyleOptions10+](ts-basic-components-progress.md#capsulestyleoptions10) | [ProgressStyleOptions](ts-basic-components-progress.md#progressstyleoptions8) |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

该组件重写了通用属性[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)，直接添加在Progress组件上，设置进度条的底色。如需设置整个Progress组件的背景色，需要在外层容器上添加backgroundColor，并用该容器包裹Progress组件。

### value

PhonePC/2in1TabletTVWearable

value(value: number)

设置当前进度值。设置小于0的数值时置为0，设置大于total的数值时置为total。非法数值不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前进度值。  默认值：0 |

### color

PhonePC/2in1TabletTVWearable

color(value: ResourceColor | LinearGradient)

设置进度条前景色。

从API version 10开始支持利用[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)设置Ring样式的渐变色。Ring类型不建议设置透明度，如需设置透明度，建议使用[DataPanel](ts-basic-components-datapanel.md)。

从API version 23开始支持利用[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)设置Linear样式和Capsule样式的渐变色。API version 22及之前版本利用LinearGradient设置Linear样式和Capsule样式的渐变色时，会以默认主题色显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，暂不支持LinearGradient。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10) | 是 | 进度条前景色。  默认值：  - Capsule：  API version 9及以下：'#ff007dff'  API version 10：'#33006cde'  API version 11及以上：'#33007dff'  - Ring：  API version 9及以下：'#ff007dff'  API version 10及以上：起始端：'#ff86c1ff'，结束端：'#ff254ff7'  - 其他样式：'#ff007dff' |

### style8+

PhonePC/2in1TabletTVWearable

style(value: ProgressStyleOptions | CapsuleStyleOptions | RingStyleOptions | LinearStyleOptions | ScaleRingStyleOptions | EclipseStyleOptions)

设置组件的样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ProgressStyleOptions8+](ts-basic-components-progress.md#progressstyleoptions8) | [CapsuleStyleOptions10+](ts-basic-components-progress.md#capsulestyleoptions10) |  [RingStyleOptions10+](ts-basic-components-progress.md#ringstyleoptions10) | [LinearStyleOptions10+](ts-basic-components-progress.md#linearstyleoptions10) |  [ScaleRingStyleOptions10+](ts-basic-components-progress.md#scaleringstyleoptions10) | [EclipseStyleOptions10+](ts-basic-components-progress.md#eclipsestyleoptions10) | 是 | 组件的样式。  - CapsuleStyleOptions：设置Capsule的样式。  - RingStyleOptions：设置Ring的样式。  - LinearStyleOptions：设置Linear的样式。  - ScaleRingStyleOptions：设置ScaleRing的样式。  - EclipseStyleOptions：设置Eclipse的样式。  - ProgressStyleOptions：仅可设置各类型进度条的strokeWidth、scaleCount、scaleWidth，仅对支持这些样式设置的进度条生效。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier:ContentModifier<ProgressConfiguration>)

定制progress内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier<ProgressConfiguration>](ts-basic-components-progress.md#progressconfiguration12) | 是 | 在progress组件上，定制内容区的方法。  modifier： 内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### privacySensitive12+

PhonePC/2in1TabletTVWearable

privacySensitive(isPrivacySensitiveMode: Optional<boolean>)

设置隐私敏感。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | [Optional<boolean>](ts-universal-attributes-custom-property.md#optionalt) | 是 | 设置隐私敏感，隐私模式下进度清零，文字将被遮罩。true：打开隐私敏感；false：关闭隐私敏感。  默认值：false  **说明：**  设置null表示不敏感。 |

## ProgressConfiguration12+

PhonePC/2in1TabletTVWearable

进度条配置。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 当前进度值。当设置的数值小于0时，将其置为0。当设置的数值大于total时，将其置为total。  默认值：0  取值范围：[0, total] |
| total | number | 否 | 否 | 进度总长。  取值范围：[0, 2147483647]  **说明：**  total是负数时，按照100处理。 |

## CommonProgressStyleOptions10+

PhonePC/2in1TabletTVWearable

进度条通用样式选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableSmoothEffect | boolean | 否 | 是 | 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，页面会有进度变化的动效；否则进度从当前值突变至设定值，页面无动效。  true：表示开启进度平滑动效。  false：表示关闭进度平滑动效。  默认值：true |

## ScanEffectOptions10+

PhonePC/2in1TabletTVWearable

扫光效果选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableScanEffect | boolean | 否 | 是 | 扫光效果的开关。仅支持[Linear、Ring、Capsule](ts-basic-components-progress.md#progresstype8枚举说明)类型的进度条。  true：表示开启扫光效果。  false：表示关闭扫光效果。  默认值：false |

## ProgressStyleOptions8+

PhonePC/2in1TabletTVWearable

进度条样式选项。

继承自[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 是 | 设置进度条宽度（不支持百分比设置）。  默认值：4.0vp  超出取值范围按默认值处理。 |
| scaleCount | number | 否 | 是 | 设置环形进度条总刻度数。  默认值：120vp  取值范围：[2, min(width, height)/scaleWidth/2/π]，超出取值范围时，样式显示为环形无刻度进度条。默认情况下宽高最小为77vp。 |
| scaleWidth | [Length](ts-types.md#length) | 否 | 是 | 设置环形进度条刻度粗细（不支持百分比设置）。刻度粗细大于进度条宽度时，为系统默认粗细。  默认值：2.0vp |

## CapsuleStyleOptions10+

PhonePC/2in1TabletTVWearable

胶囊样式选项。

继承自[ScanEffectOptions](ts-basic-components-progress.md#scaneffectoptions10)和[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 内描边颜色。  默认值：  API version 10：'#33006cde'  API version 11及以上：'#33007dff' |
| borderWidth | [Length](ts-types.md#length) | 否 | 是 | 内描边宽度（不支持百分比设置）。  默认值：1vp |
| content | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 文本内容，应用可自定义。  从API version 20开始，支持Resource类型。 |
| font | [Font](ts-types.md#font) | 否 | 是 | 文本样式。  默认值：  文本大小（不支持百分比设置）：12fp  其他文本参数跟随[Text](ts-basic-components-text.md)组件的主题值。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。  默认值：'#ff182431' |
| showDefaultPercentage | boolean | 否 | 是 | 显示百分比文本的开关。开启后，进度条上显示当前进度的百分比。设置了content属性时该属性不生效。  true：表示显示百分比文本；false：表示不显示百分比文本。  默认值：false |
| borderRadius18+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | Capsule进度条圆角半径（不支持百分比设置）。  取值范围：[0, height/2]。默认值：height / 2。  设置非法数值时，按照默认值处理。 |

## RingStyleOptions10+

PhonePC/2in1TabletTVWearable

环形无刻度样式选项。

继承自[ScanEffectOptions](ts-basic-components-progress.md#scaneffectoptions10)和[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 是 | 设置进度条宽度（不支持百分比设置）。当宽度大于等于半径时，宽度默认修改为半径值的二分之一。  默认值：4.0vp |
| shadow | boolean | 否 | 是 | 进度条阴影开关。  true：表示打开进度条阴影；false：表示关闭进度条阴影。  默认值：false |
| status | [ProgressStatus10+](ts-basic-components-progress.md#progressstatus10枚举说明) | 否 | 是 | 设置进度条状态。当设置为ProgressStatus.LOADING时会开启检查更新动效，此时设置进度值不生效。当从ProgressStatus.LOADING设置为ProgressStatus.PROGRESSING时，检查更新动效会执行到终点再停止。  默认值：ProgressStatus.PROGRESSING |

## LinearStyleOptions10+

PhonePC/2in1TabletTVWearable

线性样式选项。

继承自[ScanEffectOptions](ts-basic-components-progress.md#scaneffectoptions10)和[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 是 | 设置进度条宽度（不支持百分比设置）。  默认值：4.0vp |
| strokeRadius | [PX](ts-types.md#px10) | [VP](ts-types.md#vp10) | [LPX](ts-types.md#lpx10) | [Resource](ts-types.md#resource) | 否 | 是 | 设置线性进度条的圆角半径。  取值范围[0, strokeWidth / 2]。默认值：strokeWidth / 2。 |

## ScaleRingStyleOptions10+

PhonePC/2in1TabletTVWearable

环形有刻度样式选项。

继承自[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Length](ts-types.md#length) | 否 | 是 | 设置进度条宽度（不支持百分比设置）。  默认值：4.0vp |
| scaleCount | number | 否 | 是 | 设置环形进度条总刻度数。  默认值：120vp  取值范围：[2, min(width, height)/scaleWidth/2/π]，超出取值范围时，样式显示为环形无刻度进度条。默认情况下宽高最小为77vp。 |
| scaleWidth | [Length](ts-types.md#length) | 否 | 是 | 设置环形进度条刻度粗细（不支持百分比设置）。刻度粗细大于进度条宽度时，为系统默认粗细。  默认值：2.0vp |

## EclipseStyleOptions10+

PhonePC/2in1TabletTVWearable

圆形样式选项。圆形样式的显示类似月圆月缺的进度展示效果，从月牙逐渐变化至满月。

继承自[CommonProgressStyleOptions](ts-basic-components-progress.md#commonprogressstyleoptions10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ProgressStatus10+枚举说明

PhonePC/2in1TabletTVWearable

进度条的当前状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOADING | 'LOADING' | 加载中。 |
| PROGRESSING | 'PROGRESSING' | 进度更新中。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置进度条的类型）

该示例通过[ProgressOptions](ts-basic-components-progress.md#progressoptions对象说明)的入参type，实现了设置进度条类型的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. build() {
6. Column({ space: 15 }) {
7. Text('Linear Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. Progress({ value: 10, type: ProgressType.Linear }).width(200)
9. Progress({ value: 20, total: 150, type: ProgressType.Linear }).color(Color.Grey).value(50).width(200)

12. Text('Eclipse Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
13. Row({ space: 40 }) {
14. Progress({ value: 10, type: ProgressType.Eclipse }).width(100)
15. Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).value(50).width(100)
16. }

18. Text('ScaleRing Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
19. Row({ space: 40 }) {
20. Progress({ value: 10, type: ProgressType.ScaleRing }).width(100)
21. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
22. .color(Color.Grey).value(50).width(100)
23. .style({ strokeWidth: 15, scaleCount: 15, scaleWidth: 5 })
24. }

26. // scaleCount和scaleWidth效果对比
27. Row({ space: 40 }) {
28. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
29. .color(Color.Grey).value(50).width(100)
30. .style({ strokeWidth: 20, scaleCount: 20, scaleWidth: 5 })
31. Progress({ value: 20, total: 150, type: ProgressType.ScaleRing })
32. .color(Color.Grey).value(50).width(100)
33. .style({ strokeWidth: 20, scaleCount: 30, scaleWidth: 3 })
34. }

36. Text('Ring Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
37. Row({ space: 40 }) {
38. Progress({ value: 10, type: ProgressType.Ring }).width(100)
39. Progress({ value: 20, total: 150, type: ProgressType.Ring })
40. .color(Color.Grey).value(50).width(100)
41. .style({ strokeWidth: 20 })
42. }

44. Text('Capsule Progress').fontSize(9).fontColor(0xCCCCCC).width('90%')
45. Row({ space: 40 }) {
46. Progress({ value: 10, type: ProgressType.Capsule }).width(100).height(50)
47. Progress({ value: 20, total: 150, type: ProgressType.Capsule })
48. .color(Color.Grey)
49. .value(50)
50. .width(100)
51. .height(50)
52. }
53. }.width('100%').margin({ top: 30 })
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/wGnCJEoORhuPxR5VHdZezw/zh-cn_image_0000002583479913.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=8AEDD9B5E15E3CA750F1F0B5180A5A96CF102867AEE5DA9251E16E0D322A2CC7)

### 示例2（设置环形进度条属性）

该示例通过[style](ts-basic-components-progress.md#style8)接口的strokeWidth和shadow属性，实现了环形进度条视觉属性设置功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. private gradientColor: LinearGradient = new LinearGradient([{ color: Color.Yellow, offset: 0.5 },
6. { color: Color.Orange, offset: 1.0 }])

8. build() {
9. Column({ space: 15 }) {
10. Text('Gradient Color').fontSize(9).fontColor(0xCCCCCC).width('90%')
11. Progress({ value: 70, total: 100, type: ProgressType.Ring })
12. .width(100).style({ strokeWidth: 20 })
13. .color(this.gradientColor)

15. Text('Shadow').fontSize(9).fontColor(0xCCCCCC).width('90%')
16. Progress({ value: 70, total: 100, type: ProgressType.Ring })
17. .width(120).color(Color.Orange)
18. .style({ strokeWidth: 20, shadow: true })
19. }.width('100%').padding({ top: 5 })
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ba-1K5W-TLmQYG5qZgz_aw/zh-cn_image_0000002552800264.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=61FD9CA18672BBBDF5CE9DE42F3C6E4A1D3FEE87E9EE837251F0DBE1E06F0C54)

### 示例3（设置环形进度条动画）

该示例通过[style](ts-basic-components-progress.md#style8)接口的status和enableScanEffect属性，实现了环形进度条动效的开关功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. build() {
6. Column({ space: 15 }) {
7. Text('Loading Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. Progress({ value: 0, total: 100, type: ProgressType.Ring })
9. .width(100).color(Color.Blue)
10. .style({ strokeWidth: 20, status: ProgressStatus.LOADING })

12. Text('Scan Effect').fontSize(9).fontColor(0xCCCCCC).width('90%')
13. Progress({ value: 30, total: 100, type: ProgressType.Ring })
14. .width(100).color(Color.Orange)
15. .style({ strokeWidth: 20, enableScanEffect: true })
16. }.width('100%').padding({ top: 5 })
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/2CFlacEvTR-oaaQd4nHOlA/zh-cn_image_0000002583439959.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=66700E9CB5455BD13CCC4440D414450D929C41F3100332035BF9C970BB350A41)

### 示例4（设置胶囊形进度条属性）

该示例通过[style](ts-basic-components-progress.md#style8)接口的borderColor、borderWidth、content、font、fontColor、enableScanEffect、showDefaultPercentage属性，实现胶囊形进度条的视觉属性设置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. build() {
6. Column({ space: 15 }) {
7. Row({ space: 40 }) {
8. Progress({ value: 100, total: 100, type: ProgressType.Capsule }).width(100).height(50)
9. .style({
10. borderColor: Color.Blue,
11. borderWidth: 1,
12. content: 'Installing...',
13. font: { size: 13, style: FontStyle.Normal },
14. fontColor: Color.Gray,
15. enableScanEffect: false,
16. showDefaultPercentage: false
17. })
18. }
19. }.width('100%').padding({ top: 5 })
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ryUdja21QTObSPa33F4DeA/zh-cn_image_0000002552959914.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=E78BC19FCC6B49D7B83B22E30960FC9E3C1D51CD3703CEF93DDDB547F8747F0D)

### 示例5（设置进度平滑动效）

该示例通过[style](ts-basic-components-progress.md#style8)接口的enableSmoothEffect属性，实现了进度平滑动效开关的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State value: number = 0;

7. build() {
8. Column({ space: 10 }) {
9. Text('enableSmoothEffect: true')
10. .fontSize(9)
11. .fontColor(0xCCCCCC)
12. .width('90%')
13. .margin(5)
14. .margin({ top: 20 })
15. Progress({ value: this.value, total: 100, type: ProgressType.Linear })
16. .style({ strokeWidth: 10, enableSmoothEffect: true })

18. Text('enableSmoothEffect: false').fontSize(9).fontColor(0xCCCCCC).width('90%').margin(5)
19. Progress({ value: this.value, total: 100, type: ProgressType.Linear })
20. .style({ strokeWidth: 10, enableSmoothEffect: false })

22. Button('value +10').onClick(() => {
23. this.value += 10;
24. })
25. .width(75)
26. .height(15)
27. .fontSize(9)
28. }
29. .width('50%')
30. .height('100%')
31. .margin({ left: 20 })
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3LIKlpOFTLGgspMI4zBrig/zh-cn_image_0000002583479915.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=043F1FEE29A2E2C334BBAC3CCBBBBDF8953F93952330760808D0B274594A022C)

### 示例6（设置定制内容区）

该示例通过[contentModifier](ts-basic-components-progress.md#contentmodifier12)接口，实现了自定义进度条的功能，自定义实现星形，其中总进度为3，且当前值可通过按钮进行增减，达到的进度使用自定义颜色填充。

```
1. // xxx.ets
2. class MyProgressModifier implements ContentModifier<ProgressConfiguration> {
3. color: ResourceColor = Color.White;

5. constructor(color: ResourceColor) {
6. this.color = color;
7. }

9. applyContent(): WrappedBuilder<[ProgressConfiguration]> {
10. return wrapBuilder(myProgress);
11. }
12. }

14. @Builder
15. function myProgress(config: ProgressConfiguration) {

17. Column({ space: 30 }) {
18. Text('当前进度：' + config.value + '/' + config.total).fontSize(20)
19. Row() {
20. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
21. Path()
22. .width('30%')
23. .height('30%')
24. .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
25. .fill(config.enabled && config.value >= 1 ? (config.contentModifier as MyProgressModifier).color :
26. Color.White)
27. .stroke(Color.Black)
28. .strokeWidth(3)
29. Path()
30. .width('30%')
31. .height('30%')
32. .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
33. .fill(config.enabled && config.value >= 2 ? (config.contentModifier as MyProgressModifier).color :
34. Color.White)
35. .stroke(Color.Black)
36. .strokeWidth(3)
37. Path()
38. .width('30%')
39. .height('30%')
40. .commands('M108 0 L141 70 L218 78.3 L162 131 L175 205 L108 170 L41.2 205 L55 131 L1 78 L75 68 L108 0 Z')
41. .fill(config.enabled && config.value >= 3 ? (config.contentModifier as MyProgressModifier).color :
42. Color.White)
43. .stroke(Color.Black)
44. .strokeWidth(3)
45. }.width('100%')
46. }
47. }.margin({ bottom: 100 })
48. }

50. @Entry
51. @Component
52. struct Index {
53. @State currentValue: number = 0;
54. modifier = new MyProgressModifier('rgb(39, 135, 217)');
55. @State myModifier: (MyProgressModifier | undefined) = this.modifier;

57. build() {
58. Column() {
59. Progress({ value: this.currentValue, total: 3, type: ProgressType.Ring }).contentModifier(this.modifier)
60. Button('Progress++').onClick(() => {
61. if (this.currentValue < 3) {
62. this.currentValue += 1;
63. }
64. }).width('30%')
65. Button('Progress--').onClick(() => {
66. if (this.currentValue > 0) {
67. this.currentValue -= 1;
68. }
69. }).width('30%').margin('10')
70. }.width('100%').height('100%')
71. }
72. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/b8EZZ4ZHR2WCfHcjw4ISmQ/zh-cn_image_0000002552800266.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=B6469D793338B5B25FAF976EC82D72FE29F423D13B6745E8390778C96E99CCBC)

### 示例7（设置隐私隐藏）

该示例通过[privacySensitive](ts-basic-components-progress.md#privacysensitive12)属性，实现了隐私隐藏效果。效果展示需要卡片框架支持。

```
1. @Entry
2. @Component
3. struct ProgressExample {
4. build() {
5. Row() {
6. Column({ space: 15 }) {
7. Progress({ value: 33, total: 100, type: ProgressType.Capsule }).width(300).height(50)
8. .color(Color.Blue)
9. .style({
10. borderWidth: 5,
11. font: { size: 13, style: FontStyle.Normal },
12. enableScanEffect: false,
13. showDefaultPercentage: true
14. })
15. .privacySensitive(true)
16. Progress({ value: 33, total: 100, type: ProgressType.Capsule }).width(300).height(50)
17. .color(Color.Blue)
18. .style({
19. borderWidth: 5,
20. content: 'Installing...',
21. font: { size: 13, style: FontStyle.Normal },
22. enableScanEffect: false,
23. })
24. .privacySensitive(true)
25. }
26. }
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/adX8upPuRQ2wuqfTOEJA_A/zh-cn_image_0000002583439961.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=DFF03D49FF4A74D3EA0073EA0ED659318B8E67CA1EABF188AF69519C2960C997)

### 示例8（设置Capsule进度条圆角半径）

该示例通过[CapsuleStyleOptions](ts-basic-components-progress.md#capsulestyleoptions10)的入参borderRadius，实现了Capsule类型进度条圆角半径设置。

从API version 18开始，新增borderRadius属性。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ProgressExample {
6. build() {
7. Column({ space: 15 }) {
8. Text('Capsule Progress').fontSize(9).width('90%')
9. Row({ space: 15 }) {
10. Progress({ value: 30, total: 100, type: ProgressType.Capsule })
11. .style({ content: '默认圆角', borderWidth: 5 })
12. .width(100)
13. .height(60)
14. }

16. Row({ space: 15 }) {
17. Progress({ value: 30, total: 100, type: ProgressType.Capsule })
18. .style({ content: '圆角为20vp', borderWidth: 5, borderRadius: LengthMetrics.vp(20) })
19. .width(100)
20. .height(60)
21. }
22. }
23. .width('100%')
24. .margin({ top: 30 })
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/s7RMa6zMQN-Wo5T9iA25Ng/zh-cn_image_0000002552959916.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=4600399ED051C10DC8AAF9E89F4D0D163FCDF3DF64F09B7F51DE83C2C41CEF62)

### 示例9（设置线性进度条和胶囊进度条属性）

从API version 23开始，该示例通过[color](ts-basic-components-progress.md#color)属性中的LinearGradient，实现线性进度条和胶囊进度条渐变色的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ProgressExample {
5. private gradientColor: LinearGradient = new LinearGradient([{ color: "#87BDF9", offset: 0.5 },
6. { color: "#3662F0", offset: 1.0 }])
7. public gradientColor2: LinearGradient = new LinearGradient([{ color: "#A5A5AF", offset: 0.5 },
8. { color: "#67666C", offset: 1.0 }])

10. build() {
11. Column({ space: 15 }) {
12. Text('Linear：').fontSize(9).fontColor(0xCCCCCC).width('90%')
13. Progress({ value: 70, total: 100, type: ProgressType.Linear })
14. .width(100).style({ strokeWidth: 20 })
15. .color(this.gradientColor)

17. Text('Capsule：').fontSize(9).fontColor(0xCCCCCC).width('90%')
18. Progress({ value: 50, total: 100, type: ProgressType.Capsule })
19. .width(120).style({ strokeWidth: 40 })
20. .color(this.gradientColor2)
21. }.width('100%').padding({ top: 5 })
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/GS20ZY_-TW-vVUKVF8zyCg/zh-cn_image_0000002583479917.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=E3AA8BCE4745DD119FC397BB8444275AED50730998DF7680F5CE4F2B09534022)
