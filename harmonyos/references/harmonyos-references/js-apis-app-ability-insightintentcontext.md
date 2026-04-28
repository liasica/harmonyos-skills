---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentcontext
title: @ohos.app.ability.InsightIntentContext (意图执行上下文)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.InsightIntentContext (意图执行上下文)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f92349457d150f6afa26f08cdc0739aaebe568bf655741bd78a23ac85bbf6eb9
---

本模块提供意图执行上下文，是[意图执行基类](js-apis-app-ability-insightintentexecutor.md)和[@InsightIntentEntry的意图执行基类](js-apis-app-ability-insightintententryexecutor.md)的属性，为意图执行提供基础能力，例如启动本应用内的[UIAbility组件](js-apis-app-ability-uiability.md)。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InsightIntentContext } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| instanceId23+ | number | 否 | 否 | 意图实例唯一ID。用于通过[insightIntentProvider.sendExecuteResult接口](js-apis-app-ability-insightintentprovider.md#insightintentprovidersendexecuteresult)和[insightIntentProvider.sendIntentResult接口](js-apis-app-ability-insightintentprovider.md#insightintentprovidersendintentresult)返回指定意图的执行结果。 |

**示例：**

```
1. import { InsightIntentExecutor, insightIntent, insightIntentProvider } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class InsightIntentExecutorUI extends InsightIntentExecutor {
7. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
8. pageLoader: window.WindowStage): insightIntent.ExecuteResult {
9. hilog.info(0x0000, 'testTag', 'onExecuteInUIAbilityForegroundMode %{public}s', name);
10. let result: insightIntent.ExecuteResult;
11. result = {
12. code: 0,
13. result: {
14. message: 'Unsupported insight intent.',
15. },
16. };
17. try {
18. // 通过意图实例唯一ID返回意图执行结果
19. insightIntentProvider.sendExecuteResult(this.context.instanceId, result)
20. .then(() => {
21. console.info('testTag setExecuteResult success');
22. })
23. .catch((error: BusinessError) => {
24. console.error(`testTag setExecuteResult fail1, error code: ${JSON.stringify(error)}`);
25. });
26. } catch (e) {
27. let code = (e as BusinessError).code;
28. let msg = (e as BusinessError).message;
29. console.error(`testTag setExecuteResult fail2, error code: ${JSON.stringify(code)}, error msg: ${JSON.stringify(msg)}`);
30. }
31. return result;
32. }
33. }
```

## InsightIntentContext.startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, callback: AsyncCallback<void>): void

启动UIAbility组件，仅支持启动本应用内的UIAbility组件。使用callback异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility组件的want信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当接口调用成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000061 | Operation not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { InsightIntentExecutor, insightIntent, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class IntentExecutorImpl extends InsightIntentExecutor {
6. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
7. pageLoader: window.WindowStage): insightIntent.ExecuteResult {
8. let want: Want = {
9. bundleName: 'com.ohos.intentExecuteDemo', // 此处仅为示例，开发者在实际使用中需替换为真实包名
10. moduleName: 'entry',
11. abilityName: 'AnotherAbility',
12. };

14. try {
15. this.context.startAbility(want, (error) => {
16. if (error) {
17. hilog.error(0x0000, 'testTag', 'Start ability failed with %{public}s', JSON.stringify(error));
18. } else {
19. hilog.info(0x0000, 'testTag', '%{public}s', 'Start ability succeed');
20. }
21. })
22. } catch (error) {
23. hilog.error(0x0000, 'testTag', 'Start ability error caught %{public}s', JSON.stringify(error));
24. }

26. let result: insightIntent.ExecuteResult = {
27. code: 0,
28. result: {
29. message: 'Execute insight intent succeed.',
30. }
31. };
32. return result;
33. }
34. }
```

## InsightIntentContext.startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want): Promise<void>

启动UIAbility组件，仅支持启动本应用内的UIAbility组件。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility组件的want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000061 | Operation not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { InsightIntentExecutor, insightIntent, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class IntentExecutorImpl extends InsightIntentExecutor {
6. async onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
7. pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
8. let want: Want = {
9. bundleName: 'com.ohos.intentExecuteDemo', // 此处仅为示例，开发者在实际使用中需替换为真实包名
10. moduleName: 'entry',
11. abilityName: 'AnotherAbility',
12. };

14. try {
15. await this.context.startAbility(want);
16. hilog.info(0x0000, 'testTag', '%{public}s', 'Start ability finished');
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'Start ability error caught %{public}s', JSON.stringify(error));
19. }

21. let result: insightIntent.ExecuteResult = {
22. code: 0,
23. result: {
24. message: 'Execute insight intent succeed.',
25. }
26. };
27. return result;
28. }
29. }
```

## InsightIntentContext.setReturnModeForUIAbilityForeground23+

PhonePC/2in1TabletTVWearable

setReturnModeForUIAbilityForeground(returnMode: insightIntent.ReturnMode): void

设置意图执行结果的返回形式，适用于执行模式为[UI\_ABILITY\_FOREGROUND](js-apis-app-ability-insightintent.md#executemode)的意图。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| returnMode | [insightIntent.ReturnMode](js-apis-app-ability-insightintent.md#returnmode23) | 是 | 意图执行结果的返回形式。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. Possible causes: 1.The context is not insightIntentContext; 2.The context is not for UIAbility foreground insight intent execute mode. |

**示例：**

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

17. try {
18. this.context.setReturnModeForUIAbilityForeground(insightIntent.ReturnMode.FUNCTION);
19. } catch (error) {
20. let code = (error as BusinessError).code;
21. let msg = (error as BusinessError).message;
22. console.error(`testTag setReturnModeForUIAbilityForeground fail, error code: ${code}, err msg: ${msg}.`);
23. }

25. let localStorageData: Record<string, number> = {
26. 'insightId': this.context.instanceId,
27. };
28. let storage: LocalStorage = new LocalStorage(localStorageData);
29. pageLoader.loadContent('pages/UIAbilityIndex', storage, (err, data) => {
30. if (err.code) {
31. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
32. } else {
33. hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
34. }
35. });
36. return result;
37. }
38. }
```

## InsightIntentContext.setReturnModeForUIExtensionAbility23+

PhonePC/2in1TabletTVWearable

setReturnModeForUIExtensionAbility(returnMode: insightIntent.ReturnMode): void

设置意图执行结果的返回形式，适用于执行模式为[UI\_EXTENSION\_ABILITY](js-apis-app-ability-insightintent.md#executemode)的意图。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| returnMode | [insightIntent.ReturnMode](js-apis-app-ability-insightintent.md#returnmode23) | 是 | 意图执行结果的返回形式。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. Possible causes: 1.The context is not insightIntentContext; 2.The context is not for UIExtensionAbility insight intent execute mode. |

**示例：**

```
1. import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class InsightIntentExecutorUI extends InsightIntentExecutor {
5. onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
6. pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult {
7. hilog.info(0x0000, 'testTag', 'onExecuteInUIExtensionAbility %{public}s', name);
8. let result: insightIntent.ExecuteResult;
9. result = {
10. code: 0,
11. result: {
12. message: 'Unsupported insight intent.',
13. },
14. };
15. try {
16. this.context.setReturnModeForUIExtensionAbility(insightIntent.ReturnMode.FUNCTION)
17. } catch (error) {
18. let code = (error as BusinessError).code;
19. let msg = (error as BusinessError).message;
20. console.error(`testTag setReturnModeForUIExtensionAbility fail, error code: ${code}, error msg: ${msg}.`);
21. }

23. try {
24. let localStorageData: Record<string, number> = {
25. 'insightId': this.context.instanceId,
26. };
27. let storage: LocalStorage = new LocalStorage(localStorageData);
28. storage.setOrCreate('session', pageLoader);
29. pageLoader.loadContent('pages/UIExtensionPage', storage);
30. } catch (err) {
31. let code = (err as BusinessError).code;
32. let msg = (err as BusinessError).message;
33. console.info(`testTag loadContent error code: ${code}, error msg: ${msg}.`);
34. }
35. return result;
36. }
37. }
```
