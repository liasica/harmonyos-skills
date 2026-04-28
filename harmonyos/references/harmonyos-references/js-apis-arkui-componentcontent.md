---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent
title: ComponentContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > ComponentContent
category: harmonyos-references
scraped_at: 2026-04-28T08:00:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8e83fbf06d7b30cb650a0d7b9a32e6b8933c1c0c5580b1320130618b04a9948c
---

有两种创建实体封装组件的方式。开发者在开发过程中任选下面方式其一即可。

ComponentContent表示组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。其底层使用了BuilderNode，具体使用规格参考[BuilderNode](js-apis-arkui-buildernode.md)。

ReactiveComponentContent表示组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。其底层使用了ReactiveBuilderNode，具体使用规格参考[ReactiveBuilderNode](js-apis-arkui-buildernode.md#reactivebuildernode22)。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当前不支持在预览器中使用ComponentContent和ReactiveComponentContent。
* ComponentContent对象不支持使用JSON序列化。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ComponentContent, ReactiveComponentContent } from '@kit.ArkUI';
```

## ComponentContent

PhonePC/2in1TabletTVWearable

继承自[Content](js-apis-arkui-content.md#content-1)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, builder: WrappedBuilder<[]>)

ComponentContent的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需要的UI上下文。 |
| builder | [WrappedBuilder<[]>](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder) | 是 | 封装不带参builder函数的WrappedBuilder对象。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, builder: WrappedBuilder<[T]>, args: T)

ComponentContent的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需要的UI上下文。 |
| builder | [WrappedBuilder<[T]>](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder) | 是 | 封装带参builder函数的WrappedBuilder对象。 |
| args | T | 是 | WrappedBuilder对象封装的builder函数的参数。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, builder: WrappedBuilder<[T]>, args: T, options: BuildOptions)

ComponentContent的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需要的UI上下文。 |
| builder | [WrappedBuilder<[T]>](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder) | 是 | 封装带参builder函数的WrappedBuilder对象。 |
| args | T | 是 | WrappedBuilder对象封装的builder函数的参数。 |
| options | [BuildOptions](js-apis-arkui-buildernode.md#buildoptions12) | 是 | build的配置参数，判断是否支持@Builder中嵌套@Builder的行为。 |

**示例：**

```
1. import { ComponentContent, NodeContent, typeNode } from "@kit.ArkUI";

3. interface ParamsInterface {
4. text: string;
5. func: Function;
6. }

8. @Builder
9. function buildTextWithFunc(fun: Function) {
10. Text(fun())
11. .fontSize(20)
12. .fontWeight(FontWeight.Bold)
13. .margin({ bottom: 36 })
14. }

