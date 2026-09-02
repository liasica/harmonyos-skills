---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1304
title: 如何同时打开多个自定义弹窗并设置层级关系
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何同时打开多个自定义弹窗并设置层级关系
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:52ab908f00c748ff0d2b9e81bd102e034fc73f52e6c56e0d260b158d4c7e492d
---

## 问题现象

目前多种弹窗的实现方式中，使用什么方式能同时打开多个自定义弹窗，并能够设置其层级关系？

## 背景知识

* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)是Navigation组件路由中Navigation的子页面，会存在于Navigation路由栈中。
* NavDestination设置mode为[NavDestinationMode.DIALOG](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)弹窗类型，此时整个NavDestination默认透明显示。
* API18后，可以使用属性[LevelOrder](../harmonyos-references/js-apis-promptaction.md#levelorder18)控制弹窗层级，目前支持的弹窗有openCustomDialog、CustomDialog、AlertDialog、ActionSheet、showDialog。
* API18之前，绑定bindsheet会遮挡其他弹窗层级问题，可以bindsheet嵌套bindsheet。

## 解决方案

* **方案一**：使用NavDestinationMode.DIALOG通过路由栈控制弹窗层级。

  NavDestinationMode.DIALOG是一个弹窗模式的NavDestination页面，每次push一个Dialog页面，它就会出现在当前弹窗之上，形成层级结构。它们的层级顺序即为路由栈中的顺序。

  Navigation页面：

  ```ts
  @Entry
  @Component
  struct NavDialog {
    @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

    @Builder
    PagesMap(name: string) {
      if (name === 'DialogPage1') {
        DialogPage1();
      } else if (name === 'DialogPage2') {
        DialogPage2();
      } else if (name === 'DialogPage3') {
        DialogPage3();
      }
    }

    build() {
      Navigation(this.pageStack) {
        Button('依次打开弹窗1，2，3')
          .margin(20)
          .width('80%')
          .onClick(() => {
            this.pageStack.pushPathByName('DialogPage1', '');
            this.pageStack.pushPathByName('DialogPage2', '');
            this.pageStack.pushPathByName('DialogPage3', '');
          });
        Button('依次打开弹窗1，2，3后依次关闭弹窗3，2，1')
          .margin(20)
          .width('80%')
          .onClick(() => {
            this.pageStack.pushPathByName('DialogPage1', '');
            this.pageStack.pushPathByName('DialogPage2', '');
            this.pageStack.pushPathByName('DialogPage3', '');
            setTimeout(() => {
              this.pageStack.removeByName('DialogPage3');
            }, 1000);
            setTimeout(() => {
              this.pageStack.removeByName('DialogPage2');
            }, 2000);
            setTimeout(() => {
              this.pageStack.removeByName('DialogPage1');
            }, 3000);
          });
      }
      .mode(NavigationMode.Stack)
      .title('Main')
      .navDestination(this.PagesMap);
    }
  }

  @Component
  export struct DialogPage1 {
    @Consume('NavPathStack') pageStack: NavPathStack;

    build() {
      NavDestination() {
        Stack({ alignContent: Alignment.Center }) {
          Column() {
            Text('Dialog NavDestination1')
              .fontSize(20)
              .margin({ bottom: 100 });
            Button('Close').onClick(() => {
              this.pageStack.pop();
            }).width('30%');
          }
          .justifyContent(FlexAlign.Center)
          .backgroundColor(Color.White)
          .borderRadius(10)
          .height('30%')
          .width('80%');
        }.height('100%').width('100%');
      }
      .backgroundColor('rgba(0,0,0,0.5)')
      .hideTitleBar(true)
      .mode(NavDestinationMode.DIALOG);
    }
  }

  @Component
  export struct DialogPage2 {
    @Consume('NavPathStack') pageStack: NavPathStack;

    build() {
      NavDestination() {
        Stack({ alignContent: Alignment.Center }) {
          Column() {
            Text('Dialog NavDestination2')
              .fontSize(20)
              .margin({ bottom: 100 });
            Button('Close').onClick(() => {
              this.pageStack.pop();
            }).width('30%');
          }
          .justifyContent(FlexAlign.Center)
          .backgroundColor(Color.White)
          .borderRadius(10)
          .height('30%')
          .width('80%');
        }.height('100%').width('100%');
      }
      .backgroundColor('rgba(0,0,0,0.5)')
      .hideTitleBar(true)
      .mode(NavDestinationMode.DIALOG);
    }
  }

  @Component
  export struct DialogPage3 {
    @Consume('NavPathStack') pageStack: NavPathStack;

    build() {
      NavDestination() {
        Stack({ alignContent: Alignment.Center }) {
          Column() {
            Text('Dialog NavDestination3')
              .fontSize(20)
              .margin({ bottom: 100 });
            Button('Close').onClick(() => {
              this.pageStack.pop();
            }).width('30%');
          }
          .justifyContent(FlexAlign.Center)
          .backgroundColor(Color.White)
          .borderRadius(10)
          .height('30%')
          .width('80%');
        }.height('100%').width('100%');
      }
      .backgroundColor('rgba(0,0,0,0.5)')
      .hideTitleBar(true)
      .mode(NavDestinationMode.DIALOG);
    }
  }
  ```
* **方案二**：使用LevelOrder属性控制弹窗层级，具体参考[完整示例](../harmonyos-guides/arkts-dialog-levelorder.md#完整示例)。但是LevelOrder属性不支持动态刷新弹出框的显示顺序。

## 常见FAQ

Q：NavDestinationMode.DIALOG模式下，如何在使用removeByIndexes移除页面时，移除对应页面打开的NavDestinationMode.DIALOG？

A：由于NavDestinationMode.DIALOG也是页面的形式入页面栈，所以在销毁对应的页面前，销毁其上一个页面即可实现。

Q：使用NavDestinationMode.DIALOG弹窗时，如何实现在页面打开的同时，打开其对应的弹窗？

A：在对应页面的AboutToAppear生命周期内推送NavDestinationMode.DIALOG页面入栈即可。

## 总结

弹窗不是普通组件，属于独立的一层，不能使用属性zIndex控制层级。使用NavDestinationMode.DIALOG自定义弹窗时，每个弹窗本质上都是一个NavDestination页面，它们在栈中的顺序即为弹窗的层级。LevelOrder是基础弹窗选项BaseDialogOptions中的参数，可用于控制弹窗层级，但不支持动态刷新层级。
