---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext
title: Class (UIContext)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (UIContext)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a01b8ffeb42f47c185ac566e00331d6f5b8b874c77415e80f727c9beaef07db0
---

UIContext实例对象。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。
* 以下API需要通过对应的UIContext实例调用。获取UIContext分为三种方式，第一种是使用ohos.window中的[getUIContext()](arkts-apis-window-window.md#getuicontext10)方法获取UIContext实例，第二种是通过自定义组件内置方法[getUIContext()](ts-custom-component-api.md#getuicontext)获取UIContext实例，第三种是通过UIContext类的静态方法如[getCallingScopeUIContext](arkts-apis-uicontext-uicontext.md#getcallingscopeuicontext22)获取UIContext实例。本文中UIContext对象以uiContext表示。

**示例：**

以下示例展示了三种获取UIContext实例的方法。

```
1. // 三种方法获取到的UIContext没有差异
2. // index.ets
3. import { UIContext } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Column() {
10. Button("Button")
11. .onClick(()=>{
12. // 通过自定义组件内置方法获取
13. this.getUIContext()
14. // 通过UIContext类的静态方法获取
15. let uiContext = UIContext.getCallingScopeUIContext();
16. // 其他运行逻辑
17. })
18. }
19. }
20. }

22. // EntryAbility.ets
23. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
24. import { hilog } from '@kit.PerformanceAnalysisKit';
25. import { window } from '@kit.ArkUI';

27. const DOMAIN = 0x0000;

29. export default class EntryAbility extends UIAbility {
30. onWindowStageCreate(windowStage: window.WindowStage): void {
31. // 通过ohos.window获取
32. windowStage.getMainWindowSync().getUIContext()
33. // 其他运行逻辑
34. }
35. }
```

## constructor22+

PhonePC/2in1TabletTVWearable

constructor()

构造UIContext对象。

说明

通过构造函数创建的UIContext对象指向不明确的UI上下文，即不指向任何UI实例。该UIContext对应实例的唯一标识ID为-1。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. function GetUIContextByAtomicInterface(): UIContext {
5. let callingScopeUIContext = UIContext.getCallingScopeUIContext();
6. if (callingScopeUIContext) {
7. hilog.info(0x00, 'testTag', `Get UIContext of calling scope.`)
8. return callingScopeUIContext;
9. }
10. let allContexts = UIContext.getAllUIContexts();
11. let length = allContexts.length;
12. if (length === 1) {
13. hilog.info(0x00, 'testTag', `Get UIContext of unique UI instance.`)
14. return allContexts[0];
15. }
16. let lastFocusedUIContext = UIContext.getLastFocusedUIContext();
17. if (lastFocusedUIContext) {
18. hilog.info(0x00, 'testTag', `Get UIContext of last focused instance.`)
19. return lastFocusedUIContext;
20. }
21. let lastForegroundUIContext = UIContext.getLastForegroundUIContext();
22. if (lastForegroundUIContext) {
23. hilog.info(0x00, 'testTag', `Get UIContext of last foregrounded instance.`)
24. return lastForegroundUIContext;
25. }
26. if (length !== 0) {
27. hilog.info(0x00, 'testTag', `Get UIContext with maximum instanceId.`)
28. return allContexts[length - 1];
29. }
30. hilog.info(0x00, 'testTag', `Get UIContext of undefined calling scope.`)
31. return new UIContext();
32. }

34. @Entry
35. @Component
36. struct Index {
37. @State message: string = 'Hello World';

39. aboutToAppear() {
40. let uiContext = this.getUIContext();
41. hilog.info(0x00, 'testTag', `aboutToAppear UIContext: ${uiContext.getId()}`)
42. }

44. build() {
45. RelativeContainer() {
46. Text(this.message)
47. .id('HelloWorld')
48. .fontSize($r('app.float.page_text_font_size'))
49. .fontWeight(FontWeight.Bold)
50. .alignRules({
51. center: { anchor: '__container__', align: VerticalAlign.Center },
52. middle: { anchor: '__container__', align: HorizontalAlign.Center }
53. })
54. .onClick(() => {
55. let resolvedUIContext = UIContext.resolveUIContext();
56. let contextByAtomicInterface = GetUIContextByAtomicInterface();
57. hilog.info(0x00, 'testTag',
58. `UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}, contextByAtomicInterface: ${contextByAtomicInterface.getId()}`);
59. this.message = 'Welcome';
60. })
61. }
62. .height('100%')
63. .width('100%')
64. }
65. }
```

## getCallingScopeUIContext22+

PhonePC/2in1TabletTVWearable

static getCallingScopeUIContext(): UIContext | undefined

获取当前[调用作用域](../harmonyos-guides/arkts-global-interface.md#基本概念)的UIContext，调用作用域不明确时返回undefined。

说明

返回的UIContext对象可能指向一个已销毁的UI实例，通常在由已销毁的实例抛出异步任务时出现。建议通过[isAvailable](arkts-apis-uicontext-uicontext.md#isavailable20)接口判断其有效性。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext | undefined | 当前[调用作用域](../harmonyos-guides/arkts-global-interface.md#基本概念)的UIContext，调用作用域不明确时返回undefined。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. RelativeContainer() {
11. Text(this.message)
12. .fontWeight(FontWeight.Bold)
13. .alignRules({
14. center: { anchor: '__container__', align: VerticalAlign.Center },
15. middle: { anchor: '__container__', align: HorizontalAlign.Center }
16. })
17. .onClick(() => {
18. this.message = 'Welcome';
19. let uiContext = UIContext.getCallingScopeUIContext();
20. hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
21. })
22. }
23. .height('100%')
24. .width('100%')
25. }
26. }
```

## getLastFocusedUIContext22+

PhonePC/2in1TabletTVWearable

static getLastFocusedUIContext(): UIContext | undefined

获取最近一次切换到获焦状态的UI实例的UIContext。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext | undefined | 返回最近一次切换到获焦状态的UI实例的UIContext。如果最近一次切换到获焦状态的实例已被销毁或无实例曾经处于获焦状态，返回undefined。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. RelativeContainer() {
11. Text(this.message)
12. .fontWeight(FontWeight.Bold)
13. .alignRules({
14. center: { anchor: '__container__', align: VerticalAlign.Center },
15. middle: { anchor: '__container__', align: HorizontalAlign.Center }
16. })
17. .onClick(() => {
18. this.message = 'Welcome';
19. let uiContext = UIContext.getLastFocusedUIContext();
20. hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
21. })
22. }
23. .height('100%')
24. .width('100%')
25. }
26. }
```

## getLastForegroundUIContext22+

PhonePC/2in1TabletTVWearable

static getLastForegroundUIContext(): UIContext | undefined

获取最近一次切换到前台状态的UI实例的UIContext。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext | undefined | 返回最近一次切换到前台状态的UI实例的UIContext。如果最近一次切换到前台状态的UI实例已被销毁或无UI实例曾经处于前台状态，则返回undefined。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. RelativeContainer() {
11. Text(this.message)
12. .fontWeight(FontWeight.Bold)
13. .alignRules({
14. center: { anchor: '__container__', align: VerticalAlign.Center },
15. middle: { anchor: '__container__', align: HorizontalAlign.Center }
16. })
17. .onClick(() => {
18. this.message = 'Welcome';
19. let uiContext = UIContext.getLastForegroundUIContext();
20. hilog.info(0x00, 'testTag', 'Current calling UIContext is : ' + uiContext?.isAvailable());
21. })
22. }
23. .height('100%')
24. .width('100%')
25. }
26. }
```

## getAllUIContexts22+

PhonePC/2in1TabletTVWearable

static getAllUIContexts(): UIContext[]

获取所有当前有效的UIContext实例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext[] | 返回所有当前有效UIContext实例的数组。如果没有有效的UIContext实例，则返回空数组。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. RelativeContainer() {
11. Text(this.message)
12. .fontWeight(FontWeight.Bold)
13. .alignRules({
14. center: { anchor: '__container__', align: VerticalAlign.Center },
15. middle: { anchor: '__container__', align: HorizontalAlign.Center }
16. })
17. .onClick(() => {
18. this.message = 'Welcome';
19. let uiContexts = UIContext.getAllUIContexts();
20. hilog.info(0x00, 'testTag', `There are ${uiContexts.length} UIContext(s)`);
21. })
22. }
23. .height('100%')
24. .width('100%')
25. }
26. }
```

## resolveUIContext22+

PhonePC/2in1TabletTVWearable

static resolveUIContext(): ResolvedUIContext

使用优先级策略获取带有解析策略的UIContext实例对象。

说明

按照预定义的优先级顺序解析并返回UIContext实例和UIContext的解析策略。

解析规则按顺序如下：

1. 当前调用作用域中的UIContext。
2. 如果只存在一个UI实例，则返回其UIContext。
3. 如果存在UI实例切换到获焦状态，且最近一次切换到获焦状态的UI实例未销毁，则返回最近一次获焦UI实例的UIContext。
4. 如果存在UI实例切换到前台状态，且最近一次切换到前台状态的UI实例未销毁，则返回最近一次切换到前台状态的UI实例的UIContext。
5. 如果存在多个UI实例，则返回实例唯一标识的ID最大的UIContext。
6. 如果以上条件均不满足，则返回一个无效的UIContext实例。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedUIContext](arkts-apis-uicontext-resolveduicontext.md) | 返回带有解析策略的UIContext实例对象。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Column() {
9. Button('click').onClick(() => {
10. let resolvedUIContext = UIContext.resolveUIContext();
11. hilog.info(0x00, 'testTag', `UIContext id: ${resolvedUIContext.getId()}, strategy: ${resolvedUIContext.strategy}}`);
12. })
13. }
14. .width(UIContext.resolveUIContext().px2vp(100))
15. .height('100%')
16. }
17. }
```

## isAvailable20+

PhonePC/2in1TabletTVWearable

isAvailable(): boolean

判断UIContext对象对应的UI实例是否有效。使用[getUIContext](arkts-apis-window-window.md#getuicontext10)方法获取UIContext对象。后端UI实例存在时，该UI实例有效。通过new UIContext()创建的UIContext对象无对应的UI实例；多次[loadContent](arkts-apis-window-window.md#loadcontent9)后，旧的UI实例会失效。多窗口应用场景，当窗口关闭后，该窗口的UI实例失效。总而言之，当UIContext对象没有对应的后端UI实例时，该对象是无效的。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回UIContext对象对应的UI实例是否有效。true表示有效，false表示无效。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct UIContextCompare {
6. @State result1: string = ""
7. @State result2: string = ""

9. build() {
10. Column() {
11. Text("getUIContext() 结果: " + this.result1)
12. .fontSize(20)
13. .margin(10)

15. Text("new UIContext() 结果: " + this.result2)
16. .fontSize(20)
17. .margin(10)

19. Divider().margin(20)

21. Button("getUIContext()")
22. .width("70%")
23. .height(50)
24. .margin(10)
25. .onClick(() => {
26. try {
27. const ctx: UIContext = this.getUIContext();
28. const available: boolean = ctx.isAvailable();
29. this.result1 = `可用状态: ${available} UI实例有效 `;
30. console.info("getUIContext测试:", available);
31. } catch (e) {
32. this.result1 = "错误: " + (e instanceof Error ? e.message : String(e));
33. }
34. })

36. Button("new UIContext()")
37. .width("70%")
38. .height(50)
39. .margin(10)
40. .onClick(() => {
41. try {
42. const ctx: UIContext = new UIContext();
43. const available: boolean = ctx.isAvailable();
44. this.result2 = `可用状态: ${available} UI实例无效`;
45. console.info("new UIContext测试:", available);
46. } catch (e) {
47. this.result2 = "错误: " + (e instanceof Error ? e.message : String(e));
48. }
49. })
50. }
51. .width("100%")
52. .height("100%")
53. .padding(20)
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/_H4oOVMQTZG8fj6FcYSUFg/zh-cn_image_0000002558606276.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=91016CDA5EA36FC1C85E8151F1E15E31B2EB67C22C9E9959AF22EDC385248B88)

## getFont

PhonePC/2in1TabletTVWearable

getFont(): Font

获取Font对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Font](arkts-apis-uicontext-font.md) | 返回Font实例对象。 |

**示例：**

完整示例请参考[Font](arkts-apis-uicontext-font.md)中的示例。

## getComponentUtils

PhonePC/2in1TabletTVWearable

getComponentUtils(): ComponentUtils

