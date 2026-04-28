---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/apis-app-ability-completionhandlerforatomicservice
title: @ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:39330587510dd1a97192bfae971ac37b5caba37b2996529946961e12b1b2aabc
---

CompletionHandlerForAtomicService作为[AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md)的可选参数，用于接收打开元服务请求的结果。

说明

* 本模块首批接口从API version 20 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { CompletionHandlerForAtomicService } from '@kit.AbilityKit';
```

## FailureCode

PhonePC/2in1TabletTVWearable

打开元服务失败的特定错误码。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAILURE\_CODE\_SYSTEM\_MALFUNCTION | 0 | 表示由于系统错误（如跳转弹框崩溃）而无法打开元服务。 |
| FAILURE\_CODE\_USER\_CANCEL | 1 | 用户取消。 |
| FAILURE\_CODE\_USER\_REFUSE | 2 | 用户拒绝。 |

## CompletionHandlerForAtomicService

PhonePC/2in1TabletTVWearable

CompletionHandlerForAtomicService提供了[onAtomicServiceRequestSuccess](apis-app-ability-completionhandlerforatomicservice.md#onatomicservicerequestsuccess)和[onAtomicServiceRequestFailure](apis-app-ability-completionhandlerforatomicservice.md#onatomicservicerequestfailure)两个回调函数，分别在打开元服务成功和失败时回调。

### onAtomicServiceRequestSuccess

PhonePC/2in1TabletTVWearable

onAtomicServiceRequestSuccess(appId: string): void

打开元服务成功时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 被拉起元服务的appId。 |

**示例：**

参见[CompletionHandlerForAtomicService示例](apis-app-ability-completionhandlerforatomicservice.md#completionhandlerforatomicservice示例)。

### onAtomicServiceRequestFailure

PhonePC/2in1TabletTVWearable

onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string): void

打开元服务失败时的回调函数。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 被拉起元服务的appId。 |
| failureCode | [FailureCode](apis-app-ability-completionhandlerforatomicservice.md#failurecode) | 是 | 失败原因的错误码。 |
| failureMessage | string | 是 | 失败原因的描述。 |

**示例：**

参见[CompletionHandlerForAtomicService示例](apis-app-ability-completionhandlerforatomicservice.md#completionhandlerforatomicservice示例)。

### CompletionHandlerForAtomicService示例

```
1. import { AbilityConstant, AtomicServiceOptions, common, UIAbility, Want, CompletionHandlerForAtomicService, FailureCode } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. let completionHandler: CompletionHandlerForAtomicService = {
8. onAtomicServiceRequestSuccess(appId: string) {
9. hilog.info(0x0000, 'testTag', `appId:${appId}`);
10. },
11. onAtomicServiceRequestFailure(appId: string, failureCode: FailureCode, failureMessage: string) {
12. hilog.info(0x0000, 'testTag', `appId:${appId}, failureCode:${failureCode}, failureMessage:${failureMessage}`);
13. }
14. };
15. let options: AtomicServiceOptions = {
16. completionHandlerForAtomicService: completionHandler
17. };
18. let appId: string = '5765880207853275489'; // 根据实际appId修改此值
19. this.context.openAtomicService(appId, options).then((result: common.AbilityResult) => {
20. hilog.info(0x0000, 'testTag', `openAtomicService succeed:${JSON.stringify(result)}`);
21. }).catch((err: BusinessError) => {
22. hilog.error(0x0000, 'testTag', `openAtomicService failed:${JSON.stringify(err)}`);
23. });
24. }
25. }
```
