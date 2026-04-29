---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/embeddeduiextensionability
title: EmbeddedUIExtensionAbility
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > Stage模型应用组件 > ExtensionAbility组件 > EmbeddedUIExtensionAbility
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a92168dea218eafcdd48618cf36bc1187f62f96e0478f1f57a478cc4027edbd9
---

## 概述

[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)是EMBEDDED\_UI类型的[ExtensionAbility](../harmonyos-references/js-apis-app-ability-extensionability.md)组件，提供了跨进程界面嵌入的能力。

EmbeddedUIExtensionAbility需要和[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)一起配合使用，开发者可以在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的页面中通过EmbeddedComponent嵌入本应用的EmbeddedUIExtensionAbility提供的UI。EmbeddedUIExtensionAbility在独立进程中运行，完成其页面的布局和渲染，与UIAbility数据不互通，适用于有进程隔离诉求的模块化开发场景。

在下面的示例中，UIAbility运行在主进程，其中包含多个EmbeddedComponent。每个EmbeddedComponent对应一个EmbeddedUIExtensionAbility。多个EmbeddedUIExtensionAbility可以分别用于实现办公软件中的文档、表格、演示文件。

**图1** EmbeddedUIExtensionAbility示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/uALyDLpLTKOLBoEzJ1YS9A/zh-cn_image_0000002558604328.png?HW-CC-KV=V1&HW-CC-Date=20260429T052544Z&HW-CC-Expire=86400&HW-CC-Sign=CCDFD844898650BF1FC5F238B6311BD726DA7E7C34A8406CB5BFA4CA4A6AAA3F)

## 约束限制

当前EmbeddedUIExtensionAbility和EmbeddedComponent仅支持在拥有多进程配置的设备上使用，目前支持多进程配置的设备有2in1与Tablet。

## 生命周期

[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)提供了onCreate、onSessionCreate、onSessionDestroy、onForeground、onBackground和onDestroy生命周期回调，根据需要重写对应的回调方法。以下生命周期回调均继承自[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)。

* **onCreate**：当EmbeddedUIExtensionAbility创建时回调，执行初始化业务逻辑操作。
* **onSessionCreate**：当EmbeddedUIExtensionAbility界面内容对象创建后调用。
* **onSessionDestroy**：当EmbeddedUIExtensionAbility界面内容对象销毁后调用。
* **onForeground**：当EmbeddedUIExtensionAbility从后台转到前台时触发。
* **onBackground**：当EmbeddedUIExtensionAbility从前台转到后台时触发。
* **onDestroy**：当EmbeddedUIExtensionAbility销毁时回调，可以执行资源清理等操作。

说明

EmbeddedComponent只能在UIAbility中使用，且被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。

EmbeddedUIExtensionAbility支持应用分身，被拉起的EmbeddedUIExtensionAbility与UIAbility属于同一分身应用。

EmbeddedUIExtensionAbility通过[UIExtensionContext](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md)和[UIExtensionContentSession](../harmonyos-references/js-apis-app-ability-uiextensioncontentsession.md)提供相关能力。本文描述中称被启动的EmbeddedUIExtensionAbility为提供方，称启动EmbeddedUIExtensionAbility的EmbeddedComponent组件为使用方。

## 开发EmbeddedUIExtensionAbility提供方

