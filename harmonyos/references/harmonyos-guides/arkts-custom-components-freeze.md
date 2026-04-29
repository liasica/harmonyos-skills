---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freeze
title: 自定义组件冻结功能（V1）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件冻结 > 自定义组件冻结功能（V1）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:04+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8f7979b70f6d77f7f5c5e452833183291d8c1f579e918bec1ea9109efd5781ae
---

自定义组件冻结功能专为优化复杂UI页面的性能而设计，尤其适用于包含多个页面栈、长列表或宫格布局的场景。当状态变量绑定多个UI组件时，其变化易触发大量组件刷新，导致界面卡顿与响应延迟。为提升这类高负载UI界面的刷新性能，建议开发者使用自定义组件冻结功能。

组件冻结功能是一种性能优化机制，它会冻结非激活状态下的组件的刷新能力。当组件处于非激活状态时，即使其绑定的状态变量发生变化，也不会触发该组件的UI重新渲染，从而降低复杂UI场景下的刷新负载。

在阅读本文档前，开发者需要了解自定义组件基本语法。建议提前阅读：[自定义组件](arkts-create-custom-components.md)。

说明

从API version 11开始，支持自定义组件冻结功能。

从API version 18开始，支持自定义组件冻结混用场景。

从API version 20开始，通过配置[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)的[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)接口为true，实现BuilderNode继承冻结的能力。具体示例见[BuilderNode对象继承组件冻结](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)。

## 概述

组件冻结的工作原理是：

