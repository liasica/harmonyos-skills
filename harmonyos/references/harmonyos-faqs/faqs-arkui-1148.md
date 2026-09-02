---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1148
title: Tabs页面Navigation路由跳转的实现方式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs页面Navigation路由跳转的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cae6d82c60167e07ab54e83208bf4edf295389b0f71ad3e05c89ded3823a44fb
---

## 问题现象

使用Tabs组件结合Navigation组件实现页面跳转时，虽然TabContent能够成功跳转，但TabBar部分并未消失。

代码如下：

TempPage.ets文件：

```ts
import { tabsub } from './tabsub';

@Entry
@Component
struct TempPage {
  @State currentIndex: number = 0
  controller: TabsController = new TabsController()
  @Provide('appPathStack') appPathStack: NavPathStack = new NavPathStack();

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        ForEach(['待办', '已办', '已发'], (item: string, index: number) => {
          TabContent() {
            Navigation(this.appPathStack) {
              tabsub()
            }
          }.tabBar(this.tabBuilder(index, item))
        })
      }
      .vertical(false)
      .barWidth('100%')
      .barHeight(37)
      .onChange((index: number) => {
        this.currentIndex = index
      })
      .backgroundColor(Color.White)
      .width('100%')
      .margin({ top: 0, bottom: 0 })
    }
    .height('100%')
    .width('100%')
  }

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontSize(14)
        .fontColor(this.currentIndex === index ? '#0A59F7' : '#666666')
        .fontWeight(this.currentIndex === index ? 500 : 400)
        .lineHeight(22)
      Divider()
        .strokeWidth(3)
        .color('#4A90E2')
        .opacity(this.currentIndex === index ? 1 : 0)
        .width(30)
      Divider()
        .strokeWidth(1)
        .color('#EEEEEE')
    }
    .backgroundColor(Color.White)
    .width('100%').height(44).justifyContent(FlexAlign.SpaceEvenly)
  }
}
```

tabsub.ets文件：

```ts
@Builder
export function tabsubBuilder() {
  tabsub();
}

@Component
export struct tabsub {
  @Consume('appPathStack') appPathStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('内容')
          .fontSize(30)
          .onClick(() => {
            this.appPathStack.pushPathByName('WebView', new Object({}));
          });
      }
      .height('100%')
      .width('100%')
      .border({ width: 1, radius: 20, color: '#f1f3f5' })
      .backgroundColor('#f1f3f5')
      .justifyContent(FlexAlign.Center);
    };
  }
}
```

WebView.ets文件：

```ts
@Builder
export function WebViewBuilder() {
  WebView();
}

@Component
export struct WebView {
  @Consume('appPathStack') appPathStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Text('test')
          .fontSize(30);
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#f1f3f5')
      .justifyContent(FlexAlign.Center)
      .border({ width: 1, radius: 20, color: '#f1f3f5' });
    }
    .padding({ left: 16, right: 16, top: 16 })
    .hideBackButton(true);
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/HqT8CPYyTUe8cFNHwlMMeg/zh-cn_image_0000002628569610.png "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [routerMap](../harmonyos-guides/module-configuration-file.md#routermap标签)：此标签标识模块配置的路由表的路径。

## 问题定位

根据代码逻辑排查出是由于Navigation组件放置TabContent内部导致的。

## 分析结论

Navigation组件放置在TabContent内部，在页面跳转时，只能实现TabContent内容的替换并不能覆盖到TabBar部分。

## 修改建议

将Navigation放到Tabs外层即实现跳转，同时需要在工程配置文件module.json5中配置{"routerMap": "$profile:router\_map"}。示例代码如下：

```ts
import { tabsub } from './tabsub';

@Entry
@Component
struct TempPage {
  @State currentIndex: number = 0;
  controller: TabsController = new TabsController();
  @Provide('appPathStack') appPathStack: NavPathStack = new NavPathStack();

  build() {
    Column() {
      // solution start
      // 将Navigation放到Tabs外层
      Navigation(this.appPathStack) {
        Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
          ForEach(['待办', '已办', '已发'], (item: string, index: number) => {
            TabContent() {
              tabsub();
            }.tabBar(this.tabBuilder(index, item))
            .padding({ left: 16, right: 16, top: 16 })
            .width('100%')
            .height('100%');
          });
        }
        .vertical(false)
        .barWidth('100%')
        .barHeight(37)
        .onChange((index: number) => {
          this.currentIndex = index;
        })
        .backgroundColor(Color.White)
        .margin({ top: 0, bottom: 0 });
      }
      .hideToolBar(true);
      // solution end
    }
    .height('100%')
    .width('100%');

  }

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.currentIndex === index ? '#0A59F7' : '#000000')
        .lineHeight(22);
      Divider()
        .strokeWidth(2)
        .color('#0A59F7')
        .opacity(this.currentIndex === index ? 1 : 0)
        .width(30);
      Divider()
        .strokeWidth(1)
        .color('#EEEEEE');
    }
    .backgroundColor(Color.White)
    .width('100%').height(44).justifyContent(FlexAlign.SpaceEvenly);
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ZAV3-hWdSzKBtRMsbva2cw/zh-cn_image_0000002628409710.png "点击放大")

## 常见FAQ

Q：Navigation双栏模式下切换Tab页签，右边页面未切换成对应子页面。

A：点击切换Tab页签时触发[onTabBarClick](../harmonyos-references/ts-container-tabs.md#ontabbarclick10)事件，在此事件中清空路由栈并切换到对应子页面。
