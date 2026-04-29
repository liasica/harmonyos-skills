---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-moduleinstall_arkts
title: 产品特性按需分发(ArkTS)
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 产品特性按需分发 > 产品特性按需分发(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d5e20f8daa23a0f85d95aaf2137dc127fc18f3dd27d34d467bd47349bc50ade
---

## 场景介绍

随着HarmonyOS应用的持续发展，应用的功能将越来越丰富，实际上80%的用户使用时长都会集中在20%的特性上，其余的功能可能也仅仅是面向部分用户。为了避免用户首次下载应用耗时过长，及过多占用用户空间，应用市场服务提供按需分发的能力，支持用户按需动态下载自己所需的增强特性。

## 基本概念

按需分发：一个应用程序被打包成多个安装包，安装包包含了所有的应用程序代码和静态资源。用户从应用市场下载的应用只包含基本功能的安装包，当用户需要使用增强功能时，相应安装包将会从服务器下载到设备上（应用发布请参考[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)）。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/2Tvnqln8Sv2JdewYV35nXg/zh-cn_image_0000002558765278.png?HW-CC-KV=V1&HW-CC-Date=20260429T053709Z&HW-CC-Expire=86400&HW-CC-Sign=09B7B120AF3D4F8F9D6E0F1867185CA493B10FB3C1A85BCB8A53D4DA447B1CDE)

1. 用户下载A应用的基础包。
2. 用户使用增强功能。
3. 应用通过API下载动态安装包。
4. 动态安装包下载完成。
5. 通过on接口告知用户下载结果。

## 约束与限制

* 应用需要上架应用市场。
* 产品特性按需分发功能支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。
* 产品特性按需分发接入调试功能支持ARM版本、X86版本的模拟器。

## 接口说明

