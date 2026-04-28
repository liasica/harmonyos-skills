---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-detectbarcode
title: 识别本地图片
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 图像识码 > 识别本地图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ea6ee4fde00a38f3de94a79442f15d7aea3de1e0b39391b949faf9a227025ac
---

## 基本概念

图片识码能力支持对图库中的码图进行扫描识别，并获取信息。

## 场景介绍

图片识码能力支持对图库中的条形码、二维码、MULTIFUNCTIONAL CODE进行识别，并获得码类型、码值、码位置等信息。该能力可用于一图单码和一图多码的识别，比如条形码、付款码等。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/AUlfZsbkTpe4emFE04yU1A/zh-cn_image_0000002583438659.png?HW-CC-KV=V1&HW-CC-Date=20260427T234641Z&HW-CC-Expire=86400&HW-CC-Sign=1D126A14DB8A3A9AC22BEDEE8B21BA34104C53E10AC27D3D90A934B3D18799C1)

1. 用户向开发者的应用发起图片识码请求。
2. 应用通过调用Scan Kit的decode接口启动图片识码。
3. Scan Kit通过回调返回图片识码结果。
4. 应用向用户返回扫码结果。

## 接口说明

接口返回值有两种返回形式：Callback和Promise回调。下表中为启动图片识码Callback和Promise形式接口，Callback和Promise只是返回值方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/scan-imagedecode.md)。

