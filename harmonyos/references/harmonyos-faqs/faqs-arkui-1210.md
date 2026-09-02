---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1210
title: bindPopup弹窗自定义圆角位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > bindPopup弹窗自定义圆角位置
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4e083deb3991a406df892dd7ae376fa07d4800fbe2e64cddca9233adce8448e8
---

## 问题现象

bindPopup弹窗如何自定义圆角位置？如只设置底部或者顶部圆角？

## 背景知识

[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)为组件绑定Popup气泡，入参[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)的部分字段说明如下：

* radius：可以设置气泡圆角半径，但不支持自定义圆角位置。
* popupColor：设置气泡的背景颜色。

## 解决方案

设置气泡的背景popupColor为透明色，再通过设置气泡内的最外层组件的圆角样式，以在视觉上实现气泡自定义圆角位置的效果。

**说明** 

设置popupColor为透明色时一定要设置backgroundBlurStyle字段为BlurStyle.NONE。

只设置气泡弹窗的左上和右下圆角。

```screen
@Entry
@Component
struct BindPopupDemo {
  @State customPopup: boolean = false; // 定义变量控制弹窗显示

  // popup构造器定义弹框内容
  @Builder
  popupBuilder() {
    Column({ space: 2 }) {
      Text('Popup').margin({ top: 16, bottom: 16 });
    }
    .justifyContent(FlexAlign.SpaceAround)
    .borderRadius({ topLeft: 16, bottomRight: 16 }) // 设置Column左上和右下圆角
    .width(100)
    .borderWidth(1);
  }

  build() {
    Column() {
      Button('click')
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
          mask: false,
          popupColor: Color.Transparent, // 气泡的背景色设为透明
          backgroundBlurStyle: BlurStyle.NONE, // 关闭气泡模糊背景
          radius: 0, // 设置气泡的圆角
          shadow: { radius: 0 },
          onStateChange: (e) => {
            this.customPopup = e.isVisible;
          }
        });
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

限制：由于是在气泡自定义内容函数中根组件设置圆角样式，所以不能在bindPopup入参中再设置箭头、阴影、背景颜色等样式，否则会和弹窗根组件设置的样式产生干扰。
