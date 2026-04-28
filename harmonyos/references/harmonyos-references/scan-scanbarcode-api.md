---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-scanbarcode-api
title: scanBarcode (默认界面扫码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > scanBarcode (默认界面扫码)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09d3483d4878fe9009bf123164ad5ad1cd7a58b82f35f82036621268577d7a01
---

本模块提供默认界面扫码能力。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

**起始版本：** 4.0.0(10)

## 导入模块

PhoneTabletWearable

```
1. import { scanBarcode } from '@kit.ScanKit';
```

## ScanResult

PhoneTabletWearable

扫码结果。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scanType | scanCore.[ScanType](scan-scancore.md#scantype) | 否 | 否 | 码类型。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| originalValue | string | 否 | 否 | 码识别内容结果。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| scanCodeRect | [ScanCodeRect](scan-scanbarcode-api.md#scancoderect) | 否 | 是 | 码识别位置信息。  **起始版本：** 4.1.0(11) |
| cornerPoints | Array<[Point](scan-scanbarcode-api.md#point)> | 否 | 是 | 码识别角点位置信息，返回QR Code四个角点。此参数仅图像识码接口[detectBarcode.decodeImage](scan-imagedecode.md#detectbarcodedecodeimage)返回。  **起始版本：** 5.0.0(12) |
| isGS1 | boolean | 否 | 是 | 码图是否携带GS1（Global Standards 1）数据。  true表示码图携带GS1数据；false表示码图不携带GS1数据。默认值是false。  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.2(22) |
| source | scanCore.[ScanSource](scan-scancore.md#scansource) | 否 | 是 | 扫码结果来源。此参数仅默认界面扫码接口返回。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。  **起始版本：** 6.0.2(22) |

## ScanCodeRect

PhoneTabletWearable

码的位置信息。使用默认界面扫码（startScan和startScanForResult）不返回码位置。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 码外接矩形左上角的x坐标。单位：px。 |
| top | number | 否 | 否 | 码外接矩形左上角的y坐标。单位：px。 |
| right | number | 否 | 否 | 码外接矩形右下角的x坐标。单位：px。 |
| bottom | number | 否 | 否 | 码外接矩形右下角的y坐标。单位：px。 |

说明

自定义界面扫码返回的坐标单位与传入参数[ViewControl](scan-customscan-api.md#viewcontrol)中width、height单位一致。

## Point

PhoneTabletWearable

点坐标，该坐标系左上角为{0，0}，此坐标系是以设备充电口在右侧时的横向设备方向为基准的。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | X轴坐标，单位：px。 |
| y | number | 否 | 否 | Y轴坐标，单位：px。 |

## ScanOptions

PhoneTabletWearable

扫码、识码参数。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.0.0(10)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| scanTypes | Array<scanCore.[ScanType](scan-scancore.md#scantype)> | 否 | 是 | 设置扫码类型，默认扫码ALL（全部码类型）。  从6.1.0(23)版本开始，默认界面扫码的标题支持根据此参数进行动态显示。  对于6.1.0(23)之前版本，标题统一显示为“扫描二维码/条形码”。  对于6.1.0(23)及之后版本：  - scanTypes为ALL、FORMAT\_UNKNOWN，或同时包含条形码和二维码类型，标题显示为“扫描二维码/条形码”。  - scanTypes未设置，标题显示为“扫描二维码/条形码”。  - scanTypes仅包含条形码类型，标题显示为“扫描条形码”。  - scanTypes仅包含二维码类型，标题显示为“扫描二维码”。 |
| enableMultiMode | boolean | 否 | 是 | 是否开启多码识别，默认false。  - true：多码识别。  - false：单码识别。 |
| enableAlbum | boolean | 否 | 是 | 是否开启相册，默认true。  - true：开启相册扫码。  - false：关闭相册扫码。  此参数只控制默认界面扫码能力中的相册识码且相册识码只支持单码识别。 |

**示例：**

```
1. import { scanBarcode, scanCore } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义扫码参数options
6. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

8. function loadPage(uiContext: UIContext) {
9. try {
10. scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((data: scanBarcode.ScanResult) => {
11. hilog.info(0x0001, '[Scan Sample]',
12. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
13. }).catch((err: BusinessError) => {
14. hilog.error(0x0001, '[Scan Sample]',
15. `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
16. });
17. } catch (err) {
18. hilog.error(0x0001, '[Scan Sample]',
19. `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
20. }
21. }
```

## scanBarcode.startScanForResult

PhoneTabletWearable

startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动扫码参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScanResult](scan-scanbarcode-api.md#scanresult)> | Promise对象，返回扫码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning. |

**示例：**

```
1. import { scanBarcode, scanCore } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义扫码参数options
6. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

8. function loadPage(uiContext: UIContext) {
9. try {
10. scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((data: scanBarcode.ScanResult) => {
11. hilog.info(0x0001, '[Scan Sample]',
12. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
13. }).catch((err: BusinessError) => {
14. hilog.error(0x0001, '[Scan Sample]',
15. `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
16. });
17. } catch (err) {
18. hilog.error(0x0001, '[Scan Sample]',
19. `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
20. }
21. }
```

## scanBarcode.startScanForResult

PhoneTabletWearable

startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning. |

**示例：**

```
1. import { scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 启动扫码，拉起扫码界面
6. function loadPage(uiContext: UIContext) {
7. try {
8. scanBarcode.startScanForResult(uiContext.getHostContext(),
9. (err: BusinessError, data: scanBarcode.ScanResult) => {
10. if (err) {
11. hilog.error(0x0001, '[Scan Sample]',
12. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. hilog.info(0x0001, '[Scan Sample]',
16. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
17. });
18. } catch (err) {
19. hilog.error(0x0001, '[Scan Sample]',
20. `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
21. }
22. }
```

## scanBarcode.startScanForResult

PhoneTabletWearable

startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，返回扫码结果。需要在页面和组件的生命周期内调用。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-app-ability-common.md#context) | 是 | 应用上下文。 |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 启动扫码参数。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |
| 1000500002 | The user canceled the barcode scanning. |

**示例：**

```
1. import { scanCore, scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义扫码参数options
6. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };

8. // 启动扫码，拉起扫码界面
9. function loadPage(uiContext: UIContext) {
10. try {
11. scanBarcode.startScanForResult(uiContext.getHostContext(), options,
12. (err: BusinessError, data: scanBarcode.ScanResult) => {
13. if (err) {
14. hilog.error(0x0001, '[Scan Sample]',
15. `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. hilog.info(0x0001, '[Scan Sample]',
19. `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(data)}`);
20. });
21. } catch (err) {
22. hilog.error(0x0001, '[Scan Sample]',
23. `Failed to startScanForResult. Code: ${err.code}, message: ${err.message}`);
24. }
25. }
```

## scanBarcode.startScan(deprecated)

PhoneTabletWearable

startScan(options?: ScanOptions): Promise<ScanResult>

通过配置参数调用默认界面扫码，返回扫码结果。使用Promise异步回调。

**废弃说明：** 从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#scanbarcodestartscanforresult)替代。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动扫码参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[ScanResult](scan-scanbarcode-api.md#scanresult)> | Promise对象，返回扫码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. import { scanCore, scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 构造启动扫码的入参options
6. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
7. try {
8. scanBarcode.startScan(options).then((data: scanBarcode.ScanResult) => {
9. hilog.info(0x0001, '[Scan Sample]',
10. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
11. }).catch((err: BusinessError) => {
12. // 当扫码过程中出现错误，打印并返回报错
13. hilog.error(0x0001, '[Scan Sample]',
14. `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
15. });
16. } catch (err) {
17. hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
18. }
```

## scanBarcode.startScan(deprecated)

PhoneTabletWearable

startScan(callback: AsyncCallback<ScanResult>): void

启动默认界面扫码，返回扫码结果。使用callback异步回调。

**废弃说明：** 从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#scanbarcodestartscanforresult-1)替代。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数。当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. import { scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. scanBarcode.startScan((err: BusinessError, data: scanBarcode.ScanResult) => {
7. // error回调监听，当扫码过程中出现错误，打印并返回报错
8. if (err) {
9. hilog.error(0x0001, '[Scan Sample]',
10. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. hilog.info(0x0001, '[Scan Sample]',
14. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
15. });
16. } catch (err) {
17. hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
18. }
```

## scanBarcode.startScan(deprecated)

PhoneTabletWearable

startScan(options: ScanOptions, callback: AsyncCallback<ScanResult>): void

通过配置参数调用默认界面扫码，返回扫码结果。使用callback异步回调。

**废弃说明：** 从版本4.1.0(11)开始废弃，建议使用[startScanForResult](scan-scanbarcode-api.md#scanbarcodestartscanforresult-2)替代。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中无响应。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.0.0(10)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| options | [ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 启动扫码参数。 |
| callback | AsyncCallback<[ScanResult](scan-scanbarcode-api.md#scanresult)> | 是 | 回调函数，当扫码返回成功，err为undefined，data为获取到的扫码结果对象[ScanResult](scan-scanbarcode-api.md#scanresult)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. import { scanCore, scanBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 构造启动扫码的入参options
6. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
7. try {
8. scanBarcode.startScan(options, (err: BusinessError, data: scanBarcode.ScanResult) => {
9. // error回调监听，当扫码过程中出现错误，打印并返回报错
10. if (err) {
11. hilog.error(0x0001, '[Scan Sample]',
12. `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
13. return;
14. }
15. hilog.info(0x0001, '[Scan Sample]',
16. `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(data)}`);
17. });
18. } catch (err) {
19. hilog.error(0x0001, '[Scan Sample]', `Failed to startScan. Code: ${err.code}, message: ${err.message}`);
20. }
```
