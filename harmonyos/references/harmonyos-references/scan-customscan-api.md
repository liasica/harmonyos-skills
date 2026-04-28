---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-customscan-api
title: customScan (自定义界面扫码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > customScan (自定义界面扫码)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c29e106688f8c1bea8746df7c89854a22de08b493898d03c6d4cac017df5b158
---

本模块提供自定义界面扫码能力。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

**起始版本：** 4.1.0(11)

## 导入模块

PhoneTabletWearable

```
1. import { customScan } from '@kit.ScanKit';
```

## ViewControl

PhoneTabletWearable

相机控制参数。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | [XComponent](ts-basic-components-xcomponent.md)组件的宽，默认使用单位为vp，支持px、lpx和vp。 |
| height | number | 否 | 否 | XComponent组件的高，默认使用单位为vp，支持px、lpx和vp。 |
| surfaceId | string | 否 | 否 | XComponent持有surface的ID。 |

说明

1. ViewControl的width和height需和XComponent的保持一致，start接口根据设置宽高值会匹配最接近的相机分辨率，如果宽高比例与相机的分辨率比例相差过大会影响预览流体验。XComponent组件为预览流提供的Surface，而XComponent的能力由UI提供，相关介绍可参见[XComponent](ts-basic-components-xcomponent.md)。
2. 当开发设备为折叠屏时，折叠态切换时需自行调整XComponent的宽高，start接口会重新适配相机分辨率比例。

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { scanBarcode, customScan } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct CustomScanPage {
8. // 设置预览流高度，默认单位：vp
9. @State cameraHeight: number = 640;
10. // 设置预览流宽度，默认单位：vp
11. @State cameraWidth: number = 360;
12. private mXComponentController: XComponentController = new XComponentController();

14. build() {
15. Stack() {
16. XComponent({
17. id: 'componentId',
18. type: XComponentType.SURFACE,
19. controller: this.mXComponentController
20. })
21. .onLoad(() => {
22. hilog.info(0x0001, '[Scan Sample]', 'onLoad is called')
23. // 获取XComponent的surfaceId
24. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
25. hilog.info(0x0001, 'viewControl', `onLoad surfaceId: ${surfaceId}`);
26. // 设置ViewControl相应字段
27. let viewControl: customScan.ViewControl = {
28. width: this.cameraWidth,
29. height: this.cameraHeight,
30. surfaceId: surfaceId
31. };
32. try {
33. customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
34. hilog.info(0x0001, '[Scan Sample]',
35. `Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}`);
36. }).catch((err: BusinessError) => {
37. hilog.error(0x0001, '[Scan Sample]',
38. `Failed to get ScanResult by promise. Code: ${err.code}, message: ${err.message}`);
39. })
40. } catch (err) {
41. hilog.error(0x0001, '[Scan Sample]',
42. `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
43. }
44. })
45. .height(this.cameraHeight)
46. .width(this.cameraWidth)
47. .position({ x: 0, y: 0 })
48. }
49. .alignContent(Alignment.Bottom)
50. .height('100%')
51. .width('100%')
52. .position({ x: 0, y: 0 })
53. }
54. }
```

## ScanFrame

PhoneTabletWearable

相机预览流（YUV）。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| byteBuffer | ArrayBuffer | 否 | 否 | 相机预览流的ArrayBuffer数组。 |
| width | number | 否 | 否 | 相机预览流的宽度，单位：px。 |
| height | number | 否 | 否 | 相机预览流的高度，单位：px。 |
| scanCodeRects | Array<scanBarcode.[ScanCodeRect](scan-scanbarcode-api.md#scancoderect)> | 否 | 是 | 相机预览流的码图检测位置信息。  **设备行为差异：** 该属性在带有Kirin NPU（Neural-network Processing Unit，神经网络处理器）的设备可正常返回，在不带有Kirin NPU的设备上返回undefined。 |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. import { scanBarcode, customScan } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct CustomScanPage {
8. // 设置预览流高度，默认单位：vp
9. @State cameraHeight: number = 640;
10. // 设置预览流宽度，默认单位：vp
11. @State cameraWidth: number = 360;
12. private mXComponentController: XComponentController = new XComponentController();
13. private callback: AsyncCallback<scanBarcode.ScanResult[]> =
14. (err: BusinessError, data: scanBarcode.ScanResult[]) => {
15. if (err) {
16. hilog.error(0x0001, '[Scan Sample]',
17. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
18. return;
19. }
20. hilog.info(0x0001, '[Scan Sample]',
21. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
22. }
23. // 回调获取ScanFrame
24. private frameCallback: AsyncCallback<customScan.ScanFrame> =
25. (err: BusinessError, frameResult: customScan.ScanFrame) => {
26. if (err) {
27. hilog.error(0x0001, '[Scan Sample]',
28. `Failed to get ScanFrame by callback. Code: ${err.code}, message: ${err.message}`);
29. return;
30. }
31. // byteBuffer相机YUV图像数组
32. hilog.info(0x0001, '[Scan Sample]',
33. `Succeeded in getting ScanFrame.byteBuffer.byteLength:  ${frameResult.byteBuffer.byteLength}`);
34. hilog.info(0x0001, '[Scan Sample]',
35. `Succeeded in getting ScanFrame.scanCodeRect: ${JSON.stringify(frameResult.scanCodeRects)}`);
36. }

38. build() {
39. Stack() {
40. XComponent({
41. id: 'componentId',
42. type: XComponentType.SURFACE,
43. controller: this.mXComponentController
44. })
45. .onLoad(() => {
46. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
47. // 获取XComponent的surfaceId
48. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
49. hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
50. // 设置ViewControl相应字段
51. let viewControl: customScan.ViewControl = {
52. width: this.cameraWidth,
53. height: this.cameraHeight,
54. surfaceId: surfaceId
55. };
56. try {
57. customScan.start(viewControl, this.callback, this.frameCallback);
58. } catch (err) {
59. hilog.error(0x0001, '[Scan Sample]',
60. `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
61. }
62. })
63. .height(this.cameraHeight)
64. .width(this.cameraWidth)
65. .position({ x: 0, y: 0 })
66. }
67. .alignContent(Alignment.Bottom)
68. .height('100%')
69. .width('100%')
70. .position({ x: 0, y: 0 })
71. }
72. }
```

说明

1. scanCodeRects返回的是在横向预览流中检测到的码图位置信息。若需在竖屏场景下进行后续处理（以设备竖屏、充电口朝下为基准），须将这些坐标转换至纵向坐标系。数组中每个元素包含left、top、right、bottom四个字段，其转换逻辑如下。以scanCodeRects第一个元素（scanCodeRects[0]）为例，具体实现参见下方示例代码。
2. 对应的二维码区域位置可以使用固定定位position({x: left, y: top})，宽度width: right - left，高度height: bottom - top，画出二维码实际区域范围。

```
1. // start接口frameCallback回调返回frameResult数据
2. import { customScan, scanBarcode } from '@kit.ScanKit';

4. // 模拟相机预览流返回数据frameResult: customScan.ScanFrame
5. let frameResult: customScan.ScanFrame = {
6. "width": 1920,
7. "height": 1080,
8. // buffer 为相机流
9. "byteBuffer": buffer,
10. "scanCodeRects": [{
11. "left": 84,
12. "top": 142,
13. "right": 1695,
14. "bottom": 996
15. }]
16. };
17. if (frameResult && frameResult.scanCodeRects) {
18. let rect: scanBarcode.ScanCodeRect = frameResult.scanCodeRects[0];
19. // 预览流尺寸转换为显示组件XComponent尺寸比例，例如设置的scanWidth为360vp
20. let scanWidth = 360;
21. let ratio = scanWidth / frameResult.height;
22. let left = (frameResult.height - rect.bottom) * ratio;
23. let top = rect.left * ratio;
24. let right = (frameResult.height - rect.top) * ratio;
25. let bottom = rect.right * ratio;
26. }
```

## customScan.init

PhoneTabletWearable

init(options?: scanBarcode.ScanOptions): void

初始化自定义界面扫码。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 自定义界面扫码参数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

从5.0.2(14)开始，customScan模块的init接口新增错误码201。

* 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块init接口，返回错误码1000500001。
* 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块init接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { scanBarcode, scanCore, customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let options: scanBarcode.ScanOptions = {
5. scanTypes: [scanCore.ScanType.ALL],
6. enableMultiMode: true,
7. enableAlbum: true
8. };
9. try {
10. customScan.init(options);
11. } catch (err) {
12. hilog.error(0x0001, '[Scan Sample]', `Failed to init customScan. Code: ${err.code}, message: ${err.message}`);
13. }
```

## customScan.start

PhoneTabletWearable

start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>

启动扫码相机流获取扫码结果。使用Promise异步回调。

说明

此接口需要在init接口调用后才能使用。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| viewControl | [ViewControl](scan-customscan-api.md#viewcontrol) | 是 | 相机控制参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | Promise对象，返回启动相机流扫码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

从5.0.2(14)开始，customScan模块的start接口新增错误码201。

* 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
* 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块start接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { scanBarcode, customScan } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct CustomScanPage {
8. // 设置预览流高度，默认单位：vp
9. @State cameraHeight: number = 640
10. // 设置预览流宽度，默认单位：vp
11. @State cameraWidth: number = 360
12. private mXComponentController: XComponentController = new XComponentController();

14. build() {
15. Stack() {
16. XComponent({
17. id: 'componentId',
18. type: XComponentType.SURFACE,
19. controller: this.mXComponentController
20. })
21. .onLoad(() => {
22. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
23. // 获取XComponent的surfaceId
24. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
25. hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
26. // 设置ViewControl相应字段
27. let viewControl: customScan.ViewControl = {
28. width: this.cameraWidth,
29. height: this.cameraHeight,
30. surfaceId: surfaceId
31. };
32. try {
33. customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
34. hilog.info(0x0001, '[Scan Sample]',
35. `Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}`);
36. }).catch((err: BusinessError) => {
37. hilog.error(0x0001, '[Scan Sample]',
38. `Failed to get ScanResult by promise. Code: ${err.code}, message: ${err.message}`);
39. });
40. } catch (err) {
41. hilog.error(0x0001, '[Scan Sample]',
42. `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
43. }
44. })
45. .height(this.cameraHeight)
46. .width(this.cameraWidth)
47. .position({ x: 0, y: 0 })
48. }
49. .alignContent(Alignment.Bottom)
50. .height('100%')
51. .width('100%')
52. .position({ x: 0, y: 0 })
53. }
54. }
```

## customScan.start

PhoneTabletWearable

start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void

启动扫码相机流获取扫码结果、相机预览流（YUV-图像格式NV21基于4:2:0采样）。使用callback异步回调。

说明

此接口需要在init接口调用后才能使用。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，申请相机权限成功后，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| viewControl | [ViewControl](scan-customscan-api.md#viewcontrol) | 是 | 相机控制参数。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当启动相机流扫码成功，err为undefined，data为获取到的Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>；否则为错误对象。 |
| frameCallback | AsyncCallback<[ScanFrame](scan-customscan-api.md#scanframe)> | 否 | 回调函数，当启动相机流成功，err为undefined，data为获取到的相机预览流（YUV）[ScanFrame](scan-customscan-api.md#scanframe)；否则为错误对象。  **起始版本：** 5.0.0(12) |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

从5.0.2(14)开始，customScan模块的start接口新增错误码201。

* 对于5.0.2(14)之前版本，在未申请相机权限时调用customScan模块start接口，返回错误码1000500001。
* 对于5.0.2(14)及之后版本，在未申请相机权限时调用customScan模块start接口，返回错误码201。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. import { scanBarcode, customScan } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct CustomScanPage {
8. // 设置预览流高度，默认单位：vp
9. @State cameraHeight: number = 640;
10. // 设置预览流宽度，默认单位：vp
11. @State cameraWidth: number = 360;
12. private mXComponentController: XComponentController = new XComponentController();
13. // 返回自定义扫描结果的回调
14. private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
15. (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
16. if (err) {
17. hilog.error(0x0001, '[Scan Sample]',
18. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
19. return;
20. }
21. hilog.info(0x0001, '[Scan Sample]',
22. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
23. }
24. // 回调获取ScanFrame
25. private frameCallback: AsyncCallback<customScan.ScanFrame> =
26. (err: BusinessError, scanFrame: customScan.ScanFrame) => {
27. if (err) {
28. hilog.error(0x0001, '[Scan Sample]',
29. `Failed to get ScanFrame by callback. Code: ${err.code}, message: ${err.message}`);
30. return;
31. }
32. hilog.info(0x0001, '[Scan Sample]',
33. `Succeeded in getting ScanFrame by callback, scanFrame is ${JSON.stringify(scanFrame)}`);
34. }

36. build() {
37. Stack() {
38. XComponent({
39. id: 'componentId',
40. type: XComponentType.SURFACE,
41. controller: this.mXComponentController
42. })
43. .onLoad(() => {
44. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
45. // 获取XComponent的surfaceId
46. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
47. hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
48. // 设置ViewControl相应字段
49. let viewControl: customScan.ViewControl = {
50. width: this.cameraWidth,
51. height: this.cameraHeight,
52. surfaceId: surfaceId
53. };
54. try {
55. customScan.start(viewControl, this.callback, this.frameCallback);
56. } catch (err) {
57. hilog.error(0x0001, '[Scan Sample]',
58. `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
59. }
60. })
61. .height(this.cameraHeight)
62. .width(this.cameraWidth)
63. .position({ x: 0, y: 0 })
64. }
65. .alignContent(Alignment.Bottom)
66. .height('100%')
67. .width('100%')
68. .position({ x: 0, y: 0 })
69. }
70. }
```

## customScan.getFlashLightStatus

PhoneTabletWearable

getFlashLightStatus(): boolean

获取当前相机闪光灯状态。

说明

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | 返回当前相机闪光灯状态。true代表开启，false代表关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let flashLightStatus: boolean = false;
5. try {
6. flashLightStatus = customScan.getFlashLightStatus();
7. // 根据当前闪光灯状态，选择开启或关闭闪光灯
8. if (flashLightStatus) {
9. try {
10. customScan.closeFlashLight();
11. } catch (err) {
12. hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
13. }
14. } else {
15. try {
16. customScan.openFlashLight();
17. } catch (err) {
18. hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
19. }
20. }
21. } catch (err) {
22. hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
23. }
```

## customScan.openFlashLight

PhoneTabletWearable

openFlashLight(): void

开启相机闪光灯。

说明

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let flashLightStatus: boolean = false;
5. try {
6. flashLightStatus = customScan.getFlashLightStatus();
7. // 根据当前闪光灯状态，选择开启或关闭闪光灯
8. if (flashLightStatus) {
9. try {
10. customScan.closeFlashLight();
11. } catch (err) {
12. hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
13. }
14. } else {
15. try {
16. customScan.openFlashLight();
17. } catch (err) {
18. hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
19. }
20. }
21. } catch (err) {
22. hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
23. }
```

## customScan.closeFlashLight

PhoneTabletWearable

closeFlashLight(): void

关闭相机闪光灯。

说明

本接口必须在启动相机流start接口后使用，相机流初始化、停止和释放阶段使用都会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let flashLightStatus: boolean = false;
5. try {
6. flashLightStatus = customScan.getFlashLightStatus();
7. } catch (err) {
8. hilog.error(0x0001, '[Scan Sample]', `Failed to getFlashLightStatus. Code: ${err.code}, message: ${err.message}`);
9. }
10. // 根据当前闪光灯状态，选择开启或关闭闪光灯
11. if (flashLightStatus) {
12. try {
13. customScan.closeFlashLight();
14. } catch (err) {
15. hilog.error(0x0001, '[Scan Sample]', `Failed to closeFlashLight. Code: ${err.code}, message: ${err.message}`);
16. }
17. } else {
18. try {
19. customScan.openFlashLight();
20. } catch (err) {
21. hilog.error(0x0001, '[Scan Sample]', `Failed to openFlashLight. Code: ${err.code}, message: ${err.message}`);
22. }
23. }
```

## customScan.setZoom

PhoneTabletWearable

setZoom(zoomValue: number): void

设置变焦比。变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

说明

本接口必须在启动相机流start接口后使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| zoomValue | number | 是 | 相机变焦比，精度最高为小数点后两位（例如1.45）。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 设置变焦比
5. let zoomValue = 2.0;
6. try {
7. customScan.setZoom(zoomValue);
8. } catch (err) {
9. hilog.error(0x0001, '[Scan Sample]', `Failed to setZoom. Code: ${err.code}, message: ${err.message}`);
10. }
```

## customScan.getZoom

PhoneTabletWearable

getZoom(): number

获取当前的变焦比。

说明

本接口必须在启动相机流start接口后使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| number | 返回当前的变焦比。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { customScan } from '@kit.ScanKit';

4. try {
5. // 获取变焦比
6. let zoomValue = customScan.getZoom();
7. hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting zoomValue, zoomValue is ${zoomValue}`);
8. } catch (err) {
9. hilog.error(0x0001, '[Scan Sample]', `Failed to get zoomValue. Code: ${err.code}, message: ${err.message}`);
10. }
```

## customScan.setFocusPoint

PhoneTabletWearable

setFocusPoint(point: scanBarcode.Point): void

设置相机焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

说明

本接口必须在启动相机流start接口后使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| point | scanBarcode.[Point](scan-scanbarcode-api.md#point) | 是 | 焦点。x、y设置范围应在[0，1]之内，超过范围，如果小于0设置0，大于1设置1。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // 设置对焦点
6. customScan.setFocusPoint({ x: 0.5, y: 0.5 });
7. } catch (err) {
8. hilog.error(0x0001, '[Scan Sample]', `Failed to setFocusPoint. Code: ${err.code}, message: ${err.message}`);
9. }
```

## customScan.resetFocus

PhoneTabletWearable

resetFocus(): void

设置连续自动对焦模式。

说明

本接口必须在启动相机流start接口后使用。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // 设置连续自动对焦模式
6. customScan.resetFocus();
7. } catch (err) {
8. hilog.error(0x0001, '[Scan Sample]', `Failed to resetFocus. Code: ${err.code}, message: ${err.message}`);
9. }
```

## customScan.on('lightingFlash')

PhoneTabletWearable

on(type: 'lightingFlash', callback: AsyncCallback<boolean>): void

订阅闪光灯状态监听事件，当环境暗、亮状态变化时返回闪光灯开启或关闭时机。使用callback异步回调。

说明

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'lightingFlash'，当环境亮度发生变化时触发。可用于提示用户开启或关闭闪光灯。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示当前环境暗，可以提示用户开启闪光灯，false表示环境亮，可以提示用户关闭闪光灯。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { customScan } from '@kit.ScanKit';

5. let callback = (err: BusinessError, bool: boolean) => {
6. if (err) {
7. hilog.error(0x0001, '[Scan Sample]',
8. `Failed to light Flash by callback. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. hilog.info(0x0001, '[Scan Sample]', `Succeeded in lighting Flash by callback, bool is ${bool}`);
12. }

