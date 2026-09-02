---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-514
title: Navigation导航模式根页面onPageShow生命周期触发问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation导航模式根页面onPageShow生命周期触发问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:57+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3510c8d14a2d94b3ea4aa5efd31b79682932608aa983c5867a1ccbdf8b96dd11
---

## 问题现象

当采用Navigation导航时，软件切换后台再切换回前台或手机黑屏重新打开后，会触发子页面的aboutToAppear()事件。

* 根页面问题代码参考如下：

  ```ts
  @Entry
  @Component
  struct Index {
    pageStacks: NavPathStack = new NavPathStack();

    onPageShow(): void {
      setTimeout(() => {
        this.pageStacks.replacePathByName('MainPage', null);
      }, 2000);
    }

    build() {
      Navigation(this.pageStacks) {
        Column() {
          Text('我是启动页面！')
            .fontSize(30);
        }
        .height('100%')
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .hideToolBar(true)
      .hideBackButton(true);
    }
  }
  ```
* 子页面问题代码参考如下：

  ```ts
  @Builder
  export function MainPageBuilder() {
    MainPage();
  }

  @Component
  export struct MainPage {
    @Provide pageStacks: NavPathStack = new NavPathStack();
    @State message: string = 'Hello World!';

    aboutToAppear(): void {
      setTimeout(() => {
        this.message = '触发了aboutToAppear事件!';
      }, 2000);
    }

    build() {
      NavDestination() {
        Column() {
          Text(this.message)
            .fontSize(30)
            .fontColor(Color.Black);
        }
        .height('100%')
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .hideTitleBar(true)
      .onReady((context: NavDestinationContext) => {
        this.pageStacks = context.pathStack;
      });
    }
  }
  ```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/sKagxLDRRnSGmU1O9-z09Q/zh-cn_image_0000002628548522.gif "点击放大")

## 效果预览

退出到后台，重新进入页面后不会重新创建子页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/crrTynT1SuuyVS-vC81iHQ/zh-cn_image_0000002658907837.gif "点击放大")

## 背景知识

[Navigation导航](../harmonyos-references/ts-basic-components-navigation.md)：官方推荐的路由导航方式，支持更丰富的动效、一次开发多端部署能力和更灵活的栈操作。在进行路由导航时需要与[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)搭配使用。其中Navigation作为page页面的根容器，NavDestination子页面为Navigation的内容展示区。

生命周期差异：

* Navigation组件所在页面生命周期遵从@Entry修饰的页面的生命周期原则。
* NavDestination组件的生命周期参考：[子页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)。该生命周期本质是子组件的生命周期，不是页面级的，当NavDestination页面显示在Navigation页面上时，并不会触发Navigation所在页面的[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)事件。

## 问题定位

1. 由问题描述中展示的现象可知：当页面隐藏后台，再显示的时候触发了NavDestination页面的[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)事件，重新创建了子页面。
2. 问题代码中，能让子页面重新创建的代码是Navigation根页面的onPageShow()事件的将子页面推送入栈操作。

   将问题代码中根页面onPageShow()事件修改如下：

   ```ts
   onPageShow(): void {
     setTimeout(() => {
       this.pageStacks.replacePathByName('MainPage', null);
     }, 2000);
     console.info('执行了根页面的onPageShow事件！');
   }
   ```

对应用进行隐藏/显示操作，并查看打印日志：

```txt
11-18 17:20:31.949   32047-32047   A00000/testTag                  com.examp...58799701  I     Succeeded in loading the content.
11-18 17:20:31.978   32047-32047   A03d00/JSAPP                    com.examp...58799701  I     执行了根页面的onPageShow事件！
11-18 17:20:45.403   32047-32047   A00000/testTag                  com.examp...58799701  I     Ability onBackground
11-18 17:20:50.603   32047-32047   A03d00/JSAPP                    com.examp...58799701  I     执行了根页面的onPageShow事件！
11-18 17:20:50.614   32047-32047   A00000/testTag                  com.examp...58799701  I     Ability onForeground
```

