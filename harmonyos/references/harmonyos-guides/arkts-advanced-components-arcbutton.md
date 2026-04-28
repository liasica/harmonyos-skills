---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton
title: 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 弧形按钮 (ArcButton)(圆形屏幕推荐使用)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:98f15c63bc46c493b737d8afbc09b4b4910d81c2e37b8b2a52da27c91e768cf7
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0vc_0hdPTsOSm43qpfS72g/zh-cn_image_0000002552957880.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=F5E0FC8B1303FEDD3641B5720A4AFD08C4645D85ABD7AFFB4FD9B37FB7CD47EB)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/KvSwgKmIT0ivspigw5MGvA/zh-cn_image_0000002583477881.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=4F0FD391EBB1FE13980B90D29048F29D44B9487A0B159898AC2B030FB0106C5C)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/oeRBCwP5Sp2Qg8Si8VheXQ/zh-cn_image_0000002552798232.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=CC1189C480DED9053D59DA30B42641CFC47172D9422F32B524CC3CF2915E2705)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/McobALPGQPOepE1EtBCuWg/zh-cn_image_0000002583437927.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=5A75A2A92BA5BD936A3D984F54E3726F8D4BA4C846AE20AC6B8F7B94346C2CD4)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/rnvn5s4CQH6geoPqg2he_g/zh-cn_image_0000002552957882.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=97C176F2FC16642069575A3E1A00A121E8FD01A7EA979021F3E932898C52364C)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/iFBNFBeuT4SOOoD7Hz4zoA/zh-cn_image_0000002583477883.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=39F539978100FF8BB57B369D6F5D67D14FB90106AC7B3CD4193D6541036EC031)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/mOco9zIISO-4UMGowXphxA/zh-cn_image_0000002552798234.png?HW-CC-KV=V1&HW-CC-Date=20260427T233939Z&HW-CC-Expire=86400&HW-CC-Sign=B77B8619361007EA6F91A7B5F94F49535285A007F6F299FE02FF523570967272)
