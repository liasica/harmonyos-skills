---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-24
title: 平板上自定义键盘弹出，显示不全
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板上自定义键盘弹出，显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:74ee731e39a43c002817e46a7b24c8d12514b21051e45db4ce6ccb07800a252f
---

## 问题现象

应用在平板打开后，点击输入框弹出自定义键盘，自定义键盘显示不全。

## 背景知识

* [自定义键盘](../best-practices/bpta-custom-keyboard.md)：自定义键盘是一种简易的键盘替换系统默认键盘，允许用户根据实际业务场景和习惯偏好，调整键盘的布局和位置、添加额外的功能键。自定义键盘的高度通过自定义组件根节点的height属性设置，宽度不可设置，默认为屏幕宽度。
* [尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)：设置组件的宽高、边距。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：开启窗口尺寸变化的监听。

## 问题定位

自定义键盘宽度可以自适应屏幕宽度，高度可以通过自定义组件根节点的height属性设置，因此建议检查代码中是否使用on('windowSizeChange')动态监听窗口尺寸变化，并且自定义键盘组件的高度设置值是否根据窗口尺寸动态调整高度，确保键盘可以在大屏下完全显示。

## 分析结论

应用未使用on('windowSizeChange')动态监听窗口尺寸变化，并动态设置自定义键盘的高度，导致在大屏状态下，自定义键盘高度不够，键盘显示不全。

## 修改建议

使用on('windowSizeChange')动态监听窗口尺寸变化，动态调整自定义键盘的高度，确保每个设备都可以完整显示。

```ts
import { common } from '@kit.AbilityKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct KeyBoardDemo {
  controller: SearchController = new SearchController();
  private inputValue: string = '';
  @State windowHeight: number = 0;

  aboutToAppear() {
    this.windowHeight = display.getDefaultDisplaySync().height;
    try {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let windowStage = context.windowStage;
      let windowClass = windowStage.getMainWindowSync();
      windowClass.on('windowSizeChange', (data) => {
        this.windowHeight = data.height;
      });
    } catch (exception) {
      console.error(`Failed to enable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Row() {
        Text('此区域为自定义键盘区域，实际开发需替换为实际的键盘布局');
        Text('关闭键盘').onClick(() => {
          // 关闭自定义键盘
          this.controller.stopEditing();
        });
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround);
    }.backgroundColor('#E5E5EA')
    .height(this.getUIContext().px2vp(this.windowHeight * 0.3));
  }

  build() {
    Column() {
      Search({ controller: this.controller, value: this.inputValue })// 绑定自定义键盘
        .customKeyboard(this.CustomKeyboardBuilder()).margin(10);
    };
  }
}
```
