---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-7
title: 如何对相册图片进行编辑裁剪
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何对相册图片进行编辑裁剪
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d2a37114c947f0847e05d52cb723ee2cc0f2e79ce4fc1d9955bd141a368722b6
---

可以通过[图片处理](../harmonyos-references/js-apis-image.md)模块的[pixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)方法对图片进行编辑裁剪。

其中包括但不限于：

* [pixelMap.crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)方法，可以根据输入的尺寸对图片进行裁剪。
* [pixelMap.opacity](../harmonyos-references/arkts-apis-image-pixelmap.md#opacity9)方法，可以通过设置透明比率对图片设置透明效果。
* [pixelMap.scale](../harmonyos-references/arkts-apis-image-pixelmap.md#scale9)方法，可以根据输入的宽高对图片进行缩放。
* [pixelMap.rotate](../harmonyos-references/arkts-apis-image-pixelmap.md#rotate9)方法，可以根据输入的角度对图片进行旋转。
* [pixelMap.flip](../harmonyos-references/arkts-apis-image-pixelmap.md#flip9)方法，可以根据输入的条件对图片进行翻转。

以下示例代码为[pixelMap.crop](../harmonyos-references/arkts-apis-image-pixelmap.md#crop9)图片裁剪方法的使用：

```
1. // Crop 4:3
2. class RegionItem {
3. /**
4. * width coordinate.
5. */
6. x: number;

8. /**
9. * height coordinate.
10. */
11. y: number;

13. constructor(x: number, y: number) {
14. this.x = x;
15. this.y = y;
16. }
17. }

19. export async function cropCommon(pixelMap: PixelMap, cropWidth: number, cropHeight: number, cropPosition: RegionItem) {
20. pixelMap.crop({
21. size: {
22. width: cropWidth,
23. height: cropHeight
24. },
25. x: cropPosition.x,
26. y: cropPosition.y
27. });
28. }

30. // Pass in three parameters: image. PixelMap, image width, and image height. After obtaining the cropped image width and height,
31. // pass the parameters into the cropCommon method
32. export async function banner(pixelMap: PixelMap, width: number, height: number) {
33. if (width <= height) {
34. const cropWidth = width;
35. const cropHeight = Math.floor(width * 0.75);
36. const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
37. cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
38. return;
39. }
40. if (width * 0.75 >= height) {
41. const cropWidth = Math.floor(height / 0.75);
42. const cropHeight = height;
43. const cropPosition = new RegionItem(Math.floor((width - cropWidth) / 2), 0);
44. cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
45. return;
46. }
47. const cropWidth = width;
48. const cropHeight = Math.floor(width * 0.75);
49. const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
50. cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
51. }
```

[CropCommon.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/CropCommon.ets#L21-L71)
