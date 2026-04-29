---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton
title: 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9480f1177061a4309c0b0068f4c2330fe36bdabfa3fc382b2a22337d47eb5fbf
---

从API version 18开始支持ArcButton。ArcButton是弧形按钮组件，推荐用于圆形屏幕。为用户提供强调、普通、警告等样式按钮。具体用法请参考[ArcButton](../harmonyos-references/ohos-arkui-advanced-arcbutton.md)。

## 创建按钮

ArcButton通过调用以下接口来创建。

```
1. ArcButton({
2. options: new ArcButtonOptions({
3. label: 'OK',
4. position: ArcButtonPosition.TOP_EDGE,
5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
6. // ···
7. })
8. })
```

[ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L27-L43)

其中，[label](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮文字，[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型，[styleMode](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/ylMU4BRaQ2mbY271hi8npQ/zh-cn_image_0000002589324239.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=0A4D464E234E257BA2E8B730BF9592A252510CAE9F243CD2C312239B45835143)

## 设置按钮类型

ArcButton有上弧形按钮和下弧形按钮两种类型。使用[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)设置按钮类型。

* 下弧形按钮（默认类型）。

  通过将[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.BOTTOM\_EDGE，可以将按钮设置为下弧形按钮。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. position: ArcButtonPosition.BOTTOM_EDGE,
  5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  6. // ···
  7. })

  9. })
  ```

  [ButtonAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignBottom.ets#L27-L45)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/SbcPC6SDTO-M0Iba5uEmGg/zh-cn_image_0000002589244179.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=42222C5FE6994057418176AD9647E2FB12D7DD2871F44000DCD5FCA9A8CF1E48)
* 上弧形按钮。

  通过将[position](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置为ArcButtonPosition.TOP\_EDGE，可以将按钮设置为上弧形按钮。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. position: ArcButtonPosition.TOP_EDGE,
  5. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  6. // ···
  7. })
  8. })
  ```

  [ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L27-L43)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/V92FvVQoRgeVSZ0udYLbTg/zh-cn_image_0000002558764372.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=B63CD1CB2DAE46C85B2D710F2134045EC15247F362C44F4BCDDF532E0C88C06E)

## 自定义样式

