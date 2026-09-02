---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-31
title: 平板全屏播放视频时页面异常
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板全屏播放视频时页面异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a9952a2fb987d0521bb8f95f0f184ea06d63c1bf92587c9c8228fb042cd67f8
---

## 问题现象

在平板设备上，点击全屏播放视频时，视频没有全屏且高度变小。

## 背景知识

* [Web](../harmonyos-references/ts-basic-components-web.md)：提供具有网页显示的能力。应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。也可以通过[onFullScreenEnter](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenenter9)和[onFullScreenExit](../harmonyos-references/arkts-basic-components-web-events.md#onfullscreenexit9)方法，监听Web组件进入和退出全屏模式事件。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的显示方向属性，使用callback异步回调。仅在支持跟随sensor旋转的设备上生效，2in1设备上调用不生效，自由多窗模式（可点击设备控制中心中的自由多窗按钮开启）下调用不生效，子窗调用后不生效。

## 问题定位

1. 通过DevEco Testing查看视频所在页面，发现视频是基于Web组件实现。
2. 根据布局确认网页链接，尝试使用浏览器打开查看网页布局样式，看全屏播放时是否正常。
3. 检查代码中是否使用onFullScreenEnter方法监听Web组件进入全屏模式事件，是否通知Web页面进行横竖屏旋转。

## 分析结论

H5侧实现了全屏播放功能，但由于Web组件没有使用onFullScreenEnter方法监听Web组件进入全屏模式事件，没有对H5侧的点击事件做适配，导致全屏播放视频时页面异常。

## 修改建议

1. 通过Web组件的onFullScreenEnter和onFullScreenExit方法，监听Web组件进入和退出全屏模式事件。

   ```ts
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebFullScreenPlayVideo {
     private controller: WebviewController = new webview.WebviewController();

     private setScreenOrientation(isLandscape: boolean) {
       // 获取UIAbility实例的上下文信息
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // 调用该接口手动改变设备横竖屏状态
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
       });
     }

     build() {
       Column() {
         Web({ src: $rawfile('webFullVideo.html'), controller: this.controller })  // 请换成本地html页面
           .fileAccess(false) // 禁用本地文件访问
           .geolocationAccess(false) // 禁用地理位置
           .onFullScreenEnter(() => { // 监听Web组件进入全屏模式事件
             this.setScreenOrientation(true);
           })
           .onFullScreenExit(() => { // 监听Web组件退出全屏模式事件
             this.setScreenOrientation(false);
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
2. webFullVideo.html文件：

   ```ts
   <!DOCTYPE html>
   <html lang="zh-CN">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>全屏播放视频</title>
       <style type="text/css">
           body {
               margin: 0;
               padding: 0;
               overflow: hidden;
           }

           video {
               width: 100%;
               height: 100%;
               object-fit: fill;
           }
       </style>
   </head>

   <body>
   <video autoplay controls>
       <!-- 替换为实际地址 -->
       <source src="example.mp4" type="video/mp4">
   </video>

   <script type="text/javascript">
       let video = document.querySelector('video');

       // 进入全屏
       function requestFullscreen() {
           video.webkitRequestFullscreen();
           return 1;
       }

       // 退出全屏
       function exitFullscreen() {
           document.webkitExitFullscreen();
           return 0;
       }

       // 监听全屏变化事件
       document.addEventListener('fullscreenchange', function () {
           if (document.fullscreenElement) {

               // 进入全屏时，将视频旋转90度-->
               video.style.transform = 'rotate(90deg)';
               video.style.width = '100vh';
               video.style.height = '100vw';
           } else {
               // 退出全屏时，将视频旋转回来-->
               video.style.transform = 'none';
               video.style.width = '100%';
               video.style.height = '100%';
           }
       });

       // 监听窗口大小变化事件
       window.addEventListener('resize', function () {
           if (document.fullscreenElement) {
               // 窗口大小变化时，调整视频大小
               video.style.width = '100vh';
               video.style.height = '100vw';
           }
       });

       // 点击播放按钮时，进入全屏
       video.addEventListener('play', function () {
           requestFullscreen();
           video.style.transform = 'rotate(90deg)';
           video.style.width = '100vh';
           video.style.height = '100vw';
       });

       // 点击退出按钮时，退出全屏
       video.addEventListener('ended', function () {
           exitFullscreen();
       });
   </script>
   </body>
   </html>
   ```
