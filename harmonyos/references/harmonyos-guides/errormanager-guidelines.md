---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/errormanager-guidelines
title: 错误管理开发指导
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 错误管理及应用恢复 > 错误管理开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:780e6cd19ced8b8f4da24347a99ee0b5cc9fe2b9532b2ab9f953476710abd224
---

## 场景介绍

当应用的代码存在规范问题或错误时，会在运行中产生异常和错误，如应用未捕获异常等。在错误产生后，应用会异常退出。错误日志通常会保存在用户本地存储设备中，不方便开发者定位问题。所以，应用开发者可以使用错误管理的接口，在应用退出前，及时将相关错误及日志上报到开发者的服务平台来定位问题。

使用errorManager接口监听异常和错误后，应用不会退出，建议在回调函数执行完后，增加同步退出操作，如果只是为了获取错误日志，建议使用[HiAppEvent订阅事件](hiappevent-intro.md)。

## 接口说明

应用错误管理接口由[@ohos.app.ability.errorManager (错误管理模块)](../harmonyos-references/js-apis-app-ability-errormanager.md)提供，使用接口能力前需注册错误观测器，开发者可以通过import引入，详见[开发示例](errormanager-guidelines.md#开发示例)。

**错误管理接口功能介绍**：

| 接口名称 | 说明 |
| --- | --- |
| on(type: "error", observer: ErrorObserver): number | 注册错误监听接口，当系统监测到应用异常时会回调该监听。该接口为同步接口，返回值为注册的监听对象对应的序号。 |
| off(type: "error", observerId: number, callback: AsyncCallback<void>): void | 以callback的形式解除注册监听，传入的number为之前注册监听时返回的序号。 |
| off(type: "error", observerId: number): Promise<void> | 以Promise的形式解除注册监听，传入的number为之前注册监听时返回的序号。 |
| on(type: 'globalErrorOccurred', observer: GlobalObserver): void | 注册进程错误监听接口，当系统监测到应用异常时会回调该监听，该接口为同步接口，即一次注册，全局监听。（**推荐使用**）  说明：从API version 18开始，支持该接口。 |
| off(type: 'globalErrorOccurred', observer?: GlobalObserver): void | 以callback的形式解除注册监听。（**推荐使用**）  说明：从API version 18开始，支持该接口。 |
| on(type: 'globalUnhandledRejectionDetected', observer: GlobalObserver): void | 注册进程错误监听接口，当系统监测到应用promise异常时会回调该监听，该接口为同步接口，即一次注册，全局监听。（**推荐使用**）  说明：从API version 18开始，支持该接口。 |
| off(type: 'globalUnhandledRejectionDetected', observer?: GlobalObserver): void | 以callback的形式解除注册监听。（**推荐使用**）  说明：从API version 18开始，支持该接口。 |
| on(type: 'loopObserver', timeout: number, observer: LoopObserver): void | 注册主线程消息处理耗时监听器，当系统监测到应用主线程事件处理超时时会回调该监听。  只能在主线程调用，多次注册后，后一次的注册会覆盖前一次的。 |
| off(type: 'loopObserver', observer?: LoopObserver): void | 以LoopObserver的形式解除应用主线程消息处理耗时监听。 |
| on(type: 'freeze', observer: FreezeObserver): void | 注册应用主线程freeze监听。只能在主线程调用，重复注册后，后一次的注册会覆盖前一次的。 |
| off(type: 'freeze', observer?: FreezeObserver): void | 以FreezeObserver的形式解除应用主线程消息处理耗时监听。  说明：从API version 18开始，支持该接口。 |
| setDefaultErrorHandler(defaultHandler?: ErrorHandler): ErrorHandler | 仅允许在主线程调用，发生JS\_CRASH异常时，支持链式回调，返回值为上一次注册的处理器。  说明：从API version 21开始，支持该接口。 |

当采用callback作为异步回调时，可以在callback中进行下一步处理。

当采用Promise对象返回时，可以在Promise对象中类似地处理接口返回值，具体结果码说明见[解除注册结果码](errormanager-guidelines.md#解除注册结果码)。

**错误监听(ErrorObserver)接口功能介绍**：

| 接口名称 | 说明 |
| --- | --- |
| onUnhandledException(errMsg: string): void | 系统回调接口，应用注册后，当应用产生未捕获的异常时的回调。 |
| onException?(errObject: Error): void | 系统回调接口，应用注册后，当应用产生异常上报js层时的回调。 |

**应用主线程监听(LoopObserver)接口功能介绍**：

| 接口名称 | 说明 |
| --- | --- |
| onLoopTimeOut?(timeout: number): void | 系统回调接口，应用注册后，当应用主线程处理事件超时的回调。 |

### 解除注册结果码

| 结果码 | 原因 |
| --- | --- |
| 0 | 正常返回 |
| -1 | 传入的number参数不存在 |
| -2 | 参数错误 |

## 开发示例

注意

建议在异常回调函数处理的最后，增加同步退出操作，以避免多次异常回调。

### 单线程监听场景

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. let observer: errorManager.ErrorObserver = {
2. onUnhandledException(errorMsg) {
3. console.error('testErrorManage','onUnhandledException, errorMsg: ', errorMsg);
4. },
5. onException(errorObj) {
6. console.error('testErrorManage','onException, name: ', errorObj.name);
7. console.error('testErrorManage','onException, message: ', errorObj.message);
8. if (typeof(errorObj.stack) === 'string') {
9. console.error('testErrorManage','onException, stack: ', errorObj.stack);
10. }
11. }
12. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L25-L38)

新增触发按钮。

```
1. Button('单线程监听场景').onClick(()=>{
2. let observerId = -1;
3. try {
4. observerId = errorManager.on('error', observer);
5. } catch (paramError) {
6. let code = (paramError as BusinessError).code;
7. let message = (paramError as BusinessError).message;
8. console.error('testErrorManage',`error: ${code}, ${message}`);
9. }
10. // 构造场景故障
11. throw new Error('test errorObserver msg');
12. }).position({x:50, y:50});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L114-L127)

### 进程监听异常场景

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. function errorFunc(observer: errorManager.GlobalError) {
2. console.error('testErrorManage','result name :' + observer.name);
3. console.error('testErrorManage','result message :' + observer.message);
4. console.error('testErrorManage','result stack :' + observer.stack);
5. console.error('testErrorManage','result instanceName :' + observer.instanceName);
6. console.error('testErrorManage','result instanceType :' + observer.instanceType);
7. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L40-L48)

新增触发按钮。

```
1. Button('进程监听异常场景').onClick(()=>{
2. try {
3. errorManager.on('globalErrorOccurred', errorFunc);
4. } catch (paramError) {
5. let code = (paramError as BusinessError).code;
6. let message = (paramError as BusinessError).message;
7. console.error('testErrorManage',`error: ${code}, ${message}`);
8. }
9. // 构造场景故障
10. throw new Error('test errorFunc msg');
11. }).position({x:50, y:100});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L129-L141)

### 进程监听promise异常场景

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. function promiseFunc(observer: errorManager.GlobalError) {
2. console.error('testErrorManage','result name :' + observer.name);
3. console.error('testErrorManage','result message :' + observer.message);
4. console.error('testErrorManage','result stack :' + observer.stack);
5. console.error('testErrorManage','result instanceName :' + observer.instanceName);
6. console.error('testErrorManage','result instanceType :' + observer.instanceType);
7. };

9. async function promiseFuncOne() {
10. throw new Error('process promise exception');
11. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L58-L70)

新增触发按钮。

```
1. Button('进程监听promise异常场景').onClick(()=>{
2. try {
3. errorManager.on('globalUnhandledRejectionDetected', promiseFunc);
4. } catch (paramError) {
5. let code = (paramError as BusinessError).code;
6. let message = (paramError as BusinessError).message;
7. console.error('testErrorManage',`error: ${code}, ${message}`);
8. }
9. // 构造场景故障
10. new Promise<string>(() => {
11. promiseFuncOne();
12. }).then(() => {
13. throw new Error('test promiseFuncOne msg');
14. });
15. }).position({x:50, y:200});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L159-L175)

### 主线程监听freeze

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. function freezeCallback() {
2. console.error('testErrorManage','freezecallback');
3. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L93-L97)

新增触发按钮。

```
1. Button('主线程监听freeze').onClick(()=>{
2. try {
3. errorManager.on('freeze', freezeCallback);
4. } catch (paramError) {
5. let code = (paramError as BusinessError).code;
6. let message = (paramError as BusinessError).message;
7. console.error('testErrorManage',`error: ${code}, ${message}`);
8. }
9. // 构造场景故障
10. let date = Date.now();
11. while (Date.now() - date < 15000) {
12. };
13. }).position({x:50, y:300});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L195-L209)

