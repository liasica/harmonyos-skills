---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction
title: Class (PromptAction)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (PromptAction)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:01b3aa82d24059f6cffc2d83eb069bfae3f53d7a5d2b1287b0d6da9fbe677a04
---

创建并显示即时反馈、对话框、操作菜单以及自定义弹窗。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getPromptAction()](arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取到PromptAction对象，再通过该对象调用对应方法。

## getTopOrder18+

PhonePC/2in1TabletTVWearable

getTopOrder(): LevelOrder

返回最顶层显示的弹窗的顺序。

获取最顶层显示的弹窗的顺序，可以在下一个弹窗时指定期望的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LevelOrder](js-apis-promptaction.md#levelorder18) | 返回弹窗层级信息。 |

**示例：**

该示例通过调用getTopOrder接口，展示了获取最顶层显示弹窗顺序的功能。

```
1. import { ComponentContent, PromptAction, LevelOrder, promptAction, UIContext } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Params {
5. text: string = "";
6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column({ space: 20 }) {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }.backgroundColor('#FFF0F0F0')
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State message: string = '弹窗';
25. private ctx: UIContext = this.getUIContext();
26. private promptAction: PromptAction = this.ctx.getPromptAction();
27. private contentNode: ComponentContent<Object> =
28. new ComponentContent(this.ctx, wrapBuilder(buildText), new Params(this.message));

30. private baseDialogOptions: promptAction.BaseDialogOptions = {
31. showInSubWindow: false,
32. levelOrder: LevelOrder.clamp(30.1),
33. };

35. build() {
36. Row() {
37. Column({ space: 10 }) {
38. Button('openCustomDialog弹窗')
39. .fontSize(20)
40. .onClick(() => {
41. this.promptAction.openCustomDialog(this.contentNode, this.baseDialogOptions)
42. .catch((err: BusinessError) => {
43. console.error("openCustomDialog error: " + err.code + " " + err.message);
44. })
45. .then(() => {
46. let topOrder: LevelOrder = this.promptAction.getTopOrder();
47. if (topOrder !== undefined) {
48. console.error('topOrder: ' + topOrder.getOrder());
49. }
50. })
51. })
52. }.width('100%')
53. }.height('100%')
54. }
55. }
```

## getBottomOrder18+

PhonePC/2in1TabletTVWearable

getBottomOrder(): LevelOrder

获取最底层显示的弹窗的顺序，可以在下一个弹窗时指定期望的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LevelOrder](js-apis-promptaction.md#levelorder18) | 返回弹窗层级信息。 |

**示例：**

该示例通过调用getBottomOrder接口，展示了获取最底层显示弹窗顺序的功能。

```
1. import { ComponentContent, PromptAction, LevelOrder, promptAction, UIContext } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class Params {
5. text: string = "";
6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column({ space: 20 }) {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }.backgroundColor('#FFF0F0F0')
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State message: string = '弹窗';
25. private ctx: UIContext = this.getUIContext();
26. private promptAction: PromptAction = this.ctx.getPromptAction();
27. private contentNode: ComponentContent<Object> =
28. new ComponentContent(this.ctx, wrapBuilder(buildText), new Params(this.message));

30. private baseDialogOptions: promptAction.BaseDialogOptions = {
31. showInSubWindow: false,
32. levelOrder: LevelOrder.clamp(30.1),
33. };

35. build() {
36. Row() {
37. Column({ space: 10 }) {
38. Button('openCustomDialog弹窗')
39. .fontSize(20)
40. .onClick(() => {
41. this.promptAction.openCustomDialog(this.contentNode, this.baseDialogOptions)
42. .catch((err: BusinessError) => {
43. console.error("openCustomDialog error: " + err.code + " " + err.message);
44. })
45. .then(() => {
46. let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
47. if (bottomOrder !== undefined) {
48. console.error('bottomOrder: ' + bottomOrder.getOrder());
49. }
50. })
51. })
52. }.width('100%')
53. }.height('100%')
54. }
55. }
```

## openToast18+

PhonePC/2in1TabletTVWearable

openToast(options: promptAction.ShowToastOptions): Promise<number>

显示即时反馈。使用Promise异步回调返回即时反馈的id，可供closeToast使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ShowToastOptions](js-apis-promptaction.md#showtoastoptions) | 是 | Toast选项。 |

**返回值**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回即时反馈的id，可供closeToast使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用openToast和closeToast接口，展示了弹出以及关闭Toast的功能。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State toastId: number = 0;
8. promptAction: PromptAction = this.getUIContext().getPromptAction();

10. build() {
11. Column() {
12. Button('OpenToast')
13. .height(100)
14. .onClick(() => {
15. this.promptAction.openToast({
16. message: 'Toast Message',
17. duration: 10000,
18. }).then((toastId: number) => {
19. this.toastId = toastId;
20. })
21. .catch((error: BusinessError) => {
22. console.error(`openToast error code is ${error.code}, message is ${error.message}`);
23. })
24. })
25. Blank().height(50)
26. Button('Close Toast')
27. .height(100)
28. .onClick(() => {
29. try {
30. this.promptAction.closeToast(this.toastId);
31. } catch (error) {
32. let message = (error as BusinessError).message;
33. let code = (error as BusinessError).code;
34. console.error(`CloseToast error code is ${code}, message is ${message}`);
35. };
36. })
37. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
38. }
39. }
```

## closeToast18+

PhonePC/2in1TabletTVWearable

closeToast(toastId: number): void

关闭即时反馈。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toastId | number | 是 | openToast返回的id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[弹窗错误码](errorcode-promptaction.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 103401 | Cannot find the toast. |

**示例：**

请参考[openToast18](arkts-apis-uicontext-promptaction.md#opentoast18)的示例。

## showToast

PhonePC/2in1TabletTVWearable

showToast(options: promptAction.ShowToastOptions): void

创建并显示即时反馈。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ShowToastOptions](js-apis-promptaction.md#showtoastoptions) | 是 | Toast选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用showToast接口，创建并显示即时反馈。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. promptAction: PromptAction = this.getUIContext().getPromptAction();

9. build() {
10. Column() {
11. Button('showToast')
12. .onClick(() => {
13. try {
14. this.promptAction.showToast({
15. message: 'Message Info',
16. duration: 2000
17. });
18. } catch (error) {
19. let message = (error as BusinessError).message;
20. let code = (error as BusinessError).code;
21. console.error(`showToast args error code is ${code}, message is ${message}`);
22. };
23. })
24. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
25. }
26. }
```

## showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: promptAction.ShowDialogOptions, callback: AsyncCallback<promptAction.ShowDialogSuccessResponse>): void

创建并显示对话框，对话框响应结果使用callback异步回调返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ShowDialogOptions](js-apis-promptaction.md#showdialogoptions) | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback<[promptAction.ShowDialogSuccessResponse](js-apis-promptaction.md#showdialogsuccessresponse)> | 是 | 回调函数。弹出对话框成功，err为undefined，data为获取到的对话框响应结果，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用showDialog接口，展示了弹出对话框以及返回对话框响应结果的功能。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. promptAction: PromptAction = this.getUIContext().getPromptAction();

9. build() {
10. Column() {
11. Button('showDialog')
12. .onClick(() => {
13. try {
14. this.promptAction.showDialog({
15. title: 'showDialog Title Info',
16. message: 'Message Info',
17. buttons: [
18. {
19. text: 'button1',
20. color: '#000000'
21. },
22. {
23. text: 'button2',
24. color: '#000000'
25. }
26. ]
27. }, (err, data) => {
28. if (err) {
29. console.error('showDialog err: ' + err);
30. return;
31. }
32. console.info('showDialog success callback, click button: ' + data.index);
33. });
34. } catch (error) {
35. let message = (error as BusinessError).message;
36. let code = (error as BusinessError).code;
37. console.error(`showDialog args error code is ${code}, message is ${message}`);
38. };
39. })
40. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
41. }
42. }
```

## showDialog

PhonePC/2in1TabletTVWearable

showDialog(options: promptAction.ShowDialogOptions): Promise<promptAction.ShowDialogSuccessResponse>

创建并显示对话框，使用Promise异步回调获取对话框的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ShowDialogOptions](js-apis-promptaction.md#showdialogoptions) | 是 | 对话框选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[promptAction.ShowDialogSuccessResponse](js-apis-promptaction.md#showdialogsuccessresponse)> | Promise对象，返回对话框的响应结果。 |

**错误码：**

以下错误码的详细介绍请参见 [通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用showDialog接口，展示了弹出对话框以及通过Promise获取对话框响应结果的功能。

```
1. import { PromptAction } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. promptAction: PromptAction = this.getUIContext().getPromptAction();

8. build() {
9. Column() {
10. Button('showDialog')
11. .onClick(() => {
12. this.promptAction.showDialog({
13. title: 'Title Info',
14. message: 'Message Info',
15. buttons: [
16. {
17. text: 'button1',
18. color: '#000000'
19. },
20. {
21. text: 'button2',
22. color: '#000000'
23. }
24. ],
25. })
26. .then(data => {
27. console.info('showDialog success, click button: ' + data.index);
28. })
29. .catch((err: Error) => {
30. console.error('showDialog error: ' + err);
31. })
32. })
33. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
34. }
35. }
```

## showActionMenu11+

PhonePC/2in1TabletTVWearable

showActionMenu(options: promptAction.ActionMenuOptions, callback: AsyncCallback<[promptAction.ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)>): void

创建并显示操作菜单，菜单响应结果使用callback异步回调返回。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[promptAction.ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)> | 是 | 回调函数。弹出操作菜单成功，err为undefined，data为获取到的操作菜单响应结果，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { PromptAction, promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. promptAction: PromptAction = this.getUIContext().getPromptAction();

9. build() {
10. Column() {
11. Button('showActionMenu')
12. .onClick(() => {
13. try {
14. this.promptAction.showActionMenu({
15. title: 'Title Info',
16. buttons: [
17. {
18. text: 'item1',
19. color: '#666666'
20. },
21. {
22. text: 'item2',
23. color: '#000000'
24. }
25. ]
26. }, (err: BusinessError, data: promptAction.ActionMenuSuccessResponse) => {
27. if (err) {
28. console.error('showActionMenu err: ' + err);
29. return;
30. }
31. console.info('showActionMenu success callback, click button: ' + data.index);
32. });
33. } catch (error) {
34. let message = (error as BusinessError).message;
35. let code = (error as BusinessError).code;
36. console.error(`showActionMenu args error code is ${code}, message is ${message}`);
37. };
38. })
39. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
40. }
41. }
```

## showActionMenu

PhonePC/2in1TabletTVWearable

showActionMenu(options: promptAction.ActionMenuOptions): Promise<promptAction.ActionMenuSuccessResponse>

创建并显示操作菜单，通过Promise异步回调获取菜单的响应结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions) | 是 | 操作菜单选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[promptAction.ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)> | Promise对象，返回菜单的响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用showActionMenu接口，展示了弹出操作菜单以及通过Promise获取操作菜单响应结果的功能。

