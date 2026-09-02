---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1601
title: 如何控制Popup在指定时机消失
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何控制Popup在指定时机消失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:19c3a5b07d0dce2563ed75841a4309a4a5abbb21f810cec8268b315792b4b1c0
---

## 问题现象

Popup弹出后，没办法在指定时机消失。

* 预期效果：Popup弹出后，能在指定时机消失。如：在Button组件上弹出气泡Popup，只有再次点击Button，才会主动触发Popup消失，点击页面其它位置不消失。
* 实际效果：Popup弹出后，任何点击事件都会消失。

## 背景知识

[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)：给组件绑定Popup弹窗，并设置弹窗内容，交互逻辑和显示状态。

## 问题定位

bindPopup的第二个参数是PopupOptions对象，其默认autoCancel的值是true，mask值也是true，会展示遮罩，点击遮罩会默认关闭Popup弹窗，而遮罩会遮挡住下面内容区域，导致点击事件无法透传到下面内容区域，而直接关闭弹窗。

## 分析结论

可以将autoCancel设为false，mask设为false，点击页面其他位置，而Popup弹窗不消失，如果需要Popup消失，可以在布局容器中增加点击事件去控制show变量来隐藏弹窗。

## 修改建议

如下示例代码中，第一个Button没有设置autoCancel和mask，点击页面其他位置会关闭Popup。而第二个Button设置了autoCancel为false，mask为false之后，点击页面其他位置Popup不会消失。

```ts
@Entry
@Component
struct PopupControlMiss {
  @State customPopup: boolean = false;
  @State handlePopup: boolean = false;

  build() {
    Column({ space: 100 }) {
      Button('popup')
        .margin({ top: 50 })
        .onClick(() => {
          this.customPopup = !this.customPopup;
        })
        .bindPopup(this.customPopup, {
          message: 'this is a popup',
          arrowHeight: 20, // 设置气泡箭头高度
          arrowWidth: 20, // 设置气泡箭头宽度
          radius: 20, // 设置气泡的圆角
          shadow: ShadowStyle.OUTER_DEFAULT_XS, // 设置气泡的阴影
        });
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          width: 300,
          message: 'This is a popup with PopupOptions',
          mask: false,
          arrowPointPosition: ArrowPointPosition.START, // 设置箭头的位置
          backgroundBlurStyle: BlurStyle.NONE, // 关闭气泡的模糊背景
          popupColor: Color.Red, // 设置气泡的背景色
          autoCancel: false,
        });
    }
    .width('100%');
  }
}
```

## 总结

Popup弹窗默认会有透明遮罩挡住底部页面，将mask设为false即可。此外，如果需要更精确的控制弹窗的隐藏的话还可以在onWillDismiss事件中进行拦截控制，包含系统返回拦截以及点击组件外部区域拦截。
