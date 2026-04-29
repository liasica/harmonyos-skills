---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-scanbarcode
title: 默认界面扫码
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > 默认界面扫码
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e1cb8aedb61569e8bcf71de81211c760348719029403e71fa3f6cc72f713a274
---

## 基本概念

默认界面扫码能力提供系统级体验一致的扫码界面，包含相机预览流，相册扫码入口，暗光环境闪光灯开启提示。Scan Kit默认界面扫码对系统相机权限进行了预授权且调用期间处于安全访问状态，无需开发者再次申请相机权限。适用于不同扫码场景的应用开发。

说明

通过默认界面扫码可以实现应用内的扫码功能，为了获得更好的应用体验，推荐同时[接入“扫码直达”服务](scan-directservice.md)，应用可以同时支持系统扫码入口（控制中心扫一扫）和应用内扫码两种方式跳转到指定服务页面。

## 场景介绍

默认界面扫码能力提供了系统级体验一致的扫码界面以及相册扫码入口，支持单码和多码识别，支持多种识码类型，请参见[ScanType](../harmonyos-references/scan-scancore.md#scantype)。无需使用三方库就可帮助开发者的应用快速处理各种扫码场景。

默认界面扫码UX：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/1h5-85qdQCOZnZF5POXCmg/zh-cn_image_0000002589244917.png?HW-CC-KV=V1&HW-CC-Date=20260429T053539Z&HW-CC-Expire=86400&HW-CC-Sign=46C24AD9CE001A96187589D7AB3F74BB97C3EF77F543E6EE0A61A7519ECD7C68)

说明

1. 系统首次使用默认界面扫码功能时，会向用户弹出隐私横幅提醒。
2. 用户可以点击“进一步了解”查看安全访问相机说明，也可以关闭隐私横幅，关闭后重新打开应用的扫码界面将不再显示隐私横幅提醒，显示安全访问提示，3s后消失。
3. 从6.1.0(23)版本开始，默认界面扫码的标题支持根据[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)的scanTypes进行动态显示。

   * 对于6.1.0(23)之前版本，标题统一显示为“扫描二维码/条形码”。
   * 对于6.1.0(23)及之后版本：
     + scanTypes为ALL、FORMAT\_UNKNOWN，或同时包含条形码和二维码类型，标题显示为“扫描二维码/条形码”。
     + scanTypes未设置，标题显示为“扫描二维码/条形码”。
     + scanTypes仅包含条形码类型，标题显示为“扫描条形码”。
     + scanTypes仅包含二维码类型，标题显示为“扫描二维码”。

## 约束与限制

* 从6.1.0(23)版本开始，默认界面扫码的标题支持根据[ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)的scanTypes进行动态显示。
* 从6.1.0(23)版本开始，默认界面扫码能力支持带后置相机的Wearable，可以通过[cameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。
* 从6.0.0(20)版本开始，默认界面扫码能力支持悬浮屏、分屏场景。
* 相册扫码只支持单码识别。
* 不支持界面UX添加自定义设置。

## 业务流程

使用默认界面扫码的主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/avU2JV9fR5KaF3gkeCzhcA/zh-cn_image_0000002558765112.png?HW-CC-KV=V1&HW-CC-Date=20260429T053539Z&HW-CC-Expire=86400&HW-CC-Sign=AB648BE3D2B08FCD7077FFF7FCC9EACEE0B8A388DA7D38D4E6597105FEDE22F4)

1. 用户向开发者的应用发起扫码请求。
2. 开发者的应用通过调用Scan Kit的startScanForResult接口启动扫码界面。
3. 系统首次使用默认界面扫码功能时，会向用户弹出隐私横幅提醒。
4. 用户可以点击关闭隐私横幅，重新打开应用的扫码界面将不再显示隐私横幅提醒，显示安全访问提示，3s后消失。
5. Scan Kit通过Callback回调函数或Promise方式返回扫码结果。
6. 用户进行多码扫描时，需点击选择其中一个码图获取扫码结果返回。单码扫描则可直接返回扫码结果。
7. 解析码值结果跳转应用服务页。

## 接口说明

