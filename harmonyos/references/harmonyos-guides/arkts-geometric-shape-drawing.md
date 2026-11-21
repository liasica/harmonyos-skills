---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-geometric-shape-drawing
title: 绘制几何图形 (Shape)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 几何图形绘制 > 绘制几何图形 (Shape)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:08+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:967665b31202b57ed4a6c99395b1d0159c9a283dc92d58cd553b928bdbf221fc
---

绘制组件用于在页面绘制图形，Shape组件是绘制组件的父组件，包含所有绘制组件的通用属性。具体用法请参考[Shape](../harmonyos-references/ts-drawing-components-shape.md)。

## 创建绘制组件

绘制组件可以由以下两种形式创建：

* 绘制组件使用Shape作为父组件，实现类似SVG的效果。接口调用为以下形式：

  ```ts
  Shape(value?: PixelMap)
  ```

  该接口用于创建带有父组件的绘制组件，其中value用于设置绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。

  ```typescript
  Shape() {
    Rect().width(300).height(50)
  }
  ```
* 绘制组件单独使用，用于在页面上绘制指定的图形。有7种绘制类型，分别为[Circle](../harmonyos-references/ts-drawing-components-circle.md)（圆形）、[Ellipse](../harmonyos-references/ts-drawing-components-ellipse.md)（椭圆形）、[Line](../harmonyos-references/ts-drawing-components-line.md)（直线）、[Polyline](../harmonyos-references/ts-drawing-components-polyline.md)（折线）、[Polygon](../harmonyos-references/ts-drawing-components-polygon.md)（多边形）、[Path](../harmonyos-references/ts-drawing-components-path.md)（路径）、[Rect](../harmonyos-references/ts-drawing-components-rect.md)（矩形）。以Circle的接口调用为例：

  ```ts
  Circle(value?: { width?: string | number, height?: string | number })
  ```

  该接口用于在页面绘制圆形，其中width用于设置圆形的宽度，height用于设置圆形的高度，圆形直径由宽高最小值确定。

  ```typescript
  Circle({ width: 150, height: 150 })
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/BlzapIZpQgma9ovw1xEIsA/zh-cn_image_0000002793036772.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=A04CC779D1CF65BD098AFFD00D6888E7B5247BD50EB3C119E4D65F65BB758E9D)

## 形状视口viewPort

```ts
viewPort(value: { x?: number | string, y?: number | string, width?: number | string, height?: number | string })
```

形状视口viewPort指定用户空间中的一个矩形，该矩形映射到为关联的SVG元素建立的视区边界。viewPort属性的值包含x、y、width和height四个可选参数，x和y表示视区的左上角坐标，width和height表示其尺寸。

以下三个示例说明如何使用viewPort：

* 通过形状视口对图形进行放大与缩小。

  ```typescript
  class Tmp {
    public x: number = 0;
    public y: number = 0;
    public width: number = 75;
    public height: number = 75;
  }

  class TmpOne {
    public x: number = 0;
    public y: number = 0;
    public width: number = 300;
    public height: number = 300;
  }

  @Entry
  @Component
  struct ViewPort1 {
    viep: Tmp = new Tmp();
    viep1: TmpOne = new TmpOne();

    build() {
      Column() {
        // 画一个宽高都为75的圆
        // 请将$r('app.string.OriginalSizeCircle')替换为实际资源文件，在本示例中该资源文件的value值为"原始尺寸Circle组件"
        Text($r('app.string.OriginalSizeCircle')).margin({ top: 20 })
        Circle({ width: 75, height: 75 }).fill('rgb(39, 135, 217)')

        Row({ space: 10 }) {
          Column() {
          // 创建一个宽高都为150的shape组件，背景色为青绿色，一个宽高都为75的viewPort。
            // 用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个直径为75的圆。
            // 绘制结束，viewPort会根据组件宽高放大两倍。
            // 请将$r('app.string.EnlargedCircle')替换为实际资源文件，在本示例中该资源文件的value值为"shape内放大的Circle组件"
            Text($r('app.string.EnlargedCircle'))
            Shape() {
              Rect().width('100%').height('100%').fill('rgb(39, 135, 217)')
              Circle({ width: 75, height: 75 }).fill('rgb(213, 213, 213)')
            }
            .viewPort(this.viep)
            .width(150)
            .height(150)
            .backgroundColor('rgb(23, 169, 141)')
          }

          Column() {
            // 创建一个宽高都为150的shape组件，背景色为青绿色，一个宽高都为300的viewPort。
            // 用一个灰色的矩形来填充viewPort，在viewPort中绘制一个直径为75的圆。
            // 绘制结束，viewPort会根据组件宽高缩小两倍。
            // 请将$r('app.string.ShrunkCircle')替换为实际资源文件，在本示例中该资源文件的value值为"Shape内缩小的Circle组件"
            Text($r('app.string.ShrunkCircle'))
            Shape() {
              Rect().width('100%').height('100%').fill('rgb(213, 213, 213)')
              Circle({ width: 75, height: 75 }).fill('rgb(39, 135, 217)')
            }
            .viewPort(this.viep1)
            .width(150)
            .height(150)
            .backgroundColor('rgb(23, 169, 141)')
          }
        }
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/NgFZROl9S6iJaBIIdW563g/zh-cn_image_0000002792876804.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=517A9E7026880D9FBF4E1DD4D7721097E470B0DA3B0FF0BCE54CEBA04635A492)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewPort。用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个半径为75的圆。

  ```typescript
  class TmpTwo {
    public x: number = 0;
    public y: number = 0;
    public width: number = 300;
    public height: number = 300;
  }

  @Entry
  @Component
  struct ViewPort2 {
    viep: TmpTwo = new TmpTwo();

    build() {
      Column() {
        Shape() {
          Rect().width('100%').height('100%').fill('#0097D4')
          Circle({ width: 150, height: 150 }).fill('#E87361')
        }
        .viewPort(this.viep)
        .width(300)
        .height(300)
        .backgroundColor('#F5DC62')
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Ftmw9T7vTu-dc0j7lim4Qg/zh-cn_image_0000002821836709.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDDC37111A173AE7202382AFEEAB3257BEB9C0D6F53A2AF12588178A90ADD165)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewPort。用一个蓝色的矩形来填充viewPort，在viewPort中绘制一个半径为75的圆，将viewPort向右方和下方各平移150。

  ```typescript
  class TmpThree {
    public x: number = -150;
    public y: number = -150;
    public width: number = 300;
    public height: number = 300;
  }

  @Entry
  @Component
  struct ViewPort3 {
    viep: TmpThree = new TmpThree();

    build() {
      Column() {
        Shape() {
          Rect().width('100%').height('100%').fill('#0097D4')
          Circle({ width: 150, height: 150 }).fill('#E87361')
        }
        .viewPort(this.viep)
        .width(300)
        .height(300)
        .backgroundColor('#F5DC62')
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Juo1lKWuQ-SBNVXNo0Te1A/zh-cn_image_0000002821756711.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4EDEC752F27E602D2A140CA1AFB0255FC1CA1F788AF72E0640339A953731BF9)

## 自定义样式

**说明** 

示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

绘制组件支持通过各种属性更改组件样式。

* 通过[fill](../harmonyos-references/ts-drawing-components-common.md#fill)可以设置组件填充区域颜色。

  ```typescript
  Path()
    .width(100)
    .height(100)
    .commands('M150 0 L300 300 L0 300 Z')
    .fill('#E87361')
    .strokeWidth(0)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Z4lyxGF5TiG5KMRyM26DdA/zh-cn_image_0000002793036774.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5255B0B1FACBFC151D3B7E8E850E689FCA38245A891414F84DC1CC8FD87901A)
* 通过[stroke](../harmonyos-references/ts-drawing-components-common.md#stroke)可以设置组件边框颜色。

  ```typescript
  Path()
    .width(100)
    .height(100)
    .fillOpacity(0)
    .commands('M150 0 L300 300 L0 300 Z')
    .stroke(Color.Red)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/9s_SjA4aSuam1jizQVCVlQ/zh-cn_image_0000002792876806.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDAC29F0B645B3C82A837643CA0C6643614A0C2109D5C588E2572EC835C9AC84)
* 通过[strokeOpacity](../harmonyos-references/ts-drawing-components-common.md#strokeopacity)可以设置边框透明度。

  ```typescript
  Path()
    .width(100)
    .height(100)
    .fillOpacity(0)
    .commands('M150 0 L300 300 L0 300 Z')
    .stroke(Color.Red)
    .strokeWidth(10)
    .strokeOpacity(0.2)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xFEHrd2JQ0uj2Iz4SBT17w/zh-cn_image_0000002821836711.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACC56B2E0EBEC8C4C783B1CC3A5F72535696F486D0161983F42EDB436306746B)
* 通过[strokeLineJoin](../harmonyos-references/ts-drawing-components-common.md#strokelinejoin)可以设置线条拐角绘制样式。拐角绘制样式分为Bevel(使用斜角连接路径段)、Miter(使用尖角连接路径段)、Round(使用圆角连接路径段)。

  ```typescript
  Polyline()
    .width(100)
    .height(100)
    .fillOpacity(0)
    .stroke(Color.Red)
    .strokeWidth(8)
    .points([[20, 0], [0, 100], [100, 90]])
    // 设置折线拐角处为圆弧
    .strokeLineJoin(LineJoinStyle.Round)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/xh_ugsNsRmC5hpWId71FJQ/zh-cn_image_0000002821756713.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9C783DA90D106188268489FA69B6CC6DAF509001992ABAE2D3BBF5709FF3B27)
* 通过[strokeMiterLimit](../harmonyos-references/ts-drawing-components-common.md#strokemiterlimit)设置斜接长度与边框宽度比值的极限值。

  斜接长度表示外边框外边交点到内边交点的距离，边框宽度即[strokeWidth](../harmonyos-references/ts-drawing-components-common.md#strokewidth)属性的值。

  strokeMiterLimit取值需大于等于1，且在[strokeLineJoin](../harmonyos-references/ts-drawing-components-common.md#strokelinejoin)属性取值LineJoinStyle.Miter时生效。

  ```typescript
  Polyline()
    .width(100)
    .height(100)
    .fillOpacity(0)
    .stroke(Color.Red)
    .strokeWidth(10)
    .points([[20, 0], [20, 100], [100, 100]])
    // 设置折线拐角处为尖角
    .strokeLineJoin(LineJoinStyle.Miter)
    // 设置斜接长度与线宽的比值
    .strokeMiterLimit(1 / Math.sin(45 * Math.PI / 180))
  Polyline()
    .width(100)
    .height(100)
    .fillOpacity(0)
    .stroke(Color.Red)
    .strokeWidth(10)
    .points([[20, 0], [20, 100], [100, 100]])
    .strokeLineJoin(LineJoinStyle.Miter)
    .strokeMiterLimit(1.42)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/GdTwbZeNTEq1ebpYAx5L6g/zh-cn_image_0000002793036776.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=130B9E5B7615371523770D26A07B671427E08DAC492F8A69D8F1F75F6DF48027)
* 通过[antiAlias](../harmonyos-references/ts-drawing-components-common.md#antialias)设置是否开启抗锯齿，默认值为true（开启抗锯齿）。

  ```typescript
  // 开启抗锯齿
  Circle()
    .width(150)
    .height(200)
    .fillOpacity(0)
    .strokeWidth(5)
    .stroke(Color.Black)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/E2h89tDjSjWFlCdBuDmGJA/zh-cn_image_0000002792876808.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFB09E0F592B99D67229D9F99185C948741070C936F17F49371F3762BC82F26D)

  ```typescript
  // 关闭抗锯齿
  Circle()
    .width(150)
    .height(200)
    .fillOpacity(0)
    .strokeWidth(5)
    .stroke(Color.Black)
    .antiAlias(false)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/-NYzSrLUStWOvpyvJXSKZg/zh-cn_image_0000002821836713.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=D78FD3B83D19BF17392EA6A369271070D38757BE303237063D9F8A062396E679)
* 通过[mesh](../harmonyos-references/ts-drawing-components-shape.md#mesh8)设置网格效果，实现图像局部扭曲。

  **说明** 

  示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

  ```typescript
  import { FrameNode, NodeController, RenderNode } from '@kit.ArkUI';
  import { image } from '@kit.ImageKit';
  import { drawing } from '@kit.ArkGraphics2D';

  let offCanvas: OffscreenCanvas = new OffscreenCanvas(150, 150);
  let ctx = offCanvas.getContext('2d');

  class DrawingRenderNode extends RenderNode {

    async draw(context: DrawContext) {
      const canvas = context.canvas;
      let pixelMap = ctx.getPixelMap(0, 0, 150, 150);
      const brush = new drawing.Brush(); // 只支持brush，使用pen没有绘制效果。
      canvas.attachBrush(brush);
      let verts: number[] = [0, 0, 410, 0, 50, 0, 0, 180, 50, 180, 410, 180, 0, 360, 410, 360, 50, 360];
      canvas.drawPixelMapMesh(pixelMap, 2, 2, verts, 0, null, 0);
      canvas.detachBrush();
    }
  }

  const renderNode = new DrawingRenderNode();
  renderNode.frame = {
    x: 0,
    y: 0,
    width: 150,
    height: 150
  };

  class MyNodeController extends NodeController {
    private rootNode: FrameNode | null = null;

    makeNode(uiContext: UIContext): FrameNode | null {
      this.rootNode = new FrameNode(uiContext);

      const rootRenderNode = this.rootNode.getRenderNode();
      if (rootRenderNode !== null) {
        rootRenderNode.appendChild(renderNode);
      }
      return this.rootNode;
    }
  }

  @Entry
  @Component
  struct Mesh {
    private myNodeController: MyNodeController = new MyNodeController();
    @State showShape: boolean = false;
    @State pixelMap: image.PixelMap | undefined = undefined;
    @State shapeWidth: number = 150;
    @State strokeWidth: number = 1;
    @State meshArray: Array<number> = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360];

    aboutToAppear(): void {
      // 'resources/base/media/image.png'需要替换为开发者所需的图像资源文件
      let img: ImageBitmap = new ImageBitmap('resources/base/media/image.png');
      ctx.drawImage(img, 0, 0, 100, 100);
      this.pixelMap = ctx.getPixelMap(0, 0, 150, 150);
    }

    build() {
      Column() {
        Image(this.pixelMap)
          .backgroundColor('#86C5E3')
          .width(150)
          .height(150)
          .onClick(() => {
            // 'resources/base/media/image.png'需要替换为开发者所需的图像资源文件
            let img: ImageBitmap = new ImageBitmap('resources/base/media/image.png');
            ctx.drawImage(img, 0, 0, 100, 100);
            this.pixelMap = ctx.getPixelMap(1, 1, 150, 150);
            this.myNodeController.rebuild();
            this.strokeWidth += 1;
          })

        NodeContainer(this.myNodeController)
          .width(150)
          .height(150)
          .backgroundColor(Color.Grey)
          .onClick(() => {
            this.meshArray = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360];
          })
        Button('change mesh')
          .margin(5)
          .onClick(() => {
            this.meshArray = [0, 0, 410, 0, 50, 0, 0, 180, 50, 180, 410, 180, 0, 360, 410, 360, 50, 360];
          })
        Button('Show Shape')
          .margin(5)
          .onClick(() => {
            this.showShape = !this.showShape;
          })

        if (this.showShape) {
          Shape(this.pixelMap) {
            Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
          }
          .fillOpacity(0.2)
          .backgroundColor(Color.Grey)
          .width(this.shapeWidth)
          .height(150)
          .mesh(this.meshArray, 2, 2)
          .fill(0x317AF7)
          .stroke(0xEE8443)
          .strokeWidth(this.strokeWidth)
          .strokeLineJoin(LineJoinStyle.Miter)
          .strokeMiterLimit(5)

          Shape(this.pixelMap) {
            Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
          }
          .fillOpacity(0.2)
          .backgroundColor(Color.Grey)
          .width(this.shapeWidth)
          .height(150)
          .fill(0x317AF7)
          .stroke(0xEE8443)
          .strokeWidth(this.strokeWidth)
          .strokeLineJoin(LineJoinStyle.Miter)
          .strokeMiterLimit(5)
          .onDragStart(() => {
          })

          // mesh只对shape传入pixelMap时生效，此处不生效
          Shape() {
            Path().width(150).height(60).commands('M0 0 L400 0 L400 150 Z')
          }
          .fillOpacity(0.2)
          .backgroundColor(Color.Grey)
          .width(this.shapeWidth)
          .height(150)
          .mesh(this.meshArray, 2, 2)
          .fill(0x317AF7)
          .stroke(0xEE8443)
          .strokeWidth(this.strokeWidth)
          .strokeLineJoin(LineJoinStyle.Miter)
          .strokeMiterLimit(5)
          .onClick(() => {
            this.pixelMap = undefined;
          })
        }
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/83lMCLp_REacKpy4zU_3Yg/zh-cn_image_0000002821756715.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=60D441A4BA00E664FBA61C838020CABDDC5924CD5ACAB53DD814E357C2BECCB0)

## 场景示例

### 绘制封闭路径

在Shape的(-80, -5)点绘制一个封闭路径，填充颜色rgb(213, 213, 213)，线条宽度3，边框颜色rgb(39, 135, 217)，拐角样式锐角（默认值）。

**说明** 

示例通过commands来绘制路径，commands参数说明请参考[SVG路径描述规范](../harmonyos-references/ts-drawing-components-path.md#svg路径描述规范)。

```typescript
@Entry
@Component
struct ShapeExample {
  build() {
    Column({ space: 10 }) {
      Shape() {
        Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
      }
      .viewPort({
        x: -80,
        y: -5,
        width: 500,
        height: 300
      })
      .fill('rgb(213, 213, 213)')
      .stroke('rgb(39, 135, 217)')
      .strokeWidth(3)
      .strokeLineJoin(LineJoinStyle.Miter)
      .strokeMiterLimit(5)
    }.width('100%').margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/cWTmfRlaRnaMAafYiHNmlw/zh-cn_image_0000002793036778.png?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B3DE02721941A051D7CD995FF6AC3A2B040E2585D335F8399073B5C523DEFCC)

### 绘制圆和圆环

绘制一个直径为150的圆，和一个直径为150、线条为红色虚线的圆环（宽高设置不一致时以短边为直径）。

**说明** 

本示例通过strokeDashArray属性设置边框间隙来实现红色虚线的圆环，strokeDashArray属性参考[strokeDashArray](../harmonyos-references/ts-drawing-components-common.md#strokedasharray)。

```typescript
@Entry
@Component
struct CircleExample {
  build() {
    Column({ space: 10 }) {
      // 绘制一个直径为150的圆
      Circle({ width: 150, height: 150 })
      // 绘制一个直径为150、线条为红色虚线的圆环
      Circle()
        .width(150)
        .height(200)
        .fillOpacity(0)
        .strokeWidth(3)
        .stroke(Color.Red)
        .strokeDashArray([1, 2])
      // ...
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/EZNwKN6FSNKcp1rAezrnQw/zh-cn_image_0000002792876810.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=73C8872F4D468548628BA2F56BC75ADFDC690FABF70BA9CD0197A9CDF84284C7)

### UI视觉属性作用效果

**说明** 

[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)、[linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)等通用属性作用于组件的背景区域，而不会在组件具体的内容区域生效。

```typescript
@Entry
@Component
struct CircleExample {
  build() {
    Column({ space: 10 }) {
      // ...
      // 绘制一个直径为150的圆
      Circle()
        .width(150)
        .height(200)
        .backgroundColor(Color.Pink) // 会生效在一个150*200大小的矩形区域，而非仅在绘制的一个直径为150的圆形区域
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/B8D2UP1UQXGmCgoP1jhA4Q/zh-cn_image_0000002821836715.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T010944Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC5DD342FFAD242C41E72B6A608AF6F8EC8FD99D1F66D6EC63EC8EAA72140B1A)