16. @Builder
17. function buildText(params: ParamsInterface) {
18. Column() {
19. Text(params.text)
20. .fontSize(20)
21. .fontWeight(FontWeight.Bold)
22. .margin({ bottom: 12 })
23. buildTextWithFunc(params.func)
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State message: string = "HELLO";
31. private content: NodeContent = new NodeContent();

33. build() {
34. Row() {
35. Column({ space: 12 }) {
36. Button('addComponentContent')
37. .onClick(() => {
38. let column = typeNode.createNode(this.getUIContext(), "Column");
39. column.initialize();
40. column.addComponentContent(new ComponentContent<ParamsInterface>(this.getUIContext(),
41. wrapBuilder<[ParamsInterface]>(buildText), {
42. text: this.message, func: () => {
43. return "FUNCTION"
44. }
45. }, { nestingBuilderSupported: true }));
46. this.content.addFrameNode(column);
47. })
48. ContentSlot(this.content)
49. }
50. .id("column")
51. .width('100%')
52. .height('100%')
53. }
54. .height('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/EMkMMRZ2QSy3VtmYWOqz4g/zh-cn_image_0000002552959440.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=726079C66AE4B1D894ACC46C182B0E237F26ADC4A56FC2F988D2357A00D97EE7)

### update

PhonePC/2in1TabletTVWearable

update(args: T): void

用于更新[WrappedBuilder](../harmonyos-guides/arkts-wrapbuilder.md)对象封装的builder函数参数，与constructor传入的参数类型保持一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| args | T | 是 | 用于更新[WrappedBuilder](../harmonyos-guides/arkts-wrapbuilder.md)对象封装的builder函数参数，与constructor传入的参数类型保持一致。 |

**示例：**

```
1. import { ComponentContent } from "@kit.ArkUI";

3. class Params {
4. text: string = "";

6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }.backgroundColor('#FFF0F0F0')
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State message: string = "hello";

26. build() {
27. Row() {
28. Column() {
29. Button("click me")
30. .margin({ top: 200 })
31. .onClick(() => {
32. let uiContext = this.getUIContext();
33. let promptAction = uiContext.getPromptAction();
34. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
35. promptAction.openCustomDialog(contentNode);

37. setTimeout(() => {
38. contentNode.update(new Params("new message"));
39. }, 2000); // 2秒后自动更新弹窗内容文本
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. .height('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/weAIBNJjRVK2LojnEYQ0cA/zh-cn_image_0000002583479441.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=E2EF2CA138D56E05EC23D422B50483B60D498CD7A331C53E36AA3E3DE18E437B)

### reuse

PhonePC/2in1TabletTVWearable

reuse(param?: Object): void

触发ComponentContent中的自定义组件的复用。组件复用请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。关于ComponentContent的解绑场景请参见[解除实体节点引用关系](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Object | 否 | 用于复用ComponentContent的参数。该参数将直接用于ComponentContent中所有顶层自定义组件的复用，应该包含每个自定义组件的构造函数参数所需内容，否则会导致未定义行为。调用此方法将同步触发内部自定义组件的[aboutToReuse](ts-custom-component-lifecycle.md#abouttoreuse10)生命周期回调，并将该参数作为回调的入参。默认值为undefined，此时ComponentContent中的自定义组件将直接使用构造时的数据源。 |

### recycle

PhonePC/2in1TabletTVWearable

recycle(): void

* 触发ComponentContent中自定义组件的回收。自定义组件的回收是组件复用机制中的环节，具体信息请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。
* ComponentContent通过reuse和recycle完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

```
1. import { NodeContent, typeNode, ComponentContent } from "@kit.ArkUI";

3. const TEST_TAG: string = "Reuse+Recycle";

5. class MyDataSource {
6. private dataArray: string[] = [];
7. private listener: DataChangeListener | null = null;

9. public totalCount(): number {
10. return this.dataArray.length;
11. }

13. public getData(index: number) {
14. return this.dataArray[index];
15. }

17. public pushData(data: string) {
18. this.dataArray.push(data);
19. }

21. public reloadListener(): void {
22. this.listener?.onDataReloaded();
23. }

25. public registerDataChangeListener(listener: DataChangeListener): void {
26. this.listener = listener;
27. }

29. public unregisterDataChangeListener(): void {
30. this.listener = null;
31. }
32. }

34. class Params {
35. item: string = '';

37. constructor(item: string) {
38. this.item = item;
39. }
40. }

42. @Builder
43. function buildNode(param: Params = new Params("hello")) {
44. Row() {
45. Text(`C${param.item} -- `)
46. ReusableChildComponent2({ item: param.item }) // 该自定义组件在ComponentContent中无法被正确复用
47. }
48. }

50. // 被回收复用的自定义组件，其状态变量会更新，而子自定义组件ReusableChildComponent3中的状态变量也会更新，但ComponentContent会阻断这一传递过程
51. @Reusable
52. @Component
53. struct ReusableChildComponent {
54. @Prop item: string = '';
55. @Prop switch: string = '';
56. private content: NodeContent = new NodeContent();
57. private componentContent: ComponentContent<Params> = new ComponentContent<Params>(
58. this.getUIContext(),
59. wrapBuilder<[Params]>(buildNode),
60. new Params(this.item),
61. { nestingBuilderSupported: true });

63. aboutToAppear() {
64. let column = typeNode.createNode(this.getUIContext(), "Column");
65. column.initialize();
66. column.addComponentContent(this.componentContent);
67. this.content.addFrameNode(column);
68. }

70. aboutToRecycle(): void {
71. console.info(`${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);

73. // 当开关为open，通过ComponentContent的reuse接口和recycle接口传递给其下的自定义组件，例如ReusableChildComponent2，完成复用
74. if (this.switch === 'open') {
75. this.componentContent.recycle();
76. }
77. }

79. aboutToReuse(params: object): void {
80. console.info(`${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);

82. // 当开关为open，通过ComponentContent的reuse接口和recycle接口传递给其下的自定义组件，例如ReusableChildComponent2，完成复用
83. if (this.switch === 'open') {
84. this.componentContent.reuse(params);
85. }
86. }

88. build() {
89. Row() {
90. Text(`A${this.item}--`)
91. ReusableChildComponent3({ item: this.item })
92. ContentSlot(this.content)
93. }
94. }
95. }

97. @Component
98. struct ReusableChildComponent2 {
99. @Prop item: string = "false";

101. aboutToReuse(params: Record<string, object>) {
102. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
103. }

105. aboutToRecycle(): void {
106. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}`);
107. }

109. build() {
110. Row() {
111. Text(`D${this.item}`)
112. .fontSize(20)
113. .backgroundColor(Color.Yellow)
114. .margin({ left: 10 })
115. }.margin({ left: 10, right: 10 })
116. }
117. }

119. @Component
120. struct ReusableChildComponent3 {
121. @Prop item: string = "false";

123. aboutToReuse(params: Record<string, object>) {
124. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}`);
125. }

127. aboutToRecycle(): void {
128. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}`);
129. }

131. build() {
132. Row() {
133. Text(`B${this.item}`)
134. .fontSize(20)
135. .backgroundColor(Color.Yellow)
136. .margin({ left: 10 })
137. }.margin({ left: 10, right: 10 })
138. }
139. }

142. @Entry
143. @Component
144. struct Index {
145. @State data: MyDataSource = new MyDataSource();

147. aboutToAppear() {
148. for (let i = 0; i < 100; i++) {
149. this.data.pushData(i.toString());
150. }
151. }

153. build() {
154. Column() {
155. List({ space: 3 }) {
156. LazyForEach(this.data, (item: string) => {
157. ListItem() {
158. ReusableChildComponent({
159. item: item,
160. switch: 'open' // 将open改为close可观察到，ComponentContent不通过reuse和recycle接口传递复用时，ComponentContent内部的自定义组件的行为表现
161. })
162. }
163. }, (item: string) => item)
164. }
165. .width('100%')
166. .height('100%')
167. }
168. }
169. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/dxe4GER8Q7GeCLK4ctzExQ/zh-cn_image_0000002552799792.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=F94103654908FCD0A3C2B26B8086ECD0B12A59B8DF38E94C295A3E233D208FC4)

### dispose

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前ComponentContent对象对[基本概念：实体节点](../harmonyos-guides/arkts-user-defined-node.md#基本概念)的引用关系。关于ComponentContent的解绑场景请参见[解除实体节点引用关系](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

说明

当ComponentContent对象调用dispose之后，会与后端实体节点解除引用关系。若前端对象ComponentContent无法释放，容易导致内存泄漏。建议在不再需要操作该ComponentContent对象时，开发者主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏的风险。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. }.backgroundColor('#FFF0F0F0')
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = "hello";

27. build() {
28. Row() {
29. Column() {
30. Button("click me")
31. .onClick(() => {
32. let uiContext = this.getUIContext();
33. let promptAction = uiContext.getPromptAction();
34. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
35. promptAction.openCustomDialog(contentNode);

37. setTimeout(() => {
38. promptAction.closeCustomDialog(contentNode)
39. .then(() => {
40. console.info('customDialog closed.');
41. if (contentNode !== null) {
42. contentNode.dispose(); // 释放contentNode
43. }
44. }).catch((error: BusinessError) => {
45. let message = (error as BusinessError).message;
46. let code = (error as BusinessError).code;
47. console.error(`closeCustomDialog args error code is ${code}, message is ${message}`);
48. })
49. }, 2000); // 2秒后自动关闭
50. })
51. }
52. .width('100%')
53. .height('100%')
54. }
55. .height('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/lIAV0jCwTzWD8NXZekfPDQ/zh-cn_image_0000002583439487.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=33B0044A8547DA4844D4C575C1EF3C6BF0AABD7B780A2D41AA085E2E979784DC)

### updateConfiguration

PhonePC/2in1TabletTVWearable

updateConfiguration(): void

传递[系统环境变化](js-apis-app-ability-configuration.md)事件，触发节点的全量更新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

updateConfiguration接口用于通知对象更新当前的系统环境变化。

**示例：**

```
1. import { NodeController, FrameNode, ComponentContent, UIContext, FrameCallback } from '@kit.ArkUI';
2. import { AbilityConstant, Configuration, EnvironmentCallback, ConfigurationConstant } from '@kit.AbilityKit';

4. @Builder
5. function buildText() {
6. Column() {
7. Text('Hello')
8. .fontSize(36)
9. .fontWeight(FontWeight.Bold)
10. }
11. .backgroundColor($r('sys.color.ohos_id_color_background'))
12. .width('100%')
13. .alignItems(HorizontalAlign.Center)
14. .padding(16)
15. }

17. const componentContentMap: Array<ComponentContent<[Object]>> = new Array();

19. class MyNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;

22. makeNode(uiContext: UIContext): FrameNode | null {
23. return this.rootNode;
24. }

26. createNode(context: UIContext) {
27. this.rootNode = new FrameNode(context);
28. let component = new ComponentContent<Object>(context, wrapBuilder(buildText));
29. componentContentMap.push(component);
30. this.rootNode.addComponentContent(component);
31. }

33. deleteNode() {
34. let node = componentContentMap.pop();
35. this.rootNode?.dispose();
36. node?.dispose();
37. }
38. }

40. class MyFrameCallback extends FrameCallback {
41. onFrame() {
42. updateColorMode();
43. }
44. }

46. function updateColorMode() {
47. componentContentMap.forEach((value, index) => {
48. value.updateConfiguration();
49. })
50. }

52. @Entry
53. @Component
54. struct FrameNodeTypeTest {
55. private myNodeController: MyNodeController = new MyNodeController();

57. aboutToAppear(): void {
58. let environmentCallback: EnvironmentCallback = {
59. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
60. console.info('onMemoryLevel');
61. },
62. onConfigurationUpdated: (config: Configuration): void => {
63. console.info(`onConfigurationUpdated ${config}`);
64. this.getUIContext()?.postFrameCallback(new MyFrameCallback());
65. }
66. }
67. // 注册监听回调
68. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
69. // 设置应用深浅色跟随系统
70. this.getUIContext()
71. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
72. this.myNodeController.createNode(this.getUIContext());
73. }

75. aboutToDisappear(): void {
76. // 移除map中的引用，并将自定义节点释放
77. this.myNodeController.deleteNode();
78. }

80. build() {
81. Column({ space: 16 }) {
82. NodeContainer(this.myNodeController);
83. Button('切换深色')
84. .onClick(() => {
85. this.getUIContext()
86. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
87. })
88. Button('设置浅色')
89. .onClick(() => {
90. this.getUIContext()
91. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
92. })
93. }
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/oIavGlIGTwuouw-fLO-ijA/zh-cn_image_0000002552959442.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=99581497DC9B260E87930D1A4C0BD7CE2859A91B857A053F3365ACFC5507636A)

### isDisposed20+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前ComponentContent对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = "";

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .fontSize(50)
17. .fontWeight(FontWeight.Bold)
18. .margin({ bottom: 36 })
19. }.backgroundColor('#FFF0F0F0')
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = "hello";
26. @State beforeDispose: string = ''
27. @State afterDispose: string = ''

29. build() {
30. Row() {
31. Column() {
32. Button("click me")
33. .onClick(() => {
34. let uiContext = this.getUIContext();
35. let promptAction = uiContext.getPromptAction();
36. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
37. promptAction.openCustomDialog(contentNode);

39. setTimeout(() => {
40. promptAction.closeCustomDialog(contentNode)
41. .then(() => {
42. console.info('customDialog closed.');
43. if (contentNode !== null) {
44. this.beforeDispose =
45. contentNode.isDisposed() ? 'before dispose componentContent isDisposed is true' :
46. 'before dispose componentContent isDisposed is false';
47. contentNode.dispose(); // 释放contentNode
48. this.afterDispose = contentNode.isDisposed() ? 'after dispose componentContent isDisposed is true' :
49. 'after dispose componentContent isDisposed is false';
50. }
51. }).catch((error: BusinessError) => {
52. let message = (error as BusinessError).message;
53. let code = (error as BusinessError).code;
54. console.error(`closeCustomDialog args error code is ${code}, message is ${message}`);
55. })
56. }, 1000); // 1秒后自动关闭
57. })
58. Text(this.beforeDispose)
59. .fontSize(25)
60. .margin({ top: 10, bottom: 10 })
61. Text(this.afterDispose)
62. .fontSize(25)
63. }
64. .width('100%')
65. .height('100%')
66. }
67. .height('100%')
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/SW9SVQeATaiM_3Fyx_XHTw/zh-cn_image_0000002583479443.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=626BAE19026AC55DD6EA699E35AC96052B9920C46F6C94C72A578DF427985C17)

### inheritFreezeOptions20+

PhonePC/2in1TabletTVWearable

inheritFreezeOptions(enabled: boolean): void

查询当前ComponentContent对象是否设置为继承父组件中自定义组件的冻结策略。如果设置继承状态为false，则ComponentContent对象的冻结策略为false。在这种情况下，节点在不活跃状态下不会被冻结。

说明

ComponentContent设置inheritFreezeOptions为true，且父组件为自定义组件、BuilderNode、ComponentContent、ReactiveBuilderNode或ReactiveComponentContent时，会继承父组件的冻结策略。当子组件为自定义组件时，其冻结策略不会传递给子组件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | ComponentContent对象是否设置为继承父组件中自定义组件的冻结策略。true为继承父组件中自定义组件的冻结策略，false为不继承父组件中自定义组件的冻结策略。 |

**示例：**

```
1. import { ComponentContent, FrameNode, NodeController } from '@kit.ArkUI';

3. class Params {
4. count: number = 0;

6. constructor(count: number) {
7. this.count = count;
8. }
9. }

11. @Builder
12. // builder组件
13. function buildText(params: Params) {

15. Column() {
16. TextBuilder({ message: params.count })
17. }
18. }

20. class TextNodeController extends NodeController {
21. private rootNode: FrameNode | null = null;
22. private contentNode: ComponentContent<Params> | null = null;
23. private count: number = 0;

25. makeNode(context: UIContext): FrameNode | null {
26. this.rootNode = new FrameNode(context);
27. this.contentNode =
28. new ComponentContent(context, wrapBuilder(buildText), new Params(this.count)); // 通过buildText创建ComponentContent
29. this.contentNode.inheritFreezeOptions(true); // 设置ComponentContent的冻结继承状态为True
30. if (this.rootNode !== null) {
31. this.rootNode.addComponentContent(this.contentNode); // 将ComponentContent上树
32. }
33. return this.rootNode;
34. }

36. update(): void {
37. if (this.contentNode !== null) {
38. this.count += 1;
39. this.contentNode.update(new Params(this.count)); // 更新ComponentContent中的数据，可以触发Log
40. }
41. }
42. }

44. const textNodeController: TextNodeController = new TextNodeController();

46. @Entry
47. @Component
48. struct MyNavigationTestStack {
49. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
50. @State message: number = 0;
51. @State logNumber: number = 0;

53. @Builder
54. PageMap(name: string) {
55. if (name === 'pageOne') {
56. pageOneStack({ message: this.message, logNumber: this.logNumber })
57. } else if (name === 'pageTwo') {
58. pageTwoStack({ message: this.message, logNumber: this.logNumber })
59. }
60. }

62. build() {
63. Column() {
64. Button('update ComponentContent') // 点击更新ComponentContent
65. .onClick(() => {
66. textNodeController.update();
67. })
68. Navigation(this.pageInfo) {
69. Column() {
70. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
71. .width('80%')
72. .height(40)
73. .margin(20)
74. .onClick(() => {
75. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
76. })
77. }
78. }.title('NavIndex')
79. .navDestination(this.PageMap)
80. .mode(NavigationMode.Stack)
81. }
82. }
83. }

85. @Component
86. struct pageOneStack { // 页面一
87. @Consume('pageInfo') pageInfo: NavPathStack;
88. @State index: number = 1;
89. @Link message: number;
90. @Link logNumber: number;

92. build() {
93. NavDestination() {
94. Column() {
95. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
96. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule }) // 切换至页面二
97. .width('80%')
98. .height(40)
99. .margin(20)
100. .onClick(() => {
101. this.pageInfo.pushPathByName('pageTwo', null);
102. })
103. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回主页面
104. .width('80%')
105. .height(40)
106. .margin(20)
107. .onClick(() => {
108. this.pageInfo.pop();
109. })
110. }.width('100%').height('100%')
111. }.title('pageOne')
112. .onBackPressed(() => {
113. this.pageInfo.pop();
114. return true;
115. })
116. }
117. }

119. @Component
120. struct pageTwoStack { // 页面二
121. @Consume('pageInfo') pageInfo: NavPathStack;
122. @State index: number = 2;
123. @Link message: number;
124. @Link logNumber: number;

126. build() {
127. NavDestination() {
128. Column() {
129. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
130. Text('BuilderNode处于冻结')
131. .fontWeight(FontWeight.Bold)
132. .margin({ top: 48, bottom: 48 })
133. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回至页面一
134. .width('80%')
135. .height(40)
136. .margin(20)
137. .onClick(() => {
138. this.pageInfo.pop();
139. })
140. }.width('100%').height('100%')
141. }.title('pageTwo')
142. .onBackPressed(() => {
143. this.pageInfo.pop();
144. return true;
145. })
146. }
147. }

149. @Component({ freezeWhenInactive: true })
150. // 设置冻结策略为不活跃冻结
151. struct NavigationContentMsgStack {
152. @Link message: number;
153. @Link index: number;
154. @Link logNumber: number;

156. build() {
157. Column() {
158. if (this.index === 1) {
159. NodeContainer(textNodeController)
160. }
161. }
162. }
163. }

165. @Component({ freezeWhenInactive: true })
166. // 设置冻结策略为不活跃冻结
167. struct TextBuilder {
168. @Prop @Watch("info") message: number = 0;

170. info() {
171. console.info(`freeze-test TextBuilder message callback ${this.message}`); // 根据message内容变化来打印日志来判断是否冻结
172. }

174. build() {
175. Row() {
176. Column() {
177. Text(`文本更新次数： ${this.message}`)
178. .fontWeight(FontWeight.Bold)
179. .margin({ top: 48, bottom: 48 })
180. }
181. }
182. }
183. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/fgpE1Q3fRPmtnSQQ0amyrA/zh-cn_image_0000002552799794.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=6488585B2BC63980C5982BAC1BD1346820B450EA378F7EDAD876E721B14AFB0A)

## ReactiveComponentContent22+

PhonePC/2in1TabletTVWearable

ReactiveComponentContent继承自[Content](js-apis-arkui-content.md#content-1)，是一个用于动态承载和复用UI内容的容器组件。它通过@Builder函数构建UI，并利用[ReactiveBuilderNode](js-apis-arkui-buildernode.md#reactivebuildernode22)生成和管理组件树。该组件的核心价值在于为动态内容提供完整的生命周期管理，使其能够融入ArkUI的组件复用体系，特别适用于长列表等需要高性能渲染的场景。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor22+

PhonePC/2in1TabletTVWearable

constructor(uiContext: UIContext, builder: WrappedBuilder<T>, config: BuildOptions, ...args: T)

ReactiveComponentContent的构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 创建对应节点时所需的UI上下文。 |
| builder | [WrappedBuilder<T>](../harmonyos-guides/arkts-wrapbuilder.md) | 是 | 封装带参@Builder函数的WrappedBuilder对象。 |
| config | [BuildOptions](js-apis-arkui-buildernode.md#buildoptions12) | 是 | 作用是配置Builder的构建行为，BuildOptions中所有属性都是可选的，默认值为BuildOptions中对应的默认值。 |
| ...args | T | 否 | WrappedBuilder对象封装的builder函数的参数。负责将外部数据传递给构造函数中指定的WrappedBuilder<T>构建函数。支持多个入参。默认值为undefined。 |

**示例：**

该示例展示了如何使用ReactiveComponentContent构造函数动态创建包含响应式内容的UI组件，实现了Builder函数的嵌套调用和函数参数的灵活传递。

```
1. import { ReactiveComponentContent, NodeContent, typeNode } from '@kit.ArkUI';

3. @Builder
4. function buildTextWithFunc(fun: Function) {
5. Text(fun())
6. .fontSize(20)
7. .fontWeight(FontWeight.Bold)
8. .margin({ bottom: 36 })
9. }

11. @Builder
12. function buildText(text: string, func: Function) {
13. Column() {
14. Text(text)
15. .fontSize(20)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 12 })
18. buildTextWithFunc(func)
19. }
20. }

