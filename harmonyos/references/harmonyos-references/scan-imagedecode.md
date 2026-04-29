---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scan-imagedecode
title: detectBarcode (图像识码)
breadcrumb: API参考 > 媒体 > Scan Kit（统一扫码服务） > ArkTS API > detectBarcode (图像识码)
category: harmonyos-references
scraped_at: 2026-04-29T14:05:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:652852b55ceb85ee5b49c23384e4e40e1b853168a21ba992397baea62a687f83
---

本模块提供本地图片识码和图像数据识码能力，支持对图像中的条形码、二维码、MULTIFUNCTIONAL CODE进行识别。

为了方便开发者接入，我们提供了详细的样例工程供参考，推荐参考[示例工程](https://gitcode.com/HarmonyOS_Samples/scankit-samplecode-clientdemo-arkts)接入。

**起始版本：** 4.1.0(11)

## 导入模块

PhoneTabletWearable

```
1. import { detectBarcode } from '@kit.ScanKit';
```

## InputImage

PhoneTabletWearable

待识别的图片信息。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 图片路径，例如file://media/Photo/x/xxx.jpg。 |

**示例：**

推荐使用[picker](../harmonyos-guides/photoaccesshelper-photoviewpicker.md)获取图片路径。

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

6. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
7. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
8. photoSelectOptions.maxSelectNumber = 1;
9. photoSelectOptions.isPhotoTakingSupported = false;
10. photoSelectOptions.isEditSupported = false;
11. let photoPicker = new photoAccessHelper.PhotoViewPicker();
12. photoPicker.select(photoSelectOptions).then((data: photoAccessHelper.PhotoSelectResult) => {
13. if (!data || (data.photoUris && data.photoUris.length === 0)) {
14. hilog.error(0x0001, 'picker', 'Failed to get PhotoSelectResult by promise');
15. return;
16. }
17. hilog.info(0x0001, 'picker', `Succeeded in getting PhotoSelectResult by promise.`);
18. }).catch((err: BusinessError) => {
19. hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
20. });
```

## detectBarcode.decode

PhoneTabletWearable

decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>

通过配置参数调用图片识码返回识码结果。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动图片识码参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | Promise对象，返回识码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 定义识码参数options
7. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
8. // 通过picker拉起图库并选择图片
9. let photoOption = new photoAccessHelper.PhotoSelectOptions();
10. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
11. photoOption.maxSelectNumber = 1;
12. let photoPicker = new photoAccessHelper.PhotoViewPicker();
13. photoPicker.select(photoOption).then((data) => {
14. // 定义识码参数inputImage，其中uri为picker选择图片
15. let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
16. try {
17. // 调用图片识码接口
18. detectBarcode.decode(inputImage, options).then((data: Array<scanBarcode.ScanResult>) => {
19. hilog.info(0x0001, '[Scan Sample]',
20. `Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(data)}`);
21. }).catch((err: BusinessError) => {
22. hilog.error(0x0001, '[Scan Sample]',
23. `Failed to get ScanResult by promise with options. Code: ${err.code}, message: ${err.message}`);
24. });
25. } catch (err) {
26. hilog.error(0x0001, '[Scan Sample]',
27. `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
28. }
29. }).catch((err: BusinessError) => {
30. hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}.`);
31. });
```

## detectBarcode.decode

PhoneTabletWearable

decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

通过配置参数调用图片识码返回识码结果。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 是 | 启动图片识码参数。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
2. import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 定义识码参数options
7. let options: scanBarcode.ScanOptions = { scanTypes: [scanCore.ScanType.ALL], enableMultiMode: true, enableAlbum: true };
8. // 通过选择模式拉起photoPicker界面，用户可以选择一个图片
9. let photoOption = new photoAccessHelper.PhotoSelectOptions();
10. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
11. photoOption.maxSelectNumber = 1;
12. let photoPicker = new photoAccessHelper.PhotoViewPicker();
13. photoPicker.select(photoOption).then((data) => {
14. // 定义识码参数inputImage，其中uri为picker选择图片
15. let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
16. try {
17. // 调用图片识码接口
18. detectBarcode.decode(inputImage, options, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
19. if (err && err.code) {
20. hilog.error(0x0001, '[Scan Sample]',
21. `Failed to get ScanResult by callback with options. Code: ${err.code}, message: ${err.message}`);
22. return;
23. }
24. hilog.info(0x0001, '[Scan Sample]',
25. `Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(data)}`);
26. });
27. } catch (err) {
28. hilog.error(0x0001, '[Scan Sample]',
29. `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
30. }
31. }).catch((err: BusinessError) => {
32. hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
33. });
```

## detectBarcode.decode

PhoneTabletWearable

decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

图片识码返回识码结果。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputImage | [InputImage](scan-imagedecode.md#inputimage) | 是 | 待识别的图片信息。 |
| callback | AsyncCallback<Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>> | 是 | 回调函数，当图片识码成功，err为undefined，data为获取到的识码结果Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)>，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { scanBarcode, detectBarcode } from '@kit.ScanKit';
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // 通过picker拉起图库并选择图片
7. let photoOption = new photoAccessHelper.PhotoSelectOptions();
8. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
9. photoOption.maxSelectNumber = 1;
10. let photoPicker = new photoAccessHelper.PhotoViewPicker();
11. photoPicker.select(photoOption).then((data) => {
12. // 定义识码参数inputImage，其中uri为picker选择图片
13. let inputImage: detectBarcode.InputImage = { uri: data.photoUris[0] };
14. try {
15. // 调用图片识码接口
16. detectBarcode.decode(inputImage, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
17. if (err && err.code) {
18. hilog.error(0x0001, '[Scan Sample]',
19. `Failed to get ScanResult by callback. Code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. hilog.info(0x0001, '[Scan Sample]',
23. `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
24. });
25. } catch (err) {
26. hilog.error(0x0001, '[Scan Sample]',
27. `Failed to detect Barcode. Code: ${err.code}, message: ${err.message}`);
28. }
29. }).catch((err: BusinessError) => {
30. hilog.error(0x0001, 'picker', `Failed to get PhotoSelectResult by promise. Code: ${err.code}`);
31. });
```

## ByteImage

PhoneTabletWearable

待识别的图像数据。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| byteBuffer | ArrayBuffer | 否 | 否 | 图像数据。 |
| width | number | 否 | 否 | 图像宽度，单位：px。 |
| height | number | 否 | 否 | 图像高度，单位：px。 |
| format | [ImageFormat](scan-imagedecode.md#imageformat) | 否 | 否 | 图像数据类型。 |

**示例：**

```
1. import { detectBarcode } from '@kit.ScanKit';

3. // YUV图像的buffer, height, width数据，可通过相机预览流数据获取，比如获取宽高是1920*1080时
4. let byteImg: detectBarcode.ByteImage = {
5. byteBuffer: buffer,
6. width: 1920,
7. height: 1080,
8. format: detectBarcode.ImageFormat.NV21
9. };
```

## ImageFormat

PhoneTabletWearable

枚举，图像数据类型。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| NV21 | 0 | 图像格式为NV21。 |

## DetectResult

PhoneTabletWearable

识别结果。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scanResults | Array<scanBarcode.[ScanResult](scan-scanbarcode-api.md#scanresult)> | 否 | 否 | 扫码结果。 |
| zoomValue | number | 否 | 否 | 相机可变焦距比，通过[setZoomRatio](arkts-apis-camera-zoom.md#setzoomratio11)控制相机实现变焦功能。  **说明：**  1. 使用Camera Kit [getZoomRatio](arkts-apis-camera-zoom.md#getzoomratio11)接口获取相机当前变焦比zoomRatio。  2. 使用Camera Kit [setZoomRatio](arkts-apis-camera-zoom.md#setzoomratio11)接口设置targetRatio，目标值为zoomRatio \* zoomValue。 |

## detectBarcode.decodeImage

PhoneTabletWearable

decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise<DetectResult>

通过配置参数调用图像数据识码能力返回识码结果。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Scan.ScanBarcode

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ByteImage](scan-imagedecode.md#byteimage) | 是 | 待识别的图像数据。 |
| options | scanBarcode.[ScanOptions](scan-scanbarcode-api.md#scanoptions) | 否 | 启动图像数据识码参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[DetectResult](scan-imagedecode.md#detectresult)> | Promise对象，返回图像数据识码结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](scan-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 1000500001 | Internal error. |

**示例：**

```
1. import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 优先获取图像的YUVByteBuffer, YUVHeight, YUVWidth数据，比如获取宽高是1920*1080时
6. let byteImg: detectBarcode.ByteImage = {
7. byteBuffer: YUVByteBuffer,
8. width: 1920,
9. height: 1080,
10. format: detectBarcode.ImageFormat.NV21
11. };
12. let options: scanBarcode.ScanOptions = {
13. scanTypes: [scanCore.ScanType.ALL],
14. enableMultiMode: true,
15. enableAlbum: false
16. };
17. try {
18. detectBarcode.decodeImage(byteImg, options).then((data: detectBarcode.DetectResult) => {
19. hilog.info(0x0001, '[Scan Sample]',
20. `Succeeded in getting DetectResult by promise with options, result is ${JSON.stringify(data)}`);
21. }).catch((err: BusinessError) => {
22. hilog.error(0x0001, '[Scan Sample]',
23. `Failed to get DetectResult by promise with options. Code: ${err.code}, message: ${err.message}`);
24. });
25. } catch (err) {
26. hilog.error(0x0001, '[Scan Sample]', `Failed to decode Image. Code: ${err.code}, message: ${err.message}`);
27. }
```

说明

不支持并行调用。
