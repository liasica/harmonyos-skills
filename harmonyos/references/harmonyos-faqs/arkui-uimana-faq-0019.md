---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0019
title: ArkUI手势常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI手势常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:377e4a471c065c929486aa38b6fb519b9c6e35be349974ec2b618fae2ecabb37
---

**Q：在List组件中，单个ListItem在同时设置拖拽功能与长按功能时，实际运行之后会产生冲突，如何解决单个ListItem拖拽功能和长按功能的冲突问题？**

**A**：由于在ListItem中设置单独的长按事件会与拖拽事件产生冲突，因此建议放弃List本身的拖拽事件，使用滑动手势PanGesture，自行实现拖拽过程的逻辑，然后再通过组合手势的功能，去实现其他的长按事件。

参考代码如下：

```ts
import curves from '@ohos.curves';

@Entry
@Component
struct Page {
  // 元素数组
  @State numbers: number[] = [];
  // 多列
  private str: string = '';
  row: number = 4;
  // 元素数组中最后一个元素的索引
  @State lastIndex: number = 0;
  @State dragItem: number = -1;
  @State scaleItem: number = -1;
  item: number = -1;
  private dragRefOffsetX: number = 0;
  private dragRefOffsetY: number = 0;
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  private FIX_VP_X: number = 108;
  private FIX_VP_Y: number = 120;

  aboutToAppear() {
    for (let i = 1; i <= 36; i++) {
      this.numbers.push(i);
    }
    this.lastIndex = this.numbers.length - 1;
    // 多列
    for (let i = 0; i < this.row; i++) {
      this.str = this.str + '1fr ';
    }
  }

  itemMove(index: number, newIndex: number): void {
    console.info('index:' + index + ' newIndex:' + newIndex);
    if (!this.isDraggable(newIndex)) {
      return;
    }
    let tmp = this.numbers.splice(index, 1);
    this.numbers.splice(newIndex, 0, tmp[0]);
  }

  // 向下滑
  down(index: number): void {
    if (!this.isDraggable(index + this.row)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    // 多列
    this.itemMove(index, index + this.row);
  }

  // 向下滑(右下角为空)
  down2(index: number): void {
    if (!this.isDraggable(index + 3)) {
      return;
    }
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + 3);
  }

  // 向上滑
  up(index: number): void {
    if (!this.isDraggable(index - this.row)) {
      return;
    }
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - this.row);
  }

  // 向左滑
  left(index: number): void {
    if (!this.isDraggable(index - 1)) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.itemMove(index, index - 1);
  }

  // 向右滑
  right(index: number): void {
    if (!this.isDraggable(index + 1)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.itemMove(index, index + 1);
  }

  // 向右下滑
  lowerRight(index: number): void {
    if (!this.isDraggable(index + this.row + 1)) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + this.row + 1);
  }

  // 向右上滑
  upperRight(index: number): void {
    if (!this.isDraggable(index - (this.row - 1))) {
      return;
    }
    this.offsetX -= this.FIX_VP_X;
    this.dragRefOffsetX += this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - (this.row - 1));
  }

  // 向左下滑
  lowerLeft(index: number): void {
    if (!this.isDraggable(index + (this.row - 1))) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY -= this.FIX_VP_Y;
    this.dragRefOffsetY += this.FIX_VP_Y;
    this.itemMove(index, index + (this.row - 1));
  }

  // 向左上滑
  upperLeft(index: number): void {
    if (!this.isDraggable(index - (this.row + 1))) {
      return;
    }
    this.offsetX += this.FIX_VP_X;
    this.dragRefOffsetX -= this.FIX_VP_X;
    this.offsetY += this.FIX_VP_Y;
    this.dragRefOffsetY -= this.FIX_VP_Y;
    this.itemMove(index, index - (this.row + 1));
  }

  // 通过元素的索引，控制对应元素是否能移动排序
  isDraggable(index: number): boolean {
    console.info(`index: ${index}`);
    return index > -1; // 恒成立，所有元素均可移动排序
  }

  build() {
    Column() {
      Grid() {
        ForEach(this.numbers, (item: number) => {
          GridItem() {
            Text(item + '')
              .fontSize(16)
              .width('100%')
              .textAlign(TextAlign.Center)
              .height(100)
              .borderRadius(10)
              .backgroundColor(0xFFFFFF)
              .shadow(this.scaleItem == item ? {
                radius: 70,
                color: '#15000000',
                offsetX: 0,
                offsetY: 0
              } :
                {
                  radius: 0,
                  color: '#15000000',
                  offsetX: 0,
                  offsetY: 0
                })
              .animation({ curve: Curve.Sharp, duration: 300 });
          }
          // 添加震动
          .onTouch(() => {
          })
          .onAreaChange((oldVal, newVal) => {
            // 多列
            this.FIX_VP_X = Math.round(newVal.width as number);
            this.FIX_VP_Y = Math.round(newVal.height as number);
            console.info(`oldVal:${JSON.stringify(oldVal)}`);
          })
          // 指定固定GridItem不响应事件
          .hitTestBehavior(this.isDraggable(this.numbers.indexOf(item)) ? HitTestMode.Default : HitTestMode.None)
          .scale({ x: this.scaleItem == item ? 1.05 : 1, y: this.scaleItem == item ? 1.05 : 1 })
          .zIndex(this.dragItem == item ? 1 : 0)
          .translate(this.dragItem == item ? { x: this.offsetX, y: this.offsetY } : { x: 0, y: 0 })
          .padding(10)
          .gesture(
            GestureGroup(GestureMode.Sequence,
              LongPressGesture({ repeat: true, duration: 50 })
                .onAction((event?: GestureEvent) => {
                  console.info(`event: ${event}`);
                  this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                    this.scaleItem = item;
                  });
                })
                .onActionEnd(() => {
                  this.getUIContext().animateTo({ curve: Curve.Friction, duration: 300 }, () => {
                    this.scaleItem = -1;
                  });
                }),
              PanGesture({ fingers: 1, direction: null, distance: 0 })
                .onActionStart(() => {
                  this.dragItem = item;
                  this.dragRefOffsetX = 0;
                  this.dragRefOffsetY = 0;
                })
                .onActionUpdate((event: GestureEvent) => {
                  this.offsetY = event.offsetY - this.dragRefOffsetY;
                  this.offsetX = event.offsetX - this.dragRefOffsetX;
                  console.info(`移动过程中event.offsetY：${event.offsetY}`,
                    ` this.dragRefOffsetY: ${this.dragRefOffsetY}`, `this.offsetY: ${this.offsetY}`);
                  console.info(`移动过程中event.offsetX：${event.offsetX}`,
                    ` this.dragRefOffsetX: ${this.dragRefOffsetX}`, `this.offsetX: ${this.offsetX}`);
                  this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    let index = this.numbers.indexOf(this.dragItem);
                    console.info('index= ', index);
                    if (this.offsetY >= this.FIX_VP_Y / 2 &&
                      (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
                      && (index + this.row <= this.lastIndex)) {
                      // 向下滑
                      this.down(index);
                    } else if (this.offsetY <= -this.FIX_VP_Y / 2 &&
                      (this.offsetX <= this.FIX_VP_X / 2 && this.offsetX >= -this.FIX_VP_X / 2)
                      && index - this.row >= 0) {
                      // 向上滑
                      this.up(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 &&
                      (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
                      && !(((index - (this.row - 1)) % this.row == 0) || index == this.lastIndex)) {
                      // 向右滑
                      this.right(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 &&
                      (this.offsetY <= this.FIX_VP_Y / 2 && this.offsetY >= -this.FIX_VP_Y / 2)
                      && !(index % this.row == 0)) {
                      // 向左滑
                      this.left(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && ((index + this.row + 1 <= this.lastIndex && !((index - (this.row - 1)) % this.row == 0)) ||
                        !((index - (this.row - 1)) % this.row == 0))) {
                      // 向右下滑
                      this.lowerRight(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
                      && !((index - this.row < 0) || ((index - (this.row - 1)) % this.row == 0))) {
                      // 向右上滑
                      this.upperRight(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && (!(index % this.row == 0) && (index + (this.row - 1) <= this.lastIndex))) {
                      // 向左下滑
                      this.lowerLeft(index);
                    } else if (this.offsetX <= -this.FIX_VP_X / 2 && this.offsetY <= -this.FIX_VP_Y / 2
                      && !((index <= this.row - 1) || (index % this.row == 0))) {
                      // 向左上滑
                      this.upperLeft(index);
                    } else if (this.offsetX >= this.FIX_VP_X / 2 && this.offsetY >= this.FIX_VP_Y / 2
                      && (index == this.lastIndex)) {
                      // 向右下滑(右下角为空)
                      this.down2(index);
                    }
                  });
                })
                .onActionEnd(() => {
                  this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                    this.dragItem = -1;
                  });
                  this.getUIContext().animateTo({
                    curve: curves.interpolatingSpring(14, 1, 170, 17), delay: 150
                  }, () => {
                    this.scaleItem = -1;
                  });
                })
            )
              .onCancel(() => {
                this.getUIContext().animateTo({ curve: curves.interpolatingSpring(0, 1, 400, 38) }, () => {
                  this.dragItem = -1;
                });
                this.getUIContext().animateTo({
                  curve: curves.interpolatingSpring(14, 1, 170, 17)
                }, () => {
                  this.scaleItem = -1;
                });
              })
          );
        }, (item: number) => item.toString());
      }
      .width('90%')
      .editMode(true)
      .scrollBar(BarState.Off)
      // 多列
      .columnsTemplate(this.str);
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .width('100%').height('100%').backgroundColor('#f1f3f5').padding({ top: 5 });
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/vx3-BkqURCqWrZhU-_nvLw/zh-cn_image_0000002765940926.png "点击放大")

**Q：Grid上下左右拖拽动画如何实现？**

**A**：在跨行或跨列场景下，可以通过自定义Grid布局、自定义手势和显式动画来实现拖拽交换的效果。

**Q：点击一个组件的右下角，如何实现组件跟随手指移动进行平移、缩放和旋转操作？**

**A**：实现思路：

1. 旋转和缩放部分：使用矩阵实现，通过构建一个以组件中心为原点的坐标系，初始坐标是从中心指向边框右下角。手指移动时，在初始坐标基础上增加手指移动的向量，即可得到当前手指相对于组件中心为原点的坐标系的坐标。从而可以计算到原点的距离和旋转的角度，该距离除以初始距离即为缩放比例，该角度减去初始角度即为旋转角度。注意：每次计算当前手指相对于中心的坐标时，需要使用初始坐标加上手指偏移距离得到的坐标进行上一次旋转缩放的矩阵映射，否则会有偏差。
2. 平移部分：使用offset实现，记录上一次移动的终点位置，再加上本次手指移动的距离，即可实现平移。注意：由于平移的手势绑定在旋转缩放的组件上，所以直接使用会有偏差，必须对该坐标也进行一次相同的旋转缩放映射。

实现代码如下：

```ts
import { matrix4 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct ImageMovePage {
  // 声明平移矩阵
  @Local matrix: matrix4.Matrix4Transit = matrix4.identity().copy();
  // 声明手势前的矩阵
  private rotateAndScaleMatrix: matrix4.Matrix4Transit = matrix4.identity().copy();
  // 声明初始位置坐标
  private initStackX: number = 0;
  private initStackY: number = 0;
  // 声明初始宽高
  private initStackWidth: number = 0;
  private initStackHeight: number = 0;
  // 声明中心点坐标
  private initCenterX: number = 0;
  private initCenterY: number = 0;
  // 声明初始半径
  private initR: number = 0;
  // 声明初始角度
  private initAngle: number = 0;
  // 声明手势开始时的坐标
  private startStackX: number = 0;
  private startStackY: number = 0;
  // 声明当前位置
  @Local currentX: number = 0;
  @Local currentY: number = 0;
  // 声明缩放比例
  @Local stackScale: number = 1;
  // 声明当前旋转角度
  @Local stackRotate: number = 0;
  // 声明移动时手指的初始坐标
  private initFingerX: number = -1;
  private initFingerY: number = -1;
  lastFingerX: number = 0;
  lastFingerY: number = 0;

  // 在即将出现时初始化数据
  aboutToAppear(): void {
    this.init();
  }

  // 初始化方法：获取初始位置
  init() {
    let observer = this.getUIContext().getUIInspector().createComponentObserver('target');
    observer.on('layout', () => {
      let node = this.getUIContext().getAttachedFrameNodeById('target');
      if (node) {
        let position = node.getPositionToParent();
        this.initStackX = position.x;
        this.initStackY = position.y;
        let size = node.getMeasuredSize();
        this.initStackWidth = this.getUIContext().px2vp(size.width);
        this.initStackHeight = this.getUIContext().px2vp(size.height);
        this.initCenterX = this.initStackX + (this.initStackWidth >> 1);
        this.initCenterY = this.initStackY + (this.initStackHeight >> 1);
        this.initR = Math.sqrt((this.initStackWidth >> 1) * (this.initStackWidth >> 1) +
          (this.initStackHeight >> 1) * (this.initStackHeight >> 1));
        this.initAngle = Math.atan2((this.initStackHeight), (this.initStackWidth)) * 180 / Math.PI;
      }
      console.info(`x: ${this.initStackX}, y: ${this.initStackY}`);
      console.info(`width: ${this.initStackWidth}, height: ${this.initStackHeight}`);
      console.info(`centerX: ${this.initCenterX}, centerY: ${this.initCenterY}`);
      console.info(`initR: ${this.initR}, angle: ${this.initAngle}`);
      observer.off('layout');
    });
  }

  build() {
    NavDestination() {
      Stack() {
        Stack() {
          Stack({ alignContent: Alignment.BottomEnd }) {
            Text('harmonyos')
              .width(80)
              .height(80)
              .borderWidth(1)
              .borderColor('#0A59F7')
              .fontColor('#0A59F7');

            Text()
              .width(10)
              .height(10)
              .backgroundColor('#0A59F7');
            // 手势识别
            Text()
              .width(10)
              .height(10)
              .backgroundColor('#0A59F7')
              .gesture(
                PanGesture()
                  .onActionStart(event => {
                    console.info(`event: ${event}`);
                    // 记录上一次的矩阵
                    this.rotateAndScaleMatrix = this.matrix.copy();
                    // 获取手指位置
                    this.initFingerX = (this.initStackWidth >> 1);
                    this.initFingerY = (this.initStackHeight >> 1);
                  })
                  .onActionUpdate(event => {
                    // 获取当前坐标手指
                    let currentFingerX: number = this.initFingerX + event.offsetX;
                    let currentFingerY: number = this.initFingerY + event.offsetY;
                    // 映射手指坐标
                    let point = this.rotateAndScaleMatrix.copy().transformPoint([currentFingerX, currentFingerY]);
                    currentFingerX = point[0];
                    currentFingerY = point[1];
                    console.info(`event.offsetX: ${currentFingerX}, event.offsetY: ${currentFingerY}`);
                    // 获取半径
                    let r: number = Math.sqrt(currentFingerX * currentFingerX + currentFingerY * currentFingerY);
                    console.info(`半径r: ${r}, 初始半径：${this.initR}, 比率： ${r / this.initR}`);
                    // 获取cos和sin，判断象限
                    this.stackScale = (r / this.initR);
                    // 声明角度
                    let theta: number = Math.atan2(currentFingerY, currentFingerX) * 180 / Math.PI - this.initAngle;
                    // 判断象限
                    this.stackRotate = theta;
                    this.matrix = matrix4.identity().copy()
                      .scale({ x: r / this.initR, y: r / this.initR })
                      .rotate({ z: 1, angle: theta });
                  })
                  .onActionEnd(event => {
                    this.lastFingerX = this.initFingerX + event.offsetX;
                    this.lastFingerY = this.initFingerY + event.offsetY;
                    console.info(`旋转角度: ${this.stackRotate}, 缩放比例: ${this.stackScale}`);
                  })
              );
          }
          .transform(this.matrix)
          .gesture(
            PanGesture()
              .onActionStart(() => {
                this.startStackX = this.currentX;
                this.startStackY = this.currentY;
              })
              .onActionUpdate(event => {
                // 获取手指位置
                let point = this.matrix.copy().transformPoint([event.offsetX, event.offsetY]);
                this.currentX = this.startStackX + point[0];
                this.currentY = this.startStackY + point[1];
              })
              .onActionEnd(() => {
                console.info(`currentX: ${this.currentX}, currentY: ${this.currentY}`);
              })
          );
        }
        .id('target')
        .offset({ x: this.currentX, y: this.currentY });
      }
      .height('100%')
      .backgroundColor($r('sys.color.point_color_checked'))
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    };
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/yKxI9wdNSiqGXxQ4gIR69A/zh-cn_image_0000002765940938.png "点击放大")

**Q：横向的进度条嵌套在Scroll组件中，当触摸进度条时，手指不抬起进行拖动操作，若拖动操作起始为上下，那么后续的拖动只会影响Scroll的滚动。相反，若拖动操作起始为左右，那么后续拖动只会影响Slider进度条的变化，无法影响Scroll滚动。如何实现在单次拖动内Scroll组件和Slider进度条同时响应拖动操作？问题代码如下：**

```ts
@Entry
@Component
struct Index {
  dataArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 171, 172, 173, 174];
  @State eventType: string = ''
  @State sliderNum: number[] = []
  @State offsetX: number = 0
  @State offsetY: number = 0
  scroller: Scroller = new Scroller()

  aboutToAppear(): void {
    // 初始化进度条进度参数
    for (let i = 0; i < this.dataArr.length; i++) {
      this.sliderNum[i] = 0
    }
  }

  build() {
    Scroll() {
      WaterFlow({ scroller: this.scroller }) {
        ForEach(this.dataArr, (item: number, index: number) => {
          FlowItem() {
            Column() {
              Slider({
                value: this.sliderNum[index],
                min: 0,
                max: 100,
                style: SliderStyle.OutSet
              })
                .enabled(true) // 取消进度条交互，防止消费拖拽事件
            }
          }
          .height(100)
        })
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%')
    }
    .height('100%')
    .width('100%')
  }
}
```

**A**：使用拖动手势PanGesture可以根据手指在每个方向上的移动距离来做控制。后续仅需解决手势绑定在哪个组件上，以及如何使用手势内部参数。

1. 手势绑定的组件：

   只有当手指在Slider上拖动时，才会涉及到影响两个方向的不同组件，因此，将手势绑定在Slider上。这样方便判断拖动的是具体哪一个Slider，而且也不影响其他组件的点击拖动，降低耦合度，以及系统性能消耗。
2. 内部实现手势参数：

   通过[scrollBy](../harmonyos-references/ts-container-scroll.md#scrollby9)影响外部滑动组件。

   通过[SliderOptions](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明)对象中的value影响内部进度条组件。

即在进度条上绑定拖动手势，此时需要将Slider通过额外的容器进行包裹，手势绑定在容器上。而Slider本身使用enabled或者hitTestBehavior.None属性取消掉本身对于手势的消费。手势需额外绑定的原因为当组件消费手势，组件额外绑定的手势将不生效，因此需要将手势透传到父组件进行处理，通过定位思路中的内部手势参数即可获得对应的调控接口，实现代码如下：

```ts
@Entry
@Component
struct ScrollSlider {
  dataArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 171, 172, 173, 174];
  @State sliderNum: number[] = [];
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  scroller: Scroller = new Scroller();

  aboutToAppear(): void {
    // 初始化进度条进度参数
    for (let i = 0; i < this.dataArr.length; i++) {
      this.sliderNum[i] = 0;
    }
  }

  build() {
    Scroll() {
      WaterFlow({ scroller: this.scroller }) {
        ForEach(this.dataArr, (index: number) => {
          FlowItem() {
            Column() {
              Slider({
                value: this.sliderNum[index],
                min: 0,
                max: 70,
                style: SliderStyle.OutSet
              })
                .margin(16)
                .enabled(false); // 取消进度条交互，防止消费拖拽事件
            }
            .hitTestBehavior(HitTestMode.Block)
            .gesture(
              PanGesture()
                .onActionStart(() => {
                  this.offsetX = 0;
                  this.offsetY = 0;
                })
                .onActionUpdate((event: GestureEvent) => { // 拖动为实时拖动，因此每次拖动的参数需要用当前拖动距离与上次拖动距离做减法
                  if (event) {
                    if (event.offsetY !== 0) {
                      this.scroller.scrollBy(0, -this.getUIContext().px2vp(event.offsetY - this.offsetY));
                      this.offsetY = event.offsetY;
                    }
                    if (event.offsetX !== 0) {
                      this.sliderNum[index] += this.getUIContext().px2vp(event.offsetX - this.offsetX);
                      this.offsetX = event.offsetX;
                    }
                  }
                })
            );
          }.height(100);
        });
      }
      .columnsTemplate('1fr 1fr')
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('100%');
    }
    .height('100%')
    .width('100%');
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/wO0JmuKJQE2MUXQZoR5qJg/zh-cn_image_0000002795500381.png "点击放大")

**说明** 

1. 手势不要绑定在Scroll组件上，会增加对控制哪一个进度条的判断的问题。
2. 拖动为实时拖动，因此每次拖动的参数需要用当前拖动距离与上次拖动距离做减法。
3. 建议将拖动距离进行单位转换。

**Q：当Swiper组件与子组件发生手势冲突，或者Swiper组件的滑动与嵌套了Swiper的外部组件的gesture手势冲突时，如何解决？**

**A**：Swiper嵌套的页面包含[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)时，使Canvas不响应左右滑动事件，不会触发Swiper切换显示。可以通过以下步骤实现：

1. 通过[priorityGesture](../harmonyos-references/ts-gesture-settings.md#prioritygesture)给画布绑定优先识别手势，使得画布组件Canvas优先于其他组件响应滑动事件。
2. 通过[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)来处理滑动冲突，确保在滑动Swiper时，Canvas组件不会被滑动。
3. 在主组件Index中，创建Swiper组件，同时在Swiper中调用自定义组件CanvasExample，使得画布在Swiper的页面中可见。

示例代码如下：

```ts
@Component
struct CanvasExampleOne {
  // 用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  // 用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Column() {
      Text('Canvas');
      // 在canvas中调用CanvasRenderingContext2D对象。
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffffff')
        .onReady(() => {
          // 可以在这里绘制内容。
          this.context.strokeRect(50, 50, 200, 150);
        })
        .priorityGesture(GestureGroup(GestureMode.Exclusive,
          SwipeGesture()
            .onAction(() => {
              console.info(`Canvas响应，swiper不响应`);
            })
        ))
        .hitTestBehavior(HitTestMode.Block)
        .width('80%')
        .height('50%');
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffbfffff');
  }
}

@Entry
@Component
struct GestureDragAndSwiper {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      Text('0')
        .width('100%')
        .height('100%')
        .backgroundColor('#ff96b1ff')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('1')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffffdcc6')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      Text('2')
        .width('100%')
        .height('100%')
        .backgroundColor('#ffc9ffd9')
        .textAlign(TextAlign.Center)
        .fontSize(30);
      CanvasExampleOne();
    }.loop(false);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/XdsqqkYASoKd0w_AT8w1eg/zh-cn_image_0000002766100870.png "点击放大")

**Q：场景二中除了使用优先识别手势priorityGesture，还有其他替代方案吗？**

A：可以使用自定义手势判定方法[onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin)，实现对[手势的自定义判定](../harmonyos-references/ts-gesture-customize-judge.md#示例1自定义手势判定)。

**Q：在业务中需要通过手势控制视频播放，但是根据以下代码无法实现通过手势滑动屏幕控制音量、亮度和进度。**

```ts
@Entry
@Component
export struct Index {
  build() {
    // ...
    Stack() {
      Column() {
        // 组件B
        // ...
      }
      .gesture(PanGesture()) // 期望能够透传到这个地方
      Column() {
        // 组件C，内部包含DEF三个组件，期望能够把这个手势事件透传给上边的组件
        Blank()
          .parallelGesture(null, GestureMask.IgnoreInternal)
        // ...
      }
      .parallelGesture(null, GestureMask.IgnoreInternal)
    }
    // ...
  }
}
```

如下层叠布局：B组件表示音量控制、亮度等下层组件，D/E/F表示上层组件。

预期效果：组件D、E、F上的手势操作能够透传到B组件上控制音量、亮度变化等操作，而不执行C、D、E、F上的手势操作。

实际问题：手势操作只在上层D、E、F组件上适配，无法将手势操作透传给下层目标组件B。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/9fbKHPlsSfObpGYvp6uU-A/zh-cn_image_0000002795339639.png "点击放大")

**A**：针对业务场景代码梳理UI层级，预期将上层手势响应事件不作处理透传到下层组件进行处理，根据hitTestBehavior类型说明，选择HitTestMode.None模式，达到上层不响应，传递至子节点响应。

上述场景实现代码：

```ts
@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Column() {
          Text('ColumnB').margin({ top: 10 });
        }
        .onTouch(() => {
          console.info('Executing a gesture:ComponentB');
        })
        .gesture(TapGesture({ count: 1 }))
        .backgroundColor('#f1f3f5')
        .borderRadius(10)
        .width('90%')
        .height('90%');
      };

      // 组件C设置.hitTestBehavior(HitTestMode.None)，自身不响应触摸测试
      ComponentC()
        .onTouch(() => {
          console.info('Executing a gesture:ComponentC');
        })
        .gesture(TapGesture({ count: 1 }))
        .backgroundColor('#E5E5EA')
        .borderRadius(10)
        .width('80%')
        .height('80%')
        .hitTestBehavior(HitTestMode.None);
    }
    .onTouch(() => {
      console.info('Executing a gesture:StackA');
    })
    .gesture(TapGesture({ count: 1 }))
    .width('100%')
    .height('100%')
    .hitTestBehavior(HitTestMode.None);
  }
}

@Component
struct ComponentC {
  build() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
      Text('ColumnC')
        .width('100%')
        .textAlign(TextAlign.Center);
      Column() {
        Text('ColumnD')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentD');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#D1D1D6')
      .height('28%')
      .width('100%');

      // 组件E设置.hitTestBehavior(HitTestMode.None)，自身不响应触摸测试
      Column() {
        Text('ColumnE')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentE');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#C7C7CC')
      .height('28%')
      .width('100%')
      .hitTestBehavior(HitTestMode.None);

      Column() {
        Text('ColumnF')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentF');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#999999')
      .height('28%')
      .width('100%');

      Text('ColumnC')
        .width('100%')
        .textAlign(TextAlign.Center);
    }.width('100%')
    .height('100%')
    .hitTestBehavior(HitTestMode.None);
  }
}
```

如下效果图点击图中不同颜色区域的手势传递结果验证日志：

触摸D区域：

```txt
Executing a gesture:ComponentD
Executing a gesture:ComponentB
```

触摸E区域：

```txt
Executing a gesture:ComponentB
```

触摸F区域：

```txt
Executing a gesture:ComponentF
Executing a gesture:ComponentB
```

触摸C区域：

```txt
Executing a gesture:ComponentB
```

触摸B区域：

```txt
Executing a gesture:ComponentB
```

触摸A区域：无相关日志打印。

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/mZ8E4EE5Te-XHiBncgYxVw/zh-cn_image_0000002766100874.png "点击放大")

