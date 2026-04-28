---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock
title: PatternLock
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > PatternLock
category: harmonyos-references
scraped_at: 2026-04-28T08:02:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f45738450c618d0a651030651621074d12e66783393c9b5de5a5a614dcf21df8
---

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

说明

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 如果开发者有其他功能需求，可以使用[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)。例如自定义组件[CustomPatternLock](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/master/ArkUISample/CustomPatternLock)，通过[Canvas](ts-components-canvas-canvas.md)组件实现了图案密码锁功能，开发者可在此基础上自行进行功能扩展。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

PatternLock(controller?: PatternLockController)

创建图案密码锁组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [PatternLockController](ts-basic-components-patternlock.md#patternlockcontroller) | 否 | 设置PatternLock组件控制器，可用于控制组件状态重置。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### sideLength

PhonePC/2in1TabletTVWearable

sideLength(value: Length)

设置组件的宽度和高度（宽高相同）。当设置为0或负数时，组件不显示。

说明

PatternLock组件设置了通用属性宽高比[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)，且不等于1时（组件尺寸被设定为长方形），九宫格依然绘制为正方形（超出组件范围）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 组件的宽度和高度。默认值：288vp |

### circleRadius

PhonePC/2in1TabletTVWearable

circleRadius(value: Length)

设置宫格中圆点的半径。设置为0或负数时，取默认值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 宫格中圆点的半径。  默认值：6vp  取值范围：(0, sideLength/11]。设置小于等于0的值时，按默认值处理；超过最大值时，按最大值处理。 |

### backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(value: ResourceColor)

设置背景颜色。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 背景颜色。 |

### regularColor

PhonePC/2in1TabletTVWearable

regularColor(value: ResourceColor)

设置宫格圆点在“未选中”状态的填充颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“未选中”状态的填充颜色。  默认值：'#ff182431' |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置宫格圆点在“选中”状态的填充颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“选中”状态的填充颜色。  默认值：'#ff182431' |

### activeColor

PhonePC/2in1TabletTVWearable

activeColor(value: ResourceColor)

设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“激活”状态的填充颜色。  默认值：'#ff182431' |

### pathColor

PhonePC/2in1TabletTVWearable

pathColor(value: ResourceColor)

设置连线的颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 连线的颜色。  默认值：'#33182431' |

### pathStrokeWidth

PhonePC/2in1TabletTVWearable

pathStrokeWidth(value: number | string)

设置连线的宽度。设置为0或负数时连线不显示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 连线的宽度。  默认值：12vp  取值范围：(0, sideLength/3]，设置为0或负数时连线不显示，超过最大值按最大值处理。 |

### autoReset

PhonePC/2in1TabletTVWearable

autoReset(value: boolean)

设置在完成密码输入后再次在组件区域按下时是否重置组件状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 在完成密码输入后再次在组件区域按下时是否重置组件状态。  true：完成密码输入后再次在组件区域按下时重置组件状态（即清除之前输入的密码）；false：完成密码输入后再次在组件区域按下时不重置组件状态。  默认值：true |

### activateCircleStyle12+

PhonePC/2in1TabletTVWearable

activateCircleStyle(options: Optional<CircleStyleOptions>)

设置宫格圆点在“激活”状态下的背景圆环样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<[CircleStyleOptions](ts-basic-components-patternlock.md#circlestyleoptions12对象说明)> | 是 | 宫格圆点在“激活”状态的背景圆环样式。 |

### skipUnselectedPoint15+

PhonePC/2in1TabletTVWearable

skipUnselectedPoint(skipped: boolean)

设置未选中的宫格圆点在密码路径经过时是否自动选中。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| skipped | boolean | 是 | 未选中的宫格圆点在密码路径经过时是否自动选中。  true：跳过选中密码路径经过的宫格圆点；false：自动选中密码路径经过的宫格圆点。默认值：false。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onPatternComplete

PhonePC/2in1TabletTVWearable

onPatternComplete(callback: (input: Array<number>) => void)

密码输入结束时触发该回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | Array<number> | 是 | 与选中宫格圆点顺序一致的数字数组，每个数字表示选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。 |

### onDotConnect11+

PhonePC/2in1TabletTVWearable

onDotConnect(callback: [Callback](js-apis-base.md#callback)<number>)

密码输入选中宫格圆点时触发该回调。

回调参数为选中宫格圆点顺序的数字，数字为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](js-apis-base.md#callback)<number> | 是 | 密码输入选中宫格圆点时触发该回调。 |

## CircleStyleOptions12+对象说明

PhonePC/2in1TabletTVWearable

圆环样式的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 背景圆环颜色。  默认值：'#33182431'。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| radius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 背景圆环的半径。  默认值：[circleRadius](ts-basic-components-patternlock.md#circleradius)的1.833倍（即11/6）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableWaveEffect | boolean | 否 | 是 | 选中宫格圆点后的波浪效果开关。  true：显示波浪效果；false：不显示波浪效果。  默认值：true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableForeground15+ | boolean | 否 | 是 | 背景圆环是否显示在宫格圆点上层。  true：背景圆环显示在宫格圆点上层，遮盖宫格圆点；false：背景圆环显示在宫格圆点下层，不遮盖宫格圆点。  默认值：false。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## PatternLockController

PhonePC/2in1TabletTVWearable

PatternLock组件的控制器，用于重置组件状态。

### 导入对象

```
1. let patternLockController: PatternLockController = new PatternLockController()
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

PatternLockController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### reset

PhonePC/2in1TabletTVWearable

reset()

重置组件状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setChallengeResult11+

PhonePC/2in1TabletTVWearable

setChallengeResult(result: PatternLockChallengeResult): void

设置图案密码的正确或错误状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [PatternLockChallengeResult](ts-basic-components-patternlock.md#patternlockchallengeresult11枚举说明) | 是 | 图案密码状态。包括正确和错误状态。 |

## PatternLockChallengeResult11+枚举说明

PhonePC/2in1TabletTVWearable

图案密码状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CORRECT | 1 | 图案密码正确。 |
| WRONG | 2 | 图案密码错误。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（创建图案密码锁）

该示例展示了PatternLock组件的基本使用方法。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PatternLockExample {
5. @State passwords: number[] = [];
6. @State message: string = 'please input password!';
7. private patternLockController: PatternLockController = new PatternLockController();

9. build() {
10. Column() {
11. Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
12. PatternLock(this.patternLockController)
13. .sideLength(200)
14. .circleRadius(9)
15. .pathStrokeWidth(5)
16. .activeColor('#707070')
17. .selectedColor('#707070')
18. .pathColor('#707070')
19. .backgroundColor('#F5F5F5')
20. .regularColor(Color.Black)
21. .skipUnselectedPoint(false)
22. .autoReset(true)
23. .onDotConnect((index: number) => {
24. console.info('onDotConnect index: ' + index);
25. })
26. }.width('100%').height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/d_GA1vstSfK0FRmlfEgN1Q/zh-cn_image_0000002583439957.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000201Z&HW-CC-Expire=86400&HW-CC-Sign=BABF6BAE30ED9BFB57ADD592A84A272ED0E901D11A9DE519734E4322EF9DF40D)

### 示例2（判断密码是否正确）

该示例通过[sideLength](ts-basic-components-patternlock.md#sidelength)属性设置九宫格的大小、[circleRadius](ts-basic-components-patternlock.md#circleradius)属性设置宫格圆点样式、[onPatternComplete](ts-basic-components-patternlock.md#onpatterncomplete)属性设置密码输入时的回调。

当用户密码输入完成后，按输入的密码不同，给予不同的回应：输入的密码长度小于5时，提示重新输入；第一次输入完成后，提示第二次输入密码；第二次输入完成后，判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入。

通过'Reset PatternLock'按钮，用户可以重置密码锁。

```
1. // xxx.ets
2. import { LengthUnit } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct PatternLockExample {
7. @State passwords: number[] = [];
8. @State message: string = 'please input password!';
9. private patternLockController: PatternLockController = new PatternLockController();

11. build() {
12. Column() {
13. Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
14. PatternLock(this.patternLockController)
15. .sideLength(200)
16. .circleRadius(9)
17. .pathStrokeWidth(5)
18. .activeColor('#707070')
19. .selectedColor('#707070')
20. .pathColor('#707070')
21. .backgroundColor('#F5F5F5')
22. .autoReset(true)
23. .activateCircleStyle({
24. color: '#707070',
25. radius: { value: 16, unit: LengthUnit.VP },
26. enableWaveEffect: true
27. })
28. .onDotConnect((index: number) => {
29. console.info('onDotConnect index: ' + index);
30. })
31. .onPatternComplete((input: Array<number>) => {
32. // 输入的密码长度小于5时，提示重新输入
33. if (input.length < 5) {
34. this.message = 'The password length needs to be greater than 5, please enter again.';
35. return;
36. }
37. // 判断密码长度是否大于0
38. if (this.passwords.length > 0) {
39. // 判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入
40. if (this.passwords.toString() === input.toString()) {
41. this.passwords = input;
42. this.message = 'Set password successfully: ' + this.passwords.toString();
43. this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT);
44. } else {
45. this.message = 'Inconsistent passwords, please enter again.';
46. this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG);
47. }
48. } else {
49. // 提示第二次输入密码
50. this.passwords = input;
51. this.message = 'Please enter again.';
52. }
53. })
54. Button('Reset PatternLock').margin(30).onClick(() => {
55. // 重置密码锁
56. this.patternLockController.reset();
57. this.passwords = [];
58. this.message = 'Please input password';
59. })
60. }.width('100%').height('100%')
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/chp4mQAARsCQzZh4nDjO3w/zh-cn_image_0000002552959912.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000201Z&HW-CC-Expire=86400&HW-CC-Sign=C4D375CAC6868C155CB2969B319EF94E2C248ED71157CA326A03D63AB5CF6493)