1. 开发者通过设置[freezeWhenInactive](../harmonyos-references/ts-custom-component-parameter.md#componentoptions)属性，即可激活组件冻结机制。
2. 启用后，系统将仅对处于激活状态的自定义组件进行更新，这使得UI框架可以尽量缩小更新范围，仅限于用户可见范围内（激活状态）的自定义组件，从而提高复杂UI场景下的刷新效率。
3. 当之前处于inactive状态的自定义组件重新变为active状态时，状态管理框架会对其执行必要的刷新操作，确保UI的正确展示。

简而言之，组件冻结旨在优化复杂界面下的UI刷新性能。在存在多个不可见自定义组件的情况下，如多页面栈、长列表或宫格，通过组件冻结可以实现按需刷新，即仅刷新当前可见的自定义组件，而将不可见自定义组件的刷新延迟至它们变为可见时。

需要注意，组件active/inactive并不等同于其可见性。组件冻结目前仅适用于以下场景：

1. [页面路由](../harmonyos-references/js-apis-router.md)：当前栈顶页面为active状态，非栈顶不可见页面为inactive状态。
2. [TabContent](../harmonyos-references/ts-container-tabcontent.md)：只有当前显示的TabContent中的自定义组件处于active状态，其余则为inactive。
3. [LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)：仅当前显示的LazyForEach中的自定义组件为active状态，而缓存节点的组件则为inactive状态。
4. [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：当前显示的NavDestination中的自定义组件为active状态，而其他未显示的NavDestination组件则为inactive状态。需要注意，本文档中涉及的“激活（active）/非激活（inactive）”是指组件冻结的激活/非激活状态，和[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件中的[onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)和[onInactive](../harmonyos-references/ts-basic-components-navdestination.md#oninactive17)不同。
5. 组件复用：进入复用池的组件为inactive状态，从复用池上树的节点为active状态。
6. 混用场景：对于以上场景的组合使用，例如TabContent下面使用LazyForEach，切换Tab时，API version 17及以下，LazyForEach中的所有节点都会被设置为active状态，而从API version 18开始，只有LazyForEach的屏上节点会被设置为active状态，其余则为inactive状态。

## 当前支持的场景

### 页面路由

说明

本示例使用了router进行页面跳转，建议开发者使用组件导航(Navigation)代替页面路由(router)来实现页面切换。Navigation提供了更多的功能和更灵活的自定义能力。请参考[使用Navigation的组件冻结用例](arkts-custom-components-freeze.md#navigation)。

当页面1调用router.pushUrl接口跳转到页面2时，页面1为隐藏不可见状态，此时如果更新页面1中的状态变量，不会触发页面1刷新。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/6-FHAC1URDCqYeUkEls-4Q/zh-cn_image_0000002589323919.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=CBA700E262750B09844943859DB70D278CC0917430ACA7929F72F3432788FD5C)

页面1：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';
4. const STORAGE_LINK_INITIAL_VALUE = 47;

6. @Entry
7. @Component({ freezeWhenInactive: true })
8. struct PageOne {
9. @StorageLink('PropA') @Watch('first') storageLink: number = STORAGE_LINK_INITIAL_VALUE;

11. first() {
12. hilog.info(DOMAIN, TAG, 'first page ' + `${this.storageLink}`);
13. }

15. build() {
16. Column() {
17. Text(`From first Page ${this.storageLink}`).fontSize(50)
18. Button('first page storageLink + 1').fontSize(30)
19. .onClick(() => {
20. this.storageLink += 1;
21. })
22. Button('go to next page').fontSize(30)
23. .onClick(() => {
24. // 此处传入的url，需要开发者自行替换。
25. this.getUIContext().getRouter().pushUrl({ url: 'View/PageTwo' }, (err: Error) => {
26. if (err) {
27. hilog.error(DOMAIN, TAG, 'pushUrl failed. Cause: %{public}s', JSON.stringify(err));
28. }
29. });
30. })
31. }
32. }
33. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/Page1.ets#L15-L45)

页面2：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. @Entry
6. @Component({ freezeWhenInactive: true })
7. struct PageTwo {
8. @StorageLink('PropA') @Watch('second') storageLink: number = 1;

10. second() {
11. hilog.info(DOMAIN, TAG, 'second page: ' + `${this.storageLink}`);
12. }

14. build() {
15. Column() {
16. Text(`second Page ${this.storageLink}`).fontSize(50)
17. Button('back')
18. .onClick(() => {
19. this.getUIContext().getRouter().back();
20. })
21. // 点击Button修改storageLink，观察页面1隐藏时会不会触发first回调
22. Button('second page storageLink + 2').fontSize(30)
23. .onClick(() => {
24. this.storageLink += 2;
25. })
26. }
27. }
28. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/PageTwo.ets#L15-L43)

在上面的示例中：

1.在页面1中点击first page storageLink + 1，storageLink状态变量改变，[@Watch](arkts-watch.md)注册的方法first会被调用。

2.在页面1中点击go to next page，跳转到页面2，页面1隐藏，状态由active变为inactive。

3.在页面2中点击this.storageLink2 += 2，只会回调页面2中@Watch注册的方法second，因为页面1的状态变量此时已被冻结。

4.在页面2中点击back，页面2被销毁，页面1的状态由inactive变为active，重新刷新在inactive时被冻结的状态变量，页面1中@Watch注册的方法first被再次调用。

### TabContent

对Tabs中当前不可见的TabContent进行冻结，修改状态变量不会触发冻结组件的更新。

需要注意的是：在首次渲染的时候，Tabs只会创建当前正在显示的TabContent，当切换全部的TabContent后，TabContent才会被全部创建。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/BUGmInA7R9C0dO2-9ggjzg/zh-cn_image_0000002589243859.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=D4634EC055B5BE6D9B9B749F838A7D208964FDFEFFB0D5C5E6E50DAE22B13D3A)

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. @Entry
6. @Component
7. struct TabContentTest {
8. @State @Watch('onMessageUpdated') message: number = 0;
9. private data: number[] = [0, 1];

11. onMessageUpdated() {
12. hilog.info(DOMAIN, TAG, `TabContent message callback func ${this.message}`);
13. }

15. build() {
16. Row() {
17. Column() {
18. // 点击Button修改message，触发可见TabContent的onMessageUpdated回调
19. Button('change message').onClick(() => {
20. this.message++;
21. })
22. Tabs() {
23. ForEach(this.data, (item: number) => {
24. TabContent() {
25. FreezeChild({ message: this.message, index: item })
26. }.tabBar(`tab${item}`)
27. }, (item: number) => item.toString())
28. }
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }

36. @Component({ freezeWhenInactive: true })
37. struct FreezeChild {
38. @Link @Watch('onMessageUpdated') message: number;
39. index: number = 0;

41. onMessageUpdated() {
42. hilog.info(DOMAIN, TAG, `FreezeChild message callback func ${this.message}, index: ${this.index}`);
43. }

45. build() {
46. Text('message' + `${this.message}, index: ${this.index}`)
47. .fontSize(50)
48. .fontWeight(FontWeight.Bold)
49. }
50. }
```

[TabContentTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/TabContentTest.ets#L15-L65)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的TabContent组件中的@Watch注册的方法onMessageUpdated被触发。

2.点击tab1切换到另外的TabContent，该TabContent的状态由inactive变为active，对应的@Watch注册的方法onMessageUpdated被触发。

3.再次点击change message更改message的值，仅当前显示的TabContent子组件中的@Watch注册的方法onMessageUpdated被触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/oCjOzcfqT2GFK0p1fISpeA/zh-cn_image_0000002558764052.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=F72E11D10B24F8A903E702DB720A0AD72CB58992A26A9BA3EBD2389FA91A2AD1)

### LazyForEach

对LazyForEach中缓存的自定义组件进行冻结，修改状态变量不会触发缓存组件的更新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. // 用于处理数据监听的IDataSource的基本实现
6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: string[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): string {
15. return this.originDataArray[index];
16. }

18. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
19. registerDataChangeListener(listener: DataChangeListener): void {
20. if (this.listeners.indexOf(listener) < 0) {
21. hilog.info(DOMAIN, TAG, 'add listener');
22. this.listeners.push(listener);
23. }
24. }

26. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. hilog.info(DOMAIN, TAG, 'remove listener');
31. this.listeners.splice(pos, 1);
32. }
33. }

35. // 通知LazyForEach组件需要重载所有子组件
36. notifyDataReload(): void {
37. this.listeners.forEach(listener => {
38. listener.onDataReloaded();
39. })
40. }

42. // 通知LazyForEach组件需要在index对应索引处添加子组件
43. notifyDataAdd(index: number): void {
44. this.listeners.forEach(listener => {
45. listener.onDataAdd(index);
46. })
47. }

49. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
50. notifyDataChange(index: number): void {
51. this.listeners.forEach(listener => {
52. listener.onDataChange(index);
53. })
54. }

56. // 通知LazyForEach组件需要在index对应索引处删除该子组件
57. notifyDataDelete(index: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataDelete(index);
60. })
61. }
62. }

64. class MyDataSource extends BasicDataSource {
65. private dataArray: string[] = [];

67. public totalCount(): number {
68. return this.dataArray.length;
69. }

71. public getData(index: number): string {
72. return this.dataArray[index];
73. }

75. public addData(index: number, data: string): void {
76. this.dataArray.splice(index, 0, data);
77. this.notifyDataAdd(index);
78. }

80. public pushData(data: string): void {
81. this.dataArray.push(data);
82. this.notifyDataAdd(this.dataArray.length - 1);
83. }
84. }

86. @Entry
87. @Component
88. struct LazyforEachTest {
89. private data: MyDataSource = new MyDataSource();
90. @State @Watch('onMessageUpdated') message: number = 0;

92. onMessageUpdated() {
93. hilog.info(DOMAIN, TAG, `LazyforEach message callback func ${this.message}`);
94. }

96. aboutToAppear() {
97. for (let i = 0; i <= 20; i++) {
98. this.data.pushData(`Hello ${i}`);
99. }
100. }

102. build() {
103. Column() {
104. Button('change message').onClick(() => {
105. this.message++;
106. })
107. List({ space: 3 }) {
108. LazyForEach(this.data, (item: string) => {
109. ListItem() {
110. FreezeChild({ message: this.message, index: item })
111. }
112. }, (item: string) => item)
113. }.cachedCount(5).height(500)
114. }
115. }
116. }

118. @Component({ freezeWhenInactive: true })
119. struct FreezeChild {
120. @Link @Watch('onMessageUpdated') message: number;
121. index: string = '';

123. aboutToAppear() {
124. hilog.info(DOMAIN, TAG, `FreezeChild aboutToAppear index: ${this.index}`);
125. }

127. onMessageUpdated() {
128. hilog.info(DOMAIN, TAG, `FreezeChild message callback func ${this.message}, index: ${this.index}`);
129. }

131. build() {
132. Text('message' + `${this.message}, index: ${this.index}`)
133. .width('90%')
134. .height(160)
135. .backgroundColor(0xAFEEEE)
136. .textAlign(TextAlign.Center)
137. .fontSize(30)
138. .fontWeight(FontWeight.Bold)
139. }
140. }
```

[LazyforEachTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/LazyforEachTest.ets#L15-L156)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的ListItem中的子组件@Watch注册的方法onMessageUpdated被触发。缓存节点中@Watch注册的方法不会被触发。（如果不加组件冻结，当前正在显示的ListItem和cachecount缓存节点中@Watch注册的方法onMessageUpdated都会被触发。）

2.List区域外的ListItem滑动到List区域内，状态由inactive变为active，对应的@Watch注册的方法onMessageUpdated被触发。

3.再次点击change message更改message的值，仅有当前显示的ListItem中的子组件@Watch注册的方法onMessageUpdated被触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/aRJFbjymT7S7JykmBJoGcg/zh-cn_image_0000002558604396.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=8B2FF84B1F22A8B0B3A138D5D95338300AD04B284D7FDC65CADEE23DFAC866D4)

### Navigation

当NavDestination不可见时，会将其子自定义组件设置成非激活态，修改状态变量不会触发冻结组件的刷新。当返回该页面时，其子自定义组件重新恢复成激活态，触发@Watch回调进行刷新。

在下面例子中，NavigationContentMsgStack会被设置成非激活态，将不再响应状态变量的变化，也不会触发组件刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';
4. const PAGE_ONE_INDEX = 1;
5. const PAGE_TWO_INDEX = 2;
6. const PAGE_THREE_INDEX = 3;

8. @Entry
9. @Component
10. struct MyNavigationTestStack {
11. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
12. @State @Watch('info') message: number = 0;
13. @State logNumber: number = 0;

15. info() {
16. hilog.info(DOMAIN, TAG, `freeze-test MyNavigation message callback ${this.message}`);
17. }

19. @Builder
20. PageMap(name: string) {
21. if (name === 'pageOne') {
22. PageOneStack({ message: this.message, logNumber: this.logNumber })
23. } else if (name === 'pageTwo') {
24. PageTwoStack({ message: this.message, logNumber: this.logNumber })
25. } else if (name === 'pageThree') {
26. PageThreeStack({ message: this.message, logNumber: this.logNumber })
27. }
28. }

30. build() {
31. Column() {
32. Button('change message')
33. .onClick(() => {
34. this.message++;
35. })
36. Navigation(this.pageInfo) {
37. Column() {
38. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
39. .width('80%')
40. .height(40)
41. .margin(20)
42. .onClick(() => {
43. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
44. })
45. }
46. }.title('NavIndex')
47. .navDestination(this.PageMap)
48. .mode(NavigationMode.Stack)
49. }
50. }
51. }

53. @Component
54. struct PageOneStack {
55. @Consume('pageInfo') pageInfo: NavPathStack;
56. @State index: number = PAGE_ONE_INDEX;
57. @Link message: number;
58. @Link logNumber: number;

60. build() {
61. NavDestination() {
62. Column() {
63. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
64. Text('cur stack size:' + `${this.pageInfo.size()}`)
65. .fontSize(30)
66. .fontWeight(FontWeight.Bold)
67. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
68. .width('80%')
69. .height(40)
70. .margin(20)
71. .onClick(() => {
72. this.pageInfo.pushPathByName('pageTwo', null);
73. })
74. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
75. .width('80%')
76. .height(40)
77. .margin(20)
78. .onClick(() => {
79. this.pageInfo.pop();
80. })
81. }.width('100%').height('100%')
82. }.title('pageOne')
83. .onBackPressed(() => {
84. this.pageInfo.pop();
85. return true;
86. })
87. }
88. }

90. @Component
91. struct PageTwoStack {
92. @Consume('pageInfo') pageInfo: NavPathStack;
93. @State index: number = PAGE_TWO_INDEX;
94. @Link message: number;
95. @Link logNumber: number;

97. build() {
98. NavDestination() {
99. Column() {
100. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
101. Text('cur stack size:' + `${this.pageInfo.size()}`)
102. .fontSize(30)
103. .fontWeight(FontWeight.Bold)
104. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
105. .width('80%')
106. .height(40)
107. .margin(20)
108. .onClick(() => {
109. this.pageInfo.pushPathByName('pageThree', null);
110. })
111. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
112. .width('80%')
113. .height(40)
114. .margin(20)
115. .onClick(() => {
116. this.pageInfo.pop();
117. })
118. }.width('100%').height('100%')
119. }.title('pageTwo')
120. .onBackPressed(() => {
121. this.pageInfo.pop();
122. return true;
123. })
124. }
125. }

127. @Component
128. struct PageThreeStack {
129. @Consume('pageInfo') pageInfo: NavPathStack;
130. @State index: number = PAGE_THREE_INDEX;
131. @Link message: number;
132. @Link logNumber: number;

134. build() {
135. NavDestination() {
136. Column() {
137. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
138. Text('cur stack size:' + `${this.pageInfo.size()}`)
139. .fontSize(30)
140. .fontWeight(FontWeight.Bold)
141. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
142. .width('80%')
143. .height(40)
144. .margin(20)
145. .onClick(() => {
146. this.pageInfo.pushPathByName('pageOne', null);
147. })
148. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
149. .width('80%')
150. .height(40)
151. .margin(20)
152. .onClick(() => {
153. this.pageInfo.pop();
154. })
155. }.width('100%').height('100%')
156. }.title('pageThree')
157. .onBackPressed(() => {
158. this.pageInfo.pop();
159. return true;
160. })
161. }
162. }

164. @Component({ freezeWhenInactive: true })
165. struct NavigationContentMsgStack {
166. @Link @Watch('info') message: number;
167. @Link index: number;
168. @Link logNumber: number;

170. info() {
171. hilog.info(DOMAIN, TAG, `freeze-test NavigationContent message callback ${this.message}`);
172. hilog.info(DOMAIN, TAG, `freeze-test ---- called by content ${this.index}`);
173. this.logNumber++;
174. }

176. build() {
177. Column() {
178. Text('msg:' + `${this.message}`)
179. .fontSize(30)
180. .fontWeight(FontWeight.Bold)
181. Text('log number:' + `${this.logNumber}`)
182. .fontSize(30)
183. .fontWeight(FontWeight.Bold)
184. }
185. }
186. }
```

[MyNavigationTestStack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/MyNavigationTestStack.ets#L15-L202)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的MyNavigationTestStack组件中的@Watch注册的方法info被触发。

2.点击Next Page切换到PageOne，创建PageOneStack节点。

3.再次点击change message更改message的值，仅PageOneStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

4.再次点击Next Page切换到PageTwo，创建PageTwoStack节点。

5.再次点击change message更改message的值，仅PageTwoStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

6.再次点击Next Page切换到PageThree，创建PageThreeStack节点。

7.再次点击change message更改message的值，仅PageThreeStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

8.点击Back Page回到PageTwo，此时，仅PageTwoStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

9.再次点击Back Page回到PageOne，此时，仅PageOneStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

10.再次点击Back Page回到初始页，此时，无任何触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/93P70NK4RMayAKcUu2rytQ/zh-cn_image_0000002589323921.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=816321AA8489C14C9167A6B394F46E837DFC9D5D4A15358F542DEFB780C400E6)

### 组件复用

[组件复用](arkts-reusable.md)通过重利用缓存池中已存在的节点，而非创建新节点，来优化UI性能并提升应用流畅度。复用池中的节点尽管未在UI组件树上展示，但是状态变量的更改仍会触发UI刷新。为了解决复用池中组件异常刷新问题，可以使用组件冻结避免复用池中的组件刷新。

**组件复用、if和组件冻结混用场景**

下面是组件复用、if组件和组件冻结混合使用场景的例子，if组件绑定的状态变量变化成false时，触发子组件ChildComponent的下树，由于ChildComponent被标记了组件复用，所以不会被销毁，而是进入复用池，这个时候如果同时开启了组件冻结，则可以使在复用池里不再刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. @Reusable
6. @Component({ freezeWhenInactive: true })
7. struct ChildComponent {
8. @Link @Watch('descChange') desc: string;
9. @State count: number = 0;

11. descChange() {
12. hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
13. }

15. aboutToReuse(params: Record<string, ESObject>): void {
16. this.count = params.count as number;
17. }

19. aboutToRecycle(): void {
20. // 输出recycled提示，确认组件进入复用池
21. hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
22. }

24. build() {
25. Column() {
26. Text(`ChildComponent desc: ${this.desc}`)
27. .fontSize(20)
28. Text(`ChildComponent count ${this.count}`)
29. .fontSize(20)
30. }.border({ width: 2, color: Color.Pink })
31. }
32. }

34. @Entry
35. @Component
36. struct Page {
37. @State desc: string = 'Hello World';
38. @State flag: boolean = true;
39. @State count: number = 0;

41. build() {
42. Column() {
43. Button(`change desc`).onClick(() => {
44. this.desc += '!';
45. })
46. Button(`change flag`).onClick(() => {
47. this.count++;
48. this.flag = !this.flag;
49. })
50. if (this.flag) {
51. ChildComponent({ desc: this.desc, count: this.count })
52. }
53. }
54. .height('100%')
55. }
56. }
```

[ComponentReuse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/ComponentReuse.ets#L16-L72)

在上面的示例中：

1. 点击change flag，改变flag为false：
   * 被标记@Reusable的ChildComponent组件在下树时，不会被销毁，而是进入复用池，触发aboutToRecycle生命周期，同时设置状态为inactive。
   * ChildComponent同时也开启了组件冻结，当其状态为inactive时，不会响应任何状态变量变化带来的UI刷新。
2. 点击change desc，触发Page的成员变量desc的变化：
   * desc是@State装饰的，其变化会通知给其子组件ChildComponent[@Link](arkts-link.md)装饰的desc。
   * 但因为ChildComponent是inactive状态，且开启了组件冻结，所以这次变化并不会触发@Watch('descChange')的回调和ChildComponentUI刷新。如果没有开启组件冻结，当前@Watch('descChange')会立即回调，且复用池内的ChildComponent组件也会对应刷新。
3. 再次点击change flag，改变flag为true：
   * ChildComponent从复用池中重新加入到组件树上。
   * 回调aboutToReuse生命周期，将当前最新的count值同步给子组件。desc是通过[@State](arkts-state.md)到@Link同步的，所以无需开发者手动在aboutToReuse中赋值。
   * 设置ChildComponent为active状态，并且刷新在inactive时没有刷新的组件，在当前例子中，就是Text(ChildComponent desc: ${this.desc})。

**LazyForEach、组件复用和组件冻结混用场景**

在数据很多的长列表滑动场景下，开发者会使用LazyForEach来按需创建组件，同时配合组件复用降低在滑动过程中因创建和销毁组件带来的开销。但是开发者如果根据其复用类型不同，设置了[reuseId](../harmonyos-references/ts-universal-attributes-reuse-id.md#reuseid)，或者为了保证滑动性能设置了较大的cacheCount，这就可能使复用池或者LazyForEach缓存较多的节点。在这种情况下，如果开发者触发List下所有子节点的刷新，就会带来节点刷新数量过多的问题，这个时候，可以考虑搭配组件冻结使用。

```
1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. // 用于处理数据监听的IDataSource的基本实现
6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: string[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): string {
15. return this.originDataArray[index];
16. }

18. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
19. registerDataChangeListener(listener: DataChangeListener): void {
20. if (this.listeners.indexOf(listener) < 0) {
21. hilog.info(DOMAIN, TAG, 'add listener');
22. this.listeners.push(listener);
23. }
24. }

26. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. hilog.info(DOMAIN, TAG, 'remove listener');
31. this.listeners.splice(pos, 1);
32. }
33. }

35. // 通知LazyForEach组件需要重载所有子组件
36. notifyDataReload(): void {
37. this.listeners.forEach(listener => {
38. listener.onDataReloaded();
39. });
40. }

42. // 通知LazyForEach组件需要在index对应索引处添加子组件
43. notifyDataAdd(index: number): void {
44. this.listeners.forEach(listener => {
45. listener.onDataAdd(index);
46. });
47. }

49. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
50. notifyDataChange(index: number): void {
51. this.listeners.forEach(listener => {
52. listener.onDataChange(index);
53. });
54. }

56. // 通知LazyForEach组件需要在index对应索引处删除该子组件
57. notifyDataDelete(index: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataDelete(index);
60. });
61. }

63. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
64. notifyDataMove(from: number, to: number): void {
65. this.listeners.forEach(listener => {
66. listener.onDataMove(from, to);
67. });
68. }
69. }

71. class MyDataSource extends BasicDataSource {
72. private dataArray: string[] = [];

74. public totalCount(): number {
75. return this.dataArray.length;
76. }

78. public getData(index: number): string {
79. return this.dataArray[index];
80. }

82. public addData(index: number, data: string): void {
83. this.dataArray.splice(index, 0, data);
84. this.notifyDataAdd(index);
85. }

87. public pushData(data: string): void {
88. this.dataArray.push(data);
89. this.notifyDataAdd(this.dataArray.length - 1);
90. }
91. }

93. @Reusable
94. @Component({freezeWhenInactive: true})
95. struct ChildComponent {
96. @Link @Watch('descChange') desc: string;
97. @State item: string = '';
98. @State index: number = 0;

100. descChange() {
101. hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
102. }

104. aboutToReuse(params: Record<string, ESObject>): void {
105. this.item = params.item;
106. this.index = params.index;
107. }

109. aboutToRecycle(): void {
110. hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
111. }

113. build() {
114. Column() {
115. Text(`ChildComponent index: ${this.index} item: ${this.item}`)
116. .fontSize(20)
117. Text(`desc: ${this.desc}`)
118. .fontSize(20)
119. }.border({width: 2, color: Color.Pink})
120. }
121. }

123. @Entry
124. @Component
125. struct Page {
126. @State desc: string = 'Hello World';
127. private data: MyDataSource = new MyDataSource();

129. aboutToAppear() {
130. for (let i = 0; i < 50; i++) {
131. this.data.pushData(`Hello ${i}`);
132. }
133. }

135. build() {
136. Column() {
137. Button(`change desc`).onClick(() => {
138. hiTraceMeter.startTrace('change desc', 1);
139. this.desc += '!';
140. hiTraceMeter.finishTrace('change desc', 1);
141. })
142. List({ space: 3 }) {
143. LazyForEach(this.data, (item: string, index: number) => {
144. ListItem() {
145. ChildComponent({index: index, item: item, desc: this.desc}).reuseId(index % 10 < 5 ? '1': '0')
146. }
147. }, (item: string) => item)
148. }.cachedCount(5)
149. }
150. .height('100%')
151. }
152. }
```

[ComponentReuse1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/ComponentReuse1.ets#L15-L168)

在上面的示例中：

1. 滑动到index为14的位置，当前屏幕上可见区域内有15个ChildComponent。
2. 在滑动过程中：
   * 列表上端的ChildComponent滑出可视区域外，此时先进入LazyForEach的缓存区域内，被设置inactive。在滑出LazyForEach缓存区域外后，因为标记了组件复用，所以并不会被析构，而是会进入复用池，此时再次被设置inactive。
   * 列表下端LazyForEach的缓存节点会进入List范围内，此时会试图请求创建新的节点进入LazyForEach的缓存，发现有可复用的节点时，从复用池中拿出已有节点，触发aboutToReuse生命周期回调，此时因为节点进入的是LazyForEach的缓存区域，所以其状态依旧是inactive。
3. 点击change desc，触发Page的成员变量desc的变化：
   * desc是@State装饰的，其变化会通知给其子组件ChildComponent@Link装饰的desc。
   * 非可视区域内的ChildComponent是inactive状态，且开启了组件冻结，所以这次变化只触发可视区域内的15个节点的@Watch('descChange')回调，并只刷新对应可视区域内的15个节点。LazyForEach和复用池中的节点并不会刷新，也不会触发@Watch回调。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/lF3o7XNlTTiC2n58lWy6bw/zh-cn_image_0000002589243861.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=326184DBF2159562F1889D5D2E6E722560BFC4BBC64555B40E4C406311520E66)

可通过trace观察，仅触发了15个ChildComponent节点的刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/dkAgkjQJQOG-R0OAysq9oA/zh-cn_image_0000002558764054.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=E7315041C1DE5C1F9D1E4B869B622BB839ED209081332F112BA4E207C5C57A72)

**LazyForEach、if、组件复用和组件冻结混用场景**

下面的场景中展示了LazyForEach、if、组件复用和组件冻结混用场景。在同一个父自定义组件下，可复用的节点可能通过不同的方式进入复用池，比如：

* 通过滑动从LazyForEach的缓存区域下树，进入复用池。
* if条件切换通知子节点下树，进入复用池。

```
1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. class BasicDataSource implements IDataSource {
6. private listeners: DataChangeListener[] = [];
7. private originDataArray: string[] = [];

9. public totalCount(): number {
10. return 0;
11. }

13. public getData(index: number): string {
14. return this.originDataArray[index];
15. }

17. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. hilog.info(DOMAIN, TAG, 'add listener');
21. this.listeners.push(listener);
22. }
23. }

25. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
26. unregisterDataChangeListener(listener: DataChangeListener): void {
27. const pos = this.listeners.indexOf(listener);
28. if (pos >= 0) {
29. hilog.info(DOMAIN, TAG, 'remove listener');
30. this.listeners.splice(pos, 1);
31. }
32. }

34. // 通知LazyForEach组件需要重载所有子组件
35. notifyDataReload(): void {
36. this.listeners.forEach(listener => {
37. listener.onDataReloaded();
38. });
39. }

41. // 通知LazyForEach组件需要在index对应索引处添加子组件
42. notifyDataAdd(index: number): void {
43. this.listeners.forEach(listener => {
44. listener.onDataAdd(index);
45. });
46. }

48. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
49. notifyDataChange(index: number): void {
50. this.listeners.forEach(listener => {
51. listener.onDataChange(index);
52. });
53. }

55. // 通知LazyForEach组件需要在index对应索引处删除该子组件
56. notifyDataDelete(index: number): void {
57. this.listeners.forEach(listener => {
58. listener.onDataDelete(index);
59. });
60. }

62. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
63. notifyDataMove(from: number, to: number): void {
64. this.listeners.forEach(listener => {
65. listener.onDataMove(from, to);
66. });
67. }
68. }

70. class MyDataSource extends BasicDataSource {
71. private dataArray: string[] = [];

73. public totalCount(): number {
74. return this.dataArray.length;
75. }

77. public getData(index: number): string {
78. return this.dataArray[index];
79. }

81. public addData(index: number, data: string): void {
82. this.dataArray.splice(index, 0, data);
83. this.notifyDataAdd(index);
84. }

86. public pushData(data: string): void {
87. this.dataArray.push(data);
88. this.notifyDataAdd(this.dataArray.length - 1);
89. }
90. }

92. @Reusable
93. @Component({ freezeWhenInactive: true })
94. struct ChildComponent {
95. @Link @Watch('descChange') desc: string;
96. @State item: string = '';
97. @State index: number = 0;

99. descChange() {
100. hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
101. }

103. aboutToReuse(params: Record<string, ESObject>): void {
104. this.item = params.item;
105. this.index = params.index;
106. }

108. aboutToRecycle(): void {
109. hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
110. }

112. build() {
113. Column() {
114. Text(`ChildComponent index: ${this.index} item: ${this.item}`)
115. .fontSize(20)
116. Text(`desc: ${this.desc}`)
117. .fontSize(20)
118. }.border({ width: 2, color: Color.Pink })
119. }
120. }

122. @Entry
123. @Component
124. struct Page {
125. @State desc: string = 'Hello World';
126. @State flag: boolean = true;
127. private data: MyDataSource = new MyDataSource();

129. aboutToAppear() {
130. for (let i = 0; i < 50; i++) {
131. this.data.pushData(`Hello ${i}`);
132. }
133. }

135. build() {
136. Column() {
137. Button(`change desc`).onClick(() => {
138. hiTraceMeter.startTrace('change desc', 1);
139. this.desc += '!';
140. hiTraceMeter.finishTrace('change desc', 1);
141. })
142. Button(`change flag`).onClick(() => {
143. hiTraceMeter.startTrace('change flag', 1);
144. this.flag = !this.flag;
145. hiTraceMeter.finishTrace('change flag', 1);
146. })
147. List({ space: 3 }) {
148. LazyForEach(this.data, (item: string, index: number) => {
149. ListItem() {
150. ChildComponent({ index: index, item: item, desc: this.desc }).reuseId(index % 10 < 5 ? '1' : '0')
151. }
152. }, (item: string) => item)
153. }
154. .cachedCount(5)
155. .height('60%')
156. if (this.flag) {
157. ChildComponent({ index: -1, item: 'Hello', desc: this.desc }).reuseId('1')
158. }
159. }
160. .height('100%')
161. }
162. }
```

在上面的示例中：

1. 当滑动到index为14的位置，屏幕上可见区域内有10个ChildComponent，9个是LazyForEach的子节点，1个是if的子节点。
2. 点击change flag，if的条件变成false，其子节点ChildComponent进入复用池。当前屏幕显示9个节点。
3. 此时不管是通过LazyForEach还是if下树的节点都会进入Page节点下的复用池。
4. 点击change desc，仅更新屏幕上的9个ChildComponent节点，具体可参考下面的trace。
5. 再次点击change flag，if的条件变成true，ChildComponent从复用池中重新加入到组件树上，其状态变成active。
6. 再次点击change desc，从复用池中通过if和LazyForEach上树的节点都可正常刷新。

开启组件冻结trace：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/1XaqHrVDSz-s3V3eZQJxKg/zh-cn_image_0000002558604398.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=42DEE031FA1B4C82015C39FF24C870C95AC100A7CC3C416D431BC32319AAE04C)

没有开启组件冻结trace：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/vftocfA2Q5ek4mGjNPqoAg/zh-cn_image_0000002589323923.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=E20DBD549305B5240C2FEADDDEE5C785AE9002BC403D2943630C33C0A0C2508D)

### 组件混用

当支持组件冻结的场景彼此之间组合使用时，对于不同的API版本，冻结行为会有不同。给父组件设置组件冻结标志，在API version 17及以下，当父组件解冻时，会解冻自己子组件所有的节点；从API version 18开始，父组件解冻时，只会解冻子组件的屏上节点。

**Navigation和TabContent的混用**

代码示例如下：

```
1. // index.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. const DOMAIN = 0x0001;
4. const TAG = 'FreezeChild';
5. const TAB_STATE_INITIAL_VALUE = 47;

7. @Component
8. struct ChildOfParamComponent {
9. @Prop @Watch('onChange') childVal: number;

11. onChange() {
12. hilog.info(DOMAIN, TAG, `Appmonitor ChildOfParamComponent: childVal changed:${this.childVal}`);
13. }

15. build() {
16. Column() {
17. Text(`Child Param: ${this.childVal}`)
18. }
19. }
20. }

22. @Component
23. struct ParamComponent {
24. @Prop @Watch('onChange') paramVal: number;

26. onChange() {
27. hilog.info(DOMAIN, TAG, `Appmonitor ParamComponent: paramVal changed:${this.paramVal}`);
28. }

30. build() {
31. Column() {
32. Text(`val: ${this.paramVal}`)
33. ChildOfParamComponent({ childVal: this.paramVal })
34. }
35. }
36. }

38. @Component
39. struct DelayComponent {
40. @Prop @Watch('onChange') delayVal: number;

42. onChange() {
43. hilog.info(DOMAIN, TAG, `Appmonitor ParamComponent: delayVal changed:${this.delayVal}`);
44. }

46. build() {
47. Column() {
48. Text(`Delay Param: ${this.delayVal}`)
49. }
50. }
51. }

53. @Component({ freezeWhenInactive: true })
54. struct TabsComponent {
55. private controller: TabsController = new TabsController();
56. @State @Watch('onChange') tabState: number = TAB_STATE_INITIAL_VALUE;

58. onChange() {
59. hilog.info(DOMAIN, TAG, `Appmonitor TabsComponent: tabState changed:${this.tabState}`);
60. }

62. build() {
63. Column({ space: 10 }) {
64. Button(`Incr state ${this.tabState}`)
65. .fontSize(25)
66. .onClick(() => {
67. hilog.info(DOMAIN, TAG, 'Button increment state value');
68. this.tabState = this.tabState + 1;
69. })
70. Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {
71. TabContent() {
72. ParamComponent({ paramVal: this.tabState })
73. }.tabBar('Update')
74. TabContent() {
75. DelayComponent({ delayVal: this.tabState })
76. }.tabBar('DelayUpdate')
77. }
78. .vertical(false)
79. .scrollable(true)
80. .barMode(BarMode.Fixed)
81. .barWidth(400)
82. .barHeight(150)
83. .animationDuration(400)
84. .width('100%')
85. .height(200)
86. .backgroundColor(0xF5F5F5)
87. }
88. }
89. }

91. @Entry
92. @Component
93. struct MyNavigationTestStack {
94. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();

96. @Builder
97. PageMap(name: string) {
98. if (name === 'pageOne') {
99. PageOneStack()
100. } else if (name === 'pageTwo') {
101. PageTwoStack()
102. }
103. }

105. build() {
106. Column() {
107. Navigation(this.pageInfo) {
108. Column() {
109. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
110. .width('80%')
111. .height(40)
112. .margin(20)
113. .onClick(() => {
114. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
115. })
116. }
117. }.title('NavIndex')
118. .navDestination(this.PageMap)
119. .mode(NavigationMode.Stack)
120. }
121. }
122. }

124. @Component
125. struct PageOneStack {
126. @Consume('pageInfo') pageInfo: NavPathStack;

128. build() {
129. NavDestination() {
130. Column() {
131. TabsComponent()
132. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
133. .width('80%')
134. .height(40)
135. .margin(20)
136. .onClick(() => {
137. this.pageInfo.pushPathByName('pageTwo', null);
138. })
139. }.width('100%').height('100%')
140. }.title('pageOne')
141. .onBackPressed(() => {
142. this.pageInfo.pop();
143. return true;
144. })
145. }
146. }

148. @Component
149. struct PageTwoStack {
150. @Consume('pageInfo') pageInfo: NavPathStack;

152. build() {
153. NavDestination() {
154. Column() {
155. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
156. .width('80%')
157. .height(40)
158. .margin(20)
159. .onClick(() => {
160. this.pageInfo.pop();
161. })
162. }.width('100%').height('100%')
163. }.title('pageTwo')
164. .onBackPressed(() => {
165. this.pageInfo.pop();
166. return true;
167. })
168. }
169. }
```

[ComponentMixing.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/ComponentMixing.ets#L15-L185)

代码运行结果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/FndiwL28Tm-7V44baIf39g/zh-cn_image_0000002589243863.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=96C2D919B8F48F89AD7DBDC3255F972C470D6A98ADA8B5105D47C0D2CDBBD84D)

点击Next Page，进入pageOne页面，页面中存在两个tab标签，默认在Update标签，开启组件冻结功能，Tabcontent的标签如果未被选中，状态变量不会刷新，如以下操作。

点击Incr state，日志中查询Appmonitor，存在3个打印。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Ateol8r4SIS_wQZ-AUYFnA/zh-cn_image_0000002558764056.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=AFEA250E348A2721BA0538D4EDFB073831F0FCD66FF284654D43694D7176FB63)

切换到DelayUpdate标签，点击Incr state，日志中查询Appmonitor，存在2个打印。DelayUpdate中状态变量不会刷新与Update标签中相关的状态变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/fqQTGNyGRyaRKJoeKeOLNA/zh-cn_image_0000002558604400.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=F82ECBF1301CEFECD0716B427EAD64C3C6E81D60D9E1207926329BB65C48D3F6)

在API version 17及以下：

点击Next page进入下一个页面并返回，标签默认在DelayUpdate，再次点击Incr state，日志中查询Appmonitor，存在4个打印，页面路由返回时，会解冻Tabcontent所有的标签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/pyS6f7coQ9eRxM0cZ6EbBg/zh-cn_image_0000002589323925.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=5E083032ACEF961962810D923830C2EDC5356C6EF92A17D736AAB6E9B6AD6EF5)

在API version 18及以上：

点击Next page进入下一个页面并返回，标签默认在DelayUpdate，再次点击Incr state，日志中查询Appmonitor，存在2个打印，页面路由返回时，只会解冻对应标签的节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/g-ooUnA7S6KZFsW-O0LJPw/zh-cn_image_0000002589243865.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=0E5EB54F0C1F67D1CA3E71975033C26514111C2DE8C2C07C7987D43D640DCAEF)

**页面和LazyForEach**

Navigation和TabContent混用时，之所以会解锁TabContent标签的子节点，是因为回到前一个页面时会从父组件开始递归解冻子组件，与此行为类似的还有页面生命周期：OnPageShow。OnPageShow会将当前Page中的根节点设置为active状态，TabContent作为页面的子节点，也会被设置为active状态。在屏幕灭屏和屏幕亮屏时会分别触发页面的生命周期：OnPageHide和OnPageShow，因此页面中使用LazyForEach时，手动灭屏和亮屏也能实现页面路由一样的效果，如以下示例代码：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0x0001;
3. const TAG = 'FreezeChild';

5. // 用于处理数据监听的IDataSource的基本实现
6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: string[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): string {
15. return this.originDataArray[index];
16. }

18. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
19. registerDataChangeListener(listener: DataChangeListener): void {
20. if (this.listeners.indexOf(listener) < 0) {
21. hilog.info(DOMAIN, TAG, 'add listener');
22. this.listeners.push(listener);
23. }
24. }

26. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
27. unregisterDataChangeListener(listener: DataChangeListener): void {
28. const pos = this.listeners.indexOf(listener);
29. if (pos >= 0) {
30. hilog.info(DOMAIN, TAG, 'remove listener');
31. this.listeners.splice(pos, 1);
32. }
33. }

35. // 通知LazyForEach组件需要重载所有子组件
36. notifyDataReload(): void {
37. this.listeners.forEach(listener => {
38. listener.onDataReloaded();
39. });
40. }

42. // 通知LazyForEach组件需要在index对应索引处添加子组件
43. notifyDataAdd(index: number): void {
44. this.listeners.forEach(listener => {
45. listener.onDataAdd(index);
46. });
47. }

49. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
50. notifyDataChange(index: number): void {
51. this.listeners.forEach(listener => {
52. listener.onDataChange(index);
53. });
54. }

56. // 通知LazyForEach组件需要在index对应索引处删除该子组件
57. notifyDataDelete(index: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataDelete(index);
60. });
61. }

63. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
64. notifyDataMove(from: number, to: number): void {
65. this.listeners.forEach(listener => {
66. listener.onDataMove(from, to);
67. });
68. }
69. }

