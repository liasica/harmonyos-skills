---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-786
title: 实现Text长按和点击弹出不同的菜单
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Text长按和点击弹出不同的菜单
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a3792d3b7f1a9d759df85cbca53ef190651a14da58808814cc0aeba50eafa31e
---

## 问题现象

Text组件绑定了bindPopup和bindMenu，想要长按显示bindMenu，点击显示bindPopup，该如何实现？

## 背景知识

* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)：为组件绑定Popup气泡。
* [bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)：给组件绑定菜单，点击后弹出菜单。
* [LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md#longpressgesture-1)：创建长按手势对象。
* [TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)：创建点击手势对象。

## 解决方案

使用组合手势中的互斥手势[GestureMode.Exclusive](../harmonyos-references/ts-combined-gestures.md#gesturemode枚举说明)来实现长按手势[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)触发弹出bindMenu，点击手势[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)触发弹出bindPopup。

```screen
@Entry
@Component
struct GestureGroupDemo {
  @State isMenu: boolean = false;
  @State isPopup: boolean = false;

  @Builder
  bindMenuBuilder() {
    Row() {
      Text('MenuContent');
    }.backgroundColor(Color.Pink);
  }

  @Builder
  bindPopupBuilder() {
    Row() {
      Text('PopupContent');
    }.backgroundColor(Color.Orange);
  }

  build() {
    RelativeContainer() {
      Button('长按或者点击')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .fontSize(28)
        .gesture(
          GestureGroup(GestureMode.Exclusive,
            LongPressGesture({ repeat: true })
              .onAction(() => {
                this.isPopup = false;
                this.isMenu = true;
              }),
            TapGesture({ count: 1, fingers: 1 })
              .onAction(() => {
                this.isMenu = false;
                this.isPopup = !this.isPopup;
              }))
        )
        .bindContextMenu(this.isMenu, this.bindMenuBuilder())
        .bindPopup(this.isPopup, {
          builder: this.bindPopupBuilder(), onStateChange: (e) => {
            if (!e.isVisible) {
              this.isPopup = false;
            }
          },
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
