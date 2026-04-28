---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-measure
title: @ohos.measure (文本计算)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.measure (文本计算)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:945d3898d3dd539099a5cc288eb9551b178a0c7424c001cb37b14f3b17f99a6c
---

本模块提供文本宽度、高度等相关计算。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该模块不支持在[UIAbility](js-apis-app-ability-uiability.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
* 如需更多测算文本参数，建议使用图形对应测算接口[Paragraph](js-apis-graphics-text.md#paragraph)接口。
* 调用文本计算接口时，不建议同时使用[ApplicationContext.setFontSizeScale](js-apis-inner-application-applicationcontext.md#applicationcontextsetfontsizescale13)设置应用字体大小缩放比例。为了确保时序的一致性，建议开发者自行监听字体缩放变化，以保证测算结果的准确性。
* 在测算裁剪后的文本时，由于某些Unicode字符（如emoji）的码位长度大于1，直接按字符串长度裁剪会导致不准确的结果。建议基于Unicode码点进行迭代处理，避免错误截断字符，确保测算结果准确。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { MeasureText } from '@kit.ArkUI';
```

## MeasureText.measureText(deprecated)

PhonePC/2in1TabletTVWearable

static measureText(options: MeasureOptions): number

计算指定文本作为单行文本显示时的宽度。如果文本包含多行（由换行符\n分隔），则返回其中最长的行的宽度。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[measureText](arkts-apis-uicontext-measureutils.md#measuretext12)替代。measureText需要先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取[MeasureUtils](arkts-apis-uicontext-measureutils.md)对象，然后通过该对象进行调用。且直接使用measureText可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](arkts-apis-uicontext-measureutils.md)对象。
* measureText接口的计算结果始终是单行文本的宽度，入参options中配置的布局约束（如constraintWidth、maxLines）对measureText的结果没有影响。如果需要计算布局约束下的宽度，请使用[measureTextSize](arkts-apis-uicontext-measureutils.md#measuretextsize12)方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [MeasureOptions](js-apis-measure.md#measureoptions) | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 文本宽度。  单位：px |

说明

直接使用MeasureText可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，推荐通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](arkts-apis-uicontext-measureutils.md)实例。

**示例：**

```
1. import { MeasureText } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State textWidth: number = MeasureText.measureText({
7. // 建议使用 this.getUIContext().getMeasureUtils().measureText()接口
8. textContent: "Hello World",
9. fontSize: '50px'
10. });

12. build() {
13. Row() {
14. Column() {
15. Text(`The width of 'Hello World': ${this.textWidth}`)
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

## MeasureText.measureTextSize(deprecated)

PhonePC/2in1TabletTVWearable

static measureTextSize(options: MeasureOptions): SizeOptions

计算指定文本的宽度和高度。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[measureTextSize](arkts-apis-uicontext-measureutils.md#measuretextsize12)替代。measureTextSize需要先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取[MeasureUtils](arkts-apis-uicontext-measureutils.md)对象，然后通过该对象进行调用。且直接使用measureTextSize可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](arkts-apis-uicontext-measureutils.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [MeasureOptions](js-apis-measure.md#measureoptions) | 是 | 被计算文本描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeOptions](ts-types.md#sizeoptions) | 返回文本所占布局宽度和高度。  **说明:**  文本宽度以及高度返回值单位均为px。 |

说明

直接使用MeasureText可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，推荐通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMeasureUtils](arkts-apis-uicontext-uicontext.md#getmeasureutils12)方法获取当前UI上下文关联的[MeasureUtils](arkts-apis-uicontext-measureutils.md)实例。

**示例：**

```
1. import { MeasureText } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. textSize: SizeOptions = MeasureText.measureTextSize({
7. // 建议使用 this.getUIContext().getMeasureUtils().measureTextSize()接口
8. textContent: "Hello World",
9. fontSize: '50px'
10. });

12. build() {
13. Row() {
14. Column() {
15. Text(`The width of 'Hello World': ${this.textSize.width}`)
16. Text(`The height of 'Hello World': ${this.textSize.height}`)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

## MeasureOptions

PhonePC/2in1TabletTVWearable

被计算文本属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textContent | string | [Resource](ts-types.md#resource) | 否 | 否 | 设置被计算文本内容。 |
| constraintWidth10+ | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置被计算文本布局宽度。  **说明：**  默认单位为vp，不支持设置百分比字符串。若不设置，则文本SizeOptions宽度为单行布局所占最大宽度值，若设置则为设置值。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置被计算文本字体大小，fontSize为number类型时，使用vp单位。  默认值：16  **说明：**  不支持设置百分比字符串。  从API version 12开始，fontSize为number类型时，使用fp单位。 |
| fontStyle | number | [FontStyle](ts-appendix-enums.md#fontstyle) | 否 | 是 | 设置被计算文本字体样式。  默认值：FontStyle.Normal  number类型取值范围为[0,1]，取值间隔为1，依次对应FontStyle中的枚举值。 |
| fontWeight | number | string | [FontWeight](ts-appendix-enums.md#fontweight) | 否 | 是 | 设置被计算文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal |
| fontFamily | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置被计算文本字体列表。默认字体'HarmonyOS Sans'，且当前只支持这种字体。 |
| letterSpacing | number | string | 否 | 是 | 设置被计算文本字符间距。  默认值：0 |
| textAlign10+ | number | [TextAlign](ts-appendix-enums.md#textalign) | 否 | 是 | 设置被计算文本水平方向的对齐方式。  默认值：TextAlign.Start  number类型取值范围为[0,3]，取值间隔为1，依次对应TextAlign中的枚举值。 |
| overflow10+ | number | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 设置被计算文本超长时的截断方式。  默认值：1  number类型取值范围为[0,3]，取值间隔为1，依次对应TextOverflow中的枚举值。 |
| maxLines10+ | number | 否 | 是 | 设置被计算文本最大行数。  取值范围：[0, INT32\_MAX] |
| lineHeight10+ | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置被计算文本行高。 |
| baselineOffset10+ | number | string | 否 | 是 | 设置被计算文本基线的偏移量。  默认值：0 |
| textCase10+ | number | [TextCase](ts-appendix-enums.md#textcase) | 否 | 是 | 设置被计算文本大小写。  默认值：TextCase.Normal  number类型取值范围为[0,2]，取值间隔为1，依次对应TextCase中的枚举值。 |
| textIndent11+ | number | string | 否 | 是 | 设置首行文本缩进，默认值为0。 |
| wordBreak11+ | [WordBreak](ts-appendix-enums.md#wordbreak11) | 否 | 是 | 设置断行规则。  默认值：WordBreak.BREAK\_WORD  **说明：**  WordBreak.BREAK\_ALL与{overflow: TextOverflow.Ellipsis}，maxLines组合使用可实现英文单词按字母截断，超出部分以省略号显示。 |
