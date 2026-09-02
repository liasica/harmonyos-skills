---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-691
title: 如何实现画布的扩展以及内容的移动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现画布的扩展以及内容的移动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:047d04c3863fbe5c8f64208600b55a3c9ee5b2a84eaa663fdd56da03c54efd35
---

## 问题现象

利用Canvas画布绘制内容，如何实现画布的扩展以及内容的移动？

## 背景知识

* [Canvas](../harmonyos-guides/arkts-drawing-customization-on-canvas.md)：提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [translate](../harmonyos-references/ts-components-canvas-common-method.md#translate)：移动当前坐标系的原点。

## 解决方案

* 方案一：动态增加Canvas的宽度。
  1. 利用Scroll嵌套Canvas，利用状态变量装饰Canvas宽度，初始化值为屏幕宽度。
  2. 点击按钮增加Canvas组件宽度，并把待绘制节点保存到列表中，随后清空画布并重新绘制。

     ```ts
     draw() {
       this.context.clearRect(0, 0, this.canvasWidth, 400);
       this.context.beginPath();
       this.context.lineWidth = 2;
       this.context.lineJoin = 'round';
       this.context.moveTo(50, 250);
       this.connectionPointList.forEach(element => {
         this.context.lineTo(element.x, element.y);
         this.context.arc(element.x, element.y, 5, 0, Math.PI * 2);
       });
       this.context.stroke();
     }
     ```
  3. 利用scrollTo方法跳转到最新的绘制位置上。

     ```ts
     this.scroller.scrollTo({ xOffset: x - 300, yOffset: this.y });
     ```

  完整示例参考如下：

  ```ts
  import { display } from '@kit.ArkUI';

  class ConnectionPoint {
    x: number;
    y: number;

    constructor(x: number, y: number) {
      this.x = x;
      this.y = y;
    }
  }

  @Entry
  @Component
  struct CanvasDrawOffset {
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
    private scroller: Scroller = new Scroller();
    private connectionPointList: Array<ConnectionPoint> = [];
    private count: number = 0;
    private y: number = 350;
    private screenWidth: number = 0;
    @State canvasWidth: number = 0;

    aboutToAppear(): void {
      display.getAllDisplays((_err, data) => {
        this.canvasWidth = this.screenWidth = data[0].width;
      });

      this.connectionPointList.push(new ConnectionPoint(150, 150));
      this.connectionPointList.push(new ConnectionPoint(200, 350));
    }

    build() {
      Column() {
        Scroll(this.scroller) {
          Canvas(this.context)
            .width(this.canvasWidth)
            .height('100%')
            .backgroundColor('#f1f3f5')
            .onReady(() => {
              this.draw();
            });
        }
        .scrollBar(BarState.Off)
        .scrollable(ScrollDirection.Horizontal)
        .height('70%')
        .width('100%');

        Button('添加').width('80%').margin({ top: 20 }).onClick(() => {
          this.count++;
          let x = 200 + 50 * this.count;
          this.y = this.y === 150 ? 350 : 150;
          this.canvasWidth = this.screenWidth + x;
          this.connectionPointList.push(new ConnectionPoint(x, this.y));
          this.draw();
          this.scroller.scrollTo({ xOffset: x - 300, yOffset: this.y });
        });
      }
      .width('100%')
      .height('100%');
    }

    draw() {
      this.context.clearRect(0, 0, this.canvasWidth, 400);
      this.context.beginPath();
      this.context.lineWidth = 2;
      this.context.lineJoin = 'round';
      this.context.moveTo(50, 250);
      this.connectionPointList.forEach(element => {
        this.context.lineTo(element.x, element.y);
        this.context.arc(element.x, element.y, 5, 0, Math.PI * 2);
      });
      this.context.stroke();
    }
  }
  ```

  实现效果如下：
  :   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/O4-oHn-UTJyqGHiWEjAvIQ/zh-cn_image_0000002628554750.png "点击放大")
