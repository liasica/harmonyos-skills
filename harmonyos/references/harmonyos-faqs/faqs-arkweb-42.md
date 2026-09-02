---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-42
title: Web加载的H5页面跳转后，如何避免原有页面注册的资源被清空
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web加载的H5页面跳转后，如何避免原有页面注册的资源被清空
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6520fc71aa5a8ae2f3ef20d349718079b14a010c4d85c2622e372e88923607d0
---

使用[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)加载JS，是运行时注入，页面跳转后失效，可能会出现跳转后注册资源被清空的情况，使用[javaScriptOnDocumentStart](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptondocumentstart11)注入JS是文档初始化时注入，适用于页面跳转场景，就不会出现H5跳转注册资源被清空的情况。

使用runJavaScript复现问题代码参考：

ArkTS页面：

两个Button使用runJavaScript注册并调用test()方法和bodyOnLoadLocalStorage()，两个方法分别实现了为sessionStorage设置值和根据sessionStorage刷新H5页面。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column({ space: 20 }) {
      Button('调用注册资源')
        .onClick(e => {
          try {
            this.controller.runJavaScript(
              'test()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${error.code},  Message: ${error.message}`);
                  return;
                }
                if (result) {
                  console.info(`The test() return value is: ${result}`);
                }
              });
          } catch (error) {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          }
        })
      Button('调用注册资源')
        .onClick(e => {
          try {
            this.controller.runJavaScript(
              'bodyOnLoadLocalStorage()',
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${error.code},  Message: ${error.message}`);
                  return;
                }
                if (result) {
                  console.info(`The bodyOnLoadLocalStorage() return value is: ${result}`);
                }
              });
          } catch (error) {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .width('100%')
        .height('100%')
    }
  }
}
```

H5侧：

页面一：

index.html声明了test方法和bodyOnLoadLocalStorage方法。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
页面一：Hello world!
<div id="result"></div>
<a href="Second.html">点击跳转</a>
</body>
<script type="text/javascript">
    function bodyOnLoadLocalStorage() {
      if (typeof(Storage) !== 'undefined') {
        document.getElementById('result').innerHTML = sessionStorage.getItem('color');
      } else {
        document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
      }
    }
    function test(){
      if (typeof(Storage) !== 'undefined') {
        sessionStorage.setItem('color', 'Red');
      }
    }
</script>
</html>
```

页面二：

页面二未声明上述两个方法，利用之前的注册调用后，跳转至页面二时无法正确调用，注册资源清空的问题复现。

```html
<!-- Second.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
页面二：Hello world!
<div id="result"></div>
</body>
<script type="text/javascript">

</script>
</html>
```

使用javaScriptOnDocumentStart解决问题代码参考：

ArkUI侧

使用javaScriptOnDocumentStart执行test方法。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private localStorage: string =
    "if (typeof(Storage) !== 'undefined') {" +
      "   sessionStorage.setItem('color', 'Red');" +
      "}";
  @State scripts: Array<ScriptItem> = [
    { script: this.localStorage, scriptRules: ["*"] }
  ];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .javaScriptOnDocumentStart(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}
```

H5侧：

页面一：

页面调用bodyOnLoadLocalStorage刷新H5页面。

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
页面一：Hello world!
<div id="result"></div>
<a href="Second.html">点击跳转</a>
</body>
<script type="text/javascript">
    function bodyOnLoadLocalStorage() {
      if (typeof(Storage) !== 'undefined') {
        document.getElementById('result').innerHTML = sessionStorage.getItem('color');
      } else {
        document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
      }
    }
</script>
</html>
```

页面二：

点击跳转后，test方法会调用并生效。

```html
<!-- Second.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;" onload='bodyOnLoadLocalStorage()'>
页面二：Hello world!
<div id="result"></div>
</body>
<script type="text/javascript">
    function bodyOnLoadLocalStorage() {
      if (typeof(Storage) !== 'undefined') {
        document.getElementById('result').innerHTML = sessionStorage.getItem('color');
      } else {
        document.getElementById('result').innerHTML = 'Your browser does not support sessionStorage.';
      }
    }
</script>
</html>
```
