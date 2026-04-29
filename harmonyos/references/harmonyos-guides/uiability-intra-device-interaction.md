---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction
title: 启动应用内的UIAbility组件
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > 启动应用内的UIAbility组件
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e54578e9d0776354769913aa3eb2b9716da91bd0c94842f3e589a94ee91f1ea3
---

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)是系统调度的最小单元。在设备内的功能模块之间跳转时，会涉及到启动特定的UIAbility，包括应用内的其他UIAbility、或者其他应用的UIAbility（例如启动三方支付UIAbility）。

本文主要介绍启动应用内的UIAbility组件的方式。应用间的组件跳转详见[应用间跳转](link-between-apps-overview.md)。

* [启动应用内的UIAbility](uiability-intra-device-interaction.md#启动应用内的uiability)
* [启动应用内的UIAbility并获取返回结果](uiability-intra-device-interaction.md#启动应用内的uiability并获取返回结果)
* [启动UIAbility的指定页面](uiability-intra-device-interaction.md#启动uiability的指定页面)

## 启动应用内的UIAbility

当一个应用内包含多个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)时，存在应用内启动UIAbility的场景。例如在支付应用中从入口UIAbility启动收付款UIAbility。

假设应用中有两个UIAbility：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。

1. 在EntryAbility中，通过调用[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)方法启动UIAbility，[want](../harmonyos-references/js-apis-app-ability-want.md)为UIAbility实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的Ability名称，moduleName在待启动的UIAbility属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. import { common, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG: string = '[MainPage]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. @Entry
   9. @Component
   10. struct MainPage {
   11. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

   13. build() {
   14. Column() {
   15. List({ initialIndex: 0, space: 8 }) {

   17. ListItem() {
   18. Row() {
   19. // ...
   20. }
   21. .onClick(() => {
   22. // context为Ability对象的成员，在非Ability对象内部调用需要
   23. // 将Context对象传递过去
   24. let wantInfo: Want = {
   25. deviceId: '', // deviceId为空表示本设备
   26. bundleName: 'com.samples.uiabilityinteraction',
   27. moduleName: 'entry', // moduleName非必选
   28. abilityName: 'FuncAbilityA',
   29. parameters: {
   30. // 自定义信息
   31. // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
   32. info: $r('app.string.main_page_return_info')
   33. },
   34. };
   35. // context为调用方UIAbility的UIAbilityContext
   36. this.context.startAbility(wantInfo).then(() => {
   37. hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
   38. }).catch((error: BusinessError) => {
   39. hilog.error(DOMAIN_NUMBER, TAG, 'startAbility failed.');
   40. });
   41. })
   42. }

   44. // ...
   45. }
   46. // ...
   47. }
   48. // ...
   49. }
   50. }
   ```

   [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/MainPage.ets#L16-L213)
2. 在FuncAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调文件中接收EntryAbility传递过来的参数。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. // ···

   4. export default class FuncAbilityA extends UIAbility {
   5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   6. // 接收调用方UIAbility传过来的参数
   7. let funcAbilityWant = want;
   8. let info = funcAbilityWant?.parameters?.info;
   9. // ···
   10. }

   12. // ···
   13. }
   ```

   [FuncAbilityA.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/innerability/FuncAbilityA.ets#L16-L69)

   说明

   在被拉起的FuncAbility中，可以通过获取传递过来的[want](../harmonyos-references/js-apis-app-ability-want.md)参数的parameters来获取拉起方[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的PID、Bundle Name等信息。
3. 在FuncAbility业务完成之后，如需要停止当前[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，在FuncAbility中通过调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法实现。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG: string = '[FuncAbilityAPage]';
   5. const DOMAIN_NUMBER: number = 0xFF00;

   7. @Entry
   8. @Component
   9. struct FuncAbilityAPage {

   11. build() {
   12. Column() {
   13. // 请将$r('app.string.Stop_AbilityA')替换为实际资源文件，在本示例中该资源文件的value值为"StopFuncAbilityA"
   14. Button($r('app.string.Stop_AbilityA'))
   15. .onClick(() => {
   16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
   17. // context为需要停止的UIAbility实例的AbilityContext
   18. context.terminateSelf((err) => {
   19. if (err.code) {
   20. hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self. Code is ${err.code}, message is ${err.message}`);
   21. return;
   22. }
   23. });
   24. })
   25. // ...
   26. }
   27. // ...
   28. }
   29. }
   ```

   [FuncAbilityAPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/innerability/FuncAbilityAPage.ets#L16-L96)

   说明

   调用terminateSelf()方法停止当前UIAbility实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应UIAbility的[module.json5配置文件](module-configuration-file.md)中，将[abilities标签](module-configuration-file.md#abilities标签)的removeMissionAfterTerminate字段配置为true。
4. 如需要关闭应用所有的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，可以调用[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)的[killAllProcesses()](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextkillallprocesses)方法实现关闭应用所有的进程。

## 启动应用内的UIAbility并获取返回结果

在一个EntryAbility启动另外一个FuncAbility时，希望在被启动的FuncAbility完成相关业务后，能将结果返回给调用方。例如在应用中将入口功能和账号登录功能分别设计为两个独立的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)，在账号登录UIAbility中完成登录操作后，需要将登录的结果返回给入口UIAbility。

1. 在EntryAbility中，调用[startAbilityForResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilityforresult-2)接口启动FuncAbility，异步回调中的data用于接收FuncAbility停止自身后返回给EntryAbility的信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. import { common, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG: string = '[MainPage]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. @Entry
   9. @Component
   10. struct MainPage {
   11. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

   13. build() {
   14. Column() {
   15. List({ initialIndex: 0, space: 8 }) {

   17. // ...

   19. ListItem() {
   20. Row() {
   21. // ...
   22. }
   23. .onClick(() => {
   24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
   25. const RESULT_CODE: number = 1001;
   26. let want: Want = {
   27. deviceId: '', // deviceId为空表示本设备
   28. bundleName: 'com.samples.uiabilityinteraction',
   29. moduleName: 'entry', // moduleName非必选
   30. abilityName: 'FuncAbilityA',
   31. parameters: {
   32. // 自定义信息
   33. // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
   34. info: $r('app.string.main_page_return_info')
   35. }
   36. };
   37. context.startAbilityForResult(want).then((data) => {
   38. if (data?.resultCode === RESULT_CODE) {
   39. // 解析被调用方UIAbility返回的信息
   40. let info = data.want?.parameters?.info;
   41. hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
   42. if (info !== null) {
   43. this.getUIContext().getPromptAction().showToast({
   44. message: JSON.stringify(info)
   45. });
   46. }
   47. }
   48. hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
   49. }).catch((err: BusinessError) => {
   50. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
   51. });
   52. })
   53. }

   55. // ...
   56. }
   57. // ...
   58. }
   59. // ...
   60. }
   61. }
   ```

   [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/MainPage.ets#L17-L212)
2. 在FuncAbility停止自身时，需要调用[terminateSelfWithResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)方法，入参[abilityResult](../harmonyos-references/js-apis-inner-ability-abilityresult.md)为FuncAbility需要返回给EntryAbility的信息。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. const TAG: string = '[FuncAbilityAPage]';
   5. const DOMAIN_NUMBER: number = 0xFF00;

   7. @Entry
   8. @Component
   9. struct FuncAbilityAPage {

   11. build() {
   12. Column() {
   13. // ...

   15. List({ initialIndex: 0 }) {
   16. ListItem() {
   17. Row() {
   18. // ...
   19. }
   20. .onClick(() => {
   21. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
   22. const RESULT_CODE: number = 1001; // FuncAbilityA返回的结果
   23. let abilityResult: common.AbilityResult = {
   24. resultCode: RESULT_CODE,
   25. want: {
   26. bundleName: 'com.samples.uiabilityinteraction',
   27. moduleName: 'entry', // moduleName非必选
   28. abilityName: 'FuncAbilityA',
   29. parameters: {
   30. // 请将$r('app.string.ability_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自FuncAbility Index页面"
   31. info: context.resourceManager.getStringSync($r('app.string.ability_return_info').id)
   32. },
   33. },
   34. };
   35. context.terminateSelfWithResult(abilityResult, (err) => {
   36. if (err.code) {
   37. hilog.error(DOMAIN_NUMBER, TAG, `Failed to terminate self with result. Code is ${err.code}, message is ${err.message}`);
   38. return;
   39. }
   40. });
   41. })
   42. }
   43. }
   44. // ...
   45. }
   46. // ...
   47. }
   48. }
   ```

   [FuncAbilityAPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/innerability/FuncAbilityAPage.ets#L17-L95)
3. FuncAbility停止自身后，EntryAbility通过[startAbilityForResult()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startabilityforresult-2)方法回调接收被FuncAbility返回的信息，RESULT\_CODE需要与前面的数值保持一致。

   ```
   1. import { common, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const TAG: string = '[MainPage]';
   6. const DOMAIN_NUMBER: number = 0xFF00;

   8. @Entry
   9. @Component
   10. struct MainPage {
   11. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

   13. build() {
   14. Column() {
   15. List({ initialIndex: 0, space: 8 }) {

   17. // ...

   19. ListItem() {
   20. Row() {
   21. // ...
   22. }
   23. .onClick(() => {
   24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
   25. const RESULT_CODE: number = 1001;
   26. let want: Want = {
   27. deviceId: '', // deviceId为空表示本设备
   28. bundleName: 'com.samples.uiabilityinteraction',
   29. moduleName: 'entry', // moduleName非必选
   30. abilityName: 'FuncAbilityA',
   31. parameters: {
   32. // 自定义信息
   33. // 请将$r('app.string.main_page_return_info')替换为实际资源文件，在本示例中该资源文件的value值为"来自EntryAbility MainPage页面"
   34. info: $r('app.string.main_page_return_info')
   35. }
   36. };
   37. context.startAbilityForResult(want).then((data) => {
   38. if (data?.resultCode === RESULT_CODE) {
   39. // 解析被调用方UIAbility返回的信息
   40. let info = data.want?.parameters?.info;
   41. hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(info) ?? '');
   42. if (info !== null) {
   43. this.getUIContext().getPromptAction().showToast({
   44. message: JSON.stringify(info)
   45. });
   46. }
   47. }
   48. hilog.info(DOMAIN_NUMBER, TAG, JSON.stringify(data.resultCode) ?? '');
   49. }).catch((err: BusinessError) => {
   50. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability for result. Code is ${err.code}, message is ${err.message}`);
   51. });
   52. })
   53. }

   55. // ...
   56. }
   57. // ...
   58. }
   59. // ...
   60. }
   61. }
   ```

   [MainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/MainPage.ets#L18-L211)

## 启动UIAbility的指定页面

### 概述

一个[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。

UIAbility的启动分为两种情况：UIAbility冷启动和UIAbility热启动。

* UIAbility冷启动：指的是UIAbility实例处于完全关闭状态下被启动，这需要完整地加载和初始化UIAbility实例的代码、资源等。
* UIAbility热启动：指的是UIAbility实例已经启动并在前台运行过，由于某些原因切换到后台，再次启动该UIAbility实例，这种情况下可以快速恢复UIAbility实例的状态。

本文主要讲解[目标UIAbility冷启动](uiability-intra-device-interaction.md#目标uiability冷启动)和[目标UIAbility热启动](uiability-intra-device-interaction.md#目标uiability热启动)两种启动指定页面的场景，以及在讲解启动指定页面之前会讲解到在调用方如何指定启动页面。

### 调用方UIAbility指定启动页面

调用方[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，Second对应功能A页面），此时需要在传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中配置指定的页面路径信息，可以通过Want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const TAG: string = '[MainPage]';
6. const DOMAIN_NUMBER: number = 0xFF00;

8. @Entry
9. @Component
10. struct MainPage {
11. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

13. build() {
14. Column() {
15. List({ initialIndex: 0, space: 8 }) {

17. // ...

19. ListItem() {
20. Row() {
21. // ...
22. }
23. .onClick(() => {
24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
25. let want: Want = {
26. deviceId: '', // deviceId为空表示本设备
27. bundleName: 'com.samples.uiabilityinteraction',
28. moduleName: 'entry', // moduleName非必选
29. abilityName: 'ColdStartAbility',
30. parameters: { // 自定义参数传递页面信息
31. router: 'funcA'
32. }
33. };
34. // context为调用方UIAbility的UIAbilityContext
35. context.startAbility(want).then(() => {
36. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting ability.');
37. }).catch((err: BusinessError) => {
38. hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${err.code}, message is ${err.message}`);
39. });
40. })
41. }

43. // ...
44. }
45. // ...
46. }
47. // ...
48. }
49. }
```

[MainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/MainPage.ets#L19-L210)

### 目标UIAbility冷启动

目标[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)冷启动时，在目标UIAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调中，接收调用方传过来的参数。然后在目标UIAbility的[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，解析调用方传递过来的[want](../harmonyos-references/js-apis-app-ability-want.md)参数，获取到需要加载的页面信息url，传入[windowStage.loadContent()](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)方法。

```
1. import { AbilityConstant, Want, UIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window, UIContext } from '@kit.ArkUI';

