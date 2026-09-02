---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager
title: "@ohos.app.ability.errorManager (错误管理模块)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.errorManager (错误管理模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:37e9d15e9fafb7b2589d0df8548cf47329fc8d80410a1133b566c57a6893998b
---

ErrorManager模块提供对应用运行时各类异常的全局观测能力，包括注册和注销错误观测器，主要用于监测应用崩溃（JS\_CRASH）、应用冻屏（APP\_FREEZE）、未捕获的Promise异常、资源超基线等错误场景。通过设置监听器，开发者可以实时捕获异常信息、追踪问题根源、记录关键指标，从而提高应用的稳定性监控能力，加快故障排查和定位效率，提升应用质量和用户体验。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { errorManager } from '@kit.AbilityKit';
```

## errorManager.on('error')

on(type: 'error', observer: ErrorObserver): number

注册错误观测器。注册后可以捕获到应用产生的JS\_CRASH，属于应用崩溃的一种。观测器捕获到该异常时应用不退出，建议在回调函数执行完后，增加同步退出操作。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.off('error')](js-apis-app-ability-errormanager.md#errormanagerofferror)方法配合使用，使用完成后可调用off方法注销监听器。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.ErrorObserver = {
  onUnhandledException(errorMsg) {
    console.info('onUnhandledException, errorMsg: ', errorMsg);
  },
  onException(errorObj) {
    console.info('onException, name: ', errorObj.name);
    console.info('onException, message: ', errorObj.message);
    if (typeof(errorObj.stack) === 'string') {
      console.info('onException, stack: ', errorObj.stack);
    }
  }
};
let observerId = -1;

try {
  observerId = errorManager.on('error', observer);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.on('globalErrorOccurred')18+

on(type: 'globalErrorOccurred', observer: GlobalObserver): void

在进程中的任意线程中注册 errorManager.on 接口，监听整个进程中任意线程的异常。观测器捕获到该异常时应用不退出，建议在回调函数执行完后，增加同步退出操作。

开发者需要自行维护自定义异常处理回调函数的生命周期，保证异常回调时，自定义异常处理回调函数没有被释放。

配对调用：与[errorManager.off('globalErrorOccurred')](js-apis-app-ability-errormanager.md#errormanageroffglobalerroroccurred18)方法配合使用，使用完成后可调用off方法注销监听器。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalErrorOccurred'，表示错误观测器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 是 | 自定义异常处理回调函数，用于接收全局异常事件。回调函数入参：(reason: GlobalError) => void，其中reason为包含异常名称、消息、堆栈、线程名称和类型的对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const errorFunc = (observer: errorManager.GlobalError) => {
  console.info('result name :' + observer.name);
  console.info('result message :' + observer.message);
  console.info('result stack :' + observer.stack);
  console.info('result instanceName :' + observer.instanceName);
  console.info('result instanceType :' + observer.instanceType);
};

try {
  errorManager.on('globalErrorOccurred', errorFunc);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.off('globalErrorOccurred')18+

off(type: 'globalErrorOccurred', observer?: GlobalObserver): void

注销错误观测器，注销当前注册在同一线程的callback全局监听。

如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

建议开发者在进程回收时，调用注销错误观测器，如果其他线程发送异常回调时，可能因找不到自定义异常处理回调函数而发生崩溃。

配对调用：与[errorManager.on('globalErrorOccurred')](js-apis-app-ability-errormanager.md#errormanageronglobalerroroccurred18)方法配合使用。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalErrorOccurred'，表示错误观测器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 否 | 由on方法注册的自定义异常处理回调函数。建议使用该参数。若不传该参数，则清除所有通过on方法注册的observer；若传该参数，则仅删除指定的observer。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |
| 16300004 | If the observer does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const errorFunc = (observer: errorManager.GlobalError) => {
  console.info('result name :' + observer.name);
  console.info('result message :' + observer.message);
  console.info('result stack :' + observer.stack);
  console.info('result instanceName :' + observer.instanceName);
  console.info('result instanceType :' + observer.instanceType);
}

try {
  errorManager.off('globalErrorOccurred', errorFunc)
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.off('error')

off(type: 'error', observerId: number, callback: AsyncCallback<void>): void

注销错误观测器。使用callback异步返回。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('error')](js-apis-app-ability-errormanager.md#errormanageronerror)方法配合使用。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observerId = 100;

const unregisterErrorObserverCallback = (err: BusinessError) => {
  if (err) {
    console.error('------------ unregisterErrorObserverCallback ------------', err);
  }
};

try {
  errorManager.off('error', observerId, unregisterErrorObserverCallback);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.off('error')

off(type: 'error', observerId: number): Promise<void>

注销错误观测器。使用Promise异步返回。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('error')](js-apis-app-ability-errormanager.md#errormanageronerror)方法配合使用。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000003 | The specified ID does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observerId = 100;

try {
  errorManager.off('error', observerId)
    .then((data) => {
      console.info('----------- unregisterErrorObserver success ----------', data);
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to unregister error observer. Code: ${err.code}, message: ${err.message}`);
    });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.on('loopObserver')12+

