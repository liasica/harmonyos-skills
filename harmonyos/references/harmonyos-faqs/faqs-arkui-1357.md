---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1357
title: 使用栅格布局，span和offset的具体数值对应关系
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用栅格布局，span和offset的具体数值对应关系
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e7ac749a9b5d75f52e20a12376603d490c1a499f92148650af12db6036943639
---

## 问题现象

栅格布局中span和offset的对应关系是怎么样的，以设置span：8，offset：3为例进行说明。

## 背景知识

* [栅格布局](../harmonyos-guides/arkts-layout-development-grid-layout.md)是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。
* [span](../harmonyos-references/ts-container-gridcol.md#span)：设置占用列数。span为0，意味着该元素不参与布局计算，即不会被渲染。
* [gridColOffset](../harmonyos-references/ts-container-gridcol.md#gridcoloffset)：设置相对于前一个栅格子组件偏移的列数。
* 栅格子组件仅能通过span、offset计算子组件位置与大小。多个子组件span超过规定列数时自动换行。
* 单个元素span大小超过最大列数时后台默认span为最大column数。
* 新一行的offset加上子组件的span超过总列数时，将下一个子组件在新的一行放置。
* 栅格行布局容器默认列数为12。

## 解决方案

已知默认列数为12，span为占用列数，offset为距离前一个的列数，以span：8，offset：3为例可知：

* 第一行，左边offset为3占3格，item的span为8占8格，此时右边剩一格。
* 第二行，offset为3，第一行有一格，所以第二行空两格，item占8格，此时右边剩两格。
* 第三行，offset为3，第二行有两格，所以第三行空一格，item占8格，此时右边剩三格。
* 第四行，offset为3，第三行有三格，所以第四行空零格，item占8格，此时右边剩四格。
* 第五行，offset为3，第四行有四格，但是由于新一行的offset加上子组件的span超过总列数时，将下一个子组件在新的一行放置。所以item在新一行左边零格，右边剩四格。

代码示例如下：

```ts
@Entry
@Component
struct GridRowExample {
  @State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink];
  @State currentBp: string = 'unknown';

  build() {
    Column() {
      GridRow({
        // 默认个数为12
        columns: 12,
        gutter: { x: 5, y: 10 },
        breakpoints: {
          value: ['400vp', '600vp', '800vp'],
          reference: BreakpointsReference.WindowSize
        },
        direction: GridRowDirection.Row
      }) {
        ForEach(this.bgColors, (color: Color) => {
          // 设置span为8，offset为3
          GridCol({ span: 8, offset: 3, order: 0 }) {
            Row().width('100%').height('20vp');
          }.borderColor(color).borderWidth(2);
        });
      }.width('100%').height('100%')
      .onBreakpointChange((breakpoint) => {
        this.currentBp = breakpoint;
      });
    }.width('80%').margin({ left: 10, top: 5, bottom: 5 }).height(200)
    .border({ color: '#880606', width: 2 });
  }
}
```
