---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0001
title: ArkWeb视频加载布局异常问题定位
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > ArkWeb视频加载布局异常问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:47+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:95b4a62f9b95a4c419aba407a17d96b8cce9188adcdcd09a5d29468847a105b0
---

## 问题现象

加载视频完成前下半部分会被遮挡，加载完成再展示全部。

## 定位过程

在使用iframe加载video时，iframe没有设置宽高，video加载完成后超过iframe的宽高就会撑开，导致页面异常。

1. 通过[DevEco Testing](https://developer.huawei.com/consumer/cn/download/)的UIViewer查看页面布局，确认使用iframe嵌入的页面。
2. 对比两个iframe中的video组件的宽高。确认video组件宽高没有设置固定值。

## 分析结论

视频在加载完成后改变了自身尺寸，而iframe未对其内容的大小变化进行有效限制。因此，iframe自动扩展以适应内容，导致外部页面布局异常。

## 修改建议

1. 使用ArkWeb加载iframe页面：

   ```ts
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

   ```html
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

   ```html
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
