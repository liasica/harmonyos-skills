---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1381
title: 拖拽图片列表中的图片时如何禁止底部列表跟随滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 拖拽图片列表中的图片时如何禁止底部列表跟随滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05c74f7a748fe3a78004536cc504c803d79130ba5029551d2ccd32669ca7d81c
---

## 问题现象

有多张图片的列表中，长按拖拽图片上下移动时，底部的列表会跟随滑动，如何禁止列表跟随滑动？

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [onWillScroll](../harmonyos-references/ts-container-scrollable-common.md#onwillscroll12)：滚动事件回调，滚动组件滚动前触发。
* [onDragStart](../harmonyos-references/ts-universal-events-drag-drop.md#ondragstart)：第一次拖拽此事件绑定的组件时，长按时间>=500ms，然后手指移动距离>=10vp，触发回调。
* [onDragEnd](../harmonyos-references/ts-universal-events-drag-drop.md#ondragend10)：绑定此事件的组件触发的拖拽结束后，触发回调。

## 解决方案

解决思路：拖拽图片时，拖拽手势触发了列表的滚动事件。想要列表保持静止，可以考虑在列表滚动之前的onWillScroll事件中增加判断，如果是拖拽手势，则设置列表接下来滚动的偏移量为0，否则不做处理，响应正常的滚动事件。

具体解决方案如下：

1. 设置一个flag，初始值为false；
2. 在onPageShow生命周期中将flag设置为false，并设置沉浸式效果；
3. 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true，onDragEnd方法（图片拖拽结束后）将flag改为false；
4. List的onWillScroll方法（滚动组件滚动之前）中，如果flag为false，则不做任何处理；如果flag为true，则返回{offsetRemain: 0}，表示接下来滚动的偏移量为0；

完整示例代码如下：

```screen
import { UIContext, window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct DragPictures {
  // 设置一个flag，初始值为false
  @State flag: boolean = false;
  private scroller: Scroller = new Scroller();
  @State x: number = 0;
  @State y: number = 0;

  // 显示页面时flag设置为false，并设置沉浸式效果
  onPageShow(): void {
    this.flag = false;
    window.getLastWindow(new UIContext().getHostContext() as common.UIAbilityContext, (err, win) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      win.setWindowLayoutFullScreen(true);
    });
  }

  // 隐藏页面时解除沉浸式效果
  onPageHide(): void {
    window.getLastWindow(new UIContext().getHostContext() as common.UIAbilityContext, (err, win) => {
      const errCode: number = err.code;
      if (errCode) {
        console.error(`Failed to obtain the window. Cause code: ${err.code}, message: ${err.message}`);
        return;
      }
      win.setWindowLayoutFullScreen(false);
    });
  }

  build() {
    RelativeContainer() {
      List({ scroller: this.scroller }) {
        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.fig1'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
              // 每个ListItem图片组件的onDragEnd方法（图片拖拽结束后）将flag改为false
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.fig2'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.fig3'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.fig4'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.icon'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.startIcon'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.slider'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };

        ListItem() {
          // 显示的图片资源，开发者可根据真实场景进行替换
          Image($r('app.media.sliderBackground'))
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .width(200)
            .height(200)
            .draggable(true)
            .margin({ top: 20 })
              // 每个ListItem图片组件的onDragStart方法（开始拖拽图片）将flag改为true
            .onDragStart(() => {
              console.info('onDragStart');
              this.flag = true;
              this.x = this.scroller.currentOffset().xOffset;
              this.y = this.scroller.currentOffset().yOffset;
            })
            .onDragEnd(() => {
              console.info('onDragEnd');
              this.flag = false;
            });
        };
      }
      .backgroundColor('#FFF1F3F5')
      .alignListItem(ListItemAlign.Center)
      // List的onWillScroll方法（滚动组件滚动之前）中，如果flag为false，则不做任何处理；如果flag为true，则返回{offsetRemain: 0}，表示接下来滚动的偏移量为0
      .onWillScroll(() => {
        if (this.flag) {
          return { offsetRemain: 0 };
        }
        return;
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
