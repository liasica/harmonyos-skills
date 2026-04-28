---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-arkts
title: 图片绘制（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 图片绘制（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:75c9125ad060c746ae3f3030690754a37f6dc1d8c886b9e486d11a6bbb6fe104
---

位图是一种用于在内存中存储和表示图像的数据结构，它是一个未经过压缩的像素集合，而JPEG或PNG等格式的图片是压缩格式的，两者并不相同。如果需要将JPEG或PNG绘制到屏幕上，需要先解码成位图格式，具体可参考[图片处理服务（Image Kit）](image-overview.md)图片解码相关章节。

目前Drawing（ArkTS）中位图绘制需要依赖PixelMap，它可以用于读取或写入图像数据以及获取图像信息。详细的API介绍请参考[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

1. 创建PixelMap。

   有多个API接口可以创建PixelMap，下文以createPixelMapSync()为例。更多创建方式和接口请见[@ohos.multimedia.image (图片处理)](../harmonyos-references/arkts-apis-image.md)模块。

   ```
   1. // 图片宽高
   2. let width = 600;
   3. let height = 400;
   4. // 字节长度，RGBA_8888每个像素占4字节
   5. let byteLength = width * height * 4;
   6. const color: ArrayBuffer = new ArrayBuffer(byteLength);
   7. let bufferArr = new Uint8Array(color);
   8. for (let i = 0; i < bufferArr.length; i += 4) {
   9. // 遍历并编辑每个像素，从而形成红绿蓝相间的条纹
   10. bufferArr[i] = 0x00;
   11. bufferArr[i+1] = 0x00;
   12. bufferArr[i+2] = 0x00;
   13. bufferArr[i+3] = 0xFF;
   14. let n = Math.floor(i / 80) % 3;
   15. if (n == 0) {
   16. bufferArr[i] = 0xFF;
   17. } else if (n == 1) {
   18. bufferArr[i+1] = 0xFF;
   19. } else {
   20. bufferArr[i+2] = 0xFF;
   21. }
   22. }
   23. // 设置像素属性
   24. let opts: image.InitializationOptions =
   25. { editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: height, width: width } };
   26. // 创建PixelMap
   27. pixelMap = image.createPixelMapSync(color, opts);
   ```

   [PixelMapDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/PixelMapDrawing.ets#L24-L52)
2. （可选）编辑PixelMap中的像素。如果没有编辑像素的需求，此步骤可以省略。

   有多个API接口可以编辑PixelMap中的像素，下文以writePixelsSync()为例。更多方式和接口的使用可见[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)。

   ```
   1. // 设置编辑区域的宽高
   2. let innerWidth = 400;
   3. let innerHeight = 200;
   4. // 编辑区域的字节长度，RGBA_8888每个像素占4字节
   5. let innerByteLength = innerWidth * innerHeight * 4;
   6. const innerColor: ArrayBuffer = new ArrayBuffer(innerByteLength);
   7. let innerBufferArr = new Uint8Array(innerColor);
   8. for (let i = 0; i < innerBufferArr.length; i += 4) {
   9. // 编辑区域的像素都设置为黑白相间条纹
   10. let n = Math.floor(i / 80) % 2;
   11. if (n == 0) {
   12. innerBufferArr[i] = 0x00;
   13. innerBufferArr[i+1] = 0x00;
   14. innerBufferArr[i+2] = 0x00;
   15. } else {
   16. innerBufferArr[i] = 0xFF;
   17. innerBufferArr[i+1] = 0xFF;
   18. innerBufferArr[i+2] = 0xFF;
   19. }
   20. innerBufferArr[i+3] = 0xFF;
   21. }
   22. // 设置编辑区域的像素、宽高、偏移量等
   23. const area: image.PositionArea = {
   24. pixels: innerColor,
   25. offset: 0,
   26. stride: innerWidth * 4,
   27. region: { size: { height: innerHeight, width: innerWidth }, x: 100, y: 100 }
   28. };
   29. // 编辑位图，形成中间的黑白相间条纹
   30. pixelMap.writePixelsSync(area);
   31. // 为了使图片完全显示，修改绘制起点参数为（0，0）
   32. canvas.drawImage(pixelMap, 0, 0);
   ```

   [PixelMapDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/PixelMapDrawing.ets#L60-L93)
3. 绘制PixelMap。

   绘制PixelMap时需要通过Canvas相关接口绘制位图，下文以drawImage()为例。更多方式和接口的使用请见[drawing.Canvas](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md)。

   drawImage()函数接受4个参数，第一个就是上文中创建的PixelMap，第二个是绘制图片位置的左上角x轴坐标，第三个是左上角y轴坐标，第四个为采样选项对象，默认为不使用任何参数构造的原始采样选项对象。

   ```
   1. // 为了使图片完全显示，修改绘制起点参数为（0，0）
   2. canvas.drawImage(pixelMap, 0, 0);
   ```

   [PixelMapDrawing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/ArkTSGraphicsDraw/entry/src/main/ets/drawing/pages/PixelMapDrawing.ets#L53-L56)

   绘制效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/otDRA7HqSYyPuvGTunl8gQ/zh-cn_image_0000002552799010.png?HW-CC-KV=V1&HW-CC-Date=20260427T234711Z&HW-CC-Expire=86400&HW-CC-Sign=A4E931F78CF6370B8255031CDF638BAA2334A8F1C8C41133B6E6980EF0F18389)

## 示例代码

* [图形绘制（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/ArkTSGraphicsDraw)
