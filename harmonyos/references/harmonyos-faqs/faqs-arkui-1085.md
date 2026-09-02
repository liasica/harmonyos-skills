---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1085
title: 如何裁剪自定义形状
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何裁剪自定义形状
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:a8d0695ba657f92348bb94b82bc330c7703de70aecefa12eb229a7c0adad8713
---

## 问题现象

如何通过裁剪属性设计自定义形状？

## 背景知识

[clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。通过[PathShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#pathshape12)类型的参数按[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)自定义裁剪形状。

## 解决方案

* 场景一：按SVG路径裁剪。

  示例：裁剪圆角梯形。

  路径描述：从上底左侧点(150,0)开始，水平向右画到(250,0)，接着以半径20的圆弧连接到(270,20)，再直线延伸至右下角(350,180)，然后通过另一个圆弧过渡到(330,200)，再水平向左到(50,200)，接着用圆弧连接到(30,180)，然后垂直向下到(30,20)，再通过圆弧回到起点(50,0)，最后闭合路径。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/pXmqP7PgQ3eOCmdEDAKjig/zh-cn_image_0000002710157063.png "点击放大")

  示例代码如下：

  ```ts
  import { PathShape } from '@kit.ArkUI';

  @Entry
  @Component
  struct ServiceCardPage {
    build() {
      Column() {
        Image($r('app.media.background'))
          .width('500px')
          .height('300px')
          .clipShape(new PathShape({
            commands: 'M 150 0 H 250 A 20 20 0 0 1 270 20 L 350 180 A 20 20 0 0 1 330 200 H 50 A 20 20 0 0 1 30 180 V 20 A 20 20 0 0 1 50 0 Z'
          }));
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```
* 场景二：利用固定图形路径配合偏移量进行裁剪。

  示例：将矩形裁剪出底部圆弧。

  构造一个宽度与图片一样，高度为图片1.5倍的RectShape，为此RectShape设置圆角，然后将此RectShape进行偏移。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/obRqt_zvRgSp3gPBnBwSnA/zh-cn_image_0000002680480188.png "点击放大")

  示例代码如下：

  ```ts
  import { RectShape } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index2 {
    build() {
      Column() {
        Image($r('app.media.background'))
          .width('50%')
          .objectFit(ImageFit.Fill)
          .clipShape(new RectShape({
            radiusWidth: '40%',
            radiusHeight: '10%',
            width: '100%',
            height: '150%'
          })
            .position({ y: '-50%' })
          );
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```
* 场景三：裁剪出向上凹陷的圆角。

  示例：将组件底部裁剪出向上凹陷的圆角效果。

  使用PathShape自定义路径，在底部中间位置绘制一个向上凹陷的圆弧，实现卡片式封面效果。

  示例代码如下：

  ```ts
  import { PathShape } from '@kit.ArkUI';

  @Entry
  @Component
  struct ClipShapeExample {
    private radiusVp: number = 16; // 圆角半径

    build() {
      Column() {
        // 上方组件 - 使用PathShape裁剪
        Column() {
          // 上方组件内容区域
          Text('上方内容')
            .width('100%')
            .height('100%')
            .textAlign(TextAlign.Center)
            .backgroundColor('#FFB6C1')
        }
        .width(300)
        .height(100)
        .clipShape(new PathShape()
          .commands(this.getClipPath(300, 100, this.radiusVp))
        )

        // 下方组件 - 圆角16vp
        Column() {
          Text('下方内容')
            .width('100%')
            .height('100%')
            .textAlign(TextAlign.Center)
            .backgroundColor('#87CEEB')
        }
        .width(300)
        .height(100)
        .borderRadius(this.radiusVp)
        .clip(true)
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
    }

    // 生成裁剪路径命令
    // A指令参数说明: A rx ry x-rotation large-arc-flag sweep-flag x y
    getClipPath(widthVp: number, heightVp: number, radiusVp: number): string {
      const ctx = this.getUIContext();
      const w = ctx.vp2px(widthVp);
      const h = ctx.vp2px(heightVp);
      const r = ctx.vp2px(radiusVp);

      // 路径：从左上角开始，顺时针绘制，底部中间向上凹陷
      return `M${r} 0
  L${w - r} 0
  A${r} ${r} 0 0 1 ${w} ${r}
  L${w} ${h}
  A${r} ${r} 0 0 0 ${w - r} ${h - r}
  L${r} ${h - r}
  A${r} ${r} 0 0 0 0 ${h}
  L0 ${r}
  A${r} ${r} 0 0 1 ${r} 0 Z`;
    }
  }
  ```

## 总结

对于较为简单的裁剪，可以使用固定图案进行裁剪，并通过偏移量控制具体裁剪的区域。当需要裁剪的图案较为复杂时，可以通过SVG规范描述裁剪路径。需要注意的是：圆角为边框属性，当对组件进行裁剪后，圆角也会被裁剪，而非给裁剪后的组件添加圆角效果。如果需要给裁剪后的组件添加圆角，需要在裁剪路径中绘制圆弧来实现圆角效果。
