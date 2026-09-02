---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-468
title: 如何实现Tabs切换页签，强制重新刷新页面数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Tabs切换页签，强制重新刷新页面数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f20b59ea8e6572c60d7e18da068380f8a6979b24d53a6490711ecdd3361ad0b3
---

**问题描述**

在Tab切换数据没重新加载，如何保证每次点击Tab标签都能重新加载数据，包含一级Tab栏和二级Tab栏。

**解决措施**

可以通过在主页面通过emitter.emit('refreshTable')发送指定的事件refreshTable来强制重新刷新页面数据，即当Tab切换至index=0时触发事件，子组件通过计数器变化驱动视图更新。

请参考如下示例：

```ts
import { SubTabContent } from './SubTabContent'
import { emitter } from '@kit.BasicServicesKit'

@Entry
@Component
export struct TabContentExample {
  @State fontColor: string = '#182431'
  @State selectedFontColor: string = '#007DFF'
  @State currentIndex: number = 0
  @State selectedIndex: number = 0
  @State refreshFlag: boolean = true
  private controller: TabsController = new TabsController()

  @Builder
  tabBuilder(index: number) {
    Column() {
      Text(`Tab${index + 1}`)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(20)
        .fontWeight(500)
        .lineHeight(14)
    }.width('100%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
        TabContent() {
          Column() {
            SubTabContent()
          }
          .width('100%')
        }.tabBar(this.tabBuilder(0))

        TabContent() {
          Column() {
            Text('Tab2')
              .fontSize(36)
              .fontColor('#182431')
              .fontWeight(500)
              .opacity(0.4)
              .margin({ top: 30, bottom: 56.5 })
            Divider()
              .strokeWidth(0.5)
              .color('#182431')
              .opacity(0.05)
          }.width('100%')
        }.tabBar(this.tabBuilder(1))
      }
      .vertical(false)
      .barHeight(56)
      .onChange((index: number) => {
        this.currentIndex = index
        this.selectedIndex = index
        if (index === 0) {
          // 事件携带的数据
          let eventData: emitter.EventData = {
            data: {}
          };
          // 通过emitter.emit('refreshTable')发送指定的事件
          emitter.emit("refreshTable", eventData);
        }
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        if (index === targetIndex) {
          return
        }
        // selectedIndex控制自定义TabBar内Image和Text颜色切换
        this.selectedIndex = targetIndex
      })
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5')
      .margin({ top: 38 })
    }
    .width('100%')
    .height('100%')
    .padding({
      bottom: 30
    })
  }
}
```

在子页面通过emitter.on('refreshTable')持续订阅该事件去刷新数据。

请参考如下代码：

```ts
import { emitter } from '@kit.BasicServicesKit';

@Component
export struct SubTabContent {
  @State counter: number = 0

  aboutToAppear(): void {
    // Tabs子组件通过emitter.on('refreshTable')持续订阅该事件去刷新数据
    emitter.on("refreshTable", () => {
      this.counter += 1
    });
  }

  build() {
    Text(`切换Tabs刷新数据${this.counter}`)
  }
}
```
