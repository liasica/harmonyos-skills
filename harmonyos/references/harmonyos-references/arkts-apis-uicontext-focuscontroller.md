---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller
title: Class (FocusController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (FocusController)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab70dc13b7efedfb9b2a47080f91c064f023b6fd0b6803b61dfb89159868a6bc
---

提供控制焦点的能力，如清除、移动和激活焦点等功能。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getFocusController()](arkts-apis-uicontext-uicontext.md#getfocuscontroller12)方法获取FocusController实例，再通过该实例调用对应方法。

## clearFocus12+

PhonePC/2in1TabletTVWearable

clearFocus(): void

清除焦点，将焦点强制转移到页面根容器节点，焦点链路上其他节点失焦。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

在该示例中，按钮"button2"默认获焦，点击按钮"clearFocus"后，焦点回到该页面的根容器节点"column1"，此时按下键盘TAB键，按钮"button2"重新获焦。可通过点击"button1"使该按钮获焦，点击按钮"clearFocus"后，焦点同样回到该页面的根容器节点"column1"，此时按下键盘TAB键，由按钮"button1"重新获焦。

```
1. @Entry
2. @Component
3. struct ClearFocusExample {
4. @State inputValue: string = '';
5. @State btColor: Color = Color.Blue;

7. build() {
8. Column({ space: 20 }) {
9. Column({ space: 5 }) {
10. Button('button1')
11. .width(200)
12. .height(70)
13. .fontColor(Color.White)
14. .focusOnTouch(true)
15. .backgroundColor(Color.Blue)
16. Button('button2')
17. .width(200)
18. .height(70)
19. .fontColor(Color.White)
20. .focusOnTouch(true)
21. .backgroundColor(this.btColor)
22. .defaultFocus(true)
23. .onFocus(() => {
24. this.btColor = Color.Red;
25. })
26. .onBlur(() => {
27. this.btColor = Color.Blue;
28. })
29. Button('clearFocus')
30. .width(200)
31. .height(70)
32. .fontColor(Color.White)
33. .backgroundColor(Color.Blue)
34. .onClick(() => {
35. this.getUIContext().getFocusController().clearFocus();
36. })
37. }
38. .id('column2')
39. }
40. .id('column1')
41. .width('100%')
42. .height('100%')
43. }
44. }
```

## requestFocus12+

PhonePC/2in1TabletTVWearable

requestFocus(key: string): void

通过组件的id将焦点转移到组件树对应的实体节点，当前帧生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 节点对应的[组件标识](ts-universal-attributes-component-id.md)。 |

**错误码：**

以下错误码的详细介绍请参见[焦点错误码](errorcode-focus.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 150001 | the component cannot be focused. |
| 150002 | This component has an unfocusable ancestor. |
| 150003 | the component is not on tree or does not exist. |

**示例：**

```
1. @Entry
2. @Component
3. struct RequestExample {
4. @State btColor: Color = Color.Blue;

6. build() {
7. Column({ space: 20 }) {
8. Column({ space: 5 }) {
9. Button('Button')
10. .width(200)
11. .height(70)
12. .fontColor(Color.White)
13. .focusOnTouch(true)
14. .backgroundColor(this.btColor)
15. .onFocus(() => {
16. this.btColor = Color.Red;
17. })
18. .onBlur(() => {
19. this.btColor = Color.Blue;
20. })
21. .id("testButton")

23. Divider()
24. .vertical(false)
25. .width("80%")
26. .backgroundColor(Color.Black)
27. .height(10)

29. Button('requestFocus')
30. .width(200)
31. .height(70)
32. .onClick(() => {
33. this.getUIContext().getFocusController().requestFocus("testButton");
34. })

36. Button('requestFocus fail')
37. .width(200)
38. .height(70)
39. .onClick(() => {
40. try {
41. this.getUIContext().getFocusController().requestFocus("eee");
42. } catch (error) {
43. console.error(`requestFocus failed code is ${error.code} message is ${error.message}`);
44. }
45. })
46. }
47. }
48. .width('100%')
49. .height('100%')
50. }
51. }
```

## activate14+

PhonePC/2in1TabletTVWearable

activate(isActive: boolean, autoInactive?: boolean): void

设置当前界面的[焦点激活态](../harmonyos-guides/arkts-common-events-focus-event.md)。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isActive | boolean | 是 | 设置是否进入/退出焦点激活态。  true表示设置进入焦点激活态，false表示设置退出焦点激活态。 |
| autoInactive | boolean | 否 | 设置焦点激活态退出逻辑。  为true时，会自动在触摸事件、鼠标事件触发时退出，为false时，仅受开发者API控制。  默认值：true |

**示例：**

```
1. // 该示例表示在页面加载完成时进入焦点激活态，可按方向键在button间走焦
2. @Entry
3. @Component
4. struct ActivateExample {
5. aboutToAppear() {
6. this.getUIContext().getFocusController().activate(true, false);
7. }

9. aboutToDisappear() {
10. this.getUIContext().getFocusController().activate(false);
11. }

13. build() {
14. Row() {
15. Button('Button1')
16. .width(200)
17. .height(70)
18. .defaultFocus(true)

20. Button('Button2')
21. .width(200)
22. .height(70)

24. Button('Button3')
25. .width(200)
26. .height(70)
27. }
28. .padding(10)
29. .justifyContent(FlexAlign.SpaceBetween)
30. .width(800)
31. }
32. }
```

## isActive20+

PhonePC/2in1TabletTVWearable

isActive(): boolean

返回UI实例的焦点激活态。

焦点激活态可参考[基础概念：焦点激活态](../harmonyos-guides/arkts-common-events-focus-event.md#基础概念)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回UI实例的焦点激活态。true表示当前进入焦点激活态，false表示当前已退出焦点激活态。 |

**示例：**

验证isActive返回UI实例的焦点激活态。

```
1. @Entry
2. @Component
3. struct ClearFocusExample {
4. @State inputValue: string = '';
5. @State btColor: Color = Color.Blue;

7. build() {
8. Column({ space: 20 }) {
9. Column({ space: 5 }) {
10. Button('button1')
11. .width(200)
12. .height(70)
13. .fontColor(Color.White)
14. .focusOnTouch(true)
15. .backgroundColor(Color.Blue)
16. .onClick(() => {
17. console.info("button1 onClick");
18. this.getUIContext().getFocusController().activate(true);
19. console.info(`focus status ${this.getUIContext().getFocusController().isActive()}`);
20. })
21. Button('button2')
22. .width(200)
23. .height(70)
24. .fontColor(Color.White)
25. .focusOnTouch(true)
26. .backgroundColor(this.btColor)
27. .defaultFocus(true)
28. .onClick(() => {
29. console.info("button2 onClick");
30. this.getUIContext().getFocusController().activate(false);
31. console.info(`focus status ${this.getUIContext().getFocusController().isActive()}`);
32. })
33. .onFocus(() => {
34. this.btColor = Color.Red;
35. })
36. .onBlur(() => {
37. this.btColor = Color.Blue;
38. })
39. }
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

## setAutoFocusTransfer14+

PhonePC/2in1TabletTVWearable

setAutoFocusTransfer(isAutoFocusTransfer: boolean): void

设置页面切换时，新的页面是否需要主动获取焦点。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAutoFocusTransfer | boolean | 是 | 设置页面切换时，新的页面是否需要主动获取焦点，例如[Router](js-apis-router.md)、[Navigation](ts-basic-components-navigation.md)、[Menu](ts-basic-components-menu.md)、[Dialog](ohos-arkui-advanced-dialog.md)、[Popup](ohos-arkui-advanced-popup.md)等。true表示需要主动获取焦点，false表示不需要主动获取焦点。默认值为true。 |

**示例：**

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;

5. build() {
6. Column() {
7. Text('这是自定义弹窗')
8. .fontSize(30)
9. .height(100)
10. Text('弹窗不能主动获取焦点')
11. .fontSize(20)
12. .height(100)
13. Button('点我关闭弹窗')
14. .onClick(() => {
15. if (this.controller != undefined) {
16. this.getUIContext().getFocusController().setAutoFocusTransfer(true);
17. this.controller.close();
18. }
19. })
20. .margin(20)
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct CustomDialogUser {
28. dialogController: CustomDialogController | null = new CustomDialogController({
29. builder: CustomDialogExample({}),
30. });

32. aboutToDisappear() {
33. this.dialogController = null;
34. }

36. build() {
37. Column() {
38. Button('click me')
39. .onClick(() => {
40. if (this.dialogController != null) {
41. this.getUIContext().getFocusController().setAutoFocusTransfer(false);
42. this.dialogController.open();
43. }
44. }).backgroundColor(0x317aff)
45. }.width('100%').margin({ top: 5 })
46. }
47. }
```

## setKeyProcessingMode15+

PhonePC/2in1TabletTVWearable

setKeyProcessingMode(mode: KeyProcessingMode): void

设置按键事件处理的优先级。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [KeyProcessingMode](ts-universal-attributes-focus.md#keyprocessingmode15) | 是 | 按键处理模式。 |

**示例：**

```
1. // 该示例演示了在页面加载完成后设置走焦类型的实现方式。
2. @Entry
3. @Component
4. struct Index {
5. aboutToAppear() {
6. this.getUIContext().getFocusController().setKeyProcessingMode(KeyProcessingMode.ANCESTOR_EVENT);
7. }

9. build() {
10. Row() {
11. Row() {
12. Button('Button1').id('Button1').onKeyEvent((event) => {
13. console.info("Button1");
14. return true;
15. })
16. Button('Button2').id('Button2').onKeyEvent((event) => {
17. console.info("Button2");
18. return true;
19. })
20. }
21. .width('100%')
22. .height('100%')
23. .id('Row1')
24. .onKeyEventDispatch((event) => {
25. let context = this.getUIContext();
26. context.getFocusController().requestFocus('Button1');
27. return context.dispatchKeyEvent('Button1', event);
28. })
29. }
30. .height('100%')
31. .width('100%')
32. .onKeyEventDispatch((event) => {
33. if (event.type == KeyType.Down) {
34. let context = this.getUIContext();
35. context.getFocusController().requestFocus('Row1');
36. return context.dispatchKeyEvent('Row1', event);
37. }
38. return true;
39. })
40. }
41. }
```
