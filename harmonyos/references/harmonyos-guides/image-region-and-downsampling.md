---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-region-and-downsampling
title: 图片区域解码与下采样(ArkTS)
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(ArkTS) > 图片解码 > 图片区域解码与下采样(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6a2e0667391d96289e627dc404f11be4c8bff7c9e2d34fe889d84201d2852885
---

应用在处理大尺寸图片时，直接解码整张图片可能导致内存占用过高和解码耗时较长。通过区域解码和下采样解码功能，可以有效优化这一场景：

* **区域解码**：仅解码图片的指定矩形区域，适用于需要查看图片局部的场景。
* **下采样解码**：按期望尺寸解码图片，解码器自动选择最优采样率，适用于大图预览场景。

**适用场景**：

| 场景 | 推荐方式 | 说明 |
| --- | --- | --- |
| 图片局部放大查看 | 区域解码 | 只解码需要查看的区域。 |
| 大图预览（如4K图片在手机屏幕显示） | 下采样解码 | 降低分辨率，减少内存占用。 |
| 地图/全景图瓦片加载 | 组合使用 | 指定区域并指定输出尺寸。 |

## 区域解码

区域解码通过设置解码参数desiredRegion，指定需要解码的矩形区域。解码器仅解码该区域的数据。参数详情请参考[Region](../harmonyos-references/arkts-apis-image-i.md#region8)。

### 开发步骤

1. 参考[使用ImageSource完成图片解码](image-decoding.md)创建ImageSource实例。
2. 设置desiredRegion参数执行区域解码。

   ```typescript
   async DecodeRegion(imageSource: image.ImageSource): Promise<image.PixelMap | undefined> {
     let decodingOptions: image.DecodingOptions = {
       desiredRegion: {
         size: { width: 1000, height: 1000 },
         x: 0,
         y: 0
       }
     };

     try {
       let pixelMap = await imageSource.createPixelMap(decodingOptions);
       console.info('Succeeded in decoding region.');
       return pixelMap;
     } catch (error) {
       console.error(`Failed to decode region: ${error}.`);
       return undefined;
     }
   }
   ```

### 使用限制

* 区域坐标和大小必须在原图范围内。
* 区域大小必须为正整数。

## 下采样解码

下采样解码通过设置解码参数desiredSize，指定期望输出的图片尺寸。解码器会根据期望尺寸输出PixelMap，减少最终的内存占用。

**解码处理差异**：

* **JPEG、PNG、HEIF格式**：解码过程中采用下采样策略，按最优采样率解码，解码效率更高。
* **其他格式**：先完整解码原图，再缩放至期望尺寸。

参数详情请参考[DecodingOptions](../harmonyos-references/arkts-apis-image-i.md#decodingoptions7)。

### 开发步骤

1. 参考[使用ImageSource完成图片解码](image-decoding.md)创建ImageSource实例。
2. 设置desiredSize参数执行下采样解码。

   ```typescript
   async DownsampleDecode(imageSource: image.ImageSource): Promise<image.PixelMap | undefined> {
     let decodingOptions: image.DecodingOptions = {
       desiredSize: { width: 512, height: 512 }
     };

     try {
       let pixelMap = await imageSource.createPixelMap(decodingOptions);
       console.info('Succeeded in downsample decoding.');
       return pixelMap;
     } catch (error) {
       console.error(`Failed to downsample decode: ${error}.`);
       return undefined;
     }
   }
   ```

## 区域解码与下采样组合使用

当同时设置desiredRegion和desiredSize时，需要通过cropAndScaleStrategy参数指定裁剪与缩放的先后顺序。

### cropAndScaleStrategy策略

| 策略 | 常量值 | 操作顺序 | 说明 |
| --- | --- | --- | --- |
| SCALE\_FIRST | 1 | 先缩放，再裁剪。 | - |
| CROP\_FIRST | 2 | 先裁剪，再缩放。 | 推荐使用，可减少解码峰值内存。 |

**推荐使用CROP\_FIRST**：先裁剪再缩放可精确控制裁剪区域，保证不同格式解码效果一致。

参数详情请参考[CropAndScaleStrategy](../harmonyos-references/arkts-apis-image-e.md#cropandscalestrategy18)。

### 开发步骤

1. 参考[使用ImageSource完成图片解码](image-decoding.md)创建ImageSource实例。
2. 同时设置desiredRegion、desiredSize和cropAndScaleStrategy参数。

   ```typescript
   async CombinedDecode(imageSource: image.ImageSource): Promise<image.PixelMap | undefined> {
     let decodingOptions: image.DecodingOptions = {
       desiredRegion: {
         size: { width: 2000, height: 2000 },
         x: 1000,
         y: 500
       },
       desiredSize: { width: 512, height: 512 },
       cropAndScaleStrategy: image.CropAndScaleStrategy.CROP_FIRST
     };

     try {
       let pixelMap = await imageSource.createPixelMap(decodingOptions);
       console.info('Succeeded in combined decoding.');
       return pixelMap;
     } catch (error) {
       console.error(`Failed to combined decode: ${error}.`);
       return undefined;
     }
   }
   ```

## 注意事项

* 同时设置desiredRegion和desiredSize时，建议设置cropAndScaleStrategy为CROP\_FIRST，以保证解码效果一致。
* 对于原始像素内存超过2GB的图片，建议使用下采样解码避免内存溢出。