获取ComponentUtils对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ComponentUtils](arkts-apis-uicontext-componentutils.md) | 返回ComponentUtils实例对象。 |

**示例：**

完整示例请参考[示例1（获取ComponentUtils对象）](js-apis-arkui-componentutils.md#示例1获取componentutils对象)。

## getUIInspector

PhonePC/2in1TabletTVWearable

getUIInspector(): UIInspector

获取UIInspector对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIInspector](arkts-apis-uicontext-uiinspector.md) | 返回UIInspector实例对象。 |

**示例：**

完整示例请参考[UIInspector](arkts-apis-uicontext-uiinspector.md)中的示例。

## getUIObserver11+

PhonePC/2in1TabletTVWearable

getUIObserver(): UIObserver

获取UIObserver对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIObserver](arkts-apis-uicontext-uiobserver.md) | 返回UIObserver实例对象。 |

**示例：**

```
1. @Component
2. struct PageOne {
3. build() {
4. NavDestination() {
5. Text("pageOne")
6. }.title("pageOne")
7. }
8. }

10. @Entry
11. @Component
12. struct Index {
13. private stack: NavPathStack = new NavPathStack();

15. @Builder
16. PageBuilder(name: string) {
17. PageOne()
18. }

20. aboutToAppear() {
21. this.getUIContext().getUIObserver().on('navDestinationUpdate', (info) => {
22. console.info('NavDestination state update', JSON.stringify(info));
23. });
24. }

26. aboutToDisappear() {
27. this.getUIContext().getUIObserver().off('navDestinationUpdate');
28. }

30. build() {
31. Column() {
32. Navigation(this.stack) {
33. Button("push").onClick(() => {
34. this.stack.pushPath({ name: "pageOne" });
35. })
36. }
37. .title("Navigation")
38. .navDestination(this.PageBuilder)
39. }
40. .width('100%')
41. .height('100%')
42. }
43. }
```

## getId22+

PhonePC/2in1TabletTVWearable

getId(): number

获取UI实例对象唯一标识，多实例场景下，开发者可使用此唯一标识区分多个UI实例对象，便于管理。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回后端实例唯一标识的ID，取值范围：[-1, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct Index{
4. build(){
5. Column()
6. .width("100%")
7. .height("100%")
8. .onClick(()=>{
9. console.info(`id:${this.getUIContext()?.getId()}`);
10. })
11. }
12. }
```

## getMediaQuery

PhonePC/2in1TabletTVWearable

getMediaQuery(): MediaQuery

获取MediaQuery对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaQuery](arkts-apis-uicontext-mediaquery.md) | 返回MediaQuery实例对象。 |

**示例：**

完整示例请参考[mediaquery示例](js-apis-mediaquery.md#示例)。

## getRouter

PhonePC/2in1TabletTVWearable

getRouter(): Router

获取Router对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Router](arkts-apis-uicontext-router.md) | 返回Router实例对象。 |

**示例：**

完整示例请参考[pushUrl](arkts-apis-uicontext-router.md#pushurl)。

## getPromptAction

PhonePC/2in1TabletTVWearable

getPromptAction(): PromptAction

获取PromptAction对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PromptAction](arkts-apis-uicontext-promptaction.md) | 返回PromptAction实例对象。 |

**示例：**

完整示例请参考[PromptAction](arkts-apis-uicontext-promptaction.md)中的示例。

## getOverlayManager12+

PhonePC/2in1TabletTVWearable

getOverlayManager(): OverlayManager

获取OverlayManager对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OverlayManager](arkts-apis-uicontext-overlaymanager.md) | 返回OverlayManager实例对象。 |

**示例：**

完整示例请参考[OverlayManager](arkts-apis-uicontext-overlaymanager.md)中的示例。

## setOverlayManagerOptions15+

PhonePC/2in1TabletTVWearable

setOverlayManagerOptions(options: OverlayManagerOptions): boolean

设置[OverlayManager](arkts-apis-uicontext-overlaymanager.md)参数。用于在使用OverlayManager能力之前先初始化overlayManager的参数，包括是否需要渲染overlay根节点等属性。该方法需要在执行getOverlayManager方法之前执行生效，且该方法只生效一次。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [OverlayManagerOptions](arkts-apis-uicontext-i.md#overlaymanageroptions15) | 是 | OverlayManager参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否设置成功。  返回true表示设置成功。返回false表示设置失败。 |

**示例：**

完整示例请参考[OverlayManager](arkts-apis-uicontext-overlaymanager.md)中的示例。

## getOverlayManagerOptions15+

PhonePC/2in1TabletTVWearable

getOverlayManagerOptions(): OverlayManagerOptions

用于获取当前[OverlayManagerOptions](arkts-apis-uicontext-i.md#overlaymanageroptions15)参数。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：**: SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OverlayManagerOptions](arkts-apis-uicontext-i.md#overlaymanageroptions15) | 返回当前OverlayManagerOptions。 |

**示例：**

完整示例请参考[OverlayManager](arkts-apis-uicontext-overlaymanager.md)中的示例。

## animateToImmediately23+

PhonePC/2in1TabletTVWearable

animateToImmediately(param: AnimateParam, processor: Callback<void>): void

通过UIContext对象指定明确的动画主实例上下文，并触发显式动画立即下发。避免由于找不到实例或实例不对，导致的动画不执行或动画结束回调不执行问题。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 设置动画效果相关参数。 |
| processor | Callback<void> | 是 | 回调函数。指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

**示例：**

该示例通过UIContext对象获取显式立即动画，并调用animateToImmediately接口实现参数定义的动画效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AnimateToImmediatelyExample {
5. @State widthSize: number = 250
6. @State heightSize: number = 100
7. @State opacitySize: number = 0
8. private flag: boolean = true
9. uiContext: UIContext | null | undefined = this.getUIContext();

11. build() {
12. Column() {
13. Column()
14. .width(this.widthSize)
15. .height(this.heightSize)
16. .backgroundColor(Color.Green)
17. .opacity(this.opacitySize)
18. Button('change size')
19. .margin(30)
20. .onClick(() => {
21. if (this.flag) {
22. this.uiContext?.animateToImmediately({
23. delay: 0,
24. duration: 1000
25. }, () => {
26. this.opacitySize = 1
27. })
28. this.uiContext?.animateTo({
29. delay: 1000,
30. duration: 1000
31. }, () => {
32. this.widthSize = 150
33. this.heightSize = 60
34. })
35. } else {
36. this.uiContext?.animateToImmediately({
37. delay: 0,
38. duration: 1000
39. }, () => {
40. this.widthSize = 250
41. this.heightSize = 100
42. })
43. this.uiContext?.animateTo({
44. delay: 1000,
45. duration: 1000
46. }, () => {
47. this.opacitySize = 0
48. })
49. }
50. this.flag = !this.flag
51. })
52. }.width('100%').margin({ top: 5 })
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/lJsYtKSxRZmcHm_syURlqg/zh-cn_image_0000002589325803.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=99D8706D5E01FE0277112F4F855BE5FEC2A9581C9225019CA1351A83E822FF11)

## animateTo

PhonePC/2in1TabletTVWearable

animateTo(value: AnimateParam, event: () => void): void

提供animateTo接口，用于为闭包代码中的状态变化添加过渡动画效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

* 不推荐在aboutToAppear、aboutToDisappear中调用动画。
* 如果在[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)中调用动画，自定义组件内的build还未执行，内部组件还未创建，动画时机过早，动画属性没有初值无法对组件产生动画。
* 执行[aboutToDisappear](ts-custom-component-lifecycle.md#abouttodisappear)时，组件即将销毁，不能在aboutToDisappear里面做动画。
* 在组件出现和消失时，可以通过[组件内转场](ts-transition-animation-component.md)添加动画效果。
* 组件内转场不支持的属性，可以参考[显式动画](ts-explicit-animation.md)中的[示例2](ts-explicit-animation.md#示例2动画执行结束后组件消失)，使用animateTo实现动画执行结束后组件消失的效果。
* 某些场景下，在[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)中使用animateTo动画，会产生异常效果，具体可参考：[在状态管理V2中使用animateTo动画效果异常](../harmonyos-guides/arkts-new-local.md#在状态管理v2中使用animateto动画效果异常)。
* UIAbility从前台切换至后台时会立即结束仍在步进中的有限循环动画，从而触发[onFinish动画播放完成回调](ts-explicit-animation.md#animateparam对象说明)。
* 在设置的开发者选项中关闭过渡动画，动画会当帧结束，onFinish动画播放完成回调会立即执行，请避免在回调中加入时序相关的功能逻辑。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [AnimateParam](ts-explicit-animation.md#animateparam对象说明) | 是 | 设置动画效果相关参数。 |
| event | () => void | 是 | 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AnimateToExample {
5. @State widthSize: number = 250;
6. @State heightSize: number = 100;
7. @State rotateAngle: number = 0;
8. private flag: boolean = true;
9. uiContext: UIContext | undefined = undefined;

11. aboutToAppear() {
12. this.uiContext = this.getUIContext();
13. if (!this.uiContext) {
14. console.warn("no uiContext");
15. return;
16. }
17. }

19. build() {
20. Column() {
21. Button('change size')
22. .width(this.widthSize)
23. .height(this.heightSize)
24. .margin(30)
25. .onClick(() => {
26. if (this.flag) {
27. this.uiContext?.animateTo({
28. duration: 2000,
29. curve: Curve.EaseOut,
30. iterations: 3,
31. playMode: PlayMode.Normal,
32. onFinish: () => {
33. console.info('play end');
34. }
35. }, () => {
36. this.widthSize = 150;
37. this.heightSize = 60;
38. });
39. } else {
40. this.uiContext?.animateTo({}, () => {
41. this.widthSize = 250;
42. this.heightSize = 100;
43. });
44. }
45. this.flag = !this.flag;
46. })
47. Button('stop rotating')
48. .margin(50)
49. .rotate({ x: 0, y: 0, z: 1, angle: this.rotateAngle })
50. .onAppear(() => {
51. // 组件出现时开始做动画
52. this.uiContext?.animateTo({
53. duration: 1200,
54. curve: Curve.Friction,
55. delay: 500,
56. iterations: -1, // 设置-1表示动画无限循环
57. playMode: PlayMode.Alternate,
58. expectedFrameRateRange: {
59. min: 10,
60. max: 120,
61. expected: 60,
62. }
63. }, () => {
64. this.rotateAngle = 90
65. });
66. })
67. .onClick(() => {
68. this.uiContext?.animateTo({ duration: 0 }, () => {
69. // this.rotateAngle之前为90，在duration为0的动画中修改属性，可以停止该属性之前的动画，按新设置的属性显示
70. this.rotateAngle = 0;
71. });
72. })
73. }.width('100%').margin({ top: 5 })
74. }
75. }
```

## getSharedLocalStorage12+

PhonePC/2in1TabletTVWearable

getSharedLocalStorage(): LocalStorage | undefined

获取当前stage共享的LocalStorage实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LocalStorage](ts-state-management.md#localstorage9) | undefined | 返回LocalStorage实例。共享的LocalStorage实例不存在时返回undefined。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. storage: LocalStorage = new LocalStorage();

8. onWindowStageCreate(windowStage: window.WindowStage) {
9. windowStage.loadContent('pages/Index', this.storage);
10. }
11. }
```

```
1. // Index.ets

