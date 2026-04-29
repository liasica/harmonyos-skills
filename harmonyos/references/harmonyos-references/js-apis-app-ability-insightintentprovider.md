---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentprovider
title: @ohos.app.ability.insightIntentProvider (意图提供方管理能力)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.insightIntentProvider (意图提供方管理能力)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:32+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:711a63f356b456f5e9d9043317c211f56d7830cf2da60f8c73301310bce7e2d2
---

本模块为意图提供方提供管理能力，如主动发送指定意图的执行结果。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { insightIntentProvider } from '@kit.AbilityKit';
```

## insightIntentProvider.sendExecuteResult

PhonePC/2in1TabletTVWearable

sendExecuteResult(instanceId: number, result: insightIntent.ExecuteResult): Promise<void>

如果意图提供方需要在业务处理的特定流程中主动发送意图执行结果，可以先通过[setReturnModeForUIAbilityForeground接口](js-apis-app-ability-insightintentcontext.md#insightintentcontextsetreturnmodeforuiabilityforeground23)或[setReturnModeForUIExtensionAbility接口](js-apis-app-ability-insightintentcontext.md#insightintentcontextsetreturnmodeforuiextensionability23)将意图执行结果返回形式[ReturnMode](js-apis-app-ability-insightintent.md#returnmode23)设置为FUNCTION，然后调用该接口发送意图执行结果，适用于[配置类意图](../harmonyos-guides/insight-intent-config-development.md)。使用Promise异步回调。

意图执行结果返回形式[ReturnMode](js-apis-app-ability-insightintent.md#returnmode23)设置为FUNCTION后，应用将无需再通过[onExecuteInUIAbilityForegroundMode接口](js-apis-app-ability-insightintentexecutor.md#onexecuteinuiabilityforegroundmode)或[onExecuteInUIExtensionAbility接口](js-apis-app-ability-insightintentexecutor.md#onexecuteinuiextensionability)的返回值返回意图执行结果。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [instanceId](js-apis-app-ability-insightintentcontext.md#属性) | number | 是 | 意图实例唯一ID。 |
| result | [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | 是 | 返回意图执行结果，表示本次意图执行返回给系统入口的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000003 | The specified ID does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |

**示例：**

设置意图执行结果延迟返回示例：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class InsightIntentExecutorUI extends InsightIntentExecutor {
6. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
7. pageLoader: window.WindowStage): insightIntent.ExecuteResult {
8. hilog.info(0x0000, 'testTag', 'onExecuteInUIAbilityForegroundMode %{public}s', name);
9. let result: insightIntent.ExecuteResult;
10. result = {
11. code: 0,
12. result: {
13. message: 'Unsupported insight intent.',
14. },
15. };
16. try {
17. // 设置意图执行结果的返回形式为延迟返回
18. this.context.setReturnModeForUIAbilityForeground(insightIntent.ReturnMode.FUNCTION);
19. } catch (error) {
20. let code = (error as BusinessError).code;
21. let msg = (error as BusinessError).message;
22. console.error(`testTag setReturnModeForUIExtensionAbility fail, error code: ${code}, error msg: ${msg}.`);
23. }
24. // 将意图实例的id通过localStorage传入目标页面中
25. let localStorageData: Record<string, number> = {
26. 'insightId': this.context.instanceId,
27. };
28. let storage: LocalStorage = new LocalStorage(localStorageData);
29. // 通过pageLoader加载页面
30. pageLoader.loadContent('pages/UIAbilityIndex', storage, (err, data) => {
31. if (err.code) {
32. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
33. } else {
34. hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
35. }
36. });
37. return result;
38. }
39. }
```

主动发送意图执行结果示例：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { insightIntent, insightIntentProvider } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. insightId: number | undefined = this.storage?.get<number>('insightId');

