---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-451
title: Tabs组件，自定义tabBar切换动画有延迟，Tabs页面切换完才触发tabBar切换，如何修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs组件，自定义tabBar切换动画有延迟，Tabs页面切换完才触发tabBar切换，如何修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af2c4b417c5ab5543ee9b0b34e704404cbe0ec0a96077c3fbe63c4f1594f38af
---

新增一个selectedIndex的索引用于标识被选择的tabBar，原来的currentIndex仍然用于TabContent页签显示的控制。然后selectedIndex在onAnimationStart事件中进行切换，就可以实现页签内容切换动画发生时，tabBar也同步切换。

需要注意的是，selectedIndex和currentIndex不能为了方便使用同一个，否则会出现页面切换没有动画的情况，当共用变量时，onAnimationStart事件中的状态更新会立即触发TabContent重绘，导致系统跳过过渡动画。

可参考如下示例：

```ts
@Component
struct TabsDemo {
  @State tabArray: Array<number> = [0, 1, 2, 3];
  @State selectedIndex: number = 0;
  @State currentIndex: number = 0;
  @State selectedFontColor: Color = Color.Blue;
  @State fontColor: Color = Color.Black;
  private controller: TabsController = new TabsController();

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontSize(16)
        .lineHeight(22)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)

      Divider()
        .strokeWidth(2)
        .color('#007DEF')
        .opacity(this.selectedIndex === index ? 1 : 0)
    }
    .width('100%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        ForEach(this.tabArray,(item: number, index:number) => {
          // The system has its own tab.
          TabContent() {
            Text('我的内容' + item)
              .fontSize(30)
          }
          .tabBar(this.tabBuilder(item, 'bar' + item))
        })
      }
      .onChange((index: number) => {
        // CurrentIndex Control TabContent Display Tab.
        this.currentIndex = index;
      })
      .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
        if(index === targetIndex) {
          return;
        }
        // SelectedIndex controls the color switching between Image and Text in the custom TabBar.
        this.selectedIndex = targetIndex;
      })
    }
    .width('100%')
  }
}
```
