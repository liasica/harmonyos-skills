---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage
title: UIAbility组件基本用法
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > UIAbility组件 > UIAbility组件基本用法
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8bdf6b6c6b56f8abae12b9a653773cf67520d71570e068d9954a0adece799c47
---

本文主要介绍[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件的基本用法，包括：

* 指定UIAbility的启动页面。
* 获取UIAbility的上下文[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)。
* 获取UIAbility拉起方的信息。

## 指定UIAbility的启动页面

应用中的[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)在启动过程中，需要指定启动页面，否则应用启动后会因为没有默认加载页面而导致白屏。可以在UIAbility的[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期回调中，通过[WindowStage](../harmonyos-references/arkts-apis-window-windowstage.md)对象的[loadContent()](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)方法设置启动页面。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. // ···

5. export default class EntryAbility extends UIAbility {
6. // ···

8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. // Main window is created, set main page for this ability
10. windowStage.loadContent('pages/Index', (err) => {
11. // ···
12. });
13. }

15. // ···
16. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/entryability/EntryAbility.ets#L16-L72)

说明

在DevEco Studio中创建的UIAbility中，该UIAbility实例默认会加载Index页面，根据需要将Index页面路径替换为需要的页面路径即可。

## 获取UIAbility的上下文信息

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)类拥有自身的上下文信息，该信息为[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类的实例，[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类拥有abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，以及可以获取操作UIAbility实例的方法（如[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)、[connectServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)、[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)等）。

如果需要在页面中获得当前Ability的Context，需要通过调用组件的[getUIContext](../harmonyos-references/ts-custom-component-api.md#getuicontext)方法获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)对象，再调用UIContext对象的[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)方法获取当前页面关联的UIAbilityContext或[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)。

* 在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。

  ```
  1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  2. // ···

  4. export default class EntryAbility extends UIAbility {
  5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  6. // 获取UIAbility实例的上下文
  7. let context = this.context;
  8. }
  9. // ···
  10. }
  ```

  [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/entryability/EntryAbility.ets#L17-L71)
* 在页面中获取UIAbility实例的上下文信息，包括导入依赖资源context模块和在组件中定义一个context变量两个部分。

  ```
  1. import { common, Want } from '@kit.AbilityKit';

  3. @Entry
  4. @Component
  5. struct EventHubPage {
  6. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  8. startAbilityTest(): void {
  9. let want: Want = {
  10. // Want参数信息
  11. // ...
  12. };
  13. this.context.startAbility(want);
  14. }

  16. // 页面展示
  17. build() {
  18. // ...
  19. }
  20. }
  ```

  [EventHubPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/context/EventHubPage.ets#L16-L54)

  也可以在导入依赖资源context模块后，在具体使用[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)前进行变量定义。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. // ...

  4. @Entry
  5. @Component
  6. struct BasicUsage {
  7. startAbilityTest(): void {
  8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  9. let want: Want = {
  10. // Want参数信息
  11. // ...
  12. };
  13. context.startAbility(want);
  14. }

  16. // 页面展示
  17. build() {
  18. // ...
  19. }
  20. }
  ```

  [BasicUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/context/BasicUsage.ets#L16-L94)
* 当业务完成后，开发者如果想要终止当前[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，可以通过调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法实现。

  ```
  1. import { common, Want } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';

  5. const DOMAIN = 0x0000;

  7. @Entry
  8. @Component
  9. struct BasicUsage {
  10. // ...

  12. // 页面展示
  13. build() {
  14. Column() {
  15. // ...

  17. Button('FuncAbilityB')
  18. .onClick(() => {
  19. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  20. try {
  21. context.terminateSelf((err: BusinessError) => {
  22. if (err.code) {
  23. // 处理业务逻辑错误
  24. hilog.error(DOMAIN, 'terminateSelf', `terminateSelf failed, code is ${err.code}, message is ${err.message}.`);
  25. return;
  26. }
  27. // 执行正常业务
  28. hilog.info(DOMAIN, 'terminateSelf', `terminateSelf succeed.`);
  29. });
  30. } catch (err) {
  31. // 捕获同步的参数错误
  32. let code = (err as BusinessError).code;
  33. let message = (err as BusinessError).message;
  34. hilog.error(DOMAIN, 'terminateSelf', `terminateSelf failed, code is ${code}, message is ${message}.`);
  35. }
  36. })
  37. // ...
  38. }
  39. // ...
  40. }
  41. }
  ```

  [BasicUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/context/BasicUsage.ets#L17-L93)

## 获取UIAbility拉起方的信息

拉起方（UIAbilityA）通过startAbility启动目标方（UIAbilityB）时，UIAbilityB可以通过[parameters](../harmonyos-references/js-apis-app-ability-want.md)参数获取UIAbilityA的Pid、BundleName和AbilityName等信息。

1. 通过点击UIAbilityA中的"拉起UIAbilityB"按钮，拉起UIAbilityB。

   ```
   1. import { common, Want } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   9. build() {
   10. List({ space: 4 }) {
   11. ListItem() {
   12. Button('terminateSelf').onClick(() => {
   13. this.context.terminateSelf()
   14. })
   15. .width('100%')

   17. }

   19. ListItem() {
   20. // 请将$r('app.string.Start_UIAbilityB')替换为实际资源文件，在本示例中该资源文件的value值为"拉起UIAbilityB"
   21. Button($r('app.string.Start_UIAbilityB'))
   22. .onClick((event: ClickEvent) => {
   23. let want: Want = {
   24. bundleName: this.context.abilityInfo.bundleName,
   25. abilityName: 'UIAbilityB',
   26. };

   28. this.context.startAbility(want, (err: BusinessError) => {
   29. if (err.code) {
   30. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}.`);
   31. }
   32. });
   33. })
   34. .width('100%')
   35. }
   36. }
   37. .listDirection(Axis.Vertical)
   38. .backgroundColor(0xDCDCDC).padding(20)
   39. .margin({top:250})
   40. }
   41. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/pages/Index.ets#L16-L58)
2. 在UIAbilityB的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中，获取UIAbilityA的Pid、BundleName和AbilityName，并通过日志输出。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. const DOMAIN = 0x0000;

   7. export default class UIAbilityB extends UIAbility {
   8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   9. // 调用方无需手动传递parameters参数，系统会自动向Want对象中传递调用方信息。
   10. hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerPid: ${want.parameters?.['ohos.aafwk.param.callerPid']}.`);
   11. hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerBundleName: ${want.parameters?.['ohos.aafwk.param.callerBundleName']}.`);
   12. hilog.info(DOMAIN, 'UIAbilityB', `onCreate, callerAbilityName: ${want.parameters?.['ohos.aafwk.param.callerAbilityName']}.`);
   13. }

   15. onDestroy(): void {
   16. hilog.info(DOMAIN, 'UIAbilityB', `UIAbilityB onDestroy.`);
   17. }

   19. onWindowStageCreate(windowStage: window.WindowStage): void {
   20. hilog.info(DOMAIN, 'UIAbilityB', `Ability onWindowStageCreate.`);

   22. windowStage.loadContent('context/BasicUsage', (err) => {
   23. if (err.code) {
   24. hilog.error(DOMAIN, 'UIAbilityB', `Failed to load the content, error code: ${err.code}, error msg: ${err.message}.`);
   25. return;
   26. }
   27. hilog.info(DOMAIN, 'UIAbilityB', `Succeeded in loading the content.`);
   28. });
   29. }
   30. }
   ```

   [UIAbilityB.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/UIAbilityUsage/entry/src/main/ets/entryability/UIAbilityB.ets#L16-L47)
