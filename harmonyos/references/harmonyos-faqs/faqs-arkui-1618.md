---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1618
title: ForEach实现刻度尺相关效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ForEach实现刻度尺相关效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0f53b0f7e81134a723d1348bde099c4135d6731a3f57efdcea77560825a53f77
---

## 问题现象

* 场景一：如何使用ForEach循环渲染实现刻度尺的效果，如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/AvEKezoOQy-s-OUzqQM7gg/zh-cn_image_0000002628617570.png "点击放大")
* 场景二：如何实现一个横向的刻度选择器，支持横向滑动的效果？

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/WZuz6gj6RECfc_7vgFZqaQ/zh-cn_image_0000002628777466.png "点击放大")

## 背景知识

* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：接口基于数组类型数据来进行循环渲染。其中第一个参数arr表示数据源，第二个参数itemGenerator用于为数组中的每个元素创建对应的组件，第三个参数keyGenerator为数据源arr的每个数组项生成唯一且持久的键值。
* [List](../harmonyos-references/ts-container-list.md)：包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)：滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)：手指触摸动作触发该回调。

## 解决方案

**场景一：**

可结合自定义直尺线类RulerLine用以实现刻度尺的效果，具体步骤如下：

1. 创建自定义直尺线类RulerLine，包括组成直尺的每条线的高度属性height以及索引属性index。
2. 在aboutToAppear中初始化直尺线类，将每个新创建的类添加到直尺线数组对象rulerLines中，并计算出每1mm对应的像素px值。
3. 以rulerLines为数据源，使用ForEach循环渲染出每个直尺线类，即可实现刻度尺的效果。

完整代码如下：

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct RulerComponent {
  @State cellWidthInPixels: number = 0; // 屏幕上1mm对应的像素值px
  textWidth: number = 80; // 文本的宽度px
  @State rulerLines: RulerLine[] = []; // 尺子每个刻度的索引对应的高度

  aboutToAppear(): void {
    window.getLastWindow(this.getUIContext()?.getHostContext()).then((windowClass) => {
      windowClass.setPreferredOrientation(window.Orientation.LANDSCAPE);
    });
    this.cellWidthInPixels = display.getDefaultDisplaySync().yDPI / 25.4; // 计算当前屏幕上每毫米对应的像素值px
    for (let i = 0; i <= 15 * 10; i++) {
      let lineHeight: number = (i % 10 === 0) ? 90 : (i % 5 === 0) ? 60 : 45;
      this.rulerLines.push(new RulerLine(i, lineHeight)); // 初始化直尺每个刻度高
    }
  }

  build() {
    Column() {
      Stack() {
        // 遍历直尺线数组
        ForEach(this.rulerLines, (line: RulerLine, index: number) => {
          // 生成直尺的刻度
          Line()
            .width(1)
            .height(`${line.height}px`)
            .backgroundColor(Color.Black)
            .margin({ left: `${this.cellWidthInPixels * index}px` })
            .stroke(Color.Black);
          // 生成刻度值数字
          Text(line.showNumber())
            .fontColor(Color.Black)
            .fontSize(18)
            .width(`${this.textWidth}px`)
            .height(`${this.textWidth}px`)
            .textAlign(TextAlign.Center)
            .margin({
              left: `${this.cellWidthInPixels * index - this.textWidth / 2}px`,
              top: `${line.height}px`
            });
        });
      }
      .width('100%')
      .height('30%')
      .align(Alignment.TopStart);
    }
    .height('100%')
    .width('100%')
    .padding({ left: 30, right: 10 });
  }
}

// 直尺线类
class RulerLine {
  index: number; // 刻度索引
  height: number; // 当前刻度的高度

  constructor(index: number, height: number) {
    this.index = index;
    this.height = height;
  }

