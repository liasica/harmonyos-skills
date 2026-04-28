---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id
title: 组件标识
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 组件标识
category: harmonyos-references
scraped_at: 2026-04-28T08:01:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dfd740baf7360a4081c4af0abef3caf333175df510f0ebd443b3c47e5600ffcc
---

id为组件的唯一标识，在整个应用内唯一。本模块提供组件标识相关接口，可以获取指定id组件的属性，也提供向指定id组件发送事件的功能。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 若同一个组件设置了多个id或者key，最后设置的生效。

## id

PhonePC/2in1TabletTVWearable

id(value: string): T

组件的唯一标识，唯一性由使用者保证。当未设置id时，组件默认id为空。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 组件的唯一标识，唯一性由使用者保证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## key12+

PhonePC/2in1TabletTVWearable

key(value: string): T

组件的唯一标识，唯一性由使用者保证。

此接口仅用于对应用的测试。与id同时使用时，后赋值的属性会覆盖先赋值的属性，建议仅设置id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 组件的唯一标识，唯一性由使用者保证。  默认值：'' |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 基于组件标识的拓展能力

PhonePC/2in1TabletTVWearable

组件标识的拓展能力仅用于对应用的测试，以下各个接口示例，需要在应用工程的ohosTest/ets/test目录中调试，具体可以参考[自动化测试框架使用指导](../harmonyos-guides/arkxtest-guidelines.md)。

### getInspectorByKey9+

getInspectorByKey(id: string): string

获取指定id的组件的所有属性，不包括子组件信息。

