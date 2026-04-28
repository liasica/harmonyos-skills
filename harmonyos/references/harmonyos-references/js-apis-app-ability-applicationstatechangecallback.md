---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback
title: @ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:60946323b07ff27eab0fd0b1390d84bbf959de7e908f53fc88cf24157c3bc586
---

本模块用于监听当前应用进程的状态变化。为了便于表述，下文中将“应用进程”简称为“进程”。

开发者可调用[ApplicationContext.on('applicationStateChange')](js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)方法传入自定义ApplicationStateChangeCallback来监听当前进程的前后台状态变化，从而根据进程前后台状态变化来执行某些操作。例如，统计进程前后台时长、或者当进程退到后台时清理内存缓存。

说明

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 约束限制

PhonePC/2in1TabletTVWearable

该模块仅支持监听当前进程的前后台状态变化。如果需要监听整个应用的前后台状态变化，可使用[ApplicationStateObserver.onForegroundApplicationChanged](js-apis-inner-application-applicationstateobserver.md#applicationstateobserveronforegroundapplicationchanged)。

说明

进程的前后台状态不同于应用的前后台状态，两者的差别如下：

* 进程的前后台状态：如果进程中存在任何前台状态的UIAbility/UIExtensionAbility或可见窗口，则认为进程状态为前台，反之为后台。
* 应用的前后台状态：如果应用下有任何一个进程状态为前台，则认为应用状态为前台，反之为后台。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ApplicationStateChangeCallback } from '@kit.AbilityKit';
```

## ApplicationStateChangeCallback.onApplicationForeground

PhonePC/2in1TabletTVWearable

onApplicationForeground(): void

当前进程从后台切换到前台时触发回调。当该回调触发时，并不表示进程已完全处于前台状态，而是即将进入前台状态，此时无法执行需要依赖前台状态的操作（例如启动其他UIAbility）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

参见[onApplicationBackground](js-apis-app-ability-applicationstatechangecallback.md#applicationstatechangecallbackonapplicationbackground)。

## ApplicationStateChangeCallback.onApplicationBackground

PhonePC/2in1TabletTVWearable

onApplicationBackground(): void

当前进程从前台切换到后台时触发回调。当该回调触发时，表示进程已完全处于后台状态，可以执行适合在后台状态下完成的操作（例如清理内存缓存）。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**示例：**

```
1. import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let applicationStateChangeCallback: ApplicationStateChangeCallback = {
5. onApplicationForeground() {
6. console.info('applicationStateChangeCallback onApplicationForeground');
7. },
8. onApplicationBackground() {
9. console.info('applicationStateChangeCallback onApplicationBackground');
10. }
11. };

13. export default class MyAbility extends UIAbility {
14. onCreate() {
15. console.info('MyAbility onCreate');
16. // 1.获取applicationContext
17. let applicationContext = this.context.getApplicationContext();
18. try {
19. // 2.通过applicationContext注册当前进程状态监听
20. if (applicationContext != undefined) {
21. applicationContext.on('applicationStateChange', applicationStateChangeCallback);
22. }
23. } catch (paramError) {
24. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
25. }
26. console.info('Register applicationStateChangeCallback');
27. }
28. onDestroy() {
29. let applicationContext = this.context.getApplicationContext();
30. try {
31. // 1.通过applicationContext解除注册当前进程状态监听
32. if (applicationContext != undefined) {
33. applicationContext.off('applicationStateChange', applicationStateChangeCallback);
34. }
35. } catch (paramError) {
36. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
37. }
38. }
39. }
```
