---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-166
title: Navigation组件管理两个界面都加载本地H5进行交互跳转，如何进行页面刷新
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Navigation组件管理两个界面都加载本地H5进行交互跳转，如何进行页面刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e04161d4b4a56418243810caf362c664242498e5d51df0306067629429ca43ad
---

## 问题现象

由Navigation管理的两个界面都加载本地H5，Web首页面跳转到Web第二个页面后，如何进行页面刷新？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IMGyyJk2QniJm6D5ctT3WA/zh-cn_image_0000002629059088.png "点击放大")

## 背景知识

* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。
* [onWillShow](../harmonyos-references/ts-basic-components-navdestination.md#onwillshow12)：当该NavDestination显示之前触发此回调。

## 解决方案

点击Web页面的按钮跳转Navigation页面需要在Web组件的onLoadIntercept拦截页面加载，再使用Navigation提供的组件路由能力跳转页面，然后通过onWillShow方法中进行刷新，这样每一次进入或返回都可以重新刷新界面。

具体实现如下：

* 主界面，用于创建Navigation。

  ```ts
  import { WebOnePage } from './WebOnePage';
  import { WebTwoPage } from './WebTwoPage';

  @Entry
  @Component
  struct Index {
    @Provide navPathStack: NavPathStack = new NavPathStack();

    @Builder
    PageMap(name: string) {
      if (name === 'WebOnePage') {
        WebOnePage();
      } else if (name === 'WebTwoPage') {
        WebTwoPage();
      }
    }

    build() {
      Navigation(this.navPathStack) {
        Column() {
          Text('跳转')
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
            .padding({ top: 200 })
            .onClick(() => {
              this.navPathStack.pushPath({ name: 'WebOnePage' });
            });
        }
        .height('100%')
        .width('100%');
      }
      .hideTitleBar(true)
      .navDestination(this.PageMap);
    }
  }
  ```
* 第二个界面，创建Web组件，并加载本地index.html，通过Web组件中的onLoadIntercept方法拦截后调用Navigation组件的push方法跳转到下一个页面，并在该界面中的onWillShow方法内进行监听，每次触发该方法调用下拉刷新逻辑。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Component
  export struct WebOnePage {
    private controller: WebviewController = new webview.WebviewController();
    @Consume('navPathStack') navPathStack: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Web({
            src: $rawfile('index.html'),
            controller: this.controller
          })
            .zoomAccess(false)
            .onLoadIntercept((event) => {
              if (event.data.getRequestUrl() === 'arkts:/pages/toWebTwoPage') {
                this.navPathStack.pushPath({ name: 'WebTwoPage' });
                return true;
              }
              return false;

            });
        };
      }
      .title('返回上一界面')
      .onWillShow(() => {
        this.getUIContext().getPromptAction().showToast({
          message: '下拉刷新'
        });
      });
    }
  }
  ```

  index.html：

  ```html
  <!DOCTYPE html>
  <head>
      <meta charset="UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Document</title>
      <link rel="stylesheet" href="./css/styles.css">
  </head>

  <body>
  <div class="web_page_demo">
      <div class="title">Web首界面</div>
      <ul>
          <li>
              <a class="function_item" href="arkts:/pages/toWebTwoPage">跳转到第二个页面</a>
          </li>
      </ul>
  </div>
  </body>
  <script></script>
  ```
* 第三个界面，创建Web组件，并加载本地index1.html，通过Web组件中的onLoadIntercept回调拦截后调用Navigation组件的pop方法返回上一个界面。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Component
  export struct WebTwoPage {
    private controller: WebviewController = new webview.WebviewController();
    @Consume('navPathStack') navPathStack: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Web({
            src: $rawfile('index1.html'),
            controller: this.controller
          })
            .zoomAccess(false)
            .onLoadIntercept((event) => {
              if (event.data.getRequestUrl() === 'arkts:/pages/toBackWebOnePage') {
                this.navPathStack.pop();
                return true;
              }
              return false;
            });
        };
      }
      .title('返回上一界面');
    }
  }
  ```

  index1.html：

  ```html
  <!DOCTYPE html>
  <head>
      <meta charset="UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>Document</title>
      <link rel="stylesheet" href="./css/styles.css">
  </head>

  <body>
  <div class="web_page_demo">
      <div class="title">第二个Web界面</div>
      <ul>
          <li>
              <a class="function_item" href="arkts:/pages/toBackWebOnePage">返回上一个Web界面</a>
          </li>
      </ul>
  </div>
  </body>
  <script></script>
  ```
