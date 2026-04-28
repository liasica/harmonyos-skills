---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb_rendering_framework
title: ArkWeb渲染框架适配
breadcrumb: 最佳实践 > 应用框架 > ArkWeb > ArkWeb渲染框架适配
category: best-practices
scraped_at: 2026-04-28T08:20:18+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:90fb5dad27f3102c317467baeb2220fc9e44e5eab1076c7a49956439cbfe8146
---

## 概述

Hybrid应用开发是介于Web应用和系统应用两者之间的应用开发技术，兼具“系统应用良好交互体验”的优势和“Web应用跨平台开发”的优势。其主要原理是由Native通过JSBridge通道提供统一的API，然后用Html/CSS实现界面，JS来写业务逻辑，能够调用系统API，最终的页面在WebView中显示。

## Hybrid应用鸿蒙化方案

### 整体架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/GZqSF3eRQvGXTBbcXuqf4Q/zh-cn_image_0000002194010404.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=8196541F5D487646638A4F2A475510D5E9664FF0D3D6A1105FD4587A747B7B17)

1. Ark进程：由ArkTS引擎提供运行时，具备调用系统API的能力。应用启动从Ark进程进入，完成EntryAbility的初始化并创建HarmonyOS应用页面。Ark进程可以动态或者静态创建Webview运行时环境，并加载html/css/js资源文件。
2. Webview进程：默认支持标准W3C API，对ArkTS侧资源的访问有限制。Webview渲染能力主要由Web组件提供。用户可以通过Web组件的属性配置是否开启同层渲染能力、是否允许执行JavaScript脚本等。
3. JSBridge：上述两种进程的通讯机制，允许数据双向流动。Webview进程通过JSBridge通道访问拓展API。

### 方案设计

Hybrid应用鸿蒙化方案主要集中在双端通信JSBridge实现、拓展接口实现和基于同层渲染的原生组件实现。JSBridge是前端与ArkTS进行双向通信的桥梁。通过JSBridge，前端应用能访问到ArkTS侧实现的拓展接口，实现更丰富的业务功能。视图层方面，可以使用系统提供的同层渲染能力，把部分性能要求比较高的前端组件改成ArkTS实现，以达到更好的体验效果。下图蓝色背景的方框图展示了上述三点所处的框架位置：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/nVmfJjiwRVGJD20a4wJY8w/zh-cn_image_0000002229450681.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=4EEB1410B735294FE13ADFF6035062084ADD337A57D56F0F126D21BBB75C2708)

## 业务实现中的关键点

Hybrid应用鸿蒙化方案主要围绕双端通信、API鸿蒙化、组件鸿蒙化三方面进行开发。双端通信：JS侧使用ArkTS的通道，是鸿蒙化的基石；API鸿蒙化：针对JS侧平台相关的API，提供一套HarmonyOS版本的实现；组件鸿蒙化：针对Web组件，以同层渲染的方式提供替代组件，以提升组件的性能与交互体验。

### 双端通信

JSBridge扮演Webview进程与ArkUI主进程沟通的桥梁，是一种双向通信的机制。HarmonyOS系统提供Web组件以及@ohos.web.webview等ArkWeb API来进行Web开发。可以通过WebMessagePort以及javaScriptProxy代理的方式实现JSBridge。

