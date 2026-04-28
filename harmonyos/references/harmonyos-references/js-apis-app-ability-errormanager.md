---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager
title: @ohos.app.ability.errorManager (错误管理模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.errorManager (错误管理模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b75d60486927f17dd462ce035105d97ee15571f9b0d857612a6329d2d650e488
---

ErrorManager模块提供对错误观测器的注册和注销的能力，主要是观测应用发生js crash和appfreeze等错误。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { errorManager } from '@kit.AbilityKit';
```

## errorManager.on('error')

PhonePC/2in1TabletTVWearable

on(type: 'error', observer: ErrorObserver): number

注册错误观测器。注册后可以捕获到应用产生的js crash，属于应用崩溃的一种。观测器捕获到该异常时应用不退出，建议在回调函数执行完后，增加同步退出操作。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'error'，表示错误观测器。 |
| observer | [ErrorObserver](js-apis-inner-application-errorobserver.md) | 是 | 错误观测器。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 观测器的索引值，与观测器一一对应。可用于errorManager.off函数中的observerId参数。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.info('onUnhandledException, errorMsg: ', errorMsg);
7. },
8. onException(errorObj) {
9. console.info('onException, name: ', errorObj.name);
10. console.info('onException, message: ', errorObj.message);
11. if (typeof(errorObj.stack) === 'string') {
12. console.info('onException, stack: ', errorObj.stack);
13. }
14. }
15. };
16. let observerId = -1;

18. try {
19. observerId = errorManager.on('error', observer);
20. } catch (paramError) {
21. let code = (paramError as BusinessError).code;
22. let message = (paramError as BusinessError).message;
23. console.error(`error: ${code}, ${message}`);
24. }
```

## errorManager.on('globalErrorOccurred')18+

PhonePC/2in1TabletTVWearable

on(type: 'globalErrorOccurred', observer: GlobalObserver): void

在进程中的任意线程中注册 errormanager.on 接口，监听整个进程中任意线程的异常。观测器捕获到该异常时应用不退出，建议在回调函数执行完后，增加同步退出操作。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalErrorOccurred'，表示错误观测器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 是 | 自定义异常处理回调函数。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function errorFunc(observer: errorManager.GlobalError) {
5. console.info("result name :" + observer.name);
6. console.info("result message :" + observer.message);
7. console.info("result stack :" + observer.stack);
8. console.info("result instanceName :" + observer.instanceName);
9. console.info("result instanceType :" + observer.instanceType);
10. }

12. try {
13. errorManager.on('globalErrorOccurred', errorFunc);
14. } catch (paramError) {
15. let code = (paramError as BusinessError).code;
16. let message = (paramError as BusinessError).message;
17. console.error(`error: ${code}, ${message}`);
18. }
```

## errorManager.off('globalErrorOccurred')18+

PhonePC/2in1TabletTVWearable

off(type: 'globalErrorOccurred', observer?: GlobalObserver): void

注销错误观测器，注销之前注册在同一线程的callback全局监听。

如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalErrorOccurred'，表示错误观测器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 否 | 由on方法注册的callback。建议使用该参数，缺省时默认清除所有通过on注册的相同env的callback，否则删除指定callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |
| 16300004 | If the observer does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function errorFunc(observer: errorManager.GlobalError) {
5. console.info("result name :" + observer.name);
6. console.info("result message :" + observer.message);
7. console.info("result stack :" + observer.stack);
8. console.info("result instanceName :" + observer.instanceName);
9. console.info("result instanceType :" + observer.instanceType);
10. }

12. try {
13. errorManager.off('globalErrorOccurred', errorFunc)
14. } catch (paramError) {
15. let code = (paramError as BusinessError).code;
16. let message = (paramError as BusinessError).message;
17. console.error(`error: ${code}, ${message}`);
18. }
```

## errorManager.off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', observerId: number, callback: AsyncCallback<void>): void

注销错误观测器。使用callback异步返回。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'error'，表示错误观测器。 |
| observerId | number | 是 | 由on方法返回的观测器的index值。 |
| callback | AsyncCallback<void> | 是 | 表示指定的回调方法。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observerId = 100;

6. function unregisterErrorObserverCallback(err: BusinessError) {
7. if (err) {
8. console.error('------------ unregisterErrorObserverCallback ------------', err);
9. }
10. }

12. try {
13. errorManager.off('error', observerId, unregisterErrorObserverCallback);
14. } catch (paramError) {
15. let code = (paramError as BusinessError).code;
16. let message = (paramError as BusinessError).message;
17. console.error(`error: ${code}, ${message}`);
18. }
```

## errorManager.off('error')

PhonePC/2in1TabletTVWearable

off(type: 'error', observerId: number): Promise<void>

注销错误观测器。使用Promise异步返回。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'error'，表示错误观测器。 |
| observerId | number | 是 | 由on方法返回的观测器的index值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observerId = 100;

6. try {
7. errorManager.off('error', observerId)
8. .then((data) => {
9. console.info('----------- unregisterErrorObserver success ----------', data);
10. })
11. .catch((err: BusinessError) => {
12. console.error('----------- unregisterErrorObserver fail ----------', err);
13. });
14. } catch (paramError) {
15. let code = (paramError as BusinessError).code;
16. let message = (paramError as BusinessError).message;
17. console.error(`error: ${code}, ${message}`);
18. }
```

## errorManager.on('loopObserver')12+

PhonePC/2in1TabletTVWearable

on(type: 'loopObserver', timeout: number, observer: LoopObserver): void

注册主线程消息处理耗时监听器。注册后可以捕获到应用主线程处理消息的具体执行时间。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'loopObserver'，表示注册主线程消息处理耗时监听器。 |
| timeout | number | 是 | 表示事件执行阈值（单位：毫秒）。 阈值必须大于0。 |
| observer | [LoopObserver](js-apis-inner-application-loopobserver.md) | 是 | 注册主线程消息处理耗时监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. let observer: errorManager.LoopObserver = {
4. onLoopTimeOut(timeout: number) {
5. console.info('Duration timeout: ' + timeout);
6. }
7. };

9. errorManager.on("loopObserver", 1, observer);
```

## errorManager.on('globalUnhandledRejectionDetected')18+

PhonePC/2in1TabletTVWearable

on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void

在进程中任意线程注册被拒绝promise监听器，注册后可以捕获到当前进程中未被捕获到的promise rejection。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalUnhandledRejectionDetected'，表示注册被拒绝promise监听器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 是 | 注册被拒绝promise的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. function promiseFunc(observer: errorManager.GlobalError) {
4. console.info("result name :" + observer.name);
5. console.info("result message :" + observer.message);
6. console.info("result stack :" + observer.stack);
7. console.info("result instanceName :" + observer.instanceName);
8. console.info("result instanceType :" + observer.instanceType);
9. }

11. errorManager.on("globalUnhandledRejectionDetected", promiseFunc);
12. // 建议在抛出promise异常时，使用async抛出异常。
13. async function throwError() {
14. throw new Error("uncaught error");
15. }

17. let promise1 = new Promise<void>(() => {}).then(() => {
18. throwError();
19. });
```

## errorManager.on('unhandledRejection')12+

PhonePC/2in1TabletTVWearable

on(type: 'unhandledRejection', observer: UnhandledRejectionObserver): void

注册被拒绝promise监听器。注册后可以捕获到当前线程中未被捕获到的promise rejection。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'unhandledRejection'，表示注册被拒绝promise监听器。 |
| observer | [UnhandledRejectionObserver](js-apis-app-ability-errormanager.md#unhandledrejectionobserver12) | 是 | 注册被拒绝promise监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
4. if (promise === promise1) {
5. console.info("promise1 is rejected");
6. }
7. console.info("reason.name: ", reason.name);
8. console.info("reason.message: ", reason.message);
9. if (reason.stack) {
10. console.info("reason.stack: ", reason.stack);
11. }
12. };

14. errorManager.on("unhandledRejection", observer);

16. let promise1 = new Promise<void>(() => {}).then(() => {
17. throw new Error("uncaught error");
18. });
```

## errorManager.on('freeze')18+

PhonePC/2in1TabletTVWearable

on(type: 'freeze', observer: FreezeObserver): void

注册应用主线程freeze监听。多次注册情况下，取最后一次注册的结果。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

注意

如果该回调函数执行时间超过1s，可能导致[AppRecovery](js-apis-app-ability-apprecovery.md)功能不可用。通过解析hilog日志中的begin与Freeze callback execution completed两者的时间差可以计算回调函数执行时长，如果超过1秒，可以尝试采用异步处理、减少阻塞操作、优化数据结构等方法优化回调逻辑，降低执行时长。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'freeze'，表示应用主线程freeze观测器。 |
| observer | [FreezeObserver](js-apis-app-ability-errormanager.md#freezeobserver18) | 是 | 由on接口注册的freeze监听的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. function freezeCallback() {
4. console.info("freezecallback");
5. }
6. errorManager.on("freeze", freezeCallback);
```

## errorManager.off('loopObserver')12+

PhonePC/2in1TabletTVWearable

off(type: 'loopObserver', observer?: LoopObserver): void

注销主线程消息处理监听器。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'loopObserver'，表示应用主线程观测器。 |
| observer | [LoopObserver](js-apis-inner-application-loopobserver.md) | 否 | 应用主线程观测器标志。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. errorManager.off("loopObserver");
```

## errorManager.off('globalUnhandledRejectionDetected')18+

PhonePC/2in1TabletTVWearable

off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void

注销被拒绝promise监听器，注销后无法监听进程中的promise异常。

如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalUnhandledRejectionDetected'，表示注册被拒绝promise监听器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 否 | 由on接口注册的被拒绝promise的callback。建议使用该参数，缺省时默认清除所有通过on注册的相同env的callback，否则删除指定callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |
| 16300004 | If the observer does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. function promiseFunc(observer: errorManager.GlobalError) {
4. console.info("result name :" + observer.name);
5. console.info("result message :" + observer.message);
6. console.info("result stack :" + observer.stack);
7. console.info("result instanceName :" + observer.instanceName);
8. console.info("result instanceType :" + observer.instanceType);
9. }

11. errorManager.on("globalUnhandledRejectionDetected", promiseFunc);

13. async function throwError() {
14. throw new Error("uncaught error");
15. }

17. let promise1 = new Promise<void>(() => {}).then(() => {
18. throwError();
19. });

21. errorManager.off("globalUnhandledRejectionDetected", promiseFunc);
```

## errorManager.off('unhandledRejection')12+

PhonePC/2in1TabletTVWearable

off(type: 'unhandledRejection', observer?: UnhandledRejectionObserver): void

注销被拒绝promise监听器。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'unhandledRejection'，表示注册被拒绝promise监听器。 |
| observer | [UnhandledRejectionObserver](js-apis-app-ability-errormanager.md#unhandledrejectionobserver12) | 否 | 注册了被拒绝promise监听器。建议使用该参数，缺省时默认清除所有通过on注册的相同env的observer，否则删除指定observer。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |
| 16300004 | If the observer does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
4. if (promise === promise1) {
5. console.info("promise1 is rejected");
6. }
7. console.info("reason.name: ", reason.name);
8. console.info("reason.message: ", reason.message);
9. if (reason.stack) {
10. console.info("reason.stack: ", reason.stack);
11. }
12. };

14. errorManager.on("unhandledRejection", observer);

16. let promise1 = new Promise<void>(() => {}).then(() => {
17. throw new Error("uncaught error")
18. })

20. errorManager.off("unhandledRejection");
```

或者

```
1. import { errorManager } from '@kit.AbilityKit';

3. let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
4. if (promise === promise1) {
5. console.info("promise1 is rejected");
6. }
7. console.info("reason.name: ", reason.name);
8. console.info("reason.message: ", reason.message);
9. if (reason.stack) {
10. console.info("reason.stack: ", reason.stack);
11. }
12. };

