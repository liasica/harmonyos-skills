---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-keyboard
title: 自定义键盘
breadcrumb: 最佳实践 > 应用框架 > 输入法 > 自定义键盘
category: best-practices
scraped_at: 2026-04-29T14:11:02+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:213927209785cfdaf1a3421325e0bc73a1591e1d2e84fd60cb534720ca155c52
---

## 概述

自定义键盘是一种简易的键盘替代系统默认键盘，允许用户根据实际业务场景和习惯偏好，调整键盘的布局和位置、添加额外的功能键，使输入更加便捷和舒适，从而提升整体的用户体验。同时自定义键盘也可以增强用户输入的安全性，避免敏感信息被截取或者泄露。

本文将从以下几个方面介绍自定义键盘的实现和使用：

* [自定义键盘的实现](bpta-custom-keyboard.md#section2059651742117)
* [自定义键盘和系统键盘的切换](bpta-custom-keyboard.md#section20427115971010)
* [自定义键盘的布局避让](bpta-custom-keyboard.md#section3179730192019)
* [自定义键盘实现防截屏](bpta-custom-keyboard.md#section193891441919)

## 自定义键盘的实现

自定义键盘的实现包括以下几个步骤：

* [自定义键盘布局实现](bpta-custom-keyboard.md#section131317262217)
* [输入控件绑定自定义键盘布局](bpta-custom-keyboard.md#section147941149222)
* [自定义键盘输入控制](bpta-custom-keyboard.md#section19880122132213)
* [自定义键盘光标控制](bpta-custom-keyboard.md#section15636163317224)
* [自定义键盘弹出与收起](bpta-custom-keyboard.md#section173493918225)

### 自定义键盘布局实现

自定义键盘的布局以自定义组件的方式呈现，根据具体业务场景由开发者实现。自定义键盘的高度通过自定义组件根节点的height属性设置，宽度不可设置，默认为屏幕宽度。

```
1. @Component
2. export struct CustomKeyboard {
3. // ...
4. build() {
5. Column() {
6. // ...
7. }
8. // ...
9. .height(this.getKeyboardHeightVp())
10. // ...
11. }
12. }
```

[CustomKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboard.ets#L23-L140)

以Grid方式实现数字键盘布局示例：

**图1**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/lBsLTpQfS7O8c_LaWwjmDQ/zh-cn_image_0000002194010308.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=B589FA0235203C95D020D8B4C4FD76588EE29D154A1E6E9CB735A6D3FA8836F9)

```
1. @Component
2. export struct NumberKeyboard {
3. @Consume inputText: string;
4. @Consume keyboardController: KeyboardController;
5. layoutOptions: GridLayoutOptions = {
6. regularSize: [1, 1],
7. irregularIndexes: [14, 16],
8. onGetIrregularSizeByIndex: (index: number) => {
9. if (index === 14) {
10. return [2, 1];
11. }
12. return [1, 2];
13. }
14. };

16. build() {
17. Grid(undefined, this.layoutOptions) {
18. ForEach(numberKeyboardData, (item: Menu) => {
19. GridItem() {
20. Button(item.text, { type: ButtonType.Normal })
21. .fontColor(Color.Black)
22. .backgroundColor(item.backgroundColor)
23. .borderRadius(Constants.KEYBOARD_BUTTON_RADIUS)
24. .fontSize(Constants.KEYBOARD_BUTTON_FONTSIZE_18)
25. .padding(0)
26. .width(item.width)
27. .height(item.height)
28. .onClick(() => {
29. this.inputText = this.keyboardController.onInput(item.text);
30. })
31. }
32. }, (item: Menu) => JSON.stringify(item))
33. }
34. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
35. .rowsGap($r('app.float.number_keyboard_grid_gap'))
36. .columnsGap($r('app.float.number_keyboard_grid_gap'))
37. }
38. }
```

[NumberKeyboard.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/NumberKeyboard.ets#L21-L58)

### 输入控件绑定自定义键盘布局

输入控件（TextArea、TextInput、RichEditor、Search）支持通过[customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)属性绑定自定义键盘布局。绑定自定义键盘后，输入控件获取焦点时，不会拉起系统键盘，而是加载指定的自定义键盘。本文后续以TextInput控件为例进行介绍。

**图2**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/bLjKjKmAR0C1XnUy7f6b0Q/zh-cn_image_0000002229336101.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=33CCAE19D3EE5DD09B902BAE39FC0D5EA490E6BA1A26FEB8DC51CD981B1C86BE)

代码示例如下：

```
1. build() {
2. Column() {
3. TextInput({
4. placeholder: 'Bind Custom Keyboard',
5. text: this.inputText,
6. controller: this.textInputController
7. })
8. // ...
9. .customKeyboard(this.isCustomKeyboardAttach ? this.customKeyboard() : null)
10. // ...
11. }
12. }
13. @Builder
14. customKeyboard() {
15. CustomKeyboard()
16. }
17. }
```

[TextInputComponent.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L64-L136)

### 监听键盘弹出与收起

在输入组件内,使用@Link和@Watch('onChangeKeyboard')修饰isKeyboardShown；

当键盘状态变化后,会调用onChangeKeyboard,此时要收起键盘,则执行和键盘控制器绑定的文字输入控制器的stopEditing。

```
1. @Component
2. export struct TextInputComponent {
3. // ...
4. @Link @Watch('onChangeKeyboard') isKeyboardShown: boolean;
5. // ...
6. onChangeKeyboard() {
7. if (this.isKeyboardShown === false) {
8. this.textInputController.stopEditing();
9. }
10. }

12. // ...
13. }
```

[TextInputComponent.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L23-L133)

输入组件内有两个事件：

onFocus代表获得焦点,用户点击输入组件的时候,输入组件会获得焦点从而弹出键盘,此时设定isKeyboardShown为true,表示弹起;

onBlur代表失去焦点,当输入组件失去焦点,会被调用, 此时设为isKeyboardShown为false,表示收起;

```
1. .onBlur(() => {
2. this.isKeyboardShown = false;
3. // ...
4. })
5. .onFocus(() => {
6. this.isKeyboardShown = true;
7. // ...
8. })
```

[TextInputComponent.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L94-L106)

页面内的isKeyboardShown要和输入组件TextInputComponent 建立双向绑定,用来监听isKeyboardShown变化,响应键盘的弹出与收起.

```
1. @Entry
2. @Component
3. struct MainPage {
4. // ...
5. @State isKeyboardShown: boolean = false;
6. // ...
7. build() {
8. Navigation() {
9. Column() {
10. // ...
11. }
12. // ...
13. }
14. .onClick(() => {
15. if (this.isKeyboardShown) {
16. this.isKeyboardShown = false;
17. }
18. })
19. .mode(NavigationMode.Stack)
20. .titleMode(NavigationTitleMode.Full)
21. .title($r('app.string.main_page_title'))
22. }
23. }
```

[MainPage.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/pages/MainPage.ets#L21-L78)

## 在横竖屏切换时设置键盘高度

在键盘组件 CustomKeyboard.ets 引入方向检测与动态高度，在键盘组件内对应位置处理。

引入 @ohos.display ，新增 @State isLandscape 保存当前方向。

在 aboutToAppear 注册监听器 display.on('change') ，在aboutToDisappear 注销监听器，方向变化时调用 updateOrientation(), 通过 display.getDefaultDisplaySync() 判断 width > height 判定横屏。

```
1. @Component
2. export struct CustomKeyboard {
3. // ...

5. aboutToAppear(): void {
6. this.updateOrientation();
7. try {
8. display.on('change', this.onDisplayChange);
9. } catch (e) {
10. // ignore
11. }
12. }

14. aboutToDisappear(): void {
15. try {
16. display.off('change', this.onDisplayChange);
17. } catch (e) {
18. // ignore
19. }
20. }

22. private updateOrientation() {
23. try {
24. const d = display.getDefaultDisplaySync();
25. this.isLandscape = d.width > d.height;
26. } catch (e) {
27. this.isLandscape = false;
28. }
29. }
30. // ...
31. }
```

[CustomKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboard.ets#L25-L139)

重写 getKeyboardHeightVp() ，判断设备为平板的时候，按照平板的比例给予，横屏0.33，竖屏0.22的屏幕高度占比，手机的话固定为0.36的占比高度。

```
1. @Component
2. export struct CustomKeyboard {
3. // ...

5. private getKeyboardHeightVp(): number | Resource {
6. try {
7. const d = display.getDefaultDisplaySync();
8. const ui = this.getUIContext();
9. const screenHeightVp = ui.px2vp(d.height);
10. const shortSideVp = ui.px2vp(Math.min(d.width, d.height));
11. // Approximate judgment for tablet/large screen
12. const isLargeScreen = shortSideVp >= 600;
13. // Phone: Portrait/Landscape 36% (no orientation switching supported)
14. // Tablet: Portrait 22%, Landscape 33% (reduce height to adapt to large screen)
15. const ratio = isLargeScreen
16. ? (this.isLandscape ? 0.33 : 0.22)
17. :  0.36;

19. return Math.floor(screenHeightVp * ratio);
20. } catch (e) {
21. return $r('app.float.keyboard_total_height');
22. }
23. }
24. // ...
25. }
```

[CustomKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboard.ets#L26-L138)

修改组件高度，将键盘组件的 .height(...) 改为 .height(this.getKeyboardHeightVp()) 以采用动态计算值。

```
1. @Component
2. export struct CustomKeyboard {
3. // ...
4. build() {
5. // ...
6. // ...
7. .padding({ left: $r('app.float.keyboard_padding'), right: $r('app.float.keyboard_padding') })
8. .height(this.getKeyboardHeightVp())
9. .width('100%')
10. .backgroundColor($r('app.color.keyboard_background_color'))
11. }
12. }
```

[CustomKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboard.ets#L27-L137)

### 自定义键盘输入控制

自定义键盘可以拦截手势事件，通过对状态变量的修改，实现文本的输入。

**图3**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/T2t9cbxOTZmnauRvtsczBA/zh-cn_image_0000002194010304.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=FB3691F36CE99D9BDE4EF1BC1CD389305DAB2EDCCA10B86A9FE02FCD45E08E7A)

以英文键盘为例，监听EnglishButton的onClick事件，修改状态变量。

```
1. @Component
2. struct EnglishButton {
3. @Consume inputText: string;
4. // ...

6. build() {
7. Button({ type: ButtonType.Normal })
8. // ...
9. .onClick(() => {
10. this.inputText = this.keyboardController.onInput(this.getEnglishText(this.item));
11. })
12. }
13. }
```

[EnglishKeyboard.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/EnglishKeyboard.ets#L65-L106)

通过对状态变量inputText的修改，实现文本输入。

```
1. @Component
2. export struct TextInputComponent {
3. @Provide inputText: string = '';
4. // ...
5. build() {
6. Column() {
7. TextInput({
8. placeholder: 'Bind Custom Keyboard',
9. text: this.inputText,
10. controller: this.textInputController
11. })
12. // ...
13. }
14. }
15. // ...
16. }
```

[TextInputComponent.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L22-L137)

### 自定义键盘光标控制

通过监听TextInput的[onTextSelectionChange](../harmonyos-references/ts-basic-components-textinput.md#ontextselectionchange10)生命周期，获取初始光标位置，文本输入后，调用TextInputController的[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition8)方法，设置最终光标位置。

**图4**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/WicpjOocTzWLW0bXdh4pCA/zh-cn_image_0000002229336093.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=EE000514D3190401727AFCA53FEB76C5E14CF9C1FB7451B8986F0F2B2FAC973B)

获取光标位置：

```
1. TextInput({
2. placeholder: 'Bind Custom Keyboard',
3. text: this.inputText,
4. controller: this.textInputController
5. })
6. // ...
7. .onTextSelectionChange((start: number, end: number) => {
8. this.keyboardController.setCaretPosition(start, end);
9. })
10. // ...
```

[TextInputComponent.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L68-L135)

设置光标位置：

```
1. onChange(value: string) {
2. this.text = value;
3. if (this.keyboardType !== 'System') {
4. this.textInputController?.caretPosition(this.targetCaretPos);
5. }
6. }
```

[KeyboardController.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/model/KeyboardController.ets#L85-L90)

### 自定义键盘弹出与收起

通过对焦点进行控制，可以实现键盘的弹出和收起，参考[软键盘的弹出收起和监听](bpta-keyboard-layout-adapt.md#section117216355229)。

开发者也可以通过TextInputController的[stopEditing](../harmonyos-references/ts-basic-components-textinput.md#stopediting10)方法控制键盘关闭，下面的自定义键盘示例中，点击确认按键关闭自定义键盘。

**图5**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/DR6OqHQtRUOGEa39-gpZLw/zh-cn_image_0000002229336097.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=8255109A3F82F37CB06E9CEF6591A588CC84C4C8FCFD99BFDA61A48971FA7CC2)

```
1. onInput(value: string | Resource): string {
2. // ...

4. switch (value.id) {
5. // ...
6. case $r('app.string.keyboardButton_finish').id:
7. this.textInputController?.stopEditing();
8. break;
9. // ...
10. }
11. return this.text;
12. }
```

[KeyboardController.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/model/KeyboardController.ets#L29-L76)

## 自定义键盘和系统键盘的切换

当需要实现同一个输入框内可以切换自定义键盘和系统键盘时，可以通过如下方式实现：

Tab栏点击“123”、“ABC”按钮，this.isCustomKeyboardAttach为true，TextInput绑定自定义键盘；点击“中文”按钮，this.isCustomKeyboardAttach为false，切换系统键盘。

**图6**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/_1OYNlhaRoe7Mnt7SUGFLw/zh-cn_image_0000002193850728.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=8F4811E805DC73786811560EF727F1EF20B15E8534AD6791A4242028EBD7454B)

```
1. TextInput({
2. placeholder: 'Bind Custom Keyboard',
3. text: this.inputText,
4. controller: this.textInputController
5. })
6. // ...
7. .customKeyboard(this.isCustomKeyboardAttach ? this.customKeyboard() : null)
```

[TextInputComponent.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/TextInputComponent.ets#L69-L85)

## 自定义键盘的布局避让

### 使用系统提供的自定义键盘避让功能

为了确保输入框不被自定义键盘挡住，系统默认提供了输入框避让自定义键盘的能力。在TextInput组件的customKeyboard属性设置[supportAvoidance](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)为true，开启系统提供的自定义键盘避让功能。键盘的避让机制和常见问题的解决方法，可以参考[软键盘布局适配场景介绍](bpta-keyboard-layout-adapt.md#section08221814182316)。

**图7**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/LaUyxdTrRoeiNXddwnI8SA/zh-cn_image_0000002229450589.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=2786374E1C4A7BDD5A4138AA29FA85B0BD6F8DD6E58536A107440118E32B9673)

```
1. // entry/src/main/ets/view/TextInputComponent.ets
2. TextInput({
3. placeholder: 'Bind Custom Keyboard',
4. text: this.inputText,
5. controller: this.textInputController
6. })
7. .customKeyboard(this.customKeyboard(), { supportAvoidance: true })
8. // ...
```

[CustomKeyboardComponent.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboardComponent.ets#L51-L85)

系统默认的自定义键盘避让功能只能保证输入框不被遮挡，输入框下方的组件可能会被自定义键盘挡住，如上图中所示，输入框下方的tab栏被自定义键盘挡住。为解决这一问题，需要开发者自己实现自定义键盘的避让功能。

### 开发者自己实现自定义键盘的避让功能

开发者需要监听自定义键盘根节点的onAreaChange生命周期，获取自定义键盘的高度，根据实际场景设置布局的避让。

**图8**   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Ftk4MecRQSGh6KVwd06uOg/zh-cn_image_0000002193850704.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=4755FB2DB9C2EFF8B85CDABE2C3A3E7E83C10AA565C3AA734C476731F1A149EA)

监听自定义键盘布局的onAreaChange生命周期，通过newValue.height获取自定义键盘弹出时的高度，根据实际业务场景计算布局避让高度avoidHeight。

```
1. @Component
2. export struct CustomKeyboard {
3. // ...
4. build() {
5. Column() {
6. // ...
7. }
8. .onAreaChange((oldValue: Area, newValue: Area) => {
9. this.customKeyboardHeight = Number(newValue.height);
10. let avoidHeight: number = (this.isCustomKeyboardAttach ? this.customKeyboardHeight : this.systemKeyboardHeight)
11. - this.bottomRectHeight;
12. this.keyboardController.changeAvoidHeight(avoidHeight);
13. })
14. // ...
15. }
16. }
```

[CustomKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/CustomizeKeyboard/blob/master/entry/src/main/ets/view/CustomKeyboard.ets#L24-L141)

通过[emitter](../harmonyos-references/js-apis-emitter.md)的方式，发送自定义键盘高度变化的通知。

```
1. changeAvoidHeight(value: number) {
2. let event: emitter.InnerEvent = {
3. eventId: Constants.AVOID_EVENT_ID
4. };
5. let eventData: emitter.EventData = {
6. data: {
7. 'avoidHeight': value
8. }
9. };
10. emitter.emit(event, eventData);
11. }
```

[KeyboardController.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/model/KeyboardController.ets#L104-L114)

接收到高度变化通知后，根据实际业务场景，设置页面的避让高度。

```
1. @Entry
2. @Component
3. struct MainPage {
4. @State bottomPadding: number = 210;
5. @State isKeyboardShown: boolean = false;
6. aboutToAppear(): void {
7. let event: emitter.InnerEvent = {
8. eventId: 1
9. }
10. emitter.on(event, (eventData: emitter.EventData) => {
11. if (eventData.data) {
12. let avoidHeight: number = eventData.data['avoidHeight'];
13. if (avoidHeight === 0) {
14. this.bottomPadding = 210;
15. } else {
16. this.bottomPadding = avoidHeight;
17. }
18. }
19. })
20. }
21. build() {
22. Navigation() {
23. Column() {
24. // ...
25. }
26. .padding({ bottom: this.bottomPadding })
27. // ...
28. }
29. .onClick(() => {
30. if (this.isKeyboardShown) {
31. this.isKeyboardShown = false;
32. }
33. })
34. .mode(NavigationMode.Stack)
35. .titleMode(NavigationTitleMode.Full)
36. .title($r('app.string.main_page_title'))
37. }
38. }
```

[MainPage.ets](https://gitcode.com/harmonyos_samples/CustomizeKeyboard/blob/master/entry/src/main/ets/pages/MainPage.ets#L20-L79)

## 自定义键盘实现防截屏

用户使用自定义键盘输入敏感信息时，可以设置禁止截屏，有效防止他人在未经许可的情况下获取用户的敏感信息，从而保护用户的隐私安全。具体实现参考[如何实现防截屏功能](../harmonyos-faqs/faqs-arkui-3.md)。

## 示例代码

* [实现自定义键盘功能](https://gitcode.com/harmonyos_samples/CustomizeKeyboard)
