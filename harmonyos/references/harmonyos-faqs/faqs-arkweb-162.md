---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-162
title: Web组件拦截请求跳转指定页面后再返回时白屏
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件拦截请求跳转指定页面后再返回时白屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:182bbbc4f1dbf0f7c2f5e2c19cb40913ab234a502021633f322bbad6aa950962
---

## 问题现象

通过onLoadIntercept拦截请求，识别自定义协议链接并跳转其它页面，从其它页面返回到Web页，Web页面是白屏。

```ts
import { webview } from '@kit.ArkWeb';
import { TargetPage } from './TargetPage';

@Entry
@Component
struct Index {
  private webController: webview.WebviewController = new webview.WebviewController();
  private webUrl: ResourceStr = $rawfile('index.html');
  @Provide('pageStack') pageStack: NavPathStack = new NavPathStack();

  @Builder
  pageMap(name: string) {
    if (name === 'TargetPage') {
      TargetPage();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Web({
          controller: this.webController,
          src: this.webUrl
        })
          .onLoadIntercept((event) => {
            if (!event) {
              return false;
            }
            const url = event.data.getRequestUrl();
            // 自定义协议跳转HarmonyOS页面
            if (url.startsWith('detail:xxxx')) {
              this.pageStack.pushPathByName('TargetPage', null);
            }
            return false;
          })
          .fileAccess(false)
          .geolocationAccess(false)
      }
    }.navDestination(this.pageMap)
    // 隐藏标题栏
    .hideTitleBar(true);
  }
}
```

## 背景知识

[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。默认允许加载。

## 问题定位

1. onLoadIntercept回调接收一个布尔类型的返回值，当返回值为true时表示阻止此次访问，当返回值为false或undefined时表示允许此次访问。
2. 分析问题代码，发现在onLoadIntercept回调中判断了当前链接为自定义链接后，执行了页面跳转，但是回调函数中的代码并没有中止执行，而是跳出if判断继续执行了下面的“return false”语句，导致Web侧继续加载自定义协议链接，而该链接指向的网页是不存在的因此会显示白屏。

## 分析结论

onLoadIntercept回调中未阻止自定义类型url访问，导致Web访问了不存在的url而显示白屏。

## 修改建议

在Web组件的onLoadIntercept回调中拦截url并执行相应行为后，如果不需要加载该url应立即return true阻止该url访问。

```ts
import { webview } from '@kit.ArkWeb';
import { TargetPage } from './TargetPage';

@Entry
@Component
struct Index {
  @Provide('pageStack') pageStack: NavPathStack = new NavPathStack();
  private webController: webview.WebviewController = new webview.WebviewController();
  private webUrl: ResourceStr = $rawfile('index.html');

  @Builder
  pageMap(name: string) {
    if (name === 'TargetPage') {
      TargetPage();
    }
  }

  build() {
    Navigation(this.pageStack) {
      Column() {
        Web({
          controller: this.webController,
          src: this.webUrl
        })
          .onLoadIntercept((event) => {
            if (!event) {
              return false;
            }
            const url = event.data.getRequestUrl();
            // 自定义协议跳转HarmonyOS页面
            if (url.startsWith('detail:xxxx')) {
              this.pageStack.pushPathByName('TargetPage', null); // 跳转目标页面
              return true;
            }
            return false;
          })
          .fileAccess(false)
          .geolocationAccess(false);
      };
    }.navDestination(this.pageMap)
    // 隐藏标题栏
    .hideTitleBar(true);
  }
}
```

HTML页面如下：

```html
<!-- 文件路径：src/main/resources/rawfile/index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HarmonyOS Web Demo</title>
    <style>
        a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007dff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
        a:active {
            background-color: #005bb5;
        }
    </style>
</head>
<body>
<h1>Web组件示例</h1>
<p>点击下方链接触发路由跳转：</p>
<!-- 自定义协议跳转链接 -->
<a href="detail:xxxx">点击跳转HarmonyOS原生页面</a>
</body>
</html>
```

跳转页面TargetPage（用于验证跳转后的返回功能）如下：

```ts
// 跳转的目标页面
@Component
export struct TargetPage {
  build() {
    NavDestination() {
      Column() {
        Text('TargetPage');
      };
    };
  }
}
```