3. @Entry
4. @Component
5. struct SharedLocalStorage {
6. localStorage = this.getUIContext().getSharedLocalStorage();

8. build() {
9. Row() {
10. Column() {
11. Button("Change Local Storage to 47")
12. .onClick(() => {
13. this.localStorage?.setOrCreate("propA", 47);
14. })
15. Button("Get Local Storage")
16. .onClick(() => {
17. console.info(`localStorage: ${this.localStorage?.get("propA")}`);
18. })
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

## getHostContext12+

PhonePC/2in1TabletTVWearable

getHostContext(): Context | undefined

获得当前元能力的Context。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Context](arkts-apis-uicontext-t.md#context12) | undefined | 返回当前组件所在Ability的Context，Context的具体类型为当前Ability关联的Context对象。例如：在UIAbility窗口中的页面调用该接口，返回类型为[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)。在ExtensionAbility窗口中的页面调用该接口，返回类型为[ExtensionContext](js-apis-inner-application-extensioncontext.md)。ability上下文不存在时返回undefined。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. uiContext = this.getUIContext();

6. build() {
7. Row() {
8. Column() {
9. Text("cacheDir='" + this.uiContext?.getHostContext()?.cacheDir + "'")
10. .fontSize(25)
11. .border({ color: Color.Red, width: 2 })
12. .padding(50)
13. Text("bundleCodeDir='" + this.uiContext?.getHostContext()?.bundleCodeDir + "'")
14. .fontSize(25)
15. .border({ color: Color.Red, width: 2 })
16. .padding(50)
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

## getFrameNodeById12+

PhonePC/2in1TabletTVWearable

getFrameNodeById(id: string): FrameNode | null

通过组件的id获取组件树的实体节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](ts-universal-attributes-component-id.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | null | 返回的组件树的实体节点或者空节点。 |

说明

getFrameNodeById通过遍历查询对应id的节点，性能较差。推荐使用[getAttachedFrameNodeById](arkts-apis-uicontext-uicontext.md#getattachedframenodebyid12)。

**示例：**

完整示例请参考[获取根节点示例](js-apis-arkui-framenode.md#获取根节点示例)。

## getAttachedFrameNodeById12+

PhonePC/2in1TabletTVWearable

getAttachedFrameNodeById(id: string): FrameNode | null

通过组件的id获取当前窗口上的实体节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](ts-universal-attributes-component-id.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | null | 返回的组件树的实体节点或者空节点。 |

说明

getAttachedFrameNodeById仅能查询上屏节点。

**示例：**

```
1. @Entry
2. @Component
3. struct MyComponent {
4. @State message: string = 'Hello World';

6. build() {
7. RelativeContainer() {
8. Text(this.message)
9. .id('HelloWorld')
10. .fontSize($r('app.float.page_text_font_size'))
11. .fontWeight(FontWeight.Bold)
12. .alignRules({
13. center: { anchor: '__container__', align: VerticalAlign.Center },
14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
15. })
16. .onClick(() => {
17. let node = this.getUIContext().getAttachedFrameNodeById("HelloWorld");
18. console.info(`Find HelloWorld Tag:${node!.getNodeType()} id:${node!.getUniqueId()}`);
19. })
20. }
21. .height('100%')
22. .width('100%')
23. }
24. }
```

## getFrameNodeByUniqueId12+

PhonePC/2in1TabletTVWearable

getFrameNodeByUniqueId(id: number): FrameNode | null

提供getFrameNodeByUniqueId接口通过组件的uniqueId获取组件树的实体节点。

1. 当uniqueId对应的是系统组件时，返回组件所对应的FrameNode；
2. 当uniqueId对应的是自定义组件时，若其有渲染内容，则返回该自定义组件的根节点，类型为\_\_Common\_\_；若其无渲染内容，则返回其第一个子组件的FrameNode。
3. 当uniqueId无对应的组件时，返回null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | null | 返回的组件树的实体节点或者空节点。 |

**示例：**

```
1. import { UIContext, FrameNode } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MyComponent {
6. aboutToAppear() {
7. let uniqueId: number = this.getUniqueId();
8. let uiContext: UIContext = this.getUIContext();
9. if (uiContext) {
10. let node: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
11. }
12. }

14. build() {
15. // ...
16. }
17. }
```

## getPageInfoByUniqueId12+

PhonePC/2in1TabletTVWearable

getPageInfoByUniqueId(id: number): PageInfo

提供getPageInfoByUniqueId接口通过组件的uniqueId获取该节点对应的Router和NavDestination页面信息。

1. 当uniqueId对应的节点在Page节点中，routerPageInfo属性为其对应的Router信息；
2. 当uniqueId对应的节点在NavDestination节点中，navDestinationInfo属性为其对应的NavDestination信息；
3. 当uniqueId对应的节点无对应的Router或NavDestination信息时，对应的属性为undefined；
4. 模态弹窗并不在任何Page节点中。当uniqueId对应的节点在模态弹窗中，例如[CustomDialog](ts-methods-custom-dialog-box.md)、[bindSheet](ts-universal-attributes-sheet-transition.md#bindsheet)和[bindContentCover](ts-universal-attributes-modal-transition.md#bindcontentcover)构建的模态页面中，routerPageInfo属性为undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PageInfo](arkts-apis-uicontext-i.md#pageinfo12) | 返回节点对应的Router和NavDestination信息。 |

**示例：**

```
1. import { UIContext, PageInfo } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct PageInfoExample {
6. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

8. build() {
9. Column() {
10. Navigation(this.pageInfos) {
11. NavDestination() {
12. MyComponent()
13. }
14. }.id('navigation')
15. }
16. }
17. }

19. @Component
20. struct MyComponent {
21. @State content: string = '';

23. build() {
24. Column() {
25. Text('PageInfoExample')
26. Button('click').onClick(() => {
27. const uiContext: UIContext = this.getUIContext();
28. const uniqueId: number = this.getUniqueId();
29. const pageInfo: PageInfo = uiContext.getPageInfoByUniqueId(uniqueId);
30. console.info('pageInfo: ' + JSON.stringify(pageInfo));
31. console.info('navigationInfo: ' + JSON.stringify(uiContext.getNavigationInfoByUniqueId(uniqueId)));
32. })
33. TextArea({
34. text: this.content
35. })
36. .width('100%')
37. .height(100)
38. }
39. .width('100%')
40. .alignItems(HorizontalAlign.Center)
41. }
42. }
```

## getNavigationInfoByUniqueId12+

PhonePC/2in1TabletTVWearable

getNavigationInfoByUniqueId(id: number): observer.NavigationInfo | undefined

提供getNavigationInfoByUniqueId接口通过组件的uniqueId获取该节点对应的Navigation页面信息。

1. 当uniqueId对应的节点在Navigation节点中，返回其对应的Navigation信息；
2. 当uniqueId对应的节点无对应的Navigation信息时，返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 节点对应的UniqueId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| observer.[NavigationInfo](js-apis-arkui-observer.md#navigationinfo12) | undefined | 返回节点对应的Navigation信息。 |

**示例：**

请参考[getPageInfoByUniqueId](arkts-apis-uicontext-uicontext.md#getpageinfobyuniqueid12)的示例。

## showAlertDialog

PhonePC/2in1TabletTVWearable

showAlertDialog(options: AlertDialogParamWithConfirm | AlertDialogParamWithButtons | AlertDialogParamWithOptions): void

显示警告弹窗组件，可设置文本内容与响应回调。

说明

不支持在输入法类型窗口中使用子窗（[showInSubWindow](ts-methods-alert-dialog-box.md#alertdialogparam对象说明) 为true）的showAlertDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AlertDialogParamWithConfirm](ts-methods-alert-dialog-box.md#alertdialogparamwithconfirm对象说明) | [AlertDialogParamWithButtons](ts-methods-alert-dialog-box.md#alertdialogparamwithbuttons对象说明) | [AlertDialogParamWithOptions](ts-methods-alert-dialog-box.md#alertdialogparamwithoptions10对象说明) | 是 | 定义并显示AlertDialog组件。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. uiContext: UIContext = this.getUIContext()

6. build() {
7. Column() {
8. Button('showAlertDialog')
9. .onClick(() => {
10. this.uiContext.showAlertDialog(
11. {
12. title: 'title',
13. message: 'text',
14. autoCancel: true,
15. alignment: DialogAlignment.Bottom,
16. offset: { dx: 0, dy: -20 },
17. gridCount: 3,
18. confirm: {
19. value: 'button',
20. action: () => {
21. console.info('Button-clicking callback');
22. }
23. },
24. cancel: () => {
25. console.info('Closed callbacks');
26. }
27. }
28. );
29. })
30. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/UvdqEenuTf6rN_AF0NOpoA/zh-cn_image_0000002589245745.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=C894FDAE9AFD7055AC1372898DB652CAA0AE64D3CE297D4FE189508296B3A47E)

## showActionSheet

PhonePC/2in1TabletTVWearable

showActionSheet(value: ActionSheetOptions): void

定义列表弹窗并弹出。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ActionSheetOptions](ts-methods-action-sheet.md#actionsheetoptions对象说明) | 是 | 配置列表弹窗的参数。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. uiContext: UIContext = this.getUIContext()

6. build() {
7. Column() {
8. Button('showActionSheet')
9. .onClick(() => {
10. this.uiContext.showActionSheet({
11. title: 'ActionSheet title',
12. message: 'message',
13. autoCancel: true,
14. confirm: {
15. value: 'Confirm button',
16. action: () => {
17. console.info('Get ActionSheet handled');
18. }
19. },
20. cancel: () => {
21. console.info('ActionSheet canceled');
22. },
23. alignment: DialogAlignment.Bottom,
24. offset: { dx: 0, dy: -10 },
25. sheets: [
26. {
27. title: 'apples',
28. action: () => {
29. console.info('apples');
30. }
31. },
32. {
33. title: 'bananas',
34. action: () => {
35. console.info('bananas');
36. }
37. },
38. {
39. title: 'pears',
40. action: () => {
41. console.info('pears');
42. }
43. }
44. ]
45. });
46. })
47. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/VIRy23gkTpudvykCXrVmyQ/zh-cn_image_0000002558765934.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=D4C99BDAF6B75A011B490DCA809AAB7E6D95FCBC86185F4F4C06897199D485FA)

## showDatePickerDialog

PhonePC/2in1TabletTVWearable

showDatePickerDialog(options: DatePickerDialogOptions): void

定义日期滑动选择器弹窗并弹出。

说明

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showDatePickerDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DatePickerDialogOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明) | 是 | 配置日期滑动选择器弹窗的参数。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date("2010-1-1");

7. build() {
8. Row(){
9. Column() {
10. Button("DatePickerDialog")
11. .margin(20)
12. .onClick(() => {
13. this.getUIContext().showDatePickerDialog({
14. start: new Date("2000-1-1"),
15. end: new Date("2100-12-31"),
16. selected: this.selectedDate,
17. showTime: true,
18. useMilitaryTime: false,
19. dateTimeOptions: { hour: "numeric", minute: "2-digit" },
20. onDateAccept: (value: Date) => {
21. // 通过Date的setFullYear方法设置按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
22. this.selectedDate = value;
23. console.info("DatePickerDialog:onDateAccept()" + value.toString());
24. },
25. onCancel: () => {
26. console.info("DatePickerDialog:onCancel()");
27. },
28. onDateChange: (value: Date) => {
29. console.info("DatePickerDialog:onDateChange()" + value.toString());
30. },
31. onDidAppear: () => {
32. console.info("DatePickerDialog:onDidAppear()");
33. },
34. onDidDisappear: () => {
35. console.info("DatePickerDialog:onDidDisappear()");
36. },
37. onWillAppear: () => {
38. console.info("DatePickerDialog:onWillAppear()");
39. },
40. onWillDisappear: () => {
41. console.info("DatePickerDialog:onWillDisappear()");
42. }
43. })
44. })
45. }.width('100%')
46. }.height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/L-llKv4DT4iNDdmd0iPFow/zh-cn_image_0000002558606278.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=7BC3E62658189BE65AB0EB5E20E5667AF79272A74A8E008FE0631357F4EACDD7)

## showTimePickerDialog

PhonePC/2in1TabletTVWearable

showTimePickerDialog(options: TimePickerDialogOptions): void

定义时间滑动选择器弹窗并弹出。

说明

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTimePickerDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TimePickerDialogOptions](ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明) | 是 | 配置时间滑动选择器弹窗的参数。 |

**示例：**

```
1. // xxx.ets

3. class SelectTime{
4. selectTime: Date = new Date('2020-12-25T08:30:00');
5. hours(h:number,m:number){
6. this.selectTime.setHours(h, m);
7. }
8. }

10. @Entry
11. @Component
12. struct TimePickerDialogExample {
13. @State selectTime: Date = new Date('2023-12-25T08:30:00');

15. build() {
16. Column() {
17. Button('showTimePickerDialog')
18. .margin(30)
19. .onClick(() => {
20. this.getUIContext().showTimePickerDialog({
21. selected: this.selectTime,
22. onAccept: (value: TimePickerResult) => {
23. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
24. let time = new SelectTime();
25. if(value.hour && value.minute){
26. time.hours(value.hour, value.minute);
27. }
28. console.info("TimePickerDialog:onAccept()" + JSON.stringify(value));
29. },
30. onCancel: () => {
31. console.info("TimePickerDialog:onCancel()");
32. },
33. onChange: (value: TimePickerResult) => {
34. console.info("TimePickerDialog:onChange()" + JSON.stringify(value));
35. }
36. });
37. })
38. }.width('100%').margin({ top: 5 })
39. }
40. }
```

## showTextPickerDialog

PhonePC/2in1TabletTVWearable

showTextPickerDialog(options: TextPickerDialogOptions): void

定义文本滑动选择器弹窗并弹出。

说明

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTextPickerDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextPickerDialogOptions](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明) | 是 | 配置文本滑动选择器弹窗的参数。 |

**示例：**

```
1. // xxx.ets

3. class SelectedValue{
4. select: number = 2;
5. set(val: number){
6. this.select = val;
7. }
8. }
9. class SelectedArray{
10. select: number[] = [];
11. set(val: number[]){
12. this.select = val;
13. }
14. }
15. @Entry
16. @Component
17. struct TextPickerDialogExample {
18. @State selectTime: Date = new Date('2023-12-25T08:30:00');
19. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4', 'banana5'];
20. private select: number  = 0;
21. build() {
22. Row(){
23. Column() {
24. Button('showTextPickerDialog')
25. .margin(30)
26. .onClick(() => {
27. this.getUIContext().showTextPickerDialog({
28. range: this.fruits,
29. selected: this.select,
30. onAccept: (value: TextPickerResult) => {
31. // 设置select为按下确定按钮时候的选中项index，这样当弹窗再次弹出时显示选中的是上一次确定的选项
32. let selectedVal = new SelectedValue();
33. let selectedArr = new SelectedArray();
34. if (value.index){
35. value.index instanceof Array?selectedArr.set(value.index) : selectedVal.set(value.index);
36. }
37. console.info("TextPickerDialog:onAccept()" + JSON.stringify(value));
38. },
39. onCancel: () => {
40. console.info("TextPickerDialog:onCancel()");
41. },
42. onChange: (value: TextPickerResult) => {
43. console.info("TextPickerDialog:onChange()" + JSON.stringify(value));
44. }
45. });
46. })
47. }.width('100%').margin({ top: 5 })
48. }.height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/fcC2SKztTLCjAdZBJ_xNuA/zh-cn_image_0000002589325805.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=A1D1FC5A95D7D2FA1C4C182A4AECA9927A6B726D8BA5C75D2BA96AA14D5F6E4B)

## showTextPickerDialog20+

PhonePC/2in1TabletTVWearable

showTextPickerDialog(style: TextPickerDialogOptions|TextPickerDialogOptionsExt): void

定义文本滑动选择器弹窗并弹出，相比API version 11，新增了TextPickerDialogOptionsExt参数支持。

说明

不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的showTextPickerDialog，详情见输入法框架的约束与限制说明[createPanel](js-apis-inputmethodengine.md#createpanel10-1)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextPickerDialogOptions](ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明)| [TextPickerDialogOptionsExt](ts-methods-textpicker-dialog.md#textpickerdialogoptionsext20对象说明) | 是 | 配置文本滑动选择器弹窗的参数。 |

## createAnimator

PhonePC/2in1TabletTVWearable

createAnimator(options: AnimatorOptions): AnimatorResult

定义Animator类。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatorResult](js-apis-animator.md#animatorresult) | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { AnimatorOptions, window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. // 创建主窗口，设置此功能的主页
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (err, data) => {
11. if (err.code) {
12. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
13. return;
14. }
15. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
16. let uiContext = windowStage.getMainWindowSync().getUIContext();
17. let options:AnimatorOptions = {
18. duration: 1500,
19. easing: "friction",
20. delay: 0,
21. fill: "forwards",
22. direction: "normal",
23. iterations: 3,
24. begin: 200.0,
25. end: 400.0
26. };
27. uiContext.createAnimator(options);
28. });
29. }
30. }
```

## createAnimator18+

PhonePC/2in1TabletTVWearable

createAnimator(options: AnimatorOptions | SimpleAnimatorOptions): AnimatorResult

创建animator动画结果对象（AnimatorResult）。与[createAnimator](arkts-apis-uicontext-uicontext.md#createanimator)相比，新增对[SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18)类型入参的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimatorOptions](js-apis-animator.md#animatoroptions) | [SimpleAnimatorOptions](js-apis-animator.md#simpleanimatoroptions18) | 是 | 定义动画选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AnimatorResult](js-apis-animator.md#animatorresult) | Animator结果接口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { SimpleAnimatorOptions, window } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage) {
8. // 创建主窗口，设置此功能的主页
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
10. windowStage.loadContent('pages/Index', (err, data) => {
11. if (err.code) {
12. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
13. return;
14. }
15. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
16. let uiContext = windowStage.getMainWindowSync().getUIContext();
17. let options: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);
18. uiContext.createAnimator(options);
19. });
20. }
21. }
```

## runScopedTask

PhonePC/2in1TabletTVWearable

runScopedTask(callback: () => void): void

在当前UI上下文执行传入的回调函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 回调函数 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. uiContext = this.getUIContext();

6. build() {
7. Row() {
8. Column() {
9. Button("run task").onClick(() => {
10. this.uiContext.runScopedTask(() => {
11. // do something
12. })
13. })
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

## setKeyboardAvoidMode11+

PhonePC/2in1TabletTVWearable

setKeyboardAvoidMode(value: KeyboardAvoidMode): void

配置虚拟键盘弹出时，页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [KeyboardAvoidMode](arkts-apis-uicontext-e.md#keyboardavoidmode11) | 是 | 键盘弹出时的页面避让模式。  默认值：KeyboardAvoidMode.OFFSET |

说明

KeyboardAvoidMode.RESIZE模式会压缩页面大小，页面中设置百分比宽高的组件会跟随页面压缩，而直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode的RESIZE模式时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。

KeyboardAvoidMode.NONE模式配置页面不避让键盘，页面会被抬起的键盘遮盖。

setKeyboardAvoidMode针对页面生效，对于弹窗类组件不生效，比如Dialog、Popup、Menu、BindSheet、BindContentCover、Toast、OverlayManager。弹窗类组件的避让模式可以参考[CustomDialogControllerOptions对象说明](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)。

**示例：**

完整示例请参考[示例4（设置键盘避让模式为压缩）](ts-universal-attributes-expand-safe-area.md#示例4设置键盘避让模式为压缩)、[示例5（设置键盘避让模式为上抬）](ts-universal-attributes-expand-safe-area.md#示例5设置键盘避让模式为上抬)以及[示例6（切换避让模式）](ts-universal-attributes-expand-safe-area.md#示例6切换避让模式)。

```
1. // EntryAbility.ets
2. import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility{
5. onWindowStageCreate(windowStage: window.WindowStage) {

7. windowStage.loadContent('pages/Index', (err, data) => {
8. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
9. uiContext.setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
10. });
11. }
12. }
```

## getKeyboardAvoidMode11+

PhonePC/2in1TabletTVWearable

getKeyboardAvoidMode(): KeyboardAvoidMode

获取虚拟键盘弹出时，页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KeyboardAvoidMode](arkts-apis-uicontext-e.md#keyboardavoidmode11) | 返回当前的页面避让模式。 |

**示例：**

完整示例请参考[示例4（设置键盘避让模式为压缩）](ts-universal-attributes-expand-safe-area.md#示例4设置键盘避让模式为压缩)、[示例5（设置键盘避让模式为上抬）](ts-universal-attributes-expand-safe-area.md#示例5设置键盘避让模式为上抬)以及[示例6（切换避让模式）](ts-universal-attributes-expand-safe-area.md#示例6切换避让模式)。

```
1. // EntryAbility.ets
2. import { KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility{
5. onWindowStageCreate(windowStage: window.WindowStage) {

7. windowStage.loadContent('pages/Index', (err, data) => {
8. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
9. let KeyboardAvoidMode = uiContext.getKeyboardAvoidMode();
10. console.info("KeyboardAvoidMode:", JSON.stringify(KeyboardAvoidMode));
11. });
12. }
13. }
```

## getAtomicServiceBar11+

PhonePC/2in1TabletTVWearable

getAtomicServiceBar(): Nullable<AtomicServiceBar>

获取AtomicServiceBar对象，通过该对象设置元服务menuBar的属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Nullable<[AtomicServiceBar](arkts-apis-uicontext-atomicservicebar.md)> | 如果是元服务则返回AtomicServerBar类型，否则返回undefined。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. // Main window is created, set main page for this ability
8. console.info('Ability onWindowStageCreate');
9. windowStage.loadContent('pages/Index', (err, data) => {
10. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
11. let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
12. if (atomicServiceBar != undefined) {
13. console.info('Get AtomServiceBar Successfully.');
14. } else {
15. console.error('Get AtomicServiceBar failed.');
16. }
17. });
18. }
19. }
```

## getDragController11+

PhonePC/2in1TabletTVWearable

getDragController(): DragController

获取DragController对象，可通过该对象创建并发起拖拽。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DragController](arkts-apis-uicontext-dragcontroller.md) | 获取DragController对象。 |

**示例：**

完整示例请参考[DragController](arkts-apis-uicontext-dragcontroller.md)中的示例。

## keyframeAnimateTo11+

PhonePC/2in1TabletTVWearable

keyframeAnimateTo(param: KeyframeAnimateParam, keyframes: Array<KeyframeState>): void

产生关键帧动画。该接口的使用说明请参考[keyframeAnimateTo](ts-keyframeanimateto.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [KeyframeAnimateParam](ts-keyframeanimateto.md#keyframeanimateparam对象说明) | 是 | 关键帧动画的整体动画参数。 |
| keyframes | Array<[KeyframeState](ts-keyframeanimateto.md#keyframestate对象说明)> | 是 | 所有的关键帧状态的列表。 |

**示例：**

```
1. // xxx.ets
2. import { UIContext } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct KeyframeDemo {
7. @State myScale: number = 1.0;
8. uiContext: UIContext | undefined = undefined;

10. aboutToAppear() {
11. this.uiContext = this.getUIContext();
12. }

14. build() {
15. Column() {
16. Circle()
17. .width(100)
18. .height(100)
19. .fill("#46B1E3")
20. .margin(100)
21. .scale({ x: this.myScale, y: this.myScale })
22. .onClick(() => {
23. if (!this.uiContext) {
24. console.error("no uiContext, keyframe failed");
25. return;
26. }
27. this.myScale = 1;
28. // 设置关键帧动画整体播放3次
29. this.uiContext.keyframeAnimateTo({
30. iterations: 3,
31. expectedFrameRateRange: {
32. min: 10,
33. max: 120,
34. expected: 60,
35. }
36. }, [
37. {
38. // 第一段关键帧动画时长为800ms，scale属性做从1到1.5的动画
39. duration: 800,
40. event: () => {
41. this.myScale = 1.5;
42. }
43. },
44. {
45. // 第二段关键帧动画时长为500ms，scale属性做从1.5到1的动画
46. duration: 500,
47. event: () => {
48. this.myScale = 1;
49. }
50. }
51. ]);
52. })
53. }.width('100%').margin({ top: 5 })
54. }
55. }
```

## getFocusController12+

PhonePC/2in1TabletTVWearable

getFocusController(): FocusController

获取[FocusController](arkts-apis-uicontext-focuscontroller.md)对象，可通过该对象控制焦点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FocusController](arkts-apis-uicontext-focuscontroller.md) | 获取FocusController对象。 |

**示例：**

完整示例请参考[FocusController](arkts-apis-uicontext-focuscontroller.md)中的示例。

## getFilteredInspectorTree12+

PhonePC/2in1TabletTVWearable

getFilteredInspectorTree(filters?: Array<string>): string

获取组件树及组件属性。此接口耗时较长，仅适用于测试场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<string> | 否 | 需要获取的组件属性的过滤列表。目前仅支持过滤字段：  "id"：组件唯一标识。  "src"：资源来源。  "content"：元素、组件或对象所包含的信息或数据。  "editable"：是否可编辑。  "scrollable"：是否可滚动。  "selectable"：是否可选择。  "focusable"：是否可聚焦。  "focused"：是否已聚焦。  如果在filters参数中包含以上一个或者多个字段，则未包含的字段会在组件属性查询结果中被过滤掉。如果用户未传入filters参数或者filters参数为空数组，则以上字段全部不会在组件属性查询结果中被过滤掉。  从API version 20开始，支持该过滤字段：  "isLayoutInspector"：返回组件树是否包含[自定义组件](../harmonyos-guides/arkts-create-custom-components.md)。如果用户未传入filters参数或者filters数组不包含isLayoutInspector，返回的组件树将缺少自定义组件的信息。  其余字段仅供测试场景使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取组件树及组件属性的JSON字符串。组件中每个字段的含义请参考[getInspectorInfo](js-apis-arkui-framenode.md#getinspectorinfo12)的返回值说明。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. uiContext.getFilteredInspectorTree(['id', 'src', 'content']);
```

```
1. // xxx.ets
2. import { UIContext } from '@kit.ArkUI';
3. @Entry
4. @Component
5. struct ComponentPage {
6. loopConsole(inspectorStr: string, i: string) {
7. console.info(`InsTree ${i}| type: ${JSON.parse(inspectorStr).$type}, ID: ${JSON.parse(inspectorStr).$ID}`);
8. if (JSON.parse(inspectorStr).$children) {
9. i += '-';
10. for (let index = 0; index < JSON.parse(inspectorStr).$children.length; index++) {
11. this.loopConsole(JSON.stringify(JSON.parse(inspectorStr).$children[index]), i);
12. }
13. }
14. }

16. build() {
17. Column() {
18. Button('content').onClick(() => {
19. const uiContext: UIContext = this.getUIContext();
20. let inspectorStr = uiContext.getFilteredInspectorTree(['content']);
21. console.info(`InsTree : ${inspectorStr}`);
22. inspectorStr = JSON.stringify(JSON.parse(inspectorStr));
23. this.loopConsole(inspectorStr, '-');
24. })
25. Button('isLayoutInspector').onClick(() => {
26. const uiContext: UIContext = this.getUIContext();
27. let inspectorStr = uiContext.getFilteredInspectorTree(['isLayoutInspector']);
28. console.info(`InsTree : ${inspectorStr}`);
29. inspectorStr = JSON.stringify(JSON.parse(inspectorStr).content);
30. this.loopConsole(inspectorStr, '-');
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

当传入"content"过滤字段时，返回的JSON字符串结构如下：

```
1. InsTree : {"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":[{"$type":"Column","$ID":15,"type":"build-in","$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"","$attrs":{},"$children":[{"$type":"Button","$ID":16,"type":"build-in","$rect":"[293.00, 72.00],[427.00,132.00]","$debugLine":"","$attrs":{}},{"$type":"Button","$ID":18,"type":"build-in","$rect":"[237.00, 132.00],[484.00,192.00]","$debugLine":"","$attrs":{}}]}]}\
2. InsTree -| type: root, ID: undefined
3. InsTree --| type: Column, ID: 15
4. InsTree ---| type: Button, ID: 16
5. InsTree ---| type: Button, ID: 18
```

从API version 20开始，当传入"isLayoutInspector"过滤字段时，返回的JSON字符串结构新增外层结构"type"与"content"，其中"content"包含未增加该字段时的原有JSON字符串结构；同时，返回值结构中增添自定义组件。返回的JSON字符串结构如下：

```
1. InsTree : {"type":"root","content":{"$type":"root","width":"720.000000","height":"1280.000000","$resolution":"1.500000","$children":[{"$type":"JsView","$ID":13,"type":"custom","state":{"observedPropertiesInfo":[],"viewInfo":{"componentName":"ComponentPage","id":14,"isV2":false,"isViewActive_":true}},"$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"{\"$line\":\"(0:0)\"}","viewTag":"ComponentPage","$attrs":{"viewKey":"13"},"$children":[{"$type":"Column","$ID":15, "type":"build-in","$rect":"[0.00, 72.00],[720.00,1208.00]","$debugLine":"","$attrs":{ ...
2. InsTree -| type: root, ID: undefined
3. InsTree --| type: JsView, ID: 13
4. InsTree ---| type: Column, ID: 15
5. InsTree ----| type: Button, ID: 16
6. InsTree ----| type: Button, ID: 18
```

## getFilteredInspectorTreeById12+

PhonePC/2in1TabletTVWearable

getFilteredInspectorTreeById(id: string, depth: number, filters?: Array<string>): string

获取指定的组件及其子组件的属性。此接口耗时较长，仅适用于测试场景。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定的[组件标识](ts-universal-attributes-component-id.md)id。 |
| depth | number | 是 | 获取子组件的层数。当取值0时，获取指定的组件及其所有的子孙组件的属性。当取值1时，仅获取指定的组件的属性。当取值2时，指定的组件及其1层子组件的属性。以此类推。 |
| filters | Array<string> | 否 | 需要获取的组件属性的过滤列表。目前仅支持过滤字段：  "id"：组件唯一标识。  "src"：资源来源。  "content"：元素、组件或对象所包含的信息或数据。  "editable"：是否可编辑。  "scrollable"：是否可滚动。  "selectable"：是否可选择。  "focusable"：是否可聚焦。  "focused"：是否已聚焦。  如果在filters参数中包含以上一个或者多个字段，则未包含的字段会在组件属性查询结果中被过滤掉。如果用户未传入filters参数或者filters参数为空数组，则以上字段全部不会在组件属性查询结果中被过滤掉。  其余字段仅供测试场景使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取指定的组件及其子组件的属性的JSON字符串。组件中每个字段的含义请参考[getInspectorInfo](js-apis-arkui-framenode.md#getinspectorinfo12)的返回值说明。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |

**示例：**

```
1. uiContext.getFilteredInspectorTreeById('testId', 0, ['id', 'src', 'content']);
```

```
1. import { UIContext } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct ComponentPage {
5. build() {
6. Column() {
7. Text("Hello World")
8. .fontSize(20)
9. .id("TEXT")
10. Button('getFilteredInspectorTreeById').onClick(() => {
11. const uiContext: UIContext = this.getUIContext();
12. try {
13. let inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ["id", "src"]);
14. console.info(`result1: ${inspectorStr}`);
15. inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
16. console.info(`result2: ${inspectorStr}`);
17. inspectorStr = uiContext.getFilteredInspectorTreeById('TEXT', 1, ["src"]);
18. inspectorStr = JSON.stringify(JSON.parse(inspectorStr)['$children'][0]);
19. console.info(`result3: ${inspectorStr}`);
20. } catch(e) {
21. console.error(`getFilteredInspectorTreeById error: ${e}`);
22. }
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

返回的JSON字符串结构如下：

```
1. result1: {"$type":"root","width":"1260.000000","height":"2720.000000","$resolution":"3.250000","$children":[{"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}]}
2. result2: {"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"id":"TEXT","isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}
3. result3: {"$type":"Text","$ID":6,"type":"build-in","$rect":"[457.00, 123.00],[804.00,199.00]","$debugLine":"","$attrs":{"isLayoutDirtyMarked":false,"isRenderDirtyMarked":false,"isMeasureBoundary":false,"hasPendingRequest":false,"isFirstBuilding":false}}
```

若需获取getFilteredInspectorTreeById方法中首个参数id指定的组件，须参照示例代码将getFilteredInspectorTreeById方法结果先转换为json对象，随后提取$children数组的首项。通过result2和result3的结果对比可知，如果filters参数由["id", "src"]改为["src"]，获取到的$attrs属性将缺少"id"这一key。

## getCursorController12+

PhonePC/2in1TabletTVWearable

getCursorController(): CursorController

获取[CursorController](arkts-apis-uicontext-cursorcontroller.md)对象，可通过该对象控制光标。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CursorController](arkts-apis-uicontext-cursorcontroller.md) | 获取CursorController对象。 |

**示例：**

完整示例请参考[CursorController](arkts-apis-uicontext-cursorcontroller.md)中的示例。

## getContextMenuController12+

PhonePC/2in1TabletTVWearable

getContextMenuController(): ContextMenuController

获取[ContextMenuController](arkts-apis-uicontext-contextmenucontroller.md)对象，可通过该对象控制菜单。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ContextMenuController](arkts-apis-uicontext-contextmenucontroller.md) | 获取ContextMenuController对象。 |

## getMeasureUtils12+

PhonePC/2in1TabletTVWearable

getMeasureUtils(): MeasureUtils

允许用户通过UIContext对象，获取MeasureUtils对象进行文本计算。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MeasureUtils](arkts-apis-uicontext-measureutils.md) | 提供文本宽度、高度等相关计算。 |

**示例：**

完整示例请参考[MeasureUtils](arkts-apis-uicontext-measureutils.md)中的示例。

## getComponentSnapshot12+

PhonePC/2in1TabletTVWearable

getComponentSnapshot(): ComponentSnapshot

获取ComponentSnapshot对象，可通过该对象获取组件截图的能力。

典型使用场景（如长截图）及最佳实践请参考[使用组件截图](../harmonyos-guides/arkts-uicontext-component-snapshot.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md) | 获取ComponentSnapshot对象。 |

**示例：**

完整示例请参考[ComponentSnapshot](arkts-apis-uicontext-componentsnapshot.md)中的示例。

## vp2px12+

PhonePC/2in1TabletTVWearable

vp2px(value : number) : number

将vp单位的数值转换为以px为单位的数值。

转换公式为：px值 = vp值 × 像素密度

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](js-apis-display.md#virtualscreenconfig16).density。

说明

1. getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。
2. UI实例未创建时，[像素单位](ts-pixel-units.md)中的vp2px接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考[像素单位转换接口替换为UIContext接口](../harmonyos-guides/arkts-global-interface.md#像素单位转换接口替换为uicontext接口)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将vp单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().vp2px(50),
16. centerY: this.getUIContext().vp2px(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## px2vp12+

PhonePC/2in1TabletTVWearable

px2vp(value : number) : number

将px单位的数值转换为以vp为单位的数值。

转换公式为：vp值 = px值 ÷ 像素密度

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](js-apis-display.md#virtualscreenconfig16).density。

说明

1. getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。
2. UI实例未创建时，[像素单位](ts-pixel-units.md)中的px2vp接口使用默认屏幕的虚拟像素比进行转换。在该场景下，开发者使用UIContext接口替换时，可参考[像素单位转换接口替换为UIContext接口](../harmonyos-guides/arkts-global-interface.md#像素单位转换接口替换为uicontext接口)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以vp为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().px2vp(50),
16. centerY: this.getUIContext().px2vp(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## fp2px12+

PhonePC/2in1TabletTVWearable

fp2px(value : number) : number

将fp单位的数值转换为以px为单位的数值。

转换公式为：px值 = fp值 × 像素密度 × 字体缩放比例

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](js-apis-display.md#virtualscreenconfig16).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](ts-types.md#configuration)。

说明

getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将fp单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().fp2px(50),
16. centerY: this.getUIContext().fp2px(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## px2fp12+

PhonePC/2in1TabletTVWearable

px2fp(value : number) : number

将px单位的数值转换为以fp为单位的数值。

转换公式为：fp值 = px值 ÷ 像素密度 ÷ 字体缩放比例

像素密度：当前窗口生效的像素密度值，即虚拟屏幕的密度[VirtualScreenConfig](js-apis-display.md#virtualscreenconfig16).density。

字体缩放比例：系统设置的字体缩放系数，对应 [Configuration.fontScale](ts-types.md#configuration)。

说明

getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以fp为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().px2fp(50),
16. centerY: this.getUIContext().px2fp(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## lpx2px12+

PhonePC/2in1TabletTVWearable

lpx2px(value : number) : number

将lpx单位的数值转换为以px为单位的数值。

转换公式为：px值 = lpx值 × 实际屏幕宽度与逻辑宽度（通过[designWidth](../harmonyos-guides/module-configuration-file.md#pages标签)配置）的比值。

说明

getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将lpx单位的数值转换为以px为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().lpx2px(50),
16. centerY: this.getUIContext().lpx2px(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## px2lpx12+

PhonePC/2in1TabletTVWearable

px2lpx(value : number) : number

将px单位的数值转换为以lpx为单位的数值。

转换公式为：lpx值 = px值 ÷ 实际屏幕宽度与逻辑宽度（通过[designWidth](../harmonyos-guides/module-configuration-file.md#pages标签)配置）的比值。

说明

getUIContext需在windowStage.[loadContent](arkts-apis-window-windowstage.md#loadcontent9)之后调用，确保UIContext初始化完成后调用此接口，否则无法返回准确结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将px单位的数值转换为以lpx为单位的数值。  取值范围：(-∞, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 转换后的数值。  取值范围：(-∞, +∞) |

**示例：**

```
1. @Entry
2. @Component
3. struct MatrixExample {
4. build() {
5. Column({ space: 100 }) {
6. Text('Hello1')
7. .textAlign(TextAlign.Center)
8. .width(100)
9. .height(60)
10. .backgroundColor(0xAFEEEE)
11. .borderWidth(1)
12. .rotate({
13. z: 1,
14. angle: 90,
15. centerX: this.getUIContext().px2lpx(50),
16. centerY: this.getUIContext().px2lpx(30)
17. })
18. }.width('100%')
19. .height('100%')
20. }
21. }
```

## getWindowName12+

PhonePC/2in1TabletTVWearable

getWindowName(): string | undefined

获取当前实例所在窗口的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 当前实例所在窗口的名称。若窗口不存在，则返回undefined。 |

**示例：**

```
1. import { window } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. aboutToAppear() {
9. const windowName = this.getUIContext().getWindowName();
10. console.info('WindowName ' + windowName);
11. const currWindow = window.findWindow(windowName);
12. const windowProperties = currWindow.getWindowProperties();
13. console.info(`Window width ${windowProperties.windowRect.width}, height ${windowProperties.windowRect.height}`);
14. }

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }
```

## getWindowId23+

PhonePC/2in1TabletTVWearable

getWindowId(): number | undefined

获取当前应用实例所属的窗口ID。

说明

若UIContext位于主应用程序进程中的[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)内，则返回主应用程序的顶层窗口ID。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | undefined | 当前应用实例所属的窗口ID。若窗口不存在，则返回undefined。 |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. aboutToAppear() {
9. const windowId = this.getUIContext().getWindowId();
10. hilog.info(0x0000, 'testTag', 'current window id: %{public}d', windowId);
11. }

13. build() {
14. Row() {
15. Column() {
16. Text(this.message)
17. .fontSize(50)
18. .fontWeight(FontWeight.Bold)
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

## getWindowWidthBreakpoint13+

PhonePC/2in1TabletTVWearable

getWindowWidthBreakpoint(): WidthBreakpoint

获取当前实例所在窗口的宽度断点枚举值。具体枚举值根据窗口宽度vp值确定，详见 [WidthBreakpoint](ts-appendix-enums.md#widthbreakpoint13)。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WidthBreakpoint](ts-appendix-enums.md#widthbreakpoint13) | 当前实例所在窗口的宽度断点枚举值。若窗口宽度为 0vp，则返回WIDTH\_XS。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(30)
13. .fontWeight(FontWeight.Bold)
14. Button() {
15. Text('test')
16. .fontSize(30)
17. }
18. .onClick(() => {
19. let uiContext: UIContext = this.getUIContext();
20. let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
21. console.info(`Window widthBp: ${widthBp}`);
22. })
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

## getWindowHeightBreakpoint13+

PhonePC/2in1TabletTVWearable

getWindowHeightBreakpoint(): HeightBreakpoint

获取当前实例所在窗口的高度断点。具体枚举值根据窗口高宽比确定，详见 [HeightBreakpoint](ts-appendix-enums.md#heightbreakpoint13)。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HeightBreakpoint](ts-appendix-enums.md#heightbreakpoint13) | 当前实例所在窗口的宽高比对应的高度断点枚举值。若窗口高宽比为0，则返回HEIGHT\_SM。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'Hello World';

8. build() {
9. Row() {
10. Column() {
11. Text(this.message)
12. .fontSize(30)
13. .fontWeight(FontWeight.Bold)
14. Button() {
15. Text('test')
16. .fontSize(30)
17. }
18. .onClick(() => {
19. let uiContext: UIContext = this.getUIContext();
20. let heightBp: HeightBreakpoint = uiContext.getWindowHeightBreakpoint();
21. let widthBp: WidthBreakpoint = uiContext.getWindowWidthBreakpoint();
22. console.info(`Window heightBP: ${heightBp}, widthBp: ${widthBp}`);
23. })
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }
```

## postFrameCallback12+

PhonePC/2in1TabletTVWearable

postFrameCallback(frameCallback: FrameCallback): void

注册一个回调，仅在下一帧渲染时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](arkts-apis-uicontext-framecallback.md) | 是 | 下一帧需要执行的回调。 |

**示例：**

```
1. import { FrameCallback } from '@kit.ArkUI';

3. class MyFrameCallback extends FrameCallback {
4. private tag: string;

6. constructor(tag: string) {
7. super();
8. this.tag = tag;
9. }

11. onFrame(frameTimeNanos: number) {
12. console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Button('点击触发postFrameCallback')
22. .onClick(() => {
23. this.getUIContext().postFrameCallback(new MyFrameCallback("normTask"));
24. })
25. }
26. }
27. }
```

## postDelayedFrameCallback12+

PhonePC/2in1TabletTVWearable

postDelayedFrameCallback(frameCallback: FrameCallback, delayTime: number): void

注册一个回调，在延迟一段时间后的下一帧进行渲染时执行。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frameCallback | [FrameCallback](arkts-apis-uicontext-framecallback.md) | 是 | 下一帧需要执行的回调。 |
| delayTime | number | 是 | 延迟的时间，以毫秒为单位。传入null、undefined或小于0的值，会按0处理。 |

**示例：**

```
1. import { FrameCallback } from '@kit.ArkUI';

3. class MyFrameCallback extends FrameCallback {
4. private tag: string;

6. constructor(tag: string) {
7. super();
8. this.tag = tag;
9. }

11. onFrame(frameTimeNanos: number) {
12. console.info('MyFrameCallback ' + this.tag + ' ' + frameTimeNanos.toString());
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. build() {
20. Row() {
21. Button('点击触发postDelayedFrameCallback')
22. .onClick(() => {
23. this.getUIContext().postDelayedFrameCallback(new MyFrameCallback("delayTask"), 5);
24. })
25. }
26. }
27. }
```

## requireDynamicSyncScene12+

PhonePC/2in1TabletTVWearable

requireDynamicSyncScene(id: string): Array<DynamicSyncScene>

请求组件的动态帧率场景，用于自定义场景相关帧率配置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 节点对应的[组件标识](ts-universal-attributes-component-id.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<DynamicSyncScene> | 获取DynamicSyncScene对象数组。 |

**示例：**

```
1. import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Frame {
6. @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
7. @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30 };
8. private scenes: SwiperDynamicSyncScene[] = [];

10. build() {
11. Column() {
12. Text("动画" + JSON.stringify(this.ANIMATION))
13. Text("跟手" + JSON.stringify(this.GESTURE))
14. Row() {
15. Swiper() {
16. Text("one")
17. Text("two")
18. Text("three")
19. }
20. .width('100%')
21. .height('300vp')
22. .id("dynamicSwiper")
23. .backgroundColor(Color.Blue)
24. .autoPlay(true)
25. .onAppear(() => {
26. this.scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
27. })
28. }

30. Button("set frame")
31. .onClick(() => {
32. this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

34. if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
35. scenes.setFrameRateRange(this.ANIMATION);
36. }

38. if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
39. scenes.setFrameRateRange(this.GESTURE);
40. }
41. });
42. })
43. }
44. }
45. }
```

## openBindSheet12+

PhonePC/2in1TabletTVWearable

openBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions?: SheetOptions, targetId?: number): Promise<void>

创建并弹出以bindSheetContent作为内容的半模态页面，使用Promise异步回调。通过该接口弹出的半模态页面样式完全按照bindSheetContent中设置的样式显示。

说明

1. 使用该接口时，若未传入有效的targetId，则不支持设置SheetOptions.preferType为POPUP模式、不支持设置SheetOptions.mode为EMBEDDED模式。
2. 由于[updateBindSheet](arkts-apis-uicontext-uicontext.md#updatebindsheet12)和[closeBindSheet](arkts-apis-uicontext-uicontext.md#closebindsheet12)依赖bindSheetContent去更新或者关闭指定的半模态页面，开发者需自行维护传入的bindSheetContent。
3. 不支持设置SheetOptions.UIContext。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 半模态页面中显示的组件内容。 |
| sheetOptions | [SheetOptions](ts-universal-attributes-sheet-transition.md#sheetoptions) | 否 | 半模态页面样式。  **说明：**  1. 不支持设置SheetOptions.uiContext，该属性的值固定为当前实例的UIContext。  2. 若不传递targetId，则不支持设置SheetOptions.preferType为POPUP样式，若设置了POPUP样式则使用CENTER样式替代。  3. 若不传递targetId，则不支持设置SheetOptions.mode为EMBEDDED模式，默认为OVERLAY模式。  4. 其余属性的默认值参考[SheetOptions](ts-universal-attributes-sheet-transition.md#sheetoptions)文档。 |
| targetId | number | 否 | 需要绑定组件的ID，若不指定则不绑定任何组件。id不存在时返回错误码120004。在传入undefined时返回错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[半模态错误码](errorcode-bindsheet.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120002 | The bindSheetContent already exists. |
| 120004 | The targetId does not exist. |
| 120005 | The node of targetId is not in the component tree. |
| 120006 | The node of targetId is not a child of the page node or NavDestination node. |

**示例：**

```
1. import { FrameNode, ComponentContent } from "@kit.ArkUI";
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. let contentNode: ComponentContent<Params>;
13. let gUIContext: UIContext;

15. @Builder
16. function buildText(params: Params) {
17. Column() {
18. Text(params.text)
19. Button('Update BindSheet')
20. .fontSize(20)
21. .onClick(() => {
22. gUIContext.updateBindSheet(contentNode, {
23. backgroundColor: Color.Pink,
24. }, true)
25. .then(() => {
26. console.info('updateBindSheet success');
27. })
28. .catch((err: BusinessError) => {
29. console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
30. })
31. })

33. Button('Close BindSheet')
34. .fontSize(20)
35. .onClick(() => {
36. gUIContext.closeBindSheet(contentNode)
37. .then(() => {
38. console.info('closeBindSheet success');
39. })
40. .catch((err: BusinessError) => {
41. console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
42. })
43. })
44. }
45. }

47. @Entry
48. @Component
49. struct UIContextBindSheet {
50. @State message: string = 'BindSheet';

52. aboutToAppear() {
53. gUIContext = this.getUIContext();
54. contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
55. }

57. build() {
58. RelativeContainer() {
59. Column() {
60. Button('Open BindSheet')
61. .fontSize(20)
62. .onClick(() => {
63. let uiContext = this.getUIContext();
64. let uniqueId = this.getUniqueId();
65. let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
66. let targetId = frameNode?.getFirstChild()?.getUniqueId();
67. uiContext.openBindSheet(contentNode, {
68. height: SheetSize.MEDIUM,
69. backgroundColor: Color.Green,
70. title: { title: "Title", subtitle: "subtitle" }
71. }, targetId)
72. .then(() => {
73. console.info('openBindSheet success');
74. })
75. .catch((err: BusinessError) => {
76. console.error('openBindSheet error: ' + err.code + ' ' + err.message);
77. })
78. })
79. }
80. }
81. .height('100%')
82. .width('100%')
83. }
84. }
```

## updateBindSheet12+

PhonePC/2in1TabletTVWearable

updateBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>, sheetOptions: SheetOptions, partialUpdate?: boolean ): Promise<void>

更新bindSheetContent对应的半模态页面的样式，使用Promise异步回调。

说明

不支持更新SheetOptions.UIContext、SheetOptions.mode、回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 半模态页面中显示的组件内容。 |
| sheetOptions | [SheetOptions](ts-universal-attributes-sheet-transition.md#sheetoptions) | 是 | 半模态页面样式。  **说明：**  不支持更新SheetOptions.uiContext、SheetOptions.mode、回调函数。 |
| partialUpdate | boolean | 否 | 半模态页面更新方式, 默认值为false。  **说明：**  1. true为增量更新，保留当前值，更新SheetOptions中的指定属性。  2. false为全量更新，除SheetOptions中的指定属性，其他属性恢复默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[半模态错误码](errorcode-bindsheet.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120003 | The bindSheetContent cannot be found. |

**示例：**

```
1. import { FrameNode, ComponentContent } from "@kit.ArkUI";
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. let contentNode: ComponentContent<Params>;
13. let gUIContext: UIContext;

15. @Builder
16. function buildText(params: Params) {
17. Column() {
18. Text(params.text)
19. Button('Update BindSheet')
20. .fontSize(20)
21. .onClick(() => {
22. gUIContext.updateBindSheet(contentNode, {
23. backgroundColor: Color.Pink,
24. }, true)
25. .then(() => {
26. console.info('updateBindSheet success');
27. })
28. .catch((err: BusinessError) => {
29. console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
30. })
31. })

33. Button('Close BindSheet')
34. .fontSize(20)
35. .onClick(() => {
36. gUIContext.closeBindSheet(contentNode)
37. .then(() => {
38. console.info('closeBindSheet success');
39. })
40. .catch((err: BusinessError) => {
41. console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
42. })
43. })
44. }
45. }

47. @Entry
48. @Component
49. struct UIContextBindSheet {
50. @State message: string = 'BindSheet';

52. aboutToAppear() {
53. gUIContext = this.getUIContext();
54. contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
55. }

57. build() {
58. RelativeContainer() {
59. Column() {
60. Button('Open BindSheet')
61. .fontSize(20)
62. .onClick(() => {
63. let uiContext = this.getUIContext();
64. let uniqueId = this.getUniqueId();
65. let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
66. let targetId = frameNode?.getFirstChild()?.getUniqueId();
67. uiContext.openBindSheet(contentNode, {
68. height: SheetSize.MEDIUM,
69. backgroundColor: Color.Green,
70. title: { title: "Title", subtitle: "subtitle" }
71. }, targetId)
72. .then(() => {
73. console.info('openBindSheet success');
74. })
75. .catch((err: BusinessError) => {
76. console.error('openBindSheet error: ' + err.code + ' ' + err.message);
77. })
78. })
79. }
80. }
81. .height('100%')
82. .width('100%')
83. }
84. }
```

## closeBindSheet12+

PhonePC/2in1TabletTVWearable

closeBindSheet<T extends Object>(bindSheetContent: ComponentContent<T>): Promise<void>

关闭bindSheetContent对应的半模态页面，使用Promise异步回调。

说明

使用此接口关闭半模态页面时，不会触发shouldDismiss回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bindSheetContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 半模态页面中显示的组件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[半模态错误码](errorcode-bindsheet.md)错误码。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 120001 | The bindSheetContent is incorrect. |
| 120003 | The bindSheetContent cannot be found. |

**示例：**

```
1. import { FrameNode, ComponentContent } from "@kit.ArkUI";
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. let contentNode: ComponentContent<Params>;
13. let gUIContext: UIContext;

15. @Builder
16. function buildText(params: Params) {
17. Column() {
18. Text(params.text)
19. Button('Update BindSheet')
20. .fontSize(20)
21. .onClick(() => {
22. gUIContext.updateBindSheet(contentNode, {
23. backgroundColor: Color.Pink,
24. }, true)
25. .then(() => {
26. console.info('updateBindSheet success');
27. })
28. .catch((err: BusinessError) => {
29. console.error('updateBindSheet error: ' + err.code + ' ' + err.message);
30. })
31. })

33. Button('Close BindSheet')
34. .fontSize(20)
35. .onClick(() => {
36. gUIContext.closeBindSheet(contentNode)
37. .then(() => {
38. console.info('closeBindSheet success');
39. })
40. .catch((err: BusinessError) => {
41. console.error('closeBindSheet error: ' + err.code + ' ' + err.message);
42. })
43. })
44. }
45. }

47. @Entry
48. @Component
49. struct UIContextBindSheet {
50. @State message: string = 'BindSheet';

52. aboutToAppear() {
53. gUIContext = this.getUIContext();
54. contentNode = new ComponentContent(this.getUIContext(), wrapBuilder(buildText), new Params(this.message));
55. }

57. build() {
58. RelativeContainer() {
59. Column() {
60. Button('Open BindSheet')
61. .fontSize(20)
62. .onClick(() => {
63. let uiContext = this.getUIContext();
64. let uniqueId = this.getUniqueId();
65. let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
66. let targetId = frameNode?.getFirstChild()?.getUniqueId();
67. uiContext.openBindSheet(contentNode, {
68. height: SheetSize.MEDIUM,
69. backgroundColor: Color.Green,
70. title: { title: "Title", subtitle: "subtitle" }
71. }, targetId)
72. .then(() => {
73. console.info('openBindSheet success');
74. })
75. .catch((err: BusinessError) => {
76. console.error('openBindSheet error: ' + err.code + ' ' + err.message);
77. })
78. })
79. }
80. }
81. .height('100%')
82. .width('100%')
83. }
84. }
```

## isFollowingSystemFontScale13+

PhonePC/2in1TabletTVWearable

isFollowingSystemFontScale(): boolean

获取当前UI上下文是否跟随系统字体倍率。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前UI上下文是否跟随系统字体倍率。  true表示UI上下文跟随系统倍率，false表示UI上下文不跟随系统倍率。 |

**示例：**

参考[configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)，配置fontSizeScale的值为“followSystem”。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Button('isFollowingSystemFontScale').onClick(() => {
7. console.info('isFollowingSystemFontScale', this.getUIContext().isFollowingSystemFontScale());
8. });
9. }
10. }
11. }
```

## getMaxFontScale13+

PhonePC/2in1TabletTVWearable

getMaxFontScale(): number

获取当前UI上下文最大字体倍率。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前UI上下文最大字体倍率。 |

**示例：**

参考[configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)，配置fontSizeMaxScale的值为“1.75”。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Button('getMaxFontScale').onClick(() => {
7. console.info('getMaxFontScale', this.getUIContext().getMaxFontScale().toFixed(2));
8. });
9. }
10. }
11. }
```

## bindTabsToScrollable13+

PhonePC/2in1TabletTVWearable

bindTabsToScrollable(tabsController: TabsController, scroller: Scroller): void

绑定Tabs组件和可滚动容器组件（支持[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Grid](ts-container-grid.md)、[WaterFlow](ts-container-waterflow.md)），当滑动可滚动容器组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，上滑隐藏，下滑显示。一个TabsController可与多个Scroller绑定，一个Scroller也可与多个TabsController绑定。

说明

当多个可滚动容器组件绑定了同一个Tabs组件时，只要滑动任意一个可滚动容器组件，就会触发TabBar的显示或隐藏。且当任意一个可滚动容器组件滑动到底部时，会立即触发TabBar的显示动效。因此不建议同时触发多个可滚动容器组件的滑动。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](ts-container-tabs.md#tabscontroller) | 是 | Tabs组件的控制器。 |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。 |

**示例：**

```
1. @Entry
2. @Component
3. struct TabsExample {
4. private arr: string[] = [];
5. private parentTabsController: TabsController = new TabsController();
6. private childTabsController: TabsController = new TabsController();
7. private listScroller: Scroller = new Scroller();
8. private parentScroller: Scroller = new Scroller();
9. private childScroller: Scroller = new Scroller();

11. aboutToAppear(): void {
12. for (let i = 0; i < 20; i++) {
13. this.arr.push(i.toString());
14. }
15. let context = this.getUIContext();
16. context.bindTabsToScrollable(this.parentTabsController, this.listScroller);
17. context.bindTabsToScrollable(this.childTabsController, this.listScroller);
18. context.bindTabsToNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
19. }

21. aboutToDisappear(): void {
22. let context = this.getUIContext();
23. context.unbindTabsFromScrollable(this.parentTabsController, this.listScroller);
24. context.unbindTabsFromScrollable(this.childTabsController, this.listScroller);
25. context.unbindTabsFromNestedScrollable(this.parentTabsController, this.parentScroller, this.childScroller);
26. }

28. build() {
29. Tabs({ barPosition: BarPosition.End, controller: this.parentTabsController }) {
30. TabContent() {
31. Tabs({ controller: this.childTabsController }) {
32. TabContent() {
33. List({ space: 20, initialIndex: 0, scroller: this.listScroller }) {
34. ForEach(this.arr, (item: string) => {
35. ListItem() {
36. Text(item)
37. .width('100%')
38. .height(100)
39. .fontSize(16)
40. .textAlign(TextAlign.Center)
41. .borderRadius(10)
42. .backgroundColor(Color.Gray)
43. }
44. }, (item: string) => item)
45. }
46. .scrollBar(BarState.Off)
47. .width('90%')
48. .height('100%')
49. .contentStartOffset(56)
50. .contentEndOffset(52)
51. }.tabBar(SubTabBarStyle.of('顶部页签'))
52. }
53. .width('100%')
54. .height('100%')
55. .barOverlap(true) // 使TabBar叠加在TabContent上，当TabBar向上或向下隐藏后，原位置处不为空白
56. .clip(true) // 对超出Tabs组件范围的子组件进行裁剪，防止TabBar向上或向下隐藏后误触TabBar
57. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'scroller联动多个TabsController'))

59. TabContent() {
60. Scroll(this.parentScroller) {
61. List({ space: 20, initialIndex: 0, scroller: this.childScroller }) {
62. ForEach(this.arr, (item: string) => {
63. ListItem() {
64. Text(item)
65. .width('100%')
66. .height(100)
67. .fontSize(16)
68. .textAlign(TextAlign.Center)
69. .borderRadius(10)
70. .backgroundColor(Color.Gray)
71. }
72. }, (item: string) => item)
73. }
74. .scrollBar(BarState.Off)
75. .width('90%')
76. .height('100%')
77. .contentEndOffset(52)
78. .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST })
79. }
80. .width('100%')
81. .height('100%')
82. .scrollBar(BarState.Off)
83. .scrollable(ScrollDirection.Vertical)
84. .edgeEffect(EdgeEffect.Spring)
85. }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), '嵌套的scroller联动TabsController'))
86. }
87. .width('100%')
88. .height('100%')
89. .barOverlap(true) // 使TabBar叠加在TabContent上，当TabBar向上或向下隐藏后，原位置处不为空白
90. .clip(true) // 对超出Tabs组件范围的子组件进行裁剪，防止TabBar向上或向下隐藏后误触TabBar
91. }
92. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/z4ZvqMBUTM6DPsKDTKxsCQ/zh-cn_image_0000002589245747.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=1AB4192A721E3D482253F21023BF100E433DF2FDF7198968969CF7DAE0D38ADB)

## unbindTabsFromScrollable13+

PhonePC/2in1TabletTVWearable

unbindTabsFromScrollable(tabsController: TabsController, scroller: Scroller): void

解除Tabs组件和可滚动容器组件的绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](ts-container-tabs.md#tabscontroller) | 是 | Tabs组件的控制器。 |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。 |

**示例：**

参考[bindTabsToScrollable](arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)接口示例。

## bindTabsToNestedScrollable13+

PhonePC/2in1TabletTVWearable

bindTabsToNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

绑定Tabs组件和嵌套的可滚动容器组件（支持[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)、[Grid](ts-container-grid.md)、[WaterFlow](ts-container-waterflow.md)），当滑动父组件或子组件时，会触发所有与其绑定的Tabs组件的TabBar的显示和隐藏动效，上滑隐藏，下滑显示。一个TabsController可与多个嵌套的Scroller绑定，嵌套的Scroller也可与多个TabsController绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](ts-container-tabs.md#tabscontroller) | 是 | Tabs组件的控制器。 |
| parentScroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。 |
| childScroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。其对应组件为parentScroller对应组件的子组件，且组件间存在嵌套滚动关系。 |

**示例：**

参考[bindTabsToScrollable](arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)接口示例。

## unbindTabsFromNestedScrollable13+

PhonePC/2in1TabletTVWearable

unbindTabsFromNestedScrollable(tabsController: TabsController, parentScroller: Scroller, childScroller: Scroller): void

解除Tabs组件和嵌套的可滚动容器组件的绑定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tabsController | [TabsController](ts-container-tabs.md#tabscontroller) | 是 | Tabs组件的控制器。 |
| parentScroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。 |
| childScroller | [Scroller](ts-container-scroll.md#scroller) | 是 | 可滚动容器组件的控制器。其对应组件为parentScroller对应组件的子组件，且组件间存在嵌套滚动关系。 |

**示例：**

参考[bindTabsToScrollable](arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)接口示例。

## enableSwipeBack18+

PhonePC/2in1TabletTVWearable

enableSwipeBack(enabled: Optional<boolean>): void

设置是否支持应用内横向滑动返回上一级。

**元服务API：** 从API version 18 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | Optional<boolean> | 是 | 是否支持应用内横向滑动返回，默认值为true。  当值为true时，支持应用内横向滑动返回。  当值为false时，不支持应用内横向滑动返回。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. @State isEnable: boolean = true;

6. build() {
7. RelativeContainer() {
8. Button(`enable swipe back: ${this.isEnable}`).onClick(() => {
9. this.isEnable = !this.isEnable;
10. this.getUIContext().enableSwipeBack(this.isEnable);
11. })
12. }
13. .height('100%')
14. .width('100%')
15. }
16. }
```

## getTextMenuController16+

PhonePC/2in1TabletTVWearable

getTextMenuController(): TextMenuController

获取[TextMenuController](arkts-apis-uicontext-textmenucontroller.md)对象，可通过该对象控制文本选择菜单。

**元服务API：** 从API version 16 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextMenuController](arkts-apis-uicontext-textmenucontroller.md) | 获取TextMenuController对象。 |

**示例：**

参考[TextMenuController](arkts-apis-uicontext-textmenucontroller.md)接口示例。

## createUIContextWithoutWindow17+

PhonePC/2in1TabletTVWearable

static createUIContextWithoutWindow(context: common.UIAbilityContext | common.ExtensionContext): UIContext | undefined

创建一个不依赖窗口的UI实例，并返回其UI上下文。该接口所创建的UI实例是单例。

说明

返回的UI上下文只可用于创建[自定义节点](../harmonyos-guides/arkts-user-defined-node.md)，不能执行其他UI操作。

**元服务API：** 从API version 17 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | common.[ExtensionContext](js-apis-inner-application-extensioncontext.md) | 是 | [UIAbility](js-apis-app-ability-uiability.md)或[ExtensionAbility](js-apis-app-ability-extensionability.md)所对应的上下文环境。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UIContext | undefined | 创建的UI实例的上下文，创建失败时返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. The number of parameters is incorrect.  2. Invalid parameter type of context. |
| 100001 | Internal error. |

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { UIContext } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. let uiContext: UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
10. }

12. // ......
13. }
```

## destroyUIContextWithoutWindow17+

PhonePC/2in1TabletTVWearable

static destroyUIContextWithoutWindow(): void

销毁[createUIContextWithoutWindow](arkts-apis-uicontext-uicontext.md#createuicontextwithoutwindow17)创建的UI实例。

**元服务API：** 从API version 17 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { UIContext } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. let uiContext: UIContext | undefined = UIContext.createUIContextWithoutWindow(this.context);
10. UIContext.destroyUIContextWithoutWindow();
11. }

13. // ......
14. }
```

## dispatchKeyEvent15+

PhonePC/2in1TabletTVWearable

dispatchKeyEvent(node: number | string, event: KeyEvent): boolean

按键事件应分发给指定的组件。为了确保行为的可预测性，目标组件必须位于分发组件的子树中。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | number | string | 是 | 组件的id或者节点UniqueID。 |
| event | [KeyEvent](ts-universal-events-key.md#keyevent对象说明) | 是 | KeyEvent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 按键事件是否成功分发给指定的组件。  true表示分发成功，false表示分发失败。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. Row() {
7. Button('Button1').id('Button1').onKeyEvent((event) => {
8. console.info("Button1");
9. return true;
10. })
11. Button('Button2').id('Button2').onKeyEvent((event) => {
12. console.info("Button2");
13. return true;
14. })
15. }
16. .width('100%')
17. .height('100%')
18. .id('Row1')
19. .onKeyEventDispatch((event) => {
20. let context = this.getUIContext();
21. context.getFocusController().requestFocus('Button1');
22. return context.dispatchKeyEvent('Button1', event);
23. })

25. }
26. .height('100%')
27. .width('100%')
28. .onKeyEventDispatch((event) => {
29. if (event.type == KeyType.Down) {
30. let context = this.getUIContext();
31. context.getFocusController().requestFocus('Row1');
32. return context.dispatchKeyEvent('Row1', event);
33. }
34. return true;
35. })
36. }
37. }
```

## setPixelRoundMode18+

PhonePC/2in1TabletTVWearable

setPixelRoundMode(mode: PixelRoundMode): void

配置当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 是 | 像素取整模式。  默认值：PixelRoundMode.PIXEL\_ROUND\_ON\_LAYOUT\_FINISH |

**示例：**

```
1. // EntryAbility.ets
2. import { UIContext } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage) {

7. windowStage.loadContent('pages/Index', (err, data) => {
8. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
9. uiContext.setPixelRoundMode(PixelRoundMode.PIXEL_ROUND_ON_LAYOUT_FINISH);
10. });
11. }
12. }
```

## getPixelRoundMode18+

PhonePC/2in1TabletTVWearable

getPixelRoundMode(): PixelRoundMode

获取当前页面的像素取整模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelRoundMode](ts-appendix-enums.md#pixelroundmode18) | 当前页面的像素取整模式。 |

**示例：**

```
1. // EntryAbility.ets
2. import { UIContext } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility{
5. onWindowStageCreate(windowStage: window.WindowStage) {

7. windowStage.loadContent('pages/Index', (err, data) => {
8. let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
9. console.info("pixelRoundMode : " + uiContext.getPixelRoundMode().valueOf());
10. });
11. }
12. }
```

## setResourceManagerCacheMaxCountForHSP21+

PhonePC/2in1TabletTVWearable

static setResourceManagerCacheMaxCountForHSP(count: number): void

设置HSP资源管理对象缓存个数上限。

说明

如果缓存上限设置的太大，有内存开销过大的风险，建议合理配置。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 设置的资源缓存数量，取值范围为非负整数。 |

**错误码：**

以下错误码的详细介绍请参见[UI上下文错误码](errorcode-uicontext.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100101 | The parameter is less than 0. |
| 100102 | The parameter value cannot be a floating point number. |
| 100103 | The function cannot be called from a non main thread. |

**示例：**

```
1. // EntryAbility.ets
2. import { UIAbility } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { UIContext, window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. // Main window is created, set main page for this ability
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

11. windowStage.loadContent('pages/Index', (err, data) => {
12. if (err.code) {
13. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', err.message);
14. return;
15. }
16. UIContext.setResourceManagerCacheMaxCountForHSP(5);
17. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
18. });
19. }
20. }
```

## setImageCacheCount23+

PhonePC/2in1TabletTVWearable

setImageCacheCount(value: number): void

设置内存中缓存解码后图片的数量上限，以加快同源图片的再次加载速度。默认值为0，表示不缓存。缓存使用LRU策略，新图片加载超过上限时，会移除最久未使用的缓存。建议根据应用内存需求，合理设置缓存数量，避免内存使用过高。

setImageCacheCount方法需要在@Entry标记的页面，[onPageShow](ts-custom-component-lifecycle.md#onpageshow)或[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)里面设置才生效。

setImageCacheCount、setImageRawDataCacheSize和setImageFileCacheSize并不灵活，后续不继续演进。对于复杂情况，更推荐使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码后图片的缓存数量。  取值范围：[0, +∞) |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. onPageShow() {
6. // 设置解码后图片内存缓存上限为100张
7. this.getUIContext().setImageCacheCount(100);
8. console.info('Application onPageShow');
9. }
10. onDestroy() {
11. console.info('Application onDestroy');
12. }

14. build() {
15. Row(){
16. Image('https://www.example.com/xxx.png') // 请填写一个具体的网络图片地址
17. .width(200)
18. .height(50)
19. }.width('100%')
20. }
21. }
```

## setImageRawDataCacheSize23+

PhonePC/2in1TabletTVWearable

setImageRawDataCacheSize(value: number): void

设置内存中缓存解码前图片数据的大小上限，单位为字节，以加快再次加载同源图片的速度。默认值为0，表示不缓存。缓存使用LRU策略，新图片加载后，若解码前数据超过上限，会删除最久未使用的图片数据缓存。建议根据应用内存需求，设置合理的缓存上限，避免内存使用过高。

setImageRawDataCacheSize方法需要在@Entry标记的页面，[onPageShow](ts-custom-component-lifecycle.md#onpageshow)或[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)里面设置才生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码前图片数据的缓存大小，单位为字节。  取值范围：[0, +∞) |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. onPageShow() {
6. // 设置解码前图片数据内存缓存上限为100MB (100MB=100*1024*1024B=104857600B)
7. this.getUIContext().setImageRawDataCacheSize(104857600);
8. console.info('Application onPageShow');
9. }
10. onDestroy() {
11. console.info('Application onDestroy');
12. }

14. build() {
15. Row(){
16. Image('https://www.example.com/xxx.png') // 请填写一个具体的网络图片地址
17. .width(200)
18. .height(50)
19. }.width('100%')
20. }
21. }
```

## getMagnifier22+

PhonePC/2in1TabletTVWearable

getMagnifier(): Magnifier

获取[Magnifier](arkts-apis-uicontext-magnifier.md)对象，可控制放大镜显示和隐藏。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Magnifier](arkts-apis-uicontext-magnifier.md) | Magnifier对象，可用于控制放大镜的显示和隐藏。 |

**示例：**

参考[Magnifier](arkts-apis-uicontext-magnifier.md)的[bind](arkts-apis-uicontext-magnifier.md#bind)接口示例。

## setCustomKeyboardContinueFeature23+

PhonePC/2in1TabletTVWearable

setCustomKeyboardContinueFeature(feature: CustomKeyboardContinueFeature): void

设置自定义键盘之间切换时，是否接续。

设置为接续，切换输入框时，自定义键盘不会收起和重新拉起。

设置为不接续，切换输入框时，自定义键盘会收起并重新拉起。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feature | [CustomKeyboardContinueFeature](arkts-apis-uicontext-e.md#customkeyboardcontinuefeature23) | 是 | 自定义键盘之间切换时是否接续。  默认值：CustomKeyboardContinueFeature.DISABLED，即不接续。 |

**示例：**

```
1. // xxx.ets
2. import { CustomKeyboardContinueFeature } from '@ohos.arkui.UIContext';

4. @Entry
5. @Component
6. struct Index {
7. controller: TextInputController = new TextInputController();
8. controller2: TextInputController = new TextInputController();
9. @State inputValue: string = '';
10. @State inputValue2: string = '';
11. @State supportAvoidance: boolean = true;
12. @State isValue: CustomKeyboardContinueFeature = CustomKeyboardContinueFeature.DISABLED;
13. @State str: string = '否';

15. // 自定义键盘组件
16. @Builder
17. CustomKeyboardBuilder() {
18. Column() {
19. Row() {
20. Button('x').onClick(() => {
21. // 关闭自定义键盘
22. this.controller.stopEditing();
23. }).margin(10)
24. Button('delete').onClick(() => {
25. this.inputValue = this.inputValue.slice(0, -1);
26. }).margin(10)
27. }

29. Grid() {
30. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
31. GridItem() {
32. Button(item + '')
33. .width(110).onClick(() => {
34. this.inputValue += item;
35. })
36. }
37. })
38. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
39. }.backgroundColor('rgb(213, 213, 213)').height(300)
40. }

42. // 自定义键盘组件
43. @Builder
44. CustomKeyboardBuilder2() {
45. Column() {
46. Row() {
47. Button('x').onClick(() => {
48. // 关闭自定义键盘
49. this.controller2.stopEditing();
50. }).margin(10)
51. Button('delete').onClick(() => {
52. this.inputValue2 = this.inputValue2.slice(0, -1);
53. }).margin(10)
54. }

56. Grid() {
57. ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
58. GridItem() {
59. Button(item + '')
60. .width(110).onClick(() => {
61. this.inputValue2 += item;
62. })
63. }
64. })
65. }.maxCount(3).columnsGap(10).rowsGap(10).padding(5)
66. }.backgroundColor('rgb(227, 248, 249)').height(150)
67. }

69. build() {
70. Scroll() {
71. Column() {
72. Button('是否接续：' + this.str).onClick(() => {
73. if (this.isValue == CustomKeyboardContinueFeature.ENABLED) {
74. this.isValue = CustomKeyboardContinueFeature.DISABLED
75. this.str = '否'
76. } else {
77. this.isValue = CustomKeyboardContinueFeature.ENABLED
78. this.str = '是'
79. }
80. this.getUIContext().setCustomKeyboardContinueFeature(this.isValue);
81. }).fontSize(20).width('80%').key('button')

83. TextInput({
84. placeholder: 'TextInput1 bind CustomKeyboardBuilder',
85. controller: this.controller,
86. text: this.inputValue
87. })// 绑定自定义键盘
88. .customKeyboard(this.CustomKeyboardBuilder(), { supportAvoidance: this.supportAvoidance })
89. .margin(10)
90. .border({ width: 1 })
91. TextInput({
92. placeholder: 'TextInput2 bind CustomKeyboardBuilder2',
93. controller: this.controller2,
94. text: this.inputValue2
95. })// 绑定自定义键盘
96. .customKeyboard(this.CustomKeyboardBuilder2(), { supportAvoidance: this.supportAvoidance })
97. .margin(10)
98. .border({ width: 1 })
99. }
100. }
101. }
102. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Lg0IIVZ_Rm-WkIWH92xUlQ/zh-cn_image_0000002558765936.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055036Z&HW-CC-Expire=86400&HW-CC-Sign=BFB5FD9BBA6666AC180CB0B1A8A2549952A2E30A0529C8E54FA6C10B5F706BBA)
