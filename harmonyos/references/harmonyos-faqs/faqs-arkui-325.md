---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-325
title: 如何控制CustomDialog显示层级
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何控制CustomDialog显示层级
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b22e7f8c0187621c99715f196eae0e451df75e2aeb4118ea531cb4ecb6a83d08
---

**问题现象**

在A页面弹出一个CustomDialog，若Dialog未关闭时从A页面跳转到B页面，此时会发现在A页面弹出的Dialog会出现在B页面的层级上方。请问有什么方式可以让页面B盖住Dialog？

**解决措施**

原因是CustomDialog的默认层级高于页面。可以使用navigation方式跳转，它主要用于实现页面间以及组件内部的页面跳转，页面层级由导航栈管理，默认后打开的页面层级高于之前的页面，navigation跳转时系统会自动处理页面层级关系，包括关闭前页面的所有弹窗。具体请参考如下示例代码：

```
1. @Component
2. struct PrivacyDetailPage {
3. @State message: string = 'Hello World';

5. build() {
6. NavDestination() {
7. Row() {
8. Column() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. }
13. .width('100%')
14. }
15. .height('100%')
16. }
17. .onBackPressed(() => {
18. this.getUIContext().getPromptAction().showToast({ message: '123' });
19. return false;
20. })
21. }
22. }

24. @Entry
25. @Component
26. struct CustomDialogDisplayLevel {
27. // Used for navigation stack management
28. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
29. @State textValue: string = 'Input';
30. // Visible and hidden control is set to not occupied
31. @State visible: Visibility = Visibility.None;

33. @Builder
34. pageMap(name: string) {
35. if (name === 'pageOne') {
36. PrivacyDetailPage()
37. }
38. }

40. build() {
41. Navigation(this.pageInfos) {
42. Column() {
43. Stack() {
44. Row() {
45. Column() {
46. Text('I am the first page')
47. .fontSize(30)
48. .fontWeight(FontWeight.Bold)
49. Button('Button')
50. .onClick(() => {
51. console.info('hit me!');
52. if (this.visible === Visibility.Visible) {
53. this.visible = Visibility.None;
54. } else {
55. this.visible = Visibility.Visible;
56. }
57. })
58. .backgroundColor(0x777474)
59. .fontColor(0x000000)
60. }
61. .height('100%')
62. .width('100%')
63. .justifyContent(FlexAlign.Start)
64. .alignItems(HorizontalAlign.Center)
65. }
66. .height('100%')
67. .backgroundColor('#FFF')

69. Text('')
70. .onClick(() => {
71. if (this.visible === Visibility.Visible) {
72. this.visible = Visibility.None;
73. } else {
74. this.visible = Visibility.Visible;
75. }
76. })
77. .width('100%')
78. .height('100%')
79. // set opacity
80. .opacity(0.5)
81. .backgroundColor(Color.Black)
82. .visibility(this.visible)
83. Column() {
84. GridRow({
85. columns: {
86. xs: 1,
87. sm: 4,
88. md: 8,
89. lg: 12
90. },
91. breakpoints: {
92. value: ['400vp', '600vp', '800vp'],
93. reference: BreakpointsReference.WindowSize
94. },
95. }) {
96. GridCol({
97. span: {
98. xs: 1,
99. sm: 2,
100. md: 4,
101. lg: 8
102. },
103. offset: {
104. xs: 0,
105. sm: 1,
106. md: 2,
107. lg: 2
108. }
109. }) {
110. Column() {
111. Text('Privacy')
112. .fontSize(20)
113. .margin({
114. top: 10,
115. bottom: 10
116. })
117. Text('Do you want to jump to the privacy details page?')
118. .fontSize(16)
119. .margin({ bottom: 10 })
120. Flex({ justifyContent: FlexAlign.SpaceAround }) {
121. Button('Cancel')
122. .onClick(() => {
123. if (this.visible === Visibility.Visible) {
124. this.visible = Visibility.None;
125. } else {
126. this.visible = Visibility.Visible;
127. }
128. })
129. .backgroundColor(0xffffff)
130. .fontColor(Color.Black)
131. Button('OK')
132. .onClick(() => {
133. try {
134. this.pageInfos.pushPath({ name: 'pageOne' });
135. } catch (error) {
136. let err = error as BusinessError;
137. hilog.error(0x00, 'PrivacyDetailPage', `error code: ${err.code},message:${err.message}`);
138. }
139. })
140. .backgroundColor(0xffffff)
141. .fontColor(Color.Red)
142. }
143. .margin({ bottom: 10 })
144. }
145. .backgroundColor(0xffffff)
146. .visibility(this.visible)
147. .clip(true)
148. .borderRadius(20)
149. }
150. }
151. }
152. // set dialog width
153. .width('100%')
154. }
155. }
156. .width('100%')
157. .margin({ top: 5 })
158. }
159. .navDestination(this.pageMap)
160. }
161. }
```

[ControlLevelOfCustomDialog.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ControlLevelOfCustomDialog.ets#L24-L185)
