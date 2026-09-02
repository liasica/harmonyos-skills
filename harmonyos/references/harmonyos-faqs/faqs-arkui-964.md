---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-964
title: NavDestination嵌套使用Tabs，TabContent页面如何跳转至目标页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > NavDestination嵌套使用Tabs，TabContent页面如何跳转至目标页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4891590c8fb24a4c042a9b466d2848c56c98842de64982147836120902b78dcd
---

## 问题现象

使用Navigation组件导航，NavDestination组件嵌套使用Tabs组件，TabContent组件内再嵌套使用自定义组件，如何在TabContent的自定义组件中使用NavPathStack方法跳转至目标页面？

## 背景知识

该问题涉及Navigation组件导航与Tabs两方面内容。

* 组件导航（[Navigation](../harmonyos-references/ts-basic-components-navigation.md)）主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)作为子页面的根容器，用于显示Navigation的内容区。
* [NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)：Navigation导航控制器，其中包含NavDestination页面，以栈的结构管理，称为路由栈。
* 当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](../harmonyos-guides/arkts-navigation-tabs.md)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。

## 解决方案

1. 在src/main目录下的module.json5配置文件中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下:

   ```json
   {
     "routerMap": [
       {
         "name": "PageTabs",
         "pageSourceFile": "src/main/ets/pages/PageTabs.ets",
         "buildFunction": "PageTabsBuilder",
         "data": {
           "description": "this is PageTabs"
         }
       },
       {
         "name": "HomePage",
         "pageSourceFile": "src/main/ets/pages/HomePage.ets",
         "buildFunction": "HomePageBuilder",
         "data": {
           "description": "this is HomePage"
         }
       },
       {
         "name": "MinePage",
         "pageSourceFile": "src/main/ets/pages/MinePage.ets",
         "buildFunction": "MinePageBuilder",
         "data": {
           "description": "this is MinePage"
         }
       },
       {
         "name": "OrderPage",
         "pageSourceFile": "src/main/ets/pages/OrderPage.ets",
         "buildFunction": "OrderPageBuilder",
         "data": {
           "description": "this is OrderPage"
         }
       }
     ]
   }
   ```
2. Navigation主页面（Index）页面内容：

   点击文字跳转到“父组件（PageTabs.ets）页面”。

   ```ets
   @Entry
   @Component
   struct Index {
     pathStack: NavPathStack = new NavPathStack();

     build() {
       Navigation(this.pathStack) {
         Column() {
           Text(`Navigation主页面`)
             .fontSize(30)
             .onClick(() => {
               this.pathStack.pushPath({ name: 'PageTabs' });
             });
         }
         .justifyContent(FlexAlign.Center)
         .width('100%')
         .height('100%');
       };
     }
   }
   ```
3. 父组件（PageTabs.ets）页面内容：

   UI架构说明：该页面中，Tabs组件为NavDestination组件的子组件，TabContent组件为Tabs组件的子组件，TabContent内为自定义的组件（HomePage和MinePage）。

   ```ets
   import { MinePage } from './MinePage';
   import { HomePage } from './HomePage';

   @Builder
   export function PageTabsBuilder() {
     PageTabs();
   }

   @Component
   struct PageTabs {
     @State pathStack: NavPathStack = new NavPathStack();
     private tabsController: TabsController = new TabsController();
     @State currentIndex: number = 0;

     @Builder
     tabBarBuilder(title: string, targetIndex: number) {
       Column() {
         Text(title)
           .lineHeight(14)
           .textAlign(TextAlign.Center)
           .fontSize(20)
           .fontWeight(20)
           .fontColor(this.currentIndex === targetIndex ? '#007DFF' : '#182431')
           .margin({ top: 3 });
       }
       .background('#F1F3F5')
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center);
     }

     build() {
       NavDestination() {
         Tabs({
           barPosition: BarPosition.End,
           index: this.currentIndex,
           controller: this.tabsController
         }) {
           TabContent() {
             HomePage(); // 首页内容组件，pathStack由context获取，跳转至其他页面失败
           }.tabBar(this.tabBarBuilder('首页', 0));

           TabContent() {
             MinePage({ pathStack: this.pathStack }); // 我的页面内容组件，pathStack由本页面传入，跳转其他页面成功
           }.tabBar(this.tabBarBuilder('我的', 1));

         }
         .barHeight(76)
         .vertical(false)
         .scrollable(false)
         .onChange((index: number) => {
           this.currentIndex = index;
           this.tabsController.changeIndex(index);
         });
       }
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack;
       });
     }
   }
   ```
4. “我的”页面（MinePage.ets）内容，pathStack由父组件传入，跳转至OrderPage页面成功：

   ```ets
   @Builder
   export function MinePageBuilder() {
     MinePage();
   }

   @Component
   export struct MinePage {
     pathStack: NavPathStack = new NavPathStack();

     onVisible() {
       console.info(`MinePage visible.`);
     }

     build() {
       NavDestination() {
         Column() {
           Text('我的').fontSize(20);
         }
         .width('100%')
         .height('100%')
         .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
           if (isVisible && currentRatio >= 1.0) { // 由隐藏至显示时执行下面方法
             this.onVisible();
           }
         })
         .onClick(() => {
           try {
             // pathStack由父组件传入，跳转至订单页面成功
             this.pathStack.pushPathByName('OrderPage', null);
           } catch (err) {
             console.error(`pushPathByName error, ${err}`);
           }
         });
       }
       .hideTitleBar(true)
       .title('Mine');
     }
   }
   ```
5. HomePage页面：

   ```ets
   @Builder
   export function HomePageBuilder() {
     HomePage();
   }

   @Component
   export struct HomePage {
     pathStack: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Column() {
           Text('首页').fontSize(20);
         }
         .width('100%')
         .height('100%')
         .onClick(() => {
           try {
             this.pathStack.pushPathByName('OrderPage', null);
           } catch (err) {
             console.error(`pushPathByName error, ${err}`);
           }
         });
       }
       .hideTitleBar(true)
       .title('Home')
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack;
       });
     }
   }
   ```
6. OrderPage页面：

   ```ets
   @Builder
   export function OrderPageBuilder() {
     OrderPage();
   }

   @Component
   export struct OrderPage {
     pathStack: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Column() {
           Text('订单').fontSize(20);
         }
         .width('100%')
         .height('100%');
       };
     }
   }
   ```
