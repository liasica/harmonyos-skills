---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-25
title: 平板横屏显示时，页面滑动区域过小
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板横屏显示时，页面滑动区域过小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bff6ff66e40f1ee973afaa6767dfe15211351184e36e72bde72b797117f88d2a
---

## 问题现象

应用页面上下内容固定，中间区域可滑动，在平板横屏显示时，上下固定内容部分高度变高，中间滑动区域被压缩成一小行，无法流畅滑动。

## 背景知识

[Scroll](../harmonyos-references/ts-container-scroll.md)：可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。

## 问题定位

1. 检查代码中可滑动区域高度是否设置为固定值，示例如下：

   ```ts
   Scroll(this.scroller) {
     Column() {
       ForEach(this.arr, (item: number) => {
         Text("ListItem" + item)
           .width("100%")
           .height(150)
           .borderRadius(15)
           .fontSize(16)
           .textAlign(TextAlign.Center)
           .backgroundColor(Color.White)
       }, (item: string) => item)
     }
     .width('100%')
   }
   .width("100%")
   .height(200)
   ```
2. 检查代码中页面上下固定区域高度是否设置为百分比。

## 分析结论

应用可滑动页面只适配了手机大小，当应用在平板横屏打开时，窗口会变大，上下部分高度变高，可滑动区域高度不变，导致页面滑动区域被压缩，滑动体验不流畅。

## 修改建议

修改滑动区域高度值，也设置为百分比占比，在平板上时可以同比放大。

```ts
@Entry
@Component
struct ScrollPage3432 {
  private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  scroller: Scroller = new Scroller();

  build() {
    Flex() {
      Column() {
        Text("Scroll Area")
          .width("100%")
          .height('20%')
          .backgroundColor('#D1D1D6')
          .fontSize(16)
          .textAlign(TextAlign.Center);

        Scroll(this.scroller) {
          Column() {
            ForEach(this.arr, (item: number) => {
              Text("ListItem" + item)
                .width("100%")
                .height(150)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .backgroundColor(Color.White);
            }, (item: string) => item);
          }
          .width('100%');
        }
        .width("100%")
        // 高度设置为百分比
        .height('60%');

        Text("Scroll Area")
          .width("100%")
          .height('20%')
          .backgroundColor('#D1D1D6')
          .fontSize(16)
          .textAlign(TextAlign.Center);
      };
    }
    .width("100%").height("100%");
  }
}
```
