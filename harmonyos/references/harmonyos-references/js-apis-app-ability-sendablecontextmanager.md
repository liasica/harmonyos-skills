---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-sendablecontextmanager
title: @ohos.app.ability.sendableContextManager (sendable上下文管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.sendableContextManager (sendable上下文管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d22d5d846ddb73ec5e5e8e738f6465f28e7ffc8da86cb3bda2c7fc8a163228f
---

sendableContextManager模块提供Context与[SendableContext](js-apis-inner-application-sendablecontext.md)相互转换的能力。

说明

* 本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 使用场景

PhonePC/2in1TabletTVWearable

本模块主要用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

例如，从主线程向子线程（如TaskPool或Worker工作线程）传递Sendable数据（符合[Sendable协议](../harmonyos-guides/arkts-sendable.md#sendable协议)的数据）时，需要通过Context与SendableContext之间的相互转换来实现。过程如下：

* 主线程向子线程传递Sendable数据时，需要将Context转换为SendableContext。
* 子线程使用Sendable数据时，需要将SendableContext转换为Context。

这里的Context与[createModuleContext](js-apis-app-ability-application.md#applicationcreatemodulecontext)方法创建的Context不同，具体差异如下：

* 与SendableContext相互转换的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应同一个Context对象。当一个实例中Context属性和方法被修改时，相关实例中的Context属性和方法将会同步修改。其中，Context实例中的eventHub属性比较特殊，不同实例中的eventHub是独立的对象，不支持跨ArkTS实例使用。如果需要使用[EventHub](js-apis-inner-application-eventhub.md)跨实例传递数据，可以通过[setEventHubMultithreadingEnabled](js-apis-app-ability-sendablecontextmanager.md#sendablecontextmanagerseteventhubmultithreadingenabled20)启用跨线程数据传递功能。
* 通过[createModuleContext](js-apis-app-ability-application.md#applicationcreatemodulecontext)创建的Context：ArkTS并发实例持有的应用侧Context是不同的实例，底层对应不同的Context对象。

## 约束限制

PhonePC/2in1TabletTVWearable

“Context转换为SendableContext”和“SendableContext转换为Context”两个环节中的Context类型必须保持一致。例如，主线程使用[convertFromContext](js-apis-app-ability-sendablecontextmanager.md#sendablecontextmanagerconvertfromcontext)将[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)转换为SendableContext，子线程收到该SendableContext之后，需要通过[convertToUIAbilityContext](js-apis-app-ability-sendablecontextmanager.md#sendablecontextmanagerconverttouiabilitycontext)将SendableContext转换为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。

目前支持转换的Context包括[Context](js-apis-inner-application-context.md)、[ApplicationContext](js-apis-inner-application-applicationcontext.md)、[AbilityStageContext](js-apis-inner-application-abilitystagecontext.md)、[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableContextManager } from '@kit.AbilityKit';
```

## SendableContext

PhonePC/2in1TabletTVWearable

type SendableContext = \_SendableContext

Sendable上下文，符合[Sendable协议](../harmonyos-guides/arkts-sendable.md#sendable协议)，继承自[lang.ISendable](js-apis-arkts-lang.md#langisendable)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [\_SendableContext](js-apis-inner-application-sendablecontext.md) | 表示Sendable上下文，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。 |

## sendableContextManager.convertFromContext

PhonePC/2in1TabletTVWearable

convertFromContext(context: common.Context): SendableContext

将Context转换为SendableContext对象。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context对象。支持Context基类，[ApplicationContext](js-apis-inner-application-applicationcontext.md)、[AbilityStageContext](js-apis-inner-application-abilitystagecontext.md)和[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)子类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SendableContext | [SendableContext](js-apis-inner-application-sendablecontext.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, sendableContextManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { worker } from '@kit.ArkTS';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext) {
8. this.sendableContext = sendableContext;
9. }

11. sendableContext: sendableContextManager.SendableContext;
12. // other sendable object
13. }

15. export default class EntryAbility extends UIAbility {
16. worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

18. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
19. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

21. // convert and post
22. try {
23. let sendableContext: sendableContextManager.SendableContext =
24. sendableContextManager.convertFromContext(this.context);
25. let object: SendableObject = new SendableObject(sendableContext);
26. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
27. this.worker.postMessageWithSharedSendable(object);
28. } catch (error) {
29. hilog.error(0x0000, 'testTag', `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`);
30. }
31. }
32. }
```

## sendableContextManager.convertToContext

PhonePC/2in1TabletTVWearable

convertToContext(sendableContext: SendableContext): common.Context

将SendableContext对象转换为Context。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](js-apis-inner-application-sendablecontext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.Context | [Context](js-apis-inner-application-context.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```
1. import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { worker } from '@kit.ArkTS';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. export default class EntryAbility extends UIAbility {
17. worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

19. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

22. // convert and post
23. try {
24. let context: common.Context = this.context as common.Context;
25. let sendableContext: sendableContextManager.SendableContext = sendableContextManager.convertFromContext(context);
26. let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
27. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
28. this.worker.postMessageWithSharedSendable(object);
29. } catch (error) {
30. hilog.error(
31. 0x0000, 'testTag', `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`);
32. }
33. }
34. }
```

Worker线程接收Context：

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { common, sendableContextManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

18. workerPort.onmessage = (e: MessageEvents) => {
19. let object: SendableObject = e.data;
20. let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
21. if (object.contextName == 'BaseContext') {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'convert to context.');
23. try {
24. let context: common.Context = sendableContextManager.convertToContext(sendableContext);
25. // 获取context后获取沙箱路径
26. hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
27. } catch (error) {
28. hilog.error(
29. 0x0000, 'testTag', `convertToContext failed, error code: ${error.code}, error msg: ${error.message}`);
30. }
31. }
32. }

34. workerPort.onmessageerror = (e: MessageEvents) => {
35. hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
36. }

38. workerPort.onerror = (e: ErrorEvent) => {
39. hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
40. }
```

## sendableContextManager.convertToApplicationContext

PhonePC/2in1TabletTVWearable

convertToApplicationContext(sendableContext: SendableContext): common.ApplicationContext

将SendableContext对象转换为ApplicationContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](js-apis-inner-application-sendablecontext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.ApplicationContext | [ApplicationContext](js-apis-inner-application-applicationcontext.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```
1. import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { worker } from '@kit.ArkTS';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. export default class EntryAbility extends UIAbility {
17. worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

19. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

22. // convert and post
23. try {
24. let context: common.Context = this.context as common.Context;
25. let applicationContext = context.getApplicationContext();
26. let sendableContext: sendableContextManager.SendableContext =
27. sendableContextManager.convertFromContext(applicationContext);
28. let object: SendableObject = new SendableObject(sendableContext, 'ApplicationContext');
29. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
30. this.worker.postMessageWithSharedSendable(object);
31. } catch (error) {
32. hilog.error(
33. 0x0000, 'testTag', `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`);
34. }
35. }
36. }
```

Worker线程接收Context：

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { common, sendableContextManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

18. workerPort.onmessage = (e: MessageEvents) => {
19. let object: SendableObject = e.data;
20. let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
21. if (object.contextName == 'ApplicationContext') {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'convert to application context.');
23. try {
24. let context: common.ApplicationContext = sendableContextManager.convertToApplicationContext(sendableContext);
25. // 获取context后获取沙箱路径
26. hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
27. } catch (error) {
28. hilog.error(0x0000,
29. 'testTag', `convertToApplicationContext failed, error code: ${error.code}, error msg: ${error.message}`);
30. }
31. }
32. }

34. workerPort.onmessageerror = (e: MessageEvents) => {
35. hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
36. }

38. workerPort.onerror = (e: ErrorEvent) => {
39. hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
40. }
```

## sendableContextManager.convertToAbilityStageContext

PhonePC/2in1TabletTVWearable

convertToAbilityStageContext(sendableContext: SendableContext): common.AbilityStageContext

将SendableContext对象转换为AbilityStageContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](js-apis-inner-application-sendablecontext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.AbilityStageContext | [AbilityStageContext](js-apis-inner-application-abilitystagecontext.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```
1. import { UIAbility, sendableContextManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { worker } from '@kit.ArkTS';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. export default class EntryAbility extends UIAbility {
17. worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

19. onCreate(): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage onCreate');

22. // convert and post
23. try {
24. let sendableContext: sendableContextManager.SendableContext =
25. sendableContextManager.convertFromContext(this.context);
26. let object: SendableObject = new SendableObject(sendableContext, 'AbilityStageContext');
27. hilog.info(0x0000, 'testTag', '%{public}s', 'AbilityStage post message');
28. this.worker.postMessageWithSharedSendable(object);
29. } catch (error) {
30. hilog.error(
31. 0x0000, 'testTag', `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`);
32. }
33. }
34. }
```

Worker线程接收Context：

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { common, sendableContextManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

18. workerPort.onmessage = (e: MessageEvents) => {
19. let object: SendableObject = e.data;
20. let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
21. if (object.contextName == 'AbilityStageContext') {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'convert to abilitystage context.');
23. try {
24. let context: common.AbilityStageContext = sendableContextManager.convertToAbilityStageContext(sendableContext);
25. // 获取context后获取沙箱路径
26. hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
27. } catch (error) {
28. hilog.error(0x0000,
29. 'testTag', `convertToAbilityStageContext failed, error code: ${error.code}, error msg: ${error.message}`);
30. }
31. }
32. }

34. workerPort.onmessageerror = (e: MessageEvents) => {
35. hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
36. }

38. workerPort.onerror = (e: ErrorEvent) => {
39. hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
40. }
```

## sendableContextManager.convertToUIAbilityContext

PhonePC/2in1TabletTVWearable

convertToUIAbilityContext(sendableContext: SendableContext): common.UIAbilityContext

将SendableContext对象转换为UIAbilityContext。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sendableContext | [SendableContext](js-apis-inner-application-sendablecontext.md) | 是 | SendableContext对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| common.UIAbilityContext | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

主线程传递Context：

```
1. import { AbilityConstant, UIAbility, Want, common, sendableContextManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { worker } from '@kit.ArkTS';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. export default class EntryAbility extends UIAbility {
17. worker: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

19. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

22. // convert and post
23. try {
24. let sendableContext: sendableContextManager.SendableContext =
25. sendableContextManager.convertFromContext(this.context);
26. let object: SendableObject = new SendableObject(sendableContext, 'EntryAbilityContext');
27. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability post message');
28. this.worker.postMessageWithSharedSendable(object);
29. } catch (error) {
30. hilog.error(
31. 0x0000, 'testTag', `convertFromContext failed, error code: ${error.code}, error msg: ${error.message}`);
32. }
33. }
34. }
```

Worker线程接收Context：

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { common, sendableContextManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Sendable
6. export class SendableObject {
7. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
8. this.sendableContext = sendableContext;
9. this.contextName = contextName;
10. }

12. sendableContext: sendableContextManager.SendableContext;
13. contextName: string;
14. }

16. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

18. workerPort.onmessage = (e: MessageEvents) => {
19. let object: SendableObject = e.data;
20. let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
21. if (object.contextName == 'EntryAbilityContext') {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'convert to UIAbility context.');
23. try {
24. let context: common.UIAbilityContext = sendableContextManager.convertToUIAbilityContext(sendableContext);
25. // 获取context后获取沙箱路径
26. hilog.info(0x0000, 'testTag', 'worker context.databaseDir: %{public}s', context.databaseDir);
27. } catch (error) {
28. hilog.error(0x0000,
29. 'testTag', `convertToUIAbilityContext failed, error code: ${error.code}, error msg: ${error.message}`);
30. }
31. }
32. }

34. workerPort.onmessageerror = (e: MessageEvents) => {
35. hilog.info(0x0000, 'testTag', '%{public}s', 'onmessageerror');
36. }

38. workerPort.onerror = (e: ErrorEvent) => {
39. hilog.info(0x0000, 'testTag', '%{public}s', 'onerror');
40. }
```

## sendableContextManager.setEventHubMultithreadingEnabled20+

PhonePC/2in1TabletTVWearable

setEventHubMultithreadingEnabled(context: common.Context, enabled: boolean): void

设置[Context](js-apis-inner-application-context.md)中的[EventHub](js-apis-inner-application-eventhub.md)是否启用跨线程通信能力。

说明

* 当多个Context进行通信时，需要调用该接口设置每个Context都支持EventHub跨线程数据传递功能。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context对象。其中，Eventhub支持传递的序列化数据类型参见[序列化支持的类型](js-apis-taskpool.md#序列化支持类型)，数据大小不超过16MB。 |
| enabled | boolean | 是 | 表示是否启用Context的EventHub跨线程通信能力。  - true：表示启用跨线程通信能力，数据将通过引用的方式传递。  - false：表示禁用跨线程通信能力，数据将通过序列化的方式传递，即发送端线程与接收端线程的数据相互独立。 |

**示例：**

主线程启用[Context](js-apis-inner-application-context.md)中[EventHub](js-apis-inner-application-eventhub.md)的跨线程通信能力，并将Context转换为[SendableContext](js-apis-inner-application-sendablecontext.md)后发送到[Worker](js-apis-worker.md)线程。

```
1. import { common, sendableContextManager } from '@kit.AbilityKit';
2. import { worker } from '@kit.ArkTS';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @Sendable
8. export class SendableObject {
9. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
10. this.sendableContext = sendableContext;
11. this.contextName = contextName;
12. }

14. sendableContext: sendableContextManager.SendableContext;
15. contextName: string;
16. }

18. @Entry
19. @Component
20. struct Index {
21. @State context: common.Context | undefined = this.getUIContext().getHostContext();
22. worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

24. aboutToAppear(): void {
25. let context: common.Context = this.context as common.Context;
26. context.eventHub.on('event1', this.eventFunc);
27. context.eventHub.emit('event1', 'xingming', 22);
28. }

30. eventFunc(name: string, age: number) {
31. hilog.info(DOMAIN, 'testTag', 'name %{public}s age %{public}d', name, age);
32. }

34. build() {
35. Column() {
36. Row() {
37. Button('thread 1')
38. .size({ width: 100, height: 100 })
39. .onClick(() => {
40. if (this.context == undefined) {
41. return;
42. }
43. sendableContextManager.setEventHubMultithreadingEnabled(this.context, true);
44. let sendableContext: sendableContextManager.SendableContext =
45. sendableContextManager.convertFromContext(this.context);
46. let object: SendableObject = new SendableObject(sendableContext, 'BaseContext');
47. this.worker1.postMessageWithSharedSendable(object);
48. })
49. }
50. }
51. }
52. }
```

[Worker](js-apis-worker.md)线程接收到[SendableContext](js-apis-inner-application-sendablecontext.md)后，将其转换为[Context](js-apis-inner-application-context.md)。然后，在Worker线程内，启用Context中[EventHub](js-apis-inner-application-eventhub.md)的跨线程通信能力，并通过该功能向主线程发送消息。

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { common, sendableContextManager } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @Sendable
8. export class SendableObject {
9. constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
10. this.sendableContext = sendableContext;
11. this.contextName = contextName;
12. }

14. sendableContext: sendableContextManager.SendableContext;
15. contextName: string;
16. }

18. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

20. workerPort.onmessage = (e: MessageEvents) => {
21. let object: SendableObject = e.data;
22. let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
23. if (object.contextName == 'BaseContext') {
24. let context: common.Context = sendableContextManager.convertToContext(sendableContext);
25. sendableContextManager.setEventHubMultithreadingEnabled(context, true);
26. context.eventHub.emit('event1', 'xingming', 40);
27. }
28. };

30. workerPort.onmessageerror = (e: MessageEvents) => {
31. hilog.error(DOMAIN, 'testTag', '%{public}s', 'onmessageerror');
32. };

34. workerPort.onerror = (e: ErrorEvent) => {
35. hilog.error(DOMAIN, 'testTag', '%{public}s', 'onerror');
36. };
```
