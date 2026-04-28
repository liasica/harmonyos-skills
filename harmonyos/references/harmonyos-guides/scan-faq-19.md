---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-19
title: 如何将码图背景颜色设置成透明色
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 如何将码图背景颜色设置成透明色
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6cfa63eba275ee5fcaf9ee1099ad93a5a70cf3c7902e411c846fd1adaa2affb
---

**问题现象**

当前码图生成不支持设置背景颜色为透明色。

**解决措施**

通过图片处理将码图的背景颜色转换为透明色。

示例代码（仅供参考）：

```
1. import { image } from '@kit.ImageKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. /**
5. * 通过传入createBarcode生成的PixelMap对象及其背景色，获取透明背景色的PixelMap对象
6. *
7. * @param {image.PixelMap} originalPixelMap - createBarcode生成的PixelMap对象。
8. * @param {number} backgroundColor - CreateOptions设置的十六进制背景色。
9. * @returns {Promise<image.PixelMap | undefined>} 成功返回新的PixelMap对象，失败则返回undefined。
10. */
11. async function convertBackgroundColorToTransparent(originalPixelMap: image.PixelMap,
12. backgroundColor: number): Promise<image.PixelMap | undefined> {
13. try {
14. // 获取图像信息
15. const imageInfo: image.ImageInfo = await originalPixelMap.getImageInfo();

17. // 创建缓冲区以存储像素数据
18. const buffer: ArrayBuffer = new ArrayBuffer(originalPixelMap.getPixelBytesNumber());

20. // 将像素数据读取到缓冲区
21. originalPixelMap.readPixelsToBufferSync(buffer);

23. // 初始化新像素图的选项
24. const options: image.InitializationOptions = {
25. editable: true,
26. srcPixelFormat: imageInfo.pixelFormat,
27. pixelFormat: imageInfo.pixelFormat,
28. size: imageInfo.size
29. };

31. // 创建新的可编辑PixelMap对象
32. let newPixelMap: image.PixelMap = image.createPixelMapSync(buffer, options);

34. // 定义码图图片数据区域
35. const area: image.PositionArea = {
36. pixels: new ArrayBuffer(imageInfo.size.height * imageInfo.size.width * 4), // 像素数据缓冲区
37. offset: 0, // 偏移量
38. stride: imageInfo.stride, // 间距
39. region: { size: { height: imageInfo.size.height, width: imageInfo.size.width }, x: 0, y: 0 } // 区域
40. };

42. // 将区域数据转换为 Uint8Array
43. let areaUint8Array: Uint8Array = new Uint8Array(area.pixels);
44. let originalPixelMapUint8Array: Uint8Array = new Uint8Array(buffer);

46. // 从backgroundColor中提取红、绿、蓝通道的值
47. const redBg: number = (backgroundColor >> 16) & 0xFF;
48. const greenBg: number = (backgroundColor >> 8) & 0xFF;
49. const blueBg: number = backgroundColor & 0xFF;

51. // 遍历像素
52. for (let i = 0; i < originalPixelMapUint8Array.length; i += 4) {
53. const red: number = originalPixelMapUint8Array[i];
54. const green: number = originalPixelMapUint8Array[i + 1];
55. const blue: number = originalPixelMapUint8Array[i + 2];

57. // 检查像素是否为背景色
58. if (red === redBg && green === greenBg && blue === blueBg) {
59. areaUint8Array[i] = blue;
60. areaUint8Array[i  + 1] = green;
61. areaUint8Array[i + 2] = red;
62. areaUint8Array[i + 3] = 0; // 设置透明色
63. } else {
64. areaUint8Array[i] = blue;
65. areaUint8Array[i  + 1] = green;
66. areaUint8Array[i + 2] = red;
67. areaUint8Array[i + 3] = originalPixelMapUint8Array[i + 3]; // 保留原透明度
68. }
69. }

71. // 写入新像素数据
72. await newPixelMap.writePixels(area);

74. // 返回新的PixelMap对象
75. return newPixelMap;
76. } catch (err) {
77. hilog.error(0x0001, 'CreateBarcode', `Failed to convertBackgroundColorToTransparent. Code: ${err.code}.`);
78. return undefined;
79. }
80. }
```
