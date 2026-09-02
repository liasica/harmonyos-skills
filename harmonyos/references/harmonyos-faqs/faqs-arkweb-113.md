---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-113
title: Web加载视频布局异常
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web加载视频布局异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c6c2157ff079dcb9930cee2d9c599d2884a4c2ba4f725b64fa9e62e8ccf8fcb
---

## 问题现象

加载视频完成前下半部分会被遮挡，加载完成再展示全部。

## 背景知识

* iframe标签：用于在网页中嵌入另一个网页或资源。其默认行为是根据内容自动调整大小，除非设置了固定宽高或通过CSS限制了尺寸。
* video标签：HTML5中用于嵌入视频内容的标签，支持自动播放、全屏、尺寸控制等属性。
* 视频加载机制：当video加载完成后，其本身尺寸可能会根据视频的分辨率进行调整，若没有限制，则可能影响iframe的布局。
* [ArkWeb](../harmonyos-guides/web-component-overview.md)（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。

## 问题定位

在使用iframe加载video时，iframe没有设置宽高，video加载完成后超过iframe的宽高就会撑开，导致页面异常。

1. 通过[DevEco Testing](https://developer.huawei.com/consumer/cn/download/)的UIViewer查看页面布局，确认使用iframe嵌入的页面。
2. 对比两个iframe中的video组件的宽高。确认video组件宽高没有设置固定值。

## 分析结论

视频在加载完成后改变了自身尺寸，而iframe未对其内容的大小变化进行有效限制。因此，iframe自动扩展以适应内容，导致外部页面布局异常。

## 修改建议

1. 使用ArkWeb加载iframe页面：

   ```screen
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Web({ src: $rawfile('iframe.html'), controller: this.controller })
           .geolocationAccess(false)
           .fileAccess(true)
       }
     }
   }
   ```
2. 设置iframe内video的固定尺寸：

   ```screen
   <!doctype html>
   <html lang="zh">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport"
             content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Video</title>
   </head>
   <style>
       <!--  CSS样式设置  -->
       video {
         width: 100%;
         height: 300px;
         object-fit: contain;
       }
   </style>
   <body>
       <div>
           <!--  内联样式设置  -->
           <video width="100%" height="300px" controls>
               <source src="根据实际需要添加mp4格式的视频地址" type="video/mp4">
           </video>
       </div>
   </body>
   </html>
   ```
3. 限制iframe的最大尺寸：

   ```screen
   <!doctype html>
   <html lang="zh">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport"
             content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>Iframe</title>
   </head>
   <style>
       <!--  CSS样式设置  -->
       iframe {
           width: 100%;
           height: 300px;
           max-width: 100%;
           max-height: 300px;
           overflow: hidden;
       }
   </style>
   <body>
   <!--  内联样式设置  -->
   <iframe src="./iframeVideo.html"
           frameborder="0"
           width="100%"
           height="300px"
           style="max-width: 100%; max-height: 300px; overflow: hidden;"
           allowfullscreen="allowfullscreen">

   </iframe>
   </body>
   </html>
   ```
