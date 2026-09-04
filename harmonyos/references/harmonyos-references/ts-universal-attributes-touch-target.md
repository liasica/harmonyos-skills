---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-touch-target
title: 触摸热区设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 触摸交互控制 > 触摸热区设置
category: harmonyos-references
scraped_at: 2026-09-05T06:17:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b0571895dad6df990805e1b0c34760eb8db36459af6c251d8a9e07c3b6ed3819
---

设置组件的触摸热区。在ArkUI开发框架中，处理触屏事件和鼠标事件时，会在事件触发前进行按压点与组件响应热区的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)，以收集需响应事件的组件。基于测试结果，框架会分发相应的事件。影响[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)和[手势事件](ts-gesture-settings.md)的分发。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 设置触摸热区属性时，手指需在热区内按下，随后抬起时若满足事件响应条件，事件将被触发。此外，在当前手势结束前，若条件满足，可持续触发的事件也会被激活。

## responseRegion

responseRegion(value: Array<Rectangle> | Rectangle): T

设置一个或多个触摸热区。调用[responseRegionList](ts-universal-attributes-touch-target.md#responseregionlist22)接口时，该接口不再生效。从API版本26.0.0开始，未主动设置时[Button](ts-basic-components-button.md)、[Button模式的Toggle](ts-basic-components-toggle.md)、[Select](ts-basic-components-select.md)、[Chip](ohos-arkui-advanced-chip.md)和[ChipGroup](ohos-arkui-advanced-chipgroup.md)组件的触摸热区默认最小高度从28vp变更为32vp。该变更仅影响触摸命中范围，不影响组件实际显示高度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明)> | [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 是 | 触摸热区，包括位置和大小。  默认触摸热区为整个组件，默认值：  {  x：0,  y：0,  width：'100%',  height：'100%'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于支持链式调用。 |

## mouseResponseRegion10+

mouseResponseRegion(value: Array<Rectangle> | Rectangle): T

设置一个或多个鼠标触摸热区。调用[responseRegionList](ts-universal-attributes-touch-target.md#responseregionlist22)接口时，该接口不再生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明)> | [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 是 | 鼠标触摸热区，包括位置和大小。  默认触摸热区为整个组件，默认值：  {  x：0,  y：0,  width：'100%',  height：'100%'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于支持链式调用。 |

## responseRegionList22+

responseRegionList(regions: Array<ResponseRegion>): T

设置组件的触摸热区列表。调用该接口时，[responseRegion](ts-universal-attributes-touch-target.md#responseregion)与[mouseResponseRegion](ts-universal-attributes-touch-target.md#mouseresponseregion10)接口不再生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regions | Array<[ResponseRegion](ts-universal-attributes-touch-target.md#responseregion22对象说明)> | 是 | 组件的触摸热区数组。  每个触摸热区均包括输入工具类型、位置和大小。  默认值：  [{  tool：ResponseRegionSupportedTool.ALL,  x：LengthMetrics.vp(0),  y：LengthMetrics.vp(0),  width：LengthMetrics.percent(1),  height：LengthMetrics.percent(1)  }] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于支持链式调用。 |

## Rectangle对象说明

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | [Length](ts-types.md#length) | 否 | 是 | 触摸点相对于组件左上角的x轴坐标。  默认值：0vp |
| y | [Length](ts-types.md#length) | 否 | 是 | 触摸点相对于组件左上角的y轴坐标。  默认值：0vp |
| width | [Length](ts-types.md#length) | 否 | 是 | 触摸热区的宽度。  默认值：'100%' |
| height | [Length](ts-types.md#length) | 否 | 是 | 触摸热区的高度。  默认值：'100%' |

**说明** 

* x和y可以设置正负值百分比。当x设置为'100%'时表示热区往右偏移组件本身宽度大小，当x设置为'-100%'时表示热区往左偏移组件本身宽度大小。当y设置为'100%'时表示热区往下偏移组件本身高度大小，当y设置为'-100%'时表示热区往上偏移组件本身高度大小。
* width和height设置百分比时，只能设置正值百分比。width：'100%'表示热区宽度设置为该组件本身的宽度。比如组件本身宽度是100vp，那么'100%'表示热区宽度也为100vp。height：'100%'表示热区高度设置为该组件本身的高度。
* 百分比相对于组件自身宽高进行计算。
* 当父组件设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)(true)时，子组件的响应会受到父组件触摸热区的影响，不在父组件触摸热区内的子组件无法响应手势和事件。
* width和height不支持calc()的动态计算。

## ResponseRegion22+对象说明

由输入工具类型、触摸位置和大小组成的触摸热区。

**说明** 

* 当父组件设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)为true时，子组件的响应会受到父组件触摸热区的影响，不在父组件触摸热区内的子组件无法响应手势和事件。
* 如果触摸热区未配置输入工具类型、触摸位置或大小，对应项采用默认值。
* x和y的计算结果为正值时，分别代表向右偏移和向下偏移；当计算结果为负值时，分别代表向左偏移和向上偏移。
* width和height采用string类型时，string需采用小写字符，否则不生效，支持calc()的动态计算。指定calc()的入参字符串格式为'宽高缩放比例 ± 宽高增量'，宽高缩放比例为百分比，宽高增量单位为px或vp。例如'calc(80% + 10vp)'中，80%为宽高缩放比例、10vp为宽高增量。width和height采用LengthMetrics类型且单位为percent时，相对于组件自身宽高进行计算，percent(1)代表100%。当计算结果为负值时，采用默认值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tool | [ResponseRegionSupportedTool](ts-appendix-enums.md#responseregionsupportedtool22) | 否 | 是 | 触摸热区适用的输入工具类型。  默认值：ResponseRegionSupportedTool.ALL |
| x | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 触摸点相对于组件左上角的x轴坐标。  默认值：LengthMetrics.vp(0) |
| y | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 触摸点相对于组件左上角的y轴坐标。  默认值：LengthMetrics.vp(0) |
| width | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | string | 否 | 是 | 触摸热区的宽度。  默认值：LengthMetrics.percent(1) |
| height | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | string | 否 | 是 | 触摸热区的高度。  默认值：LengthMetrics.percent(1) |

## 示例

### 示例1（通过responseRegion接口设置触摸热区）

该示例通过responseRegion设置按钮的触摸热区以响应点击事件。

```ts
// xxx.ets
@Entry
@Component
struct TouchTargetExample {
  @State text: string = '';

  build() {
    Column({ space: 20 }) {
      Text("{x:0,y:0,width:'50%',height:'100%'}")
      // 热区宽度为按钮的一半，点击button1右半部无响应
      Button('button1')
        .responseRegion({
          x: 0,
          y: 0,
          width: '50%',
          height: '100%'
        })
        .onClick(() => {
          this.text = 'button1 clicked';
        })

      // 为一个组件添加多个热区
      Text("[{x:'100%',y:0,width:'50%',height:'100%'}," +
        "\n{ x: 0, y: 0, width: '50%', height: '100%' }]")
      Button('button2')
        .responseRegion([
          {
            x: '100%',
            y: 0,
            width: '50%',
            height: '100%'
          }, // 第一个热区宽度为按钮的一半，且右移一个按钮宽度，点击button2右边按钮宽度一半的区域，点击事件生效
          {
            x: 0,
            y: 0,
            width: '50%',
            height: '100%'
          } // 第二个热区宽度为按钮的一半，点击button2左半部，点击事件生效
        ])
        .onClick(() => {
          this.text = 'button2 clicked';
        })
      // 热区大小为整个按钮，且下移一个按钮高度，点击button3下方按钮大小区域，点击事件生效
      Text("{x:0,y:'100%',width:'100%',height:'100%'}")
      Button('button3')
        .responseRegion({
          x: 0,
          y: '100%',
          width: '100%',
          height: '100%'
        })
        .onClick(() => {
          this.text = 'button3 clicked';
        })

      Text(this.text).margin({ top: 50 })
    }.width('100%').margin({ top: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/RjnRHovATRqZMNsJx7vKDA/zh-cn_image_0000002742124835.gif)

### 示例2（通过responseRegionList接口设置触摸热区）

该示例通过[responseRegionList](ts-universal-attributes-touch-target.md#responseregionlist22)设置按钮的触摸热区以响应点击事件。

从API version 22开始，新增responseRegionList接口。

```ts
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct TouchTargetExample {
  @State text: string = '';

  build() {
    Column({ space: 20 }) {
      Text('left part of button1')
      // 热区宽度为按钮的一半，点击button1右半部无响应
      Button('button1')
        .responseRegionList([{
          x: LengthMetrics.vp(0),
          y: LengthMetrics.vp(0),
          width: LengthMetrics.percent(0.5),
          height: LengthMetrics.percent(1),
        }])
        .onClick(() => {
          this.text = 'button1 clicked';
        })

      // 热区一的大小为整个按钮，且右移一个按钮宽度，点击button2右边按钮大小区域，点击事件生效
      // 热区二的大小为整个按钮，且下移一个按钮高度，鼠标点击button2下方按钮大小区域，点击事件生效
      Text('one button size right of button2,' + '\n one button size below button2')
      Button('button2')
        .responseRegionList([{
          x: LengthMetrics.percent(1),
          y: LengthMetrics.vp(0),
          width: LengthMetrics.percent(1),
          height: LengthMetrics.percent(1),
        }, {
          tool: ResponseRegionSupportedTool.MOUSE,
          x: LengthMetrics.vp(0),
          y: LengthMetrics.percent(1),
          width: 'calc(100% + 0vp)',
          height: 'calc(100% - 0px)',
        }])
        .onClick(() => {
          this.text = 'button2 clicked';
        })

      Text(this.text).margin({ top: 50 })
    }.width('100%').margin({ top: 10 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/DthOk4_cRDKcsbyE_6quvA/zh-cn_image_0000002712245928.gif)

### 示例3（设置鼠标的触摸热区以响应点击事件）

该示例通过[mouseResponseRegion](ts-universal-attributes-touch-target.md#mouseresponseregion10)设置鼠标的触摸热区以响应点击事件。

```ts
// xxx.ets
@Entry
@Component
struct MouseResponseRegionExample {
  @State clickInfo: string = '点击热区触发事件';

  build() {
    Column({ space: 30 }) {
      // 示例1：单个热区（仅按钮左半部分响应鼠标点击）
      Text('热区：按钮左半区域（点击左半才触发）')
        .fontSize(14)
      Button('Button1（左半热区）')
        .width(200)
        .height(60)
        // 鼠标热区：仅按钮左半部分（x/y相对组件自身，宽度50%）
        .mouseResponseRegion({
          // 热区相对组件的X坐标（左上角为原点）
          x: 0,
          // 热区相对组件的Y坐标
          y: 0,
          // 热区宽度（按钮的50%）
          width: '50%',
          // 热区高度（按钮的100%）
          height: '100%'
        })
        .onClick(() => {
          this.clickInfo = 'Button1 左半热区被点击';
        })
      // 示例2：多个热区（按钮左半 + 按钮下方区域都响应）
      Text('热区：按钮左半 + 按钮下方区域（点击两处都触发）')
        .fontSize(14)
      Button('Button2（多热区）')
        .width(200)
        .height(60)
        // 鼠标热区：数组形式，包含2个独立热区
        .mouseResponseRegion([
          // 热区1：按钮左半部分
          {
            x: 0,
            y: 0,
            width: '50%',
            height: '100%'
          },
          // 热区2：按钮正下方区域（y=100%表示按钮底部，高度60vp）
          {
            x: 0,
            y: '100%',
            width: '100%',
            height: 60
          }
        ])
        .onClick(() => {
          this.clickInfo = 'Button2 任一热区被点击';
        })
      // 示例3：热区在按钮外部（按钮右侧空白处响应）
      Text('热区：按钮右侧外部（点击按钮右边空白处触发）')
        .fontSize(14)
      Button('Button3（右侧外热区）')
        .width(200)
        .height(60)
        // 鼠标热区：按钮右侧外部区域（x=100%表示按钮右边缘）
        .mouseResponseRegion({
          // 热区X坐标：按钮右边缘
          x: '100%',
          y: 0,
          // 热区宽度80vp
          width: 80,
          height: '100%'
        })
        .onClick(() => {
          this.clickInfo = 'Button3 右侧外热区被点击';
        })
      // 显示点击结果
      Text(this.clickInfo)
        .fontSize(16)
        .margin({ top: 20 })
    }
    .width('100%')
    .height('100%')
    // 整体居中显示
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/J-y-kizQQbqq399ejW2h7g/zh-cn_image_0000002742004877.gif)
