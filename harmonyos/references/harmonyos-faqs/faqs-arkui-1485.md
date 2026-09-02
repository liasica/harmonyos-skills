---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1485
title: 使用clipShape进行裁剪后，borderRadius无法生效怎么处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用clipShape进行裁剪后，borderRadius无法生效怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:15bb2ef9f3aa42c5743f2642633157addf083970a180d605c547cdcbc17b76c8
---

## 问题现象

对容器组件使用clipShape进行裁剪后，再使用borderRadius对被裁剪容器设置圆角时无法生效，问题代码与问题效果图如下：

```ts
import { PathShape } from '@kit.ArkUI';

@Entry
@Component
struct IrregularShape {
  build() {
    Column() {
      Row()
        .width(300)
        .height(200)
        .backgroundColor('rgba(10, 89, 247, 0.3)')
        .clipShape(new PathShape().commands(`M0 0 L500 0 L500 300 L0 150 Z`))
        .borderRadius(20);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/M-zYC77FSLaR9zuPWpq4Sw/zh-cn_image_0000002658965027.png "点击放大")

## 背景知识

* **设置组件圆角的方法。**
  + [borderRadius](../harmonyos-references/ts-universal-attributes-border.md#borderradius)：borderRadius属性用于设置组件边框的圆角，可以同时设置四个角，也可以分别对四个角的圆角大小进行设置。为了避免子组件尺寸大于组件，导致子组件覆盖圆角，可以搭配属性[clip](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clip12)使用。
  + [clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)：clipShape属性用于对组件进行形状裁剪，通过传入不同的组件类型，将组件裁剪为对应的形状。
* **绘制圆角的方法。**
  + Path：[Path](../harmonyos-references/ts-drawing-components-path.md)是路径绘制组件，可以通过commands属性绘制出所需的形状，包括圆角（圆角多边形）。
* **Path和clipShape的区别。**
  + Path是绘制组件，通过设置路径绘制出所需的形状，其填充区域一般是颜色而非图片。
  + clipShape是通用属性，通过设置不同组件类型对组件进行裁剪，裁剪后的形状背景是组件的一部分。比如对Image组件进行裁剪，裁剪后的形状背景是该Image组件图片的一部分。

## 解决方案

borderRadius属性从规格上是相对于组件的大小而言的，当组件同时设置borderRadius和clipShape时，borderRadius会首先生效，对整个组件设置圆角效果，然后clipShape裁剪效果会覆盖borderRadius的圆角效果，导致borderRadius不生效。

* **方案一：对裁剪的组件设置圆角。**

  使用clipShape对组件进行裁剪时，根据需求，对需设置为圆角的角进行圆角裁剪处理。被裁剪的组件可以是容器组件（如Column、Row等）或Image组件。

  **说明** 

  不能设置两次clipShape属性进行多次裁剪，否则最后一个clipShape的裁剪将会覆盖前面的clipShape裁剪。

  以下示例对Image组件设置clipShape属性，使用PathShape形状描述组件被裁剪后的形状。

  ```ts
  import { PathShape } from '@kit.ArkUI';

  @Entry
  @Component
  struct ClipFilletCorner {
    // 定义PathShape绘制的路线
    /*
      绘制原始图形，即不裁剪，绘制路线的单位为px，宽高默认单位为vp，可以按需要使用像素单位转换方法进行转换
     */
    commands1: string =
      `M0 0 L${this.getUIContext().vp2px(300)} 0 L${this.getUIContext().vp2px(300)} ${this.getUIContext()
        .vp2px(200)} L0 ${this.getUIContext().vp2px(200)} Z`;
    /*
      将图片裁剪为三角形
      * commands的命令M是定义绘制的起点，如M0 0是定义点(0, 0)为绘制起点
      * commands的命令L是绘制当前点到指定点的直线，如L600 0是绘制当前点到(600, 0)的直线
      * commands的命令Z是指绘制当前点到起点的直线并结束绘制
     */
    commands2: string = 'M0 0 L600 0 L600 300 Z';
    /*
      将图片裁剪为带圆角的不规则图形
      * commands的命令H是绘制当前点到对应x坐标的点的水平线，如M0 100 H300是绘制从(0, 100)到(300, 100)的水平线
      * commands的命令V是绘制当前点到对应y坐标的点的垂直线，如M100 0 V300是绘制从(100, 0)到(100, 300)的垂直线
      * commands的命令S是绘制当前点到终点的二次贝塞尔曲线，前两个值是设置控制点，后两个值是曲线终点
     */
    commands3: string = 'M0 100 S0 0 100 0 H300 S400 0 400 100 V300 S400 400 300 400 H200Z';
    @State shapeNum: number = 1;

    build() {
      Column() {
        // 待裁剪图片
        Image($r('app.media.startIcon'))
          .height(200)
          .width(300)
          .margin({ top: 10, bottom: 10 })
          .objectFit(ImageFit.Cover)
          .borderRadius({ topRight: 5 })
          .clipShape(new PathShape().commands(this.shapeNum === 1 ? this.commands1 :
            (this.shapeNum === 2 ? this.commands2 : this.commands3)));

        // 定义命令控制器
        Row() {
          Button('Original')
            .type(ButtonType.Capsule)
            .width(80)
            .onClick(() => {
              this.shapeNum = 1;
            });

          Button('Triangle')
            .type(ButtonType.Capsule)
            .width(80)
            .onClick(() => {
              this.shapeNum = 2;
            });

          Button('Irregular')
            .type(ButtonType.Capsule)
            .width(80)
            .onClick(() => {
              this.shapeNum = 3;
            });
        }.width(300)
        .height(100)
        .justifyContent(FlexAlign.SpaceEvenly);
      }
      .width('100%')
      .height('40%')
      .backgroundColor('rgba(0, 0, 0, 0.05)')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/HsFqjAG_RSSLvJPr2GDogw/zh-cn_image_0000002628605822.png "点击放大")
* **方案二：绘制带圆角的组件**。

  某些场景下可能需要绘制出带有圆角或其他形状的图形，此时可以使用Path组件进行绘制。

  ```ts
  @Entry
  @Component
  struct PathFilletCorner {
    build() {
      Column() {
        // 绘制上一示例的带圆角的不规则图形
        Path()
          .fill('rgba(10, 89, 247, 0.3)')
          .stroke('#0A59F7')
          // 命令与上一示例的commands3相同
          .commands('M0 100 S0 0 100 0 H300 S400 0 400 100 V300 S400 400 300 400 H200Z');

        // 绘制带圆角的三角形
        Path()
          .fill('rgba(0, 0, 0, 0.2)')
          .stroke('#0A59F7')
          .commands('M120 150 L480 150 S600 150 480 90 L360 30 S300 0 240 30 L120 90 S0 150 120 150Z');
      }
      .width('100%')
      .height('40%')
      .backgroundColor('rgba(0, 0, 0, 0.05)')
      .justifyContent(FlexAlign.SpaceEvenly);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/U_WXhFW3Re6t7EGfSHtoGA/zh-cn_image_0000002658845075.png "点击放大")

## 总结

* 当对组件进行圆角设置时，可以使用borderRadius属性。
* 当需要对裁剪后的组件进行圆角设置时，borderRadius属性的效果会被覆盖，可以在使用clipShape对组件进行裁剪时，使用PathShape形状按需要进行形状和圆角的裁剪。
* 当需要绘制带圆角的图形时，可以使用Path组件进行绘制。
