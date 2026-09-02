---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1161
title: 使用customKeyboard设置自定义键盘时，弹出失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 使用customKeyboard设置自定义键盘时，弹出失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8fad21bb42eb7f5abbe628a097f59ad54fad9765d16574645a40be1fb7e774c0
---

## 问题现象

自定义键盘通过focusController获取焦点的时候，弹出的键盘是系统键盘，而不是预期的自定义键盘。

问题代码示例参考如下：

```screen
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController()
  @State keyboardVisible: boolean = false
  customKeyboard: CustomBuilder = () => {
    this.buildCustomKeyboard()
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined) // 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘
      Button('切换自定义键盘').onClick(() => {
        this.keyboardVisible = true
        this.getUIContext().getFocusController().requestFocus('RichEditor')
      })
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false
        })
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 自定义键盘
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘')
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd')
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/0nSRHe54Tny6hhf5R3VMMg/zh-cn_image_0000002628569772.gif "点击放大")

## 背景知识

* [@Builder装饰器](../harmonyos-guides/arkts-builder.md)：ArkUI提供了一种轻量的UI元素复用机制@Builder，其内部UI结构固定，仅与使用方进行数据传递，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。
* [customKeyboard属性](../harmonyos-references/ts-basic-components-richeditor.md#customkeyboard)：该属性可用于设置自定义键盘。其第一个参数[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)用于自定义UI描述，必须结合@Builder使用。
* [@ohos.arkui.UIContext(UIContext)](../harmonyos-references/js-apis-arkui-uicontext.md)与通用[焦点事件](../harmonyos-references/ts-universal-attributes-focus.md)获取焦点差异：

  [this.getUIContext().getFocusController().requestFocus()](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#requestfocus12)：通过组件的id将焦点转移到组件树对应的实体节点。在当前帧生效。

  [focusControl.requestFocus()](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：此接口可以主动让焦点转移至参数指定的组件上。非当前帧生效，在下一帧才生效。

## 问题定位

1. this.customKeyboard函数未用@Builder装饰器修饰。

   customKeyboard属性的第一个参数[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)用于自定义UI描述，必须结合@Builder使用。
2. 由于customKeyboard属性不是实时渲染，在更改this.keyboardVisible变量后，customKeyboard需要更新渲染。

   该问题代码中this.getUIContext().getFocusController().requestFocus("RichEditor")是在当前帧生效。更改this.keyboardVisible变量后，customKeyboard还没有完成渲染，因此第一次依旧会弹出系统键盘。使用focusControl.requestFocus("RichEditor")让控件在下一帧获取焦点即可，此时customKeyboard已完成渲染。

## 分析结论

该问题代码存在以下两个问题：

1. customKeyboard属性内this.customKeyboard函数未使用@Builder装饰器修饰，导致customKeyboard属性设置失效，无法弹出自定义键盘。
2. this.getUIContext().getFocusController().requestFocus("RichEditor")获取焦点是在当前帧生效，由于更改keyboardVisible变量后，customKeyboard未更新渲染完成，导致第一次获取焦点无法弹出自定义键盘。

## 修改建议

1. 采用@Builder装饰器自定义构建函数。修改customKeyboard函数代码：

   ```screen
   @Builder
   customKeyboard() {
     this.buildCustomKeyboard();
   }
   ```
2. customKeyboard属性更新后再获取焦点。采用focusControl.requestFocus方法代替this.getUIContext().getFocusController().requestFocus方法获取组件焦点。

   ```screen
   Button('切换自定义键盘')
     .onClick(() => {
       this.keyboardVisible = true;
       focusControl.requestFocus('RichEditor');
     });
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController();
  @State keyboardVisible: boolean = false;

  @Builder
  customKeyboard() {
    this.buildCustomKeyboard();
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined); // 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘
      Button('切换自定义键盘')
        .onClick(() => {
          this.keyboardVisible = true;
          focusControl.requestFocus('RichEditor');
        });
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false;
        });
    }
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }

  // 自定义键盘
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘');
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd');
  }
}
```
