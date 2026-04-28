---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry
title: @ohos.app.appstartup.StartupConfigEntry (启动框架配置)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.appstartup.StartupConfigEntry (启动框架配置)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:23+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:689cb69d3cd01da4bd2580336a770185eaf275c6a3aad8d401c5cc6de15387be
---

本模块提供[应用启动框架](../harmonyos-guides/app-startup.md)配置的能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { StartupConfigEntry } from '@kit.AbilityKit';
```

## StartupConfigEntry

PhonePC/2in1TabletTVWearable

### onConfig

PhonePC/2in1TabletTVWearable

onConfig?(): StartupConfig

在回调[AbilityStage.onCreate](js-apis-app-ability-abilitystage.md#oncreate)前，若该AbilityStage对应的HAP中启动框架配置文件中[定义了启动框架配置](../harmonyos-guides/app-startup.md#定义启动参数配置)，则会触发该回调。

开发者可以在该回调中设置启动框架配置信息，详细使用方法可参考[设置启动参数](../harmonyos-guides/app-startup.md#设置启动参数)章节。

**系统能力**：SystemCapability.Ability.AppStartup

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [StartupConfig](js-apis-app-appstartup-startupconfig.md#startupconfig) | 启动框架配置信息。 |

**示例：**

```
1. import { StartupConfig, StartupConfigEntry, StartupListener } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export default class MyStartupConfigEntry extends StartupConfigEntry {
6. onConfig() {
7. hilog.info(0x0000, 'testTag', `onConfig`);
8. let onCompletedCallback = (error: BusinessError<void>) => {
9. hilog.info(0x0000, 'testTag', `onCompletedCallback`);
10. if (error) {
11. hilog.error(0x0000, 'testTag', 'onCompletedCallback: %{public}d, message: %{public}s', error.code,
12. error.message);
13. } else {
14. hilog.info(0x0000, 'testTag', `onCompletedCallback: success.`);
15. }
16. }
17. let startupListener: StartupListener = {
18. 'onCompleted': onCompletedCallback
19. }
20. let config: StartupConfig = {
21. 'timeoutMs': 10000,
22. 'startupListener': startupListener
23. }
24. return config;
25. }
26. }
```

### onRequestCustomMatchRule20+

PhonePC/2in1TabletTVWearable

onRequestCustomMatchRule(want: Want): string

在回调[AbilityStage.onCreate](js-apis-app-ability-abilitystage.md#oncreate)前，若该AbilityStage对应的HAP中启动框架配置文件中[定义了启动框架配置](../harmonyos-guides/app-startup.md#定义启动参数配置)，则会在[StartupConfigEntry.onConfig](js-apis-app-appstartup-startupconfigentry.md#onconfig)后触发该回调。

开发者可以在该回调中，可以根据调用方传入启动UIAbility的Want中的不同参数来返回不同的自定义匹配规则。启动框架会将其与启动任务配置的matchRules中customization字段进行匹配。若匹配成功，任务将在自动模式执行。详细匹配规则请参考[添加任务匹配规则](../harmonyos-guides/app-startup.md#添加任务匹配规则)章节。

该接口通常用于无法直接通过uri、action或意图名称规则来匹配启动任务的场景，可以使用本接口对匹配规则进一步细化。

**系统能力**：SystemCapability.Ability.AppStartup

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility的Want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回自定义匹配规则值，用于匹配启动任务是否自动执行。 |

**示例：**

```
1. import { StartupConfigEntry, Want } from '@kit.AbilityKit';

3. export default class MyStartupConfigEntry extends StartupConfigEntry {
4. // ...

6. onRequestCustomMatchRule(want: Want): string {
7. if (want?.parameters?.customParam == 'param1') {
8. return 'customRule1';
9. }
10. return '';
11. }
12. }
```
