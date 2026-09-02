---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-180
title: Web组件如何加载HEIF、HEIC、SVGA、SVG文件
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何加载HEIF、HEIC、SVGA、SVG文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a5c43ce96289526bbdb4e2b2d157fa2913520a6371d46bd683adf8bb60f17ae
---

## 问题现象

HEIF和HEIC、SVGA和SVG分别是什么，Web组件如何加载这些文件？

## 背景知识

* HEIF图片（High Efficiency Image File Format），是一个用于单张图像或图像序列的文件格式。目前主流的HEIF图片均使用HEVC(H.265)编码。
* HEIC是符合HEIF标准、使用HEVC编码的具体图像文件。
* SVGA是一种轻量级的动画格式，相比GIF和APNG格式，它支持更多的动画特性，如透明度、缩放和旋转等。
* SVG（Scalable Vector Graphics）是可缩放矢量图形，它是一种基于XML（可扩展标记语言）的图形格式，用于描述二维图形和图像。具体可参考[SVG标签说明](../harmonyos-references/ts-basic-svg.md)。

## 解决方案

* HEIF、HEIC和SVG图片支持在HTML里直接通过img标签展示，以加载本地图片为例（需要先将HTML文件放到rawfile目录下，图片资源文件放到rawfile/img目录下）。

  完整样例代码如下：

  ```screen
  <!-- heif.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>测试HEIF/HEIC/SVG图片</title>
      <style>
          p {
              font-size: 16px;
          }
          .flex-center {
              display: block;
              justify-content: center;
              align-items: center;
              min-height: 300px;
          }
          .responsive-img {
              width: 55%;
              height: auto;
              justify-content: center;
              align-items: center;
          }
      </style>
  </head>
  <body>
  <div class="flex-center">
      <div>
          <p>HEIF图片</p>
          <!--网络图片src直接换成对应的url地址即可-->
          <img class="responsive-img" src="img/test.heif">
      </div>
      <div>
          <p>HEIC图片</p>
          <!--网络图片src直接换成对应的url地址即可-->
          <img class="responsive-img" src="img/test.heic">
      </div>
      <div>
          <p>SVG图片</p>
          <!--网络图片src直接换成对应的url地址即可-->
          <img class="responsive-img" src="img/test.svg">
      </div>
  </div>
  <script>
  </script>
  </body>
  </html>
  ```

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct HEIFDemo {
    controller: webview.WebviewController = new webview.WebviewController();
    context: Context = this.getUIContext().getHostContext() as Context;

    build() {
      Column() {
        Web({
          src: $rawfile('heif.html'),
          controller: this.controller
        })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(false);
      };
    }
  }
  ```
* SVGA动画不支持在HTML里直接通过img标签展示，可以通过使用SVGA-Web播放器([SVGAPlayer-Web](https://github.com/svga/SVGAPlayer-Web))在Web组件中加载SVGA动画，具体步骤如下：
  1. 在resources目录下新建一个resfile目录，并把HTML文件放到resfile目录下，图片资源文件放到resfile/img目录下，js文件放到resfile/js目录下。
  2. 引入播放器库：

     在HTML的head标签中，引入SVGA播放器库。

     ```screen
     <script src="js/svga.min.js"></script>
     ```
  3. 准备动画容器：

     在页面中创建一个div元素作为SVGA动画的舞台。

     ```screen
     <div id="svgaContainer"></div>
     ```
  4. 加载并播放动画：

     编写JavaScript代码，初始化播放器并加载远程或本地的.svga文件。

     ```screen
     document.addEventListener('DOMContentLoaded', function () {
       // 1. 初始化播放器，绑定到容器
       let player = new SVGA.Player('#svgaContainer');
       // 2. 初始化解析器
       let parser = new SVGA.Parser();

       // 3. 加载并解析SVGA文件，此处load的url使用的是本地文件的地址，也可以使用在线的svga文件，例如：xxx.com/xxx.svga
       parser.load("file:///data/storage/el1/bundle/entry/resources/resfile/img/test.svga",
         function (videoItem) {
           // 4. 将解析好的视频项设置给播放器
           player.setVideoItem(videoItem);
           // 5. 开始播放动画
           player.startAnimation();
         }, function (error) {
           console.error('SVGA文件加载失败:', error);
         });
     });
     ```

  完整的样例代码如下：

  ```screen
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct SVGADemo {
    controller: webview.WebviewController = new webview.WebviewController();
    context: Context = this.getUIContext().getHostContext() as Context;

    build() {
      Column() {
        Web({
          src: '',
          controller: this.controller
        })
          .onControllerAttached(() => {
            try {
              this.controller.setPathAllowingUniversalAccess([
                this.getUIContext().getHostContext()!.resourceDir
              ]);
              this.controller.loadUrl('file://' + this.context!.resourceDir + '/svga.html');
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
            }
          })
          .fileAccess(true)
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(false);
      };
    }
  }
  ```

  ```screen
  <!DOCTYPE html>
  <html>
  <head>
      <title>加载SVGA</title>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
          .img-container {
              padding: 20px;
              margin: 10px;
          }
          .flex-center {
              display: flex;
              justify-content: center;
              align-items: center;
          }
          #svgaContainer {
              width: 300px;
          }
      </style>
      <script src="js/svga.min.js"></script>
  </head>
  <body>
  <div class="img-container flex-center">
      <div id="svgaContainer"></div>
  </div>
  <script>
      document.addEventListener('DOMContentLoaded', function () {
          // 1. 初始化播放器，绑定到容器
          let player = new SVGA.Player('#svgaContainer');
          // 2. 初始化解析器
          let parser = new SVGA.Parser();
          // 3. 加载并解析SVGA文件，此处load的url使用的是本地文件的地址，也可以使用在线的svga文件，例如：xxx.com/xxx.svga
          parser.load("file:///data/storage/el1/bundle/entry/resources/resfile/img/test.svga",
              function (videoItem) {
                  // 4. 将解析好的视频项设置给播放器
                  player.setVideoItem(videoItem);
                  // 5. 开始播放动画
                  player.startAnimation();
              }, function (error) {
                  console.error('SVGA文件加载失败:', error);
              });
      });
  </script>
  </body>
  </html>
  ```
