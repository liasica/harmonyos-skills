---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-111
title: 视频详情页加载时，视频出现由小变大的缩放问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 视频详情页加载时，视频出现由小变大的缩放问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b4a3f5fe5a87487b650adc3abce3aa551cdae41f5cc51ae82c70d656739e4e0
---

## 问题现象

页面加载时，先出现一个背景为黑色的视频播放组件，等视频预览图加载完成后，切换成和预览图宽高相同的视频播放组件，页面出现闪跳。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/K35-03LCQK6r6tWngc2xyA/zh-cn_image_0000002629059046.png "点击放大")

## 背景知识

* [Web](../harmonyos-references/arkts-basic-components-web.md)组件提供网页显示能力。
* html页面中video是用于嵌入视频内容的标签，其src属性为视频文件的URL，poster为视频未开始播放前显示的预览图。

## 问题定位

查看该Web页面的设置，该页面的视频组件初始尺寸较小，在加载完预览图后根据预览图的大小动态调整视频窗口的大小，导致页面出现闪跳。

```html
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>动态调整视频播放器尺寸</title>
    <style>
        * {
            padding: 0;
            margin: 0;
        }

        body {
            width: 100%;
            height: 100%;
            box-sizing: border-box;
            background-color: #f1f3f5;
        }

        .page {
            display: flex;
            justify-content: center;  /* 水平居中 */
            align-items: center;      /* 垂直居中 */
            align-items: flex-start;
            width: 100%;
            height: 100%;
            box-sizing: border-box;
        }

        .video-box {
            width: 300px;
            display: flex;
            justify-content: center;  /* 水平居中 */
            align-items: center;      /* 垂直居中 */
            align-items: center;
            box-sizing: border-box;
            margin-top: 200px;
        }

        .myVideo {
            width: 100%;
            height: 100%;
            object-fit: contain;
            background-color: black;
        }
    </style>
</head>
<body>

<div class="page" >
    <div class="video-box" id="videoContainer">
        <video autoplay loop id="videoPlayer" class="myVideo" controls controlslist="nodownload noremoteplayback noplaybackrate">
            <source type="video/mp4">
        </video>
    </div>
</div>
<script>
    const videoPlayer = document.getElementById('videoPlayer');
    const videoContainer = document.getElementById('videoContainer');

    // 模拟加载图片和视频资源延时
    setTimeout(() => {
      const img = new Image();
      // 'xxx.jpg'需要替换为开发者需要的图片资源文件
      videoPlayer.poster = 'xxx.jpg'; 
      // 'xxx.mp4'需要替换为开发者需要的视频资源文件
      videoPlayer.src = 'xxx.mp4';
      img.src = videoPlayer.poster;

      img.onload = function () {
        // 获取图片尺寸
        const width = this.naturalWidth*0.6;
        const height = this.naturalHeight*0.6;

        // 动态设置容器尺寸
        videoContainer.style.width = width + 'px';
        videoContainer.style.height = height + 'px';
      };
     }, 1000);
</script>
</body>
</html>
```

## 分析结论

该Web页面的视频组件初始尺寸较小，在加载完预览图后根据预览图的大小动态调整视频窗口的大小，导致页面出现闪跳。

## 修改建议

为Web页面的视频组件设置合适的尺寸，并设置为不随预览图的大小而改变尺寸。

* ets文件：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    controller: webview.WebviewController = new webview.WebviewController();

    aboutToAppear(): void {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowLayoutFullScreen(true);
      });
    }

    build() {
      Stack() {
        Web({ src: $rawfile('webVideo.html'), controller: this.controller })
          .geolocationAccess(false)
          .fileAccess(true)
          .height('100%')
          .width('100%')
      }
      .height('100%')
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]) // 扩展页面区域到导航栏和状态栏
    }
  }
  ```
* html文件：

  ```html
  <!DOCTYPE html>
  <html lang="zh">
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>动态调整视频播放器尺寸</title>
      <style>
          * {
              padding: 0;
              margin: 0;
          }

          body {
              width: 100%;
              height: 100%;
              box-sizing: border-box;
              background-color: #f1f3f5;
          }

          .page {
              display: flex;
              justify-content: center;  /* 水平居中 */
              align-items: center;      /* 垂直居中 */
              align-items: flex-start;
              width: 100%;
              height: 100%;
              box-sizing: border-box;
          }

          .video-box {
              width: 380px;
              height: 240px;
              display: flex;
              justify-content: center;  /* 水平居中 */
              align-items: center;      /* 垂直居中 */
              align-items: center;
              box-sizing: border-box;
              margin-top: 200px;
          }

          .myVideo {
              width: 100%;
              height: 100%;
              object-fit: contain;
              background-color: black;
          }
      </style>
  </head>
  <body>

  <div class="page" >
      <div class="video-box" id="videoContainer">
          <video autoplay loop id="videoPlayer" class="myVideo" controls>
              <source type="video/mp4">
          </video>
      </div>
  </div>
  <script>
      const videoPlayer = document.getElementById('videoPlayer');
      const videoContainer = document.getElementById('videoContainer');

      // 模拟加载图片和视频资源延时
      setTimeout(() => {
        const img = new Image();
         // https://www.example.png
        videoPlayer.poster = '预加载的图片，请根据需要替换成实际图片地址';
        // https://www.example.mp4
        videoPlayer.src = '加载的视频，请根据需要替换成实际视频地址';

       }, 1000);
  </script>
  </body>
  </html>
  ```
