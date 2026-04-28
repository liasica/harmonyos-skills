---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback
title: @ohos.app.ability.EnvironmentCallback (系统环境变化监听器)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.EnvironmentCallback (系统环境变化监听器)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:19+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:48a80ac1baa75c9ef15432cf3d5d96e7d5395478e782070fea5b290ea4f87e79
---

EnvironmentCallback模块提供对系统环境变化监听回调的能力。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { EnvironmentCallback } from '@kit.AbilityKit';
```

## EnvironmentCallback

PhonePC/2in1TabletTVWearable

### onConfigurationUpdated

PhonePC/2in1TabletTVWearable

onConfigurationUpdated(config: Configuration): void

[注册系统环境变化的监听](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)后，在系统环境变化时触发回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [Configuration](js-apis-app-ability-configuration.md) | 是 | 变化后的Configuration对象。 |

**示例：**

参见[EnvironmentCallback使用](js-apis-app-ability-environmentcallback.md#environmentcallback使用)。

### onMemoryLevel

PhonePC/2in1TabletTVWearable

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

[注册系统环境变化的监听](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)后，在系统内存变化时触发回调。

说明

onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务，因此不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel) | 是 | 整机可用内存级别，对应的触发场景详见[AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel)。 |

**示例：**

参见[EnvironmentCallback使用](js-apis-app-ability-environmentcallback.md#environmentcallback使用)。

## EnvironmentCallback使用

PhonePC/2in1TabletTVWearable

**示例：**

```
1. import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let callbackId: number;

6. export default class MyAbility extends UIAbility {
7. onCreate() {
8. console.info('MyAbility onCreate');
9. let environmentCallback: EnvironmentCallback  =  {
10. onConfigurationUpdated(config){
11. console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
12. },

14. onMemoryLevel(level){
15. console.info(`onMemoryLevel level: ${JSON.stringify(level)}`);
16. }
17. };
18. // 1.获取applicationContext
19. let applicationContext = this.context.getApplicationContext();
20. try {
21. // 2.通过applicationContext注册监听应用内生命周期
22. callbackId = applicationContext.on('environment', environmentCallback);
23. } catch (paramError) {
24. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
25. }
26. console.info(`registerEnvironmentCallback number: ${JSON.stringify(callbackId)}`);
27. }

29. onDestroy() {
30. let applicationContext = this.context.getApplicationContext();
31. try {
32. applicationContext.off('environment', callbackId, (error, data) => {
33. if (error && error.code !== 0) {
34. console.error(`unregisterEnvironmentCallback fail, error: ${JSON.stringify(error)}`);
35. } else {
36. console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
37. }
38. });
39. } catch (paramError) {
40. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
41. }
42. }
43. }
```
