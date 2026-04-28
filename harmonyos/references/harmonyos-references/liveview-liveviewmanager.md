---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-liveviewmanager
title: liveViewManager
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > liveViewManager
category: harmonyos-references
scraped_at: 2026-04-28T08:17:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a152e2cabda0dd7d4860aa4954ffeb4bcf6713b2c996abc07c465b677e10c496
---

本模块提供Live View Kit的基础能力，包括创建、更新和结束实况窗、获取实况窗和检查实况窗开关的功能。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1Tablet

```
1. import { liveViewManager } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## liveViewManager.isLiveViewEnabled

PhonePC/2in1Tablet

isLiveViewEnabled(): Promise<boolean>

查看应用实况窗开关，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回当前应用实况窗的开关状态。  **●** true表示实况窗开关开启。  **●** false表示实况窗开关关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. liveViewManager.isLiveViewEnabled().then((isEnabled: boolean) => {
7. hilog.info(0x0000, 'testTag', 'Succeeded in checking whether liveView is enabled, liveView is : %{public}s', isEnabled);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', err.code, err.message);
10. });
11. } catch (err) {
12. let e: BusinessError = err as BusinessError;
13. hilog.error(0x0000, 'testTag', 'Failed to check whether liveView is enabled: %{public}d %{public}s', e.code, e.message);
14. }
```

## liveViewManager.startLiveView

PhonePC/2in1Tablet

startLiveView(liveView: LiveView): Promise<LiveViewResult>