1. WebMessagePort是一种比较基础的消息发送以及接收机制，支持的消息类型为string和ArrayBuffer，具体业务消息内容的封装和解析需要从零设计，存在上手难、工作量大的特点。
2. JavaScriptProxy代理机制注入ArkUI主进程对象（如命名为native）到Webview中，在Webview的window上生成对应代理对象，业务可以直接调用该代理对象的方法，相关的操作将作用到ArkUI主进程的native对象。代码实例如下：

   ```
   1. // Web component loading H5.
   2. Web({ src: this.param.path, controller: this.webController })
   3. .zoomAccess(false)
   4. .width(Const.WEB_CONSTANT_WIDTH)
   5. .aspectRatio(1)
   6. .margin({
   7. left: Const.WEB_CONSTANT_MARGIN_LEFT, right: Const.WEB_CONSTANT_MARGIN_RIGHT,
   8. top: Const.WEB_CONSTANT_MARGIN_TOP
   9. })
   10. .onErrorReceive((event) => {
   11. if (event?.error.getErrorInfo() === 'ERR_INTERNET_DISCONNECTED') {
   12. this.getUIContext().getPromptAction().showToast({
   13. message: $r('app.string.internet_err'),
   14. duration: Const.WEB_CONSTANT_DURATION
   15. });
   16. }
   17. if (event?.error.getErrorInfo() === 'ERR_CONNECTION_TIMED_OUT') {
   18. this.getUIContext().getPromptAction().showToast({
   19. message: $r('app.string.internet_err'),
   20. duration: Const.WEB_CONSTANT_DURATION
   21. });
   22. }
   23. })
   24. .onProgressChange((event) => {
   25. if (event?.newProgress === Const.WEB_CONSTANT_PROGRESS_MAX) {
   26. this.isLoading = false;
   27. clearInterval(this.intervalLoading);
   28. this.intervalLoading = -1;
   29. }
   30. })
   31. .javaScriptProxy({
   32. object: this.linkObj,
   33. name: 'linkObj',
   34. methodList: ['messageFromHtml'],
   35. controller: this.webController
   36. })
   ```

   [WebPage.ets](https://gitcode.com/HarmonyOS_Codelabs/WebComponent/blob/master/entry/src/main/ets/pages/WebPage.ets#L95-L130)

前端可以使用native.makePhoneCall(..) 的方式进行调用。且方法的参数支持基本类型、字典对象、函数等，对于JSBridge的设计提供了便利。关于Web.javaScriptProxy()以及WebviewController.registerJavaScriptProxy()的使用方法可以参考《[前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)》。

通过对比，javaScriptProxy注入对象的方式构造JSBridge是一个比较好的技术选型。建议JSBridge的实现基于注入机制进行设计，并考虑分层设计来提高其通用性和灵活性，下图展示一种分层设计思路：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/nKVmt6sSQdmDgSv9mib4NA/zh-cn_image_0000002229450697.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=51197373103D7C68B4B61C0785FFE2066B13D90FD85096AEC2838B5ABC82DA19)