此接口仅用于对应用的测试，使用时建议等应用启动且布局完成后再调用此接口。由于耗时长，不建议测试之外的场景使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 要获取属性的组件id。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 组件属性列表的JSON字符串。  **说明**：  字符串信息包含组件的tag、id、位置信息(相对于窗口左上角的坐标)以及用于测试检查的组件所包含的相关属性信息。组件中每个字段的含义请参考[getInspectorInfo](js-apis-arkui-framenode.md#getinspectorinfo12)的返回值说明。 |

**示例:**

```
1. @Entry
2. @Component
3. struct ComponentPage {
4. build() {
5. Column() {
6. Text("Hello World")
7. .fontSize(20)
8. .id("TEXT")
9. .onClick(() => {
10. console.info(`Text is clicked`);
11. })
12. Button('TEST BUTTON').onClick(() => {
13. let result = getInspectorByKey("TEXT");
14. console.info(`result is ${result}`);
15. })
16. }
17. .width('100%')
18. .height('100%')
19. }
20. }
```

### getInspectorTree9+

getInspectorTree(): Object

获取组件树及组件属性。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Object | 组件树及组件属性列表的JSON对象。组件中每个字段的含义请参考[getInspectorInfo](js-apis-arkui-framenode.md#getinspectorinfo12)的返回值说明。 |

**示例:**

```
1. @Entry
2. @Component
3. struct ComponentPage {
4. build() {
5. Column() {
6. Text("Hello World")
7. .fontSize(20)
8. .id("TEXT")
9. .onClick(() => {
10. console.info(`Text is clicked`);
11. })
12. Button('TEST BUTTON').onClick(() => {
13. let result = getInspectorTree();
14. console.info(`result is ${JSON.stringify(result)}`);
15. })
16. }
17. .width('100%')
18. .height('100%')
19. }
20. }
```

### sendEventByKey9+

sendEventByKey(id: string, action: number, params: string): boolean

给指定id的组件发送事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 要触发事件的组件的id。 |
| action | number | 是 | 要触发的事件类型，目前支持取值：  - 点击事件Click: 10。  - 长按事件LongClick: 11。 |
| params | string | 是 | 事件参数，无参数传空字符串 ""。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| boolean | 找不到指定id的组件时返回false，其余情况返回true。 |

**示例:**

```
1. @Entry
2. @Component
3. struct ComponentPage {
4. build() {
5. Column() {
6. Text("Hello World")
7. .fontSize(20)
8. .id("TEXT")
9. .onClick(() => {
10. console.info(`Text is clicked`);
11. })
12. Button('TEST BUTTON').onClick(() => {
13. sendEventByKey("TEXT", 10, "");
14. })
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

### sendTouchEvent9+

sendTouchEvent(event: TouchObject): boolean

发送触摸事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [TouchObject](ts-universal-events-touch.md#touchobject) | 是 | 触发触摸事件的位置，event参数见[TouchObject](ts-universal-events-touch.md#touchobject)的介绍。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

### sendKeyEvent9+

sendKeyEvent(event: KeyEvent): boolean

发送按键事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [KeyEvent](ts-universal-events-key.md#keyevent对象说明) | 是 | 按键事件，event参数见[KeyEvent](ts-universal-events-key.md#keyevent对象说明)介绍。 |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

### sendMouseEvent9+

sendMouseEvent(event: MouseEvent): boolean

发送鼠标事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明) | 是 | 鼠标事件，event参数见[MouseEvent](ts-universal-mouse-key.md#mouseevent对象说明)介绍。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要展示如何通过组件标识接口，获取特定id组件的属性，以及如何向该id的组件触发事件。

```
1. // xxx.ets
2. import { IntentionCode } from '@kit.InputKit';

4. class Utils {
5. static rect_left: number;
6. static rect_top: number;
7. static rect_right: number;
8. static rect_bottom: number;
9. static rect_value: Record<string, number>;

11. // 获取组件所占矩形区域坐标
12. static getComponentRect(key: string): Record<string, number> {
13. let strJson = getInspectorByKey(key);
14. let obj: Record<string, string> = JSON.parse(strJson);
15. console.info("[getInspectorByKey] current component obj is: " + JSON.stringify(obj));
16. let rectInfo: string[] = JSON.parse('[' + obj.$rect + ']');
17. console.info("[getInspectorByKey] rectInfo is: " + rectInfo);
18. Utils.rect_left = JSON.parse('[' + rectInfo[0] + ']')[0]; // 相对于组件左上角的水平方向坐标
19. Utils.rect_top = JSON.parse('[' + rectInfo[0] + ']')[1]; // 相对于组件左上角的垂直方向坐标
20. Utils.rect_right = JSON.parse('[' + rectInfo[1] + ']')[0]; // 相对于组件右下角的水平方向坐标
21. Utils.rect_bottom = JSON.parse('[' + rectInfo[1] + ']')[1]; // 相对于组件右下角的垂直方向坐标
22. return Utils.rect_value = {
23. "left": Utils.rect_left,
24. "top": Utils.rect_top,
25. "right": Utils.rect_right,
26. "bottom": Utils.rect_bottom
27. };
28. };
29. }

31. @Entry
32. @Component
33. struct IdExample {
34. @State text: string = '';

36. build() {
37. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {

39. Button() {
40. Text('onKeyTab').fontSize(25).fontWeight(FontWeight.Bold)
41. }.margin({ top: 20 }).backgroundColor('#0D9FFB')
42. .onKeyEvent(() => {
43. this.text = "onKeyTab";
44. })

46. Button() {
47. Text('click to start').fontSize(25).fontWeight(FontWeight.Bold)
48. }.margin({ top: 20 })
49. .onClick(() => {
50. console.info(getInspectorByKey("click"));
51. console.info(JSON.stringify(getInspectorTree()));
52. this.text = "Button 'click to start' is clicked";
53. setTimeout(() => {
54. sendEventByKey("longClick", 11, ""); // 向id为"longClick"的组件发送长按事件
55. }, 2000)
56. }).id('click')

58. Button() {
59. Text('longClick').fontSize(25).fontWeight(FontWeight.Bold)
60. }.margin({ top: 20 }).backgroundColor('#0D9FFB')
61. .gesture(
62. LongPressGesture().onActionEnd(() => {
63. console.info('long clicked');
64. this.text = "Button 'longClick' is longclicked";
65. setTimeout(() => {
66. let rect = Utils.getComponentRect('onTouch'); // 获取id为"onTouch"组件的矩形区域坐标
67. let touchPoint: TouchObject = {
68. id: 1,
69. type: TouchType.Down,
70. x: rect.left + (rect.right - rect.left) / 2, // 相对于组件左上角的水平方向坐标
71. y: rect.top + (rect.bottom - rect.top) / 2, // 相对于组件左上角的垂直方向坐标
72. screenX: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的水平方向坐标，API10已废弃，采用windowX替代
73. screenY: rect.top + (rect.bottom - rect.top) / 2, // 相对于应用窗口左上角的垂直方向坐标，API10已废弃，采用windowY替代
74. windowX: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的水平方向坐标
75. windowY: rect.top + (rect.bottom - rect.top), // 相对于应用窗口左上角的垂直方向坐标
76. displayX: rect.left + (rect.right - rect.left) / 2, // 相对于设备屏幕左上角的水平方向坐标
77. displayY: rect.top + (rect.bottom - rect.top) / 2, // 相对于设备屏幕左上角的垂直方向坐标
78. };
79. sendTouchEvent(touchPoint); // 发送触摸事件
80. touchPoint.type = TouchType.Up;
81. sendTouchEvent(touchPoint); // 发送触摸事件
82. }, 2000)
83. })).id('longClick')

85. Button() {
86. Text('onTouch').fontSize(25).fontWeight(FontWeight.Bold)
87. }.type(ButtonType.Capsule).margin({ top: 20 })
88. .onClick(() => {
89. console.info('onTouch is clicked');
90. this.text = "Button 'onTouch' is clicked";
91. setTimeout(() => {
92. let rect = Utils.getComponentRect('onMouse'); // 获取id为"onMouse"组件的矩形区域坐标
93. let mouseEvent: MouseEvent = {
94. button: MouseButton.Left,
95. action: MouseAction.Press,
96. x: rect.left + (rect.right - rect.left) / 2, // 相对于组件左上角的水平方向坐标
97. y: rect.top + (rect.bottom - rect.top) / 2, // 相对于组件左上角的垂直方向坐标
98. screenX: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的水平方向坐标，API10已废弃，采用windowX替代
99. screenY: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的垂直方向坐标，API10已废弃，采用windowY替代
100. windowX: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的水平方向坐标
101. windowY: rect.left + (rect.right - rect.left) / 2, // 相对于应用窗口左上角的垂直方向坐标
102. displayX: rect.left + (rect.right - rect.left) / 2, // 相对于设备屏幕左上角的水平方向坐标
103. displayY: rect.left + (rect.right - rect.left) / 2, // 相对于设备屏幕左上角的垂直方向坐标
104. stopPropagation: () => {
105. },
106. timestamp: 1,
107. target: {
108. area: {
109. width: 1,
110. height: 1,
111. position: {
112. x: 1,
113. y: 1
114. },
115. globalPosition: {
116. x: 1,
117. y: 1
118. }
119. }
120. },
121. source: SourceType.Mouse,
122. pressure: 1,
123. tiltX: 1,
124. tiltY: 1,
125. sourceTool: SourceTool.Unknown
126. };
127. sendMouseEvent(mouseEvent); // 发送鼠标事件
128. }, 2000)
129. }).id('onTouch')

131. Button() {
132. Text('onMouse').fontSize(25).fontWeight(FontWeight.Bold)
133. }.margin({ top: 20 }).backgroundColor('#0D9FFB')
134. .onMouse(() => {
135. console.info('onMouse');
136. this.text = "Button 'onMouse' in onMouse";
137. setTimeout(() => {
138. let keyEvent: KeyEvent = {
139. type: KeyType.Down,
140. keyCode: 2049,
141. keyText: 'tab',
142. keySource: 4,
143. deviceId: 0,
144. metaKey: 0,
145. timestamp: 0,
146. stopPropagation: () => {
147. },
148. intentionCode: IntentionCode.INTENTION_DOWN
149. };
150. sendKeyEvent(keyEvent); // 发送按键事件
151. }, 2000)
152. }).id('onMouse')

154. Text(this.text).fontSize(25).padding(15)
155. }
156. .width('100%').height('100%')
157. }
158. }
```
