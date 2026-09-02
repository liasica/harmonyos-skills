---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-15
title: 应用拍照时延长
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用拍照时延长
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:118ca63ee4ae71a7b530a07b3ad0ee2fe82d50052cd54db71d735bbeb5040caf
---

## 问题现象

拍照耗时较长，点击拍照等一会儿才会有拍照成功显示。

## 背景知识

相机拍照性能依赖算法处理的速度，而处理速度依赖算法的复杂度，算法复杂度越高，处理时间就越长。目前系统相机开发有两种相机拍照方案，分别是[相机分段式拍照](../harmonyos-guides/camera-deferred-capture.md)和[相机单段式拍照](../harmonyos-guides/camera-shooting.md)。

* 分段式拍照是系统相机开发的重要功能之一，即相机拍照可输出低质量图用作缩略图，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平。通过分段式拍照，优化了系统的拍照响应时延，从而提升用户体验。
* 单段式拍照是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，这样会导致Shot2See（从用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延比较长。
* 接口区别：
  + 单段式拍照使用了[on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)接口注册了高质量图的监听，默认不使用分段式拍照。
  + 分段式拍照指应用下发拍照任务后，系统会分多个阶段上报不同质量的图片。在第一阶段，系统快速上报低质量图，应用通过[on('photoAssetAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)接口会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。在第二阶段，分段式子服务会根据系统负载及定制场景进行动态调度，将后处理好的原图回传给媒体库，替换低质量图。
* 性能对比分析表：

  | **拍照实现方式** | **耗时(不同设备和场景有区别，数据仅供参考)** |
  | --- | --- |
  | 单段式拍照 | 1900ms |
  | 分段式拍照 | 672.7ms |
* 性能分析方法：
  + 静态校验：在相机类应用中，单段式拍照场景下仅返回一张图片，将图片用作Shot2See后的缩略图则会导致Shot2See完成时延比较长。
  + 动态校验：应用侧拍照流程为应用设置拍照回调函数，用户点击拍照按钮时调用photoOutput类的[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture)方法执行拍照任务，任务完成后触发回调函数，在回调函数中获取图片处理并显示在用户界面上。

    执行拍照任务和图片资源生成的日志和Trace关键字如下，可以根据两者之间的时间来确认耗时。

    | 关键流程 | hilog日志关键字 | Trace关键字 |
    | --- | --- | --- |
    | 调用photoOutput类的capture方法 | Capture is called | PhotoOutputNapi::Capture或HStreamCapture::Capture |
    | 执行photoAvailable回调函数 | PhotoListener::OnBufferAvailable | PhotoListener::OnBufferAvailable |

## 问题定位

1. 首先确认拍照方式是单段式拍照还是分段式拍照，有以下几种方法：
   * hilog日志：

     在日志中搜photoAvailable|photoAssetAvailable来确定，打印photoAvailable表示为单段式拍照，photoAssetAvailable为分段式拍照。

     如无photoAvailable|photoAssetAvailable日志打印，则在日志中搜索PhotoListener::OnBufferAvailable|Capture is called确认拍照耗时，根据拍照耗时来推测拍照方式，如下图中多次拍照耗时在2~3s，根据上述性能耗时对比分析表，属于单段式拍照。

     ```txt
     08-25 10:17:27.790  5277  5278 I C02B00/com.example.myapplication/CAMERA: {OnBufferAvailable()-photo_output_napi.cpp:82} PhotoListener::OnBufferAvailable is called
     08-25 10:17:31.527  5277  5277 I C02B00/com.example.myapplication/CAMERA: {Capture()-photo_output_napi.cpp:1297} Capture is called
     08-25 10:17:34.396  5277  5764 I C02B00/com.example.myapplication/CAMERA: {OnBufferAvailable()-photo_output_napi.cpp:82} PhotoListener::OnBufferAvailable is called
     08-25 10:17:37.741  5277  5277 I C02B00/com.example.myapplication/CAMERA: {Capture()-photo_output_napi.cpp:1297} Capture is called
     08-25 10:17:40.540  5277  5278 I C02B00/com.example.myapplication/CAMERA: {OnBufferAvailable()-photo_output_napi.cpp:82} PhotoListener::OnBufferAvailable is called
     08-25 10:17:43.347  5277  5277 I C02B00/com.example.myapplication/CAMERA: {Capture()-photo_output_napi.cpp:1297} Capture is called
     ```
   * 查看代码：

     在代码中搜索photoAvailable和photoAssetAvailable，通过查看代码中监听photoAvailable还是photoAssetAvailable事件来确定。

     ```ts
     // 单段式拍照
     photoOutput.on('photoAvailable', (err: BusinessError, photo: camera.Photo) => {
     // 获取图像数据处理
     });

     // 分段式拍照
     photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
     // 获取图像数据处理
     });
     ```
   * Trace分析：

     在Trace中搜索PhotoOutputNapi::Capture或HStreamCapture::Capture、PhotoListener::OnBufferAvailable，查看两者间时间间隔，通过拍照耗时来确定拍照方式。

     从下图可以看出，单段式拍照方式耗时达到了3.3s。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/IHnS9vJYQfWCTuvuo40XZg/zh-cn_image_0000002628395116.png "点击放大")

     分段式拍照方式拍照耗时643ms。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/AWbbFs91R0WpOUtgklN5MA/zh-cn_image_0000002658914337.png "点击放大")
2. 如果是单段式拍照方式，在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，完成时延比较长，导致拍照慢，可更换成分段式拍照方式。
3. 如果是分段式拍照方式，拍照慢需要分析耗时集中在哪部分。

   首先使用[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具ArkUI Inspector抓取拍照加载过程的页面布局，确认加载动效使用的是什么组件，如下图中可看到加载动效使用的是LoadingProgress，以及组件ID。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/m7Whx50EQkGPnPtC_xnqgA/zh-cn_image_0000002658794385.png)

   然后使用[Frame分析](../harmonyos-guides/ide-insight-session-frame.md)工具抓取拍照整体阶段的Trace信息，根据PhotoOutputNapi::Capture或HStreamCapture::Capture、PhotoListener::OnBufferAvailable确定应用调用拍照接口到获取图像数据阶段的耗时，根据LoadingProgress组件首次绘制和最后一次绘制的Trace点（H:FrameNode[LoadingProgress][id:组件ID]::RenderTask）来确定应用处理图像数据的耗时。

   从下图中可看到整体耗时2.2s，耗时较多的是应用处理图像数据部分，达到1.6s。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/IRgKbjSXQsO5xHbE-gTkWQ/zh-cn_image_0000002628555020.png "点击放大")

## 分析结论

拍照耗时长的原因有：

* 采用了单段式拍照方式，在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，完成时延比较长。
* 采用了分段式拍照方式，但图像数据处理逻辑复杂，耗时较长。

## 修改建议

* 根据背景知识中的性能分析对照，将单段式拍照优化为[分段式拍照方式](../harmonyos-guides/camera-deferred-capture.md)可有效减少拍照时延。
* 对于已采取分段式拍照仍存在耗时的情况，可优化图像数据处理算法减少拍照时延。
