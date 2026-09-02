---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1215
title: 实现Grid组件中特定GridItem的点击效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Grid组件中特定GridItem的点击效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:39e55e11ff18e3fcadab983af36b649c122e9ea8ce81ed732bf201a39f58aef1
---

## 问题现象

为Grid组件添加点击事件以实现缩放动画效果时，如何实现只点击特定GridItem项的功能？

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)是HarmonyOS提供的一种网格容器，由行和列分割的单元格所组成，通过指定项目所在的单元格做出各种各样的布局。网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要的自适应布局。
* [scale](../harmonyos-references/ts-components-canvas-common-method.md#scale)属性用于设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

## 解决方案

1. GridLayoutOptions是Grid组件的布局选项，在该对象中设置onGetRectByIndex方法用以初始化整个Grid组件。

   ```ts
   layoutOptions: GridLayoutOptions = {
     regularSize: [1, 1],
     onGetRectByIndex: (index: number) => {
       if (index === 0) {
         return [0, 0, 1, 1];
       } else if (index === 1) {
         return [0, 1, 2, 2];
       } else if (index === 2) {
         return [0, 3, 3, 3];
       } else if (index === 3) {
         return [3, 0, 3, 3];
       } else if (index === 4) {
         return [4, 3, 2, 2];
       } else {
         return [5, 5, 1, 1];
       }
     }
   };
   ```
2. 使用foreach方法依据上一步的设置的值循环渲染出每个GridItem组件，并为组件添加onclick方法，点击特定的GridItem组件时，在scale方法中将对应的GridItem组件缩放比例调整为0.5。

   ```ts
   ForEach(this.numberT, (day: string, index: number) => {
     GridItem() {
       Text(day)
         .fontSize(16)
         .backgroundColor(0xF9CF93)
         .width('100%')
         .height('100%')
         .textAlign(TextAlign.Center);
     }
     .scale(this.currentGridItem === index ? {
       x: 0.5,
       y: 0.5,
       z: 0,
     } : null)
     .onClick(() => {
       this.currentGridItem = index;
     })
     .height('100%')
     .width('100%');
   }, (day: string) => day);
   ```

完整代码如下所示：

```ts
@Entry
@Component
struct GridClick {
  @State numberT: String[] = ['0', '1', '2', '3', '4', '5'];
  @State currentGridItem: number | null = null;
  layoutOptions: GridLayoutOptions = {
    regularSize: [1, 1],
    onGetRectByIndex: (index: number) => {
      if (index === 0) {
        return [0, 0, 1, 1];
      } else if (index === 1) {
        return [0, 1, 2, 2];
      } else if (index === 2) {
        return [0, 3, 3, 3];
      } else if (index === 3) {
        return [3, 0, 3, 3];
      } else if (index === 4) {
        return [4, 3, 2, 2];
      } else {
        return [5, 5, 1, 1];
      }
    }
  };

  build() {
    Column({ space: 5 }) {
      Grid(undefined, this.layoutOptions) {
        ForEach(this.numberT, (day: string, index: number) => {
          GridItem() {
            Text(day)
              .fontSize(16)
              .backgroundColor(0xF9CF93)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .scale(this.currentGridItem === index ? {
            x: 0.5,
            y: 0.5,
            z: 0,
          } : null)
          .onClick(() => {
            this.currentGridItem = index;
          })
          .height('100%')
          .width('100%');
        }, (day: string) => day);
      }
      .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('90%')
      .backgroundColor(0xFAEEE0)
      .height(300);
    }
    .width('100%')
    .margin({ top: 5 });
  }
}
```

运行效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/75i5ZdyGReGBTygk03_dRw/zh-cn_image_0000002628593594.png "点击放大")
