---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-getpage-height
title: 获取网页内容高度
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > Web渲染和布局 > 获取网页内容高度
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:23+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:da02ed9c34aef7b5443ed6b44ce280f48f266d395097ff89d99110a8dc02fc67
---

通过调用[getPageHeight](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getpageheight)可获取当前网页内容的实际高度，开发者可以根据具体需求选择合适的方法。

## 使用场景

在网页加载过程中，获取的高度可能不够精确，特别是在网页还未渲染完成时。因为动态内容加载后会更新这个值。网页内容可能需要长时间加载。目前网站为优化首次加载速度，会使用动态网页加载技术，用户在看到网页首帧时，页面资源还在动态加载页面，特别是包含图片、动态内容的页面。

非静态网页不建议在[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)、[onPageVisible](../harmonyos-references/arkts-basic-components-web-events.md#onpagevisible9)、[onFirstContentfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstcontentfulpaint10)、[onFirstMeaningfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstmeaningfulpaint12)事件等Web组件生命周期回调和Web性能指标回调中获取网页内容高度。需要根据当前网页的特点，通过JSBridge或延迟等方案，在前端特定的回调通知里获取当前网页内容的实际高度。

## 普通静态展示页面

普通静态网页，可以在onPageEnd等Web组件生命周期回调和Web性能指标回调中通过getPageHeight获取网页内容的高度。

应用侧代码

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .onPageEnd(() => {
            console.info("page height: onPageEnd: " + this.controller.getPageHeight());
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

## 复杂动态网页使用JSBridge传递特定回调

动态网页可以通过JSBridge传递特定回调，通知到应用侧调用。

应用侧代码

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

class TestClass {
  testController: webview.WebviewController;

  constructor(controller: webview.WebviewController) {
    this.testController = controller;
  }

  notifyToGet(): void {
    console.info("page height: " + this.testController.getPageHeight());
  }
}

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State jsbObj: TestClass = new TestClass(this.controller);

  build() {
    Row() {
      Column() {
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .javaScriptAccess(true)
          .javaScriptProxy({
            object: this.jsbObj,
            name: "jsbObj",
            methodList: ["notifyToGet"],
            controller: this.controller
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

### 加载普通网页

普通网页可以通过load事件，在网页的所有资源都完全加载完成后触发。

前端代码

```html
<!--index.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    window.addEventListener("load", function() {
        if (typeof jsbObj !== 'undefined') {
            jsbObj.notifyToGet();
        } else {
            console.info("jsbObj is undefined");
        }
    })
</script>
</body>
</html>
```

### 加载大图片的网页

当网页含有大图片时，可使用图片加载完成回调触发。

在前端代码中，请将示例图片路径替换为实际使用的图片资源。

```html
<!--index.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="example.jpg" id="largeImage" alt="Large Image">
<script>
    var img = document.getElementById('largeImage');

    img.addEventListener('load', function() {
        if (typeof jsbObj !== 'undefined') {
            jsbObj.notifyToGet();
        } else {
            console.info("jsbObj is error");
        }
    });
</script>
</body>
</html>
```

### 加载大量图片的网页

针对图片密集网页，在所有图片加载完成后触发。

在前端代码中，请替换图片为真实图片。

```html
<!--index.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <img src="example1.jpg" >
    <img src="example2.jpg" >
<script>
    function waitForImages() {
        const images = Array.from(document.images);
        const promises = images.map(img => {
            if (img.complete) return Promise.resolve();
            return new Promise(resolve => {
                img.onload = img.onerror = resolve;
            });
        });

        return Promise.all(promises).then(() => {
            if (typeof jsbObj !== 'undefined') {
                jsbObj.notifyToGet();
            } else {
                console.info("jsbObj is error");
            }
        })
    }
    document.addEventListener("DOMContentLoaded", waitForImages);
</script>
</body>
</html>
```

## 无法使用JSBridge场景

在无法使用JSBridge的场景下，可以通过添加setTimeout等函数来延迟获取当前页面的高度。具体的延迟时间可以根据网页的复杂度来确定。

应用侧代码

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Row() {
      Column() {
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .onPageEnd(() => {
            setTimeout(()=>{
                console.info("page height: onPageEnd: setTimeout: " + this.controller.getPageHeight());
            },2000)
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```
