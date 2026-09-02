---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-674
title: 如何根据单行Item数量动态调整布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何根据单行Item数量动态调整布局
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4508a0d9751a26e397892af8cf6fda0de51f27ef367917b544716518c53efada
---

## 问题现象

如何使用Grid组件实现布局只有一行，宽度固定，横向排列，当Item数量小于5时，Item宽度按照数量均分，当Item数量大于5时指定宽度且横向可以滚动的效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/I4wuIlR5Ss6BzPr1j81tcw/zh-cn_image_0000002658913891.gif "点击放大")

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。
* [rowsTemplate](../harmonyos-references/ts-container-grid.md#rowstemplate)：设置当前网格布局行的数量、固定行高或最小行高值，不设置时默认1行。
* [columnsGap](../harmonyos-references/ts-container-grid.md#columnsgap)：设置列与列的间距。设置为小于0的值时，按默认值显示。
* [display.getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)：获取当前默认的[display](../harmonyos-references/js-apis-display.md#display)对象。
* [px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)：将px单位的数值转换为以vp为单位的数值。

## 解决方案

获取当前屏幕的宽度，当Item数量大于5时，Item宽度指定为100vp，当Item数量小于5时，动态设置Item宽度。

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct HorizontalIndex {
  @State screenWidth: number = 0;
  @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7];

  aboutToAppear(): void {
    // 使用display.getDefaultDisplaySync()方法获取当前屏幕宽度
    this.screenWidth = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
  }

  getItemWidth(): number {
    // 当Item数量大于5时，宽度指定为100
    if (this.arr.length > 5) {
      return 100;
    } else {
      // 当Item数量小于5时，Item宽度按照数量均分
      return (this.screenWidth - (this.arr.length - 1) * 10) / this.arr.length;
    }
  }

  build() {
    Column() {
      Grid() {
        ForEach(this.arr, (num: number) => {
          GridItem() {
            Column() {
              Text(`${num}`)
                .fontColor(Color.White);
            }
            .justifyContent(FlexAlign.Center)
            .alignItems(HorizontalAlign.Center)
            .backgroundColor(Color.Blue)
            .width(this.getItemWidth())
            .height(100);
          };
        });
      }
      // 设置当前网格布局行的数量为1
      .rowsTemplate('1fr')
      .height(100)
      // 设置列与列的间距为10
      .columnsGap(10)
      .width('100%')
      .backgroundColor('#fafafa');

      Button('数量改变')
        .margin({ top: 20 })
        .onClick(() => {
          this.arr = [0, 1, 2, 3,];
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