10. build() {
11. Column() {
12. // 通过sendExecuteResult接口主动返回意图执行结果
13. Button('insightIntentProvider sendExecuteResult')
14. .onClick(() => {
15. try {
16. let result: insightIntent.ExecuteResult;
17. result = {
18. code: 0,
19. result: {
20. message: 'Unsupported insight intent.',
21. },
22. };
23. insightIntentProvider.sendExecuteResult(this.insightId, result)
24. .then(() => {
25. console.info('testTag setExecuteResult success');
26. })
27. .catch((error: BusinessError) => {
28. console.error(`testTag setExecuteResult fail1, error code: ${error.code}, error msg: ${error.message}.`);
29. });
30. } catch (e) {
31. let code = (e as BusinessError).code;
32. let msg = (e as BusinessError).message;
33. console.error(`testTag setExecuteResult fail2, error code: ${code}, error msg: ${msg}`);
34. }
35. })
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

## insightIntentProvider.sendIntentResult

PhonePC/2in1TabletTVWearable

sendIntentResult(instanceId: number, result: insightIntent.IntentResult<T>): Promise<void>

如果意图提供方需要在业务处理的特定流程中主动发送意图执行结果，可以先通过[setReturnModeForUIAbilityForeground接口](js-apis-app-ability-insightintentcontext.md#insightintentcontextsetreturnmodeforuiabilityforeground23)或[setReturnModeForUIExtensionAbility接口](js-apis-app-ability-insightintentcontext.md#insightintentcontextsetreturnmodeforuiextensionability23)将意图执行结果返回形式[ReturnMode](js-apis-app-ability-insightintent.md#returnmode23)设置为FUNCTION，然后调用该接口发送意图执行结果。适用于[@InsightIntentEntry](js-apis-app-ability-insightintentdecorator.md#insightintententry)修饰的[装饰器类意图](../harmonyos-guides/insight-intent-decorator-development.md)。使用Promise异步回调。

意图执行结果返回形式[ReturnMode](js-apis-app-ability-insightintent.md#returnmode23)设置为FUNCTION后，应用将无需再通过[onExecute接口](js-apis-app-ability-insightintententryexecutor.md#onexecute)的返回值返回意图执行结果。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| [instanceId](js-apis-app-ability-insightintentcontext.md#属性) | number | 是 | 意图实例唯一ID。 |
| result | [insightIntent.IntentResult<T>](js-apis-app-ability-insightintent.md#intentresultt20) | 是 | 返回意图执行结果，表示本次意图执行返回给系统入口的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000003 | The specified ID does not exist. |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |

**示例：**

设置意图执行结果延迟返回示例：

```
1. import { insightIntent, InsightIntentEntry, InsightIntentEntryExecutor } from '@kit.AbilityKit';

3. class PlayVideoResultDef {
4. resultCode: number = 0;
5. resultMsg: string = '';
6. someInvalid1: string | undefined = undefined;
7. someInvalid2: string | null = null;
8. }

10. // 播放视频
11. @InsightIntentEntry({
12. intentName: 'PlayVideo',
13. domain: 'VideosDomain',
14. intentVersion: '1.0.2',
15. displayName: '播放视频',
16. displayDescription: '播放视频意图',
17. schema: 'PlayVideo',
18. icon: $r('app.media.background'),
19. llmDescription: '播放视频意图',
20. keywords: ['视频播放', '播放视频', 'PlayVideo'],
21. abilityName: 'EntryAbility1',
22. executeMode: [insightIntent.ExecuteMode.UI_ABILITY_FOREGROUND],
23. })
24. export default class PlayVideo extends InsightIntentEntryExecutor<PlayVideoResultDef> {
25. entityId: string = 'zhz';
26. episodeId: string = '50';
27. episodeNumber: number = 12;

29. onExecute(): Promise<insightIntent.IntentResult<PlayVideoResultDef>> {
30. console.info('testTag', 'PlayVideo onExecute success')
31. let result: insightIntent.IntentResult<PlayVideoResultDef> = {
32. code: 0,
33. result: {
34. resultCode: 0x0000,
35. resultMsg: 'Callback PlayVideo Success',
36. someInvalid1: undefined,
37. someInvalid2: null
38. }
39. }
40. let instanceId: number = this.context.instanceId;
41. try {
42. // 设置意图执行结果的返回形式为延迟返回
43. this.context.setReturnModeForUIAbilityForeground(insightIntent.ReturnMode.FUNCTION);
44. console.info('testTag: setReturnModeForUIAbilityForeground success');
45. } catch (error) {
46. let code = (error as BusinessError).code;
47. let msg = (error as BusinessError).message;
48. console.error(`testTag: setReturnModeForUIAbilityForeground failed, error code: ${code}, error msg: ${msg}.`);
49. }

51. try {
52. // 将意图实例的id通过localStorage传入目标页面中
53. let localStorageData: Record<string, number> = {
54. 'insightId': instanceId,
55. };
56. let storage: LocalStorage = new LocalStorage(localStorageData);
57. // 通过pageLoader加载页面
58. this.windowStage?.loadContent('pages/Index', storage);
59. console.info('testTag', 'Succeeded in loading the content1')
60. } catch (err) {
61. let code = (err as BusinessError).code;
62. let msg = (err as BusinessError).message;
63. console.error(`testTag loadContent error code: ${code}, error msg: ${msg}.`);
64. }
65. return Promise.resolve(result);
66. }
67. }
```

主动发送意图执行结果示例：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { insightIntent, insightIntentProvider } from '@kit.AbilityKit';

4. class PlayVideoResultDef {
5. resultCode: number = 0;
6. resultMsg: string = '';
7. someInvalid1: string | undefined = undefined;
8. someInvalid2: string | null = null;
9. }

11. @Entry
12. @Component
13. struct Index {
14. storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
15. insightId: number | undefined = this.storage?.get<number>('insightId');

17. build() {
18. Column() {
19. // 通过sendExecuteResult接口主动返回意图执行结果
20. Button('insightIntentProvider sendIntentResult')
21. .onClick(() => {
22. try {
23. let result: insightIntent.IntentResult<PlayVideoResultDef> = {
24. code: 0,
25. result: {
26. resultCode: 123,
27. resultMsg: 'Function PlayVideo Success',
28. someInvalid1: undefined,
29. someInvalid2: null
30. }
31. }
32. insightIntentProvider.sendIntentResult(this.insightId, result)
33. .then(() => {
34. console.info('testTag sendIntentResult success');
35. })
36. .catch((error: BusinessError) => {
37. console.error(`testTag sendIntentResult error, error code: ${error.code}, error msg: ${error.message}.`);
38. });
39. } catch (error) {
40. let code = (error as BusinessError).code;
41. let msg = (error as BusinessError).message;
42. console.error(`testTag sendIntentResult fail, error code: ${code}, error msg: ${msg}.`);
43. }
44. })
45. }
46. .height('100%')
47. .width('100%')
48. }
49. }
```
