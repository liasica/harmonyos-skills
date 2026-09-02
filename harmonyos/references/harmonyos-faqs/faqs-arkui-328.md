---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-328
title: Tab组件页面切换时，如何不显示中间过渡的tab页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tab组件页面切换时，如何不显示中间过渡的tab页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7b658a671de639b0224b1388601a0ed4eff88090560438bca3950d8895dbd8a9
---

如果需要做动画，可以通过设置[.animationDuration(0)](../harmonyos-references/ts-container-tabs.md#animationduration)跳过中间过渡页显示，示例代码如下：

```ts
@Entry
@Component
struct TABTransitionAnimation {
  @State fontColor: string = '#182431';
  @State selectedFontColor: string = '#007DFF';
  @State currentIndex: number = 0;
  private tabController: TabsController = new TabsController();

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({
          top: 17,
          bottom: 7
        })
      Divider()
        .strokeWidth(2)
        .color($r('sys.color.brand'))
        .opacity(this.currentIndex === index ? 1 : 0)
    }
    .width('100%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.tabController }) {
        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#00CB87')
        }.tabBar(this.tabBuilder(0, 'green'))

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor($r('sys.color.brand'))
        }.tabBar(this.tabBuilder(1, 'blue'))

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor($r('sys.color.multi_color_11'))
        }.tabBar(this.tabBuilder(2, 'yellow'))

        TabContent() {
          Column()
            .width('100%')
            .height('100%')
            .backgroundColor('#E67C92')
        }
        .tabBar(this.tabBuilder(3, 'pink'))
      }
      .width(360)
      .height(296)
      .barWidth(360)
      .barHeight(56)
      .vertical(false)
      .barMode(BarMode.Fixed)
      .backgroundColor('#F1F3F5')
      .margin({ top: 52 })
      .animationDuration(0) // Setting the animation time to 0 can solve the problem of switching between pages and displaying intermediate transition pages
      .onChange((index: number) => {
        if (index >= 0 && index <= 3) {
          this.currentIndex = index;
        }
      })
    }
    .width('100%')
  }
}
```
