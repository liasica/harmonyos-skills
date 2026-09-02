---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-17
title: 点击web页面分享按钮生成页面截图响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击web页面分享按钮生成页面截图响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0c33a961fbfbd51cd176d35807c92798a44aff29ba79c57d42f69e189894e4d4
---

## 问题现象

点击应用页面的分享按钮，等待一段时间之后才看见生成页面截图，响应慢。

## 背景知识

* [Web](../harmonyos-references/ts-basic-components-web.md)：具有在应用程序中显示Web页面内容的组件。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* [ArkWeb分析模板](../harmonyos-guides/ide-profiler-arkweb.md)是DevEco Profiler提供用于定位Web应用加载和丢帧问题的分析工具。

  Trace关键字说明：

  | 关键字 | 泳道 | 说明 |
  | --- | --- | --- |
  | DispatchTouchEvent xxx type=1 | 应用主线程 | 应用收到手指离开屏幕的事件 |
  | H:ProxyMain::BeginMainFrame | 应用包名:render | 开始一帧的渲染 |
  | H:EvaluateScript | 应用包名:render | js编译与执行 |
  | H:ResourceFetcher::requestResource | 应用包名:render | 子资源请求发起 |
  | SkiaOutputSurfaceImplOnGpu::SwapBuffers | CompositorGpuTh | Web页面渲染输出 |
  | H:Task Perform | OS\_TaskWorker | 执行taskpool.execute调用时设置的任务 |
  | H:Napi execute | - | 调用Napi接口函数 |
  | H:Napi complete | - | Napi接口函数执行完成，执行回调函数 |

## 问题定位

以点击某Web应用页面分享按钮生成页面截图响应慢为例，具体定位过程如下：

1. 使用ArkUI Inspector抓取显示页面截图的组件，发现该组件为Web，可知显示页面截图涉及到Web组件渲染输出。
2. 使用DevEco Studio的ArkWeb分析抓取该过程的Trace信息，以应用收到手指离开屏幕事件的Trace关键字作为问题分析的起点。由于非连续不稳定的vsync信号不一定导致界面上的渲染行为，取问题分析终点为渲染服务render\_service连续稳定渲染的第一帧vsync信号。可得到如下分析结果，从图中可知响应时间为2.2s左右。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/esrZc6v2Tbyv47dlSdHI0g/zh-cn_image_0000002628555028.png "点击放大")
3. 由于Web页面的渲染绘制是由应用的render主线程触发，因此查看连续稳定渲染之前应用render主线的Trace信息，从图中可看到js编译与执行的Trace关键字，而在此之前render线程长时间处于sleeping状态，推测该截图信息不是由Web端生成，而是在ArkTS端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/iR4qnw9uQQCUBNgK-N78BQ/zh-cn_image_0000002628395124.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/cDkhCAV6TKu-R2uefY5rog/zh-cn_image_0000002658914349.png "点击放大")
4. 由于Web网页显示内容会涉及到资源请求，在render线程的js编译与执行Trace关键字附近框选Trace信息，通过requestResource过滤，可看到应用有从沙箱目录中请求图片资源，查看设备目录下该图片资源，发现大小为6.9M。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/0_J0m4WoToupclSl-QTKcQ/zh-cn_image_0000002658794397.png "点击放大")

   点击render线程最左侧Running状态，通过WakeUp From Tid不断找唤醒线程，发现最终唤醒线程为应用主线程，可知render线程进行js编译与执行是由主线程触发的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/bAIq3IlZTieMpV1Hi9qy0A/zh-cn_image_0000002628555034.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/wyXXIRYpQKS8YhKMRV-J1A/zh-cn_image_0000002628395132.png "点击放大")
5. 找到上图红框中主线程最左侧的runnable状态，通过WakeUp From Tid发现主线程是由OS\_TaskWorker线程唤醒。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/57h1fsoqQKucvDcqOnSZvg/zh-cn_image_0000002658914355.png "点击放大")

   点击上图中跳转箭头找到OS\_TaskWorker线程，该线程有执行PackToFile完成后的回调函数，[PackToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11)表示将图片数据编码进文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/r4tLzMNHR5C5M7FRnw0Ovg/zh-cn_image_0000002658794403.png "点击放大")

   通过上图中H:Napi complete, name:PackToFile处左侧runnable状态找到执行PackToFile的线程，可看到PackToFile耗时1.28s左右，图片分辨率为3375x7825。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/S2BnNxOOQESenPCJ-hajlw/zh-cn_image_0000002628555040.png "点击放大")

   根据runnable状态查找执行PackToFile的线程的唤醒线程，发现唤醒线程为OS\_TaskWorker线程，同时线程有执行screenshot截图，耗时为673ms左右。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/NnEXk486TkSj6TyDJka0nQ/zh-cn_image_0000002628395138.png "点击放大")

   通过Running状态发现OS\_TaskWorker线程的唤醒线程为应用主线程，可知应用收到点击事件之后，会通过taskpool执行生成截图的任务，首先截图，然后将截图数据编码到文件，保存到沙箱目录，最后通知到Web侧执行js代码，请求沙箱中的图片资源并将图片显示在Web页面中，该过程耗时主要集中在截图和数据编码到文件部分。
6. 展开Callstack泳道，找到截图部分的调用栈，发现耗时较多为CoreCanvas::DrawImageRect，此处表示应用在Canvas画布上绘制图片。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/CU9NuQIETc69Bn8-kvHkfg/zh-cn_image_0000002658914361.png "点击放大")

   而图片编码处H:DoEncode部分，通过调用栈发现耗时主要集中在将图片编码进png格式文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/ErkIALdFTliID8qZl0M0Qg/zh-cn_image_0000002658794409.png "点击放大")

   截图、图片编码进png格式文件耗时较多是因为绘制、编码的图片分辨率较大，达到了3375x7825。

## 分析结论

应用在生成页面截图时，设置的图片分辨率较大，截图、数据编码到文件耗时较多，导致响应慢的问题。

## 修改建议

1. 减小生成的图片分辨率大小。
2. 增加加载动效，如下示例代码。

   ```ts
   import { taskpool } from '@kit.ArkTS';
   import { BusinessError } from '@ohos.base';

   @Concurrent
   async function generalScreenShot(): Promise<PixelMap | undefined> {
     let pixelMap : PixelMap | undefined = undefined;
     // 耗时操作模拟生成截图
     for (let i = 0; i < 100000; i++) {
       console.info(`number:${i}`);
     }
     return pixelMap;
   }

   @Entry
   @Component
   struct DemoPage {
     @State isLoading: boolean = false;

     build() {
       RelativeContainer() {
         Button('分享')
           .id("shareButton")
           .onClick(() => {
             this.isLoading = true;
             taskpool.execute(generalScreenShot).then(() => {
               this.isLoading = false;
               // 显示分享界面
             }).catch((error: BusinessError) => {
               console.error(`Failed to execute task: errCode is ${error.code}, errMessage is ${error.message}`);
             });
           })
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
         LoadingProgress()
           .color(Color.Blue)
           .width(50)
           .height(50)
           .visibility(this.isLoading ? Visibility.Visible : Visibility.None)
           .alignRules({
             top: { anchor: 'shareButton', align: VerticalAlign.Bottom },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
