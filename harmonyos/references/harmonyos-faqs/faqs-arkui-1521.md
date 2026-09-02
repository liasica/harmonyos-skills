---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1521
title: 跳转其他页面返回时，如何设置Tabs的默认显示页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 跳转其他页面返回时，如何设置Tabs的默认显示页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f8011396179fd6a4ae97bb217cec3c8bcbe71dc47a0ad334cc1f8ee8ec369284
---

## 问题现象

使用Tabs组件，如何实现当前显示页签为1的页面内容，点击某个页签使用router跳转到其他页面再返回时，显示的依然是页签为1的页面内容？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/t_ZPRtzNTc2mnvZiXrAOIQ/zh-cn_image_0000002658966205.gif "点击放大")

## 背景知识

* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)：页面每次显示时触发一次，包括路由过程、应用进入前台等场景，仅[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件作为页面时生效。
* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [getRouter().pushUrl()](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)：跳转到应用内的指定页面，通过Promise获取跳转异常的返回结果。

## 解决方案

@Entry修饰的页面在显示时会触发onPageShow生命周期回调，可以在此回调中设置页面显示的初始状态，Tabs组件显示具体哪个页面由Tabs内的currentIndex参数决定的，当页面返回时在onPageShow()方法内重设currentIndex的值使其显示对应页面。运行下述示例需要自行创建一个简单的PageA页面。

```screen
class TabBar {
  title: string;
  index: number;

  constructor(title: string, index: number) {
    this.title = title;
    this.index = index;
  }
}

@Entry
@Component
struct TabsTestPage {
  uiContext = this.getUIContext();
  // 当前选中Tabs的索引
  @State currentIndex: number = 1;
  // 判断Tabs是否选中（用于自定义Tabs列表的选中状态）

  @State selectedIndex: number = 0;
  private tabsController: TabsController = new TabsController();
  private tabBars: TabBar[] = [
    new TabBar('翻译机', 0),
    new TabBar('首页', 1),
    new TabBar('推荐', 2),
  ];

  // 页面显示时初始化状态
  onPageShow(): void {
    this.currentIndex = 1;
  }

  // 自定义Tabs组件构建函数
  @Builder
  TabBuilder() {
    List() {
      ForEach(this.tabBars, (item: TabBar, index: number) => {
        ListItem() {
          Column() {
            Text(item.title) // 根据选中状态改变文字颜色
              .fontColor(this.currentIndex === item.index ? '#0A59F7' : Color.Black)
              .fontSize(20)
              .align(Alignment.Center);
          }
          .justifyContent(FlexAlign.Center)
          .alignItems(HorizontalAlign.Start)
          .margin({ left: 10 })
          .onClick(() => {
            // 更新Tabs组件的选中状态
            this.currentIndex = index;
          });
        }.height(100);
      });
    }.height(100)
    .listDirection(Axis.Horizontal)
    .scrollBar(BarState.Off);
  }

  build() {
    Column() {
      Flex({ alignItems: ItemAlign.Center }) {
        this.TabBuilder();
      }.width('100%').height(100);

      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.tabsController }) {
        TabContent() {
          Text('翻译机的内容')
            .fontSize(30)
            .onClick(() => {
              let promptShow = this.uiContext.getPromptAction();
              promptShow.showToast({
                message: '翻译机跳转'
              });
              // 需要自行创建一个PageA的@Entry页面
              this.uiContext.getRouter().pushUrl({ url: 'pages/PageA' });
            });
        };

        TabContent() {
          Text('首页的内容')
            .fontSize(30);
        };

        TabContent() {
          Text('推荐的内容')
            .fontSize(30);
        };
      }.barHeight(0)
      .onAnimationStart((targetIndex: number) => {
        this.currentIndex = targetIndex;
      })
      .onChange((index: number) => {
        // currentIndex控制TabContent显示页签
        this.currentIndex = index;
        this.selectedIndex = index;
      });

    }.height('100%').width('100%');
  }
}
```

## 总结

单例模式跳转时，由于也是复用路由栈内已有的页面实例，也可在本方案所述的页面生命周期内实现。
