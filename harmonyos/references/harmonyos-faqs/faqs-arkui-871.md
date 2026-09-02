---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-871
title: 平板设备横屏状态下，点击输入框时页面上移导致看不到输入框
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 平板设备横屏状态下，点击输入框时页面上移导致看不到输入框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4c6a3a646b58661f5bbf45f75a570348f42e952d4c1e20d9ebbd6d0a30af9969
---

## 问题现象

在设备上打开应用，点击页面底部的输入框弹起键盘后，页面整体内容上移导致页面顶部内容超出屏幕看不到。

## 背景知识

* [软键盘布局适配](../best-practices/bpta-keyboard-layout-adapt.md)：包含重要信息被软键盘遮挡、软键盘弹出导致布局错位、软键盘弹出导致弹窗过度上抬等情况适配。
* [setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)：控制虚拟键盘抬起时页面的避让模式。
* [KeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)：配置键盘弹出时页面的避让模式。

## 问题定位

1. 全局代码中搜索setKeyboardAvoidMode，查看应用是否通过该方法设置键盘不同的避让模式。
2. 当应用中未设置或设置为KeyboardAvoidMode.OFFSET时，此时键盘避让为上抬模式。会导致点击输入框时，键盘抬起，为避让键盘整体页面上移，页面顶部内容超出屏幕看不见。

## 分析结论

系统虚拟键盘的避让模式默认值为上抬模式，当键盘抬起时，页面为了避让软键盘，页面内容会整体上抬，导致页面上方的内容超出了屏幕外，页面需要根据实际情况，选择不同的避让模式。

## 修改建议

1. 设置虚拟键盘抬起时页面的避让模式为NONE不避让键盘模式。

   ```screen
   import { KeyboardAvoidMode } from '@kit.ArkUI';

   @Entry
   @Component
   struct keyboard {
     placeHolderArr: string[] = ['1', '2', '3', '4', '5', '6', '7', '8'];

     aboutToAppear(): void {
       this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE);
     }

     build() {
       Row() {
         Column() {
           ForEach(this.placeHolderArr, (placeholder: string) => {
             TextInput({ placeholder: 'TextInput ' + placeholder })
               .margin(30);
           });
         };
       }
       .alignItems(VerticalAlign.Top)
       .width('100%')
       .height('100%');
     }
   }
   ```
2. 也可设置避让模式为压缩模式KeyboardAvoidMode.RESIZE，避免遮挡其他组件；更多场景、案例参考[软键盘布局适配](../best-practices/bpta-keyboard-layout-adapt.md)。
