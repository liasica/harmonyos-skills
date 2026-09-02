---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-55
title: 组件宽高与Profile分辨率的关系
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 组件宽高与Profile分辨率的关系
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:72b0e29f7b0ef8d39d6240ad4f005d91d7248c6c5da89491a70300341b2934f0
---

## 问题现象

使用[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)接口获取到的Profile去创建相机流，有时会出现预览画面压缩或拉伸的情况，该如何解决？

## 背景知识

* [使用XComponentController管理Surface生命周期](../harmonyos-guides/napi-xcomponent-guidelines.md#管理xcomponent持有surface的生命周期)：本场景通过在ArkTS侧获取SurfaceId，布局信息、生命周期回调、触摸、鼠标、按键等事件回调等均在ArkTS侧触发，按需传递到Native侧进行处理。
* [setXComponentSurfaceRect](../harmonyos-references/ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)：设置XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。
* [CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)：相机输出能力项。

## 解决方案

1. 组件宽高：

   相机预览流送显的重要容器为Surface，Surface容器通过XComponent组件来创建，详细的创建过程可参考[相机预览开发步骤](../harmonyos-guides/camera-preview.md#开发步骤)中的第二步，这里不做赘述，本文仅讨论容器组件宽高与预览流分辨率宽高的关系。

   在相机预览流渲染这一开发场景下，我们可以将Surface和XComponent想象成两个矩形区域，XComponent组件区域就是前端页面上绘制并显示的区域，Surface区域是预览流渲染的区域。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/PWbLwYhJSVGye2JNTrwBjA/zh-cn_image_0000002628392588.png "点击放大")

   以上图为例，用户实际上能看到的XComponent区域的内容，因为Surface的范围超出了XComponent组件范围，所以预览流的帧画面中只有灰色部分的画面能被看到，而白色部分的画面将被裁切掉。

   通常情况下Surface区域与XComponent组件的区域默认是重合的，也就是说在默认情况下，预览流画面会铺满XComponent区域。这种默认情况可以通过以下两种方法改变：

   * 调用setXComponentSurfaceRect()重新定义Surface的宽高以及坐标。
   * 给XComponent组件设置border或padding等属性。
2. 分辨率宽高：

   应用通过getSupportedOutputCapability接口可以获取到当前设备支持的输出能力，previewProfiles数组为当前设备支持的预览能力，而其中[Profile.size](../harmonyos-references/arkts-apis-camera-i.md#size)即为分辨率宽高信息。

   这里分辨率的宽高指的是照片横纵两个方向上的像素数量，在分辨率宽高比不改变的情况下，分辨率的变化不影响画面视角范围，只影响画面清晰度。因为分辨率越高像素块越多，能表示的色彩也就越多，所以画面也就更加清晰。
3. 组件宽高与分辨率宽高的关系：

   如上所说，相机采集到的帧画面最终是送到Surface渲染，如果帧画面的分辨率宽高比与Surface宽高比不一致，那么帧画面在被渲染到Surface区域时，帧内的像素格无法保持其原本的显示比例而在某一个方向上出现“排列拥挤”，也就会使最终画面发生拉伸或压缩变形。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/bf1HWO5ZTWGVaaS-UxuPgg/zh-cn_image_0000002658791859.png "点击放大")

   以上图为例，假设原始帧画面是2\*3的像素排列，由于帧的宽高比和XComponent区域的宽高比相差较大，所以画面渲染到XComponent之后，每一个像素格都由原先“瘦长”的比例变成了“短胖”的比例，最终呈现出来的效果就是画面在纵向上的压缩变形。
4. 如何处理画面拉伸/压缩变形？

   基于前文所述画面拉伸/压缩变形的原理，为了处理这种变形，就必须让分辨率宽高比与Surface宽高比保持一致，具体的实现思路大致包括如下两种：

   * 调整XComponent组件的宽高比：

     因为Surface区域默认与XComponent组件区域重合，所以处理画面拉伸/压缩变形的最直接的办法就是根据所选Profile分辨率宽高比去设计XComponent组件的宽高。系统支持的分辨率因设备而异，但是基本上都能支持16:9、4:3、1:1这三个宽高比的分辨率，因此应用可以从这三个比例之中选取与自身业务最契合的宽高比，然后再根据既定的宽高比来筛选Profile以及设计XComponent组件的宽高。
   * 调整Surface区域的宽高比：

     如果业务的页面布局限制严格，无法调整XComponent组件宽高，且XComponent组件宽高比并不在16:9、4:3、1:1之中，则可以将XComponent区域与Surface区域解耦，然后使Surface区域的宽高比与分辨率宽高比保持一致，这样一来就可以防止预览画面产生形变。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/OZdC4ZsFSBKfMN0vL_yRzg/zh-cn_image_0000002628552480.png "点击放大")

     从上图可以看到，因为Surface的宽高比与帧画面的宽高比一致，所以在渲染时就不会产生拉伸/压缩变形，但是由于Surface的实际大小超过了XComponent组件的大小，因此在最终显示时阴影部分的画面将被裁剪掉。

     如果不希望预览画面被裁剪，也可以通过调整Surface宽高，使Surface区域包含在XComponent区域内，在这种情况下Surface未覆盖的部分将以黑色填充，如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/1ZzdPd_1QcqgvaVpg8rcyg/zh-cn_image_0000002658911801.png "点击放大")

     该思路的实现方案可以参考[自定义相机预览开发步骤](../harmonyos-guides/camera-preview.md#开发步骤)第3步中的setPreviewSize()方法，通过setXComponentSurfaceRect()设置Surface的宽高，将XComponent组件区域与Surface区域解耦，完整代码可参考[自定义相机预览示例代码](../harmonyos-guides/camera-preview.md#示例代码)。

## 常见FAQ

Q：是否可以直接用XComponent组件的宽高去筛选相同分辨率宽高的Profile？

A：不建议这么做。因为XComponent组件的宽高通常是自定义的，而不同的设备支持的分辨率宽高是不同的，如果根据XComponent组件宽高去筛选分辨率，则可能在某些设备上会出现找不到对应分辨率而无法初始化预览流的情况。因此只需要保持宽高比一致即可，而不建议两者宽高完全相同。

Q：如果分辨率宽高不影响画面大小，那为什么在将分辨率从1080\*1080切换到2560\*1440时画面视角范围会发生变化？

A：切换前后的分辨率宽高比不一致导致的。出图的时候系统会按照分辨率宽高比对原始图片进行裁剪，1080\*1080的宽高比是1:1，2560\*1440的宽高比是16:9，两者的裁剪系数是不一样的，因此最终画面视角范围不一致。

Q：使用XComponent渲染组件搭配Camera接口实现拍照功能时，页面拍照区域显示过小，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/0Ba6x9kxTROHV1C-pJtJug/zh-cn_image_0000002628392594.png "点击放大")

A：使用[ArkUI Inspector](../best-practices/bpta-optimization-overview.md#section1465143164111)工具查看可知，XComponent本身区域就很小，导致预览区域也小。另外从图中可以看到不只是预览区域范围小，图片的视角也很小（画面中只能看到键盘的一角），这种情况主要是因为Surface区域的大小远超XComponent组件的大小，导致最终渲染出来的画面只有Surface中的一小部分。
