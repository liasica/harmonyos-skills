---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-processing-arkts
title: 使用VideoProcessingEngine完成图片超分
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片编辑和处理 > 使用VideoProcessingEngine完成图片超分
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef7c49cfaf017318f958dc57de8655a32706ef9390637ab81f7e7693c91e5689
---

本模块提供图片细节增强的[ArkTS接口](../harmonyos-references/js-apis-videoprocessingengine.md)，通过调用本模块，可以实现图片内容的清晰度增强及缩放功能，处理后的数据可以用于送显和输出。

典型应用场景如：从URL获取图片源 > 图片细节增强 > 显示。

## 约束与限制

1. 当前仅支持处理同时满足以下条件的图片：

   * 图片为SDR（Standard dynamic range）图片。
   * 图片的像素格式为RGBA、BGRA、NV12、NV21，输出格式与输入格式一致。
   * 处理的PixelMap对象需为[DMA内存](image-allocator-type.md#内存类型介绍)。
2. 本模块提供4个质量档位的算法，处理效果逐渐变优，但性能也会逐渐下降。

   | 质量档位 | 输入分辨率要求  （单位：像素） | 输出分辨率要求  （单位：像素） | 说明 |
   | --- | --- | --- | --- |
   | NONE | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例，无清晰度增强效果。 |
   | LOW | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例。  缩放时会对图像进行低质量的清晰度增强，处理效率较高。  此质量档位为默认设置。 |
   | MEDIUM | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例。  缩放时会对图像进行中等质量的清晰度增强，处理效率适中。 |
   | HIGH | 宽：[512,2000]  高：[512,2000] | 宽：[512,2000]  高：[512,2000] | 适用于缩放及清晰度增强场景，支持改变宽高比例。  缩放时会对图像进行高质量的清晰度增强，处理效率相对较低。 |

## 开发步骤

1. 添加引用文件。

   ```
   1. import { image, videoProcessingEngine } from '@kit.ImageKit';
   ```
2. 初始化环境。

   ```
   1. let promise: Promise<void> = videoProcessingEngine.initializeEnvironment();
   ```
3. （可选）配置输入。

   ```
   1. let scale: number = 0.5;
   2. let width: number = 512; // 示例代码，配置宽为512。
   3. let height: number = 512;// 示例代码，配置高为512。
   4. const color: ArrayBuffer = new ArrayBuffer(width * height * 4); // width * height * 4为需要创建的像素buffer大小。
   5. let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height, width } }
   6. let sourceImage : image.PixelMap = image.createPixelMapSync(color, opts);
   7. let level : videoProcessingEngine.QualityLevel = videoProcessingEngine.QualityLevel.LOW;
   ```
4. 创建图像处理模块。

   预期返回值：videoProcessingEngine.ImageProcessor，图片处理模块实例。

   ```
   1. // 创建图片细节增强模块实例
   2. let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
   ```
5. 启动细节增强处理。当输入图片srcImage和输出图片dstImage分辨率不一致时，进行缩放。

   示例中的变量说明如下：

   sourceImage：PixelMap类型的输入图像，必填。

   width：目标宽度（单位px），当没有配置目标缩放比例时必填。

   height：目标高度（单位px），当没有配置目标缩放比例时必填。

   scale：目标缩放比例，当没有配置目标分辨率时必填。目标分辨率即宽\*高。

   level：[质量算法档位](image-processing-arkts.md#约束与限制)，默认为LOW。

   * 方式一：指定原图、目标分辨率。

     ```
     1. // 同步方法
     2. let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
     3. sourceImage, width, height, level);
     ```

     ```
     1. // 异步方法
     2. let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(sourceImage, width, height, level);
     ```
   * 方式二：指定原图、缩放比例。

     ```
     1. // 同步方法
     2. let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
     3. sourceImage, scale, level);
     ```

     ```
     1. // 异步方法
     2. let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(
     3. sourceImage, scale, level);
     ```
6. 释放处理资源。

   ```
   1. videoProcessingEngine.deinitializeEnvironment();
   ```
