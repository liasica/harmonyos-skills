---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1214
title: 如何解决NavDestination页面做首页时跳转动画异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决NavDestination页面做首页时跳转动画异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:57+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:dc446008005d2fc432129bb5f0677e017c579209dd268e85fb03679fe14a8135
---

## 问题现象

由于Navigation导航页的功能限制，用导航页作为首页时，无法将首页推送入栈，只能通过清空路由栈的方式返回首页，在一些场景下不适用。所以开发时可能会选择首页不实现UI布局，采用子页代替首页的实现方式。参考代码如下：

1. 导航页空白布局。

   ```ts
   @Entry
   @Component
   struct NavigationExample {
     pageInfos: NavPathStack = new NavPathStack();

     aboutToAppear() {
       this.pageInfos.pushPath({ name: 'pageOne' }); // 推送第一个子页作为首页
     }

     build() {
       Navigation(this.pageInfos) {
       }
       .backgroundColor(Color.Gray); // 为了使动画异常更明显设置对比色
     }
   }
   ```
2. 第一个子页代替导航页成为首页。

   ```ts
   @Builder
   export function PageOneBuilder(name: string, param: Object) {
     PageOne();
   }

   @Component
   export struct PageOne {
     pageInfos: NavPathStack = new NavPathStack();
     @State getAllPathName: string[] = [];

     build() {
       NavDestination() {
         Column() {
           Button('我为首页', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20);
         }
         .width('100%')
         .height('100%');
       }
       .title('pageOne')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       });
     }
   }
   ```

上述实现方式，在打开应用时导航页总是会显示一瞬间，如何实现子页代替导航页成为首页的功能，并避免这种跳转异常？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Zm33v_uBSZukqx7M5VOXYA/zh-cn_image_0000002658832835.gif "点击放大")

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)是路由导航组件，可以采用[pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)、[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)等方式进行路由跳转。这些跳转方式默认集成了动画的功能，同时也可以通过设置关闭跳转时的动画功能。

## 问题定位

导航页跳转子页操作是在[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)内执行，程序首先加载导航页，且跳转默认具有动画效果，所以有空白主页左移和子页出现的过程。

## 分析结论

未关闭跳转的动画效果，所以在UI显示上有导航页显示的情况。

## 修改建议

* **方案一**：采用[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)隐藏导航页。

  隐藏导航页时会取消动画，主页代码修改如下，PageOne页面代码同问题现象的子页。

  ```ts
  @Entry
  @Component
  struct HideNavBarPage {
    pageInfos: NavPathStack = new NavPathStack();

    aboutToAppear() {
      this.pageInfos.pushPath({ name: 'pageOne' }); // 推送第一个子页作为首页
    }

    build() {
      Navigation(this.pageInfos) {
      }
      .backgroundColor(Color.Gray)
      .hideNavBar(true); // 隐藏导航页
    }
  }
  ```
* **方案二**：修改pushPath等入栈方法属性。
  1. pushPath入参animated参数默认为true支持动画，可以设置为false。
  2. pushPath入参[NavPathInfo](../harmonyos-references/ts-basic-components-navigation.md#navpathinfo10)可以设置isEntry属性，该参数表示是否作为首页推送子页，当该参数设置为true时，从该页面按返回键会自动返回桌面。

  修改方式如下：

  1. 把子页作为主页推送。

     ```ts
     @Entry
     @Component
     struct NavigationExample {
       pageInfos: NavPathStack = new NavPathStack();

       aboutToAppear() {
         this.pageInfos.pushPath({ name: 'pageOne', isEntry: true }, false); // 作为入口页面推送，并关闭动画
       }

       build() {
         Navigation(this.pageInfos) {
         }
         .backgroundColor(Color.Gray);
       }
     }
     ```
  2. 子页重写返回逻辑。若不重写返回，在未结束app进程的前提下，isEntry参数只能支持一次返回桌面的逻辑。

     ```ts
     .onBackPressed(() => {
       try {
         // 获取Context
         let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
         // 通过Context获取windowStage
         let windowStage = context.windowStage;
         // 通过windowStage获取主窗口
         let mainWindow = windowStage.getMainWindowSync();
         // 将主窗口最小化
         mainWindow.minimize();
       } catch (exception) {
         console.error(`onBackPress failed. Cause code: ${exception.code}, message: ${exception.message}`);
       }
       return true;
     });
     ```

**说明** 

请参考[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)的配置方法，两种方案运行还需在模块的module.json5文件中添加路由表配置"routerMap": "$profile:route\_map"，并在工程resources/base/profile中创建route\_map.json文件。添加如下配置信息：

```json
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/pageOne.ets",
      "buildFunction": "PageOneBuilder"
    }
  ]
}
```

上述两种方案，不可使用[clear](../harmonyos-references/ts-basic-components-navigation.md#clear10)方式清空路由栈，即使清空后也必须立即推送主页。