```
1. import { PromptAction } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct Index {
5. promptAction: PromptAction = this.getUIContext().getPromptAction();

7. build() {
8. Column() {
9. Button('showActionMenu')
10. .onClick(() => {
11. this.promptAction.showActionMenu({
12. title: 'showActionMenu Title Info',
13. buttons: [
14. {
15. text: 'item1',
16. color: '#666666'
17. },
18. {
19. text: 'item2',
20. color: '#000000'
21. },
22. ]
23. })
24. .then(data => {
25. console.info('showActionMenu success, click button: ' + data.index);
26. })
27. .catch((err: Error) => {
28. console.error('showActionMenu error: ' + err);
29. })
30. })
31. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
32. }
33. }
```

## openCustomDialog12+

PhonePC/2in1TabletTVWearable

openCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options?: promptAction.BaseDialogOptions): Promise<void>

创建并弹出dialogContent对应的自定义弹窗，使用Promise异步回调。通过该接口弹出的弹窗内容样式完全按照dialogContent中设置的样式显示，即相当于customDialog设置customStyle为true时的显示效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 自定义弹窗中显示的组件内容。 |
| options | [promptAction.BaseDialogOptions](js-apis-promptaction.md#basedialogoptions11) | 否 | 弹窗样式。  **说明：** 如果BaseDialogOptions中的[isModal](js-apis-promptaction.md#basedialogoptions11)与[showInSubWindow](js-apis-promptaction.md#basedialogoptions11)同时设置为true，则只生效showInSubWindow = true，此时为非模态弹出框且不会显示蒙层，并在子窗口中显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | Dialog content error. The ComponentContent is incorrect. |
| 103302 | Dialog content already exist. The ComponentContent has already been opened. |

**示例：**

该示例通过监听[系统环境信息](js-apis-app-ability-configuration.md)（系统语言、深浅色等）的变化，调用[ComponentContent<T>](js-apis-arkui-componentcontent.md) 的[update](js-apis-arkui-buildernode.md#update)和[updateConfiguration](js-apis-arkui-buildernode.md#updateconfiguration12)实现自定义弹窗的数据更新及节点的全量刷新。

```
1. import { ComponentContent } from '@kit.ArkUI';
2. import { AbilityConstant, Configuration, EnvironmentCallback, ConfigurationConstant } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { resourceManager } from '@kit.LocalizationKit';

6. class Params {
7. text: string = "";
8. colorMode: resourceManager.ColorMode = resourceManager.ColorMode.LIGHT

10. constructor(text: string, colorMode: resourceManager.ColorMode) {
11. this.text = text
12. this.colorMode = colorMode
13. }
14. }

16. @Builder
17. function BuilderDialog(params: Params) {
18. Column() {
19. Text(params.text)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. .margin({ bottom: 36 })
23. }.backgroundColor(params.colorMode == resourceManager.ColorMode.LIGHT ? "#D5D5D5" : "#004AAF")
24. }

26. @Entry
27. @Component
28. struct Index {
29. @State message: string = "hello";
30. contentNode: ComponentContent<Params> | null = null;
31. callbackId: number | undefined = 0;

33. aboutToAppear(): void {
34. let environmentCallback: EnvironmentCallback = {
35. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
36. },
37. onConfigurationUpdated: (config: Configuration): void => {
38. console.info(`onConfigurationUpdated ${config}`);
39. this.getUIContext().getHostContext()?.getApplicationContext().resourceManager.getConfiguration((err,
40. config) => {
41. // 调用ComponentContent的update更新colorMode信息
42. this.contentNode?.update(new Params(this.message, config.colorMode))
43. setTimeout(() => {
44. // 调用ComponentContent的updateConfiguration，触发节点的全量更新
45. this.contentNode?.updateConfiguration()
46. })
47. })
48. }
49. }
50. // 注册监听系统环境变化监听器
51. this.callbackId =
52. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback)
53. // 设置应用深浅色跟随系统
54. this.getUIContext()
55. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET)
56. }

58. aboutToDisappear() {
59. // 解注册监听系统环境变化的回调
60. this.getUIContext().getHostContext()?.getApplicationContext().off('environment', this.callbackId)
61. this.contentNode?.dispose()
62. }

64. build() {
65. Row() {
66. Column() {
67. Button("click me")
68. .onClick(() => {
69. let uiContext = this.getUIContext();
70. let promptAction = uiContext.getPromptAction();
71. if (this.contentNode == null && uiContext.getHostContext() != undefined) {
72. this.contentNode = new ComponentContent(uiContext, wrapBuilder(BuilderDialog), new Params(this.message,
73. uiContext.getHostContext()!!.getApplicationContext().resourceManager.getConfigurationSync().colorMode))
74. }
75. if (this.contentNode == null) {
76. return
77. }
78. promptAction.closeCustomDialog(this.contentNode)
79. promptAction.openCustomDialog(this.contentNode).then(() => {
80. console.info("succeeded")
81. }).catch((error: BusinessError) => {
82. console.error(`OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
83. })
84. })
85. }
86. .width('100%')
87. .height('100%')
88. }
89. .height('100%')
90. }
91. }
```

## openCustomDialog12+

PhonePC/2in1TabletTVWearable

openCustomDialog(options: promptAction.CustomDialogOptions): Promise<number>

创建并弹出自定义弹窗。使用Promise异步回调返回对话框的id，可供closeCustomDialog使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.CustomDialogOptions](js-apis-promptaction.md#customdialogoptions11) | 是 | 自定义弹窗的内容。  **说明：** 如果BaseDialogOptions中的[isModal](js-apis-promptaction.md#basedialogoptions11)与[showInSubWindow](js-apis-promptaction.md#basedialogoptions11)同时设置为true，则只生效showInSubWindow = true，此时为非模态弹出框且不会显示蒙层，并在子窗口中显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回对话框id，可供closeCustomDialog使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. private customDialogComponentId: number = 0;

8. @Builder
9. customDialogComponent() {
10. Column() {
11. Text('打开了一个弹窗').fontSize(20)
12. Row({ space: 10 }) {
13. Button('取消').onClick(() => {
14. try {
15. this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId)
16. } catch (error) {
17. let message = (error as BusinessError).message;
18. let code = (error as BusinessError).code;
19. console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
20. }
21. }).width(100).backgroundColor('#d5d5d5').fontColor('#707070')
22. Button('确定').onClick(() => {
23. try {
24. this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId)
25. } catch (error) {
26. let message = (error as BusinessError).message;
27. let code = (error as BusinessError).code;
28. console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
29. }
30. }).width(100)
31. }
32. }.height(150).padding(20).justifyContent(FlexAlign.SpaceBetween)
33. }

35. build() {
36. Row() {
37. Column({ space: 20 }) {
38. Button('Click Me')
39. .fontSize(30)
40. .onClick(() => {
41. this.getUIContext()
42. .getPromptAction()
43. .openCustomDialog({
44. builder: () => {
45. this.customDialogComponent()
46. },
47. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
48. console.info('reason' + JSON.stringify(dismissDialogAction.reason));
49. console.info('dialog onWillDismiss');
50. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
51. dismissDialogAction.dismiss();
52. }
53. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
54. dismissDialogAction.dismiss();
55. }
56. }
57. })
58. .then((dialogId: number) => {
59. this.customDialogComponentId = dialogId;
60. })
61. .catch((error: BusinessError) => {
62. console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
63. })
64. })
65. }
66. .width('100%')
67. }
68. .height('100%')
69. }
70. }
```

