---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1118
title: 拉起软键盘后，软键盘遮挡页面内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 拉起软键盘后，软键盘遮挡页面内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:3ea38ef8071c29e271f8c86e1435485bcc255090702f75d29bd0cf57cee0e5d4
---

## 问题现象

拉起软键盘后，软键盘遮挡页面，体验不佳。

## 背景知识

1. 软键盘是用户进行交互的重要途径之一，同时软键盘的弹出和收起，可能会影响到正在显示的UI元素，影响用户体验。
2. 软键盘避让机制：系统默认的软键盘避让形式只能保证输入框不被遮挡，输入框下方的组件可能就会被软键盘挡住。
3. 软键盘避让模式：当用户在输入时，为了确保输入框不会被键盘遮挡，系统提供了避让模式来解决这一问题。开发者可以通过[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)控制虚拟键盘抬起时页面的避让模式，避让模式有上抬模式和压缩模式两种，键盘抬起时默认页面避让模式为上抬模式。
   * 上抬模式（KeyboardAvoidMode.OFFSET）：为了避让软键盘，Page内容会整体上抬。
   * 压缩模式（KeyboardAvoidMode.RESIZE）：压缩Page的大小，Page下设置百分比宽高的组件会跟随Page压缩，直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode.RESIZE时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。

4. 在移动设备上，支持设置[Web页面的软键盘避让模式](../harmonyos-guides/web-docking-softkeyboard.md#设置软键盘避让模式)。
   * 在应用代码中设置UIContext的软键盘避让模式setKeyboardAvoidMode()。ArkWeb组件支持Resize和Offset两种模式。
     + Resize模式下，应用窗口高度可缩小避开软键盘，ArkWeb组件跟随ArkUI重新布局。
     + Offset模式下（以及默认模式），应用窗口高度不变，ArkWeb组件根据自身的避让模式进行避让。
   * 在UIContext的键盘避让模式为Offset模式时，应用可通过[WebKeyboardAvoidMode()](../harmonyos-references/arkts-basic-components-web-e.md#webkeyboardavoidmode12)设置ArkWeb组件的键盘避让模式。Web组件的WebKeyboardAvoidMode()接口优先级高于W3C侧virtualKeyboard.overlayContens。
5. [customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)接口用于设置自定义键盘，[KeyboardOptions](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)接口用于设置自定义键盘是否支持避让功能。

## 问题定位

1. 检索关键字customKeyboard，确认键盘是否是自定义键盘。若为自定义键盘，查看是否设置支持避让功能。

   ```ts
   @State supportAvoidance: boolean = false; // 默认值为false，表示不支持避让；true表示支持避让

   TextInput({ controller: this.controller, text: this.inputValue }) // 绑定自定义键盘
     .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
     .margin(10)
     .border({ width: 1 })
   ```
2. 若键盘不是自定义键盘，打开EntryAbility文件，检查代码，定位关键词setKeyboardAvoidMode查看应用避让模式。

   ```ts
   // 上抬模式
   windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET);
   ```
3. 设置为KeyboardAvoidMode.OFFSET或没有设置，页面避让模式都为上抬模式，只能保证输入框不被遮挡，输入框下方的组件可能就会被软键盘挡住。
4. 尝试修改避让模式为压缩模式，核心代码如下。

   ```ts
   // 压缩模式
   windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
   ```

## 分析结论

自定义键盘没有设置支持避让功能或系统默认键盘没有根据页面布局选择合适的软键盘避让模式。

## 修改建议

1. 若页面使用的是[自定义键盘避让](../harmonyos-guides/arkts-customize-keyboard.md#使用系统提供的自定义键盘避让功能)，需要手动设置TextInput组件的customKeyboard属性[supportAvoidance](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)为true，开启系统提供的自定义键盘避让功能。
2. 若页面使用的是系统默认键盘，建议在拉起软键盘的地方设置[避让模式](../best-practices/bpta-keyboard-layout-adapt.md#section19987195213425)为压缩模式，避免遮挡其他组件。
3. 更多场景、案例参考[软键盘布局适配解决方案](../best-practices/bpta-keyboard-layout-adapt.md)。
