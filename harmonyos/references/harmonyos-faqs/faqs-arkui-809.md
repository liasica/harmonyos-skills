---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-809
title: Tabs组件实现的侧边栏，如何实现自顶到底的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs组件实现的侧边栏，如何实现自顶到底的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3200042f1e62b50c85de30bed7442636ce421a2b6836b5607aff9235d63c8bd
---

## 问题现象

在实现侧边栏时，希望侧边栏从最顶部开始往下排列，在条目撑满侧边栏时可以滑动，且在选中条目时能自动居中。但是使用Tabs组件中把页签设置在侧边，页签中的条目始终是居中排列，无法做到从最顶部开始往下排列。

## 背景知识

* [Tabs组件](../harmonyos-guides/arkts-navigation-tabs.md)：是一种常见的界面导航结构。通过页签容器，用户可以快捷地访问应用的不同模块。
* 使用Tabs组件时，可以使用[barMode(BarMode.Scrollable)](../harmonyos-references/ts-container-tabs.md#barmode枚举说明)配置实现可滚动页签，但是Tabs组件中条目高度无法自定义，而且条目数量未撑满Tabs组件时，无法实现自顶到底的效果。
* [List组件](../harmonyos-references/ts-container-list.md)适合连续、多行呈现同类数据，例如图片和文本。

## 解决方案

由于Tabs组件无法实现自顶到底的效果，可以通过自定义组件来达到此效果。实现如下：

* 最外层使用Row()组件包裹，使List自定义的导航栏和Tab页内容左右分布。
* 导航栏使用List实现，使用Scroller的[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法控制List的滚动，达到子项居中显示的效果。
* 使用TabsController的[changeIndex](../harmonyos-references/ts-container-tabs.md#changeindex)方法控制Tab组件的切换。

```ts
@Entry
@Component
struct Q2025040100041 {
  @State currentIndex: number = 0;
  tabBarArr: string[] = ['tab0', 'tab1', 'tab2', 'tab3', 'tab4', 'tab5', 'tab6', 'tab7', 'tab8', 'tab9'];
  listScroller: Scroller = new Scroller();
  tabsController: TabsController = new TabsController();

  build() {
    Row() {
      List({ scroller: this.listScroller }) {
        ForEach(this.tabBarArr, (item: string, index: number) => {
          ListItem() {
            Text(item)
              .fontColor(index === this.currentIndex ? "#0a59f7" : "#808080")
              .textAlign(TextAlign.Center)
              .height('100vp')
              .width('100vp');
          }
          .onClick(() => {
            this.currentIndex = index;
            this.listScroller.scrollToIndex(this.currentIndex, true, ScrollAlign.CENTER);
            this.tabsController.changeIndex(this.currentIndex);
          });
        });
      }
      .scrollBar(BarState.Off)
      .width('100vp')
      .height('100%');

      Tabs({ controller: this.tabsController, barPosition: BarPosition.Start }) {
        ForEach(this.tabBarArr, (item: string) => {
          TabContent() {
            Text(item).fontSize('30fp');
          };
        });
      }
      .barWidth(0)
      .backgroundColor("#f1f3f5")
      .onChange((index: number) => {
        this.currentIndex = index;
        this.listScroller.scrollToIndex(this.currentIndex, true, ScrollAlign.CENTER);
      })
      .vertical(true)
      .width('calc(100% - 100vp)')
      .height('100%');
    }
    .alignItems(VerticalAlign.Top)
    .width('100%')
    .height('100%');
  }
}
```
