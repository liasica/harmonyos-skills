---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-33
title: 如何解决Canvas画板设置CanvasRenderingContext2D线条样式失败的问题
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何解决Canvas画板设置CanvasRenderingContext2D线条样式失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:89451099440613789ba7594e460904a6827df2ca927cc24bc35d80eb11d3720a
---

## 问题现象

在Tab页面中包含三个Canvas画板。尽管在配置参数时为所有画板设置了相同的线条粗细和颜色样式，但实际显示结果中，第一个画板的线条样式与后两个画板存在差异，具体表现为线条粗细或颜色不一致。

问题代码示例参考如下：

```ts
// 画板
@Component
export struct CanvasView {
  @ObjectLink dataModel: CanvasDataModel;
  // 是否显示画板边框
  showBorder: boolean = true;
  // 画笔颜色
  brushColor: Color | string = Color.Red;
  // 画笔粗细
  @Prop brushSize: number = 6;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private lastX: number = 0;
  private lastY: number = 0;
  private isDown: boolean = false;
  private panOption: PanGestureOptions = new PanGestureOptions({
    direction: PanDirection.All,
    distance: 0.6,
    fingers: 1
  });
  private canvasLoaded: boolean = false
  // 绘制
  private draw(startX: number, startY: number, endX: number, endY: number) {
    this.context.moveTo(startX, startY);
    this.context.lineTo(endX, endY);
    this.context.stroke();
  };

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Stack() {
        // 画板
        Canvas(this.context)
          .height('100%')
          .width('100%')
          .padding(10)
          .borderColor(Color.Grey)
          .borderWidth(this.showBorder ? 1 : 0)
          .backgroundColor(Color.Gray)
          .onReady(() => {
            if (!this.canvasLoaded) {
              this.canvasLoaded = true;
              this.context.font = '60px sans-serif'
              this.context.lineWidth = this.brushSize
              this.context.strokeStyle = this.brushColor
              this.context.lineCap = "round"
              this.context.lineJoin = "round"
              console.info(`画板信息(${this.dataModel.signType})onReady：` + this.context.width + " - " +
              this.context.height);
            }          })
          .gesture(
            PanGesture(this.panOption)
              .onActionStart((event: GestureEvent) => { // 滑动手势识别回调
                this.isDown = true;
                if (event.fingerList.length > 0) {
                  this.lastX = event.fingerList[0].localX;
                  this.lastY = event.fingerList[0].localY;
                }
                this.context.beginPath();
              })
              .onActionUpdate((event: GestureEvent) => { // 滑动手势更新回调
                if (this.isDown) {
                  if (event.fingerList.length > 0) {
                    let _x = event.fingerList[0].localX;
                    let _y = event.fingerList[0].localY;
                    this.draw(this.lastX, this.lastY, _x, _y);
                    this.lastX = _x;
                    this.lastY = _y;
                  }
                }
              })
              .onActionEnd(() => { // 长按手势结束回调
                this.isDown = false;
                this.context.closePath();
              })
          )
      }
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
  }
}
```

## 背景知识

* ArkUI组件生命周期与初始化时序：在ArkUI中，组件属性初始化（如[@Prop装饰器](../harmonyos-guides/arkts-prop.md)、[@State装饰器](../harmonyos-guides/arkts-state.md)）和生命周期回调（如onReady、aboutToAppear）的执行顺序可能不同步。
* ArkUI属性传递机制：@Prop用于父组件向子组件传递单向绑定的属性。若父组件未显式传递值，子组件会使用自身定义的默认值。但默认值的同步可能受组件初始化顺序影响。
* Canvas上下文配置：CanvasRenderingContext2D的配置（如[lineWidth](../harmonyos-references/ts-components-canvas-common-property.md#linewidth)、[strokeStyle](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md#strokestyle)）需要在画布初始化（onReady）时完成。若依赖外部属性（如brushSize），需确保属性值在onReady触发前已正确赋值。

## 问题定位

1. 第一个画板的onReady回调可能早于brushSize/brushColor属性初始化完成，可能为初始化时序问题。
2. brushSize使用@Prop传递但未设置默认值同步机制，有可能在属性传递机制上出现问题。

## 分析结论

在onReady中打印的日志显示context.width和context.height并未初始化完成三个画板的样式，说明Canvas尺寸尚未确定时已进行绘制设置，所以是初始化时序的问题。前后日志如图：问题日志：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/dWIP9XfjRPObPzL1D6cW1g/zh-cn_image_0000002628553250.png "点击放大")

修复日志：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/COEJvwH2S_WKBZ-8OuzW-Q/zh-cn_image_0000002658912561.png "点击放大")

## 修改建议

@Prop传递数据时具有一个延迟效果，可以通过设置setTimeout等待数据传递完成后再开始绘图，确保Canvas尺寸就绪：

```ts
.onReady(() => {
  // 添加尺寸判断
  if (this.context.width === 0 || this.context.height === 0) {
    setTimeout(() => {
      this.initCanvas();
    }, 16); // 延迟16ms等待布局完成
  } else {
    this.initCanvas();
  }
})
```

完整示例参考如下：

