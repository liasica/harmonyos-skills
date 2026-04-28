---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/keypressed-guidelines
title: 优先响应系统功能键开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 优先响应系统功能键开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4ad0a5d9f2adec7241387a11d9e238573bdd2b394d28b95bf6a7d9632b303b55
---

## 场景介绍

每个系统功能键均具有默认功能，由系统固定实现，比如音量键是用来调节设备音量，但是部分应用在特定场景下期望定制这部分按键的功能，本篇指导用于支撑这部分应用的诉求达成。

常见使用场景：阅读类型应用期望通过音量键翻页，相机应用期望通过音量键拍照等应用响应系统功能键做其他业务的场景。

支持功能键列表：从API version 16开始支持音量加按键和音量减按键。从API version 21开始支持多媒体播放/暂停、多媒体下一首和多媒体上一首按键。

## 约束与限制

* 应用只有处于焦点时，优先响应才生效。
* 应用选择高于系统优先响应指定的系统功能键后，功能键的默认行为将失效，所以应用需要确保只有在确定响应时才激活该功能。

## 接口说明

按键按下事件常用接口如下表所示，接口详细介绍请参考[@ohos.multimodalInput.inputConsumer](../harmonyos-references/js-apis-inputconsumer.md)。

| 接口名称 | 描述 |
| --- | --- |
| on(type: "keyPressed", options: KeyPressedConfig, callback: Callback<KeyEvent>): void | 订阅指定按键按下事件，拦截系统默认响应。 |
| off(type: "keyPressed", callback?: Callback<KeyEvent>): void | 取消按键事件订阅，恢复系统默认响应。 |

## 开发步骤

应用开启时调用[on](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeronkeypressed16)方法订阅按键按下事件，应用关闭时再用[off](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeroffkeypressed16)方法取消订阅按键按下事件。

### 音量键翻页和应用内拍照

在电子书或新闻阅读应用中，用户希望通过音量键控制翻页（例如：音量加键向下翻页，音量减键向上翻页）；在相机或扫码类应用中，用户按音量键可直接拍照，而不跳转系统相机应用。

