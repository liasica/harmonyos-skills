---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentexecutor
title: @ohos.app.ability.InsightIntentExecutor (意图执行基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.InsightIntentExecutor (意图执行基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:964bfbf7c32d74537a55d0f37b84da20f36838d678e32086c6c63e6653b96043
---

本模块提供意图执行基类，开发者通过本模块对接端侧[意图框架](../harmonyos-guides/insight-intent-overview.md)，[通过配置文件开发意图](../harmonyos-guides/insight-intent-config-development.md)实现意图的业务逻辑。

除了可以通过配置文件开发意图，还可以通过装饰器开发意图。对于API version 20及以后的版本，推荐使用[通过装饰器开发意图](../harmonyos-guides/insight-intent-decorator-development.md)。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InsightIntentExecutor } from '@kit.AbilityKit';
```

## InsightIntentExecutor

PhonePC/2in1TabletTVWearable

表示意图执行基类。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [InsightIntentContext](js-apis-app-ability-insightintentcontext.md) | 否 | 否 | 意图执行上下文。 |

### onExecuteInUIAbilityForegroundMode

PhonePC/2in1TabletTVWearable

onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIAbility](js-apis-app-ability-uiability.md)组件前台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)、onExecuteInUIAbilityForegroundMode、[onForeground](js-apis-app-ability-uiability.md#onforeground)。
* 若UIAbility组件热启动，且启动时UIAbility组件处于后台，意图执行时UIAbility组件生命周期触发顺序：[onNewWant](js-apis-app-ability-uiability.md#onnewwant)、onExecuteInUIAbilityForegroundMode、[onForeground](js-apis-app-ability-uiability.md#onforeground)。
* 若UIAbility组件热启动，且启动时UIAbility组件处于前台，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityForegroundMode。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |
| pageLoader | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 表示windowStage实例对象，和[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)接口的windowStage实例是同一个，可用于加载意图执行的页面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class IntentExecutorImpl extends InsightIntentExecutor {
6. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
7. pageLoader: window.WindowStage): insightIntent.ExecuteResult {
8. let result: insightIntent.ExecuteResult;
9. if (name !== 'SupportedInsightIntentName') {
10. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
11. result = {
12. // 由开发者定义
13. code: 404,
14. result: {
15. message: 'Unsupported insight intent.',
16. }
17. };
18. return result;
19. }

21. // 若开发者需要加载意图内容，pages/IntentPage即为意图页面
22. pageLoader.loadContent('pages/IntentPage', (err, data) => {
23. if (err.code) {
24. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
25. } else {
26. hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in loading the content');
27. }
28. });

30. result = {
31. code: 0,
32. result: {
33. message: 'Execute insight intent succeed.',
34. }
35. };
36. return result;
37. }
38. }
```

使用Promise异步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
6. return new Promise((resolve, reject) => {
7. let result: insightIntent.ExecuteResult = {
8. code: 0,
9. result: {
10. message: 'Execute insight intent succeed.',
11. }
12. };
13. resolve(result);
14. })
15. }

17. export default class IntentExecutorImpl extends InsightIntentExecutor {
18. // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
19. async onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>,
20. pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
21. let result: insightIntent.ExecuteResult;
22. if (name !== 'SupportedInsightIntentName') {
23. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
24. result = {
25. // 由开发者定义
26. code: 404,
27. result: {
28. message: 'Unsupported insight intent.',
29. }
30. };
31. return result;
32. }

34. result = await executeInsightIntent(param);
35. return result;
36. }
37. }
```

### onExecuteInUIAbilityBackgroundMode

PhonePC/2in1TabletTVWearable

onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIAbility](js-apis-app-ability-uiability.md)组件后台启动时，会在UIAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 若UIAbility组件冷启动，意图执行时UIAbility组件生命周期触发顺序：[onCreate](js-apis-app-ability-uiability.md#oncreate)、onExecuteInUIAbilityBackgroundMode、[onBackground](js-apis-app-ability-uiability.md#onbackground)。
* 若UIAbility组件热启动，意图执行时UIAbility组件生命周期触发顺序：onExecuteInUIAbilityBackgroundMode。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';

3. export default class IntentExecutorImpl extends InsightIntentExecutor {
4. onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
5. let result: insightIntent.ExecuteResult = {
6. code: 0,
7. result: {
8. message: 'Execute insight intent succeed.',
9. }
10. };
11. return result;
12. }
13. }
```

使用Promise异步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';

3. async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
4. return new Promise((resolve, reject) => {
5. let result: insightIntent.ExecuteResult = {
6. code: 0,
7. result: {
8. message: 'Execute insight intent succeed.',
9. }
10. };
11. resolve(result);
12. })
13. }

