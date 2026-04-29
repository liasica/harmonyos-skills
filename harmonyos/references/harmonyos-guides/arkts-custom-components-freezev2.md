---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freezev2
title: 自定义组件冻结功能（V2）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件冻结 > 自定义组件冻结功能（V2）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:05+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e009eea5a6235b1f45dc46063e967a0066fca9250f67cdd9109d18c89fa3c107
---

当@ComponentV2装饰的自定义组件处于非激活状态时，状态变量将不响应更新，即[@Monitor](arkts-new-monitor.md)不会调用，状态变量关联的节点不会刷新。该冻结机制在复杂UI场景下能显著优化性能，避免非激活组件因状态变量更新进行无效刷新，从而减少资源消耗。通过freezeWhenInactive属性来决定是否使用冻结功能，不传参数时默认不使用。支持的场景有：[页面路由](../harmonyos-references/js-apis-router.md)、[TabContent](../harmonyos-references/ts-container-tabcontent.md)、[Navigation](../harmonyos-references/ts-basic-components-navigation.md)、[Repeat](../harmonyos-references/ts-rendering-control-repeat.md)。

在阅读本文档前，开发者需要了解@ComponentV2基本语法。建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)。

说明

从API version 12开始，支持@ComponentV2装饰的自定义组件冻结功能。

从API version 18开始，支持自定义组件冻结混用场景。

从API version 22开始，通过将[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)的[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)配置为true，可实现如下场景：当父组件启用组件冻结，且组件树的中间层级启用了BuilderNode时，BuilderNode的子组件能够被冻结。具体可参考[设置BuilderNode继承冻结能力](arkts-user-defined-arktsnode-buildernode.md#设置buildernode继承冻结能力)。

与@Component的组件冻结不同，@ComponentV2装饰的自定义组件不支持在[LazyForEach](arkts-rendering-control-lazyforeach.md)场景下缓存节点组件冻结。

## 当前支持的场景

### 页面路由

说明

本示例使用了router进行页面跳转，建议开发者使用组件导航(Navigation)代替页面路由(router)来实现页面切换。Navigation提供了更多的功能和更灵活的自定义能力。请参考[使用Navigation的组件冻结用例](arkts-custom-components-freezev2.md#navigation)。

当页面1调用this.getUIContext().getRouter().pushUrl()接口跳转到页面2时，页面1为隐藏不可见状态，此时如果更新页面1中的状态变量，不会触发页面1刷新。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/b3ii7OXyS0mu4KL4UFEtHw/zh-cn_image_0000002589323919.png?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=20DAE4976D8750BB981312FF6DEACA58C3905766E5FF652B119DAFD171605173)

页面1：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;
4. const BOOK_INITIAL_NAME = '100';

6. @ObservedV2
7. export class Book {
8. @Trace public name: string = BOOK_INITIAL_NAME;

10. constructor(page: string) {
11. this.name = page;
12. }
13. }

15. @Entry
16. @ComponentV2({ freezeWhenInactive: true })
17. export struct Page1 {
18. @Local bookTest: Book = new Book(`A Midsummer Night's Dream`);

20. @Monitor('bookTest.name')
21. onMessageChange(monitor: IMonitor) {
22. hilog.info(DOMAIN, 'testTag', `The book name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
23. }

25. build() {
26. Column() {
27. Text(`Book name is  ${this.bookTest.name}`).fontSize(25)
28. Button('changeBookName').fontSize(25)
29. .onClick(() => {
30. this.bookTest.name = 'The Old Man and the Sea';
31. })
32. // 点击Button，路由跳转到页面2
33. Button('go to next page').fontSize(25)
34. .onClick(() => {
35. this.getUIContext().getRouter().pushUrl({ url: 'pages/freeze/template1/Page2' });
36. setTimeout(() => {
37. this.bookTest = new Book(`Jane Austen's Pride and Prejudice`);
38. }, 1000)
39. })
40. }
41. }
42. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template1/Page1.ets#L15-L57)

页面2：

