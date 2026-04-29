---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning
title: 设置应用内主题换肤
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 主题设置 > 设置应用内主题换肤
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f8389f966556d15ac389e317da41c2f90c97fdd9939f730db9ac02e314fac2d
---

## 概述

对于采用ArkTS开发的应用，提供了应用内组件的主题换肤功能，支持局部的深浅色切换及动态换肤。目前，该功能只支持设置应用内主题换肤，暂不支持在UIAbility或窗口层面进行主题设置，同时也不支持C-API和Node-API。

## 自定义主题色

当应用需要使用换肤功能时，应自定义主题颜色。[CustomTheme](../harmonyos-references/js-apis-arkui-theme.md#customtheme)用于自定义主题色的内容，其属性可选，仅需对需要修改的token字段赋值，其余token将继承系统默认颜色值，可参考[系统默认的token颜色值](theme_skinning.md#系统缺省token色值)。请参照以下示例自定义主题色：

```
1. import { CustomColors, CustomTheme } from '@kit.ArkUI';

3. export class AppColors implements CustomColors {
4. // 自定义主题色
5. public brand: ResourceColor = '#FF75D9';
6. // 使用$r，让一级警示色在深色和浅色模式下，设置为不同的颜色
7. public warning: ResourceColor = $r('sys.color.ohos_id_color_warning');
8. }

10. export class AppTheme implements CustomTheme {
11. public colors: AppColors = new AppColors();
12. }

14. export let gAppTheme: CustomTheme = new AppTheme();
```

[AppTheme.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ThemeSkinning/entry/src/main/ets/pages/Theme1/AppTheme.ets#L16-L31)

## 设置应用内组件自定义主题色

* 若在页面入口处设置应用内组件自定义主题色，需确保在页面build前执行[ThemeControl](../harmonyos-references/js-apis-arkui-theme.md#themecontrol).[setDefaultTheme](../harmonyos-references/js-apis-arkui-theme.md#setdefaulttheme)。

  示例代码中，[onWillApplyTheme](../harmonyos-references/ts-custom-component-lifecycle.md#onwillapplytheme12)回调函数用于使自定义组件获取当前生效的Theme对象。

  ```
  1. // Index.ets
  2. import { Theme, ThemeControl } from '@kit.ArkUI';
  3. import { gAppTheme } from './AppTheme';

  5. //在页面build前执行ThemeControl
  6. ThemeControl.setDefaultTheme(gAppTheme);

  8. @Entry
  9. @Component
  10. struct DisplayPage {
  11. @State menuItemColor: ResourceColor = $r('sys.color.background_primary');

  13. onWillApplyTheme(theme: Theme) {
  14. this.menuItemColor = theme.colors.backgroundPrimary;
  15. }

  17. build() {
  18. Column() {
  19. List({ space: 10 }) {
  20. ListItem() {
  21. Column({ space: '5vp' }) {
  22. Text('Color mode')
  23. .margin({ top: '5vp', left: '14fp' })
  24. .width('100%')
  25. Row() {
  26. Column() {
  27. Text('Light')
  28. .fontSize('16fp')
  29. .textAlign(TextAlign.Start)
  30. .alignSelf(ItemAlign.Center)
  31. Radio({ group: 'light or dark', value: 'light' })
  32. .checked(true)
  33. }
  34. .width('50%')

  36. Column() {
  37. Text('Dark')
  38. .fontSize('16fp')
  39. .textAlign(TextAlign.Start)
  40. .alignSelf(ItemAlign.Center)
  41. Radio({ group: 'light or dark', value: 'dark' })
  42. }
  43. .width('50%')
  44. }
  45. }
  46. .width('100%')
  47. .height('90vp')
  48. .borderRadius('10vp')
  49. .backgroundColor(this.menuItemColor)
  50. }

  52. ListItem() {
  53. Column() {
  54. Text('Brightness')
  55. .width('100%')
  56. .margin({ top: '5vp', left: '14fp' })
  57. Slider({ value: 40, max: 100 })
  58. }
  59. .width('100%')
  60. .height('70vp')
  61. .borderRadius('10vp')
  62. .backgroundColor(this.menuItemColor)
  63. }

  65. ListItem() {
  66. Column() {
  67. Row() {
  68. Column({ space: '5vp' }) {
  69. Text('Touch sensitivity')
  70. .fontSize('16fp')
  71. .textAlign(TextAlign.Start)
  72. .width('100%')
  73. Text('Increase the touch sensitivity of your screen' +
  74. ' for use with screen protectors')
  75. .fontSize('12fp')
  76. .fontColor(Color.Blue)
  77. .textAlign(TextAlign.Start)
  78. .width('100%')
  79. }
  80. .alignSelf(ItemAlign.Center)
  81. .margin({ left: '14fp' })
  82. .width('75%')

  84. Toggle({ type: ToggleType.Switch, isOn: true })
  85. .margin({ right: '14fp' })
  86. .alignSelf(ItemAlign.Center)
  87. }
  88. .width('100%')
  89. .height('80vp')
  90. }
  91. .width('100%')
  92. .borderRadius('10vp')
  93. .backgroundColor(this.menuItemColor)
  94. }
  95. ListItem() {
  96. Column() {
  97. Text('Warning')
  98. .width('100%')
  99. .margin({ top: '5vp', left: '14fp' })
  100. Button('Text')
  101. .type(ButtonType.Capsule)
  102. .role(ButtonRole.ERROR)
  103. .width('40%')
  104. }
  105. .width('100%')
  106. .height('70vp')
  107. .borderRadius('10vp')
  108. .backgroundColor(this.menuItemColor)
  109. }
  110. }
  111. }
  112. .padding('10vp')
  113. .backgroundColor('#dcdcdc')
  114. .width('100%')
  115. .height('100%')
  116. }
  117. }
  ```

  [Theme1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ThemeSkinning/entry/src/main/ets/pages/Theme1/Theme1.ets#L16-L134)
* 若在UIAbility中设置应用内组件自定义主题色，需在onWindowStageCreate()方法的windowStage.[loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)的完成时回调中调用[ThemeControl](../harmonyos-references/js-apis-arkui-theme.md#themecontrol).[setDefaultTheme](../harmonyos-references/js-apis-arkui-theme.md#setdefaulttheme)，设置应用内组件的自定义主题色。

  ```
  1. // EntryAbility.ets
  2. import {AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';
  4. import { window, CustomColors, ThemeControl } from '@kit.ArkUI';

  6. class AppColors implements CustomColors {
  7. fontPrimary = 0xFFD53032;
  8. iconOnPrimary = 0xFFD53032;
  9. iconFourth = 0xFFD53032;
  10. }

  12. const abilityThemeColors = new AppColors();

  14. export default class EntryAbility extends UIAbility {
  15. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
  16. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  17. }

  19. onDestroy() {
  20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  21. }

  23. onWindowStageCreate(windowStage: window.WindowStage) {
  24. // Main window is created, set main page for this ability
  25. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  27. windowStage.loadContent('pages/Index', (err, data) => {
  28. if (err.code) {
  29. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
  30. return;
  31. }
  32. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
  33. // 在onWindowStageCreate()方法中setDefaultTheme
  34. ThemeControl.setDefaultTheme({ colors: abilityThemeColors });
  35. hilog.info(0x0000, 'testTag', '%{public}s', 'ThemeControl.setDefaultTheme done');
  36. });
  37. }
  38. }
  ```

  [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ThemeSkinning/entry/src/main/ets/entryability/EntryAbility.ets#L16-L55)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/f1zpCH2RSGeQH03iMM_ARQ/zh-cn_image_0000002589244335.png?HW-CC-KV=V1&HW-CC-Date=20260429T052825Z&HW-CC-Expire=86400&HW-CC-Sign=0FE80F16108CCBEB1324E0CB78B8C9D694A90187927446A4FA31B8AC99197AF6)

  说明

  + 当setDefaultTheme的参数为undefined时，会清除先前设置的自定义主题，默认token值对应的色值参考[系统缺省token色值](theme_skinning.md#系统缺省token色值)。
  + setDefaultTheme需要在ArkUI初始化后即windowStage.loadContent的完成时回调中使用。

## 设置应用局部页面自定义主题风格

通过设置[WithTheme](../harmonyos-references/ts-container-with-theme.md)，将自定义主题Theme的配色应用于内部组件的默认样式。在WithTheme的作用范围内，组件的配色会根据Theme的配色进行调整。

说明

在自定义节点[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)中使用[WithTheme](../harmonyos-references/ts-container-with-theme.md)，为了确保显示效果正确，需手动传递系统环境变化事件，触发节点的全量更新，详细请参考[BuilderNode系统环境变化更新](../harmonyos-references/js-apis-arkui-buildernode.md#updateconfiguration12)。

如示例所示，使用WithTheme({ theme: this.CustomTheme })可将作用域内组件的配色设置为自定义主题风格。后续可以通过更新this.CustomTheme来更换主题风格。[onWillApplyTheme](../harmonyos-references/ts-custom-component-lifecycle.md#onwillapplytheme12)回调函数用于使自定义组件能够获取当前生效的Theme对象。

```
1. import { CustomColors, CustomTheme, Theme } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';
3. //请将$r('app.color.xxx')替换为实际资源文件
4. class AppColors implements CustomColors {
5. public fontPrimary: ResourceColor = $r('app.color.brand_purple');
6. public backgroundEmphasize: ResourceColor = $r('app.color.brand_purple');
7. }

9. class AppColorsSec implements CustomColors {
10. public fontPrimary: ResourceColor = $r('app.color.brand');
11. public backgroundEmphasize: ResourceColor = $r('app.color.brand');
12. }

14. class AppTheme implements CustomTheme {
15. public colors: AppColors = new AppColors();
16. }

18. class AppThemeSec implements CustomTheme {
19. public colors: AppColors = new AppColorsSec();
20. }

22. @Entry
23. @Component
24. struct DisplayPage1 {
25. @State customTheme: CustomTheme = new AppTheme();
26. // 请将$r('app.string.SetCustomThemeStyle')替换为实际资源文件，在本示例中该资源文件的value值为"设置应用局部页面自定义主题风格"
27. @State message: ResourceStr = $r('app.string.SetCustomThemeStyle');
28. count = 0;

30. build() {
31. WithTheme({ theme: this.customTheme }) {
32. Row(){
33. Column() {
34. Text('WithTheme')
35. .fontSize(30)
36. .margin({bottom: 10})
37. Text(this.message)
38. .margin({bottom: 10})
39. Button('change theme').onClick(() => {
40. this.count++;
41. if (this.count > 1) {
42. this.count = 0;
43. }
44. switch (this.count) {
45. case 0:
46. this.customTheme = new AppTheme();
47. break;
48. case 1:
49. this.customTheme = new AppThemeSec();
50. break;
51. default:
52. break;
53. }
54. })
55. }
56. .width('100%')
57. }
58. .height('100%')
59. .width('100%')
60. }
61. }
62. }
```

[Theme2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ThemeSkinning/entry/src/main/ets/pages/Theme2/Theme2.ets#L16-L79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ZdycFLAzSe-TqNf9HtyJsw/zh-cn_image_0000002558764528.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052825Z&HW-CC-Expire=86400&HW-CC-Sign=5665C58F365101DA6E945AABC7ED6BD26A7FAA327C65D04C813207726D160154)

## 设置应用页面局部深浅色

通过[WithTheme](../harmonyos-references/ts-container-with-theme.md)可以设置三种颜色模式，跟随系统模式，浅色模式和深色模式。

在WithTheme的作用范围内，组件的样式资源值会根据指定的模式，读取对应的深浅色模式系统和应用资源值。这意味着，在WithTheme作用范围内，组件的配色会根据所指定的深浅模式进行调整。

如下面的示例所示，通过WithTheme({ colorMode: ThemeColorMode.DARK })，可以将作用范围内的组件设置为深色模式。

设置局部深浅色时，需要添加dark.json资源文件，深浅色模式才会生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/IaMlgAMzTpeTKu407aj1Jw/zh-cn_image_0000002558604872.png?HW-CC-KV=V1&HW-CC-Date=20260429T052825Z&HW-CC-Expire=86400&HW-CC-Sign=CDA02540716385D019B9D322AC4E5189623EBF183E0F449339C853422D47B012)

dark.json数据示例：

```
1. {
2. "color": [
3. {
4. "name": "start_window_background",
5. "value": "#000000"
6. }
7. ]
8. }
```

```
1. import { ThemeControl } from '@kit.ArkUI';

3. ThemeControl.setDefaultTheme(undefined);

5. @Entry
6. @Component
7. struct DisplayPage3 {
8. @State message: string = 'Hello World';
9. @State colorMode: ThemeColorMode = ThemeColorMode.DARK;

11. build() {
12. WithTheme({ colorMode: this.colorMode }) {
13. Row() {
14. Column() {
15. Text(this.message)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. Button('Switch ColorMode').onClick(() => {
19. if (this.colorMode === ThemeColorMode.LIGHT) {
20. this.colorMode = ThemeColorMode.DARK;
21. } else if (this.colorMode === ThemeColorMode.DARK) {
22. this.colorMode = ThemeColorMode.LIGHT;
23. }
24. })
25. }
26. .width('100%')
27. }
28. .backgroundColor($r('sys.color.background_primary'))
29. .height('100%')
30. // 扩展安全区，实现沉浸式深浅色变更效果
31. .expandSafeArea(
32. [SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START])
33. }
34. }
35. }
```

[Theme3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ThemeSkinning/entry/src/main/ets/pages/Theme3/Theme3.ets#L16-L50)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/5KTQQUczSvOMkTFSmQF7LQ/zh-cn_image_0000002589324397.png?HW-CC-KV=V1&HW-CC-Date=20260429T052825Z&HW-CC-Expire=86400&HW-CC-Sign=9535D4893882C840F249D30F89002A1B188483D9C332DF31065425F3BED27ED7)

## 系统缺省token色值

| Token | 场景类别 | Light | 说明 | Dark | 说明 |
| --- | --- | --- | --- | --- | --- |
| theme.colors.brand | 品牌色 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.warning | 一级警示色 | #ffe84026 |  | #ffd94838 |  |
| theme.colors.alert | 二级警示色 | #ffed6f21 |  | #ffdb6b42 |  |
| theme.colors.confirm | 确认色 | #ff64bb5c |  | #ff5be854 |  |
| theme.colors.fontPrimary | 一级文本 | #e5000000 |  | #e5ffffff |  |
| theme.colors.fontSecondary | 二级文本 | #99000000 |  | #99ffffff |  |
| theme.colors.fontTertiary | 三级文本 | #66000000 |  | #66ffffff |  |
| theme.colors.fontFourth | 四级文本 | #33000000 |  | #33ffffff |  |
| theme.colors.fontEmphasize | 高亮文本 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.fontOnPrimary | 一级文本反色 | #ffffffff |  | #ff000000 |  |
| theme.colors.fontOnSecondary | 二级文本反色 | #99ffffff |  | #99000000 |  |
| theme.colors.fontOnTertiary | 三级文本反色 | #66ffffff |  | #66000000 |  |
| theme.colors.fontOnFourth | 四级文本反色 | #33ffffff |  | #33000000 |  |
| theme.colors.iconPrimary | 一级图标 | #e5000000 |  | #e5ffffff |  |
| theme.colors.iconSecondary | 二级图标 | #99000000 |  | #99ffffff |  |
| theme.colors.iconTertiary | 三级图标 | #66000000 |  | #66ffffff |  |
| theme.colors.iconFourth | 四级图标 | #33000000 |  | #33ffffff |  |
| theme.colors.iconEmphasize | 高亮图标 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.iconSubEmphasize | 高亮辅助图标 | #660a59f7 |  | #66317af7 |  |
| theme.colors.iconOnPrimary | 一级图标反色 | #ffffffff |  | #ff000000 |  |
| theme.colors.iconOnSecondary | 二级图标反色 | #99ffffff |  | #99000000 |  |
| theme.colors.iconOnTertiary | 三级图标反色 | #66ffffff |  | #66000000 |  |
| theme.colors.iconOnFourth | 四级图标反色 | #33ffffff |  | #33000000 |  |
| theme.colors.backgroundPrimary | 一级背景（实色/不透明色） | #ffffffff |  | #ffe5e5e5 |  |
| theme.colors.backgroundSecondary | 二级背景（实色/不透明色） | #fff1f3f5 |  | #ff191a1c |  |
| theme.colors.backgroundTertiary | 三级背景（实色/不透明色） | #ffe5e5ea |  | #ff202224 |  |
| theme.colors.backgroundFourth | 四级背景（实色/不透明色） | #ffd1d1d6 |  | #ff2e3033 |  |
| theme.colors.backgroundEmphasize | 高亮背景（实色/不透明色） | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.compForegroundPrimary | 前背景 | #ff000000 |  | #ffe5e5e5 |  |
| theme.colors.compBackgroundPrimary | 白色背景 | #ffffffff |  | #ffffffff |  |
| theme.colors.compBackgroundPrimaryTran | 白色透明背景 | #ffffffff |  | #33ffffff |  |
| theme.colors.compBackgroundPrimaryContrary | 常亮背景 | #ffffffff |  | #ffe5e5e5 |  |
| theme.colors.compBackgroundGray | 灰色背景 | #fff1f3f5 |  | #ffe5e5ea |  |
| theme.colors.compBackgroundSecondary | 二级背景 | #19000000 |  | #19ffffff |  |
| theme.colors.compBackgroundTertiary | 三级背景 | #0c000000 |  | #0cffffff |  |
| theme.colors.compBackgroundEmphasize | 高亮背景 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.compBackgroundNeutral | 黑色中性高亮背景 | #ff000000 |  | #ffffffff |  |
| theme.colors.compEmphasizeSecondary | 20%高亮背景 | #330a59f7 |  | #33317af7 |  |
| theme.colors.compEmphasizeTertiary | 10%高亮背景 | #190a59f7 |  | #19317af7 |  |
| theme.colors.compDivider | 分割线颜色 | #33000000 |  | #33ffffff |  |
| theme.colors.compCommonContrary | 通用反色 | #ffffffff |  | #ff000000 |  |
| theme.colors.compBackgroundFocus | 获焦态背景色 | #fff1f3f5 |  | #ff000000 |  |
| theme.colors.compFocusedPrimary | 获焦态一级反色 | #e5000000 |  | #e5ffffff |  |
| theme.colors.compFocusedSecondary | 获焦态二级反色 | #99000000 |  | #99ffffff |  |
| theme.colors.compFocusedTertiary | 获焦态三级反色 | #66000000 |  | #66ffffff |  |
| theme.colors.interactiveHover | 通用悬停交互式颜色 | #0c000000 |  | #0cffffff |  |
| theme.colors.interactivePressed | 通用按压交互式颜色 | #19000000 |  | #19ffffff |  |
| theme.colors.interactiveFocus | 通用获焦交互式颜色 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.interactiveActive | 通用激活交互式颜色 | #ff0a59f7 |  | #ff317af7 |  |
| theme.colors.interactiveSelect | 通用选择交互式颜色 | #33000000 |  | #33ffffff |  |
| theme.colors.interactiveClick | 通用点击交互式颜色 | #19000000 |  | #19ffffff |  |

各个token色值可影响的组件可参考[Colors](../harmonyos-references/js-apis-arkui-theme.md#colors)接口说明。
