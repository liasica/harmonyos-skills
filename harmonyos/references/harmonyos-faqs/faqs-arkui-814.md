---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-814
title: 如何使Popup宽度占满屏幕
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使Popup宽度占满屏幕
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9940128fa39e1b30aff6e4b7c50334ca197b04d9c57e42b066ad8943d016ce45
---

## 问题现象

使用bindPopup创建气泡弹窗，如何使气泡弹窗的宽度占满屏幕？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Aw-h4j1FRdOFbpS20ssYvg/zh-cn_image_0000002658917117.png "点击放大")

## 背景知识

[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)方法中填入的Popup参数有两种类型，[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)和[CustomPopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)：

* PopupOptions依靠文本信息构建内容，样式相对固定。
* CustomPopupOptions通过自定义构建函数@Builder构建内容。

## 解决方案

选用CustomPopupOptions类型的参数，并依靠自定义构建函数@Builder构建内容。

将CustomPopupOptions中的width设为100%：

```ts
@Entry
@Component
struct PopupWidth {
  @State handlePopup: boolean = false;

  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Text('Custom Popup').fontSize(12);
    }.width(100).height(50).padding(5);
  }

  build() {
    Column({ space: 100 }) {
      Button('CustomPopupOptions中width设置为100%')
        .onClick(() => {
          this.handlePopup = !this.handlePopup;
        })
        .bindPopup(this.handlePopup, {
          width: '100%',
          builder: this.popupBuilder,
          arrowPointPosition: ArrowPointPosition.START, // 设置箭头的位置
          backgroundBlurStyle: BlurStyle.NONE, // 关闭气泡的模糊背景
          autoCancel: true,
        });
    }
    .margin({ top: 50 })
    .width('100%');
  }
}
```

## 常见FAQ

Q：使用Popup时，创建监听，会导致崩溃，是什么原因？

```ts
aboutToAppear(): void {
  this.listener.on('draw', () => {
    this.pageMainContentHeight = componentUtils.getRectangleById('pageMainContent').size.height // 单位是px
  })
}
```

A：使用Popup时要手动取消监听。

```ts
aboutToDisappear() {
  // Unregister callback before destruction
  this.listener.off('draw', () => {});
}
```
