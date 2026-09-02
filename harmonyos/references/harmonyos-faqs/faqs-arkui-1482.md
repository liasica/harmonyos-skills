---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1482
title: TextInput组件点击组件外区域收起软键盘的实现方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput组件点击组件外区域收起软键盘的实现方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:a5b9e986dc8b7a2359f9b880fdae9f03e713cd12a3f1f0f79bd8e04bfe0e9054
---

## 问题现象

使用TextInput组件时，点击组件获取焦点后弹出软键盘，当点击TextInput组件外部区域时，如何实现收起软键盘？

## 背景知识

* [TextInput](../harmonyos-guides/arkts-common-components-text-input.md)：单行文本输入框组件。
* [stopEditing](../harmonyos-references/ts-basic-components-textarea.md#stopediting10)：退出编辑态。
* [@ohos.inputMethod (输入法框架)](../harmonyos-references/js-apis-inputmethod.md)：本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等。
* [stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9)：结束输入会话。

## 解决方案

针对TextInput获取焦点时，实现点击组件外区域收起软键盘的效果。

* **方案一**：当页面只有一个TextInput组件时，通过给外层组件添加点击事件，调用stopEditing方法收起键盘。

  ```ts
  .onClick(() => {
    // 调用stopEditing()方法关闭键盘
    this.controller.stopEditing();
  });
  ```

* **方案二**：当页面只有多个TextInput组件时，如果使用方案一调用stopEditing方法关闭键盘时需要定义多个controller控制器比较繁琐，这种情况下使用@ohos.inputMethod(输入法框架)，通过输入法服务InputMethodController的[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9)接口控制点击组件外区域收起键盘。

  ```ts
  .onClick(() => {
        // 调用[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)()方法关闭键盘
        inputMethod.getController().[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)();
      });
  ```

完整示例代码如下：

```ts
import { inputMethod } from '@kit.IMEKit';
import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';

@Component
struct SingleTextInput {
  controller: TextInputController = new TextInputController();
  @State message: string = '';

  build() {
    Column() {
      TextInput({ text: this.message, placeholder: '请输入内容', controller: this.controller })
        .height(40);
    }
    .width('100%')
    .height('100%')
    // Startsolution1
    .onClick(() => {
      // 调用stopEditing()方法关闭键盘
      this.controller.stopEditing();
    });

    // Endsolution1
  }
}

@Component
struct MultiTextInput {
  build() {
    Column({ space: 16 }) {
      TextInput({ placeholder: '请输入内容' }).height(40);
      TextInput({ placeholder: '请输入内容' }).height(40);
    }
    .height('100%')
    .width('100%')
    // Startsolution2
    .onClick(() => {
      // 调用[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)()方法关闭键盘
      inputMethod.getController().[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9-1)();
    });

    // Endsolution2
  }
}

@Entry
@Component
struct TextStopInput {
  fontColor: string = '#182431';
  selectedFontColor: string = '#0A59F7';
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  @State tabSelectedIndexes: number[] = [0]; // SegmentButton默认选项
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: [{ text: '单输入框场景' }, { text: '多输入框场景' },] as ItemRestriction<SegmentButtonTextItem>,
    backgroundColor: '#0d000000',
    selectedBackgroundColor: $r('sys.color.white'),
    fontWeight: 400,
    selectedFontWeight: 500,
    textPadding: 6
  });
  private controller: TabsController = new TabsController();

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 });
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.selectedIndex === index ? 1 : 0);
    }.width('100%');
  }

  build() {
    Column() {
      SegmentButton({
        options: this.tabOptions,
        selectedIndexes: $tabSelectedIndexes,
        onItemClicked: (index) => {
          this.getUIContext().animateTo({ duration: 400 }, () => {
            this.currentIndex = index;
            this.controller.changeIndex(index);
          });
        }
      })
        .borderRadius(20)
        .margin({
          bottom: 16
        })
        .width('100%')
        .height(40);

      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          SingleTextInput();
        }.tabBar(this.tabBuilder(0, '单输入框场景'));

        TabContent() {
          MultiTextInput();
        }.tabBar(this.tabBuilder(1, '多输入框场景'));

      }
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(0)
      .onChange((index: number) => {
        // currentIndex控制TabContent显示页签
        this.currentIndex = index;
        this.selectedIndex = index;
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        if (index === targetIndex) {
          return;
        }
        console.info(`event currentOffset ${event.currentOffset}`);
        // selectedIndex控制自定义TabBar内Image和Text颜色切换
        this.selectedIndex = targetIndex;
      })
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .padding({
      left: 16,
      right: 16,
      top: 12
    });
  }
}
```

## 常见FAQ

Q：方案二中通过输入法服务[InputMethodController](../harmonyos-references/js-apis-inputmethod.md#inputmethodcontroller)的[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9)接口实现点击组件外区域收起软键盘的效果，会影响其他组件交互吗？比如按钮等。

A：此种方式下可以做到不影响其他组件交互。

## 总结

| 方案 | 使用场景 |
| --- | --- |
| 方案一 | 页面TextInput组件较少时使用。 |
| 方案二 | 页面TextInput组件较多时使用。 |