22. @Entry
23. @Component
24. struct Index {
25. @State message: string = 'HELLO';
26. private content: NodeContent = new NodeContent();

28. build() {
29. Row() {
30. Column({ space: 12 }) {
31. Button('addComponentContent')
32. .onClick(() => {
33. // 动态创建Column节点
34. let column = typeNode.createNode(this.getUIContext(), 'Column');
35. column.initialize();
36. // 创建ReactiveComponentContent并添加到Column节点
37. column.addComponentContent(new ReactiveComponentContent<[string, Function]>(this.getUIContext(),
38. wrapBuilder<[string, Function]>(buildText), { nestingBuilderSupported: true },
39. this.message,
40. () => {
41. return 'FUNCTION'
42. }
43. ));
44. // 将构建好的节点添加到内容容器
45. this.content.addFrameNode(column);
46. })
47. ContentSlot(this.content) // 显示动态添加的内容
48. }
49. .id('column')
50. .width('100%')
51. .height('100%')
52. }
53. .height('100%')
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/dFOkGO1SQyix_S2a3qYXrg/zh-cn_image_0000002552959440.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=17C46417D841D6D508265B637BD7BC356E014658B77A47ED0D93269E666CEB92)

### reuse22+

PhonePC/2in1TabletTVWearable

reuse(param?: Object): void

触发ReactiveComponentContent中的自定义组件的复用。组件复用请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。关于ReactiveComponentContent的解绑场景请参见[解除实体节点引用关系](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

ReactiveComponentContent通过reuse和[recycle](js-apis-arkui-componentcontent.md#recycle)接口完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Object | 否 | 用于复用[ReactiveComponentContent](js-apis-arkui-buildernode.md#reactivebuildernode22)的参数。该参数将直接用于ReactiveComponentContent中所有顶层自定义组件的复用，应该包含每个自定义组件的构造函数参数所需内容，否则会导致未定义行为。调用此方法将同步触发内部自定义组件的[aboutToReuse](ts-custom-component-lifecycle.md#abouttoreuse10)生命周期回调，并将该参数作为回调的入参。默认值为undefined，此时ReactiveComponentContent中的自定义组件将直接使用构造时的数据源。 |

**示例：**

请参考[recycle](js-apis-arkui-componentcontent.md#recycle22)中的示例。

### recycle22+

PhonePC/2in1TabletTVWearable

recycle(): void

触发ReactiveComponentContent中自定义组件的回收。自定义组件的回收是组件复用机制中的环节，具体信息请参见[@Reusable装饰器：V1组件复用](../harmonyos-guides/arkts-reusable.md)。

ReactiveComponentContent通过[reuse](js-apis-arkui-componentcontent.md#reuse)和recycle完成其内外自定义组件之间的复用事件传递，具体使用场景请参见[BuilderNode调用reuse和recycle接口实现节点复用能力](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#buildernode调用reuse和recycle接口实现节点复用能力)。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

实现了一个包含多层组件复用的高性能长列表，通过ReactiveComponentContent动态管理Builder内容，在列表滚动时实现组件的自动回收与复用。

```
1. import { NodeContent, typeNode, ReactiveComponentContent } from '@kit.ArkUI';

3. const TEST_TAG: string = 'Reuse+Recycle';

5. // 自定义数据源类，用于管理列表数据
6. class MyDataSource {
7. private dataArray: string[] = [];
8. private listener: DataChangeListener | null = null;

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number) {
15. return this.dataArray[index];
16. }

18. public pushData(data: string) {
19. this.dataArray.push(data);
20. }

22. public reloadListener(): void {
23. this.listener?.onDataReloaded();
24. }

26. public registerDataChangeListener(listener: DataChangeListener): void {
27. this.listener = listener;
28. }

30. public unregisterDataChangeListener(): void {
31. this.listener = null;
32. }
33. }

35. @Builder
36. function buildNode(param: string) {
37. Row() {
38. Text(`C${param} -- `)
39. ReusableChildComponent2({ item: param })
40. }
41. }

43. @Reusable
44. @Component
45. struct ReusableChildComponent {
46. @Prop item: string = '';
47. @Prop switch: string = '';
48. private content: NodeContent = new NodeContent();
49. // 创建ReactiveComponentContent实例，封装Builder动态内容
50. private componentContent: ReactiveComponentContent<[string]> = new ReactiveComponentContent<[string]>(
51. this.getUIContext(),
52. wrapBuilder<[string]>(buildNode),
53. { nestingBuilderSupported: true },
54. this.item);

56. aboutToAppear() {
57. let column = typeNode.createNode(this.getUIContext(), 'Column');
58. column.initialize();
59. column.addComponentContent(this.componentContent);
60. this.content.addFrameNode(column);
61. }

63. // 组件回收生命周期回调
64. aboutToRecycle(): void {
65. console.info(`${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);

67. // 当开关开启时，触发内部ReactiveComponentContent的回收
68. if (this.switch === 'open') {
69. this.componentContent.recycle();
70. }
71. }

73. // 组件复用时命周期回调
74. aboutToReuse(params: object): void {
75. console.info(`${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);

77. // 当开关开启时，触发内部ReactiveComponentContent的复用
78. if (this.switch === 'open') {
79. this.componentContent.reuse(params);
80. }
81. }

83. build() {
84. Row() {
85. Text(`A${this.item}--`)
86. ReusableChildComponent3({ item: this.item })
87. ContentSlot(this.content)
88. }
89. }
90. }

92. @Component
93. struct ReusableChildComponent2 {
94. @Prop item: string = 'false';

96. aboutToReuse(params: Record<string, object>) {
97. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
98. }

100. aboutToRecycle(): void {
101. console.info(`${TEST_TAG} ReusableChildComponent2 aboutToRecycle ${this.item}`);
102. }

104. build() {
105. Row() {
106. Text(`D${this.item}`)
107. .fontSize(20)
108. .backgroundColor(Color.Yellow)
109. .margin({ left: 10 })
110. }.margin({ left: 10, right: 10 })
111. }
112. }

114. @Component
115. struct ReusableChildComponent3 {
116. @Prop item: string = 'false';

118. aboutToReuse(params: Record<string, object>) {
119. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToReuse ${JSON.stringify(params)}`);
120. }

122. aboutToRecycle(): void {
123. console.info(`${TEST_TAG} ReusableChildComponent3 aboutToRecycle ${this.item}`);
124. }

126. build() {
127. Row() {
128. Text(`B${this.item}`)
129. .fontSize(20)
130. .backgroundColor(Color.Yellow)
131. .margin({ left: 10 })
132. }.margin({ left: 10, right: 10 })
133. }
134. }

136. @Entry
137. @Component
138. struct Index {
139. @State data: MyDataSource = new MyDataSource();

141. aboutToAppear() {
142. // 初始化100条测试数据
143. for (let i = 0; i < 100; i++) {
144. this.data.pushData(i.toString());
145. }
146. }

148. build() {
149. Column() {
150. // 使用LazyForEach渲染长列表，启用组件复用
151. List({ space: 3 }) {
152. LazyForEach(this.data, (item: string) => {
153. ListItem() {
154. ReusableChildComponent({
155. item: item,
156. switch: 'open'
157. })
158. }
159. }, (item: string) => item)
160. }
161. .width('100%')
162. .height('100%')
163. }
164. }
165. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/VYU8diBLQ3SBzwf6GWfigg/zh-cn_image_0000002552799792.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=79E7F3F964EF23C03A492666037C04772829A27109F25138A31253496EDA4F6B)

### dispose22+

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前ReactiveComponentContent对象对[实体节点](../harmonyos-guides/arkts-user-defined-node.md#基本概念)的引用关系。关于ReactiveComponentContent的解绑场景请参见[解除实体节点引用关系](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md#解除实体节点引用关系)。

说明

ReactiveComponentContent对象调用dispose接口后，会与后端实体节点解除引用关系。若前端ReactiveComponentContent对象无法释放，容易导致内存泄漏。建议开发者在不需要操作该ReactiveComponentContent对象时，主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏风险。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了如何使用dispose接口正确释放ReactiveComponentContent对象，管理节点生命周期。

```
1. import {
2. ReactiveComponentContent,
3. Binding,
4. MutableBinding,
5. UIContext,
6. UIUtils,
7. NodeController,
8. FrameNode
9. } from '@kit.ArkUI';

11. // dispose
12. @Builder
13. function buildText(
14. MsgAge: MutableBinding<number>,
15. message: MutableBinding<string>
16. ) {
17. Column() {
18. Row() {
19. Text(`age: ${MsgAge.value}, name: ${message.value}`)
20. }
21. }
22. .justifyContent(FlexAlign.Center)
23. .alignItems(HorizontalAlign.Center)
24. .width('100%')
25. .height('100%')
26. }

28. interface GeneratedObjectLiteralInterface_1 {
29. MsgAge: number;
30. message: string;
31. }

33. const params: GeneratedObjectLiteralInterface_1 = {
34. MsgAge: 10,
35. message: 'Mike',
36. };

38. class MyNodeController extends NodeController {
39. private rootNode: FrameNode | null = null;
40. private contentNode: ReactiveComponentContent<[Binding<number>, Binding<string>]> | null = null;

42. makeNode(context: UIContext): FrameNode | null {
43. // 创建FrameNode作为根容器
44. this.rootNode = new FrameNode(context);
45. // 创建ReactiveComponentContent响应式内容
46. this.contentNode = new ReactiveComponentContent <[Binding<number>, Binding<string>]>(context,
47. wrapBuilder<[Binding<number>, Binding<string>]>(buildText),
48. {},
49. UIUtils.makeBinding<number>(() => params.MsgAge, (val: number) => {
50. params.MsgAge = val
51. console.info("NodeTest1 get", params.MsgAge);
52. }),
53. UIUtils.makeBinding<string>(() => params.message, val => {
54. console.info("NodeTest2 set before", params.message);
55. params.message = val;
56. console.info("NodeTest3 set after", params.message);
57. }),
58. );
59. // 将响应式内容添加到根节点
60. if (this.rootNode !== null) {
61. this.rootNode.addComponentContent(this.contentNode);
62. }
63. return this.rootNode;
64. }

66. // 释放资源的方法
67. dispose() {
68. if (this.contentNode !== null) {
69. this.contentNode.dispose(); // 释放ReactiveComponentContent资源
70. }
71. }
72. }

74. @Entry
75. @Component
76. struct Index {
77. private myNodeController: MyNodeController = new MyNodeController();

79. build() {
80. Row() {
81. Column() {
82. // 显示自定义节点内容
83. NodeContainer(this.myNodeController)
84. .width('100%')
85. .height(100)
86. .backgroundColor('#FFF0F0F0')
87. // 触发资源释放
88. Button('ReactiveComponentContent dispose')
89. .onClick(() => {
90. this.myNodeController.dispose(); // 调用dispose释放资源
91. })
92. }
93. .width('100%')
94. .height('100%')
95. }
96. }
97. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/bRvhivOTRuu8tAkLHXp3xQ/zh-cn_image_0000002583439489.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=805EC7187C8A57E263288293FA2CFCB5D0B0085B3A4F412BAE529CDEF3A8EF85)

### updateConfiguration22+

PhonePC/2in1TabletTVWearable

updateConfiguration(): void

传递[系统环境变化](js-apis-app-ability-configuration.md)事件，触发节点的全量更新。可用于通知对象更新，是否更新所使用的系统环境由应用当前的系统环境变化决定。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了如何使用updateConfiguration接口响应系统环境配置变化，实现ReactiveComponentContent构建的UI节点的动态适配更新。

```
1. import { NodeController, FrameNode, ReactiveComponentContent, UIContext, FrameCallback } from '@kit.ArkUI';
2. import { AbilityConstant, Configuration, EnvironmentCallback, ConfigurationConstant } from '@kit.AbilityKit';

4. @Builder
5. function buildText() {
6. Column() {
7. Text('Hello')
8. .fontSize(20)
9. .fontWeight(FontWeight.Bold)
10. }
11. .backgroundColor($r('sys.color.ohos_id_color_background')) // 使用系统颜色资源，会根据深浅色模式自动切换
12. .width('100%')
13. .alignItems(HorizontalAlign.Center)
14. .padding(16)
15. }

17. const componentContentMap: Array<ReactiveComponentContent<[]>> = new Array();

19. class MyNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;

22. makeNode(uiContext: UIContext): FrameNode | null {
23. return this.rootNode;
24. }

26. createNode(context: UIContext) {
27. this.rootNode = new FrameNode(context);
28. let component = new ReactiveComponentContent<[]>(context, wrapBuilder(buildText), {});
29. componentContentMap.push(component);
30. this.rootNode.addComponentContent(component);
31. }

33. deleteNode() {
34. let node = componentContentMap.pop();
35. this.rootNode?.dispose();
36. node?.dispose();
37. }
38. }

40. class MyFrameCallback extends FrameCallback {
41. onFrame() {
42. updateColorMode();
43. }
44. }

46. // 遍历所有ReactiveComponentContent实例，调用updateConfiguration通知系统环境变化
47. function updateColorMode() {
48. componentContentMap.forEach((value, index) => {
49. // updateConfiguration()的作用：传递系统环境变化事件，触发节点的全量更新
50. // 当系统深浅色模式、语言、字体大小等配置发生变化时，调用此接口会通知ReactiveComponentContent重新应用最新的系统配置
51. value.updateConfiguration();
52. })
53. }

55. @Entry
56. @Component
57. struct FrameNodeTypeTest {
58. private myNodeController: MyNodeController = new MyNodeController();

60. aboutToAppear(): void {
61. let environmentCallback: EnvironmentCallback = {
62. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
63. console.info('onMemoryLevel');
64. },
65. onConfigurationUpdated: (config: Configuration): void => {
66. console.info(`onConfigurationUpdated ${config}`);
67. // 当系统配置更新时，通过帧回调触发updateConfiguration调用
68. this.getUIContext()?.postFrameCallback(new MyFrameCallback());
69. }
70. }
71. // 注册监听系统环境变化的回调
72. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
73. // 设置应用深浅色跟随系统
74. this.getUIContext()
75. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
76. this.myNodeController.createNode(this.getUIContext());
77. }

79. aboutToDisappear(): void {
80. // 移除componentContentMap中的引用，并将自定义节点释放
81. this.myNodeController.deleteNode();
82. }

84. build() {
85. Column({ space: 16 }) {
86. NodeContainer(this.myNodeController);
87. Button('设置深色')
88. .onClick(() => {
89. this.getUIContext()
90. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
91. })
92. Button('设置浅色')
93. .onClick(() => {
94. this.getUIContext()
95. .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
96. })
97. }
98. }
99. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/i0OdNdNzT9GJubTZmrlgZg/zh-cn_image_0000002552959442.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=760E390619282A998F3201B1CCC48613348FDF3FEF2B4C5F72F92FAE546E9F64)

### flushState22+

PhonePC/2in1TabletTVWearable

flushState(): void

更新ReactiveComponentContent。当ReactiveComponentContent中[WrappedBuilder](../harmonyos-guides/arkts-wrapbuilder.md)对象封装的builder函数中使用的绑定参数是由V1装饰器（如@Observed）装饰的类实例时，需要在此类数据变更后手动调用本接口更新数据，当使用V2装饰器（如@ObservedV2）装饰的类实例时，支持自动更新，无需手动调用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

该示例展示了flushState接口在ReactiveComponentContent中的使用场景，通过对比V1和V2装饰器的数据更新机制，演示了不同响应式方案下的状态更新策略。

```
1. import {
2. ReactiveComponentContent, NodeContent, Binding, UIUtils, typeNode
3. } from '@kit.ArkUI';

5. // Builder函数，用于构建显示年龄的文本组件
6. @Builder
7. function buildText(age: Binding<number>) {
8. Column() {
9. Text(`age: ${age.value}`); // 显示年龄值
10. }
11. }

13. // 使用V2装饰器的类，支持自动状态更新
14. @ObservedV2
15. class GeneratedObjectLiteralInterface_1 {
16. constructor(age: number) {
17. this.age = age;
18. }

20. @Trace age: number = 0; // 使用@Trace装饰器追踪属性变化
21. }

23. // 使用普通类（V1装饰器风格），需要手动触发更新
24. class GeneratedObjectLiteralInterface_2 {
25. constructor(age: number) {
26. this.age = age;
27. }

29. age: number = 0; // 普通属性，无自动追踪
30. }

32. @Entry
33. @ComponentV2
34. struct Index {
35. private content: NodeContent = new NodeContent();
36. // V2装饰器的数据对象，支持自动更新
37. params: GeneratedObjectLiteralInterface_1 = new GeneratedObjectLiteralInterface_1(25);
38. // V1装饰器的数据对象，需要手动更新
39. params2: GeneratedObjectLiteralInterface_2 = new GeneratedObjectLiteralInterface_2(25);
40. private componentContent: ReactiveComponentContent<[Binding<number>]> | null = null

42. build() {
43. Row() {
44. Scroll() {
45. Column({ space: 12 }) {
46. // 创建使用V2装饰器的ReactiveComponentContent
47. Button('绑定参数由V2装饰器装饰').onClick(
48. () => {
49. let column = typeNode.createNode(this.getUIContext(), "Column");
50. column.initialize();
51. // 创建ReactiveComponentContent，使用V2装饰器的数据绑定
52. column.addComponentContent(new ReactiveComponentContent<[Binding<number>]>(this.getUIContext(),
53. wrapBuilder<[Binding<number>]>(buildText),
54. {},
55. UIUtils.makeBinding<number>(() => {
56. return this.params.age; // 绑定V2装饰器的数据
57. })));

59. this.content.addFrameNode(column);
60. })

62. // 创建使用V1装饰器的ReactiveComponentContent
63. Button('绑定参数由V1装饰器装饰').onClick(
64. () => {
65. let column = typeNode.createNode(this.getUIContext(), "Column");
66. column.initialize();
67. // 创建ReactiveComponentContent，使用V1装饰器的数据绑定
68. this.componentContent =
69. new ReactiveComponentContent<[Binding<number>]>(this.getUIContext(),
70. wrapBuilder<[Binding<number>]>(buildText),
71. {},
72. UIUtils.makeBinding<number>(() => {
73. return this.params2.age; // 绑定V1装饰器的数据
74. })
75. );
76. column.addComponentContent(this.componentContent);
77. this.content.addFrameNode(column);
78. })

80. // 更新V2装饰器的数据（自动更新）
81. Button('change age - V2可自动更新').onClick(() => {
82. this.params.age += 1; // V2装饰器会自动检测变化并更新UI
83. })

85. // 更新V1装饰器的数据（需要手动更新）
86. Button('change age - V1需手动更新').onClick(() => {
87. this.params2.age += 1;
88. // 对于V1装饰器的数据，需要手动调用flushState来触发UI更新
89. this.componentContent?.flushState();
90. })

92. // 显示动态创建的内容
93. ContentSlot(this.content)
94. }
95. .id("column")
96. .width('100%')
97. }
98. .scrollable(ScrollDirection.Vertical)
99. .scrollBar(BarState.On)
100. .scrollBarColor(Color.Gray)
101. .scrollBarWidth(10)
102. }
103. .height('100%')
104. }
105. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/ZsG1c4pCS3muBTHSAQivcQ/zh-cn_image_0000002552959444.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=25DFC03FF8DC9C125EE6B573C4E4A46C085E6F0C054786C4B1E3D6ED41E4DA36)

### inheritFreezeOptions22+

PhonePC/2in1TabletTVWearable

inheritFreezeOptions(enabled: boolean): void

查询当前ReactiveComponentContent对象是否设置为继承父组件中自定义组件的[冻结策略](ts-custom-component-parameter.md#componentoptions)。如果设置继承状态为false，则ReactiveComponentContent对象的冻结策略为false。在这种情况下，节点在不活跃状态下不会被冻结。

说明

ReactiveComponentContent设置inheritFreezeOptions为true，且父组件为自定义组件、BuilderNode、ComponentContent、ReactiveBuilderNode或ReactiveComponentContent时，会继承父组件的冻结策略。当子组件为自定义组件时，其冻结策略不会传递给子组件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | ReactiveComponentContent对象是否设置为继承父组件中自定义组件的冻结策略。  true：继承父组件中自定义组件的冻结策略；false：不继承父组件中自定义组件的冻结策略。 |

**示例：**

该示例演示了ReactiveComponentContent设置继承状态为true，继承父自定义组件的冻结策略，在不活跃的时候进行冻结，切换为活跃状态解冻，更新缓存的数据。

```
1. import { ReactiveComponentContent, FrameNode, NodeController, Binding, UIUtils } from '@kit.ArkUI';

3. @Builder
4. // builder组件
5. function buildText(count: Binding<number>) {

7. Column() {
8. TextBuilder({ message: count.value })
9. }
10. }

12. class TextNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;
14. private contentNode: ReactiveComponentContent<[Binding<number>]> | null = null;
15. private count: number = 0;

17. makeNode(context: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(context);
19. this.contentNode = new ReactiveComponentContent(context, wrapBuilder<[Binding<number>]>(buildText), {},
20. UIUtils.makeBinding<number>(() => {
21. return this.count
22. }));
23. this.contentNode.inheritFreezeOptions(true);
24. if (this.rootNode !== null) {
25. this.rootNode.addComponentContent(this.contentNode);
26. }
27. return this.rootNode;
28. }

30. update(): void {
31. if (this.contentNode !== null) {
32. this.count += 1;
33. this.contentNode.flushState();
34. }
35. }
36. }

38. const textNodeController: TextNodeController = new TextNodeController();

40. @Entry
41. @Component
42. struct MyNavigationTestStack {
43. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
44. @State message: number = 0;
45. @State logNumber: number = 0;

47. @Builder
48. PageMap(name: string) {
49. if (name === 'pageOne') {
50. pageOneStack({ message: this.message, logNumber: this.logNumber })
51. } else if (name === 'pageTwo') {
52. pageTwoStack({ message: this.message, logNumber: this.logNumber })
53. }
54. }

56. build() {
57. Column() {
58. Button('update ComponentContent')
59. .onClick(() => {
60. textNodeController.update();
61. })
62. Navigation(this.pageInfo) {
63. Column() {
64. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
65. .width('80%')
66. .height(40)
67. .margin(20)
68. .onClick(() => {
69. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
70. })
71. }
72. }.title('NavIndex')
73. .navDestination(this.PageMap)
74. .mode(NavigationMode.Stack)
75. }
76. }
77. }

79. @Component
80. struct pageOneStack { // 页面一
81. @Consume('pageInfo') pageInfo: NavPathStack;
82. @State index: number = 1;
83. @Link message: number;
84. @Link logNumber: number;

86. build() {
87. NavDestination() {
88. Column() {
89. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
90. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule }) // 切换至页面二
91. .width('80%')
92. .height(40)
93. .margin(20)
94. .onClick(() => {
95. this.pageInfo.pushPathByName('pageTwo', null);
96. })
97. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回主页面
98. .width('80%')
99. .height(40)
100. .margin(20)
101. .onClick(() => {
102. this.pageInfo.pop();
103. })
104. }.width('100%').height('100%')
105. }.title('pageOne')
106. .onBackPressed(() => {
107. this.pageInfo.pop();
108. return true;
109. })
110. }
111. }

