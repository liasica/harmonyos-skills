---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-993
title: 如何实现速度均匀的多边形伸缩动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现速度均匀的多边形伸缩动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1abe7505aa1c490be9cc89dc3aefab815aac2bbacf83360ef08600532c00089b
---

## 问题现象

如何实现多边形组件从一个中心点匀速展开的动画，即各个顶点从一个中心点向外移动，最终生成一个多边形，要求每个点移动的速度相同，移动距离短的点花费的时间也短，移动距离长的点花费的时间也长。

以下示例是通过animateTo实现的动画，但每个顶点移动到终点（无论起点到终点的距离多长）的花费时间是相同的。

```ts
declare type Point = number[];

// 定义可动画属性接口的参数类型，实现AnimatableArithmetic<T>接口中加法、减法、乘法和判断相等函数
class PointClass extends Array<number> {
  constructor(value: Point) {
    super(value[0], value[1])
  }

  add(rhs: PointClass): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) {
      result.push(rhs[i] + this[i])
    }
    return new PointClass(result);
  }

  subtract(rhs: PointClass): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) {
      result.push(this[i] - rhs[i]);
    }
    return new PointClass(result);
  }

  multiply(scale: number): PointClass {
    let result: Point = new Array<number>() as Point;
    for (let i = 0; i < 2; i++) {
      result.push(this[i] * scale)
    }
    return new PointClass(result);
  }
}

class PointVector extends Array<PointClass> implements AnimatableArithmetic<Array<Point>> {
  constructor(initialValue: Array<Point>) {
    super();
    if (initialValue.length) {
      initialValue.forEach((p: Point) => this.push(new PointClass(p)))
    }
  }

  // implement the IAnimatableArithmetic interface
  plus(rhs: PointVector): PointVector {
    let result = new PointVector([]);
    const len = Math.min(this.length, rhs.length)
    for (let i = 0; i < len; i++) {
      result.push(this[i].add(rhs[i]))
    }
    return result;
  }

  subtract(rhs: PointVector): PointVector {
    let result = new PointVector([]);
    const len = Math.min(this.length, rhs.length)
    for (let i = 0; i < len; i++) {
      result.push(this[i].subtract(rhs[i]))
    }
    return result;
  }

  multiply(scale: number): PointVector {
    let result = new PointVector([]);
    for (let i = 0; i < this.length; i++) {
      result.push(this[i].multiply(scale))
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
@AnimatableExtend(Polygon)
function animatablePoints(points: number[][]) {
  .points(points)
}

@Entry
@Component
export struct WidgetsProgress {
  @State radianValue: number = 0.85
  @State pointVec1: PointVector = new PointVector([[50, 50], [50, 50], [50, 50], [50, 50], [50, 50], [50, 50]])
  @State pointVec2: PointVector = new PointVector([[50, 0], [0, 50], [20, 100], [50, 100], [80, 100], [100, 50]])
  @State polyline1Vec: PointVector = this.pointVec1;

  setSwiperAnimation() {
    this.getUIContext().animateTo({ duration: 20000, delay: 0, curve: Curve.Ease }, () => {
      this.polyline1Vec = this.pointVec2
    })

  }

  build() {
    Column() {
      Polygon()
        .width(100)
        .height(100)
        .fill(Color.Red)
        .fillOpacity(0.6)
        .animatablePoints(this.polyline1Vec)
        .onAppear(() => { // 挂载之后只调用一次
          this.setSwiperAnimation();
        })
    }
    .width('100%')
    .height('100%')
    .backgroundColor("#ffffff")

  }
}
```

演示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/05LSC0wxRD6jwWWGbAaS5A/zh-cn_image_0000002658921035.png "点击放大")

## 背景知识

* [Polygon](../harmonyos-references/ts-drawing-components-polygon.md)是多边形绘制组件，通过传入各个顶点的坐标绘制多边形。
* [animateTo](../harmonyos-references/ts-explicit-animation.md)通过属性变化自动插值生成动画。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)是定时器，可以每隔一段时间去修改变量的值。

## 解决方案

animateTo只能定义动画整体的完成时间，也就是多边形各个顶点从起始点到终点花费的时间都是相同的。如果希望每个顶点到终点匀速变化，根据距离长短花费不同的时间，需要使用setInterval定时器去定义各个顶点的移动，使每个顶点在每一步移动相同的距离，直到走完每个顶点各自的距离。

1. 定义各个顶点的起始坐标：均从[50,50]这个中心点往外移动。

   ```ts
   @State pointVec1: number[][] = [[50, 50], [50, 50], [50, 50], [50, 50], [50, 50], [50, 50]];
   ```