创建实况窗，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveView | [LiveView](liveview-liveviewmanager.md#liveview) | 是 | 一个实况窗实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveViewResult](liveview-liveviewmanager.md#liveviewresult)> | Promise对象，返回创建实况窗的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500004](liveview-error-code.md#section1003500004-实况窗开关关闭) | LiveView is not enabled. |
| [1003500005](liveview-error-code.md#section1003500005-实况窗权益未申请) | The right of liveView is not enabled. |
| [1003500006](liveview-error-code.md#section1003500006-实况窗已存在) | The liveView already exists. |
| [1003500007](liveview-error-code.md#section1003500007-无法连接服务器) | Couldn't connect to server. |
| [1003500008](liveview-error-code.md#section1003500008-实况窗频度超过限制) | Over max number liveViews per second. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Want, wantAgent } from '@kit.AbilityKit';

6. async function startLiveView(): Promise<void> {
7. try {
8. // 定义创建的liveView
9. let liveView: liveViewManager.LiveView = {
10. id: 123,
11. event: "PICK_UP",
12. sequence: 1,
13. isMute: false,
14. liveViewData: {
15. primary: {
16. title: "餐品已备好",
17. content: [
18. { text: "请前往" },
19. { text: "一号窗口", textColor: "#FFFF0000" }
20. ],
21. keepTime: 1,
22. clickAction: await buildWantAgent(),
23. extensionData: {
24. text: "待取餐",
25. type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
26. },
27. layoutData: {
28. layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
29. title: "取餐码",
30. content: "72988",
31. underlineColor: "#FFFF0000",
32. descPic: "coffee.jpg"
33. }
34. },
35. capsule: {
36. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
37. status: 1,
38. icon: "coffee.jpg",
39. title: "待取餐",
40. content: "取餐码：72988",
41. backgroundColor: "#FF308977"
42. }
43. }
44. };

46. liveViewManager.startLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
47. hilog.info(0x0000, 'testTag', 'Succeeded in starting liveView, result: %{public}s', JSON.stringify(liveViewResult));
48. }).catch((err: BusinessError) => {
49. hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', err.code, err.message);
50. });
51. } catch (err) {
52. let e: BusinessError = err as BusinessError;
53. hilog.error(0x0000, 'testTag', 'Failed to start liveView: %{public}d %{public}s', e.code, e.message);
54. }
55. }

57. async function buildWantAgent(): Promise<Want> {
58. const wantAgentInfo: wantAgent.WantAgentInfo = {
59. wants: [
60. {
61. bundleName: 'xxx.xxx.xxx',
62. abilityName: 'EntryAbility'
63. } as Want
64. ],
65. actionType: wantAgent.OperationType.START_ABILITIES,
66. requestCode: 0,
67. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
68. };
69. try {
70. const agent = await wantAgent.getWantAgent(wantAgentInfo);
71. return agent;
72. } catch (e) {
73. const err: BusinessError = e as BusinessError;
74. hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
75. throw e as Error;
76. }
77. }
```

## liveViewManager.updateLiveView

PhonePC/2in1Tablet

updateLiveView(liveView: LiveView): Promise<LiveViewResult>

更新实况窗，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveView | [LiveView](liveview-liveviewmanager.md#liveview) | 是 | 一个实况窗实例。对于非必填字段，若无特殊说明，则不携带时默认继承上一次的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveViewResult](liveview-liveviewmanager.md#liveviewresult)> | Promise对象，返回更新实况窗的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500004](liveview-error-code.md#section1003500004-实况窗开关关闭) | LiveView is not enabled. |
| [1003500008](liveview-error-code.md#section1003500008-实况窗频度超过限制) | Over max number liveViews per second. |
| [1003500009](liveview-error-code.md#section1003500009-实况窗id不存在) | The liveView does not exist. |
| [1003500010](liveview-error-code.md#section1003500010-实况窗已结束) | The liveView has ended. |
| [1003500011](liveview-error-code.md#section1003500011-实况窗顺序不正确) | The liveView sequence is incorrect. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Want, wantAgent } from '@kit.AbilityKit';

6. async function updateLiveView(): Promise<void> {
7. try {
8. // 定义更新的liveView
9. let liveView: liveViewManager.LiveView = {
10. id: 123,
11. event: "PICK_UP",
12. sequence: 2,
13. isMute: false,
14. liveViewData: {
15. primary: {
16. title: "餐品已备好",
17. content: [
18. { text: "请前往" },
19. { text: "一号窗口", textColor: "#FFFF0000" }
20. ],
21. keepTime: 1,
22. clickAction: await buildWantAgent(),
23. extensionData: {
24. text: "待取餐",
25. type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
26. },
27. layoutData: {
28. layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
29. title: "取餐码",
30. content: "72988",
31. underlineColor: "#FFFF0000",
32. descPic: "coffee.jpg"
33. }
34. },
35. capsule: {
36. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
37. status: 1,
38. icon: "coffee.jpg",
39. title: "待取餐",
40. content: "取餐码：72988",
41. backgroundColor: "#FF308977"
42. }
43. }
44. };

46. liveViewManager.updateLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
47. hilog.info(0x0000, 'testTag', 'Succeeded in updating liveView, result: %{public}s', JSON.stringify(liveViewResult));
48. }).catch((err: BusinessError) => {
49. hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', err.code, err.message);
50. });
51. } catch (err) {
52. let e: BusinessError = err as BusinessError;
53. hilog.error(0x0000, 'testTag', 'Failed to update liveView: %{public}d %{public}s', e.code, e.message);
54. }
55. }

57. async function buildWantAgent(): Promise<Want> {
58. const wantAgentInfo: wantAgent.WantAgentInfo = {
59. wants: [
60. {
61. bundleName: 'xxx.xxx.xxx',
62. abilityName: 'EntryAbility'
63. } as Want
64. ],
65. actionType: wantAgent.OperationType.START_ABILITIES,
66. requestCode: 0,
67. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
68. };
69. try {
70. const agent = await wantAgent.getWantAgent(wantAgentInfo);
71. return agent;
72. } catch (e) {
73. const err: BusinessError = e as BusinessError;
74. hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
75. throw e as Error;
76. }
77. }
```

## liveViewManager.stopLiveView

PhonePC/2in1Tablet

stopLiveView(liveView: LiveView): Promise<LiveViewResult>

结束实况窗，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveView | [LiveView](liveview-liveviewmanager.md#liveview) | 是 | 一个实况窗实例。对于非必填字段，若无特殊说明，则不携带时默认继承上一次的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveViewResult](liveview-liveviewmanager.md#liveviewresult)> | Promise对象，返回结束实况窗的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500004](liveview-error-code.md#section1003500004-实况窗开关关闭) | LiveView is not enabled. |
| [1003500008](liveview-error-code.md#section1003500008-实况窗频度超过限制) | Over max number liveViews per second. |
| [1003500009](liveview-error-code.md#section1003500009-实况窗id不存在) | The liveView does not exist. |
| [1003500010](liveview-error-code.md#section1003500010-实况窗已结束) | The liveView has ended. |
| [1003500011](liveview-error-code.md#section1003500011-实况窗顺序不正确) | The liveView sequence is incorrect. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Want, wantAgent } from '@kit.AbilityKit';

6. async function stopLiveView(): Promise<void> {
7. try {
8. // 定义要结束的liveView
9. let liveView: liveViewManager.LiveView = {
10. id: 123,
11. event: "PICK_UP",
12. sequence: 3,
13. isMute: false,
14. liveViewData: {
15. primary: {
16. title: "餐品已备好",
17. content: [
18. { text: "请前往" },
19. { text: "一号窗口", textColor: "#FFFF0000" }
20. ],
21. keepTime: 1,
22. clickAction: await buildWantAgent(),
23. extensionData: {
24. text: "待取餐",
25. type: liveViewManager.ExtensionType.EXTENSION_TYPE_COMMON_TEXT
26. },
27. layoutData: {
28. layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
29. title: "取餐码",
30. content: "72988",
31. underlineColor: "#FFFF0000",
32. descPic: "coffee.jpg"
33. }
34. },
35. capsule: {
36. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
37. status: 1,
38. icon: "coffee.jpg",
39. title: "待取餐",
40. content: "取餐码：72988",
41. backgroundColor: "#FF308977"
42. }
43. }
44. };

46. liveViewManager.stopLiveView(liveView).then((liveViewResult: liveViewManager.LiveViewResult) => {
47. hilog.info(0x0000, 'testTag', 'Succeeded in stopping liveView, result: %{public}s', JSON.stringify(liveViewResult));
48. }).catch((err: BusinessError) => {
49. hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', err.code, err.message);
50. });
51. } catch (err) {
52. let e: BusinessError = err as BusinessError;
53. hilog.error(0x0000, 'testTag', 'Failed to stop liveView: %{public}d %{public}s', e.code, e.message);
54. }
55. }

57. async function buildWantAgent(): Promise<Want> {
58. const wantAgentInfo: wantAgent.WantAgentInfo = {
59. wants: [
60. {
61. bundleName: 'xxx.xxx.xxx',
62. abilityName: 'EntryAbility'
63. } as Want
64. ],
65. actionType: wantAgent.OperationType.START_ABILITIES,
66. requestCode: 0,
67. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
68. };
69. try {
70. const agent = await wantAgent.getWantAgent(wantAgentInfo);
71. return agent;
72. } catch (e) {
73. const err: BusinessError = e as BusinessError;
74. hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
75. throw e as Error;
76. }
77. }
```

## liveViewManager.getActiveLiveView

PhonePC/2in1Tablet

getActiveLiveView(id: number): Promise<LiveView>

获取活动的liveView，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 实况窗的id，取值范围为[-2147483648, 2147483647]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveView](liveview-liveviewmanager.md#liveview)> | Promise对象，返回活动的实况窗实例。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500009](liveview-error-code.md#section1003500009-实况窗id不存在) | The liveView does not exist. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义需要查询的实况窗id
6. const id = 1;
7. try {
8. liveViewManager.getActiveLiveView(id).then((liveView: liveViewManager.LiveView) => {
9. hilog.info(0x0000, 'testTag', 'Succeeded in getting active liveView, liveView is : %{public}s', JSON.stringify(liveView));
10. }).catch((err: BusinessError) => {
11. hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', err.code, err.message);
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to get active liveView: %{public}d %{public}s', e.code, e.message);
16. }
```

## liveViewManager.isGeofenceTriggerEnabled

PhonePC/2in1Tablet

isGeofenceTriggerEnabled(): Promise<boolean>

查询基于地理位置的实况窗提醒开关，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回当前基于地理位置的实况窗提醒的开关状态。  **●** true表示基于地理位置的实况窗提醒开关开启。  **●** false表示基于地理位置的实况窗提醒开关关闭。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. liveViewManager.isGeofenceTriggerEnabled().then((isEnabled: boolean) => {
7. hilog.info(0x0000, 'testTag', 'Succeeded in checking whether geofence trigger is enabled, geofence trigger is : %{public}s', isEnabled);
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testTag', 'Failed to check whether geofence trigger is enabled: %{public}d %{public}s', err.code, err.message);
10. });
11. } catch (err) {
12. let e: BusinessError = err as BusinessError;
13. hilog.error(0x0000, 'testTag', 'Failed to check whether geofence trigger is enabled: %{public}d %{public}s', e.code, e.message);
14. }
```

## liveViewManager.startLiveViewByTrigger

PhonePC/2in1Tablet

startLiveViewByTrigger(liveView: LiveView, trigger:Trigger): Promise<LiveViewResult>

增加由条件触发创建实况的消息，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveView | [LiveView](liveview-liveviewmanager.md#liveview) | 是 | 一个实况窗实例。 |
| trigger | [Trigger](liveview-liveviewmanager.md#trigger) | 是 | 触发实况窗的条件对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveViewResult](liveview-liveviewmanager.md#liveviewresult)> | Promise对象，返回添加基于地理位置触发创建实况窗的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. The device model does not support geofencing. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500004](liveview-error-code.md#section1003500004-实况窗开关关闭) | LiveView is not enabled. |
| [1003500005](liveview-error-code.md#section1003500005-实况窗权益未申请) | The right of liveView is not enabled. |
| [1003500006](liveview-error-code.md#section1003500006-实况窗已存在) | The liveView already exists. |
| [1003500007](liveview-error-code.md#section1003500007-无法连接服务器) | Couldn't connect to server. |
| [1003500008](liveview-error-code.md#section1003500008-实况窗频度超过限制) | Over max number liveViews per second. |
| [1003500017](liveview-error-code.md#section1003500017-超过条件实况窗次数限制) | Over max number liveViews by trigger. |
| [1003500018](liveview-error-code.md#section1003500018-基于地理位置的实况窗提醒开关关闭) | Geofencing-based liveView is not enabled. |
| [1003500019](liveview-error-code.md#section1003500019-位置功能的开关关闭) | The location switch is off. |
| [1003500020](liveview-error-code.md#section1003500020-感知与提醒的开关关闭) | The "Awareness & suggestions" switch of the location-based service is turned off. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Want, wantAgent } from '@kit.AbilityKit';

6. async function startLiveViewByTrigger(): Promise<void> {
7. try {
8. // 定义创建的liveView
9. let liveView: liveViewManager.LiveView = {
10. id: 0, // 实况窗ID，开发者生成。
11. event: "EXPRESS", // 实况窗的应用场景。EXPRESS：快递。
12. liveViewData: {
13. primary: {
14. title: "快递已送达",
15. content: [
16. { text: "请前往" },
17. { text: " XXX店 ", textColor: "#FF0A59F7" },
18. { text: "取快递" },
19. ],
20. keepTime: 15,
21. clickAction: await buildWantAgent(),
22. layoutData: {
23. layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
24. title: "快递码",
25. content: "72988",
26. underlineColor: "#FF0A59F7",
27. descPic: "express.png" // 扩展区右侧产品描述图，取值为“/resources/rawfile”路径下的文件名或image.PixelMap
28. }
29. },
30. capsule: {
31. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
32. status: 1,
33. icon: "express.jpg",
34. title: "快递码",
35. content: "快递码：72988",
36. backgroundColor: "#FF308977"
37. }
38. }
39. };
40. let trigger: liveViewManager.Trigger = {
41. type: liveViewManager.TriggerType.TRIGGER_TYPE_GEOFENCE,
42. displayTime: 15,
43. condition: {
44. longitude: 116.3971356415625,
45. latitude: 39.91800603311188,
46. coordinateSystemType: liveViewManager.CoordinateSystemType.COORDINATE_TYPE_GCJ02,
47. monitorEvent: liveViewManager.MonitorEvent.MONITOR_TYPE_ENTRY,
48. radius: 2000,
49. delayTime: 0
50. }
51. };

53. liveViewManager.startLiveViewByTrigger(liveView, trigger).then((liveViewResult: liveViewManager.LiveViewResult) => {
54. hilog.info(0x0000, 'testTag', 'Succeeded in starting liveView by trigger, result: %{public}s', JSON.stringify(liveViewResult));
55. }).catch((err: BusinessError) => {
56. hilog.error(0x0000, 'testTag', 'Failed to start liveView by trigger: %{public}d %{public}s', err.code, err.message);
57. });
58. } catch (err) {
59. let e: BusinessError = err as BusinessError;
60. hilog.error(0x0000, 'testTag', 'Failed to start liveView by trigger: %{public}d %{public}s', e.code, e.message);
61. }
62. }

64. async function buildWantAgent(): Promise<Want> {
65. const wantAgentInfo: wantAgent.WantAgentInfo = {
66. wants: [
67. {
68. bundleName: 'xxx.xxx.xxx',
69. abilityName: 'EntryAbility'
70. } as Want
71. ],
72. actionType: wantAgent.OperationType.START_ABILITIES,
73. requestCode: 0,
74. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
75. };
76. try {
77. const agent = await wantAgent.getWantAgent(wantAgentInfo);
78. return agent;
79. } catch (e) {
80. const err: BusinessError = e as BusinessError;
81. hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
82. throw e as Error;
83. }
84. }
```

## liveViewManager.stopLiveViewByTrigger

PhonePC/2in1Tablet

stopLiveViewByTrigger(liveView: LiveView, trigger:Trigger): Promise<LiveViewResult>

增加由条件触发结束实况的消息，使用Promise异步返回结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveView | [LiveView](liveview-liveviewmanager.md#liveview) | 是 | 一个实况窗实例。 |
| trigger | [Trigger](liveview-liveviewmanager.md#trigger) | 是 | 触发实况窗的条件对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[LiveViewResult](liveview-liveviewmanager.md#liveviewresult)> | Promise对象，返回添加基于地理位置触发结束实况窗的结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](liveview-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](errorcode-universal.md#section801-该设备不支持此api) | Capability not supported. The device model does not support geofencing. |
| [1003500001](liveview-error-code.md#section1003500001-系统错误) | Internal error. |
| [1003500002](liveview-error-code.md#section1003500002-序列化或反序列化失败) | Marshalling or unmarshalling error. |
| [1003500003](liveview-error-code.md#section1003500003-连接服务失败) | Failed to connect service. |
| [1003500004](liveview-error-code.md#section1003500004-实况窗开关关闭) | LiveView is not enabled. |
| [1003500008](liveview-error-code.md#section1003500008-实况窗频度超过限制) | Over max number liveViews per second. |
| [1003500009](liveview-error-code.md#section1003500009-实况窗id不存在) | The liveView does not exist. |
| [1003500010](liveview-error-code.md#section1003500010-实况窗已结束) | The liveView has ended. |
| [1003500011](liveview-error-code.md#section1003500011-实况窗顺序不正确) | The liveView sequence is incorrect. |
| [1003500017](liveview-error-code.md#section1003500017-超过条件实况窗次数限制) | Over max number liveViews by trigger. |
| [1003500018](liveview-error-code.md#section1003500018-基于地理位置的实况窗提醒开关关闭) | Geofencing-based liveView is not enabled. |
| [1003500019](liveview-error-code.md#section1003500019-位置功能的开关关闭) | The location switch is off. |
| [1003500020](liveview-error-code.md#section1003500020-感知与提醒的开关关闭) | The "Awareness & suggestions" switch of the location-based service is turned off. |

**示例：**

```
1. import { liveViewManager } from '@kit.LiveViewKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Want, wantAgent } from '@kit.AbilityKit';

6. async function stopLiveViewByTrigger(): Promise<void> {
7. try {
8. // 定义要结束的liveView
9. let liveView: liveViewManager.LiveView = {
10. id: 0, // 实况窗ID，开发者生成。
11. event: "EXPRESS", // 实况窗的应用场景。EXPRESS：快递。
12. liveViewData: {
13. primary: {
14. title: "快递已送达",
15. content: [
16. { text: "请前往" },
17. { text: " XXX店 ", textColor: "#FF0A59F7" },
18. { text: "取快递" },
19. ],
20. keepTime: 15,
21. clickAction: await buildWantAgent(),
22. layoutData: {
23. layoutType: liveViewManager.LayoutType.LAYOUT_TYPE_PICKUP,
24. title: "快递码",
25. content: "72988",
26. underlineColor: "#FF0A59F7",
27. descPic: "express.png" // 扩展区右侧产品描述图，取值为“/resources/rawfile”路径下的文件名或image.PixelMap
28. }
29. },
30. capsule: {
31. type: liveViewManager.CapsuleType.CAPSULE_TYPE_TEXT,
32. status: 1,
33. icon: "express.jpg",
34. title: "快递码",
35. content: "快递码：72988",
36. backgroundColor: "#FF308977"
37. }
38. }
39. };
40. let trigger: liveViewManager.Trigger = {
41. type: liveViewManager.TriggerType.TRIGGER_TYPE_GEOFENCE,
42. displayTime: 15,
43. condition: {
44. longitude: 116.3971356415625,
45. latitude: 39.91800603311188,
46. coordinateSystemType: liveViewManager.CoordinateSystemType.COORDINATE_TYPE_GCJ02,
47. monitorEvent: liveViewManager.MonitorEvent.MONITOR_TYPE_LEAVE,
48. radius: 2000,
49. delayTime: 0
50. }
51. };

53. liveViewManager.stopLiveViewByTrigger(liveView, trigger).then((liveViewResult: liveViewManager.LiveViewResult) => {
54. hilog.info(0x0000, 'testTag', 'Succeeded in stopping liveView by trigger, result: %{public}s', JSON.stringify(liveViewResult));
55. }).catch((err: BusinessError) => {
56. hilog.error(0x0000, 'testTag', 'Failed to stop liveView by trigger: %{public}d %{public}s', err.code, err.message);
57. });
58. } catch (err) {
59. let e: BusinessError = err as BusinessError;
60. hilog.error(0x0000, 'testTag', 'Failed to stop liveView by trigger: %{public}d %{public}s', e.code, e.message);
61. }
62. }

64. async function buildWantAgent(): Promise<Want> {
65. const wantAgentInfo: wantAgent.WantAgentInfo = {
66. wants: [
67. {
68. bundleName: 'xxx.xxx.xxx',
69. abilityName: 'EntryAbility'
70. } as Want
71. ],
72. actionType: wantAgent.OperationType.START_ABILITIES,
73. requestCode: 0,
74. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
75. };
76. try {
77. const agent = await wantAgent.getWantAgent(wantAgentInfo);
78. return agent;
79. } catch (e) {
80. const err: BusinessError = e as BusinessError;
81. hilog.error(0x0000, 'testTag', 'Failed to get wantAgent: %{public}s', err.message);
82. throw e as Error;
83. }
84. }
```

## Trigger

PhonePC/2in1Tablet

触发创建或结束实况窗的条件对象参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [TriggerType](liveview-liveviewmanager.md#triggertype) | 否 | 否 | 触发创建或结束实况窗的条件类型 |
| condition | [Geofence](liveview-liveviewmanager.md#geofence) | 否 | 否 | 触发创建或结束实况窗的条件具体描述 |
| displayTime | number | 否 | 是 | 条件触发实况的展示持续时间，取值范围为[15，1800]，默认值为900，单位：s |

## Geofence

PhonePC/2in1Tablet

地理围栏对象参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| longitude | number | 否 | 否 | 地理围栏中心点经度，取值范围为[-180，180] |
| latitude | number | 否 | 否 | 地理围栏中心点纬度，取值范围为[-90，90] |
| coordinateSystemType | [CoordinateSystemType](liveview-liveviewmanager.md#coordinatesystemtype) | 否 | 否 | 地理围栏中心点的坐标系类型 |
| radius | number | 否 | 否 | 地理围栏半径，取值范围为[200，2000] ，单位：m |
| monitorEvent | [MonitorEvent](liveview-liveviewmanager.md#monitorevent) | 否 | 否 | 触发地理围栏的事件类型 |
| delayTime | number | 否 | 是 | 延迟触发时间，即：进入/离开围栏后持续多长时间触发围栏，取值范围为[0，300]，默认值为0，单位：s |

说明

* 经、纬度传入值不允许同时为0。
* 当[coordinateSystemType](liveview-liveviewmanager.md#coordinatesystemtype)为COORDINATE\_TYPE\_GCJ02时，经度传入值不允许为-180或180，纬度传入值不允许为-90或90。

## TriggerType

PhonePC/2in1Tablet

触发创建或结束实况窗的条件类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRIGGER\_TYPE\_GEOFENCE | 1 | 地理围栏条件类型 |

## CoordinateSystemType

PhonePC/2in1Tablet

地理围栏中心点坐标系类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COORDINATE\_TYPE\_WGS84 | 1 | WGS84坐标系 |
| COORDINATE\_TYPE\_GCJ02 | 2 | GCJ02坐标系 |

## MonitorEvent

PhonePC/2in1Tablet

触发地理围栏的事件类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.0(23)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MONITOR\_TYPE\_ENTRY | 1 | 进入围栏 |
| MONITOR\_TYPE\_LEAVE | 2 | 退出围栏 |

## LiveView

PhonePC/2in1Tablet

实况窗对象参数，具体示例请见[构建本地实况窗](../harmonyos-guides/liveview-create-locally.md#创建实况窗)。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 实况窗唯一标识，取值范围为[-2147483648, 2147483647]，由开发者自行生成。对应Push Kit中LiveViewPayload的[activityId](push-scenariozed-api-request-param.md#section66881469306)字段。 |
| event | string | 否 | 否 | 实况窗的应用场景。  **●** TAXI：出行打车。  **●** DELIVERY：即时配送（外卖、生鲜）。  **●** FLIGHT：航班。  **●** TRAIN：高铁/火车。  **●** QUEUE：排队。  **●** PICK\_UP：取餐。  **●** SCORE：赛事比分。  **●** RENT：共享租赁。  **●** TIMER：计时。  **●** WORKOUT：运动锻炼。  **●** NAVIGATION：导航。  **●** CHECK\_IN：打卡。  **●** EXPRESS：快递。  使用对应场景需要申请权益，详情请参见[实况窗权益说明](../harmonyos-guides/liveview-rights.md)。 |
| sequence | number | 否 | 是 | 支持实况窗消息更新和结束保序能力，取值范围为[0, 2147483647]，新的实况窗版本号需大于当前展示实况窗版本号，否则更新和结束会失败。若不传入参数值，Live View Kit不会自动生成（此时，调用getActiveLiveView接口查询实况信息，返回结果中sequence：4294967295为无效值，该无效值不允许用来更新实况），也不会校验实况窗版本号。对应Push Kit中的[version](push-scenariozed-api-request-param.md#section66881469306)字段。 |
| isMute | boolean | 否 | 是 | 消息提醒方式。若您在创建或更改实况窗状态时不传入此字段，则始终默认静默提醒。  **●** true：静默提醒。  **●** false：铃声震动提醒。 |
| timer | [LiveViewTimer](liveview-liveviewmanager.md#liveviewtimer) | 否 | 是 | 实况窗计时器，展示时每秒刷新一次。  **起始版本：** 5.0.0(12)。  配置了计时器后，可以在部分字段中使用占位符：**${placeholder.timer}**，系统会将占位符替换为计时器。  当前支持使用占位符的字段：  **●** liveViewData.primary.[title](liveview-liveviewmanager.md#primarydata)  **●** liveViewData.primary.[content](liveview-liveviewmanager.md#primarydata)  **●** liveViewData.primary.layoutData.[content](liveview-liveviewmanager.md#pickuplayout)  **●** liveViewData.primary.layoutData.[competitionTime](liveview-liveviewmanager.md#scorelayout) |
| liveViewData | [LiveViewData](liveview-liveviewmanager.md#liveviewdata) | 否 | 否 | 实况窗详细信息。 |

## LiveViewTimer

PhonePC/2in1Tablet

实况窗计时器参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| time | number | 否 | 是 | 计时器初始值，单位为毫秒，默认为0，取值范围为[0,9223372036854775807]。每秒刷新一次。 |
| isCountdown | boolean | 否 | 是 | 计时器是否为倒计时，默认为false。  **●** true：计时器为倒计时类型  **●** false：计时器为正计时类型 |
| isPaused | boolean | 否 | 是 | 计时器是否暂停，默认false。计时器暂停时，会显示暂停的那一秒。  **●** true：暂停。  **●** false：不暂停（默认值）。 |
| countdownPreset | [CountdownPreset](liveview-liveviewmanager.md#countdownpreset) | 否 | 是 | 当倒计时到0时，系统将自动更新实况窗卡片模板扩展区标题（title）和扩展区内容（content）字段为卡片预置结构体（countdownPreset）中的标题（presetTitle）和内容（presetContent）。  仅当满足以下条件时，上述功能生效：  **●** [layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_PICKUP强调文本模板；  **●** liveViewData.primary.layoutData.[content](liveview-liveviewmanager.md#pickuplayout)中使用占位符${placeholder.timer}。  **起始版本：** 6.0.0(20)。 |
| capsuleCountdownPreset | [CountdownPreset](liveview-liveviewmanager.md#countdownpreset) | 否 | 是 | 当倒计时到0时，系统将自动更新计时器类型实况胶囊主文本（time）和实况胶囊副文本（content）为实况胶囊预设结构体（capsuleCountdownPreset）中的主文本（presetTitle）和副文本（presetContent）。仅当满足以下条件时，上述功能生效：  **●** [capsuleType](liveview-liveviewmanager.md#capsuletype)为CAPSULE\_TYPE\_TIMER计时器类型实况胶囊。  **起始版本：** 6.0.0(20)。 |

## CountdownPreset

PhonePC/2in1Tablet

实况窗计时器预置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| presetTitle | string | 否 | 是 | 自动更新扩展区标题或实况胶囊主文本为预设主文本。不支持时间占位符，若填值时不能为空，长度小于128。 |
| presetContent | string | 否 | 是 | 自动更新扩展区文本内容或实况胶囊副文本为预设副文本，若填值时不能为空，长度小于128。 |

## LiveViewData

PhonePC/2in1Tablet

实况窗详细信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| primary | [PrimaryData](liveview-liveviewmanager.md#primarydata) | 否 | 否 | 卡片形态内容。 |
| capsule | [TextCapsule](liveview-liveviewmanager.md#textcapsule) | [TimerCapsule](liveview-liveviewmanager.md#timercapsule) | [ProgressCapsule](liveview-liveviewmanager.md#progresscapsule) | 否 | 是 | 实况胶囊形态内容。 |
| external | [ExternalData](liveview-liveviewmanager.md#externaldata) | 否 | 是 | 小折叠外屏形态内容。 |

## PrimaryData

PhonePC/2in1Tablet

卡片形态参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 创建：否  更新或结束：是 | 固定区标题，若填值时不能为空，长度小于1024。 |
| content | Array<[RichText](liveview-liveviewmanager.md#richtext)> | 否 | 创建：否  更新或结束：是 | 固定区内容，若填值时不能为空。  **●** 数组中所有对象的text字段字符串长度总和需小于1024。  **●** 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色。 |
| keepTime | number | 否 | 是 | 实况窗存档时间，在结束实况窗后，通知仍保留在通知中心的时长，**默认0不保留**，范围[0,3600]秒(s)。 |
| clickAction | [WantAgent](js-apis-app-ability-wantagent.md) | 否 | 创建：否  更新或结束：是 | 点击实况窗默认动作，请调用wantAgent.[getWantAgent()](js-apis-app-ability-wantagent.md#wantagentgetwantagent-1)来构造。 |
| extensionData | [ExtensionData](liveview-liveviewmanager.md#extensiondata) | 否 | 是 | 辅助区内容。 |
| [layoutData](liveview-liveviewmanager.md#layoutdata) | [ProgressLayout](liveview-liveviewmanager.md#progresslayout) | [PickupLayout](liveview-liveviewmanager.md#pickuplayout) | [FlightLayout](liveview-liveviewmanager.md#flightlayout) | [ScoreLayout](liveview-liveviewmanager.md#scorelayout) | [NavigationLayout](liveview-liveviewmanager.md#navigationlayout) | 否 | 创建：否  更新或结束：是 | 扩展区数据。  **说明：** 从5.0.0(12)版本开始，新增支持参数类型NavigationLayout。 |
| liveViewLockScreenPicture | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 锁屏沉浸实况窗大图样式在指定路径下的文件名。传入实际存在的图片时，用户在锁屏下点击实况胶囊中的应用图标、长按实况胶囊内容或长按卡片内容，会进入沉浸态，展示大图。不传入或传入图片不存在时，用户点击行为不会进入沉浸态。  **●** string类型的取值为在“/resources/rawfile”路径下的文件名，长度小于256  ;示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 建议使用大小约为1000\*1000的图片，不支持GIF格式的图片文件。  **起始版本：** 5.0.0(12)。 |
| liveViewLockScreenAbilityName | string | 否 | 是 | [LiveViewLockScreenExtensionAbility](liveview-lock-screen-ability.md)（锁屏沉浸实况窗扩展Ability）的名称，仅创建实况窗时生效，传入时值不可为空，长度最大为128。若在创建实况窗时与liveViewLockScreenPicture同时传入，则仅本字段生效。  **起始版本：** 5.0.0(12)。 |
| liveViewLockScreenAbilityParameters | Record<string, string> | 否 | 是 | 用户自定义向[LiveViewLockScreenExtensionAbility](liveview-lock-screen-ability.md)（锁屏沉浸实况窗扩展Ability）传入的参数，填值时不能为空，key-value键值对最多50个，传入后可在ability的onSessionCreate()中，通过want.parameters获取。  **起始版本：** 5.0.0(12)。 |
| backgroundType | [BackgroundType](liveview-liveviewmanager.md#backgroundtype) | 否 | 是 | 表示实况窗卡片的背景氛围类型，仅支持左右文本模板(即[layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_FLIGHT)展示背景。  当传入实况窗卡片的背景氛围类型参数backgroundType值为赏月航班或夕阳航班时，且同时传入天气类型（[WeatherInfo](liveview-liveviewmanager.md#weatherinfo)）为雨、雪特殊天气，卡片上优先展示天气背景，其余非特殊天气在卡片上展示赏月航班或夕阳航班背景氛围。  **起始版本：** 6.0.0(20)。 |

## BackgroundType

PhonePC/2in1Tablet

航班场景下卡片背景类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYS\_BACKGROUND\_UNDEFINED | 0 | 未定义，表示在卡片上不展示背景氛围。 |
| SYS\_BACKGROUND\_FLIGHT\_MOON | 100 | 赏月航班，表示在卡片上展示赏月的背景氛围。 |
| SYS\_BACKGROUND\_FLIGHT\_SUNSET | 101 | 夕阳航班，表示在卡片上展示夕阳的背景氛围。 |

## ExtensionData

PhonePC/2in1Tablet

辅助区参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ExtensionType](liveview-liveviewmanager.md#extensiontype) | 否 | 是 | 辅助区显示类型，默认为[EXTENSION\_TYPE\_DEFAULT](liveview-liveviewmanager.md#extensiontype)不显示辅助区。 |
| text | string | 否 | 创建：否（仅当type值为ExtensionType.EXTENSION\_TYPE\_COMMON\_TEXT或ExtensionType.EXTENSION\_TYPE\_CAPSULE\_TEXT时）  更新或结束：是 | 辅助区显示的文本信息，若填值时不能为空，长度小于128。 |
| pic | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建：否（仅当type值为ExtensionType.EXTENSION\_TYPE\_PIC或ExtensionType.EXTENSION\_TYPE\_ICON时）  更新或结束：是 | 辅助区显示的图片，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| clickAction | [WantAgent](js-apis-app-ability-wantagent.md) | 否 | 是 | 点击辅助区的跳转动作，请调用wantAgent.[getWantAgent()](js-apis-app-ability-wantagent.md#wantagentgetwantagent-1)来构造。 |

## LayoutData

PhonePC/2in1Tablet

定义扩展区模板类型及公共参数。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_DEFAULT时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| layoutType | [LayoutType](liveview-liveviewmanager.md#layouttype) | 否 | 否 | 模板类型。 |
| serviceButtons | Array<[ServiceButton](liveview-liveviewmanager.md#servicebutton)> | 否 | 是 | 传入连续服务按钮结构体数组。 更新连续服务按钮时，需要同时更新辅助区[ExtensionData](liveview-liveviewmanager.md#extensiondata)的clickAction字段和连续服务按钮。  **起始版本：** 5.1.1(19)。 |
| isServiceButtonsDisplayed | boolean | 否 | 是 | 是否显示连续服务按钮，默认false。  **●** true：显示按钮  **●** false：不显示按钮  **起始版本：** 5.1.1(19)。 |
| weatherInfo | [WeatherInfo](liveview-liveviewmanager.md#weatherinfo) | 否 | 是 | 传入天气信息结构体。  目的地天气类型仅支持左右文本模板（即[layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_FLIGHT）；  本地天气类型仅支持基础模板、进度可视化模板和强调文本模板（即[layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_DEFAULT/LAYOUT\_TYPE\_PROGRESS/LAYOUT\_TYPE\_PICKUP）。  当传入天气信息，且同时传入实况窗卡片的背景氛围类型参数[backgroundType](liveview-liveviewmanager.md#backgroundtype)值为赏月航班（SYS\_BACKGROUND\_FLIGHT\_MOON）或夕阳航班（SYS\_BACKGROUND\_FLIGHT\_SUNSET）时，若天气类型为雨、雪特殊天气，卡片上优先展示天气背景，其余非特殊天气在卡片上优先展示赏月航班或夕阳航班背景氛围。  **说明：**  从6.0.0(20)开始支持展示目的地天气效果；  从6.0.2(22)开始支持展示本地天气效果。 |

## WeatherInfo

PhonePC/2in1Tablet

应用传入天气信息的基类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| weatherType | [WeatherType](liveview-liveviewmanager.md#weathertype) | 否 | 是 | 天气类型。创建实况窗时，若weatherType不传入或传入非法值，则不展示天气效果。 |
| locationType | [WeatherLocationType](liveview-liveviewmanager.md#weatherlocationtype) | 否 | 是 | 天气位置类型。创建实况窗时，若locationType不传入或传入非法值，则不展示天气效果。 |
| highTemperature | number | 否 | 是 | 天气最高温度，当前仅支持摄氏度，需小于等于58℃且大于传入的最低温度值（lowTemperature）。创建实况窗时，若不传入或传入非法值，则不展示温度信息。 |
| lowTemperature | number | 否 | 是 | 天气最低温度，当前仅支持摄氏度，需大于等于-95℃且小于传入的最高温度值（highTemperature）。创建实况窗时，若不传入或传入非法值，则不展示温度信息。 |

## WeatherType

PhonePC/2in1Tablet

天气类型，为枚举值，雨、雪天气支持在实况卡片上展示天气动效背景，其余天气类型（WEATHER\_TYPE\_UNDEFINED除外）仅支持在实况卡片上展示天气图标和温度，不支持在实况卡片上展示天气动效背景。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WEATHER\_TYPE\_UNDEFINED | 0 | 表示不展示天气效果。 |
| WEATHER\_TYPE\_SUNNY | 1 | 晴天气类型，展示天晴天气效果。 |
| WEATHER\_TYPE\_HAZY | 5 | 霾天气类型，展示霾天气效果。 |
| WEATHER\_TYPE\_CLOUDY | 7 | 多云天气类型，展示多云天气效果。 |
| WEATHER\_TYPE\_OVERCAST | 8 | 阴天气类型，展示阴天气效果。 |
| WEATHER\_TYPE\_FOG | 11 | 雾天气类型，展示雾天气效果。 |
| WEATHER\_TYPE\_SHOWERS | 12 | 阵雨天气类型，展示阵雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_T\_STORMS | 15 | 雷阵雨天气类型，展示雷阵雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_RAIN | 18 | 雨天气类型，展示雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_SNOW | 22 | 雪天气类型，展示雪天气效果。实况卡片支持雪动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_RAIN\_AND\_SNOW | 29 | 雨夹雪天气类型，展示雨夹雪天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_HOT | 30 | 高温天气类型，展示高温天气效果。 |
| WEATHER\_TYPE\_COLD | 31 | 低温天气类型，展示低温天气效果。 |
| WEATHER\_TYPE\_WINDY | 32 | 大风天气类型，展示大风天气效果。 |
| WEATHER\_TYPE\_THUNDERSHOWER\_WITH\_HAIL | 45 | 冰雹天气类型，展示冰雹天气效果。 |
| WEATHER\_TYPE\_LIGHT\_RAIN | 46 | 小雨天气类型，展示小雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_MODERATE\_RAIN | 47 | 中雨天气类型，展示中雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_HEAVY\_RAIN | 48 | 大雨天气类型，展示大雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_STORM | 49 | 暴雨天气类型，展示暴雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_SEVERE\_STORM | 51 | 特大暴雨天气类型，展示特大暴雨天气效果。实况卡片支持雨动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_LIGHT\_SNOW | 52 | 小雪天气类型，展示小雪天气效果。实况卡片支持雪动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_MODERATE\_SNOW | 53 | 中雪天气类型，展示中雪天气效果。实况卡片支持雪动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_HEAVY\_SNOW | 54 | 大雪天气类型，展示大雪天气效果。实况卡片支持雪动效背景。  **说明：** 从6.0.0(20)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_SNOW\_STORM | 55 | 暴雪天气类型，展示暴雪天气效果。实况卡片支持雪动效背景。  **说明：** 从6.0.2(22)开始支持展示天气动效背景 |
| WEATHER\_TYPE\_DUST\_STORM | 56 | 沙尘暴天气类型，展示沙尘暴天气效果。 |
| WEATHER\_TYPE\_DUST | 65 | 浮尘天气类型，展示浮尘天气效果。 |
| WEATHER\_TYPE\_SAND | 66 | 扬沙天气类型，展示扬沙天气效果。 |
| WEATHER\_TYPE\_SAND\_STORM | 67 | 强沙尘暴天气类型，展示强沙尘暴天气效果。 |

## WeatherLocationType

PhonePC/2in1Tablet

天气位置类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCATION\_TYPE\_LOCAL | 1 | 表示展示本地天气效果，仅支持基础模板、进度可视化模板和强调文本模板（即[layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_DEFAULT/LAYOUT\_TYPE\_PROGRESS/LAYOUT\_TYPE\_PICKUP）。天气图标将展示在固定区标题右侧，不支持显示温度。  **说明：** 从6.0.2(22)开始支持展示本地天气效果。 |
| LOCATION\_TYPE\_DESTINATION | 2 | 表示展示目的地天气效果，仅支持左右文本模板（即[layoutType](liveview-liveviewmanager.md#layouttype)为LAYOUT\_TYPE\_FLIGHT）。天气图标及温度信息将展示在左右文本模板扩展区右侧，扩展区右侧标题及右侧内容的左侧。  **说明：** 从6.0.0(20)开始支持展示目的地天气效果； |

## ServiceButton

PhonePC/2in1Tablet

应用传入连续服务按钮的基类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.1.1(19)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 连续服务按钮名字，长度小于128，超过该长度的字符将被截断。 |
| clickAction | [WantAgent](js-apis-app-ability-wantagent.md) | 否 | 是 | 点击连续服务按钮时触发的跳转动作，请调用wantAgent.[getWantAgent()](js-apis-app-ability-wantagent.md#wantagentgetwantagent-1)来构造。 |

## ProgressLayout

PhonePC/2in1Tablet

进度可视化模板扩展区参数，继承[LayoutData](liveview-liveviewmanager.md#layoutdata)。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_PROGRESS时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 进度百分比，决定指示器在进度条中的位置，值范围：[0,100]。 |
| color | string | 否 | 是 | 进度条颜色，"#ARGB"16进制格式，长度为9。默认颜色为#FF317AF7。 |
| backgroundColor | string | 否 | 是 | 进度条背景颜色，"#ARGB"16进制格式，长度为9。默认颜色为#19000000，深色模式默认颜色#19FFFFFF。 |
| indicatorType | [IndicatorType](liveview-liveviewmanager.md#indicatortype) | 否 | 是 | 扩展区指示器小图标显示类型，默认不显示指示器小图标。 |
| indicatorIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：否（仅当indicatorType值为IndicatorType.INDICATOR\_TYPE\_UP或IndicatorType.INDICATOR\_TYPE\_OVERLAY时）  更新或结束：是 | 进度条指示器图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| lineType | [LineType](liveview-liveviewmanager.md#linetype) | 否 | 是 | 扩展区进度条显示类型，默认为虚线进度。 |
| nodeIcons | Array<string | image.[PixelMap](arkts-apis-image-pixelmap.md)> | 否 | 创建或模板切换：否  更新或结束：是 | 进度条每个节点图标，数组长度范围为[2, 5]，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |

## PickupLayout

PhonePC/2in1Tablet

强调文本模板扩展区参数，继承[LayoutData](liveview-liveviewmanager.md#layoutdata)。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_PICKUP时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区标题，若填值时不能为空，长度小于128。 |
| content | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区内容，若填值时不能为空，长度小于128。 |
| underlineColor | string | 否 | 是 | 扩展区内容下划线颜色，"#ARGB"16进制格式，长度为9，默认不显示下划线。 |
| descPic | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧产品描述图，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |

## FlightLayout

PhonePC/2in1Tablet

左右文本模板扩展区参数，继承[LayoutData](liveview-liveviewmanager.md#layoutdata)。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_FLIGHT时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| style | [FlightLayoutStyle](liveview-liveviewmanager.md#flightlayoutstyle) | 否 | 是 | 左右文本子样式类型，若未填默认为强调型子样式。  **●** 0：强调型子样式类型。  **●** 1：均衡型子样式类型。  **起始版本：** 5.0.2(14)。 |
| firstTitle | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区左侧标题，若填值时不能为空，长度小于128。 |
| firstContent | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区左侧内容，若填值时不能为空，长度小于128。 |
| lastTitle | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧标题，若填值时不能为空，长度小于128。 |
| lastContent | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧内容，若填值时不能为空，长度小于128。 |
| lastTitleSuperscript | string | 否 | 是 | 扩展区右侧标题的右上角展示内容，若填值时不能为空，长度小于128。若用于表示到达时间跨天，传入值长度等于2，格式为"+X", 其中X为数字，例如"+1", "+2"等。  **起始版本：** 5.0.2(14)。 |
| lastContentSuperscript | string | 否 | 是 | 扩展区右侧内容的右上角展示内容，若填值时不能为空，长度小于128。若用于表示到达时间跨天，传入值长度等于2，格式为"+X", 其中X为数字，例如"+1", "+2"等。  **起始版本：** 5.0.2(14)。 |
| spaceType | [SpaceType](liveview-liveviewmanager.md#spacetype) | 否 | 是 | 左右文本模板扩展区中间的显示类型。  **●** 未携带该字段或0：显示spaceIcon指定的中间间隔图标。  **●** 1：显示由spaceText指定的中间间隔文本。  **起始版本：** 5.0.2(14)。 |
| spaceIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：未填spaceType或spaceType为SpaceType.SPACE\_TYPE\_ICON时必填 | 扩展区中间间隔图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| spaceText | string | 否 | 创建或模板切换：spaceType为SpaceType.SPACE\_TYPE\_TEXT时必填 | 扩展区中间间隔文本，用于展示日期，例如10/28 周六、2025/09/15等。  限制为6个中文字符长度或12个英文字符长度，若超长则截断展示。  更新或结束不携带时显示上次的文本。  **说明：** 起始版本：5.0.2(14)。 |
| isHorizontalLineDisplayed | boolean | 否 | 是 | 是否显示扩展区分割线，默认显示分割线。  **●** true：显示。  **●** false：不显示。 |
| additionalText | string | 否 | 是 | 扩展区底部内容，长度小于1024。  **起始版本：** 5.0.0(12)。 |

## ScoreLayout

PhonePC/2in1Tablet

赛事比分模板扩展区参数，继承[LayoutData](liveview-liveviewmanager.md#layoutdata)。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_SCORE时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hostName | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区左侧名称，若填值时不能为空，长度小于128。 |
| hostIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区左侧图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| hostScore | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区左侧比分，若填值时不能为空，长度小于128。 |
| guestName | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧名称，若填值时不能为空，长度小于128。 |
| guestIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| guestScore | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区右侧比分，若填值时不能为空，长度小于128。 |
| competitionDesc | string| Array<[RichText](liveview-liveviewmanager.md#richtext)> | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区中间上方描述文本，比赛介绍，若填值时不能为空。  **●** 填string时，字符串长度需小于128。  **●** 填Array<[RichText](liveview-liveviewmanager.md#richtext)>时：  1. 数组中所有对象的text字段字符串长度总和需小于128。  2. 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色  **说明：** 从5.0.0(12)版本开始，新增支持入参类型Array<[RichText](liveview-liveviewmanager.md#richtext)>。 |
| competitionTime | string | 否 | 创建或模板切换：否  更新或结束：是 | 扩展区中间下方比赛时间，若填值时不能为空，长度小于128。 |
| isHorizontalLineDisplayed | boolean | 否 | 是 | 是否显示扩展区分割线，默认显示分割线。  **●** true：显示。  **●** false：不显示。 |

## NavigationLayout

PhonePC/2in1Tablet

导航模板扩展区参数，继承[LayoutData](liveview-liveviewmanager.md#layoutdata)。当[layoutType](liveview-liveviewmanager.md#layouttype)为LayoutType.LAYOUT\_TYPE\_NAVIGATION时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentNavigationIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建或模板切换：否  更新或结束：是 | 当前导航方向。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为128。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  若本地资源不存在，创建时失败，更新或结束时导航模板扩展区不更新。  **说明：** 为确保图片在系统深浅模式下的显示效果，系统将对png、svg格式图片做赋色处理，其他格式图片保留原样显示不支持赋色。具体参考 [卡片模板](../design-guides/system-features-live-view-0000001955186861.md#section1511241615274) 的 "导航定制模板"说明。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| navigationIcons | Array<string | image.[PixelMap](arkts-apis-image-pixelmap.md)> | 否 | 是 | 导航方向的箭头集合图片，支持1-11个。创建时不传，则不展示扩展区。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为128。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  若本地资源不存在，创建时失败，更新或结束时导航模板扩展区不更新。  **说明：** 为确保在系统深浅模式下的显示效果，系统将对png、svg格式图片做赋色处理，其他格式图片保留原样显示不支持赋色。具体参考 [卡片模板](../design-guides/system-features-live-view-0000001955186861.md#section1511241615274) 的 "导航定制模板"说明。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| isNavigationIconsDisplayed | boolean | 否 | 是 | 控制导航方向的箭头集合图片是否展示。更新或结束未填时，继承上一次状态变更时的值。其他情况不传值时默认为展示。  **●** true：展示  **●** false：不展示  **起始版本**：5.0.3(15) |

## CapsuleData

PhonePC/2in1Tablet

定义实况胶囊基本属性的基类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CapsuleType](liveview-liveviewmanager.md#capsuletype) | 否 | 否 | 实况胶囊的类型。 |
| status | number | 否 | 否 | 实况胶囊的显示状态。  **●** 1：显示实况胶囊。  **●** -1：结束显示实况胶囊。 |
| icon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建：否  更新或结束：是 | 实况胶囊的图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为255。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |
| tailIcon | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 实况胶囊的尾部图标，更新或结束不携带时显示上次的图片。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为255。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。  **起始版本：** 6.0.0(20) |
| backgroundColor | string | 否 | 创建：否  更新或结束：是 | 实况胶囊的背景颜色，"#ARGB"16进制格式，长度为9。更新或结束未填时，继承上一次状态变更时的颜色。  不建议使用以下颜色：  **●** #FF000000  **●** #FFFFFFFF  **●** #FFF1F3F5 |
| isContentDisplayed | boolean | 否 | 是 | 实况胶囊的副文本是否展示。该参数未填时，继承上一次创建或更新实况窗时传入的值。其他情况不传值时默认为展示。  **●** true：展示  **●** false：不展示  isContentDisplayed与isTailIconDisplayed均为false时，实况胶囊的副文本及尾部图标区域不展示。  **起始版本：** 5.0.3(15) |
| isTailIconDisplayed | boolean | 否 | 是 | 实况胶囊的尾部图标是否展示。该参数未填时，继承上一次创建或更新实况窗时传入的值。其他情况不传值时默认不展示。  **●** true：展示  **●** false：不展示  isContentDisplayed与isTailIconDisplayed均为false时，实况胶囊的副文本及尾部图标区域不展示。  **起始版本：** 6.0.0(20) |

## TextCapsule

PhonePC/2in1Tablet

文本实况胶囊参数，继承[CapsuleData](liveview-liveviewmanager.md#capsuledata)。当[type](liveview-liveviewmanager.md#capsuledata)为CapsuleType.CAPSULE\_TYPE\_TEXT时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 创建或模板切换：否  更新或结束：是 | 实况胶囊的主文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。  **说明：** 从6.0.0(20)版本开始，支持当传入值为"数值:数值"，且[layoutType](liveview-liveviewmanager.md#layouttype)为赛事类型LAYOUT\_TYPE\_SCORE时，系统将自动提取实况卡片扩展区两侧图片和比分，更新实况胶囊样式，显示为赛事队伍图标及比分情况。 |
| content | string | 否 | 是 | 实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。 |

## TimerCapsule

PhonePC/2in1Tablet

计时器实况胶囊参数，继承[CapsuleData](liveview-liveviewmanager.md#capsuledata)。当[type](liveview-liveviewmanager.md#capsuledata)为CapsuleType.CAPSULE\_TYPE\_TIMER时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| content | string | 否 | 是 | 实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。 |
| time | number | 否 | 是 | 实况胶囊计时器初始值，每秒刷新一次，单位：ms，默认为0。 |
| isCountdown | boolean | 否 | 是 | 是否显示倒计时器。  **●** true：倒计时。  **●** false：正计时（默认值）。 |
| isPaused | boolean | 否 | 是 | 实况胶囊计时器是否暂停，计时器暂停时，实况胶囊会显示暂停的那一秒。  **●** true：暂停。  **●** false：不暂停（默认值）。 |

## ProgressCapsule

PhonePC/2in1Tablet

进度实况胶囊参数，继承[CapsuleData](liveview-liveviewmanager.md#capsuledata)。当[type](liveview-liveviewmanager.md#capsuledata)为CapsuleType.CAPSULE\_TYPE\_PROGRESS时，使用此类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| max | number | 否 | 是 | 进度条最大进度值，默认为1，范围为[1, 2147483647]。 |
| progress | number | 否 | 是 | 进度条当前进度值，默认为0，范围为[0, 2147483647]。进度的值为progress/max的比值。 |
| indeterminate | boolean | 否 | 是 | 进度显示类型，默认显示为数值占比。  **●** true：百分比。  **●** false：数值占比（默认）。 |
| content | string | 否 | 是 | 实况胶囊的副文本，长度小于128，若传入该参数，其值不能为以下值：null/undefined/空字符串/全为空格的字符串。  **起始版本：** 6.0.0(20) |

## ExternalData

PhonePC/2in1Tablet

外屏形态模板参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 创建：否  更新或结束：是 | 外屏标题，若填值时不能为空，长度小于128。 |
| content | Array<[RichText](liveview-liveviewmanager.md#richtext)> | 否 | 创建：否  更新或结束：是 | 外屏内容，应用可以设置字符串中部分文本的颜色，若填值时不能为空。  **●** 数组中所有对象的text字段字符串长度总和需小于128。  **●** 数组中对象不设置textColor字段时，文本颜色默认为#99000000；设置textColor字段时，所有拥有textColor字段的对象仅能设置同一种颜色。 |
| type | [ExternalType](liveview-liveviewmanager.md#externaltype) | 否 | 是 | 外屏背景样式类型，默认为背景色。  **起始版本：** 5.0.0(12)。 |
| backgroundColor | string | 否 | 是 | 外屏背景颜色，"#RGB"16进制格式， 长度为7，默认颜色为#F1F3F5。 |
| backgroundPicture | string|image.[PixelMap](arkts-apis-image-pixelmap.md) | 否 | 创建：否（仅当type为ExternalType.BACKGROUND\_PICTURE时）  更新或结束：是（当type为ExternalType.BACKGROUND\_PICTURE时，此参数生效） | 外屏背景图片，更新或结束不携带时显示上次的图片。  **起始版本：** 5.0.0(12)。  **●** 当此参数类型为string时，取值为在“/resources/rawfile”路径下的本地资源文件名，长度最大为256。  示例：图片文件“icon.png”存放在应用的“/resources/rawfile”路径下，则取值为“icon.png”。  **●** 当此参数类型为image.[PixelMap](arkts-apis-image-pixelmap.md)时，图片大小不大于30KB。 |

## RichText

PhonePC/2in1Tablet

富文本参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 文本内容，长度小于128。 |
| textColor | string | 否 | 是 | 文本颜色，"#ARGB"16进制格式，长度为9。不设置textColor时，文本颜色默认为#99000000；设置textColor时，数组中的所有对象仅能设置一种颜色。 |

## LiveViewResult

PhonePC/2in1Tablet

实况窗结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| resultCode | number | 实况窗结果码。  **●** 0：成功。  **●** 1：固定区更新或结束失败。  **●** 2：辅助区更新或结束失败。  **●** 3：扩展区更新或结束失败。  **●** 4：实况胶囊更新或结束失败。  **●** 5：外屏更新或结束失败。 |
| message | String | 实况窗结果信息。 |

## LayoutType

PhonePC/2in1Tablet

扩展区类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LAYOUT\_TYPE\_DEFAULT | -1 | 不显示扩展区。 |
| LAYOUT\_TYPE\_PROGRESS | 3 | 进度可视化类型。 |
| LAYOUT\_TYPE\_PICKUP | 4 | 强调文本类型。 |
| LAYOUT\_TYPE\_FLIGHT | 5 | 左右文本类型。 |
| LAYOUT\_TYPE\_SCORE | 7 | 赛事类型。 |
| LAYOUT\_TYPE\_NAVIGATION | 8 | 导航类型。  **起始版本：** 5.0.0(12) |

## ExtensionType

PhonePC/2in1Tablet

辅助区类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EXTENSION\_TYPE\_DEFAULT | 0 | 不显示辅助区。 |
| EXTENSION\_TYPE\_COMMON\_TEXT | 1 | 普通文本。 |
| EXTENSION\_TYPE\_CAPSULE\_TEXT | 2 | 实况胶囊文本。 |
| EXTENSION\_TYPE\_PIC | 3 | 显示图片。 |
| EXTENSION\_TYPE\_ICON | 4 | 显示图标。 |

## IndicatorType

PhonePC/2in1Tablet

指示器类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INDICATOR\_TYPE\_UNDISPLAYED | 0 | 不显示指示器小图标。 |
| INDICATOR\_TYPE\_UP | 1 | 显示在进度线上方。 |
| INDICATOR\_TYPE\_OVERLAY | 2 | 显示覆盖在进度线上。 |

## LineType

PhonePC/2in1Tablet

扩展区进度条类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINE\_TYPE\_DOTTED\_LINE | 0 | 虚线进度。 |
| LINE\_TYPE\_NORMAL\_SOLID\_LINE | 1 | 实线进度。 |
| LINE\_TYPE\_THICK\_SOLID\_LINE | 2 | 粗实线进度。 |

## CapsuleType

PhonePC/2in1Tablet

实况胶囊类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAPSULE\_TYPE\_TEXT | 1 | 文本实况胶囊。 |
| CAPSULE\_TYPE\_TIMER | 2 | 计时器实况胶囊。 |
| CAPSULE\_TYPE\_PROGRESS | 3 | 进度实况胶囊。 |

## ExternalType

PhonePC/2in1Tablet

外屏背景样式类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND\_COLOR | 0 | 显示背景色。 |
| BACKGROUND\_PICTURE | 1 | 显示背景图片。 |

## FlightLayoutStyle

PhonePC/2in1Tablet

左右文本子样式类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STYLE\_FLIGHT\_EMPHASIS | 0 | 强调型子样式类型。 |
| STYLE\_FLIGHT\_BALANCE | 1 | 均衡型子样式类型。 |

说明

扩展区支持强调型和均衡型两种子样式，两种子样式区别在于左右文本标题和内容字号大小不同，均衡型左右文本标题字号缩小，内容字号增大，展示效果更均衡。详细模板设计样式请参考：[实况窗设计指南>通用卡片模板>模板类型>左右文本模板](../design-guides/system-features-live-view-0000001955186861.md#section1511241615274)。

## SpaceType

PhonePC/2in1Tablet

左右文本模板扩展区中间的显示类型，为枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPACE\_TYPE\_ICON | 0 | 扩展区中间显示图标。 |
| SPACE\_TYPE\_TEXT | 1 | 扩展区中间显示文本。 |
