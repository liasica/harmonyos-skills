---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1508
title: 如何通过Swiper实现可见式卡片轮播效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过Swiper实现可见式卡片轮播效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1e5bc48bab3bc2a3d90bc9487f3755ecc2e2f61180bd69cc61817519df23af80
---

## 问题现象

如何使用Swiper组件实现在当前页面可显示出上/下一页部分内容，并且在滑动切换过程中有缩放动效，实现卡片轮播效果？

## 背景知识

滑块视图容器组件[Swiper](../harmonyos-references/ts-container-swiper.md)，提供子组件滑动轮播显示的能力。简单介绍实现该功能需要用到的属性以及事件：

* [prevMargin](../harmonyos-references/ts-container-swiper.md#prevmargin10)：设置前边距，用于露出前一项的一小部分。
* [nextMargin](../harmonyos-references/ts-container-swiper.md#nextmargin10)：设置后边距，用于露出后一项的一小部分。
* [onGestureSwipe](../harmonyos-references/ts-container-swiper.md#ongestureswipe10)：在页面跟手滑动过程中，逐帧触发该回调。
* [onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)：当切换动画开始时触发该回调。
* [onChange](../harmonyos-references/ts-container-swiper.md#onchange)：当前显示的子组件索引变化时触发该事件，返回值为当前显示的子组件的索引值。
* [onAnimationEnd](../harmonyos-references/ts-container-swiper.md#onanimationend9)：当切换动效结束时触发该回调。
* [customContentTransition](../harmonyos-references/ts-container-swiper.md#customcontenttransition12)：自定义Swiper页面切换动画。在页面跟手滑动和离手后执行切换动画的过程中，会对视窗内所有页面逐帧触发回调，可以在回调中设置透明度、缩放比例、位移等属性来自定义切换动画。

事件执行顺序：onGestureSwipe => onAnimationStart => onChange => onAnimationEnd。

## 解决方案

* 方案一：将回调onGestureSwipe、onAnimationStart、onChange、onAnimationEnd组合使用实现轮播效果。

  使用prevMargin与nextMargin属性设置前边距、后边距，并且通过onGestureSwipe、onAnimationStart、onChange、onAnimationEnd回调事件修改当前页、前一页、后一页的scale值，从而实现突出中间项缩小前后两项的效果，代码实现如下：

  1. 注册回调函数GestureSwiperEvent，在页面跟手滑动过程中，逐帧触发该回调。

     ```ts
     GestureSwiperEvent(index: number, extraInfo: SwiperAnimationEvent) {
       // 记录当前页初始状态时相对于Swiper起始位置的位移
       if (this.startSwiperOffset === 0) {
         this.startSwiperOffset = extraInfo.currentOffset;
       }
       // 记录Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。
       let offset: number = extraInfo.currentOffset;
       let nextIndex = (index === this.scaleArray.length - 1 ? 0 : index + 1);
       let preIndex = (index === 0 ? this.scaleArray.length - 1 : index - 1);
       // 记录当前页的缩放倍数
       let currentScale: number = 0;
       // 记录下一页的缩放倍数
       let nextScale: number = 0;
       // 记录上一页的缩放倍数
       let preScale: number = 0;
       // 计算当前页的滑动距离吧
       let distance = Math.abs(this.startSwiperOffset - offset);
       // 通过滑动距离控制当前页面缩小倍数，通过Math.min控制最小为MIN_SCALE
       currentScale = MAX_SCALE - Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
       // 判断滑动方向
       if (offset < this.startSwiperOffset) {
         // 通过滑动距离控制下一个页面放大倍数，通过Math.min控制最大为MAX_SCALE
         nextScale = MIN_SCALE + Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
         preScale = MIN_SCALE;
       } else {
         preScale = MIN_SCALE + Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
         nextScale = MIN_SCALE;
       }
       this.scaleArray[index] = currentScale;
       this.scaleArray[nextIndex] = nextScale;
       this.scaleArray[preIndex] = preScale;
     }
     ```
  2. 注册回调函数AnimationStartEvent，切换动画开始时触发该回调。

     ```ts
     AnimationStartEvent(index: number, targetIndex: number) {
       // 若元素当前页面为最后一页，则下一页置为0，否则置为targetIndex+1
       let nextIndex = (targetIndex === this.scaleArray.length - 1 ? 0 : targetIndex + 1);
       // 若元素当前页面为第一页，则上一页置为最后一项的targetIndex，否则置为targetIndex-1
       let preIndex = (targetIndex === 0 ? this.scaleArray.length - 1 : targetIndex - 1);
       // 将当前页scale放大比例置为MAX_SCALE，上一页与下一页都置为MIN_SCALE
       this.scaleArray[targetIndex] = MAX_SCALE;
       this.scaleArray[nextIndex] = MIN_SCALE;
       this.scaleArray[preIndex] = MIN_SCALE;
     }
     ```
  3. 注册回调函数ChangeEvent，当前显示的子组件索引变化时触发。

     ```ts
     ChangeEvent(index: number) {
       this.currentIndex = index;
     }
     ```
  4. 注册回调函数AnimationEndEvent，当切换动效结束时触发该回调。

     ```ts
     AnimationEndEvent() {
       // startSwiperOffset重置为0
       this.startSwiperOffset = 0;
     }
     ```

  完整示例代码如下：

  ```ts
  class MyOwnDataSource implements IDataSource {
    private list: string[] = [];

    constructor(list: string[]) {
      this.list = list;
    }

    totalCount(): number {
      return this.list.length;
    }

    getData(index: number): string {
      return this.list[index];
    }

    registerDataChangeListener() {
    }

    unregisterDataChangeListener() {
    }
  }

  // 最大缩放
  const MAX_SCALE = 1;
  // 最小缩放
  const MIN_SCALE = 0.8;
  // 可通过以下两个参数变化观察效果，然后优化
  // 子控件动画时长
  const PAGE_DURATION = 100;
  // swiper组件切换动画时长
  const SWIPER_DURATION = 500;
  // 拖动时用来计算缩放，影响拖动缩放速度，可根据屏幕尺寸来定
  const DRAGGING_MAX_DISTANCE = 1000;

  @Entry
  @Component
  struct SwiperPageOne {
    private swiperController: SwiperController = new SwiperController();
    private data: MyOwnDataSource = new MyOwnDataSource([]);
    @State currentIndex: number = 0;
    @State scaleArray: number[] = [];
    startSwiperOffset: number = 0; // Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移

    GestureSwiperEvent(index: number, extraInfo: SwiperAnimationEvent) {
      // 记录当前页初始状态时相对于Swiper起始位置的位移
      if (this.startSwiperOffset === 0) {
        this.startSwiperOffset = extraInfo.currentOffset;
      }
      // 记录Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移。
      let offset: number = extraInfo.currentOffset;
      let nextIndex = (index === this.scaleArray.length - 1 ? 0 : index + 1);
      let preIndex = (index === 0 ? this.scaleArray.length - 1 : index - 1);
      // 记录当前页的缩放倍数
      let currentScale: number = 0;
      // 记录下一页的缩放倍数
      let nextScale: number = 0;
      // 记录上一页的缩放倍数
      let preScale: number = 0;
      // 计算当前页的滑动距离吧
      let distance = Math.abs(this.startSwiperOffset - offset);
      // 通过滑动距离控制当前页面缩小倍数，通过Math.min控制最小为MIN_SCALE
      currentScale = MAX_SCALE - Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
      // 判断滑动方向
      if (offset < this.startSwiperOffset) {
        // 通过滑动距离控制下一个页面放大倍数，通过Math.min控制最大为MAX_SCALE
        nextScale = MIN_SCALE + Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
        preScale = MIN_SCALE;
      } else {
        preScale = MIN_SCALE + Math.min(distance / DRAGGING_MAX_DISTANCE, MAX_SCALE - MIN_SCALE);
        nextScale = MIN_SCALE;
      }
      this.scaleArray[index] = currentScale;
      this.scaleArray[nextIndex] = nextScale;
      this.scaleArray[preIndex] = preScale;
    }

    AnimationStartEvent(index: number, targetIndex: number) {
      // 若元素当前页面为最后一页，则下一页置为0，否则置为targetIndex+1
      let nextIndex = (targetIndex === this.scaleArray.length - 1 ? 0 : targetIndex + 1);
      // 若元素当前页面为第一页，则上一页置为最后一项的targetIndex，否则置为targetIndex-1
      let preIndex = (targetIndex === 0 ? this.scaleArray.length - 1 : targetIndex - 1);
      // 将当前页scale放大比例置为MAX_SCALE，上一页与下一页都置为MIN_SCALE
      this.scaleArray[targetIndex] = MAX_SCALE;
      this.scaleArray[nextIndex] = MIN_SCALE;
      this.scaleArray[preIndex] = MIN_SCALE;
    }

    ChangeEvent(index: number) {
      this.currentIndex = index;
    }

    AnimationEndEvent() {
      // startSwiperOffset重置为0
      this.startSwiperOffset = 0;
    }

    aboutToAppear(): void {
      let list: string[] = [];
      for (let i = 0; i <= 5; i++) {
        list.push(i.toString());
        this.scaleArray.push(i === 0 ? MAX_SCALE : MIN_SCALE);
      }
      this.data = new MyOwnDataSource(list);
    }

    build() {
      Column({ space: 25 }) {
        Swiper(this.swiperController) {
          LazyForEach(this.data, (item: string, index: number) => {
            Column() {
              Text(item)
                .width(40)
                .height(40)
                .textAlign(TextAlign.Center)
                .fontSize(30);
            }
            .width('100%')
            .height('100%')
            .backgroundColor('#F7B0BB')
            // 通过scale控制缩放倍数
            .scale({ x: this.scaleArray[index], y: this.scaleArray[index] })
            .animation({
              duration: PAGE_DURATION,
              curve: Curve.Linear
            });
          }, (item: string) => item);
        }
        .displayMode(SwiperDisplayMode.STRETCH)
        .displayCount(1)
        .width('100%')
        .height('100%')
        .index(this.currentIndex)
        .cachedCount(2)
        .indicator(true)
        .duration(SWIPER_DURATION)
        .itemSpace(0)
        .nextMargin(40)
        .prevMargin(40)
        .curve(Curve.Linear)
        .backgroundColor(0xcccccc)
        .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
          // 调用回调函数GestureSwiperEvent()
          this.GestureSwiperEvent(index, extraInfo);
        })
        .onAnimationStart((index: number, targetIndex: number) => {
          // 调用回调函数AnimationStartEvent()
          this.AnimationStartEvent(index, targetIndex);
        })
        .onChange((index: number) => {
          // 调用回调函数ChangeEvent()
          this.ChangeEvent(index);
        })
        .onAnimationEnd(() => {
          // 调用回调函数AnimationEndEvent()
          this.AnimationEndEvent();
        });
      }
      .width('100%')
      .height('20%')
      .margin({ top: 5 });
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Xc-Gwle5SOiIq6KKqtuhhQ/zh-cn_image_0000002628606554.png "点击放大")
* 方案二：通过自定义页面切换的动画来实现图片滑动过程中的缩放效果。
  1. 创建继承IDataSource的类MyDataSource，监听滑动的图片。
  2. 图片展示时，在onChange中根据当前图片的索引，来确定前后图片的缩放值。
  3. 在customContentTransition中获取SwiperContentTransitionProxy回调的proxy对象，根据对象的属性selectedIndex、index、position、mainAxisLength计算滑动图片的缩放值，实现滑动时的缩放效果。

  完整示例代码如下：

  ```ts
  class MyDataSource implements IDataSource {
    private listeners: DataChangeListener[] = [];
    private list: string[] = [];

    constructor(list: string[]) {
      this.list = list;
    }

    totalCount(): number {
      return this.list.length;
    }

    getData(index: number): string {
      return this.list[index];
    }

    registerDataChangeListener(listener: DataChangeListener): void {
      if (this.listeners.indexOf(listener) < 0) {
        this.listeners.push(listener);
      }
    }

    unregisterDataChangeListener() {
    }
  }

  const MAX_SIZE = 1; // 最大缩放
  const MIN_SIZE = 0.75; // 最小缩放
  // 可通过以下两个参数变化观察效果，然后优化
  const PAGE_TIME = 200; // 子控件动画时长
  const SWIPER_TIME = 300; // swiper组件切换动画时长
  // 拖动时用来计算缩放，影响拖动缩放速度，可根据屏幕尺寸来定
  const DRAGGING_MAX_LENGTH = 1000;
  const DISPLAY_TIME: number = 1;

  @Entry
  @Component
  struct SwiperPageTwo {
    private swiperController: SwiperController = new SwiperController();
    private data: MyDataSource = new MyDataSource([]);
    @State currentIndex: number = 0;
    @State scaleArray: number[] = []; // 缩放值
    startSwiperOffset: number = 0; // 开始滑动距离
    imageArr: string[] = [
      'app.media.drag_and_exchange_ic_public_app1', // app.media.drag_and_exchange_ic_public_app1仅供参考，需要自行配置。
      'app.media.drag_and_exchange_ic_public_app2', // app.media.drag_and_exchange_ic_public_app2仅供参考，需要自行配置。
      'app.media.drag_and_exchange_ic_public_app3', // app.media.drag_and_exchange_ic_public_app3仅供参考，需要自行配置。
      'app.media.drag_and_exchange_ic_public_app4', // app.media.drag_and_exchange_ic_public_app4仅供参考，需要自行配置。
      'app.media.drag_and_exchange_ic_public_app5', // app.media.drag_and_exchange_ic_public_app5仅供参考，需要自行配置。
      'app.media.drag_and_exchange_ic_public_app6',// app.media.drag_and_exchange_ic_public_app6仅供参考，需要自行配置。
    ];

    aboutToAppear(): void {
      let list: string[] = [];
      for (let i = 0; i <= 5; i++) {
        list.push(this.imageArr[i]);
        this.scaleArray.push(i === 0 ? MAX_SIZE : MIN_SIZE);
      }
      this.data = new MyDataSource(list);
    }

    build() {
      Column({ space: 25 }) {
        Swiper(this.swiperController) {
          LazyForEach(this.data, (item: string, index: number) => {
            Column() {
              // swiper内容区域
              Image($r(item))
                .width(200)
                .height(250);
            }
            .alignSelf(ItemAlign.Center)
            .height('100%')
            .scale({ x: this.scaleArray[index], y: this.scaleArray[index] })
            .animation({
              duration: PAGE_TIME,
              curve: Curve.Linear
            });
          }, (item: string) => item);
        }
        .displayMode(SwiperDisplayMode.STRETCH)
        .displayCount(DISPLAY_TIME)
        .width('100%')
        .height('100%')
        .index(this.currentIndex)
        .cachedCount(2)
        .indicator(false)
        .autoPlay(false)
        .loop(true)
        .duration(SWIPER_TIME)
        .itemSpace(0)
        .nextMargin(10)
        .prevMargin(180)
        .curve(Curve.Linear)
        .onChange((index) => {
          this.currentIndex = index;
          // 设置当前index缩放值为最大值
          this.scaleArray[this.currentIndex] = MAX_SIZE;
          if (this.currentIndex === 0) {
            // 当前index=0时，设置上一张图片的缩放值
            this.scaleArray[this.scaleArray.length - 1] = MIN_SIZE;
          } else {
            // 当前index不为0时，设置上一张图片的缩放值
            this.scaleArray[this.currentIndex -1] = MIN_SIZE;
          }

          if (this.currentIndex === this.scaleArray.length - 1) {
            // 当index为最后一张图片时，设置下一张图片的缩放值
            this.scaleArray[0] = MIN_SIZE;
          } else {
            // 当index不为最后一张时，设置下一张图片的缩放值
            this.scaleArray[this.currentIndex + 1] = MIN_SIZE;
          }
        })
        .customContentTransition({
          // 页面移除视窗时超时1000ms下渲染树
          timeout: 1000,
          // 对视窗内所有页面逐帧回调transition，在回调中修改opacity、scale、translate、zIndex等属性值，实现自定义动画
          transition: (proxy: SwiperContentTransitionProxy) => {
            if (this.startSwiperOffset === 0) {
              this.startSwiperOffset = proxy.position * proxy.mainAxisLength;
            }
            let offset: number = proxy.position * proxy.mainAxisLength; // 移动距离
            let currentScale: number = this.scaleArray[proxy.index]; // 当前index缩放值
            let nextIndex = (proxy.index === this.scaleArray.length - 2 ? 0 : proxy.index + 1); // 计算下一个index
            let preIndex = (proxy.index === 0 ? this.scaleArray.length - 2 : proxy.index - 1); // 计算上一个index
            let nextScale: number = this.scaleArray[nextIndex]; // 下一个index缩放值
            let preScale: number = this.scaleArray[preIndex]; // 上一个index缩放值
            // 滑动距离
            let distance = Math.abs(offset);
            currentScale = MAX_SIZE - Math.min(distance / DRAGGING_MAX_LENGTH, MAX_SIZE - MIN_SIZE); // 当前缩放值
            if (this.startSwiperOffset > offset) {
              nextScale = MIN_SIZE + Math.min(distance / DRAGGING_MAX_LENGTH, MAX_SIZE - MIN_SIZE);
              preScale = MIN_SIZE;
            } else {
              preScale = MIN_SIZE + Math.min(distance / DRAGGING_MAX_LENGTH, MAX_SIZE - MIN_SIZE);
              nextScale = MIN_SIZE;
            }
            this.scaleArray[this.currentIndex] = currentScale; // 当前index缩放值
            this.scaleArray[nextIndex] = nextScale; // 下一个index缩放值
            this.scaleArray[preIndex] = preScale; // 上一个index缩放值
          }
        });
      }
      .width('100%')
      .height(250);
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4FKw2it6RCaycQt8TndqDg/zh-cn_image_0000002658845803.png "点击放大")