113. @Component
114. struct pageTwoStack { // 页面二
115. @Consume('pageInfo') pageInfo: NavPathStack;
116. @State index: number = 2;
117. @Link message: number;
118. @Link logNumber: number;

120. build() {
121. NavDestination() {
122. Column() {
123. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
124. Text('BuilderNode处于冻结状态')
125. .fontWeight(FontWeight.Bold)
126. .margin({ top: 48, bottom: 48 })
127. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule }) // 返回至页面一
128. .width('80%')
129. .height(40)
130. .margin(20)
131. .onClick(() => {
132. this.pageInfo.pop();
133. })
134. }.width('100%').height('100%')
135. }.title('pageTwo')
136. .onBackPressed(() => {
137. this.pageInfo.pop();
138. return true;
139. })
140. }
141. }

143. @Component({ freezeWhenInactive: true })
144. // 设置冻结策略为不活跃冻结
145. struct NavigationContentMsgStack {
146. @Link message: number;
147. @Link index: number;
148. @Link logNumber: number;

150. build() {
151. Column() {
152. if (this.index === 1) {
153. NodeContainer(textNodeController)
154. }
155. }
156. }
157. }

159. @Component({ freezeWhenInactive: true })
160. // 设置冻结策略为不活跃冻结
161. struct TextBuilder {
162. @Prop @Watch('info') message: number = 0;

164. info() {
165. console.info(`freeze-test TextBuilder message callback ${this.message}`); // 根据message内容变化来打印日志来判断是否冻结
166. }

168. build() {
169. Row() {
170. Column() {
171. Text(`文本更新次数： ${this.message}`)
172. .fontWeight(FontWeight.Bold)
173. .margin({ top: 48, bottom: 48 })
174. }
175. }
176. }
177. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/lYM__FmSRLmUDaam8oCcVA/zh-cn_image_0000002583479445.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=533C0FF08CFE52D5EA168FD1CB4C3FF3751BB1D707EAA7328436C195DF1A6A7D)