15. export default class IntentExecutorImpl extends InsightIntentExecutor {
16. // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
17. async onExecuteInUIAbilityBackgroundMode(name: string,
18. param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
19. let result: insightIntent.ExecuteResult = await executeInsightIntent(param);
20. return result;
21. }
22. }
```

### onExecuteInUIExtensionAbility

PhonePC/2in1TabletTVWearable

onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)启动时，会在UIExtensionAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 意图执行时UIExtensionAbility生命周期触发顺序：[onCreate](js-apis-app-ability-uiextensionability.md#oncreate)、[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)、onExecuteInUIExtensionAbility、[onForeground](js-apis-app-ability-uiextensionability.md#onforeground)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |
| pageLoader | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | 表示UIExtensionContentSession实例对象，和[onSessionCreate](js-apis-app-ability-uiextensionability.md#onsessioncreate)接口的UIExtensionContentSession实例是同一个，可用于加载意图执行的页面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class IntentExecutorImpl extends InsightIntentExecutor {
5. onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
6. pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult {
7. let result: insightIntent.ExecuteResult;
8. if (name !== 'SupportedInsightIntentName') {
9. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
10. result = {
11. // 由开发者定义
12. code: 404,
13. result: {
14. message: 'Unsupported insight intent.',
15. }
16. };
17. return result;
18. }

20. // 若开发者需要加载意图内容，pages/Index即为意图页面
21. pageLoader.loadContent('pages/Index');

23. result = {
24. code: 0,
25. result: {
26. message: 'Execute insight intent succeed.',
27. }
28. };
29. return result;
30. }
31. }
```

使用Promise异步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent, UIExtensionContentSession } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
5. return new Promise((resolve, reject) => {
6. let result: insightIntent.ExecuteResult = {
7. code: 0,
8. result: {
9. message: 'Execute insight intent succeed.',
10. }
11. };
12. resolve(result);
13. })
14. }

16. export default class IntentExecutorImpl extends InsightIntentExecutor {
17. // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
18. async onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>,
19. pageLoader: UIExtensionContentSession): Promise<insightIntent.ExecuteResult> {
20. let result: insightIntent.ExecuteResult;
21. if (name !== 'SupportedInsightIntentName') {
22. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
23. result = {
24. // 由开发者定义
25. code: 404,
26. result: {
27. message: 'Unsupported insight intent.',
28. }
29. };
30. return result;
31. }

33. result = await executeInsightIntent(param);
34. return result;
35. }
36. }
```

### onExecuteInServiceExtensionAbility

PhonePC/2in1TabletTVWearable

onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>

当意图执行依赖ServiceExtensionAbility组件启动时，会在ServiceExtensionAbility组件生命周期执行中触发本意图执行接口。支持同步返回和使用Promise异步返回。

* 意图执行时ServiceExtensionAbility生命周期触发顺序：onCreate、onRequest、onExecuteInServiceExtensionAbility。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 意图名称。 |
| param | Record<string, Object> | 是 | 意图参数，表示本次意图执行由系统入口传递给应用的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult) | Promise<[insightIntent.ExecuteResult](js-apis-app-ability-insightintent.md#executeresult)> | 返回意图执行结果或返回带有意图执行结果的Promise对象，表示本次意图执行返回给系统入口的数据。 |

**示例：**

同步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export default class IntentExecutorImpl extends InsightIntentExecutor {
5. onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult {
6. let result: insightIntent.ExecuteResult;
7. if (name !== 'SupportedInsightIntentName') {
8. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
9. result = {
10. // 由开发者定义
11. code: 404,
12. result: {
13. message: 'Unsupported insight intent.',
14. }
15. };
16. return result;
17. }

19. result = {
20. code: 0,
21. result: {
22. message: 'Execute insight intent succeed.',
23. }
24. };
25. return result;
26. }
27. }
```

使用Promise异步返回意图执行结果的示例如下：

```
1. import { InsightIntentExecutor, insightIntent } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function executeInsightIntent(param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
5. return new Promise((resolve, reject) => {
6. let result: insightIntent.ExecuteResult = {
7. code: 0,
8. result: {
9. message: 'Execute insight intent succeed.',
10. }
11. };
12. resolve(result);
13. });
14. }

16. export default class IntentExecutorImpl extends InsightIntentExecutor {
17. // 实现异步接口需要使用async/await语法糖，通过async声明该接口是一个异步函数
18. async onExecuteInServiceExtensionAbility(name: string,
19. param: Record<string, Object>): Promise<insightIntent.ExecuteResult> {
20. let result: insightIntent.ExecuteResult;
21. if (name !== 'SupportedInsightIntentName') {
22. hilog.warn(0x0000, 'testTag', 'Unsupported insight intent %{public}s', name);
23. result = {
24. // 由开发者定义
25. code: 404,
26. result: {
27. message: 'Unsupported insight intent.',
28. }
29. };
30. return result;
31. }

33. result = await executeInsightIntent(param);
34. return result;
35. }
36. }
```