71. class MyDataSource extends BasicDataSource {
72. private dataArray: string[] = [];

74. public totalCount(): number {
75. return this.dataArray.length;
76. }

78. public getData(index: number): string {
79. return this.dataArray[index];
80. }

82. public addData(index: number, data: string): void {
83. this.dataArray.splice(index, 0, data);
84. this.notifyDataAdd(index);
85. }

87. public pushData(data: string): void {
88. this.dataArray.push(data);
89. this.notifyDataAdd(this.dataArray.length - 1);
90. }
91. }

93. @Reusable
94. @Component({ freezeWhenInactive: true })
95. struct ChildComponent {
96. @State desc: string = '';
97. @Link @Watch('sumChange') sum: number;

99. sumChange() {
100. hilog.info(DOMAIN, TAG, `sum: Change ${this.sum}`);
101. }

103. aboutToReuse(params: Record<string, Object>): void {
104. this.desc = params.desc as string;
105. this.sum = params.sum as number;
106. }

108. aboutToRecycle(): void {
109. hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
110. }

112. build() {
113. Column() {
114. Divider()
115. .color('#ff11acb8')
116. Text(`subcomponent: ${this.desc}`)
117. .fontSize(30)
118. .fontWeight(30)
119. Text(`${this.sum}`)
120. .fontSize(30)
121. .fontWeight(30)
122. }
123. }
124. }