```
1. @Entry
2. @ComponentV2
3. struct Page2 {
4. build() {
5. Column() {
6. Text('This is the page2').fontSize(25)
7. // 点击Button，路由跳转回页面1
8. Button('Back')
9. .onClick(() => {
10. this.getUIContext().getRouter().back();
11. })
12. }
13. }
14. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template1/Page2.ets#L15-L29)

在上面的示例中：

1.在页面1中点击changeBookName，bookTest变量的name属性改变，@Monitor中注册的方法onMessageChange会被调用。

2.在页面1中点击go to next page，跳转到页面2，然后延迟1s更新状态变量bookTest。在更新bookTest的时候，已经跳转到页面2，页面1处于inactive状态，[@Local](arkts-new-local.md)装饰的状态变量bookTest将不响应更新，其@Monitor不会调用，关联的节点不会刷新。

Trace如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/FXXdWN-BT7GOfzL0xfzq6Q/zh-cn_image_0000002558604404.png?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=5B871486818992C674192F1DD25B2981976E23ADEC3D979D95A4A946D0A98814)

3.点击Back，页面2被销毁，页面1的状态由inactive变为active。状态变量bookTest的更新被观察到，@Monitor中注册的方法onMessageChange被调用，对应的Text显示内容改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/F52SNu1YStWr6SUyyv57mg/zh-cn_image_0000002589323929.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=156D294A6AC2F2643635BCF7AE17C423F6CDF488BFA4412FF90203223DBFC415)

### TabContent

对Tabs中当前不可见的TabContent进行冻结，修改状态变量不会触发冻结组件的更新。

需要注意的是：在首次渲染时，Tabs只会创建当前正在显示的TabContent，当切换全部的TabContent后，TabContent才会被全部创建。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/nRF7Us-pRlafcF1q--xZDg/zh-cn_image_0000002589243859.png?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=571908BE4F90B94C2064D1FF15A6D6328C096D3F9C1FC1366D64DCDDEA2F9A5B)

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;

5. @Entry
6. @ComponentV2
7. struct TabContentTest {
8. @Local message: number = 0;
9. @Local data: number[] = [0, 1];

11. build() {
12. Row() {
13. Column() {
14. // 点击Button修改message，可见的TabContent触发onMessageUpdated回调
15. Button('change message').onClick(() => {
16. this.message++;
17. })

19. Tabs() {
20. ForEach(this.data, (item: number) => {
21. TabContent() {
22. FreezeChild({ message: this.message, index: item })
23. }.tabBar(`tab${item}`)
24. }, (item: number) => item.toString())
25. }
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }

33. @ComponentV2({ freezeWhenInactive: true })
34. struct FreezeChild {
35. @Param message: number = 0;
36. @Param index: number = 0;

38. @Monitor('message')
39. onMessageUpdated(mon: IMonitor) {
40. hilog.info(DOMAIN, 'testTag', `FreezeChild message callback func ${this.message}, index: ${this.index}`);
41. }

43. build() {
44. Text('message' + `${this.message}, index: ${this.index}`)
45. .fontSize(50)
46. .fontWeight(FontWeight.Bold)
47. }
48. }
```

[TabContentTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template2/TabContentTest.ets#L15-L63)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的TabContent组件中@Monitor注册的方法onMessageUpdated被触发。

2.点击tab1切换到另外的TabContent，该TabContent的状态由inactive变为active，对应的@Monitor注册的方法onMessageUpdated被触发。

3.再次点击change message更改message的值，仅当前显示的TabContent子组件中@Monitor注册的方法onMessageUpdated被触发。其他inactive的TabContent组件不会触发@Monitor。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/2cPdyz4gQeiu2VC53zU-0Q/zh-cn_image_0000002558764052.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=F70B76D5EF4DE3DD89FDDED5E0B3DD9489C63592C5641A1F26DD957075C3D8BF)

### Navigation

当NavDestination不可见时，会将其子自定义组件设置成非激活态，修改状态变量不会触发冻结组件的刷新。当返回该页面时，其子自定义组件重新恢复成激活态，触发@Monitor回调进行刷新。