1. 通信层：对上层屏蔽具体的通信机制，主要负责Web侧和ArkTS侧数据的传递，但不解析数据的业务含义，不关注传递的数据内容。数据可以序列化为字符串进行传递或者以object对象进行传递。使用javaScriptProxy代理机制实现的通信层代码示例如下：

   ```
   1. // Web component loading H5.
   2. Web({ src: this.param.path, controller: this.webController })
   3. .zoomAccess(false)
   4. .width(Const.WEB_CONSTANT_WIDTH)
   5. .aspectRatio(1)
   6. .margin({
   7. left: Const.WEB_CONSTANT_MARGIN_LEFT, right: Const.WEB_CONSTANT_MARGIN_RIGHT,
   8. top: Const.WEB_CONSTANT_MARGIN_TOP
   9. })
   10. .onErrorReceive((event) => {
   11. if (event?.error.getErrorInfo() === 'ERR_INTERNET_DISCONNECTED') {
   12. this.getUIContext().getPromptAction().showToast({
   13. message: $r('app.string.internet_err'),
   14. duration: Const.WEB_CONSTANT_DURATION
   15. });
   16. }
   17. if (event?.error.getErrorInfo() === 'ERR_CONNECTION_TIMED_OUT') {
   18. this.getUIContext().getPromptAction().showToast({
   19. message: $r('app.string.internet_err'),
   20. duration: Const.WEB_CONSTANT_DURATION
   21. });
   22. }
   23. })
   24. .onProgressChange((event) => {
   25. if (event?.newProgress === Const.WEB_CONSTANT_PROGRESS_MAX) {
   26. this.isLoading = false;
   27. clearInterval(this.intervalLoading);
   28. this.intervalLoading = -1;
   29. }
   30. })
   31. .javaScriptProxy({
   32. object: this.linkObj,
   33. name: 'linkObj',
   34. methodList: ['messageFromHtml'],
   35. controller: this.webController
   36. })
   ```

   [WebPage.ets](https://gitcode.com/HarmonyOS_Codelabs/WebComponent/blob/master/entry/src/main/ets/pages/WebPage.ets#L95-L130)
2. 通道层（Channel）：允许注册多种方法层通道。该层的JS侧实现负责把方法层的API信息对象（包含名称、参数、返回值类型等信息）打包成通信层识别的信息数据，交给通信层传递到ArkTS侧。ArkTS侧的实现包含两个主要功能，一个是把信息数据解包出API的信息，并交给ArkTS侧的方法层调用具体的API；另外一个功能就是执行jsCall，ArkTS侧通过WebviewController .runJavaScript()方法在执行JS侧的回调函数。

   在JS侧，nativeCall()方法提供打包转换能力。如下面示例：

   ```
   1. function openDialog() {
   2. linkObj.messageFromHtml(prizesArr[prizesPosition]);
   3. }
   ```

   [index.js](https://gitcode.com/HarmonyOS_Codelabs/WebComponent/blob/master/HttpServerOfWeb/public/js/index.js#L100-L102)

   在ArkTS侧，通过runJavaScript()执行JS侧方法：

   ```
   1. Button($r('app.string.btnValue'))
   2. .fontSize(Const.WEB_CONSTANT_BUTTON_FONT_SIZE)
   3. .fontColor($r('app.color.start_window_background'))
   4. .margin({ top: Const.WEB_CONSTANT_BUTTON_MARGIN_TOP })
   5. .width(Const.WEB_CONSTANT_BUTTON_WIDTH)
   6. .height(Const.WEB_CONSTANT_BUTTON_HEIGHT)
   7. .backgroundColor($r('app.color.blue'))
   8. .borderRadius(Const.WEB_CONSTANT_BUTTON_BORDER_RADIUS)
   9. .onClick(() => {
   10. this.webController.runJavaScript('startDraw()');
   11. })
   ```

   [WebPage.ets](https://gitcode.com/HarmonyOS_Codelabs/WebComponent/blob/master/entry/src/main/ets/pages/WebPage.ets#L152-L162)
3. 方法层（MethodChannel）：可以针对一类API格式封装成一种MethodChannel。同种MethodChannel的API具备一致的参数规范、返回值规范，比如小程序API规范，这样便于把API的调用信息封装成结构化的信息对象，供给通道层进行传递。

JSBridge的设计是否合理关系到应用的性能，开发者也可以考虑是否需要批量缓存请求再统一发送请求来减少请求次数，或者把不变的请求结果进行缓存等等。

### API鸿蒙化

H5业务设计中除了使用W3C API外，还可以使用ArkTS侧API拓展来访问设备。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/3BZpw6Q1SIyiWPy-RXZ3YQ/zh-cn_image_0000002229450693.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=A99016E7A791D600A39E5DD27227DC8A8D8D305A23994411CAE0CB28A53039E2)

系统高阶API是对系统API的一层封装，实现更符合业务要求的接口。拓展API的规范设计具有较大的灵活性，建议对API的参数，返回值类型格式进行限制，使用基本类型或者简单的字典对象，尽量避免使用复杂的类型的参数或返回值，可以参考比较成熟的小程序框架，其规范格式可以分成三种类型：

1. func(paramObj), 其中 paramObj包含基本类型的数据属性以及success/fail/complete()回调函数。
2. on/offFunc(callback), 注册和移除监听函数。
3. getXxManager(): obj, 获取某类功能的全局单例管理器，如文件管理器。管理器的方法也遵守上述两点规范。

设计过程中可以把API都汇聚到一个对象作为属性字段存在，方便在切面视角增加统一的参数、返回值加工处理，拦截处理。示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/QXuSUyqPQCaV62aQ0CK6nA/zh-cn_image_0000002229450701.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=A41AF1FDC2C6CF7EAD4A0E9895103AEEB72544C6ED1F0FED247E0735E818613A)

### 组件鸿蒙化

HarmonyOS提供同层渲染能力把原生组件直接渲染到WebView层级，从而获得更大的灵活性以及性能上获得更好表现。开发者可通过Web组件同层渲染相关属性来进行控制：enableNativeEmbedMode开关控制；onNativeEmbedLifecycleChange处理同层渲染生命周期：CREATE/UPDATE/DESTROY；onNativeEmbedGestureEvent处理交互事件。同层渲染功能要求前端页面文件中显式使用embed标签，并且embed标签内type必须以“native/”开头。使用Vue等框架可以方便地进一步封装embed标签生成自定义组件，并增加更多属性、事件和方法，通过JSBridge与ArkTS侧进行同步。在ArkTS侧，对应地需要自定义实现一个原生组件或者使用系统内置组件，通过NodeContainer组件进行动态挂载。同层渲染的原理如下：

开发角度：前端页面开发者使用<embed>标签来表示使用原生组件；应用开发者使用NodeContainer关联离屏节点树，使用makeNode()接口在H5页面上渲染出组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/sdTZFxyfSQSrDd1dOs2HrA/zh-cn_image_0000002229450685.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=1FD24E824CC659B37EC0B8C45DBE779945B97E0A2A1872666E3D6026ED753A29)

离屏节点动态上下树：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Y8wpslDKSruu9kNiDa-sHg/zh-cn_image_0000002229450689.png?HW-CC-KV=V1&HW-CC-Date=20260428T002016Z&HW-CC-Expire=86400&HW-CC-Sign=F9DA1098424EA10E9A574AE9CBF1DF1CD98FC39F2F9213F90661A3D4817A2D2F)