* 设置背景色。

  使用[backgroundColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的背景色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. styleMode: ArcButtonStyleMode.CUSTOM,
  5. backgroundColor: ColorMetrics.resourceColor('#707070')
  6. })
  7. })
  ```

  [ButtonBcgColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonBcgColor.ets#L23-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/TB-S5G90R-agjehFMmHgpg/zh-cn_image_0000002558604716.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=C22C4CAAE56813558AD8F01E63A20C2ED59F86280569DA9367B84059DB776A7B)
* 设置文本颜色。

  使用[fontColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的文本颜色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. styleMode: ArcButtonStyleMode.CUSTOM,
  5. backgroundColor: ColorMetrics.resourceColor('#E84026'),
  6. fontColor: ColorMetrics.resourceColor('#707070')
  7. })
  8. })
  ```

  [ButtonFontColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonFontColor.ets#L23-L32)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Fg7mtqiRRke9VdeEkkvCCg/zh-cn_image_0000002589324241.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=BC19BD450CBD7FB3D7ECB5ED42E79EF0C188DFCB0BC7610D3A6FBA48A15A9B01)
* 设置阴影颜色。

  使用[shadowEnabled](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性启用按钮阴影，并通过[shadowColor](../harmonyos-references/ohos-arkui-advanced-arcbutton.md#arcbuttonoptions)属性设置按钮的阴影颜色。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. shadowEnabled: true,
  5. shadowColor: ColorMetrics.resourceColor('#ffec1022')
  6. })
  7. })
  ```

  [ButtonShadow.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonShadow.ets#L23-L31)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/ys93LFacRxu-RSBWc2-E2g/zh-cn_image_0000002589244181.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=14EE3D2DD2883CE86CF8AE28C04D8708500678B6A2EDEEEE507846F9C4F44717)

## 添加事件

* 绑定onClick事件来响应点击操作后的自定义行为。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. // ···
  5. onClick: () => {
  6. hilog.info(DOMAIN, TAG, 'ArcButton onClick');
  7. },
  8. })
  9. })
  ```

  [ButtonAlignTop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignTop.ets#L28-L44)
* 绑定onTouch事件来响应触摸操作后的自定义行为。

  ```
  1. ArcButton({
  2. options: new ArcButtonOptions({
  3. label: 'OK',
  4. // ···
  5. onTouch: (event: TouchEvent) => {
  6. hilog.info(DOMAIN, TAG, 'ArcButton onTouch');
  7. }
  8. })

  10. })
  ```

  [ButtonAlignBottom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonAlignBottom.ets#L28-L44)

## 场景示例

在亮度设置界面，进度条显示当前亮度为30%。点击重置后，亮度值将被重置为默认的50%。

运行该示例推荐在Wearable设备上以获得最佳显示效果，同时支持在其他设备上运行。若要在Wearable设备上运行，在src/main目录下的工程配置文件[module.json5](module-configuration-file.md)中[deviceTypes标签](module-configuration-file.md#devicetypes标签)内配置wearable。

```
1. "module": {
2. // ···
3. "deviceTypes": [
4. "wearable"
5. ],
6. // ···
7. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/module.json5#L17-L70)

```
1. import { LengthMetrics, LengthUnit, ArcButton, ArcButtonOptions, ArcButtonStyleMode } from '@kit.ArkUI';

3. const BRIGHT_NESS_VALUE = 30;
4. const BRIGHT_NESS_VALUE_DEFAULT = 50;

6. @Entry
7. @ComponentV2
8. struct BrightnessPage {
9. @Local brightnessValue: number = BRIGHT_NESS_VALUE;
10. private defaultBrightnessValue: number = BRIGHT_NESS_VALUE_DEFAULT;

12. build() {
13. RelativeContainer() {
14. // 请将$r('app.string.Brightness')替换为实际资源文件，在本示例中该资源文件的value值为"设置亮度"
15. Text($r('app.string.Brightness'))
16. .fontColor(Color.White)
17. .id('id_brightness_set_text')
18. .fontSize(24)
19. .margin({ top: 16 })
20. .alignRules({
21. middle: { anchor: '__container__', align: HorizontalAlign.Center }
22. })

24. Text(`${this.brightnessValue} %`)
25. .fontColor(Color.White)
26. .id('id_brightness_min_text')
27. .margin({ left: 16 })
28. .alignRules({
29. start: { anchor: '__container__', align: HorizontalAlign.Start },
30. center: { anchor: '__container__', align: VerticalAlign.Center }
31. })

33. Slider({
34. value: this.brightnessValue,
35. min: 0,
36. max: 100,
37. style: SliderStyle.InSet
38. })
39. .blockColor('#191970')
40. .trackColor('#ADD8E6')
41. .selectedColor('#4169E1')
42. .width(150)
43. .id('id_brightness_slider')
44. .margin({ left: 16, right: 16 })
45. .onChange((value: number, mode: SliderChangeMode) => {
46. this.brightnessValue = value;
47. })
48. .alignRules({
49. center: { anchor: 'id_brightness_min_text', align: VerticalAlign.Center },
50. start: { anchor: 'id_brightness_min_text', align: HorizontalAlign.End }
51. })

53. ArcButton({
54. options: new ArcButtonOptions({
55. // 请将$r('app.string.Reset')替换为实际资源文件，在本示例中该资源文件的value值为"重置"
56. label: $r('app.string.Reset'),
57. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
58. fontSize: new LengthMetrics(19, LengthUnit.FP),
59. onClick: () => {
60. this.brightnessValue = this.defaultBrightnessValue;
61. }
62. })
63. })
64. .alignRules({
65. middle: { anchor: '__container__', align: HorizontalAlign.Center },
66. bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
67. })
68. }
69. .height('100%')
70. .width('100%')
71. .backgroundColor(Color.Black)
72. }
73. }
```

[ButtonBrightness.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ButtonComponent/entry/src/main/ets/pages/ButtonBrightness.ets#L16-L90)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/f-mvwHToSzS1hgNZ2mQ4uw/zh-cn_image_0000002558764374.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=0FCB0C953070EFA48DABC705B539E28A3811CD8C80951F5F2E081FEACD5D5DE0)
