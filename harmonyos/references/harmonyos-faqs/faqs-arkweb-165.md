---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-165
title: 应用侧如何获取H5中input元素的accept属性值
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 应用侧如何获取H5中input元素的accept属性值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7345ba8b1b206bf6d5fb17c57f0f59ff3823594b207ee5f0377204ad5e0f5d8
---

## 问题现象

应用侧如何获取H5中input元素的accept属性值？

```screen
<input type="file" id="upload" accept="image/*, video/*" name="upload"/>
```

## 背景知识

[onShowFileSelector](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)：调用此函数以处理具有“文件”输入类型的HTML表单。如果不调用此函数或返回false，Web组件会提供默认的“选择文件”处理界面。如果返回true，应用可以自定义“选择文件”的响应行为。

## 解决方案

通过getMimeTypes方法获取accept属性值。

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
export struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mimeTypes: string = '';
  @State acceptTypes: string = '';

  build() {
    Column() {
      Column() {
        Text(`${this.mimeTypes}`)
          .margin(10);
        Text(`${this.acceptTypes}`);
      }
      .margin(10);

      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          if (event) {
            let mimeTypes = event?.fileSelector.getMimeTypes();
            console.info(`getMimeTypes：${mimeTypes}`);
            this.mimeTypes = `getMimeTypes：${mimeTypes}`;
            let acceptTypes = event?.fileSelector.getAcceptType();
            console.info(`getAcceptType：${acceptTypes}`);
            this.acceptTypes = `getAcceptType：${acceptTypes}`;
          }
          return false;
        });
    };
  }
}
```

```screen
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
</head>
<body>
<form id="upload-form" enctype="multipart/form-data">
    <input type="file" id="upload" accept="image/*, video/*" name="upload"/>
</form>
</body>
</html>
```

## 常见FAQ

Q：回调中getAcceptType和getMimeTypes的区别？

A：getAcceptType返回的是accept属性值全量转换为文件扩展名所组成的字符串数组，getMimeTypes返回的是accept属性值用逗号拆分后所组成的字符串数组。如若accept属性值为video/mp4,.png，则getAcceptType返回.mp4, .m4v;.png ，getMimeTypes返回video/mp4;.png。

Q：Web组件中如何获取HTML内容？

A：可以在Webview中注入JavaScript代码，执行document.documentElement.outerHTML来获取整个页面的HTML内容。

```screen
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
export struct WebPage {
  controller: webview.WebviewController = new webview.WebviewController();
  @State htmlContext: string = '';

  build() {
    Column() {
      Text(this.htmlContext);
      Button('测试')
        .onClick(() => {
          this.controller.runJavaScript(`document.documentElement.outerHTML`).then((res) => {
            hilog.info(0x0000, 'WebPage', res);
            // 替换转义序列
            this.htmlContext = res.replace(/\\u003C/g, '<').replace(/\\u003E/g, '>');
            hilog.info(0x0000, 'WebPage', this.htmlContext);
          }).catch((err: BusinessError) => {
            hilog.info(0x0000, 'WebPage', `errMsg: ${err.message}  errCode: ${err.code}`);
          });
        });
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true);

    };
  }
}
```
