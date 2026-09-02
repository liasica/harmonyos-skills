---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-attribute-animation
title: 自定义属性动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 属性动画 > 自定义属性动画
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1656416f4d22bed1d1c81da004424ecd875868dbbd012874e658f7027f0b2544
---

[属性动画](arkts-attribute-animation-overview.md)是指当可动画属性的参数值发生变化时，在UI上产生的连续视觉效果。当参数值连续变化，且设置到可以引起UI发生变化的属性接口上时，即可实现属性动画。除了组件本身支持动画的属性，ArkUI还提供了[@AnimatableExtend装饰器](arkts-animatable-extend.md)用于自定义可动画属性。

由于参数的数据类型必须具备一定程度的连续性，即可以通过插值方法来填补数据点之间的空隙以达到视觉上的连续效果，自定义可动画属性接口的参数类型仅支持number类型和实现[AnimatableArithmetic<T>接口](arkts-animatable-extend.md#animatablearithmetict接口说明)的自定义类型。通过自定义可动画属性接口和可动画数据类型，通过逐帧回调函数修改不可动画属性接口的值，能够让不可动画属性接口实现动画效果，可参考示例[使用自定义数据类型改变图形形状](arkts-custom-attribute-animation.md#使用自定义数据类型改变图形形状)。也可通过逐帧回调函数每帧修改可动画属性的值，实现逐帧布局的效果，可参考示例[使用number数据类型改变Text组件宽度实现逐帧布局的效果](arkts-custom-attribute-animation.md#使用number数据类型改变text组件宽度实现逐帧布局的效果)。关于可动画属性接口和不可动画属性接口的说明可参考[属性动画概述](arkts-attribute-animation-overview.md)中的属性接口分类说明。

## 使用number数据类型改变Text组件宽度实现逐帧布局的效果

该示例中通过[@AnimatableExtend装饰器](arkts-animatable-extend.md)定义了可动画属性接口animatableWidth，通过传入number数据类型修改属性[width](../harmonyos-references/ts-universal-attributes-size.md#width)的值，实现了逐帧改变[Text](../harmonyos-references/ts-basic-components-text.md)组件宽度的动画。

```typescript
// 第一步：使用@AnimatableExtend装饰器，自定义可动画属性接口
@AnimatableExtend(Text)
function animatableWidth(width: number) {
  .width(width) // 调用系统属性接口，逐帧回调函数每帧修改可动画属性的值，实现逐帧布局的效果。
}

@Entry
@Component
struct AnimatablePropertyExample {
  @State textWidth: number = 80; // 80: 初始文本宽度

  build() {
    Column() {
      Text('AnimatableProperty')
        .animatableWidth(this.textWidth) // 第二步：将自定义可动画属性接口设置到组件上
        .animation({ duration: 2000, curve: Curve.Ease }) // 第三步:为自定义可动画属性接口绑定动画。
      Button('Play')
        .onClick(() => {
          this.textWidth = this.textWidth === 80 ? 160 : 80; // 第四步：改变自定义可动画属性的参数，产生动画。
        })
    }
    .width('100%')
    .padding(10) // 10: 内边距
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/hvnDrXNnRImsekf6enP0SA/zh-cn_image_0000002706833774.gif)

## 使用自定义数据类型改变图形形状

该示例中通过[@AnimatableExtend装饰器](arkts-animatable-extend.md)定义了可动画属性接口animatablePoints，通过传入自定义的数据类型修改不可动画属性[points](../harmonyos-references/ts-drawing-components-polyline.md#points)的值，实现了改变[Polyline](../harmonyos-references/ts-drawing-components-polyline.md)组件形状的动画。由于系统不支持Polyline组件points属性的动画，因此需要通过实现[AnimatableArithmetic<T>接口](arkts-animatable-extend.md#animatablearithmetict接口说明)中加法、减法、乘法和判断相等函数，为该属性的参数定义做动画插值的方法。在动画过程中，系统侧根据定义的数据插值方法计算每帧的数据值，回调到[@AnimatableExtend装饰器](arkts-animatable-extend.md)修饰的自定义可动画属性接口，进而设置points属性，为points属性产生动画。

```typescript
declare type Point = number[];

// 定义可动画属性接口的参数类型，实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数
class PointClass extends Array<number> {
  constructor(value: Point) {
    super(value[0], value[1]);
  }

  add(rhs: PointClass): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) { // 2: 二维坐标点
      result.push(rhs[i] + this[i]);
    }
    return new PointClass(result);
  }

  subtract(rhs: PointClass): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) { // 2: 二维坐标点
      result.push(this[i] - rhs[i]);
    }
    return new PointClass(result);
  }

  multiply(scale: number): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) { // 2: 二维坐标点
      result.push(this[i] * scale);
    }
    return new PointClass(result);
  }
}

