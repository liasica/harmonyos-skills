---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1306
title: 如何适配内部有图案并且需要根据图案布局的.9图背景
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何适配内部有图案并且需要根据图案布局的.9图背景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4d8de17f34e003467db3c085b74d418f65144dffc2f43ea7cc65876791893079
---

## 问题现象

有如下图所示的背景，需要在斜杠两侧各排布文字，并且在不同设备上，当该框格宽度变宽时，斜杠的位置不变，布局与之前相同。其他平台是通过.9图实现，HarmonyOS没有.9图，要如何实现该功能？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/mMZpteBjR96daXJI0Wu3Qg/zh-cn_image_0000002628599012.png "点击放大")

## 背景知识

* .9图是一种特殊的PNG图像，用于根据内容大小自动拉伸背景或边框。它能定义哪些区域可以拉伸、内容如何填充。一张.9图会被系统划分为一个3×3的九宫格：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Z9pP-idvSUeuoVij49j0hw/zh-cn_image_0000002628758910.png)

  其中四角TL/TR/BL/BR不会被拉伸，上下边T/B只会被水平拉伸，左右边L/R只会被垂直拉伸，中心C可以随意拉伸。
* 通用属性[backgroundImageResizable](../harmonyos-references/ts-universal-attributes-background.md#backgroundimageresizable12)以及Image的[resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)属性支持设置图像在拉伸时可调整大小，其参数[ResizableOptions](../harmonyos-references/ts-basic-components-image.md#resizableoptions11)类型的slice属性为[EdgeWidths](../harmonyos-references/ts-types.md#edgewidths9)，可设置top/right/bottom/left使图像顶部/右部/底部/左部拉伸时保持不变的距离，与.9图的拉伸规则类似。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vqtLhyw4RBaVkE2k3xkpNg/zh-cn_image_0000002658958231.png "点击放大")

## 解决方案

背景适配.9图并根据图案布局，有组件直接使用通用属性backgroundImageResizable和使用Stack堆叠Image和布局两种方案，其核心思路是相同的。思路如下：

1. 首先确定不发生形变的位置。

   以该问题为例，该图片是一个1038×753px的图形，其中斜杠位置是从(240,0)到(296,131)，因此slice的top、left参数要分别大于131px、296px，可以适当放大。除斜杠位置外，四角圆角不变，测量圆角半径约为40px，因此slice的right、bottom参数要大于40px。slice的四个参数单位为vp，因此ResizableOptions值可以为：

   ```ts
   slice: {
     top: this.getUIContext().px2vp(140),
     bottom: this.getUIContext().px2vp(50),
     left: this.getUIContext().px2vp(300),
     right: this.getUIContext().px2vp(50)
   }
   ```
2. 定位文本位置。这里需要注意的是，对于不同设备，相同vp/fp值对应的px不同，而通过slice设置的不形变距离是通过原图的px确认的。因此，这里所有涉及位置、大小的属性需要使用px值，否则会发生定位不准的情况。同样以该问题为例，布局示例代码如下：

   ```ts
   Row() {
     Text(deviceInfo.deviceType)
       .width(this.getUIContext().px2vp(260))
       .textAlign(TextAlign.Center)
       .fontSize(this.getUIContext().px2fp(60));

     Text('使用backgroundImageResizable')
       .padding({ left: this.getUIContext().px2vp(24) })
       .fontSize(this.getUIContext().px2fp(40));
   }
   .margin({ top: this.getUIContext().px2vp(36) })
   .width('100%')
   .justifyContent(FlexAlign.Start);
   ```

该问题两种方案的完整示例参考如下：

1. 组件直接使用通用属性backgroundImageResizable。
2. 使用Stack堆叠Image和布局。

```ts
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct Point9 {
  build() {
    Column({ space: 10 }) {
      Column() {
        Row() {
          Text(deviceInfo.deviceType)
            .width(this.getUIContext().px2vp(260))
            .textAlign(TextAlign.Center)
            .fontSize(this.getUIContext().px2fp(60));

          Text('使用backgroundImageResizable')
            .padding({ left: this.getUIContext().px2vp(24) })
            .fontSize(this.getUIContext().px2fp(40));
        }
        .margin({ top: this.getUIContext().px2vp(36) })
        .width('100%')
        .justifyContent(FlexAlign.Start);
      }
      .backgroundImage($r('app.media.point9'))
      .backgroundImageSize(ImageSize.FILL)
      .backgroundImageResizable({
        slice: {
          top: this.getUIContext().px2vp(140),
          bottom: this.getUIContext().px2vp(50),
          left: this.getUIContext().px2vp(300),
          right: this.getUIContext().px2vp(50)
        }
      })
      .width('90%')
      .height(200);

      Stack() {
        Image($r('app.media.point9'))
          .objectFit(ImageFit.Fill)
          .resizable({
            slice: {
              top: this.getUIContext().px2vp(140),
              bottom: this.getUIContext().px2vp(50),
              left: this.getUIContext().px2vp(300),
              right: this.getUIContext().px2vp(50)
            }
          });

        Row() {
          Text(deviceInfo.deviceType)
            .width(this.getUIContext().px2vp(260))
            .textAlign(TextAlign.Center)
            .fontSize(this.getUIContext().px2fp(60));

          Text('使用Image的resizable')
            .padding({ left: this.getUIContext().px2vp(24) })
            .fontSize(this.getUIContext().px2fp(40));
        }
        .margin({ top: this.getUIContext().px2vp(36) })
        .width('100%')
        .justifyContent(FlexAlign.Start);
      }
      .alignContent(Alignment.TopStart)
      .width('90%')
      .height(200);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

在手机设备上的效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/eHsdLgv1Sfqrju5Iyl9yFw/zh-cn_image_0000002658838285.png "点击放大")

在平板设备上的效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/dd9o3bYESqWLfNQ_SSZQlQ/zh-cn_image_0000002628599014.png "点击放大")

## 总结

在使用backgroundImageResizable与通过Stack堆叠Image进行布局时，两者均可配合ResizableOptions实现图片的可伸缩效果，其中slice参数的拉伸逻辑与传统 .9 图的规则基本一致。在进行适配时需注意，不同设备上相同像素值对应的vp/fp值可能存在差异，因此建议尽量基于像素（px）值进行布局，以提升一致性与适配效果。