需要注意：本文档里说的“激活（active）/非激活（inactive）”是指组件冻结的激活/非激活状态，和[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件中的[onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)和[onInactive](../harmonyos-references/ts-basic-components-navdestination.md#oninactive17)不同。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;
4. const PAGE_ONE_INDEX = 1;
5. const PAGE_TWO_INDEX = 2;
6. const PAGE_THREE_INDEX = 3;

8. @Entry
9. @ComponentV2
10. struct MyNavigationTestStack {
11. @Provider('pageInfo') pageInfo: NavPathStack = new NavPathStack();
12. @Local message: number = 0;

14. @Monitor('message')
15. info() {
16. hilog.info(DOMAIN, 'testTag', `freeze-test MyNavigation message callback ${this.message}`);
17. }

19. @Builder
20. PageMap(name: string) {
21. if (name === 'pageOne') {
22. PageOneStack({ message: this.message })
23. } else if (name === 'pageTwo') {
24. PageTwoStack({ message: this.message })
25. } else if (name === 'pageThree') {
26. PageThreeStack({ message: this.message })
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
39. .onClick(() => {
40. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
41. })
42. }
43. }.title('NavIndex')
44. .navDestination(this.PageMap)
45. .mode(NavigationMode.Stack)
46. }
47. }
48. }

50. @ComponentV2
51. struct PageOneStack {
52. @Consumer('pageInfo') pageInfo: NavPathStack = new NavPathStack();
53. @Local index: number = PAGE_ONE_INDEX;
54. @Param message: number = 0;

56. build() {
57. NavDestination() {
58. Column() {
59. NavigationContentMsgStack({ message: this.message, index: this.index })
60. Text('cur stack size:' + `${this.pageInfo.size()}`)
61. .fontSize(30)
62. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
63. .onClick(() => {
64. this.pageInfo.pushPathByName('pageTwo', null);
65. })
66. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
67. .onClick(() => {
68. this.pageInfo.pop();
69. })
70. }.width('100%').height('100%')
71. }.title('pageOne')
72. .onBackPressed(() => {
73. this.pageInfo.pop();
74. return true;
75. })
76. }
77. }

79. @ComponentV2
80. struct PageTwoStack {
81. @Consumer('pageInfo') pageInfo: NavPathStack = new NavPathStack();
82. @Local index: number = PAGE_TWO_INDEX;
83. @Param message: number = 0;

85. build() {
86. NavDestination() {
87. Column() {
88. NavigationContentMsgStack({ message: this.message, index: this.index })
89. Text('cur stack size:' + `${this.pageInfo.size()}`)
90. .fontSize(30)
91. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
92. .onClick(() => {
93. this.pageInfo.pushPathByName('pageThree', null);
94. })
95. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
96. .onClick(() => {
97. this.pageInfo.pop();
98. })
99. }
100. }.title('pageTwo')
101. .onBackPressed(() => {
102. this.pageInfo.pop();
103. return true;
104. })
105. }
106. }

108. @ComponentV2
109. struct PageThreeStack {
110. @Consumer('pageInfo') pageInfo: NavPathStack = new NavPathStack();
111. @Local index: number = PAGE_THREE_INDEX;
112. @Param message: number = 0;

114. build() {
115. NavDestination() {
116. Column() {
117. NavigationContentMsgStack({ message: this.message, index: this.index })
118. Text('cur stack size:' + `${this.pageInfo.size()}`)
119. .fontSize(30)
120. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
121. .height(40)
122. .onClick(() => {
123. this.pageInfo.pushPathByName('pageOne', null);
124. })
125. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
126. .height(40)
127. .onClick(() => {
128. this.pageInfo.pop();
129. })
130. }
131. }.title('pageThree')
132. .onBackPressed(() => {
133. this.pageInfo.pop();
134. return true;
135. })
136. }
137. }

