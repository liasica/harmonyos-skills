---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder
title: Interface (AVScreenCaptureRecorder)
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > ArkTS API > @ohos.multimedia.media (媒体服务) > Interface (AVScreenCaptureRecorder)
category: harmonyos-references
scraped_at: 2026-04-28T08:13:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5503c64c785c0316cb5a2c03a15ab4918d395f9b8abc350045e646f0800570fe
---

屏幕录制管理类，用于进行屏幕录制。在调用AVScreenCaptureRecorder的方法前，需要先通过[createAVScreenCaptureRecorder()](arkts-apis-media-f.md#mediacreateavscreencapturerecorder12)创建一个AVScreenCaptureRecorder实例。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { media } from '@kit.MediaKit';
```

## init12+

PhonePC/2in1TabletTV

init(config: AVScreenCaptureRecordConfig): Promise<void>

进行录屏初始化，设置录屏参数。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [AVScreenCaptureRecordConfig](arkts-apis-media-i.md#avscreencapturerecordconfig12) | 是 | 配置屏幕录制的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import fileIo from '@ohos.file.fs';
3. import { media } from '@kit.MediaKit';

5. // 初始化avScreenCaptureRecorder。
6. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
7. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
8. if (captureRecorder != null) {
9. avScreenCaptureRecorder = captureRecorder;
10. console.info('Succeeded in creating avScreenCaptureRecorder');
11. } else {
12. console.error('Failed to create avScreenCaptureRecorder');
13. }
14. }).catch((error: BusinessError) => {
15. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
16. });

18. // 创建文件。
19. let filesDir = '/data/storage/el2/base/haps';
20. let file = fileIo.openSync(filesDir + '/screenCapture.mp4', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);

22. let avCaptureConfig: media.AVScreenCaptureRecordConfig = {
23. fd: file.fd, // 文件需要先由调用者创建，通常是MP4文件，赋予写权限，将文件fd传给此参数。
24. frameWidth: 640,
25. frameHeight: 480
26. // 补充其他参数。
27. };

29. if (avScreenCaptureRecorder != undefined) {
30. avScreenCaptureRecorder.init(avCaptureConfig).then(() => {
31. console.info('Succeeded in initializing avScreenCaptureRecorder');
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to init avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
34. });
35. }
```

## startRecording12+

PhonePC/2in1TabletTV

startRecording(): Promise<void>

开始录屏，在使用前需要先调用[init](arkts-apis-media-avscreencapturerecorder.md#init12)接口。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用startRecording方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.startRecording().then(() => {
21. console.info('Succeeded in starting avScreenCaptureRecorder');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to start avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## stopRecording12+

PhonePC/2in1TabletTV

stopRecording(): Promise<void>

结束录屏。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用stopRecording方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.stopRecording().then(() => {
21. console.info('Succeeded in stopping avScreenCaptureRecorder');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to stop avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## skipPrivacyMode12+

PhonePC/2in1TabletTV

skipPrivacyMode(windowIDs: Array<number>): Promise<void>

录屏时，应用可对本应用的隐私窗口做安全豁免。使用Promise异步回调。

如录屏时，用户在本应用进行输入密码等操作，应用不会进行黑屏处理。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowIDs | Array<number> | 是 | 需要豁免隐私的窗口列表，包括主窗口id和子窗口id，窗口属性获取方法可以参考[getWindowProperties](arkts-apis-window-window.md#getwindowproperties9)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用skipPrivacyMode方法。
19. if (avScreenCaptureRecorder != undefined) {
20. let windowIDs = [];
21. avScreenCaptureRecorder.skipPrivacyMode(windowIDs).then(() => {
22. console.info('Succeeded in skipping privacy mode');
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to skip privacy mode. Code: ${err.code}, message: ${err.message}`);
25. });
26. }
```

## setMicEnabled12+

PhonePC/2in1TabletTV

setMicEnabled(enable: boolean): Promise<void>

设置麦克风开关。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 麦克风开关控制，true代表麦克风打开，false代表麦克风关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用setMicEnabled方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.setMicEnabled(true).then(() => {
21. console.info('Succeeded in setting microphone enabled.');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to set microphone enabled. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## setPickerMode22+

PhonePC/2in1TabletTV

setPickerMode(pickerMode: PickerMode): Promise<void>

设置Picker显示模式，在下一次显示Picker时生效。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pickerMode | [PickerMode](arkts-apis-media-e.md#pickermode22) | 是 | 选择Picker模式。  定义了在Picker中显示的内容类型：  - SCREEN\_ONLY：仅显示屏幕列表。  - WINDOW\_ONLY：仅显示窗口列表。  - SCREEN\_AND\_WINDOW：同时显示屏幕列表和窗口列表（默认值）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用setPickerMode方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.setPickerMode(media.PickerMode.WINDOW_ONLY).then(() => {
21. console.info('Succeeded in setting picker mode.');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to set picker mode. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## excludePickerWindows22+

PhonePC/2in1TabletTV

excludePickerWindows(excludedWindows: Array<number>): Promise<void>

设置在Picker中隐藏的窗口列表，在下一次显示Picker时生效。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| excludedWindows | Array<number> | 是 | 需要在Picker中隐藏的窗口列表，窗口属性获取方法可以参考[getWindowProperties](arkts-apis-window-window.md#getwindowproperties9)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let excludedWindows: Array<number> = [101, 102, 103];

5. // 初始化avScreenCaptureRecorder。
6. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
7. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
8. if (captureRecorder != null) {
9. avScreenCaptureRecorder = captureRecorder;
10. console.info('Succeeded in creating avScreenCaptureRecorder');
11. } else {
12. console.error('Failed to create avScreenCaptureRecorder');
13. }
14. }).catch((error: BusinessError) => {
15. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
16. });

18. // 其余流程。

20. // 调用excludePickerWindows方法。
21. if (avScreenCaptureRecorder != undefined) {
22. avScreenCaptureRecorder.excludePickerWindows(excludedWindows).then(() => {
23. console.info('Succeeded in excluding picker windows.');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to exclude picker windows. Code: ${err.code}, message: ${err.message}`);
26. });
27. }
```

## presentPicker22+

PhonePC/2in1TabletTV

presentPicker(): Promise<void>

录屏开始后，调用该接口再次弹出Picker，可动态更新录制源（窗口、屏幕）。使用Promise异步回调。

说明

* 更新录制源过程中，原录制流程不中断。
* 通过picker动态更新录制源后，按照新的录制源进行录制。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用presentPicker方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.presentPicker().then(() => {
21. console.info('Succeeded in presenting picker avScreenCaptureRecorder.');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to present picker avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## release12+

PhonePC/2in1TabletTV

release(): Promise<void>

释放录屏。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | IO error. Return by promise. |
| 5400105 | Service died. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用release方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.release().then(() => {
21. console.info('Succeeded in releasing avScreenCaptureRecorder');
22. }).catch((err: BusinessError) => {
23. console.error(`Failed to release avScreenCaptureRecorder. Code: ${err.code}, message: ${err.message}`);
24. });
25. }
```

## on('stateChange')12+

PhonePC/2in1TabletTV

on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void

订阅录屏状态切换的事件，当状态发生的时候，会通过订阅的回调通知用户。用户只能订阅一个状态切换的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | Callback<[AVScreenCaptureStateCode](arkts-apis-media-e.md#avscreencapturestatecode12)> | 是 | 状态切换事件回调方法，[AVScreenCaptureStateCode](arkts-apis-media-e.md#avscreencapturestatecode12)表示切换到的状态。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用on方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.on('stateChange', (state: media.AVScreenCaptureStateCode) => {
21. console.info('avScreenCaptureRecorder stateChange to ' + state);
22. });
23. }
```

## on('error')12+

PhonePC/2in1TabletTV

on(type: 'error', callback: ErrorCallback): void

订阅AVScreenCaptureRecorder的错误事件，用户可以根据应用自身逻辑对错误事件进行处理。用户只能订阅一个错误事件的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | 录屏错误事件回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permission denied. |
| 5400103 | IO error. Return by ErrorCallback. |
| 5400105 | Service died. Return by ErrorCallback. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用on方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.on('error', (err: BusinessError) => {
21. console.error(`avScreenCaptureRecorder error: Code: ${err.code}, message: ${err.message}`);
22. });
23. }
```

## off('stateChange')12+

PhonePC/2in1TabletTV

off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void

取消订阅状态切换回调事件。用户可以指定填入状态切换的回调方法来取消订阅。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'stateChange'。 |
| callback | Callback<[AVScreenCaptureStateCode](arkts-apis-media-e.md#avscreencapturestatecode12)> | 否 | 状态切换事件回调方法，[AVScreenCaptureStateCode](arkts-apis-media-e.md#avscreencapturestatecode12)表示切换到的状态，不填此参数则会取消最后一次订阅事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用off方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.off('stateChange');
21. }
```

## off('error')12+

PhonePC/2in1TabletTV

off(type: 'error', callback?: ErrorCallback): void

取消订阅错误回调事件。用户可以指定填入错误回调方法来取消订阅。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态切换事件回调类型，支持的事件：'error'。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 录屏错误事件回调方法，不填此参数则会取消最后一次订阅事件。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 初始化avScreenCaptureRecorder。
4. let avScreenCaptureRecorder: media.AVScreenCaptureRecorder | undefined;
5. media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
6. if (captureRecorder != null) {
7. avScreenCaptureRecorder = captureRecorder;
8. console.info('Succeeded in creating avScreenCaptureRecorder');
9. } else {
10. console.error('Failed to create avScreenCaptureRecorder');
11. }
12. }).catch((error: BusinessError) => {
13. console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
14. });

16. // 其余流程。

18. // 调用off方法。
19. if (avScreenCaptureRecorder != undefined) {
20. avScreenCaptureRecorder.off('error');
21. }
```
