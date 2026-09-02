---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-30
title: 应用内相机拍照后图片花屏
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用内相机拍照后图片花屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:bba1199751990dc109921f89766f21dc604d74954315fa26dc34e237c9428d21
---

## 问题现象

应用内启动相机拍照，预览界面图像正常，点击拍摄后展示的图片呈现花屏，从拍摄结果页返回后相机预览页重新点击拍照结果又是正常的。

## 背景知识

* [Camera Kit](../harmonyos-guides/camera-overview.md)：开发者通过调用Camera Kit(相机服务)提供的接口可以开发相机应用，应用通过访问和操作相机硬件，实现基础操作，如预览、拍照和录像；还可以通过接口组合完成更多操作，如控制闪光灯和曝光时间、对焦或调焦等。
* [双路预览](../harmonyos-guides/camera-dual-channel-preview.md)：应用通过Surface进行数据传递，通过ImageReceiver的Surface获取拍照流的数据、通过XComponent的Surface获取预览流的数据。如果要实现双路预览，即将拍照流改为预览流，将拍照流中的Surface改为预览流的Surface，通过ImageReceiver的Surface创建previewOutput，其余流程与拍照流和预览流一致。
* [Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)：相机配置信息项，包含输出格式及相机分辨率宽度和高度。
* [CameraFormat](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)：相机输出格式枚举。
* [image.createImageSource](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagesource9-3)：通过缓冲区创建ImageSource实例，支持设置图片属性，包括图片像素密度、像素格式和图片尺寸。
* [PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)：图片像素格式枚举。

## 问题定位

1. 第一次进入相机预览页后，日志全局搜索关键字“CreatePreviewOutputInstance”：从日志可以分析出首次进入相机预览页时，开启预览流的Profile格式为2002，即[YCRCB\_P010格式](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)。

   ```screen
   07-25 15:52:12.639   41696-41696   C02B01/com.hm.example/CAMERA  com.hm.example  I     {CreatePreviewOutputInstance():853} CameraManagerNapi::CreatePreviewOutputInstance ParseProfile size.width = 1920, size.height = 1440, format = 2002, surfaceId = 179082956374016
   ```
2. 拍照返回后重新进入相机预览页，日志全局搜索关键字“CreatePreviewOutputInstance”：从日志可以发现此时开启预览流的Profile格式为1003，即[YUV\_420\_SP](../harmonyos-references/arkts-apis-camera-e.md#cameraformat)格式。

   ```screen
   07-25 15:52:12.639   41696-41696   C02B01/com.hm.example/CAMERA  com.hm.example  I     {CreatePreviewOutputInstance():853} CameraManagerNapi::CreatePreviewOutputInstance ParseProfile size.width = 1920, size.height = 1440, format = 1003, surfaceId = 179082956374016
   ```
3. 排查应用拍照实现方案：日志搜索关键字“CreatePhotoOutputInstance”，未检索到相应日志，表明应用使用的相机能力未开启拍照流，因此应用拍照功能应该是基于双路预览实现的。继续搜索关键字“CreatePixelMapExtended”，有以下日志输出，说明当前应用使用的相机拍照能力是基于双路预览结合图片转换实现。

   ```screen
   07-25 20:54:14.227   41696-63370   C02B61/com.hm.example/ImageSource  com.hm.example  I     CreatePixelMapExtended success, imageId:1753448054204387, desiredSize: (0, 0), imageSize: (1920, 1440), desiredHdr: 1, hdrType : 1, memoryType : 4, cost 22771 us
   07-25 20:54:15.009   41696-63370   C02B61/com.hm.example/ImageSource  com.hm.example  I     CreatePixelMapExtended success, imageId:1753448055007373, desiredSize: (0, 0), imageSize: (288, 168), desiredHdr: 1, hdrType : 1, memoryType : 2, cost 1896 us
   07-25 20:54:15.022   41696-63846   C02B61/com.hm.example/ImageSource  com.hm.example  I     CreatePixelMapExtended success, imageId:1753448055005062, desiredSize: (0, 0), imageSize: (1440, 1920), desiredHdr: 1, hdrType : 1, memoryType : 4, cost 17130 us
   ```

## 分析结论

前后2次进入相机预览页时，相机预览流选取的Profile格式不一致，第一次选择的是2002（YCRCB\_P010格式），第二次选择的是1003（YUV\_420\_SP格式）。而最终拍照是使用双路预览结合图片转换实现，在图片转换时设置的格式固定为1003对应的[PixelMapFormat](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7).NV21，导致第一次图片转换异常。

## 修改建议

每次设置相机预览流时，固定选取相同格式的Profile，且在图片转换时设置图片格式与之相符，如2002对应image.PixelMapFormat的值为YCRCB\_P010，1003对应image.PixelMapFormat的值为NV21。

格式对照可参考下表：

| CameraFormat  枚举名称 | CameraFormat  枚举值 | PixelMapFormat  枚举名称 | PixelMapFormat  枚举值 | 说明 |
| --- | --- | --- | --- | --- |
| CAMERA\_FORMAT\_RGBA\_8888 | 3 | RGBA\_8888 | 3 | RGBA\_8888格式的图片 |
| CAMERA\_FORMAT\_YUV\_420\_SP | 1003 | NV21 | 8 | YUV\_420\_SP格式的图片，对应为NV21格式的图片。 |
| CAMERA\_FORMAT\_YCBCR\_P010 | 2001 | YCBCR\_P010 | 11 | YCBCR\_P010格式的图片。 |
| CAMERA\_FORMAT\_YCRCB\_P010 | 2002 | YCRCB\_P010 | 12 | YCRCB\_P010格式的图片。 |

## FAQ

Q：拍照与录制是否都可以选取CAMERA\_FORMAT\_YUV\_420\_SP格式的Profile？

A：CAMERA\_FORMAT\_YUV\_420\_SP格式针对拍照与录制的Profile过滤都适用，详情[自定义相机拍照](../harmonyos-guides/camera-shooting.md)示例代码、[自定义相机录像](../harmonyos-guides/camera-recording.md)。

Q：目前想要实现拍照与录制视频功能，遇到的问题主要是如何查找目标Profile，拍照和录制时需要2个目标Profile。

A：您可以直接参考官网示例代码[实现自定义相机功能-拍照](https://gitee.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/PhotoManager.ets)以及[实现自定义相机功能-录制](https://gitee.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/VideoManager.ets)，示例代码中对查找目标profile都有对应的实现。
