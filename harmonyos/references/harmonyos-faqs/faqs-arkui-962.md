---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-962
title: 如何在同一个坐标系统里绘制多个Polygon
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在同一个坐标系统里绘制多个Polygon
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30b1a1ce65cd2c0bbd39f32de05864742513ffa36627e300ef37192c3fab865e
---

## 问题现象

在普通的容器中例如Column容器，多个Polygon组件只会上下排列，如何在同一个坐标系统里绘制多个Polygon？并且可以动态添加points？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/82KigigjRfeRNIUQWioNig/zh-cn_image_0000002628561582.gif "点击放大")

## 背景知识

* [Polygon](../harmonyos-references/ts-drawing-components-polygon.md)是HarmonyOS提供的多边形绘制组件，利用该组件可以绘制多边形背景，多边形图案等。
* [Shape](../harmonyos-references/ts-drawing-components-shape.md)绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。

## 解决方案

在Shape组件中绘制多个Polygon组件，同时指定Shape组件的视口[viewPort](../harmonyos-references/ts-drawing-components-shape.md#viewport)。viewPort的区域范围，就是多个Polygon组件的同一坐标系。Polygon的points属性接收类型为number的二维数组，每个数组元素表示一个坐标点。可通过动态更新points数组，实现点的增删与实时渲染。

完整示例参考如下：

```ts
@Entry
@Component
struct PolygonDemo {
  @State points: number[][] = [];

  aboutToAppear(): void {
    let p1: number[] = [10, 10];
    this.points.push(p1);

    let p2: number[] = [100, 10];
    this.points.push(p2);

    let p3: number[] = [100, 110];
    this.points.push(p3);

    let p4: number[] = [20, 100];
    this.points.push(p4);
  }

  build() {
    Column() {
      Shape() {
        Polygon({ width: 100, height: 100 })
          .points([[10, 10], [220, 30], [180, 260], [10, 130]]) // 画一个四边形
          .stroke('#EE6F20')
          .fillOpacity(0)
          .strokeWidth(2)
        Polygon({ width: 100, height: 100 })
          .points(this.points) // 默认画一个三角形，可通过动态更新points数组，实现点的增删与实时渲染
          .stroke('#0A59F7')
          .fillOpacity(0)
          .strokeWidth(2)
      }
      .backgroundColor('#ffe7e6e6')
      .viewPort({
        // viewport的区域范围，就是Shape的子组件同一坐标范围。
        x: 0,
        y: 0,
        width: 280,
        height: 400
      })

      Button('添加point')
        .margin({ top: 10 })
        .onClick(() => {
          let p5: number[] = [80, 140];
          this.points.push(p5);
        })
      Button('移除P3')
        .margin({ top: 10, bottom: 10 })
        .onClick(() => {
          this.points.splice(2, 1);
        })

    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```
