---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1279
title: Popup弹窗如何实现按钮关闭和外部点击关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Popup弹窗如何实现按钮关闭和外部点击关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7bcc02fa18ad3e551071157ae8e17517b355cacae5c6312dae67dab82f3bf78
---

## 问题现象

需求的场景是弹出Popup，Popup弹窗内部有提示内容和按钮，期望：

1. 点击按钮：执行逻辑后，Popup消失。
2. 点击弹窗内部非按钮区域：Popup不消失，无反应即可。
3. 点击弹窗外部：Popup消失。

## 背景知识

[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)可以为组件绑定气泡弹窗，其参数show用于控制显隐，参数PopupOptions中含有用于设置点击弹窗外部是否可以关闭弹窗的属性。

## 解决方案

1. bindPopup创建的弹窗本身具有点击弹窗内部区域后弹窗不会消失的特性。
2. 将autoCancel参数设置为true，可以实现点击弹窗外部使Popup消失。该参数不进行设置时，默认为true。
3. 给弹窗内部的按钮添加点击逻辑，改变用于控制Popup显隐的show的值。

```ts
@Entry
@Component
struct ClosePopupExample {
  @State customPopup: boolean = false;

  // popup构造器定义弹框内容
  @Builder
  popupBuilder() {
    Column({ space: 16 }) {
      Text(`Custom Popup`);
      Text('Close')
        .fontColor('#0a59f7')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        });
    }
    .width(300)
    .borderRadius(1)
    .padding({ top: 16, bottom: 16 });
  }

  build() {
    Column() {
      Row() {
      }.width('100%').height(0)
      .bindPopup(this.customPopup, {
        builder: this.popupBuilder,
        placement: Placement.Top,
        radius: 32,
        shadow: { radius: 0 },
        mask: { color: '#33000000' },
        showInSubWindow: false,
        enableArrow: false,
        autoCancel: true,
        onStateChange: (e) => {
          if (!e.isVisible) {
            this.customPopup = false;
          }
        }
      });

      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        });
    }
    .justifyContent(FlexAlign.Center)
    .width('100%').height('100%');
  }
}
```
