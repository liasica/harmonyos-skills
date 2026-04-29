---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol
title: 图标小符号 (SymbolGlyph/SymbolSpan)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 图标小符号 (SymbolGlyph/SymbolSpan)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7464c35c4ba39168320ca152e4ec78d55eb8543d4db69c2c68443726bcff41c
---

SymbolGlyph是图标小符号组件，便于使用精美的图标，如渲染多色图标和使用动效图标。SymbolSpan作为Text组件的子组件，可在文本中穿插显示图标小符号。具体用法请参考[SymbolGlyph](../harmonyos-references/ts-basic-components-symbolglyph.md)和[SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)组件的API文档。

## 创建图标

SymbolGlyph通过$r引用Resource资源来创建，目前仅支持系统预置的Symbol资源名。

相关资源可参考[系统图标](../design-guides/system-icons-0000001929854962.md)。

```
1. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
2. .fontSize(96)
3. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
4. .fontColor([Color.Black, Color.Green, Color.White])
```

[CreatSymbolGlyph.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/CreatSymbolGlyph.ets#L25-L30)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/v7BgfyP8Ta6tGcOIrW1Ohw/zh-cn_image_0000002589324193.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=FE7B079AE79B2B6E39336124332BB29D0837CCE60732D1682C63D74C872B9EF5)

## 添加到文本中

[SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md)可作为[Text](../harmonyos-references/ts-basic-components-text.md)的子组件用于显示图标小符号。可以在一个Text组件内添加多个SymbolSpan，从而展示一串连续的图标。

* 创建SymbolSpan。

  SymbolSpan组件需嵌入在Text组件中才能显示，单独使用不会呈现任何内容。

  ```
  1. Text() {
  2. SymbolSpan($r('sys.symbol.ohos_trash'))
  3. .fontWeight(FontWeight.Normal)
  4. .fontSize(96)
  5. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L30-L36)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/ilFkIHbaSyS7mic7acPZUQ/zh-cn_image_0000002589244133.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=FFB3DF226FB77CE11878F3870AD2DF32782B39FB2CBF6843267CFFB172442C08)
* 通过[fontSize](../harmonyos-references/ts-basic-components-symbolspan.md#fontsize)属性设置SymbolSpan的大小。

  ```
  1. Row() {
  2. Column() {
  3. Text('48')
  4. Text() {
  5. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  6. .fontSize(48)
  7. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  8. .fontColor([Color.Black, Color.Green, Color.White])
  9. }
  10. }

  12. Column() {
  13. Text('72')
  14. Text() {
  15. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  16. .fontSize(72)
  17. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  18. .fontColor([Color.Black, Color.Green, Color.White])
  19. }
  20. }

  22. Column() {
  23. Text('96')
  24. Text() {
  25. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  26. .fontSize(96)
  27. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  28. .fontColor([Color.Black, Color.Green, Color.White])
  29. }
  30. }
  31. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L42-L74)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/1qTbyIKcQeuk-89gp5GxeQ/zh-cn_image_0000002558764326.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=F8ACB911ABDDF82DB87D9E815721AED98C67AD3615E9735B0F0A9F0F0D12EAA5)
* 通过[fontWeight](../harmonyos-references/ts-basic-components-symbolspan.md#fontweight)属性设置SymbolSpan组件的粗细。

  ```
  1. Row() {
  2. Column() {
  3. Text('Light')
  4. Text() {
  5. SymbolSpan($r('sys.symbol.ohos_trash'))
  6. .fontWeight(FontWeight.Lighter)
  7. .fontSize(96)
  8. }
  9. }

  11. Column() {
  12. Text('Normal')
  13. Text() {
  14. SymbolSpan($r('sys.symbol.ohos_trash'))
  15. .fontWeight(FontWeight.Normal)
  16. .fontSize(96)
  17. }
  18. }

  20. Column() {
  21. Text('Bold')
  22. Text() {
  23. SymbolSpan($r('sys.symbol.ohos_trash'))
  24. .fontWeight(FontWeight.Bold)
  25. .fontSize(96)
  26. }
  27. }
  28. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L80-L109)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_1psRd7cT8m2_1MxhQV5NQ/zh-cn_image_0000002558604670.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=F23813DE6423558B808673CC460575EBE4AF1439F8D67F199FB04356E65FA605)
* 通过[fontColor](../harmonyos-references/ts-basic-components-symbolspan.md#fontcolor)属性设置SymbolSpan的颜色。

  ```
  1. Row() {
  2. Column() {
  3. Text('Black')
  4. Text() {
  5. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  6. .fontSize(96)
  7. .fontColor([Color.Black])
  8. }
  9. }

  11. Column() {
  12. Text('Green')
  13. Text() {
  14. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  15. .fontSize(96)
  16. .fontColor([Color.Green])
  17. }
  18. }

  20. Column() {
  21. Text('Pink')
  22. Text() {
  23. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  24. .fontSize(96)
  25. .fontColor([Color.Pink])
  26. }
  27. }
  28. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L115-L144)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/crd0ZfCSQRm5eJGUsWywvg/zh-cn_image_0000002589324195.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=BFC70CCA5BFAED5D2CC9DC5A5D678784C74326CFFC3BE3637D7846A2B5674885)
