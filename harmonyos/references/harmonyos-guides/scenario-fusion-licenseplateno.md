---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-licenseplateno
title: 推荐车牌号场景
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 推荐车牌号场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc1d258a74d4aa7ad1e453034b5a076baa99ee5891d58c9b69cbb034018170a8
---

从5.1.0(18)开始，支持智能填充的推荐车牌号场景。

在填写车牌号表单场景时，智能填充可从用户的历史表单输入中提供输入建议，开发者可以参考如下代码进行开发。

说明

只推荐机主本人历史表单信息的车牌号信息（与登录设备的账号信息，实名姓名+手机号或邮箱信息相同）。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/XbHyMkWyQSSLpZlfIUq1Ig/zh-cn_image_0000002552959158.png?HW-CC-KV=V1&HW-CC-Date=20260427T235046Z&HW-CC-Expire=86400&HW-CC-Sign=8C6DCA784FD96D5E115C16A44505827AD0912B44CB9AFB54435F827C5DAD68B0)

## 示例代码

```
1. import { display } from '@kit.ArkUI';

3. const NEW_ENERGY_TEXT = '新能源';

5. @Extend(Text)
6. function extendStyles(value: string, width: number, height: number, active: boolean) {
7. .fontSize(value === NEW_ENERGY_TEXT ? 10 : 18)
8. .fontWeight(FontWeight.Medium)
9. .textAlign(TextAlign.Center)
10. .width(width)
11. .height(height)
12. .borderWidth('3px')
13. .borderColor(active ? Color.Blue : '#ccc')
14. .borderRadius(5)
15. }

17. @Entry
18. @Component
19. struct LicensePlate {
20. // 车牌号输入框的数量。
21. private length = 8;
22. private licenseItemId = '_license_item';
23. @State licensePlateVal: string[] = [];
24. @State activeIndex: number = -1;
25. @State itemWidth: number = 30;
26. @State itemHeight: number = 30;
27. @State inputText: string = '';
28. // 用户是否已经触发输入。
29. @State isUserInput: boolean = false;
30. // 匹配历史输入的上一个输入框的值
31. private beforeValue: string = '';

33. aboutToAppear(): void {
34. this.licensePlateVal = new Array(this.length).fill('');
35. let displayClass = display.getDefaultDisplaySync();
36. let width = displayClass.width;
37. // 每个框的宽度根据屏幕宽度计算。
38. this.itemWidth = this.getUIContext().px2vp(width) / (this.length + 1) - 4;
39. this.itemHeight = this.itemWidth * 1.2;
40. }

42. setValue(val: string): void {
43. if (!this.isUserInput) {
44. // 根据智能填充填写车牌号输入框。
45. this.handleAutoFill(val);
46. this.beforeValue = val;
47. return;
48. }
49. if (!val || val.length === 0 || this.beforeValue.length > val.length) {
50. let licensePlate = this.getLicensePlate();
51. if (licensePlate.length > 0) {
52. this.inputText = licensePlate;
53. }
54. this.beforeValue = this.inputText;
55. return;
56. }
57. let inputData = val.substring(this.beforeValue.length);
58. if (inputData.length > this.length) {
59. inputData = inputData.substring(0, this.length);
60. }
61. // 用户输入仅替换选定的输入框，而智能填充则替换所有输入框中的所有值。
62. this.handleUserInput(inputData);
63. this.beforeValue = val;
64. }

66. getLicensePlate(): string {
67. return this.licensePlateVal.join('');
68. }

70. handleUserInput(val: string): void {
71. if (val.length > this.length - this.activeIndex) {
72. val = val.substring(0, this.length - this.activeIndex);
73. }
74. for (let i = 0; i < val.length; i++) {
75. this.licensePlateVal[this.activeIndex] = val[i];
76. this.activeIndex = Math.min(this.activeIndex + 1, this.length - 1);
77. }
78. }

80. handleAutoFill(val: string): void {
81. let value = val.split('');
82. this.licensePlateVal.fill('');
83. for (let i = 0; i < this.length; i++) {
84. this.licensePlateVal[i] = i < value.length ? value[i] : this.licensePlateVal[i];
85. }
86. this.activeIndex = Math.min(value.length + 1, this.length - 1);
87. }

89. handleDelete() {
90. if (!this.licensePlateVal[this.activeIndex]) {
91. this.licensePlateVal[this.activeIndex - 1] = '';
92. } else {
93. this.licensePlateVal[this.activeIndex] = '';
94. }
95. this.activeIndex = Math.max(0, this.activeIndex - 1);
96. }

98. getValue(index: number): string {
99. return (index === this.length - 1 && !this.licensePlateVal[index]) ? NEW_ENERGY_TEXT : this.licensePlateVal[index];
100. }

102. handleLicenseClick(screenX: number) {
103. for(let index = 0; index <= 7; index++) {
104. let id = index + this.licenseItemId;
105. let position = this.getUIContext().getComponentUtils().getRectangleById(id);
106. // 相对于屏幕的位置信息,单位px
107. let left = position?.screenOffset?.x ?? 0;
108. let right = left + (position?.size?.width ?? 0);
109. if (screenX >= left && screenX <= right) {
110. this.activeIndex = index;
111. }
112. }
113. }

115. @Builder
116. displayItem(index: number) {
117. Column() {
118. Text(this.getValue(index))
119. .extendStyles(this.getValue(index), this.itemWidth, this.itemHeight, this.activeIndex === index)
120. }
121. .id(index + this.licenseItemId)
122. .padding({
123. left: 2,
124. right: 2
125. })
126. }

128. @Builder
129. buildLicensePlateNumber() {
130. Flex({
131. direction: FlexDirection.Row,
132. alignItems: ItemAlign.Center,
133. justifyContent: FlexAlign.SpaceBetween
134. }) {
135. Column() {
136. Row() {
137. Text("车牌号码")
138. }.height(30)

140. Stack({ alignContent: Alignment.BottomStart }) {
141. Row() {
142. this.displayItem(0)
143. this.displayItem(1)
144. Text('·')
145. .fontSize(22)
146. .fontWeight(600)
147. .height(this.itemHeight)
148. this.displayItem(2)
149. this.displayItem(3)
150. this.displayItem(4)
151. this.displayItem(5)
152. this.displayItem(6)
153. this.displayItem(7)
154. }

156. TextInput({ text: $$this.inputText })
157. .width('100%')
158. .height('100%')
159. .opacity(0)
160. .contentType(ContentType.LICENSE_PLATE)
161. .onClick((event) => {
162. // 相对于屏幕的X轴坐标,单位px
163. let displayX = this.getUIContext().vp2px(event.displayX);
164. this.handleLicenseClick(displayX);
165. if (this.activeIndex < 0) {
166. this.activeIndex = 0;
167. }
168. })
169. .onChange((val: string) => {
170. if (val === this.beforeValue) {
171. return;
172. }
173. this.setValue(val);
174. this.isUserInput = false;
175. })
176. .onDidInsert(() => {
177. // 当使用输入法输入数据时触发。如果输入法是自定义的，则在用户输入数据时将isUserInput设置为true。
178. this.isUserInput = true;
179. })
180. .onDidDelete((val: DeleteValue) => {
181. // 当使用输入方法删除数据时触发。如果输入方法是自定义的，当用户删除数据时，将`isUserInput`设置为`true`，并调用相应的处理函数。
182. if (val?.deleteValue?.length > 0) {
183. this.isUserInput = true;
184. }
185. this.handleDelete();
186. })
187. }
188. .height(this.itemHeight)
189. .margin({ top: 20 })
190. }
191. }
192. .backgroundColor(Color.White)
193. .height(50)
194. .margin({ left: 15, right: 15 })
195. .id("customInput")
196. .defaultFocus(false)
197. }

199. build() {
200. Column() {
201. this.buildLicensePlateNumber()
202. }
203. }
204. }
```
