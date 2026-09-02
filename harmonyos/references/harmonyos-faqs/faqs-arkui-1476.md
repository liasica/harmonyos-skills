---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1476
title: Tabs子组件切换时触发数据刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs子组件切换时触发数据刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0850a3b68215350447c2c592419581ea64a9286812996c1a515ded53c11ec18e
---

## 问题现象

在实际开发过程中，切换Tabs时通常会涉及内容视图的数据刷新。以下是常见的Tabs页面刷新场景：

* 场景一：Tabs每次切换时，目标TabContent页面都请求数据刷新页面。
* 场景二：TabContent仅在首次显示时请求数据并刷新页面，后续切换回该TabContent时不再重复请求。

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [TabContent](../harmonyos-references/ts-container-tabcontent.md)：仅在Tabs中使用，对应一个切换页签的内容视图。
* [@ohos.events.emitter](../harmonyos-references/js-apis-emitter.md)主要提供线程间发送和处理事件的能力，包括对持续订阅事件或单次订阅事件的处理、取消订阅事件、发送事件到事件队列等。工作原理是使用[emitter.emit](../harmonyos-references/js-apis-emitter.md#emitteremit)发送指定事件，再通过[emitter.on](../harmonyos-references/js-apis-emitter.md#emitteron)持续订阅指定的事件，并在接收到该事件时，执行对应的回调处理函数。
* [@Provider装饰器和@Consumer装饰器：跨组件层级双向同步](../harmonyos-guides/arkts-new-provider-and-consumer.md)。
  + @Provider，即数据提供方，其所有的子组件都可以通过@Consumer绑定相同的key来获取@Provider提供的数据。
  + @Consumer，即数据消费方，可以通过绑定同样的key获取其最近父节点的@Provider的数据，当查找不到@Provider的数据时，使用本地默认值。

## 解决方案

| 场景 | 方案 |
| --- | --- |
| 场景一 | 方案一：基于事件总线（Emitter）的通信机制  方案二：基于状态共享（@Provider/@Consumer）的响应式通信 |
| 场景二 | 方案一：基于事件总线（Emitter）的通信机制  方案二：基于状态共享（@Provider/@Consumer）的响应式通信  方案三：基于自定义组件生命周期函数aboutToAppear实现 |

场景一：Tabs每次切换时，目标TabContent页面都请求数据刷新页面。

* 方案一：使用emitter发送切换信息，TabContent接收到消息后执行请求数据、刷新页面等操作。
  1. 在Tabs组件的onAnimationStart回调中，通过全局事件发射器emitter.emit发送页签切换事件。
  2. 在TabContent子组件通过emitter.on订阅事件，接收到事件时执行请求数据、刷新页面等操作。

  TabEmitterPage.ets代码如下：

  ```ts
  import { emitter } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct TabEmitterPage {
    fontColor: string = '#182431';
    selectedFontColor: string = '#007DFF';
    @State selectedIndex: number = 0;

    @Builder
    tabBuilder(index: number) {
      Column() {
        Text(`Tab${index + 1}`)
          .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
          .fontSize(20)
          .fontWeight(500);
      }.width('100%');
    }

    refreshTabContent(index: number) {
      if (index === 0) {
        // 事件携带的数据
        let eventData: emitter.EventData = {
          data: {}
        };
        // 通过emitter.emit('refreshTableOne')发送指定的事件
        emitter.emit('refreshTableOne', eventData);
      } else if (index === 1) {
        // 事件携带的数据
        let eventData: emitter.EventData = {
          data: {}
        };
        // 通过emitter.emit('refreshTableTwo')发送指定的事件
        emitter.emit('refreshTableTwo', eventData);
      }
    }

    build() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Column() {
            EmitterContentOne();
          }.height('100%').width('100%')
          .justifyContent(FlexAlign.Center);
        }.tabBar(this.tabBuilder(0));

        TabContent() {
          Column() {
            EmitterContentTwo();
          }.height('100%').width('100%')
          .justifyContent(FlexAlign.Center);
        }.tabBar(this.tabBuilder(1));
      }
      .barHeight(56)
      .onAnimationStart((index: number, targetIndex: number) => {
        if (index === targetIndex) {
          return;
        }
        this.selectedIndex = targetIndex; // selectedIndex控制自定义TabBar内Text颜色切换
        this.refreshTabContent(targetIndex); // 在切换动画启动时发送刷新事件
      }).width('100%').height('100%');
    }
  }

  @Component
  struct EmitterContentOne {
    @State counter: number = 0;

    aboutToAppear(): void {
      // Tabs子组件通过emitter.on持续订阅该事件去刷新数据
      emitter.on('refreshTableOne', () => {
        this.counter += 1;
      });
    }

    aboutToDisappear(): void {
      emitter.off('refreshTableOne');
    }

    build() {
      Text(`切换Tabs刷新数据${this.counter}`);
    }
  }

  @Component
  struct EmitterContentTwo {
    @State text: string = 'A';

    aboutToAppear(): void {
      // Tabs子组件通过emitter.on持续订阅该事件去刷新数据
      emitter.on('refreshTableTwo', () => {
        this.text += 'A';
      });
    }

    aboutToDisappear(): void {
      emitter.off('refreshTableTwo');
    }

    build() {
      Text(`切换Tabs刷新数据${this.text}`);
    }
  }
  ```
* 方案二：Tabs通过@Provider向TabContent子组件的@Consumer传递页签切换信息，TabContent监听页签切换信息并执行请求数据、刷新页面等操作。
  1. 在Tabs组件中，使用@Provide('refreshNumber')将当前切换的页签索引作为共享状态进行发布。在onAnimationStart回调中更新该状态值，实现状态同步。
  2. TabContent子组件通过@Consume('refreshNumber')获取该共享状态，并通过[@Watch](../harmonyos-guides/arkts-watch.md)监听refreshNumber的变化，当refreshNumber与自身对应的页签索引一致时，执行请求数据、刷新页面等操作。

  ConsumerPage.ets代码如下：

  ```ts
  @Entry
  @Component
  struct ConsumerPage {
    fontColor: string = '#182431';
    selectedFontColor: string = '#007DFF';
    @Provide('refreshNumber') refreshNumber: number = 0; // 记录要刷新的子页
    @State selectedIndex: number = 0;

    @Builder
    tabBuilder(index: number) {
      Column() {
        Text(`Tab${index + 1}`)
          .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
          .fontSize(20)
          .fontWeight(500);
      }.width('100%');
    }

    build() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Column() {
            ConsumerContentOne({ index: 0 });
          }.height('100%').width('100%')
          .justifyContent(FlexAlign.Center);
        }.tabBar(this.tabBuilder(0));

        TabContent() {
          Column() {
            ConsumerContentTwo({ index: 1 });
          }.height('100%').width('100%')
          .justifyContent(FlexAlign.Center);
        }.tabBar(this.tabBuilder(1));
      }
      .barHeight(56)
      .onAnimationStart((index: number, targetIndex: number) => {
        if (index === targetIndex) {
          console.info(`onAnimationStart ${index} ${targetIndex}`);
          return;
        }
        this.selectedIndex = targetIndex; // selectedIndex控制自定义TabBar内Text颜色切换
        this.refreshNumber = targetIndex; // 更新目标页签，触发刷新
      })
      .width('100%')
      .height('100%');
    }
  }

  @Component
  struct ConsumerContentOne {
    index: number = 0; // 记录当前子页的页签序号
    @State counter: number = 0;
    @Consume('refreshNumber') @Watch('refresh') refreshNumber: number;

    refresh() {
      // 目标页签是当前子页
      if (this.index === this.refreshNumber) {
        // 在此进行网络请求
        this.counter += 1; // 刷新数据
      }
    }

    build() {
      Text(`切换Tabs刷新数据${this.counter}`);
    }
  }

  @Component
  struct ConsumerContentTwo {
    index: number = 0; // 记录当前子页的页签序号
    @State text: string = 'A';
    @Consume('refreshNumber') @Watch('refresh') refreshNumber: number;

    refresh() {
      // 目标页签是当前子页
      if (this.index === this.refreshNumber) {
        // 在此进行网络请求
        this.text += 'A'; // 刷新数据
      }
    }

    build() {
      Text(`切换Tabs刷新数据${this.text}`);
    }
  }
  ```

场景二：TabContent仅在首次显示时请求数据并刷新页面，后续切换回该TabContent时不再重复请求。

* 方案一：在场景一的方案一基础上，在TabContent子组件添加一个是否已请求数据的标识。在首次请求并完成数据加载后，将该标识设置为false，后续切换时不触发请求。
* 方案二：在场景一的方案一基础上，在TabContent子组件添加一个是否已请求数据的标识。在首次请求并完成数据加载后，将该标识设置为false，以避免后续切换时重复请求。

  示例如下：对ConsumerPage.ets中的ConsumerContentTwo组件做如下修改后，则该子组件只会刷新一次。

  ```ts
  @Component
  export struct ConsumerContentTwo {
    enableFresh: boolean = true;
    index: number = 0; // 记录当前子页的页签序号
    @State text: string = 'A';
    @Consume('refreshNumber') @Watch('refresh') refreshNumber: number;

    refresh() {
      // 目标页签是当前子页
      if (this.enableFresh && this.index === this.refreshNumber) {
        // 在此进行网络请求
        this.text += 'A'; // 刷新数据
        this.enableFresh = false;
      }
    }

    build() {
      Text(`切换Tabs刷新数据${this.text}`);
    }
  }
  ```
* 方案三：将数据请求操作放在TabContent子组件的[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期中，此回调只会执行一次。

## 常见FAQ

Q：Tab中其嵌套Web页面，在Web页面的onPageShow添加页面刷新不生效？

A：在TabContent里面的子组件不会回调onPageShow方法，参考上述方案刷新TabContent子页。

Q：为什么数据在页签切换时没有立即更新，在切换完成后页面才刷新数据？

A：Tabs的onChange事件是在页面切换之后才开始执行的，所以会出现数据未及时的情况。可以将刷新的逻辑放在[onAnimationStart](../harmonyos-references/ts-container-tabs.md#onanimationstart11)或[onSelected](../harmonyos-references/ts-container-tabs.md#onselected18)中执行。

Q：数据dataSource已经改变了，但是页面没有刷新？

A：根据dataSource所使用的装饰器，查看官网文档中此装饰器对应限制条件。并按[状态变量改变不触发组件刷新问题常用定位方法](../harmonyos-guides/troubleshooting-state-manage.md)进行排查。

Q：为什么TabContent切换时，布局会变动，页面内容闪烁？

A：在设置根组件的justifyContent属性时，使用了和页签索引绑定的@State状态变量，所以页签切换时，TabContent会重绘。