14. try {
15. customScan.on('lightingFlash', callback);
16. } catch (err) {
17. hilog.error(0x0001, '[Scan Sample]',
18. `Failed to listen lightingFlash. Code: ${err.code}, message: ${err.message}`);
19. }
```

## customScan.off('lightingFlash')

PhoneTabletWearable

off(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void

注销闪光灯状态监听事件。使用callback异步回调。

说明

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，固定为'lightingFlash'，当环境亮度发生变化时触发，可用于提示用户开启或关闭闪光灯。 |
| callback | AsyncCallback<boolean> | 否 | 回调函数，如果指定参数则必须和customScan.on中监听的事件保持一致，否则注销所有绑定在'lightingFlash'上的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { customScan } from '@kit.ScanKit';

5. let callback = (err: BusinessError, bool: boolean) => {
6. if (err) {
7. hilog.error(0x0001, '[Scan Sample]',
8. `Failed to cancel Flash by callback. Code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. hilog.info(0x0001, '[Scan Sample]', `Succeeded in cancelling Flash by callback, bool is ${bool}`);
12. }
13. // 可以不填callback，取消lightingFlash所有监听。填写callback，必须保持和customScan.on中监听的事件保持一致
14. try {
15. customScan.off('lightingFlash', callback);
16. } catch (err) {
17. hilog.error(0x0001, '[Scan Sample]',
18. `Failed to listen lightingFlash. Code: ${err.code}, message: ${err.message}`);
19. }
```

## customScan.rescan

PhoneTabletWearable

rescan(): void

触发一次重新扫码。如果扫描结果不是预期结果，可以调用此接口触发下一次扫描。

说明

本接口必须在启动相机流start接口后，stop接口之前使用，未启动相机流调用会抛出内部错误的异常。

仅对start接口的Callback异步回调有效，Promise异步回调接口无效。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. import { scanBarcode, customScan } from '@kit.ScanKit';

5. @Entry
6. @Component
7. struct CustomScanPage {
8. // 设置预览流高度，默认单位：vp
9. @State cameraHeight: number = 640;
10. // 设置预览流宽度，默认单位：vp
11. @State cameraWidth: number = 360;
12. private mXComponentController: XComponentController = new XComponentController();
13. // 返回自定义扫描结果的回调
14. private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
15. (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
16. if (err) {
17. hilog.error(0x0001, '[Scan Sample]',
18. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
19. return;
20. }
21. hilog.info(0x0001, '[Scan Sample]',
22. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
23. // 重新触发扫码。如需不重启相机并重新触发一次扫码，可以在start接口的Callback异步回调中，调用rescan接口。
24. try {
25. customScan.rescan();
26. } catch (err) {
27. hilog.error(0x0001, '[Scan Sample]',
28. `Failed to rescan customScan. Code: ${err.code}, message: ${err.message}`);
29. }
30. }

32. build() {
33. Stack() {
34. XComponent({
35. id: 'componentId',
36. type: XComponentType.SURFACE,
37. controller: this.mXComponentController
38. })
39. .onLoad(() => {
40. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in loading, onLoad is called');
41. // 获取XComponent的surfaceId
42. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
43. hilog.info(0x0001, '[Scan Sample]', `Succeeded in getting surfaceId: ${surfaceId}`);
44. // 设置ViewControl相应字段
45. let viewControl: customScan.ViewControl = {
46. width: this.cameraWidth,
47. height: this.cameraHeight,
48. surfaceId: surfaceId
49. };
50. try {
51. customScan.start(viewControl, this.callback);
52. } catch (err) {
53. hilog.error(0x0001, '[Scan Sample]',
54. `Failed to start customScan. Code: ${err.code}, message: ${err.message}`);
55. }
56. })
57. .height(this.cameraHeight)
58. .width(this.cameraWidth)
59. .position({ x: 0, y: 0 })
60. }
61. .alignContent(Alignment.Bottom)
62. .height('100%')
63. .width('100%')
64. .position({ x: 0, y: 0 })
65. }
66. }
```

