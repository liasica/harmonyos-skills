---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-815
title: 深浅色模式切换页面渲染失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 深浅色模式切换页面渲染失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ad888385ef1da0bc2c1e9f1e068bd9fdb48b7d2d0d60557344e80c089952407
---

## 问题现象

在Tabs的tabBar中使用Canvas，当深浅色模式切换后，tabBar中的内容消失。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/yXcUJ70tQ32tXdzO-Pq5Og/zh-cn_image_0000002628397896.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/_7hP-kzxQcSZKZW8-Y8WVg/zh-cn_image_0000002658797169.gif "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)对象和[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* 组件树指的是用户界面（UI）的组件层次结构。在ArkTS开发环境中，UI组件是组成应用界面的基本元素，它们按照一定的层次关系组织在一起，形成了组件树。组件树的根节点通常是应用的主窗口，而子节点则是各种UI组件，如按钮、文本框、图像等。

## 解决方案

出现上述问题是因为在切换深浅色模式时，Canvas组件会被销毁并重新创建，此时在tabBar中使用的Canvas组件会在短时间内重新渲染并重新加载到组件树中，从而使得CanvasRenderingContext2D被旧的Canvas组件绑定，而新的Canvas组件无法正确绘制内容。为了解决上述问题，可以将CanvasRenderingContext2D和Canvas组件封装为一个自定义组件，以避免这种情况。

```ts
interface ITabs {
  name: string;
  currentName?: string;
  previousName?: string;
  canvasRenderingContext: CanvasRenderingContext2D;
}

const tabList: ITabs[] = [
  { name: 'home', canvasRenderingContext: new CanvasRenderingContext2D() },
  {
    name: 'category',
    canvasRenderingContext: new CanvasRenderingContext2D()
  },
  { name: 'cart', canvasRenderingContext: new CanvasRenderingContext2D() },
  { name: 'my', canvasRenderingContext: new CanvasRenderingContext2D() },
];

@Component
struct TabBuilderLottie {
  @Prop index: number;

  build() {
    Canvas(tabList[this.index].canvasRenderingContext)
      .onReady(() => {
        let path = new Path2D();
        path.moveTo(150, 50);
        path.lineTo(50, 150);
        path.lineTo(100, 250);
        path.lineTo(200, 250);
        path.lineTo(250, 150);
        path.closePath();
        // 设定填充色为蓝色
        tabList[this.index].canvasRenderingContext.fillStyle = '#0097D4';
        // 使用填充的方式，将Path2D描述的五边形绘制在canvas组件内部
        tabList[this.index].canvasRenderingContext.fill(path);
        tabList[this.index].canvasRenderingContext.fillStyle = '#0097D4';
        // 以(50,50)为左上顶点，画一个宽高200的矩形
        tabList[this.index].canvasRenderingContext.fillRect(50, 50, 200, 200);
        // 以(70,70)为左上顶点，清除宽150高100的区域
        tabList[this.index].canvasRenderingContext.clearRect(70, 70, 150, 100);
        tabList[this.index].canvasRenderingContext.restore();
      });
  }
}

@Entry
@Component
struct TabBuilderLottiePage {
  @State tabs: ITabs[] = tabList;

  build() {
    Tabs({ barPosition: BarPosition.End }) {
      ForEach(this.tabs, (item: ITabs, index: number) => {
        TabContent() {
          Text(item.name);
        }
        .tabBar(this.TabBuilderLottie(index));
      });
    }
    .width('100%')
    .height('100%')
    .barMode(BarMode.Fixed)
    .barHeight(60)
    .fadingEdge(false)
    .scrollable(false);
  }

  @Builder
  TabBuilderLottie(index: number) {
    TabBuilderLottie({ index: index });
  }
}
```