开发者在实现一个[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)提供方时，需要在DevEco Studio工程中手动新建一个EmbeddedUIExtensionAbility，具体步骤如下。

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为embeddeduiextability。
2. 在embeddeduiextability目录，右键选择“New > File”，新建一个.ets文件并命名为EmbeddedUIExtAbility.ets。
3. 打开EmbeddedUIExtAbility.ets文件，导入EmbeddedUIExtensionAbility的依赖包，自定义类继承EmbeddedUIExtensionAbility并实现onCreate、onSessionCreate、onSessionDestroy、onForeground、onBackground和onDestroy生命周期回调。

   ```
   1. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';

   3. const TAG: string = '[EmbeddedUIExtAbility]';

   5. export default class EmbeddedUIExtAbility extends EmbeddedUIExtensionAbility {
   6. onCreate() {
   7. console.info(TAG, `onCreate`);
   8. }

   10. onForeground() {
   11. console.info(TAG, `onForeground`);
   12. }

   14. onBackground() {
   15. console.info(TAG, `onBackground`);
   16. }

   18. onDestroy() {
   19. console.info(TAG, `onDestroy`);
   20. }

   22. onSessionCreate(want: Want, session: UIExtensionContentSession) {
   23. console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
   24. let param: Record<string, UIExtensionContentSession> = {
   25. 'session': session
   26. };
   27. let storage: LocalStorage = new LocalStorage(param);
   28. session.loadContent('pages/extension', storage);
   29. }

   31. onSessionDestroy(session: UIExtensionContentSession) {
   32. console.info(TAG, `onSessionDestroy`);
   33. }
   34. }
   ```

   [EmbeddedUIExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/EmbeddedUIExtensionAbility/entry/src/main/ets/embeddeduiextability/EmbeddedUIExtAbility.ets#L16-L51)
4. EmbeddedUIExtensionAbility的onSessionCreate中加载了入口页面文件pages/extension.ets内容如下：

   ```
   1. import { UIExtensionContentSession } from '@kit.AbilityKit';

   3. @Entry()
   4. @Component
   5. struct Extension {
   6. @State message: string = 'EmbeddedUIExtensionAbility Index';
   7. localStorage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
   8. private session: UIExtensionContentSession | undefined = this.localStorage?.get<UIExtensionContentSession>('session');

   10. build() {
   11. Column() {
   12. Text(this.message)
   13. .fontSize(20)
   14. .fontWeight(FontWeight.Bold)
   15. Button('terminateSelfWithResult').fontSize(20).onClick(() => {
   16. this.session?.terminateSelfWithResult({
   17. resultCode: 1,
   18. want: {
   19. bundleName: 'com.samples.embeddeduiextensionability',
   20. abilityName: 'ExampleEmbeddedAbility'
   21. }});
   22. })
   23. }.width('100%').height('100%')
   24. }
   25. }
   ```

   [Extension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/EmbeddedUIExtensionAbility/entry/src/main/ets/pages/Extension.ets#L16-L42)
5. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册EmbeddedUIExtensionAbility，type标签需要设置为“embeddedUI”，srcEntry标签表示当前EmbeddedUIExtensionAbility组件所对应的代码路径。

   ```
   1. {
   2. "module": {
   3. // ···
   4. "extensionAbilities": [
   5. // ···
   6. {
   7. "name": "EmbeddedUIExtAbility",
   8. "icon": "$media:startIcon",
   9. "description": "EmbeddedUIExtAbility",
   10. "type": "embeddedUI",
   11. "srcEntry": "./ets/embeddeduiextability/EmbeddedUIExtAbility.ets"
   12. }
   13. ]
   14. }
   15. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/EmbeddedUIExtensionAbility/entry/src/main/module.json5#L15-L78)

## 开发EmbeddedUIExtensionAbility使用方

开发者可以在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的页面中通过[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)容器加载自己应用内的[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)。此外，EmbeddedUIExtensionAbility在[want](../harmonyos-references/js-apis-app-ability-want.md).parameters中新增了两个字段ohos.extension.processMode.hostSpecified和ohos.extension.processMode.hostInstance。

* ohos.extension.processMode.hostSpecified控制非首次启动的EmbeddedUIExtensionAbility是否运行在同[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md)的进程中，参数是进程名称。例如，"ohos.extension.processMode.hostSpecified"： "com.ohos.inentexecutedemo:embeddedUI"。
* ohos.extension.processMode.hostInstance控制启动的EmbeddedUIExtensionAbility是否按照独立进程启动，传入false时，按照UIExtensionAbility的进程模型启动，入参true的时候，不管被拉起的UIExtensionAbility配置的是什么进程模型，都会新增一个进程，例如，"ohos.extension.processMode.hostInstance": "true"。

ohos.extension.processMode.hostSpecified和ohos.extension.processMode.hostInstance同时配置时，hostSpecified优先，会运行在指定的进程中。

如在首页文件：pages/Index.ets中添加如下内容：

```
1. import { Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct BasicClass {
7. @State message: string = 'Message: ';
8. private want: Want = {
9. bundleName: 'com.samples.embeddeduiextensionability',
10. abilityName: 'EmbeddedUIExtAbility',
11. parameters: {
12. 'ohos.extension.processMode.hostInstance': 'true'
13. }
14. };

16. build() {
17. Row() {
18. Column() {
19. Text(this.message).fontSize(30)
20. EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
21. .width('100%')
22. .height('90%')
23. .onTerminated((info: TerminationInfo) => {
24. this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
25. })
26. .onError((error: BusinessError) => {
27. this.message = 'Error: code = ' + error.code;
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

[BasicClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Ability/EmbeddedUIExtensionAbility/entry/src/main/ets/pages/BasicClass.ets#L16-L51)
