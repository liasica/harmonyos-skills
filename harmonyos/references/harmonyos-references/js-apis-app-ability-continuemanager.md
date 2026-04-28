---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-continuemanager
title: @ohos.app.ability.continueManager (跨端迁移)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.continueManager (跨端迁移)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:31+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:59dc4ea5164a65ccb7971336355de280169c6e0f0ab5fc0df44817965bde69b6
---

continueManager提供了应用跨端迁移的管理能力，如获取应用跨端迁移过程中快速拉起目标应用的结果。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { continueManager } from '@kit.AbilityKit';
```

## continueManager.on

PhonePC/2in1TabletTVWearable

on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void

在应用快速拉起时，注册回调函数以获取快速拉起结果。使用callback异步回调。

说明

快速拉起功能支持在用户触发迁移、等待迁移数据返回的过程中，并行拉起应用，减小用户等待时间。在源端应用[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)的continueType标签的取值中添加“\_ContinueQuickStart”后缀，可以开启快速拉起功能。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值：prepareContinue。 |
| context | [Context](js-apis-inner-application-basecontext.md) | 是 | Ability的Context。 |
| callback | AsyncCallback<[ContinueResultInfo](js-apis-app-ability-continuemanager.md#continueresultinfo)> | 是 | 回调函数。当快速拉起结果获取成功，err为undefined，ContinueResultInfo为获取到的快速启动结果。否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16300501 | the system ability work abnormally. |

**示例**：

```
1. import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[MigrationAbility]';
5. const DOMAIN_NUMBER: number = 0xFF00;

7. export default class MigrationAbility extends UIAbility {
8. storage : LocalStorage = new LocalStorage();

10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
11. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onCreate');

13. // 1.已配置快速拉起功能，应用立即启动时触发应用生命周期回调
14. if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE_CONTINUATION) {
15. // 注册快速拉起结果通知的回调函数
16. try {
17. continueManager.on("prepareContinue", this.context, (err, continueResultInfo) => {
18. if (err.code != 0) {
19. console.error('register failed, cause: ' + JSON.stringify(err));
20. return;
21. }
22. console.info('register finished, ' + JSON.stringify(continueResultInfo));
23. });
24. } catch (e) {
25. console.error('register failed, cause: ' + JSON.stringify(e));
26. }
27. // 若应用迁移数据较大，可在此处添加加载页面(页面中显示loading等)
28. // 可处理应用自定义跳转、时序等问题
29. // ...
30. }
31. }
32. }
```

## continueManager.off

PhonePC/2in1TabletTVWearable

off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void

在应用快速拉起时，注销回调函数，不再获取快速拉起结果。使用callback异步回调。

说明

快速拉起功能支持在用户触发迁移、等待迁移数据返回的过程中，并行拉起应用，减小用户等待时间。在源端应用[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)的continueType标签的取值中添加“\_ContinueQuickStart”后缀，可以开启快速拉起功能。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定值：prepareContinue。 |
| context | [Context](js-apis-inner-application-basecontext.md) | 是 | Ability的Context。 |
| callback | AsyncCallback<[ContinueResultInfo](js-apis-app-ability-continuemanager.md#continueresultinfo)> | 否 | 回调函数。当回调函数注销成功，err为undefined，ContinueResultInfo为获回调函数注销结果。否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[DistributedSchedule错误码](errorcode-distributedschedule.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16300501 | the system ability work abnormally. |

**示例**：

```
1. import { AbilityConstant, UIAbility, Want, continueManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[MigrationAbility]';
5. const DOMAIN_NUMBER: number = 0xFF00;

7. export default class MigrationAbility extends UIAbility {
8. storage : LocalStorage = new LocalStorage();

10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
11. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onCreate');

13. // 1.已配置快速拉起功能，应用立即启动时触发应用生命周期回调
14. if (launchParam.launchReason === AbilityConstant.LaunchReason.PREPARE_CONTINUATION) {
15. // 注销快速拉起结果通知的回调函数
16. try {
17. continueManager.off("prepareContinue", this.context, (err, continueResultInfo) => {
18. if (err.code != 0) {
19. console.error('unregister failed, cause: ' + JSON.stringify(err));
20. return;
21. }
22. console.info('unregister finished, ' + JSON.stringify(continueResultInfo));
23. });
24. } catch (e) {
25. console.error('unregister failed, cause: ' + JSON.stringify(e));
26. }
27. // 若应用迁移数据较大，可在此处添加加载页面(页面中显示loading等)
28. // 可处理应用自定义跳转、时序等问题
29. // ...
30. }
31. }
32. }
```

## ContinueResultInfo

PhonePC/2in1TabletTVWearable

注册或注销回调函数返回的快速拉起的结果。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultState | [ContinueStateCode](js-apis-app-ability-continuemanager.md#continuestatecode) | 否 | 否 | 操作结果状态码。  **模型约束**：此接口仅可在Stage模型下使用。 |
| resultInfo | string | 否 | 是 | 操作结果的说明。  **模型约束**：此接口仅可在Stage模型下使用。 |

## ContinueStateCode

PhonePC/2in1TabletTVWearable

快速拉起的结果状态码的枚举值。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Mission

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 操作成功。  **模型约束**：此接口仅可在Stage模型下使用。 |
| SYSTEM\_ERROR | 1 | 操作失败。  **模型约束**：此接口仅可在Stage模型下使用。 |