139. @ComponentV2({ freezeWhenInactive: true })
140. struct NavigationContentMsgStack {
141. @Param message: number = 0;
142. @Param index: number = 0;

144. @Monitor('message')
145. info() {
146. hilog.info(DOMAIN, 'testTag', `freeze-test NavigationContent message callback ${this.message}`);
147. hilog.info(DOMAIN, 'testTag', `freeze-test ---- called by content ${this.index}`);
148. }

150. build() {
151. Column() {
152. Text('msg:' + `${this.message}`)
153. .fontSize(30)
154. }
155. }
156. }
```

[MyNavigationTestStack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template3/MyNavigationTestStack.ets#L15-L172)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的MyNavigationTestStack组件中@Monitor注册的方法info被触发。

2.点击Next Page切换到PageOne，创建PageOneStack节点。

3.再次点击change message更改message的值，仅PageOneStack中的NavigationContentMsgStack子组件中@Monitor注册的方法info被触发。

4.再次点击Next Page切换到PageTwo，创建PageTwoStack节点。PageOneStack节点状态由active变为inactive。

5.再次点击change message更改message的值，仅PageTwoStack中的NavigationContentMsgStack子组件中@Monitor注册的方法info被触发。Navigation路由栈中非栈顶的NavDestination中的子自定义组件是inactive状态，@Monitor方法不会触发。

6.再次点击Next Page切换到PageThree，创建PageThreeStack节点。PageTwoStack节点状态由active变为inactive。

7.再次点击change message更改message的值，仅PageThreeStack中的NavigationContentMsgStack子组件中@Monitor注册的方法info被触发。Navigation路由栈中非栈顶的NavDestination中的子自定义组件是inactive状态，@Monitor方法不会触发。

8.点击Back Page回到PageTwo，此时，PageTwoStack节点状态由inactive变为active，其NavigationContentMsgStack子组件中@Monitor注册的方法info被触发。

9.再次点击Back Page回到PageOne，此时，PageOneStack节点状态由inactive变为active，其NavigationContentMsgStack子组件中@Monitor注册的方法info被触发。

10.再次点击Back Page回到初始页，此时，无任何触发。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/jr2eS2jwS-KlIWKBGCXbnw/zh-cn_image_0000002589323921.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=97401409797EB5BF029C693650A8C929B21C624A473A9779127C80F176798382)

### Repeat

说明

Repeat从API version 18开始支持自定义组件冻结。

对Repeat缓存池中的自定义组件进行冻结，避免不必要的组件刷新。建议提前阅读[Repeat节点更新/复用能力说明](arkts-new-rendering-control-repeat.md#节点更新复用能力说明)。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;

5. @Entry
6. @ComponentV2
7. struct RepeatVirtualScrollFreeze {
8. @Local simpleList: Array<string> = [];
9. @Local bgColor: Color = Color.Pink;

11. aboutToAppear(): void {
12. for (let i = 0; i < 7; i++) {
13. this.simpleList.push(`item${i}`);
14. }
15. }

17. build() {
18. Column() {
19. Row() {
20. Button('Reduce length to 5')
21. .onClick(() => {
22. this.simpleList = this.simpleList.slice(0, 5);
23. })
24. Button('Change bgColor')
25. .onClick(() => {
26. this.bgColor = this.bgColor == Color.Pink ? Color.Blue : Color.Pink;
27. })
28. }

30. List() {
31. Repeat(this.simpleList)
32. .each((obj: RepeatItem<string>) => {
33. })
34. .key((item: string, index: number) => item)
35. .virtualScroll({ totalCount: this.simpleList.length })
36. .templateId(() => 'a')
37. .template('a', (ri) => {
38. ChildComponent({
39. message: ri.item,
40. bgColor: this.bgColor
41. })
42. }, { cachedCount: 2 })
43. }
44. .cachedCount(0)
45. .height(500)
46. }
47. .height('100%')
48. }
49. }

51. // 开启组件冻结
52. @ComponentV2({ freezeWhenInactive: true })
53. struct ChildComponent {
54. @Param @Require message: string = '';
55. @Param @Require bgColor: Color = Color.Pink;

57. @Monitor('bgColor')
58. onBgColorChange(monitor: IMonitor) {
59. // bgColor改变时，缓存池中组件不刷新，不会打印日志
60. hilog.info(DOMAIN, 'testTag', `repeat---bgColor change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
61. }

