---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode
title: QRCode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > QRCode
category: harmonyos-references
scraped_at: 2026-09-05T06:17:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:60b2d0bdb8f793192cda8907d3dcd968e3be80ab0b2769966ea6d83b2af521f2
---

QRCode组件用于显示单个二维码，支持自定义二维码颜色、背景颜色及内容不透明度，适用于需要展示二维码以供扫描获取字符串信息的场景。

**说明** 

* 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 二维码组件的像素点数量与内容有关，组件尺寸过小可能导致内容无法展示，此时需要适当调整组件尺寸。
* 该组件当前仅支持生成二维码，涉及扫码的业务场景，推荐使用[Scan Kit（统一扫码服务）](../harmonyos-guides/scan-kit-guide.md)。

## 子组件

无

## 接口

QRCode(value: ResourceStr)

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。  从API version 20开始，支持Resource类型。  **说明：**  设置为null时与设置字符串"null"效果一致；设置为undefined时与设置字符串"undefined"效果一致；当传入空字符串时，将生成无效二维码。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

color(value: ResourceColor)

设置二维码颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 二维码颜色。默认值：'#ff000000'，且不跟随系统深浅色模式切换而修改。 |

### backgroundColor

backgroundColor(value: ResourceColor)

设置二维码背景颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 二维码背景颜色。  默认值：Color.White  从API version 11开始，默认值改为'#ffffffff'，且不跟随系统深浅色模式切换而修改。 |

### contentOpacity11+

contentOpacity(value: number | Resource)

设置二维码内容颜色的不透明度。不透明度最小值为0，最大值为1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 二维码内容颜色的不透明度。  默认值：1  取值范围：[0, 1]，超出取值范围按默认值处理。 |

## 事件

通用事件支持[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)和[挂载卸载事件](ts-universal-events-show-hide.md)。

## 示例

### 示例1（设置颜色、背景颜色、不透明度）

该示例展示了QRCode组件的基本使用方法，通过[color](ts-basic-components-qrcode.md#color)属性设置二维码颜色、[backgroundColor](ts-basic-components-qrcode.md#backgroundcolor)属性设置二维码背景颜色、[contentOpacity](ts-basic-components-qrcode.md#contentopacity11)属性设置二维码不透明度。

```ts
// xxx.ets
@Entry
@Component
struct QRCodeExample {
  private value: string = 'hello world';

  build() {
    Column({ space: 5 }) {
      Text('normal').width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140)

      // 设置二维码颜色
      Text('color').width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).color(0xF7CE00).width(140).height(140)

      // 设置二维码背景色
      Text('backgroundColor').width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140).backgroundColor(Color.Orange)

      // 设置二维码不透明度
      Text('contentOpacity').width('90%').fontColor(0xCCCCCC).fontSize(30)
      QRCode(this.value).width(140).height(140).color(Color.Black).contentOpacity(0.1)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/gOIVp5KqSZi--HRhTA-nNQ/zh-cn_image_0000002712406304.png)

### 示例2（设置背景颜色为透明）

该示例通过[backgroundColor](ts-basic-components-qrcode.md#backgroundcolor)属性设置二维码背景颜色为透明，从而实现二维码内容与背景融合。

```ts
// xxx.ets
@Entry
@Component
struct QRCodeExample {
  private value: string = 'hello world';

  build() {
    Column({ space: 5 }) {
      RelativeContainer() {
        // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
        Image($r('app.media.ocean'))
        // 设置二维码背景色为透明
        QRCode(this.value).width(200).height(200).backgroundColor('#00ffffff')
      }.width(200).height(200)
    }.width('100%').margin({ top: 5 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/W0sXKU6ASzixJXM4rClTKg/zh-cn_image_0000002742125253.png)
