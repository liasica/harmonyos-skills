---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-19
title: 如何将码图背景颜色设置成透明色
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 如何将码图背景颜色设置成透明色
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0b93a3cfcff2a01ad7f24bec56d567b8432d9917e54c0d8e73d1993ed2d8ef93
---

**问题现象**

当前码图生成不支持设置背景颜色为透明色。

**解决措施**

通过图片处理将码图的背景颜色转换为透明色。

示例代码（仅供参考）：

```typescript
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

/**
 * 通过传入createBarcode生成的PixelMap对象及其背景色，获取透明背景色的PixelMap对象
 *
 * @param {image.PixelMap} originalPixelMap - createBarcode生成的PixelMap对象。
 * @param {number} backgroundColor - CreateOptions设置的十六进制背景色。
 * @returns {Promise<image.PixelMap | undefined>} 成功返回新的PixelMap对象，失败则返回undefined。
 */
export async function convertBackgroundColorToTransparent(originalPixelMap: image.PixelMap,
  backgroundColor: number): Promise<image.PixelMap | undefined> {
  try {
    // 获取图像信息
    const imageInfo: image.ImageInfo = await originalPixelMap.getImageInfo();

    // 创建缓冲区以存储像素数据
    const buffer: ArrayBuffer = new ArrayBuffer(originalPixelMap.getPixelBytesNumber());

    // 将像素数据读取到缓冲区
    originalPixelMap.readPixelsToBufferSync(buffer);

    // 初始化新像素图的选项
    const options: image.InitializationOptions = {
      editable: true,
      srcPixelFormat: imageInfo.pixelFormat,
      pixelFormat: imageInfo.pixelFormat,
      size: imageInfo.size
    };

    // 创建新的可编辑PixelMap对象
    let newPixelMap: image.PixelMap = image.createPixelMapSync(buffer, options);

    // 定义码图图片数据区域
    const area: image.PositionArea = {
      pixels: new ArrayBuffer(imageInfo.size.height * imageInfo.size.width * 4), // 像素数据缓冲区
      offset: 0, // 偏移量
      stride: imageInfo.stride, // 间距
      region: { size: { height: imageInfo.size.height, width: imageInfo.size.width }, x: 0, y: 0 } // 区域
    };

    // 将区域数据转换为 Uint8Array
    let areaUint8Array: Uint8Array = new Uint8Array(area.pixels);
    let originalPixelMapUint8Array: Uint8Array = new Uint8Array(buffer);

    // 从backgroundColor中提取红、绿、蓝通道的值
    const redBg: number = (backgroundColor >> 16) & 0xFF;
    const greenBg: number = (backgroundColor >> 8) & 0xFF;
    const blueBg: number = backgroundColor & 0xFF;

    // 遍历像素
    for (let i = 0; i < originalPixelMapUint8Array.length; i += 4) {
      const red: number = originalPixelMapUint8Array[i];
      const green: number = originalPixelMapUint8Array[i + 1];
      const blue: number = originalPixelMapUint8Array[i + 2];

      // 直接复制红绿蓝通道
      areaUint8Array[i] = red;
      areaUint8Array[i + 1] = green;
      areaUint8Array[i + 2] = blue;

      // 检查像素是否为背景色
      if (red === redBg && green === greenBg && blue === blueBg) {
        areaUint8Array[i + 3] = 0; // 设置透明色
      } else {
        areaUint8Array[i + 3] = originalPixelMapUint8Array[i + 3]; // 保留原透明度
      }
    }

    // 写入新像素数据
    await newPixelMap.writePixels(area);

    // 返回新的PixelMap对象
    return newPixelMap;
  } catch (err) {
    hilog.error(0x0001, 'CreateBarcode', `Failed to convertBackgroundColorToTransparent. Code: ${err.code}.`);
    return undefined;
  }
}
```