63. build() {
64. Text(`[a]: ${this.message}`)
65. .fontSize(50)
66. .backgroundColor(this.bgColor)
67. }
68. }
```

[RepeatVirtualScrollFreeze.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template4/RepeatVirtualScrollFreeze.ets#L15-L84)

在上面的示例中：

点击Reduce length to 5后，被移除的两个组件会进入Repeat缓存池，然后点击Change bgColor更改bgColor的值触发节点刷新。

开启组件冻结（freezeWhenInactive: true），只有剩余节点中@Monitor装饰的方法onBgColorChange被触发，如示例中屏上的5个节点会刷新并打印5条日志，缓存池中的节点则不会。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/u91SusSSSZy4huDGJkepkA/zh-cn_image_0000002589243869.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=A9D24DB339B6507CD74216239C0FCE72B1027F937B132FDE873E7D6F611795AF)

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;
4. // ...
5. // 关闭组件冻结
6. @ComponentV2({ freezeWhenInactive: false })
7. struct ChildComponent1 {
8. @Param @Require message: string = '';
9. @Param @Require bgColor: Color = Color.Pink;

11. @Monitor('bgColor')
12. onBgColorChange(monitor: IMonitor) {
13. // bgColor改变时，缓存池组件也会刷新，并打印日志
14. hilog.info(DOMAIN, 'testTag', `repeat---bgColor change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
15. }

17. build() {
18. Text(`[a]: ${this.message}`)
19. .fontSize(50)
20. .backgroundColor(this.bgColor)
21. }
22. }
```

[PageB.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template4/PageB.ets#L15-L84)

不开启组件冻结（freezeWhenInactive: false，当未指定freezeWhenInactive参数时默认不开启组件冻结），剩余节点和缓存池节点中@Monitor装饰的方法onBgColorChange都会被触发，即会有7个节点会刷新并打印7条日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/2ncOjXSYRo2aA7dvW8_lmQ/zh-cn_image_0000002558764062.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=50EF802A3AE17BD45CE3A65C07B9E6882408F1CD00313620C1CEE652FFF13226)

### 仅子组件开启组件冻结

如果开发者只想冻结某个子组件，可以选择只在子组件设置freezeWhenInactive为true。

```
1. // src/main/ets/pages/freeze/template5/PageA.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. @ObservedV2
7. class Book {
8. @Trace public name: string = 'TS';

10. constructor(name: string) {
11. this.name = name;
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct PageA {
18. pageInfo: NavPathStack = new NavPathStack();

20. build() {
21. Column() {
22. Navigation(this.pageInfo) {
23. Child()

25. // 点击Button，跳转页面至PageB
26. Button('Go to next page').fontSize(30)
27. .onClick(() => {
28. this.pageInfo.pushPathByName('PageB', null);
29. })
30. }
31. }
32. }
33. }

35. @ComponentV2({ freezeWhenInactive: true })
36. export struct Child {
37. @Local bookTest: Book = new Book(`A Midsummer Night's Dream`);

39. @Monitor('bookTest.name')
40. onMessageChange(monitor: IMonitor) {
41. hilog.info(DOMAIN, 'testTag', `The book name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
42. }

44. textUpdate(): number {
45. hilog.info(DOMAIN, 'testTag', 'The text is update');
46. return 25;
47. }

49. build() {
50. Column() {
51. Text(`The book name is ${this.bookTest.name}`).fontSize(this.textUpdate())

53. Button('change BookName')
54. .onClick(() => {
55. setTimeout(() => {
56. this.bookTest = new Book(`Jane Austen's Pride and Prejudice`);
57. }, 3000);
58. })
59. }
60. }
61. }
```

[PageA.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template5/PageA.ets#L15-L76)

```
1. // src/main/ets/pages/freeze/template5/PageB.ets
2. @Builder
3. function pageBBuilder() {
4. PageB()
5. }

