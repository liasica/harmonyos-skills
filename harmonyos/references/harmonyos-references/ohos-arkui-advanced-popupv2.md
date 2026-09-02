---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popupv2
title: PopupV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > PopupV2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bd64f700e79fd3fb229877de664731606f5a0b34771dffe2981d583ceba1408b
---

PopupV2用于显示特定样式的气泡，适用于提示信息、操作确认或信息通知等需要用户关注或响应的场景。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制显示特定样式的气泡，实现更高效的用户界面刷新。

**起始版本：** 26.0.0

## 导入模块

```ts
import { PopupV2, PopupV2Button, PopupV2InitInfo } from '@kit.ArkUI';
```

## 子组件

无

## PopupV2

PopupV2(options: PopupV2InitInfo): void

**起始版本：** 26.0.0

**装饰器类型：** @Builder

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PopupV2InitInfo](ohos-arkui-advanced-popupv2.md#popupv2initinfo) | 是 | 定义PopupV2组件的配置参数。 |

## PopupV2InitInfo

定义PopupV2的具体样式参数。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置PopupV2图标。  **说明：** 默认值：''，不显示图标。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置PopupV2标题文本。  **说明：** 默认值：''，不显示标题文本。 |
| message | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置PopupV2内容文本。  **说明：** 默认值：''，不显示内容文本。 |
| titleModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置标题文本属性，如设置标题颜色、字体大小、字重等。  默认值：undefined，使用系统标题文本属性。 |
| iconModifier | [ImageModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置图标属性，如图标颜色、大小、边框等。  默认值：undefined，使用系统图标属性。 |
| messageModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置内容文本属性，如设置内容文本颜色、字体大小、字重等。  默认值：undefined，使用系统内容文本属性。 |
| showClose | boolean | [Resource](ts-types.md#resource) | 否 | 是 | 设置PopupV2关闭按钮。true：显示关闭按钮；false：不显示关闭按钮。Resource类型：显示对应的图标。  默认值：true |
| onClose | Callback<void> | 否 | 是 | 设置PopupV2关闭按钮回调函数。  默认不设置关闭按钮回调函数。 |
| buttons | [[PopupV2Button](ohos-arkui-advanced-popupv2.md#popupv2button)?,[PopupV2Button](ohos-arkui-advanced-popupv2.md#popupv2button)?] | 否 | 是 | 设置PopupV2操作按钮，按钮最多设置两个。默认不显示按钮。  默认值：[{ text: '' }, { text: '' }] |
| direction | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 设置PopupV2的布局方向，用于控制文本排列与对齐方式，适用于国际化场景下的RTL（从右到左）布局。具体枚举值含义见[Direction](ts-appendix-enums.md#direction)。  默认值：Direction.Auto |
| maxWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置PopupV2的最大宽度，通过此接口PopupV2可以自定义宽度显示。  默认值：400vp  **说明：**  1. 在使用引用资源类型时，规定其参数类型要与属性方法本身类型一致。  2. maxWidth为[Dimension](ts-types.md#dimension10)类型，支持数字、百分比或带单位的字符串（如400、'50%'、'400vp'）。在使用引用资源类型时，资源类型支持float和整型，例如$r('app.float.maxWidth')、$r('app.integer.maxWidth')。  3. 当类型为Resource时，如果未设置单位，默认单位为px。 |

## PopupV2Button

PopupV2Button定义按钮的相关属性和事件。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置按钮内容。 |
| action | Callback<void> | 否 | 是 | 设置按钮点击回调。  默认不执行任何操作。 |
| buttonTextModifier | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置按钮文本属性，如设置文本颜色、字体大小等。默认值：undefined，值为undefined时，默认使用系统按钮文本属性。**模型约束**：此接口仅可在Stage模型下使用。 |

## 示例

### 示例1（设置气泡样式）

该示例通过配置[titleModifier](ohos-arkui-advanced-popupv2.md#popupv2initinfo)、[messageModifier](ohos-arkui-advanced-popupv2.md#popupv2initinfo)、[PopupV2Button](ohos-arkui-advanced-popupv2.md#popupv2button)实现气泡样式。

从API版本26.0.0开始，新增titleModifier、messageModifier、PopupV2Button。

```ts
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Row() {
      // PopupV2自定义高级组件
      PopupV2 ({
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width(300)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/gIg85KQIQsWYG185Jht1iw/zh-cn_image_0000002706836302.png)

### 示例2（设置布局方向）

该示例通过配置[direction](ohos-arkui-advanced-popupv2.md#popupv2initinfo)实现镜像布局效果，适用于国际化场景下的RTL（从右到左）布局需求。

从API版本26.0.0开始，新增direction参数。

```ts
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Column() {
      // PopupV2自定义高级组件
      PopupV2 ({
        direction: Direction.Rtl,
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/KzJpYEzfRNqN-d7nv3a11g/zh-cn_image_0000002736315407.png)

### 示例3（设置自定义宽度）

该示例通过配置[maxWidth](ohos-arkui-advanced-popupv2.md#popupv2initinfo)实现自定义宽度效果，适用于内容较长的消息通知等需要调整显示宽度的场景。

从API版本26.0.0开始，新增maxWidth参数。

```ts
// xxx.ets
import { PopupV2, PopupV2Button } from '@kit.ArkUI';
import { ImageModifier, TextModifier } from '@kit.ArkUI';

@Entry
@ComponentV2
struct PopupExample {

  build() {
    Row() {
      // PopupV2自定义高级组件
      PopupV2 ({
        maxWidth: '50%',
        // 请开发者替换为实际的资源文件
        icon:  $r('app.media.startIcon'),
        iconModifier: new ImageModifier().width(32).height(32).fillColor(Color.White).borderRadius(16),
        title: 'This is a popupv2',
        titleModifier: new TextModifier().fontSize(20).fontColor(Color.Black).fontWeight(FontWeight.Normal),
        message:  'This is the message, This is the message, This is the message, This is the message',
        messageModifier: new TextModifier().fontSize(15).fontColor(Color.Black),
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            buttonTextModifier: new TextModifier().fontSize(15).fontColor(Color.Black)
          }] as [PopupV2Button | undefined, PopupV2Button | undefined]
      })
    }
    .width(400)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/q_8uv8D6R6-aNSdE-pULkw/zh-cn_image_0000002706676368.png)
