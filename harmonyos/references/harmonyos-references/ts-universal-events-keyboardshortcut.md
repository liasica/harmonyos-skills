---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-keyboardshortcut
title: 组件快捷键事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 交互响应事件 > 组件快捷键事件
category: harmonyos-references
scraped_at: 2026-04-29T13:51:10+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:86384f6be4acf5db866beb75ef4ab05a2e8ae8926c3382877d678fdd7bf854ad
---

开发者可以设置组件的自定义组合键，每个组件可以设置多个组合键。

即使组件未获焦或是在所在页面未展示，只要已经挂载到获焦窗口的组件树上就会响应自定义组合键。

开发者在设置组合键的同时可以设置自定义事件，组合键按下时，触发该自定义事件，若没有设置自定义事件，则组合键行为与click行为一致。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## keyboardShortcut

PhonePC/2in1TabletTVWearable

keyboardShortcut(value: string | FunctionKey, keys: Array<ModifierKey>, action?: () => void): T

设置组件的自定义组合键。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [FunctionKey](ts-appendix-enums.md#functionkey10) | 是 | 热键的单个字符（可以通过键盘输入的字符）或[FunctionKey](ts-appendix-enums.md#functionkey10)。  空字符串意为取消快捷键绑定。 |
| keys | Array<[ModifierKey](ts-appendix-enums.md#modifierkey10)> | 是 | 热键组合。  仅当value为[FunctionKey](ts-appendix-enums.md#functionkey10)的情况下keys的值可以为空。 |
| action | () => void | 否 | 组合快捷键触发成功后的自定义事件回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 快捷键使用注意事项

PhonePC/2in1TabletTVWearable

快捷键是对系统按键的响应，优先于普通的按键事件OnKeyEvent，按键事件触发的逻辑详见[按键事件数据流](../harmonyos-guides/arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

| 场景 | 快捷键处理逻辑 | 例子 |
| --- | --- | --- |
| 所有支持onClick事件的组件 | 支持自定义组合键 | 无 |
| 自定义组合键要求 | 控制键Ctrl、Shift、Alt及它们的组合加上热键的单个字符（可以通过键盘输入的字符）或[FunctionKey](ts-appendix-enums.md#functionkey10) | Button('button1').keyboardShortcut('a',[ModifierKey.CTRL]) |
| 多个不同组件设置相同组合键 | 只响应节点树上的深度最浅的组件，其它组件不响应快捷键 | Button('button1').keyboardShortcut('a',[ModifierKey.CTRL])  Button('button2').keyboardShortcut('a',[ModifierKey.CTRL]) |
| 无论组件是否获焦 | 只要窗口获焦，快捷键就会响应 | 无 |
| 使用单个FunctionKey触发快捷键 | 单个FunctionKey，没有ModifierKey，可以绑定为快捷键 | Button('button1').keyboardShortcut(FunctionKey.F2,[]) |
| keyboardShortcut的入参value为空 | 取消绑定的快捷键。  绑定了多个快捷键的不能解除绑定快捷键 | Button('button1').keyboardShortcut('',[ModifierKey.CTRL])  Button('button2').keyboardShortcut('',[]) |
| keyboardShortcut接口中的keys命令中Ctrl、Shift、Alt | 不区分左右键都响应 | Button('button1').keyboardShortcut('a',[ModifierKey.CTRL, ModifierKey.ALT]) |
| keyboardShortcut接口中的value单个字符 | 不区分大小写都响应 | Button('button1').keyboardShortcut('a',[ModifierKey.CTRL])  Button('button2').keyboardShortcut('A',[ModifierKey.CTRL]) |
| 快捷键的响应 | keys键处于按下状态且value键触发down事件（长按会连续响应） | 无 |
| 隐藏组件 | 响应快捷键 | 无 |
| 不可交互（[enabled](ts-universal-attributes-enable.md#enabled)设置为false）状态的组件 | 不响应快捷键 | 无 |
| 1. 组件的组合键(包括系统预定义快捷键)相同时  2. 接口参数value有多个字符时  3. 接口参数keys有重复的控制键时 | 这几种情况不绑定组合键，先前绑定的组合键仍然有效 | Button('button1').keyboardShortcut(FunctionKey.F4,[ModifierKey.ALT])  Button('button2').keyboardShortcut('ab',[ModifierKey.CTRL])  Button('button3').keyboardShortcut('ab',[ModifierKey.CTRL,ModifierKey.CTRL]) |

### 禁止绑定的系统快捷键

以下组合键绑定为快捷键不生效。

* Alt + F4
* Alt + Shift + F4
* Alt + TAB
* Alt + Shift + TAB
* Ctrl + Shift + ESC

### 系统已存在的按键事件

已存在如下系统响应的按键事件，具体规格如下表。

表中的按键事件与自定义按键事件的触发有优先级关系，高优先级的事件会拦截低优先级事件，焦点事件响应优先级详见[按键事件数据流](../harmonyos-guides/arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

| 快捷键 | 获焦组件 | 用途 | 事件处理类别 |
| --- | --- | --- | --- |
| 方向键、Shift + 方向键 | 输入框组件 | 移动光标 | 输入法 |
| 方向键、Shift + 方向键 | 通用组件 | 系统处于走焦状态时，用于方向走焦 | 系统按键 |
| TAB、Shift + TAB | 通用组件 | 触发进入走焦状态/走焦 | 系统按键 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件快捷键）

该示例通过设置组件的快捷键，同时按控制键+对应的字符可以触发组件响应快捷键，并触发onClick事件或自定义事件。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World'

6. build() {
7. Row() {
8. Column({ space: 5 }) {
9. Text(this.message)
10. Button("Test short cut 1").onClick((event: ClickEvent) => {
11. this.message = "I clicked Button 1";
12. console.info("I clicked 1");
13. }).keyboardShortcut('.', [ModifierKey.SHIFT, ModifierKey.CTRL, ModifierKey.ALT])
14. .onKeyEvent((event: KeyEvent) => {
15. console.info("event.keyCode: " + JSON.stringify(event));
16. })
17. Button("Test short cut 2").onClick((event: ClickEvent) => {
18. this.message = "I clicked Button 2";
19. console.info("I clicked 2");
20. }).keyboardShortcut('1', [ModifierKey.CTRL])
21. Button("Test short cut 3").onClick((event: ClickEvent) => {
22. this.message = "I clicked Button 3";
23. console.info("I clicked 3");
24. }).keyboardShortcut('A', [ModifierKey.SHIFT])
25. Button("Test short cut 4").onClick((event: ClickEvent) => {
26. this.message = "I clicked Button 4";
27. console.info("I clicked 4");
28. }).keyboardShortcut(FunctionKey.F5, [], () => {
29. this.message = "I clicked Button 4";
30. console.info("I clicked user callback.");
31. }).keyboardShortcut(FunctionKey.F3, [])
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/KFGeVQgvS1iOe9rnLYLSTQ/zh-cn_image_0000002589325861.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=C83DA1F9F1FB06E8F33A06BC2F9DE658B67B6C76B5FE258AD45BC625E35B3612)

### 示例2（快捷键的绑定和解除绑定）

该示例演示了如何实现快捷键的绑定和解除绑定。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'disable'
5. @State shortCutEnable: boolean = false
6. @State keyValue: string = ''

8. build() {
9. Row() {
10. Column({ space: 5 }) {
11. Text('Ctrl+A is ' + this.message)
12. Button("Test short cut").onClick((event: ClickEvent) => {
13. this.message = "I clicked Button";
14. console.info("I clicked");
15. }).keyboardShortcut(this.keyValue, [ModifierKey.CTRL])
16. Button(this.message + 'shortCut').onClick((event: ClickEvent) => {
17. this.shortCutEnable = !this.shortCutEnable;
18. this.message = this.shortCutEnable ? 'enable' : 'disable';
19. this.keyValue = this.shortCutEnable ? 'a' : '';
20. })
21. Button('multi-shortcut').onClick((event: ClickEvent) => {
22. console.info('Trigger keyboard shortcut success.')
23. }).keyboardShortcut('q', [ModifierKey.CTRL])
24. .keyboardShortcut('w', [ModifierKey.CTRL])
25. .keyboardShortcut('', []) // 不生效，绑定了多个快捷键的组件不能解除绑定快捷键
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/9_iYcVDvSmypcr8IaWEeAw/zh-cn_image_0000002589245803.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055107Z&HW-CC-Expire=86400&HW-CC-Sign=910B1F4CE4964938B889AB51C1D290DFA3B1C9EC5604BB6985360E04BF7B98B2)
