---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type
title: UIAbility组件启动模式
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > UIAbility组件启动模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:40+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9863cfad9c98d619779df88363a2d34a51554559971c9ad4d0efdd23ddb823a1
---

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的启动模式是指UIAbility实例在启动时的不同呈现状态。针对不同的业务场景，系统提供了三种启动模式：

* [singleton（单实例模式）](uiability-launch-type.md#singleton启动模式)
* [multiton（多实例模式）](uiability-launch-type.md#multiton启动模式)
* [specified（指定实例模式）](uiability-launch-type.md#specified启动模式)

说明

standard是multiton的曾用名，效果与多实例模式一致。

## singleton启动模式

singleton启动模式为单实例模式，也是默认情况下的启动模式。

每次调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法时，如果应用进程中该类型的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例已经存在，则复用系统中的UIAbility实例。系统中只存在唯一一个该UIAbility实例，即在最近任务列表中只存在一个该类型的UIAbility实例。

**图1** 单实例模式演示效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/WwWgrWs1SIyF8PamOT-6lA/zh-cn_image_0000002552797840.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=9804D7407559DE6B4D85DD025D66F283AE90368657A8AD4E41F536E28A67FAFC)

说明

应用的UIAbility实例已创建，该UIAbility配置为单实例模式，再次调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法启动该UIAbility实例。由于启动的还是原来的UIAbility实例，并未重新创建一个新的UIAbility实例，此时只会进入该UIAbility的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调，不会进入其[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调。如果已经创建的实例仍在启动过程中，调用startAbility()方法启动该实例，将收到错误码16000082。

如果需要使用singleton启动模式，在[module.json5配置文件](module-configuration-file.md)中的launchType字段配置为singleton即可。

```
1. {
2. "module": {
3. // ···
4. "abilities": [
5. // ···
6. {
7. "launchType": "singleton",
8. // ···
9. }
10. // ···
11. ]
12. }
13. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLaunchType/entry/src/main/module.json5#L15-L138)

## multiton启动模式

multiton启动模式为多实例模式，每次调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法时，都会在应用进程中创建一个新的该类型[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例。即在最近任务列表中可以看到有多个该类型的UIAbility实例。这种情况下可以将UIAbility配置为multiton（多实例模式）。

**图2** 多实例模式演示效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/UhwJRdQmTkiwSs5kb39WUw/zh-cn_image_0000002583437535.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=27988D368EEF70C5C65458B30274A9C48B3BF38851BBD0AE749376FC3353C219)

multiton启动模式的开发使用，在[module.json5配置文件](module-configuration-file.md)中的launchType字段配置为multiton即可。

```
1. {
2. "module": {
3. // ···
4. "abilities": [
5. // ···
6. {
7. "launchType": "multiton",
8. // ···
9. }
10. // ···
11. ]
12. }
13. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLaunchType/entry/src/main/module.json5#L16-L137)

## specified启动模式

specified启动模式为指定实例模式，针对一些特殊场景使用（例如文档应用中每次新建文档希望都能新建一个文档实例，重复打开一个已保存的文档希望打开的都是同一个文档实例）。

**图3** 指定实例启动模式原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/5VdS982zQFqLs-hViZTG3A/zh-cn_image_0000002552957490.png?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=F82BE7CFE4DDE9607BC7754099453C56F19CE9A3A3B37BA3E68C2ACCC7477C4E)

假设应用有两个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，即EntryAbility和SpecifiedAbility。EntryAbility以specified模式启动SpecifiedAbility。基本原理如下：

1. EntryAbility调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法，并在[Want](../harmonyos-references/js-apis-app-ability-want.md)的parameters字段中设置唯一的Key值，用于标识SpecifiedAbility。
2. 系统在拉起SpecifiedAbility之前，会先进入对应的[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)的[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)生命周期回调，获取用于标识目标UIAbility的Key值。
3. 系统会根据获取的Key值来匹配UIAbility。
   * 如果匹配到对应的UIAbility，则会启动该UIAbility实例，并进入[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调。
   * 如果无法匹配对应的UIAbility，则会创建一个新的UIAbility实例，并进入该UIAbility实例的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调和[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调。

**图4** 指定实例模式演示效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/AbKitJVkTGOa6xKH56GTrg/zh-cn_image_0000002583477491.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233739Z&HW-CC-Expire=86400&HW-CC-Sign=74AB053CD9055F8D5ABEA3545CE1D9547D2B6BE848AAB9D411E5993EE66EE2C1)

1. 在SpecifiedAbility中，需要将[module.json5配置文件](module-configuration-file.md)的launchType字段配置为specified。

   ```
   1. {
   2. "module": {
   3. // ···
   4. "abilities": [
   5. {
   6. "launchType": "specified",
   7. // ···
   8. }
   9. // ···
   10. ]
   11. }
   12. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLaunchType/entry/src/main/module.json5#L17-L136)
2. 在EntryAbility中，调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法时，可以在[want](../harmonyos-references/js-apis-app-ability-want.md)参数中传入了自定义参数instanceKey作为唯一标识符，以此来区分不同的UIAbility实例。示例中instanceKey的value值设置为字符串'KEY'。

   ```
   1. // 在启动指定实例模式的UIAbility时，给每一个UIAbility实例配置一个独立的Key标识
   2. // 例如在文档使用场景中，可以用文档路径作为Key标识
   3. import { common, Want } from '@kit.AbilityKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';

   7. const TAG: string = '[SpecifiedPage]';
   8. const DOMAIN_NUMBER: number = 0xFF00;

   10. function getInstance(): string {
   11. return 'KEY';
   12. }

   14. @Entry
   15. @Component
   16. struct SpecifiedPage {
   17. private KEY_NEW = 'KEY';

   19. build() {
   20. Row() {
   21. Column() {
   22. // ...
   23. // 请将$r('app.string.new_doc')替换为实际资源文件，在本示例中该资源文件的value值为"新建一个文档"
   24. Button($r('app.string.new_doc'))
   25. // ...
   26. .onClick(() => {
   27. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   28. // context为调用方UIAbility的UIAbilityContext;
   29. let want: Want = {
   30. deviceId: '', // deviceId为空表示本设备
   31. bundleName: 'com.samples.uiabilitylaunchtype',
   32. abilityName: 'SpecifiedFirstAbility',
   33. moduleName: 'entry', // moduleName非必选
   34. parameters: {
   35. // 自定义信息
   36. instanceKey: this.KEY_NEW
   37. }
   38. };
   39. context.startAbility(want).then(() => {
   40. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.');
   41. }).catch((err: BusinessError) => {
   42. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`);
   43. });
   44. this.KEY_NEW = this.KEY_NEW + 'a';
   45. })

   47. // 请将$r('app.string.open_old_doc')替换为实际资源文件，在本示例中该资源文件的value值为"打开已保存文档"
   48. Button($r('app.string.open_old_doc'))
   49. // ...
   50. .onClick(() => {
   51. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   52. // context为调用方UIAbility的UIAbilityContext;
   53. let want: Want = {
   54. deviceId: '', // deviceId为空表示本设备
   55. bundleName: 'com.samples.uiabilitylaunchtype',
   56. abilityName: 'SpecifiedSecondAbility',
   57. moduleName: 'entry', // moduleName非必选
   58. parameters: {
   59. // 自定义信息
   60. instanceKey: getInstance()
   61. }
   62. };
   63. context.startAbility(want).then(() => {
   64. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting SpecifiedAbility.');
   65. }).catch((err: BusinessError) => {
   66. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start SpecifiedAbility. Code is ${err.code}, message is ${err.message}`);
   67. });
   68. this.KEY_NEW = this.KEY_NEW + 'a';
   69. })
   70. }
   71. .width('100%')
   72. }
   73. .height('100%')
   74. }
   75. }
   ```

   [SpecifiedPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLaunchType/entry/src/main/ets/pages/SpecifiedPage.ets#L15-L71)
3. 开发者根据业务在SpecifiedAbility所对应AbilityStage的[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)生命周期回调设置该UIAbility的标识。示例中标识设置为SpecifiedAbilityInstance\_KEY。

   ```
   1. import { AbilityStage, Want } from '@kit.AbilityKit';

   3. export default class MyAbilityStage extends AbilityStage {
   4. onAcceptWant(want: Want): string {
   5. // 在被调用方的AbilityStage中，针对启动模式为specified的UIAbility返回一个UIAbility实例对应的一个Key值
   6. // 当前示例指的是module1 Module的SpecifiedAbility
   7. if (want.abilityName === 'SpecifiedFirstAbility' || want.abilityName === 'SpecifiedSecondAbility') {
   8. // 返回的字符串KEY标识为自定义拼接的字符串内容
   9. if (want.parameters) {
   10. return `SpecifiedAbilityInstance_${want.parameters.instanceKey}`;
   11. }
   12. }
   13. return 'MyAbilityStage';
   14. }
   15. }
   ```

   [MyAbilityStage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityLaunchType/entry/src/main/ets/abilitystage/MyAbilityStage.ets#L15-L31)

   说明

   1. 当应用的UIAbility实例已经被创建，并且配置为指定实例模式时，如果再次调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法启动该UIAbility实例，且[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)的[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)回调匹配到一个已创建的UIAbility实例，则系统会启动原来的UIAbility实例，并且不会重新创建一个新的UIAbility实例。此时，该UIAbility实例的onNewWant()回调会被触发，而不会触发onCreate()和onWindowStageCreate()生命周期回调。
   2. DevEco Studio默认工程中未自动生成AbilityStage，AbilityStage文件的创建请参见[AbilityStage开发步骤](abilitystage.md#开发步骤)。
   3. 建议specified启动模式的UIAbility，在[module.json5配置文件](module-configuration-file.md)中的removeMissionAfterTerminate字段设置为true，以达到UIAbility生命周期结束即从任务列表中移除任务的目的。 否则，在应用冷启动场景下会无法复用历史任务，在任务列表中出现多个相同任务的情况。

   例如在文档应用中，可以为不同的文档实例内容绑定不同的Key值。每次新建文档时，可以传入一个新的Key值（例如可以将文件的路径作为一个Key标识），此时[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)中启动[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)时都会创建一个新的UIAbility实例；当新建的文档保存之后，回到桌面，或者新打开一个已保存的文档，回到桌面，此时再次打开该已保存的文档，此时AbilityStage中再次启动该UIAbility时，打开的仍然是之前原来已保存的文档界面。

   以如下步骤所示进行举例说明。

   1. 打开文件A，对应启动一个新的UIAbility实例，例如启动UIAbility实例1。
   2. 在最近任务列表中关闭文件A的任务进程，此时UIAbility实例1被销毁，回到桌面，再次打开文件A，此时对应启动一个新的UIAbility实例，例如启动UIAbility实例2。
   3. 回到桌面，打开文件B，此时对应启动一个新的UIAbility实例，例如启动UIAbility实例3。
   4. 回到桌面，再次打开文件A，此时仍然启动之前的UIAbility实例2，因为系统会自动匹配UIAbility实例的Key值，如果存在与之匹配的Key，则会启动与之绑定的UIAbility实例。在此例中，之前启动的UIAbility实例2与文件A绑定的Key是相同的，因此系统会拉回UIAbility实例2并让其获焦，而不会创建新的实例。

## 示例代码

* [UIAbility的启动方式](https://gitcode.com/HarmonyOS_Samples/ability-start-mode)
