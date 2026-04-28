---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-application
title: 应用内状态变量迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 应用内状态变量迁移
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b69cac0051032c5b519c3efd0e056739c3850bee65aec385e624cc8e5fb03df
---

本文档主要介绍应用内状态变量迁移，包含以下场景。

| V1装饰器名称/场景 | 迁移方案 |
| --- | --- |
| [LocalStorage](arkts-localstorage.md) | [@ObservedV2](arkts-new-observedv2-and-trace.md) [@Trace](arkts-new-observedv2-and-trace.md) |
| [AppStorage](arkts-appstorage.md) | [AppStorageV2](arkts-new-appstoragev2.md) |
| [Environment](arkts-environment.md) | 通过[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)的config属性获取系统环境变量 |
| [PersistentStorage](arkts-persiststorage.md) | [PersistenceV2](arkts-new-persistencev2.md) |
| 存量迁移场景 | @ObservedV2、@Trace、[@Monitor](arkts-new-monitor.md) |

## LocalStorage->@ObservedV2/@Trace

**迁移规则**

LocalStorage的目的是实现页面间的状态变量共享。由于V1状态变量和View层耦合，开发者难以自主实现页面间状态变量的共享，因此框架提供了该能力。

状态管理V2将状态变量的观察能力内嵌到数据本身，不再和View层耦合。因此，不再需要类似LocalStorage的能力，可以使用创建@ObservedV2和@Trace装饰类的实例，开发者需自行import和export，实现状态变量的页面间共享。

### 基本场景

V1:

通过windowStage.[loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)和this.getUIContext().[getSharedLocalStorage](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getsharedlocalstorage12)接口实现页面间的状态变量共享。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. public para: Record<string, number> = { 'count': 47 };
6. public storage: LocalStorage = new LocalStorage(this.para);

8. onWindowStageCreate(windowStage: window.WindowStage): void {
9. windowStage.loadContent('pages/Page1', this.storage);
10. }
11. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV1/EntryAbility.ets#L15-L27)

在下面的示例中，使用@LocalStorageLink，可以将开发者本地的修改同步回LocalStorage中。

```
1. // Page1.ets
2. // 预览器上不支持获取页面共享的LocalStorage实例。
3. @Entry({ useSharedStorage: true })
4. @Component
5. struct Page1 {
6. @LocalStorageLink('count') count: number = 0;
7. pageStack: NavPathStack = new NavPathStack();

9. build() {
10. Navigation(this.pageStack) {
11. Column() {
12. Text(`${this.count}`)
13. .fontSize(50)
14. .onClick(() => {
15. this.count++;
16. })
17. Button('push to Page2')
18. .onClick(() => {
19. this.pageStack.pushPathByName('Page2', null);
20. })
21. }
22. }
23. }
24. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV1/pages/Page1.ets#L15-L40)

```
1. // Page2.ets
2. @Builder
3. export function Page2Builder() {
4. Page2()
5. }

7. // Page2组件获得了父亲Page1组件的LocalStorage实例
8. @Component
9. struct Page2 {
10. @LocalStorageLink('count') count: number = 0;
11. pathStack: NavPathStack = new NavPathStack();

13. build() {
14. NavDestination() {
15. Column() {
16. Text(`${this.count}`)
17. .fontSize(50)
18. .onClick(() => {
19. this.count++;
20. })
21. Button('change')
22. .fontSize(50)
23. .onClick(() => {
24. const storage = this.getUIContext().getSharedLocalStorage();
25. if (storage) {
26. storage.set('count', 20);
27. }
28. })
29. }
30. }
31. .onReady((context: NavDestinationContext) => {
32. this.pathStack = context.pathStack;
33. })
34. }
35. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV1/pages/Page2.ets#L15-L51)

使用Navigation时，需要添加配置系统路由表文件src/main/resources/base/profile/route\_map.json，并替换pageSourceFile为Page2页面的路径，并且在module.json5中添加："routerMap": "$profile:route\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "Page2",
5. "pageSourceFile": "src/main/ets/pages/Page2.ets",
6. "buildFunction": "Page2Builder",
7. "data": {
8. "description": "LocalStorage example"
9. }
10. }
11. ]
12. }
```

V2:

* 声明@ObservedV2装饰的MyStorage类，并import到需要使用的页面中。
* 声明被@Trace的属性作为页面间共享的可观察的数据。

```
1. @ObservedV2
2. export class MyStorage {
3. public static singleton_: MyStorage;

5. static instance() {
6. if (!MyStorage.singleton_) {
7. MyStorage.singleton_ = new MyStorage();
8. }
9. return MyStorage.singleton_;
10. }
11. @Trace public count: number = 47;
12. }
```

[storage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV2/storage.ets#L15-L28)

```
1. // Page1.ets
2. import { MyStorage } from './storage';

