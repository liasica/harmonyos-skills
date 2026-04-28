---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-vision-base-api
title: VisionBase（Core Vision Kit基类）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > VisionBase（Core Vision Kit基类）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a39d401ed92f4fb2ace983af1dd1b5153890af651757f063bbe223b4036a9ee8
---

visionBase作为一个基础的视觉能力库，封装基本资源对象，视觉能力场景常用对象，数据结构，常用方法。减少冗余代码书写简化功能接口使用，而不必重复“造轮子”。开发者可以将它理解为一个“工具箱”，里面装着一些常用的“工具”，利用visionBase基类，会更高效、更标准地实现各自的功能。visionBase提供了Core Vision Kit AI能力所需的基础设施，如数据结构、接口模型、生命周期管理等。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { visionBase } from '@kit.CoreVisionKit';
```

## SceneMode

PhonePC/2in1Tablet

场景模式的枚举类。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOREGROUND | 1 | （默认）前台模式。 |
| BACKGROUND | 2 | 后台模式。 |

## ImageData

PhonePC/2in1Tablet

待识别的视觉信息对象。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 待识别的图片。 |

## InputData

PhonePC/2in1Tablet

type InputData = ImageData | ImageData[]

多个图像数据组成的数组。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| [ImageData](core-vision-vision-base-api.md#imagedata) | [ImageData](core-vision-vision-base-api.md#imagedata)[] | 待识别的图片数组。可输入一个或多个图片。 |

## BoundingBox

PhonePC/2in1Tablet

视觉AI能力的内切框。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 边界框左上角的x坐标。 |
| top | number | 否 | 否 | 边界框左上角的y坐标。 |
| height | number | 否 | 否 | 边界框高度，单位为像素。 |
| width | number | 否 | 否 | 边界框宽度，单位为像素。 |

## Point

PhonePC/2in1Tablet

二维平面上的点。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 点的横坐标。 |
| y | number | 否 | 否 | 点的纵坐标。 |

## Orientation

PhonePC/2in1Tablet

表示三维平面上的朝向。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| yaw | number | 否 | 否 | 表示绕垂直轴（Y轴）旋转的角度，也称为“偏航角”，决定了物体在水平面上的朝向。取值范围[-180,180]。 |
| pitch | number | 否 | 否 | 表示绕水平轴（X轴）旋转的角度，也称为“俯仰角”，决定了物体在垂直平面上的朝向。取值范围[-180,180]。 |
| roll | number | 否 | 否 | 表示绕前后轴（Z轴）旋转的角度，也称为“翻滚角”，决定了物体在前后方向上的朝向。取值范围[-180,180]。 |

## DownloadStartData

PhonePC/2in1Tablet

下载开始事件的数据结构，当AI模型开始下载时触发，告知开发者哪个资源开始下载。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resId | string | 否 | 否 | 资源标识符，用于标识正在下载的模型。 |

## DownloadCompleteData

PhonePC/2in1Tablet

模型下载完成时触发的下载完成事件的数据结构。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resId | string | 否 | 否 | 资源标识符。 |
| resVersion | string | 否 | 否 | 资源版本号。 |

## DownloadCancelData

PhonePC/2in1Tablet

下载过程被取消时触发的下载取消事件的数据结构。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resId | string | 否 | 否 | 资源标识符。 |

## DownloadStatusData

PhonePC/2in1Tablet

下载状态事件的数据结构，用于报告下载过程中的各种状态，比如网络错误、参数无效等。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resId | string | 否 | 否 | 资源标识符。 |
| statusCode | [downloadStatusCode](core-vision-vision-base-api.md#downloadstatuscode) | 否 | 否 | 状态码。 |
| message | string | 否 | 否 | 状态描述信息。无固定描述。 |

## DownloadProgressData

PhonePC/2in1Tablet

下载进度事件的数据结构，用于报告下载进度，让开发者能够实时显示下载进度。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resId | string | 否 | 否 | 资源标识符。 |
| progressInfo | string | 否 | 否 | 进度信息。 |

## downloadStatusCode

PhonePC/2in1Tablet

下载状态的枚举类。该字段为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PARAMETER\_INVALID | 0 | 传入的下载参数有误，比如资源ID格式错误，建议检查传入参数的格式和有效性。 |
| NO\_NETWORK\_STATUS | 1 | 设备离线或网络不可用，建议提示用户检查网络连接。 |
| NO\_MODEL | 2 | 服务器上找不到对应的模型文件，建议验证模型资源ID是否正确，确认服务器上模型文件是否存在。 |
| COPY\_FILE\_FAILED | 3 | 下载后无法将模型文件复制到指定位置，建议检查存储权限和可用空间。 |
| DOWNLOAD\_NOT\_ALLOWED | 4 | 需要用户确认的场合，用户已选择拒绝。 |
| DOWNLOAD\_TIME\_OUT | 5 | 网络较慢或服务器响应延迟。 |
| DOWNLOAD\_EXCEPTION | 6 | 下载过程中出现错误，任何其他未明确分类的错误。 |
| DOWNLOAD\_BACK\_TO\_DESKTOP | 7 | 用户在下载过程中切换出应用。 |
| TASK\_BUSY | 8 | 系统繁忙，正在执行另一个任务。  **起始版本：** 6.0.0(20) |

## Request

PhonePC/2in1Tablet

入参变量的基类。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputData | [InputData](core-vision-vision-base-api.md#inputdata) | 否 | 否 | 待识别的图片。可以是单个对象或多个对象的数组。 |
| scene | [SceneMode](core-vision-vision-base-api.md#scenemode) | 否 | 是 | 请求的场景模式。  该参数为预留字段，暂未实现。 |
| requestId | string | 否 | 是 | 请求的标识。用于开发者跟踪和管理自己的请求。  该参数为预留字段，暂未实现。 |

## Response

PhonePC/2in1Tablet

响应基类，作为能力请求的返回结果。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestId | string | 否 | 是 | 请求的唯一标识。开发者可用来跟踪和管理自己的请求。 |

## Analyzer

PhonePC/2in1Tablet

Analyzer基类，充当能力引擎。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

### destroy

PhonePC/2in1Tablet

destroy(): Promise<void>

用于销毁多种视觉能力的进程。使用Promise异步回调。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，销毁接口无返回值。 |

**示例：**

请参见[ObjectDetection.destroy](core-vision-object-detection-api.md#destroy)

## on('downloadStart')

PhonePC/2in1Tablet

on(type: 'downloadStart', callback: Callback<DownloadStartData>): void

下载开始事件监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadStart'。监听模型开始下载事件。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadStartData](core-vision-vision-base-api.md#downloadstartdata)> | 是 | Callback回调返回是哪个资源开始下载。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. visionBase.on('downloadStart', (data) => {
4. console.info(`资源 ${data.resId} 开始下载`);
5. });

7. @Entry
8. @Component
9. struct Page {
10. build() {
11. Column(){
12. Button('Button').onClick(() => {

14. })
15. }
16. }
17. }
```