// 定义可动画属性接口的参数类型，实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数
// 模板T支持嵌套实现AnimatableArithmetic<T>的类型
class PointVector extends Array<PointClass> implements AnimatableArithmetic<Array<Point>> {
  constructor(initialValue: Array<Point>) {
    super();
    if (initialValue.length) {
      initialValue.forEach((p: Point) => this.push(new PointClass(p)));
    }
  }

  // implement the IAnimatableArithmetic interface
  plus(rhs: PointVector): PointVector {
    let result = new PointVector([]);
    const len = Math.min(this.length, rhs.length);
    for (let i = 0; i < len; i++) {
      result.push(this[i].add(rhs[i]));
    }
    return result;
  }

  subtract(rhs: PointVector): PointVector {
    let result = new PointVector([]);
    const len = Math.min(this.length, rhs.length);
    for (let i = 0; i < len; i++) {
      result.push(this[i].subtract(rhs[i]));
    }
    return result;
  }

  multiply(scale: number): PointVector {
    let result = new PointVector([]);
    for (let i = 0; i < this.length; i++) {
      result.push(this[i].multiply(scale));
    }
    return result;
  }

  equals(rhs: PointVector): boolean {
    if (this.length !== rhs.length) {
      return false;
    }
    for (let index = 0, size = this.length; index < size; ++index) {
      if (this[index][0] !== rhs[index][0] || this[index][1] !== rhs[index][1]) {
        return false;
      }
    }
    return true;
  }
}

// 自定义可动画属性接口
@AnimatableExtend(Polyline)
function animatablePoints(points: PointVector) {
  .points(points);
}

@Entry
@Component
struct AnimatedShape {
  squareStartPointX: number = 75; // 75: 正方形起始点X坐标
  squareStartPointY: number = 25; // 25: 正方形起始点Y坐标
  squareWidth: number = 150; // 150: 正方形宽度
  squareEndTranslateX: number = 50; // 50: 正方形结束位置X轴平移量
  squareEndTranslateY: number = 50; // 50: 正方形结束位置Y轴平移量
  @State pointVec1: PointVector = new PointVector([
    [this.squareStartPointX, this.squareStartPointY],
    [this.squareStartPointX + this.squareWidth, this.squareStartPointY],
    [this.squareStartPointX + this.squareWidth, this.squareStartPointY + this.squareWidth],
    [this.squareStartPointX, this.squareStartPointY + this.squareWidth]
  ]);
  @State pointVec2: PointVector = new PointVector([
    [this.squareStartPointX + this.squareEndTranslateX, this.squareStartPointY + this.squareStartPointY],
    [this.squareStartPointX + this.squareWidth + this.squareEndTranslateX,
      this.squareStartPointY + this.squareStartPointY],
    [this.squareStartPointX + this.squareWidth, this.squareStartPointY + this.squareWidth],
    [this.squareStartPointX, this.squareStartPointY + this.squareWidth]
  ]);
  @State color: Color = Color.Green;
  @State fontSize: number = 20.0; // 20.0: 字体大小
  @State polyline1Vec: PointVector = this.pointVec1;
  @State polyline2Vec: PointVector = this.pointVec2;

  build() {
    Row() {
      Polyline()
        .width(300) // 300: 折线宽度
        .height(200) // 200: 折线高度
        .backgroundColor('#0C000000') // 0C000000: 背景颜色（黑色带透明度）
        .fill('#317AF7') // 317AF7: 填充颜色（蓝色）
        .animatablePoints(this.polyline1Vec)
        .animation({ duration: 2000, delay: 0, curve: Curve.Ease }) // 2000: 动画持续时间（毫秒），0: 动画延迟时间
        .onClick(() => {
          if (this.polyline1Vec.equals(this.pointVec1)) {
            this.polyline1Vec = this.pointVec2;
          } else {
            this.polyline1Vec = this.pointVec1;
          }
        })
    }
    .width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/-BZZow5PQ2ujng7FRsqV7A/zh-cn_image_0000002736312883.gif)
