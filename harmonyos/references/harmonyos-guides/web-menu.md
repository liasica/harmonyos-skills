---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-menu
title: 使用Web组件菜单处理网页内容
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 处理网页内容 > 使用Web组件菜单处理网页内容
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f57db417514ecbd76cf8e546223a8c6a53017a396309fd040b55c5d4a045a8a
---

菜单作为用户交互的关键组件，其作用是构建清晰的导航体系，通过结构化布局展示功能入口，使用户能够迅速找到目标内容或执行操作。作为人机交互的重要枢纽，它显著提升了Web组件的可访问性和用户体验，是应用设计中必不可少的部分。Web组件菜单类型包括[文本选中菜单](web-menu.md#文本选中菜单)、[上下文菜单](web-menu.md#上下文菜单)和[自定义菜单](web-menu.md#自定义菜单)，应用可根据具体需求灵活选择。

| 菜单类型 | 目标元素 | 响应类型 | 是否支持自定义 |
| --- | --- | --- | --- |
| [文本选中菜单](web-menu.md#文本选中菜单) | 文本 | 手势长按 | 可增减菜单项，菜单样式不可自定义 |
| [上下文菜单](web-menu.md#上下文菜单) | 超链接、图片、文字 | 手势长按、鼠标右键 | 支持通过菜单组件自定义 |
| [自定义菜单](web-menu.md#自定义菜单) | 图片 | 手势长按 | 支持通过菜单组件自定义 |

## 文本选中菜单

Web组件的文本选中菜单是一种通过自定义元素实现的上下文交互组件，当用户选中文本时会动态显示，提供复制、分享、标注等语义化操作，具备标准化功能与良好可扩展性，是移动端文本操作的核心功能之一。文本选中菜单在用户长按选中文本或编辑状态下长按出现单手柄时弹出，菜单项横向排列。系统提供默认的菜单实现。应用可通过[editMenuOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#editmenuoptions12)接口对文本选中菜单进行自定义操作。

1. 通过onCreateMenu方法自定义菜单项，通过操作Array<[TextMenuItem](../harmonyos-references/ts-text-common.md#textmenuitem12对象说明)>数组可对显示菜单项进行增减操作，在[TextMenuItem](../harmonyos-references/ts-text-common.md#textmenuitem12对象说明)中定义菜单项名称、图标、ID等内容。
2. 通过onMenuItemClick方法处理菜单项点击事件，当返回false时会执行系统默认逻辑。
3. 创建一个[EditMenuOptions](../harmonyos-references/ts-text-common.md#editmenuoptions)对象，包含onCreateMenu和onMenuItemClick两个方法，通过Web组件的[editMenuOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#editmenuoptions12)接口与Web组件绑定。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
9. let items = menuItems.filter((menuItem) => {
10. // 过滤用户需要的系统菜单项
11. return (
12. menuItem.id.equals(TextMenuItemId.CUT) ||
13. menuItem.id.equals(TextMenuItemId.COPY) ||
14. menuItem.id.equals(TextMenuItemId.PASTE)
15. );
16. });
17. let customItem1: TextMenuItem = {
18. content: 'customItem1',
19. id: TextMenuItemId.of('customItem1'),
20. // 请将$r('app.media.startIcon')替换为实际资源文件
21. icon: $r('app.media.startIcon')
22. };
23. let customItem2: TextMenuItem = {
24. // 请将$r('app.string.EntryAbility_label')替换为实际资源文件，在本示例中该资源文件的value值为"label"
25. content: $r('app.string.EntryAbility_label'),
26. id: TextMenuItemId.of('customItem2'),
27. // 请将$r('app.media.startIcon')替换为实际资源文件
28. icon: $r('app.media.startIcon')
29. };
30. items.push(customItem1); // 在选项列表后添加新选项
31. items.unshift(customItem2); // 在选项列表前添加选项
32. items.push(customItem1);
33. items.push(customItem1);
34. items.push(customItem1);
35. items.push(customItem1);
36. items.push(customItem1);
37. return items;
38. }

40. onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
41. if (menuItem.id.equals(TextMenuItemId.CUT)) {
42. // 用户自定义行为
43. console.info('intercept id：CUT')
44. return true; // 返回true不执行系统回调
45. } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
46. // 用户自定义行为
47. console.info('Do not intercept id：COPY')
48. return false; // 返回false执行系统回调
49. } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
50. // 用户自定义行为
51. console.info('intercept id：customItem1')
52. return true; // 用户自定义菜单选项返回true时点击后不关闭菜单，返回false时关闭菜单
53. } else if (menuItem.id.equals(TextMenuItemId.of('customItem2'))) {
54. // 用户自定义行为
55. console.info('intercept id：customItem2')
56. return true;
57. }
58. return false; // 返回默认值false
59. }

61. @State editMenuOptions: EditMenuOptions = { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick }

63. build() {
64. Column() {
65. Web({ src: $rawfile('index.html'), controller: this.controller })
66. .editMenuOptions(this.editMenuOptions)
67. }
68. }
69. }
```

[WebTextMenuItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebTextMenuItem.ets#L15-L85)

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>editMenuOptions Demo</h1>
9. <span>edit menu options</span>
10. </body>
11. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/SpEJL684To28qwIXE8dsbA/zh-cn_image_0000002558605072.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=224BE8DA549509492F6750E35F86D38BABF4C26BA19C0255C287BC2EA9E948FE)

## 上下文菜单

上下文菜单是用户通过特定操作（如右键点击或长按富文本）触发的快捷菜单，用于提供与当前操作对象或界面元素相关的功能选项。菜单项纵向排列。系统未提供默认实现，若应用未实现，则不显示上下文菜单。应用需要创建一个[Menu](../harmonyos-references/ts-basic-components-menu.md)组件并与Web组件绑定，在菜单弹出时可通过Web组件的[onContextMenuShow](../harmonyos-references/arkts-basic-components-web-events.md#oncontextmenushow9)回调接口获取上下文菜单的详细信息，包括点击位置的HTML元素信息及点击位置信息。

1. [Menu](../harmonyos-references/ts-basic-components-menu.md)组件作为弹出的菜单，包含所有菜单项行为与样式。
2. 使用bindPopup方法将Menu组件与Web组件绑定。当上下文菜单弹出时，将显示创建的Menu组件。
3. 在onContextMenuShow回调中获取上下文菜单事件信息[onContextMenuShowEvent](../harmonyos-references/arkts-basic-components-web-i.md#oncontextmenushowevent12)。其中param为[WebContextMenuParam](../harmonyos-references/arkts-basic-components-web-webcontextmenuparam.md)类型，包含点击位置对应HTML元素信息和位置信息，result为[WebContextMenuResult](../harmonyos-references/arkts-basic-components-web-webcontextmenuresult.md)类型，提供常见的菜单能力。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { pasteboard } from '@kit.BasicServicesKit';

5. const TAG = 'ContextMenu';

7. @Entry
8. @Component
9. struct WebComponent {
10. controller: webview.WebviewController = new webview.WebviewController();
11. private result: WebContextMenuResult | undefined = undefined;
12. @State linkUrl: string = '';
13. @State offsetX: number = 0;
14. @State offsetY: number = 0;
15. @State showMenu: boolean = false;
16. uiContext: UIContext = this.getUIContext();

18. @Builder
19. // 构建自定义菜单及触发功能接口
20. MenuBuilder() {
21. // 以垂直列表形式显示的菜单。
22. Menu() {
23. // 展示菜单Menu中具体的菜单项。
24. MenuItem({
25. content: 'Copy Image',
26. })
27. .width(100)
28. .height(50)
29. .onClick(() => {
30. this.result?.copyImage();
31. this.showMenu = false;
32. })
33. MenuItem({
34. content: 'Cut',
35. })
36. .width(100)
37. .height(50)
38. .onClick(() => {
39. this.result?.cut();
40. this.showMenu = false;
41. })
42. MenuItem({
43. content: 'Copy',
44. })
45. .width(100)
46. .height(50)
47. .onClick(() => {
48. this.result?.copy();
49. this.showMenu = false;
50. })
51. MenuItem({
52. content: 'Paste',
53. })
54. .width(100)
55. .height(50)
56. .onClick(() => {
57. this.result?.paste();
58. this.showMenu = false;
59. })
60. MenuItem({
61. content: 'Copy link',
62. })
63. .width(100)
64. .height(50)
65. .onClick(() => {
66. let pasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkUrl);
67. pasteboard.getSystemPasteboard().setData(pasteData, (error) => {
68. if (error) {
69. return;
70. }
71. })
72. this.showMenu = false;
73. })
74. MenuItem({
75. content: 'Select All',
76. })
77. .width(100)
78. .height(50)
79. .onClick(() => {
80. this.result?.selectAll();
81. this.showMenu = false;
82. })
83. }
84. .width(150)
85. .height(300)
86. }

88. build() {
89. Column() {
90. Web({ src: $rawfile('index1.html'), controller: this.controller })
91. // 触发自定义弹窗
92. .onContextMenuShow((event) => {
93. if (event) {
94. this.result = event.result
95. console.info('x coord = ' + event.param.x());
96. console.info('link url = ' + event.param.getLinkUrl());
97. this.linkUrl = event.param.getLinkUrl();
98. }
99. console.info(TAG, `x: ${this.offsetX}, y: ${this.offsetY}`);
100. this.showMenu = true;
101. this.offsetX = 0;
102. this.offsetY = Math.max(this.uiContext!.px2vp(event?.param.y() ?? 0) - 0, 0);
103. return true;
104. })
105. .bindPopup(this.showMenu,
106. {
107. builder: this.MenuBuilder(),
108. enableArrow: false,
109. placement: Placement.LeftTop,
110. offset: { x: this.offsetX, y: this.offsetY },
111. mask: false,
112. onStateChange: (e) => {
113. if (!e.isVisible) {
114. this.showMenu = false;
115. this.result!.closeContextMenu();
116. }
117. }
118. })
119. }
120. }
121. }
```

[WebContextMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebContextMenu.ets#L15-L137)

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html lang="en">
4. <body>
5. <h1>onContextMenuShow</h1>
6. <a href="http://www.example.com" style="font-size:27px">超链接www.example.com</a>
7. <!--example.png为html同目录下图片-->
8. <div><img src="example.png"></div>
9. <p>选中文字鼠标右键弹出菜单</p>
10. </body>
11. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/h5o6AxfXQ3eG-8niGQL6DQ/zh-cn_image_0000002589324597.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=DF4FC008CFCCB198E89E653FC626A98D9C31ABFE3C59B2E2A20175EB5F11A53A)

## 自定义菜单

自定义菜单赋予开发者灵活控制菜单触发时机与视觉呈现的能力，使应用能够根据用户操作场景动态匹配功能入口，显著简化开发过程中的界面适配工作，同时让交互体验更贴近用户直觉。

开发者可通过[bindSelectionMenu](../harmonyos-references/arkts-basic-components-web-attributes.md#bindselectionmenu13)接口实现自定义菜单功能。目前，已额外支持通过长按图片、链接和文本，触发自定义菜单及自定义文本菜单。

1. 创建[Menu](../harmonyos-references/ts-basic-components-menu.md)组件作为菜单弹窗。
2. 通过Web组件的[bindSelectionMenu](../harmonyos-references/arkts-basic-components-web-attributes.md#bindselectionmenu13)方法绑定MenuBuilder菜单弹窗。将[WebElementType](../harmonyos-references/arkts-basic-components-web-e.md#webelementtype13)设置为WebElementType.IMAGE，[responseType](../harmonyos-references/arkts-basic-components-web-e.md#webresponsetype13)设置为WebResponseType.LONG\_PRESS，表示长按图片时弹出菜单。在[options](../harmonyos-references/arkts-basic-components-web-i.md#selectionmenuoptionsext13)中定义菜单显示回调onAppear、菜单消失回调onDisappear、预览窗口preview和菜单类型menuType。

```
1. import { webview } from '@kit.ArkWeb';

3. interface PreviewBuilderParam {
4. previewImage: Resource | string | undefined;
5. width: number;
6. height: number;
7. }

9. @Builder function previewBuilderGlobal($$: PreviewBuilderParam) {
10. Column() {
11. Image($$.previewImage)
12. .objectFit(ImageFit.Fill)
13. .autoResize(true)
14. }.width($$.width).height($$.height)
15. }

17. @Entry
18. @Component
19. struct WebComponent {
20. controller: webview.WebviewController = new webview.WebviewController();

22. private result: WebContextMenuResult | undefined = undefined;
23. @State previewImage: Resource | string | undefined = undefined;
24. @State previewWidth: number = 0;
25. @State previewHeight: number = 0;
26. uiContext: UIContext = this.getUIContext();

28. @Builder
29. MenuBuilder() {
30. Menu() {
31. MenuItem({ content: 'Copy', })
32. .onClick(() => {
33. this.result?.copy();
34. this.result?.closeContextMenu();
35. })
36. MenuItem({ content: 'Select All', })
37. .onClick(() => {
38. this.result?.selectAll();
39. this.result?.closeContextMenu();
40. })
41. }
42. }
43. build() {
44. Column() {
45. Web({ src: $rawfile('index2.html'), controller: this.controller })
46. .bindSelectionMenu(WebElementType.IMAGE, this.MenuBuilder, WebResponseType.LONG_PRESS,
47. {
48. onAppear: () => {},
49. onDisappear: () => {
50. this.result?.closeContextMenu();
51. },
52. preview: previewBuilderGlobal({
53. previewImage: this.previewImage,
54. width: this.previewWidth,
55. height: this.previewHeight
56. }),
57. menuType: MenuType.PREVIEW_MENU
58. })
59. .onContextMenuShow((event) => {
60. if (event) {
61. this.result = event.result;
62. if (event.param.getLinkUrl()) {
63. return false;
64. }
65. this.previewWidth = this.uiContext!.px2vp(event.param.getPreviewWidth());
66. this.previewHeight = this.uiContext!.px2vp(event.param.getPreviewHeight());
67. if (event.param.getSourceUrl().indexOf('resource://rawfile/') == 0) {
68. this.previewImage = $rawfile(event.param.getSourceUrl().substr(19));
69. } else {
70. this.previewImage = event.param.getSourceUrl();
71. }
72. return true;
73. }
74. return false;
75. })
76. }
77. }
78. }
```

[WebBindSelectionMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebBindSelectionMenu.ets#L15-L94)

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>bindSelectionMenu Demo</h1>
9. <!--img.png为html同目录下图片-->
10. <img src="./img.png" >
11. </body>
12. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/OpbVfQ0VRxOmcxdtUc4qyQ/zh-cn_image_0000002589244535.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=1B1FC2DD43DF2BD6D13DAF4DC3CCFEB0C6D843D3ECD194786CB7E772824D925B)

自API version 20起，支持绑定长按超链接菜单。可以为图片和链接绑定不同的自定义菜单。

以下示例中，PreviewBuilder定义了超链接对应菜单的弹出内容，用Web组件加载了超链接内容（需要注意PreviewBuilder中的Web组件不会接收事件），使用[Progress组件](arkts-common-components-progress-indicator.md)展示了加载进度。

```
1. import { webview } from '@kit.ArkWeb';
2. import { pasteboard } from '@kit.BasicServicesKit';

4. interface PreviewBuilderParam {
5. width: number;
6. height: number;
7. url:Resource | string | undefined;
8. }

10. interface PreviewBuilderParamForImage {
11. previewImage: Resource | string | undefined;
12. width: number;
13. height: number;
14. }

17. @Builder function previewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
18. Column() {
19. Image($$.previewImage)
20. .objectFit(ImageFit.Fill)
21. .autoResize(true)
22. }.width($$.width).height($$.height)
23. }

25. @Entry
26. @Component
27. struct SelectionMenuLongPress {
28. controller: webview.WebviewController = new webview.WebviewController();
29. previewController: webview.WebviewController = new webview.WebviewController();
30. @Builder PreviewBuilder($$: PreviewBuilderParam){
31. Column() {
32. Stack(){
33. Text('') // 可选择是否展示url
34. .padding(5)
35. .width('100%')
36. .textAlign(TextAlign.Start)
37. .backgroundColor(Color.White)
38. .copyOption(CopyOptions.LocalDevice)
39. .maxLines(1)
40. .textOverflow({overflow:TextOverflow.Ellipsis})
41. Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // 展示进度条
42. .style({ strokeWidth: 3, enableSmoothEffect: true })
43. .backgroundColor(Color.White)
44. .opacity(this.progressVisible?1:0)
45. .backgroundColor(Color.White)
46. }.alignContent(Alignment.Bottom)
47. Web({src:$$.url,controller: new webview.WebviewController()})
48. .javaScriptAccess(true)
49. .fileAccess(true)
50. .onlineImageAccess(true)
51. .imageAccess(true)
52. .domStorageAccess(true)
53. .onPageBegin(()=>{
54. this.progressValue = 0;
55. this.progressVisible = true;
56. })
57. .onProgressChange((event)=>{
58. this.progressValue = event.newProgress;
59. })
60. .onPageEnd(()=>{
61. this.progressVisible = false;
62. })
63. .hitTestBehavior(HitTestMode.None) // 使预览Web不响应手势
64. }.width($$.width).height($$.height) // 设置预览宽高
65. }

67. private result: WebContextMenuResult | undefined = undefined;
68. @State previewImage: Resource | string | undefined = undefined;
69. @State previewWidth: number = 1;
70. @State previewHeight: number = 1;
71. @State previewWidthImage: number = 1;
72. @State previewHeightImage: number = 1;
73. @State linkURL:string = '';
74. @State progressValue:number = 0;
75. @State progressVisible:boolean = true;
76. uiContext: UIContext = this.getUIContext();

78. @Builder
79. LinkMenuBuilder() {
80. Menu() {
81. MenuItem({ content: 'Copy link', })
82. .onClick(() => {
83. const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkURL);
84. const systemPasteboard = pasteboard.getSystemPasteboard();
85. systemPasteboard.setData(pasteboardData);
86. })
87. MenuItem({content:'Open the link'})
88. .onClick(()=>{
89. this.controller.loadUrl(this.linkURL);
90. })
91. }
92. }
93. @Builder
94. ImageMenuBuilder() {
95. Menu() {
96. MenuItem({ content: 'Copy Image', })
97. .onClick(() => {
98. this.result?.copyImage();
99. this.result?.closeContextMenu();
100. })
101. }
102. }
103. build() {
104. Column() {
105. Web({ src: $rawfile('index3.html'), controller: this.controller })
106. .javaScriptAccess(true)
107. .fileAccess(true)
108. .onlineImageAccess(true)
109. .imageAccess(true)
110. .domStorageAccess(true)
111. .bindSelectionMenu(WebElementType.LINK, this.LinkMenuBuilder, WebResponseType.LONG_PRESS,
112. {
113. onAppear: () => {},
114. onDisappear: () => {
115. this.result?.closeContextMenu();
116. },
117. preview: this.PreviewBuilder({
118. width: 500,
119. height: 400,
120. url:this.linkURL
121. }),
122. menuType: MenuType.PREVIEW_MENU,
123. })
124. .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG_PRESS,
125. {
126. onAppear: () => {},
127. onDisappear: () => {
128. this.result?.closeContextMenu();
129. },
130. preview: previewBuilderGlobalForImage({
131. previewImage: this.previewImage,
132. width: this.previewWidthImage,
133. height: this.previewHeightImage,
134. }),
135. menuType: MenuType.PREVIEW_MENU,
136. })
137. .zoomAccess(true)
138. .onContextMenuShow((event) => {
139. if (event) {
140. this.result = event.result;
141. this.previewWidthImage = this.uiContext!.px2vp(event.param.getPreviewWidth());
142. this.previewHeightImage = this.uiContext!.px2vp(event.param.getPreviewHeight());
143. if (event.param.getSourceUrl().indexOf('resource://rawfile/') == 0) {
144. this.previewImage = $rawfile(event.param.getSourceUrl().substring(19));
145. } else {
146. this.previewImage = event.param.getSourceUrl();
147. }
148. this.linkURL = event.param.getLinkUrl()
149. return true;
150. }
151. return false;
152. })
153. }

155. }
156. // 侧滑返回
157. onBackPress(): boolean | void {
158. try {
159. if (this.controller.accessStep(-1)) {
160. this.controller.backward();
161. return true;
162. }
163. } catch (err) {
164. console.error(`onBackPress failed with error: ${err.code}, ${err.message}`);
165. }
166. return false;
167. }
168. }
```

[WebPreviewBuilder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebPreviewBuilder.ets#L15-L181)

html示例

```
1. <html lang="zh-CN"><head>
2. <meta charset="UTF-8">
3. <meta name="viewport" content="width=device-width, initial-scale=1.0">
4. <title>综合信息页面</title>
5. </head>
6. <body>
7. <div>
8. <h1>综合信息与联系详情</h1>
9. <section>
10. <a href="https://www.example.com">EXAMPLE</a>
11. <br>
12. <a href="https://www.example1.com/">EXAMPLE1</a>
13. </section>
14. </div>
15. <footer>
16. <p>请注意，以上提供的所有网址仅供演示之用。</p>
17. </footer>
18. </body>
19. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/fMaTnotCTV2PJ08RCkptPA/zh-cn_image_0000002558764730.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=15174075BDE63C9F8A1A0BC761E2710975A3E40B6A21758CF69A97C4CE70D794)

## Web菜单保存图片

1. 创建MenuBuilder组件作为菜单弹窗，使用[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)组件实现图片保存，通过bindContextMenu将MenuBuilder与Web绑定。
2. 在onContextMenuShow中获取图片url，通过copyLocalPicToDir或copyUrlPicToDir将图片保存至应用沙箱。
3. 通过photoAccessHelper将应用沙箱中的图片保存至图库。

```
1. import { webview } from '@kit.ArkWeb';
2. import { common } from '@kit.AbilityKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { systemDateTime } from '@kit.BasicServicesKit';
5. import { http } from '@kit.NetworkKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. @Entry
9. @Component
10. struct WebComponent {
11. saveButtonOptions: SaveButtonOptions = {
12. icon: SaveIconStyle.FULL_FILLED,
13. text: SaveDescription.SAVE_IMAGE,
14. buttonType: ButtonType.Capsule
15. }
16. controller: webview.WebviewController = new webview.WebviewController();
17. @State showMenu: boolean = false;
18. @State imgUrl: string = '';
19. context = this.getUIContext().getHostContext() as common.UIAbilityContext;

21. copyLocalPicToDir(rawfilePath: string, newFileName: string): string {
22. try {
23. let srcFileDes = this.context.resourceManager.getRawFdSync(rawfilePath);
24. let dstPath = this.context.filesDir + '/' + newFileName;
25. let dest: fileIo.File = fileIo.openSync(dstPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
26. let bufsize = 4096;
27. let buf = new ArrayBuffer(bufsize);
28. let off = 0;
29. let len = 0;
30. let readedLen = 0;
31. while ((len = fileIo.readSync(srcFileDes.fd, buf, { offset: srcFileDes.offset + off, length: bufsize })) != 0) {
32. readedLen += len;
33. fileIo.writeSync(dest.fd, buf, { offset: off, length: len });
34. off = off + len;
35. if ((srcFileDes.length - readedLen) < bufsize) {
36. bufsize = srcFileDes.length - readedLen;
37. }
38. }
39. fileIo.close(dest.fd);
40. return dest.path;
41. } catch (err) {
42. console.error(`copyLocalPicToDir failed with error: ${err.code}, ${err.message}`);
43. return '';
44. }
45. }

47. async copyUrlPicToDir(picUrl: string, newFileName: string): Promise<string> {
48. let uri = '';
49. let httpRequest = http.createHttp();
50. try {
51. let data: http.HttpResponse = await (httpRequest.request(picUrl) as Promise<http.HttpResponse>);
52. if (data?.responseCode == http.ResponseCode.OK) {
53. let dstPath = this.context.filesDir + '/' + newFileName;
54. let dest: fileIo.File = fileIo.openSync(dstPath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
55. let writeLen: number = fileIo.writeSync(dest.fd, data.result as ArrayBuffer);
56. uri = dest.path;
57. }
58. } catch (err) {
59. console.error(`copyUrlPicToDir failed with error: ${err.code}, ${err.message}`);
60. } finally {
61. httpRequest.destroy();
62. }
63. return uri;
64. }

66. @Builder
67. MenuBuilder() {
68. Column() {
69. Row() {
70. SaveButton(this.saveButtonOptions)
71. .onClick(async (event, result: SaveButtonOnClickResult) => {
72. if (result == SaveButtonOnClickResult.SUCCESS) {
73. try {
74. let context = this.context;
75. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
76. let uri = '';
77. if (this.imgUrl?.includes('rawfile')) {
78. let rawFileName: string = this.imgUrl.substring(this.imgUrl.lastIndexOf('/') + 1);
79. uri = this.copyLocalPicToDir(rawFileName, 'copyFile.png');
80. } else if (this.imgUrl?.includes('http') || this.imgUrl?.includes('https')) {
81. uri = await this.copyUrlPicToDir(this.imgUrl, `onlinePic${systemDateTime.getTime()}.png`);
82. }
83. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
84. photoAccessHelper.MediaAssetChangeRequest.createImageAssetRequest(context,  uri);
85. await phAccessHelper.applyChanges(assetChangeRequest);
86. } catch (err) {
87. console.error(`create asset failed with error: ${err.code}, ${err.message}`);
88. }
89. } else {
90. console.error(`SaveButtonOnClickResult create asset failed`);
91. }
92. this.showMenu = false;
93. })
94. }
95. .margin({ top: 20, bottom: 20 })
96. .justifyContent(FlexAlign.Center)
97. }
98. .width('80')
99. .backgroundColor(Color.White)
100. .borderRadius(10)
101. }

103. build() {
104. Column() {
105. Web({src: $rawfile('index4.html'), controller: this.controller})
106. .onContextMenuShow((event) => {
107. if (event) {
108. let hitValue = this.controller.getLastHitTest();
109. this.imgUrl = hitValue.extra;
110. }
111. this.showMenu = true;
112. return true;
113. })
114. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
115. .fileAccess(true)
116. .javaScriptAccess(true)
117. .domStorageAccess(true)
118. }
119. }
120. }
```

[WebSaveImage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebSaveImage.ets#L15-L125)

```
1. <!--index4.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>SavePicture</title>
6. </head>
7. <body>
8. <h1>SavePicture</h1>
9. <br>
10. <br>
11. <br>
12. <br>
13. <br>
14. <!--startIcon.png为html同目录下图片-->
15. <img src="./startIcon.png">
16. </body>
17. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/vr9MrGAMQ7u0JTu-sviBRQ/zh-cn_image_0000002558605074.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=1DFEEA2DC0FFDED67ACB0BE04521FF25F0575029F0D429202F9D13DCEA72A2A1)

## Web菜单获取选中文本

Web组件的[editMenuOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#editmenuoptions12)接口中没有提供获取选中文本的方式。开发者可通过[javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)获取到JavaScript的选中文本，实现自定义菜单的逻辑。

1. 创建SelectClass类，通过[javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)将SelectClass对象注册到Web组件中。
2. 在HTML侧注册选区变更监听器，在选区变更时通过SelectClass对象将选区设置到ArkTS侧。

```
1. import { webview } from '@kit.ArkWeb';
2. let selectText = '';

4. class SelectClass {
5. constructor() {
6. }

8. setSelectText(param: string) {
9. selectText = param.toString();
10. }
11. }

13. @Entry
14. @Component
15. struct WebComponent {
16. webController: webview.WebviewController = new webview.WebviewController();
17. @State selectObj: SelectClass = new SelectClass();
18. @State textStr: string = '';

20. build() {
21. Column() {
22. Web({ src: $rawfile('index5.html'), controller: this.webController})
23. .javaScriptProxy({
24. object: this.selectObj,
25. name: 'selectObjName',
26. methodList: ['setSelectText'],
27. controller: this.webController
28. })
29. .height('40%')
30. Text('Click here to get the selected text.')
31. .fontSize(20)
32. .onClick(() => {
33. this.textStr = selectText;
34. })
35. .height('10%')
36. Text('Selected text is ' + this.textStr)
37. .fontSize(20)
38. .height('10%')
39. }
40. }
41. }
```

[WebEditMenuOptions.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebEditMenuOptions.ets#L15-L57)

```
1. <!DOCTYPE html>
2. <html>
3. <head>
4. <title>Test Get Select</title>
5. <style>
6. body {
7. margin: 40px;
8. background-color: #f4f4f4;
9. }
10. .edit-container {
11. padding: 20px;
12. background-color: #fff;
13. border-radius: 8px;
14. box-shadow: 0 0 10px rgba(0,0,0,0.1);
15. margin: auto;
16. }
17. textarea {
18. width: 100%;
19. height: 400px;
20. font-size: 16px;
21. padding: 10px;
22. border: 1px solid #ccc;
23. border-radius: 4px;
24. }
25. </style>
26. </head>
27. <body>
28. <div class="edit-container">
29. <textarea placeholder="Enter the text here and select it by long pressing."></textarea>
30. </div>
31. <script>
32. document.addEventListener('selectionchange', () => {
33. var selection = window.getSelection();
34. if(selection.rangeCount > 0) {
35. var selectedText = selection.toString();
36. selectObjName.setSelectText(selectedText);
37. }
38. })
39. </script>
40. </body>
41. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/Uj-V0eerRBex3IW4exxSxw/zh-cn_image_0000002589324599.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=282050B7FC73ED211F937305D33E8CDF8575877E410F22EC22DA05628616E4FC)

## 常见问题

### 如何禁用长按选择时弹出菜单

可通过[editMenuOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#editmenuoptions12)接口将系统默认菜单全部过滤，此时无菜单项，则不会显示菜单。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
9. let items = menuItems.filter((menuItem) => {
10. // 过滤用户需要的系统菜单项
11. return false;
12. });
13. return items;
14. }

16. onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
17. return false; // 返回默认值false
18. }

20. @State editMenuOptions: EditMenuOptions = { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick }

22. build() {
23. Column() {
24. Web({ src: $rawfile('index7.html'), controller: this.controller })
25. .editMenuOptions(this.editMenuOptions)
26. }
27. }
28. }
```

[WebDisableLongPress.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebDisableLongPress.ets#L15-L44)

```
1. <!--index.html-->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <title>测试网页</title>
6. </head>
7. <body>
8. <h1>editMenuOptions Demo</h1>
9. <span>edit menu options</span>
10. </body>
11. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/wXrtQZeISDyaI03Zx8EmNA/zh-cn_image_0000002589244537.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=3A6D088B9EC100DDCCBA26D2606CC509CCB4F25721751AA7A438BDD42EC5AA3C)

### 出现选区时手柄菜单不显示

可排查是否通过JavaScript的[selection-api](https://www.w3.org/TR/selection-api/)对选区进行了操作，目前通过这种方式改变选区会导致文本选中菜单不显示。

### 如何修改文本选中菜单的样式

从API version 21开始，应用可通过[bindSelectionMenu](../harmonyos-references/arkts-basic-components-web-attributes.md#bindselectionmenu13)接口，实现自定义文本选中菜单。

**示例代码**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. clearSelection() {
10. try {
11. this.controller.runJavaScript(
12. 'clearSelection()',
13. (error, result) => {
14. if (error) {
15. console.error(`run clearSelection JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
16. return;
17. }
18. if (result) {
19. console.info(`The clearSelection() return value is: ${result}`);
20. }
21. });
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
24. }
25. }

27. @Builder
28. TextMenuBuilder() {
29. Menu() {
30. MenuItem({ content: 'Copy', })
31. .onClick(() => {
32. try {
33. this.controller.runJavaScript(
34. 'copySelectedText()',
35. (error, result) => {
36. if (error) {
37. console.error(`run copySelectedText JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
38. return;
39. }
40. if (result) {
41. console.info(`The copySelectedText() return value is: ${result}`);
42. }
43. });
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
46. }
47. this.clearSelection()
48. }).backgroundColor(Color.Pink)
49. }
50. }
51. build() {
52. Column() {
53. Web({ src: $rawfile('bindSelectionMenuText.html'), controller: this.controller })
54. .javaScriptAccess(true)
55. .fileAccess(true)
56. .onlineImageAccess(true)
57. .imageAccess(true)
58. .domStorageAccess(true)
59. .zoomAccess(true)
60. .bindSelectionMenu(WebElementType.TEXT, this.TextMenuBuilder, WebResponseType.LONG_PRESS,
61. {
62. onAppear: () => {},
63. onDisappear: () => {},
64. menuType: MenuType.SELECTION_MENU,
65. })
66. }
67. }
68. onBackPress(): boolean | void {
69. if (this.controller.accessStep(-1)) {
70. this.controller.backward();
71. return true;
72. } else {
73. return false;
74. }
75. }
76. }
```

[WebBindSelectionMenuText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ArkWebMenu/entry/src/main/ets/pages/WebBindSelectionMenuText.ets#L15-L92)

```
1. <!--bindSelectionMenuText.html-->
2. <!DOCTYPE html>
3. <html lang="zh-CN">
4. <head>
5. <meta charset="UTF-8">
6. <meta name="viewport" content="width=device-width, initial-scale=1.0">
7. <title>自定义文本菜单</title>
8. <style>
9. .container {
10. background-color: white;
11. padding: 30px;
12. margin: 20px 0;
13. }

15. .context {
16. line-height: 1.8;
17. font-size: 18px;
18. }

20. .context span {
21. border-radius: 8px;
22. background-color: #f8f9fa;
23. }
24. </style>
25. </head>
26. <body>
27. <div class="container">
28. <div class="context">
29. <span>在这个数字时代，文本复制功能变得日益重要。无论是引用名言、保存重要信息，还是分享有趣的内容，复制文本都是我们日常操作的  一部分。</span>
30. </div>
31. </div>

33. <script>
34. function copySelectedText() {
35. const selectedText = window.getSelection().toString();
36. if (selectedText.length > 0) {
37. // 使用Clipboard API复制文本
38. navigator.clipboard.writeText(selectedText)
39. .then(() => {
40. showNotification();
41. })
42. .catch(err => {
43. console.error('copy failed:', err);
44. });
45. }
46. }
47. function clearSelection() {
48. if (window.getSelection) {
49. window.getSelection().removeAllRanges();
50. }
51. }
52. </script>
53. </body>
54. </html>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/28tLWEGfRO2MRbNZBHuH8g/zh-cn_image_0000002558764732.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052929Z&HW-CC-Expire=86400&HW-CC-Sign=AEFB51D5AFA5714A0A3736AA8F0C4D3A2E65D87E2109E3A6328D378FDE51D7DB)
