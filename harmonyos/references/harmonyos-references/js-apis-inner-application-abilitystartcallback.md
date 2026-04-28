---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystartcallback
title: AbilityStartCallback
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityStartCallback
category: harmonyos-references
scraped_at: 2026-04-28T07:58:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cad0f6d1a909fd40fd5c5fa177406dea29d2c399a7646e67ede7d563ce052654
---

定义拉起UIExtensionAbility执行结果的回调。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

从API version 11开始，本模块接口支持在元服务中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## AbilityStartCallback

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| completionHandler21+ | [CompletionHandlerForAbilityStartCallback](p-ability-completionhandlerforabilitystartcallback.md) | 否 | 是 | 用于返回拉起指定类型的Ability组件的回调结果。  **元服务API**：从API version 21开始，该接口支持在元服务中使用。 |

### onError

PhonePC/2in1TabletTVWearable

onError(code: number, name: string, message: string): void

拉起UIExtensionAbility执行失败的回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 拉起UIExtensionAbility执行失败时返回的结果码。 |
| name | string | 是 | 拉起UIExtensionAbility执行失败时返回的名称。 |
| message | string | 是 | 拉起UIExtensionAbility执行失败时返回的错误信息。 |

**示例：**

```
1. import { UIAbility, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let wantParam: Record<string, Object> = {
7. 'time': '2023-10-23 20:45',
8. };
9. let abilityStartCallback: common.AbilityStartCallback = {
10. onError: (code: number, name: string, message: string) => {
11. console.info(`code: ${code}, name: ${name}, message: ${message}`);
12. },
13. onResult: (abilityResult: common.AbilityResult) => {
14. console.info(`resultCode: ${abilityResult.resultCode}, bundleName: ${abilityResult.want?.bundleName}`);
15. }
16. };

18. this.context.startAbilityByType('photoEditor', wantParam, abilityStartCallback, (err: BusinessError) => {
19. if (err) {
20. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
21. } else {
22. console.info(`success`);
23. }
24. });
25. }
26. }
```

### onResult12+

PhonePC/2in1TabletTVWearable

onResult?(parameter: AbilityResult): void

拉起UIExtensionAbility终止时的回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 当调用[terminateSelfWithResult](js-apis-inner-application-uiextensioncontext.md#terminateselfwithresult12)方法终止UIExtensionAbility时返回的结果。 |

**示例：**

```
1. import { UIAbility, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let wantParam: Record<string, Object> = {
7. 'time': '2023-10-23 20:45',
8. };
9. let abilityStartCallback: common.AbilityStartCallback = {
10. onError: (code: number, name: string, message: string) => {
11. console.info(`code:` + code + `name:` + name + `message:` + message);
12. },
13. onResult: (abilityResult: common.AbilityResult) => {
14. console.info(`resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
15. }
16. };

18. this.context.startAbilityByType('photoEditor', wantParam, abilityStartCallback, (err: BusinessError) => {
19. if (err) {
20. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
21. } else {
22. console.info(`success`);
23. }
24. });
25. }
26. }
```