126. @Entry
127. @Component({ freezeWhenInactive: true })
128. struct Page {
129. private data: MyDataSource = new MyDataSource();
130. @State sum: number = 0;
131. @State desc: string = '';

133. aboutToAppear() {
134. for (let index = 0; index < 20; index++) {
135. this.data.pushData(index.toString());
136. }
137. }

139. build() {
140. Column() {
141. Button(`add sum`).onClick(() => {
142. this.sum++;
143. })
144. .fontSize(30)
145. .margin(20)
146. List() {
147. LazyForEach(this.data, (item: string) => {
148. ListItem() {
149. ChildComponent({ desc: item, sum: this.sum })
150. }
151. .width('100%')
152. .height(100)
153. }, (item: string) => item)
154. }.cachedCount(5)
155. }
156. .height('100%')
157. .width('100%')
158. }
159. }
```

[ComponentMixing1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/ComponentMixing1.ets#L15-L175)

在组件复用场景中，已经对LazyForEach的节点进行了详细说明，分为屏上节点和cachedCount节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/sdlqKNcXSPyMLsESQXpWFw/zh-cn_image_0000002558764058.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=8ABAFF0335C43CDC62CFD749D94D6E33606AAF8EF988AEDE150B7C8684FF1400)

向下滑动LazyForEach，让cachedCount补充节点，点击add sum，搜索打印日志：sum: Change，出现了8条打印。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SS_zmiU-T_OpTnCrUVBzLQ/zh-cn_image_0000002558604402.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=519BA3F9A3852D7CFAF61942D3370566EB05BA53469090E5BF7787504B246C0A)

在API version 17及以下：

灭屏之后亮屏，触发OnPageShow，点击add sum，打印数量为屏上节点与cachedCount数量的总和。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/hc4ao1JkQuKO0ARJ55BaSg/zh-cn_image_0000002589323927.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=92020E5B6FD12A0E21BC116AB330B75524EBCEB5E9E6DF2CCA8E91073BFE303E)

从API version 18开始：

灭屏之后亮屏，触发OnPageShow，点击add sum，只会打印屏上节点数量，不会再解冻cachedCount中的节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/T2Zj6zBxTnCANbnxX3Wj3g/zh-cn_image_0000002589243867.png?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=F13D5506E50CEA89153A7D9F7E3EBCB52CE43DC56DAE43C636F75923E4F62681)

## 限制条件

### BuilderNode无法继承父组件冻结

在API version 20之前，BuilderNode无法继承父组件冻结。如下面的例子所示，FreezeBuildNode中使用了自定义节点[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)。BuilderNode可以通过命令式动态挂载组件，而组件冻结又是强依赖父子关系来通知是否开启组件冻结。如果父组件使用组件冻结，且组件树的中间层级上又启用了BuilderNode，则BuilderNode的子组件将无法被冻结。

在API version 20及以后，开发者可以通过配置BuilderNode的inheritFreezeOptions接口为true，实现BuilderNode继承冻结的能力。具体示例见[BuilderNode对象继承组件冻结](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. const DOMAIN = 0x0001;
4. const TAG = 'FreezeChild';

6. // 定义一个Params类，用于传递参数
7. class Params {
8. public index: number = 0;

10. constructor(index: number) {
11. this.index = index;
12. }
13. }

15. // 定义一个BuildNodeChild组件，它包含一个message属性和一个index属性
16. @Component
17. struct BuildNodeChild {
18. @StorageProp('buildNodeTest') @Watch('onMessageUpdated') message: string = 'hello world';
19. @State index: number = 0;

21. // 当message更新时，调用此方法
22. onMessageUpdated() {
23. hilog.info(DOMAIN, TAG, `FreezeBuildNode builderNodeChild message callback func ${this.message},index:${this.index}`);
24. }

26. build() {
27. Text(`buildNode Child message: ${this.message}`).fontSize(30)
28. }
29. }

31. // 定义一个buildText函数，它接收一个Params参数并构建一个Column组件
32. @Builder
33. function buildText(params: Params) {
34. Column() {
35. BuildNodeChild({ index: params.index })
36. }
37. }

39. // 定义一个TextNodeController类，继承自NodeController
40. class TextNodeController extends NodeController {
41. private textNode: BuilderNode<[Params]> | null = null;
42. private index: number = 0;

44. // 构造函数接收一个index参数
45. constructor(index: number) {
46. super();
47. this.index = index;
48. }

50. // 创建并返回一个FrameNode
51. makeNode(context: UIContext): FrameNode | null {
52. this.textNode = new BuilderNode(context);
53. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.index));
54. return this.textNode.getFrameNode();
55. }
56. }

58. // 定义一个Index组件，它包含一个message属性和一个data数组
59. @Entry
60. @Component
61. struct Index {
62. @StorageLink('buildNodeTest') message: string = 'hello';
63. private data: number[] = [0, 1];

65. build() {
66. Row() {
67. Column() {
68. Button('change').fontSize(30)
69. .onClick(() => {
70. this.message += 'a';
71. })
72. Tabs() {
73. ForEach(this.data, (item: number) => {
74. TabContent() {
75. FreezeBuildNode({ index: item })
76. }.tabBar(`tab${item}`)
77. }, (item: number) => item.toString())
78. }
79. }
80. }
81. .width('100%')
82. .height('100%')
83. }
84. }

86. // 定义一个FreezeBuildNode组件，它包含一个message属性和一个index属性
87. @Component({ freezeWhenInactive: true })
88. struct FreezeBuildNode {
89. @StorageProp('buildNodeTest') @Watch('onMessageUpdated') message: string = '1111';
90. @State index: number = 0;

92. // 当message更新时，调用此方法
93. onMessageUpdated() {
94. hilog.info(DOMAIN, TAG, `FreezeBuildNode message callback func ${this.message}, index: ${this.index}`);
95. }

97. build() {
98. NodeContainer(new TextNodeController(this.index))
99. .width('100%')
100. .height('100%')
101. .backgroundColor('#FFF0F0F0')
102. }
103. }
```