## on('downloadComplete')

PhonePC/2in1Tablet

on(type: 'downloadComplete', callback: Callback<DownloadCompleteData>): void

下载完成事件监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadComplete'。监听模型下载完成事件。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadCompleteData](core-vision-vision-base-api.md#downloadcompletedata)> | 是 | Callback回调返回完成下载的资源标识符及版本。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. visionBase.on('downloadComplete', (data) => {
4. console.info(`资源 ${data.resId} 下载完成，版本：${data.resVersion}`);
5. });

7. @Entry
8. @Component
9. struct Page {
10. build() {
11. Column(){
12. Button('Button').onClick(() => {

14. })
15. }
16. }
17. }
```

## on( 'downloadCancel')

PhonePC/2in1Tablet

on(type: 'downloadCancel', callback: Callback<DownloadCancelData>): void

下载取消事件监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadCancel'。监听模型取消下载事件。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadCancelData](core-vision-vision-base-api.md#downloadcanceldata)> | 是 | Callback回调返回是哪个资源取消下载。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. visionBase.on('downloadCancel', (data) => {
4. console.info(`资源 ${data.resId} 下载已取消`);
5. });

7. @Entry
8. @Component
9. struct Page {
10. build() {
11. Column(){
12. Button('Button').onClick(() => {

14. })
15. }
16. }
17. }
```

## on( 'downloadStatus')

PhonePC/2in1Tablet

on(type: 'downloadStatus', callback: Callback<DownloadStatusData>): void

下载状态事件监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadStatus'。监听模型下载状态事件。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadStatusData](core-vision-vision-base-api.md#downloadstatusdata)> | 是 | Callback回调返回下载状态信息。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. visionBase.on('downloadStatus', (data) => {
4. console.info(`资源 ${data.resId} 下载状态：${data.statusCode}, ${data.message}`);
5. });

