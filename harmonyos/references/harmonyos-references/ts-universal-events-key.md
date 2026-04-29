---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key
title: 按键事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 按键事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e30dd0aa2ab4c7283beabd9f91591e2700436c647a41b8cd80aaa66f0f0422be
---

按键事件是指组件与物理键盘、遥控器等按键设备交互时触发的事件，适用于所有可获焦组件，例如Button。对于默认不可获焦的组件，如Text，Image等，可以将[focusable](ts-universal-attributes-focus.md#focusable)属性设置为true后使用按键事件。

按键事件触发的流程和具体时机参考[按键事件数据流](../harmonyos-guides/arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## onKeyEvent

PhonePC/2in1TabletTVWearable

onKeyEvent(event: (event: KeyEvent) => void): T

绑定该方法的组件获焦后，按键动作触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | (event: [KeyEvent](ts-universal-events-key.md#keyevent对象说明)) => void | 是 | 获得KeyEvent对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onKeyEvent15+

PhonePC/2in1TabletTVWearable

onKeyEvent(event: Callback<KeyEvent, boolean>): T

当绑定该方法的组件获焦后，按键操作将触发此回调。若此回调的返回值为true，则视为按键事件已被处理。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[KeyEvent](ts-universal-events-key.md#keyevent对象说明), boolean> | 是 | 按键事件的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onKeyPreIme12+

PhonePC/2in1TabletTVWearable

onKeyPreIme(event: Callback<KeyEvent, boolean>): T

绑定该方法的组件获焦后，按键动作优先触发该回调。

该回调的返回值为true时，视作该按键事件已被消费，后续的事件回调（keyboardShortcut、输入法事件、onKeyEventDispatch、onKeyEvent）会被拦截，不再触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[KeyEvent](ts-universal-events-key.md#keyevent对象说明), boolean> | 是 | 处理按键事件的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## onKeyEventDispatch15+

PhonePC/2in1TabletTVWearable

onKeyEventDispatch(event: Callback<KeyEvent, boolean>): T

对应组件收到按键事件时，会触发该回调，该按键事件不会分发给其子组件。不支持构造KeyEvent进行分发，只支持分发已有的按键事件。

该回调的返回值为true时，视作该按键事件已被消费，不会[冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)给父组件处理。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<[KeyEvent](ts-universal-events-key.md#keyevent对象说明), boolean> | 是 | 处理按键事件分发的回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## KeyEvent对象说明

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [KeyType](ts-appendix-enums.md#keytype) | 否 | 否 | 按键的类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| keyCode | number | 否 | 否 | 按键的键值。按键设备提供的键值请参考[KeyCode](js-apis-keycode.md#keycode)。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| keyText | string | 否 | 否 | 按键的名称。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| keySource | [KeySource](ts-appendix-enums.md#keysource) | 否 | 否 | 触发当前按键的输入设备类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| deviceId | number | 否 | 否 | 触发当前按键的输入设备ID。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| metaKey | number | 否 | 否 | 按键发生时元键（即键盘左下角紧挨Ctrl键或Fn标记了窗口logo的按键）的状态，1表示按压态，0表示未按压态。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| timestamp | number | 否 | 否 | 事件时间戳。触发事件时距离系统启动的时间间隔，单位：ns。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| stopPropagation | () => void | 否 | 否 | 阻塞[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)传递。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| intentionCode10+ | [IntentionCode](ts-universal-events-key.md#intentioncode10) | 否 | 否 | 按键对应的意图。  默认值：IntentionCode.INTENTION\_UNKNOWN。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| unicode14+ | number | 否 | 是 | 按键的Unicode码值。支持范围为非空格的基本拉丁字符：0x0021-0x007E，不支持字符为0。组合键场景下，返回当前keyEvent对应按键的Unicode码值。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| isNumLockOn19+ | boolean | 否 | 是 | NumLock是否锁定（true: 锁定；false: 解锁）。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| isCapsLockOn19+ | boolean | 否 | 是 | CapsLock是否锁定（true: 锁定；false: 解锁）。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| isScrollLockOn19+ | boolean | 否 | 是 | ScrollLock是否锁定（true: 锁定；false: 解锁）。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

### getModifierKeyState12+

PhonePC/2in1TabletTVWearable

getModifierKeyState?(keys: Array<string>): boolean

获取功能键按压状态。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | Array<string> | 是 | 功能键列表。支持功能键 'Ctrl'| 'Alt' | 'Shift'。  **说明：**  此接口不支持在手写笔场景下使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 功能键是否被按下。true表示被按下，false表示未被按下。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

## IntentionCode10+

PhonePC/2in1TabletTVWearable

type IntentionCode = IntentionCode

按键对应的意图。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [IntentionCode](js-apis-intentioncode.md#intentioncode) | 按键对应的意图。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（触发onKeyEvent回调）

该示例通过按钮设置了按键事件。按钮获焦时，按下按键可触发onKeyEvent回调。按键事件触发的流程和具体时机参考[按键事件数据流](../harmonyos-guides/arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct KeyEventExample {
5. @State text: string = ''
6. @State eventType: string = ''

8. build() {
9. Column() {
10. Button('KeyEvent')
11. .defaultFocus(true)
12. .onKeyEvent((event?: KeyEvent) => {
13. if (event) {
14. if (event.type === KeyType.Down) {
15. this.eventType = 'Down'
16. }
17. if (event.type === KeyType.Up) {
18. this.eventType = 'Up'
19. }
20. this.text = 'KeyType:' + this.eventType + '\nkeyCode:' + event.keyCode + '\nkeyText:' + event.keyText +
21. '\nintentionCode:' + event.intentionCode
22. }
23. })
24. Text(this.text).padding(15)
25. }.height(300).width('100%').padding(35)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/eslrh4VfTAKaUwE0_Z8E_g/zh-cn_image_0000002589245795.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055104Z&HW-CC-Expire=86400&HW-CC-Sign=796585502E24F4384E29D5FE3468B89305A44958415E6F3109CF740C6124F085)

### 示例2（获取Unicode码值）

该示例通过按键事件获取所按按键的Unicode码值。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct KeyEventExample {
5. @State text: string = ''
6. @State eventType: string = ''
7. @State keyType: string = ''

9. build() {
10. Column({ space: 10 }) {
11. Button('KeyEvent')
12. .onKeyEvent((event?: KeyEvent) => {
13. if (event) {
14. if (event.type === KeyType.Down) {
15. this.eventType = 'Down'
16. }
17. if (event.type === KeyType.Up) {
18. this.eventType = 'Up'
19. }
20. if (event.unicode == 97) {
21. this.keyType = 'a'
22. } else if (event.unicode == 65) {
23. this.keyType = 'A'
24. } else {
25. this.keyType = ' '
26. }
27. this.text =
28. 'KeyType:' + this.eventType + '\nUnicode:' + event.unicode + '\nkeyCode:' + event.keyCode + '\nkeyType:' +
29. this.keyType
30. }
31. })
32. Text(this.text).padding(15)
33. }.height(300).width('100%').padding(35)
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/n_4IhczyQReAVK8tvJzjZg/zh-cn_image_0000002558765984.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055104Z&HW-CC-Expire=86400&HW-CC-Sign=18DF91B19E3BA5FE780C91D24371C151051486D2326C2F8C97E9982E98BDD0C9)

### 示例3（触发onKeyPreIme回调）

该示例使用onKeyPreIme屏蔽输入框中的方向左键。

```
1. import { KeyCode } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct PreImeEventExample {
6. @State buttonText: string = '';
7. @State buttonType: string = '';
8. @State columnText: string = '';
9. @State columnType: string = '';

11. build() {
12. Column() {
13. Search({
14. placeholder: "Search..."
15. })
16. .width("80%")
17. .height("40vp")
18. .border({ radius: "20vp" })
19. .onKeyPreIme((event: KeyEvent) => {
20. // 使用方向左键不生效
21. if (event.keyCode == KeyCode.KEYCODE_DPAD_LEFT) {
22. return true;
23. }
24. return false;
25. })
26. }
27. }
28. }
```

### 示例4（使用stopPropagation阻止冒泡）

该示例使用stopPropagation阻止事件冒泡。即，通过在Button的onKeyEvent回调中加入event.stopPropagation()方法，达到“仅Button响应键盘事件，Column不响应”的效果。

说明

1. onKeyEvent事件默认是冒泡的。
2. 事件冒泡：在一个树形结构中，当子节点处理完一个事件后，再将该事件交给它的父节点处理。
3. 可以在[onKeyEvent15+](ts-universal-events-key.md#onkeyevent15)中，通过返回true消费按键事件阻止冒泡，效果等同于stopPropagation。

```
1. @Entry
2. @Component
3. struct KeyEventExample {
4. @State buttonText: string = '';
5. @State buttonType: string = '';
6. @State columnText: string = '';
7. @State columnType: string = '';

9. build() {
10. Column() {
11. Button('onKeyEvent')
12. .defaultFocus(true)
13. .width(112).height(56)
14. .onKeyEvent((event?: KeyEvent) => {
15. // 通过stopPropagation阻止事件冒泡
16. if (event) {
17. if (event.stopPropagation) {
18. event.stopPropagation();
19. }
20. if (event.type === KeyType.Down) {
21. this.buttonType = 'Down';
22. }
23. if (event.type === KeyType.Up) {
24. this.buttonType = 'Up';
25. }
26. this.buttonText = 'Button: \n' +
27. 'KeyType:' + this.buttonType + '\n' +
28. 'KeyCode:' + event.keyCode + '\n' +
29. 'KeyText:' + event.keyText;
30. }
31. })

33. Divider()
34. Text(this.buttonText).fontColor(Color.Green)

36. Divider()
37. Text(this.columnText).fontColor(Color.Red)
38. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
39. .onKeyEvent((event?: KeyEvent) => { // 给父组件Column设置onKeyEvent事件
40. if (event) {
41. if (event.type === KeyType.Down) {
42. this.columnType = 'Down';
43. }
44. if (event.type === KeyType.Up) {
45. this.columnType = 'Up';
46. }
47. this.columnText = 'Column: \n' +
48. 'KeyType:' + this.columnType + '\n' +
49. 'KeyCode:' + event.keyCode + '\n' +
50. 'KeyText:' + event.keyText;
51. }
52. })
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/hUY0jMTUQkKgl7daRlSyGw/zh-cn_image_0000002558606328.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055104Z&HW-CC-Expire=86400&HW-CC-Sign=96841B309ADBA5B1F387F5EEE63CDDB5638A9F0CAB1B9FB549FE2B85E51ED9EB)
