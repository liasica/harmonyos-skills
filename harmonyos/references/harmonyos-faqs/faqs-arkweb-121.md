---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-121
title: 点击H5页面中的按钮，未正常跳转其他页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 点击H5页面中的按钮，未正常跳转其他页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd206fe51bdec5b6f373169a54aa0428445eb68f876156922025805b623b6012
---

## 问题现象

应用中展示的H5页面具有一个“跳转其他页面”按钮，当点击该按钮期望跳转下一个页面，但没有成功跳转返回。

## 背景知识

[ArkWeb](../harmonyos-guides/web-component-overview.md)（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。

## 问题定位

分析Web异常日志，通过“Cannot read properties of ...”得知当前试图访问未定义对象，导致异常。

```txt
xxx.xxx.html:21 Uncaught TypeError: Cannot read properties of undefined (reading 'toMenu')
    at goJump (xxx.xxx.html:21:32)
    at HTMLButtonElement.onclick (xxx.xxx.html:1140:28)
goBack	@	xxx.xxx.html:21
onclick	@	xxx.xxx.html:1140
```

## 分析结论

当前Web页面“跳转其他页面”按钮绑定的goJump函数未正确定义，导致点击跳转异常。

## 修改建议

通过[javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)建立应用侧与Web侧的交互通道，将正确的点击跳转方法注册到Web页面中。

WebTest.ets示例代码如下：

```ts
import { Router } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestClass {
  private routerInstance: Router | undefined = undefined;

  constructor(context: UIContext) {
    this.routerInstance = context.getRouter();
  }

  goJump() {
    this.routerInstance?.pushUrl({
      url: 'pages/Index',
    }).catch((error: BusinessError) => {
      console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
    });
  }
}

@Entry
@Component
struct WebTest {
  webviewController: webview.WebviewController = new webview.WebviewController();
  // 声明需要注册的对象
  @State testObj: TestClass = new TestClass(this.getUIContext());

  build() {
    Column() {
      // Web组件加载本地routerPage.html页面
      Web({ src: $rawfile('routerPage.html'), controller: this.webviewController })
        // 将对象注入到Web端
        .javaScriptProxy({
          object: this.testObj,
          name: 'testObjName',
          methodList: ['goJump'],
          controller: this.webviewController,
        })
        .fileAccess(false)
        .geolocationAccess(false);
    };
  }
}
```

Index.ets示例代码如下：

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

routerPage.html示例代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover"/>
<body>
<p>
    这是一个网页
</p>
<button onclick="handleClick()">跳转其他页面</button>
</body>
</html>
<script>
    function handleClick() {
      // 调用ArkTS注册的方法
      if (window.testObjName && typeof window.testObjName.goJump === 'function') {
        window.testObjName.goJump();
      } else {
        console.error('未找到跳转方法');
      }
    }
</script>
```
