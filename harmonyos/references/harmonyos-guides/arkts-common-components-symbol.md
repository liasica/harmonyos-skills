---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol
title: 图标小符号 (SymbolGlyph/SymbolSpan)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 图标小符号 (SymbolGlyph/SymbolSpan)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9721ae28431e2b5140e7323de3ede53a1cbad4c36f64809f900a41d714090e63
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/gZnXl7RJRXGEodp49H66aA/zh-cn_image_0000002552957834.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=60915DF4005BFFD595CF311300E0458E7F069790238C3F7B9907B4B9B2BC0831)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/_YIPjMRYRn26Er68uvG6Ng/zh-cn_image_0000002583477835.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=58DE26C914AF5D04B3E5BA5108EBEF68849555837B6A1FE50097D4D792303C47)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/1oqVT6pQSeKOxfsxJshJ6A/zh-cn_image_0000002552798186.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=FCC3DEC9C9F34452380D649341332C375B8B56B1713F9D7BF3E488039B192E18)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/2_m3VxObSvmsKPQfWdcomQ/zh-cn_image_0000002583437881.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=240DC9078E27C718C67DC07B8C8B87C4D690C60C502DF64D786FC325A74B9892)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/o16WwFhoQ0uUS6fOD2NHvA/zh-cn_image_0000002552957836.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=609767D7001ACACE5158B71977053F76BCEF4ED9E9C0AF1D731C130D72B97DE5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/pc8iRv-SQhmCt8goFcy4dg/zh-cn_image_0000002583477837.png?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=D1EF716EFFBB770E34FCDB9BE28FB1CAA2814F60507EEA14645FC87FF10E21C5)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/81Z3CT0URLWYFkxois4bvg/zh-cn_image_0000002552798188.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=79B18AA1DFF27C14F5E03B3E356B75BFB1490709ADDBAD88D0C8B7C57137A99C)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/rdz00N4cQY2vLFwwQAPLMQ/zh-cn_image_0000002583437883.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=2CD45A8ACE305AC089799B111E25963FE44A4BB0D17743B2D1CA043A01E372E4)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FkUzf2iBSAmHNHFcSn2NOw/zh-cn_image_0000002552957838.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=D6A1BADD35967BBE6C4823F64D8AE51C3144ECEE58EE5DE8A8788D60C3B9A2C3)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Ulq7NAwzSkeGxSutBmusSQ/zh-cn_image_0000002583477839.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=BCEE73C7D5AB5EB1899DE76F5F5267B130EEC0A9EA807E5E7891D80E5C4C0533)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/B6uwBexPQ6uNFagMx6_kow/zh-cn_image_0000002552798190.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=47DA8CB410070B5CF686F428E8E6271D24039B1D461555ABA5C02D6B78F3B5BE)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/rAeBa3H5Rcq2GpGBcNCYZw/zh-cn_image_0000002583437885.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=3BEEE9C4C02C681E485258C52B5301DA8D638EAF0CA1270D8A5EF52BF6434876)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ywjMliPRTiqXw2mwpdOYYw/zh-cn_image_0000002552957840.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=A98D4D048D0FF2C93E2F59BEA8BCC54430C0A2E3F56653EBB2D9F78DBEC8BA3D)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QUPfx9w7TnyXvh0qZrGP2g/zh-cn_image_0000002583477841.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=61267211510E3790ADCFD7BFF8CB8EEA2CA46A5F4224E1FD4C67CC5614CBA35B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/NTI5jeQITQSwlyUVbT0BOg/zh-cn_image_0000002552798192.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=D6C750F51296AD626295B51E78B5361BF4B9FD7D9617A57B11FBB0906D26A99C)
