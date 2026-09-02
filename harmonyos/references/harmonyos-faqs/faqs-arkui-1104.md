---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1104
title: 如何解决页面跳转无响应问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决页面跳转无响应问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:975beb4ca40b518f830b3b2c79b7d45f8ea8ba41357e15c0d55a5e6529ee339b
---

## 问题现象

使用Navigation进行页面跳转或返回时，页面无响应，如何排查？

## 背景知识

* [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)组件是路由导航的根视图容器，可以通过导航控制器[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)跳转[NavDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)子页。
* [pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)通过指定的路由名称将目标页面压入导航栈，并支持传递参数。
* 开发者可参考[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)实现对系统路由表的文件配置。
* [routerMap标签](../harmonyos-guides/module-configuration-file.md#routermap标签)：标识模块配置的路由表的路径。可在resources/base/profile下面定义配置文件，文件名可以自定义，例如：router\_map.json。

## 解决方案

1. 检查父页面是否有使用Navigation组件承载路由，跳转目标页面的根节点使用NavDestination组件。
2. 检查导航控制器NavPathStack是否绑定Navigation组件。
3. 使用系统路由表时，检查resources/base/profile路径中是否创建了系统路由表配置文件；使用自定义路由表时，检查Navigation组件的[navDestination](../harmonyos-references/ts-basic-components-navigation.md#navdestination10)是否绑定路由路径与页面组件。
4. 检查跳转方法中的name（NavDestination页面名称）在系统路由表配置文件是否被正确定义。
5. 检查子页面是否自行创建NavPathStack而非复用父级栈。
   * 方法一：通过@Consume注入父级栈。
   * 方法二：在页面初始化时，通过[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)回调确保子页面和父页面为同一NavPathStack，参考[示例7（通过onReady获取栈）](../harmonyos-references/ts-basic-components-navigation.md#示例7通过onready获取栈)。
6. 代码混淆会导致无法跳转，若采用系统路由表进行跳转，则需将模块下resources/base/profile/route\_map.json文件中pageSourceFile字段对应的路径添加到白名单中。使用[-keep-file-name](../harmonyos-guides/source-obfuscation-keep-options.md#section-keep-file-name)来保留这些文件路径。对于API20及之后版本，不再需要手动配置白名单。
7. Tabs嵌套Navigation时，检查是否存在多个Navigation同时绑定了同一个NavPathStack对象。

正确使用Navigation跳转可参考如下代码：

```ts
class TabNavStack {
  id: number; // 标识符
  navStack: NavPathStack; //  导航栈对象。需确保每个TabContent内Navigation绑定的NavPathStack对象不同
  content: string; // 内容

  constructor(id: number, navStack: NavPathStack, content: string) {
    this.id = id;
    this.navStack = navStack;
    this.content = content;
  }
}

@Entry
@Component
struct Index {
  pageStack1: NavPathStack = new NavPathStack();
  pageStack2: NavPathStack = new NavPathStack();
  pageStack3: NavPathStack = new NavPathStack();
  tabArr: TabNavStack[] = [
    new TabNavStack(1, this.pageStack1, '页签1的内容'),
    new TabNavStack(2, this.pageStack2, '页签2的内容'),
    new TabNavStack(3, this.pageStack3, '页签3的内容')
  ];
  @State currentIndex: number = 0;

  @Builder
  tabBuilder(index: number) {
    Column() {
      Text(`页签${index + 1}`)
        .fontSize(16)
        .padding(16)
        .fontColor(this.currentIndex === index ? '#0a59f7' : '#000000');
    }
    .width('100%')
    .height('100%');
  }

  build() {
    Tabs() {
      ForEach(this.tabArr, (item: TabNavStack, index: number) => {
        TabContent() {
          NavigationComponent({ pageStack: item.navStack, content: item.content });
        }
        .tabBar(this.tabBuilder(index));
      });
    }
    .width('100%')
    .height('100%')
    .onChange((index: number) => {
      this.currentIndex = index;
    });
  }
}

@Component
struct NavigationComponent {
  pageStack: NavPathStack = new NavPathStack();
  content: string = '';

  build() {
    // 父页面需要由Navigation承载路由
    Column() {
      // NavPathStack导航控制器需与Navigation绑定。
      Navigation(this.pageStack) {
        Column() {
          Text(`${this.content}1`)
            .fontSize(24)
            .padding(16);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      }
      .clip(true)
      .hideTitleBar(true)
      .height('60%')
      .backgroundColor('#f1f3f5')
      .borderRadius(8);
      Button('跳转到下一页面', { type: ButtonType.Capsule })
        .fontSize(16)
        .height(40)
        .margin({ top: 24 })
        .onClick(() => {
          // 传入的页面字符串与router_map.json文件中的name是否一致，注意大小写。
          this.pageStack.pushPathByName('PageOne', this.content, true);
        });
      Button('返回上一页', { type: ButtonType.Capsule })
        .fontSize(16)
        .margin({ top: 16 })
        .height(40)
        .onClick(() => {
          // 传入的页面字符串与router_map.json文件中的name是否一致，注意大小写。
          this.pageStack.pop();
        });
    }
    .padding({ left: 16, right: 16 })
    .width('100%')
    .height('100%');
  }
}
```

```ts
// 跳转页面入口函数
@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
struct PageOne {
  // 确保子页面可通过@Consume或参数传递共享同一个NavPathStack实例
  pathStack: NavPathStack = new NavPathStack();
  @State content: string = '';

  build() {
    Column() {
      NavDestination() {
        Column() {
          Text(`${this.content}2`)
            .fontSize(24)
            .padding(16);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      }
      .hideBackButton(true)
      .hideTitleBar(true)
      .backgroundColor('#f1f3f5')
      .borderRadius(8)
      .onReady((context: NavDestinationContext) => {
        // 通过onReady事件能够拿到对应的NavPathInfo和所属的NavPathStack。
        this.pathStack = context.pathStack;
        this.content = context.pathInfo.param as string;
      });
    };
  }
}
```

src/main/resources/base/profile/router\_map.json配置如下所示：

```json
{
  "routerMap": [
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder"
    }
  ]
}
```

效果图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/sPxKfcVVTpyQ5cd_knc2IQ/zh-cn_image_0000002658806741.png "点击放大")
