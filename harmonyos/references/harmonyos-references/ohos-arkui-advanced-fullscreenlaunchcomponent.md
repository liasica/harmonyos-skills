---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-fullscreenlaunchcomponent
title: FullScreenLaunchComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FullScreenLaunchComponent
category: harmonyos-references
scraped_at: 2026-04-28T08:02:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:463369e95d6bf343c381312eda5faf15c42edcebf3164ab3af174cd34219ef04
---

全屏启动元服务组件，当被拉起方授权使用方可以嵌入式运行元服务时，使用方全屏嵌入式运行元服务；未授权时，使用方跳出式拉起元服务。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件不支持在Wearable设备上使用。

如果需要在该组件中实现可嵌入式运行的元服务，必须继承自[EmbeddableUIAbility](js-apis-app-ability-embeddableuiability.md)。否则，系统无法保证元服务功能正常。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FullScreenLaunchComponent } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## FullScreenLaunchComponent

PhonePC/2in1TabletTVWearable

FullScreenLaunchComponent({ content: Callback<void>, appId: string, options?: AtomicServiceOptions, onError?: ErrorCallback, onTerminated?: Callback<TerminationInfo> })

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| content | Callback<void> | 是 | @BuilderParam | 可以使用组件组合来自定义拉起元服务前的占位图标，实现类似大桌面应用图标的效果。点击占位组件后，将拉起元服务。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| appId | string | 是 | - | 需要拉起的元服务appId，appId是元服务的唯一标识。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。可在应用市场元服务一栏找到需要使用的元服务，在元服务隐私声明内找到对应元服务开发者的联系方式，联系对应元服务开发者获取。 |
| options | [AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md) | 否 | - | 拉起元服务参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onError18+ | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | - | 被拉起的嵌入式运行元服务在运行过程中发生异常时触发本回调。可通过回调参数中的code、name和message获取错误信息并做处理。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onTerminated18+ | [Callback](js-apis-base.md#callback)<[TerminationInfo](ts-container-embedded-component.md#terminationinfo)> | 否 | - | 被拉起的嵌入式运行元服务通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)或者[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)正常退出时，触发本回调函数。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| onReceive20+ | [Callback](js-apis-base.md#callback)<Record<string, Object>> | 否 | - | 被拉起的嵌入式运行元服务通过[Window](../harmonyos-guides/application-window-stage.md)调用API时，触发本回调。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

说明

* 若元服务通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)退出，其携带的信息会传给回调函数的入参；
* 若元服务通过调用[terminateSelf](js-apis-inner-application-uiabilitycontext.md#terminateself)退出，上述回调函数的入参中，"code"取默认值"0"，"want"为"undefined"。

## 示例

PhonePC/2in1TabletTVWearable

本示例展示组件使用方法和扩展的元服务。实际运行时请使用开发者自己的元服务appId。

FullScreenLaunchComponent组件需要由使用方调用。在提供方完成本地的安装后，即可实现在使用方应用或者元服务中全屏嵌入式拉起提供方的效果。

**使用方**

```
1. // 使用方入口界面Index.ets内容如下:
2. import { FullScreenLaunchComponent } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State appId: string = '6917573653426122083'; // 元服务appId

9. build() {
10. Row() {
11. Column() {
12. FullScreenLaunchComponent({
13. content: ColumnChild,
14. appId: this.appId,
15. options: {},
16. onTerminated: (info) => {
17. console.info(`onTerminated code: ${info.code.toString()}`);
18. },
19. onError: (err) => {
20. console.error(`onError code: ${err.code}, message: ${err.message}`);
21. },
22. onReceive: (data) => {
23. console.info(`onReceive, data: ${JSON.stringify(data)}`);
24. }
25. }).width("80vp").height("80vp")
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }

33. @Builder
34. function ColumnChild() {
35. Column() {
36. Image($r('app.media.startIcon'))
37. Text('test')
38. }
39. }
```

**组件提供方**

元服务提供方需要修改两个文件：

* 提供方入口文件：/src/main/ets/entryability/EntryAbility.ets。

```
1. import { AbilityConstant, Want, EmbeddableUIAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const DOMAIN = 0x0000;

7. export default class EntryAbility extends EmbeddableUIAbility {
8. storage = new LocalStorage();
9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
11. }

13. onDestroy(): void {
14. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
15. }

17. onWindowStageCreate(windowStage: window.WindowStage): void {
18. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
19. let mainWindow = windowStage.getMainWindowSync()
20. this.storage.setOrCreate("window", mainWindow)
21. this.storage.setOrCreate("windowStage", windowStage)
22. windowStage.loadContent('pages/Index', this.storage);
23. }

25. onWindowStageDestroy(): void {
26. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
27. }

29. onForeground(): void {
30. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
31. }

33. onBackground(): void {
34. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
35. }
36. }
```

* 提供方扩展Ability入口页面文件：/src/main/ets/pages/Index.ets。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { window } from '@kit.ArkUI';

4. const DOMAIN = 0x0000;

6. @Entry
7. @Component
8. struct Index {
9. private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();

11. build() {
12. Row() {
13. Column() {
14. GridRow({ columns: 2 }) {
15. GridCol() {
16. Button("setWindowSystemBar")
17. .onClick(() => {
18. this.testSetSystemBarEnable()
19. }).width(120)
20. }.height(60)

22. GridCol() {
23. Button("setGestureBack")
24. .onClick(() => {
25. this.testSetGestureBackEnable()
26. }).width(120)
27. }.height(60)

29. GridCol() {
30. Button("setImmersive")
31. .onClick(() => {
32. this.testSetImmersiveEnable()
33. }).width(120)
34. }.height(60)

36. GridCol() {
37. Button("setSpecificSystemBarEnabled")
38. .onClick(() => {
39. this.testSetSpecificSystemBarEnabled()
40. }).width(120)
41. }.height(60)
42. }
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }

49. testSetSystemBarEnable() {
50. let window: window.Window | undefined = this.storage?.get("window");
51. let p = window?.setWindowSystemBarEnable(["status"])
52. p?.then(() => {
53. console.info('setWindowSystemBarEnable success');
54. }).catch((err: BusinessError) => {
55. console.error(`setWindowSystemBarEnable failed, error = ${JSON.stringify(err)}`);
56. })
57. }

59. testSetGestureBackEnable() {
60. let window: window.Window | undefined = this.storage?.get("window");
61. let p = window?.setGestureBackEnabled(true)
62. p?.then(() => {
63. console.info('setGestureBackEnabled success');
64. }).catch((err: BusinessError) => {
65. console.error(`setGestureBackEnabled failed, error = ${JSON.stringify(err)}`);
66. })
67. }

69. testSetImmersiveEnable() {
70. let window: window.Window | undefined = this.storage?.get("window");
71. try {
72. window?.setImmersiveModeEnabledState(true)
73. } catch (err) {
74. console.error(`setImmersiveModeEnabledState failed, error = ${JSON.stringify(err)}`);
75. }
76. }

78. testSetSpecificSystemBarEnabled() {
79. let window: window.Window | undefined = this.storage?.get("window");
80. let p = window?.setSpecificSystemBarEnabled('navigationIndicator', false, false)
81. p?.then(() => {
82. console.info('setSpecificSystemBarEnabled success');
83. }).catch((err: BusinessError) => {
84. console.error(`setSpecificSystemBarEnabled failed, error = ${JSON.stringify(err)}`);
85. })
86. }
87. }
```
