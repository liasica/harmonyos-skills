---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitystage
title: AbilityStage组件管理器
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > AbilityStage组件管理器
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a640eb571a11971bc82cb26ab90cc764acd08189b8746e6b468e7de174c845ff
---

## 概述

[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)是一个[Module](application-package-overview.md#应用的多module设计机制)级别的组件管理器，应用的[HAP](hap-package.md)在首次加载时会创建一个AbilityStage实例，可以对该Module进行初始化等操作。AbilityStage与HAP一一对应，即每个HAP拥有一个AbilityStage实例。

AbilityStage拥有[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)、[onDestroy()](../harmonyos-references/js-apis-app-ability-abilitystage.md#ondestroy12)生命周期回调和[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)、[onConfigurationUpdate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)、[onMemoryLevel()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)、[onNewProcessRequest()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onnewprocessrequest11)、[onPrepareTermination()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onpreparetermination15)等事件回调。

* onCreate()生命周期回调：在开始加载对应Module的第一个应用组件（如[UIAbility组件](../harmonyos-references/js-apis-app-ability-uiability.md)或具体扩展能力的[ExtensionAbility组件](../harmonyos-references/js-apis-app-ability-extensionability.md)）实例之前会先创建AbilityStage，并在AbilityStage创建完成之后执行其onCreate()生命周期回调。AbilityStage模块提供在Module加载的时候，通知开发者，可以在此进行该Module的初始化（如资源预加载、线程创建等）。
* onAcceptWant()事件回调：UIAbility[指定实例模式（specified）](uiability-launch-type.md#specified启动模式)启动时触发的事件回调，具体使用请参见[UIAbility启动模式综述](uiability-launch-type.md)。
* onConfigurationUpdate()事件回调：当系统环境变量（例如系统语言、深浅色等）发生变更时触发的事件回调，配置项均定义在[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)类中。
* onMemoryLevel()事件回调：当系统调整内存时触发的事件回调。应用被切换到后台时，系统会将在后台的应用保留在缓存中。即使应用处于缓存中，也会影响系统整体性能。当系统资源不足时，系统会通过多种方式从应用中回收内存，必要时会完全停止应用，从而释放内存用于执行关键任务。为了进一步保持系统内存的平衡，避免系统停止用户的应用进程，可以在AbilityStage中的onMemoryLevel()生命周期回调中订阅系统内存的变化情况，释放不必要的资源。
* onNewProcessRequest()事件回调：UIAbility启动时触发的事件回调。通过该回调，开发者可以指定每个UIAbility启动时是否在独立的进程中创建。该回调返回一个开发者自定义字符串标识，如果返回的字符串标识为开发者曾创建的，则复用该标识所对应的进程，否则创建新的进程。需要注意该回调需要配合在module.json5中声明[isolationProcess](module-configuration-file.md#abilities标签)字段为true。
* onPrepareTermination()事件回调：当应用被用户关闭时调用，可用于询问用户选择立即执行操作还是取消操作。开发者通过在回调中返回[AbilityConstant.PrepareTermination](../harmonyos-references/js-apis-app-ability-abilityconstant.md#preparetermination15)中定义的枚举类型通知系统是否继续执行关闭动作。
* onDestroy()生命周期回调：当对应Module的最后一个Ability实例退出后触发。此方法仅在应用正常销毁时触发。当应用程序异常退出或被终止时，将不会调用此方法。

## 开发步骤

### 创建AbilityStage文件

DevEco Studio默认工程中未自动生成AbilityStage，如需要使用AbilityStage的能力，可以手动新建一个AbilityStage文件，具体步骤如下。

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为exampleabilitystage。
2. 在exampleabilitystage目录，右键选择“New > ArkTS File”，新建一个文件并命名为MyAbilityStage.ets。
3. 打开MyAbilityStage.ets文件，导入AbilityStage的依赖包，自定义类继承AbilityStage并加上需要的生命周期回调，示例中增加了一个[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)生命周期回调。

   ```
   1. import { AbilityStage, Want } from '@kit.AbilityKit';

   3. export default class MyAbilityStage extends AbilityStage {
   4. onCreate(): void {
   5. // 应用HAP首次加载时触发，可以在此执行该Module的初始化操作（例如资源预加载、线程创建等）。
   6. }

   8. onAcceptWant(want: Want): string {
   9. // 仅specified模式下触发
   10. return 'MyAbilityStage';
   11. }
   12. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AbilityStage/entry/src/main/ets/exampleabilitystage/MyAbilityStage.ets#L16-L29)
4. 在[module.json5配置文件](module-configuration-file.md)中，通过配置 srcEntry 参数来指定模块对应的代码路径，以作为HAP加载的入口。

   ```
   1. {
   2. "module": {
   3. "name": "entry",
   4. "type": "entry",
   5. "srcEntry": "./ets/myabilitystage/MyAbilityStage.ets",
   6. // ···
   7. }
   8. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AbilityStage/entry/src/main/module.json5#L16-L71)

### 监听系统环境变量的变化

下面以监听系统环境变量的变化的开发场景为例，介绍AbilityStage组件回调函数的使用。

* 在onCreate()生命周期中，通过EnvironmentCallback来监听系统环境变化，例如系统语言、深浅色模式、屏幕方向、字体大小缩放比例、字体粗细缩放比例等信息。
* 当系统环境变量发生变更时，会触发EnvironmentCallback中的onConfigurationUpdated()回调，并打印相关信息。
* 通过关闭应用进程，可以触发AbilityStage的onDestroy()生命周期回调。

  ```
  1. import { EnvironmentCallback, AbilityStage } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. export default class MyAbilityStage extends AbilityStage {
  5. onCreate(): void {
  6. console.info('AbilityStage onCreate');
  7. let envCallback: EnvironmentCallback = {
  8. onConfigurationUpdated(config) {
  9. console.info(`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}`);
  10. let language = config.language; // 应用程序的当前语言
  11. let colorMode = config.colorMode; // 深浅色模式
  12. let direction = config.direction; // 屏幕方向
  13. let fontSizeScale = config.fontSizeScale; // 字体大小缩放比例
  14. let fontWeightScale = config.fontWeightScale; // 字体粗细缩放比例
  15. },
  16. onMemoryLevel(level) {
  17. console.info(`onMemoryLevel level: ${level}`);
  18. }
  19. };
  20. try {
  21. let applicationContext = this.context.getApplicationContext();
  22. let callbackId = applicationContext.on('environment', envCallback);
  23. console.info(`callbackId: ${callbackId}`);
  24. } catch (paramError) {
  25. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
  26. }
  27. }

  29. onDestroy(): void {
  30. // 通过onDestroy()方法，可以监听到Ability的销毁事件。
  31. console.info('AbilityStage onDestroy');
  32. }
  33. }
  ```

  [MyAbilityStage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/AbilityStage/entry/src/main/ets/myabilitystage/MyAbilityStage.ets#L16-L50)