| 接口名 | 描述 |
| --- | --- |
| [decode](../harmonyos-references/scan-imagedecode.md#detectbarcodedecode)(inputImage: [InputImage](../harmonyos-references/scan-imagedecode.md#inputimage), options?: scanBarcode.[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)): Promise<Array<scanBarcode.[ScanResult](../harmonyos-references/scan-scanbarcode-api.md#scanresult)>> | 启动图片识码，通过InputImage传入图片信息，通过ScanOptions进行识码参数设置（options为可选参数），使用Promise异步回调返回识码结果。 |
| [decode](../harmonyos-references/scan-imagedecode.md#detectbarcodedecode-1)(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void | 启动图片识码，通过InputImage传入图片信息，通过ScanOptions进行识码参数设置，使用Callback异步回调返回识码结果。 |
| [decode](../harmonyos-references/scan-imagedecode.md#detectbarcodedecode-2)(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void | 启动图片识码，通过InputImage传入图片信息，使用Callback异步回调返回识码结果。 |

## 开发步骤

图片识码接口支持识别图库中的条形码，二维码以及MULTIFUNCTIONAL CODE，并返回图片中码类型，码值、码位置（码图最小外接矩形左上角和右下角的坐标）等信息。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

以下示例为调用图片识码的detectBarcode.decode接口获取码图信息。

1. 导入图片识码接口和相关接口模块，该接口提供了图片识码参数和方法，导入方法如下。

   ```
   1. // 导入图片识码需要的日志和picker模块
   2. import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
   3. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用detectBarcode.decode接口解析码图。

   * 通过Promise回调函数得到扫码结果，InputImage对象中uri参数推荐通过[picker](photoaccesshelper-photoviewpicker.md)方式获取。

     ```
     1. @Entry
     2. @Component
     3. struct DetectPage {
     4. build() {
     5. Column() {
     6. Button('Promise with options')
     7. .backgroundColor('#0D9FFB')
     8. .fontSize(20)
     9. .fontColor($r('sys.color.comp_background_list_card'))
     10. .fontWeight(FontWeight.Normal)
     11. .align(Alignment.Center)
     12. .type(ButtonType.Capsule)
     13. .width('90%')
     14. .height(40)
     15. .margin({ top: 5, bottom: 5 })
     16. .onClick(() => {
     17. // 定义识码参数options
     18. let options: scanBarcode.ScanOptions = {
     19. scanTypes: [scanCore.ScanType.ALL],
     20. enableMultiMode: true,
     21. }
     22. // 通过picker拉起图库的图片
     23. let photoOption = new photoAccessHelper.PhotoSelectOptions();
     24. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
     25. photoOption.maxSelectNumber = 1;
     26. let photoPicker = new photoAccessHelper.PhotoViewPicker();
     27. photoPicker.select(photoOption).then((data) => {
     28. // 定义识码参数inputImage，其中uri为picker选择图片
     29. let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
     30. try {
     31. // 调用图片识码接口
     32. detectBarcode.decode(inputImage, options).then((data: Array<scanBarcode.ScanResult>) => {
     33. hilog.info(0x0001, '[Scan Sample]',
     34. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
     35. }).catch((err: BusinessError) => {
     36. hilog.error(0x0001, '[Scan Sample]',
     37. `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
     38. });
     39. } catch (err) {
     40. hilog.error(0x0001, '[Scan Sample]',
     41. `Failed to detectBarcode. Code: ${err.code}, message: ${err.message}`);
     42. }
     43. }).catch((err: BusinessError) => {
     44. hilog.error(0x0001, '[Scan Sample]',
     45. `Failed to select a photo. Code: ${err.code}, message: ${err.message}`);
     46. })
     47. });
     48. }
     49. .width('100%')
     50. .height('100%')
     51. .alignItems(HorizontalAlign.Center)
     52. .justifyContent(FlexAlign.Center)
     53. }
     54. }
     ```
   * 通过Callback回调函数得到扫码结果，InputImage对象中uri参数推荐通过[picker](photoaccesshelper-photoviewpicker.md)方式获取。

     ```
     1. @Entry
     2. @Component
     3. struct DetectPage {
     4. build() {
     5. Column() {
     6. Button('Callback with options')
     7. .backgroundColor('#0D9FFB')
     8. .fontSize(20)
     9. .fontColor($r('sys.color.comp_background_list_card'))
     10. .fontWeight(FontWeight.Normal)
     11. .align(Alignment.Center)
     12. .type(ButtonType.Capsule)
     13. .width('90%')
     14. .height(40)
     15. .margin({ top: 5, bottom: 5 })
     16. .onClick(() => {
     17. // 定义识码参数options
     18. let options: scanBarcode.ScanOptions = {
     19. scanTypes: [scanCore.ScanType.ALL],
     20. enableMultiMode: true,
     21. enableAlbum: true
     22. }
     23. // 通过选择模式拉起photoPicker界面，用户可以选择一个图片
     24. let photoOption = new photoAccessHelper.PhotoSelectOptions();
     25. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
     26. photoOption.maxSelectNumber = 1;
     27. let photoPicker = new photoAccessHelper.PhotoViewPicker();
     28. photoPicker.select(photoOption).then((data) => {
     29. // 定义识码参数inputImage，其中uri为picker选择图片
     30. let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
     31. try {
     32. // 调用图片识码接口
     33. detectBarcode.decode(inputImage, options,
     34. (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
     35. if (err && err.code) {
     36. hilog.error(0x0001, '[Scan Sample]',
     37. `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
     38. return;
     39. }
     40. hilog.info(0x0001, '[Scan Sample]',
     41. `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(data)}`);
     42. });
     43. } catch (err) {
     44. hilog.error(0x0001, '[Scan Sample]',
     45. `Failed to detectBarcode. Code: ${err.code}, message: ${err.message}`);
     46. }
     47. }).catch((err: BusinessError) => {
     48. hilog.error(0x0001, '[Scan Sample]',
     49. `Failed to select a photo. Code: ${err.code}, message: ${err.message}`);
     50. })
     51. });
     52. }
     53. .width('100%')
     54. .height('100%')
     55. .alignItems(HorizontalAlign.Center)
     56. .justifyContent(FlexAlign.Center)
     57. }
     58. }
     ```

## 模拟器开发

支持模拟器开发，模拟器使用指导请参见[使用模拟器运行应用](ide-run-emulator.md)。
