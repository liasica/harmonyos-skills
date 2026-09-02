---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-127
title: Web场景下主动拉起软键盘
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web场景下主动拉起软键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d56b40b34653af37e46d7d01760983a10baebf7aab11e549835d1fe9316919a
---

## 问题现象

Web组件加载H5页面，H5页面中有input输入框，如何实现刚进入H5页面就直接拉起软键盘？

## 背景知识

* [onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)：网页加载完成时触发该回调，且只在主frame触发，iframe或者frameset的内容加载时不会触发此回调。
* [@ohos.inputMethod (输入法框架)](../harmonyos-references/js-apis-inputmethod.md)：本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等等。

## 解决方案

H5页面有输入框时，可以在Web的onPageEnd回调中使用@ohos.inputMethod (输入法框架)框架的[showTextInput](../harmonyos-references/js-apis-inputmethod.md#showtextinput10)方法实现页面加载时主动使输入框获焦并拉起键盘，inputMethod.TextConfig可以设置键盘的编辑框样式，attach方法将自绘控件与输入法绑定。

端侧示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';
import { inputMethod } from '@kit.IMEKit';
import { BusinessError } from '@kit.BasicServicesKit';

let inputMethodController = inputMethod.getController();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Scroll() {
      Column() {
        Web({
          src: $rawfile('keyBoardDemo.html'),
          controller: this.controller,
        })
          .onPageEnd(() => {
            try {
              let textConfig: inputMethod.TextConfig = {
                inputAttribute: {
                  textInputType: 0,
                  enterKeyType: 1
                }
              };
              inputMethodController.attach(true, textConfig, (err: BusinessError) => {
                if (err) {
                  console.error(`Failed to attach: ${err.code} ${err.message}`);
                  return;
                }
                console.info('Succeeded in attaching the inputMethod.');
              });
            } catch (err) {
              console.error(`Failed to attach: ${err.code} ${err.message}`);
            }
            inputMethodController.showTextInput().then(() => {
              console.info('Succeeded in showing text input.');
            }).catch((err: BusinessError) => {
              console.error(`Failed to showTextInput: ${err.code} ${err.message}}`);
            });
          })
          .fileAccess(false)
          .geolocationAccess(false)
          .domStorageAccess(true)
          .height('100%');
      };
    };
  }
}
```

HTML示例代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>Document</title>
</head>
<body>
<h1>H5侧</h1>
<div>
    <input id="myInput" type="text" value="" style="margin:10px 0" onload/><br/>
</div>
</body>
<script>
    function test() {
       document.getElementById("myInput").focus();
    }
    // 加载时立即执行此函数
    document.addEventListener('DOMContentLoaded', test);
</script>
</html>
<style>
    body {
        width:100%;
        height:auto;
        margin:50px auto;
        text-align:center;
    }
</style>
```

## 常见FAQ

Q：滚动时如何收起键盘？

A：滚动时键盘不消失是系统的默认逻辑，可以通过Web组件的[onScroll](../harmonyos-references/arkts-basic-components-web-events.md#onscroll9)回调中使用[stopInputSession](../harmonyos-references/js-apis-inputmethod.md#stopinputsession9)收起键盘。
