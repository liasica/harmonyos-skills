---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-17
title: 将pixelFormat设置为nv21或者nv12时抛出错误码62980096怎么处理
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 将pixelFormat设置为nv21或者nv12时抛出错误码62980096怎么处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f09e47b5355e0f83322eaa2496321b7fe6b4ac86198c0fda822681ab2eab5901
---

**问题详情：**

调用createPixelMap方法时，如果将pixelFormat设置为nv21或nv12，可能会遇到错误代码62980096。建议检查以下几点：

确认pixelFormat参数值是否正确。

检查createPixelMap方法的其他参数是否符合要求。

确认系统环境是否支持nv21和nv12格式。

如果问题仍然存在，请参考官方文档或联系技术支持获取进一步帮助。

**解决措施：**

pixelFormat枚举目前用于ImageSource。因此，如果要创建PixelMap，NV21或NV12格式的图片需要通过以下方式：

1. 使用createImageSource方法创建ImageSource。

   设置createImageSource的sourceOption参数时，sourcePixelFormat参数值8对应NV21格式，9对应NV12格式。sourceSize参数需设置为原始YUV图片的宽高，且宽度值必须为偶数。
2. 使用ImageSource的createPixelMap接口创建PixelMap。

具体代码如下：

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'NV21AndNV12ToPixelMap';
7. @State private pixelMap: PixelMap | null = null;
8. @State private pixelMap2: PixelMap | null = null;

10. build() {
11. Row() {
12. Column() {
13. Image(this.pixelMap)
14. .width(200).height(200).margin(15)
15. Text(this.message)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .onClick(async () => {
19. let resourceManager = this.getUIContext().getHostContext()!.resourceManager
20. let imageArray = await resourceManager.getMediaContent($r("app.media.sample14_NV21_fromJPG_510X510"));
21. let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer;
22. // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
23. let sourceOptions: image.SourceOptions =
24. { sourceDensity: 120, sourcePixelFormat: 8, sourceSize: { width: 510, height: 510 } };
25. let imageResource = image.createImageSource(pixelBuffer, sourceOptions);
26. let opts: image.DecodingOptions = { editable: true }
27. this.pixelMap = await imageResource.createPixelMap(opts);

29. let imageArray2 = await resourceManager.getMediaContent($r('app.media.sample10_NV12_fromJPG_510X510'));
30. let pixelBuffer2 = new Uint8Array(imageArray2).buffer as Object as ArrayBuffer;
31. // The value 8 of the sourcePixelFormat parameter corresponds to NV21 format, and 9 corresponds to NV12 format; The sourceSize parameter needs to set the width and height (the width and height data of the original yuv image), and the width value cannot be odd.
32. let sourceOptions2: image.SourceOptions =
33. { sourceDensity: 120, sourcePixelFormat: 9, sourceSize: { width: 510, height: 510 } };
34. let imageResource2 = image.createImageSource(pixelBuffer2, sourceOptions2);
35. let opts2: image.DecodingOptions = { editable: true }
36. this.pixelMap2 = await imageResource2.createPixelMap(opts2);
37. })
38. Image(this.pixelMap2)
39. .width(200).height(200).margin(15)
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }
45. }
```

[PixelFormat.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/PixelFormat.ets#L21-L65)
