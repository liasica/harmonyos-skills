---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-23
title: 如何生成带logo的二维码
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何生成带logo的二维码
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:33+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:9baf9677bb71be2eb48b379fa10ea11469a24d2cbcf4acf6e3216a21dd5144bf
---

1. 使用Canvas组件绘制二维码图片和logo图片。

   ```
   1. Canvas(this.context)
   2. .width(300)
   3. .height(300)
   4. .onReady(() => {
   5. this.createQRCode();
   6. })
   ```

   [GenerateQrCode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/GenerateQrCode.ets#L67-L72)
2. 首先调用createBarcode接口生成码图pixelMap，再调用drawImage接口绘制码图pixelMap，最后再次调用drawImage接口绘制logo叠加到码图之上。

   ```
   1. let options: generateBarcode.CreateOptions = {
   2. scanType: scanCore.ScanType.QR_CODE,
   3. height: this.QRCodeWidth,
   4. width: this.QRCodeWidth
   5. };
   6. generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
   7. this.pixelMap = pixelMap;
   8. this.context.drawImage(this.pixelMap, 0, 0, 300, 300, 0, 0, 300, 300);
   9. this.context.drawImage(this.img, 0, 0, 80, 80, 110, 110, 80, 80);
   10. }).catch((error: BusinessError) => {
   11. hilog.error(0x0001, '[generateBarcode]', 'promise error : %{public}s', JSON.stringify(error));
   12. })
   ```

   [GenerateQrCode.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/GenerateQrCode.ets#L49-L60)

示例代码中，image类型为PixelMap。在API version 18前，默认单位为px；在API version 18及以后，默认单位为vp。

API version 18之前的示例代码如下：

```
1. import { image } from '@kit.ImageKit';
2. import { generateBarcode, scanCore } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Entry
7. @Component
8. struct Index {
9. @State pixelMap: image.PixelMap | undefined = undefined;
10. private setting: RenderingContextSettings = new RenderingContextSettings(true);
11. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.setting);
12. private img: ImageBitmap = new ImageBitmap('common/startIcon.png');
13. private QRCodeWidth: number = 300;
14. private QRCodeHeight: number = 300;

16. createQRCode() {
17. this.pixelMap = undefined;
18. let content: string = 'helloWorld';
19. let options: generateBarcode.CreateOptions = {
20. scanType: scanCore.ScanType.QR_CODE,
21. height: this.QRCodeHeight,
22. width: this.QRCodeWidth
23. };
24. generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
25. this.pixelMap = pixelMap;
26. this.context.drawImage(this.pixelMap, 0, 0, 300, 300, 0, 0, 300, 300);
27. this.context.drawImage(this.img, 0, 0, 80, 80, 110, 110, 80, 80);
28. }).catch((error: BusinessError) => {
29. hilog.error(0x0001, '[generateBarcode]', 'promise error : %{public}s', JSON.stringify(error));
30. })
31. }

33. build() {
34. Column() {
35. Canvas(this.context)
36. .width(300)
37. .height(300)
38. .onReady(() => {
39. this.createQRCode();
40. })
41. }
42. .width('100%')
43. .height('100%')
44. .alignItems(HorizontalAlign.Start)
45. .justifyContent(FlexAlign.Start)
46. }
47. }
```

[GenerateQrCodeBeforeAPI18.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/GenerateQrCodeBeforeAPI18.ets#L21-L71)

API version 18及以后的示例代码如下：

```
1. import { image } from '@kit.ImageKit';
2. import { generateBarcode, scanCore } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Entry
7. @Component
8. struct Index {
9. @State pixelMap: image.PixelMap | undefined = undefined;
10. private setting: RenderingContextSettings = new RenderingContextSettings(true);
11. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.setting);
12. private img: ImageBitmap = new ImageBitmap('common/startIcon.png');
13. private QRCodeWidth: number = 300;
14. private QRCodeHeight: number = 300;

16. aboutToAppear(): void {
17. this.QRCodeWidth = this.getUIContext().vp2px(this.QRCodeWidth);
18. this.QRCodeHeight = this.getUIContext().vp2px(this.QRCodeHeight);
19. }

21. createQRCode() {
22. this.pixelMap = undefined;
23. let content: string = 'helloWorld';
24. let options: generateBarcode.CreateOptions = {
25. scanType: scanCore.ScanType.QR_CODE,
26. height: this.QRCodeHeight,
27. width: this.QRCodeWidth
28. };
29. generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
30. this.pixelMap = pixelMap;
31. this.context.drawImage(this.pixelMap, 0, 0, 300, 300, 0, 0, 300, 300);
32. this.context.drawImage(this.img, 0, 0, 80, 80, 110, 110, 80, 80);
33. }).catch((error: BusinessError) => {
34. hilog.error(0x0001, '[generateBarcode]', 'promise error : %{public}s', JSON.stringify(error));
35. })
36. }

38. build() {
39. Column() {
40. Canvas(this.context)
41. .width(300)
42. .height(300)
43. .onReady(() => {
44. this.createQRCode();
45. })
46. }
47. .width('100%')
48. .height('100%')
49. .alignItems(HorizontalAlign.Start)
50. .justifyContent(FlexAlign.Start)
51. }
52. }
```

[GenerateQrCodeAfterAPI18.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/MediaKit/entry/src/main/ets/pages/GenerateQrCodeAfterAPI18.ets#L21-L76)
