---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-994
title: Popup如何实现点击按钮不关闭气泡，点击按钮外部关闭气泡
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Popup如何实现点击按钮不关闭气泡，点击按钮外部关闭气泡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9468d8684179b86e7212959823730cdce155118cd5824bd23399b1aa7dd9133f
---

## 问题现象

如何实现点击按钮展示气泡，点击按钮不关闭气泡，仍保持展示状态，但是点击非按钮区域关闭气泡？

## 背景知识

* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)为组件绑定Popup气泡，并设置气泡内容、交互逻辑和显示状态。参数show控制气泡显示状态。Popup气泡必须等待页面全部构建完成才能展示，因此show不能在页面构建中设置为true，否则会导致Popup气泡显示位置及形状错误。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)触摸事件由手指在组件上按下、滑动或抬起时触发。

## 解决方案

Popup气泡弹出时，默认有遮罩层（即参数mask默认为true），且页面有操作时气泡自动关闭（即参数autoCancel默认为true）。因此在点击按钮弹出气泡后，遮罩层覆盖整个页面，再次点击按钮，触发气泡自动关闭。

要实现点击按钮气泡不关闭保持展示状态，点击非按钮区域关闭气泡，可以禁用气泡遮罩层，通过为非按钮区域绑定onTouch事件自行处理气泡关闭逻辑。

```ts
@Entry
@Component
struct PopupForClickButtonNotClose {
  @State handlePopup: boolean = false;

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Text('这里是自定义气泡的内容')
        .textAlign(TextAlign.Center)
        .fontSize(10);
    }.height(40).padding({ left: 10, right: 10 });
  }

  build() {
    Column({ space: 100 }) {
      Button('PopupOptions').margin({ top: 100 })
        .onClick(() => {
          this.handlePopup = true;
        })
        .onTouch((e) => {
          e.stopPropagation();
        }) // 阻止事件传递,避免气泡有关闭再打开的效果
        .bindPopup(this.handlePopup, {
          builder: this.popupBuilder,
          placement: Placement.Bottom,
          enableArrow: false, // 气泡弹出时不显示箭头
          targetSpace: '15vp',
          mask: false,
          autoCancel: false,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.handlePopup = false;
            }
          }
        });
    }
    .width('100%')
    .height('100%')
    .onTouch(() => {
      this.handlePopup = false;
    });
  }
}
```
