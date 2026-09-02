---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-552
title: 平板或PC上，视频布局异常且播放时黑屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 平板或PC上，视频布局异常且播放时黑屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:868e3c9232c1265cd6d99ed91103e436021298541383b491ce96a4dea0f82bb4
---

## 问题现象

应用在平板或PC上，视频宽度没有占满整个屏幕且播放时出现黑屏无法播放。

## 背景知识

* [Web](../harmonyos-references/arkts-basic-components-web.md)：提供具有网页显示能力的Web组件。应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。
* [mixedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)：设定当安全源尝试从非安全源加载资源时的行为，默认值为MixedMode.None，即禁止安全源从非安全源加载内容。
* video：HTML5中用于嵌入视频内容的标签，支持自动播放、全屏、尺寸控制等属性。

## 问题定位

1. 使用[DevEco Testing](../harmonyos-guides/get-familiar.md)查看页面布局，发现视频是通过Web组件中的video标签展示。
2. 根据布局排查video组件的宽度，是否与设备屏幕宽度一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/iFWkPyIFRTyU8KiFMFk3Pw/zh-cn_image_0000002628551556.png "点击放大")
3. 播放视频时根据关键字“This request has been blocked”排查日志，发现应用在使用了HTTPS协议的Web页面加载了使用HTTP协议的视频。

   ```shell
   Mixed Content: The page at 'xxx' was loaded over HTTPS, but requested an insecure video 'xxx'. This request has been blocked; the content must be served over HTTPS.", source: xxx
   ```

## 分析结论

1. video组件的width设置错误，没有与设备屏幕宽度一致。
2. Web页面的协议和video资源路径的协议不一致，导致无法加载资源。

## 修改建议

1. 设置video组件的width属性为100%，使其宽度与屏幕宽度一致。核心示例代码如下：

   ```html
   <!DOCTYPE html>
   <html lang="zh-CN">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>视频异常</title>
   </head>
   <body>
   <div class="content">
       <video width="100%" controls>
           <!-- 替换为实际地址 -->
           <source src="example.mp4" type="video/mp4">
       </video>
   </div>
   </body>
   </html>
   ```
2. 将Web页面内所有资源文件路径的协议与Web页面的协议类型保持一致或者设置Web组件中的mixedMode属性使其允许加载HTTP和HTTPS混合内容，核心示例代码如下：

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   export struct WebVideoIndex {
     private controller: WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Web({ src: $rawfile('webVideo.html'), controller: this.controller })  // 加载本地html页面
           .width('100%')
           .mixedMode(MixedMode.All); // 设置Web组件中的mixedMode属性使其允许加载HTTP和HTTPS混合内容
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/FcNbdloRQCCQ1nbDU6A8LA/zh-cn_image_0000002628391676.png "点击放大")