[Constraints.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsFreeze/entry/src/main/ets/View/Constraints.ets#L15-L119)

在上面的示例中：

点击change，改变message的值，当前正在显示的TabContent组件中@Watch注册的方法onMessageUpdated被触发。未显示的TabContent中的BuilderNode节点下组件的@Watch方法onMessageUpdated也被触发，并没有被冻结。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/z7MyRb8LT5OJB4JYuqLdzQ/zh-cn_image_0000002558764060.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052702Z&HW-CC-Expire=86400&HW-CC-Sign=C7149D798C4B0C32F86799CA7D6F92C294C664BF6AE7AA167704AED7825ECB10)

### 组件冻结与组件复用混用时解冻不会触发Watch

在以下示例中，子组件ChildComponent开启了组件冻结且被标记了组件复用，当if组件绑定的状态变量condition修改为false时，子组件ChildComponent下树并进入复用池。由于子组件开启了组件冻结，所以进入复用池时，该组件也会被冻结。在复用池内，若修改状态变量count，该组件因处于inactive状态，即不会刷新也不会触发Watch回调。

当if组件绑定的状态变量condition修改为true时，子组件ChildComponent出复用池并被标记为active状态，但不会触发状态变量count绑定的Watch回调。这是因为组件复用的执行逻辑早于组件解冻的执行逻辑。子组件被复用时会将[脏节点刷新](arkts-state-management-introduce.md#触发更新)（包括在冻结期间需要延迟刷新的[变量绑定的系统组件](arkts-state-management-introduce.md#收集依赖)），并清空脏节点列表。在子组件被复用后，重新被标记为active状态，此时子组件执行解冻逻辑，由于复用时清空了脏节点列表，所以此时判断冻结期间无变量改变，不会触发Watch回调。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'FreezeChild';

6. @Reusable
7. @Component({ freezeWhenInactive: true })
8. struct ChildComponent {
9. @Link @Watch('onChange') count: number;

11. onChange() {
12. hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.count}`);
13. }

15. aboutToReuse(params: Record<string, ESObject>): void {
16. // 在aboutToReuse中改值，解冻时同样不会触发Watch回调
17. this.count++;
18. hilog.info(DOMAIN, TAG, `ChildComponent has been reused`);
19. }

21. aboutToRecycle(): void {
22. hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
23. }

25. build() {
26. Column() {
27. Text(`ChildComponent count: ${this.count}`)
28. .fontSize(20)
29. }
30. }
31. }

33. @Entry
34. @Component
35. struct Index {
36. @State flag: boolean = true;
37. @State count: number = 0;

39. build() {
40. Column() {
41. Button(`change flag`)
42. .onClick(() => {
43. this.flag = !this.flag;
44. })
45. .margin(10)
46. .width('50%')
47. Button(`change count`)
48. .onClick(() => {
49. this.count++;
50. })
51. .margin(10)
52. .width('50%')
53. if (this.flag) {
54. ChildComponent({ count: this.count })
55. }
56. }
57. .height('100%')
58. }
59. }
```
