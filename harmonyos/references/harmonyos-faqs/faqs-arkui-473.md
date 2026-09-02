---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-473
title: Tabs如何实现预加载特定的TabContent页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tabs如何实现预加载特定的TabContent页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb5991fded4e7679c77093ef87a88495f5f2bf47829cbbf39ae282f61d53a17d
---

方案一：不论用ForEach还是LazyForEach循环渲染TabContent里面的内容都是一次渲染，故不能使用循环渲染。

由于Tabs组件自带滑动切换页面动画，所以在点击TabBar切换页面时会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载。可以使用自定义切换动画去规避Tabs组件自带的动画导致多个TabContent加载的问题。参考customContentTransition使用说明。

参考代码：

```ts
@Entry
@Component
struct TabsDemo {
  @State currentIndex: number = 0;
  private tabsController: TabsController = new TabsController();
  // Set up page switching animations instead of sliding to jump to page animations
  private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
    (from: number, to: number) => {
      let tabContentAnimatedTransition = {
        timeout: 1000,
        transition: (proxy: TabContentTransitionProxy) => {
          this.getUIContext().animateTo({
            duration: 0,
            onFinish: () => {
              proxy.finishTransition();
            }
          }, () => {
          })
        }
      } as TabContentAnimatedTransition
      return tabContentAnimatedTransition;
    }

  build() {
    Column() {
      Tabs({ index: this.currentIndex, controller: this.tabsController }) {
        TabContent() {
          MyComponent({ color: '#00CB87' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#007DFF' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#FFBF00' })
        }.tabBar(SubTabBarStyle.of('green'))

        TabContent() {
          MyComponent({ color: '#E67C92' })
        }.tabBar(SubTabBarStyle.of('green'))
      }
      .customContentTransition(this.customContentTransition)
      .width('100%')
      .height(296)
      .barBackgroundColor('#F1F3F5')
      .onChange((index: number) => {
        this.currentIndex = index;
      })
    }
  }
}

@Component
struct MyComponent {
  private color: string = '';

  aboutToAppear(): void {
    // It can be observed by printing the log that no intermediate page has been loaded
    console.info('aboutToAppear backgroundColor:' + this.color);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear backgroundColor:' + this.color);
  }

  build() {
    Column()
      .width('100%')
      .height('100%')
      .backgroundColor(this.color)
  }
}
```

方案二：若要同时规避加载中间页面，又要保留手势滑动切换页面功能，可以使用Swiper自定义实现Tabs组件。通过调用SwiperController的changeIndex方法翻至指定页面，useAnimation设置为false时没有动效。

参考代码：

```typescript
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

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);

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
            .backgroundColor(0XAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
        }, (item: string) => item)
      }
      .cachedCount(2)
      .index(1)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .indicator(false)

      Row({ space: 12 }) {
        Button('change to index:4')
          .onClick(() => {
            this.swiperController.changeIndex(3, false);
          })
        Button('change to index:7')
          .onClick(() => {
            this.swiperController.changeIndex(6, false);
          })
      }
      .margin(5)
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```
