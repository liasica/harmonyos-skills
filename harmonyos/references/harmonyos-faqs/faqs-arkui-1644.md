---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1644
title: HarmonyOS中Navigation组件单栏与分栏模式动态切换及横屏布局异常解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > HarmonyOS中Navigation组件单栏与分栏模式动态切换及横屏布局异常解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:f8e2e74135ddb814dacba58017e7f4c2aa53ed4883e5a41a4b05c43dca2cb2a0
---

## 问题现象

在应用开发中使用Navigation组件时，常遇到与单栏与分栏模式相关的显示需求或异常：

问题一：Navigation组件在宽屏设备（如平板、折叠屏）默认显示双栏，在普通手机竖屏默认显示单栏，开发者希望实现页面在单栏与分栏模式间动态切换显示。

问题二：应用在普通手机设备横屏显示时，发现页面内容仅占据屏幕左侧部分，右侧未铺满（呈现分栏样式）；而在竖屏时可以占据整个屏幕，如何修正此布局问题？

## 背景知识

* [Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的分栏模式由[mode属性](../harmonyos-references/ts-basic-components-navigation.md#mode9)控制，包括单栏（Stack）、分栏（Split）和自适应（Auto）三个属性。该属性默认为Auto模式，在该模式下会自动监听屏幕属性，当为折叠屏或平板时，默认分栏显示，在折叠状态或普通手机时可为单栏显示。可通过[状态管理](../harmonyos-guides/arkts-state-management-overview.md)实现动态切换mode属性的单栏与分栏模式，实现子页的放大效果。
* 状态管理中的[AppStorage](../harmonyos-references/ts-state-management.md#appstorage)能实现全局的UI状态存储且通过[@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)可以和AppStorage中key对应的属性建立双向数据同步：
  1. StorageLink装饰的变量本地发生修改后，该修改会被写回AppStorage中。
  2. AppStorage中的修改发生后，该修改会被同步到所有绑定AppStorage对应key的属性上实现状态同步，包括单向（@StorageProp和通过Prop创建的单向绑定变量）、双向（@StorageLink和通过Link创建的双向绑定变量）变量和其他实例（比如PersistentStorage）。

## 解决方案

* **针对问题一：实现页面在单栏与分栏模式间动态切换显示。**

  若应用需要在不同宽屏设备或用户交互中动态改变单栏与分栏效果，可以通过全局状态管理变量来控制 Navigation 组件的 mode 属性。

  + **场景一：特定子页面缩小与放大。**
    1. 通过 @StorageLink 创建状态管理变量 isSplit 控制 Navigation 组件的 mode 属性。

       ```ts
       @Entry
       @Component
       struct MainPage {
         pageInfos: NavPathStack = new NavPathStack();
         @StorageLink('isSplit') isSplit: boolean = true;

         // 跳转回主页时重新修改为分栏模式，根据实际需求设置
         aboutToAppear(): void {
           AppStorage.set('isSplit', true);
         }

         build() {
           Navigation(this.pageInfos) {
             Column() {
               Button('跳转')
                 .backgroundColor('#0a59f7')
                 .width('150')
                 .height('60')
                 .onClick(() => {
                   this.pageInfos.pushPath({ name: 'NavPageOne' });
                 })
             }
           }
           .mode(this.isSplit ? NavigationMode.Split : NavigationMode.Stack)
           .hideTitleBar(true)
           .hideToolBar(true)
         }
       }
       ```
    2. 通过 AppStorage.set 方法修改状态管理变量 isSplit 值，从而控制 Navigation 组件的 mode 属性，并刷新UI。

       ```ts
       @Builder
       export function NavPageOneBuilder() {
         NavPageOne();
       }

       @Component
       struct NavPageOne {
         @State message: string = '放大';

         // 跳转回该页面时重新修改为分栏模式，根据实际需求设置
         aboutToAppear(): void {
           AppStorage.set('isSplit', true);
         }

         build() {
           NavDestination() {
             RelativeContainer() {
               Text(this.message)
                 .onClick(() => {
                   let value = AppStorage.get<boolean>('isSplit');
                   if (value === false || value === undefined) {
                     AppStorage.set('isSplit', true);
                     this.message = '放大';
                   } else {
                     AppStorage.set('isSplit', false);
                     this.message = '缩小';
                   }
                 })
                 .width(50)
                 .textAlign(TextAlign.Center)
             }
             .height('100%')
             .width('100%')
           }
           .hideTitleBar(true)
         }
       }
       ```

       实现效果如下：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/EBPWHPOMSMKSWR3e-Tj8JA/zh-cn_image_0000002663720495.png "点击放大")
  + **场景二：跳转不同页面采用不同的模式设置。**

    在推送子页时修改 Navigation 模式，需要单栏显示的页面设置为 false，需要分栏显示的页面设置为 true。参考场景一，修改代码如下：

    ```ts
    @Builder
    export function NavPageTwoBuilder() {
      NavPageTwo();
    }

    @Component
    struct NavPageTwo {
      @State message: string = '缩小';

      // Startsolution1
      // 其它页面跳转该页面时，会先重置为单栏模式
      aboutToAppear(): void {
        AppStorage.set('isSplit', false);
        this.message = '缩小';
      }
      // Endsolution1

      build() {
        NavDestination() {
          RelativeContainer() {
            Text(this.message)
              .onClick(() => {
                let value = AppStorage.get<boolean>('isSplit');
                if (value === false || value === undefined) {
                  AppStorage.set('isSplit', true);
                  this.message = '放大';
                } else {
                  AppStorage.set('isSplit', false);
                  this.message = '缩小';
                }
              })
              .width(50)
              .textAlign(TextAlign.Center);
          }
          .height('100%')
          .width('100%');
        }
        .hideTitleBar(true);
      }
    }
    ```

    **注意**：以上方案未配置路由表，路由表配置相关官网：[系统路由表配置](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。在工程resources/base/profile中创建route\_map.json文件，并在跳转目标模块的配置文件module.json5添加该路由表。route\_map.json配置信息如下：

    ```json
    {
      "routerMap": [
        {
          "name": "NavPageTwo",
          "pageSourceFile": "src/main/ets/pages/NavPageTwo.ets",
          "buildFunction": "NavPageTwoBuilder"
        }
        ,{
          "name": "NavPageOne",
          "pageSourceFile": "src/main/ets/pages/NavPageOne.ets",
          "buildFunction": "NavPageOneBuilder"
        }
      ]
    }
    ```
* **针对问题二：修正普通手机设备横屏显示时分栏样式未铺满屏幕的布局问题。**

  **问题原因**：该现象是由 Navigation 组件的默认分栏模式引起的。Navigation 组件的 mode 属性默认值为 NavigationMode.Auto。从 API version 10 开始，当 Navigation 组件的宽度 >= 600vp 时，会自动采用 Split 分栏模式显示。普通手机在横屏时，宽度往往会达到或超过 600vp，从而自动触发分栏样式，导致页面内容仅占据屏幕左侧部分；而竖屏时宽度不足，保持单栏模式。

  **解决方案**：若应用希望在普通手机设备横屏时依然保持单栏全屏显示，可以将 Navigation 组件的 mode 属性强制指定为 NavigationMode.Stack。

  ```ts
  @Entry
  @Component
  struct MainPage {
    pageInfos: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pageInfos) {
        Column() {
          Button('跳转')
            .backgroundColor('#0a59f7')
            .width('150')
            .height('60')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'NavPageOne' });
            })
        }
      }
      .mode(NavigationMode.Stack) // 强制设置为单栏模式，避免横屏时自动切换为分栏模式
      .hideTitleBar(true)
      .hideToolBar(true)
    }
  }
  ```

## 常见FAQ

Q：[navBarWidth](../harmonyos-references/ts-basic-components-navigation.md#navbarwidth9)和[navBarWidthRange](../harmonyos-references/ts-basic-components-navigation.md#navbarwidthrange10)属性是否可以实现子页放大的功能？

A：不建议通过navBarWidth和navBarWidthRange实现子页放大功能，该方式存在一定的宽度限制，建议使用上述方案或者分栏模式下设置[hideNavBar()](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)为true。

Q：在进行一多适配时，通过display.getDefaultDisplaySync().width获取屏幕宽度然后给UI组件设置宽度，但是分栏模式下由于分栏不是整个屏幕宽度，会导致布局错乱。如何自动获取分栏的宽度？

A：目前没有直接的接口获取分栏的宽度，可以参考链接中[NavigationMode](../harmonyos-references/ts-basic-components-navigation.md#navigationmode9枚举说明)为Split时，navBarWidth（左分屏宽度）计算规则实现自动计算分栏宽度。从而进行一多适配分栏模式开发。

Q：Navigation如何禁用分栏模式？

A：Navigation组件默认处于Auto模式，其样式会根据应用窗口尺寸在单栏和双栏之间自动切换，想要禁用双栏模式，将Navigation的mode属性值置为Stack即可，其它更丰富的实现方式可参考官网：[实现单双栏的显示效果](../best-practices/bpta-multi-settings-application-page.md)。

Q：分栏模式下点击导航栏的页面推送导致右侧内容区渲染了多个相同的页面，返回时会多次返回相同的页面，有什么方式可以防止这种现象发生？

A：推送页面时采用单例模式跳转（即跳转时[LaunchMode](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)采用MOVE\_TO\_TOP\_SINGLETON或POP\_TO\_SINGLETON模式）或者设置判定变量判断是否推送过该页面，若是推送过则采用[this.pathStack.replacePathByName()](../harmonyos-references/ts-basic-components-navigation.md#replacepathbyname11)方法替换页面，而不是重新推送新页面。

Q：通过状态管理实现动态切换mode属性的单栏与分栏模式，是否会造成性能问题？

A：Navigation的mode属性虽然作用于整个容器，但是mode的改变只会调整容器的布局模式。由于ArkUI的UI开发模式属于MVVM模式，其组件更新机制是局部刷新（状态管理数据驱动更新），只有受影响的部分会重新渲染。