发现在子页面作为最顶层显示时，此时对整个应用的隐藏与显示，会触发根页面的onPageShow()事件，从而导致黑屏后重新显示、前后台切换等操作会执行子页面重建入栈的操作。

## 分析结论

由于Navigation路由的底层逻辑为：NavDestination子页面实际是Navigation根页面的展示区域，是父子组件关系（本质是在一个页面内）。这种独特的导航方式导致，当NavDestination子页面显示在最上层时，前后台切换，看似只会触发该NavDestination子页面的显隐事件，实际也会触发Navigation所在的根页面的显隐事件。

## 修改建议

由于应用的显隐操作并不会触发aboutToAppear()，所以将Navigation根页面的onPageShow()事件更换为aboutToAppear()事件，核心修改如下：

```ts
aboutToAppear(): void {
  setTimeout(() => {
    this.pageStacks.replacePathByName('MainPage', null);
  }, 2000);
}
```

完整示例参考如下：

1. Index.ets主页面。

   ```ts
   @Entry
   @Component
   struct Index {
     pageStacks: NavPathStack = new NavPathStack();

     aboutToAppear(): void {
       setTimeout(() => {
         this.pageStacks.replacePathByName('MainPage', null);
       }, 2000);
     }

     build() {
       Navigation(this.pageStacks) {
         Column() {
           Text('我是启动页面！')
             .fontSize(30)
         }
         .height('100%')
         .width('100%')
         .justifyContent(FlexAlign.Center)
       }
       .hideToolBar(true)
       .hideBackButton(true)
     }
   }
   ```
2. MainPage.ets子页面。

   ```ts
   @Builder
   export function MainPageBuilder() {
     MainPage();
   }

   @Component
   export struct MainPage {
     @Provide pageStacks: NavPathStack = new NavPathStack();
     @State message: string = 'Hello World!';

     aboutToAppear(): void {
       setTimeout(() => {
         this.message = '触发了aboutToAppear事件!';
       }, 2000);
     }

     build() {
       NavDestination() {
         Column() {
           Text(this.message)
             .fontSize(30)
             .fontColor(Color.Black)
         }
         .height('100%')
         .width('100%')
         .justifyContent(FlexAlign.Center)
       }
       .hideTitleBar(true)
       .onReady((context: NavDestinationContext) => {
         this.pageStacks = context.pathStack;
       })
     }
   }
   ```

**说明** 

路由配置参考官网链接：[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。

## 常见FAQ

Q：为什么每次页面切到后台，再切到前台，都会刷新页面？

A：请排查刷新的页面是属于Navigation路由或者是router路由：

* router路由时，每个页面都是@Entry修饰的页面：刷新的方法调用被写在了页面的onPageShow()事件中，onPageShow()事件在每次页面进入前台时都会触发。如果仅需要页面第一次进入时调用刷新方法，建议将页面刷新方法调用写在页面的aboutToAppear()事件中。
* Navigation路由时，分两种情况：
  1. NavDestination子页面在顶层显示，触发了Navigation页面的onPageShow()刷新事件。此时可参照本文修改建议，将刷新事件放置在Navigation页面的aboutToAppear()事件中。
  2. NavDestination子页面在顶层显示，触发了NavDestination页面的[onShown()](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)刷新事件：onShown()事件在每次NavDestination子页面显隐时都会触发。如果仅需要子页面第一次进入时调用刷新方法，建议将子页面刷新方法调用写在页面的aboutToAppear()或[onReady()](../harmonyos-references/ts-basic-components-navdestination.md#onready11)事件中。

Q：Navigation导航时如何监听根页面的显隐事件？

A：由于Navigation页面和NavDestination所在的页面实际是父子组件的关系，导致NavDestination子页切换到Navigation页面时并不会触发Navigation页面的onPageShow事件。Navigation作为根页面，若需监听其显示与隐藏状态，可通过监听Navigation组件的[onNavBarStateChange()](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)事件，并在回调函数中判断页面的显示或隐藏状态。
