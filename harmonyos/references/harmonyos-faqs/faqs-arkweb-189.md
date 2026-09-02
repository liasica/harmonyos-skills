---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-189
title: 如何解决应用侧从H5侧接收参数报错问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决应用侧从H5侧接收参数报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfc510d30b83d2d92968e2a09e0a06513c054124230a44bd31819f8d087cd43f
---

## 问题现象

1. 参考[建立应用侧与前端页面数据通道](../harmonyos-guides/web-app-page-data-channel.md)代码，H5中通过postMessage方法传递消息，应用侧接收不到？

   代码报错：

   ```shell
   This type not support, only string/number/boolean/arraybuffer/array/error is supported
   ```

   截取部分代码：

   ```java
   function PostMsgToEts() {
     if (h5Port) {
       let obj = {name:'hahah',id:10}
       h5Port.postMessage(obj);
     } else {
       console.error('h5Port is null, Please initialize first');
     }
   }
   ```
2. 通过runJavaScriptExt方法执行了H5的方法，H5会回传一个字典类型的数据，但是无法获取到该数据，执行JsMessageExt的getType()和getString()方法报错，具体报错如下：

   ```java
   This type not support, only string/number/boolean/arraybuffer/array is supported
   ```

## 背景知识

* [WebMessagePort](../harmonyos-references/arkts-apis-webview-webmessageport.md)：通过WebMessagePort可以进行消息的发送以及接收，发送WebMessageType/WebMessage类型消息给HTML5侧。
* [WebMessage](../harmonyos-references/arkts-apis-webview-t.md#webmessage)：用于描述WebMessagePort所支持的数据类型。
* [runJavaScriptExt](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)：异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。runJavaScriptExt需要在loadUrl完成后，比如onPageEnd中调用。
* [JsMessageExt](../harmonyos-references/arkts-apis-webview-jsmessageext.md)：runJavaScriptExt接口执行脚本返回的数据对象。

## 问题定位

根据报错提示This type not support类型不支持，查看消息类型是否正确。检查后发现传递的数据类型为对象，与系统支持的数据类型不符。系统仅支持以下数据类型：string、number、boolean、arraybuffer及array。

## 分析结论

1. WebMessage所支持的数据类型有string/arraybuffer，代码中传递的数据是对象类型。
2. JsMessageExt所支持的数据类型有string/number/boolean/arraybuffer/array，代码中传递的数据是对象类型。

## 修改建议

WebMessage所支持的数据类型有string和arraybuffer， JsMessageExt所支持的数据类型有string/number/boolean/arraybuffer/array，两者都不支持对象类型，可以把对象类型通过JSON.stringify方法转成string类型进行传递。

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  ports: webview.WebMessagePort[] = [];
  @State receivedFromHtml: string = 'Display received message send from HTML';

  build() {
    Column() {
      // 展示接收到的来自HTML的内容
      Text(this.receivedFromHtml);
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(false)
        .fileAccess(false)
        .onPageEnd(() => {
          try {
            // 1、创建两个消息端口。
            this.ports = this.controller.createWebMessagePorts();
            if (this.ports && this.ports[0] && this.ports[1]) {
              // 2、在应用侧的消息端口(如端口1)上注册回调事件。
              this.ports[1].onMessageEvent((result: webview.WebMessage) => {
                let msg = 'Got msg from HTML:';
                if (typeof (result) === 'string') {
                  console.info(`received string message from html5, string is: ${result}`);
                  msg = msg + result;
                } else if (typeof (result) === 'object') {
                  if (result instanceof ArrayBuffer) {
                    console.info(`received arraybuffer from html5, length is: ${result.byteLength}`);
                    msg = msg + 'length is ' + result.byteLength;
                  } else {
                    console.info('not support');
                  }
                } else {
                  console.info('not support');
                }
                this.receivedFromHtml = msg;
              });
              // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
              this.controller.postMessage('__init_port__', [this.ports[0]], '*');
            } else {
              console.error(`ports is null, Please initialize first`);
            }
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
    };
  }
}
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <title>WebView Message Port Demo</title>
</head>
<body>
<h1>WebView Message Port Demo</h1>
<div>
    <input onclick="postMsgToEts();" type="button" value="SendToEts"/><br/>
</div>

</body>
<script>
    let h5Port;
    let output = document.querySelector('.output');
    window.addEventListener('message', function (event) {
        if (event.data === '__init_port__') {
            if (event.ports[0] !== null) {
                // 1. 保存从应用侧发送过来的端口。
                h5Port = event.ports[0];
                h5Port.onmessage = function (event) {
                  // 2. 接收ets侧发送过来的消息。
                  let msg = 'Got message from ets:';
                  let result = event.data;
                  if (typeof(result) === 'string') {
                    console.info(`received string message from ets, string is: ${result}`);
                    msg = msg + result;
                  } else if (typeof(result) === 'object') {
                    if (result instanceof ArrayBuffer) {
                      console.info(`received arraybuffer from ets, length is: ${result.byteLength}`);
                      msg = msg + 'length is ' + result.byteLength;
                    } else {
                      console.info('not support');
                    }
                  } else {
                    console.info('not support');
                  }
                }
            }
        }
    })
    // 3. 使用h5Port向应用侧发送消息。
    function postMsgToEts() {
        if (h5Port) {
            let obj = { name: 'hahah', id: 10 }
            h5Port.postMessage(JSON.stringify(obj)); // 对象类型通过JSON.stringify方法转成string类型
        } else {
            console.error('h5Port is null, Please initialize first');
        }
    }
</script>
</html>
```

## 常见FAQ

Q：runJavaScript()和runJavaScriptExt()有什么区别？

A：[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)的区别主要体现在参数和返回值的类型上。[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)仅支持string类型参数，而[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)支持string和ArrayBuffer类型参数；[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)返回脚本执行的结果只能是string，而[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)可以返回的类型支持[JsMessageType](../harmonyos-references/arkts-apis-webview-e.md#jsmessagetype10)，包括字符串、数组类型等。