```
1. import { inputConsumer, KeyEvent } from '@kit.InputKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { KeyCode } from '@kit.InputKit';

5. const DOMAIN = 0x0000;

7. @Entry
8. @Component
9. struct TestDemo14 {
10. @State text: string = "Default monitoring for Volume Up and Down keys has been added."
11. private volumeUpCallBackFunc: (event: KeyEvent) => void = () => {
12. }
13. private volumeDownCallBackFunc: (event: KeyEvent) => void = () => {
14. }
15. options1: inputConsumer.KeyPressedConfig = {
16. key: KeyCode.KEYCODE_VOLUME_UP,
17. action: 1, // 按下按键的行为
18. isRepeat: false, // 优先消费掉按键事件，不上报
19. }
20. options2: inputConsumer.KeyPressedConfig = {
21. key: KeyCode.KEYCODE_VOLUME_DOWN,
22. action: 1, // 按下按键的行为
23. isRepeat: false, // 优先消费掉按键事件，不上报
24. }

26. aboutToAppear(): void {
27. try {
28. // 点击了音量按键上事件回调
29. this.volumeUpCallBackFunc = (event: KeyEvent) => {
30. this.getUIContext().getPromptAction().showToast({ message: 'Volume Up key pressed' })
31. // do something
32. }

34. // 点击了音量按键下事件回调
35. this.volumeDownCallBackFunc = (event: KeyEvent) => {
36. this.getUIContext().getPromptAction().showToast({ message: 'Volume Down key pressed' })
37. // do something
38. }
39. // 注册监听事件
40. inputConsumer.on('keyPressed', this.options1, this.volumeUpCallBackFunc);
41. inputConsumer.on('keyPressed', this.options2, this.volumeDownCallBackFunc);
42. } catch (error) {
43. hilog.error(DOMAIN, 'InputConsumer', `Subscribe execute failed, error: %{public}s`,
44. JSON.stringify(error, ["code", "message"]));
45. }
46. }

48. build() {
49. Column() {
50. Row() {
51. Button('Add monitoring for Volume Up key')
52. .onClick(() => {
53. try {
54. // 添加指定回调函数
55. inputConsumer.on('keyPressed', this.options1, this.volumeUpCallBackFunc);
56. this.getUIContext()
57. .getPromptAction()
58. .showToast({ message: 'Successfully added monitoring for Volume Up key!' })
59. this.text = "Monitoring for Volume Up key has been added."
60. } catch (error) {
61. hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
62. JSON.stringify(error, ["code", "message"]));
63. this.getUIContext()
64. .getPromptAction()
65. .showToast({ message: 'Failed to add monitoring for Volume Up key!' })
66. this.text = `Failed to add monitoring for Volume Up key: ${JSON.stringify(error, ["code", "message"])}`
67. }
68. })
69. }.width('100%')
70. .justifyContent(FlexAlign.Center)
71. .margin({ top: 20, bottom: 50 })

73. Row() {
74. Button('Remove monitoring for Volume Up key')
75. .onClick(() => {
76. try {
77. // 取消指定回调函数
78. inputConsumer.off('keyPressed', this.volumeUpCallBackFunc);
79. this.getUIContext()
80. .getPromptAction()
81. .showToast({ message: 'Successfully removed monitoring for Volume Up key!' })
82. this.text = "Monitoring for Volume Up key has been removed."
83. } catch (error) {
84. hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
85. JSON.stringify(error, ["code", "message"]));
86. this.getUIContext()
87. .getPromptAction()
88. .showToast({ message: 'Failed to remove monitoring for Volume Up key!' })
89. this.text = `Failed to remove monitoring for Volume Up key: ${JSON.stringify(error, ["code", "message"])}`
90. }
91. })
92. }.width('100%')
93. .justifyContent(FlexAlign.Center)
94. .margin({ top: 20, bottom: 50 })

96. Row() {
97. Button('Add monitoring for Volume Down key')
98. .onClick(() => {
99. try {
100. // 添加指定回调函数
101. inputConsumer.on('keyPressed', this.options2, this.volumeDownCallBackFunc);
102. this.getUIContext()
103. .getPromptAction()
104. .showToast({ message: 'Successfully added monitoring for Volume Down key!' })
105. this.text = "Monitoring for Volume Down key has been added."
106. } catch (error) {
107. hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
108. JSON.stringify(error, ["code", "message"]));
109. this.getUIContext()
110. .getPromptAction()
111. .showToast({ message: 'Failed to add monitoring for Volume Down key!' })
112. this.text = `Failed to add monitoring for Volume Down key: ${JSON.stringify(error, ["code", "message"])}`
113. }
114. })
115. }.width('100%')
116. .justifyContent(FlexAlign.Center)
117. .margin({ top: 20, bottom: 50 })

119. Row() {
120. Button('Remove monitoring for Volume Down key')
121. .onClick(() => {
122. try {
123. // 取消指定回调函数
124. inputConsumer.off('keyPressed', this.volumeDownCallBackFunc);
125. this.getUIContext()
126. .getPromptAction()
127. .showToast({ message: 'Successfully removed monitoring for Volume Down key!' })
128. this.text = "Monitoring for Volume Down key has been removed."
129. } catch (error) {
130. hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
131. JSON.stringify(error, ["code", "message"]));
132. this.getUIContext()
133. .getPromptAction()
134. .showToast({ message: 'Failed to remove monitoring for Volume Down key!' })
135. this.text =
136. `Failed to remove monitoring for Volume Down key: ${JSON.stringify(error, ["code", "message"])}`
137. }
138. })
139. }.width('100%')
140. .justifyContent(FlexAlign.Center)
141. .margin({ top: 20, bottom: 50 })

143. Row() {
144. Text(this.text)
145. }
146. .width('100%')
147. .justifyContent(FlexAlign.Center)
148. }.width('100%').height('100%')
149. }
150. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/ArkTSInputConsumer/entry/src/main/ets/pages/Index.ets#L16-L168)