4. @Entry
5. @ComponentV2
6. struct Page1 {
7. storage: MyStorage = MyStorage.instance();
8. pageStack: NavPathStack = new NavPathStack();

10. build() {
11. Navigation(this.pageStack) {
12. Column() {
13. Text(`${this.storage.count}`)
14. .fontSize(50)
15. .onClick(() => {
16. this.storage.count++;
17. })
18. Button('push to Page2')
19. .onClick(() => {
20. this.pageStack.pushPathByName('Page2', null);
21. })
22. }
23. }
24. }
25. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV2/Page1.ets#L15-L41)

```
1. // Page2.ets
2. import { MyStorage } from './storage';

4. @Builder
5. export function Page2Builder() {
6. Page2()
7. }

9. @ComponentV2
10. struct Page2 {
11. storage: MyStorage = MyStorage.instance();
12. pathStack: NavPathStack = new NavPathStack();

14. build() {
15. NavDestination() {
16. Column() {
17. Text(`${this.storage.count}`)
18. .fontSize(50)
19. .onClick(() => {
20. this.storage.count++;
21. })
22. }
23. }
24. .onReady((context: NavDestinationContext) => {
25. this.pathStack = context.pathStack;
26. })
27. }
28. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@ObservedV2@TraceV2/Page2.ets#L15-L44)

使用Navigation时，需要添加配置系统路由表文件src/main/resources/base/profile/route\_map.json，并替换pageSourceFile为Page2页面的路径，并且在module.json5中添加："routerMap": "$profile:route\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "Page2",
5. "pageSourceFile": "src/main/ets/pages/Page2.ets",
6. "buildFunction": "Page2Builder",
7. "data": {
8. "description" : "LocalStorage example"
9. }
10. }
11. ]
12. }
```

如果开发者需要实现类似于@LocalStorageProp的效果，但希望本地的修改不同步回LocalStorage中，可参考以下示例：

* 在Page1中改变count值，由于count被@LocalStorageProp装饰的，因此其更改仅在本地生效，不会同步到LocalStorage。
* 点击push to Page2按钮，跳转到Page2。由于在Page1中改变count值不会同步到LocalStorage，因此Page2中的Text组件仍显示初始值47。
* 点击change Storage Count按钮，调用LocalStorage的setOrCreate，改变count对应的值，并通知所有绑定该key的变量。

```
1. // Page1.ets
2. export let storage: LocalStorage = new LocalStorage();

4. storage.setOrCreate('count', 47);

6. @Entry(storage)
7. @Component
8. struct Page1 {
9. @LocalStorageProp('count') count: number = 0;
10. pageStack: NavPathStack = new NavPathStack();

12. build() {
13. Navigation(this.pageStack) {
14. Column() {
15. Text(`${this.count}`)
16. .fontSize(50)
17. .onClick(() => {
18. this.count++;
19. })
20. Button('change Storage Count')
21. .onClick(() => {
22. storage.setOrCreate('count', storage.get<number>('count') as number + 100);
23. })
24. Button('push to Page2')
25. .onClick(() => {
26. this.pageStack.pushPathByName('Page2', null);
27. })
28. }
29. }
30. }
31. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@TracesetOrCreateV1/Page1.ets#L15-L47)

```
1. // Page2.ets
2. import { storage } from './Page1'

4. @Builder
5. export function Page2Builder() {
6. Page2()
7. }

9. // Page2组件获得了父亲Page1组件的LocalStorage实例
10. @Component
11. struct Page2 {
12. @LocalStorageProp('count') count: number = 0;
13. pathStack: NavPathStack = new NavPathStack();

15. build() {
16. NavDestination() {
17. Column() {
18. Text(`${this.count}`)
19. .fontSize(50)
20. .onClick(() => {
21. this.count++;
22. })
23. Button('change Storage Count')
24. .onClick(() => {
25. storage.setOrCreate('count', storage.get<number>('count') as number + 100);
26. })
27. }
28. }
29. .onReady((context: NavDestinationContext) => {
30. this.pathStack = context.pathStack;
31. })
32. }
33. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@TracesetOrCreateV1/Page2.ets#L15-L49)

在V2中，可以借助@Local和@Monitor实现类似的效果。

* @Local装饰的count变量为组件本地的值，其改变不会同步回storage。
* @Monitor监听storage.count的变化，当storage.count改变时，在@Monitor的回调里改变本地@Local的值。

```
1. // Page1.ets
2. import { MyStorage } from './storage';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @Entry
8. @ComponentV2
9. struct Page1 {
10. storage: MyStorage = MyStorage.instance();
11. pageStack: NavPathStack = new NavPathStack();
12. @Local count: number = this.storage.count;

14. @Monitor('storage.count')
15. onCountChange(mon: IMonitor) {
16. hilog.info(DOMAIN, 'testTag', '%{public}s', `Page1 ${mon.value()?.before} to ${mon.value()?.now}`);
17. this.count = this.storage.count;
18. }

20. build() {
21. Navigation(this.pageStack) {
22. Column() {
23. Text(`${this.count}`)
24. .fontSize(50)
25. .onClick(() => {
26. this.count++;
27. })
28. Button('change Storage Count')
29. .onClick(() => {
30. this.storage.count += 100;
31. })
32. Button('push to Page2')
33. .onClick(() => {
34. this.pageStack.pushPathByName('Page2', null);
35. })
36. }
37. }
38. }
39. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@TracesetOrCreateV2/Page1.ets#L15-L55)

```
1. // Page2.ets
2. import { MyStorage } from './storage';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @Builder
8. export function Page2Builder() {
9. Page2()
10. }

12. @ComponentV2
13. struct Page2 {
14. storage: MyStorage = MyStorage.instance();
15. pathStack: NavPathStack = new NavPathStack();
16. @Local count: number = this.storage.count;

18. @Monitor('storage.count')
19. onCountChange(mon: IMonitor) {
20. hilog.info(DOMAIN, 'testTag', '%{public}s', `Page2 ${mon.value()?.before} to ${mon.value()?.now}`);
21. this.count = this.storage.count;
22. }

24. build() {
25. NavDestination() {
26. Column() {
27. Text(`${this.count}`)
28. .fontSize(50)
29. .onClick(() => {
30. this.count++;
31. })
32. Button('change Storage Count')
33. .onClick(() => {
34. this.storage.count += 100;
35. })
36. }
37. }
38. .onReady((context: NavDestinationContext) => {
39. this.pathStack = context.pathStack;
40. })
41. }
42. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/Internal@TracesetOrCreateV2/Page2.ets#L15-L58)

### 自定义组件接收LocalStorage实例场景

为了配合Navigation的场景，LocalStorage支持作为自定义组件的入参，传递给以当前自定义组件为根节点的所有子自定义组件。

对于该场景，V2可以使用创建多个全局@ObservedV2和@Trace装饰类的实例进行替代。

V1:

```
1. let localStorageA: LocalStorage = new LocalStorage();
2. localStorageA.setOrCreate('propA', 'propA');

4. let localStorageB: LocalStorage = new LocalStorage();
5. localStorageB.setOrCreate('propB', 'propB');

7. let localStorageC: LocalStorage = new LocalStorage();
8. localStorageC.setOrCreate('propC', 'propC');

10. @Entry
11. @Component
12. struct MyNavigationTestStack {
13. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();

15. @Builder
16. PageMap(name: string) {
17. if (name === 'pageOne') {
18. // 传递不同的LocalStorage实例
19. PageOneStack({}, localStorageA)
20. } else if (name === 'pageTwo') {
21. PageTwoStack({}, localStorageB)
22. } else if (name === 'pageThree') {
23. PageThreeStack({}, localStorageC)
24. }
25. }

27. build() {
28. Column({ space: 5 }) {
29. Navigation(this.pageInfo) {
30. Column() {
31. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
32. .width('80%')
33. .height(40)
34. .margin(20)
35. .onClick(() => {
36. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
37. })
38. }
39. }.title('NavIndex')
40. .navDestination(this.PageMap)
41. .mode(NavigationMode.Stack)
42. .borderWidth(1)
43. }
44. }
45. }

47. @Component
48. struct PageOneStack {
49. @Consume('pageInfo') pageInfo: NavPathStack;
50. @LocalStorageLink('propA') propA: string = 'Hello World';

52. build() {
53. NavDestination() {
54. Column() {
55. // 显示'propA'
56. NavigationContentMsgStack()
57. // 显示'propA'
58. Text(`${this.propA}`)
59. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
60. .width('80%')
61. .height(40)
62. .margin(20)
63. .onClick(() => {
64. this.pageInfo.pushPathByName('pageTwo', null);
65. })
66. }.width('100%').height('100%')
67. }.title('pageOne')
68. .onBackPressed(() => {
69. this.pageInfo.pop();
70. return true;
71. })
72. }
73. }

75. @Component
76. struct PageTwoStack {
77. @Consume('pageInfo') pageInfo: NavPathStack;
78. @LocalStorageLink('propB') propB: string = 'Hello World';

80. build() {
81. NavDestination() {
82. Column() {
83. // 显示'Hello'，当前LocalStorage实例localStorageB没有propA对应的值，使用本地默认值'Hello'
84. NavigationContentMsgStack()
85. // 显示'propB'
86. Text(`${this.propB}`)
87. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
88. .width('80%')
89. .height(40)
90. .margin(20)
91. .onClick(() => {
92. this.pageInfo.pushPathByName('pageThree', null);
93. })

95. }.width('100%').height('100%')
96. }.title('pageTwo')
97. .onBackPressed(() => {
98. this.pageInfo.pop();
99. return true;
100. })
101. }
102. }

104. @Component
105. struct PageThreeStack {
106. @Consume('pageInfo') pageInfo: NavPathStack;
107. @LocalStorageLink('propC') propC: string = 'pageThreeStack';

109. build() {
110. NavDestination() {
111. Column() {
112. // 显示'Hello'，当前LocalStorage实例localStorageC没有propA对应的值，使用本地默认值'Hello'
113. NavigationContentMsgStack()
114. // 显示'propC'
115. Text(`${this.propC}`)
116. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
117. .width('80%')
118. .height(40)
119. .margin(20)
120. .onClick(() => {
121. this.pageInfo.pushPathByName('pageOne', null);
122. })

124. }.width('100%').height('100%')
125. }.title('pageThree')
126. .onBackPressed(() => {
127. this.pageInfo.pop();
128. return true;
129. })
130. }
131. }

133. @Component
134. struct NavigationContentMsgStack {
135. @LocalStorageLink('propA') propA: string = 'Hello';

137. build() {
138. Column() {
139. Text(`${this.propA}`)
140. .fontSize(30)
141. .fontWeight(FontWeight.Bold)
142. }
143. }
144. }
```

[InternalTraceCustomizeV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalTraceCustomize/InternalTraceCustomizeV1.ets#L15-L160)

V2：

声明@ObservedV2装饰的class代替LocalStorage。其中LocalStorage的key可以用@Trace装饰的属性代替。

```
1. @ObservedV2
2. export class MyStorageA {
3. @Trace public propA: string = 'Hello';

5. constructor(propA?: string) {
6. this.propA = propA ? propA : this.propA;
7. }
8. }

10. @ObservedV2
11. export class MyStorageB extends MyStorageA {
12. @Trace public propB: string = 'Hello';

14. constructor(propB: string) {
15. super();
16. this.propB = propB;
17. }
18. }

20. @ObservedV2
21. export class MyStorageC extends MyStorageA {
22. @Trace public propC: string = 'Hello';

24. constructor(propC: string) {
25. super();
26. this.propC = propC;
27. }
28. }
```

[storage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalTraceCustomize/storage.ets#L15-L44)

在PageOneStack、PageTwoStack和PageThreeStack组件内分别创建MyStorageA、MyStorageB、MyStorageC的实例，并通过@Param传递给其子组件NavigationContentMsgStack，从而实现类似LocalStorage实例在子组件树上共享的能力。

```
1. // Index.ets
2. import { MyStorageA, MyStorageB, MyStorageC } from './storage';

4. @Entry
5. @ComponentV2
6. struct MyNavigationTestStack {
7. pageInfo: NavPathStack = new NavPathStack();

9. @Builder
10. PageMap(name: string) {
11. if (name === 'pageOne') {
12. PageOneStack()
13. } else if (name === 'pageTwo') {
14. PageTwoStack()
15. } else if (name === 'pageThree') {
16. PageThreeStack()
17. }
18. }

20. build() {
21. Column({ space: 5 }) {
22. Navigation(this.pageInfo) {
23. Column() {
24. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
25. .width('80%')
26. .height(40)
27. .margin(20)
28. .onClick(() => {
29. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
30. })
31. }
32. }.title('NavIndex')
33. .navDestination(this.PageMap)
34. .mode(NavigationMode.Stack)
35. .borderWidth(1)
36. }
37. }
38. }

40. @ComponentV2
41. struct PageOneStack {
42. pageInfo: NavPathStack = new NavPathStack();
43. @Local storageA: MyStorageA = new MyStorageA('PropA');

45. build() {
46. NavDestination() {
47. Column() {
48. // 显示'PropA'
49. NavigationContentMsgStack({ storage: this.storageA })
50. // 显示'PropA'
51. Text(`${this.storageA.propA}`)
52. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
53. .width('80%')
54. .height(40)
55. .margin(20)
56. .onClick(() => {
57. this.pageInfo.pushPathByName('pageTwo', null);
58. })
59. }.width('100%').height('100%')
60. }.title('pageOne')
61. .onBackPressed(() => {
62. this.pageInfo.pop();
63. return true;
64. })
65. .onReady((context: NavDestinationContext) => {
66. this.pageInfo = context.pathStack;
67. })
68. }
69. }

71. @ComponentV2
72. struct PageTwoStack {
73. pageInfo: NavPathStack = new NavPathStack();
74. @Local storageB: MyStorageB = new MyStorageB('PropB');

76. build() {
77. NavDestination() {
78. Column() {
79. // 显示'Hello'
80. NavigationContentMsgStack({ storage: this.storageB })
81. // 显示'PropB'
82. Text(`${this.storageB.propB}`)
83. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
84. .width('80%')
85. .height(40)
86. .margin(20)
87. .onClick(() => {
88. this.pageInfo.pushPathByName('pageThree', null);
89. })

91. }.width('100%').height('100%')
92. }.title('pageTwo')
93. .onBackPressed(() => {
94. this.pageInfo.pop();
95. return true;
96. })
97. .onReady((context: NavDestinationContext) => {
98. this.pageInfo = context.pathStack;
99. })
100. }
101. }

103. @ComponentV2
104. struct PageThreeStack {
105. pageInfo: NavPathStack = new NavPathStack();
106. @Local storageC: MyStorageC = new MyStorageC('PropC');

108. build() {
109. NavDestination() {
110. Column() {
111. // 显示'Hello'
112. NavigationContentMsgStack({ storage: this.storageC })
113. // 显示'PropC'
114. Text(`${this.storageC.propC}`)
115. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
116. .width('80%')
117. .height(40)
118. .margin(20)
119. .onClick(() => {
120. this.pageInfo.pushPathByName('pageOne', null);
121. })

123. }.width('100%').height('100%')
124. }.title('pageThree')
125. .onBackPressed(() => {
126. this.pageInfo.pop();
127. return true;
128. })
129. .onReady((context: NavDestinationContext) => {
130. this.pageInfo = context.pathStack;
131. })
132. }
133. }

135. @ComponentV2
136. struct NavigationContentMsgStack {
137. @Require @Param storage: MyStorageA;

139. build() {
140. Column() {
141. Text(`${this.storage.propA}`)
142. .fontSize(30)
143. .fontWeight(FontWeight.Bold)
144. }
145. }
146. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalTraceCustomize/Index.ets#L15-L162)

### 多实例场景LocalStorage的迁移

为了解决不同Ability之间数据的共享，LocalStorage支持跨Ability存取数据。

对于该场景，V2可结合@ObservedV2+@Trace创建可观测的全局单例对象，定义Map类型存储不同Ability页面的数据，从而实现不同Ability之间数据共享。启动Ability可以参考[specified启动模式](uiability-launch-type.md#specified启动模式)。

**主页面**

```
1. // Index.ets
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

9. build() {
10. Column() {
11. Text('使用文件管理器，使用本应用打开多个PDF')
12. .fontSize($r('app.float.page_text_font_size'))
13. .fontWeight(FontWeight.Bold)
14. .alignRules({
15. center: { anchor: '__container__', align: VerticalAlign.Center },
16. middle: { anchor: '__container__', align: HorizontalAlign.Center }
17. })
18. Button('Jump to PDF_A').onClick(() => {
19. let wantInfo: Want = {
20. bundleName: 'com.samples.paradigmstatemanagement',
21. abilityName: 'PdfEntryAbility',
22. uri: 'PDF_A',
23. parameters: {
24. key: 'PDF_A',
25. value: 'PDF_A-1111111111',
26. }
27. };
28. this.context.startAbility(wantInfo);
29. })
30. Button('Jump to PDF_B').onClick(() => {
31. let wantInfo: Want = {
32. bundleName: 'com.samples.paradigmstatemanagement',
33. abilityName: 'PdfEntryAbility',
34. uri: 'PDF_B',
35. parameters: {
36. key: 'PDF_B',
37. value: 'PDF_B-22222222222',
38. }
39. };
40. this.context.startAbility(wantInfo);
41. })
42. }
43. .height('100%')
44. .width('100%')
45. }
46. }
```

V2:

使用@ObservedV2+@Trace定义全局可观测单例，通过全局的map对象进行数据关联，这种方式需要开发者自行建立唯一的key和value关系。注意单例单独封装存放。

```
1. // model/PDFData.ets
2. @ObservedV2
3. export default class PDFData {
4. // 单例实例
5. private static instance_: PDFData | null = null;
6. @Trace private data: Map<string, string> = new Map();
7. @Trace private flag: string = '';

9. private constructor() {
10. }

12. static getInstance(): PDFData {
13. if (!PDFData.instance_) {
14. PDFData.instance_ = new PDFData();
15. }
16. return PDFData.instance_;
17. }

19. setData(key: string, value: string) {
20. this.data.set(key, value);
21. }

23. getData() {
24. return this.data;
25. }

27. setFlage(value: string) {
28. this.flag = value;
29. }

31. getFlag() {
32. return this.flag;
33. }
34. }
```

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import PDFData from './model/PDFData';

5. export default class PDFAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. // 用单例存储数据
8. const data = this.launchWant.parameters as Record<string, string>;
9. PDFData.getInstance().setData(data.key, data.value);
10. PDFData.getInstance().setFlage(this.launchWant.uri || '');
11. windowStage.loadContent('pages/internalmigrate/LocalStorageMultiInstance/PDF').catch();
12. }
13. }
```

```
1. // PDF.ets
2. import PDFData from './model/PDFData';

4. @Entry
5. @ComponentV2
6. struct PDF {
7. @Local message: string = 'uri';

9. build() {
10. Column() {
11. Text(this.message)
12. .fontSize($r('app.float.page_text_font_size'))
13. .fontWeight(FontWeight.Bold)
14. }
15. .backgroundColor(Color.Pink)
16. .height('100%')
17. .width('100%')
18. }

20. aboutToAppear(): void {
21. // 此处只做简略显示uri，实际功能为打开渲染PDF文件
22. const key: string = PDFData.getInstance().getFlag();
23. // 根据唯一标识，从单例中获取页面对应数据
24. this.message = PDFData.getInstance().getData().get(key) || '';
25. }
26. }
```

## AppStorage->AppStorageV2

上一小节中，对于创建全局@ObserveV2和@Trace装饰实例的改造不适用于跨Ability的数据共享，可以使用AppStorageV2替代。

V1:

AppStorage与应用进程绑定，支持跨[Ability](../harmonyos-references/js-apis-app-ability-ability.md)数据共享。

在下面的示例中，使用@StorageLink，可以使得开发者本地的修改同步回AppStorage中。

```
1. // EntryAbility Index.ets
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @StorageLink('count') count: number = 0;
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Text(`EntryAbility count: ${this.count}`)
13. .fontSize(50)
14. .onClick(() => {
15. this.count++;
16. })
17. Button('Jump to EntryAbility1').onClick(() => {
18. let wantInfo: Want = {
19. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
20. abilityName: 'EntryAbility1'
21. };
22. this.context.startAbility(wantInfo);
23. })
24. }
25. }
26. }
```

[InternalAppStorageV1one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAppStorageV1one.ets#L15-L42)

```
1. // EntryAbility1 Index1.ets
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index1 {
7. @StorageLink('count') count: number = 0;
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Text(`EntryAbility1 count: ${this.count}`)
13. .fontSize(50)
14. .onClick(() => {
15. this.count++;
16. })
17. Button('Jump to EntryAbility').onClick(() => {
18. let wantInfo: Want = {
19. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
20. abilityName: 'EntryAbility'
21. };
22. this.context.startAbility(wantInfo);
23. })
24. }
25. }
26. }
```

[InternalAppStorageV1two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAppStorageV1two.ets#L15-L42)

V2:

可以使用AppStorageV2实现跨Ability共享。

如下面示例：

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { AppStorageV2 } from '@kit.ArkUI';

4. @ObservedV2
5. export class MyStorage {
6. @Trace public count: number = 0;
7. }

9. @Entry
10. @ComponentV2
11. struct Index {
12. @Local storage: MyStorage = AppStorageV2.connect(MyStorage, 'storage', () => new MyStorage())!;
13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

15. build() {
16. Column() {
17. Text(`EntryAbility1 count: ${this.storage.count}`)
18. .fontSize(50)
19. .onClick(() => {
20. this.storage.count++;
21. })
22. Button('Jump to EntryAbility1').onClick(() => {
23. let wantInfo: Want = {
24. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
25. abilityName: 'EntryAbility1'
26. };
27. this.context.startAbility(wantInfo);
28. })
29. }
30. }
31. }
```

[InternalAppStorageV2one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAppStorageV2one.ets#L15-L47)

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { AppStorageV2 } from '@kit.ArkUI';

4. @ObservedV2
5. export class MyStorage {
6. @Trace public count: number = 0;
7. }

9. @Entry
10. @ComponentV2
11. struct Index1 {
12. @Local storage: MyStorage = AppStorageV2.connect(MyStorage, 'storage', () => new MyStorage())!;
13. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

15. build() {
16. Column() {
17. Text(`EntryAbility1 count: ${this.storage.count}`)
18. .fontSize(50)
19. .onClick(() => {
20. this.storage.count++;
21. })
22. Button('Jump to EntryAbility').onClick(() => {
23. let wantInfo: Want = {
24. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
25. abilityName: 'EntryAbility'
26. };
27. this.context.startAbility(wantInfo);
28. })
29. }
30. }
31. }
```

[InternalAppStorageV2two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalAppStorageV2two.ets#L15-L47)

如果开发者需要实现类似于@StorageProp的效果，希望本地的修改不同步回AppStorage，而AppStorage的变化能够通知到使用@StorageProp装饰器的组件，可以参考以下示例对比。

V1：

```
1. // EntryAbility Index.ets
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @StorageProp('count') count: number = 0;
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Text(`EntryAbility count: ${this.count}`)
13. .fontSize(25)
14. .onClick(() => {
15. this.count++;
16. })
17. Button('change Storage Count')
18. .onClick(() => {
19. AppStorage.setOrCreate('count', AppStorage.get<number>('count') as number + 100);
20. })
21. Button('Jump to EntryAbility1').onClick(() => {
22. let wantInfo: Want = {
23. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
24. abilityName: 'EntryAbility1'
25. };
26. this.context.startAbility(wantInfo);
27. })
28. }
29. }
30. }
```

[InternalStoragePropV1one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalStoragePropV1one.ets#L15-L46)

```
1. // EntryAbility1 Index1.ets
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index1 {
7. @StorageProp('count') count: number = 0;
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

10. build() {
11. Column() {
12. Text(`EntryAbility1 count: ${this.count}`)
13. .fontSize(50)
14. .onClick(() => {
15. this.count++;
16. })
17. Button('change Storage Count')
18. .onClick(() => {
19. AppStorage.setOrCreate('count', AppStorage.get<number>('count') as number + 100);
20. })
21. Button('Jump to EntryAbility').onClick(() => {
22. let wantInfo: Want = {
23. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
24. abilityName: 'EntryAbility'
25. };
26. this.context.startAbility(wantInfo);
27. })
28. }
29. }
30. }
```

[InternalStoragePropV1two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalStoragePropV1two.ets#L15-L46)

V2:

开发者可以使用@Monitor和@Local实现类似效果，示例如下。

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { AppStorageV2 } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @ObservedV2
8. export class MyStorage {
9. @Trace public count: number = 0;
10. }

12. @Entry
13. @ComponentV2
14. struct Index {
15. @Local storage: MyStorage = AppStorageV2.connect(MyStorage, 'storage', () => new MyStorage())!;
16. @Local count: number = this.storage.count;
17. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

19. @Monitor('storage.count')
20. onCountChange(mon: IMonitor) {
21. hilog.info(DOMAIN, 'testTag', '%{public}s', `Index1 ${mon.value()?.before} to ${mon.value()?.now}`);
22. this.count = this.storage.count;
23. }

25. build() {
26. Column() {
27. Text(`EntryAbility1 count: ${this.count}`)
28. .fontSize(25)
29. .onClick(() => {
30. this.count++;
31. })
32. Button('change Storage Count')
33. .onClick(() => {
34. this.storage.count += 100;
35. })
36. Button('Jump to EntryAbility1').onClick(() => {
37. let wantInfo: Want = {
38. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
39. abilityName: 'EntryAbility1'
40. };
41. this.context.startAbility(wantInfo);
42. })
43. }
44. }
45. }
```

[InternalStoragePropV2one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalStoragePropV2one.ets#L15-L61)

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { AppStorageV2 } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. @ObservedV2
8. export class MyStorage {
9. @Trace public count: number = 0;
10. }

12. @Entry
13. @ComponentV2
14. struct Index1 {
15. @Local storage: MyStorage = AppStorageV2.connect(MyStorage, 'storage', () => new MyStorage())!;
16. @Local count: number = this.storage.count;
17. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

19. @Monitor('storage.count')
20. onCountChange(mon: IMonitor) {
21. hilog.info(DOMAIN, 'testTag', '%{public}s', `Index1 ${mon.value()?.before} to ${mon.value()?.now}`);
22. this.count = this.storage.count;
23. }

25. build() {
26. Column() {
27. Text(`EntryAbility1 count: ${this.count}`)
28. .fontSize(25)
29. .onClick(() => {
30. this.count++;
31. })
32. Button('change Storage Count')
33. .onClick(() => {
34. this.storage.count += 100;
35. })
36. Button('Jump to EntryAbility').onClick(() => {
37. let wantInfo: Want = {
38. bundleName: 'com.example.myapplication', // 替换成AppScope/app.json5里的bundleName
39. abilityName: 'EntryAbility'
40. };
41. this.context.startAbility(wantInfo);
42. })
43. }
44. }
45. }
```

[InternalStoragePropV2two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalStoragePropV2two.ets#L15-L61)

## Environment->调用Ability接口直接获取系统环境变量

V1中，开发者可以通过Environment来获取环境变量，但Environment获取的结果无法直接使用，需要配合AppStorage才能得到对应环境变量的值。

在切换V2的过程中，开发者无需再通过Environment来获取环境变量，可以直接通过[UIAbilityContext的config属性](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#uiabilitycontext-1)获取系统环境变量。

V1:

以languageCode为例。

```
1. // 将设备languageCode存入AppStorage中
2. Environment.envProp('languageCode', 'en');

4. @Entry
5. @Component
6. struct Index {
7. @StorageProp('languageCode') languageCode: string = 'en';

9. build() {
10. Row() {
11. Column() {
12. // 输出当前设备的languageCode
13. Text(this.languageCode)
14. }
15. }
16. }
17. }
```

[InternalEnvironmentV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalEnvironmentV1.ets#L15-L33)

V2:

封装Env类型来传递多个系统环境变量。

```
1. // Env.ets
2. import { ConfigurationConstant } from '@kit.AbilityKit';

4. export class Env {
5. public language: string | undefined;
6. public colorMode: ConfigurationConstant.ColorMode | undefined;
7. // 字体大小缩放的倍数
8. public fontSizeScale: number | undefined;
9. // 字体粗细缩放的倍数
10. public fontWeightScale: number | undefined;
11. }

13. export let env: Env = new Env();
```

[Env.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/pages/Env.ets#L15-L29)

在onCreate里获取需要的系统环境变量。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { env } from '../pages/Env';

5. export default class EntryAbility extends UIAbility {
6. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
7. env.language = this.context.config.language;
8. env.colorMode = this.context.config.colorMode;
9. env.fontSizeScale = this.context.config.fontSizeScale;
10. env.fontWeightScale = this.context.config.fontWeightScale;
11. }

13. onWindowStageCreate(windowStage: window.WindowStage): void {
14. windowStage.loadContent('pages/Index');
15. }
16. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalEnvironmentV2/EntryAbility.ets#L15-L32)

在页面中获取当前Env的值。

```
1. // Index.ets
2. import { env } from '../pages/Env';

4. @Entry
5. @ComponentV2
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 输出当前设备的环境变量
11. Text(`languageCode: ${env.language}`).fontSize(20)
12. Text(`colorMode: ${env.colorMode}`).fontSize(20)
13. Text(`fontSizeScale: ${env.fontSizeScale}`).fontSize(20)
14. Text(`fontWeightScale: ${env.fontWeightScale}`).fontSize(20)
15. }
16. }
17. }
18. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalEnvironmentV2/Index.ets#L15-L34)

## PersistentStorage->PersistenceV2

V1中PersistentStorage提供了持久化UI数据的能力，而V2则提供了更加方便使用的PersistenceV2接口来替代它。

* PersistentStorage持久化的触发时机依赖AppStorage的观察能力，且与AppStorage耦合，开发者无法自主选择写入或读取持久化数据的时机。
* PersistentStorage使用序列化和反序列化，并没有传入类型，所以在持久化后，会丢失其类型，且对象的属性方法不能持久化。

对于PersistenceV2：

* 与PersistenceV2关联的@ObservedV2对象，其@Trace属性的变化，会触发整个关联对象的自动持久化。
* 开发者也可以调用[PersistenceV2.save()](../harmonyos-references/js-apis-statemanagement.md#save)和[PersistenceV2.globalConnect()](arkts-new-persistencev2.md#使用globalconnect存储数据)来手动触发持久化写入和读取。

V1:

```
1. class Data {
2. public name: string = 'ZhangSan';
3. public id: number = 0;
4. }

6. PersistentStorage.persistProp('numProp', 47);
7. PersistentStorage.persistProp('dataProp', new Data());

9. @Entry
10. @Component
11. struct Index {
12. @StorageLink('numProp') numProp: number = 48;
13. @StorageLink('dataProp') dataProp: Data = new Data();

15. build() {
16. Column() {
17. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
18. Text(`numProp: ${this.numProp}`)
19. .onClick(() => {
20. this.numProp += 1;
21. })
22. .fontSize(30)

24. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
25. Text(`dataProp.name: ${this.dataProp.name}`)
26. .onClick(() => {
27. this.dataProp.name += 'a';
28. })
29. .fontSize(30)
30. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
31. Text(`dataProp.id: ${this.dataProp.id}`)
32. .onClick(() => {
33. this.dataProp.id += 1;
34. })
35. .fontSize(30)

37. }
38. .width('100%')
39. }
40. }
```

[InternalPersistentStorageV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalPersistentStorageV1.ets#L15-L56)

V2:

下面的案例展示了：

* 将PersistentStorage的持久化数据迁移到V2的PersistenceV2中。V2对被@Trace标记的数据可以自动持久化，对于非@Trace数据，需要手动调用save进行持久化。
* 示例中的move函数和需要显示的组件放在了一个ets中，开发者可以定义自己的move函数，并放入合适的位置进行统一迁移操作。

```
1. // 迁移到globalConnect
2. import { PersistenceV2, Type } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. // 接受序列化失败的回调
7. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
8. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
9. });

11. class Data {
12. public name: string = 'ZhangSan';
13. public id: number = 0;
14. }

16. @ObservedV2
17. class V2Data {
18. @Trace public name: string = '';
19. @Trace public id: number = 1;
20. }

22. @ObservedV2
23. export class Sample {
24. // 对于复杂对象需要@Type修饰，确保序列化成功
25. @Type(V2Data)
26. @Trace public num: number = 1;
27. @Trace public V2: V2Data = new V2Data();
28. }

30. // 用于判断是否完成数据迁移的辅助数据
31. @ObservedV2
32. class StorageState {
33. @Trace public isCompleteMoving: boolean = false;
34. }

36. function move() {
37. let movingState = PersistenceV2.globalConnect({ type: StorageState, defaultCreator: () => new StorageState() })!;
38. if (!movingState.isCompleteMoving) {
39. PersistentStorage.persistProp('numProp', 47);
40. PersistentStorage.persistProp('dataProp', new Data());
41. let num = AppStorage.get<number>('numProp')!;
42. let v1Data = AppStorage.get<Data>('dataProp')!;
43. PersistentStorage.deleteProp('numProp');
44. PersistentStorage.deleteProp('dataProp');

46. // V2创建对应数据
47. let migrate = PersistenceV2.globalConnect({
48. type: Sample,
49. key: 'connect2',
50. defaultCreator: () => new Sample()
51. })!; // 使用默认构造函数也可以
52. // 赋值数据，@Trace修饰的会自动保存，对于非@Trace对象，也可以调用save保存，如：PersistenceV2.save('connect2');
53. migrate.num = num;
54. migrate.V2.name = v1Data.name;
55. migrate.V2.id = v1Data.id;

57. // 将迁移标志设置为true
58. movingState.isCompleteMoving = true;
59. }
60. }

62. move();

64. @Entry
65. @ComponentV2
66. struct Page1 {
67. @Local refresh: number = 0;
68. // 使用key:connect2存入数据
69. @Local p: Sample =
70. PersistenceV2.globalConnect({ type: Sample, key: 'connect2', defaultCreator: () => new Sample() })!;

72. build() {
73. Column({ space: 5 }) {
74. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
75. Text(`numProp: ${this.p.num}`)
76. .onClick(() => {
77. this.p.num += 1;
78. })
79. .fontSize(30)

81. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
82. Text(`dataProp.name: ${this.p.V2.name}`)
83. .onClick(() => {
84. this.p.V2.name += 'a';
85. })
86. .fontSize(30)
87. // 应用退出时会保存当前结果。重新启动后，会显示上一次的保存结果
88. Text(`dataProp.id: ${this.p.V2.id}`)
89. .onClick(() => {
90. this.p.V2.id += 1;
91. })
92. .fontSize(30)
93. }
94. .width('100%')
95. }
96. }
```

[InternalPersistentStorageV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/internalmigrate/InternalPersistentStorageV2.ets#L15-L112)
