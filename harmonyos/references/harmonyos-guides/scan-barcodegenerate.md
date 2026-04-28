---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-barcodegenerate
title: 通过文本生成码图
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 码图生成 > 通过文本生成码图
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:109d21910b25b5e0477fcd6378c4cc7071ec9cd349f0a383dc2877574d96b144
---

## 基本概念

码图生成能力支持将字符串转换为自定义格式的码图。

## 场景介绍

码图生成能力支持将字符串转换为自定义格式的码图，包含条形码、二维码生成。

可以将字符串转成联系人码图，手机克隆码图，例如将"HUAWEI"字符串生成码图使用。

## 约束与限制

码图生成能力支持Phone、Tablet、Wearable、2in1、TV（从5.1.0(18)版本开始支持Wearable、从5.1.1(19)版本开始支持2in1、TV）。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/x1ETXrs1TpiUfVZ9VKnaYg/zh-cn_image_0000002583478615.png?HW-CC-KV=V1&HW-CC-Date=20260427T234641Z&HW-CC-Expire=86400&HW-CC-Sign=1DFC42EFA1E67F9BADFD8A67C6E5DA73A51BF4C1584BEEE7B9D625BFA225BCBB)

1. 用户向应用发起生成码图请求后，输入需要生成的码图信息，包括码图的类型、宽高等。
2. 应用通过调用Scan Kit的createBarcode接口启动码图生成能力。
3. Scan Kit通过将字符串转换为所需格式的码图并返回给应用。
4. 应用向用户返回生成码图结果。

## 接口说明

接口返回值有两种返回形式：Callback和Promise回调。下表中为码图生成能力的Callback和Promise形式接口，Callback和Promise只是返回值方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/scan-generatebarcode.md)。

| 接口名 | 接口描述 |
| --- | --- |
| [createBarcode](../harmonyos-references/scan-generatebarcode.md#generatebarcodecreatebarcode)(content: string, options: [CreateOptions](../harmonyos-references/scan-generatebarcode.md#createoptions)): Promise<image.[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | 码图生成接口，返回生成的码图，类型为image.PixelMap，可以使用Image组件渲染成图片。使用Promise异步回调。 |
| [createBarcode](../harmonyos-references/scan-generatebarcode.md#generatebarcodecreatebarcode-1)(content: string, options: CreateOptions, callback: AsyncCallback<image.PixelMap>): void | 码图生成接口，返回生成的码图，类型为image.PixelMap，可以使用Image组件渲染成图片。使用callback异步回调。 |

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
   ```
2. 调用码图生成能力的createBarcode接口实现码图生成。

   * 通过Promise方式回调，获取生成的码图。

     ```
     1. @Entry
     2. @Component
     3. struct Index {
     4. @State pixelMap: image.PixelMap | undefined = undefined

     6. build() {
     7. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
     8. Button('generateBarcode Promise').onClick(() => {
     9. // 以QR码为例，码图生成参数
     10. this.pixelMap = undefined;
     11. let content: string = 'huawei';
     12. let options: generateBarcode.CreateOptions = {
     13. scanType: scanCore.ScanType.QR_CODE,
     14. height: 400,
     15. width: 400
     16. }
     17. try {
     18. // 码图生成接口，成功返回PixelMap格式图片
     19. generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
     20. this.pixelMap = pixelMap;
     21. }).catch((err: BusinessError) => {
     22. hilog.error(0x0001, '[generateBarcode]',
     23. `Failed to get PixelMap by promise with options. Code: ${err.code}, message: ${err.message}`);
     24. })
     25. } catch (err) {
     26. hilog.error(0x0001, '[generateBarcode]',
     27. `Failed to createBarcode by promise with options. Code: ${err.code}, message: ${err.message}`);
     28. }

     30. })
     31. // 获取生成码图后显示
     32. if (this.pixelMap) {
     33. Image(this.pixelMap).width(300).height(300).objectFit(ImageFit.Contain)
     34. }
     35. }
     36. .width('100%')
     37. .height('100%')
     38. }
     39. }
     ```
   * 通过Callback方式回调，获取生成的码图。

     ```
     1. @Entry
     2. @Component
     3. struct Index {
     4. @State pixelMap: image.PixelMap | undefined = undefined

     6. build() {
     7. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
     8. Button('generateBarcode Callback').onClick(() => {
     9. // 以QR码为例，码图生成参数
     10. let content = 'huawei';
     11. let options: generateBarcode.CreateOptions = {
     12. scanType: scanCore.ScanType.QR_CODE,
     13. height: 400,
     14. width: 400
     15. }
     16. try {
     17. // 码图生成接口，成功返回PixelMap格式图片
     18. generateBarcode.createBarcode(content, options, (err: BusinessError, pixelMap: image.PixelMap) => {
     19. if (err) {
     20. hilog.error(0x0001, '[generateBarcode]',
     21. `Failed to get PixelMap by callback with options. Code: ${err.code}, message: ${err.message}`);
     22. return;
     23. }
     24. this.pixelMap = pixelMap;
     25. })
     26. } catch (err) {
     27. hilog.error(0x0001, '[generateBarcode]',
     28. `Failed to createBarcode by callback with options. Code: ${err.code}, message: ${err.message}`);
     29. }
     30. })
     31. // 获取生成码图后显示
     32. if (this.pixelMap) {
     33. Image(this.pixelMap).width(300).height(300).objectFit(ImageFit.Contain)
     34. }
     35. }
     36. .width('100%')
     37. .height('100%')
     38. }
     39. }
     ```

## 模拟器开发

暂不支持模拟器开发，调用接口会返回错误信息“Emulator is not supported.”
