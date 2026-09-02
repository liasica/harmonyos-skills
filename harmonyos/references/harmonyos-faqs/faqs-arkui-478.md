---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-478
title: Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:018fc0eaa16a0116debee5d03c72d138d95a6fad70326372d5684df564cf9d92
---

**问题描述**

在Tabs刚启动的时候创建四个TabContent ，当this.isShowMessageTab为true会再加一个TabContent，

当前有遇到一个问题，当this.isShowMessageTab从false变到true后（即TabContent从4个变成5个后）。 点击最后一个tabBar后，再点击前面的tabBar就无法响应Tabs下的onChange，用左右滑动可以切换Tabs且触发onChange。

**解决方案**

定义一个selectedIndex变量，在onChange函数中将当前Tabs的index赋值给selectedIndex。此时selectedIndex的值等于当前被选中Tab的索引值。在tabBuilder中，对选中的Tab进行样式的修改即可。

完整示例代码如下：

```ts
@Entry
@Component
struct Index {
  private currentIndex: number = 0;
  private controller: TabsController = new TabsController();
  @State selectedIndex: number = 0;
  @State change: boolean = false;

  @Builder
  tabBuilder(index: number, name: string) {
    RelativeContainer() {
      Text(name)
        .fontColor(this.selectedIndex === index ? '#007DFF' : '#182431')
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .height('auto')
        .padding({
          left: 8,
          right: 8,
          top: 6,
          bottom: 6
        })
        .id('textTitle')
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })
      Divider()
        .strokeWidth(1)
        .color('#C3C3C3')
        .width(100)
        .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.selectedIndex === index ? 1 : 0)
        .width(100)
        .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
    }
    .width(100)
    .backgroundColor('#F0F1F3')
  }

  build() {
    RelativeContainer() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          Text('Page One')
        }
        .tabBar(this.tabBuilder(0, 'Page One'))
        .backgroundColor('#ffa2051d')

        TabContent() {
          Text('Page Two, Click on Page Three to show or hide')
            .onClick(() => {
              this.change = !this.change;
            })
        }
        .tabBar(this.tabBuilder(1, 'Page Two'))
        .backgroundColor('#ffefd005')

        if (this.change) {
          TabContent() {
            Text('Page Three')
          }
          .tabBar(this.tabBuilder(2, 'Page Three'))
          .backgroundColor('#ff061ef8')

          TabContent() {
            Text('Page Four')
          }
          .tabBar(this.tabBuilder(3, 'Page Four'))
          .backgroundColor('#ff039105')

          TabContent() {
            Text('Page Five')
          }
          .tabBar(this.tabBuilder(4, 'Page Five'))
          .backgroundColor('#ff02e7c4')
        }
        // When the page is hidden, it is necessary to ensure that the first parameter Index of the TabContent page is continuous
        else {
          TabContent() {
            Text('Page Four')
          }
          .tabBar(this.tabBuilder(2, 'Page Four'))
          .backgroundColor('#ff039105')

          TabContent() {
            Text('Page Five')
          }
          .tabBar(this.tabBuilder(3, 'Page Five'))
          .backgroundColor('#ff02e7c4')
        }
      }
      .barMode(BarMode.Scrollable)
      .barBackgroundColor('#fff3f3f3')
      .onChange((index) => {
        this.selectedIndex = index;
      })
      .animationDuration(400)
      .scrollable(true)
      .vertical(false)
      .width('100%')
      .fadingEdge(false)
    }
  }
}
```
