---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-602
title: 如何只展示对应的TabContent的内容页
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何只展示对应的TabContent的内容页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a04c32a8826fbdc9b8538ee622f3d885bd62d01a9dcaaefd87bdb9c4021689d
---

## 问题现象

在Tabs组件中，由于Tabs组件自带滑动切换页面动画，所以在点击tabBar切换页面时会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载。

## 背景知识

* LazyForEach必须在容器组件内使用，仅有List、ListItemGroup、Grid、Swiper以及WaterFlow组件支持数据懒加载，其他组件仍然是一次性加载所有的数据，参考[使用限制](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#使用限制)。
* 自定义Tabs页面切换动画，参考[customContentTransition](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)的使用。

## 解决方案

* **方案一**：由于Tabs组件自带滑动切换页面动画，在点击tabBar切换页面、会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载。可以使用自定义切换动画去规避Tabs组件自带的动画。参考customContentTransition使用说明。

  ```screen
  @Entry
  @Component
  struct TabsExample {
    @State currentIndex: number = 0;
    private tabsController: TabsController = new TabsController();
    // 设置页面切换动画，代替滑动跳转页面动画
    private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
      (from: number, to: number) => {
        console.info(`from ${from} to ${to}`);
        let tabContentAnimatedTransition = {
          timeout: 1000,
          transition: (proxy: TabContentTransitionProxy) => {
            this.getUIContext().animateTo({
              duration: 0,
              onFinish: () => {
                proxy.finishTransition();
              }
            }, () => {
            });
          }
        } as TabContentAnimatedTransition;
        return tabContentAnimatedTransition;
      };

    build() {
      Column() {
        Tabs({ index: this.currentIndex, controller: this.tabsController }) {
          TabContent() {
            MyComponent({ color: '#00CB87' });
          }.tabBar(SubTabBarStyle.of('green'));

          TabContent() {
            MyComponent({ color: '#007DFF' });
          }.tabBar(SubTabBarStyle.of('blue'));

          TabContent() {
            MyComponent({ color: '#FFBF00' });
          }.tabBar(SubTabBarStyle.of('yellow'));

          TabContent() {
            MyComponent({ color: '#E67C92' });
          }.tabBar(SubTabBarStyle.of('pink'));
        }
        .customContentTransition(this.customContentTransition)
        .width('100%')
        .height(296)
        .onChange((index: number) => {
          this.currentIndex = index;
        });
      };
    }
  }

  @Component
  struct MyComponent {
    private color: string = '';

    aboutToAppear(): void {
      console.info(`------aboutToAppear backgroundColor: ${this.color}`); // 通过打印日志可以观察到没有加载中间页面
    }

    aboutToDisappear(): void {
      console.info(`------aboutToDisappear backgroundColor: ${this.color}`);
    }

    build() {
      Column() {
        Text(this.color)
          .width('90%')
          .height(200)
          .borderRadius(10)
          .backgroundColor($r('sys.color.comp_background_focus'))
          .textAlign(TextAlign.Center)
          .fontSize(30);
      };
    }
  }
  ```
* **方案二**：若要同时规避加载中间页面、又要保留手势滑动切换页面功能，可以使用Swiper自定义实现Tabs组件。通过调用SwiperController的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex12)方法翻至指定页面，useAnimation设置为false时没有动效。

  ```screen
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
  struct SwiperExample {
    private swiperController: SwiperController = new SwiperController();
    private data: MyDataSource = new MyDataSource([]);

    aboutToAppear(): void {
      let list: number[] = [];
      for (let i = 1; i <= 10; i++) {
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
              .borderRadius(10)
              .backgroundColor($r('sys.color.comp_background_focus'))
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(1)
        .autoPlay(true)
        .interval(4000)
        .loop(true)
        .duration(1000)
        .itemSpace(0)
        .indicator(false);

        Row({ space: 12 }) {
          Button('change to index:4')
            .onClick(() => {
              this.swiperController.changeIndex(3, false);
            });
          Button('change to index:7')
            .onClick(() => {
              this.swiperController.changeIndex(6, false);
            });
        }.margin(5);
      }.width('100%')
      .margin({ top: 5 });
    }
  }
  ```
