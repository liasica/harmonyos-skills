---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1147
title: 在Swiper上添加滑动手势监听
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 在Swiper上添加滑动手势监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:547ef8799ce416ff65be5c061d0e453c727036e832e20b939895b84613dbcb37
---

## 问题现象

Swiper组件，在滑动时手指抬起后，怎样监听到是要显示下一个界面还是停留在当前界面？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/jzWgwNJKQM-wuMzlKZSV3g/zh-cn_image_0000002658808973.png "点击放大")

## 背景知识

* [onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)和[onAnimationEnd](../harmonyos-references/ts-container-swiper.md#onanimationend9)是HarmonyOS中用于处理动画事件的两个重要函数。它们分别在动画开始和结束时被调用，允许开发者在这些时刻执行自定义代码。onAnimationStart的参数为：index、targetIndex、extraInfo，而extraInfo的类型为[SwiperAnimationEvent](../harmonyos-references/ts-container-swiper.md#swiperanimationevent10对象说明)，SwiperAnimationEvent对象又包括了currentOffset、targetOffset、velocity。可以通过输出这些参数来对滑动手势进行监听。
* [showNext](../harmonyos-references/ts-container-swiper.md#shownext)和[showPrevious](../harmonyos-references/ts-container-swiper.md#showprevious)方法用于实现翻至下一页和翻至上一页，翻页带动画切换过程，时长通过Swiper的duration属性设置。

## 解决方案

将index、targetIndex输出，观察index和targetIndex的值是否相同，若相同，则说明手指抬起时并没有滑入下一个页面；若不相同，则说明手指抬起时已经滑入了下一个页面。可以根据以下步骤来完成：

1. 创建数据源类：实现IDataSource接口，提供Swiper组件所需的数据。例如，MyDataSource类用于存储和管理数据项。
2. 初始化组件和数据：在组件的生命周期方法aboutToAppear()中，初始化数据源，并将其赋值给Swiper组件使用。
3. 构建Swiper组件：使用Swiper组件，并通过LazyForEach循环渲染数据项。每个数据项可以是一个Text组件或其他自定义组件。
4. 添加滑动事件监听：使用onAnimationStart监听滑动开始的事件。
5. 添加控制按钮：在Row布局中添加showNext和showPrevious按钮，分别调用swiperController.showNext()和swiperController.showPrevious()方法，实现手动滑动到下一页和上一页。

示例代码如下所示：

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
struct SwiperDemo {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  private currentIndex: number = 4;

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 0; i <= 10; i++) {
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
            .backgroundColor('#f1f3f5')
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }, (item: string) => item);
      }
      .index(this.currentIndex) // 设置当前显示的索引
      .loop(false) // 设置是否循环显示。false表示不循环
      // 监听当前索引的变化，当滑动到新页面时更新currentIndex
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .onAnimationStart((index: number, targetIndex: number, extraInfo: SwiperAnimationEvent) => {
        console.info(`index: ${index}`);
        console.info(`targetIndex: ${targetIndex}`);
        console.info(`current offset: ${extraInfo.currentOffset}`);
        console.info(`target offset: ${extraInfo.targetOffset}`);
        console.info(`velocity: ${extraInfo.velocity}`);
      }); // 核心是这段代码
      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext();
          });
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious();
          });
      }.margin(5);
    }.width('100%')
    .margin({ top: 5 });
  }
}
```

输出结果和效果预览一致。

另外，currentOffset、targetOffset、velocity分别输出了Swiper当前显示元素在主轴方向上，相对于Swiper起始位置的位移、Swiper动画目标元素在主轴方向上，相对于Swiper起始位置的位移以及Swiper离开动画开始时的离开速度。这些数据可以对手势进行更具体的监听。
