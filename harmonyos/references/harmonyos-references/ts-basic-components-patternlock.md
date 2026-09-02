---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock
title: PatternLock
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > PatternLock
category: harmonyos-references
scraped_at: 2026-09-02T15:01:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a081c2dcae547c8e5878d70c5be90c49948bae9d55feb1b760d09f8a466ba6c
---

图案密码锁组件，以九宫格图案的方式输入密码，用于密码验证场景。组件支持自定义九宫格尺寸、圆点及连线样式、选中/激活状态颜色等外观属性，支持密码输入过程中的实时反馈以及密码验证结果（正确/错误）的状态设置。手指在PatternLock组件区域按下时开始进入输入状态，手指离开屏幕时结束输入状态完成密码输入。

**说明** 

* 该组件从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 如果开发者有其他功能需求，可以使用[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)。例如自定义组件[CustomPatternLock](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/master/ArkUISample/CustomPatternLock)，通过[Canvas](ts-components-canvas-canvas.md)组件实现了图案密码锁功能，开发者可在此基础上自行进行功能扩展。

## 子组件

无

## 接口

PatternLock(controller?: PatternLockController)

创建图案密码锁组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [PatternLockController](ts-basic-components-patternlock.md#patternlockcontroller) | 否 | 设置PatternLock组件控制器，用于重置组件状态和设置图案密码状态。当需要程序化控制组件状态（如重置密码锁、设置密码验证结果）时传入此参数；不传入时无法通过控制器手动操作组件状态（即无法调用reset()、setChallengeResult()等方法）。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### sideLength

sideLength(value: Length)

设置组件的宽度和高度（宽高相同）。当设置为0或负数时，组件不显示。未通过该接口设置时，默认宽高为288vp。

**说明** 

PatternLock组件设置了通用属性宽高比[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)，且不等于1时（组件尺寸被设定为长方形），九宫格依然绘制为正方形（超出组件范围）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 组件的宽度和高度。  取值范围：大于0。  设置为0或负数时，组件不显示。 |

### circleRadius

circleRadius(value: Length)

设置宫格中圆点的半径。未通过该接口设置时，默认半径为6vp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 宫格中圆点的半径。  取值范围：(0, sideLength/11]。设置小于等于0的值时，按默认值处理；超过最大值时，按最大值处理。 |

### backgroundColor

backgroundColor(value: ResourceColor)

设置背景颜色。未通过该接口设置时，默认为透明，无背景色。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 背景颜色。 |

### regularColor

regularColor(value: ResourceColor)

设置宫格圆点在“未选中”状态的填充颜色。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“未选中”状态的填充颜色。 |

### selectedColor

selectedColor(value: ResourceColor)

设置宫格圆点在“选中”状态的填充颜色。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“选中”状态的填充颜色。 |

### activeColor

activeColor(value: ResourceColor)

设置宫格圆点在“激活”状态的填充颜色，“激活”状态为手指经过圆点但还未选中的状态。未通过该接口设置时，默认填充颜色为'#ff182431'（深灰色）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 宫格圆点在“激活”状态的填充颜色。 |

### pathColor

pathColor(value: ResourceColor)

设置连线的颜色。未通过该接口设置时，默认连线颜色为'#33182431'（深灰色，20%不透明度）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 连线的颜色。 |

### pathStrokeWidth

pathStrokeWidth(value: number | string)

设置连线的宽度。未通过该接口设置时，默认连线宽度为12vp。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 连线的宽度。  单位：vp  取值范围：(0, sideLength/3]，设置为0或负数时连线不显示，超过最大值按最大值处理。 |

### autoReset

autoReset(value: boolean)

设置在完成密码输入后再次在组件区域按下时是否重置组件状态。未通过该接口设置时，默认重置组件状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 在完成密码输入后再次在组件区域按下时是否重置组件状态。  true：重置组件状态（即清除之前输入的密码）；false：不重置组件状态。 |

### activateCircleStyle12+

activateCircleStyle(options: Optional<CircleStyleOptions>)

设置宫格圆点在“激活”状态下的背景圆环样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<[CircleStyleOptions](ts-basic-components-patternlock.md#circlestyleoptions12对象说明)> | 是 | 宫格圆点在“激活”状态的背景圆环样式。 |

### skipUnselectedPoint15+

skipUnselectedPoint(skipped: boolean)

设置未选中的宫格圆点在密码路径经过时是否跳过选中。未通过该接口设置时，未选中的宫格圆点在密码路径经过时默认自动选中。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| skipped | boolean | 是 | 未选中的宫格圆点在密码路径经过时是否跳过选中。  true：跳过选中；false：自动选中。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onPatternComplete

onPatternComplete(callback: (input: Array<number>) => void)

密码输入结束时触发该回调。

**说明** 

该回调在密码输入结束时触发，返回完整密码数组。与[onDotConnect](ts-basic-components-patternlock.md#ondotconnect11)的关系：onDotConnect在选中每个圆点时实时触发，onPatternComplete在输入结束时触发，两者可以配合使用以实现实时反馈和最终验证。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | Array<number> | 是 | 与选中宫格圆点顺序一致的数字数组，每个数字表示选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。 |

### onDotConnect11+

onDotConnect(callback: import('../api/@ohos.base').Callback<number>)

密码输入选中宫格圆点时触发该回调。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | import('../api/@ohos.base').[Callback](js-apis-base.md#callback)<number> | 是 | 密码输入选中宫格圆点时触发该回调。回调参数为选中宫格圆点的索引值（第一行圆点从左往右依次为0、1、2，第二行圆点从左往右依次为3、4、5，第三行圆点从左往右依次为6、7、8）。 |

## CircleStyleOptions12+对象说明

圆环样式的参数说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 背景圆环颜色。  默认值：'#33182431'（深灰色，20%不透明度）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| radius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 背景圆环的半径。  默认值：[circleRadius](ts-basic-components-patternlock.md#circleradius)的约1.833倍（即11/6）。  取值范围：大于0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableWaveEffect | boolean | 否 | 是 | 选中宫格圆点后的波浪效果开关。  true：显示波浪效果；false：不显示波浪效果。  默认值：true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableForeground15+ | boolean | 否 | 是 | 背景圆环是否显示在宫格圆点上层。  true：背景圆环显示在宫格圆点上层，遮盖宫格圆点；false：背景圆环显示在宫格圆点下层，不遮盖宫格圆点。  默认值：false。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |

## PatternLockController

PatternLock组件的控制器，用于重置组件状态和设置图案密码状态。

### 导入对象

```typescript
let patternLockController: PatternLockController = new PatternLockController();
```

### constructor

constructor()

PatternLockController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### reset

reset()

重置组件状态。需要在PatternLock组件构造时传入对应的controller参数才可生效，未传入时调用不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setChallengeResult11+

setChallengeResult(result: PatternLockChallengeResult): void

设置图案密码的正确或错误状态。需要在PatternLock组件构造时传入对应的controller参数才可生效，未传入时调用不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [PatternLockChallengeResult](ts-basic-components-patternlock.md#patternlockchallengeresult11枚举说明) | 是 | 图案密码状态。包括正确和错误状态。 |

## PatternLockChallengeResult11+枚举说明

图案密码状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CORRECT | 1 | 图案密码正确。 |
| WRONG | 2 | 图案密码错误。 |

## 示例

### 示例1（创建图案密码锁）

该示例展示了PatternLock组件的基本使用方法。

```ts
// xxx.ets
@Entry
@Component
struct PatternLockExample {
  @State passwords: number[] = [];
  @State message: string = 'please input password!';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .regularColor(Color.Black)
        .autoReset(true)
        .onDotConnect((index: number) => {
          console.info('onDotConnect index: ' + index);
        })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/PmV980xbQ_GnSDPQfRfktw/zh-cn_image_0000002736435241.gif)

### 示例2（判断密码是否正确）

该示例通过[sideLength](ts-basic-components-patternlock.md#sidelength)属性设置九宫格的大小、[circleRadius](ts-basic-components-patternlock.md#circleradius)属性设置宫格中圆点的半径、[onPatternComplete](ts-basic-components-patternlock.md#onpatterncomplete)属性设置密码输入完成时的回调。

当用户密码输入完成后，按输入的密码不同，给予不同的回应：输入的密码长度小于5时，提示重新输入；第一次输入完成后，提示第二次输入密码；第二次输入完成后，判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入。

通过'Reset PatternLock'按钮，用户可以重置密码锁。

```ts
// xxx.ets
import { LengthUnit } from '@kit.ArkUI';

@Entry
@Component
struct PatternLockExample {
  @State passwords: number[] = [];
  @State message: string = 'Please input password';
  private patternLockController: PatternLockController = new PatternLockController();

  build() {
    Column() {
      Text(this.message).textAlign(TextAlign.Center).margin(20).fontSize(20)
      PatternLock(this.patternLockController)
        .sideLength(200)
        .circleRadius(9)
        .pathStrokeWidth(5)
        .activeColor('#707070')
        .selectedColor('#707070')
        .pathColor('#707070')
        .backgroundColor('#F5F5F5')
        .autoReset(true)
        .activateCircleStyle({
          color: '#707070',
          radius: { value: 16, unit: LengthUnit.VP },
          enableWaveEffect: true
        })
        .onDotConnect((index: number) => {
          console.info('onDotConnect index: ' + index);
        })
        .onPatternComplete((input: Array<number>) => {
          // 输入的密码长度小于5时，提示重新输入
          if (input.length < 5) {
            this.message = 'The password length needs to be at least 5, please enter again.';
            return;
          }
          // 判断密码长度是否大于0
          if (this.passwords.length > 0) {
            // 判断两次输入的密码是否相同，相同则提示密码设置成功，否则提示重新输入
            if (this.passwords.toString() === input.toString()) {
              this.passwords = input;
              this.message = 'Set password successfully: ' + this.passwords.toString();
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.CORRECT);
            } else {
              this.message = 'Inconsistent passwords, please enter again.';
              this.patternLockController.setChallengeResult(PatternLockChallengeResult.WRONG);
            }
          } else {
            // 提示第二次输入密码
            this.passwords = input;
            this.message = 'Please enter again.';
          }
        })
      Button('Reset PatternLock').margin(30).onClick(() => {
        // 重置密码锁
        this.patternLockController.reset();
        this.passwords = [];
        this.message = 'Please input password';
      })
    }.width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Tm2r0y_9QPat3M4mkxp6aw/zh-cn_image_0000002706836094.gif)
