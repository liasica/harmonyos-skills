---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1211
title: 滚动组件是否支持滚动时隐藏键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 滚动组件是否支持滚动时隐藏键盘
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:18+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:f253f67a66077a90abf1b23267e5789e631baea4d396f79dfdd61ad6260986c7
---

## 问题现象

List组件里面嵌套TextInput组件，如何实现滚动时隐藏键盘的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/R3REJkPsSBKWafA7NKl6bw/zh-cn_image_0000002628593592.png "点击放大")

## 背景知识

* [focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)：设置当前组件是否可以获焦。
* [onScrollStart](../harmonyos-references/ts-container-list.md#onscrollstart9)：列表滑动开始时触发。手指拖动列表或列表的滚动条触发的滑动开始时，会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画开始时会触发该事件。
* [onScrollStop](../harmonyos-references/ts-container-list.md#onscrollstop)：列表滑动停止时触发。手指拖动列表或列表的滚动条触发的滑动，手离开屏幕并且滑动停止时会触发该事件。使用Scroller滑动控制器触发的带动画的滑动，动画停止会触发该事件。

## 解决方案

通过设置focusable的属性值来控制键盘的显示和隐藏，当List组件开始滚动时，设置focusable的属性值为false隐藏键盘。当List组件停止滚动时，设置focusable的属性值为true点击时显示键盘。

```ts
@Entry
@Component
struct ListExampleDemo {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
  controller: TextInputController = new TextInputController();
  @State isFocusable: boolean = true;

  build() {
    Column() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {

            TextInput({ text: item + '', controller: this.controller })
              .fontSize(16)
              .backgroundColor(0xFFFFFF)
              .focusable(this.isFocusable)
              .onClick(() => {
                this.isFocusable = true;
              });
          };
        }, (item: string) => item);
      }
      .listDirection(Axis.Vertical) // 排列方向
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(EdgeEffect.Spring) // 边缘效果设置为Spring
      .onScrollStart(() => {
        // List组件开始滚动时，将focusable设置为false
        this.isFocusable = false;
      })
      .onScrollStop(() => {
        // List组件停止滚动时，将focusable设置为true
        this.isFocusable = true;
      })
      .width('90%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#f1f3f5')
    .padding({ top: 5 });
  }
}
```