7. @Entry
8. @Component
9. struct Page {
10. build() {
11. Column(){
12. Button('Button').onClick(() => {

14. })
15. }
16. }
17. }
```

## on('downloadProgress')

PhonePC/2in1Tablet

on(type: 'downloadProgress', callback: Callback<DownloadProgressData>): void

下载进度事件监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadProgress'。监听模型下载进度事件。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadProgressData](core-vision-vision-base-api.md#downloadprogressdata)> | 是 | Callback回调返回下载进度信息。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. visionBase.on('downloadProgress', (data) => {
4. console.info(`资源 ${data.resId} 下载进度：${data.progressInfo}`);
5. })

7. @Entry
8. @Component
9. struct Page {
10. build() {
11. Column(){
12. Button('Button').onClick(() => {

14. })
15. }
16. }
17. }
```

## off('downloadStart')

PhonePC/2in1Tablet

off(type: 'downloadStart', callback?: Callback<DownloadStartData>): void

取消监听开始下载事件。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadStart'。取消开始下载事件的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadStartData](core-vision-vision-base-api.md#downloadstartdata)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. // 定义回调函数
4. const startCallback = (data: visionBase.DownloadStartData) => {
5. console.info(`资源 ${data.resId} 开始下载`);
6. };
7. // 注册监听器
8. visionBase.on('downloadStart', startCallback);
9. // 移除特定的监听器
10. visionBase.off('downloadStart', startCallback);

12. @Entry
13. @Component
14. struct Page {
15. build() {
16. Column(){
17. Button('Button').onClick(() => {

19. })
20. }
21. }
22. }
```

## off('downloadComplete')

PhonePC/2in1Tablet

off(type: 'downloadComplete', callback?: Callback<DownloadCompleteData>): void

取消监听完成下载事件。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadComplete'。取消下载事件完成的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadCompleteData](core-vision-vision-base-api.md#downloadcompletedata)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. // 定义回调函数
4. const callback = (data: visionBase.DownloadCompleteData) => {
5. console.info(`资源 ${data.resId} 下载完成`);
6. };
7. // 注册监听器
8. visionBase.on('downloadComplete', callback);
9. // 移除特定的监听器
10. visionBase.off('downloadComplete', callback);

12. @Entry
13. @Component
14. struct Page {
15. build() {
16. Column(){
17. Button('Button').onClick(() => {

19. })
20. }
21. }
22. }
```

## off('downloadCancel')

PhonePC/2in1Tablet

off(type: 'downloadCancel', callback?: Callback<DownloadCancelData>): void

取消对下载取消事件的监听。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadCancel'。取消对下载取消事件的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadCancelData](core-vision-vision-base-api.md#downloadcanceldata)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. // 定义回调函数
4. const callback = (data: visionBase.DownloadCancelData) => {
5. console.info(`资源 ${data.resId} 下载取消`);
6. };
7. // 注册监听器
8. visionBase.on('downloadCancel', callback);
9. // 移除特定的监听器
10. visionBase.off('downloadCancel', callback);

12. @Entry
13. @Component
14. struct Page {
15. build() {
16. Column(){
17. Button('Button').onClick(() => {

19. })
20. }
21. }
22. }
```

## off('downloadStatus')

PhonePC/2in1Tablet

off(type: 'downloadStatus', callback?: Callback<DownloadStatusData>): void

取消监听下载状态事件。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadStatus'。取消对下载状态事件的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadStatusData](core-vision-vision-base-api.md#downloadstatusdata)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. // 定义回调函数
4. const callback = (data: visionBase.DownloadStatusData) => {
5. console.info(`资源 ${data.resId} 下载状态`);
6. };
7. // 注册监听器
8. visionBase.on('downloadStatus', callback);
9. // 移除特定的监听器
10. visionBase.off('downloadStatus', callback);

12. @Entry
13. @Component
14. struct Page {

16. build() {
17. Column(){
18. Button('Button').onClick(() => {

20. })
21. }
22. }
23. }
```

## off('downloadProgress')

PhonePC/2in1Tablet

off(type: 'downloadProgress', callback?: Callback<DownloadProgressData>): void

取消监听下载进度事件。该方法为预留接口，当前版本暂不支持。

**系统能力：** SystemCapability.AI.Vision.VisionBase

**起始版本：** 5.0.2(14)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定字符串 'downloadProgress'。取消对下载进度事件的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[DownloadProgressData](core-vision-vision-base-api.md#downloadprogressdata)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. |

**示例：**

```
1. import { visionBase } from '@kit.CoreVisionKit';

3. // 定义回调函数
4. const callback = (data: visionBase.DownloadProgressData) => {
5. console.info(`资源 ${data.resId} 下载进度`);
6. };
7. // 注册监听器
8. visionBase.on('downloadProgress', callback);
9. // 移除特定的监听器
10. visionBase.off('downloadProgress', callback);

12. @Entry
13. @Component
14. struct Page {

16. build() {
17. Column(){
18. Button('Button').onClick(() => {

20. })
21. }
22. }
23. }
```
