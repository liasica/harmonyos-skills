---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-37
title: 如何绘制圆角矩形
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何绘制圆角矩形
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:80d104f79774c8ab8978373fb65b5f1c25c2e1aad6611127afee8cc651bc33d5
---

## 问题现象

开发者在绘制圆角矩形时，可能会遇到以下几个场景：

* 场景一：如何使用不同的方式绘制圆角矩形？
* 场景二：如何绘制圆角矩形，并在其中居中添加文字？
* 场景三：如何实现绘制圆角矩形的挖空遮罩？
* 场景四：如何绘制一边倾斜的进度条，有圆角和渐变色？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)提供画布组件，用于自定义绘制图形，开发者使用[CanvasRenderingContext2D对象](../harmonyos-references/ts-canvasrenderingcontext2d.md)和[OffscreenCanvasRenderingContext2D对象](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [Polygon](../harmonyos-references/ts-drawing-components-polygon.md)为多边形绘制组件，可以用来绘制图形。[strokeLineJoin](../harmonyos-references/ts-drawing-components-common.md#strokelinejoin)方法用于设置边框拐角绘制样式。
* [ArkGraphics 2D](../harmonyos-guides/arkgraphics2d-introduction.md)（方舟2D图形服务）主要提供图形绘制与显示相关的能力。

## 解决方案

* 场景一：如何使用不同的方式绘制圆角矩形？
  + 方案一：可以通过CanvasRenderingContext2D绘制一个带圆角的矩形。
    1. 接口定义：RectSize定义矩形的宽高，RectPosition定义左上角坐标，PositionData整合位置与尺寸。
    2. 组件结构：使用@Entry与@Component装饰器定义CanvasRadiusRect组件，初始化[RenderingContextSettings](../harmonyos-references/ts-canvasrenderingcontext2d.md#renderingcontextsettings)启用抗锯齿，创建CanvasRenderingContext2D实例context用于绘图。
    3. 位置数据：positionList为存储PositionData对象的数组，定义矩形的位置与尺寸。
    4. drawRect绘制方法：接收矩形位置、大小及圆角半径（默认10），使用[beginPath](../harmonyos-references/ts-components-canvas-common-method.md#beginpath)新建路径，从左上角依次绘制四边，并在每个角落使用[arcTo](../harmonyos-references/ts-components-canvas-common-method.md#arcto)方法绘制圆角，最后设置填充颜色，填充路径并关闭。

    ```ts
    interface RectSize {
      width: number,
      height: number
    }

    interface RectPosition {
      x: number,
      y: number
    }

    interface PositionData {
      postion: RectPosition,
      size: RectSize,
    }

    @Entry
    @Component
    struct CanvasRadiusRect {
      private settings: RenderingContextSettings = new RenderingContextSettings(true);
      private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
      private positionList: PositionData[] = [
        {
          postion: { x: 8, y: 50 },
          size: { width: 360, height: 185 }
        }
      ];

      drawRect(rectPosition: RectPosition, rectSize: RectSize, radius: number = 10) {
        // 圆角弧度
        // 左上角坐标x
        let x = rectPosition.x;
        // 左上角坐标y
        let y = rectPosition.y;
        // 矩形宽
        let width = rectSize.width;
        // 矩形高
        let height = rectSize.height;
        this.context.beginPath();
        this.context.moveTo(0, 0);
        this.context.lineTo(0, this.context.height);
        this.context.lineTo(this.context.width, this.context.height);
        this.context.lineTo(this.context.width, 0);
        this.context.lineTo(0, 0);
        this.context.moveTo(x + radius, y);
        this.context.lineTo(x + width - radius, y);
        this.context.arcTo(x + width, y, x + width, y + radius, radius);
        this.context.lineTo(x + width, y + height - radius);
        this.context.arcTo(x + width, y + height, x + width - radius, y + height, radius);
        this.context.lineTo(x + radius, y + height);
        this.context.arcTo(x, y + height, x, y + height - radius, radius);
        this.context.lineTo(x, y + radius);
        this.context.arcTo(x, y, x + radius, y, radius);
        this.context.fillStyle = '#aa6ad4d0';
        this.context.fill();
        this.context.closePath();
      }

      build() {
        Column() {
          Canvas(this.context)
            .width('100%')
            .height('100%')
            .backgroundColor('#00000000')
            .onReady(() => {
              this.drawRect(this.positionList[0]?.postion, this.positionList[0]?.size);
            });
        }
        .height('100%')
        .width('100%');
      }
    }
    ```
  + 方案二：通过使用Polygon实现。

    ```ts
    @Entry
    @Component
    struct PolygonExample {
      build() {
        Column({ space: 10 }) {
          // 在100*100的矩形框中绘制一个四边形，起点(0,0)，经过(0,100)和(100,100)，终点(100,0)。
          Polygon()
            .width(100)
            .height(100)
            .points([[0, 0], [0, 100], [100, 100], [100, 0]])
            .strokeWidth(10)
            .stroke('#99000000')
            .fill('#99000000')
            .strokeLineJoin(LineJoinStyle.Round); // 设置边框拐角绘制样式
        }
        .width('100%')
        .margin({ top: 10 });
      }
    }
    ```
  + 方案三：使用roundRect（从API version 20开始支持）创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。具体使用可参考[roundRect](../harmonyos-references/ts-components-canvas-common-method.md#roundrect20)。
  + 方案四：使用ArkGraphics 2D[绘制圆角矩形](../harmonyos-guides/geometric-shape-drawing-arkts.md#绘制圆角矩形)。
  + 方案五：使用C++的OH\_Drawing\_RoundRectCreate()接口[绘制圆角矩形](../harmonyos-guides/geometric-shape-drawing-c.md#绘制圆角矩形)。

  五种方案对比：

  | 方案 | 优缺点 | 适用场景 |
  | --- | --- | --- |
  | 方案一 | 使用较复杂，支持通过路径操作实现复杂图形的构建与处理。 | 适用于对图形定制化程度较高，或需要动态更新的复杂应用场景。 |
  | 方案二 | 使用便捷，但可定制化程度有限。 | 适用于对图形复杂度要求较低的简单绘制场景。 |
  | 方案三 | 依赖CPU进行绘制，绘制速度相对较慢，因此对绘制性能有较高要求的场景应避免使用离屏绘制。 | 适用于非频繁更新的静态内容。 |
  | 方案四 | 代码结构简洁，但无法动态计算路径坐标，难以实现复杂图形；渲染引擎直接处理性能较高。 | 适用于对图形复杂度要求不高的简单绘制场景。 |
  | 方案五 | 使用较复杂，性能较高，但需注意内存管理。 | 适用于对高性能有需求，或需要与Native代码交互的场景。 |
* 场景二：如何绘制圆角矩形，并在其中居中添加文字？
  1. 创建一个Path2D路径对象，并在该路径对象中绘制一个圆角矩形。
  2. 使用CanvasRenderingContext2D对象的fill方法对所创建的矩形路径进行填充。
  3. 在CanvasRenderingContext2D对象中，设置[textAlign](../harmonyos-references/ts-components-canvas-common-property.md#textalign)属性为center，[textBaseline](../harmonyos-references/ts-components-canvas-common-property.md#textbaseline)属性为middle，以配置文本的对齐方式和基线类型。
  4. 使用fillText方法将指定文字绘制在圆角矩形中心的指定x、y坐标位置。

  ```ts
  import { Point } from '@kit.TestKit';

  @Entry
  @Component
  struct CanvasRadiusText {
    private readonly settings: RenderingContextSettings = new RenderingContextSettings(true);
    private readonly ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    center: Point = { x: 200, y: 200 };
    backSize: Size = { width: 200, height: 200 };

    private drawRoundRect(center: Point, size: Size, radius: number) {
      const x = center.x - size.width / 2;
      const y = center.y - size.height / 2;
      let path = new Path2D();
      path.moveTo(x + radius, y);
      path.arcTo(x + size.width, y, x + size.width, y + radius, radius);
      path.arcTo(x + size.width, y + size.height, x + size.width - radius, y + size.height, radius);
      path.arcTo(x, y + size.height, x, y + radius, radius);
      path.arcTo(x, y, x + radius, y, radius);
      path.closePath();
      this.ctx.fillStyle = '#0097D4';
      this.ctx.fill(path);
    }

    private drawText() {
      let str = 'hello world';
      this.ctx.font = '30vp';
      this.ctx.textAlign = 'center';
      this.ctx.textBaseline = 'middle';
      let metrics = this.ctx.measureText(str);
      // 绘制文字显示区域
      this.ctx.fillStyle = Color.Green;
      this.ctx.fillRect(this.center.x - metrics.width / 2, this.center.y - metrics.height / 2, metrics.width,
        metrics.height);
      // 把文字绘制到背景正中心
      this.ctx.fillStyle = Color.Black;
      this.ctx.fillText(str, this.center.x, this.center.y);
    }

    build() {
      Stack() {
        Canvas(this.ctx)
          .height('100%')
          .width('100%')
          .onReady(() => {
            this.drawRoundRect(this.center, this.backSize, 20);
            this.drawText();
          })
          .backgroundColor('#eee');
      }.height('100%').width('100%');
    }
  }
  ```
* 场景三：如何实现绘制圆角矩形的挖空遮罩？
  1. 根据矩形的坐标位置与尺寸，调用beginPath方法新建一个绘制路径，从矩形的左上角顶点开始，依次绘制四条边；在每个转角处，使用arcTo方法实现圆角效果。
  2. 设置fillStyle属性以定义填充颜色，调用fill方法对路径进行填充，最后通过closePath方法闭合路径，确保图形完整封闭。

  ```ts
  @Entry
  @Component
  struct CanvasMaskDemo {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

    build() {
      Row() {
        Column() {
          Stack() {
            Image($r('app.media.startIcon')).height(300); // 此处仅为样例，请开发者替换为可用图片
            Canvas(this.context)
              .width('100%')
              .height('100%')
              .backgroundColor('#00000000')
              .onReady(() => {
                // 圆角弧度
                let radius = 10;
                // 左上角坐标x
                let x = 100;
                // 左上角坐标y
                let y = 350;
                // 矩形宽
                let width = 100;
                // 矩形高
                let height = 40;
                this.context.beginPath();
                this.context.moveTo(0, 0);
                this.context.lineTo(0, this.context.height);
                this.context.lineTo(this.context.width, this.context.height);
                this.context.lineTo(this.context.width, 0);
                this.context.lineTo(0, 0);
                this.context.moveTo(x + radius, y);
                this.context.lineTo(x + width - radius, y);
                this.context.arcTo(x + width, y, x + width, y + radius, radius);
                this.context.lineTo(x + width, y + height - radius);
                this.context.arcTo(x + width, y + height, x + width - radius, y + height, radius);
                this.context.lineTo(x + radius, y + height);
                this.context.arcTo(x, y + height, x, y + height - radius, radius);
                this.context.lineTo(x, y + radius);
                this.context.arcTo(x, y, x + radius, y, radius);
                this.context.fillStyle = '#aa000000';
                this.context.fill();
                this.context.closePath();
              });
          }.width('100%')
          .height('100%');
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* 场景四：如何绘制一边倾斜的进度条，有圆角和渐变色？
  1. 根据矩形的坐标位置与尺寸，绘制PK条，调用beginPath方法新建一个绘制路径，从矩形的左上角顶点开始，依次绘制四条边；在每个转角处，使用arcTo方法实现圆角效果，调用addColorStop添加底色。
  2. 使用drawImage绘制头像，fillText填充文字。

  ```ts
  @Entry
  @Component
  struct PKBarCanvas {
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    // ImageBitmap需使能相关开关：模块的build-profile.json5中buildOption>resOptions>copyCodeResource>enable设置为true。
    private avatarImage: ImageBitmap = new ImageBitmap('common/images/startIcon.png');

    build() {
      Column() {
        Canvas(this.context)
          .width(350)
          .height(60)
          .onReady(() => {
            this.drawPKBar();
          })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .backgroundColor(0x222222)
    }

    drawPKBar() {
      const ctx = this.context;
      const totalWidth = 350;
      const totalHeight = 60;
      const cornerRadius = 15;
      const slopeOffset = 12;
      const middleGap = 10;
      // 【新增】左边占比（0.6表示左边占60%，右边占40%，可调整）
      const leftWidthRatio = 0.6;
      // 根据比例计算左右分割线的X坐标
      const splitX = totalWidth * leftWidthRatio;

      // ————————————————1.绘制PK条底色————————————————
      ctx.clearRect(0, 0, totalWidth, totalHeight);

      // 左边底色（变长）
      ctx.beginPath();
      ctx.moveTo(cornerRadius, 0);
      // 上边线终点改为splitX
      ctx.lineTo(splitX - (middleGap / 2) + slopeOffset, 0);
      // 斜边底端X坐标改为splitX
      ctx.lineTo(splitX - (middleGap / 2) - slopeOffset, totalHeight);
      ctx.lineTo(cornerRadius, totalHeight);
      ctx.arcTo(0, totalHeight, 0, totalHeight - cornerRadius, cornerRadius);
      ctx.lineTo(0, cornerRadius);
      ctx.arcTo(0, 0, cornerRadius, 0, cornerRadius);
      ctx.closePath();
      // 左边渐变终点也改为splitX
      const leftGradient = ctx.createLinearGradient(0, 0, splitX, 0);
      leftGradient.addColorStop(0, '#FF416C');
      leftGradient.addColorStop(1, '#FF4B2B');
      ctx.fillStyle = leftGradient;
      ctx.fill();

      // 右边底色（变短）
      ctx.beginPath();
      // 起点改为splitX
      ctx.moveTo(splitX + (middleGap / 2) + slopeOffset, 0);
      ctx.lineTo(totalWidth - cornerRadius, 0);
      ctx.arcTo(totalWidth, 0, totalWidth, cornerRadius, cornerRadius);
      ctx.lineTo(totalWidth, totalHeight - cornerRadius);
      ctx.arcTo(totalWidth, totalHeight, totalWidth - cornerRadius, totalHeight, cornerRadius);
      // 下边线终点改为splitX
      ctx.lineTo(splitX + (middleGap / 2) - slopeOffset, totalHeight);
      ctx.lineTo(splitX + (middleGap / 2) + slopeOffset, 0);
      ctx.closePath();
      // 右边渐变起点也改为splitX
      const rightGradient = ctx.createLinearGradient(totalWidth, 0, splitX, 0);
      rightGradient.addColorStop(0, '#00F260');
      rightGradient.addColorStop(1, '#0575E6');
      ctx.fillStyle = rightGradient;
      ctx.fill();

      // ————————————————2.绘制头像和分数————————————————
      const avatarRadius = 18;
      const textMargin = 10;
      const fontSize = 20;
      const leftScore = '96';
      const rightScore = '86';

      // 左边头像和分数（位置不变，依然在最左侧）
      ctx.save();
      const leftAvatarX = cornerRadius + 5 + avatarRadius;
      const leftAvatarY = totalHeight / 2;
      ctx.beginPath();
      ctx.arc(leftAvatarX, leftAvatarY, avatarRadius, 0, Math.PI * 2);
      ctx.clip();
      ctx.drawImage(
        this.avatarImage,
        leftAvatarX - avatarRadius,
        leftAvatarY - avatarRadius,
        avatarRadius * 2,
        avatarRadius * 2
      );
      ctx.restore();
      ctx.font = `bold ${fontSize}vp sans-serif`;
      ctx.fillStyle = '#FFFFFF';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText(leftScore, leftAvatarX + avatarRadius + textMargin, leftAvatarY);

      // 右边头像和分数（位置不变，依然在最右侧）
      ctx.save();
      const rightAvatarX = totalWidth - cornerRadius - 5 - avatarRadius;
      const rightAvatarY = totalHeight / 2;
      ctx.beginPath();
      ctx.arc(rightAvatarX, rightAvatarY, avatarRadius, 0, Math.PI * 2);
      ctx.clip();
      ctx.drawImage(
        this.avatarImage,
        rightAvatarX - avatarRadius,
        rightAvatarY - avatarRadius,
        avatarRadius * 2,
        avatarRadius * 2
      );
      ctx.restore();
      ctx.textAlign = 'right';
      ctx.fillText(rightScore, rightAvatarX - avatarRadius - textMargin, rightAvatarY);
    }
  }
  ```
