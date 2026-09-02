---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-847
title: 如何解决Image组件切换网络图片失败后占位图未显示的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Image组件切换网络图片失败后占位图未显示的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:42+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:26fd9e3ad1a832fb77a156f0b4261143697c790b02d00fec7eb5509808c83eff
---

## 问题现象

如下图，在切换网络图片时，若目标图片加载失败，界面不会更新为占位图，而是继续显示之前已加载成功的图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/06GZshKUQj2eS4thod2QqA/zh-cn_image_0000002658797917.png "点击放大")

问题代码如下：

```ts
@Entry
@Component
struct Page {
  @State imageUrl: string | Resource = '';

  build() {
    Column({ space: 30 }) {
      Image(this.imageUrl)
        .width(200)
        .height(200)
        // 本地资源自行替换
        .alt($r('app.media.startIcon'));
      Button('加载正常图片')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 网络路径需自行替换
          this.imageUrl = 'XXX.XXX.png';
        });
      Button('加载其他图片')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 网络路径需自行替换
          this.imageUrl = 'XXX.XXX.png';
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。

  **说明** 

  src由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。
* [alt](../harmonyos-references/ts-basic-components-image.md#alt)设置图片加载过程中显示的占位图，可以在图片内容尚未加载完成或加载失败时，临时显示的替代图像。
* 在Image组件上可以绑定[onError](../harmonyos-references/ts-basic-components-image.md#onerror9)事件，当图片加载异常时触发该回调。

## 解决方案

方案一：对于API22及以后的版本可以设置alt属性实现图片加载过程中和图片加载失败时显示指定图片，具体案例可以查看[使用alt属性实现设置加载失败中图片和加载失败时图片](../harmonyos-references/ts-basic-components-image.md#示例28使用alt属性设置加载过程中和加载失败时的占位图)。

方案二：对于API22以前的版本，由于该问题是由于Image组件在成功加载当前图片后，若将其路径更新为无效值（包括空值），组件不会自动触发重新渲染，导致界面仍保留已加载的图片，占位图因此无法显示。可以参考以下方案达到预期的效果：

1. 为Image组件添加onError事件回调，用于监听图片加载失败的情况。
2. 在onError回调函数中，将图片源替换为占位图的路径，从而实现显示默认占位图的效果。

参考代码如下：

```ts
@Entry
@Component
struct Index {
  @State imageUrl: string | Resource = '';

  build() {
    Column({ space: 30 }) {
      Image(this.imageUrl)
        .width(200)
        .height(200)
        .onError((err: ImageError) => {
          console.error(`${err.message}`);
          console.error(`${err.error?.code}`);
          // 本地资源自行替换
          this.imageUrl = $r('app.media.startIcon');
        });
      Button('加载正常图片')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 网络路径需自行替换
          this.imageUrl = 'XXX.XXX.png';
        });
      Button('加载失败显示占位图')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 网络路径需自行替换
          this.imageUrl = 'XXX.XXX.png';
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XNESviYvQFeiuZbba4D-Wg/zh-cn_image_0000002628558548.png "点击放大")