  // 10的倍数展示刻度值
  showNumber(): string {
    return this.index % 10 === 0 ? `${this.index / 10}` : '';
  }
}
```

**场景二：**

使用横向List实现一个可滚动的刻度尺，通过滚动偏移计算当前值并传递给回调函数。

1. 刻度渲染：在aboutToAppear初始化要显示的刻度，ForEach逐项渲染，根据数值区分长/中/短刻度；0和max默认在List的两端，无法居中对齐选中刻度线，需在List两端添加50%宽的占位ListItem用于把0和max居中。
2. 初始定位：aboutToAppear延迟调用scroller.scrollTo，把初始值滚到中间指示器下方。
3. 滚动与当前值计算：在onScroll中用xOffset除以itemWidth并向下取整得到当前值，然后传递给回调函数。
4. 触摸与吸附行为：在onTouch中监听Down/Up事件，抬起时计算最近刻度，把刻度滚动到中心位置。
5. 视觉中心指示：在容器中间绘制固定的指示器，始终位于容器水平中心，供刻度对齐参考。

代码实现如下：

```ts
@ComponentV2
export struct RulerComponent {
  @Param value: number = 0;
  @Param min: number = 0;
  @Param max: number = 60;
  private itemWidth: number = 20; // 每个刻度的宽度
  private scroller: Scroller = new Scroller();
  @Local isTouching: boolean = false;
  @Event onValueChange?: (value: number) => void;
  arr: Array<number> = [];

  aboutToAppear() {
    // 延迟滚动到初始位置
    setTimeout(() => {
      let offset = this.value * this.itemWidth + Math.floor(this.itemWidth / 2);
      console.info(`start offset: ${offset}`);
      this.scroller.scrollTo({ xOffset: offset, yOffset: 0, animation: { duration: 200 } });
    }, 100);
    for (let index = 0; index < this.max + 1; index++) {
      this.arr.push(index);
    }
  }

  build() {
    RelativeContainer() {
      // 刻度列表
      List({ scroller: this.scroller }) {
        // 头部占位，使0刻度能居中
        ListItem()
          .width('50%')
          .height(60);

        ForEach(this.arr, (index: number) => {
          ListItem() {
            Column() {
              // 刻度线
              if (index % 10 === 0) {
                // 长刻度
                Column()
                  .width(2)
                  .height(30)
                  .backgroundColor('#333333');
                // 刻度值
                Text(index.toString())
                  .fontSize(12)
                  .fontColor('#333333')
                  .margin({ top: 8 });
              } else if (index % 5 === 0) {
                // 中刻度
                Column()
                  .width(1.5)
                  .height(20)
                  .backgroundColor('#666666');
              } else {
                // 短刻度
                Column()
                  .width(1)
                  .height(12)
                  .backgroundColor('#999999');
              }
            }
            .width(this.itemWidth)
            .height(60)
            .justifyContent(FlexAlign.Start)
            .alignItems(HorizontalAlign.Center);
          }
        })

        // 尾部占位，使最大刻度能居中
        ListItem()
          .width('50%')
          .height(60);
      }
      .listDirection(Axis.Horizontal)
      .edgeEffect(EdgeEffect.None)
      .scrollBar(BarState.Off)
      .width('100%')
      .height(80)
      .onDidScroll(() => {
        const x = this.scroller.currentOffset().xOffset;
        let newValue = Math.floor(x / this.itemWidth);
        if (newValue < this.min) {
          newValue = this.min;
        }
        if (newValue > this.max) {
          newValue = this.max;
        }
        this.onValueChange?.(newValue);
      })
      .onTouch((event: TouchEvent) => {
        if (event.type === TouchType.Down) {
          this.isTouching = true;
        } else if (event.type === TouchType.Up) {
          this.isTouching = false;
          // 手指抬起时吸附到最近的刻度
          const x = this.scroller.currentOffset().xOffset;
          const targetValue = Math.round(x / this.itemWidth);
          // 让刻度居中
          let offSet = (targetValue * this.itemWidth) + Math.floor(this.itemWidth / 2);
          this.scroller.scrollTo({
            xOffset: offSet,
            yOffset: 0,
            animation: { duration: 200, curve: Curve.EaseOut }
          });
        }
      })
      .alignRules({
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      });

      // 中间指示器
      Column() {
        Column()
          .width(2)
          .height(30)
          .backgroundColor(Color.Yellow)
          .margin({ top: 20 });
      }
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        middle: { anchor: '__container__', align: HorizontalAlign.Center }
      });
    }
    .width('100%')
    .height(100);
  }
}

@Entry
@Component
struct Index {
  @State value: number = 0;

  build() {
    Column() {

      Text(`${this.value}`)
        .fontSize(20)
        .margin({ top: 50 });

      RulerComponent({
        min: 0,
        max: 90,
        value: this.value,
        onValueChange: (v: number) => {
          this.value = v;
        }
      })
        .width('100%')
        .margin({ top: 10 });

    }.width('100%')
    .height('100%')
  }
}
```