7. @ComponentV2
8. struct PageB {
9. pathStack: NavPathStack = new NavPathStack();

11. build() {
12. NavDestination() {
13. Column() {
14. Text('This is the PageB')

16. // 点击Button，页面跳转回PageA
17. Button('Back').fontSize(30)
18. .onClick(() => {
19. this.pathStack.pop();
20. })
21. }
22. }.onReady((context: NavDestinationContext) => {
23. this.pathStack = context.pathStack;
24. })
25. }
26. }
```

[PageB.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template5/PageB.ets#L16-L42)

使用Navigation时，需要添加配置系统路由表文件src/main/resources/base/profile/route\_map.json，并替换pageSourceFile为PageB页面的路径，并且在module.json5中添加："routerMap": "$profile:route\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "PageB",
5. "pageSourceFile": "src/main/ets/pages/freeze/template5/PageB.ets",
6. "buildFunction": "pageBBuilder",
7. "data": {
8. "description" : "This is the PageB"
9. }
10. }
11. ]
12. }
```

在上面的示例中：

* PageA的子组件Child，设置freezeWhenInactive: true, 开启了组件冻结功能。
* 点击change BookName，然后3s内点击Go to next page。在更新bookTest的时候，已经跳转到PageB，PageA的组件处于inactive状态，又因为Child组件开启了组件冻结，状态变量@Local bookTest将不响应更新，其@Monitor装饰的回调方法不会被调用，状态变量关联的组件不会刷新。
* 点击Back回到前一个页面，调用@Monitor装饰的回调方法，状态变量关联的组件刷新。

### 混用场景

