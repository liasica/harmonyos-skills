---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-9
title: 如何将app.media.app_icon，转换为PixelMap
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何将app.media.app_icon，转换为PixelMap
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:894124ac5770cd6d6656b138783eb9aefffab3561c9c7d4d18f4d849b46e054d
---

使用getMediaContent获取媒体文件内容。使用createPixelMap创建PixelMap。

参考代码如下：

```
1. import { image } from '@kit.ImageKit';

3. @Entry
4. @Component
5. struct Index {
6. @State pixelMap: PixelMap | null = null;

8. convert() {
9. try {
10. // Byte array of media files
11. this.getUIContext().getHostContext()!.resourceManager.getMediaContent($r('app.media.startIcon').id,
12. (error: BusinessError, value: Uint8Array) => {
13. if (error) {
14. console.error(`getMediaContent failed: ${error.code}, ${error.message}`);
15. return;
16. }
17. let pixelMapInitOptions: image.InitializationOptions = {
18. editable: true,
19. pixelFormat: 3,
20. size: { height: 4, width: 6 }
21. };
22. // Create an imageSource instance
23. let imageSource = image.createImageSource(value.buffer);
24. // Decoding to generate PixelMap
25. imageSource.createPixelMap(pixelMapInitOptions).then((pixelMap) => {
26. this.pixelMap = pixelMap;
27. // Pixel operations or rendering can be performed here.
28. }).catch((decodeError: BusinessError) => {
29. console.error(`Decode failed: ${decodeError.code}, ${decodeError.message}`);
30. });
31. });
32. } catch (error) {
33. console.error(`Global error: ${error.code}, ${error.message}`);
34. }
35. }

38. build() {
39. Column() {
40. Button('Click to convert')
41. .onClick(() => {
42. this.convert();
43. })
44. .margin({ bottom: 16 })
45. Image(this.pixelMap)
46. }
47. .padding(16)
48. }
49. }
```

[ConvertAppIconToPixelMap.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/ConvertAppIconToPixelMap.ets#L21-L69)

**参考链接**

[getMediaContent](../harmonyos-references/js-apis-resource-manager.md#getmediacontent9)

[image.createPixelMap](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmap8)
