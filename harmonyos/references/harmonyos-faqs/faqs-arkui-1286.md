---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1286
title: 如何监听Swiper滑动索引位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何监听Swiper滑动索引位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4859cb23f13d313ac51549f3ed341587a9700d2a0dffceba5d612e8ad589188b
---

## 问题现象

需要在Swiper组件滑动切换后获取新的索引的场景下，如何通过监听获取Swiper组件的索引位置？

## 背景知识

* [onChange](../harmonyos-references/ts-container-swiper.md#onchange)事件可以在子组件索引变化时触发并且返回索引值，通过onChange方法即可监听当前页面的下标位置。
* [onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)回调在切换动画开始时触发，其参数类型为[OnSwiperAnimationStartCallback](../harmonyos-references/ts-container-swiper.md#onswiperanimationstartcallback18)，其中的参数index为当前显示元素的索引，而切换动画结束回调[onAnimationEnd](../harmonyos-references/ts-container-swiper.md#onanimationend9)也包含index参数。

## 解决方案

* 方案一：onChange事件可以在子组件索引变化时触发并且返回索引值，当Swiper滑动时，即可获取当前页面的索引值，监听当前页面的下标位置。调用onChange示例代码如下：

  ```ts
  class MyDataSource implements IDataSource {
    private list: number[] = [];

    constructor(list: number[]) {
      this.list = list;
    }

    totalCount(): number {
      return this.list.length;
    }

    getData(index: number): number {
      return this.list[index];
    }

    registerDataChangeListener(): void {
    }

    unregisterDataChangeListener() {
    }
  }

  @Entry
  @Component
  struct SwiperOnChange {
    private swiperController: SwiperController = new SwiperController();
    private data: MyDataSource = new MyDataSource([]);

    aboutToAppear(): void {
      let list: number[] = [];
      for (let i = 1; i <= 15; i++) {
        list.push(i);
      }
      this.data = new MyDataSource(list);
    }

    build() {
      Column({ space: 5 }) {
        Swiper(this.swiperController) {
          LazyForEach(this.data, (item: string) => {
            Text(item.toString())
              .width('90%')
              .height(160)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(5)
        .autoPlay(true)
        .interval(4000)
        .loop(true)
        .duration(1000)
        .itemSpace(0)
        .onChange((index: number) => {
          console.info(`onChangeIndex + ${index}`);
        })
        .indicator( // 设置圆点导航点样式
          new DotIndicator()
            .itemWidth(8)
            .itemHeight(8)
            .selectedItemWidth(16)
            .selectedItemHeight(8)
            .color(Color.Gray)
            .selectedColor(Color.Blue)
            .maxDisplayCount(9))
        .displayArrow({
          // 设置导航点箭头样式
          showBackground: true,
          isSidebarMiddle: true,
          backgroundSize: 24,
          backgroundColor: Color.White,
          arrowSize: 18,
          arrowColor: Color.Blue
        }, false)
        .curve(Curve.Linear);
      }.width('100%')
      .margin({ top: 5 });
    }
  }
  ```
* 方案二：通过监听[属性](../harmonyos-references/ts-container-swiper.md#属性-1)index获取视窗内页面的索引，能够监听index参数的事件有：

  onAnimationStart事件，onAnimationEnd事件，[onGestureSwipe](../harmonyos-references/ts-container-swiper.md#ongestureswipe10)事件以及[onContentDidScroll](../harmonyos-references/ts-container-swiper.md#oncontentdidscroll12)事件。以onAnimationStart事件为例获取index索引，示例代码如下：

  ```ts
  class MyOwnDataSource implements IDataSource {
    private list: number[] = [];

    constructor(list: number[]) {
      this.list = list;
    }

    totalCount(): number {
      return this.list.length;
    }

    getData(index: number): number {
      return this.list[index];
    }

    registerDataChangeListener(): void {
    }

    unregisterDataChangeListener() {
    }
  }

  @Entry
  @Component
  struct SwiperOnAnimationStart {
    private swiperController: SwiperController = new SwiperController();
    private data: MyOwnDataSource = new MyOwnDataSource([]);

    aboutToAppear(): void {
      let list: number[] = [];
      for (let i = 1; i <= 15; i++) {
        list.push(i);
      }
      this.data = new MyOwnDataSource(list);
    }

    build() {
      Column({ space: 5 }) {
        Swiper(this.swiperController) {
          LazyForEach(this.data, (item: string) => {
            Text(item.toString())
              .width('90%')
              .height(160)
              .backgroundColor(0xAFEEEE)
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(5)
        .autoPlay(true)
        .interval(4000)
        .loop(true)
        .duration(1000)
        .itemSpace(0)
        .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
          console.info(`index: + ${index}`);
          console.info(`targetIndex: + ${targetIndex}`);
          console.info(`current offset: + ${extraInfo.currentOffset}`);
          console.info(`target offset: + ${extraInfo.targetOffset}`);
          console.info(`velocity: + ${extraInfo.velocity}`);
        })
        .indicator( // 设置圆点导航点样式
          new DotIndicator()
            .itemWidth(8)
            .itemHeight(8)
            .selectedItemWidth(16)
            .selectedItemHeight(8)
            .color(Color.Gray)
            .selectedColor(Color.Blue)
            .maxDisplayCount(9))
        .displayArrow({
          // 设置导航点箭头样式
          showBackground: true,
          isSidebarMiddle: true,
          backgroundSize: 24,
          backgroundColor: Color.White,
          arrowSize: 18,
          arrowColor: Color.Blue
        }, false)
        .curve(Curve.Linear);
      }.width('100%')
      .margin({ top: 5 });
    }
  }
  ```

## 常见FAQ

Q：如何通过监听判断Swiper组件是否要切换到下一界面？

A：onAnimationStart事件的参数targetIndex为切换动画目标元素的索引，监听该参数即可判断Swiper是否要切换到下一界面。

Q：需要在Swiper组件切换时立即改变其他组件状态，目前通过在onChange里用index更新其他变量来实现，但是onChange触发有明显延迟，怎么解决？

A：onChange事件在页签切换动画结束后才能收到回调，如果需要在切换动画过程中就获取新的index，可以使用切换动画开始时就触发的onAnimationStart事件，通过获取切换动画目标元素的索引targetIndex来实现。
