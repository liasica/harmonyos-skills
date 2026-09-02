---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1282
title: 实现手指按下切换图片，松手换回原图
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现手指按下切换图片，松手换回原图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d1bdb0531657f94c0ed49275e04b5c1ff6e8387ff9036a665d8a15c2f322de5
---

## 问题现象

在应用开发中，存在以下交互场景：一个Image组件默认显示图片A，当用户手指按下（触摸）该图片时，它需要立即切换为显示图片B；当用户手指松开（结束触摸）时，图片应恢复显示为图片A。这常用于实现按钮或图标的按压态视觉反馈。

## 背景知识

* [Image组件](../harmonyos-references/ts-basic-components-image.md)：常用于显示图片的基础组件，其属性src用于设置图片的资源路径。
* [onTouch事件](../harmonyos-references/ts-universal-events-touch.md#ontouch)：组件支持的通用触摸事件回调。当用户手指在组件上按下、移动或抬起时，会触发此回调，并返回一个TouchEvent对象。该TouchEvent对象的[type属性](../harmonyos-references/ts-universal-events-touch.md#touchevent对象说明)用于标识触摸事件类型，常见类型包括TouchType.Down（按下）、TouchType.Up（抬起）、TouchType.Move（移动）和TouchType.Cancel（事件取消）。

## 解决方案

使用[@State](../harmonyos-guides/arkts-state.md)装饰控制Image组件src属性的状态变量。然后，在该Image上设置onTouch事件监听。当触摸事件触发时：

* 在TouchType.Down时，将src切换至按压态图片。
* 在TouchType.Up或TouchType.Cancel时，将src恢复为默认图片。

状态变量变化后，会自动触发UI更新，从而实现“按下换图，松手恢复”的效果。

示例代码如下：

```ts
@Entry
@Component
struct ImageClickDemo {
  // 图片资源需自行替换
  private imageOne: Resource = $r('app.media.img1');
  private imageTwo: Resource = $r('app.media.img2');
  @State src: Resource = this.imageOne;
  @State eventType: string = '事件';

  build() {
    Column() {
      Text(this.eventType)
        .margin(20);

      Image(this.src)
        .width('80%')
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.eventType = 'Down';
            this.src = this.imageTwo;
          }
          if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            this.eventType = 'Up or Cancel';
            this.src = this.imageOne;
          }
        });
    }.width('100%').height('100%');
  }
}
```