**Q：页面有多个按钮，其中一个按钮用于控制按钮能否拖动，如何实现按钮可通过滑动手势改变位置，并在退出应用时保存按钮的位置？**

**A**：可以通过为组件绑定滑动手势[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)，识别滑动动作，通过translate实现改变位置，并通过PersistentStorage持久化保存按钮组件的translate位移的值，使组件位置在应用重新启动时与关闭时一致。

示例代码如下：

* EntryAbility.ets文件，onWindowStageCreate中初始化PersistentStorage。

  ```ts
  onWindowStageCreate(windowStage: window.WindowStage): void {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        // 初始化PersistentStorage
        PersistentStorage.persistProp('customerFlag', false);
        PersistentStorage.persistProp('offsetX', 0);
        PersistentStorage.persistProp('offsetY', 0);
        PersistentStorage.persistProp('offset2X', 0);
        PersistentStorage.persistProp('offset2Y', 0);
      });
    }
  ```

* Index.ets文件，获取持久化的按钮位置信息，实现滑动手势改变位置功能，并将新的按钮位置信息持久化。

  ```ts
  @Entry
  @Component
  struct Index {
    @State flag: boolean = false;
    positionX: number = 0;
    positionY: number = 0;
    @State offsetX: number = 0;
    @State offsetY: number = 0;
    @State offset2X: number = 0;
    @State offset2Y: number = 0;

    aboutToAppear(): void {
      // AppStorage获取对应值
      this.flag = AppStorage.get<boolean>('customerFlag') ?? false;
      this.offsetX = AppStorage.get<number>('offsetX') ?? 0;
      this.offsetY = AppStorage.get<number>('offsetY') ?? 0;
      this.offset2X = AppStorage.get<number>('offset2X') ?? 0;
      this.offset2Y = AppStorage.get<number>('offset2Y') ?? 0;
    }

    build() {
      Column({ space: 10 }) {
        Row() {
          Button(this.flag ? '完成' : '自定义位置')
            .onClick(() => {
              this.flag = !this.flag;
              // AppStorage设置对应属性值
              AppStorage.setOrCreate('customerFlag', this.flag);
            });
        }
        .width('100%')
        .height(80)
        .justifyContent(FlexAlign.End)
        .margin({ right: 10 });

        Button('组件1')
          .zIndex(3)
          // 组件平移位置
          .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
          .gesture(
            // 绑定拖动手势
            PanGesture()
              .onActionStart(() => {
                this.positionX = this.offsetX;
                this.positionY = this.offsetY;
              }) // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
              .onActionUpdate((event: GestureEvent | undefined) => {
                if (!this.flag) {
                  return;
                }
                if (event) {
                  this.offsetX = this.positionX + event.offsetX;
                  this.offsetY = this.positionY + event.offsetY;
                }
              })
              .onActionEnd(() => {
                // AppStorage设置对应属性值
                AppStorage.setOrCreate('offsetX', this.offsetX);
                AppStorage.setOrCreate('offsetY', this.offsetY);
              })
          );

        Button('组件2')
          .zIndex(2)
          // 组件平移位置
          .translate({ x: this.offset2X, y: this.offset2Y, z: 0 })
          .gesture(
            // 绑定拖动手势
            PanGesture()
              .onActionStart(() => {
                this.positionX = this.offset2X;
                this.positionY = this.offset2Y;
              }) // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
              .onActionUpdate((event: GestureEvent | undefined) => {
                if (!this.flag) {
                  return;
                }
                if (event) {
                  this.offset2X = this.positionX + event.offsetX;
                  this.offset2Y = this.positionY + event.offsetY;
                }
              })
              .onActionEnd(() => {
                // AppStorage设置对应属性值
                AppStorage.setOrCreate('offset2X', this.offset2X);
                AppStorage.setOrCreate('offset2Y', this.offset2Y);
              })
          );
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/mSdZnDz1Si-mTGClgt2ZlQ/zh-cn_image_0000002795499441.png "点击放大")
