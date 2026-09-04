---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup
title: Popup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > Popup
category: harmonyos-references
scraped_at: 2026-09-05T06:17:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:69f83f17284110a11925bd0636ff549c97a7c8f8c26a68e5127ac37c0413c8f7
---

Popup是用于显示特定样式气泡的组件，支持图标、文本和按钮的灵活组合，适用于通知提示、信息确认、警告提示等场景。通过可定制的样式选项，能够快速实现一致的气泡交互体验。

**说明** 

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 建议结合[Popup控制](ts-universal-attributes-popup.md)中的自定义气泡功能。

## 导入模块

```ts
import { Popup, PopupOptions, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';
```

## 子组件

无

## Popup

Popup(options: PopupOptions): void

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PopupOptions](ohos-arkui-advanced-popup.md#popupoptions) | 是 | Popup组件的配置参数。 |

## PopupOptions

PopupOptions定义Popup的具体样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [PopupIconOptions](ohos-arkui-advanced-popup.md#popupiconoptions) | 否 | 是 | 设置Popup图标。  **说明：**  当width和height设置异常值或0时不显示。  默认不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | [PopupTextOptions](ohos-arkui-advanced-popup.md#popuptextoptions) | 否 | 是 | 设置Popup标题文本。  默认不显示标题文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| message | [PopupTextOptions](ohos-arkui-advanced-popup.md#popuptextoptions) | 否 | 否 | 设置Popup内容文本。  **说明：**  message不支持设置fontWeight。  默认不显示内容文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| showClose | boolean | [Resource](ts-types.md#resource) | 否 | 是 | 设置Popup关闭按钮。  true：显示关闭按钮；false：不显示关闭按钮。  Resource：显示对应的图标。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onClose | () => void | 否 | 是 | 设置Popup关闭按钮回调函数。  默认不设置关闭按钮回调函数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttons | [[PopupButtonOptions](ohos-arkui-advanced-popup.md#popupbuttonoptions)?,[PopupButtonOptions](ohos-arkui-advanced-popup.md#popupbuttonoptions)?] | 否 | 是 | 设置Popup操作按钮，按钮最多设置两个。  默认不显示按钮。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 设置Popup内容的布局方向，可用枚举值见[Direction](ts-appendix-enums.md#direction)。  默认值：Direction.Auto  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxWidth18+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置Popup的最大宽度，支持自定义宽度显示。  **说明：**  1. 在使用引用资源类型时，规定其参数类型要与maxWidth属性本身的类型一致。  2. maxWidth是[Dimension](ts-types.md#dimension10)类型，支持数字类型和百分比字符串类型。数字类型支持float和integer，例如$r('app.float.maxWidth')、$r('app.integer.maxWidth')；百分比字符串例如'50%'。  3. 当类型为Resource时，如果未设置单位，默认单位为px。  默认值：400vp  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## PopupTextOptions

设置文本样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置文本内容。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本字体大小。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。  number：取值范围(0,+∞)。为number类型时单位：fp。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置文本字体颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_secondary') |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 设置文本字体粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Regular |

## PopupButtonOptions

PopupButtonOptions定义按钮的相关属性和事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置按钮内容。 |
| action | () => void | 否 | 是 | 设置按钮click回调。  默认不执行任何操作。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置按钮文本字体大小。  默认值：$r('sys.float.ohos\_id\_text\_size\_button2')  string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。  number：取值范围(0,+∞)。为number类型时单位：fp。  设置值为异常值时取默认值。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置按钮文本字体颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated') |

## PopupIconOptions

PopupIconOptions定义图标的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置图标内容。 |
| width | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置图标宽度。单位：vp。  默认值：32vp |
| height | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置图标高度。单位：vp。  默认值：32vp |
| fillColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置图标填充颜色。仅针对svg图源生效。  默认不改变图标颜色。 |
| borderRadius | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 设置图标圆角。单位：vp。  默认值：$r('sys.float.ohos\_id\_corner\_radius\_default\_s') |

## 示例

### 示例1（设置气泡样式）

该示例通过配置PopupIconOptions、PopupTextOptions、PopupButtonOptions实现气泡的样式。

```ts
// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupExample {
  build() {
    Row() {
      // popup 自定义高级组件
      Popup({
        // PopupIconOptions类型设置图标内容
        icon: {
          // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
          image: $r('app.media.icon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16
        } as PopupIconOptions,
        // PopupTextOptions 类型设置文字内容
        title: {
          text: 'This is a popup with PopupOptions',
          fontSize: 20,
          fontColor: Color.Black,
          fontWeight: FontWeight.Normal
        } as PopupTextOptions,
        // PopupTextOptions 类型设置文字内容
        message: {
          text: 'This is the message',
          fontSize: 15,
          fontColor: Color.Black
        } as PopupTextOptions,
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        // PopupButtonOptions 类型设置按钮内容
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black
          },] as [PopupButtonOptions?, PopupButtonOptions?]
      })
    }
    .width(300)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/gFoL5tV3QC633ID9N8FR0g/zh-cn_image_0000002742005515.png)

### 示例2（设置镜像效果）

该示例通过配置direction参数实现Popup的镜像布局效果。

```ts
// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupPage {
  @State currentDirection: Direction = Direction.Rtl;

  build() {
    Column() {
      // popup 自定义高级组件
      Popup({
        // PopupIconOptions类型设置图标内容
        direction: this.currentDirection,
        icon: {
          // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
          image: $r('app.media.icon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16,
        } as PopupIconOptions,
        // PopupTextOptions 类型设置文字内容
        title: {
          text: 'This is a popup with PopupOptions',
          fontSize: 20,
          fontColor: Color.Black,
          fontWeight: FontWeight.Normal,

        } as PopupTextOptions,
        // PopupTextOptions 类型设置文字内容
        message: {
          text: 'This is the message',
          fontSize: 15,
          fontColor: Color.Black,
        } as PopupTextOptions,
        showClose: true,
        onClose: () => {
          console.info('close Button click');
        },
        // PopupButtonOptions 类型设置按钮内容
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,

        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black,
          },] as [PopupButtonOptions?, PopupButtonOptions?],
      })

    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/K2GDhI18To-u_yxrmY5FWg/zh-cn_image_0000002712406528.png)

### 示例3（设置自定义宽度）

该示例通过配置maxWidth实现Popup的自定义宽度效果。

```ts
// xxx.ets
import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

@Entry
@Component
struct PopupPage {

  build() {
    Row() {
      // popup 自定义高级组件
      Popup({
        // 设置自定义宽度
        maxWidth: '50%',
        // PopupIconOptions类型设置图标内容
        icon: {
          // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
          image: $r('app.media.startIcon'),
          width: 32,
          height: 32,
          fillColor: Color.White,
          borderRadius: 16,
        } as PopupIconOptions,
        // PopupTextOptions 类型设置文字内容
        message: {
          text: 'This is the message,This is the message,This is the message,This is the message',
          fontSize: 15,
          fontColor: Color.Black
        } as PopupTextOptions,
        showClose: false,
        onClose: () => {
          console.info('close Button click');
        },
        // PopupButtonOptions 类型设置按钮内容
        buttons: [{
          text: 'confirm',
          action: () => {
            console.info('confirm button click');
          },
          fontSize: 15,
          fontColor: Color.Black,
        },
          {
            text: 'cancel',
            action: () => {
              console.info('cancel button click');
            },
            fontSize: 15,
            fontColor: Color.Black
          },] as [PopupButtonOptions?, PopupButtonOptions?]
      })
    }
    .width(400)
    .height(200)
    .borderWidth(2)
    .justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/QOj4LNr9RdOYk0G1M5ByZg/zh-cn_image_0000002742125475.png)
