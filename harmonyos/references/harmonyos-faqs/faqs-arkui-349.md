---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-349
title: 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:44da731dd98004de3a80a316c5645444e1fb370299d2ffa33406cb85604b2b0b
---

通过radius参数调整圆角大小，但箭头颜色需通过popupColor间接设置。示例代码如下：

```ts
@Entry
@Component
struct BindPopupDemo {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Popup constructor defines the content of the popup box
  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Image($r('app.media.startIcon'))
        .width(24)
        .height(24)
        .margin({ left: -5 })
      Text('Custom Popup')
        .fontSize(10)
    }
    .width(100)
    .height(50)
    .padding(5)
  }

  build() {
    RelativeContainer() {
      Button('CustomPopupOptions')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          radius: 30,
          popupColor: Color.Yellow,
          enableArrow: true,
          onStateChange: (e) => {
            if (!e.isVisible) {
              this.customPopup = false;
            }
          }
        })
    }
  }
}
```
