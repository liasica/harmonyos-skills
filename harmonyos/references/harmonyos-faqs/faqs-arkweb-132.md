---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-132
title: 如何解决Scroll组件嵌套Web组件后无法跟随页面整体滚动的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Scroll组件嵌套Web组件后无法跟随页面整体滚动的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cf98f54d208ad0fe7330aed3a5d8c984567d7b46bbf535ddd21c2cb3cb064fd
---

## 问题现象

在Scroll组件内嵌套使用Web组件和其他容器组件的组合时，嵌套布局如下：

```ts
Scroll() {
  Row() {}
  Web() {}
  Row() {}
  List() {}
}
```

Web组件显示不全或只能单独滚动，无法实现与Row、List等组件连为一个整体进行滚动。

## 背景知识

* [layoutMode](../harmonyos-references/arkts-basic-components-web-attributes.md#layoutmode11)：设置Web布局模式。当属性没有显式调用时，默认Web布局跟随系统模式。
* [RenderMode](../harmonyos-references/arkts-basic-components-web-e.md#rendermode12)：定义Web组件的渲染方式，默认为异步渲染模式。建议使用异步渲染模式，异步渲染模式有更好的性能和更低的功耗。

## 问题定位

从问题现象可以看出当前有两种状态：Web组件会单独滚动以及内容显示不全。

分析两种状态的原因：

1. Web组件单独滚动是因为固定了组件的高度，且该高度小于内容高度。
2. Web组件内容显示不全是因为在第1点的基础上禁止了Web的滚动。

## 分析结论

问题的关键在于如何控制Web组件的高度，让其可以适应内容高度，从而将Web变成一个完全展开的view。

## 解决方案

通过设置layoutMode属性为WebLayoutMode.FIT\_CONTENT让Web自适应内容高度。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebFit {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Scroll() {
      Column() {
        Row() {
          Text('测试顶部');
        }
        .width('100%')
        .height('30%')
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Gray);

        // 网页内容过宽或者过长时需要设置为RenderMode.SYNC_RENDER
        Web({ src: $rawfile('test.html'), controller: this.webviewController, renderMode: RenderMode.SYNC_RENDER })
          .width('100%')
          .height('100%')
          .metaViewport(true)
          .layoutMode(WebLayoutMode.FIT_CONTENT) // 设置Web组件高度进行自适应
          .overScrollMode(OverScrollMode.NEVER) // 关闭过界回弹效果
          .zoomAccess(false) // 关闭手势缩放
          .fileAccess(false)
          .geolocationAccess(false);
        Row() {
          Text('测试底部');
        }
        .width('100%')
        .height('30%')
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Gray);
      };
    };
  }
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
    <title>Fit-Content</title>
</head>
<body>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
    <p>这就是一个测试话题。</p>
</body>
</html>
```

## 总结

通过layoutMode属性使Web组件的大小根据页面内容自适应变化，当Web页面宽高超过7680px（物理像素），建议设置渲染模式为同步渲染：renderMode: RenderMode.SYNC\_RENDER。
