---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1392
title: 页面跳转时，有渐入渐出的动效
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面跳转时，有渐入渐出的动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e987ffb29c754b0131d283be14cfd7ceda501f6a95aa9a5bdbe03a2afe2cbc1d
---

## 问题现象

页面跳转时，有渐入渐出的动效，新旧页面内容出现重叠显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/0b_WsKYDQ1qjEkStCdCzIQ/zh-cn_image_0000002658961879.png "点击放大")

## 背景知识

* [Web](../harmonyos-references/arkts-basic-components-web.md)组件提供网页显示的能力。
* [transition](../harmonyos-references/ts-transition-animation-component.md)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。

## 问题定位

1. 使用DevEco Testing查看该页面的组件，跳转前后的页面分别通过不同的Web组件显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/pL34YSmpQWGDknxNWG4Olw/zh-cn_image_0000002628602668.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/gX4259b6TKCl0UcYgTU_bA/zh-cn_image_0000002658841939.png "点击放大")
2. 查看跳转之后的Web组件的相关设置，发现应用transition属性设置了透明度渐变的过渡效果。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebVideo {
     controller: webview.WebviewController = new webview.WebviewController();
     @State isShowNewWeb: boolean = false;

     build() {
       Stack() {
         Column() {
           Web({ src: $rawfile('VideoList.html'), controller: this.controller })
             .height('100%')
             .width('100%')
             .fileAccess(true)
             .geolocationAccess(false)
             .onLoadIntercept((event) => {
               if (event.data.getRequestUrl() === 'resource://rawfile/index_cn.html') {
                 this.isShowNewWeb = true;
                 return true; // 拦截此次跳转
               } else {
                 return false; // 允许跳转
               }
             });
         };

         if (this.isShowNewWeb) {
           Web({ src: $rawfile('index_cn.html'), controller: this.controller })
             .height('100%')
             .width('100%')
             .fileAccess(true)
             .geolocationAccess(false)
             .transition(TransitionEffect.OPACITY.animation({ duration: 2000, curve: Curve.Ease })); // 设置透明度渐变的过渡效果
         }
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 分析结论

在页面跳转过程中，使用新的Web组件呈现内容，同时对跳转后的Web组件应用transition属性设置了透明度渐变转场效果。

## 修改建议

* 方案一：不使用新的Web组件来显示页面，而是在原来的Web组件上进行页面跳转。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct SolutionOne {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Stack() {
        Column() {
          Web({ src: $rawfile('VideoList.html'), controller: this.controller })
            .height('100%')
            .width('100%')
            .fileAccess(true)
            .geolocationAccess(false)
          // 不对视频播放页面进行拦截，在原来的Web组件上进行页面跳转
        };
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  src/main/resources/rawfile/VideoList.html：

  ```ts
  <!DOCTYPE html>
  <html lang="zh">
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>视频列表</title>
      <style>
          body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
            color: #333;
          }

          /* 视频列表容器 */
          .video-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
          }

          /* 视频卡片 */
          .video-card {
            display: flex;           /* 启用 Flexbox */
            background-color: #f1f3f5;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
          }

          .video-text {
            text-align: center;
            width: 100px;
            margin-top: 40px;
          }

          .video-thumbnail {
            width: 150px;
            height: 100px;
            object-fit: contain;
            display: block;
            margin-left: 10px;
          }

      </style>
  </head>
  <body>

  <h1 style="font-size: 16px;">视频列表</h1>

  <div class="video-list">
      <!-- 视频项 1 -->
      <div class="video-card" onclick="newPage()">
          <!-- "img/poster1.PNG"需要替换为开发者需要的图片资源文件 -->
          <img src="img/poster1.PNG" alt="视频封面" class="video-thumbnail">
          <div class="video-text"> 视频1</div>
      </div>

      <!-- 视频项 2 -->
      <div class="video-card">
          <!-- "img/poster2.PNG"需要替换为开发者需要的图片资源文件 -->
          <img src="img/poster2.PNG" alt="视频封面" class="video-thumbnail">
          <div class="video-text"> 视频2</div>
      </div>
  </div>

  <script>
      function newPage() {
          // 跳转到新页面
          window.location.href = "./index_cn.html";
      }
  </script>

  </body>
  </html>
  ```

  src/main/resources/rawfile/index\_cn.html：

  ```ts
  <!DOCTYPE html>
  <html lang="en">

  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>测试页面</title>
      <style>
          * {
              padding: 0;
              margin: 0;
          }

          body {
              width: 100vw;
              height: 100vh;
              box-sizing: border-box;
          }

          .page {
              display: flex;
              flex-direction: column;
              justify-content: flex-start;
              align-items: flex-start;
              width: 100%;
              height: 100%;
              box-sizing: border-box;
          }

          .video-box {
              width: 100%;
              display: flex;
              flex-direction: column;
              justify-content: start;
              align-items: center;
              box-sizing: border-box;
              margin-top: 20px;
          }

          .myVideo {
              width: 100%;
              height: calc(100vw * 9 / 16);
              object-fit: contain;
              background-color: black;
          }
      </style>
  </head>

  <body>
  <div class="page">
      <h1 style="margin-left: 100px;margin-top: 20px">网页视频显示</h1>
      <div class="video-box">
          <video autoplay muted loop class="myVideo" controls>
              <!-- "www.example.mp4"需要替换为开发者需要的视频资源文件 -->
              <source src="www.example.mp4" type="video/mp4">
          </video>
      </div>

      <div style="margin-top: 40px; margin-left: 20px">
          <h2>视频简介</h2>
          <div style="margin-top: 10px">
              该网页视频为示例视频
          </div>
      </div>
  </div>

  </body>

  </html>
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/5uxF_pEQRmem0_EZQ4MxjQ/zh-cn_image_0000002628762568.png "点击放大")
* 方案二：跳转后的Web组件不设置透明度渐变的过渡效果。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct SolutionTwo {
    controller: webview.WebviewController = new webview.WebviewController();
    @State isShowNewWeb: boolean = false;

    build() {
      Stack() {
        Column() {
          Web({ src: $rawfile('VideoList.html'), controller: this.controller })
            .height('100%')
            .width('100%')
            .fileAccess(true)
            .geolocationAccess(false)
            .onLoadIntercept((event) => {
              console.info('url:' + event.data.getRequestUrl());
              if (event.data.getRequestUrl() === 'resource://rawfile/index_cn.html') {
                this.isShowNewWeb = true;
                return true; // 拦截此次跳转
              } else {
                return false; // 允许跳转
              }
            });
        };

        if (this.isShowNewWeb) {
          Web({ src: $rawfile('index_cn.html'), controller: this.controller })
            .height('100%')
            .width('100%')
            .fileAccess(true)
            .geolocationAccess(false)
          // 不设置透明度由浅到深的转场效果
        }
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  src/main/resources/rawfile/VideoList.html：

  ```ts
  <!DOCTYPE html>
  <html lang="zh">
  <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <title>视频列表</title>
      <style>
          body {
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
            color: #333;
          }

          /* 视频列表容器 */
          .video-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)));
            gap: 20px;
            max-width: 1400px;
            margin: 0 auto;
          }

          /* 视频卡片 */
          .video-card {
            display: flex;           /* 启用 Flexbox */
            background-color: #f1f3f5;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
          }

          .video-text {
            text-align: center;
            width: 100px;
            margin-top: 40px;
          }

          .video-thumbnail {
            width: 150px;
            height: 100px;
            object-fit: contain;
            display: block;
            margin-left: 10px;
          }

      </style>
  </head>
  <body>

  <h1 style="font-size: 16px;">视频列表</h1>

  <div class="video-list">
      <!-- 视频项 1 -->
      <div class="video-card" onclick="newPage()">
          <!-- "img/poster1.PNG"需要替换为开发者需要的图片资源文件 -->
          <img src="img/poster1.PNG" alt="视频封面" class="video-thumbnail">
          <div class="video-text"> 视频1</div>
      </div>

      <!-- 视频项 2 -->
      <div class="video-card">
          <!-- "img/poster2.PNG"需要替换为开发者需要的图片资源文件 -->
          <img src="img/poster2.PNG" alt="视频封面" class="video-thumbnail">
          <div class="video-text"> 视频2</div>
      </div>
  </div>

  <script>
      function newPage() {
          // 跳转到新页面
          window.location.href = "./index_cn.html";
      }
  </script>

  </body>
  </html>
  ```

  src/main/resources/rawfile/index\_cn.html：

  ```ts
  <!DOCTYPE html>
  <html lang="en">

  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>测试页面</title>
      <style>
          * {
              padding: 0;
              margin: 0;
          }

          body {
              width: 100vw;
              height: 100vh;
              box-sizing: border-box;
          }

          .page {
              display: flex;
              flex-direction: column;
              justify-content: flex-start;
              align-items: flex-start;
              width: 100%;
              height: 100%;
              box-sizing: border-box;
          }

          .video-box {
              width: 100%;
              display: flex;
              flex-direction: column;
              justify-content: start;
              align-items: center;
              box-sizing: border-box;
              margin-top: 20px;
          }

          .myVideo {
              width: 100%;
              height: calc(100vw * 9 / 16);
              object-fit: contain;
              background-color: black;
          }
      </style>
  </head>

  <body>
  <div class="page">
      <h1 style="margin-left: 100px;margin-top: 20px">网页视频显示</h1>
      <div class="video-box">
          <video autoplay muted loop class="myVideo" controls>
              <!-- "www.example.mp4"需要替换为开发者需要的视频资源文件 -->
              <source src="www.example.mp4" type="video/mp4">
          </video>
      </div>

      <div style="margin-top: 40px; margin-left: 20px">
          <h2>视频简介</h2>
          <div style="margin-top: 10px">
              该网页视频为示例视频
          </div>
      </div>
  </div>

  </body>

  </html>
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/GWQrGvIzRwGcRwyfDktZFw/zh-cn_image_0000002658961881.png "点击放大")
