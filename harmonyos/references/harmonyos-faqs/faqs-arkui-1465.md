---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1465
title: 如何实现根据屏幕宽度自适应列数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现根据屏幕宽度自适应列数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:021db067ef7839bffca31b3a0e6f58824e36fa6fdb757bcb305104a3be749d46
---

## 问题现象

如何实现多尺寸多设备的动态布局，比如根据屏幕大小适配不同展示列数？

## 背景知识

* [栅格容器组件](../harmonyos-references/ts-container-gridrow.md)(GridRow)仅可以和[栅格子组件](../harmonyos-references/ts-container-gridcol.md)(GridCol)在栅格布局场景中使用。栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题，保证不同设备上各个模块的布局一致性。
* 可通过GridCol的[span](../harmonyos-references/ts-container-gridcol.md#span)属性设置占用列数，xs、sm、md、lg分别对应不同栅格大小设备上栅格容器组件的栅格列数。

## 解决方案

可以通过栅格布局实现对不同屏幕大小的适配，具体实现方式及示例代码如下：

1. 配置栅格容器组件(GridRow)的columns参数，即设定栅格布局的列数，默认API version 20之前为12列。
2. 配置栅格子组件(GridCol)的span参数，设定不同栅格大小设备对应的栅格列数，可根据屏幕越大对应显示的列数越多来设定xs、sm、md、lg的值。
3. 通过[onScrollStop](../harmonyos-references/ts-container-scroll.md#onscrollstop9)回调，触发加载更多数据。

```ts
let tmpData: number[] =
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,];

@Entry
@Component
struct GridRowAdaptiveColumnCount {
  @State data: number[] = tmpData;
  scroller: Scroller = new Scroller();

  build() {
    Column({ space: 5 }) {
      Scroll(this.scroller) {
        GridRow({
          columns: 12,
          gutter: 5,
        }) {
          ForEach(this.data, (item: number) => {
            GridCol({
              span: {
                xs: 12,
                sm: 6,
                md: 3,
                lg: 2
              }
            }) {
              Row() {
                Text(item.toString())
                  .fontSize(20)
                  .fontWeight(400)
                  .fontColor(Color.White)
                  .textAlign(TextAlign.Center)
                  .width('100%')
                  .height('100%');
              }.width('100%').height(80).backgroundColor('#0D5AF5');
            };
          });
        }.margin({ top: 5 })
        .onBreakpointChange((breakpoint: string) => {
          console.info(breakpoint);
        })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info(`onAreaChange, oldValue: ${oldValue}, newValue: ${newValue}`);
        });
      }
      .backgroundColor('#F1F3F5')
      .height('100%')
      .scrollSnap({
        snapAlign: ScrollSnapAlign.START,
        snapPagination: 400,
        enableSnapToStart: true,
        enableSnapToEnd: true
      })
      .onScrollStop(() => {
        console.info('Scroll Stop');
        tmpData = tmpData.map(item => item + 30);
        this.data = this.data.concat(tmpData);
        console.info(String(this.data));
      });
    }.width('100%').height('100%');
  }
}
```
