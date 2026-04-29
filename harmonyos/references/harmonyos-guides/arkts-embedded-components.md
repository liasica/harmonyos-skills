---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-embedded-components
title: 同应用进程嵌入式组件 (EmbeddedComponent)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > UI系统场景化能力 > 嵌入式组件 > 同应用进程嵌入式组件 (EmbeddedComponent)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48baaf204f098d66857a036d0ea01d73112897763122f4ce83fcc666926f334f
---

EmbeddedComponent组件允许当前页面嵌入同一应用内其他EmbeddedUIExtensionAbility供给的UI内容，这些UI运行在独立进程中，提供更高的安全性和稳定性。

EmbeddedComponent组件主要用于实现跨模块、跨进程的嵌入式界面集成，其核心目标是通过模块化设计提升应用的灵活性和用户体验。

开发者在使用时需注意其使用限制和生命周期管理，合理设计应用架构以最大限度地发挥其优势。

## 基本概念

* [EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)组件

  EmbeddedComponent组件用于在当前页面嵌入本应用内其他EmbeddedUIExtensionAbility提供的UI。它允许开发者将应用的某些功能或界面嵌入另一个界面中，实现更灵活的用户界面设计，适用于需要进程隔离的模块化开发场景。
* [EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)组件

  提供方应用中定义使用，用于实现跨进程界面嵌入功能，仅能被同应用的UIAbility拉起，并需在多进程权限的场景下使用。

## 使用约束

* 设备要求

  EmbeddedComponent组件仅可在支持[EmbeddedUIExtensionAbility](../harmonyos-references/js-apis-app-ability-embeddeduiextensionability.md)的设备上正常运行。
* 应用范围

  EmbeddedComponent组件只能在UIAbility中使用，且被拉起的EmbeddedUIExtensionAbility需与UIAbility属于同一应用。
* 属性限制

  EmbeddedComponent组件支持[通用属性](../harmonyos-references/ts-component-general-attributes.md)，且宽高默认值和最小值均为10vp；

  不支持如下与宽高相关的属性：

  "constraintSize"、"aspectRatio"、"layoutWeight"、"flexBasis"、"flexGrow"和"flexShrink"。
