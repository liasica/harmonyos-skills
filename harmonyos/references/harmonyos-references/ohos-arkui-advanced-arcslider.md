---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcslider
title: ArcSlider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > ArcSlider
category: harmonyos-references
scraped_at: 2026-04-29T13:52:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d00985f456ba06ac1f3ed2011aebe91b4131b604c519d1db95e2943611cfbaa
---

弧形滑动条组件，通常用于在圆形屏幕的穿戴设备中快速调节设置值，如音量调节、亮度调节等应用场景。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {
2. ArcSlider,
3. ArcSliderPosition,
4. ArcSliderOptions,
5. ArcSliderValueOptions,
6. ArcSliderLayoutOptions,
7. ArcSliderStyleOptions,
8. ArcSliderValueOptionsConstructorOptions,
9. ArcSliderLayoutOptionsConstructorOptions,
10. ArcSliderStyleOptionsConstructorOptions,
11. ArcSliderOptionsConstructorOptions
12. } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## ArcSlider

PhonePC/2in1TabletTVWearable

ArcSlider({ options: ArcSliderOptions })

创建ArcSlider实例，入参是弧形进度条配置选项。

**装饰器类型：**@Component

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderOptions](ohos-arkui-advanced-arcslider.md#arcslideroptions) | 是 | 配置弧形滑动条的参数。  默认值：[ArcSliderOptions](ohos-arkui-advanced-arcslider.md#arcslideroptions)的各项子属性均取其默认值。 |

## ArcSliderOptions

PhonePC/2in1TabletTVWearable

配置弧形Slider的信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| valueOptions | [ArcSliderValueOptions](ohos-arkui-advanced-arcslider.md#arcslidervalueoptions) | 否 | 是 | 配置弧形Slider的数值信息。  默认值：[ArcSliderValueOptions](ohos-arkui-advanced-arcslider.md#arcslidervalueoptions)的各项子属性均取其默认值。  **装饰器类型：** @Trace |
| layoutOptions | [ArcSliderLayoutOptions](ohos-arkui-advanced-arcslider.md#arcsliderlayoutoptions) | 否 | 是 | 配置弧形Slider的布局信息。  默认值：[ArcSliderLayoutOptions](ohos-arkui-advanced-arcslider.md#arcsliderlayoutoptions)的各项子属性均取其默认值。  **装饰器类型：** @Trace |
| styleOptions | [ArcSliderStyleOptions](ohos-arkui-advanced-arcslider.md#arcsliderstyleoptions) | 否 | 是 | 配置弧形Slider的样式信息。  默认值：[ArcSliderStyleOptions](ohos-arkui-advanced-arcslider.md#arcsliderstyleoptions)的各项子属性均取其默认值。  **装饰器类型：** @Trace |
| digitalCrownSensitivity | [CrownSensitivity](ts-appendix-enums.md#crownsensitivity18) | 否 | 是 | 设置旋转表冠的灵敏度。  默认值：CrownSensitivity.MEDIUM  **装饰器类型：** @Trace |
| onTouch | [ArcSliderTouchHandler](ohos-arkui-advanced-arcslider.md#arcslidertouchhandler) | 否 | 是 | 弧形Slider被触摸时，告知应用。  默认值：不传入的情况，无回调。  **装饰器类型：** @Trace |
| onChange | [ArcSliderChangeHandler](ohos-arkui-advanced-arcslider.md#arcsliderchangehandler) | 否 | 是 | 弧形Slider的进度值发生变化时，告知应用。  默认值：不传入的情况，无回调。  **装饰器类型：** @Trace |
| onEnlarge | [ArcSliderEnlargeHandler](ohos-arkui-advanced-arcslider.md#arcsliderenlargehandler) | 否 | 是 | 弧形Slider放大或缩小时，告知应用。  默认值：不传入的情况，无回调。  **装饰器类型：** @Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ArcSliderOptionsConstructorOptions)

ArcSliderOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderOptionsConstructorOptions](ohos-arkui-advanced-arcslider.md#arcslideroptionsconstructoroptions) | 否 | ArcSliderOptions的构造信息。 |

## ArcSliderValueOptions

PhonePC/2in1TabletTVWearable

配置弧形Slider的数值信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 是 | 设置当前进度值。  默认值：与参数min的取值一致  **装饰器类型：** @Trace |
| min | number | 否 | 是 | 设置最小值。  默认值：0  **装饰器类型：** @Trace |
| max | number | 否 | 是 | 设置最大值。  默认值：100  **说明：**  当出现异常情况min >= max时，min取默认值0，max取默认值100。  progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。  **装饰器类型：** @Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ArcSliderValueOptionsConstructorOptions)

ArcSliderValueOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderValueOptionsConstructorOptions](ohos-arkui-advanced-arcslider.md#arcslidervalueoptionsconstructoroptions) | 否 | ArcSliderValueOptions的构造信息。 |

## ArcSliderLayoutOptions

PhonePC/2in1TabletTVWearable

配置弧形Slider的布局信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reverse | boolean | 否 | 是 | 设置弧形Slider取值范围是否反向。值为false时表示从上往下滑。  默认值：true，表示从下往上滑动。  **装饰器类型：** @Trace |
| position | [ArcSliderPosition](ohos-arkui-advanced-arcslider.md#arcsliderposition) | 否 | 是 | 弧形Slider的屏幕显示位置。  默认值：ArcSliderPosition.RIGHT  **装饰器类型：** @Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ArcSliderLayoutOptionsConstructorOptions)

ArcSliderLayoutOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderLayoutOptionsConstructorOptions](ohos-arkui-advanced-arcslider.md#arcsliderlayoutoptionsconstructoroptions) | 否 | ArcSliderLayoutOptions的构造信息。 |

## ArcSliderStyleOptions

PhonePC/2in1TabletTVWearable

配置弧形Slider的样式信息。

**装饰器类型：**@ObservedV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trackThickness | number | 否 | 是 | 正常状态下弧形Slider的描边粗细，单位：vp。  默认值：5  取值范围：[5, 16]，异常值按默认值处理。  **装饰器类型：** @Trace |
| activeTrackThickness | number | 否 | 是 | 放大状态下弧形Slider的描边粗细，单位：vp。  默认值：24  取值范围：[24, 36]，异常值按默认值处理。  **装饰器类型：** @Trace |
| trackColor | string | 否 | 是 | 设置描边背景色。  默认值：#33FFFFFF  **装饰器类型：** @Trace |
| selectedColor | string | 否 | 是 | 设置描边高亮色。  默认值：#FF5EA1FF  **装饰器类型：** @Trace |
| trackBlur | number | 否 | 是 | 设置描边背景模糊值，单位：vp。  默认值：20  设置小于0的值时，按照默认值处理。  **装饰器类型：** @Trace |

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ArcSliderStyleOptionsConstructorOptions)

ArcSliderStyleOptions的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcSliderStyleOptionsConstructorOptions](ohos-arkui-advanced-arcslider.md#arcsliderstyleoptionsconstructoroptions) | 否 | ArcSliderStyleOptions的构造信息。 |

## ArcSliderPosition

PhonePC/2in1TabletTVWearable

配置弧形Slider的屏幕显示位置。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 弧形Slider的屏幕显示位置在左侧。 |
| RIGHT | 1 | 弧形Slider的屏幕显示位置在右侧。 |

## ArcSliderTouchHandler

PhonePC/2in1TabletTVWearable

type ArcSliderTouchHandler = (event: TouchEvent) => void

弧形Slider被触摸时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchEvent](ts-universal-events-touch.md#touchevent对象说明) | 是 | 获得TouchEvent对象。 |

## ArcSliderChangeHandler

PhonePC/2in1TabletTVWearable

type ArcSliderChangeHandler = (progress: number) => void

弧形Slider的进度值发生变化时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | Slider当前的进度值。 |

## ArcSliderEnlargeHandler

PhonePC/2in1TabletTVWearable

type ArcSliderEnlargeHandler = (isEnlarged: boolean) => void

弧形Slider放大或缩小时，告知应用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnlarged | boolean | 是 | ArcSlider当前是否放大。  isEnlarged为false时，ArcSlider组件处于缩小状态。  isEnlarged为true时，ArcSlider组件处于放大状态。 |

## ArcSliderOptionsConstructorOptions

PhonePC/2in1TabletTVWearable

ArcSliderOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| valueOptions | [ArcSliderValueOptions](ohos-arkui-advanced-arcslider.md#arcslidervalueoptions) | 否 | 是 | 配置弧形Slider的数值信息。  默认值：[ArcSliderValueOptions](ohos-arkui-advanced-arcslider.md#arcslidervalueoptions)的各项子属性均取其默认值。 |
| layoutOptions | [ArcSliderLayoutOptions](ohos-arkui-advanced-arcslider.md#arcsliderlayoutoptions) | 否 | 是 | 配置弧形Slider的布局信息。  默认值：[ArcSliderLayoutOptions](ohos-arkui-advanced-arcslider.md#arcsliderlayoutoptions)的各项子属性均取其默认值。 |
| styleOptions | [ArcSliderStyleOptions](ohos-arkui-advanced-arcslider.md#arcsliderstyleoptions) | 否 | 是 | 配置弧形Slider的样式信息。  默认值：[ArcSliderStyleOptions](ohos-arkui-advanced-arcslider.md#arcsliderstyleoptions)的各项子属性均取其默认值。 |
| digitalCrownSensitivity | [CrownSensitivity](ts-appendix-enums.md#crownsensitivity18) | 否 | 是 | 设置旋转表冠的灵敏度。  默认值：CrownSensitivity.MEDIUM |
| onTouch | [ArcSliderTouchHandler](ohos-arkui-advanced-arcslider.md#arcslidertouchhandler) | 否 | 是 | 弧形Slider被触摸时，告知应用。  默认值：不传入的情况，无回调。 |
| onChange | [ArcSliderChangeHandler](ohos-arkui-advanced-arcslider.md#arcsliderchangehandler) | 否 | 是 | 弧形Slider的进度值发生变化时，告知应用。  默认值：不传入的情况，无回调。 |
| onEnlarge | [ArcSliderEnlargeHandler](ohos-arkui-advanced-arcslider.md#arcsliderenlargehandler) | 否 | 是 | 弧形Slider放大或缩小时，告知应用。  默认值：不传入的情况，无回调。 |

## ArcSliderValueOptionsConstructorOptions

PhonePC/2in1TabletTVWearable

ArcSliderValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 是 | 设置当前进度值。  默认值：与参数min的取值一致。 |
| min | number | 否 | 是 | 设置最小值。  默认值：0 |
| max | number | 否 | 是 | 设置最大值。  默认值：100  **说明：**  当出现异常情况min >= max时，min取默认值0，max取默认值100。  progress不在[min, max]范围之内，取min或者max，靠近min取min，靠近max取max。 |

## ArcSliderLayoutOptionsConstructorOptions

PhonePC/2in1TabletTVWearable

ArcSliderLayoutValueOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reverse | boolean | 否 | 是 | 设置弧形Slider取值范围是否反向。  默认值：true。表示从下往上滑动。 |
| position | [ArcSliderPosition](ohos-arkui-advanced-arcslider.md#arcsliderposition) | 否 | 是 | 弧形Slider的屏幕显示位置。  默认值：ArcSliderPosition.RIGHT |

## ArcSliderStyleOptionsConstructorOptions

PhonePC/2in1TabletTVWearable

ArcSliderStyleOptions的构造信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| trackThickness | number | 否 | 是 | 正常状态下弧形Slider的描边粗细，单位：vp。  默认值：5  取值范围：[5, 16]，异常值按默认值处理。 |
| activeTrackThickness | number | 否 | 是 | 放大状态下弧形Slider的描边粗细，单位：vp。  默认值：24  取值范围：[24, 36]，异常值按默认值处理。 |
| trackColor | string | 否 | 是 | 设置描边背景色。  默认值：#33FFFFFF |
| selectedColor | string | 否 | 是 | 设置描边高亮色。  默认值：#FF5EA1FF |
| trackBlur | number | 否 | 是 | 设置描边背景模糊值，单位：vp。  默认值：20  设置小于0的值时，按照默认值处理。 |

## 示例

PhonePC/2in1TabletTVWearable

从API version 18开始，该示例展示了ArcSlider组件的基本用法。

```
1. // xxx.ets
2. import {
3. ArcSlider,
4. ArcSliderPosition,
5. ArcSliderOptions,
6. ArcSliderValueOptions,
7. ArcSliderLayoutOptions,
8. ArcSliderStyleOptions,
9. ArcSliderValueOptionsConstructorOptions,
10. ArcSliderLayoutOptionsConstructorOptions,
11. ArcSliderStyleOptionsConstructorOptions,
12. ArcSliderOptionsConstructorOptions
13. } from '@kit.ArkUI';

15. @Entry
16. @ComponentV2
17. struct ArcSliderExample {
18. valueOptionsConstructorOptions: ArcSliderValueOptionsConstructorOptions = {
19. progress: 60,
20. min: 10,
21. max: 110
22. };

24. layoutOptionsConstructorOptions: ArcSliderLayoutOptionsConstructorOptions = {
25. reverse: true,
26. position: ArcSliderPosition.RIGHT
27. };
28. styleOptionsConstructorOptions: ArcSliderStyleOptionsConstructorOptions = {
29. trackThickness: 8,
30. activeTrackThickness: 30,
31. trackColor: '#ffd5d5d5',
32. selectedColor: '#ff2787d9',
33. trackBlur: 20
34. };
35. valueOptions: ArcSliderValueOptions = new ArcSliderValueOptions(this.valueOptionsConstructorOptions);
36. layoutOptions: ArcSliderLayoutOptions = new ArcSliderLayoutOptions(this.layoutOptionsConstructorOptions);
37. styleOptions: ArcSliderStyleOptions = new ArcSliderStyleOptions(this.styleOptionsConstructorOptions);
38. arcSliderOptionsConstructorOptions: ArcSliderOptionsConstructorOptions = {
39. valueOptions: this.valueOptions,
40. layoutOptions: this.layoutOptions,
41. styleOptions: this.styleOptions,
42. digitalCrownSensitivity:CrownSensitivity.LOW,
43. onTouch: (event: TouchEvent) => {
44. },
45. onChange: (progress: number) => {
46. },
47. onEnlarge: (isEnlarged: boolean) => {
48. }
49. };
50. arcSliderOptions: ArcSliderOptions = new ArcSliderOptions(this.arcSliderOptionsConstructorOptions);

52. build() {
53. Column() {
54. ArcSlider({ options: this.arcSliderOptions })}
55. .width('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/FXYH_KTtQqCMa1tX0g7FHA/zh-cn_image_0000002558606596.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055203Z&HW-CC-Expire=86400&HW-CC-Sign=6E0F6380C9B33FF969F686D0CE669027D540A1704FDEB22DBC11A49FFFBB672A)
