---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-generatearray
title: 通过字节数组生成码图
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 码图生成 > 通过字节数组生成码图
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:42+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2fa914eca0731cda82faf1f50e3022ea115c0fb1b5ce6db53c0ba982e980ce44
---

## 基本概念

码图生成能力支持将字节数组转换为自定义格式的码图。

## 场景介绍

码图生成能力支持将字节数组转换为自定义格式的码图。

例如：调用码图生成能力，将字节数组转换成交通一卡通二维码使用。

## 约束与限制

* 码图生成能力支持Phone、Tablet、Wearable、2in1、TV（从5.1.0(18)版本开始支持Wearable、从5.1.1(19)版本开始支持2in1、TV）。
* 若Scan Kit识别某码图内容显示内容为乱码，则该码图的字节数组需要通过专门的解码器解析，例如地铁闸机。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/toF2t2cBQ6C3Dtkz6lgkFg/zh-cn_image_0000002589324985.png?HW-CC-KV=V1&HW-CC-Date=20260429T053541Z&HW-CC-Expire=86400&HW-CC-Sign=0440AD45C8382B7AB286137814106656F38A788517471C7CCDE8123130E58345)

1. 用户向应用发起生成码图请求后，传入需要生成的码图信息，包括码图的类型、宽高等。
2. 应用通过调用Scan Kit的createBarcode接口启动码图生成能力。
3. Scan Kit通过将字节数组转换为码图并返回给应用。
4. 应用向用户返回生成码图结果。

## 接口说明

通过字节数组生成码图，以Promise形式生成码图。具体API说明详见[接口文档](../harmonyos-references/scan-generatebarcode.md)。

| 接口名 | 接口描述 |
| --- | --- |
| [createBarcode](../harmonyos-references/scan-generatebarcode.md#generatebarcodecreatebarcode-2)(content: ArrayBuffer, options: [CreateOptions](../harmonyos-references/scan-generatebarcode.md#createoptions)): Promise<image.[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 码图生成接口，返回生成的码图，类型为image.PixelMap，可以使用Image组件渲染成图片。使用Promise异步回调。 |

## 开发步骤

码图生成根据传参内容直接生成所需码图，需要传入固定参数和可选参数。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

以下示例为调用码图生成能力的createBarcode接口实现码图生成。

1. 导入码图生成接口模块，该模块提供了码图生成的参数和方法，导入方法如下。

   ```
   1. // 导入码图生成需要的图片模块、错误码模块
   2. import { scanCore, generateBarcode } from '@kit.ScanKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { image } from '@kit.ImageKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   6. import { buffer } from '@kit.ArkTS';
   ```
2. 调用码图生成能力的createBarcode接口实现码图生成。

   * 通过Promise方式回调，获取生成的码图。

     ```
     1. const TAG: string = 'Create barcode';

     3. @Entry
     4. @Component
     5. struct Index {
     6. @State pixelMap: image.PixelMap | undefined = undefined;

     8. build() {
     9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
     10. Button('generateBarcode Promise').onClick(() => {
     11. this.pixelMap = undefined;
     12. let content: string =
     13. '0177C10DD10F7768600202312110000063458FD14112345678FFFFD381012610b746365409210201b66636540ad0200020000000000110e617003201000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006645fbec664358ECF657CB40693c92da';
     14. let contentBuffer: ArrayBuffer = buffer.from(content, 'hex').buffer; // 将包含十六进制字符的字符串转换成ArrayBuffer
     15. let options: generateBarcode.CreateOptions = {
     16. scanType: scanCore.ScanType.QR_CODE,
     17. height: 400,
     18. width: 400
     19. };
     20. try {
     21. // 码图生成接口，成功返回PixelMap格式图片
     22. generateBarcode.createBarcode(contentBuffer, options).then((pixelMap: image.PixelMap) => {
     23. this.pixelMap = pixelMap;
     24. hilog.info(0x0001, TAG, 'Succeeded in creating barCode.');
     25. }).catch((err: BusinessError) => {
     26. hilog.error(0x0001, TAG, `Failed to createBarCode. Code: ${err.code}, message: ${err.message}`);
     27. });
     28. } catch (err) {
     29. hilog.error(0x0001, TAG,
     30. `Failed to createBarcode by Promise with options. Code: ${err.code}, message: ${err.message}`);
     31. }
     32. })
     33. // 获取生成码图后显示
     34. if (this.pixelMap) {
     35. Image(this.pixelMap).width(300).height(300).objectFit(ImageFit.Contain)
     36. }
     37. }
     38. .width('100%')
     39. .height('100%')
     40. }
     41. }
     ```

## 模拟器开发

暂不支持模拟器开发，调用接口会返回错误信息“Emulator is not supported.”
