---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preload-application
title: 应用预加载
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 应用预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:91b462b4ccbb222794a26d64b1bdb27323a56e912e807846851e2525482e2786
---

## 概述

从API version 20开始，提供应用预加载机制。该机制会根据用户的使用习惯，在系统资源充足时提前加载应用至特定阶段。当用户启动应用时，由于此前已完成了应用的部分加载，所需的启动时间会缩短，有助于提升用户体验和应用竞争力。

该机制尤其适用于因加载大量资源而启动耗时较长的应用，例如大型游戏应用和大型办公应用。

## 约束限制

* 当前仅支持2in1设备。
* 仅支持entry模块的AbilityStage和UIAbility预加载。无论预加载到哪种阶段，entry模块必须配置入口UIAbility，详见[开发步骤](preload-application.md#开发步骤)中步骤2。
* 应用配置预加载后，实际是否进行预加载以及具体的预加载时机，均由系统根据用户习惯等信息来综合决定。开发者无法对此进行干预。

## 运行机制

当系统资源充足时，系统将应用加载到特定阶段，提升启动速度。当前支持预加载到三种阶段。开发者可以根据应用冷启动各阶段耗时情况，选择其中的一种。

说明

在应用预加载过程中不会显示任何界面，因此在预加载的任何阶段不应包含与界面显示、界面交互或依赖用户可见的相关操作，同时应确保用户正式启动应用后，所有功能正常运行且体验不受影响。

* processCreated：进程创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，但是不会触发任何生命周期回调。
* abilityStageCreated：[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，随后触发entry模块[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)的[onCreate](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)回调。
* windowStageCreated：[WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)创建完成阶段。开发者配置此阶段后，预加载机制会创建空进程并初始化Application，随后触发entry模块[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)的[onCreate](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)回调。接着会拉起entry模块的入口UIAbility，并触发其[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调和[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)回调。开发者可以在UIAbility的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调中，通过[launchParam.launchReason](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchreason)的枚举值获取启动原因。枚举值为PRELOAD表示当前UIAbility是由预加载机制启动的。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/JZeTxQoGQ7yxl0On9xzI3w/zh-cn_image_0000002552797852.png?HW-CC-KV=V1&HW-CC-Date=20260427T233744Z&HW-CC-Expire=86400&HW-CC-Sign=7259A3FC0A110BC3E416E1485D8579CB56B4A843F2D9060298730D04995BBE92)

## 开发步骤

1. 声明应用支持预加载到的阶段。

   以windowStageCreated阶段为例，在[app.json5配置文件](app-configuration-file.md)中配置[appPreloadPhase](app-configuration-file.md#配置文件标签)标签。

   ```
   1. {
   2. "app": {
   3. "bundleName": "com.demo.preloadtest",
   4. "vendor": "example",
   5. "versionCode": 1000000,
   6. "versionName": "1.0.0",
   7. "icon": "$media:layered_image",
   8. "label": "$string:app_name",
   9. "appPreloadPhase": "windowStageCreated"
   10. }
   11. }
   ```
2. 配置入口UIAbility（新建工程默认已自动配置）。

   1. 以EntryAbility为例，在entry模块的[module.json5配置文件](module-configuration-file.md)中，设置mainElement为EntryAbility，且EntryAbility的skills标签下面的entities中添加"entity.system.home"、actions中添加"ohos.want.action.home"。
   2. 当[app.json5配置文件](app-configuration-file.md)中的[appPreloadPhase](app-configuration-file.md#配置文件标签)配置为windowStageCreated时，需要在entry模块的[module.json5配置文件](module-configuration-file.md)中配置EntryAbility的launchType标签为[singleton](uiability-launch-type.md#singleton启动模式)或[specified](uiability-launch-type.md#specified启动模式)。

   ```
   1. {
   2. "module": {
   3. "name": "entry",
   4. "type": "entry",
   5. "mainElement": "EntryAbility",
   6. // ...
   7. "abilities": [
   8. {
   9. "name": "EntryAbility",
   10. "srcEntry": "./ets/entryability/EntryAbility.ets",
   11. "launchType": "singleton",
   12. "skills": [
   13. {
   14. "entities": [
   15. "entity.system.home"
   16. ],
   17. "actions": [
   18. "ohos.want.action.home"
   19. ]
   20. }
   21. ]
   22. // ...
   23. }
   24. ]
   25. }
   26. }
   ```
3. （可选）获取UIAbility启动原因。

   仅当appPreloadPhase配置为windowStageCreated时，开发者可在UIAbility的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调中通过[launchParam.launchReason](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchreason)的枚举值获取启动原因。枚举值为PRELOAD表示当前UIAbility是由预加载机制启动的。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

   3. export default class EntryAbility extends UIAbility {
   4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   5. console.info(`EntryAbility onCreate, LaunchReason:${launchParam.launchReason}`);
   6. // 判断是否是预加载启动
   7. let isPreloadStart = launchParam.launchReason === AbilityConstant.LaunchReason.PRELOAD;
   8. // ...
   9. }
   10. }
   ```
