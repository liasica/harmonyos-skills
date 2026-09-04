---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton
title: 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5870a1e88e480e3ca1ed65f4dc9d8ad01b35399f91aaf336db65b0dddbb3dbdc
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

其中，[label](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮文字，[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型，[styleMode](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/Bw1y92phTG-ItycSNFTzOw/zh-cn_image_0000002712243896.png)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型。

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/u1hxKozpQzGkXGt_g0RJdQ/zh-cn_image_0000002742002849.png)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/6NywWxbARvWBHK7rxN5RXw/zh-cn_image_0000002712403862.png)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/b7V3g5SqQ8uA147BkpJA_Q/zh-cn_image_0000002742122811.png)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/EjMjbTx2Tf6lHoYA-9W-fg/zh-cn_image_0000002712243898.png)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/AxQrm4lMReG2uCeRu0b-dQ/zh-cn_image_0000002742002851.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/f_wOuZH7SKCavhqS_A0_Sw/zh-cn_image_0000002712403864.png)
