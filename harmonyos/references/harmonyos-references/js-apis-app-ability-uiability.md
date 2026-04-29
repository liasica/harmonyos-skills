---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability
title: @ohos.app.ability.UIAbility (带界面的应用组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.UIAbility (带界面的应用组件)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d5315cd803c64746f9af574d18b55e36a868530c82aa5a73090f3ff832c388a
---

UIAbility是包含UI界面的应用组件，继承自[Ability](js-apis-app-ability-ability.md)，提供UIAbility组件创建、销毁、前后台切换等[生命周期](js-apis-app-ability-uiability.md#uiability生命周期状态)回调，同时也具备[后台通信能力](js-apis-app-ability-uiability.md#后台通信能力)。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

## UIAbility生命周期状态

PhonePC/2in1TabletTVWearable

**图1** UIAbility生命周期状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/3j9ShAlmRQ6ammBCOJgsRQ/zh-cn_image_0000002558606258.png?HW-CC-KV=V1&HW-CC-Date=20260429T054833Z&HW-CC-Expire=86400&HW-CC-Sign=7EFD98D0AAAE93C9A7C6B585062F3B8476ADB35659D5E87C57843F7288D3AD9E)

* Create：表示UIAbility实例已创建。系统会在该状态下触发其[onCreate](js-apis-app-ability-uiability.md#oncreate)回调函数，开发者可以在[onCreate](js-apis-app-ability-uiability.md#oncreate)中执行初始化操作。
* Foreground：表示UIAbility被拉到前台。系统会在该状态下触发其[onForeground](js-apis-app-ability-uiability.md#onforeground)回调函数，开发者可以在[onForeground](js-apis-app-ability-uiability.md#onforeground)中申请应用所需的资源。
* Background：表示UIAbility被拉到后台。系统会在该状态下触发其[onBackground](js-apis-app-ability-uiability.md#onbackground)回调函数，开发者可以在[onBackground](js-apis-app-ability-uiability.md#onbackground)中释放一些应用资源。
* Destroy：表示UIAbility实例即将销毁。系统会在该状态下触发其[onDestroy](js-apis-app-ability-uiability.md#ondestroy)回调函数，开发者可以在[onDestroy](js-apis-app-ability-uiability.md#ondestroy)中执行数据保存等操作。

## 后台通信能力

PhonePC/2in1TabletTVWearable

通过Call调用可以与目标UIAbility进行后台通信。Call调用示意图如下所示。

**图2** Call调用示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/OADd81FtTRKi9DO3eMV9EA/zh-cn_image_0000002589323851.png?HW-CC-KV=V1&HW-CC-Date=20260429T054833Z&HW-CC-Expire=86400&HW-CC-Sign=56DBD4FA81564BD2E007ACE78CEDCDE34B94279E08B61E1875D9A7AFDB9F0706)

* Caller UIAbility调用[startAbilityByCall()](js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口获取[Caller](js-apis-app-ability-uiability.md#caller)对象，并使用Caller对象的[call](js-apis-app-ability-uiability.md#call)方法向Callee UIAbility发送数据。
* Callee UIAbility持有一个[Callee](js-apis-app-ability-uiability.md#callee)对象，通过Callee的[on](js-apis-app-ability-uiability.md#on)方法注册回调函数，用于接收Caller对象发送的数据。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { UIAbility } from '@kit.AbilityKit';
```

## UIAbility

PhonePC/2in1TabletTVWearable

表示包含UI界面的应用组件，提供组件创建、销毁、前后台切换等生命周期回调，同时也具备后台通信能力。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 否 | 否 | UIAbility的上下文。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| launchWant | [Want](js-apis-app-ability-want.md) | 否 | 否 | UIAbility[冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)时接收到的Want参数，取值为[onCreate](js-apis-app-ability-uiability.md#oncreate)接收到的Want参数。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| lastRequestWant | [Want](js-apis-app-ability-want.md) | 否 | 否 | 最近一次拉起UIAbility请求的Want参数。  - 首次拉起UIAbility时，取值为[onCreate](js-apis-app-ability-uiability.md#oncreate)接收到的Want参数。  - 重复拉起UIAbility时，取值为[onNewWant](js-apis-app-ability-uiability.md#onnewwant)最近一次接收到的Want参数。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| callee | [Callee](js-apis-app-ability-uiability.md#callee) | 否 | 否 | 系统为UIAbility创建的后台通信对象，Callee UIAbility（被调用方）可以通过Callee对象接收Caller对象发送的数据。 |
| specifiedId23+ | string | 否 | 是 | 仅当UIAbility启动模式为[specified](../harmonyos-guides/uiability-launch-type.md#specified启动模式)时存在，取值为开发者自定义的UIAbility标识。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void

当UIAbility实例创建完成时，系统会触发该回调，开发者可在该回调中执行初始化逻辑（如定义变量、加载资源等）。该回调仅会在UIAbility[冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)时触发。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 调用方拉起该UIAbility时传递的数据。 |
| launchParam | [AbilityConstant.LaunchParam](js-apis-app-ability-abilityconstant.md#launchparam) | 是 | 应用启动参数，包含应用启动原因、应用上次退出原因等。 |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class MyUIAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. // 执行异步任务
7. hilog.info(0x0000, 'testTag',
8. `onCreate, want: ${want.abilityName}, the launchReason is ${launchParam.launchReason}, the lastExitReason is ${launchParam.lastExitReason}`);
9. }
10. }
```

### onWindowStageCreate

PhonePC/2in1TabletTVWearable

onWindowStageCreate(windowStage: window.WindowStage): void

当[WindowStage](arkts-apis-window-windowstage.md)实例创建完成后，系统会触发该回调。开发者可以在该回调中通过WindowStage加载页面。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | WindowStage实例对象。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. export default class MyUIAbility extends UIAbility {
6. // 主窗口已创建，为该UIAbility设置主页面
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', (err, data) => {
9. if (err.code) {
10. hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err)}`);
11. return;
12. }
13. hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data)}`);
14. });
15. }
16. }
```

### onWindowStageWillDestroy12+

PhonePC/2in1TabletTVWearable

onWindowStageWillDestroy(windowStage: window.WindowStage): void

当WindowStage即将销毁时，系统触发该回调。开发者可以在该生命周期中取消windowStage事件的监听。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | WindowStage实例对象。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. export default class MyUIAbility extends UIAbility {
6. onWindowStageWillDestroy(windowStage: window.WindowStage) {
7. hilog.info(0x0000, 'testTag', `onWindowStageWillDestroy`);
8. }
9. }
```

### onWindowStageDestroy

PhonePC/2in1TabletTVWearable

onWindowStageDestroy(): void

当WindowStage销毁后，系统触发该回调。该回调用于通知开发者WindowStage对象已被销毁，不能再继续使用。

仅当UIAbility正常退出时会触发该回调，异常退出场景（例如低内存终止进程）不会触发该回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class MyUIAbility extends UIAbility {
5. onWindowStageDestroy() {
6. // 主窗口已销毁，释放UI相关资源
7. hilog.info(0x0000, 'testTag', `onWindowStageDestroy`);
8. }
9. }
```

### onWindowStageRestore

PhonePC/2in1TabletTVWearable

onWindowStageRestore(windowStage: window.WindowStage): void

当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时回调。

说明

在应用迁移启动时，无论是[冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)还是[热启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability热启动)，都会在执行完[onCreate()](js-apis-app-ability-uiability.md#oncreate)/[onNewWant()](js-apis-app-ability-uiability.md#onnewwant)后，触发onWindowStageRestore()生命周期函数，不执行onWindowStageCreate()生命周期函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | WindowStage实例对象。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. export default class MyUIAbility extends UIAbility {
6. onWindowStageRestore(windowStage: window.WindowStage) {
7. hilog.info(0x0000, 'testTag', `onWindowStageRestore`);
8. }
9. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void | Promise<void>

当UIAbility被销毁（例如使用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)接口停止UIAbility）时，系统触发该回调。开发者可以在该生命周期中执行资源清理、数据保存等相关操作。

使用同步回调或Promise异步回调。

说明

* 在执行完onDestroy生命周期回调后，应用可能会退出，从而导致其中的异步函数（比如异步写入数据库）未能正确执行。在此情况下，推荐使用Promise异步回调。
* 该回调仅在UIAbility正常退出时触发，当UIAbility异常退出（例如低内存终止进程）时，该回调将不被触发。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回结果或无返回结果的Promise对象。 |

**示例：**

* 同步回调示例如下：

  ```
  1. import { UIAbility } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';

  4. export default class MyUIAbility extends UIAbility {
  5. onDestroy() {
  6. hilog.info(0x0000, 'testTag', `onDestroy`);
  7. // 调用同步函数...
  8. }
  9. }
  ```
* Promise异步回调示例如下：

  ```
  1. import { UIAbility } from '@kit.AbilityKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';

  4. export default class MyUIAbility extends UIAbility {
  5. async onDestroy() {
  6. hilog.info(0x0000, 'testTag', `onDestroy`);
  7. // 调用异步函数...
  8. }
  9. }
  ```

### onWillForeground20+

PhonePC/2in1TabletTVWearable

onWillForeground(): void

UIAbility生命周期回调，应用转到前台前触发，在[onForeground](js-apis-app-ability-uiability.md#onforeground)前被调用。可在该回调中实现采集应用开始进入前台的时间。如果与[onDidForeground](js-apis-app-ability-uiability.md#ondidforeground20)配合使用，还可以统计出从应用开始进入前台到切换至前台状态的耗时。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. // ...

8. onWillForeground(): void {
9. // 应用开始进入前台事件打点
10. let eventParams: Record<string, number> = { 'xxxx': 100 };
11. let eventInfo: hiAppEvent.AppEventInfo = {
12. // 事件领域定义
13. domain: "lifecycle",
14. // 事件名称定义
15. name: "onwillforeground",
16. // 事件类型定义
17. eventType: hiAppEvent.EventType.BEHAVIOR,
18. // 事件参数定义
19. params: eventParams,
20. };
21. hiAppEvent.write(eventInfo).then(() => {
22. hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
23. }).catch((err: BusinessError) => {
24. hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
25. });
26. }

28. // ...

30. onDidForeground(): void {
31. // 应用进入前台后事件打点
32. let eventParams: Record<string, number> = { 'xxxx': 100 };
33. let eventInfo: hiAppEvent.AppEventInfo = {
34. // 事件领域定义
35. domain: "lifecycle",
36. // 事件名称定义
37. name: "ondidforeground",
38. // 事件类型定义
39. eventType: hiAppEvent.EventType.BEHAVIOR,
40. // 事件参数定义
41. params: eventParams,
42. };
43. hiAppEvent.write(eventInfo).then(() => {
44. hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`);
45. }).catch((err: BusinessError) => {
46. hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`);
47. });
48. }
49. }
```

### onForeground

PhonePC/2in1TabletTVWearable

onForeground(): void

当应用首次启动到前台或者从后台转入到前台时，系统触发该回调。开发者可在该回调中实现系统所需资源的申请，如应用转到前台时申请定位服务等。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class MyUIAbility extends UIAbility {
5. onForeground() {
6. hilog.info(0x0000, 'testTag', `onForeground`);
7. }
8. }
```

### onDidForeground20+

PhonePC/2in1TabletTVWearable

onDidForeground(): void

UIAbility生命周期回调，应用转到前台后触发，在[onForeground](js-apis-app-ability-uiability.md#onforeground)后被调用，可在该回调中实现应用切换到前台后的时间打点。如果与[onWillForeground](js-apis-app-ability-uiability.md#onwillforeground20)配合使用，还可以统计出从应用开始进入前台到切换至前台状态的耗时。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

参考[onWillForeground](js-apis-app-ability-uiability.md#onwillforeground20)。

### onWillBackground20+

PhonePC/2in1TabletTVWearable

onWillBackground(): void

UIAbility生命周期回调，当应用从前台转到后台前触发，在[onBackground](js-apis-app-ability-uiability.md#onbackground)前被调用。可在该回调中实现数据打点，例如，打点应用运行过程中发生的故障信息、统计信息、安全信息、用户行为信息等。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MyUIAbility extends UIAbility {
6. onWillBackground(): void {
7. let eventParams: Record<string, number | string> = {
8. "int_data": 100,
9. "str_data": "strValue",
10. };
11. // 打点应用故障信息
12. hiAppEvent.write({
13. domain: "test_domain",
14. name: "test_event",
15. eventType: hiAppEvent.EventType.FAULT,
16. params: eventParams,
17. }, (err: BusinessError) => {
18. if (err) {
19. hilog.error(0x0000, 'testTag', `hiAppEvent code: ${err.code}, message: ${err.message}`);
20. return;
21. }
22. hilog.info(0x0000, 'testTag', `hiAppEvent success to write event`);
23. });
24. }
25. }
```

### onBackground

PhonePC/2in1TabletTVWearable

onBackground(): void

当应用从前台转入到后台时，系统触发该回调。开发者可在该回调中实现UI不可见时的资源释放操作，如停止定位功能等。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class MyUIAbility extends UIAbility {
5. onBackground() {
6. // UIAbility回到后台
7. hilog.info(0x0000, 'testTag', `onBackground`);
8. }
9. }
```

### onDidBackground20+

PhonePC/2in1TabletTVWearable

onDidBackground(): void

UIAbility生命周期回调，当应用从前台转到后台后触发，在[onBackground](js-apis-app-ability-uiability.md#onbackground)之后被调用。可在该回调中实现应用进入后台之后的资源释放操作，如进入后台后停止音频播放等。

同步接口，不支持异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { audio } from '@kit.AudioKit';

6. export default class MyUIAbility extends UIAbility {
7. static audioRenderer: audio.AudioRenderer;

9. // ...
10. onForeground(): void {
11. let audioStreamInfo: audio.AudioStreamInfo = {
12. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
13. channels: audio.AudioChannel.CHANNEL_2, // 通道。
14. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
15. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
16. };

18. let audioRendererInfo: audio.AudioRendererInfo = {
19. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
20. rendererFlags: 0 // 音频渲染器标志。
21. };

23. let audioRendererOptions: audio.AudioRendererOptions = {
24. streamInfo: audioStreamInfo,
25. rendererInfo: audioRendererInfo
26. };

28. // 在前台时申请audioRenderer，用于播放PCM（Pulse Code Modulation）音频数据
29. audio.createAudioRenderer(audioRendererOptions).then((data) => {
30. MyUIAbility.audioRenderer = data;
31. hilog.info(0x0000, 'testTag', `AudioRenderer Created : Success : Stream Type: SUCCESS.`);
32. }).catch((err: BusinessError) => {
33. hilog.error(0x0000, 'testTag', `AudioRenderer Created : F : ${JSON.stringify(err)}.`);
34. });
35. }

37. onDidBackground() {
38. // 转到后台后，释放audioRenderer资源
39. MyUIAbility.audioRenderer.release((err: BusinessError) => {
40. if (err) {
41. hilog.error(0x0000, 'testTag', `AudioRenderer release failed, error: ${JSON.stringify(err)}.`);
42. } else {
43. hilog.info(0x0000, 'testTag', `AudioRenderer released.`);
44. }
45. });
46. }
47. }
```

### onContinue

PhonePC/2in1TabletTVWearable

onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult>

当UIAbility准备跨端迁移时触发，可以保存待迁移的业务数据。

说明

对于API version 18（不含18） 之前版本仅支持同步调用，从API version 18及后续版本可支持异步调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | 开发者通过该参数保存待迁移的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityConstant.OnContinueResult](js-apis-app-ability-abilityconstant.md#oncontinueresult) | Promise<[AbilityConstant.OnContinueResult](js-apis-app-ability-abilityconstant.md#oncontinueresult)> | 表示是否同意迁移的结果：  - AGREE：表示同意。  - REJECT：表示拒绝，如应用在onContinue中异常可以返回REJECT。  - MISMATCH：表示版本不匹配，接续源端应用可以在onContinue中获取到迁移对端应用的版本号，进行协商后，如果版本不匹配导致无法迁移，可以返回该结果。  该回调与onWindowStageRestore成对出现。在接续场景下，源端的UIAbility触发onContinue保存自定义数据，在目标端UIAbility触发onWindowStageRestore恢复自定义数据。 |

**示例：**

* 应用迁移时使用同步接口进行数据保存，示例如下：

  ```
  1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

  3. export default class MyUIAbility extends UIAbility {
  4. onContinue(wantParams: Record<string, Object>) {
  5. console.info('onContinue');
  6. wantParams['myData'] = 'my1234567';
  7. return AbilityConstant.OnContinueResult.AGREE;
  8. }
  9. }
  ```
* 应用迁移时使用异步接口进行数据保存，示例如下：

  ```
  1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

  3. export default class MyUIAbility extends UIAbility {
  4. async setWant(wantParams: Record<string, Object>) {
  5. console.info('setWant start');
  6. for (let time = 0; time < 1000; ++time) {
  7. wantParams[time] = time;
  8. }
  9. console.info('setWant end');
  10. }

  12. async onContinue(wantParams: Record<string, Object>) {
  13. console.info('onContinue');
  14. return this.setWant(wantParams).then(() => {
  15. return AbilityConstant.OnContinueResult.AGREE;
  16. });
  17. }
  18. }
  ```

### onNewWant

PhonePC/2in1TabletTVWearable

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void

当已经启动的UIAbility实例再次被拉起时，系统会触发该回调。若在特定场景下（参见[Scenarios](js-apis-app-ability-contextconstant.md#scenarios20)），不需要触发该生命周期回调，可以使用[setOnNewWantSkipScenarios](js-apis-inner-application-uiabilitycontext.md#setonnewwantskipscenarios20)接口设置。

同步接口，不支持异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 调用方再次拉起该UIAbility时传递的数据。 |
| launchParam | [AbilityConstant.LaunchParam](js-apis-app-ability-abilityconstant.md#launchparam) | 是 | UIAbility启动参数，包含启动原因等。 |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

3. export default class MyUIAbility extends UIAbility {
4. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. console.info(`onNewWant, want: ${want.abilityName}`);
6. console.info(`onNewWant, launchParam: ${JSON.stringify(launchParam)}`);
7. }
8. }
```

### onDump

PhonePC/2in1TabletTVWearable

onDump(params: Array<string>): Array<string>

应用调测场景下，通过命令行dump UIAbility数据时，系统会触发该回调。开发者可以在该回调中返回UIAbility要转储的非敏感信息。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<string> | 是 | 表示dump命令参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回的dump信息。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyUIAbility extends UIAbility {
4. onDump(params: Array<string>) {
5. console.info(`dump, params: ${JSON.stringify(params)}`);
6. return ['params'];
7. }
8. }
```

### onSaveState

PhonePC/2in1TabletTVWearable

onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult

该接口需要与[appRecovery](js-apis-app-ability-apprecovery.md)配合使用。如果应用已使能故障恢复功能（即[enableAppRecovery](js-apis-app-ability-apprecovery.md#apprecoveryenableapprecovery)接口中的saveOccasion参数设置为SAVE\_WHEN\_ERROR），当应用出现故障时，系统将触发该回调来保存UIAbility的数据。

说明

从API version 20开始，当[onSaveStateAsync](js-apis-app-ability-uiability.md#onsavestateasync20)实现时，本回调函数将不执行。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [AbilityConstant.StateType](js-apis-app-ability-abilityconstant.md#statetype) | 是 | 触发应用保存状态的原因，当前仅支持APP\_RECOVERY（即应用故障恢复场景）。 |
| wantParam | Record<string, Object> | 是 | 用户自定义的应用状态数据，应用再启动时被保存在[onCreate](js-apis-app-ability-uiability.md#oncreate)的Want.parameters中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityConstant.OnSaveResult](js-apis-app-ability-abilityconstant.md#onsaveresult) | 返回一个数据保存策略的对象（如全部拒绝、全部允许、只允许故障恢复场景等）。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyUIAbility extends UIAbility {
4. onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>) {
5. console.info('onSaveState');
6. wantParam['myData'] = 'my1234567';
7. return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
8. }
9. }
```

### onSaveStateAsync20+

PhonePC/2in1TabletTVWearable

onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>

该接口需要与[appRecovery](js-apis-app-ability-apprecovery.md)配合使用。如果应用已使能故障恢复功能（即[enableAppRecovery](js-apis-app-ability-apprecovery.md#apprecoveryenableapprecovery)接口中的saveOccasion参数设置为SAVE\_WHEN\_ERROR），当应用出现故障时，将触发该回调来保存UIAbility的数据。使用Promise异步回调。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stateType | [AbilityConstant.StateType](js-apis-app-ability-abilityconstant.md#statetype) | 是 | 触发应用保存状态的原因，当前仅支持APP\_RECOVERY（即应用故障恢复场景）。 |
| wantParam | Record<string, Object> | 是 | 用户自定义的应用状态数据，应用再启动时被保存在[onCreate](js-apis-app-ability-uiability.md#oncreate)的Want.parameters中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityConstant.OnSaveResult](js-apis-app-ability-abilityconstant.md#onsaveresult)> | Promise对象。返回一个数据保存策略的对象（如全部拒绝、全部允许、只允许故障恢复场景等）。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. class MyUIAbility extends UIAbility {
4. async onSaveStateAsync(reason: AbilityConstant.StateType,
5. wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult> {
6. await new Promise<string>((res, rej) => {
7. setTimeout(res, 1000); // 延时1秒后执行
8. });
9. return AbilityConstant.OnSaveResult.RECOVERY_AGREE;
10. }
11. }
```

### onShare10+

PhonePC/2in1TabletTVWearable

onShare(wantParam: Record<string, Object>): void

当跨端分享元服务时，系统触发该回调。开发者可以在该回调中设置待分享元服务的标题、摘要和URL等数据。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | 待分享的数据。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class MyUIAbility extends UIAbility {
4. onShare(wantParams: Record<string, Object>) {
5. console.info('onShare');
6. wantParams['ohos.extra.param.key.shareUrl'] = 'example.com';
7. }
8. }
```

### onPrepareToTerminate10+

PhonePC/2in1TabletTVWearable

onPrepareToTerminate(): boolean

在UIAbility即将关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)接口关闭。例如，询问用户是否确认关闭UIAbility，再主动销毁UIAbility。

说明

* 从API version 15开始，当[UIAbility.onPrepareToTerminateAsync](js-apis-app-ability-uiability.md#onpreparetoterminateasync15)实现时，本回调函数将不执行。当[AbilityStage.onPrepareTerminationAsync](js-apis-app-ability-abilitystage.md#onprepareterminationasync15)或[AbilityStage.onPrepareTermination](js-apis-app-ability-abilitystage.md#onpreparetermination15)实现时，在dock栏或系统托盘处右键点击关闭，本回调函数将不执行。
* 如果应用本身或者所使用的三方框架注册了[window.WindowStage.on('windowStageClose')](arkts-apis-window-windowstage.md#onwindowstageclose14)监听，本回调函数将不执行。

**需要权限**：ohos.permission.PREPARE\_APP\_TERMINATE

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常执行回调，在其他设备上不执行回调。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否执行UIAbility关闭操作，返回true表示本次UIAbility关闭流程取消，返回false表示UIAbility继续正常关闭。 |

**示例：**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onPrepareToTerminate() {
6. // 开发者定义预关闭动作
7. // 例如拉起另一个ability，根据ability处理结果执行异步关闭
8. let want: Want = {
9. bundleName: "com.example.myapplication",
10. moduleName: "entry",
11. abilityName: "SecondAbility"
12. }
13. this.context.startAbilityForResult(want)
14. .then((result) => {
15. // 获取ability处理结果，当返回结果的resultCode为0关闭当前UIAbility
16. console.info('startAbilityForResult success, resultCode is ' + result.resultCode);
17. if (result.resultCode === 0) {
18. this.context.terminateSelf();
19. }
20. }).catch((err: BusinessError) => {
21. // 异常处理
22. console.error('startAbilityForResult failed, err:' + JSON.stringify(err));
23. this.context.terminateSelf();
24. })

26. return true; // 已定义预关闭操作后，返回true表示UIAbility取消关闭
27. }
28. }
```

### onPrepareToTerminateAsync15+

PhonePC/2in1TabletTVWearable

onPrepareToTerminateAsync(): Promise<boolean>

在UIAbility关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。

开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)接口关闭。例如，询问用户是否确认关闭UIAbility，再主动销毁UIAbility。

说明

* 当[AbilityStage.onPrepareTerminationAsync](js-apis-app-ability-abilitystage.md#onprepareterminationasync15)或[AbilityStage.onPrepareTermination](js-apis-app-ability-abilitystage.md#onpreparetermination15)实现时，在dock栏或系统托盘处右键点击关闭，本回调函数将不执行。
* 如果应用本身或者所使用的三方框架注册了[window.WindowStage.on('windowStageClose')](arkts-apis-window-windowstage.md#onwindowstageclose14)监听，本回调函数将不执行。
* 若异步回调内发生crash，按超时处理，执行等待超过10秒未响应，UIAbility将被强制关闭。

**需要权限**：ohos.permission.PREPARE\_APP\_TERMINATE

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**设备行为差异**：

* 从API version 15开始，该接口仅在2in1设备中可正常执行回调，在其他设备上不执行回调。
* 从API version 19开始，该接口在2in1和Tablet设备中可正常执行回调，在其他设备上不执行回调。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示是否执行UIAbility关闭操作，返回true表示本次UIAbility关闭流程取消，返回false表示UIAbility继续正常关闭。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. async onPrepareToTerminateAsync(): Promise<boolean> {
5. await new Promise<boolean>((res, rej) => {
6. setTimeout(res, 2000); // 延时2秒
7. });
8. return true; // 已定义预关闭操作后，返回true表示UIAbility取消关闭
9. }
10. }
```

### onBackPressed10+

PhonePC/2in1TabletTVWearable

onBackPressed(): boolean

UIAbility生命周期回调，当UIAbility侧滑返回时触发，根据返回值决定是否销毁UIAbility。

* 当targetSdkVersion<12时，默认返回值为false，会销毁UIAbility。
* 当targetSdkVersion>=12时，默认返回值为true，会将UIAbility移动到后台不销毁。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示UIAbility将会被移到后台不销毁，返回false表示UIAbility将正常销毁。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onBackPressed() {
5. return true;
6. }
7. }
```

### onCollaborate18+

PhonePC/2in1TabletTVWearable

onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult

UIAbility生命周期回调，在多设备协同场景下，协同方应用在被拉起的过程中返回是否接受协同。

说明

* 该生命周期回调不支持[specified启动模式](../harmonyos-guides/uiability-launch-type.md#specified启动模式)。
* 通过[startAbility](js-apis-inner-application-uiabilitycontext.md#startability)等方法拉起协同方应用时，需要在Want对象中设置协同标记[Flags](js-apis-app-ability-wantconstant.md#flags)为FLAG\_ABILITY\_ON\_COLLABORATE。
* [冷启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability冷启动)时，该回调在[onForeground](js-apis-app-ability-uiability.md#onforeground)前或[onBackground](js-apis-app-ability-uiability.md#onbackground)后调用；[热启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability热启动)时，该回调在[onNewWant](js-apis-app-ability-uiability.md#onnewwant)前调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wantParam | Record<string, Object> | 是 | want相关参数，仅支持key值取"ohos.extra.param.key.supportCollaborateIndex"。通过该key值可以获取到调用方传输的数据并进行相应的处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AbilityConstant.CollaborateResult](js-apis-app-ability-abilityconstant.md#collaborateresult18) | 协同方是否接受协同的结果。 |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onCollaborate(wantParam: Record<string, Object>) {
5. return AbilityConstant.CollaborateResult.ACCEPT;
6. }
7. }
```

## Caller

PhonePC/2in1TabletTVWearable

调用方Caller UIAbility通过[startAbilityByCall](js-apis-inner-application-uiabilitycontext.md#startabilitybycall)接口拉起目标Callee UIAbility，目标UIAbility启动成功后，返回一个Caller对象给调用方进行通信。

### call

PhonePC/2in1TabletTVWearable

call(method: string, data: rpc.Parcelable): Promise<void>

Caller UIAbility向Callee UIAbility发送双方约定好的序列化的数据。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| data | [rpc.Parcelable](js-apis-rpc.md#parcelable9) | 是 | 由Caller向Callee发送的消息内容，消息内容是序列化的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. class MyMessageAble implements rpc.Parcelable { // 自定义的Parcelable数据结构
7. name: string;
8. str: string;
9. num: number = 1;

11. constructor(name: string, str: string) {
12. this.name = name;
13. this.str = str;
14. }

16. marshalling(messageSequence: rpc.MessageSequence) {
17. messageSequence.writeInt(this.num);
18. messageSequence.writeString(this.str);
19. console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
20. return true;
21. }

23. unmarshalling(messageSequence: rpc.MessageSequence) {
24. this.num = messageSequence.readInt();
25. this.str = messageSequence.readString();
26. console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
27. return true;
28. }
29. }

31. let method = 'call_Function'; // 约定的通知消息字符串

33. export default class MainUIAbility extends UIAbility {
34. onWindowStageCreate(windowStage: window.WindowStage) {
35. this.context.startAbilityByCall({
36. bundleName: 'com.example.myservice',
37. abilityName: 'MainUIAbility',
38. deviceId: ''
39. }).then((obj) => {
40. let caller: Caller = obj;
41. let msg = new MyMessageAble('msg', 'world'); // 参考Parcelable数据定义
42. caller.call(method, msg)
43. .then(() => {
44. console.info('Caller call() called');
45. })
46. .catch((callErr: BusinessError) => {
47. console.error(`Caller.call catch error, error.code: ${callErr.code}, error.message: ${callErr.message}`);
48. });
49. }).catch((err: BusinessError) => {
50. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
51. });
52. }
53. }
```

### callWithResult

PhonePC/2in1TabletTVWearable

callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>

Caller UIAbility向Callee UIAbility发送消息，Callee UIAbility处理完成后返回结果。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| data | [rpc.Parcelable](js-apis-rpc.md#parcelable9) | 是 | 由Caller向Callee发送的消息内容，消息内容是序列化的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[rpc.MessageSequence](js-apis-rpc.md#messagesequence9)> | Promise对象，返回Callee UIAbility的应答数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. class MyMessageAble implements rpc.Parcelable {
7. name: string
8. str: string
9. num: number = 1

11. constructor(name: string, str: string) {
12. this.name = name;
13. this.str = str;
14. }

16. marshalling(messageSequence: rpc.MessageSequence) {
17. messageSequence.writeInt(this.num);
18. messageSequence.writeString(this.str);
19. console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
20. return true;
21. }

23. unmarshalling(messageSequence: rpc.MessageSequence) {
24. this.num = messageSequence.readInt();
25. this.str = messageSequence.readString();
26. console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
27. return true;
28. }
29. }

31. let method = 'call_Function';
32. let caller: Caller;

34. export default class MainUIAbility extends UIAbility {
35. onWindowStageCreate(windowStage: window.WindowStage) {
36. this.context.startAbilityByCall({
37. bundleName: 'com.example.myservice',
38. abilityName: 'MainUIAbility',
39. deviceId: ''
40. }).then((obj) => {
41. caller = obj;
42. let msg = new MyMessageAble('msg', 'world');
43. caller.callWithResult(method, msg)
44. .then((data) => {
45. console.info('Caller callWithResult() called');
46. let retMsg = new MyMessageAble('msg', 'world');
47. data.readParcelable(retMsg);
48. })
49. .catch((callErr: BusinessError) => {
50. console.error(`Caller.callWithResult catch error, error.code: ${callErr.code}, error.message: ${callErr.message}`);
51. });
52. }).catch((err: BusinessError) => {
53. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
54. });
55. }
56. }
```

### release

PhonePC/2in1TabletTVWearable

release(): void

Caller主动释放与Callee UIAbility的连接。调用该接口后，Caller不能再使用call或callWithResult向Callee方发送消息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16200001 | The caller has been released. |
| 16200002 | The callee does not exist. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let caller: Caller;

7. export default class MainUIAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. this.context.startAbilityByCall({
10. bundleName: 'com.example.myservice',
11. abilityName: 'MainUIAbility',
12. deviceId: ''
13. }).then((obj) => {
14. caller = obj;
15. try {
16. caller.release();
17. } catch (releaseErr) {
18. console.error(`Caller.release catch error, error.code: ${releaseErr.code}, error.message: ${releaseErr.message}`);
19. }
20. }).catch((err: BusinessError) => {
21. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
22. });
23. }
24. }
```

### onRelease

PhonePC/2in1TabletTVWearable

onRelease(callback: OnReleaseCallback): void

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnReleaseCallback](js-apis-app-ability-uiability.md#onreleasecallback) | 是 | 回调函数，返回onRelease回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MainUIAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. this.context.startAbilityByCall({
8. bundleName: 'com.example.myservice',
9. abilityName: 'MainUIAbility',
10. deviceId: ''
11. }).then((obj) => {
12. let caller: Caller = obj;
13. try {
14. caller.onRelease((str) => {
15. console.info(`Caller OnRelease CallBack is called ${str}`);
16. });
17. } catch (error) {
18. console.error(`Caller.onRelease catch error, error.code: ${error.code}, error.message: ${error.message}`);
19. }
20. }).catch((err: BusinessError) => {
21. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
22. });
23. }
24. }
```

### onRemoteStateChange10+

PhonePC/2in1TabletTVWearable

onRemoteStateChange(callback: OnRemoteStateChangeCallback): void

注册协同场景下跨设备组件状态变化监听通知。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnRemoteStateChangeCallback](js-apis-app-ability-uiability.md#onremotestatechangecallback10) | 是 | 回调函数，返回onRemoteStateChange回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MainAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let dstDeviceId: string = 'xxxxx';
8. this.context.startAbilityByCall({
9. bundleName: 'com.example.myservice',
10. abilityName: 'MainUIAbility',
11. deviceId: dstDeviceId
12. }).then((obj) => {
13. let caller: Caller = obj;
14. try {
15. caller.onRemoteStateChange((str) => {
16. console.info('Remote state changed ' + str);
17. });
18. } catch (error) {
19. console.error(`Caller.onRemoteStateChange catch error, error.code: ${JSON.stringify(error.code)}, error.message: ${JSON.stringify(error.message)}`);
20. }
21. }).catch((err: BusinessError) => {
22. console.error(`Caller GetCaller error, error.code: ${JSON.stringify(err.code)}, error.message: ${JSON.stringify(err.message)}`);
23. });
24. }
25. }
```

### on('release')

PhonePC/2in1TabletTVWearable

on(type: 'release', callback: OnReleaseCallback): void

Caller UIAbility可使用该接口注册与Callee UIAbility连接断开通知的监听。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |
| callback | [OnReleaseCallback](js-apis-app-ability-uiability.md#onreleasecallback) | 是 | 回调函数，返回on回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Caller } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MainUIAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. let dstDeviceId: string = 'xxxx';
8. this.context.startAbilityByCall({
9. bundleName: 'com.example.myservice',
10. abilityName: 'MainUIAbility',
11. deviceId: dstDeviceId
12. }).then((obj) => {
13. let caller: Caller = obj;
14. try {
15. caller.on('release', (str) => {
16. console.info(`Caller OnRelease CallBack is called ${str}`);
17. });
18. } catch (error) {
19. console.error(`Caller.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
20. }
21. }).catch((err: BusinessError) => {
22. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
23. });
24. }
25. }
```

### off('release')

PhonePC/2in1TabletTVWearable

off(type: 'release', callback: OnReleaseCallback): void

取消注册Callee UIAbility断开通知的监听，与[on('release')](js-apis-app-ability-uiability.md#onrelease-1)是反向操作，当前暂未支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |
| callback | [OnReleaseCallback](js-apis-app-ability-uiability.md#onreleasecallback) | 是 | 回调函数，返回off回调结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class MainUIAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. this.context.startAbilityByCall({
8. bundleName: 'com.example.myservice',
9. abilityName: 'MainUIAbility',
10. deviceId: ''
11. }).then((obj) => {
12. let caller: Caller = obj;
13. try {
14. let onReleaseCallBack: OnReleaseCallback = (str) => {
15. console.info(`Caller OnRelease CallBack is called ${str}`);
16. };
17. caller.on('release', onReleaseCallBack);
18. caller.off('release', onReleaseCallBack);
19. } catch (error) {
20. console.error(`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
21. }
22. }).catch((err: BusinessError) => {
23. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
24. });
25. }
26. }
```

### off('release')

PhonePC/2in1TabletTVWearable

off(type: 'release'): void

取消注册Callee UIAbility断开通知的监听，与[Caller.on('release')](js-apis-app-ability-uiability.md#onrelease-1)是反向操作，当前暂未支持。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听releaseCall事件，固定为'release'。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { UIAbility, Caller, OnReleaseCallback } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let caller: Caller;

7. export default class MainUIAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. this.context.startAbilityByCall({
10. bundleName: 'com.example.myservice',
11. abilityName: 'MainUIAbility',
12. deviceId: ''
13. }).then((obj) => {
14. caller = obj;
15. try {
16. let onReleaseCallBack: OnReleaseCallback = (str) => {
17. console.info(`Caller OnRelease CallBack is called ${str}`);
18. };
19. caller.on('release', onReleaseCallBack);
20. caller.off('release');
21. } catch (error) {
22. console.error(`Caller.on or Caller.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
23. }
24. }).catch((err: BusinessError) => {
25. console.error(`Caller GetCaller error, error.code: ${err.code}, error.message: ${err.message}`);
26. });
27. }
28. }
```

## Callee

PhonePC/2in1TabletTVWearable

系统为UIAbility创建的后台通信对象，Callee UIAbility（被调用方）可以通过Callee对象接收Caller对象发送的数据。

### on

PhonePC/2in1TabletTVWearable

on(method: string, callback: CalleeCallback): void

通用组件服务端注册消息通知callback。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 由Caller和Callee双方约定好的方法名，Callee方通过该字段区分消息类型。 |
| callback | [CalleeCallback](js-apis-app-ability-uiability.md#calleecallback) | 是 | 一个[rpc.MessageSequence](js-apis-rpc.md#messagesequence9)类型入参的js通知同步回调函数, 回调函数至少要返回一个空的[rpc.Parcelable](js-apis-rpc.md#parcelable9)数据对象, 其他视为函数执行错误。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200004 | The method has been registered. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';

4. class MyMessageAble implements rpc.Parcelable {
5. name: string
6. str: string
7. num: number = 1

9. constructor(name: string, str: string) {
10. this.name = name;
11. this.str = str;
12. }

14. marshalling(messageSequence: rpc.MessageSequence) {
15. messageSequence.writeInt(this.num);
16. messageSequence.writeString(this.str);
17. console.info(`MyMessageAble marshalling num[${this.num}] str[${this.str}]`);
18. return true;
19. }

21. unmarshalling(messageSequence: rpc.MessageSequence) {
22. this.num = messageSequence.readInt();
23. this.str = messageSequence.readString();
24. console.info(`MyMessageAble unmarshalling num[${this.num}] str[${this.str}]`);
25. return true;
26. }
27. }

29. let method = 'call_Function';

31. function funcCallBack(pdata: rpc.MessageSequence) {
32. let msg = new MyMessageAble('test', '');
33. pdata.readParcelable(msg);
34. return new MyMessageAble('test1', 'Callee test');
35. }

37. export default class MainUIAbility extends UIAbility {
38. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
39. console.info('Callee onCreate is called');
40. try {
41. this.callee.on(method, funcCallBack);
42. } catch (error) {
43. console.error(`Callee.on catch error, error.code: ${error.code}, error.message: ${error.message}`);
44. }
45. }
46. }
```

### off

PhonePC/2in1TabletTVWearable

off(method: string): void

解除通用组件服务端注册消息通知callback。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| method | string | 是 | 已注册的通知事件字符串。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200005 | The method has not been registered. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

3. let method = 'call_Function';

5. export default class MainUIAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
7. console.info('Callee onCreate is called');
8. try {
9. this.callee.off(method);
10. } catch (error) {
11. console.error(`Callee.off catch error, error.code: ${error.code}, error.message: ${error.message}`);
12. }
13. }
14. }
```

## OnReleaseCallback

PhonePC/2in1TabletTVWearable

### (msg: string)

PhonePC/2in1TabletTVWearable

(msg: string): void

注册通用组件服务端Stub（桩）断开监听通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 用于传递释放消息。 |

## OnRemoteStateChangeCallback10+

PhonePC/2in1TabletTVWearable

### (msg: string)10+

PhonePC/2in1TabletTVWearable

(msg: string): void

注册协同场景下跨设备组件状态变化监听通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msg | string | 是 | 用于传递释放消息。 |

## CalleeCallback

PhonePC/2in1TabletTVWearable

### (indata: rpc.MessageSequence)

PhonePC/2in1TabletTVWearable

(indata: rpc.MessageSequence): rpc.Parcelable

通用组件服务端注册消息通知的回调函数类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indata | [rpc.MessageSequence](js-apis-rpc.md#messagesequence9) | 是 | 发送需传递的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [rpc.Parcelable](js-apis-rpc.md#parcelable9) | 返回的数据对象。 |
