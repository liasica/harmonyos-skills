---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-149
title: Webview中如何使用自定义字体
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Webview中如何使用自定义字体
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95634d7e2201780a28b15bf189c0224e12d230f7beb8abeb00865030eb3d59b7
---

## 问题现象

Webview中h5侧如何使用自定义字体？

## 背景知识

自定义字体是指开发者根据应用需求创建或选择的字体，通常用于实现特定的文字风格或满足独特的设计要求。当应用需要使用特定的文本样式和字符集时，可以注册并使用自定义字体进行文本渲染。

## 解决方案

使用本地自定义字体，实现思路参考如下：

1. 将字体文件放在resources/rawfile/font文件夹里。
2. h5侧直接通过font-face引用字体。

   ```screen
   @font-face {
     font-family: 'HarmonyOS Sans';
     src: url('./font/HarmonyOS_Sans_SC_Regular.ttf');
   }
   .harmonyos-sans {
     font-family: 'HarmonyOS Sans', sans-serif;
   }
   ```

完整示例参考如下：

* src/main/ets/pages/webPage页面。

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Web({
          src: $rawfile('Index.html'), controller: this.controller
        })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .onlineImageAccess(true)
          .geolocationAccess(false)
      }
    }
  }
  ```
* resources/rawfile/Index.html页面。

  ```screen
  <!DOCTYPE html>
  <html lang="en-gb">
  <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
      <title>自定义字体</title>
      <style>
          body {
            font-size: 20px;
          }
          @font-face {
            font-family: 'HarmonyOS Sans';
            src: url('./font/HarmonyOS_Sans_SC_Regular.ttf');
          }
          .harmonyos-sans {
            font-family: 'HarmonyOS Sans', sans-serif;
          }
      </style>
  </head>
  <body>
  <div class="harmonyos-sans">Sans字体：Innation in china</div>
  </body>
  </html>
  ```
