---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-errorobserver
title: ErrorObserver
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ErrorObserver
category: harmonyos-references
scraped_at: 2026-04-28T07:58:39+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:b8cf6ed0344601f3047dddcb4faa12a9d8a8cce666e5cacf85384caa21230f46
---

定义异常监听，可以作为[errorManager.on('error')](js-apis-app-ability-errormanager.md#errormanageronerror)的入参监听当前应用发生的异常。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { errorManager } from '@kit.AbilityKit';
```

## ErrorObserver.onUnhandledException

PhonePC/2in1TabletTVWearable

onUnhandledException(errMsg: string): void

应用产生未捕获的异常时的回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errMsg | string | 是 | 有关异常的消息和错误堆栈跟踪。 |

**示例：**

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.error('onUnhandledException, errorMsg: ', errorMsg);
7. }
8. };

10. try {
11. errorManager.on('error', observer);
12. } catch (error) {
13. console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
14. }
```

## ErrorObserver.onException10+

PhonePC/2in1TabletTVWearable

onException?(errObject: Error): void

应用产生异常，上报js层时的回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errObject | Error | 是 | 有关异常事件名字、消息和错误堆栈信息的对象。 |

**示例：**

```
1. import { errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.error('onUnhandledException, errorMsg: ', errorMsg);
7. },
8. onException(errorObj) {
9. console.error('onException, name: ', errorObj.name);
10. console.error('onException, message: ', errorObj.message);
11. if (typeof (errorObj.stack) === 'string') {
12. console.error('onException, stack: ', errorObj.stack);
13. }
14. }
15. };

17. try {
18. errorManager.on('error', observer);
19. } catch (error) {
20. console.error(`registerErrorObserver failed, error.code: ${(error as BusinessError).code}, error.message: ${(error as BusinessError).message}`);
21. }
```