* 通过[renderingStrategy](../harmonyos-references/ts-basic-components-symbolspan.md#renderingstrategy)属性设置SymbolSpan的渲染策略。

  ```
  1. Row() {
  2. Column() {
  3. // 请将$r('app.string.single_color')替换为实际资源文件，在本示例中该资源文件的value值为"单色"
  4. Text($r('app.string.single_color'));
  5. Text() {
  6. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  7. .fontSize(96)
  8. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
  9. .fontColor([Color.Black, Color.Green, Color.White])
  10. }
  11. }

  13. Column() {
  14. // 请将$r('app.string.multi_color')替换为实际资源文件，在本示例中该资源文件的value值为"多色"
  15. Text($r('app.string.multi_color'));
  16. Text() {
  17. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  18. .fontSize(96)
  19. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
  20. .fontColor([Color.Black, Color.Green, Color.White])
  21. }
  22. }

  24. Column() {
  25. // 请将$r('app.string.hierarchical')替换为实际资源文件，在本示例中该资源文件的value值为"分层"
  26. Text($r('app.string.hierarchical'));
  27. Text() {
  28. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
  29. .fontSize(96)
  30. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
  31. .fontColor([Color.Black, Color.Green, Color.White])
  32. }
  33. }
  34. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L150-L185)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/1T0mPZjLRI-uAmcQlq1jwQ/zh-cn_image_0000002589244135.png?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=3F363DBFC486908BC4726F40DA75C403313A8DAAA07B33BD9E57A8AE2FAE04E6)
* 通过[effectStrategy](../harmonyos-references/ts-basic-components-symbolspan.md#effectstrategy)属性设置SymbolSpan的动效策略。

  ```
  1. Row() {
  2. Column() {
  3. // 请将$r('app.string.no_action')替换为实际资源文件，在本示例中该资源文件的value值为"无动效"
  4. Text($r('app.string.no_action'));
  5. Text() {
  6. SymbolSpan($r('sys.symbol.ohos_wifi'))
  7. .fontSize(96)
  8. .effectStrategy(SymbolEffectStrategy.NONE)
  9. }
  10. }

  12. Column() {
  13. // 请将$r('app.string.overall_scaling_animation_effect')替换为实际资源文件，在本示例中该资源文件的value值为"整体缩放动效"
  14. Text($r('app.string.overall_scaling_animation_effect'));
  15. Text() {
  16. SymbolSpan($r('sys.symbol.ohos_wifi'))
  17. .fontSize(96)
  18. .effectStrategy(SymbolEffectStrategy.SCALE)
  19. }
  20. }

  22. Column() {
  23. // 请将$r('app.string.hierarchical_animation')替换为实际资源文件，在本示例中该资源文件的value值为"层级动效"
  24. Text($r('app.string.hierarchical_animation'));
  25. Text() {
  26. SymbolSpan($r('sys.symbol.ohos_wifi'))
  27. .fontSize(96)
  28. .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
  29. }
  30. }
  31. }
  ```

  [SymbolAddToText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddToText.ets#L192-L224)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/CBzkWVvnQdCfEIhLEEc7cw/zh-cn_image_0000002558764328.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=42ED397958246DDF13DAEBF6B9466F1E19CEE849F38DEC335E95E68665160E28)
* SymbolSpan不支持通用事件。

## 自定义图标动效

相较于effectStrategy属性在启动时即触发动效，可以通过以下两种方式来控制动效的播放状态，以及选择更多样化的动效策略。

关于effectStrategy属性与symbolEffect属性的多种动态属性使用及生效原则，详情请参阅[SymbolGlyph.symbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#symboleffect12-1)属性的说明。

* 通过设置SymbolEffect属性，可以同时配置SymbolGlyph的动效策略和播放状态。

  ```
  1. @State isActive: boolean = true;
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L22-L24)

  ```
  1. Column() {
  2. // 请将$r('app.string.variable_color_animation')替换为实际资源文件，在本示例中该资源文件的value值为"可变颜色动效"
  3. Text($r('app.string.variable_color_animation'));
  4. SymbolGlyph($r('sys.symbol.ohos_wifi'))
  5. .fontSize(96)
  6. .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
  7. // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
  8. // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
  9. Button(this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
  10. this.isActive = !this.isActive;
  11. })
  12. }
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L42-L55)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/2WCnWj6JSh2F8EhEzRhjEw/zh-cn_image_0000002558604672.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=369DE0C41E95B4FEE054C7E55C4ACCC2FC4B47FB127B7DCC7FA6C76AFD7D0B47)
* 通过设置SymbolEffect属性，可以同时指定SymbolGlyph的动画效果策略及其播放触发条件。

  ```
  1. @State triggerValueReplace: number = 0;
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L25-L29)

  ```
  1. Column() {
  2. // 请将$r('app.string.bounce_animation')替换为实际资源文件，在本示例中该资源文件的value值为"弹跳动效"
  3. Text($r('app.string.bounce_animation'));
  4. SymbolGlyph($r('sys.symbol.ellipsis_message_1'))
  5. .fontSize(96)
  6. .fontColor([Color.Gray])
  7. .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE, EffectDirection.UP),
  8. this.triggerValueReplace)
  9. Button('trigger').onClick(() => {
  10. this.triggerValueReplace = this.triggerValueReplace + 1;
  11. })
  12. }
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L60-L73)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/w51aR2u9R5Og4kwuCs7R-Q/zh-cn_image_0000002589324197.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=F6669B13BD893B7EA3E64B55FF63EDA59CF5AE5D53F35454AF87AD31820A92CD)
* 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#replacesymboleffect12)，设置[ReplaceEffectType](../harmonyos-references/ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明)为ReplaceEffectType.SLASH\_OVERLAY，可以指定SymbolGlyph的禁用动画效果及其播放触发条件。

  ```
  1. @State triggerValueReplace: number = 0;
  2. replaceFlag: boolean = true;
  3. @State renderMode: number = 1;
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L26-L33)

  ```
  1. Column() {
  2. // 请将$r('app.string.disable_animation')替换为实际资源文件，在本示例中该资源文件的value值为"禁用动效"
  3. Text($r('app.string.disable_animation'));
  4. SymbolGlyph(this.replaceFlag ? $r('sys.symbol.eye_slash') : $r('sys.symbol.eye'))
  5. .fontSize(96)
  6. .renderingStrategy(this.renderMode)
  7. .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH_OVERLAY),
  8. this.triggerValueReplace)
  9. Button('trigger').onClick(() => {
  10. this.replaceFlag = !this.replaceFlag;
  11. this.triggerValueReplace = this.triggerValueReplace + 1;
  12. })
  13. }
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L79-L93)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/augs3ikLRCKAcoIsm7qasA/zh-cn_image_0000002589244137.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=C3C9F2076FE268CF309207AE8555EBAACF5FDCDB0CB22539F087DD2545A51F7B)
* 从API version 20开始，支持通过设置SymbolEffect属性为[ReplaceSymbolEffect](../harmonyos-references/ts-basic-components-symbolglyph.md#replacesymboleffect12)，设置[ReplaceEffectType](../harmonyos-references/ts-basic-components-symbolglyph.md#replaceeffecttype20枚举说明)为ReplaceEffectType.CROSS\_FADE，可以指定SymbolGlyph的快速替换动画效果及其播放触发条件。

  ```
  1. @State triggerValueReplace: number = 0;
  2. replaceFlag: boolean = true;
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L27-L31)

  ```
  1. Column() {
  2. // 请将$r('app.string.quick_replacement_animation')替换为实际资源文件，在本示例中该资源文件的value值为"快速替换动效"
  3. Text($r('app.string.quick_replacement_animation'));
  4. SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark_circle') : $r('sys.symbol.repeat_1'))
  5. .fontSize(96)
  6. .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS_FADE),
  7. this.triggerValueReplace)
  8. Button('trigger').onClick(() => {
  9. this.replaceFlag = !this.replaceFlag;
  10. this.triggerValueReplace = this.triggerValueReplace + 1;
  11. })
  12. }
  ```

  [SymbolCustomIconAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolCustomIconAnimation.ets#L99-L112)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/DLXfihIlQp2HSd2XUk-ESQ/zh-cn_image_0000002558764330.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=8A857AFDBE6F326F1FA8E413DA764CAECA2E218B7276444F6764470B656A664A)

## 设置阴影和渐变色

* 从API version 20开始，支持通过[symbolShadow](../harmonyos-references/ts-basic-components-symbolglyph.md#symbolshadow20)接口实现了symbolGlyph组件显示阴影效果。

  ```
  1. @State isActive: boolean = true;

  3. options: ShadowOptions = {
  4. radius: 10.0,
  5. color: Color.Blue,
  6. offsetX: 10,
  7. offsetY: 10,
  8. };
  ```

  [SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L22-L31)

  ```
  1. Column() {
  2. // 请将$r('app.string.shadow_ability')替换为实际资源文件，在本示例中该资源文件的value值为"阴影能力"
  3. Text($r('app.string.shadow_ability'));
  4. SymbolGlyph($r('sys.symbol.ohos_wifi'))
  5. .fontSize(96)
  6. .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), !this.isActive)
  7. .symbolShadow(this.options)
  8. // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
  9. // 请将$r('app.string.on')替换为实际资源文件，在本示例中该资源文件的value值为"播放"
  10. Button(!this.isActive ? $r('app.string.off') : $r('app.string.on')).onClick(() => {
  11. this.isActive = !this.isActive;
  12. })
  13. }
  ```

  [SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L47-L61)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Q6qgafXuQUySaYA0VJ3Riw/zh-cn_image_0000002558604674.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=35DFC8E6FB4B2A59FBA226974E167C06EB0564536E16E5C4A782B7440690884C)
* 从API version 20开始，支持通过[shaderStyle](../harmonyos-references/ts-basic-components-symbolglyph.md#shaderstyle20)接口实现了symbolGlyph组件显示渐变色效果。

  ```
  1. radialGradientOptions: RadialGradientOptions = {
  2. center: ['50%', '50%'],
  3. radius: '20%',
  4. colors: [[Color.Red, 0.0], [Color.Blue, 0.3], [Color.Green, 0.5]],
  5. repeating: true,
  6. };
  ```

  [SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L33-L40)

  ```
  1. Column() {
  2. // 请将$r('app.string.radial_gradient')替换为实际资源文件，在本示例中该资源文件的value值为"径向渐变"
  3. Text($r('app.string.radial_gradient'))
  4. .fontSize(18)
  5. .fontColor(0xCCCCCC)
  6. .textAlign(TextAlign.Center)
  7. SymbolGlyph($r('sys.symbol.ohos_folder_badge_plus'))
  8. .fontSize(96)
  9. .shaderStyle([new RadialGradientStyle(this.radialGradientOptions)])
  10. }
  ```

  [SymbolShadowAndColor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolShadowAndColor.ets#L64-L75)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Ip2DKPDqR1W3sPoGGt5dFQ/zh-cn_image_0000002589324199.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=E3C9752FDD84110B3D9828BFCDBAB46DDC7B343D22529BF169CC004F792739D4)

## 添加事件

SymbolGlyph组件可以添加通用事件，例如绑定[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)、[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)等事件来响应操作。

```
1. @State wifiColor: ResourceColor = Color.Black;
```

[SymbolAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddEvent.ets#L21-L23)

```
1. SymbolGlyph($r('sys.symbol.ohos_wifi'))
2. .fontSize(96)
3. .fontColor([this.wifiColor])
4. .onClick(() => {
5. this.wifiColor = Color.Gray;
6. })
```

[SymbolAddEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolAddEvent.ets#L29-L36)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DTywtjjNRUCA7vNeALvvDQ/zh-cn_image_0000002589244139.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=D2183BA5801020400DCC0237FDF8956675293AAD632F6CEB926890BCCA251519)

## 场景示例

该示例通过symbolEffect、fontSize、fontColor属性展示了播放列表的效果。

```
1. // resourceGetString封装工具，从资源中获取字符串
2. import resourceGetString from '../../common/resource';

4. @Entry
5. @Component
6. struct SymbolMusicDemo {
7. @State triggerValueReplace: number = 0;
8. @State symbolSources: Resource[] =
9. [$r('sys.symbol.repeat'), $r('sys.symbol.repeat_1'), $r('sys.symbol.arrow_left_arrow_right')];
10. @State symbolSourcesIndex: number = 0;
11. @State symbolText: string[] = [
12. // 请将$r('app.string.play_in_order')替换为实际资源文件，在本示例中该资源文件的value值为"顺序播放"
13. this.getUIContext()
14. .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_order').id),
15. // 请将$r('app.string.play_in_single_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"单曲循环"
16. this.getUIContext()
17. .getHostContext()!.resourceManager.getStringSync($r('app.string.play_in_single_repeat').id),
18. // 请将$r('app.string.shuffle_play')替换为实际资源文件，在本示例中该资源文件的value值为"随机播放"
19. this.getUIContext()
20. .getHostContext()!.resourceManager.getStringSync($r('app.string.shuffle_play').id),
21. ];
22. @State symbolTextIndex: number = 0;
23. @State fontColorValue: ResourceColor = Color.Grey;
24. @State fontColorValue1: ResourceColor = '#E8E8E8';

26. build() {
27. Column({ space: 10 }) {
28. Row() {
29. Text() {
30. // 请将$r('app.string.current_playlist')替换为实际资源文件，在本示例中该资源文件的value值为"当前播放列表"
31. Span(this.getUIContext()
32. .getHostContext()!.resourceManager.getStringSync($r('app.string.current_playlist').id))
33. .fontSize(20)
34. .fontWeight(FontWeight.Bolder)
35. Span('（101）')
36. }
37. }

39. Row() {
40. Row({ space: 5 }) {
41. SymbolGlyph(this.symbolSources[this.symbolSourcesIndex])
42. .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
43. .fontSize(20)
44. .fontColor([this.fontColorValue])
45. Text(this.symbolText[this.symbolTextIndex])
46. .fontColor(this.fontColorValue)
47. }
48. .onClick(() => {
49. this.symbolTextIndex++;
50. this.symbolSourcesIndex++;
51. this.triggerValueReplace++;
52. if (this.symbolSourcesIndex > (this.symbolSources.length - 1)) {
53. this.symbolSourcesIndex = 0;
54. this.triggerValueReplace = 0;
55. }
56. if (this.symbolTextIndex > (this.symbolText.length - 1)) {
57. this.symbolTextIndex = 0;
58. }
59. })
60. .width('75%')

62. Row({ space: 5 }) {
63. Text() {
64. SymbolSpan($r('sys.symbol.arrow_down_circle_badge_vip_circle_filled'))
65. .fontColor([this.fontColorValue])
66. .fontSize(20)
67. }

69. Text() {
70. SymbolSpan($r('sys.symbol.heart_badge_plus'))
71. .fontColor([this.fontColorValue])
72. .fontSize(20)
73. }

75. Text() {
76. SymbolSpan($r('sys.symbol.ohos_trash'))
77. .fontColor([this.fontColorValue])
78. .fontSize(20)
79. }
80. }
81. .width('25%')
82. }

84. Divider().width(5).color(this.fontColorValue1).width('98%')
85. Row() {
86. Row() {
87. // 请将$r('app.string.song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲一"
88. Text($r('app.string.song'))
89. }.width('82%')

91. Row({ space: 5 }) {
92. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
93. .fontColor([this.fontColorValue])
94. .fontSize(20)
95. SymbolGlyph($r('sys.symbol.trash'))
96. .fontColor([this.fontColorValue])
97. .fontSize(20)
98. }
99. }

101. Divider().width(5).color(this.fontColorValue1).width('98%')
102. Row() {
103. Row() {
104. // 请将$r('app.string.song_again')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲二"
105. Text($r('app.string.song_again'))
106. }.width('82%')

108. Row({ space: 5 }) {
109. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
110. .fontColor([this.fontColorValue])
111. .fontSize(20)
112. SymbolGlyph($r('sys.symbol.trash'))
113. .fontColor([this.fontColorValue])
114. .fontSize(20)
115. }
116. }

118. Divider().width(5).color(this.fontColorValue1).width('98%')
119. Row() {
120. Row() {
121. // 请将$r('app.string.again_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲三"
122. Text($r('app.string.again_song'))
123. }.width('82%')

125. Row({ space: 5 }) {
126. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
127. .fontColor([this.fontColorValue])
128. .fontSize(20)
129. SymbolGlyph($r('sys.symbol.trash'))
130. .fontColor([this.fontColorValue])
131. .fontSize(20)
132. }
133. }

135. Divider().width(5).color(this.fontColorValue1).width('98%')
136. Row() {
137. Row() {
138. // 请将$r('app.string.song_repeat')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲四"
139. Text($r('app.string.song_repeat'))
140. }.width('82%')

142. Row({ space: 5 }) {
143. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
144. .fontColor([this.fontColorValue])
145. .fontSize(20)
146. SymbolGlyph($r('sys.symbol.trash'))
147. .fontColor([this.fontColorValue])
148. .fontSize(20)
149. }
150. }

152. Divider().width(5).color(this.fontColorValue1).width('98%')
153. Row() {
154. Row() {
155. // 请将$r('app.string.repeat_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲五"
156. Text($r('app.string.repeat_song'))
157. }.width('82%')

159. Row({ space: 5 }) {
160. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
161. .fontColor([this.fontColorValue])
162. .fontSize(20)
163. SymbolGlyph($r('sys.symbol.trash'))
164. .fontColor([this.fontColorValue])
165. .fontSize(20)
166. }
167. }

169. Divider().width(5).color(this.fontColorValue1).width('98%')
170. Row() {
171. Row() {
172. // 请将$r('app.string.song_play')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲六"
173. Text($r('app.string.song_play'))
174. }.width('82%')

176. Row({ space: 5 }) {
177. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
178. .fontColor([this.fontColorValue])
179. .fontSize(20)
180. SymbolGlyph($r('sys.symbol.trash'))
181. .fontColor([this.fontColorValue])
182. .fontSize(20)
183. }
184. }

186. Divider().width(5).color(this.fontColorValue1).width('98%')
187. Row() {
188. Row() {
189. // 请将$r('app.string.play_song')替换为实际资源文件，在本示例中该资源文件的value值为"歌曲七"
190. Text($r('app.string.play_song'))
191. }.width('82%')

193. Row({ space: 5 }) {
194. SymbolGlyph($r('sys.symbol.play_arrow_triangle_2_circlepath'))
195. .fontColor([this.fontColorValue])
196. .fontSize(20)
197. SymbolGlyph($r('sys.symbol.trash'))
198. .fontColor([this.fontColorValue])
199. .fontSize(20)
200. }
201. }

203. Divider().width(5).color(this.fontColorValue1).width('98%')
204. Column() {
205. // 请将$r('app.string.off')替换为实际资源文件，在本示例中该资源文件的value值为"关闭"
206. Text($r('app.string.off'))
207. }
208. .alignItems(HorizontalAlign.Center)
209. .width('98%')
210. }
211. .alignItems(HorizontalAlign.Start)
212. .width('100%')
213. .height(400)
214. .padding({
215. left: 10,
216. top: 10
217. })
218. }
219. }
```

[SymbolSceneExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/TextComponent/entry/src/main/ets/pages/symbol/SymbolSceneExample.ets#L18-L234)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/eY7kOd65RPim9YCeQANjOQ/zh-cn_image_0000002558764332.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052744Z&HW-CC-Expire=86400&HW-CC-Sign=76F7538FE8F1D8D57990A9F0EA23EF678C860951523FD658583F166DD629ABE5)
