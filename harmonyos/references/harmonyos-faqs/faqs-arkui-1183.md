---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1183
title: 实现Text组件和TextInput组件可以切换的堆叠布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Text组件和TextInput组件可以切换的堆叠布局
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0178d356d3d75d72f5ddffae765de925d90448c58ad4e311b5d828b019a49d63
---

## 问题现象

如何实现Text组件和TextInput组件的堆叠布局？可以相互切换，同时TextInput组件展示时，要展示焦点，同时拉起键盘。

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [@ohos.inputMethod (输入法框架)](../harmonyos-references/js-apis-inputmethod.md)：本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与第三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等等。
* [stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)：结束输入会话。
* 焦点是指光标被激活的位置，当移动鼠标点击组件时，会让组件获得焦点，获取接收键盘或者鼠标输入的能力。

## 解决方案

通过Stack容器实现Text组件和TextInput组件堆叠布局，通过配置[focusControl.requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)来指定组件获取焦点，切换时通过[showTextInput](../harmonyos-references/js-apis-inputmethod.md#showtextinput10-1)和[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)实现键盘的弹起和退出。

完整代码示例如下：

```ts
import { inputMethod } from '@kit.IMEKit';

@Entry
@Component
struct StackTextInput {
  @State isEditing: boolean = false;

  build() {
    Column() {
      Column() {
        Text('Text 切换 TextInput')
        Stack() {
          TextInput()
            .width('50%')
            .height(50)
            .defaultFocus(true)
            .enableKeyboardOnFocus(this.isEditing)
            .id('textInput')
          Text('text')
            .backgroundColor(Color.Gray)
            .textAlign(TextAlign.Center)
            .visibility(this.isEditing ? Visibility.Hidden : Visibility.Visible)
            .width('50%')
            .height(50)
            .onClick(() => {
              // 可以通过配置focusControl.requestFocus使指定组件获取焦点
              focusControl.requestFocus('textInput');
              this.isEditing = true;
              // 拉起键盘
              let inputMethodController = inputMethod.getController();
              inputMethodController.showTextInput();
            })
        }
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .onClick(() => {
        this.isEditing = false;
        // 退出键盘
        let inputMethodController = inputMethod.getController();
        inputMethodController.stopInputSession();
      })
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