## customScan.setAutoZoomEnabled

PhoneTabletWearable

setAutoZoomEnabled(enabled: boolean): void

设置自动变焦能力的开启和关闭。未调用时默认开启自动变焦。

说明

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启自动变焦能力。true代表开启，false代表关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { customScan } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. // 开启或关闭自动变焦能力，true为开启，false为关闭
6. customScan.setAutoZoomEnabled(false);
7. } catch (err) {
8. hilog.error(0x0001, '[Scan Sample]', `Failed to setAutoZoomEnabled. Code: ${err.code}, message: ${err.message}`);
9. }
```

## customScan.stop

PhoneTabletWearable

stop(): Promise<void>

暂停扫码相机流。使用Promise异步回调。

说明

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { customScan } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. customScan.stop().then(() => {
7. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by promise');
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0001, '[Scan Sample]',
10. `Failed to stop scan by promise. Code: ${err.code}, message: ${err.message}`);
11. });
12. } catch (err) {
13. hilog.error(0x0001, '[Scan Sample]',
14. `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
15. }
```

## customScan.stop

PhoneTabletWearable

stop(callback: AsyncCallback<void>): void

暂停扫码相机流。使用callback异步回调。

说明

本接口必须在启动相机流start接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停相机流成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { customScan } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. customScan.stop((err: BusinessError) => {
7. if (err) {
8. hilog.error(0x0001, '[Scan Sample]',
9. `Failed to stop scan by callback. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in stopping scan by callback');
13. })
14. } catch (err) {
15. hilog.error(0x0001, '[Scan Sample]',
16. `Failed to stop customScan. Code: ${err.code}, message: ${err.message}`);
17. }
```

## customScan.release

PhoneTabletWearable

release(): Promise<void>

释放扫码相机流。使用Promise异步回调。

说明

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { customScan } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. customScan.release().then(() => {
7. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by promise');
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0001, '[Scan Sample]',
10. `Failed to release scan by promise. Code: ${err.code}, message: ${err.message}`);
11. })
12. } catch (err) {
13. hilog.error(0x0001, '[Scan Sample]',
14. `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
15. }
```

## customScan.release

PhoneTabletWearable

release(callback: AsyncCallback<void>): void

释放扫码相机流。使用callback异步回调。

说明

本接口建议在启动相机流start接口且暂停相机流stop接口后使用，未启动相机流调用会抛出内部错误的异常。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**设备行为差异：** 对于6.0.2(22)及之前版本，该接口在Phone、Tablet中可正常调用。对于6.1.0(23)及之后版本，该接口在Phone、Tablet、带后置相机的Wearable中可正常调用，在不带后置相机的Wearable中返回错误码1000500001。可以通过[cameraManager.getSupportedCameras](arkts-apis-camera-cameramanager.md#getsupportedcameras)接口查询是否带后置相机。

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放相机流成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000500001 | Internal error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { customScan } from '@kit.ScanKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. customScan.release((err: BusinessError) => {
7. if (err) {
8. hilog.error(0x0001, '[Scan Sample]',
9. `Failed to release scan by callback. Code: ${err.code}, message: ${err.message}`);
10. return;
11. }
12. hilog.info(0x0001, '[Scan Sample]', 'Succeeded in releasing scan by callback');
13. });
14. } catch (err) {
15. hilog.error(0x0001, '[Scan Sample]',
16. `Failed to release customScan. Code: ${err.code}, message: ${err.message}`);
17. }
```
