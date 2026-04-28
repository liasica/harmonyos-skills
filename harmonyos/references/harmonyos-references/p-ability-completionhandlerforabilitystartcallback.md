---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/p-ability-completionhandlerforabilitystartcallback
title: @ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:707354f9c23e63ada755fb746c2f48cbb9a43341ef3f3e7cbcc1f5326c48a75a
---

CompletionHandlerForAbilityStartCallback作为[AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md)的可选参数，用于返回垂域面板拉起指定类型的Ability组件的回调结果。

说明

* 本模块首批接口从API version 21 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { CompletionHandlerForAbilityStartCallback } from '@kit.AbilityKit';
```

## CompletionHandlerForAbilityStartCallback

PhonePC/2in1TabletTVWearable

CompletionHandlerForAbilityStartCallback提供了onRequestSuccess和onRequestFailure两个回调函数属性，分别在拉起指定类型的Ability组件成功和失败时回调。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| onRequestSuccess | [OnRequestSuccessFn](p-ability-completionhandlerforabilitystartcallback.md#onrequestsuccessfn) | 否 | 是 | 拉起指定类型的Ability组件成功时的回调函数。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |
| onRequestFailure | [OnRequestFailureFn](p-ability-completionhandlerforabilitystartcallback.md#onrequestfailurefn) | 否 | 是 | 拉起指定类型的Ability组件失败时的回调函数。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |

## OnRequestSuccessFn

PhonePC/2in1TabletTVWearable

type OnRequestSuccessFn = (name: string) => void

拉起指定类型的Ability组件成功时的回调函数类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 被拉起Ability组件或系统操作的名称。  Ability组件名称采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。 |

**示例：**

参见[OnRequestFailureFn](p-ability-completionhandlerforabilitystartcallback.md#onrequestfailurefn)。

## OnRequestFailureFn

PhonePC/2in1TabletTVWearable

type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void

拉起指定类型的Ability组件失败时的回调函数类型。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 被拉起Ability组件或系统操作的名称。  Ability组件名称采用'[bundleName]#[moduleName]#[abilityName]'格式拼接。如果用户自动取消拉起，name为空。 |
| failureCode | [AbilityStartFailureCode](p-ability-completionhandlerforabilitystartcallback.md#abilitystartfailurecode) | 是 | 失败原因的错误码。 |
| failureMessage | string | 是 | 失败原因的描述。 |

**示例：**

```
1. import { AbilityStartFailureCode, common, CompletionHandlerForAbilityStartCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';
8. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. completionHandler: CompletionHandlerForAbilityStartCallback = {
11. onRequestSuccess: (name: string) => {
12. console.info(`testTag onRequestSuccess name` + name);
13. },
14. onRequestFailure: (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => {
15. console.info(`testTag onRequestFailure name: ` + name + `, failureCode:` + failureCode + `, failureMessage:` +
16. failureMessage);
17. }
18. };
19. abilityStartCallback: common.AbilityStartCallback = {
20. onError: (code: number, name: string, message: string) => {
21. console.info(`testTag code:` + code + `name:` + name + `message:` + message);
22. },
23. onResult: (abilityResult: common.AbilityResult) => {
24. console.info(`testTag resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
25. },
26. completionHandler: this.completionHandler,
27. };

29. build() {
30. Column({ space: 10 }) {
31. Button('test')
32. .type(ButtonType.Capsule)
33. .offset({ x: 0, y: 60 })
34. .width('80%')
35. .type(ButtonType.Capsule)
36. .margin({ top: 10 })
37. .onClick(() => {
38. let wantParam: Record<string, Object> = {
39. 'time': '2023-10-23 20:45'
40. };
41. this.context.startAbilityByType("share", wantParam, this.abilityStartCallback).then(() => {
42. console.info(`startAbilityByType success`);
43. }).catch((err: BusinessError) => {
44. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
45. });
46. })
47. }
48. }
49. }
```

## AbilityStartFailureCode

PhonePC/2in1TabletTVWearable

拉起指定类型的Ability组件失败的特定错误码。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAILURE\_CODE\_SYSTEM\_MALFUNCTION | 0 | 表示由于系统错误（如跳转弹框崩溃）而无法拉起Ability组件。 |
| FAILURE\_CODE\_USER\_CANCEL | 1 | 用户取消。 |
