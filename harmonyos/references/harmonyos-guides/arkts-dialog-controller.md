---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller
title: 弹出框控制器
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框控制器
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8fa9670080653df0b0a573a9903bb7d26cb90a98d96dd240b9506f82c6f0bec
---

ArkUI的弹出框控制器在绑定弹出框后，可提供对弹出框的操作能力，当前支持关闭功能。可以将控制器传入弹出框内容区域后进行操作。

从API version 18开始，可设置controller参数以绑定[DialogController](../harmonyos-references/js-apis-promptaction.md#dialogcontroller18)控制器，通过控制器能够操作弹出框。

## 使用约束

目前[openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)和[presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18)支持通过controller参数来绑定弹出框进行操作，目前[getDialogController](../harmonyos-references/ts-custom-component-api.md#getdialogcontroller18)支持获取自定义组件所在的弹出框的控制器。

说明

一个弹出框控制器只能绑定一个弹出框，且操作只对该弹出框生效。

使用[getDialogController](../harmonyos-references/ts-custom-component-api.md#getdialogcontroller18)获取弹出框控制器时，如果当前自定义组件不在弹出框中显示则获取为undefined。

## 创建自定义内容为ComponentContent的弹出框控制器

说明

详细变量定义请参考[完整示例](arkts-dialog-controller.md#完整示例)。

1. 初始化一个自定义弹出框内容区的入参类，内部包含弹出框控制器。

   ```
   1. class Params {
   2. public text: string = '';
   3. public dialogController: promptAction.CommonController = new promptAction.DialogController();

   5. constructor(text: string, dialogController: promptAction.CommonController) {
   6. this.text = text;
   7. this.dialogController = dialogController;
   8. }
   9. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L23-L34)
2. 初始化一个自定义的弹出框内容区，内部包含一个按钮，该按钮通过该自定义组件自带的弹出框控制器实现关闭功能。

   ```
   1. @Component
   2. struct MyComponent {
   3. build() {
   4. Column({ space: 5 }) {
   5. Button('Close Dialog(Built-in Controller)')
   6. .onClick(() => {
   7. let dialogController: promptAction.DialogController = this.getDialogController();
   8. if (dialogController !== undefined) {
   9. dialogController.close();
   10. }
   11. })
   12. }
   13. }
   14. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L36-L52)
3. 初始化另一自定义弹出框内容区，其中包含一个Text组件和一个按钮，该按钮通过外部传递的弹出框控制器用于关闭弹出框，并且该内容区还包含前一个自定义弹出框内容区。

   ```
   1. @Builder
   2. function buildText(params: Params) {
   3. Column({ space: 5 }) {
   4. Text(params.text)
   5. .fontSize(30)
   6. if (params.dialogController !== undefined) {
   7. Button('Close Dialog(External Controller)')
   8. .onClick(() => {
   9. params.dialogController.close();
   10. })
   11. }
   12. MyComponent()
   13. }
   14. .width(300)
   15. .height(200)
   16. .backgroundColor('#FFF0F0F0')
   17. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L54-L73)
4. 初始化一个弹出框控制器，并通过设置控制器参数来初始化一个弹出框内容实体对象。最后，通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)接口，并且设置初始化的内容实体对象和控制器参数以创建弹出框。

   ```
   1. let dialogController: promptAction.CommonController = new promptAction.DialogController();
   2. let contentNode: ComponentContent<Object> =
   3. new ComponentContent(this.getUIContext(), wrapBuilder(buildText),
   4. new Params(this.message, dialogController));
   5. this.getUIContext().getPromptAction().openCustomDialogWithController(
   6. contentNode, dialogController, this.baseDialogOptions).catch((err: BusinessError) => {
   7. hilog.error(0x0000, 'dialogController',
   8. 'openCustomDialogWithController error: ' + err.code + ' ' + err.message);
   9. });
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L200-L210)

## 创建自定义内容为CustomBuilder的弹出框控制器

说明

详细变量定义请参考[完整示例](arkts-dialog-controller.md#完整示例)。

1. 初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过外部传递的弹出框控制器实现关闭功能。

   ```
   1. @Builder
   2. customDialogComponent(dialogController: promptAction.DialogController) {
   3. Column({ space: 5 }) {
   4. Text(this.message)
   5. .fontSize(30)
   6. if (dialogController !== undefined) {
   7. Button('Close Dialog(External Controller)')
   8. .onClick(() => {
   9. dialogController.close();
   10. })
   11. }
   12. }
   13. .height(200)
   14. .padding(5)
   15. .justifyContent(FlexAlign.SpaceBetween)
   16. .backgroundColor('#FFF0F0F0')
   17. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L122-L141)
2. 初始化一个弹出框控制器，并通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18)接口，设置初始化的内容实体对象和控制器参数以创建弹出框。

   ```
   1. let dialogController: promptAction.CommonController = new promptAction.DialogController();
   2. this.getUIContext().getPromptAction().presentCustomDialog(() => {
   3. this.customDialogComponent(dialogController);
   4. }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
   5. hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
   6. });
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L214-L221)

## 创建自定义内容为CustomBuilderWithId的弹出框控制器

说明

详细变量定义请参考[完整示例](arkts-dialog-controller.md#完整示例)。

1. 初始化一个弹出框内容区，内部包含一个Text组件、一个通过外部传递的弹出框ID用于关闭弹出框的按钮和一个通过外部传递的弹出框控制器用于关闭弹出框的按钮。

   ```
   1. @Builder
   2. customDialogComponentWithId(dialogId: number, dialogController: promptAction.DialogController) {
   3. Column({ space: 5 }) {
   4. Text(this.message)
   5. .fontSize(30)
   6. if (dialogId !== undefined) {
   7. Button('Close Dialog(DialogID)')
   8. .onClick(() => {
   9. this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
   10. })
   11. }
   12. if (dialogController !== undefined) {
   13. Button('Close Dialog(External Controller)')
   14. .onClick(() => {
   15. dialogController.close();
   16. })
   17. }
   18. }
   19. .height(200)
   20. .padding(5)
   21. .justifyContent(FlexAlign.SpaceBetween)
   22. .backgroundColor('#FFF0F0F0')
   23. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L143-L168)
2. 初始化一个弹出框控制器，并通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18)接口，设置初始化的内容实体对象和控制器参数以创建弹出框。

   ```
   1. let dialogController: promptAction.CommonController = new promptAction.DialogController();
   2. this.getUIContext().getPromptAction().presentCustomDialog((dialogId: number) => {
   3. this.customDialogComponentWithId(dialogId, dialogController);
   4. }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
   5. hilog.error(0x0000, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
   6. });
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L225-L232)

## 在CustomDialogController内容区直接获取弹出框控制器

说明

详细变量定义请参考[完整示例](arkts-dialog-controller.md#完整示例)。

1. 初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过弹出框控制器关闭弹出框。

   ```
   1. @CustomDialog
   2. @Component
   3. struct CustomDialogExample {
   4. controller?: CustomDialogController;

   6. build() {
   7. Column({ space: 5 }) {
   8. Text('I am content')
   9. .fontSize(30)
   10. Button('Close Dialog(Built-in Controller)')
   11. .onClick(() => {
   12. let dialogController: PromptActionDialogController = this.getDialogController();
   13. if (dialogController !== undefined) {
   14. dialogController.close();
   15. }
   16. })
   17. }
   18. .height(200)
   19. .backgroundColor('#FFF0F0F0')
   20. }
   21. }
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L75-L98)
2. 初始化一个自定义弹出框构造器，关联自定义弹出框内容区。

   ```
   1. let customDialogController: CustomDialogController = new CustomDialogController({
   2. builder: CustomDialogExample(),
   3. offset: {
   4. dx: 0,
   5. dy: 50
   6. }
   7. });
   8. customDialogController.open();
   ```

   [DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L245-L254)

## 使用控制器获取弹出框的状态

在自定义弹出框场景中，从API version 20 开始，可以通过控制器调用[getState](../harmonyos-references/js-apis-promptaction.md#getstate20)接口获取弹出框状态。

说明

详细变量定义请参考[完整示例](arkts-dialog-controller.md#完整示例)。

初始化一个自定义弹出框内容区，内部包含一个Text组件和一个按钮，该按钮通过调用getState获取当前弹出框状态。

```
1. @Builder
2. customDialogComponentGetState(dialogController: promptAction.DialogController) {
3. Column({ space: 5 }) {
4. Text(this.message)
5. .fontSize(30)
6. if (dialogController !== undefined) {
7. Button('Check Status:' + this.dialogState)
8. .onClick(() => {
9. this.dialogState = dialogController.getState();
10. })
11. Button('Close Dialog(External Controller)')
12. .onClick(() => {
13. dialogController.close();
14. })
15. }
16. }
17. .height(200)
18. .padding(5)
19. .justifyContent(FlexAlign.SpaceBetween)
20. .backgroundColor('#FFF0F0F0')
21. }
```

[DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L170-L193)

## 完整示例

通过外部传递的弹出框控制器和自定义组件自带的弹出框控制器，在自定义弹出框内容区域内实现关闭功能。

```
1. import { ComponentContent, promptAction } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. class Params {
8. public text: string = '';
9. public dialogController: promptAction.CommonController = new promptAction.DialogController();

11. constructor(text: string, dialogController: promptAction.CommonController) {
12. this.text = text;
13. this.dialogController = dialogController;
14. }
15. }

18. @Component
19. struct MyComponent {
20. build() {
21. Column({ space: 5 }) {
22. Button('Close Dialog(Built-in Controller)')
23. .onClick(() => {
24. let dialogController: promptAction.DialogController = this.getDialogController();
25. if (dialogController !== undefined) {
26. dialogController.close();
27. }
28. })
29. }
30. }
31. }

34. @Builder
35. function buildText(params: Params) {
36. Column({ space: 5 }) {
37. Text(params.text)
38. .fontSize(30)
39. if (params.dialogController !== undefined) {
40. Button('Close Dialog(External Controller)')
41. .onClick(() => {
42. params.dialogController.close();
43. })
44. }
45. MyComponent()
46. }
47. .width(300)
48. .height(200)
49. .backgroundColor('#FFF0F0F0')
50. }

53. @CustomDialog
54. @Component
55. struct CustomDialogExample {
56. controller?: CustomDialogController;

58. build() {
59. Column({ space: 5 }) {
60. Text('I am content')
61. .fontSize(30)
62. Button('Close Dialog(Built-in Controller)')
63. .onClick(() => {
64. let dialogController: PromptActionDialogController = this.getDialogController();
65. if (dialogController !== undefined) {
66. dialogController.close();
67. }
68. })
69. }
70. .height(200)
71. .backgroundColor('#FFF0F0F0')
72. }
73. }

76. @Entry
77. @Component
78. export struct DialogController {
79. @State dialogState: promptAction.CommonState = 0;
80. private message = 'dialog';
81. private baseDialogOptions: promptAction.BaseDialogOptions = {
82. isModal: false,
83. autoCancel: false,
84. offset: {
85. dx: 0,
86. dy: 50
87. }
88. };
89. private dialogOptions: promptAction.DialogOptions = {
90. isModal: false,
91. autoCancel: false,
92. offset: {
93. dx: 0,
94. dy: 50
95. }
96. };

98. @Builder
99. customDialogComponent(dialogController: promptAction.DialogController) {
100. Column({ space: 5 }) {
101. Text(this.message)
102. .fontSize(30)
103. if (dialogController !== undefined) {
104. Button('Close Dialog(External Controller)')
105. .onClick(() => {
106. dialogController.close();
107. })
108. }
109. }
110. .height(200)
111. .padding(5)
112. .justifyContent(FlexAlign.SpaceBetween)
113. .backgroundColor('#FFF0F0F0')
114. }

117. @Builder
118. customDialogComponentWithId(dialogId: number, dialogController: promptAction.DialogController) {
119. Column({ space: 5 }) {
120. Text(this.message)
121. .fontSize(30)
122. if (dialogId !== undefined) {
123. Button('Close Dialog(DialogID)')
124. .onClick(() => {
125. this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
126. })
127. }
128. if (dialogController !== undefined) {
129. Button('Close Dialog(External Controller)')
130. .onClick(() => {
131. dialogController.close();
132. })
133. }
134. }
135. .height(200)
136. .padding(5)
137. .justifyContent(FlexAlign.SpaceBetween)
138. .backgroundColor('#FFF0F0F0')
139. }

142. @Builder
143. customDialogComponentGetState(dialogController: promptAction.DialogController) {
144. Column({ space: 5 }) {
145. Text(this.message)
146. .fontSize(30)
147. if (dialogController !== undefined) {
148. Button('Check Status:' + this.dialogState)
149. .onClick(() => {
150. this.dialogState = dialogController.getState();
151. })
152. Button('Close Dialog(External Controller)')
153. .onClick(() => {
154. dialogController.close();
155. })
156. }
157. }
158. .height(200)
159. .padding(5)
160. .justifyContent(FlexAlign.SpaceBetween)
161. .backgroundColor('#FFF0F0F0')
162. }

165. build() {
166. NavDestination() {
167. Column({ space: 5 }) {
168. Button('OpenCustomDialogWithController')
169. .onClick(() => {
170. let dialogController: promptAction.CommonController = new promptAction.DialogController();
171. let contentNode: ComponentContent<Object> =
172. new ComponentContent(this.getUIContext(), wrapBuilder(buildText),
173. new Params(this.message, dialogController));
174. this.getUIContext().getPromptAction().openCustomDialogWithController(
175. contentNode, dialogController, this.baseDialogOptions).catch((err: BusinessError) => {
176. hilog.error(DOMAIN, 'dialogController',
177. 'openCustomDialogWithController error: ' + err.code + ' ' + err.message);
178. });
179. })
180. Button('PresentCustomDialog+CustomBuilder')
181. .onClick(() => {
182. let dialogController: promptAction.CommonController = new promptAction.DialogController();
183. this.getUIContext().getPromptAction().presentCustomDialog(() => {
184. this.customDialogComponent(dialogController);
185. }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
186. hilog.error(DOMAIN, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
187. });
188. })
189. Button('PresentCustomDialog+CustomBuilderWithId')
190. .onClick(() => {
191. let dialogController: promptAction.CommonController = new promptAction.DialogController();
192. this.getUIContext().getPromptAction().presentCustomDialog((dialogId: number) => {
193. this.customDialogComponentWithId(dialogId, dialogController);
194. }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
195. hilog.error(DOMAIN, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
196. });
197. })
198. Button('PresentCustomDialog+CustomBuilderGetState')
199. .onClick(() => {
200. let dialogController: promptAction.CommonController = new promptAction.DialogController();
201. this.getUIContext().getPromptAction().presentCustomDialog(() => {
202. this.customDialogComponentGetState(dialogController);
203. }, dialogController, this.dialogOptions).catch((err: BusinessError) => {
204. hilog.error(DOMAIN, 'dialogController', 'presentCustomDialog error: ' + err.code + ' ' + err.message);
205. });
206. })
207. Button('CustomDialogController')
208. .onClick(() => {
209. let customDialogController: CustomDialogController = new CustomDialogController({
210. builder: CustomDialogExample(),
211. offset: {
212. dx: 0,
213. dy: 50
214. }
215. });
216. customDialogController.open();
217. })
218. }.width('100%')
219. }
220. }
221. }
```

[DialogController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogcontroller/DialogController.ets#L16-L261)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/HCroYMaiSquZzayWHdYyWw/zh-cn_image_0000002552798260.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233943Z&HW-CC-Expire=86400&HW-CC-Sign=3172728BE5626D7AD16CE5EFB79CEF6611959C035E1702D621748DFEE0417968)
