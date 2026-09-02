---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-173
title: Web组件加载网络链接失败后如何加载错误页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件加载网络链接失败后如何加载错误页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c5134729d4ec0acabbaa7ef2ba847d9eefb945ead6c35d8268b685bfbca05f1b
---

## 问题现象

如果网络或者在线链接有问题时，Web组件加载网络链接会失败，此时如何加载本地缺省页面（指定失败页面）并进行页面刷新？

* 场景一：使用ArkTS页面实现缺省页面。
* 场景二：使用html页面实现缺省页面。
* 场景三：使用html格式的文本数据实现缺省页面。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/5iM-PFp8Q-Gc-1sdujm9Ow/zh-cn_image_0000002659258391.png "点击放大")

## 背景知识

* [onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)：网页加载遇到错误或无网络的情况下触发该回调。主资源与子资源出错都会回调该接口，可以通过isMainFrame来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。错误码范围：[ArkWeb的网络协议栈错误列表](../harmonyos-references/arkts-apis-neterrorlist.md)。
* [javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)：将javaScriptProxy中的ArkTS对象注册到Web组件中。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
  + Hidden：隐藏，但参与布局进行占位。
  + Visible：显示。
  + None：隐藏，但不参与布局，不进行占位。
* [loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)：加载指定的URL。
* [loadData](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loaddata)：加载指定的数据。
* [onOverrideErrorPage](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideerrorpage20)：网页加载遇到错误时触发，只有主资源出错才会回调该接口，可以使用该接口自定义错误展示页。该功能需通过调用[setErrorPageEnabled](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#seterrorpageenabled20)接口启用默认错误页后，才会生效。

## 解决方案

* **场景一**：

  ArkWeb的网络协议栈错误列表中，errorCode为0表示正常加载，其他值表示异常加载。

  定义successLoad变量控制页面显示，当加载失败后把errorCode赋值给successLoad变量，重新刷新页面时设置successLoad的值为0（若不设置为0，则缺省页面一直展示）。页面采用Stack布局，包含缺省页面层和Web页面层，当successLoad为0时展示Web页面，successLoad为其他值展示缺省页面。

  ```ts
  import { webview } from '@kit.ArkWeb';

  // 请换成实际应用的在线地址
  const WEB_URL: string | Resource = 'www.example.com';

  @Entry
  @Component
  struct WebLoadErrorPage1 {
    @State successLoad: number = 0;
    webController: webview.WebviewController = new webview.WebviewController();

    build() {
      Stack() {
        Column() { // 缺省页
          Button('重新加载')
            .onClick(() => {
              this.successLoad = 0;
              this.webController.refresh();
            });
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
        .visibility(this.successLoad !== 0 ? Visibility.Visible : Visibility.None);

        Web({ src: WEB_URL, controller: this.webController }) // Web页面
          .width('100%')
          .height('100%')
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false)
          .visibility(this.successLoad === 0 ? Visibility.Visible : Visibility.Hidden)
          .onErrorReceive((event) => {
            if (event.error.getErrorCode() !== 0) {
              this.successLoad = event.error.getErrorCode();
            }
          });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* **场景二**：

  ArkTS侧实现Web加载H5页面的功能，当加载失败后onErrorReceive回调的errorCode不为0时，使用loadUrl加载本地H5页面，并通过javaScriptProxy接口给H5注入对应的对象和方法，以便H5侧能调用。

  ```ts
  import { webview } from '@kit.ArkWeb';

  // 请换成实际应用的在线地址
  const WEB_URL: string | Resource = 'www.example.com';

  class WebManager {
    private controller?: webview.WebviewController;

    constructor(controller: webview.WebviewController) {
      this.controller = controller;
    }

    refresh() {
      this.controller?.loadUrl(WEB_URL);
    }
  }

  @Entry
  @Component
  struct WebLoadErrorPage2 {
    webController: webview.WebviewController = new webview.WebviewController;
    webManager: WebManager = new WebManager(this.webController);

    build() {
      Column() {
        Web({ src: WEB_URL, controller: this.webController })
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false)
          .javaScriptProxy({
            object: this.webManager,
            name: 'WebManager',
            methodList: ['refresh'],
            controller: this.webController,
          })
          .domStorageAccess(true)
          .onErrorReceive((event) => {
            if (event.error.getErrorCode() !== 0) {
              this.webController.loadUrl($rawfile('index.html'));
            }
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  在加载的本地H5侧触发重新加载的方法。

  html示例代码：

  ```html
  <!-- index.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <style>
          body {
            height: 100vh;
            display: flex;
            justify-content: center;  /* 水平居中 */
            align-items: center;      /* 垂直居中 */
          }
          .btn {
            border: none;   /* 移除边框 */
            border-radius: 30px;  /* 添加圆角 */
            padding: 12px 30px;
            font-size: 16px;
            background-color: #0A59F7;
            color: white;
            cursor: pointer;
          }
      </style>
  </head>
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover"/>
  <body>
  <button class="btn" onclick="refresh()">重新加载</button>
  </body>
  </html>
  <script>
      function refresh() {
        console.info('refresh')
        return window.WebManager.refresh()
      }
  </script>
  ```
* **场景三**：
  + **方案一**：ArkTS侧实现Web加载H5页面的功能，当加载失败后onErrorReceive回调的errorCode不为0时，使用loadData加载本地html格式的文本数据，并通过javaScriptProxy接口给H5注入对应的对象和方法，以便H5侧能调用。

    ```ts
    import { webview } from '@kit.ArkWeb';

    // 请换成实际应用的在线地址
    const WEB_URL: string | Resource = 'www.example.com';

    class WebManager {
      private controller?: webview.WebviewController;

      constructor(controller: webview.WebviewController) {
        this.controller = controller;
      }

      refresh() {
        this.controller?.loadUrl(WEB_URL);
      }
    }

    @Entry
    @Component
    struct WebLoadErrorPage3 {
      controller: webview.WebviewController = new webview.WebviewController();
      webManager: WebManager = new WebManager(this.controller);

      build() {
        Column() {
          Web({ src: WEB_URL, controller: this.controller })
            .domStorageAccess(true)
            .fileAccess(false)
            .geolocationAccess(false)
            .javaScriptProxy({
              object: this.webManager,
              name: 'WebManager',
              methodList: ['refresh'],
              controller: this.controller,
            })
            .onErrorReceive((event) => {
              if (event.error.getErrorCode() !== 0) {
                this.controller.loadData(
                  '<html>\n' +
                    '<head>\n' +
                    '    <meta charset=\"UTF-8\" />\n' +
                    '   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n' +
                    '    <style>\n' +
                    '        body {\n' +
                    '          height: 90vh;\n' +
                    '          display: flex;\n' +
                    '          justify-content: center;  /* 水平居中 */\n' +
                    '          align-items: center;      /* 垂直居中 */\n' +
                    '        }\n' +
                    '        .btn {\n' +
                    '          border: none;\n' +
                    '          border-radius: 30px;\n' +
                    '          padding: 12px 30px;\n' +
                    '          font-size: 16px;\n' +
                    '          background-color: #0A59F7;\n' +
                    '          color: white;\n' +
                    '          cursor: pointer;\n' +
                    '        }\n' +
                    '    </style>\n' +
                    '</head>\n' +
                    '<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover\"/>\n' +
                    '<body>\n' +
                    '<button class=\"btn\" onclick=\"refresh()\">重新加载</button>\n' +
                    '</body>\n' +
                    '</html>\n' +
                    '<script>\n' +
                    '    function refresh() {\n' +
                    '      console.info("refresh")\n' +
                    '      return window.WebManager.refresh()\n' +
                    '    }\n' +
                    '</script>',
                  'text/html',
                  'UTF-8',
                  ' ', // baseUrl设置为空格
                  ' ' // historyUrl设置为空格
                );
              }
            });
        };
      }
    }
    ```
  + **方案二**：如果在API20及以上版本，可以在onControllerAttached回调中将setErrorPageEnabled设置为true启用默认错误页。当加载网络页面加载失败后会回调onOverrideErrorPage接口，该接口是一个用于处理错误页面的机制，将需要实现html文本return后，就会把内容渲染在该页面上。

    ```ts
    import { webview } from '@kit.ArkWeb';

    // 请换成实际应用的在线地址
    const WEB_URL: string | Resource = 'www.baidu.com';

    class WebManager {
      private controller?: webview.WebviewController;

      constructor(controller: webview.WebviewController) {
        this.controller = controller;
      }

      refresh() {
        this.controller?.loadUrl(WEB_URL);
      }
    }

    @Entry
    @Component
    struct WebLoadErrorPage4 {
      controller: webview.WebviewController = new webview.WebviewController();
      webManager: WebManager = new WebManager(this.controller);

      build() {
        Column() {
          Web({ src: WEB_URL, controller: this.controller })
            .domStorageAccess(true)
            .fileAccess(false)
            .geolocationAccess(false)
            .onControllerAttached(() => {
              this.controller.setErrorPageEnabled(true);
              if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
              }
            })
            .javaScriptProxy({
              object: this.webManager,
              name: 'WebManager',
              methodList: ['refresh'],
              controller: this.controller,
            })
            .onOverrideErrorPage(event => {
              if (event.error.getErrorCode() !== 0) {
                let htmlStr = '<html>\n' +
                  '<head>\n' +
                  '    <meta charset=\"UTF-8\" />\n' +
                  '   <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n' +
                  '    <style>\n' +
                  '        body {\n' +
                  '          height: 100vh;\n' +
                  '          display: flex;\n' +
                  '          justify-content: center;  /* 水平居中 */\n' +
                  '          align-items: center;      /* 垂直居中 */\n' +
                  '        }\n' +
                  '        .btn {\n' +
                  '          border: none;\n' +
                  '          border-radius: 30px;\n' +
                  '          padding: 12px 30px;\n' +
                  '          font-size: 16px;\n' +
                  '          background-color: #0A59F7;\n' +
                  '          color: white;\n' +
                  '          cursor: pointer;\n' +
                  '        }\n' +
                  '    </style>\n' +
                  '</head>\n' +
                  '<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,maximum-scale=1,minimum-scale=1,viewport-fit=cover\"/>\n' +
                  '<body>\n' +
                  '<button class=\"btn\" onclick=\"refresh()\">重新加载</button>\n' +
                  '</body>\n' +
                  '</html>\n' +
                  '<script>\n' +
                  '    function refresh() {\n' +
                  '      console.info("refresh")\n' +
                  '      return window.WebManager.refresh()\n' +
                  '    }\n' +
                  '</script>';
                return htmlStr;
              }
              return null;
            });
        };
      }
    }
    ```

    **说明** 

    加载在线网址时需在module.json5中声明ohos.permission.INTERNET权限，确保在线跳转可用。

    ```json
    "requestPermissions": [
      { "name": "ohos.permission.INTERNET" }
    ],
    ```

## 常见FAQ

Q：为什么加载视频的网页一直触发onErrorReceive？

A：在onErrorReceive回调中，查看getErrorCode获取的错误码为-2。-2表示ERR\_FAILED，是一个通用的错误代码，表明产生了一般性的错误。错误产生与多种原因有关，可以表示网络错误、文件传输失败、协议栈错误等。接着分析网页的网络请求，发现网页发出了多个请求，而多个响应的HTTP状态码为206。

HTTP的206状态码用于表示服务器已成功处理部分Get请求，常见于视频加载和文件下载，尤其是断点续传场景。从错误码和状态码验证可知，一直触发onErrorReceive的原因是，网页中请求了视频资源，而视频使用了断点续传技术，就会导致资源请求多次。因为每一次只处理部分请求，没有完成整个文件的传输，就会引起onErrorReceive回调一次或者多次。

## 总结

可以根据缺省页面的实现形式选择实现方案：

| 缺省页面的实现形式 | 方案的主要实现方法 | 优点 | 缺点 |
| --- | --- | --- | --- |
| ArkTS页面 | onErrorReceive回调+visibility控件显示状态。 | 加载速度极快，ArkTS渲染，无加载延迟。 | 需要编写缺省页ArkTS页面布局。 |
| html页面 | onErrorReceive回调+loadUrl加载本地html页面。 | 可模块化管理，便于调试，可复用其他端html页面。 | 需要将html文件放在资源目录下，需要文件系统IO，首次加载有延迟。 |
| html格式的文本数据 | 方案一： onErrorReceive回调+loadData加载html格式的文本数据。 | 从内存解析，启动瞬间完成。 | 复杂页面难以维护，全部写成字符串很臃肿。 |
| html格式的文本数据 | 方案二：setErrorPageEnabled+onOverrideErrorPage回调中添加html格式的字符串。 | 系统自定义页面，可以直接将html内容渲染在页面上，用户体验感相对于loadData更好。 | 复杂页面难以维护，全部写成字符串很臃肿。 |

* 优先推荐使用ArkTS页面实现缺省页，ArkTS渲染，体验感最佳。
* 如果缺省页页面逻辑简单，且需要使用html实现，在API20及以上版本推荐使用onOverrideErrorPage回调方法，API20以下版本推荐使用loadData方法。
* 页面复杂并已有html页面，推荐使用loadUrl方法。
