---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme
title: WithTheme
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 主题 > WithTheme
category: harmonyos-references
scraped_at: 2026-04-29T13:52:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:42ac7410830c57be37883af32b3706414b38d751b79900f9a3032ddef8c6ea1d
---

WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

WithTheme支持的系统组件如下：[TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)、[Button](ts-basic-components-button.md)、[Badge](ts-container-badge.md)、[Swiper](ts-container-swiper.md)、[Text](ts-basic-components-text.md)、[Select](ts-basic-components-select.md)、[Menu](ts-basic-components-menu.md)、[TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、[TextPicker](ts-basic-components-textpicker.md)、[Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md)、[Slider](ts-basic-components-slider.md)、[Progress](ts-basic-components-progress.md)、[QRCode](ts-basic-components-qrcode.md)、[Toggle](ts-basic-components-toggle.md)、[PatternLock](ts-basic-components-patternlock.md)、[Divider](ts-basic-components-divider.md)

WithTheme相关使用指导请参考[设置应用内主题换肤](../harmonyos-guides/theme_skinning.md)。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

WithTheme(options: WithThemeOptions)

设置应用局部页面自定义主题风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WithThemeOptions](ts-container-with-theme.md#withthemeoptions) | 是 | 设置作用域内组件配色。 |

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## WithThemeOptions

PhonePC/2in1TabletTVWearable

设置WithTheme作用域内组件缺省样式及深浅色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| theme | [CustomTheme](ts-container-with-theme.md#customtheme) | 否 | 是 | 用于自定义WithTheme作用域内组件缺省配色。  默认值：undefined，缺省样式跟随系统[token默认样式](../harmonyos-guides/theme_skinning.md#系统缺省token色值)。 |
| colorMode | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 是 | 用于指定WithTheme作用域内组件配色深浅色模式。  默认值：ThemeColorMode.SYSTEM |

## CustomTheme

PhonePC/2in1TabletTVWearable

type CustomTheme = CustomTheme

自定义配色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [CustomTheme](js-apis-arkui-theme.md#customtheme) | 自定义WithTheme作用域内组件缺省配色。 |

## 示例

PhonePC/2in1TabletTVWearable

设置局部深浅色时，需要添加dark.json资源文件，深浅色模式才会生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/coBNzoXqSvKJpnSlD4EZKw/zh-cn_image_0000002589326469.png?HW-CC-KV=V1&HW-CC-Date=20260429T055250Z&HW-CC-Expire=86400&HW-CC-Sign=A33EBA94C93137706D57AFF9651C3EBA78A0A6C9A3FAE1D2937747483E27474F)

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

### 示例1（指定局部深浅色模式）

```
1. // 指定局部深浅色模式
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. // 系统默认
8. Column() {
9. Text('无WithTheme')
10. .fontSize(40)
11. .fontWeight(FontWeight.Bold)
12. }
13. .justifyContent(FlexAlign.Center)
14. .width('100%')
15. .height('33%')
16. .backgroundColor($r('app.color.start_window_background'))
17. // 设置组件为深色模式
18. WithTheme({ colorMode: ThemeColorMode.DARK }) {
19. Column() {
20. Text('WithTheme')
21. .fontSize(40)
22. .fontWeight(FontWeight.Bold)
23. Text('DARK')
24. .fontSize(40)
25. .fontWeight(FontWeight.Bold)
26. }
27. .justifyContent(FlexAlign.Center)
28. .width('100%')
29. .height('33%')
30. .backgroundColor($r('sys.color.background_primary'))
31. }
32. // 设置组件为浅色模式
33. WithTheme({ colorMode: ThemeColorMode.LIGHT }) {
34. Column() {
35. Text('WithTheme')
36. .fontSize(40)
37. .fontWeight(FontWeight.Bold)
38. Text('LIGHT')
39. .fontSize(40)
40. .fontWeight(FontWeight.Bold)
41. }
42. .justifyContent(FlexAlign.Center)
43. .width('100%')
44. .height('33%')
45. .backgroundColor($r('sys.color.background_primary'))
46. }
47. }
48. .height('100%')
49. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START])
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/pRLfTcORTDOZxZ4ZWZ2eCA/zh-cn_image_0000002589246411.png?HW-CC-KV=V1&HW-CC-Date=20260429T055250Z&HW-CC-Expire=86400&HW-CC-Sign=0D53DCA7A92971FF958E31279CBB3A0A79CAE1C8ED925C93BE7D0C512ADAFDF1)

### 示例2（自定义WithTheme作用域内组件缺省配色）

```
1. // 自定义WithTheme作用域内组件缺省配色
2. import { CustomTheme, CustomColors } from '@kit.ArkUI';

4. class GreenColors implements CustomColors {
5. fontPrimary = '#ff049404';
6. fontEmphasize = '#FF00541F';
7. fontOnPrimary = '#FFFFFFFF';
8. compBackgroundTertiary = '#1111FF11';
9. backgroundEmphasize = '#FF00541F';
10. compEmphasizeSecondary = '#3322FF22';
11. }

13. class RedColors implements CustomColors {
14. fontPrimary = '#fff32b3c';
15. fontEmphasize = '#FFD53032';
16. fontOnPrimary = '#FFFFFFFF';
17. compBackgroundTertiary = '#44FF2222';
18. backgroundEmphasize = '#FFD00000';
19. compEmphasizeSecondary = '#33FF1111';
20. }

22. class PageCustomTheme implements CustomTheme {
23. colors?: CustomColors

25. constructor(colors: CustomColors) {
26. this.colors = colors
27. }
28. }

30. @Entry
31. @Component
32. struct IndexPage {
33. static readonly themeCount = 3;
34. themeNames: string[] = ['System', 'Custom (green)', 'Custom (red)'];
35. themeArray: (CustomTheme | undefined)[] = [
36. undefined, // System
37. new PageCustomTheme(new GreenColors()),
38. new PageCustomTheme(new RedColors())
39. ]
40. @State themeIndex: number = 0;

42. build() {
43. Column() {
44. Column({ space: '8vp' }) {
45. Text(`未使用WithTheme`)
46. // 点击按钮切换局部换肤
47. Button(`切换theme配色：${this.themeNames[this.themeIndex]}`)
48. .onClick(() => {
49. this.themeIndex = (this.themeIndex + 1) % IndexPage.themeCount;
50. })

52. // 系统默认按钮配色
53. Button('Button.style(NORMAL) with System Theme')
54. .buttonStyle(ButtonStyleMode.NORMAL)
55. Button('Button.style(EMP..ED) with System Theme')
56. .buttonStyle(ButtonStyleMode.EMPHASIZED)
57. Button('Button.style(TEXTUAL) with System Theme')
58. .buttonStyle(ButtonStyleMode.TEXTUAL)
59. }
60. .margin({
61. top: '50vp'
62. })

64. WithTheme({ theme: this.themeArray[this.themeIndex] }) {
65. // WithTheme作用域
66. Column({ space: '8vp' }) {
67. Text(`使用WithTheme`)
68. Button('Button.style(NORMAL) with Custom Theme')
69. .buttonStyle(ButtonStyleMode.NORMAL)
70. Button('Button.style(EMP..ED) with Custom Theme')
71. .buttonStyle(ButtonStyleMode.EMPHASIZED)
72. Button('Button.style(TEXTUAL) with Custom Theme')
73. .buttonStyle(ButtonStyleMode.TEXTUAL)
74. }
75. .width('100%')
76. }
77. }
78. }
79. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/sLZanZgBSk-kf-_098vKag/zh-cn_image_0000002558766604.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055250Z&HW-CC-Expire=86400&HW-CC-Sign=1D49BB84816FC0FCFE5FCC677EB82E8D1EA96D2F0B17C0E4CB147116AF19249A)