### 主线程监听消息处理耗时

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. let loopObserver: errorManager.LoopObserver = {
2. onLoopTimeOut(timeout: number) {
3. console.error('testErrorManage','Duration timeout: ' + timeout);
4. }
5. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L50-L56)

新增触发按钮。

```
1. Button('主线程监听消息处理耗时').onClick(()=>{
2. try {
3. errorManager.on('loopObserver', 1, loopObserver);
4. } catch (paramError) {
5. let code = (paramError as BusinessError).code;
6. let message = (paramError as BusinessError).message;
7. console.error('testErrorManage',`error: ${code}, ${message}`);
8. }
9. // 构造场景故障
10. let date = Date.now();
11. while (Date.now() - date < 4000) {
12. };
13. }).position({x:50, y:150});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L143-L157)

### 进程promise监听注册被拒绝

引入头文件。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L16-L19)

新增监听回调函数。

```
1. let promise1 = new Promise<void>(() => {}).then(() => {
2. throw new Error('uncaught error');
3. });

5. let unhandledrejectionObserver: errorManager.UnhandledRejectionObserver = (reason: Error, promise: Promise<void>) => {
6. if (promise === promise1) {
7. console.error('testErrorManage','promise1 is rejected');
8. }
9. console.error('testErrorManage','reason.name: ', reason.name);
10. console.error('testErrorManage','reason.message: ', reason.message);
11. if (reason.stack) {
12. console.error('testErrorManage','reason.stack: ', reason.stack);
13. }
14. };

