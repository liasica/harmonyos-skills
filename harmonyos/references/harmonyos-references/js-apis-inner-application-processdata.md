---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processdata
title: ProcessData
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ProcessData
category: harmonyos-references
scraped_at: 2026-04-28T07:58:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fea5c5eae9e4d56c4321d11bb117b639c899eb9d4dad6b7ab3bdc3bd6d2e3bd0
---

进程数据的对象定义。使用接口[appManager.on('applicationState')](js-apis-app-ability-appmanager.md#appmanageronapplicationstate14)注册生命周期变化监听后，当应用或组件的生命周期变化时，系统通过[ApplicationStateObserver](js-apis-inner-application-applicationstateobserver.md)的[onProcessCreated](js-apis-inner-application-applicationstateobserver.md#applicationstateobserveronprocesscreated)等方法回调给开发者。

说明

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appManager } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 进程ID。 |
| bundleName | string | 否 | 否 | 应用包名。 |
| uid | number | 否 | 否 | 应用的uid。 |
| isContinuousTask | boolean | 否 | 否 | 是否为长时任务，true表示是，false表示不是。 |
| isKeepAlive | boolean | 否 | 否 | 是否为常驻进程，true表示是，false表示不是 |
| state | number | 否 | 否 | 应用的状态，取值及对应的状态为：  0 - 初始化状态，进程正在初始化，  1 - 就绪状态，进程已初始化完毕，  2 - 前台，  4 - 后台，  5 - 已终止。 |

**示例：**

```
1. import { appManager } from '@kit.AbilityKit';

3. let observerCode = appManager.on('applicationState', {
4. onForegroundApplicationChanged(appStateData: appManager.AppStateData) {
5. console.info(`onForegroundApplicationChanged, appStateData: ${JSON.stringify(appStateData)}.`);
6. },
7. onAbilityStateChanged(abilityStateData: appManager.AbilityStateData) {
8. console.info(`onAbilityStateChanged, abilityStateData: ${JSON.stringify(abilityStateData)}.`);
9. },
10. onProcessCreated(processData: appManager.ProcessData) {
11. console.info(`onProcessCreated, processData: ${JSON.stringify(processData)}.`);
12. },
13. onProcessDied(processData: appManager.ProcessData) {
14. console.info(`onProcessDied, processData: ${JSON.stringify(processData)}.`);
15. },
16. onProcessStateChanged(processData: appManager.ProcessData) {
17. console.info(`onProcessStateChanged, processData.pid : ${JSON.stringify(processData.pid)}.`);
18. console.info(`onProcessStateChanged, processData.bundleName : ${JSON.stringify(processData.bundleName)}.`);
19. console.info(`onProcessStateChanged, processData.uid : ${JSON.stringify(processData.uid)}.`);
20. console.info(`onProcessStateChanged, processData.isContinuousTask : ${JSON.stringify(processData.isContinuousTask)}.`);
21. console.info(`onProcessStateChanged, processData.isKeepAlive : ${JSON.stringify(processData.isKeepAlive)}.`);
22. },
23. onAppStarted(appStateData: appManager.AppStateData) {
24. console.info(`onAppStarted, appStateData: ${JSON.stringify(appStateData)}.`);
25. },
26. onAppStopped(appStateData: appManager.AppStateData) {
27. console.info(`onAppStopped, appStateData: ${JSON.stringify(appStateData)}.`);
28. }
29. });
```
