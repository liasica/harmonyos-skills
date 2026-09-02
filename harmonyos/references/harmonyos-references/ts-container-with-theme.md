---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme
title: WithTheme
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 主题 > WithTheme
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a32bbc51a54e27de983400e513debbb6803bc4600468f6928cb0e84755ae6384
---

WithTheme组件用于设置应用局部页面自定义主题风格，可设置子组件深浅色模式和自定义配色。

**说明** 

* 该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。
* WithTheme支持的系统组件如下：[TextInput](ts-basic-components-textinput.md)、[Search](ts-basic-components-search.md)、[Button](ts-basic-components-button.md)、[Badge](ts-container-badge.md)、[Swiper](ts-container-swiper.md)、[Text](ts-basic-components-text.md)、[Select](ts-basic-components-select.md)、[Menu](ts-basic-components-menu.md)、[TimePicker](ts-basic-components-timepicker.md)、[DatePicker](ts-basic-components-datepicker.md)、[TextPicker](ts-basic-components-textpicker.md)、[Checkbox](ts-basic-components-checkbox.md)、[CheckboxGroup](ts-basic-components-checkboxgroup.md)、[Radio](ts-basic-components-radio.md)、[Slider](ts-basic-components-slider.md)、[Progress](ts-basic-components-progress.md)、[QRCode](ts-basic-components-qrcode.md)、[Toggle](ts-basic-components-toggle.md)、[TextClock](ts-basic-components-textclock.md)、[PatternLock](ts-basic-components-patternlock.md)、[Divider](ts-basic-components-divider.md)。从API版本26.0.0开始，新增[CalendarPicker](ts-basic-components-calendarpicker.md)、[UIPickerComponent](ts-container-ui-picker-component.md)、[TextArea](ts-basic-components-textarea.md)、[属性字符串](ts-universal-styled-string.md)、[Gauge](ts-basic-components-gauge.md)、[DataPanel](ts-basic-components-datapanel.md)、[RichEditor](ts-basic-components-richeditor.md)、[MenuItem](ts-basic-components-menuitem.md)、[MenuItemGroup](ts-basic-components-menuitemgroup.md)、[Image](ts-basic-components-image.md)、[ImageAnimator](ts-basic-components-imageanimator.md)、[Counter](ts-container-counter.md)、[bindSheet](ts-universal-attributes-sheet-transition.md#bindsheet)、[LoadingProgress](ts-basic-components-loadingprogress.md)。
* WithTheme相关使用指导请参考[设置应用内主题换肤](../harmonyos-guides/theme_skinning.md)。

## 子组件

支持单个子组件。

## 接口

WithTheme(options: WithThemeOptions)

设置应用局部页面自定义主题风格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [WithThemeOptions](ts-container-with-theme.md#withthemeoptions) | 是 | 设置作用域内组件配色。 |

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## WithThemeOptions

设置WithTheme作用域内组件缺省样式及深浅色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| theme | [CustomTheme](ts-container-with-theme.md#customtheme) | 否 | 是 | 用于自定义WithTheme作用域内组件缺省配色。  默认值：undefined，缺省样式跟随系统[token默认样式](../harmonyos-guides/theme_skinning.md#系统缺省token色值)。 |
| colorMode | [ThemeColorMode](ts-universal-attributes-foreground-blur-style.md#themecolormode枚举说明) | 否 | 是 | 用于指定WithTheme作用域内组件配色深浅色模式。  默认值：ThemeColorMode.SYSTEM |

## CustomTheme

type CustomTheme = import('../api/@ohos.arkui.theme').CustomTheme

自定义配色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.theme').[CustomTheme](js-apis-arkui-theme.md#customtheme) | 自定义WithTheme作用域内组件缺省配色。 |

## 示例

设置局部深浅色时，需要添加dark.json资源文件，深浅色模式才会生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/Vcr3VAShQn6S54lk7F0EvQ/zh-cn_image_0000002736435397.png)

dark.json数据示例：

```ts
  {
    "color": [
      {
        "name": "start_window_background",
        "value": "#000000"
      }
    ]
  }
```

### 示例1（指定局部深浅色模式）

```ts
// 指定局部深浅色模式
@Entry
@Component
struct Index {
  build() {
    Column() {
    // 系统默认
      Column() {
        Text('无WithTheme')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('33%')
      .backgroundColor($r('app.color.start_window_background'))
      // 设置组件为深色模式
      WithTheme({ colorMode: ThemeColorMode.DARK }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('DARK')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }
      // 设置组件为浅色模式
      WithTheme({ colorMode: ThemeColorMode.LIGHT }) {
        Column() {
          Text('WithTheme')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
          Text('LIGHT')
            .fontSize(40)
            .fontWeight(FontWeight.Bold)
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('33%')
        .backgroundColor($r('sys.color.background_primary'))
      }
    }
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.END, SafeAreaEdge.BOTTOM, SafeAreaEdge.START])
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/og29KqDWQzaHhMVPbc-FXA/zh-cn_image_0000002706836246.png)

### 示例2（自定义WithTheme作用域内组件缺省配色）

```ts
// 自定义WithTheme作用域内组件缺省配色
import { CustomTheme, CustomColors } from '@kit.ArkUI';

class GreenColors implements CustomColors {
  fontPrimary = '#ff049404';
  fontEmphasize = '#FF00541F';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#1111FF11';
  backgroundEmphasize = '#FF00541F';
  compEmphasizeSecondary = '#3322FF22';
}

class RedColors implements CustomColors {
  fontPrimary = '#fff32b3c';
  fontEmphasize = '#FFD53032';
  fontOnPrimary = '#FFFFFFFF';
  compBackgroundTertiary = '#44FF2222';
  backgroundEmphasize = '#FFD00000';
  compEmphasizeSecondary = '#33FF1111';
}

class PageCustomTheme implements CustomTheme {
  colors?: CustomColors

  constructor(colors: CustomColors) {
    this.colors = colors
  }
}

@Entry
@Component
struct IndexPage {
  static readonly themeCount = 3;
  themeNames: string[] = ['System', 'Custom (green)', 'Custom (red)'];
  themeArray: (CustomTheme | undefined)[] = [
    undefined, // System
    new PageCustomTheme(new GreenColors()),
    new PageCustomTheme(new RedColors())
  ]
  @State themeIndex: number = 0;

  build() {
    Column() {
      Column({ space: '8vp' }) {
        Text(`未使用WithTheme`)
        // 点击按钮切换局部换肤
        Button(`切换theme配色：${this.themeNames[this.themeIndex]}`)
          .onClick(() => {
            this.themeIndex = (this.themeIndex + 1) % IndexPage.themeCount;
          })

        // 系统默认按钮配色
        Button('Button.style(NORMAL) with System Theme')
          .buttonStyle(ButtonStyleMode.NORMAL)
        Button('Button.style(EMP..ED) with System Theme')
          .buttonStyle(ButtonStyleMode.EMPHASIZED)
        Button('Button.style(TEXTUAL) with System Theme')
          .buttonStyle(ButtonStyleMode.TEXTUAL)
      }
      .margin({
        top: '50vp'
      })

      WithTheme({ theme: this.themeArray[this.themeIndex] }) {
        // WithTheme作用域
        Column({ space: '8vp' }) {
          Text(`使用WithTheme`)
          Button('Button.style(NORMAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.NORMAL)
          Button('Button.style(EMP..ED) with Custom Theme')
            .buttonStyle(ButtonStyleMode.EMPHASIZED)
          Button('Button.style(TEXTUAL) with Custom Theme')
            .buttonStyle(ButtonStyleMode.TEXTUAL)
        }
        .width('100%')
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZoC1Md15Tni5g-YtPNmnbA/zh-cn_image_0000002736315351.gif)