## openCustomDialogWithController18+

PhonePC/2in1TabletTVWearable

openCustomDialogWithController<T extends Object>(dialogContent: ComponentContent<T>, controller: promptAction.DialogController, options?: promptAction.BaseDialogOptions): Promise<void>

创建并弹出dialogContent对应的自定义弹窗，使用Promise异步回调。支持传入弹窗控制器与自定义弹窗绑定，后续可以通过控制器控制自定义弹窗。

通过该接口弹出的弹窗内容样式完全按照dialogContent中设置的样式显示，即相当于customDialog设置customStyle为true时的显示效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 自定义弹窗中显示的组件内容。 |
| controller | [promptAction.DialogController](js-apis-promptaction.md#dialogcontroller18) | 是 | 自定义弹窗的控制器。 |
| options | [promptAction.BaseDialogOptions](js-apis-promptaction.md#basedialogoptions11) | 否 | 自定义弹窗的样式。  **说明：** 如果BaseDialogOptions中的[isModal](js-apis-promptaction.md#basedialogoptions11)与[showInSubWindow](js-apis-promptaction.md#basedialogoptions11)同时设置为true，则只生效showInSubWindow = true，此时为非模态弹出框且不会显示蒙层，并在子窗口中显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | Dialog content error. The ComponentContent is incorrect. |
| 103302 | Dialog content already exist. The ComponentContent has already been opened. |

**示例：**

该示例通过调用openCustomDialog接口，展示了支持传入弹窗控制器与自定义弹窗绑定的功能。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent, promptAction } from '@kit.ArkUI';

4. class Params {
5. text: string = "";
6. dialogController: promptAction.DialogController = new promptAction.DialogController();

8. constructor(text: string, dialogController: promptAction.DialogController) {
9. this.text = text;
10. this.dialogController = dialogController;
11. }
12. }

14. @Builder
15. function buildText(params: Params) {
16. Column() {
17. Text(params.text)
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .margin({ bottom: 36 })
21. Button('点我关闭弹窗：通过外部传递的DialogController')
22. .onClick(() => {
23. if (params.dialogController != undefined) {
24. params.dialogController.close();
25. }
26. })
27. }.backgroundColor('#FFF0F0F0')
28. }

30. @Entry
31. @ComponentV2
32. struct Index {
33. @Local message: string = "hello";
34. private dialogController: promptAction.DialogController = new promptAction.DialogController();

36. build() {
37. Row() {
38. Column() {
39. Button("click me")
40. .onClick(() => {
41. let uiContext = this.getUIContext();
42. let promptAction = uiContext.getPromptAction();
43. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText),
44. new Params(this.message, this.dialogController));
45. promptAction.openCustomDialogWithController(contentNode, this.dialogController)
46. .then(() => {
47. console.info('succeeded');
48. })
49. .catch((error: BusinessError) => {
50. console.error(`OpenCustomDialogWithController args error code is ${error.code}, message is ${error.message}`);
51. })
52. })
53. }
54. .width('100%')
55. .height('100%')
56. }
57. .height('100%')
58. }
59. }
```

## updateCustomDialog12+

PhonePC/2in1TabletTVWearable

updateCustomDialog<T extends Object>(dialogContent: ComponentContent<T>, options: promptAction.BaseDialogOptions): Promise<void>

更新已弹出的dialogContent对应的自定义弹窗的样式，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 自定义弹窗中显示的组件内容。 |
| options | [promptAction.BaseDialogOptions](js-apis-promptaction.md#basedialogoptions11) | 是 | 弹窗样式，目前仅支持更新alignment、offset、autoCancel、maskColor。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | Dialog content error. The ComponentContent is incorrect. |
| 103303 | Dialog content not found. The ComponentContent cannot be found. |

**示例：**

该示例通过调用updateCustomDialog接口，动态调整已弹出自定义弹窗的位置。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. }.backgroundColor('#FFF0F0F0')
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = "hello";

27. build() {
28. Row() {
29. Column() {
30. Button("click me")
31. .onClick(() => {
32. let uiContext = this.getUIContext();
33. let promptAction = uiContext.getPromptAction();
34. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
35. promptAction.openCustomDialog(contentNode)
36. .then(() => {
37. console.info('succeeded');
38. })
39. .catch((error: BusinessError) => {
40. console.error(`updateCustomDialog args error code is ${error.code}, message is ${error.message}`);
41. })

43. setTimeout(() => {
44. promptAction.updateCustomDialog(contentNode, { alignment: DialogAlignment.CenterEnd })
45. .then(() => {
46. console.info('succeeded');
47. })
48. .catch((error: BusinessError) => {
49. console.error(`updateCustomDialog args error code is ${error.code}, message is ${error.message}`);
50. })
51. }, 2000); //2秒后自动更新弹窗位置
52. })
53. }
54. .width('100%')
55. .height('100%')
56. }
57. .height('100%')
58. }
59. }
```