1）开发者初始构建一个NodeContainer对象表示一个空的占位符。NodeContainer里面内容为空时，在初始化的时候大小为0，不参与布局。

2）NodeController持有buildnode对象，通过makeNode()接口将buildnode对象返回给NodeContainer，来实现动态上树。

3） NodeController里面rebuild()方法，触发NodeContainer重新调用makeNode()接口。 makeNode()接口若返回空，则实现动态下树。

使用H5结合embed标签示例：

```
1. <div>
2. <div id="bodyId">
3. <embed id="nativeSearch" type = "native/component" width="100%" height="100%" src="view"/>
4. </div>
5. </div>
```

[embed\_view.html](https://gitcode.com/harmonyos_samples/arkweb-same-level-rendering/blob/master/entry/src/main/resources/rawfile/embed_view.html#L9-L13)

在ArkTS侧，可以扩展NodeController来统一管理同层渲染节点。其makeNode()接口实现示例如下：

```
1. import { PRODUCT_DATA } from '../viewmodel/GoodsViewModel';
2. import { ProductDataModel } from '../model/GoodsModel';
3. import { BuilderNode, FrameNode, NodeController, NodeRenderType } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';

6. // Margin vertical
7. const MARGIN_VERTICAL: number = 8;
8. // Font weight
9. const FONT_WEIGHT: number = 500;
10. // Placeholder
11. const PLACEHOLDER: ResourceStr = $r('app.string.embed_search');

13. declare class Params {
14. width: number;
15. height: number;
16. }

18. declare class NodeControllerParams {
19. surfaceId: string;
20. type: string;
21. renderType: NodeRenderType;
22. embedId: string;
23. width: number;
24. height: number;
25. }

27. class SearchNodeController extends NodeController {
28. private rootNode: BuilderNode<[Params]> | undefined | null = null;
29. private embedId: string = "";
30. private surfaceId: string = "";
31. private renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
32. private componentWidth: number = 0;
33. private componentHeight: number = 0;
34. private componentType: string = "";

36. /**
37. * 设置渲染参数
38. *
39. * @param params 渲染参数
40. */
41. setRenderOption(params: NodeControllerParams): void {
42. this.surfaceId = params.surfaceId;
43. this.renderType = params.renderType;
44. this.embedId = params.embedId;
45. this.componentWidth = params.width;
46. this.componentHeight = params.height;
47. this.componentType = params.type;
48. }

50. /**
51. * 创建节点
52. *
53. * @param uiContext UIContext
54. * @returns 节点
55. */
56. makeNode(uiContext: UIContext): FrameNode | null {
57. this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId, type: this.renderType });
58. if (this.componentType === 'native/component') {
59. this.rootNode.build(wrapBuilder(searchBuilder), { width: this.componentWidth, height: this.componentHeight });
60. }
61. return this.rootNode.getFrameNode();
62. }

64. setBuilderNode(rootNode: BuilderNode<Params[]> | null): void {
65. this.rootNode = rootNode;
66. }

68. getBuilderNode(): BuilderNode<[Params]> | undefined | null {
69. return this.rootNode;
70. }

72. updateNode(arg: Object): void {
73. this.rootNode?.update(arg);
74. }

76. getEmbedId(): string {
77. return this.embedId;
78. }

80. postEvent(event: TouchEvent | undefined): boolean {
81. return this.rootNode?.postTouchEvent(event) as boolean;
82. }
83. }
84. @Component
85. struct SearchComponent {
86. @Prop params: Params;
87. controller: SearchController = new SearchController()

89. build() {
90. Column({ space: MARGIN_VERTICAL }) {
91. Text($r("app.string.embed_mall"))
92. .fontSize($r('app.string.ohos_id_text_size_body4'))
93. .fontWeight(FONT_WEIGHT)
94. .fontFamily('HarmonyHeiTi-Medium')
95. Row() {
96. Search({ placeholder: PLACEHOLDER, controller: this.controller })
97. .backgroundColor(Color.White)
98. }
99. .width($r("app.string.embed_full_percent"))
100. .margin($r("app.integer.embed_row_margin"))

102. Grid() {
103. ForEach(PRODUCT_DATA, (item: ProductDataModel, index: number) => {
104. GridItem() {
105. Column({ space: MARGIN_VERTICAL }) {
106. Image(item.imageRes).width($r("app.integer.embed_image_size"))
107. Row({ space: MARGIN_VERTICAL }) {
108. Text(item.title)
109. .fontSize($r('app.string.ohos_id_text_size_body1'))
110. .width(100)
111. .maxLines(1)
112. .textOverflow({ overflow: TextOverflow.Ellipsis })
113. Text(item.price)
114. .fontSize($r('app.string.ohos_id_text_size_body1'))
115. .width(50)
116. .maxLines(1)
117. }
118. }
119. .backgroundColor($r('app.color.ohos_id_color_background'))
120. .alignItems(HorizontalAlign.Center)
121. .justifyContent(FlexAlign.Center)
122. .width($r("app.string.embed_full_percent"))
123. .height($r("app.string.embed_full_percent"))
124. .borderRadius($r('app.string.ohos_id_corner_radius_default_m'))
125. }
126. }, (item: ProductDataModel, index: number) => index.toString())
127. }
128. .columnsTemplate('1fr 1fr')
129. .rowsTemplate('1fr 1fr 1fr')
130. .rowsGap($r('app.string.ohos_id_elements_margin_vertical_m'))
131. .columnsGap($r('app.string.ohos_id_elements_margin_vertical_m'))
132. .width($r("app.string.embed_full_percent"))
133. .height($r("app.string.embed_sixty_percent"))
134. .backgroundColor($r('app.color.ohos_id_color_sub_background'))
135. }
136. .padding($r('app.string.ohos_id_card_margin_start'))
137. .width(this.params.width)
138. .height(this.params.height)
139. }
140. }
141. @Builder
142. function searchBuilder(params: Params) {
143. SearchComponent({ params: params })
144. .backgroundColor($r('app.color.ohos_id_color_sub_background'))
145. }

147. @Entry
148. @Component
149. struct Index {
150. browserTabController: WebviewController = new webview.WebviewController();
151. @State componentIdArr: Array<string> = [];
152. private nodeControllerMap: Map<string, SearchNodeController> = new Map();

154. build() {
155. Stack() {
156. ForEach(this.componentIdArr, (componentId: string) => {
157. NodeContainer(this.nodeControllerMap.get(componentId));
158. }, (embedId: string) => embedId)
159. Web({ src: $rawfile("embed_view.html"), controller: this.browserTabController })
160. .backgroundColor($r('app.color.ohos_id_color_sub_background'))
161. .zoomAccess(false)
162. .enableNativeEmbedMode(true)
163. .onNativeEmbedLifecycleChange((embed) => {
164. const componentId = embed.info?.id?.toString() as string
165. if (embed.status === NativeEmbedStatus.CREATE) {
166. let nodeController = new SearchNodeController();
167. nodeController.setRenderOption({
168. surfaceId: embed.surfaceId as string,
169. type: embed.info?.type as string,
170. renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
171. embedId: embed.embedId as string,
172. width: this.getUIContext().px2vp(embed.info?.width),
173. height: this.getUIContext().px2vp(embed.info?.height)
174. });
175. nodeController.rebuild();
176. this.nodeControllerMap.set(componentId, nodeController);
177. this.componentIdArr.push(componentId);
178. } else if (embed.status === NativeEmbedStatus.UPDATE) {
179. let nodeController = this.nodeControllerMap.get(componentId);
180. nodeController?.updateNode({
181. text: 'update',
182. width: this.getUIContext().px2vp(embed.info?.width),
183. height: this.getUIContext().px2vp(embed.info?.height)
184. } as ESObject);
185. nodeController?.rebuild();
186. } else {
187. let nodeController = this.nodeControllerMap.get(componentId);
188. nodeController?.setBuilderNode(null);
189. nodeController?.rebuild();
190. }
191. })
192. .onNativeEmbedGestureEvent((touch) => {
193. this.componentIdArr.forEach((componentId: string) => {
194. let nodeController = this.nodeControllerMap.get(componentId);
195. if (nodeController?.getEmbedId() === touch.embedId) {
196. nodeController?.postEvent(touch.touchEvent);
197. }
198. })
199. })
200. }
201. }
202. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/arkweb-same-level-rendering/blob/master/entry/src/main/ets/pages/Index.ets#L16-L219)

实现中可以使用map容器把embedType和离屏节点的builder()函数进行关联，当makeNode()执行时，取出embedType对应的builder()函数来创建rootNode节点，最后把rootNode节点关联的FrameNode返回，达到离屏节点动态上树、H5渲染出原生组件的效果。同层渲染可以参考文档《[同层渲染绘制Video和Button组件](../harmonyos-guides/web-same-layer.md)》

## 示例代码

* [基于Web组件实现随机抽奖功能](https://gitcode.com/HarmonyOS_Codelabs/WebComponent)
* [基于ArkWeb实现系统原生组件渲染至H5页面上](https://gitcode.com/harmonyos_samples/arkweb-same-level-rendering)
