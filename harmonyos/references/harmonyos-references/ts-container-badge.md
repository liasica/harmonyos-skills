---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge
title: Badge
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > Badge
category: harmonyos-references
scraped_at: 2026-09-05T06:17:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:506e657260b3e1de785fc885f69c552f256b3e93370690c6731dad1a2b27a512
---

信息标记容器组件，可以附加在单个组件上用于信息提醒。支持数字、字符串和圆点三种标记形式，可自定义标记样式（文本颜色、大小、标记颜色和大小）和显示位置。适用于需要提示用户有新消息或未读消息的场景，例如未读消息计数、新功能提示等，帮助用户快速识别和关注重要信息，提升用户体验。

**说明** 

该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 子组件

支持单个子组件。

**说明** 

* 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 自定义组件宽高默认为0，需要给其设置宽高，否则标记组件将不显示。
* 当存在多个子组件时，只有最后一个子组件会在界面上显示，但其余子组件的状态更新仍会触发Badge及其包含的所有子组件重新布局渲染。
* 不影响子组件布局，即不会主动规避子组件内容。

## 接口

### Badge

Badge(value: BadgeParamWithNumber)

根据数字创建标记组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](ts-container-badge.md#badgeparamwithnumber对象说明) | 是 | 数字标记组件参数，用于配置根据数字创建的Badge组件，包含消息数、显示位置和样式等属性。 |

### Badge

Badge(value: BadgeParamWithString)

根据字符串创建标记组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithString](ts-container-badge.md#badgeparamwithstring对象说明) | 是 | 字符串标记组件参数。 |

## BadgeParam对象说明

包含用于创建Badge组件的基础参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [BadgePosition](ts-container-badge.md#badgeposition枚举说明)|[Position10+](ts-types.md#position) | 否 | 是 | 设置标记显示位置。  默认值：BadgePosition.RightTop  **说明：**  Position作为入参，不支持设置百分比；设置为非法值时，按(0,0)处理，(0,0)为组件左上角位置。  BadgePosition作为入参时，会跟随[Direction](ts-appendix-enums.md#direction)属性控制镜像显示。 |
| style | [BadgeStyle](ts-container-badge.md#badgestyle对象说明) | 否 | 否 | Badge组件可设置样式，支持设置文本颜色、大小、标记颜色和标记大小。 |

## BadgeParamWithNumber对象说明

BadgeParamWithNumber继承自[BadgeParam](ts-container-badge.md#badgeparam对象说明)，具有BadgeParam的全部属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 否 | 设置提醒消息数。  **说明：**  当该值小于等于0且小于maxCount时不显示信息标记。  取值范围：[-2147483648, 2147483647]。超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。 |
| maxCount | number | 否 | 是 | 最大消息数，超过最大消息时仅显示maxCount+，如maxCount是99时，显示99+。  默认值：99  取值范围：[-2147483648, 2147483647]。超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。 |

## BadgeParamWithString对象说明

BadgeParamWithString继承自[BadgeParam](ts-container-badge.md#badgeparam对象说明)，具有BadgeParam的全部属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 提示内容的文本字符串。  **说明：**  value为空字符串时不显示文本，仅显示圆点标记。  从API version 20开始，支持ResourceStr类型。 |

## BadgePosition枚举说明

标记显示位置。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RightTop | - | 标记显示在右上角。 |
| Right | - | 标记显示在右侧纵向居中。 |
| Left | - | 标记显示在左侧纵向居中。 |

## BadgeStyle对象说明

Badge的样式。包括文本颜色、大小、字重、标记颜色和标记大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。  默认值：Color.White  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 文本大小。string类型仅支持number类型取值的字符串形式，可以附带单位，支持的单位有"px"、"vp"、"fp"、"lpx"，例如"10"、"10fp"，不附带单位时默认单位为"fp"。  默认值：10vp  默认单位：fp  取值范围：大于0；取值为0时不显示文本，取值小于0时取默认值。  **说明：**  1. 不支持设置百分比，当设置为百分比时，按照默认值处理。  2. 从API version 20开始，支持ResourceStr类型。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| badgeSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Badge的大小。string类型支持number类型取值的字符串形式，可以附带单位，支持的单位有"px"、"vp"、"fp"、"lpx"，例如"16"、"16fp"，不附带单位时默认单位为"fp"。  默认值：16vp  默认单位：fp  取值范围：大于0；取值为0时不显示Badge，取值小于0时取默认值。  **说明：**  1. 不支持设置百分比，当设置为百分比时，按照默认值处理。  2. 从API version 20开始，支持ResourceStr类型。  3. 当设置了fontSize且badgeSize小于fontSize时，badgeSize将按照fontSize生效。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| badgeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Badge的颜色。  默认值：Color.Red  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight10+ | number | [FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置文本的字体粗细。number类型取值范围：[100, 900]，取值间隔为100。取值越大，字体越粗。设置number类型在取值范围外时，按默认值400处理。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal  **说明：**  不支持设置百分比，当设置为百分比时，按照默认值处理。从API version 20开始，支持ResourceStr类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| borderColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 底板描边颜色。  默认值：Color.Red  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| borderWidth10+ | [Length](ts-types.md#length) | 否 | 是 | 底板描边粗细。  默认值：1  单位：vp  **说明：**  不支持设置百分比，当设置为百分比时，按照默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| outerBorderColor22+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 底板外描边颜色。  默认值：Color.White  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| outerBorderWidth22+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 底板外描边粗细。  默认值：0  单位：vp  不支持设置百分比，当设置为百分比时，按照默认值处理。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| enableAutoAvoidance22+ | boolean | 否 | 是 | 角标文本延伸显示时是否避让。  true表示避让，false表示不避让。  默认值：false  **说明：**  1. 避让效果为角标文本向组件内部延伸显示。  2. 当外描边的宽度大于0时，角标的延伸起点为外描边的内侧。  3. 当position设置为具体坐标值时，角标不进行避让处理。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。  **模型约束：** 此接口仅可在Stage模型下使用。 |

**说明** 

当borderWidth大于0且borderColor与badgeColor颜色不一致时，先绘制角标，再绘制描边。由于边缘像素经过抗锯齿处理，抗锯齿产生半透明像素，四角会出现 badgeColor 颜色的描边线。如需实现相关场景，建议使用[Text](ts-basic-components-text.md)组件设置[outline](ts-universal-attributes-outline.md#outline)代替Badge组件。

## 属性

支持[通用属性](ts-component-general-attributes.md)。

## 事件

支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（设置标记组件内容）

该示例通过[BadgeParamWithNumber](ts-container-badge.md#badgeparamwithnumber对象说明)的入参count、[BadgeParamWithString](ts-container-badge.md#badgeparamwithstring对象说明)的入参value，实现了传入空值、字符、数字时标记组件展现不同的效果。

```ts
// xxx.ets
@Entry
@Component
struct BadgeExample {
  @Builder
  tabBuilder(index: number) {
    Column() {
      if (index === 2) {
        Badge({
          value: '',
          style: { badgeSize: 6, badgeColor: '#FA2A2D' }
        }) {
          Image('/common/public_icon_off.svg')
            .width(24)
            .height(24)
        }
        .width(24)
        .height(24)
        .margin({ bottom: 4 })
      } else {
        Image('/common/public_icon_off.svg')
          .width(24)
          .height(24)
          .margin({ bottom: 4 })
      }
      Text('Tab')
        .fontColor('#182431')
        .fontSize(10)
        .fontWeight(500)
        .lineHeight(14)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }

  @Builder
  itemBuilder(value: string) {
    Row() {
      Image('common/public_icon.svg').width(32).height(32).opacity(0.6)
      Text(value)
        .width(177)
        .height(21)
        .margin({ left: 15, right: 76 })
        .textAlign(TextAlign.Start)
        .fontColor('#182431')
        .fontWeight(500)
        .fontSize(16)
        .opacity(0.9)
      Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)
    }.width('100%').padding({ left: 12, right: 12 }).height(56)
  }

  build() {
    Column() {
      // 红点类型的标记组件
      Text('dotsBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
      Tabs() {
        TabContent()
          .tabBar(this.tabBuilder(0))
        TabContent()
          .tabBar(this.tabBuilder(1))
        TabContent()
          .tabBar(this.tabBuilder(2))
        TabContent()
          .tabBar(this.tabBuilder(3))
      }
      .width(360)
      .height(56)
      .backgroundColor('#F1F3F5')

      // 根据字符创建的标记组件
      Column() {
        Text('stringBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
        List({ space: 12 }) {
          ListItem() {
            Text('list1').fontSize(14).fontColor('#182431').margin({ left: 12 })
          }
          .width('100%')
          .height(56)
          .backgroundColor('#FFFFFF')
          .borderRadius(24)
          .align(Alignment.Start)

          ListItem() {
            Badge({
              value: 'New',
              position: BadgePosition.Right,
              style: { badgeSize: 16, badgeColor: '#FA2A2D' }
            }) {
              Text('list2').width(27).height(19).fontSize(14).fontColor('#182431')
            }.width(49.5).height(19)
            .margin({ left: 12 })
          }
          .width('100%')
          .height(56)
          .backgroundColor('#FFFFFF')
          .borderRadius(24)
          .align(Alignment.Start)
        }.width(336)

        // 根据数字创建的标记组件
        Text('numberBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
        List() {
          ListItem() {
            this.itemBuilder('list1')
          }

          ListItem() {
            Row() {
              Image('common/public_icon.svg').width(32).height(32).opacity(0.6)
              Badge({
                count: 1,
                position: BadgePosition.Right,
                style: { badgeSize: 16, badgeColor: '#FA2A2D' }
              }) {
                Text('list2')
                  .width(177)
                  .height(21)
                  .textAlign(TextAlign.Start)
                  .fontColor('#182431')
                  .fontWeight(500)
                  .fontSize(16)
                  .opacity(0.9)
              }.width(240).height(21).margin({ left: 15, right: 11 })

              Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)
            }.width('100%').padding({ left: 12, right: 12 }).height(56)
          }

          ListItem() {
            this.itemBuilder('list3')
          }

          ListItem() {
            this.itemBuilder('list4')
          }
        }
        .width(336)
        .height(232)
        .backgroundColor('#FFFFFF')
        .borderRadius(24)
        .padding({ top: 4, bottom: 4 })
        .divider({
          strokeWidth: 0.5,
          color: 'rgba(0,0,0,0.1)',
          startMargin: 60,
          endMargin: 12
        })
      }.width('100%').backgroundColor('#F1F3F5').padding({ bottom: 12 })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/m7PvWPe0QD-jVqrIpOO72A/zh-cn_image_0000002742005277.png)

### 示例2（设置数字控制标记显隐）

该示例通过count属性，实现了设置数字0和1时标记组件的隐藏和显示效果。

```ts
@Entry
@Component
struct Index {
  @State badgeCount: number = 1;

  build() {
    Column({ space: 40 }) {
      Badge({
        count: this.badgeCount,
        style: {},
        position: BadgePosition.RightTop,
      }) {
        Image($r('app.media.startIcon'))
          .width(50)
          .height(50)
      }
      .width(55)

      Button('count 0').onClick(() => {
        this.badgeCount = 0;
      })
      Button('count 1').onClick(() => {
        this.badgeCount = 1;
      })
    }
    .margin({ top: 20 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uAX6PLw9S7KDOg-LE3HhPQ/zh-cn_image_0000002712406288.gif)

### 示例3（设置外描边和文本延伸方式）

从API version 22开始，该示例使用outerBorderColor和outerBorderWidth属性设置外描边，通过enableAutoAvoidance属性控制增加角标文本延伸显示时是否避让。

```ts
// 该示例实现了Badge组件自定义外描边和文本延伸方向
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State badgeValue: string = '1234';
  @State textAvoid: boolean[] = [false, true];
  @State textAvoidIndex: number = 0;
  @State textAvoidString: string [] = ['false', 'true'];
  build() {
    Column() {
      Badge({
        value: this.badgeValue,
        style: {
          badgeSize: 30,
          fontSize: 20,
          outerBorderColor : Color.Pink,
          outerBorderWidth : LengthMetrics.vp(5),
          enableAutoAvoidance : this.textAvoid[this.textAvoidIndex]
        },
        position: BadgePosition.RightTop
      }) {
        // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.startIcon'))
          .width(80)
          .height(80)
      }
      .direction(Direction.Ltr)
      .margin({ top: 20, bottom: 20 })
      Button('enableAutoAvoidance ： ' + this.textAvoidString[this.textAvoidIndex])
        .onClick(() => {
          this.textAvoidIndex = (this.textAvoidIndex + 1) % this.textAvoidString.length;
        })
    }
    .width('100%')
    .height('80%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/NzsT-nizQYqxPgcnh2053g/zh-cn_image_0000002742125237.png)