* 方案二：固定Canvas宽度，通过手势来移动整个画布。
  1. 定义状态变量isMoving，当isMoving=true时为移动模式，当isMoving=false时为绘画模式。
  2. 为画布绑定滑动手势，根据状态变量isMoving值不同做不同逻辑。
     + onActionStart：手势开始时，如果是移动模式，记录当前平移量；如果是绘画模式，创建一个新的线条。
     + onActionUpdate：手势更新时，如果是移动模式，更新平移量；如果是绘画模式，更新线条的终点。然后重新绘制。
     + onActionEnd：手势结束时，重置当前绘制的线条。

       ```ts
       PanGesture({ fingers: 1 })
         .onActionStart(event => {
           if (this.isMoving) {
             this.lastTranslateX = this.translateX;
             this.lastTranslateY = this.translateY;
           } else {
             let line = new Line();
             line.start(event.fingerList[0].localX - this.translateX,
               event.fingerList[0].localY - this.translateY);
             this.current = line;
             this.list.add(line);
           }
         })
         .onActionUpdate(event => {
           if (this.isMoving) {
             this.translateX = this.lastTranslateX + event.offsetX;
             this.translateY = this.lastTranslateY + event.offsetY;
           } else {
             let line: Line = this.current as Line;
             line.lineTo(event.fingerList[0].localX - this.translateX,
               event.fingerList[0].localY - this.translateY);
           }
           this.paint();
         })
         .onActionEnd(() => {
           this.current = undefined;
         })
       ```
  3. 重置画布内容，并通过translate移动到最新的坐标点，遍历历史存放的坐标进行重新绘制。

     ```ts
     paint() {
       this.ctx.reset();
       this.ctx.translate(this.translateX, this.translateY);
       this.list.forEach(item => {
         if (item.isInCanvas(-this.translateX, -this.translateY, this.ctx.width, this.ctx.height)) {
           item.paint(this.ctx);
         }
       });
     }
     ```

  完整示例参考如下：

  ```ts
  import { LinkedList } from '@kit.ArkTS';

  @Entry
  @Component
  struct CanvasDrawTransLate {
    private ctx: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));
    private list: LinkedList<BaseItem> = new LinkedList();
    private current?: BaseItem;
    private translateX: number = 0;
    private translateY: number = 0;
    private lastTranslateX: number = 0;
    private lastTranslateY: number = 0;
    private isMoving: boolean = false;

    paint() {
      this.ctx.reset();
      this.ctx.translate(this.translateX, this.translateY);
      this.list.forEach(item => {
        if (item.isInCanvas(-this.translateX, -this.translateY, this.ctx.width, this.ctx.height)) {
          item.paint(this.ctx);
        }
      });
    }

    build() {
      Column() {
        Row() {
          Button('绘画')
            .onClick(() => {
              this.isMoving = false;
            });
          Button('移动')
            .margin({ left: 10 })
            .onClick(() => {
              this.isMoving = true;
            });
        };

        Canvas(this.ctx)
          .width('100%')
          .height('100%')
          .margin({ top: 10 })
          .backgroundColor('#f1f3f5')
          .gesture(
            GestureGroup(GestureMode.Exclusive,
              PanGesture({ fingers: 1 })
                .onActionStart(event => {
                  if (this.isMoving) {
                    this.lastTranslateX = this.translateX;
                    this.lastTranslateY = this.translateY;
                  } else {
                    let line = new Line();
                    line.start(event.fingerList[0].localX - this.translateX,
                      event.fingerList[0].localY - this.translateY);
                    this.current = line;
                    this.list.add(line);
                  }
                })
                .onActionUpdate(event => {
                  if (this.isMoving) {
                    this.translateX = this.lastTranslateX + event.offsetX;
                    this.translateY = this.lastTranslateY + event.offsetY;
                  } else {
                    let line: Line = this.current as Line;
                    line.lineTo(event.fingerList[0].localX - this.translateX,
                      event.fingerList[0].localY - this.translateY);
                  }
                  this.paint();
                })
                .onActionEnd(() => {
                  this.current = undefined;
                })
            )
          );
      };
    }
  }

  abstract class BaseItem {
    protected left: number = 0;
    protected top: number = 0;
    protected right: number = 0;
    protected bottom: number = 0;

    isInCanvas(x: number, y: number, width: number, height: number) {
      return !(this.right < x || this.left > x + width || this.top > y + height || this.bottom < y);
    }

    abstract paint(ctx: CanvasRenderingContext2D);
  }

  class Line extends BaseItem {
    path: Path2D = new Path2D();

    constructor() {
      super();
    }

    start(x: number, y: number) {
      this.path.moveTo(x, y);
      this.left = x;
      this.top = y;
    }

    lineTo(x: number, y: number) {
      this.path.lineTo(x, y);
      this.left = Math.min(x, this.left);
      this.top = Math.min(y, this.top);
      this.right = Math.max(x, this.right);
      this.bottom = Math.max(y, this.bottom);
    }

    paint(ctx: CanvasRenderingContext2D): void {
      ctx.strokeStyle = '#0097D4';
      ctx.lineWidth = 10;
      ctx.stroke(this.path);
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/s3zkoGexTOS4N6lxpBh6rg/zh-cn_image_0000002628394856.png "点击放大")

  两种实现方案对比如下：

  | 方案 | 实现方式 | 优点 | 缺点 |
  | --- | --- | --- | --- |
  | 方案一 | 使用Scroller实现画布扩展和内容移动。 | 实现简单、易于理解，画布尺寸可以扩展。 | 无法自由移动，场景单一。 |
  | 方案二 | 使用PanGesture实现画布平移和绘制。 | 可以自由移动，可以达到无限移动的效果。 | 实现较为复杂。 |

## 总结

本文提供了两种方案实现画布的扩展以及内容的移动。若需要改变画布尺寸，可以参照方案一实现，但是需要注意Canvas尺寸存在上限，超过10000px\*10000px则无法成功创建；若不需要修改画布尺寸，实现内容无限移动，可以使用方案二实现。
