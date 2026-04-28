---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle
title: 自定义组件的生命周期
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件的生命周期
category: harmonyos-references
scraped_at: 2026-04-28T08:02:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fbec532883def1504724c8ac5d783f65e1d39859e30857f5fa886d3ea7748fd6
---

自定义组件的生命周期回调函数用于通知用户该自定义组件的生命周期，这些回调函数是私有的，在运行时由开发框架在特定的时间进行调用，不能从应用程序中手动调用这些回调函数。不要在多个窗口复用同一个自定义组件节点，其生命周期可能会紊乱。

说明

* 本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 允许在生命周期函数中使用Promise和异步回调函数，比如网络资源获取，定时器设置等。

## build

PhonePC/2in1TabletTVWearable

build(): void

build()函数用于定义自定义组件的声明式UI描述，自定义组件必须定义build()函数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## aboutToAppear

PhonePC/2in1TabletTVWearable

aboutToAppear?(): void

aboutToAppear函数在创建自定义组件的新实例后，在其build()函数执行前调用。允许在aboutToAppear函数中改变[状态变量](../harmonyos-guides/arkts-state-management-glossary.md#状态变量state-variables)，更改将在后续执行build()函数中生效。实现[自定义布局](ts-custom-component-layout.md)的自定义组件的aboutToAppear生命周期在布局过程中触发。具体使用说明，详见[自定义组件生命周期指南](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。

说明

* 在该回调函数内，建议仅执行当前节点组件的初始化逻辑，避免高耗时操作阻塞主线程。对于高耗时操作，推荐采用缓存或异步方案替代。最佳实践请参考[UI组件性能优化-避免在自定义组件的生命周期内执行高耗时操作](../best-practices/bpta-ui-component-performance-optimization.md#section18755173594714)。
* 在需要频繁创建和销毁组件的场景中，将会频繁调用该回调函数。最佳实践请参考[主线程耗时操作优化指导-组件生命周期回调](../best-practices/bpta-time-optimization-of-the-main-thread.md#section418843713435)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onDidBuild12+

PhonePC/2in1TabletTVWearable

onDidBuild?(): void

onDidBuild函数在自定义组件的build()函数执行后调用，开发者可以在这个阶段实现埋点数据上报等不影响实际UI的功能。具体使用说明，详见[自定义组件生命周期指南](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## aboutToDisappear

PhonePC/2in1TabletTVWearable

aboutToDisappear?(): void

aboutToDisappear函数在自定义组件析构销毁时执行。不允许在aboutToDisappear函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。具体使用说明，详见[自定义组件生命周期指南](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。不建议在aboutToDisappear函数调用后再触发例如[自定义弹窗的创建](ts-methods-custom-dialog-box.md#open)等逻辑，这可能会因为组件树信息丢失导致应用行为异常，例如[@Consume](../harmonyos-guides/arkts-provide-and-consume.md)找不到对应的[@Provide](../harmonyos-guides/arkts-provide-and-consume.md)、弹窗内白屏不显示组件等。

说明

在需要频繁创建和销毁组件的场景中，将会频繁调用该回调函数。最佳实践请参考[主线程耗时操作优化指导-组件生命周期回调](../best-practices/bpta-time-optimization-of-the-main-thread.md#section418843713435)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onPageShow

PhonePC/2in1TabletTVWearable

onPageShow?(): void

router路由页面（即[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件）每次显示时触发一次，包括路由跳转、应用进入前台等场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onPageHide

PhonePC/2in1TabletTVWearable

onPageHide?(): void

router路由页面（即[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件）每次隐藏时触发一次，包括路由跳转、应用进入后台等场景。

说明

在该回调函数内，建议避免执行高耗时操作阻塞主线程造成卡顿。对于高耗时操作例如相机资源释放，推荐使用异步方案替代。最佳实践请参考[优化应用时延问题-延迟执行资源释放操作](../best-practices/bpta-application-latency-optimization-cases.md#section8783201923819)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onBackPress

PhonePC/2in1TabletTVWearable

onBackPress?(): void | boolean

在router路由页面（即[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件）生效，当用户点击返回按钮时触发。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | boolean | 返回按钮动作。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct IndexComponent {
5. @State textColor: Color = Color.Black;

7. onPageShow() {
8. this.textColor = Color.Blue;
9. console.info('IndexComponent onPageShow');
10. }

12. onPageHide() {
13. this.textColor = Color.Transparent;
14. console.info('IndexComponent onPageHide');
15. }

17. onBackPress() {
18. this.textColor = Color.Red;
19. console.info('IndexComponent onBackPress');
20. }

22. build() {
23. Column() {
24. Text('Hello World')
25. .fontColor(this.textColor)
26. .fontSize(30)
27. .margin(30)
28. }.width('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/vcfnTRXuQLK7qGt8PovBYA/zh-cn_image_0000002583440135.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=F481ED77FB06B5D3B52E61CD0A39FECCCC35F68392CA52BADF344BF647A1FF8D)

## onNewParam19+

PhonePC/2in1TabletTVWearable

onNewParam?(param: ESObject): void

该回调仅生效于由[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的、作为[router](js-apis-router.md)路由页面存在的自定义组件。当之前存在于路由栈中的页面，通过单实例模式[RouterMode](js-apis-router.md#routermode9)移动到栈顶时触发该回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | ESObject | 是 | 路由跳转时传递到目标页面的数据。 |

```
1. // pages/Index.ets
2. import { router } from '@kit.ArkUI';

4. export class routerParam {
5. msg: string = '__NA__';

7. constructor(msg: string) {
8. this.msg = msg;
9. }
10. }

12. @Entry
13. @Component
14. struct Index {
15. aboutToAppear(): void {
16. console.info('onNewParam', 'Index aboutToAppear');
17. }

19. onNewParam(param: ESObject) {
20. console.info('onNewParam', 'Index onNewParam, param: ' + JSON.stringify(param));
21. }

23. build() {
24. Column() {
25. Button('push pageOne Standard')
26. .margin(10)
27. .onClick(() => {
28. this.getUIContext().getRouter().pushUrl({
29. url: 'pages/PageOne',
30. params: new routerParam('push pageOne Standard')
31. }, router.RouterMode.Standard);
32. })
33. Button('push pageOne Single')
34. .margin(10)
35. .onClick(() => {
36. this.getUIContext().getRouter().pushUrl({
37. url: 'pages/PageOne',
38. params: new routerParam('push pageOne Single')
39. }, router.RouterMode.Single)
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. }
```

```
1. // pages/PageOne.ets
2. import { router } from '@kit.ArkUI';
3. import { routerParam } from './Index';

5. @Entry
6. @Component
7. struct PageOne {
8. aboutToAppear(): void {
9. console.info('onNewParam', 'PageOne aboutToAppear');
10. }

12. onNewParam(param: ESObject) {
13. console.info('onNewParam', 'PageOne onNewParam, param: ' + JSON.stringify(param));
14. }

16. build() {
17. Column() {
18. Button('push Index Standard')
19. .margin(10)
20. .onClick(() => {
21. this.getUIContext().getRouter().pushUrl({
22. url: 'pages/Index',
23. params: new routerParam('push Index Standard')
24. }, router.RouterMode.Standard);
25. })
26. Button('push Index Single')
27. .margin(10)
28. .onClick(() => {
29. this.getUIContext().getRouter().pushUrl({
30. url: 'pages/Index',
31. params: new routerParam('push Index Single')
32. }, router.RouterMode.Single)
33. })
34. }
35. .width('100%')
36. .height('100%')
37. }
38. }
```

## aboutToReuse10+

PhonePC/2in1TabletTVWearable

aboutToReuse?(params: Record<string, Object | undefined | null>): void

当一个可复用的自定义组件从复用缓存中重新加入到节点树时，触发aboutToReuse生命周期回调，并将组件的构造参数传递给aboutToReuse。

说明

* [避免对@Link/@ObjectLink/@Prop等自动更新的状态变量，在aboutToReuse()中重复赋值](../best-practices/bpta-component-reuse.md#section7441712174414)。
* 在滑动场景中，使用组件复用通常需要用该回调函数去更新组件的状态变量，因此在该回调函数中应避免耗时操作，否则会导致丢帧卡顿。最佳实践请参考[主线程耗时操作优化指导-组件复用回调](../best-practices/bpta-time-optimization-of-the-main-thread.md#section20815336174316)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Record<string, Object | undefined | null> | 是 | 自定义组件的构造参数。 |

```
1. // xxx.ets
2. export class Message {
3. value: string | undefined;

5. constructor(value: string) {
6. this.value = value
7. }
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State switch: boolean = true

15. build() {
16. Column() {
17. Button('Hello World')
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. this.switch = !this.switch
22. })
23. if (this.switch) {
24. Child({ message: new Message('Child') })
25. }
26. }
27. .height("100%")
28. .width('100%')
29. }
30. }

32. @Reusable
33. @Component
34. struct Child {
35. @State message: Message = new Message('AboutToReuse');

37. aboutToReuse(params: Record<string, ESObject>) {
38. console.info("Recycle Child")
39. this.message = params.message as Message
40. }

42. build() {
43. Column() {
44. Text(this.message.value)
45. .fontSize(20)
46. }
47. .borderWidth(2)
48. .height(100)
49. }
50. }
```

## aboutToReuse18+

PhonePC/2in1TabletTVWearable

aboutToReuse?(): void

当一个状态管理V2的可复用自定义组件从复用池被取出重新加入到节点树时，触发aboutToReuse生命周期回调。

详细内容请参考[@ReusableV2](../harmonyos-guides/arkts-new-reusablev2.md)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local condition: boolean = true;
5. build() {
6. Column() {
7. Button('回收/复用').onClick(()=>{this.condition=!this.condition;}) // 点击切换回收/复用状态
8. if (this.condition) {
9. ReusableV2Component()
10. }
11. }
12. }
13. }
14. @ReusableV2
15. @ComponentV2
16. struct ReusableV2Component {
17. @Local message: string = 'Hello World';
18. aboutToReuse() {
19. console.info('ReusableV2Component aboutToReuse'); // 复用时被调用
20. }
21. build() {
22. Column() {
23. Text(this.message)
24. }
25. }
26. }
```

## aboutToRecycle10+

PhonePC/2in1TabletTVWearable

aboutToRecycle?(): void

组件的生命周期回调，在可复用组件从组件树上被加入到复用缓存之前调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

```
1. // xxx.ets
2. export class Message {
3. value: string | undefined;

5. constructor(value: string) {
6. this.value = value;
7. }
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State switch: boolean = true;

15. build() {
16. Column() {
17. Button('Hello World')
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. this.switch = !this.switch;
22. })
23. if (this.switch) {
24. Child({ message: new Message('Child') })
25. }
26. }
27. .height("100%")
28. .width('100%')
29. }
30. }

32. @Reusable
33. @Component
34. struct Child {
35. @State message: Message = new Message('AboutToReuse');

37. aboutToReuse(params: Record<string, ESObject>) {
38. console.info("Reuse Child");
39. this.message = params.message as Message;
40. }

42. aboutToRecycle() {
43. // 这里可以释放比较占内存的内容或其他非必要资源引用，避免一直占用内存，引发内存泄漏
44. console.info("Recycle Child,child进入复用池中");
45. }

47. build() {
48. Column() {
49. Text(this.message.value)
50. .fontSize(20)
51. }
52. .borderWidth(2)
53. .height(100)
54. }
55. }
```

## onWillApplyTheme12+

PhonePC/2in1TabletTVWearable

onWillApplyTheme?(theme: Theme): void

onWillApplyTheme函数用于获取当前组件上下文的Theme对象，在创建自定义组件的新实例后，在执行其build()函数之前执行。允许在onWillApplyTheme函数中改变状态变量，更改将在后续执行build()函数中生效。

说明

从API version 18开始，该接口支持在状态管理V2组件中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| theme | [Theme](ts-custom-component-lifecycle.md#theme12) | 是 | 自定义组件当前生效的Theme对象。 |

## Theme12+

PhonePC/2in1TabletTVWearable

type Theme = Theme

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Theme](js-apis-arkui-theme.md#theme) | 自定义组件当前生效的Theme对象。 |

V1：

```
1. // xxx.ets
2. import { CustomTheme, CustomColors, Theme, ThemeControl } from '@kit.ArkUI';

4. class BlueColors implements CustomColors {
5. fontPrimary = Color.White;
6. backgroundPrimary = Color.Blue;
7. brand = Color.Blue; // 品牌色
8. }

10. class PageCustomTheme implements CustomTheme {
11. colors?: CustomColors;

13. constructor(colors: CustomColors) {
14. this.colors = colors;
15. }
16. }
17. const BlueColorsTheme = new PageCustomTheme(new BlueColors());
18. // setDefaultTheme应该在应用入口页面调用或者在Ability中调用。
19. ThemeControl.setDefaultTheme(BlueColorsTheme);

21. @Entry
22. @Component
23. struct IndexComponent {
24. @State textColor: ResourceColor = $r('sys.color.font_primary');
25. @State columnBgColor: ResourceColor = $r('sys.color.background_primary');

27. // onWillApplyTheme中可获取当前组件上下文的Theme对象。此处在onWillApplyTheme中将状态变量textColor、columnBgColor，赋值为当前使用的Theme对象（BlueColorsTheme）中的配色。
28. onWillApplyTheme(theme: Theme) {
29. this.textColor = theme.colors.fontPrimary;
30. this.columnBgColor = theme.colors.backgroundPrimary;
31. console.info('IndexComponent onWillApplyTheme');
32. }

34. build() {
35. Column() {
36. // 组件初始值配色样式
37. Column() {
38. Text('Hello World')
39. .fontColor($r('sys.color.font_primary'))
40. .fontSize(30)
41. }
42. .width('100%')
43. .height('25%')
44. .borderRadius('10vp')
45. .backgroundColor($r('sys.color.background_primary'))

47. // 组件颜色生效为onWillApplyTheme中配置颜色。
48. Column() {
49. Text('onWillApplyTheme')
50. .fontColor(this.textColor)
51. .fontSize(30)
52. Text('Hello World')
53. .fontColor(this.textColor)
54. .fontSize(30)
55. }
56. .width('100%')
57. .height('25%')
58. .borderRadius('10vp')
59. .backgroundColor(this.columnBgColor)
60. }
61. .padding('16vp')
62. .backgroundColor('#dcdcdc')
63. .width('100%')
64. .height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/2M6tf3ydRy69hHwwwxKBIA/zh-cn_image_0000002552960090.png?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=3E0204AE08413F4DF7C8C4878387AAF8935E66A9253FC76F559D7972CAA023AE)

V2：

```
1. import { CustomTheme, CustomColors, Theme, ThemeControl } from '@kit.ArkUI';

3. class BlueColors implements CustomColors {
4. fontPrimary = Color.White;
5. backgroundPrimary = Color.Blue;
6. brand = Color.Blue; // 品牌色
7. }

9. class PageCustomTheme implements CustomTheme {
10. colors?: CustomColors;

12. constructor(colors: CustomColors) {
13. this.colors = colors;
14. }
15. }

17. const BlueColorsTheme = new PageCustomTheme(new BlueColors());
18. // setDefaultTheme应该在应用入口页面调用或者在Ability中调用。
19. ThemeControl.setDefaultTheme(BlueColorsTheme);

21. @Entry
22. @ComponentV2
23. struct IndexComponent {
24. @Local textColor: ResourceColor = $r('sys.color.font_primary');
25. @Local columnBgColor: ResourceColor = $r('sys.color.background_primary');

27. // onWillApplyTheme中可获取当前组件上下文的Theme对象。此处在onWillApplyTheme中将状态变量textColor、columnBgColor，赋值为当前使用的Theme对象（BlueColorsTheme）中的配色。
28. onWillApplyTheme(theme: Theme) {
29. this.textColor = theme.colors.fontPrimary;
30. this.columnBgColor = theme.colors.backgroundPrimary;
31. console.info('IndexComponent onWillApplyTheme');
32. }

34. build() {
35. Column() {
36. // 组件初始值配色样式
37. Column() {
38. Text('Hello World')
39. .fontColor($r('sys.color.font_primary'))
40. .fontSize(30)
41. }
42. .width('100%')
43. .height('25%')
44. .borderRadius('10vp')
45. .backgroundColor($r('sys.color.background_primary'))

47. // 组件颜色生效为onWillApplyTheme中配置颜色。
48. Column() {
49. Text('onWillApplyTheme')
50. .fontColor(this.textColor)
51. .fontSize(30)
52. Text('Hello World')
53. .fontColor(this.textColor)
54. .fontSize(30)
55. }
56. .width('100%')
57. .height('25%')
58. .borderRadius('10vp')
59. .backgroundColor(this.columnBgColor)
60. }
61. .padding('16vp')
62. .backgroundColor('#dcdcdc')
63. .width('100%')
64. .height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Dzd3SlISR-aF_-4sgA9MSA/zh-cn_image_0000002583480091.png?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=76A960CF010E8FC7721B22CB5A8490321C3EC34DD91E8BAB2903FD6813E23488)

## pageTransition9+

PhonePC/2in1TabletTVWearable

pageTransition?(): void

进入此页面或移动到其他页面时实现动画。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onFormRecycle11+

PhonePC/2in1TabletTVWearable

onFormRecycle?(): string

onFormRecycle回调函数在卡片回收时执行，卡片提供方可以返回需要卡片管理服务代保存的数据，在卡片恢复时通过[onFormRecover](ts-custom-component-lifecycle.md#onformrecover11)接口传给卡片提供方。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回卡片提供方需要卡片管理服务代保存的数据。 |

**示例：**

```
1. @Entry
2. @Component
3. struct WidgetCard {
4. readonly title: string = 'Hello World';
5. readonly actionType: string = 'router';
6. readonly abilityName: string = 'EntryAbility';
7. readonly message: string = 'add detail';
8. readonly fullWidthPercent: string = '100%';
9. readonly fullHeightPercent: string = '100%';

11. onFormRecycle(): string {
12. let formId: string = "1859635745"
13. console.info("card is recycled, formID: " + formId);
14. return formId;
15. }

17. onFormRecover(statusData: string): void {
18. console.info("card has been restored, formID: " + statusData);
19. }

21. build() {
22. Row() {
23. Column() {
24. Text(this.title)
25. .fontSize($r('app.float.font_size'))
26. .fontWeight(FontWeight.Medium)
27. .fontColor($r('sys.color.font'))
28. }
29. .width(this.fullWidthPercent)
30. }
31. .height(this.fullHeightPercent)
32. .backgroundColor($r('sys.color.comp_background_primary'))
33. .onClick(() => {
34. postCardAction(this, {
35. action: this.actionType,
36. abilityName: this.abilityName,
37. params: {
38. message: this.message
39. }
40. });
41. })
42. }
43. }
```

## onFormRecover11+

PhonePC/2in1TabletTVWearable

onFormRecover?(statusData: string): void

onFormRecover回调函数在卡片恢复时执行，卡片提供方可以拿到卡片回收时卡片管理服务代保存的数据，该数据可以通过[onFormRecycle](ts-custom-component-lifecycle.md#onformrecycle11)卡片回收回调函数保存到卡片管理服务。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| statusData | string | 是 | 卡片回收时卡片管理服务代保存的数据。 |

**示例：**

```
1. @Entry
2. @Component
3. struct WidgetCard {
4. readonly title: string = 'Hello World';
5. readonly actionType: string = 'router';
6. readonly abilityName: string = 'EntryAbility';
7. readonly message: string = 'add detail';
8. readonly fullWidthPercent: string = '100%';
9. readonly fullHeightPercent: string = '100%';

11. onFormRecycle(): string {
12. let formId: string = "1859635745"
13. console.info("card is recycled, formID: " + formId);
14. return formId;
15. }

17. onFormRecover(statusData: string): void {
18. console.info("card has been restored, formID: " + statusData);
19. }

21. build() {
22. Row() {
23. Column() {
24. Text(this.title)
25. .fontSize($r('app.float.font_size'))
26. .fontWeight(FontWeight.Medium)
27. .fontColor($r('sys.color.font'))
28. }
29. .width(this.fullWidthPercent)
30. }
31. .height(this.fullHeightPercent)
32. .backgroundColor($r('sys.color.comp_background_primary'))
33. .onClick(() => {
34. postCardAction(this, {
35. action: this.actionType,
36. abilityName: this.abilityName,
37. params: {
38. message: this.message
39. }
40. });
41. })
42. }
43. }
```
