---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1327
title: 如何通过拖拽拉起半模态弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何通过拖拽拉起半模态弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8d3945ebae15fbe9e57a2b22a47c708bfd76c3df25629a10c6ea965a81b91ee
---

## 问题现象

如何通过拖拽方式拉起半模态弹窗？例如通过上拉将半模态弹窗引出。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/LmkBtuUjT8er2owxDL9k7Q/zh-cn_image_0000002658958967.png "点击放大")

## 背景知识

* [半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)：通过[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性为组件绑定半模态页面，在组件插入时可通过设置自定义或默认的内置高度确定半模态大小，点击后显示模态页面。
* 在[绑定手势方法](../harmonyos-references/ts-gesture-settings.md)中，[gesture](../harmonyos-references/ts-gesture-settings.md#gesture)属性能够给组件绑定手势，手势识别成功后可以通过事件回调通知组件。还可以通过[组合手势](../harmonyos-references/ts-combined-gestures.md)的方法将多种手势组合为复合手势，支持顺序识别、并发识别和互斥识别。

## 解决方案

通过[draggable](../harmonyos-references/ts-universal-attributes-drag-drop.md#draggable)将文本组件设置为可拖动的。使用bindSheet将文本组件与一个半模态窗口Sheet绑定，并且使用gesture为文本组件添加手势监听，当用户拖动文本组件时，触发手势的更新事件，将bindSheet的属性isShow设置为true，从而显示半模态弹窗，实现拖拽拉起半模态弹窗。

```ts
@Entry
@Component
struct SheetTransitionExample {
  @State numbers: number[] = [];
  @State isShow: boolean = false;
  @State sheetHeight: number = 300;

  aboutToAppear() {
    for (let i = 1; i <= 111; i++) {
      this.numbers.push(i);
    }
  }

  // 使用@Builder装饰器定义一个可复用的UI构建器myBuilder。
  @Builder
  myBuilder() {
    Column() {
      List() {
        // 使用ForEach遍历numbers数组生成列表项。
        ForEach(this.numbers, (item: string) => {
          ListItem() {
            Text(item.toString())
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .size({ height: 100, width: '100%' });
          }.margin(10)
          .borderRadius(10)
          .backgroundColor('#F1F3F5')
        }, (item: string) => item)
          .onMove((from: number, to: number) => {
            let tmp = this.numbers.splice(from, 1);
            this.numbers.splice(to, 0, tmp[0]);
          });
      }
      .lanes({ minLength: 80, maxLength: 400 })
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .backgroundColor(Color.White)
    .padding({ top: 5 });
  }

  build() {
    Column() {
      Text('向上拖')
        .draggable(true) // 允许该文本被拖动。
        .fontSize(20)
        .margin(10)
          // 将文本与Sheet绑定，点击或拖动可触发显示myBuilder内容。
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: this.sheetHeight,
          backgroundColor: '#F1F3F5',
          blurStyle: BlurStyle.Thick,
          showClose: true,
          title: { title: 'title', subtitle: 'subtitle' },
        })
          // 添加手势识别器，监听拖动手势。
        .gesture(
          GestureGroup(GestureMode.Sequence, // 设置手势模式为顺序执行。
            PanGesture({ fingers: 1, direction: null, distance: 0 })
              .onActionUpdate((event: GestureEvent) => {
                this.isShow = true;
                console.info('输出：', event.offsetY);
                this.sheetHeight = Math.abs(event.offsetY);
              })
          )
        );
    }
    .justifyContent(FlexAlign.End)
    .width('100%')
    .height('100%');
  }
}
```

## 总结

本文通过给可拖动组件绑定组合手势来控制半模态弹窗的显隐，实现通过拖拽拉起半模态弹窗的效果。