on(type: 'loopObserver', timeout: number, observer: LoopObserver): void

注册主线程消息处理耗时监听器。注册后可以捕获到应用主线程处理消息的具体执行时间。

该接口通过监测每个消息从开始执行到完成的时间间隔，当执行时间超过设定的timeout阈值时触发回调。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.off('loopObserver')](js-apis-app-ability-errormanager.md#errormanageroffloopobserver12)方法配合使用，使用完成后可调用off方法注销监听器释放资源。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'loopObserver'，表示注册主线程消息处理耗时监听器。 |
| timeout | number | 是 | 表示事件执行阈值（单位：毫秒）。 阈值必须大于0。 |
| observer | [LoopObserver](js-apis-inner-application-loopobserver.md) | 是 | 注册主线程消息处理耗时监听器。定义了onLoopTimeOut方法，当主线程消息处理时间超过阈值时被调用。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: errorManager.LoopObserver = {
  onLoopTimeOut(timeout: number) {
    console.info('Duration timeout: ' + timeout);
  }
};

try {
  errorManager.on('loopObserver', 1, observer);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.on('globalUnhandledRejectionDetected')18+

on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void

在进程中任意线程注册被拒绝Promise监听器，注册后可以捕获到当前进程中未被捕获到的Promise rejection。

开发者需要自行维护自定义异常处理回调函数的生命周期，保证异常回调时，自定义异常处理回调函数没有被释放。

配对调用：与[errorManager.off('globalUnhandledRejectionDetected')](js-apis-app-ability-errormanager.md#errormanageroffglobalunhandledrejectiondetected18)方法配合使用，使用完成后可调用off方法注销监听器。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalUnhandledRejectionDetected'，表示注册被拒绝Promise监听器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 是 | 注册被拒绝Promise的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';

const promiseFunc = (observer: errorManager.GlobalError) => {
  console.info('result name :' + observer.name);
  console.info('result message :' + observer.message);
  console.info('result stack :' + observer.stack);
  console.info('result instanceName :' + observer.instanceName);
  console.info('result instanceType :' + observer.instanceType);
};

errorManager.on('globalUnhandledRejectionDetected', promiseFunc);
// 建议在抛出Promise异常时，使用async抛出异常。
const throwError = async () => {
  throw new Error('uncaught error');
};

let promise1 = new Promise<void>(() => {}).then(() => {
  throwError();
});
```

## errorManager.on('unhandledRejection')12+

on(type: 'unhandledRejection', observer: UnhandledRejectionObserver): void

注册被拒绝Promise监听器。注册后可以捕获到当前线程中未被捕获到的Promise rejection。

接口入参不符合要求时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.off('unhandledRejection')](js-apis-app-ability-errormanager.md#errormanageroffunhandledrejection12)方法配合使用，使用完成后可调用off方法注销监听器释放资源。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'unhandledRejection'，表示注册被拒绝Promise监听器。 |
| observer | [UnhandledRejectionObserver](js-apis-app-ability-errormanager.md#unhandledrejectionobserver12) | 是 | 注册被拒绝Promise监听器。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
  if (promise === promise1) {
    console.info('promise1 is rejected');
  }
  console.info('reason.name: ', reason.name);
  console.info('reason.message: ', reason.message);
  if (reason.stack) {
    console.info('reason.stack: ', reason.stack);
  }
};

errorManager.on('unhandledRejection', observer);

let promise1 = new Promise<void>(() => {}).then(() => {
  throw new Error('uncaught error');
});
```

## errorManager.on('freeze')18+

on(type: 'freeze', observer: FreezeObserver): void

注册应用主线程freeze监听。多次注册情况下，取最后一次注册的结果。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.off('freeze')](js-apis-app-ability-errormanager.md#errormanagerofffreeze18)方法配合使用，使用完成后可调用off方法注销监听器。

**注意** 

如果该回调函数执行时间超过1s，可能导致[AppRecovery](js-apis-app-ability-apprecovery.md)功能不可用。通过解析hilog日志中的begin与Freeze callback execution completed两者的时间差可以计算回调函数执行时长，如果超过1秒，可以尝试采用异步处理、减少阻塞操作、优化数据结构等方法优化回调逻辑，降低执行时长。

该接口请勿与[errorManager.setDefaultFreezeObserver](js-apis-app-ability-errormanager.md#errormanagersetdefaultfreezeobserver)接口混用，混用可能会导致注册的回调函数执行失败。

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

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const freezeCallback = () => {
  console.info('freezecallback');
};
try {
  errorManager.on('freeze', freezeCallback);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.off('loopObserver')12+

off(type: 'loopObserver', observer?: LoopObserver): void

注销主线程消息处理监听器。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('loopObserver')](js-apis-app-ability-errormanager.md#errormanageronloopobserver12)方法配合使用，使用完成后可调用off方法注销监听器释放资源。

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  errorManager.off('loopObserver');
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.off('globalUnhandledRejectionDetected')18+

off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void

注销被拒绝Promise监听器，注销后无法监听进程中的Promise异常。

建议开发者在进程回收时，调用注销错误观测器，如果其他线程发送异常回调时，可能因找不到自定义异常处理回调函数而发生崩溃。

如果传入的回调不在通过on方法注册的回调队列中，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('globalUnhandledRejectionDetected')](js-apis-app-ability-errormanager.md#errormanageronglobalunhandledrejectiondetected18)方法配合使用。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'globalUnhandledRejectionDetected'，表示注销被拒绝Promise监听器。 |
| observer | [GlobalObserver](js-apis-app-ability-errormanager.md#globalobserver18) | 否 | 由on接口注册的被拒绝Promise的callback。建议使用该参数，缺省时默认清除所有通过on注册的相同虚拟机实例环境（env）的callback，否则删除指定callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16200001 | If the caller is invalid. |
| 16300004 | If the observer does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';

const promiseFunc = (observer: errorManager.GlobalError) => {
  console.info('result name :' + observer.name);
  console.info('result message :' + observer.message);
  console.info('result stack :' + observer.stack);
  console.info('result instanceName :' + observer.instanceName);
  console.info('result instanceType :' + observer.instanceType);
};

errorManager.on('globalUnhandledRejectionDetected', promiseFunc);

const throwError = async () => {
  throw new Error('uncaught error');
};

let promise1 = new Promise<void>(() => {}).then(() => {
  throwError();
});

errorManager.off('globalUnhandledRejectionDetected', promiseFunc);
```

## errorManager.off('unhandledRejection')12+

off(type: 'unhandledRejection', observer?: UnhandledRejectionObserver): void

注销被拒绝Promise监听器。

接口入参不符合要求时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('unhandledRejection')](js-apis-app-ability-errormanager.md#errormanageronunhandledrejection12)方法配合使用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'unhandledRejection'，表示注销被拒绝Promise监听器。 |
| observer | [UnhandledRejectionObserver](js-apis-app-ability-errormanager.md#unhandledrejectionobserver12) | 否 | 需要注销的被拒绝Promise监听器。建议使用该参数，缺省时默认清除所有通过on注册的相同虚拟机实例环境（env）的callback，否则删除指定observer。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300004 | If the observer does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
  if (promise === promise1) {
    console.info('promise1 is rejected');
  }
  console.info('reason.name: ', reason.name);
  console.info('reason.message: ', reason.message);
  if (reason.stack) {
    console.info('reason.stack: ', reason.stack);
  }
};

errorManager.on('unhandledRejection', observer);

let promise1 = new Promise<void>(() => {}).then(() => {
  throw new Error('uncaught error')
})

errorManager.off('unhandledRejection');
```

或者

```ts
import { errorManager } from '@kit.AbilityKit';

let observer: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
  if (promise === promise1) {
    console.info('promise1 is rejected');
  }
  console.info('reason.name: ', reason.name);
  console.info('reason.message: ', reason.message);
  if (reason.stack) {
    console.info('reason.stack: ', reason.stack);
  }
};

errorManager.on('unhandledRejection', observer);

let promise1 = new Promise<void>(() => {}).then(() => {
  throw new Error('uncaught error')
})

errorManager.off('unhandledRejection', observer);
```

## errorManager.off('freeze')18+

off(type: 'freeze', observer?: FreezeObserver): void

注销已注册的应用主线程freeze监听。

仅在主线程中使用。使用线程出错时，将抛出错误码，因此建议使用try-catch逻辑进行处理。

如果传入的回调与通过on方法注册回调不一致，将抛出16300004错误码，因此建议使用try-catch逻辑进行处理。

配对调用：与[errorManager.on('freeze')](js-apis-app-ability-errormanager.md#errormanageronfreeze18)方法配合使用。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写'freeze'，表示应用主线程freeze观测器。 |
| observer | [FreezeObserver](js-apis-app-ability-errormanager.md#freezeobserver18) | 否 | 由on接口注册的freeze监听的callback。建议使用该参数。若不传该参数，则清除所有通过on方法注册的callback；若传该参数，则仅删除指定的callback。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16300004 | If the observer does not exist. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const freezeCallback = () => {
  console.info('freezecallback');
};
try {
  errorManager.on('freeze', freezeCallback);
  errorManager.off('freeze', freezeCallback);
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message}`);
}
```

## errorManager.setDefaultErrorHandler21+

setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler

发生JS\_CRASH异常时，支持链式回调，返回上一次注册的处理器，仅限主线程调用。

如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。

若接口参数为空，后续注册的处理器将无法与前序已注册的处理器建立关联，从而中断链式调用。

链式调用机制允许依次执行多个错误处理器：注册新处理器时，会返回上一次注册的处理器；在处理器中可以调用前序处理器，形成处理器链。这样可以实现多层错误处理逻辑的叠加，确保每个处理器都能按预期执行。

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
| 16000205 | The API is not called on the main thread. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { process } from '@kit.ArkTS';

let oldHandler: errorManager.ErrorHandler;
const errorHandler: errorManager.ErrorHandler = (reason: Error) => {
  // 自定义的errorHandler实现逻辑
  console.info('[Handler] Uncaught exception handler invoked.');
  if (oldHandler) {
      oldHandler(reason);
  } else {
      // 建议增加判空操作，如果为空采用同步退出方式
      const processManager = new process.ProcessManager();
      processManager.exit(0);
  }
};
oldHandler = errorManager.setDefaultErrorHandler(errorHandler);
```

## errorManager.setDefaultResourceUsageObserver24+

setDefaultResourceUsageObserver(defaultObserver?: ResourceUsageObserver): ResourceUsageObserver

设置资源占用观察者，应用资源超基线时，支持链式回调。

该接口通过系统资源监控服务实时采集应用的内存、文件描述符、线程数等资源使用情况，与预设基线进行比较，当资源使用量超过基线时触发观察者回调。返回上一次注册的资源占用观察者，仅限主线程调用。

如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。

若接口参数为空，后续注册的观察者将无法与前序已注册的观察者建立关联，从而中断链式调用。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultObserver | [ResourceUsageObserver](js-apis-app-ability-errormanager.md#resourceusageobserver24) | 否 | 新注册的资源观察者，缺省时默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ResourceUsageObserver](js-apis-app-ability-errormanager.md#resourceusageobserver24) | 返回上一次注册的资源观察者。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000205 | The API is not called on the main thread. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { process } from '@kit.ArkTS';

let oldObserver: errorManager.ResourceUsageObserver;
const resourceUsageObserver: errorManager.ResourceUsageObserver = (resourceType, resourceSize, detailInfo) => {
  // 自定义的resourceUsageObserver实现逻辑
  console.info('[Observer] Resource usage observer.');
  if (oldObserver) {
    oldObserver(resourceType, resourceSize, detailInfo);
  } else {
    // 建议增加判空操作，如果为空采用同步退出方式
    const processManager = new process.ProcessManager();
    processManager.exit(0);
  }
};
oldObserver = errorManager.setDefaultResourceUsageObserver(resourceUsageObserver);
```

## errorManager.setDefaultFreezeObserver

setDefaultFreezeObserver(defaultObserver?: FreezeObserver) : FreezeObserver

发生APP\_FREEZE时，支持链式回调，返回上一次注册的处理器，仅限主线程调用。

如果传入非法参数或在子线程调用，将抛出错误码并返回undefined，因此建议使用try-catch逻辑进行处理。

**说明** 

该接口以下场景会返回空指针，使用返回值前必须进行判空处理，避免空指针解引用导致应用崩溃：

1. 开发者注册的处理器为空时。
2. 首次注册时，上一次注册的处理器为空。

该接口请勿与[on('freeze')](js-apis-app-ability-errormanager.md#errormanageronfreeze18)或[off('freeze')](js-apis-app-ability-errormanager.md#errormanagerofffreeze18)接口混用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultObserver | [FreezeObserver](js-apis-app-ability-errormanager.md#freezeobserver18) | 否 | 新注册的freeze观察者，默认值为空。  当参数为空时，后续注册的处理器将无法与前序已注册的处理器建立关联，从而中断链式调用。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [FreezeObserver](js-apis-app-ability-errormanager.md#freezeobserver18) | 返回上一次注册的处理器。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000205 | The API is not called on the main thread. |

**示例**：

```ts
import { errorManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 用于保存上一次注册的处理器。如果是第一次注册，无前置处理器。
let oldHandler: errorManager.FreezeObserver = () => {};
const freezeHandler: errorManager.FreezeObserver = () => {
  // 自定义的FreezeHandler实现逻辑
  console.info('[freezeHandler] freeze handler invoked.');
  if (oldHandler) {
    oldHandler();
  } else {
    console.info('[freezeHandler] freeze handler end.');
  }
};

export function setFreezeHandler() {
  try {
    oldHandler = errorManager.setDefaultFreezeObserver(freezeHandler);
  } catch (paramError) {
    let code = (paramError as BusinessError).code;
    let message = (paramError as BusinessError).message;
    console.error(`Failed to set freeze handler. Code: ${code}, message: ${message}`);
  }
  console.info('Registered freeze Handler.');
}
```

## ErrorObserver

type ErrorObserver = \_ErrorObserver.default

ErrorObserver模块。该模块定义了错误观测器的接口，包含onUnhandledException和onException两个回调方法。通过实现该接口，开发者可以自定义对未处理异常和已捕获异常的处理逻辑。系统在捕获到异常时会自动调用相应回调，并将异常信息传递给观测器。详细实现机制请参见[ErrorObserver](js-apis-inner-application-errorobserver.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_ErrorObserver.default](js-apis-inner-application-errorobserver.md) | ErrorObserver模块。 |

## LoopObserver12+

type LoopObserver = \_LoopObserver

LoopObserver模块。定义异常监听，可作为 errorManager.on 函数的参数，监听并处理当前应用主线程超时的事件。

该接口通过在ArkUI事件循环的消息处理前后记录时间戳，计算消息执行时长，当执行时长超过设定的timeout阈值时触发onLoopTimeOut回调。详细监测机制请参见[LoopObserver](js-apis-inner-application-loopobserver.md)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_LoopObserver](js-apis-inner-application-loopobserver.md) | LoopObserver模块。 |

## UnhandledRejectionObserver12+

type UnhandledRejectionObserver = (reason: Error | any, promise: Promise<any>) => void

定义异常监听，用于捕获Promise异步操作失败的原因。当Promise被reject且没有相应的catch处理时触发回调。系统会将拒绝原因（reason）和对应的Promise对象传递给观测器，便于开发者进行异常处理和追踪。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | Error | any | 是 | 通常是Error类型，表示被拒绝的理由。 |
| promise | Promise<any> | 是 | 被拒绝的Promise。 |

## FreezeObserver18+

type FreezeObserver = () => void

定义应用主线程freeze回调，用于应用自定义添加freeze信息。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

## GlobalObserver18+

type GlobalObserver = (reason: GlobalError) => void

定义异常监听，可以作为[errorManager.on('globalErrorOccurred')](js-apis-app-ability-errormanager.md#errormanageronglobalerroroccurred18)和[errorManager.on('globalUnhandledRejectionDetected')](js-apis-app-ability-errormanager.md#errormanageronglobalunhandledrejectiondetected18)的入参，用于监听全局异常事件和未捕获的Promise rejection。通过回调机制获取异常详情，帮助开发者及时发现和定位故障问题。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [GlobalError](js-apis-app-ability-errormanager.md#globalerror18) | 是 | 有关异常事件名字、消息、错误堆栈信息、异常线程名称和类型的对象。 |

## GlobalError18+

有关异常事件名字、消息、错误堆栈信息、异常线程名称和类型的对象。继承自Error。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| instanceName | string | 否 | 否 | 表示虚拟机实例名称。  **说明**：  TaskPool线程中异常的instanceName标识规则：  - globalErrorOccurred：标识为“TaskPool Thread + 方法名”；  - globalUnhandledRejectionDetected：标识为“TaskPool Thread + 任务名”；  - 若仅标识为“TaskPool Thread”，则表明异常源于异步回调内部。 |
| instanceType | [InstanceType](js-apis-app-ability-errormanager.md#instancetype18) | 否 | 否 | 表示虚拟机的实例类型。 |

## InstanceType18+

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

type ErrorHandler = (errObject: Error) => void

定义错误处理器函数类型，用于处理JS异常，作为[errorManager.setDefaultErrorHandler](js-apis-app-ability-errormanager.md#errormanagersetdefaulterrorhandler21)的参数类型，在异常发生时被调用，接收异常对象并执行自定义错误处理逻辑。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errObject | Error | 是 | 有关异常事件名字、消息、错误堆栈信息的对象。 |

## ResourceUsageObserver24+

type ResourceUsageObserver = (resourceType: ResourceType, resourceSize: number, detailInfo?: Record<string, number>) => void

定义应用资源使用情况的观察者回调函数，作为[errorManager.setDefaultResourceUsageObserver](js-apis-app-ability-errormanager.md#errormanagersetdefaultresourceusageobserver24)的入参，用于监听各类资源占用变化，并支持应用执行自定义资源处理逻辑。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceType | [ResourceType](js-apis-app-ability-errormanager.md#resourcetype24) | 是 | 表示应用资源超基线的类型。 |
| resourceSize | number | 是 | 表示应用资源超基线的资源使用量。单位：KB。取值范围：大于0的正整数。 |
| detailInfo | Record<string, number> | 否 | 表示应用资源超基线资源使用量的细分项字典。  **说明**：仅在resourceType为PSS\_MEMORY时存在，为其他类型或缺省时为空；  key为小写内存类型，value为对应细分项资源大小；  细分项的key包含arkts、native、ion、gpu、ashmem和other。 |

## ResourceType24+

应用资源超基线的类型。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 24开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PSS\_MEMORY | 1 | 表示应用当前超基线的资源是PSS的内存。 |
| ION\_MEMORY | 2 | 表示应用当前超基线的资源是ION的内存。 |
| ASHMEM\_MEMORY | 3 | 表示应用当前超基线的资源是ASHMEM的内存。 |
| GPU\_MEMORY | 4 | 表示应用当前超基线的资源是GPU的内存。 |
| FD | 5 | 表示应用当前超基线的资源是FD的数量。 |
| THREAD | 6 | 表示应用当前超基线的资源是THREAD的数量。 |
