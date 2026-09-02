---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-984
title: 如何设置bindPopup的箭头颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置bindPopup的箭头颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:27869f96c54eec9747203d96cd69d36d84c313ab32edd97ebd0bee3a26a08834
---

## 问题现象

使用bindPopup时，如何设置弹出气泡的箭头颜色，以实现定制化气泡样式的诉求？

## 背景知识

* [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)：为组件绑定Popup气泡，并设置气泡内容、交互逻辑和显示状态。
* [PopupOptions类型说明](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的popupColor属性可用于配置气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。该属性默认值为透明色。

## 解决方案

bindPopup箭头是容器的一部分，和popupColor一致，popupColor默认是透明色。如果想让bindPopup的箭头和内容颜色不一致，可以在Builder中设置内容颜色，popupColor再单独设置气泡颜色。内容与气泡背景色的差异，就是箭头的颜色。

```screen
@Entry
@Component
struct PopupDemoForPopArrowColor {
  @State customPopup: boolean = false;

  // popup构造器定义弹框内容
  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Image($r("app.media.startIcon")).width(24).height(24).margin({ left: -5 });
      Text('Custom Popup').fontSize(10);
    }.height(50).padding({ left: 15, right: 15 })
    .backgroundColor(Color.White);
  }

  build() {
    Flex({ direction: FlexDirection.Column }) {
      // CustomPopupOptions 类型设置弹框内容
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          backgroundBlurStyle: BlurStyle.NONE,
          popupColor: Color.Blue,
          enableArrow: true,
          showInSubWindow: true,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
        .position({ x: 80, y: 350 });
    }.width('100%').padding({ top: 5 });
  }
}
```