16. async function promiseFuncTwo() {
17. throw new Error('process promise unhandled rejection exception');
18. };
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L72-L91)

新增触发按钮。

```
1. Button('进程promise监听注册被拒绝').onClick(()=>{
2. try {
3. errorManager.on('unhandledRejection', unhandledrejectionObserver);
4. } catch (paramError) {
5. let code = (paramError as BusinessError).code;
6. let message = (paramError as BusinessError).message;
7. console.error('testErrorManage',`error: ${code}, ${message}`);
8. }
9. // 构造场景故障
10. new Promise<string>(() => {
11. promiseFuncTwo();
12. }).then(() => {
13. throw new Error('test promiseFuncTwo msg');
14. });
15. }).position({x:50, y:250});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L177-L193)

### 错误处理器责任链模式场景

定义第一个错误处理器及注册方法，无前置处理器时退出进程。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { process } from '@kit.ArkTS';

4. let firstHandler: errorManager.ErrorHandler;
5. const firstErrorHandler: errorManager.ErrorHandler = (reason: Error) => {
6. // 自定义的第一个errorHandler实现逻辑
7. console.info('[FirstHandler] First uncaught exception handler invoked.');
8. if (firstHandler) {
9. firstHandler(reason);
10. } else {
11. // 建议增加判空操作，如果为空采用同步退出方式
12. const processManager = new process.ProcessManager();
13. processManager.exit(0);
14. }
15. };

17. export function setFirstErrorHandler() {
18. firstHandler = errorManager.setDefaultErrorHandler(firstErrorHandler);
19. console.info('Registered First Error Handler');
20. }
```

[FirstErrorHandler.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/FirstErrorHandler.ets#L1-L22)

定义第二个错误处理器及注册方法，形成链式调用。

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { process } from '@kit.ArkTS';

4. let secondHandler: errorManager.ErrorHandler;
5. const secondErrorHandler: errorManager.ErrorHandler = (reason: Error) => {
6. // 自定义的第二个errorHandler实现逻辑
7. console.info('[SecondHandler] Second uncaught exception handler invoked.');
8. if (secondHandler) {
9. secondHandler(reason);
10. } else {
11. const processManager = new process.ProcessManager();
12. processManager.exit(0);
13. }
14. };

16. export function setSecondErrorHandler() {
17. secondHandler = errorManager.setDefaultErrorHandler(secondErrorHandler);
18. console.info('Registered Second Error Handler');
19. }
```

[SecondErrorHandler.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/SecondErrorHandler.ets#L1-L21)

引入头文件。

```
1. import { setFirstErrorHandler } from './FirstErrorHandler';
2. import { setSecondErrorHandler } from './SecondErrorHandler';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L20-L23)

新增错误处理器责任链模式构造函数。

```
1. function testErrorHandlers() {
2. setFirstErrorHandler();
3. setSecondErrorHandler();
4. throw new Error('Test uncaught exception!');
5. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L99-L105)

主组件通过按钮触发测试，注册两个处理器并抛错验证处理链。

```
1. Button('错误处理器责任链模式场景').onClick(()=>{
2. testErrorHandlers();
3. }).position({x:50, y:350});
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/ErrorManage/ErrorManage/entry/src/main/ets/pages/Index.ets#L211-L215)