5. const DOMAIN_NUMBER: number = 0xFF00;
6. const TAG: string = '[ColdStartAbility]';

8. export default class ColdStartAbility extends UIAbility {
9. private funcAbilityWant: Want | undefined = undefined;
10. private uiContext: UIContext | undefined = undefined;

12. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
13. // 接收调用方UIAbility传过来的参数
14. this.funcAbilityWant = want;
15. }

17. onWindowStageCreate(windowStage: window.WindowStage): void {
18. // Main window is created, set main page for this ability
19. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
20. // Main window is created, set main page for this ability
21. let url = 'pages/Index';
22. if (this.funcAbilityWant?.parameters?.router && this.funcAbilityWant.parameters.router === 'funcA') {
23. url = 'pages/ColdPage';
24. }
25. windowStage.loadContent(url, (err, data) => {
26. // ···
27. });
28. }
29. }
```

[ColdStartAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/specifiedability/ColdStartAbility.ets#L16-L61)

### 目标UIAbility热启动

在应用开发中，会遇到目标[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例之前已经启动过的场景，这时再次启动目标UIAbility时，不会重新走初始化逻辑，只会直接触发[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期方法。为了实现跳转到指定页面，需要在onNewWant()中解析参数进行处理。

例如短信应用和联系人应用配合使用的场景。

1. 用户先打开短信应用，短信应用的UIAbility实例启动，显示短信应用的主页。
2. 用户将设备回到桌面界面，短信应用进入后台运行状态。
3. 用户打开联系人应用，找到联系人张三。
4. 用户点击联系人张三的短信按钮，会再次启动短信应用的UIAbility实例。
5. 由于短信应用的UIAbility实例已经启动过了，此时会触发该UIAbility的onNewWant()回调，而不会再走[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)和[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)等初始化逻辑。

图1 目标UIAbility热启动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/T9eSctGfTBeyr9ZZ7e7_nA/zh-cn_image_0000002558604326.png?HW-CC-KV=V1&HW-CC-Date=20260429T052543Z&HW-CC-Expire=86400&HW-CC-Sign=44030390D369CB2DFB857908D69F699101ACAAA6332C1E9BB2592C17E49C66A7)

开发步骤如下所示。

1. 冷启动短信应用的UIAbility实例时，在[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，通过调用[getUIContext()](../harmonyos-references/arkts-apis-window-window.md#getuicontext10)接口获取UI上下文实例[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)对象。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { Want, UIAbility } from '@kit.AbilityKit';
   3. import { window, UIContext } from '@kit.ArkUI';
   4. const DOMAIN_NUMBER: number = 0xFF00;
   5. const TAG: string = '[HotStartAbility]';

   7. export default class HotStartAbility extends UIAbility {
   8. private funcAbilityWant: Want | undefined = undefined;
   9. private uiContext: UIContext | undefined = undefined;
   10. // ···

   12. onWindowStageCreate(windowStage: window.WindowStage): void {
   13. // Main window is created, set main page for this ability
   14. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');
   15. let url = 'pages/Index';
   16. windowStage.loadContent(url, (err, data) => {
   17. if (err.code) {
   18. return;
   19. }

   21. let windowClass: window.Window;
   22. windowStage.getMainWindow((err, data) => {
   23. if (err.code) {
   24. hilog.error(DOMAIN_NUMBER, TAG, `Failed to obtain the main window. Code is ${err.code}, message is ${err.message}`);
   25. return;
   26. }
   27. windowClass = data;
   28. this.uiContext = windowClass.getUIContext();
   29. });
   30. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
   31. });
   32. }

   34. // ···
   35. }
   ```

   [HotStartAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/specifiedability/HotStartAbility.ets#L16-L68)
2. 在短信应用UIAbility的[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中通过AppStorage设置全局变量nameForNavi的值，并进行指定页面的跳转。此时再次启动该短信应用的UIAbility实例时，即可跳转到该短信应用的UIAbility实例的指定页面。

   1. 导入相关模块，并在onNewWant()生命周期回调中设置全局变量nameForNavi的值。

      ```
      1. import { hilog } from '@kit.PerformanceAnalysisKit';
      2. import { Want, UIAbility, AbilityConstant } from '@kit.AbilityKit';
      3. // ···
      4. const DOMAIN_NUMBER: number = 0xFF00;
      5. const TAG: string = '[HotStartAbility]';

      7. export default class HotStartAbility extends UIAbility {
      8. // ···

      10. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      11. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'onNewWant');
      12. AppStorage.setOrCreate<string>('nameForNavi', 'pageOne');
      13. }
      14. }
      ```

      [HotStartAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/specifiedability/HotStartAbility.ets#L17-L67)
   2. 在Index页面显示时触发onPageShow回调，获取全局变量nameForNavi的值，并进行执行页面的跳转。

      ```
      1. @Entry
      2. @Component
      3. struct Index {
      4. @State message: string = 'Index';
      5. pathStack: NavPathStack = new NavPathStack();

      7. onPageShow(): void {
      8. let somePage = AppStorage.get<string>('nameForNavi')
      9. if (somePage) {
      10. this.pathStack.pushPath({ name: somePage }, false);
      11. AppStorage.delete('nameForNavi');
      12. }
      13. }

      15. build() {
      16. Navigation(this.pathStack) {
      17. Text(this.message)
      18. .id('Index')
      19. // 请将$r('app.float.page_text_font_size')替换为实际资源文件，在本示例中该资源文件的value值为"50fp"
      20. .fontSize($r('app.float.page_text_font_size'))
      21. .fontWeight(FontWeight.Bold)
      22. .alignRules({
      23. center: { anchor: '__container__', align: VerticalAlign.Center },
      24. middle: { anchor: '__container__', align: HorizontalAlign.Center }
      25. })
      26. }
      27. .mode(NavigationMode.Stack)
      28. .height('100%')
      29. .width('100%')
      30. .margin({top:250})
      31. }
      32. }
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/Index.ets#L16-L48)
   3. 实现Navigation子页面。

      ```
      1. @Builder
      2. export function PageOneBuilder() {
      3. PageOne();
      4. }

      6. @Component
      7. export struct PageOne {
      8. @State message: string = 'PageOne';
      9. pathStack: NavPathStack = new NavPathStack();

      11. build() {
      12. NavDestination() {
      13. Text(this.message)
      14. .id('PageOne')
      15. // 请将$r('app.float.page_text_font_size')替换为实际资源文件，在本示例中该资源文件的value值为"50fp"
      16. .fontSize($r('app.float.page_text_font_size'))
      17. .fontWeight(FontWeight.Bold)
      18. .alignRules({
      19. center: { anchor: '__container__', align: VerticalAlign.Center },
      20. middle: { anchor: '__container__', align: HorizontalAlign.Center }
      21. })
      22. }
      23. .onReady((context: NavDestinationContext) => {
      24. this.pathStack = context.pathStack;
      25. })
      26. .height('100%')
      27. .width('100%')
      28. .margin({top:250})
      29. }
      30. }
      ```

      [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/ets/pages/PageOne.ets#L16-L46)
   4. 在系统配置文件route\_map.json中配置子页信息（参考[系统路由表](arkts-navigation-cross-package.md#系统路由表)）。

      ```
      1. // route_map.json
      2. {
      3. "routerMap": [
      4. {
      5. "name": "pageOne",
      6. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      7. "buildFunction": "PageOneBuilder",
      8. "data": {
      9. "description": "this is pageOne"
      10. }
      11. }
      12. ]
      13. }
      ```
   5. 在[module.json5配置文件](module-configuration-file.md#routermap标签)中配置routerMap路由映射。

      ```
      1. {
      2. "module": {
      3. // ···
      4. "routerMap": "$profile:router_map",
      5. // ···
      6. }
      7. }
      ```

      [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityInteraction/entry/src/main/module.json5#L16-L134)

说明

当被调用方[UIAbility组件启动模式](uiability-launch-type.md)设置为multiton启动模式时，每次启动都会创建一个新的实例，那么onNewWant()回调就不会被用到。
