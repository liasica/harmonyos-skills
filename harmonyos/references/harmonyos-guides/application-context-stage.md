---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage
title: 应用上下文Context
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > 应用上下文Context
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d32f1fb9f5f9e848afed9f47c6dc8937b1773b395ade8250899dbfdb2b481a1e
---

## 概述

[Context](../harmonyos-references/js-apis-inner-application-context.md)是应用中对象的上下文，其提供了应用的一些基础信息，例如[resourceManager](../harmonyos-references/js-apis-resource-manager.md)（资源管理）、[applicationInfo](../harmonyos-references/js-apis-bundlemanager-applicationinfo.md)（当前应用信息）、[area](../harmonyos-references/js-apis-app-ability-contextconstant.md#areamode)（文件分区）等。

## 不同类型Context的对比

[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件和各种[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)派生类组件都有各自不同的Context类。分别有基类Context、[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)、[AbilityStageContext](../harmonyos-references/js-apis-inner-application-abilitystagecontext.md)、[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)、[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)等Context。各类Context的继承和持有关系详见[不同类型Context的继承和持有关系](../harmonyos-references/js-apis-inner-application-context.md#不同类型context的继承和持有关系)。

不同类型Context的获取方式与使用场景说明，如下表所示。

说明

不同类型的Context具有不同的能力，不可相互替代或强行转换。例如，[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)绑定了[setFontSizeScale](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetfontsizescale13)方法，但[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)中没有此方法。因此，即使将UIAbilityContext强行转换为ApplicationContext，也无法调用setFontSizeScale方法。

**表1** 不同类型Context的说明

| Context类型 | 说明 | 获取方式 | 使用场景 |
| --- | --- | --- | --- |
| [ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md) | 应用的全局上下文，提供应用级别的信息和能力。 | - 从API version 14开始，可以直接使用[getApplicationContext](../harmonyos-references/js-apis-app-ability-application.md#applicationgetapplicationcontext14)获取。  - API version 14以前版本，只能使用其他Context实例的[getApplicationContext](../harmonyos-references/js-apis-inner-application-context.md#getapplicationcontext)方法获取。 | - [获取当前应用的基本信息](application-context-stage.md#获取基本信息)。  - [获取应用级别的文件路径](application-context-stage.md#获取应用文件路径)。  - [获取和修改加密分区](application-context-stage.md#获取和修改加密分区)。  - [监听应用前后台变化](application-context-stage.md#监听应用前后台变化)。 |
| [AbilityStageContext](../harmonyos-references/js-apis-inner-application-abilitystagecontext.md) | 模块级别的上下文，提供模块级别的信息和能力。 | - 如果需要获取当前AbilityStage的Context，可以直接通过AbilityStage实例获取[context](../harmonyos-references/js-apis-app-ability-abilitystage.md#属性)属性。  - 如果需要获取同一应用中其他Module的Context，可以通过[createModuleContext](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatemodulecontext)方法。 | - 获取当前模块的基本信息。  - [获取模块级别的文件路径](application-context-stage.md#获取应用文件路径)。 |
| [UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md) | UIAbility组件对应的上下文，提供UIAbility对外的信息和能力。 | - 通过UIAbility实例直接获取[context](../harmonyos-references/js-apis-app-ability-uiability.md#属性)属性。  - 在UIAbility的窗口中加载的UI组件实例，需要使用@ohos.arkui.UIContext提供的[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)方法。 | - 获取当前UIAbility的基本信息。  - 启动其他应用或元服务、连接/断连系统应用创建的ServiceExtensionAbility等。  - 销毁自身的UIAbility。 |
| [ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md) | ExtensionAbility组件对应的上下文，每种类型的ExtensionContext提供不同的信息和能力。 | 通过ExtensionAbility实例直接获取Context属性。 | 不同类型的ExtensionAbility对应的Context提供的能力不同。以输入法上下文[InputMethodExtensionContext](../harmonyos-references/js-apis-inputmethod-extension-context.md)为例，主要提供如下能力：  - 获取InputMethodExtensionAbility的基本信息。  - 销毁当前输入法。 |
| [UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md) | ArkUI的UI实例上下文，提供UI操作相关的能力。与上述其他类型的Context无直接关系。 | - 在UI组件内获取UIContext，直接使用组件内置的[getUIContext](../harmonyos-references/ts-custom-component-api.md#getuicontext)方法。  - 在存在Window实例的情况下，使用@ohos.window提供的[getUIContext](../harmonyos-references/arkts-apis-window-window.md#getuicontext10)方法。 | 主要用于UI实例中UI相关操作，例如：  - 获取当前UI实例的字体。  - 显示不同类型的弹框。  - 设置软键盘弹出时UI避让模式。 |

## Context的获取方式

开发者如果需要通过Context获取应用资源、应用路径等信息，或者使用Context提供的方法来实现应用跳转、设置环境变量、清理数据、获取权限等操作，需要先获取对应的Context。本节分别介绍不同类型Context的获取方式与使用场景。

### 获取ApplicationContext（应用的全局上下文）

[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)在基类Context的基础上提供了监听应用内应用组件的生命周期的变化、监听系统内存变化、监听应用内系统环境变化、设置应用语言、设置应用颜色模式、清除应用自身数据的同时撤销应用向用户申请的权限等能力，在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)、[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)、[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)中均可以获取。

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. let applicationContext = this.context.getApplicationContext();
6. }
7. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/entryexampleability/EntryAbility.ets#L16-L24)

### 获取AbilityStageContext（模块级别的上下文）

[AbilityStageContext](../harmonyos-references/js-apis-inner-application-abilitystagecontext.md)和基类Context相比，额外提供[HapModuleInfo](../harmonyos-references/js-apis-bundlemanager-hapmoduleinfo.md)、[Configuration](../harmonyos-references/js-apis-app-ability-configuration.md)等信息。

```
1. import { AbilityStage } from '@kit.AbilityKit';

3. export default class MyAbilityStage extends AbilityStage {
4. onCreate(): void {
5. let abilityStageContext = this.context;
6. // ...
7. }
8. }
```

[MyAbilityStage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/abilitystagecontextability/MyAbilityStage.ets#L16-L25)

### 获取本应用中其他Module的Context（模块级别的上下文）

调用[createModuleContext](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatemodulecontext)方法，获取本应用中其他Module的Context。获取到其他Module的Context之后，即可获取到相应Module的资源信息。

```
1. import { common, application } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = '[CreateModuleContext]';
6. const DOMAIN = 0xF811;

8. let storageEventCall = new LocalStorage();

10. @Entry(storageEventCall)
11. @Component
12. struct CreateModuleContext {
13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

15. build() {
16. Column() {
17. // ...
18. List({ initialIndex: 0 }) {
19. ListItem() {
20. Row() {
21. // ...
22. }
23. .onClick(() => {
24. let moduleName2: string = 'entry';
25. application.createModuleContext(this.context, moduleName2)
26. .then((data: common.Context) => {
27. hilog.info(DOMAIN, TAG, `CreateModuleContext success, data: ${JSON.stringify(data)}`);
28. if (data !== null) {
29. this.getUIContext().getPromptAction().showToast({
30. // 请将$r('app.string.success_message')替换为实际资源文件，在本示例中该资源文件的value值为"成功获取Context"
31. message: $r('app.string.success_message')
32. });
33. }
34. })
35. .catch((err: BusinessError) => {
36. hilog.error(DOMAIN, TAG, `CreateModuleContext failed, err code:${err.code}, err msg: ${err.message}`);
37. });
38. })
39. }
40. // ...
41. }
42. // ...
43. }
44. // ...
45. }
46. }
```

[CreateModuleContext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/CreateModuleContext.ets#L16-L75)

### 获取UIAbilityContext（UIAbility组件的上下文）

[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)和基类[Context](../harmonyos-references/js-apis-inner-application-context.md)相比，额外提供abilityInfo、currentHapModuleInfo等属性。通过UIAbilityContext可以获取UIAbility的相关配置信息，如包代码路径、Bundle名称、Ability名称和应用程序需要的环境状态等属性信息，也可以获取操作UIAbility实例的方法（如[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)、[connectServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)、[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)等）。

* 在UIAbility中可以通过this.context获取UIAbility实例的上下文信息。

  ```
  1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

  3. export default class EntryAbility extends UIAbility {
  4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  5. // 获取UIAbility实例的上下文
  6. let context = this.context;
  7. }
  8. }
  ```

  [UIAbilityContextAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/uiAbilitycontextability/UIAbilityContextAbility.ets#L16-L25)
* 在页面中获取UIAbility实例的上下文信息。

  ```
  1. import { common, Want } from '@kit.AbilityKit'; // 导入依赖资源context模块

  3. @Entry
  4. @Component
  5. struct EventHub {
  6. // 定义context变量
  7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  9. startAbilityTest(): void {
  10. let want: Want = {
  11. // Want参数信息
  12. };
  13. this.context.startAbility(want);
  14. }

  16. // 页面展示
  17. build() {
  18. // ···
  19. }
  20. }
  ```

  [EventHub.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/EventHub.ets#L16-L43)

  也可以在导入依赖资源context模块后，在具体使用[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)前进行变量定义。

  ```
  1. import { common, Want } from '@kit.AbilityKit';

  3. @Entry
  4. @Component
  5. struct UIAbilityComponentsBasicUsage {
  6. startAbilityTest(): void {
  7. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  8. let want: Want = {
  9. // Want参数信息
  10. };
  11. context.startAbility(want);
  12. }

  14. // 页面展示
  15. build() {
  16. // ···
  17. }
  18. }
  ```

  [UIAbilityComponentsBasicUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/UIAbilityComponentsBasicUsage.ets#L16-L41)
* 当业务完成后，开发者如果想要终止当前[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)实例，可以通过调用[terminateSelf()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)方法实现。

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';

  5. const TAG = '[UIAbilityComponentsUsage]';
  6. const DOMAIN = 0xF811;
  7. @Entry
  8. @Component
  9. struct UIAbilityComponentsUsage {
  10. // 页面展示
  11. build() {
  12. Column() {
  13. // ···
  14. Button('FuncAbilityB')
  15. .onClick(() => {
  16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  17. try {
  18. context.terminateSelf((err: BusinessError) => {
  19. if (err.code) {
  20. // 处理业务逻辑错误
  21. hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${err.code}, message is ${err.message}.`);
  22. return;
  23. }
  24. // 执行正常业务
  25. hilog.info(DOMAIN, TAG, `terminateSelf succeed.`);
  26. });
  27. } catch (err) {
  28. // 捕获同步的参数错误
  29. let code = (err as BusinessError).code;
  30. let message = (err as BusinessError).message;
  31. hilog.error(DOMAIN, TAG, `terminateSelf failed, code is ${code}, message is ${message}.`);
  32. }
  33. })
  34. }
  35. }
  36. }
  ```

  [UIAbilityComponentsUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/UIAbilityComponentsUsage.ets#L16-L56)

### 获取ExtensionAbilityContext (ExtensionAbility组件的上下文)

获取特定场景[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)。以FormExtensionContext为例，表示卡片服务的上下文环境，继承自ExtensionContext，提供卡片服务相关的接口能力。

```
1. import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
2. import { Want } from '@kit.AbilityKit';

4. export default class MyFormExtensionAbility extends FormExtensionAbility {
5. onAddForm(want: Want) {
6. let formExtensionContext = this.context;
7. let dataObj1: Record<string, string> = {
8. 'temperature': '11c',
9. 'time': '11:00'
10. };
11. let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
12. return obj1;
13. }
14. }
```

[MyFormExtensionAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/extensionability/MyFormExtensionAbility.ets#L16-L31)

## Context的典型使用场景

本章节通过以下具体场景来介绍Context的用法：

* [获取基本信息](application-context-stage.md#获取基本信息)
* [获取应用文件路径](application-context-stage.md#获取应用文件路径)
* [获取和修改加密分区](application-context-stage.md#获取和修改加密分区)
* [监听应用前后台变化](application-context-stage.md#监听应用前后台变化)
* [监听UIAbility生命周期变化](application-context-stage.md#监听uiability生命周期变化)

### 获取基本信息

继承自[Context](../harmonyos-references/js-apis-inner-application-context.md)的不同类型Context，默认会继承父类的方法和属性，还会拥有自己独立的方法与属性。

通过Context属性可以获取当前应用、模块、UIAbility或ExtensionAbility的基本信息（例如资源管理对象、应用程序信息等），下面以UIAbility的信息获取为例：

如果需要跨包获取资源对象，可以参考[资源访问](resource-categories-and-access.md#资源访问)。

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. // 获取ResourceManager（资源管理）
6. let resourceManager = this.context.getApplicationContext().resourceManager;
7. // 获取applicationInfo（当前应用信息）
8. let applicationInfo = this.context.getApplicationContext().applicationInfo;
9. }
10. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/entrysceneability/EntryAbility.ets#L16-L27)

### 获取应用文件路径

[基类Context](../harmonyos-references/js-apis-inner-application-context.md)提供了获取应用文件路径的能力，[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)、[AbilityStageContext](../harmonyos-references/js-apis-inner-application-abilitystagecontext.md)、[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)和[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)均继承该能力。不同类型的Context获取的路径可能存在差异。

* 通过[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)可以获取应用级的文件路径。该路径用于存放应用全局信息，路径下的文件会跟随应用的卸载而删除。
* 通过[AbilityStageContext](../harmonyos-references/js-apis-inner-application-abilitystagecontext.md)、[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)、[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)，可以获取[Module](application-package-overview.md)级的文件路径。该路径用于存放Module相关信息，路径下的文件会跟随[HAP](hap-package.md)/[HSP](in-app-hsp.md)的卸载而删除。HAP/HSP的卸载不会影响应用级路径下的文件，除非该应用的HAP/HSP已全部卸载。

  + UIAbilityContext：可以获取UIAbility所在Module的文件路径。
  + ExtensionContext：可以获取ExtensionAbility所在Module的文件路径。
  + AbilityStageContext：由于AbilityStageContext创建时机早于UIAbilityContext和ExtensionContext，通常用于在AbilityStage中获取文件路径。

说明

应用文件路径属于应用沙箱路径，具体请参见[应用沙箱目录](app-sandbox-directory.md)。

**表1** 不同级别Context获取的应用文件路径说明

| 属性 | 说明 | ApplicationContext获取的路径 | AbilityStageContext、UIAbilityContext、ExtensionContext获取的路径 |
| --- | --- | --- | --- |
| bundleCodeDir | 安装包目录。 | <路径前缀>/el1/bundle | <路径前缀>/el1/bundle |
| cacheDir | 缓存目录。 | <路径前缀>/<加密等级>/base/cache | <路径前缀>/<加密等级>/base/**haps/<module-name>**/cache |
| filesDir | 文件目录。 | <路径前缀>/<加密等级>/base/files | <路径前缀>/<加密等级>/base/**haps/<module-name>**/files |
| preferencesDir | preferences目录。 | <路径前缀>/<加密等级>/base/preferences | <路径前缀>/<加密等级>/base/**haps/<module-name>**/preferences |
| tempDir | 临时目录。 | <路径前缀>/<加密等级>/base/temp | <路径前缀>/<加密等级>/base/**haps/<module-name>**/temp |
| databaseDir | 数据库目录。 | <路径前缀>/<加密等级>/database | <路径前缀>/<加密等级>/database/**<module-name>** |
| distributedFilesDir | 分布式文件目录。 | <路径前缀>/el2/distributedFiles | <路径前缀>/el2/distributedFiles/ |
| resourceDir11+ | 资源目录。  **说明：**  需要开发者手动在\<module-name>\resources路径下创建resfile目录。 | 不涉及 | <路径前缀>/el1/bundle/**<module-name>**/resources/resfile |
| cloudFileDir12+ | 云文件目录。 | <路径前缀>/el2/cloud | <路径前缀>/el2/cloud/ |
| logFileDir22+ | 日志文件目录。 | <路径前缀>/el2/log | <路径前缀>/el2/log/ |

本节以使用ApplicationContext获取cacheDir和filesDir为例，分别介绍如何获取应用缓存目录，以及如何获取应用文件目录，并用于新建文件和读写文件。

* **获取应用缓存目录**

  ```
  1. import { common } from '@kit.AbilityKit';

  3. @Entry
  4. @Component
  5. struct ApplicationContextCache {
  6. @State message: string = 'Hello World';
  7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  9. build() {
  10. Row() {
  11. Column() {
  12. Text(this.message)
  13. // ···
  14. Button() {
  15. Text('create file')
  16. // ···
  17. .onClick(() => {
  18. let applicationContext = this.context.getApplicationContext();
  19. // 获取应用缓存路径
  20. let cacheDir = applicationContext.cacheDir;
  21. })
  22. }
  23. // ···
  24. }
  25. // ···
  26. }
  27. // ···
  28. }
  29. }
  ```

  [ApplicationContextCache.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/ApplicationContextCache.ets#L16-L56)
* **获取应用文件目录**

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { buffer } from '@kit.ArkTS';
  3. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
  4. import { hilog } from '@kit.PerformanceAnalysisKit';

  6. const TAG: string = '[ApplicationContextFile]';
  7. const DOMAIN_NUMBER: number = 0xFF00;

  9. @Entry
  10. @Component
  11. struct ApplicationContextFile {
  12. @State message: string = 'Hello World';
  13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  15. build() {
  16. Row() {
  17. Column() {
  18. Text(this.message)
  19. // ···
  20. Button() {
  21. Text('create file')
  22. // ···
  23. .onClick(() => {
  24. let applicationContext = this.context.getApplicationContext();
  25. // 获取应用文件路径
  26. let filesDir = applicationContext.filesDir;
  27. hilog.info(DOMAIN_NUMBER, TAG, `filePath: ${filesDir}`);
  28. // 文件不存在时创建并打开文件，文件存在时打开文件
  29. let file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  30. // 写入一段内容至文件
  31. let writeLen = fileIo.writeSync(file.fd, 'Try to write str.');
  32. hilog.info(DOMAIN_NUMBER, TAG, `The length of str is: ${writeLen}`);
  33. // 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
  34. let arrayBuffer = new ArrayBuffer(1024);
  35. // 设置读取的偏移量和长度
  36. let readOptions: ReadOptions = {
  37. offset: 0,
  38. length: arrayBuffer.byteLength
  39. };
  40. // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
  41. let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
  42. // 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
  43. let buf = buffer.from(arrayBuffer, 0, readLen);
  44. hilog.info(DOMAIN_NUMBER, TAG, `the content of file: ${buf.toString()}`);
  45. // 关闭文件
  46. fileIo.closeSync(file);
  47. })
  48. }
  49. // ···
  50. }
  51. // ···
  52. }
  53. // ···
  54. }
  55. }
  ```

  [ApplicationContextFile.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/ApplicationContextFile.ets#L16-L82)

### 获取和修改加密分区

应用文件加密是一种保护数据安全的方法，可以使得文件在未经授权访问的情况下得到保护。在不同的场景下，应用需要不同程度的文件保护。

在实际应用中，开发者需要根据不同场景的需求选择合适的加密分区，从而保护应用数据的安全。通过合理使用不同级别的加密分区，可以有效提升应用数据的安全性。关于不同分区的权限说明，详见[ContextConstant](../harmonyos-references/js-apis-app-ability-contextconstant.md)的[AreaMode](../harmonyos-references/js-apis-app-ability-contextconstant.md#areamode)。

* EL1：对于私有文件，如闹铃、壁纸等，应用可以将这些文件放到设备级加密分区（EL1）中，以保证在用户输入密码前就可以被访问。
* EL2：对于更敏感的文件，如个人隐私信息等，应用可以将这些文件放到更高级别的加密分区（EL2）中，以保证更高的安全性。
* EL3：对于应用中的记录步数、文件下载、音乐播放，需要在锁屏时读写和创建新文件，放在（EL3）的加密分区比较合适。
* EL4：对于用户安全信息相关的文件，锁屏时不需要读写文件、也不能创建文件，放在（EL4）的加密分区更合适。
* EL5：对于用户隐私敏感数据文件，锁屏后默认不可读写，如果锁屏后需要读写文件，则锁屏前可以调用[acquireAccess](../harmonyos-references/js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口申请继续读写文件，或者锁屏后也需要创建新文件且可读写，放在（EL5）的应用级加密分区更合适。

要实现获取和设置当前加密分区，可以通过读写[Context](../harmonyos-references/js-apis-inner-application-context.md)的area属性来实现。

```
1. import { UIAbility, contextConstant, AbilityConstant, Want } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
5. // 存储普通信息前，切换到EL1设备级加密
6. this.context.area = contextConstant.AreaMode.EL1; // 切换area
7. // 存储普通信息

9. // 存储敏感信息前，切换到EL2用户级加密
10. this.context.area = contextConstant.AreaMode.EL2; // 切换area
11. // 存储敏感信息

13. // 存储敏感信息前，切换到EL3用户级加密
14. this.context.area = contextConstant.AreaMode.EL3; // 切换area
15. // 存储敏感信息

17. // 存储敏感信息前，切换到EL4用户级加密
18. this.context.area = contextConstant.AreaMode.EL4; // 切换area
19. // 存储敏感信息

21. // 存储敏感信息前，切换到EL5应用级加密
22. this.context.area = contextConstant.AreaMode.EL5; // 切换area
23. // 存储敏感信息
24. }
25. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/entryareaability/EntryAbility.ets#L16-L42)

```
1. // AreaContext.ets
2. import { contextConstant, common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct AreaContext {
7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

9. build() {
10. Column() {
11. // ···
12. List({ initialIndex: 0 }) {
13. // ···
14. ListItem() {
15. Row() {
16. // ···
17. }
18. .onClick(() => {
19. // 存储普通信息前，切换到EL1设备级加密
20. if (this.context.area === contextConstant.AreaMode.EL2) { // 获取area
21. this.context.area = contextConstant.AreaMode.EL1; // 修改area
22. this.getUIContext().getPromptAction().showToast({
23. message: 'SwitchToEL1'
24. });
25. }
26. // 存储普通信息
27. })
28. }
29. // ···
30. ListItem() {
31. Row() {
32. // ···
33. }
34. .onClick(() => {
35. // 存储敏感信息前，切换到EL2用户级加密
36. if (this.context.area === contextConstant.AreaMode.EL1) { // 获取area
37. this.context.area = contextConstant.AreaMode.EL2; // 修改area
38. this.getUIContext().getPromptAction().showToast({
39. message: 'SwitchToEL2'
40. });
41. }
42. // 存储敏感信息
43. })
44. }
45. // ···
46. }
47. // ···
48. }
49. // ···
50. }
51. }
```

[AreaContext.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/pages/AreaContext.ets#L16-L92)

### 监听应用前后台变化

开发者可以使用[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)的相关能力，监听应用的前后台变化。当应用前后台切换时，可以收到相应回调函数的通知，从而执行一些依赖前后台的方法，或者进行应用前后台切换频率等数据统计。

以[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)中的使用为例进行说明。

```
1. import { UIAbility, ApplicationStateChangeCallback } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = '[LifecycleAbility]';
6. const DOMAIN = 0xF811;

8. export default class LifecycleAbility extends UIAbility {
9. onCreate() {
10. let applicationStateChangeCallback: ApplicationStateChangeCallback = {
11. onApplicationForeground() {
12. hilog.info(DOMAIN, TAG, 'applicationStateChangeCallback onApplicationForeground');
13. },
14. onApplicationBackground() {
15. hilog.info(DOMAIN, TAG, 'applicationStateChangeCallback onApplicationBackground');
16. }
17. }

19. // 1.获取applicationContext
20. let applicationContext = this.context.getApplicationContext();
21. try {
22. // 2.通过applicationContext注册应用前后台状态监听
23. applicationContext.on('applicationStateChange', applicationStateChangeCallback);
24. } catch (paramError) {
25. hilog.error(DOMAIN, TAG, `error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
26. }
27. hilog.info(DOMAIN, TAG, 'Register applicationStateChangeCallback');
28. }
29. }
```

[LifecycleAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/lifecycleability/LifecycleAbility.ets#L15-L45)

### 监听UIAbility生命周期变化

开发者可以通过[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)监听UIAbility生命周期变化。当[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)生命周期变化时，如UIAbility创建、切换至前/后台、销毁等情况，UIAbility会收到相应回调函数的通知，从而执行依赖UIAbility生命周期的方法，也可以统计指定页面停留时间和访问频率等信息。

每次注册回调函数时，都会返回一个监听生命周期的ID，此ID会自增1。以[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)中的使用为例进行说明。

```
1. import { AbilityConstant, AbilityLifecycleCallback, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import  { BusinessError } from '@kit.BasicServicesKit';

6. const TAG: string = '[EntryLifecycleAbility]';
7. const DOMAIN_NUMBER: number = 0xFF00;

9. export default class EntryLifecycleAbility extends UIAbility {
10. // 定义生命周期ID
11. private lifecycleId: number = -1;

13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. // 定义生命周期回调对象
15. let abilityLifecycleCallback: AbilityLifecycleCallback = {
16. // 当UIAbility创建时被调用
17. onAbilityCreate(uiAbility) {
18. hilog.info(DOMAIN_NUMBER, TAG, `onAbilityCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
19. },
20. // 当窗口创建时被调用
21. onWindowStageCreate(uiAbility, windowStage: window.WindowStage) {
22. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageCreate uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
23. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageCreate windowStage: ${JSON.stringify(windowStage)}`);
24. },
25. // 当窗口处于活动状态时被调用
26. onWindowStageActive(uiAbility, windowStage: window.WindowStage) {
27. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageActive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
28. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageActive windowStage: ${JSON.stringify(windowStage)}`);
29. },
30. // 当窗口处于非活动状态时被调用
31. onWindowStageInactive(uiAbility, windowStage: window.WindowStage) {
32. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageInactive uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
33. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageInactive windowStage: ${JSON.stringify(windowStage)}`);
34. },
35. // 当窗口被销毁时被调用
36. onWindowStageDestroy(uiAbility, windowStage: window.WindowStage) {
37. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
38. hilog.info(DOMAIN_NUMBER, TAG, `onWindowStageDestroy windowStage: ${JSON.stringify(windowStage)}`);
39. },
40. // 当UIAbility被销毁时被调用
41. onAbilityDestroy(uiAbility) {
42. hilog.info(DOMAIN_NUMBER, TAG, `onAbilityDestroy uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
43. },
44. // 当UIAbility从后台转到前台时触发回调
45. onAbilityForeground(uiAbility) {
46. hilog.info(DOMAIN_NUMBER, TAG, `onAbilityForeground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
47. },
48. // 当UIAbility从前台转到后台时触发回调
49. onAbilityBackground(uiAbility) {
50. hilog.info(DOMAIN_NUMBER, TAG, `onAbilityBackground uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
51. },
52. // 当UIAbility迁移时被调用
53. onAbilityContinue(uiAbility) {
54. hilog.info(DOMAIN_NUMBER, TAG, `onAbilityContinue uiAbility.launchWant: ${JSON.stringify(uiAbility.launchWant)}`);
55. }
56. };
57. // 获取应用上下文
58. let applicationContext = this.context.getApplicationContext();
59. try {
60. // 注册应用内生命周期回调
61. this.lifecycleId = applicationContext.on('abilityLifecycle', abilityLifecycleCallback);
62. } catch (err) {
63. let code = (err as BusinessError).code;
64. let message = (err as BusinessError).message;
65. hilog.error(DOMAIN_NUMBER, TAG, `Failed to register applicationContext. Code is ${code}, message is ${message}`);
66. }

68. hilog.info(DOMAIN_NUMBER, TAG, `register callback number: ${this.lifecycleId}`);
69. }
70. onDestroy(): void {
71. // 获取应用上下文
72. let applicationContext = this.context.getApplicationContext();
73. try {
74. // 取消应用内生命周期回调
75. applicationContext.off('abilityLifecycle', this.lifecycleId);
76. } catch (err) {
77. let code = (err as BusinessError).code;
78. let message = (err as BusinessError).message;
79. hilog.error(DOMAIN_NUMBER, TAG, `Failed to unregister applicationContext. Code is ${code}, message is ${message}`);
80. }
81. }
82. }
```

[EntryLifecycleAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/ApplicationContextDemo/entry/src/main/ets/entrylifecycleability/EntryLifecycleAbility.ets#L16-L99)
