---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-125
title: Web组件调用WebviewController相关接口报17100001错误
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件调用WebviewController相关接口报17100001错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:274b48033650f00db1532da08bf0c71be4cb23376ece00ca0b46980bf238e64c
---

## 问题现象

当调用WebviewController相关接口（如加载H5页面、执行JS脚本）时，系统抛出错误码17100001，提示“Init error. The WebviewController must be associated with a Web component.”。

* **场景一**：WebviewController相关接口调用时机过早。

  问题代码示例参考如下：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Index {
    controller: webview.WebviewController = new webview.WebviewController();
    @State webResult: string = '';

    onPageShow(): void {
      this.controller.loadUrl($rawfile('index.html'));
      this.controller.runJavaScript(
        'test()', 
        (error, result) => { 
          if (error) {
            console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            return;
          }
          if (result) {
            this.webResult = result;
            console.info(`The test() return value is: ${result}`);
          }
        });
    }

    build() {
      Column() {
        Web({ src: '', controller: this.controller });
      };
    }
  }
  ```
* **场景二**：WebviewController相关接口调用时机过晚。

## 背景知识

[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)可以控制Web组件各种行为。一个WebviewController对象只能控制一个Web组件，且必须在Web组件和WebviewController绑定后，以及在Web组件销毁前，才能调用WebviewController上的方法（静态方法除外）。

## 问题定位

* **场景一**：

  调用时机过早，WebviewController没有和具体的Web组件关联，可以通过onControllerAttached()接口进行检查，onControllerAttached()接口调用说明WebviewController和Web组件绑定成功，在这之后能避免调用过早。
* **场景二**：

  Web组件析构销毁后，对应的WebviewController也处于解绑状态，此时调用相关接口也会抛出异常。只要Web组件（[离线Web](../harmonyos-guides/web-offline-mode.md)除外）从当前UI树中被移除（如页面退出、条件渲染失效或父组件销毁等），该组件就会被销毁。应用开发者可以在Web所在的自定义组件中的[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)方法中加日志，确保controller调用在该日志之前。

## 分析结论

* **场景一**：

  WebviewController在没有和具体的Web组件绑定的情况下调用了[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)、[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)等非静态方法，导致系统抛出错误码17100001。
* **场景二**：

  与WebviewController绑定的Web组件销毁后，调用了WebviewController的非静态方法，导致系统抛出错误码17100001。

## 修改建议

* **场景一**：
  + 使用loadUrl加载指定的Url，可以在onControllerAttached()回调里调用，因为WebviewController成功绑定到Web组件时触发onControllerAttached回调。
  + 使用runJavaScript执行JavaScript脚本，为了避免页面生命周期[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)回调函数中无法确认WebviewController与Web组件绑定时序关系，需要在loadUrl完成后执行。建议在Web组件[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)回调函数中（此时WebviewController已绑定）调用WebviewController.runJavaScript()。

  Index.ets：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Index {
    webviewController: webview.WebviewController = new webview.WebviewController();
    @State webResult: string = '';

    build() {
      Column() {
        Text(this.webResult).fontSize(20);
        Web({ src: '', controller: this.webviewController })
          .onControllerAttached(() => {
            this.webviewController.loadUrl($rawfile('index.html'));
          })
          .geolocationAccess(false)
          .fileAccess(false)
          .javaScriptAccess(true)
          .onPageEnd((event) => {
            if (event) {
              console.info(`url:`, event.url);
            }
            try {
              this.webviewController.runJavaScript(
                'test()',
                (error, result) => {
                  if (error) {
                    console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                    return;
                  }
                  if (result) {
                    this.webResult = result;
                    console.info(`The test() return value is: ${result}`);
                  }
                });
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
      };
    }
  }
  ```

  index.html：

  ```html
  <!DOCTYPE html>
  <html>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <body>
  Hello world!
  </body>
  <script type="text/javascript">
      function test() {
          console.info('Ark WebComponent');
          return "This value is from index.html";
      }
  </script>
  </html>
  ```
* **场景二**：

  使用WebviewController相关接口前调用[getAttachState](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getattachstate20)查询当前controller是否是绑定状态，只有在绑定状态下才能调用相关方法（静态方法除外）。

## 常见FAQ

Q：Web组件绑定WebviewController之后，能复用WebviewController吗？

A：不能，一个WebController对象只能控制一个Web组件。

Q：Web组件和WebviewController绑定后，支持解绑和更换WebviewController吗？

A：不支持。
