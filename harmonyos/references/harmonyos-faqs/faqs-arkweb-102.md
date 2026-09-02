---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-102
title: 应用内弹窗无法通过侧滑关闭
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 应用内弹窗无法通过侧滑关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:12b64d47d5896b988b0d22e1eb84398b45665a36ba546b006844161163fbf886
---

## 问题现象

侧滑操作退出了应用，而不是关闭提示窗口。

## 背景知识

* [onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)：基于Navigation自定义弹窗实现，使用NavDestination的回调函数onBackPressed，当onBackPressed返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。
* [Class (WebviewController)](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)：通过WebviewController可以控制Web组件各种行为（包括页面导航、生命周期状态、JavaScript交互等行为）。
* [runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript-1)：在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过Promise方式返回。

## 问题定位

1. 从ArkUI Inspector页面发现这是一个Web页面。
2. 通过DevTools检查页面结构发现，弹窗由div元素实现，且与Web页面同级。因此侧滑操作会触发整个Web页面的返回事件，而Web页面位于应用首页，导致直接触发应用退出。

## 分析结论

弹窗与Web页面同层，导致侧滑返回时被识别为“返回上一级”，又因为当前已是首页，最终导致退出应用。

## 修改建议

在Web页面中定义关闭弹窗的JavaScript函数，并在onBackPress中通过WebViewController.runJavaScript调用该函数，优先尝试关闭弹窗；若弹窗未打开或已关闭，则执行默认返回逻辑（如终止应用）。

```ts
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State private webViewController: webview.WebviewController = new webview.WebviewController();

  onBackPress() {
    let url: string = this.webViewController.getUrl()
    if (url === 'resource://rawfile/H5/index3.html') {
      this.webViewController.runJavaScript('closeDialog()').then((result) => {
        if (result === '"close dialog success"') {
          console.info('关闭弹窗成功');
        }else {
          console.info('关闭网页成功');
          // 若需要返回上一页，可使用this.webViewController.backward()
          let context = getContext(this) as common.UIAbilityContext;
          context.terminateSelf();
        }
      })
      return true;
    }
    return false;
  }

  build() {
    Column() {
      Web({
        src: $rawfile('H5/index3.html'),
        controller: this.webViewController
      })
        .javaScriptAccess(true)
        .width('80%')
        .height('50%')
        .backgroundColor('#CCF4F5')
        .domStorageAccess(true)
    }
    .backgroundColor('#CCF4F5')
    .justifyContent(FlexAlign.Center)
    .width('100%').height('100%')
  }
}
```

```html
<!DOCTYPE html>
<html style="font-size: 115.625px;">
<head>
    <link rel="stylesheet" type="text/css" href="./css/index.css">
    <meta charset="UTF-8">
    <title>Web页面1</title>
</head>
<body>
    <div id="dialog" style="width:800px;height:300px;border:1px solid black;display: flex;justify-content: center;align-items: center;"><p id="paragraph">这是一个弹窗</p></div>
    <button style="width: 600px; height: 70px;font-size: 50px;" onclick="closeDialog()">点击关闭弹窗</button>
</body>
<script>
    function closeDialog() {
        var element = document.getElementById("dialog");
        if(element.style.display != "none"){
            element.style.display = "none";
            return 'close dialog success'
        }
    }
</script>
</html>
```
