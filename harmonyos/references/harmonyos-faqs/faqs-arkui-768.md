---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-768
title: 如何实现Web组件在Navigation页面中返回上一页
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Web组件在Navigation页面中返回上一页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b827280b2b1ec00703f2bea64d12adadec5d46e7d7a78f9374f29fbbd19bdb8
---

## 问题现象

在Navigation导航的页面中使用Web组件加载H5页面时，如何实现以下功能：

1. Web组件和Navigation导航共用一个返回按钮。
2. 侧边返回H5页面的上一页。

## 背景知识

在HarmonyOS中，通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)对象控制Web组件，实现返回H5页面中上一页的功能，通常需要对返回操作进行拦截后自定义内容，以下是可能会涉及到的组件属性：

* [accessBackward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessbackward)：判断当前页面是否可后退，即当前页面是否有返回历史记录。
* [backward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#backward)：按照Web历史栈，后退一个页面。
* [onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)：Navigation默认提供的返回按钮，返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。
* [pop](../harmonyos-references/ts-basic-components-navigation.md#pop11)：弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

使用Navigation实现页面跳转，需要在module.json5[配置文件标签](../harmonyos-guides/module-configuration-file.md#配置文件标签)中添加routerMap配置，同时需要在resources/base/profile下添加[routerMap标签](../harmonyos-guides/module-configuration-file.md#routermap标签)配置文件。

## 解决方案

在默认的返回按钮accessBackward中添加Web组件的onBackPressed判断，即判断当前Web页面内容是否可后退。如果可以后退，则调用Web的backward()返回上一个Web页面内容；如果不可后退，则调用Navigation的pop()返回Navigation的上一个页面。请参考[开发准备](../harmonyos-guides/graphics-accelerate-assetdownload-prepare.md)配置网络权限。

首页：

```ts
@Entry
@Component
struct NavigationExample {
  pageInfos: NavPathStack = new NavPathStack();
  isUseInterception: boolean = false;

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfos.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
          });
      };
    }
    .title('Home');
  }
}
```

PageOne页面：

```ts
import { webview } from '@kit.ArkWeb';

@Builder
export function PageOneBuilder() {
  PageOne();
}

@Component
export struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    NavDestination() {
      Column() {
        // 'www.xxx.com'更换为目标网址
        Web({ src: 'www.xxx.com', controller: this.controller });
      }
      .width('100%')
      .height('100%');
    }
    .title('pageOne')
    .onBackPressed(() => {
      if (this.controller.accessBackward()) { // 判断web页面是否可以后退
        this.controller.backward(); // web页面后退
        return true;
      } else {
        this.pageInfos.pop();
        return true;
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    });
  }
}
```

router\_map.json文件配置如下：

```json
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder",
      "data": {}
    }
  ]
}
```

## 常见FAQ

Q：弹窗如何拦截侧边返回？

A：通过配置[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的onWillDismiss参数进行拦截。
