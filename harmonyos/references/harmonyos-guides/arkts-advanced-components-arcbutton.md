---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton
title: 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5a9754276d9f4f9d872d7d8dbf32997793ff71978f63c62c3c83292cb9b7b3df
---

从API version 18开始支持ArcButton。ArcButton是弧形按钮组件，推荐用于圆形屏幕。为用户提供强调、普通、警告等样式按钮。具体用法请参考[ArcButton](../harmonyos-references/ohos-arkui-advanced-arcbutton.md)。

## 创建按钮

ArcButton通过调用以下接口来创建。

```typescript
ArcButton({
  options: new ArcButtonOptions({
    label: 'OK',
    position: ArcButtonPosition.TOP_EDGE,
    styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  // ···
  })
})
```

其中，[label](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮文字，[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮位置，[styleMode](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/TsECgBjLTtS_TNKe29ExUQ/zh-cn_image_0000002821756649.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=4702B7CA5A081AAC6D4BF7B79C363CE0FDB5C73ACB0184E7EA4AC16A02320792)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮位置。

* 下弧形按钮（默认类型）。

  通过将[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM\_EDGE，可以将按钮设置为下弧形按钮。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
      position: ArcButtonPosition.BOTTOM_EDGE,
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
    // ···
    })

  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/8EwKSIO0SLKPc2_-7gkcfA/zh-cn_image_0000002793036712.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=ABBFEA7611864B1A277B52EE086F068E21C7EF207DB5C7351A28079FAAE48E35)
* 上弧形按钮。

  通过将[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.TOP\_EDGE，可以将按钮设置为上弧形按钮。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
      position: ArcButtonPosition.TOP_EDGE,
      styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
    // ···
    })
  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/sUGo4XqGTaSDcqmiZiFnBA/zh-cn_image_0000002792876744.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B52FD725E1B82D69EE8552B8C76D3195D482139213A98D358D1FA650FD811A1)

## 自定义样式

* 设置背景色。

  使用[backgroundColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的背景色。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
      styleMode: ArcButtonStyleMode.CUSTOM,
      backgroundColor: ColorMetrics.resourceColor('#707070')
    })
  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ulEnzaA5SNetE26R5KkC7w/zh-cn_image_0000002821836649.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC966CED21C9E2E587E999C6214712ACE79D75A1BBDC5146B29ECB7412328AB)
* 设置文本颜色。

  使用[fontColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的文本颜色。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
      styleMode: ArcButtonStyleMode.CUSTOM,
      backgroundColor: ColorMetrics.resourceColor('#E84026'),
      fontColor: ColorMetrics.resourceColor('#707070')
    })
  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/QR6HYubvRASKN19lgoqpdQ/zh-cn_image_0000002821756651.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=757D23B225890882639F5232DAA0F986F914C71020595A3D9C0A965FEA740651)
* 设置阴影颜色。

  使用[shadowEnabled](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的阴影颜色。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
      shadowEnabled: true,
      shadowColor: ColorMetrics.resourceColor('#ffec1022')
    })
  })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/F5qCEjDpQM2CJh8HBmOTNw/zh-cn_image_0000002793036714.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=146ABDEFEC47347BBD9EF13F112629FDA0F12E22D1D8B46D7961D605E681839A)

## 添加事件

* 绑定onClick事件来响应点击操作后的自定义行为。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
    // ···
      onClick: () => {
        hilog.info(DOMAIN, TAG, 'ArcButton onClick');
      },
    })
  })
  ```
* 绑定onTouch事件来响应触摸操作后的自定义行为。

  ```typescript
  ArcButton({
    options: new ArcButtonOptions({
      label: 'OK',
    // ···
      onTouch: (event: TouchEvent) => {
        hilog.info(DOMAIN, TAG, 'ArcButton onTouch');
      }
    })

  })
  ```

## 场景示例

在亮度设置界面，进度条显示当前亮度为30%。点击重置后，亮度值将被重置为默认的50%。

运行该示例推荐在Wearable设备上以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，在src/main目录下的工程配置文件[module.json5](module-configuration-file.md)中[deviceTypes标签](module-configuration-file.md#devicetypes标签)内配置wearable。

```json5
"module": {
  // ...
  "deviceTypes": [
    "default",
    "wearable"
  ],
  // ...
}
```

```typescript
import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

const BRIGHT_NESS_VALUE = 30;
const BRIGHT_NESS_VALUE_DEFAULT = 50;

@Entry
@ComponentV2
struct BrightnessPage {
  @Local brightnessValue: number = BRIGHT_NESS_VALUE;
  private defaultBrightnessValue: number = BRIGHT_NESS_VALUE_DEFAULT;

  build() {
    RelativeContainer() {
      // 请将$r('app.string.Brightness')替换为实际资源文件，在本示例中该资源文件的value值为"设置亮度"
      Text($r('app.string.Brightness'))
        .fontColor(Color.White)
        .id('id_brightness_set_text')
        .fontSize(24)
        .margin({ top: 16 })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

      Text(`${this.brightnessValue} %`)
        .fontColor(Color.White)
        .id('id_brightness_min_text')
        .margin({ left: 16 })
        .alignRules({
          start: { anchor: '__container__', align: HorizontalAlign.Start },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })

      Slider({
        value: this.brightnessValue,
        min: 0,
        max: 100,
        style: SliderStyle.InSet
      })
        .blockColor('#191970')
        .trackColor('#ADD8E6')
        .selectedColor('#4169E1')
        .width(150)
        .id('id_brightness_slider')
        .margin({ left: 16, right: 16 })
        .onChange((value: number, mode: SliderChangeMode) => {
          this.brightnessValue = value;
        })
        .alignRules({
          center: { anchor: 'id_brightness_min_text', align: VerticalAlign.Center },
          start: { anchor: 'id_brightness_min_text', align: HorizontalAlign.End }
        })

      ArcButton({
        options: new ArcButtonOptions({
          // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
          label: $r('app.string.Reset'),
          styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
          fontSize: new LengthMetrics(19, LengthUnit.FP),
          onClick: () => {
            this.brightnessValue = this.defaultBrightnessValue;
          }
        })
      })
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        })
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/GZKfdFSVSTaFStuSQ1Q2Rg/zh-cn_image_0000002792876746.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=A429843406EE5A80F078FEC48E892DBAAF047255DD8C1411A9668EE6312BF654)
