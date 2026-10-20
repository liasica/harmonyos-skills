---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-faq-0005
title: ArkWeb多媒体文件加载常见问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 常见问题 > ArkWeb多媒体文件加载常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:47+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:078b7b72083bd931846eb1edbb45260695ccd3ae1586d9e8f47ba0ed1eaad911
---

**Q：HEIF和HEIC、SVGA和SVG分别是什么，Web组件如何加载这些文件？**

**A**：HEIF、HEIC和SVG图片支持在HTML里直接通过img标签展示，以加载本地图片为例（需要先将HTML文件放到rawfile目录下，图片资源文件放到rawfile/img目录下），完整样例代码如下：

```html
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

```ts
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

SVGA动画不支持在HTML里直接通过img标签展示，可以通过使用SVGA-Web播放器([SVGAPlayer-Web](https://github.com/svga/SVGAPlayer-Web))在Web组件中加载SVGA动画，具体步骤如下：

1. 在resources目录下新建一个resfile目录，并把HTML文件放到resfile目录下，图片资源文件放到resfile/img目录下，js文件放到resfile/js目录下。
2. 引入播放器库：

   在HTML的head标签中，引入SVGA播放器库。

   ```html
   -->
       <script src="js/svga.min.js"></script>
       <!--
   ```
3. 准备动画容器：

   在页面中创建一个div元素作为SVGA动画的舞台。

   ```html
   -->
       <div id="svgaContainer"></div>
       <!--
   ```
4. 加载并播放动画：

   编写JavaScript代码，初始化播放器并加载远程或本地的.svga文件。

   ```js
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

```ts
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

```html
-->
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
    <!-- Start solution2 -->
    <script src="js/svga.min.js"></script>
    <!-- End solution2 -->
</head>

<body>
<div class="img-container flex-center">
    <!-- Start solution3 -->
    <div id="svgaContainer"></div>
    <!-- End solution3 -->
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
<!--
```
