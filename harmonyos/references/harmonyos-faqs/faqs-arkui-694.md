---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-694
title: 如何实现类似9-patch功能使图片指定区域不被拉伸
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现类似9-patch功能使图片指定区域不被拉伸
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:40+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:1e5f9bd40f3b86fad1508a4c7444d787414552a0424f4febb312b7cccdbfb007
---

## 问题现象

如何实现一个带箭头的聊天气泡背景，在拉伸时气泡四角和箭头都不变形，类似9-patch图。

## 背景知识

* 9-patch图：是一种特殊的PNG格式图片，分为伸缩区（下图灰色，可拉伸区域）和安全区（下图黑色，固定区域），当图片拉伸时，仅对可拉伸区域进行拉伸，固定区域保持原始尺寸与形态不变。

  | 水平拉伸（灰色为可拉伸区域） | 垂直拉伸（灰色为可拉伸区域） |
  | --- | --- |
  |  |  |
* Image组件的[resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)属性，可精准指定图片的可拉伸区域与固定区域，从而确保图片在不同尺寸的容器中都能保持良好的视觉效果。
  + [slice](../harmonyos-guides/arkts-implementing-image-resizable.md#使用slice拉伸图片)参数可以通过上、下、左、右四个偏移量定义四个角的区域为固定区域。
  + [lattice](../harmonyos-guides/arkts-implementing-image-resizable.md#使用lattice拉伸图片)参数支持将图像划分为矩形网格，同时处于偶数列和偶数行（从0开始计算）上的网格图像是固定的，不会被拉伸。
* 矩形网格对象通过[createImageLattice](../harmonyos-references/arkts-apis-graphics-drawing-lattice.md#createimagelattice12)方法创建，使用屏幕物理像素单位px。可以将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的。如果目标网格足够大，则这些固定网格以其原始大小进行绘制；如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。其余网格将进行缩放，来适应剩余的空间。

## 解决方案

* **方案一**、对于样式简单的气泡图，通过配置ResizableOptions类型的slice参数，设置统一的上下左右拉伸距离，即可实现类似9-patch图的拉伸效果。拉伸示例图如下（灰色为可拉伸区域）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/c5phfzeAQiaqT_q1dFohMg/zh-cn_image_0000002658794125.png "点击放大")

  1. 通过为slice参数指定上、下、左、右四个方向的像素偏移值，将一张图片划分为九宫格布局。
  2. 此时四个角的区域为固定区域，其余为可拉伸区域。

  **说明** 

  slice除了在resizable属性中使用，还支持在[backgroundImageResizable](../harmonyos-references/ts-universal-attributes-background.md#backgroundimageresizable12)属性中使用。

  ```ts
  @Entry
  @Component
  struct Page {
    build() {
      Column({ space: 20 }) {
        Stack() {
          // 加载原始图片资源（不改变大小，不进行任何拉伸处理）
          Image($r('app.media.bubble'))
            .objectFit(ImageFit.None);
          Column() {
            Text('初始图片')
              .fontColor(Color.White);
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
          .height('calc(100% - 10px)');
        }
        .height(100);

        // 第二个Stack：显示应用九宫格拉伸的图片
        Stack() {
          // 加载相同图片资源，应用九宫格拉伸规则
          Image($r('app.media.bubble'))
            .resizable({
              slice: {
                top: '80px',
                left: '30px',
                bottom: '30px',
                right: '80px'
              }
            })
            .width('100%')
            .height('100%');
          Column() {
            Text('实现四角+箭头不拉伸,其他内部文字可以撑开固定区域,比如下面这一段文字，可以把这个气泡撑开，圆角箭头无变形，来达到四角和箭头不拉伸')
              .fontColor(Color.White)
              .padding({
                left: 10,
                right: 15,
              });
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
          .height('100%');
        }
        .alignContent(Alignment.TopStart)
        .width(240)
        .height(120);
      }
      .margin(20);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/1bOX_eiDS0KqTqhtc3iWcA/zh-cn_image_0000002628554754.png "点击放大")
* **方案二**、针对结构复杂的气泡图，可以通过ResizableOptions类型的lattice参数，将图像划分为一个矩形网格来实现拉伸控制。拉伸示例图如下（灰色为可拉伸区域）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Qd62lLiyT9CGBD7nHkuANQ/zh-cn_image_0000002628394860.png "点击放大")

  1. 首先将原图划分为矩形网格，使无需发生形变的区域处于矩形网格的偶数行偶数列，并获取相应像素值。如上图所示，气泡图的水平方向包含左、中、右三个固定区域（图中黑色标注部分），因此水平上一共划分为五个区域。垂直方向上，则只有中间部分为可拉伸区域（图中灰色标注部分），因此垂直方向上共划分为三个区域。
  2. 创建DrawingLattice对象，并应用在Stack中作为背景图片的Image上。

  **说明** 

  lattice参数对同样可以设置图像拉伸的[backgroundImageResizable](../harmonyos-references/ts-universal-attributes-background.md#backgroundimageresizable12)接口不生效。

  ```ts
  import { drawing } from '@kit.ArkGraphics2D';

  @Entry
  @Component
  struct Index {
    // X轴分割线：定义图片在水平方向的4条切割线（单位：像素）,将图片分为5个区域
    xDivs: Array<number> = [79, 162, 198, 279];
    // Y轴分割线：定义垂直方向的2条切割线（单位：像素）,将图片分为2个区域
    yDivs: Array<number> = [78, 81];
    // 创建九宫格拉伸规则对象,水平分割线数组，垂直分割线数组，水平分区数(5区域)，垂直分区数(3区域)
    lattice: DrawingLattice =
      drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.xDivs.length, this.yDivs.length);

    build() {
      Column({ space: 20 }) {
        // 第一个Stack：显示原始图片
        Stack() {
          // 加载原始图片资源（不进行任何拉伸处理）
          Image($r('app.media.9patch'))
            .objectFit(ImageFit.None);
          Column() {
            Text('初始图片')
              .fontColor(Color.White);
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
          .height('calc(100% - 20px)');
        }
        .height(65);

        // 第二个Stack：显示应用九宫格拉伸的图片
        Stack() {
          // 加载相同图片资源，应用九宫格拉伸规则
          Image($r('app.media.9patch'))
          // 应用自定义拉伸规则
            .resizable({ lattice: this.lattice })
            .width('100%')
            .height('100%');
          Column() {
            Text('实现四角+底部中间箭头不拉伸呵呵')
              .fontColor(Color.White)
              .padding({
                left: 15,
                right: 15,
              });
          }
          .justifyContent(FlexAlign.Center)
          .width('100%')
          .height('calc(100% - 20px)');
        }
        .alignContent(Alignment.TopStart)
        .width(240)
        .height(65);
      }
      .margin(20);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/g4JGA8ciS3iXHbUxa_L94w/zh-cn_image_0000002658914079.png "点击放大")