接口返回值有两种返回形式：Callback和Promise回调。下表中为默认界面扫码Callback和Promise形式接口，Callback和Promise只是返回值方式不一样，功能相同。startScanForResult接口打开的是应用内呈现的扫码界面样式。具体API说明详见[接口文档](../harmonyos-references/scan-scanbarcode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [startScanForResult](../harmonyos-references/scan-scanbarcode-api.md#scanbarcodestartscanforresult)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context), options?: [ScanOptions](../harmonyos-references/scan-scanbarcode-api.md#scanoptions)): Promise<[ScanResult](../harmonyos-references/scan-scanbarcode-api.md#scanresult)> | 启动默认界面扫码，通过ScanOptions进行扫码参数设置，返回扫码结果。使用Promise异步回调。 |
| [startScanForResult](../harmonyos-references/scan-scanbarcode-api.md#scanbarcodestartscanforresult-2)(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void | 启动默认界面扫码，通过ScanOptions进行扫码参数设置，返回扫码结果。使用callback异步回调。 |
| [startScanForResult](../harmonyos-references/scan-scanbarcode-api.md#scanbarcodestartscanforresult-1)(context: common.Context, callback: AsyncCallback<ScanResult>): void | 启动默认界面扫码，返回扫码结果。使用callback异步回调。 |

说明

startScanForResult接口需要在页面和组件的生命周期内调用。若需要设置扫码页面为全屏或沉浸式，请参见[开发应用沉浸式效果](arkts-develop-apply-immersive-effects.md)。

## 开发步骤

Scan Kit提供了默认界面扫码的能力，由扫码接口直接控制相机实现最优的相机放大控制、自适应的曝光调节、自适应对焦调节等操作，保障流畅的扫码体验，减少开发者的工作量。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

以下示例为调用Scan Kit的startScanForResult接口跳转扫码页面。

1. 导入默认界面扫码模块，[scanCore](../harmonyos-references/scan-scancore.md)提供扫码类型定义，[scanBarcode](../harmonyos-references/scan-scanbarcode-api.md)提供拉起默认界面扫码的方法和参数，导入方法如下。

   ```
   1. import { scanCore, scanBarcode } from '@kit.ScanKit';
   2. // 导入默认界面扫码需要的日志模块和错误码模块
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用startScanForResult方法拉起默认界面扫码。

   * 通过Promise方式得到扫码结果。

     ```
     1. @Entry
     2. @Component
     3. struct ScanBarCodePage {
     4. build() {
     5. Column() {
     6. Row() {
     7. Button('Promise with options')
     8. .backgroundColor('#0D9FFB')
     9. .fontSize(20)
     10. .fontColor($r('sys.color.comp_background_list_card'))
     11. .fontWeight(FontWeight.Normal)
     12. .align(Alignment.Center)
     13. .type(ButtonType.Capsule)
     14. .width('90%')
     15. .height(40)
     16. .margin({ top: 5, bottom: 5 })
     17. .onClick(() => {
     18. // 定义扫码参数options
     19. let options: scanBarcode.ScanOptions = {
     20. scanTypes: [scanCore.ScanType.ALL],
     21. enableMultiMode: true,
     22. enableAlbum: true
     23. };
     24. try {
     25. // 可调用getHostContext接口获取当前页面关联的Context
     26. scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options)
     27. .then((data: scanBarcode.ScanResult) => {
     28. // 解析码值结果跳转应用服务页
     29. hilog.info(0x0001, '[Scan CPSample]',
     30. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
     31. })
     32. .catch((err: BusinessError) => {
     33. hilog.error(0x0001, '[Scan CPSample]',
     34. `Failed to get ScanResult by promise with options. Code:${err.code}, message: ${err.message}`);
     35. });
     36. } catch (err) {
     37. hilog.error(0x0001, '[Scan CPSample]',
     38. `Failed to start the scanning service. Code:${err.code}, message: ${err.message}`);
     39. }
     40. })
     41. }
     42. .height('100%')
     43. }
     44. .width('100%')
     45. }
     46. }
     ```
   * 通过Callback回调函数得到扫码结果。

     ```
     1. @Entry
     2. @Component
     3. struct ScanBarCodePage {
     4. build() {
     5. Column() {
     6. Row() {
     7. Button('Callback with options')
     8. .backgroundColor('#0D9FFB')
     9. .fontSize(20)
     10. .fontColor($r('sys.color.comp_background_list_card'))
     11. .fontWeight(FontWeight.Normal)
     12. .align(Alignment.Center)
     13. .type(ButtonType.Capsule)
     14. .width('90%')
     15. .height(40)
     16. .margin({ top: 5, bottom: 5 })
     17. .onClick(() => {
     18. // 定义扫码参数options
     19. let options: scanBarcode.ScanOptions = {
     20. scanTypes: [scanCore.ScanType.ALL],
     21. enableMultiMode: true,
     22. enableAlbum: true
     23. };
     24. try {
     25. // 可调用getHostContext接口获取当前页面关联的Context
     26. scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options,
     27. (err: BusinessError, data: scanBarcode.ScanResult) => {
     28. if (err) {
     29. hilog.error(0x0001, '[Scan CPSample]',
     30. `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
     31. return;
     32. }
     33. // 解析码值结果跳转应用服务页
     34. hilog.info(0x0001, '[Scan CPSample]',
     35. `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(data)}`);
     36. });
     37. } catch (err) {
     38. hilog.error(0x0001, '[Scan CPSample]',
     39. `Failed to start the scanning service. Code:${err.code}, message: ${err.message}`);
     40. }
     41. })
     42. }
     43. .height('100%')
     44. }
     45. .width('100%')
     46. }
     47. }
     ```

## 模拟器开发

从6.0.0(20)版本开始，模拟器支持默认界面扫码能力开发，模拟器使用指导请参见[使用模拟器运行应用](ide-run-emulator.md)。

模拟器中默认界面扫码的相机流存在镜像问题，且由于仅支持固定分辨率比例，画面会出现上下黑边。
