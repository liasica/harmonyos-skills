---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1108
title: 组件如何实现带三角形指示箭头的边框
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 组件如何实现带三角形指示箭头的边框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d4310ed455d0891b9b32c864841908814c0ac7c28a132ef4791a7625a42f560e
---

## 问题现象

如何实现带三角形指示箭头的容器边框。效果见下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/TNRvE4YFSKOctsCHOT0IUw/zh-cn_image_0000002658806745.png "点击放大")

## 背景知识

* [Stack](../harmonyos-guides/arkts-layout-development-stack-layout.md)：层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过Stack容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [Column](../harmonyos-references/ts-container-column.md)：沿垂直方向布局的容器。
* [气泡提示（Popup）](../harmonyos-guides/arkts-popup-and-menu-components-popup.md)：Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

## 解决方案

方案一、可以使用CustomPopupOptions的builder创建自定义气泡，@Builder中可以放自定义的内容。具体参考[自定义气泡](../harmonyos-guides/arkts-popup-and-menu-components-popup.md#自定义气泡)。

方案二、凸起的一部分可以理解成使用一个容器来覆盖底部容器，再对边框和背景做相应处理来达到需要的效果，子元素的堆叠可以使用Stack布局实现，具体实现方式如下：

1. 使用Stack布局将箭头容器覆盖在对话框主体上，
2. 通过borderWidth仅保留左上两边，形成直角边框，
3. 通过45度旋转使直角边框变成对角方向，
4. 通过负边距margin实现边框覆盖粘连效果（一般情况下top值为宽高的一半，但是要注意拼接图形的边框宽度会略微调整，边框越宽，为实现粘连效果所需的负边距绝对值就越小。在实际开发中，需要根据项目中使用的具体边框宽度来动态调整）。

代码如下：

```ts
@Entry
@Component
struct Page {
  build() {
    Column() {
      Stack({ alignContent: Alignment.TopStart }) {
        Column() {
        }
        .width(300)
        .height(75)
        .borderWidth(3)
        .borderRadius(15);

        Column() {
        }
        .width(20)
        .height(20)
        .borderWidth({ left: 3, top: 3 })
        .backgroundColor(Color.White)
        // 对组件进行平移和旋转
        .margin({ top: -9, left: 40 })
        .rotate({
          x: 0,
          y: 0,
          z: 1,
          centerX: '50%',
          centerY: '50%',
          angle: 45
        });
      };
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