产品特性按需分发场景提供以下ArkTS接口，具体API说明详见[接口文档](../harmonyos-references/store-moduleinstallmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [getInstalledModule](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagergetinstalledmodule)(moduleName: string): [InstalledModule](../harmonyos-references/store-moduleinstallmanager.md#installedmodule) | 查询模块安装信息接口。 |
| [createModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallprovidercreatemoduleinstallrequest)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md) | [common.ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)): [ModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallrequest) | 创建按需加载请求对象。 |
| [addModule](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallrequestaddmodule)(moduleName: string): [ReturnCode](../harmonyos-references/store-moduleinstallmanager.md#returncode) | 添加要按需加载的模块名。 |
| [fetchModules](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagerfetchmodules)(moduleInstallRequest: [ModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallrequest)): Promise<[ModuleInstallSessionState](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallsessionstate)> | 按需加载请求接口，异步返回结果。 |
| [cancelTask](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagercanceltask)(taskId: string): [ReturnCode](../harmonyos-references/store-moduleinstallmanager.md#returncode) | 取消下载任务接口。 |
| [showCellularDataConfirmation](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagershowcellulardataconfirmation)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md) | [common.ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md), taskId: string): [ReturnCode](../harmonyos-references/store-moduleinstallmanager.md#returncode) | 流量提醒弹窗接口。 |
| [on](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanageronmoduleinstallstatus)(type: 'moduleInstallStatus', callback: Callback<[ModuleInstallSessionState](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallsessionstate)>, timeout: number): void | 监听当前应用下载任务的进度。 |
| [off](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanageroffmoduleinstallstatus)(type: 'moduleInstallStatus', callback?: Callback<[ModuleInstallSessionState](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallsessionstate)>): void | 取消监听当前应用下载任务的进度。 |

## 开发步骤

### 获取模块安装信息

1. 导入moduleInstallManager模块及相关公共模块。

   ```
   1. // LoadInstallService.ets
   2. import { moduleInstallManager } from '@kit.AppGalleryKit';
   ```
2. 构造参数。

   入参为需要查询的模块名称。

   ```
   1. const moduleName: string = 'AModule';
   ```
3. 调用[getInstalledModule](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagergetinstalledmodule)方法，将步骤2中构造的参数传入模块中的getInstalledModule方法。

   ```
   1. const moduleInfo: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule(moduleName);
   ```

### 创建按需加载的请求实例

1. 导入moduleInstallManager模块及相关公共模块。

   ```
   1. // LoadInstallService.ets
   2. import { moduleInstallManager } from '@kit.AppGalleryKit';
   3. import type { common } from '@kit.AbilityKit';
   ```
2. 构造参数。

   入参为当前应用的上下文context，只支持[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)和[ExtensionContext](../harmonyos-references/js-apis-inner-application-extensioncontext.md)类型的上下文，其中UIAbilityContext类型的上下文是要校验当前应用是否在前台，如果不在前台，则会被拒绝调用。

   ```
   1. const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   ```
3. 调用[createModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallprovidercreatemoduleinstallrequest)方法，将步骤2中构造的参数依次传入模块中的createModuleInstallRequest方法。

   ```
   1. const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider = new moduleInstallManager.ModuleInstallProvider();
   2. const myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest = myModuleInstallProvider.createModuleInstallRequest(context);
   ```

### 请求按需加载模块

1. 导入moduleInstallManager模块及相关公共模块。

   ```
   1. // LoadInstallService.ets
   2. import type { common } from '@kit.AbilityKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { moduleInstallManager } from '@kit.AppGalleryKit';
   ```
2. 构造参数。

   入参为当前要按需加载的模块名。

   ```
   1. const moduleNameA: string = 'AModule';
   2. const moduleNameB: string = 'BModule';
   ```
3. 调用[ModuleInstallRequest](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallrequest)中的[addModule](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallrequestaddmodule)方法，将步骤2中构造的参数依次传入模块中的addModule方法。

   ```
   1. let myModuleInstallRequest: moduleInstallManager.ModuleInstallRequest;
   2. try {
   3. const myModuleInstallProvider: moduleInstallManager.ModuleInstallProvider = new moduleInstallManager.ModuleInstallProvider();
   4. const context: common.UIAbilityContext | common.ExtensionContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   5. myModuleInstallRequest = myModuleInstallProvider.createModuleInstallRequest(context);
   6. const aResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule(moduleNameA);
   7. const bResult: moduleInstallManager.ReturnCode = myModuleInstallRequest.addModule(moduleNameB);
   8. hilog.info(0, 'TAG', 'aResult:' + aResult + ' bResult:' + bResult);
   9. } catch (error) {
   10. hilog.error(0, 'TAG', `addModule onError.code is ${error.code}, message is ${error.message}`);
   11. }
   ```
4. 调用[fetchModules](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagerfetchmodules)方法，将步骤3中的myModuleInstallRequest传入模块中的fetchModules方法。

   ```
   1. try {
   2. moduleInstallManager.fetchModules(myModuleInstallRequest)
   3. .then(() => {
   4. hilog.info(0, 'TAG', 'Succeeded in fetching Modules data.');
   5. })
   6. } catch (error) {
   7. hilog.error(0, 'TAG', `fetching Modules onError.code is ${error.code}, message is ${error.message}`);
   8. }
   ```

### 使用动态模块

假如应用A由entry.hap、AModulelib.hsp两个包组成，其中entry是基础包，AModulelib扩展是功能包（创建方式请参考[应用程序包开发与使用](application-package-dev.md)）。通过应用市场下载安装只会下载安装entry包，在entry包里面可以通过[fetchModules](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagerfetchmodules)接口动态下载AModulelib包，并使用[动态import](arkts-dynamic-import.md)技术调用AModulelib里的方法和组件。

AModulelib中主要实现如下：

* 在动态模块AModulelib的module.json5中设置deliveryWithInstall为false，来标识当前AModulelib在用户主动安装应用A的时候不会一起下载安装。

  ```
  1. {
  2. "module": {
  3. "name": "AModulelib",
  4. "deliveryWithInstall": false
  5. }
  6. }
  ```
* 在动态模块AModulelib中定义add方法和DateComponent组件。其中add方法用于计算加法，DateComponent用于显示文本。

  Calc.ets定义如下：

  ```
  1. export function add(a:number, b:number) {
  2. return a + b;
  3. }
  ```

  DateComponent.ets定义如下：

  ```
  1. @Component
  2. struct DateComponent {
  3. build() {
  4. Column() {
  5. Text('我是AModulelib中的组件')
  6. .margin(10);
  7. }
  8. .width(300).backgroundColor(Color.Yellow);
  9. }
  10. }

  12. @Builder
  13. export function showDateComponent() {
  14. DateComponent()
  15. }
  ```
* 在AModulelib的AModulelib/Index.ets中导出add方法和showDateComponent方法。

  ```
  1. export { add } from './src/main/ets/utils/Calc';
  2. export { showDateComponent } from './src/main/ets/components/DateComponent';
  ```

entry中主要实现如下：

* 在entry基础模块中，增加动态依赖配置。entry的oh-package.json5中使用dynamicDependencies来动态依赖AModulelib模块。

  ```
  1. {
  2. "dynamicDependencies": {
  3. "AModulelib": "file:../AModulelib"
  4. }
  5. }
  ```
* 在entry中使用动态模块AModulelib模块里面的方法和组件。在调用AModulelib中的功能前需要判断AModulelib是否已经加载，未加载时请参考[请求按需加载的接口](store-moduleinstall_arkts.md#请求按需加载模块)完成加载。

  ```
  1. import { moduleInstallManager } from '@kit.AppGalleryKit';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import { BusinessError, Callback } from '@kit.BasicServicesKit';
  4. import { common } from '@kit.AbilityKit';

  6. @Entry
  7. @Component
  8. struct Index {
  9. @BuilderParam AModulelibComponent: Function;
  10. @State countTotal: number = 0;
  11. @State isShow: boolean = false;

  13. build() {
  14. Row() {
  15. Column() {
  16. Button(`调用增量模块中的add功能:3+6`)
  17. .onClick(() => {
  18. this.initAModulelib(() => {
  19. import('AModulelib').then((ns: ESObject) => {
  20. this.countTotal = ns.add(3, 6);
  21. }).catch((error: BusinessError) => {
  22. hilog.error(0, 'TAG', `add onError.code is ${error.code}, message is ${error.message}`);
  23. })
  24. })
  25. });
  26. Text('计算结果：' + this.countTotal)
  27. .margin(10);
  28. Button(`调用增量模块中的showDateComponent功能`)
  29. .onClick(() => {
  30. this.initAModulelib(() => {
  31. import('AModulelib').then((ns: ESObject) => {
  32. this.AModulelibComponent = ns.showDateComponent;
  33. this.isShow = true;
  34. }).catch((error: BusinessError) => {
  35. hilog.error(0, 'TAG', `showDateComponent onError.code is ${error.code}, message is ${error.message}`);
  36. })
  37. })
  38. }).margin({
  39. top: 10, bottom: 10
  40. });
  41. if (this.isShow) {
  42. this.AModulelibComponent()
  43. }
  44. }
  45. .width('100%')
  46. }
  47. .height('100%')
  48. }

  50. private showToastInfo(msg: string) {
  51. this.getUIContext().getPromptAction().showToast({
  52. message: msg,
  53. duration: 2000
  54. });
  55. }

  57. /**
  58. * 检查是否已加载AModulelib包
  59. *
  60. * @param successCallBack 回调
  61. */
  62. private initAModulelib(successCallBack: Callback<void>): void {
  63. try {
  64. const result: moduleInstallManager.InstalledModule = moduleInstallManager.getInstalledModule('AModulelib');
  65. if (result?.installStatus === moduleInstallManager.InstallStatus.INSTALLED) {
  66. hilog.info(0, 'TAG', 'AModulelib installed');
  67. successCallBack && successCallBack();
  68. } else {
  69. // AModulelib模块未安装, 需要调用fetchModules下载AModulelib模块
  70. hilog.info(0, 'TAG', 'AModulelib not installed');
  71. this.fetchModule('AModulelib', successCallBack)
  72. }
  73. } catch (error) {
  74. hilog.error(0, 'TAG', `getInstalledModule onError.code is ${error.code}, message is ${error.message}`);
  75. }
  76. }

  78. /**
  79. * 添加监听事件
  80. *
  81. * @param successCallBack 回调
  82. */
  83. private onListenEvents(successCallBack: Callback<void>): void {
  84. const timeout = 3 * 60; // 单位秒， 默认最大监听时间为30min（即30*60秒）
  85. moduleInstallManager.on('moduleInstallStatus', (data: moduleInstallManager.ModuleInstallSessionState) => {
  86. // 返回成功
  87. if (data.taskStatus === moduleInstallManager.TaskStatus.INSTALL_SUCCESSFUL) {
  88. successCallBack && successCallBack();
  89. this.showToastInfo('install success');
  90. }
  91. }, timeout)
  92. }

  94. /**
  95. * 加载指定包
  96. *
  97. * @param moduleName 需要加载的安装包名称
  98. * @param successCallBack 回调
  99. */
  100. private fetchModule(moduleName: string, successCallBack: Callback<void>) {
  101. try {
  102. hilog.info(0, 'TAG', 'handleFetchModules start');
  103. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  104. const moduleInstallProvider: moduleInstallManager.ModuleInstallProvider =
  105. new moduleInstallManager.ModuleInstallProvider();
  106. const moduleInstallRequest: moduleInstallManager.ModuleInstallRequest =
  107. moduleInstallProvider.createModuleInstallRequest(context);
  108. if (!moduleInstallRequest) {
  109. hilog.warn(0, 'TAG', 'moduleInstallRequest is empty');
  110. return;
  111. }
  112. moduleInstallRequest.addModule(moduleName);
  113. moduleInstallManager.fetchModules(moduleInstallRequest)
  114. .then((data: moduleInstallManager.ModuleInstallSessionState) => {
  115. hilog.info(0, 'TAG', 'Succeeded in fetching Modules result.');
  116. if (data.code === moduleInstallManager.RequestErrorCode.SUCCESS) {
  117. this.onListenEvents(successCallBack)
  118. } else {
  119. hilog.info(0, 'TAG', 'fetchModules failure');
  120. }
  121. })
  122. .catch((error: BusinessError) => {
  123. hilog.error(0, 'TAG', `fetchModules onError.code is ${error.code}, message is ${error.message}`);
  124. })
  125. } catch (error) {
  126. hilog.error(0, 'TAG', `handleFetchModules onError.code is ${error.code}, message is ${error.message}`);
  127. }
  128. }
  129. }
  ```

运行结果效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/eNT1mk4_SsmdkTUHFngx6g/zh-cn_image_0000002558605622.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053709Z&HW-CC-Expire=86400&HW-CC-Sign=09C964C0DAA4635FEA3F89394815C394D4A3A9AF73EF652B88A447B981553ADD)

### 接入调试功能

产品特性按需分发为开发者提供接入调试功能，支持开发者在接入过程中进行调试，应用无需上架应用市场。假如应用A由entry.hap、AModulelib.hsp两个包组成，其中entry是基础包，AModulelib是扩展功能包（创建方式请参考[应用程序包开发与使用](hap-package.md)）。

1. 使用[调试证书签名](ide-signing.md)应用/服务，本地编译构建出entry.hap、AModulelib.hsp，可通过[HDC命令安装](hdc.md#hdc命令列表)或DevEco Studio直接安装基础包。

   ```
   1. hdc install entry.hap
   ```
2. 打开[开发者调试模式](ide-developer-mode.md#section530763213432)：进入设置 -> 机型 -> 关于手机，连续点击软件版本7次，弹出“开启“开发者模式””，点击“确认开启”。
3. [访问设备沙箱路径](ide-device-file-explorer.md#section48216711204)，在[应用el2级别加密数据目录](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)下，创建cache/moduleinstall/<ModuleName>目录（这里<ModuleName>是AModulelib），将模块调试包AModulelib.hsp上传至对应模块目录下（请确保模块调试包文件应有读写权限）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/-7QqDmlcRe2CYap-BYhxTw/zh-cn_image_0000002589325149.png?HW-CC-KV=V1&HW-CC-Date=20260429T053709Z&HW-CC-Expire=86400&HW-CC-Sign=7D7773AB2114292707545AC46222912A5E491E776E149D7AD1A8E2789BE6BE11)
4. 按照[创建按需加载的请求实例](store-moduleinstall_arkts.md#创建按需加载的请求实例)、[请求按需加载的接口](store-moduleinstall_arkts.md#请求按需加载模块)或[使用动态模块](store-moduleinstall_arkts.md#使用动态模块)，无需改动参数即可安装好模块调试包。监听到安装成功后，对应模块目录下的文件会被自动删除。