14. errorManager.on("unhandledRejection", observer);

16. let promise1 = new Promise<void>(() => {}).then(() => {
17. throw new Error("uncaught error")
18. })

20. errorManager.off("unhandledRejection", observer);
```

## errorManager.off('freeze')18+

PhonePC/2in1TabletTVWearable

off(type: 'freeze', observer?: FreezeObserver): void

取消之前注册的应用主线程freeze监听。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

如果传入的回调与通过on方法注册回调不一致，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'freeze'，表示应用主线程freeze观测器。 |
| observer | [FreezeObserver](js-apis-app-ability-errormanager.md#freezeobserver18) | 否 | 由on接口注册的freeze监听的callback。建议使用该参数，如果参数不填会直接清空callback，否则删除指定的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300004 | If the observer does not exist. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';

3. function freezeCallback() {
4. console.info("freezecallback");
5. }
6. errorManager.on("freeze", freezeCallback);
7. errorManager.off("freeze", freezeCallback);
```

## errorManager.setDefaultErrorHandler21+

PhonePC/2in1TabletTVWearable

setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler

发生JS\_CRASH异常时，支持链式回调，返回上一次注册的处理器，仅限主线程调用。

如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。

若接口参数为空，后续注册的处理器将无法与前序已注册的处理器建立关联，从而中断链式调用。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultHandler | [ErrorHandler](js-apis-app-ability-errormanager.md#errorhandler21) | 否 | 新注册的错误处理器，缺省时默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ErrorHandler](js-apis-app-ability-errormanager.md#errorhandler21) | 返回上一次注册的错误处理器。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000205 | The API is not called in the main thread. |

**示例**：

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { process } from '@kit.ArkTS';

4. let oldHandler: errorManager.ErrorHandler;
5. const errorHandler: errorManager.ErrorHandler = (reason: Error) => {
6. // 自定义的errorHandler实现逻辑
7. console.info('[Handler]  Uncaught exception handler invoked.');
8. if (oldHandler) {
9. oldHandler(reason);
10. } else {
11. // 建议增加判空操作，如果为空采用同步退出方式
12. const processManager = new process.ProcessManager();
13. processManager.exit(0);
14. }
15. };
16. oldHandler = errorManager.setDefaultErrorHandler(errorHandler);
```

## ErrorObserver

PhonePC/2in1TabletTVWearable

type ErrorObserver = \_ErrorObserver.default

ErrorObserver模块。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ErrorObserver.default](js-apis-inner-application-errorobserver.md) | ErrorObserver模块。 |

## LoopObserver12+

PhonePC/2in1TabletTVWearable

type LoopObserver = \_LoopObserver

LoopObserver模块。定义异常监听，可作为 errormanager.on 函数的参数，监听并处理当前应用主线程超时的事件。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_LoopObserver](js-apis-inner-application-loopobserver.md) | LoopObserver模块。 |

## UnhandledRejectionObserver12+

PhonePC/2in1TabletTVWearable

type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void

定义异常监听，用于捕获Promise异步操作失败的原因。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | Error | any | 是 | 通常是Error类型，表示被拒绝的理由。 |
| promise | Promise<any> | 是 | 被拒绝的promise。 |

## FreezeObserver18+

PhonePC/2in1TabletTVWearable

type FreezeObserver = () => void

定义应用主线程freeze回调，用于应用自定义添加freeze信息。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

## GlobalObserver18+

PhonePC/2in1TabletTVWearable

type GlobalObserver = (reason: GlobalError) => void

定义异常监听，可以作为[errorManager.on('globalErrorOccurred')](js-apis-app-ability-errormanager.md#errormanageronglobalerroroccurred18)和[errorManager.on('globalUnhandledRejectionDetected')](js-apis-app-ability-errormanager.md#errormanageronglobalunhandledrejectiondetected18)的入参监听当前应用主线程事件处理事件。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [GlobalError](js-apis-app-ability-errormanager.md#globalerror18) | 是 | 有关异常事件名字、消息、错误堆栈信息、异常线程名称和类型的对象。 |

## GlobalError18+

PhonePC/2in1TabletTVWearable

有关异常事件名字、消息、错误堆栈信息、异常线程名称和类型的对象。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| instanceName | string | 否 | 否 | 表示虚拟机实例名称。  **说明**：  TaskPool线程中异常的instanceName标识规则：  - globalErrorOccurred：标识为“TaskPool Thread + 方法名”；  - globalUnhandledRejectionDetected：标识为“TaskPool Thread + 任务名”；  - 若仅标识为“TaskPool Thread”，则表明异常源于异步回调内部。 |
| instanceType | [InstanceType](js-apis-app-ability-errormanager.md#instancetype18) | 否 | 否 | 表示虚拟机的实例类型。 |

## InstanceType18+

PhonePC/2in1TabletTVWearable

虚拟机的实例类型。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAIN | 0 | 表示主虚拟机实例。 |
| WORKER | 1 | 表示工作虚拟机实例。 |
| TASKPOOL | 2 | 表示任务池虚拟机实例。 |
| CUSTOM | 3 | 表示用户通过[napi\_create\_ark\_runtime](napi.md#napi_create_ark_runtime)从本机代码创建的虚拟机实例。 |

## ErrorHandler21+

PhonePC/2in1TabletTVWearable

type ErrorHandler = (errObject: Error) => void

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errObject | Error | 是 | 有关异常事件名字、消息、错误堆栈信息的对象。 |