* 事件调用

  与屏幕坐标相关的事件信息会基于EmbeddedComponent的位置宽高进行坐标转换后传递给被拉起的EmbeddedUIExtensionAbility处理。

  EmbeddedComponent组件不支持[点击](../harmonyos-references/ts-universal-events-click.md)等通用事件，仅支持[onTerminated](../harmonyos-references/ts-container-embedded-component.md#onterminated)事件和[onError](../harmonyos-references/ts-container-embedded-component.md#onerror)事件。

## 场景示例

该示例简单展示了EmbeddedComponent组件和EmbeddedUIExtensionAbility的基础使用方式。

**加载项首页**

加载项首页是EmbeddedComponent组件的宿主页面，负责加载和展示嵌入式UI扩展能力的内容。以下是一个完整的加载项首页实现示例：

```
1. import { Want } from '@kit.AbilityKit';

3. @Component
4. export struct Embedded {
5. @State message: string = 'Message: ';
6. private want: Want = {
7. bundleName: 'com.samples.uiextensionandaccessibility',
8. abilityName: 'ExampleEmbeddedAbility',
9. };
10. build() {
11. // ...
12. Row() {
13. Column() {
14. Text(this.message).fontSize(30)
15. EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
16. .width('100%')
17. .height('90%')
18. .onTerminated((info) => {
19. // 点击extension页面内的terminateSelfWithResult按钮后触发onTerminated回调，文本框显示如下信息
20. this.message = `Termination: code = ${info.code} , want = ${JSON.stringify(info.want)}`;
21. })
22. .onError((error) => {
23. // 失败或异常触发onError回调，文本框显示如下报错内容
24. this.message = `Error: code = ${error.code}`;
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. // ...
31. }
32. }
```

[Embedded.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/UIExtensionAndAccessibility/entry/src/main/ets/pages/EmbeddedComponent/Embedded.ets#L16-L56)

在ArkTS项目中，EmbeddedUIExtensionAbility的实现代码通常位于项目的ets/extensionAbility目录下。例如，ExampleEmbeddedAbility.ets文件位于./ets/extensionAbility/目录中。

在实现加载项首页时，开发者需要注意以下几点：

* 多进程模型检测

  在应用启动时，建议检测设备是否已开启多进程模型。如果未开启，应提供明确的错误提示或引导用户开启。
* 异常处理

  通过[onError](../harmonyos-references/ts-container-embedded-component.md#onerror)事件处理加载或运行嵌入式能力时可能出现的错误，提升用户体验。
* 生命周期管理

  了解并管理好嵌入式组件的生命周期，确保资源的正确释放和回收。
* 样式配置

  合理配置EmbeddedComponent组件的大小和位置，确保嵌入式界面能够以期望的尺寸和位置显示。

**提供方应用生命周期实现**

提供方应用是指提供嵌入式UI扩展能力的应用。以下是提供方应用生命周期实现的代码示例：

```
1. import { EmbeddedUIExtensionAbility, UIExtensionContentSession, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[ExampleEmbeddedAbility]'

6. export default class ExampleEmbeddedAbility extends EmbeddedUIExtensionAbility {
7. onCreate() {
8. hilog.info(0x0000, TAG, '%{public}s', `onCreate`);
9. }

11. onForeground() {
12. hilog.info(0x0000, TAG, '%{public}s',  `onForeground`);
13. }

15. onBackground() {
16. hilog.info(0x0000, TAG, '%{public}s', `onBackground`);
17. }

19. onDestroy() {
20. hilog.info(0x0000, TAG, '%{public}s', `onDestroy`);
21. }

23. onSessionCreate(want: Want, session: UIExtensionContentSession) {
24. hilog.info(0x0000, TAG , '%{public}s', `onSessionCreate, want: ${JSON.stringify(want)}`);
25. let param: Record<string, UIExtensionContentSession> = {
26. 'session': session
27. };
28. let storage: LocalStorage = new LocalStorage(param);
29. // 加载 Extension.ets 页面内容
30. session.loadContent('pages/EmbeddedComponent/Extension', storage);
31. }

33. onSessionDestroy(session: UIExtensionContentSession) {
34. hilog.info(0x0000, TAG , '%{public}s',  `onSessionDestroy`);
35. }
36. }
```

[ExampleEmbeddedAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/UIExtensionAndAccessibility/entry/src/main/ets/extensionability/ExampleEmbeddedAbility.ets#L15-L52)

关键实现说明：

* 生命周期阶段

  onCreate → onForeground：组件初始化到可见的完整流程；

  onBackground → onForeground：前后台切换时的状态迁移；

  onDestroy：组件被宿主主动销毁时的资源回收点。
* 会话管理

  onSessionCreate：创建独立存储上下文并加载UI界面；

  onSessionDestroy：处理会话结束时（如用户主动关闭）的清理操作。
* 上下文传递

  通过LocalStorage实现UIExtensionContentSession的跨组件传递；

  使用loadContent方法绑定ArkTS页面与扩展能力上下文。

**入口页面**

以下提供方应用的入口组件实现，展示了如何使用UIExtensionContentSession会话以及如何通过按钮点击事件退出嵌入式页面并返回结果，该代码文件需要在main\_pages.json配置文件中声明使用。

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';

3. @Entry()
4. @Component
5. struct Extension {
6. @State message: string = 'EmbeddedUIExtensionAbility Index';
7. private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
8. private session: UIExtensionContentSession | undefined = this.storage?.get<UIExtensionContentSession>('session');

10. build() {
11. Column() {
12. Text(this.message)
13. .fontSize(20)
14. .fontWeight(FontWeight.Bold)
15. Button('terminateSelfWithResult').fontSize(20).onClick(() => {
16. // 点击按钮后调用terminateSelfWithResult退出
17. this.session?.terminateSelfWithResult({
18. resultCode: 1,
19. want: {
20. bundleName: 'com.samples.uiextensionandaccessibility',
21. abilityName: 'ExampleEmbeddedAbility',
22. }
23. });
24. })
25. }.width('100%').height('100%')
26. }
27. }
```

[Extension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/UIExtensionAndAccessibility/entry/src/main/ets/pages/EmbeddedComponent/Extension.ets#L16-L45)

在实现入口页面时，开发者需要注意以下几点：

1. 会话管理

   正确获取并使用UIExtensionContentSession会话对象，确保与宿主应用的通信正常。
2. 结果返回

   通过terminateSelfWithResult方法向宿主应用返回结果时，需要指定：

   * resultCode：结果代码；
   * want：目标意图，指定结果的接收方。
3. 页面生命周期

   了解并管理好入口页面的生命周期，确保资源的正确释放和回收。
4. 样式配置

   合理配置页面元素的样式，确保界面显示效果符合预期。

**添加配置项**

为了使嵌入式UI扩展能力正常工作，需要在应用的配置文件中进行相应的设置。

在module.json5配置文件的"extensionAbilities"标签下增加ExampleEmbeddedAbility配置，以注册ExampleEmbeddedAbility嵌入式UI扩展能力。

```
1. {
2. "name": "ExampleEmbeddedAbility",
3. "srcEntry": "./ets/extensionability/ExampleEmbeddedAbility.ets",
4. "type": "embeddedUI"
5. },
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/UIExtensionAndAccessibility/entry/src/main/module.json5#L64-L70)

**预期效果**

1. 在支持EmbeddedUIExtensionAbility的设备上启动应用；

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/EfwdVj9uRsuoojdFlibtcA/zh-cn_image_0000002589324419.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052826Z&HW-CC-Expire=86400&HW-CC-Sign=2820B926F05F4FB0CF6E5648539433569B92E9E77EFEF08E7F79BB0A417638B7)
2. 点击terminateSelfWithResult按钮，提供方内容消失，页面显示onTerminated信息。
