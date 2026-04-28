---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog
title: 不依赖UI组件的全局自定义弹出框 (openCustomDialog)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 不依赖UI组件的全局自定义弹出框 (openCustomDialog)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97f9f48b5db68137ac4183ccd56e51924aed05428ea2a19f110ab6e2d9917eb7
---

在广告、中奖、警告、软件更新等与用户交互响应操作的场景下，可以使用UIContext中获取到的PromptAction对象提供的[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口来实现自定义弹出框。相较于[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)优势点在于页面解耦，支持[动态刷新](../harmonyos-references/js-apis-arkui-componentcontent.md#update)。

说明

弹出框（openCustomDialog）存在两种入参方式创建自定义弹出框：

* openCustomDialog（传参为ComponentContent形式）：通过ComponentContent封装内容可以与UI界面解耦，调用更加灵活，可以满足开发者的封装诉求。具有较高的灵活性，弹出框样式完全自定义，并且在弹出框打开后可以使用updateCustomDialog方法动态更新弹出框的参数。
* openCustomDialog（传参为builder形式）：相对于ComponentContent，builder必须要与上下文做绑定，与UI存在一定耦合。此方法有默认的弹出框样式，适合于开发者想要实现与系统弹窗默认风格一致的效果。

本文介绍通过入参形式为ComponentContent创建自定义弹出框，传builder形式的弹出框使用方法可参考[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)。

弹出框（openCustomDialog）默认为模态弹窗且有蒙层，不可与蒙层下方控件进行交互（不支持点击和手势等向下透传）。可以通过配置[promptAction.BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)类型中的isModal属性来实现模态和非模态弹窗，详细说明可参考[弹窗的种类](arkts-dialog-overview.md#弹窗的种类)。

当isModal为true时，弹出框为模态弹窗，且弹窗周围的蒙层区不支持透传。isModal为false时，弹出框为非模态弹窗，且弹窗周围的蒙层区可以透传。因此如果需要同时允许弹出框的交互和弹出框外页面的交互行为，需要将弹出框设置为非模态。

## 生命周期

弹出框提供了生命周期函数用于通知用户该弹出框的生命周期。生命周期的触发时序依次为：onWillAppear -> onDidAppear -> onWillDisappear -> onDidDisappear。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onDidAppear | () => void | 弹出框弹出后的事件回调。 |
| onDidDisappear | () => void | 弹出框消失后的事件回调。 |
| onWillAppear | () => void | 弹出框显示动效前的事件回调。 |
| onWillDisappear | () => void | 弹出框退出动效前的事件回调。 |

## 自定义弹出框的打开与关闭

说明

详细变量定义请参考[完整示例](arkts-uicontext-custom-dialog.md#完整示例)。

1. 创建ComponentContent。

   ComponentContent用于定义自定义弹出框的内容。其中，wrapBuilder(buildText)封装自定义组件，new Params(this.message)是自定义组件的入参，可以缺省，也可以传入基础数据类型。

   ```
   1. private contentNode: ComponentContent<Object> =
   2. new ComponentContent(this.ctx, wrapBuilder(buildText), new Params(this.message));
   ```

   [OpenDialogAndUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/opencustomdialog/OpenDialogAndUpdate.ets#L48-L51)
2. 打开自定义弹出框。

   调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口打开的弹出框默认customStyle为true，即弹出框的内容样式完全按照contentNode自定义样式显示。

   ```
   1. PromptActionClassNew.ctx.getPromptAction().openCustomDialog(PromptActionClassNew.contentNode, PromptActionClassNew.options)
   2. .then(() => {
   3. hilog.info(DOMAIN, 'testTag', 'testTag', 'OpenCustomDialog complete.');
   4. })
   5. .catch((error: BusinessError) => {
   6. let message = (error as BusinessError).message;
   7. let code = (error as BusinessError).code;
   8. hilog.error(DOMAIN, 'testTag', 'testTag', 'OpenCustomDialog args error code is ${code}, message is ${message}');
   9. })
   ```

   [PromptActionClassNew.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/common/PromptActionClassNew.ts#L42-L52)
3. 关闭自定义弹出框。

   由于[closeCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closecustomdialog12)接口需要传入待关闭弹出框对应的ComponentContent。因此，如果需要在弹出框中设置关闭方法，则可参考完整示例封装静态方法来实现。

   关闭弹出框之后若需要释放对应的ComponentContent，则需要调用ComponentContent的[dispose](../harmonyos-references/js-apis-arkui-componentcontent.md#dispose)方法。

   ```
   1. PromptActionClassNew.ctx.getPromptAction().closeCustomDialog(PromptActionClassNew.contentNode)
   2. .then(() => {
   3. hilog.info(DOMAIN, 'testTag', 'testTag', 'CloseCustomDialog complete.g complete.');
   4. if (this.contentNode !== null) {
   5. this.contentNode.dispose();   // 释放contentNode
   6. }
   7. })
   8. .catch((error: BusinessError) => {
   9. let message = (error as BusinessError).message;
   10. let code = (error as BusinessError).code;
   11. hilog.error(DOMAIN, 'testTag', 'testTag', 'CloseCustomDialog args error code is ${code}, message is ${message}');
   12. })
   ```

   [PromptActionClassNew.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/common/PromptActionClassNew.ts#L72-L85)

## 更新自定义弹出框的内容

ComponentContent与[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)有相同的使用限制，不支持自定义组件使用[@Reusable](arkts-reusable.md)、[@Link](arkts-link.md)、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)等装饰器，来同步弹出框弹出的页面与ComponentContent中自定义组件的状态。因此，若需要更新弹出框中自定义组件的内容可以通过ComponentContent提供的update方法来实现。

```
1. this.contentNode.update(new Params('update'))
```

## 更新自定义弹出框的属性

通过updateCustomDialog可以动态更新弹出框的属性。目前支持更新弹出框的对齐方式、基于对齐方式的偏移量、是否点击蒙层自动关闭以及蒙层颜色，对应的属性分别为[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中的alignment、offset、autoCancel和maskColor。

更新属性时，未设置的属性会恢复为默认值。例如，初始设置{ alignment: DialogAlignment.Top, offset: { dx: 0, dy: 50 } }，更新时设置{ alignment: DialogAlignment.Bottom }，则初始设置的offset: { dx: 0, dy: 50 }不会保留，会恢复为默认值。

```
1. PromptActionClassNew.ctx.getPromptAction().updateCustomDialog(PromptActionClassNew.contentNode, options)
2. .then(() => {
3. hilog.info(DOMAIN, 'testTag', 'testTag', 'UpdateCustomDialog complete.');
4. })
5. .catch((error: BusinessError) => {
6. let message = (error as BusinessError).message;
7. let code = (error as BusinessError).code;
8. hilog.error(DOMAIN, 'testTag', 'testTag', 'UpdateCustomDialog args error code is ${code}, message is ${message}');
9. })
```

[PromptActionClassNew.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/common/PromptActionClassNew.ts#L91-L101)

## 为弹出框内容和蒙层设置不同的动画效果

当弹出框出现时，内容与蒙层显示动效一致。若开发者希望为弹出框内容及蒙层设定不同动画效果，从API version 19开始，可通过[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中dialogTransition和maskTransition属性单独配置弹窗内容与蒙层的动画。具体的动画效果请参考[组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)。

说明

当isModal为true时，蒙层将显示，此时可以设置蒙层的动画效果；否则，maskTransition将不生效。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. @Entry
7. @Component
8. export struct CustomDialogComponentWithTransition {
9. private customDialogComponentId: number = 0

11. @Builder
12. customDialogComponent() {
13. Row({ space: 50 }) {
14. // 请将$r('app.string.this_is_a_window')替换为实际资源文件，在本示例中该资源文件的value值为"这是一个弹窗"
15. Button($r('app.string.this_is_a_window'))
16. }.height(200).padding(5)
17. }

19. build() {
20. NavDestination() {
21. Row() {
22. Row({ space: 20 }) {
23. // 请将$r('app.string.open_windows')替换为实际资源文件，在本示例中该资源文件的value值为"打开弹窗"
24. Text($r('app.string.open_windows'))
25. .fontSize(30)
26. .onClick(() => {
27. this.getUIContext()
28. .getPromptAction()
29. .openCustomDialog({
30. builder: () => {
31. this.customDialogComponent()
32. },
33. isModal: true,
34. showInSubWindow: false,
35. maskColor: Color.Pink,
36. maskRect: {
37. x: 20,
38. y: 20,
39. width: '90%',
40. height: '90%'
41. },

43. dialogTransition: // 设置弹窗内容显示的过渡效果
44. TransitionEffect.translate({ x: 0, y: 290, z: 0 })
45. .animation({ duration: 4000, curve: Curve.Smooth }), // 四秒钟的偏移渐变动画

47. maskTransition: // 设置蒙层显示的过渡效果
48. TransitionEffect.opacity(0)
49. .animation({ duration: 4000, curve: Curve.Smooth }) // 四秒钟的透明渐变动画

51. })
52. .then((dialogId: number) => {
53. this.customDialogComponentId = dialogId;
54. })
55. .catch((error: BusinessError) => {
56. hilog.error(DOMAIN, 'testTag',
57. `openCustomDialog error code is ${error.code}, message is ${error.message}`)
58. })
59. })
60. }
61. .width('100%')
62. }
63. .height('100%')
64. }
65. }
66. }
```

[customDialogComponentWithTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/opencustomdialog/customDialogComponentWithTransition.ets#L16-L84)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/y7mE_msiS7yEplRouksGGw/zh-cn_image_0000002583437943.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233941Z&HW-CC-Expire=86400&HW-CC-Sign=926ECC98A6FF7770CD792DEEB61F4A9E77B4E6929D3812FBCC46B4BA5BC6DB6E)

## 设置弹出框避让软键盘的距离

为显示弹出框的独立性，弹出框弹出时会与周边进行避让，包括状态栏、导航条以及键盘等留有间距。故当软键盘弹出时，默认情况下，弹出框会自动避开软键盘，并与之保持16vp的距离。从API version 15开始，开发者可以利用[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中的keyboardAvoidMode和keyboardAvoidDistance这两个配置项，来设置弹出框在软键盘弹出时的行为，包括是否需要避开软键盘以及与软键盘之间的距离。

设置软键盘间距时，需要将keyboardAvoidMode值设为KeyboardAvoidMode.DEFAULT。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { LengthMetrics } from '@kit.ArkUI'
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @Entry
8. @Component
9. export struct CustomDialogWithKeyboardAvoidDistance {
10. @Builder
11. customDialogComponent() {
12. Column() {
13. Text('keyboardAvoidDistance: 0vp')
14. .fontSize(20)
15. .margin({ bottom: 36 })
16. TextInput({ placeholder: '' })
17. }.backgroundColor('#FFF0F0F0')
18. }

20. build() {
21. NavDestination() {
22. Row() {
23. Row({ space: 20 }) {
24. // 请将$r('app.string.open_windows')替换为实际资源文件，在本示例中该资源文件的value值为"打开弹窗"
25. Text($r('app.string.open_windows'))
26. .fontSize(30)
27. .onClick(() => {
28. this.getUIContext().getPromptAction().openCustomDialog({
29. builder: () => {
30. this.customDialogComponent();
31. },
32. alignment: DialogAlignment.Bottom,
33. keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // 软键盘弹出时，弹出框自动避让
34. keyboardAvoidDistance: LengthMetrics.vp(0) // 软键盘弹出时与弹出框的距离为0vp
35. }).catch((error: BusinessError) => {
36. hilog.error(DOMAIN, 'testTag',
37. `openCustomDialog error code is ${error.code}, message is ${error.message}`);
38. })
39. })
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }
45. }
46. }
```

[customDialogWithKeyboardAvoidDistance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/opencustomdialog/customDialogWithKeyboardAvoidDistance.ets#L16-L64)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/JNfNJKwhShelj4BIn0S3MQ/zh-cn_image_0000002552957898.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233941Z&HW-CC-Expire=86400&HW-CC-Sign=4048774722591A3A57E0CEE424D0DD12FB65D21DA90A9117A22C605E3DD926A2)

## 完整示例

```
1. // PromptActionClassNew.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { ComponentContent, promptAction, UIContext } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. const DOMAIN = 0x0000;

7. export class PromptActionClassNew {
8. static ctx: UIContext;
9. static contentNode: ComponentContent<Object>;
10. static options: promptAction.BaseDialogOptions;

12. static setContext(context: UIContext) {
13. PromptActionClassNew.ctx = context;
14. }

16. static setContentNode(node: ComponentContent<Object>) {
17. PromptActionClassNew.contentNode = node;
18. }

20. static setOptions(options: promptAction.BaseDialogOptions) {
21. PromptActionClassNew.options = options;
22. }

24. // 打开弹窗
25. static openDialog() {
26. if (PromptActionClassNew.contentNode !== null) {
27. PromptActionClassNew.ctx.getPromptAction().openCustomDialog(PromptActionClassNew.contentNode, PromptActionClassNew.options)
28. .then(() => {
29. hilog.info(DOMAIN, 'testTag', 'testTag', 'OpenCustomDialog complete.');
30. })
31. .catch((error: BusinessError) => {
32. let message = (error as BusinessError).message;
33. let code = (error as BusinessError).code;
34. hilog.error(DOMAIN, 'testTag', 'testTag', 'OpenCustomDialog args error code is ${code}, message is ${message}');
35. })
36. }
37. }

39. // 关闭弹窗
40. static closeDialog() {
41. if (PromptActionClassNew.contentNode !== null) {
42. PromptActionClassNew.ctx.getPromptAction().closeCustomDialog(PromptActionClassNew.contentNode)
43. .then(() => {
44. hilog.info(DOMAIN, 'testTag', 'testTag', 'CloseCustomDialog complete.');
45. })
46. .catch((error: BusinessError) => {
47. let message = (error as BusinessError).message;
48. let code = (error as BusinessError).code;
49. hilog.error(DOMAIN, 'testTag', 'testTag', 'CloseCustomDialog args error code is ${code}, message is ${message}');
50. })
51. }
52. }

54. // ...

56. // 更新弹窗
57. static updateDialog(options: promptAction.BaseDialogOptions) {
58. if (PromptActionClassNew.contentNode !== null) {
59. PromptActionClassNew.ctx.getPromptAction().updateCustomDialog(PromptActionClassNew.contentNode, options)
60. .then(() => {
61. hilog.info(DOMAIN, 'testTag', 'testTag', 'UpdateCustomDialog complete.');
62. })
63. .catch((error: BusinessError) => {
64. let message = (error as BusinessError).message;
65. let code = (error as BusinessError).code;
66. hilog.error(DOMAIN, 'testTag', 'testTag', 'UpdateCustomDialog args error code is ${code}, message is ${message}');
67. })
68. }
69. }
70. }
```

[PromptActionClassNew.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/common/PromptActionClassNew.ts#L16-L105)

```
1. // Index.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. import { PromptActionClassNew } from '../../common/PromptActionClassNew';

5. class Params {
6. public text: string = '';

8. constructor(text: string) {
9. this.text = text;
10. }
11. }

13. @Builder
14. function buildText(params: Params) {
15. Column() {
16. Text(params.text)
17. .fontSize(50)
18. .fontWeight(FontWeight.Bold)
19. .margin({ bottom: 36 })
20. Button('Close')
21. .onClick(() => {
22. PromptActionClassNew.closeDialog();
23. })
24. }.backgroundColor('#FFF0F0F0')
25. }

27. @Entry
28. @Component
29. export struct OpenDialogAndUpdate {
30. @State message: string = 'hello';
31. private ctx: UIContext = this.getUIContext();
32. private contentNode: ComponentContent<Object> =
33. new ComponentContent(this.ctx, wrapBuilder(buildText), new Params(this.message));
34. aboutToAppear(): void {
35. PromptActionClassNew.setContext(this.ctx);
36. PromptActionClassNew.setContentNode(this.contentNode);
37. PromptActionClassNew.setOptions({ alignment: DialogAlignment.Top, offset: { dx: 0, dy: 50 } });
38. }

40. build() {
41. NavDestination() {
42. Row() {
43. Column() {
44. Button('open dialog and update options')
45. .margin({ top: 50 })
46. .onClick(() => {
47. PromptActionClassNew.openDialog();

49. setTimeout(() => {
50. PromptActionClassNew.updateDialog({
51. alignment: DialogAlignment.Bottom,
52. offset: { dx: 0, dy: -50 }
53. });
54. }, 1500)
55. })
56. Button('open dialog and update content')
57. .margin({ top: 50 })
58. .onClick(() => {
59. PromptActionClassNew.openDialog();

61. setTimeout(() => {
62. this.contentNode.update(new Params('update'));
63. }, 1500)
64. })
65. }
66. .width('100%')
67. .height('100%')
68. }
69. .height('100%')
70. }
71. }
72. }
```

[OpenDialogAndUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/opencustomdialog/OpenDialogAndUpdate.ets#L16-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/pJpPS7DmSICg-ZJBklZX5w/zh-cn_image_0000002583477899.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233941Z&HW-CC-Expire=86400&HW-CC-Sign=757E611FDAA97BECDC6E46A49D4ACB1DA02625DC6A11E21FEB907B1DF0D056BF)
