---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-getcontext
title: getContext
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > getContext
category: harmonyos-references
scraped_at: 2026-04-28T08:00:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:094d7a4994b4f0954bfec7947204f3e8e556097ef3e689dc4cf63f575bf819d0
---

如果需要在页面中获得当前Ability的Context，可调用getContext接口获取当前页面关联的[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)或[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该接口仅限Stage模型使用。

## getContext(deprecated)

PhonePC/2in1TabletTVWearable

getContext(component?: Object):Context

获取与页面上下文组件关联的Context对象。

说明

从API version 9开始支持，从API version 18开始废弃，建议使用getHostContext替代。[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例对象后再进行获取。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| component | Object | 否 | 当前自定义组件的实例。未传入component或传入的参数类型非法，则返回默认上下文。默认上下文是指通过追溯当前方法的调用链所跟踪到的Context。在异步调用的回调方法中使用该接口，或者该接口的起始调用不在当前页面，将可能导致无法跟踪到该实例的Context，则会返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](js-apis-getcontext.md#context) | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility窗口中的页面调用该接口，返回类型为ExtensionContext。 |

## Context

PhonePC/2in1TabletTVWearable

type Context = Context

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [Context](../harmonyos-guides/application-context-stage.md) | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为UIAbilityContext。在ExtensionAbility窗口中的页面调用该接口，返回类型为ExtensionContext。 |

说明

直接使用getContext可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getHostContext](arkts-apis-uicontext-uicontext.md#gethostcontext12)调用绑定实例的getContext。

**示例：**

在UIAbility中通过windowStage.loadContent加载具体页面。

```
1. // EntryAbility.ets
2. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. }

11. onDestroy() {
12. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
13. }

15. onWindowStageCreate(windowStage: window.WindowStage) {
16. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

18. windowStage.loadContent('pages/Index', (err, data) => {
19. if (err.code) {
20. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
21. return;
22. }
23. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
24. });
25. }

27. onWindowStageDestroy() {
28. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
29. }

31. onForeground() {
32. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
33. }

35. onBackground() {
36. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
37. }
38. }
```

在具体的Index.ets中可以通过getContext接口获取Context上下文，本示例返回的Context类型为UIAbilityContext。

```
1. //pages/Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'Hello World'

7. build() {
8. Row() {
9. Column() {
10. Text(this.message)
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. .onClick(() => {
14. // 建议使用this.getUIContext().getHostContext()
15. let context: Context = getContext(this) as Context;
16. console.info("CacheDir:" + context.cacheDir);
17. })
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```