当支持组件冻结的场景彼此之间组合使用时，对于不同的API版本，冻结行为会有不同。给父组件设置组件冻结标志，在API version 17及以下，当父组件解冻时，会解冻其子组件所有的节点；从API version 18开始，父组件解冻时，只会解冻子组件的屏上节点，详细说明见[@Component的自定义组件冻结的混用场景](arkts-custom-components-freeze.md#组件混用)。

**Navigation和TabContent的混用**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0000;
4. const TAB_STATE_INITIAL_VALUE = 47;

6. @ComponentV2
7. struct ChildOfParamComponent {
8. @Require @Param childVal: number;

10. @Monitor('childVal')
11. onChange(m: IMonitor) {
12. hilog.info(DOMAIN, 'testTag',
13. `Appmonitor ChildOfParamComponent: changed ${m.dirty[0]}: ${m.value()?.before} -> ${m.value()?.now}`);
14. }

16. build() {
17. Column() {
18. Text(`Child Param： ${this.childVal}`)
19. }
20. }
21. }

23. @ComponentV2
24. struct ParamComponent {
25. @Require @Param val: number;

27. @Monitor('val')
28. onChange(m: IMonitor) {
29. hilog.info(DOMAIN, 'testTag',
30. `Appmonitor ParamComponent: changed ${m.dirty[0]}: ${m.value()?.before} -> ${m.value()?.now}`);
31. }

33. build() {
34. Column() {
35. Text(`val： ${this.val}`)
36. ChildOfParamComponent({ childVal: this.val })
37. }
38. }
39. }

41. @ComponentV2
42. struct DelayComponent {
43. @Require @Param delayVal1: number;

45. @Monitor('delayVal1')
46. onChange(m: IMonitor) {
47. hilog.info(DOMAIN, 'testTag',
48. `Appmonitor DelayComponent: changed ${m.dirty[0]}: ${m.value()?.before} -> ${m.value()?.now}`);
49. }

51. build() {
52. Column() {
53. Text(`Delay Param： ${this.delayVal1}`)
54. }
55. }
56. }

58. @ComponentV2({ freezeWhenInactive: true })
59. struct TabsComponent {
60. private controller: TabsController = new TabsController();
61. @Local tabState: number = TAB_STATE_INITIAL_VALUE;

63. @Monitor('tabState')
64. onChange(m: IMonitor) {
65. hilog.info(DOMAIN, 'testTag',
66. `Appmonitor TabsComponent: changed ${m.dirty[0]}: ${m.value()?.before} -> ${m.value()?.now}`);
67. }

69. build() {
70. Column({ space: 10 }) {
71. Button(`Incr state ${this.tabState}`)
72. .fontSize(25)
73. .onClick(() => {
74. hilog.info(DOMAIN, 'testTag', 'Button increment state value');
75. this.tabState = this.tabState + 1;
76. })
77. Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {
78. TabContent() {
79. ParamComponent({ val: this.tabState })
80. }.tabBar('Update')
81. TabContent() {
82. DelayComponent({ delayVal1: this.tabState })
83. }.tabBar('DelayUpdate')
84. }
85. .vertical(false)
86. .scrollable(true)
87. .barMode(BarMode.Fixed)
88. .barWidth(400)
89. .barHeight(150)
90. .animationDuration(400)
91. .width('100%')
92. .height(200)
93. .backgroundColor(0xF5F5F5)
94. }
95. }
96. }

98. @Entry
99. @Component
100. struct MyNavigationTestStack1 {
101. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();

103. @Builder
104. PageMap(name: string) {
105. if (name === 'pageOne') {
106. PageOneStack1()
107. } else if (name === 'pageTwo') {
108. PageTwoStack2()
109. }
110. }

112. build() {
113. Column() {
114. Navigation(this.pageInfo) {
115. Column() {
116. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
117. .width('80%')
118. .height(40)
119. .margin(20)
120. .onClick(() => {
121. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
122. })
123. }
124. }.title('NavIndex')
125. .navDestination(this.PageMap)
126. .mode(NavigationMode.Stack)
127. }
128. }
129. }

131. @Component
132. struct PageOneStack1 {
133. @Consume('pageInfo') pageInfo: NavPathStack;

135. build() {
136. NavDestination() {
137. Column() {
138. // NavDestination中创建TabContent
139. TabsComponent()

141. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
142. .width('80%')
143. .height(40)
144. .margin(20)
145. .onClick(() => {
146. this.pageInfo.pushPathByName('pageTwo', null);
147. })
148. }.width('100%').height('100%')
149. }.title('pageOne')
150. .onBackPressed(() => {
151. this.pageInfo.pop();
152. return true;
153. })
154. }
155. }

157. @Component
158. struct PageTwoStack2 {
159. @Consume('pageInfo') pageInfo: NavPathStack;

161. build() {
162. NavDestination() {
163. Column() {
164. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
165. .width('80%')
166. .height(40)
167. .margin(20)
168. .onClick(() => {
169. this.pageInfo.pop();
170. })
171. }.width('100%').height('100%')
172. }.title('pageTwo')
173. .onBackPressed(() => {
174. this.pageInfo.pop();
175. return true;
176. })
177. }
178. }
```

[MyNavigationTestStack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template6/MyNavigationTestStack.ets#L15-L193)

在API version 17及以下：

点击Next page进入下一个页面并返回，会解冻Tabcontent所有的标签。

在API version 18及以上：

点击Next page进入下一个页面并返回，只会解冻对应标签的节点。

## 限制条件

API version 21及之前版本，如下面示例所示，FreezeBuildNode中使用了自定义节点[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)。BuilderNode可以通过命令式动态挂载组件，而组件冻结又是强依赖父子关系来通知是否开启组件冻结。如果父组件使用组件冻结，且组件树的中间层级上又启用了BuilderNode，则BuilderNode的子组件将无法被冻结。从API version 22开始，可以[设置BuilderNode继承冻结能力](arkts-user-defined-arktsnode-buildernode.md#设置buildernode继承冻结能力)。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. // 定义一个Params类，用于传递参数
7. @ObservedV2
8. class Params {
9. // 单例模式，确保只有一个Params实例
10. public static singleton_: Params;

12. // 获取Params实例的方法
13. public static instance() {
14. if (!Params.singleton_) {
15. Params.singleton_ = new Params(0);
16. }
17. return Params.singleton_;
18. }

20. // 使用@Trace装饰器装饰message属性，以便跟踪其变化
21. @Trace public message: string = 'Hello';
22. public index: number = 0;

24. constructor(index: number) {
25. this.index = index;
26. }
27. }

29. // 定义一个BuildNodeChild组件，它包含一个storage属性和一个index属性
30. @ComponentV2
31. struct BuildNodeChild {
32. // 使用Params实例作为storage属性
33. storage: Params = Params.instance();
34. @Param index: number = 0;

36. // 使用@Monitor装饰器监听storage.message的变化
37. @Monitor('storage.message')
38. onMessageChange(monitor: IMonitor) {
39. hilog.info(DOMAIN, 'onMessageChange',
40. `FreezeBuildNode BuildNodeChild message callback func ${this.storage.message}, index:${this.index}`);
41. }

43. build() {
44. Text(`buildNode Child message: ${this.storage.message}`).fontSize(30)
45. }
46. }

48. // 定义一个buildText函数，它接收一个Params参数并构建一个Column组件
49. @Builder
50. function buildText(params: Params) {
51. Column() {
52. BuildNodeChild({ index: params.index })
53. }
54. }

56. class TextNodeController extends NodeController {
57. private textNode: BuilderNode<[Params]> | null = null;
58. private index: number = 0;

60. // 构造函数接收一个index参数
61. constructor(index: number) {
62. super();
63. this.index = index;
64. }

66. // 创建并返回一个FrameNode
67. makeNode(context: UIContext): FrameNode | null {
68. this.textNode = new BuilderNode(context);
69. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.index));
70. return this.textNode.getFrameNode();
71. }
72. }

74. // 定义一个Index组件，它包含一个message属性和一个data数组
75. @Entry
76. @ComponentV2
77. struct Index {
78. // 使用Params实例作为storage属性
79. storage: Params = Params.instance();
80. private data: number[] = [0, 1];

82. build() {
83. Row() {
84. Column() {
85. Button('change').fontSize(30)
86. .onClick(() => {
87. this.storage.message += 'a';
88. })

90. Tabs() {
91. // 使用Repeat重复渲染TabContent组件
92. Repeat<number>(this.data)
93. .each((obj: RepeatItem<number>) => {
94. TabContent() {
95. FreezeBuildNode({ index: obj.item })
96. .margin({ top: 20 })
97. }.tabBar(`tab${obj.item}`)
98. })
99. .key((item: number) => item.toString())
100. }
101. }
102. }
103. .width('100%')
104. .height('100%')
105. }
106. }

108. // 定义一个FreezeBuildNode组件，它包含一个message属性和一个index属性
109. @ComponentV2({ freezeWhenInactive: true })
110. struct FreezeBuildNode {
111. // 使用Params实例作为storage属性
112. storage: Params = Params.instance();
113. @Param index: number = 0;

115. // 使用@Monitor装饰器监听storage.message的变化
116. @Monitor('storage.message')
117. onMessageChange(monitor: IMonitor) {
118. hilog.info(DOMAIN, 'onMessageChange',
119. `FreezeBuildNode message callback func ${this.storage.message}, index: ${this.index}`);
120. }

122. build() {
123. NodeContainer(new TextNodeController(this.index))
124. .width('100%')
125. .height('100%')
126. .backgroundColor('#FFF0F0F0')
127. }
128. }
```

[BuilderNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FreezeV2/entry/src/main/ets/pages/freeze/template7/BuilderNode.ets#L15-L144)

点击change，改变message的值，当前正在显示的TabContent组件中@Monitor注册的方法onMessageChange被触发。未显示的TabContent中的BuilderNode节点下组件的@Monitor方法onMessageChange也被触发，并没有被冻结。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/7NwxxWuPT8-xObXLbsZmnQ/zh-cn_image_0000002558764060.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052703Z&HW-CC-Expire=86400&HW-CC-Sign=117B726487286E8F1EDBD4BD1A49023F77DC23D03615736C0C9F720BC5348901)