### isDisposed22+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前ReactiveComponentContent对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。因为在节点dispose后可能仍存在被调用dispose接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。  true：节点已与后端实体节点解除引用；false：节点未与后端实体节点解除引用。 |

**示例：**

该示例展示了如何使用isDisposed接口检查ReactiveComponentContent对象是否已解除与后端实体节点的引用关系，提供了节点状态安全检测的完整实现方案。

```
1. import {
2. ReactiveComponentContent,
3. Binding,
4. MutableBinding,
5. UIContext,
6. UIUtils,
7. NodeController,
8. FrameNode
9. } from '@kit.ArkUI';

11. @Builder
12. function buildText(
13. MsgAge: MutableBinding<number>,
14. message: MutableBinding<string>
15. ) {
16. Column() {
17. Row() {
18. Text(`age: ${MsgAge.value}, name: ${message.value}`)
19. .fontSize(15)
20. }
21. }
22. .justifyContent(FlexAlign.Center)
23. .alignItems(HorizontalAlign.Center)
24. .width('100%')
25. .height('100%')
26. }

28. interface GeneratedObjectLiteralInterface_1 {
29. MsgAge: number;
30. message: string;
31. }

33. const params: GeneratedObjectLiteralInterface_1 = {
34. MsgAge: 10,
35. message: 'Mike',
36. };

38. class MyNodeController extends NodeController {
39. private rootNode: FrameNode | null = null;
40. private contentNode: ReactiveComponentContent<[Binding<number>, Binding<string>]> | null = null;

42. makeNode(context: UIContext): FrameNode | null {
43. this.rootNode = new FrameNode(context);
44. this.contentNode = new ReactiveComponentContent <[Binding<number>, Binding<string>]>(context,
45. wrapBuilder<[Binding<number>, Binding<string>]>(buildText),
46. {},
47. UIUtils.makeBinding<number>(() => params.MsgAge, (val: number) => {
48. params.MsgAge = val
49. console.info("NodeTest1 get", params.MsgAge);
50. }),
51. UIUtils.makeBinding<string>(() => params.message, val => {
52. console.info("NodeTest2 set before", params.message);
53. params.message = val;
54. console.info("NodeTest3 set after", params.message);
55. }),
56. );
57. if (this.rootNode !== null) {
58. this.rootNode.addComponentContent(this.contentNode);
59. }
60. return this.rootNode;
61. }

63. dispose() {
64. if (this.contentNode !== null) {
65. this.contentNode.dispose();
66. }
67. }

69. // 检验当前Node是否已被释放
70. isDisposed(): string {
71. if (this.contentNode !== null) {
72. if (this.contentNode.isDisposed()) {
73. return 'contentNode isDisposed is true';
74. } else {
75. return 'contentNode isDisposed is false';
76. }
77. }
78. return 'contentNode is null';
79. }
80. }

82. @Entry
83. @Component
84. struct Index {
85. @State text: string = ''
86. private myNodeController: MyNodeController = new MyNodeController();

88. build() {
89. Row() {
90. Column({ space: 12 }) {
91. NodeContainer(this.myNodeController)
92. .width('100%')
93. .height(100)
94. .backgroundColor('#FFF0F0F0')
95. Button('dispose')
96. .onClick(() => {
97. this.myNodeController.dispose();
98. this.text = '';
99. })
100. .fontSize(15)
101. .width(200)
102. .height(30)
103. Button('isDisposed')
104. .onClick(() => {
105. this.text = this.myNodeController.isDisposed();
106. })
107. .width(200)
108. .height(30)
109. .fontSize(15)
110. Text(this.text)
111. .fontSize(15)
112. }
113. .width('100%')
114. .height('100%')
115. }
116. }
117. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/II11jDevSZKk4qZBXMkIiw/zh-cn_image_0000002552799796.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000034Z&HW-CC-Expire=86400&HW-CC-Sign=F3E470E30C9A73EC79E4ED8B60C8A9F11173504BA604938AEFB478A140218FE8)