## closeCustomDialog12+

PhonePC/2in1TabletTVWearable

closeCustomDialog<T extends Object>(dialogContent: ComponentContent<T>): Promise<void>

关闭已弹出的dialogContent对应的自定义弹窗，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogContent | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | 自定义弹窗中显示的组件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | Dialog content error. The ComponentContent is incorrect. |
| 103303 | Dialog content not found. The ComponentContent cannot be found. |

**示例：**

该示例通过调用closeCustomDialog接口，关闭已弹出的dialogContent对应的自定义弹窗。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. }.backgroundColor('#FFF0F0F0')
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = "hello";

27. build() {
28. Row() {
29. Column() {
30. Button("click me")
31. .onClick(() => {
32. let uiContext = this.getUIContext();
33. let promptAction = uiContext.getPromptAction();
34. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
35. promptAction.openCustomDialog(contentNode)
36. .then(() => {
37. console.info('succeeded');
38. })
39. .catch((error: BusinessError) => {
40. console.error(`OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
41. })
42. setTimeout(() => {
43. promptAction.closeCustomDialog(contentNode)
44. .then(() => {
45. console.info('succeeded');
46. })
47. .catch((error: BusinessError) => {
48. console.error(`OpenCustomDialog args error code is ${error.code}, message is ${error.message}`);
49. })
50. }, 2000); //2秒后自动关闭
51. })
52. }
53. .width('100%')
54. .height('100%')
55. }
56. .height('100%')
57. }
58. }
```

## closeCustomDialog12+

PhonePC/2in1TabletTVWearable

closeCustomDialog(dialogId: number): void

关闭自定义弹窗。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogId | number | 是 | openCustomDialog返回的对话框id。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { PromptAction } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. promptAction: PromptAction = this.getUIContext().getPromptAction();
7. private customDialogComponentId: number = 0;

9. @Builder
10. customDialogComponent() {
11. Column() {
12. Text('弹窗').fontSize(30)
13. Row({ space: 50 }) {
14. Button("确认").onClick(() => {
15. this.promptAction.closeCustomDialog(this.customDialogComponentId);
16. })
17. Button("取消").onClick(() => {
18. this.promptAction.closeCustomDialog(this.customDialogComponentId);
19. })
20. }
21. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
22. }

24. build() {
25. Row() {
26. Column() {
27. Button("click me")
28. .onClick(() => {
29. this.promptAction.openCustomDialog({
30. builder: () => {
31. this.customDialogComponent()
32. },
33. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
34. console.info(`reason ${dismissDialogAction.reason}`);
35. console.info('dialog onWillDismiss');
36. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
37. dismissDialogAction.dismiss();
38. }
39. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
40. dismissDialogAction.dismiss();
41. }
42. }
43. }).then((dialogId: number) => {
44. this.customDialogComponentId = dialogId;
45. })
46. })
47. }
48. .width('100%')
49. .height('100%')
50. }
51. .height('100%')
52. }
53. }
```

## presentCustomDialog18+

PhonePC/2in1TabletTVWearable

presentCustomDialog(builder: CustomBuilder | CustomBuilderWithId, controller?: promptAction.DialogController, options?: promptAction.DialogOptions): Promise<number>

创建并弹出自定义弹窗。使用Promise异步回调返回对话框的id，可供closeCustomDialog使用。

支持在自定义弹窗内容中持有弹窗ID进行对应操作。支持传入弹窗控制器与自定义弹窗绑定，后续可以通过控制器控制自定义弹窗。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | [CustomBuilderWithId](arkts-apis-uicontext-t.md#custombuilderwithid18) | 是 | 自定义弹窗的内容。 |
| controller | [promptAction.DialogController](js-apis-promptaction.md#dialogcontroller18) | 否 | 自定义弹窗的控制器。 |
| options | [promptAction.DialogOptions](js-apis-promptaction.md#dialogoptions18) | 否 | 自定义弹窗的样式。  **说明：** 如果BaseDialogOptions中的[isModal](js-apis-promptaction.md#basedialogoptions11)与[showInSubWindow](js-apis-promptaction.md#basedialogoptions11)同时设置为true，则只生效showInSubWindow = true，此时为非模态弹出框且不会显示蒙层，并在子窗口中显示。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回自定义弹窗ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { PromptAction, promptAction } from '@kit.ArkUI';

4. @Entry
5. @ComponentV2
6. struct Index {
7. @Local message: string = "hello";
8. private ctx: UIContext = this.getUIContext();
9. private promptAction: PromptAction = this.ctx.getPromptAction();
10. private dialogController: promptAction.DialogController = new promptAction.DialogController();

12. private customDialogComponentId: number = 0;
13. @Builder customDialogComponent() {
14. Column() {
15. Text(this.message).fontSize(30)
16. Row({ space: 10 }) {
17. Button("通过DialogId关闭").onClick(() => {
18. this.promptAction.closeCustomDialog(this.customDialogComponentId);
19. })
20. Button("通过DialogController关闭").onClick(() => {
21. this.dialogController.close();
22. })
23. }
24. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
25. }

27. @Builder customDialogComponentWithId(dialogId: number) {
28. Column() {
29. Text(this.message).fontSize(30)
30. Row({ space: 10 }) {
31. Button("通过DialogId关闭").onClick(() => {
32. this.promptAction.closeCustomDialog(dialogId);
33. })
34. Button("通过DialogController关闭").onClick(() => {
35. this.dialogController.close();
36. })
37. }
38. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
39. }

41. build() {
42. Row() {
43. Column({ space: 10 }) {
44. Button('presentCustomDialog')
45. .fontSize(20)
46. .onClick(() => {
47. this.promptAction.presentCustomDialog(() => {
48. this.customDialogComponent()
49. }, this.dialogController)
50. .then((dialogId: number) => {
51. this.customDialogComponentId = dialogId;
52. })
53. .catch((err: BusinessError) => {
54. console.error("presentCustomDialog error: " + err.code + " " + err.message);
55. })
56. })
57. Button('presentCustomDialog with id')
58. .fontSize(20)
59. .onClick(() => {
60. this.promptAction.presentCustomDialog((dialogId: number) => {
61. this.customDialogComponentWithId(dialogId)
62. }, this.dialogController)
63. .catch((err: BusinessError) => {
64. console.error("presentCustomDialog with id error: " + err.code + " " + err.message);
65. })
66. })
67. }
68. .width('100%')
69. .height('100%')
70. }
71. .height('100%')
72. }
73. }
```

## openPopup18+

PhonePC/2in1TabletTVWearable

openPopup<T extends Object>(content: ComponentContent<T>, target: TargetInfo, options?: PopupCommonOptions): Promise<void>

创建并弹出以content作为内容的Popup弹窗，使用Promise异步回调。

说明

* 使用该接口时，若未传入有效的target，则无法弹出popup弹窗。
* 由于[updatePopup](arkts-apis-uicontext-promptaction.md#updatepopup18)和[closePopup](arkts-apis-uicontext-promptaction.md#closepopup18)依赖content去更新或者关闭指定的popup弹窗，开发者需自行维护传入的content。
* 如果在wrapBuilder中包含其他组件（例如：[Popup](ohos-arkui-advanced-popup.md)、[Chip](ohos-arkui-advanced-chip.md)组件），则[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)应采用带有四个参数的构造函数constructor，其中options参数应传递{ nestingBuilderSupported: true }。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | popup弹窗中显示的组件内容。 |
| target | [TargetInfo](arkts-apis-uicontext-i.md#targetinfo18) | 是 | 需要绑定组件的信息。 |
| options | [PopupCommonOptions](ts-universal-attributes-popup.md#popupcommonoptions18类型说明) | 否 | popup弹窗样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103302 | The ComponentContent already exists. |
| 103304 | The targetId does not exist. |
| 103305 | The node of targetId is not in the component tree. |

**示例：**

该示例通过调用openPopup、updatePopup和closePopup接口，展示了弹出、更新以及关闭Popup的功能。

```
1. import { ComponentContent, FrameNode } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. interface PopupParam {
5. updateFunc?: () => void;
6. closeFunc?: () => void;
7. }

9. export function showPopup(context: UIContext, uniqueId: number, contentNode: ComponentContent<PopupParam>,
10. popupParam: PopupParam) {
11. const promptAction = context.getPromptAction();
12. let frameNode: FrameNode | null = context.getFrameNodeByUniqueId(uniqueId);
13. let targetId = frameNode?.getFirstChild()?.getUniqueId();
14. promptAction.openPopup(contentNode, { id: targetId }, {
15. radius: 16,
16. mask: { color: Color.Pink },
17. enableArrow: true,
18. })
19. .then(() => {
20. console.info('openPopup success');
21. })
22. .catch((err: BusinessError) => {
23. console.error('openPopup error: ' + err.code + ' ' + err.message);
24. })
25. popupParam.updateFunc = () => {
26. promptAction.updatePopup(contentNode, {
27. enableArrow: false
28. }, true)
29. .then(() => {
30. console.info('updatePopup success');
31. })
32. .catch((err: BusinessError) => {
33. console.error('updatePopup error: ' + err.code + ' ' + err.message);
34. })
35. }
36. popupParam.closeFunc = () => {
37. promptAction.closePopup(contentNode)
38. .then(() => {
39. console.info('closePopup success');
40. })
41. .catch((err: BusinessError) => {
42. console.error('closePopup error: ' + err.code + ' ' + err.message);
43. })
44. }
45. }

47. @Builder
48. function buildText(param?: PopupParam) {
49. Column() {
50. Text('popup')
51. Button('Update Popup')
52. .fontSize(20)
53. .onClick(() => {
54. param?.updateFunc?.();
55. })
56. Button('Close Popup')
57. .fontSize(20)
58. .onClick(() => {
59. param?.closeFunc?.();
60. })
61. }
62. }

64. @Entry
65. @Component
66. struct Index {
67. build() {
68. Column() {
69. Button('Open Popup')
70. .fontSize(20)
71. .onClick(() => {
72. let context = this.getUIContext();
73. const popupParam: PopupParam = {};
74. const contentNode = new ComponentContent(context, wrapBuilder(buildText), popupParam);
75. showPopup(context, this.getUniqueId(), contentNode, popupParam);
76. })
77. }
78. }
79. }
```

## updatePopup18+

PhonePC/2in1TabletTVWearable

updatePopup<T extends Object>(content: ComponentContent<T>, options: PopupCommonOptions, partialUpdate?: boolean ): Promise<void>

更新content对应的Popup弹窗的样式，使用Promise异步回调。

说明

不支持更新showInSubWindow、focusable、onStateChange、onWillDismiss、transition。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | popup弹窗中显示的组件内容。 |
| options | [PopupCommonOptions](ts-universal-attributes-popup.md#popupcommonoptions18类型说明) | 是 | popup弹窗样式。  **说明：**  不支持更新showInSubWindow、focusable、onStateChange、onWillDismiss、transition。 |
| partialUpdate | boolean | 否 | popup弹窗更新方式，默认值为false。  **说明：**  true：增量更新，此时更新options中的指定属性，其它属性保留当前值。options中传入的属性为异常值或undefined时，不会对该属性进行更新。  false：全量更新，此时更新options中的指定属性，并且其他属性恢复默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103303 | The ComponentContent cannot be found. |

**示例：**

请参考[openPopup](arkts-apis-uicontext-promptaction.md#openpopup18)示例。

## closePopup18+

PhonePC/2in1TabletTVWearable

closePopup<T extends Object>(content: ComponentContent<T>): Promise<void>

关闭content对应的Popup弹窗，使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | popup弹窗中显示的组件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103303 | The ComponentContent cannot be found. |

**示例：**

请参考[openPopup](arkts-apis-uicontext-promptaction.md#openpopup18)示例。

## openMenu18+

PhonePC/2in1TabletTVWearable

openMenu<T extends Object>(content: ComponentContent<T>, target: TargetInfo, options?: MenuOptions): Promise<void>

创建并弹出以content作为内容的Menu弹窗。使用Promise异步回调。

说明

* 使用该接口时，若未传入有效的target，则无法弹出menu弹窗。
* 由于[updateMenu](arkts-apis-uicontext-promptaction.md#updatemenu18)和[closeMenu](arkts-apis-uicontext-promptaction.md#closemenu18)依赖content去更新或者关闭指定的menu弹窗，开发者需自行维护传入的content。
* 如果在wrapBuilder中包含其他组件（例如：[Popup](ohos-arkui-advanced-popup.md)、[Chip](ohos-arkui-advanced-chip.md)组件），则[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)应采用带有四个参数的构造函数constructor，其中options参数应传递{ nestingBuilderSupported: true }。
* 子窗弹窗里不能再弹出子窗弹窗，例如[openMenu](arkts-apis-uicontext-promptaction.md#openmenu18)设置了showInSubWindow为true时，则不能再弹出另一个设置了showInSubWindow为true的弹窗。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | menu弹窗中显示的组件内容。 |
| target | [TargetInfo](arkts-apis-uicontext-i.md#targetinfo18) | 是 | 需要绑定组件的信息。 |
| options | [MenuOptions](ts-universal-attributes-menu.md#menuoptions10) | 否 | menu弹窗样式。  **说明：**  title属性不生效。  preview参数仅支持设置MenuPreviewMode类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103302 | The ComponentContent already exists. |
| 103304 | The targetId does not exist. |
| 103305 | The node of targetId is not in the component tree. |

**示例：**

该示例通过调用openMenu接口，展示了弹出Menu的功能。

```
1. import { ComponentContent, FrameNode } from '@kit.ArkUI';

3. export function doSomething(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
4. showMenu(context, uniqueId, contentNode);
5. }

7. @Builder
8. function MyMenu() {
9. Column() {
10. Menu() {
11. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项1" })
12. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项2" })
13. }
14. }
15. .width('80%')
16. .padding('20lpx')
17. }

19. export function showMenu(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
20. const promptAction = context.getPromptAction();
21. let frameNode: FrameNode | null = context.getFrameNodeByUniqueId(uniqueId);
22. let frameNodeTarget = frameNode?.getFirstChild();
23. frameNodeTarget = frameNodeTarget?.getChild(0);
24. let targetId = frameNodeTarget?.getUniqueId();
25. promptAction.openMenu(contentNode, { id: targetId }, {
26. enableArrow: true,
27. });
28. }

30. @Entry
31. @Component
32. struct Index {
33. build() {
34. Column() {
35. Button('OpenMenu', { type: ButtonType.Normal, stateEffect: true })
36. .borderRadius('16lpx')
37. .width('80%')
38. .margin(10)
39. .onClick(() => {
40. let context = this.getUIContext();
41. const contentNode = new ComponentContent(context, wrapBuilder(MyMenu));
42. doSomething(context, this.getUniqueId(), contentNode);
43. })
44. }
45. }
46. }
```

## updateMenu18+

PhonePC/2in1TabletTVWearable

updateMenu<T extends Object>(content: ComponentContent<T>, options: MenuOptions, partialUpdate?: boolean ): Promise<void>

更新content对应的Menu弹窗的样式。使用Promise异步回调。

说明

* 不支持更新showInSubWindow、preview、previewAnimationOptions、transition、onAppear、aboutToAppear、onDisappear、aboutToDisappear、onWillAppear、onDidAppear、onWillDisappear和onDidDisappear。
* 支持mask通过设置[MenuMaskType](ts-universal-attributes-menu.md#menumasktype20类型说明)实现更新蒙层样式，不支持mask通过设置boolean实现蒙层从无到有或者从有到无的更新。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | menu弹窗中显示的组件内容。 |
| options | [MenuOptions](ts-universal-attributes-menu.md#menuoptions10) | 是 | menu弹窗样式。  **说明：**  1. 不支持更新showInSubWindow、preview、previewAnimationOptions、transition、onAppear、aboutToAppear、onDisappear、aboutToDisappear、onWillAppear、onDidAppear、onWillDisappear和onDidDisappear。  2. 支持mask通过设置[MenuMaskType](ts-universal-attributes-menu.md#menumasktype20类型说明)实现更新蒙层样式，不支持mask通过设置boolean实现蒙层从无到有或者从有到无的更新。 |
| partialUpdate | boolean | 否 | menu弹窗更新方式，默认值为false。  **说明：**  1. true为增量更新，保留当前值，更新options中的指定属性。  2. false为全量更新，除options中的指定属性，其他属性恢复默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103303 | The ComponentContent cannot be found. |

**示例：**

该示例通过调用updateMenu接口，展示了更新Menu箭头样式的功能。

```
1. import { ComponentContent, FrameNode } from '@kit.ArkUI';

3. export function doSomething(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
4. showMenu(context, uniqueId, contentNode);
5. }

7. @Builder
8. function MyMenu() {
9. Column() {
10. Menu() {
11. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项1" })
12. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项2" })
13. }
14. }
15. .width('80%')
16. .padding('20lpx')
17. }

19. export function showMenu(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
20. const promptAction = context.getPromptAction();
21. let frameNode: FrameNode | null = context.getFrameNodeByUniqueId(uniqueId);
22. let frameNodeTarget = frameNode?.getFirstChild();
23. frameNodeTarget = frameNodeTarget?.getChild(0);
24. let targetId = frameNodeTarget?.getUniqueId();
25. promptAction.openMenu(contentNode, { id: targetId }, {
26. enableArrow: true,
27. });
28. setTimeout(() => {
29. promptAction.updateMenu(contentNode, {
30. enableArrow: false,
31. });
32. }, 2000);
33. }

35. @Entry
36. @Component
37. struct Index {
38. build() {
39. Column() {
40. Button('OpenMenu', { type: ButtonType.Normal, stateEffect: true })
41. .borderRadius('16lpx')
42. .width('80%')
43. .margin(10)
44. .onClick(() => {
45. let context = this.getUIContext();
46. const contentNode = new ComponentContent(context, wrapBuilder(MyMenu));
47. doSomething(context, this.getUniqueId(), contentNode);
48. })
49. }
50. }
51. }
```

## closeMenu18+

PhonePC/2in1TabletTVWearable

closeMenu<T extends Object>(content: ComponentContent<T>): Promise<void>

关闭content对应的Menu弹窗。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent<T>](js-apis-arkui-componentcontent.md) | 是 | menu弹窗中显示的组件内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[弹窗错误码](errorcode-promptaction.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 103301 | The ComponentContent is incorrect. |
| 103303 | The ComponentContent cannot be found. |

**示例：**

该示例通过调用closeMenu接口，展示了关闭Menu的功能。

```
1. import { ComponentContent, FrameNode } from '@kit.ArkUI';

3. export function doSomething(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
4. showMenu(context, uniqueId, contentNode);
5. }

7. @Builder
8. function MyMenu() {
9. Column() {
10. Menu() {
11. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项1" })
12. MenuItem({ startIcon: $r("app.media.startIcon"), content: "菜单选项2" })
13. }
14. }
15. .width('80%')
16. .padding('20lpx')
17. }

19. export function showMenu(context: UIContext, uniqueId: number, contentNode: ComponentContent<Object>) {
20. const promptAction = context.getPromptAction();
21. let frameNode: FrameNode | null = context.getFrameNodeByUniqueId(uniqueId);
22. let frameNodeTarget = frameNode?.getFirstChild();
23. frameNodeTarget = frameNodeTarget?.getChild(0);
24. let targetId = frameNodeTarget?.getUniqueId();
25. promptAction.openMenu(contentNode, { id: targetId }, {
26. enableArrow: true,
27. });
28. setTimeout(() => {
29. promptAction.closeMenu(contentNode);
30. }, 2000);
31. }

33. @Entry
34. @Component
35. struct Index {
36. build() {
37. Column() {
38. Button('OpenMenu', { type: ButtonType.Normal, stateEffect: true })
39. .borderRadius('16lpx')
40. .width('80%')
41. .margin(10)
42. .onClick(() => {
43. let context = this.getUIContext();
44. const contentNode = new ComponentContent(context, wrapBuilder(MyMenu));
45. doSomething(context, this.getUniqueId(), contentNode);
46. })
47. }
48. }
49. }
```

## showActionMenu(deprecated)

PhonePC/2in1TabletTVWearable

showActionMenu(options: promptAction.ActionMenuOptions, callback: [promptAction.ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse)): void

创建并显示操作菜单，菜单响应结果使用callback异步回调返回。

说明

从API version 10开始支持，从API version 11开始废弃，建议使用[showActionMenu](arkts-apis-uicontext-promptaction.md#showactionmenu11)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [promptAction.ActionMenuOptions](js-apis-promptaction.md#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | [promptAction.ActionMenuSuccessResponse](js-apis-promptaction.md#actionmenusuccessresponse) | 是 | 回调函数，返回菜单的响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

该示例通过调用showActionMenu接口，展示了弹出操作菜单以及返回菜单响应结果的功能。

```
1. import { PromptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. promptAction: PromptAction = this.getUIContext().getPromptAction();

9. build() {
10. Column() {
11. Button('showActionMenu')
12. .onClick(() => {
13. try {
14. this.promptAction.showActionMenu({
15. title: 'Title Info',
16. buttons: [
17. {
18. text: 'item1',
19. color: '#666666'
20. },
21. {
22. text: 'item2',
23. color: '#000000'
24. }
25. ]
26. }, { index: 0 });
27. } catch (error) {
28. let message = (error as BusinessError).message;
29. let code = (error as BusinessError).code;
30. console.error(`showActionMenu args error code is ${code}, message is ${message}`);
31. }
32. ;
33. })
34. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
35. }
36. }
```