2. 定义移动过程中每个顶点的坐标并初始化：

   ```ts
   @State polyline1Vec: number[][] = [[50, 50], [50, 50], [50, 50], [50, 50], [50, 50], [50, 50]];
   ```
3. 定义每个顶点的位移量：

   ```ts
   dataList = [43, 40, 40, 30, 30, 20];
   ```
4. 定义不同顶点的移动方向：角间隔为60度。

   ```ts
   // 获取弧度
   getRadByIndex(index: number, length: number) {
     if (length === 0) {
       return 0;
     }
     let angles = 360 / length * index;
     let rad = Math.PI / 180 * angles;
     return rad;
   }
   ```
5. 利用定时器执行每个顶点的位移：

   ```ts
   this.timer = setInterval(() => {
     // 定义移动速度和统计已完成的顶点数
     let speed = 0.2;
     let cNum = 0;
     for (let index = 0; index < this.polyline1Vec.length; index++) {
       // 1.计算角度方向
       let sinNum = Math.sin(this.getRadByIndex(index, this.polyline1Vec.length));
       let cosNum = Math.cos(this.getRadByIndex(index, this.polyline1Vec.length));
       // 2.获取目标距离
       let dataItem = this.dataList[index];
       // 3.计算当前已移动的偏移量
       let offsetx = this.polyline1Vec[index][0] - this.pointVec1[index][0];
       let offsety = this.polyline1Vec[index][1] - this.pointVec1[index][1];
       // 4.判断是否已到达终点？如果是，跳过
       if (offsetx === 0 && Math.abs(offsety) > Math.abs(dataItem * cosNum)) {
         cNum++;
         continue;
       } else if (Math.abs(offsetx) > Math.abs(dataItem * sinNum)) {
         cNum++;
         continue;
       }
       // 5.更新每个顶点的坐标
       this.polyline1Vec[index][0] += sinNum * speed;
       this.polyline1Vec[index][1] += cosNum * speed;
     }
     this.polyline1Vec = JSON.parse(JSON.stringify(this.polyline1Vec));
     // 6.判断是否所有顶点都完成位移以结束动画
     if (cNum === this.polyline1Vec.length) {
       clearInterval(this.timer);
     }
   }, 20);
   ```

完整示例代码如下：

```ts
@Entry
@Component
export struct WidgetsProgress {
  @State pointVec1: number[][] = [[50, 50], [50, 50], [50, 50], [50, 50], [50, 50], [50, 50]];
  @State polyline1Vec: number[][] = [[50, 50], [50, 50], [50, 50], [50, 50], [50, 50], [50, 50]];
  dataList = [43, 40, 40, 30, 30, 20];
  timer = -1;

  // 获取弧度
  getRadByIndex(index: number, length: number) {
    if (length === 0) {
      return 0;
    }
    let angles = 360 / length * index;
    let rad = Math.PI / 180 * angles;
    return rad;
  }

  build() {
    Column() {
      Polygon()
        .width(100)
        .height(100)
        .fill(Color.Red)
        .fillOpacity(0.6)
        .points(this.polyline1Vec)
        .onAppear(() => { // 挂载之后只调用一次
          this.timer = setInterval(() => {
            // 定义移动速度和统计已完成的顶点数
            let speed = 0.2;
            let cNum = 0;
            for (let index = 0; index < this.polyline1Vec.length; index++) {
              // 1.计算角度方向
              let sinNum = Math.sin(this.getRadByIndex(index, this.polyline1Vec.length));
              let cosNum = Math.cos(this.getRadByIndex(index, this.polyline1Vec.length));
              // 2.获取目标距离
              let dataItem = this.dataList[index];
              // 3.计算当前已移动的偏移量
              let offsetx = this.polyline1Vec[index][0] - this.pointVec1[index][0];
              let offsety = this.polyline1Vec[index][1] - this.pointVec1[index][1];
              // 4.判断是否已到达终点？如果是，跳过
              if (offsetx === 0 && Math.abs(offsety) > Math.abs(dataItem * cosNum)) {
                cNum++;
                continue;
              } else if (Math.abs(offsetx) > Math.abs(dataItem * sinNum)) {
                cNum++;
                continue;
              }
              // 5.更新每个顶点的坐标
              this.polyline1Vec[index][0] += sinNum * speed;
              this.polyline1Vec[index][1] += cosNum * speed;
            }
            this.polyline1Vec = JSON.parse(JSON.stringify(this.polyline1Vec));
            // 6.判断是否所有顶点都完成位移以结束动画
            if (cNum === this.polyline1Vec.length) {
              clearInterval(this.timer);
            }
          }, 20);
        });
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffffff');

  }
}
```