```ts
import { window } from '@kit.ArkUI';
import common from '@ohos.app.ability.common';
import { image } from '@kit.ImageKit';
import { Size } from '@kit.ArkUI';

// 画板
@Component
export struct CanvasView {
  @ObjectLink dataModel: CanvasDataModel;
  // 是否显示画板边框
  showBorder: boolean = true;
  // 画笔颜色
  brushColor: Color | string = Color.Red;
  // 画笔粗细
  @Prop brushSize: number = 6;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private lastX: number = 0;
  private lastY: number = 0;
  private isDown: boolean = false;
  private panOption: PanGestureOptions = new PanGestureOptions({
    direction: PanDirection.All,
    distance: 0.6,
    fingers: 1
  });

  // 绘制
  private draw(startX: number, startY: number, endX: number, endY: number) {
    this.context.moveTo(startX, startY);
    this.context.lineTo(endX, endY);
    this.context.stroke();
  };

  // 新增初始化方法
  private initCanvas() {
    this.context.font = '60px sans-serif';
    this.context.lineWidth = this.brushSize;
    this.context.strokeStyle = this.brushColor;
    this.context.lineCap = 'round';
    this.context.lineJoin = 'round';
    console.info(`画板信息(${this.dataModel.signType})onReady：` + this.context.width + ' - ' +
    this.context.height);
  };

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Stack() {
        // 画板
        Canvas(this.context)
          .height('100%')
          .width('100%')
          .padding(10)
          .borderColor(Color.Grey)
          .borderWidth(this.showBorder ? 1 : 0)
          .backgroundColor(Color.Gray)
          .onReady(() => {
            // 添加尺寸判断
            if (this.context.width === 0 || this.context.height === 0) {
              setTimeout(() => {
                this.initCanvas();
              }, 16); // 延迟16ms等待布局完成
            } else {
              this.initCanvas();
            }
          })
          .gesture(
            PanGesture(this.panOption)
              .onActionStart((event: GestureEvent) => { // 滑动手势识别回调
                this.isDown = true;
                if (event.fingerList.length > 0) {
                  this.lastX = event.fingerList[0].localX;
                  this.lastY = event.fingerList[0].localY;
                }
                this.context.beginPath();
              })
              .onActionUpdate((event: GestureEvent) => { // 滑动手势更新回调
                if (this.isDown) {
                  if (event.fingerList.length > 0) {
                    let _x = event.fingerList[0].localX;
                    let _y = event.fingerList[0].localY;
                    this.draw(this.lastX, this.lastY, _x, _y);
                    this.lastX = _x;
                    this.lastY = _y;
                  }
                }
              })
              .onActionEnd(() => { // 长按手势结束回调
                this.isDown = false;
                this.context.closePath();
              })
          );
      }
      .layoutWeight(1);
    }
    .width('100%')
    .height('100%');
  }
}

export class DrawingInfo {
  imageData?: image.PixelMap;
  imageSize?: Size;
}
;

@Observed
export class CanvasDataModel {
  // 关联的签字类型
  signType: string = '1';
  // 图像
  drawingInfo?: DrawingInfo;
  // 签署姓名的时候需要签的字
  signText?: string;
}
;

@Entry
@Component
struct DrawingCanvasPageView {
  @State currentIndex: number = 0;
  @State canvasDataModelList: CanvasDataModel[] = [];
  private tabController: TabsController = new TabsController();

  @Builder
  TabBuilder(index: number, type: string) {
    Column() {
      Text(type)
        .fontColor(this.currentIndex === index ? Color.Green : '#182431')
        .fontSize(14)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(18);
      Divider()
        .strokeWidth(2)
        .color(Color.Green)
        .opacity(this.currentIndex === index ? 1 : 0);
    };
  };

  // 设置为横屏展示
  onPageShow(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(window.Orientation.LANDSCAPE);
    });
  };

  // 获取当前日期
  getCurrentTime() {
    let dt = new Date();
    return `${dt.getFullYear()}/${dt.getMonth() + 1}/${dt.getDate()}`;
  };

  aboutToAppear(): void {
    // 普通签字
    this.canvasDataModelList.push({
      signType: '1'
    });
    this.canvasDataModelList.push({
      signType: '2'
    });
    this.canvasDataModelList.push({
      signType: '3'
    });
  };

  build() {
    Flex({ direction: FlexDirection.Column }) {
      Flex({
        direction: FlexDirection.Row,
        justifyContent: FlexAlign.SpaceBetween,
        alignItems: ItemAlign.Center
      }) {
        // 日期提示
        Text(
          `请在下方签字（当前日期：${this.getCurrentTime()}）`,
        )
          .fontColor(Color.Grey)
          .fontSize(16)
          .textAlign(TextAlign.Center);
        // 完成签字
        Text('完成')
          .fontWeight(FontWeight.Bold)
          .width(44)
          .height(44);
      }
      .width('100%')
      .padding({ left: 16, right: 16 });

      // 画板区域
      Tabs({ barPosition: BarPosition.Start, controller: this.tabController }) {
        ForEach(this.canvasDataModelList, (item: CanvasDataModel, index) => {
          TabContent() {
            // 画板
            CanvasView({
              dataModel: item
            });
          }
          .width('100%')
          .height('100%')
          .tabBar(this.TabBuilder(index, item.signType));
        });
      }
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(120)
      .barHeight(45)
      .animationDuration(100)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .width('100%')
      .height('100%');
    }
    .width('100%')
    .height('100%');
  }
}
```
