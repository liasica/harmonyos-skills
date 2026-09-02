---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-508
title: 怎么解决Progress组件配合animateTo实现循环动画无反应问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 怎么解决Progress组件配合animateTo实现循环动画无反应问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:813af94ac4e5263f8c2c8fec9d9526ac6c67e128f63ca748768a94a5eff6d10e
---

## 问题现象

使用Progress组件配合animateTo来实现进度条循环动画，动画效果失效无反应。

```ts
/** 进度条最小值 */
const PROGRESS_MIN1 = 0;
/** 进度条最大值 */
const PROGRESS_MAX1 = 100;

@Entry
@Component
struct ProgressAnimWithProblem {
  /** 进度条当前值 */
  @State progressValue: number = PROGRESS_MIN1;
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    };
    this.uiContext?.animateTo({
      duration: 2000,
      iterations: -1, // 设置-1表示动画无限循环
    }, () => {
      this.progressValue = PROGRESS_MAX1;
    });
  };

  build() {
    Column({ space: 15 }) {
      Progress({
        value: this.progressValue, // 进度条当前进度值
        total: PROGRESS_MAX1, // 进度条总长
        type: ProgressType.Ring, // 进度条类型，分为Linear线性样式、ScaleRing环形有刻度样式、Ring环形无刻度样式、Eclipse圆形样式、Capsule胶囊样式
      })
        .style({
          strokeWidth: 10, // 进度条宽度，默认4vp
          enableSmoothEffect: true // 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值true
        })
        .width(100) // 进度条组件宽度
        .color('#0A59F7') // 进度条前景色
        .backgroundColor(Color.White); // 进度条背景色
    }
    .width('100%')
    .height('100%')
    .padding({ top: 5 })
    .justifyContent(FlexAlign.Center);
  };
};
```

## 背景知识

* [进度条（Progress）](../harmonyos-guides/arkts-common-components-progress-indicator.md)：用于显示内容加载或操作处理等进度。可以有多种表现形式，官方提供胶囊型、环形有刻度、环形无刻度、圆形，且支持自定义图形样式。
* 显式动画（animateTo）：提供全局[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。同属性动画，布局类改变宽高的动画，内容都是直接到终点状态，例如文字、Canvas的内容等。
* [定时器（Timer）](../harmonyos-references/js-apis-timer.md)：[setInterval()](../harmonyos-references/js-apis-timer.md#setinterval)方法重复调用一个函数，在每次调用之间具有固定的时间延迟。此方法创建一个定时器并返回该定时器ID，删除该定时器需要手动调用[clearInterval()](../harmonyos-references/js-apis-timer.md#clearinterval)。

## 问题定位

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），问题代码使用animateTo改变Progress组件的进度值，结果是进度条从0到100动画仅执行一次。可见不支持使用animateTo控制Progress组件进度条循环效果。

## 分析结论

animateTo适用于组件自身属性动画场景（如尺寸、颜色改变等），不支持使用animateTo控制Progress组件进度值变化来实现进度条循环效果。

## 修改建议

可以使用定时器来控制Progress组件进度值变化。用setInterval()方法创建定时任务，每间隔一段时间（如20毫秒）均匀地改变Progress组件进度值（如每次加1），即可实现预期效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/6PBO4eIsSv-yFu51GT99tw/zh-cn_image_0000002628388622.png "点击放大")

```ts
/** 进度条最小值 */
const PROGRESS_MIN = 0;
/** 进度条最大值 */
const PROGRESS_MAX = 100;

@Entry
@Component
struct ProgressAnim {
  /** 进度条当前值 */
  @State progressValue: number = PROGRESS_MIN;

  aboutToAppear(): void {
    // 进入界面时即启动进度条动画
    this.startAnim();
  };

  build() {
    Column({ space: 15 }) {
      Progress({
        value: this.progressValue, // 进度条当前进度值
        total: PROGRESS_MAX, // 进度条总长
        type: ProgressType.Ring, // 进度条类型，分为Linear线性样式、ScaleRing环形有刻度样式、Ring环形无刻度样式、Eclipse圆形样式、Capsule胶囊样式
      })
        .style({
          strokeWidth: 10, // 进度条宽度，默认4vp
          enableSmoothEffect: true // 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值，默认值true
        })
        .width(100) // 进度条组件宽度
        .color('#0A59F7') // 进度条前景色
        .backgroundColor(Color.White); // 进度条背景色
    }
    .width('100%')
    .height('100%')
    .padding({ top: 5 })
    .justifyContent(FlexAlign.Center);
  };

  // 开启进度条动画
  private startAnim() {
    // intervalId为null时表示未启动interval
    setInterval(() => {
      // 使用setInterval()方法重复执行以下代码片段，在每次调用之间具有固定的时间间隔20毫秒
      // 每次进度值+1
      this.progressValue++;
      // 当进度值达到最大值时，将进度值重置为最小值，循环往复
      if (this.progressValue == PROGRESS_MAX) {
        this.progressValue = PROGRESS_MIN;
      };
    }, 20);
  };
};
```
