---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-reusable
title: @Reusable装饰器：V1组件复用
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件复用 > @Reusable装饰器：V1组件复用
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:26dcfeb17fa65f8fa78d63a8dc1d1a64446135993adb3bbb91287d50dcad1161
---

@Reusable装饰的自定义组件支持组件复用。当自定义组件从组件树上移除时，会被存入缓存池，后续在创建相同类型的组件节点时，将优先复用缓存池中的组件对象，从而避免重复创建和销毁，提升性能。

说明

API version 10开始支持@Reusable，支持在ArkTS中使用。

关于组件复用的原理与使用、优化方法、适用场景，请参考[组件复用最佳实践](../best-practices/bpta-component-reuse.md)。

## 概述

@Reusable用于装饰自定义组件，表示该自定义组件具有被复用的能力。

在开发复杂界面时，UI渲染效率是一个需要考虑的问题。例如在长列表快速滑动时，大量列表项的创建和销毁可能导致界面卡顿。组件复用是一种优化UI性能的重要方法。通过复用先前创建并且已经下树的组件对象，降低组件创建和销毁的频率，从而减小计算开销，提升UI渲染效率。

注意

* @Reusable装饰的自定义组件在从组件树中移除时，自定义组件（包含视图节点、组件实例和状态上下文）将被放入其父自定义组件的缓存池中。后续创建新自定义组件节点时，将优先复用缓存池中的节点，从而节约组件重新创建的时间。
* @Reusable提供了[aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)和[aboutToReuse](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoreuse10)两个生命周期，在组件被回收时调用aboutToRecycle，在组件被复用时调用aboutToReuse。开发者可以在这两个生命周期中实现组件回收、复用相关的业务逻辑。
* @Reusable装饰的自定义组件下有子组件时，会在回收和复用时递归调用子组件的aboutToRecycle和aboutToReuse（与子组件是否被@Reusable标记无关），直到遍历完所有子组件。
* 组件复用前后应保持组件结构不变。针对组件结构存在差异的场景，可以使用[reuseId](../harmonyos-references/ts-universal-attributes-reuse-id.md)来区分不同结构的复用组件。

## 限制条件

### 仅用于自定义组件

@Reusable装饰器仅用于自定义组件[@Component](arkts-create-custom-components.md#component)，不可与[@Builder](arkts-builder.md)搭配使用。

@Reusable不支持跟[@ComponentV2](arkts-create-custom-components.md#componentv2)搭配使用，@ComponentV2组件复用推荐[@ReusableV2装饰器](arkts-new-reusablev2.md)。

```
1. import { ComponentContent } from '@kit.ArkUI';

3. // @Builder不能与@Reusable搭配使用。
4. // @Reusable
5. @Builder
6. function buildCreativeLoadingDialog(closedClick: () => void) {
7. Crash();
8. }

10. @Component
11. export struct Crash {
12. build() {
13. Column() {
14. Text('Crash')
15. .fontSize(12)
16. .lineHeight(18)
17. .fontColor(Color.Blue)
18. .margin({
19. left: 6
20. })
21. }.width('100%')
22. .height('100%')
23. .justifyContent(FlexAlign.Center)
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State message: string = 'Hello World';
31. private uiContext = this.getUIContext();

33. build() {
34. RelativeContainer() {
35. Text(this.message)
36. .id('Index')
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .alignRules({
40. center: { anchor: '__container__', align: VerticalAlign.Center },
41. middle: { anchor: '__container__', align: HorizontalAlign.Center }
42. })
43. .onClick(() => {
44. let contentNode = new ComponentContent(this.uiContext, wrapBuilder(buildCreativeLoadingDialog), () => {
45. });
46. this.uiContext.getPromptAction().openCustomDialog(contentNode);
47. })
48. }
49. .height('100%')
50. .width('100%')
51. }
52. }
```

[ReusableForCustomComponents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForCustomComponents.ets#L16-L69)

### 状态变量更新限制

被@Reusable装饰的自定义组件在复用时，会递归调用该自定义组件及其所有子组件的aboutToReuse回调函数。若在子组件的aboutToReuse函数中修改了父组件的状态变量，此次修改将不会生效，请避免此类用法。若需设置父组件的状态变量，可使用setTimeout设置延迟执行，将任务移出组件复用的作用范围，使修改生效。

【反例】

在子组件的aboutToReuse中，直接修改父组件的状态变量。

```
1. class IncorrectBasicDataSource implements IDataSource {
2. private listener: DataChangeListener | undefined = undefined;
3. public dataArray: number[] = [];

5. totalCount(): number {
6. return this.dataArray.length;
7. }

9. getData(index: number): number {
10. return this.dataArray[index];
11. }

13. registerDataChangeListener(listener: DataChangeListener): void {
14. this.listener = listener;
15. }

17. unregisterDataChangeListener(listener: DataChangeListener): void {
18. this.listener = undefined;
19. }
20. }

22. @Entry
23. @Component
24. struct IncorrectIndex {
25. private data: IncorrectBasicDataSource = new IncorrectBasicDataSource();

27. aboutToAppear(): void {
28. for (let index = 1; index < 20; index++) {
29. this.data.dataArray.push(index);
30. }
31. }

33. build() {
34. List() {
35. LazyForEach(this.data, (item: number, index: number) => {
36. ListItem() {
37. IncorrectReuseComponent({ num: item });
38. }
39. }, (item: number, index: number) => index.toString())
40. }.cachedCount(0)
41. }
42. }

44. @Reusable
45. @Component
46. struct IncorrectReuseComponent {
47. @State num: number = 0;

49. aboutToReuse(params: ESObject): void {
50. this.num = params.num;
51. }

53. build() {
54. Column() {
55. Text('ReuseComponent num:' + this.num.toString())
56. IncorrectReuseComponentChild({ num: this.num })
57. Button('plus')
58. .onClick(() => {
59. this.num += 10;
60. })
61. }
62. .height(200)
63. }
64. }

66. @Component
67. struct IncorrectReuseComponentChild {
68. @Link num: number;

70. aboutToReuse(params: ESObject): void {
71. this.num = -1 * params.num;
72. }

74. build() {
75. Text('ReuseComponentChild num:' + this.num.toString())
76. }
77. }
```

[ReusableIncorrectSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableIncorrectSample.ets#L16-L94)

【正例】

在子组件的aboutToReuse中，使用setTimeout，将修改移出组件复用的作用范围。

```
1. class BasicDataSource implements IDataSource {
2. private listener: DataChangeListener | undefined = undefined;
3. public dataArray: number[] = [];

5. totalCount(): number {
6. return this.dataArray.length;
7. }

9. getData(index: number): number {
10. return this.dataArray[index];
11. }

13. registerDataChangeListener(listener: DataChangeListener): void {
14. this.listener = listener;
15. }

17. unregisterDataChangeListener(listener: DataChangeListener): void {
18. this.listener = undefined;
19. }
20. }

22. @Entry
23. @Component
24. struct Index {
25. private data: BasicDataSource = new BasicDataSource();

27. aboutToAppear(): void {
28. for (let index = 1; index <= 20; index++) { // 循环20次
29. this.data.dataArray.push(index);
30. }
31. }

33. build() {
34. List() {
35. LazyForEach(this.data, (item: number, index: number) => {
36. ListItem() {
37. ReuseComponent({ num: item })
38. }
39. }, (item: number, index: number) => index.toString())
40. }.cachedCount(0)
41. }
42. }

44. @Reusable
45. @Component
46. struct ReuseComponent {
47. @State num: number = 0;

49. aboutToReuse(params: ESObject): void {
50. this.num = params.num;
51. }

53. build() {
54. Column() {
55. Text('ReuseComponent num:' + this.num.toString())
56. ReuseComponentChild({ num: this.num })
57. Button('plus')
58. .onClick(() => {
59. this.num += 10; // 每次点击增加10
60. })
61. }
62. .height(200)
63. }
64. }

66. @Component
67. struct ReuseComponentChild {
68. @Link num: number;

70. aboutToReuse(params: ESObject): void {
71. setTimeout(() => {
72. this.num = -1 * params.num;
73. }, 1)
74. }

76. build() {
77. Text('ReuseComponentChild num:' + this.num.toString());
78. }
79. }
```

[ReusableCorrectSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableCorrectSample.ets#L16-L96)

### 组件结构需一致

被@Reusable装饰的自定义组件在复用前后，应保持组件的结构不变。否则，会在复用过程中创建或销毁子组件，降低复用效率和性能，甚至造成应用行为异常。

对于复用过程中创建的子组件，框架会在其创建后依次调用aboutToReuse方法和aboutToAppear方法。在调用aboutToReuse方法时，由于其aboutToAppear方法还未执行，且内部子组件还未创建，因此aboutToReuse方法中依赖aboutToAppear方法执行结果，或依赖内部子组件状态的相关操作会引起预期外的行为。在调用aboutToReuse方法后，框架会再调用aboutToAppear方法并初始化组件。

针对组件结构存在差异的场景，开发者需要通过设定不同的reuseId来进行区分，具体方式请参考[多种条目类型使用场景](arkts-reusable.md#多种条目类型使用场景)。

【反例】

组件结构存在差异，但未通过reuseId进行区分。

以下示例中，先点击“show/hide branch A”按钮，组件被回收，再点击“show/hide branch B”按钮，组件被复用。子组件ReusableChildB在复用过程中被创建，aboutToReuse方法和aboutToAppear方法被依次调用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_ReusableComponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'ReusableComponent_';

7. @Entry
8. @Component
9. struct Index {
10. @State showBranchA: boolean = true;
11. @State showBranchB: boolean = false;

13. build() {
14. Column({ space: 5 }) {
15. Button('show/hide branch A')
16. .onClick(() => {
17. this.showBranchA = !this.showBranchA;
18. })
19. if (this.showBranchA) {
20. ReusableComponent({ flag: true })
21. }
22. Button('show/hide branch B')
23. .onClick(() => {
24. this.showBranchB = !this.showBranchB;
25. })
26. if (this.showBranchB) {
27. ReusableComponent({ flag: false })
28. }
29. }
30. }
31. }

33. @Reusable
34. @Component
35. struct ReusableComponent {
36. @Require @Prop flag: boolean = true;

38. aboutToAppear() {
39. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToAppear');
40. }

42. aboutToReuse(params: ESObject) {
43. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToReuse');
44. this.flag = params.flag;
45. }

47. build() {
48. Column({ space: 5 }) {
49. Text('ReusableComponent')
50. if (this.flag) {
51. ReusableChildA()
52. } else {
53. ReusableChildB()
54. }
55. }.border({ width: 1 })
56. }
57. }

59. @Component
60. struct ReusableChildA {
61. aboutToAppear() {
62. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToAppear');
63. }

65. aboutToReuse() {
66. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToReuse');
67. }

69. build() {
70. Text('ReusableChildA')
71. .border({ width: 1 })
72. }
73. }

75. @Component
76. struct ReusableChildB {
77. aboutToAppear() {
78. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToAppear');
79. }

81. aboutToReuse() {
82. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToReuse');
83. }

85. build() {
86. Text('ReusableChildB')
87. .border({ width: 1 })
88. }
89. }
```

[ReusableForIncorrectReuseId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForIncorrectReuseId.ets#L16-L106)

【正例】

组件结构存在差异，通过reuseId进行区分。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_ReusableComponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'ReusableComponent_';

7. @Entry
8. @Component
9. struct Index {
10. @State showBranchA: boolean = true;
11. @State showBranchB: boolean = false;

13. build() {
14. Column({ space: 5 }) {
15. Button('show/hide branch A')
16. .onClick(() => {
17. this.showBranchA = !this.showBranchA;
18. })
19. if (this.showBranchA) {
20. ReusableComponent({ flag: true })
21. .reuseId('ReuseA') // 通过reuseId区分不同结构的复用组件
22. }
23. Button('show/hide branch B')
24. .onClick(() => {
25. this.showBranchB = !this.showBranchB;
26. })
27. if (this.showBranchB) {
28. ReusableComponent({ flag: false })
29. .reuseId('ReuseB') // 通过reuseId区分不同结构的复用组件
30. }
31. }
32. }
33. }

35. @Reusable
36. @Component
37. struct ReusableComponent {
38. @Require @Prop flag: boolean = true;

40. aboutToAppear() {
41. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToAppear');
42. }

44. aboutToReuse(params: ESObject) {
45. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableComponent aboutToReuse');
46. this.flag = params.flag;
47. }

49. build() {
50. Column({ space: 5 }) {
51. Text('ReusableComponent')
52. if (this.flag) {
53. ReusableChildA()
54. } else {
55. ReusableChildB()
56. }
57. }.border({ width: 1 })
58. }
59. }

61. @Component
62. struct ReusableChildA {
63. aboutToAppear() {
64. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToAppear');
65. }

67. aboutToReuse() {
68. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildA aboutToReuse');
69. }

71. build() {
72. Text('ReusableChildA')
73. .border({ width: 1 })
74. }
75. }

77. @Component
78. struct ReusableChildB {
79. aboutToAppear() {
80. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToAppear');
81. }

83. aboutToReuse() {
84. hilog.info(DOMAIN, TAG, BUNDLE + 'ReusableChildB aboutToReuse');
85. }

87. build() {
88. Text('ReusableChildB')
89. .border({ width: 1 })
90. }
91. }
```

[ReusableForReuseId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForReuseId.ets#L16-L108)

### 不支持ComponentContent

ComponentContent不支持传入@Reusable装饰器装饰的自定义组件。

```
1. import { ComponentContent } from '@kit.ArkUI';

3. @Builder
4. function buildCreativeLoadingDialog(closedClick: () => void) {
5. Crash();
6. }

8. // 如果注释掉就可以正常弹出弹窗，如果加上@Reusable就直接crash。
9. @Reusable
10. @Component
11. export struct Crash {
12. build() {
13. Column() {
14. Text('Crash')
15. .fontSize(12)
16. .lineHeight(18)
17. .fontColor(Color.Blue)
18. .margin({
19. left: 6
20. })
21. }.width('100%')
22. .height('100%')
23. .justifyContent(FlexAlign.Center)
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State message: string = 'Hello World';
31. private uiContext = this.getUIContext();

33. build() {
34. RelativeContainer() {
35. Text(this.message)
36. .id('Index')
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .alignRules({
40. center: { anchor: '__container__', align: VerticalAlign.Center },
41. middle: { anchor: '__container__', align: HorizontalAlign.Center }
42. })
43. .onClick(() => {
44. // ComponentContent底层是BuilderNode，BuilderNode不支持传入@Reusable注解的自定义组件。
45. let contentNode = new ComponentContent(this.uiContext, wrapBuilder(buildCreativeLoadingDialog), () => {
46. });
47. this.uiContext.getPromptAction().openCustomDialog(contentNode);
48. })
49. }
50. .height('100%')
51. .width('100%')
52. }
53. }
```

[ComponentContentNotSupportReusable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ComponentContentNotSupportReusable.ets#L16-L70)

### 不建议嵌套使用

@Reusable装饰器不建议嵌套使用，会增加内存，降低复用效率，加大维护难度。嵌套使用会导致额外缓存池的生成，各缓存池拥有相同树状结构，复用效率低下。此外，嵌套使用会使生命周期管理复杂，资源和变量共享困难。

## 使用场景

### 动态布局更新

重复创建与移除视图可能引起频繁的布局计算，从而影响帧率。采用组件复用可以避免不必要的视图创建与布局计算，提升性能。

以下示例中，将Child自定义组件标记为复用组件，通过Button点击更新Child，触发复用。

```
1. // xxx.ets
2. export class Message {
3. public value: string | undefined;

5. constructor(value: string) {
6. this.value = value;
7. }
8. }

10. @Entry
11. @Component
12. struct Index {
13. @State switch: boolean = true;

15. build() {
16. Column() {
17. Button('Hello')
18. .fontSize(30)
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. this.switch = !this.switch;
22. })
23. if (this.switch) {
24. // 如果只有一个复用的组件，可以不用设置reuseId。
25. Child({ message: new Message('Child') })
26. .reuseId('Child');
27. }
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }

34. @Reusable
35. @Component
36. struct Child {
37. @State message: Message = new Message('AboutToReuse');

39. aboutToReuse(params: Record<string, ESObject>) {
40. this.message = params.message as Message;
41. }

43. build() {
44. Column() {
45. Text(this.message.value)
46. .fontSize(30)
47. }
48. .borderWidth(1)
49. .height(100)
50. }
51. }
```

[DynamicLayoutUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/DynamicLayoutUpdate.ets#L16-L68)

### 列表滚动配合LazyForEach使用

当应用展示大量数据的列表并进行滚动操作时，频繁创建和销毁列表项视图可能导致卡顿和性能问题。使用列表组件的组件复用机制可以重用已创建的列表项视图，提高滚动流畅度。

以下示例代码将CardView自定义组件标记为复用组件，List上下滑动，触发CardView复用。

```
1. class MyDataSource implements IDataSource {
2. private dataArray: string[] = [];
3. private listener: DataChangeListener | undefined;

5. public totalCount(): number {
6. return this.dataArray.length;
7. }

9. public getData(index: number): string {
10. return this.dataArray[index];
11. }

13. public pushData(data: string): void {
14. this.dataArray.push(data);
15. }

17. public reloadListener(): void {
18. this.listener?.onDataReloaded();
19. }

21. public registerDataChangeListener(listener: DataChangeListener): void {
22. this.listener = listener;
23. }

25. public unregisterDataChangeListener(listener: DataChangeListener): void {
26. this.listener = undefined;
27. }
28. }

30. @Entry
31. @Component
32. struct ReuseDemo {
33. private data: MyDataSource = new MyDataSource();

35. aboutToAppear() {
36. for (let i = 1; i <= 1000; i++) { // 循环1000次
37. this.data.pushData(i + '');
38. }
39. }

41. build() {
42. Column() {
43. List() {
44. LazyForEach(this.data, (item: string) => {
45. ListItem() {
46. CardView({ item: item });
47. }
48. }, (item: string) => item)
49. }
50. }
51. }
52. }

54. // 复用组件
55. @Reusable
56. @Component
57. export struct CardView {
58. // 被@State修饰的变量item才能更新，未被@State修饰的变量不会更新。
59. @State item: string = '';

61. aboutToReuse(params: Record<string, Object>): void {
62. this.item = params.item as string;
63. }

65. build() {
66. Column() {
67. Text(this.item)
68. .fontSize(30)
69. }
70. .borderWidth(1)
71. .height(100)
72. }
73. }
```

[ListScrollingWithLazyForEach.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ListScrollingWithLazyForEach.ets#L16-L91)

### 列表滚动-if使用场景

以下示例代码将OneMoment自定义组件标记为复用组件。当List上下滑动时，会触发OneMoment的复用。设置reuseId可为复用组件分配复用组，相同reuseId的组件将在同一复用组中复用。单个复用组件无需设置reuseId。使用reuseId标识复用组件，可避免重复执行if语句的删除和重新创建逻辑，提高复用效率和性能。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_ReusableComponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'ReusableComponent_';

7. @Entry
8. @Component
9. struct Index {
10. private dataSource = new MyDataSource<FriendMoment>();

12. aboutToAppear(): void {
13. for (let i = 0; i < 20; i++) { // 循环20次
14. let title = i + 1 + 'test_if';
15. // 请开发者自行在src/main/resources/base/media路径下添加app.media.app_icon图片，否则运行时会因资源缺失而Image空白。
16. this.dataSource.pushData(new FriendMoment(i.toString(), title, 'app.media.app_icon'));
17. }

19. for (let i = 0; i < 50; i++) { // 循环50次
20. let title = i + 1 + 'test_if';
21. this.dataSource.pushData(new FriendMoment(i.toString(), title, ''));
22. }
23. }

25. build() {
26. Column() {
27. // TopBar()
28. List({ space: 3 }) {
29. LazyForEach(this.dataSource, (moment: FriendMoment) => {
30. ListItem() {
31. // 使用reuseId进行组件复用的控制。
32. OneMoment({ moment: moment })
33. .reuseId((moment.image !== '') ? 'withImage' : 'noImage');
34. }
35. }, (moment: FriendMoment) => moment.id)
36. }
37. .cachedCount(0)
38. }
39. }
40. }

42. class FriendMoment {
43. public id: string = '';
44. public text: string = '';
45. public title: string = '';
46. public image: string = '';
47. public answers: Array<ResourceStr> = [];

49. constructor(id: string, title: string, image: string) {
50. this.text = id;
51. this.title = title;
52. this.image = image;
53. }
54. }

56. @Reusable
57. @Component
58. export struct OneMoment {
59. @Prop moment: FriendMoment;

61. // 复用id相同的组件才能触发复用。
62. aboutToReuse(params: ESObject): void {
63. hilog.info(DOMAIN, TAG, BUNDLE + '=====aboutToReuse====OneMoment==复用了==' + this.moment.text);
64. }

66. build() {
67. Column() {
68. Text(this.moment.text)
69. // if分支判断。
70. if (this.moment.image !== '') {
71. Flex({ wrap: FlexWrap.Wrap }) {
72. Image($r(this.moment.image)).height(50).width(50);
73. Image($r(this.moment.image)).height(50).width(50);
74. Image($r(this.moment.image)).height(50).width(50);
75. Image($r(this.moment.image)).height(50).width(50);
76. }
77. }
78. }
79. }
80. }

82. class BasicDataSource<T> implements IDataSource {
83. private listeners: DataChangeListener[] = [];
84. private originDataArray: T[] = [];

86. public totalCount(): number {
87. return 0;
88. }

90. public getData(index: number): T {
91. return this.originDataArray[index];
92. }

94. registerDataChangeListener(listener: DataChangeListener): void {
95. if (this.listeners.indexOf(listener) < 0) {
96. this.listeners.push(listener);
97. }
98. }

100. unregisterDataChangeListener(listener: DataChangeListener): void {
101. const pos = this.listeners.indexOf(listener);
102. if (pos >= 0) {
103. this.listeners.splice(pos, 1);
104. }
105. }

107. notifyDataAdd(index: number): void {
108. this.listeners.forEach(listener => {
109. listener.onDataAdd(index);
110. });
111. }
112. }

114. export class MyDataSource<T> extends BasicDataSource<T> {
115. private dataArray: T[] = [];

117. public totalCount(): number {
118. return this.dataArray.length;
119. }

121. public getData(index: number): T {
122. return this.dataArray[index];
123. }

125. public pushData(data: T): void {
126. this.dataArray.push(data);
127. this.notifyDataAdd(this.dataArray.length - 1);
128. }
129. }
```

[ListScrollingWithIfStatements.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ListScrollingWithIfStatements.ets#L16-L145)

### 列表滚动-Foreach使用场景

使用Foreach创建可复用的自定义组件，由于Foreach渲染控制语法的全展开属性，导致复用组件无法复用。示例中点击update，数据刷新成功，但滑动列表时，ListItemView无法复用。点击clear，再次点击update，ListItemView复用成功，因为一帧内重复创建多个已被销毁的自定义组件。

```
1. // xxx.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG = '[Sample_ReusableComponent]';
5. const DOMAIN = 0xF811;
6. const BUNDLE = 'ReusableComponent_';

8. class MyDataSource implements IDataSource {
9. private dataArray: string[] = [];

11. public totalCount(): number {
12. return this.dataArray.length;
13. }

15. public getData(index: number): string {
16. return this.dataArray[index];
17. }

19. public pushData(data: string): void {
20. this.dataArray.push(data);
21. }

23. public registerDataChangeListener(listener: DataChangeListener): void {
24. }

26. public unregisterDataChangeListener(listener: DataChangeListener): void {
27. }
28. }

30. @Entry
31. @Component
32. struct Index {
33. private data: MyDataSource = new MyDataSource();
34. private data02: MyDataSource = new MyDataSource();
35. @State isShow: boolean = true;
36. @State dataSource: ListItemObject[] = [];

38. aboutToAppear() {
39. for (let i = 0; i < 100; i++) { // 循环100次
40. this.data.pushData(i.toString());
41. }

43. for (let i = 30; i <= 80; i++) { // 循环50次
44. this.data02.pushData(i.toString());
45. }
46. }

48. build() {
49. Column() {
50. Row() {
51. Button('clear').onClick(() => {
52. for (let i = 1; i <= 50; i++) { // 循环50次
53. this.dataSource.pop();
54. }
55. }).height(40)

57. Button('update').onClick(() => {
58. for (let i = 1; i <= 50; i++) { // 循环50次
59. let obj = new ListItemObject();
60. obj.id = i;
61. obj.uuid = Math.random().toString();
62. obj.isExpand = false;
63. this.dataSource.push(obj);
64. }
65. }).height(40)
66. }

68. List({ space: 10 }) {
69. ForEach(this.dataSource, (item: ListItemObject) => {
70. ListItem() {
71. ListItemView({
72. obj: item
73. })
74. }
75. }, (item: ListItemObject) => {
76. return item.uuid.toString();
77. })

79. }.cachedCount(0)
80. .width('100%')
81. .height('100%')
82. }
83. }
84. }

86. @Reusable
87. @Component
88. struct ListItemView {
89. @ObjectLink obj: ListItemObject;
90. @State item: string = '';

92. aboutToAppear(): void {
93. // 点击 update，首次进入，上下滑动，由于Foreach折叠展开属性，无法复用。
94. hilog.info(DOMAIN, TAG, BUNDLE + '=====aboutToAppear=====ListItemView==创建了==' + this.item);
95. }

97. aboutToReuse(params: ESObject) {
98. this.item = params.item;
99. // 点击clear，再次update，复用成功。
100. // 符合一帧内重复创建多个已被销毁的自定义组件。
101. hilog.info(DOMAIN, TAG, BUNDLE + '=====aboutToReuse====ListItemView==复用了==' + this.item);
102. }

104. build() {
105. Column({ space: 10 }) {
106. Text(`${this.obj.id}.标题`)
107. .fontSize(16)
108. .fontColor('#000000')
109. .padding({
110. top: 20,
111. bottom: 20,
112. })

114. if (this.obj.isExpand) {
115. Text('')
116. .fontSize(14)
117. .fontColor('#999999')
118. }
119. }
120. .width('100%')
121. .borderRadius(10)
122. .backgroundColor(Color.White)
123. .padding(15)
124. .onClick(() => {
125. this.obj.isExpand = !this.obj.isExpand;
126. })
127. }
128. }

130. @Observed
131. class ListItemObject {
132. public uuid: string = '';
133. public id: number = 0;
134. public isExpand: boolean = false;
135. }
```

[ListScrollingWithForEach.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ListScrollingWithForEach.ets#L16-L152)

### Grid使用场景

示例中使用@Reusable装饰器修饰GridItem中的自定义组件ReusableChildComponent，即表示其具备组件复用的能力。

使用aboutToReuse可以在Grid滑动时，从复用缓存中加入到组件树之前触发，从而更新组件状态变量，展示正确内容。

需要注意的是无需在aboutToReuse中对[@Link](arkts-link.md)、[@StorageLink](arkts-appstorage.md#storagelink)、[@ObjectLink](arkts-observed-and-objectlink.md)、[@Consume](arkts-provide-and-consume.md)等自动更新值的状态变量进行更新，可能触发不必要的组件刷新。

```
1. // MyDataSource类实现IDataSource接口。
2. class MyDataSource implements IDataSource {
3. private dataArray: number[] = [];

5. public pushData(data: number): void {
6. this.dataArray.push(data);
7. }

9. // 数据源的数据总量。
10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. // 返回指定索引位置的数据。
15. public getData(index: number): number {
16. return this.dataArray[index];
17. }

19. registerDataChangeListener(listener: DataChangeListener): void {
20. }

22. unregisterDataChangeListener(listener: DataChangeListener): void {
23. }
24. }

26. @Entry
27. @Component
28. struct MyComponent {
29. // 数据源。
30. private data: MyDataSource = new MyDataSource();

32. aboutToAppear() {
33. for (let i = 1; i <= 1000; i++) { // 循环1000次
34. this.data.pushData(i);
35. }
36. }

38. build() {
39. Column({ space: 5 }) {
40. Grid() {
41. LazyForEach(this.data, (item: number) => {
42. GridItem() {
43. // 使用可复用自定义组件。
44. ReusableChildComponent({ item: item });
45. }
46. }, (item: string) => item)
47. }
48. .cachedCount(2) // 设置GridItem的缓存数量。
49. .columnsTemplate('1fr 1fr 1fr')
50. .columnsGap(10)
51. .rowsGap(10)
52. .margin(10)
53. .height(500)
54. .backgroundColor(0xFAEEE0)
55. }
56. }
57. }

59. @Reusable
60. @Component
61. struct ReusableChildComponent {
62. @State item: number = 0;

64. // aboutToReuse从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容。
65. // aboutToReuse参数类型已不支持any，这里使用Record指定明确的数据类型。Record用于构造一个对象类型，其属性键为Keys，属性值为Type。
66. aboutToReuse(params: Record<string, number>) {
67. this.item = params.item;
68. }

70. build() {
71. Column() {
72. // 请开发者自行在src/main/resources/base/media路径下添加app.media.app_icon图片，否则运行时会因资源缺失而报错。
73. Image($r('app.media.app_icon'))
74. .objectFit(ImageFit.Fill)
75. .layoutWeight(1)
76. Text(`图片${this.item}`)
77. .fontSize(16)
78. .textAlign(TextAlign.Center)
79. }
80. .width('100%')
81. .height(120)
82. .backgroundColor(0xF9CF93)
83. }
84. }
```

[ReusableForGridUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForGridUsageScenario.ets#L16-L101)

### WaterFlow使用场景

* 在WaterFlow滑动场景中，FlowItem及其子组件频繁创建和销毁。可以将FlowItem中的组件封装成自定义组件，并使用@Reusable装饰器修饰，实现组件复用。

  ```
  1. import { hilog } from '@kit.PerformanceAnalysisKit';

  3. const TAG = '[Sample_ReusableComponent]';
  4. const DOMAIN = 0xF811;
  5. const BUNDLE = 'ReusableComponent_';

  7. class WaterFlowDataSource implements IDataSource {
  8. private dataArray: number[] = [];
  9. private listeners: DataChangeListener[] = [];

  11. constructor() {
  12. for (let i = 0; i < 60; i++) { // 循环60次
  13. this.dataArray.push(i);
  14. }
  15. }

  17. // 获取索引对应的数据。
  18. public getData(index: number): number {
  19. return this.dataArray[index];
  20. }

  22. // 通知控制器增加数据。
  23. notifyDataAdd(index: number): void {
  24. this.listeners.forEach(listener => {
  25. listener.onDataAdd(index);
  26. });
  27. }

  29. // 获取数据总数。
  30. public totalCount(): number {
  31. return this.dataArray.length;
  32. }

  34. // 注册改变数据的控制器。
  35. registerDataChangeListener(listener: DataChangeListener): void {
  36. if (this.listeners.indexOf(listener) < 0) {
  37. this.listeners.push(listener);
  38. }
  39. }

  41. // 注销改变数据的控制器。
  42. unregisterDataChangeListener(listener: DataChangeListener): void {
  43. const pos = this.listeners.indexOf(listener);
  44. if (pos >= 0) {
  45. this.listeners.splice(pos, 1);
  46. }
  47. }

  49. // 在数据尾部增加一个元素。
  50. public addLastItem(): void {
  51. this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
  52. this.notifyDataAdd(this.dataArray.length - 1);
  53. }
  54. }

  56. @Reusable
  57. @Component
  58. struct ReusableFlowItem {
  59. @State item: number = 0;

  61. // 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容。
  62. aboutToReuse(params: ESObject) {
  63. this.item = params.item;
  64. hilog.info(DOMAIN, TAG, BUNDLE + '=====aboutToReuse====FlowItem==复用了==' + this.item);
  65. }

  67. aboutToRecycle(): void {
  68. hilog.info(DOMAIN, TAG, BUNDLE + '=====aboutToRecycle====FlowItem==回收了==' + this.item);
  69. }

  71. build() {
  72. // 请开发者自行在src/main/resources/base/media路径下添加app.media.app_icon图片，否则运行时会因资源缺失而报错。
  73. Column() {
  74. Text('N' + this.item).fontSize(24).height('26').margin(10);
  75. Image($r('app.media.app_icon'))
  76. .objectFit(ImageFit.Cover)
  77. .width(50)
  78. .height(50);
  79. }
  80. }
  81. }

  83. @Entry
  84. @Component
  85. struct Index {
  86. @State minSize: number = 50; // 最小值50
  87. @State maxSize: number = 80; // 最大值80
  88. @State fontSize: number = 24; // 字体大小为24
  89. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  90. scroller: Scroller = new Scroller();
  91. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  92. private itemWidthArray: number[] = [];
  93. private itemHeightArray: number[] = [];

  95. // 计算flow item宽/高。
  96. getSize() {
  97. let ret = Math.floor(Math.random() * this.maxSize);
  98. return (ret > this.minSize ? ret : this.minSize);
  99. }

  101. // 保存flow item宽/高。
  102. getItemSizeArray() {
  103. for (let i = 0; i < 100; i++) { // 循环100次
  104. this.itemWidthArray.push(this.getSize());
  105. this.itemHeightArray.push(this.getSize());
  106. }
  107. }

  109. aboutToAppear() {
  110. this.getItemSizeArray();
  111. }

  113. build() {
  114. Stack({ alignContent: Alignment.TopStart }) {
  115. Column({ space: 2 }) {
  116. Button('back top')
  117. .height('5%')
  118. .onClick(() => {
  119. // 点击后回到顶部。
  120. this.scroller.scrollEdge(Edge.Top);
  121. })
  122. WaterFlow({ scroller: this.scroller }) {
  123. LazyForEach(this.dataSource, (item: number) => {
  124. FlowItem() {
  125. ReusableFlowItem({ item: item })
  126. }.onAppear(() => {
  127. if (item + 20 == this.dataSource.totalCount()) { // 阈值为20
  128. for (let i = 0; i < 50; i++) { // 循环50次
  129. this.dataSource.addLastItem();
  130. }
  131. }
  132. })

  134. })
  135. }
  136. }
  137. }
  138. }
  139. }
  ```

  [ReusableForWaterFlowUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForWaterFlowUsageScenario.ets#L16-L156)

### Swiper使用场景

* 在Swiper滑动场景中，条目中的子组件频繁创建和销毁。可以将这些子组件封装成自定义组件，并使用@Reusable装饰器修饰，以实现组件复用。

  ```
  1. @Entry
  2. @Component
  3. struct Index {
  4. private dataSource = new MyDataSource<Question>();

  6. aboutToAppear(): void {
  7. for (let i = 0; i < 1000; i++) { // 循环1000次
  8. let title = i + 1 + 'test_swiper';
  9. let answers = ['test1', 'test2', 'test3', 'test4'];
  10. // 请开发者自行在src/main/resources/base/media路径下添加app.media.app_icon图片，否则运行时会因资源缺失而报错。
  11. this.dataSource.pushData(new Question(i.toString(), title, $r('app.media.app_icon'), answers));
  12. }
  13. }

  15. build() {
  16. Column({ space: 5 }) {
  17. Swiper() {
  18. LazyForEach(this.dataSource, (item: Question) => {
  19. QuestionSwiperItem({ itemData: item });
  20. }, (item: Question) => item.id)
  21. }
  22. }
  23. .width('100%')
  24. .margin({ top: 5 })
  25. }
  26. }

  28. class Question {
  29. public id: string = '';
  30. public title: ResourceStr = '';
  31. public image: ResourceStr = '';
  32. public answers: Array<ResourceStr> = [];

  34. constructor(id: string, title: ResourceStr, image: ResourceStr, answers: Array<ResourceStr>) {
  35. this.id = id;
  36. this.title = title;
  37. this.image = image;
  38. this.answers = answers;
  39. }
  40. }

  42. @Reusable
  43. @Component
  44. struct QuestionSwiperItem {
  45. @State itemData: Question | null = null;

  47. aboutToReuse(params: Record<string, Object>): void {
  48. this.itemData = params.itemData as Question;
  49. }

  51. build() {
  52. Column() {
  53. Text(this.itemData?.title)
  54. .fontSize(18)
  55. .fontColor($r('sys.color.ohos_id_color_primary'))
  56. .alignSelf(ItemAlign.Start)
  57. .margin({
  58. top: 10,
  59. bottom: 16
  60. })

  62. Image(this.itemData?.image)
  63. .width('100%')
  64. .borderRadius(12)
  65. .objectFit(ImageFit.Contain)
  66. .margin({
  67. bottom: 16
  68. })
  69. .height(80)
  70. .width(80)

  72. Column({ space: 16 }) {
  73. ForEach(this.itemData?.answers, (item: Resource) => {
  74. Text(item)
  75. .fontSize(16)
  76. .fontColor($r('sys.color.ohos_id_color_primary'))
  77. }, (item: ResourceStr) => JSON.stringify(item))
  78. }
  79. .width('100%')
  80. .alignItems(HorizontalAlign.Start)
  81. }
  82. .width('100%')
  83. .padding({
  84. left: 16,
  85. right: 16
  86. })
  87. }
  88. }

  90. class BasicDataSource<T> implements IDataSource {
  91. private listeners: DataChangeListener[] = [];
  92. private originDataArray: T[] = [];

  94. public totalCount(): number {
  95. return 0;
  96. }

  98. public getData(index: number): T {
  99. return this.originDataArray[index];
  100. }

  102. registerDataChangeListener(listener: DataChangeListener): void {
  103. if (this.listeners.indexOf(listener) < 0) {
  104. this.listeners.push(listener);
  105. }
  106. }

  108. unregisterDataChangeListener(listener: DataChangeListener): void {
  109. const pos = this.listeners.indexOf(listener);
  110. if (pos >= 0) {
  111. this.listeners.splice(pos, 1);
  112. }
  113. }

  115. notifyDataAdd(index: number): void {
  116. this.listeners.forEach(listener => {
  117. listener.onDataAdd(index);
  118. });
  119. }
  120. }

  122. export class MyDataSource<T> extends BasicDataSource<T> {
  123. private dataArray: T[] = [];

  125. public totalCount(): number {
  126. return this.dataArray.length;
  127. }

  129. public getData(index: number): T {
  130. return this.dataArray[index];
  131. }

  133. public pushData(data: T): void {
  134. this.dataArray.push(data);
  135. this.notifyDataAdd(this.dataArray.length - 1);
  136. }
  137. }
  ```

  [ReusableForSwiperUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForSwiperUsageScenario.ets#L16-L154)

### 列表滚动-ListItemGroup使用场景

* 可以视作特殊List滑动场景，将ListItem需要移除重建的子组件封装成自定义组件，并使用@Reusable装饰器修饰，使其具备组件复用能力。

  ```
  1. @Entry
  2. @Component
  3. struct ListItemGroupAndReusable {
  4. data: DataSrc2 = new DataSrc2();

  6. @Builder
  7. itemHead(text: string) {
  8. Text(text)
  9. .fontSize(20)
  10. .backgroundColor(0xAABBCC)
  11. .width('100%')
  12. .padding(10)
  13. }

  15. aboutToAppear() {
  16. for (let i = 0; i < 10000; i++) { // 循环10000次
  17. let data1 = new DataSrc1();
  18. for (let j = 0; j < 12; j++) { // 循环12次
  19. data1.data.push(`测试条目数据: ${i} - ${j}`);
  20. }
  21. this.data.data.push(data1);
  22. }
  23. }

  25. build() {
  26. Stack() {
  27. List() {
  28. LazyForEach(this.data, (item: DataSrc1, index: number) => {
  29. ListItemGroup({ header: this.itemHead(index.toString()) }) {
  30. LazyForEach(item, (ii: string, index: number) => {
  31. ListItem() {
  32. Inner({ str: ii });
  33. }
  34. })
  35. }
  36. .width('100%')
  37. .height('60vp')
  38. })
  39. }
  40. }
  41. .width('100%')
  42. .height('100%')
  43. }
  44. }

  46. @Reusable
  47. @Component
  48. struct Inner {
  49. @State str: string = '';

  51. aboutToReuse(param: ESObject) {
  52. this.str = param.str;
  53. }

  55. build() {
  56. Text(this.str);
  57. }
  58. }

  60. class DataSrc1 implements IDataSource {
  61. public listeners: DataChangeListener[] = [];
  62. public data: string[] = [];

  64. public totalCount(): number {
  65. return this.data.length;
  66. }

  68. public getData(index: number): string {
  69. return this.data[index];
  70. }

  72. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听。
  73. registerDataChangeListener(listener: DataChangeListener): void {
  74. if (this.listeners.indexOf(listener) < 0) {
  75. this.listeners.push(listener);
  76. }
  77. }

  79. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听。
  80. unregisterDataChangeListener(listener: DataChangeListener): void {
  81. const pos = this.listeners.indexOf(listener);
  82. if (pos >= 0) {
  83. this.listeners.splice(pos, 1);
  84. }
  85. }

  87. // 通知LazyForEach组件需要重载所有子组件。
  88. notifyDataReload(): void {
  89. this.listeners.forEach(listener => {
  90. listener.onDataReloaded();
  91. });
  92. }

  94. // 通知LazyForEach组件需要在index对应索引处添加子组件。
  95. notifyDataAdd(index: number): void {
  96. this.listeners.forEach(listener => {
  97. listener.onDataAdd(index);
  98. });
  99. }

  101. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件。
  102. notifyDataChange(index: number): void {
  103. this.listeners.forEach(listener => {
  104. listener.onDataChange(index);
  105. });
  106. }

  108. // 通知LazyForEach组件需要在index对应索引处删除该子组件。
  109. notifyDataDelete(index: number): void {
  110. this.listeners.forEach(listener => {
  111. listener.onDataDelete(index);
  112. });
  113. }

  115. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换。
  116. notifyDataMove(from: number, to: number): void {
  117. this.listeners.forEach(listener => {
  118. listener.onDataMove(from, to);
  119. });
  120. }
  121. }

  123. class DataSrc2 implements IDataSource {
  124. public listeners: DataChangeListener[] = [];
  125. public data: DataSrc1[] = [];

  127. public totalCount(): number {
  128. return this.data.length;
  129. }

  131. public getData(index: number): DataSrc1 {
  132. return this.data[index];
  133. }

  135. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听。
  136. registerDataChangeListener(listener: DataChangeListener): void {
  137. if (this.listeners.indexOf(listener) < 0) {
  138. this.listeners.push(listener);
  139. }
  140. }

  142. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听。
  143. unregisterDataChangeListener(listener: DataChangeListener): void {
  144. const pos = this.listeners.indexOf(listener);
  145. if (pos >= 0) {
  146. this.listeners.splice(pos, 1);
  147. }
  148. }

  150. // 通知LazyForEach组件需要重载所有子组件。
  151. notifyDataReload(): void {
  152. this.listeners.forEach(listener => {
  153. listener.onDataReloaded();
  154. });
  155. }

  157. // 通知LazyForEach组件需要在index对应索引处添加子组件。
  158. notifyDataAdd(index: number): void {
  159. this.listeners.forEach(listener => {
  160. listener.onDataAdd(index);
  161. });
  162. }

  164. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件。
  165. notifyDataChange(index: number): void {
  166. this.listeners.forEach(listener => {
  167. listener.onDataChange(index);
  168. });
  169. }

  171. // 通知LazyForEach组件需要在index对应索引处删除该子组件。
  172. notifyDataDelete(index: number): void {
  173. this.listeners.forEach(listener => {
  174. listener.onDataDelete(index);
  175. });
  176. }

  178. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换。
  179. notifyDataMove(from: number, to: number): void {
  180. this.listeners.forEach(listener => {
  181. listener.onDataMove(from, to);
  182. });
  183. }
  184. }
  ```

  [ReusableForListItemGroupUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForListItemGroupUsageScenario.ets#L16-L201)

### 多种条目类型使用场景

**标准型**

复用组件的布局相同，示例参见本文列表滚动部分的描述。

**有限变化型**

复用组件间存在差异，但类型有限。例如，可以通过显式设置两个reuseId或使用两个自定义组件来实现复用。

```
1. class LimitedMyDataSource implements IDataSource {
2. private dataArray: string[] = [];
3. private listener: DataChangeListener | undefined;

5. public totalCount(): number {
6. return this.dataArray.length;
7. }

9. public getData(index: number): string {
10. return this.dataArray[index];
11. }

13. public pushData(data: string): void {
14. this.dataArray.push(data);
15. }

17. public reloadListener(): void {
18. this.listener?.onDataReloaded();
19. }

21. public registerDataChangeListener(listener: DataChangeListener): void {
22. this.listener = listener;
23. }

25. public unregisterDataChangeListener(listener: DataChangeListener): void {
26. this.listener = undefined;
27. }
28. }

30. @Entry
31. @Component
32. struct LimitedIndex {
33. private data: LimitedMyDataSource = new LimitedMyDataSource();

35. aboutToAppear() {
36. for (let i = 0; i < 1000; i++) { // 循环1000次
37. this.data.pushData(i + '');
38. }
39. }

41. build() {
42. Column() {
43. List({ space: 10 }) {
44. LazyForEach(this.data, (item: number) => {
45. ListItem() {
46. ReusableComponent({ item: item })
47. // 设置两种有限变化的reuseId
48. .reuseId(item % 2 === 0 ? 'ReusableComponentOne' : 'ReusableComponentTwo')
49. }
50. .backgroundColor(Color.Orange)
51. .width('100%')
52. }, (item: number) => item.toString())
53. }
54. .cachedCount(2)
55. }
56. }
57. }

59. @Reusable
60. @Component
61. struct ReusableComponent {
62. @State item: number = 0;

64. aboutToReuse(params: ESObject) {
65. this.item = params.item;
66. }

68. build() {
69. Column() {
70. // 组件内部根据类型差异渲染
71. if (this.item % 2 === 0) {
72. Text(`Item ${this.item} ReusableComponentOne`)
73. .fontSize(20)
74. .margin({ left: 10 })
75. } else {
76. Text(`Item ${this.item} ReusableComponentTwo`)
77. .fontSize(20)
78. .margin({ left: 10 })
79. }
80. }.margin({ left: 10, right: 10 })
81. }
82. }
```

[ReusableForLimitedVariation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForLimitedVariation.ets#L16-L99)

**组合型**

复用组件间存在多种差异，但通常具备共同的子组件。将三种复用组件以组合型方式转换为Builder函数后，内部的共享子组件将统一置于父组件MyComponent之下。复用这些子组件时，缓存池在父组件层面实现共享，减少组件创建过程中的资源消耗。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_ReusableComponent]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'ReusableComponent_';
6. const NUMBER3 = 3;
7. const NUMBER5 = 5;

9. class MyDataSource implements IDataSource {
10. private dataArray: string[] = [];
11. private listener: DataChangeListener | undefined;

13. public totalCount(): number {
14. return this.dataArray.length;
15. }

17. public getData(index: number): string {
18. return this.dataArray[index];
19. }

21. public pushData(data: string): void {
22. this.dataArray.push(data);
23. }

25. public reloadListener(): void {
26. this.listener?.onDataReloaded();
27. }

29. public registerDataChangeListener(listener: DataChangeListener): void {
30. this.listener = listener;
31. }

33. public unregisterDataChangeListener(listener: DataChangeListener): void {
34. this.listener = undefined;
35. }
36. }

38. @Entry
39. @Component
40. struct MyComponent {
41. private data: MyDataSource = new MyDataSource();

43. aboutToAppear() {
44. for (let i = 0; i < 1000; i++) { // 循环1000次
45. this.data.pushData(i.toString());
46. }
47. }

49. // itemBuilderOne作为复用组件的写法未展示，以下为转为Builder之后的写法。
50. @Builder
51. itemBuilderOne(item: string) {
52. Column() {
53. ChildComponentA({ item: item });
54. ChildComponentB({ item: item });
55. ChildComponentC({ item: item });
56. }
57. }

59. // itemBuilderTwo转为Builder之后的写法。
60. @Builder
61. itemBuilderTwo(item: string) {
62. Column() {
63. ChildComponentA({ item: item });
64. ChildComponentC({ item: item });
65. ChildComponentD({ item: item });
66. }
67. }

69. // itemBuilderThree转为Builder之后的写法。
70. @Builder
71. itemBuilderThree(item: string) {
72. Column() {
73. ChildComponentA({ item: item });
74. ChildComponentB({ item: item });
75. ChildComponentD({ item: item });
76. }
77. }

79. build() {
80. List({ space: 40 }) {
81. LazyForEach(this.data, (item: string, index: number) => {
82. ListItem() {
83. if (index % NUMBER3 === 0) {
84. this.itemBuilderOne(item);
85. } else if (index % NUMBER5 === 0) {
86. this.itemBuilderTwo(item);
87. } else {
88. this.itemBuilderThree(item);
89. }
90. }
91. .backgroundColor('#cccccc')
92. .width('100%')
93. .onAppear(() => {
94. hilog.info(DOMAIN, TAG, BUNDLE + `ListItem ${index} onAppear`);
95. })
96. }, (item: number) => item.toString())
97. }
98. .width('100%')
99. .height('100%')
100. .cachedCount(0)
101. }
102. }

104. @Reusable
105. @Component
106. struct ChildComponentA {
107. @State item: string = '';

109. aboutToReuse(params: ESObject) {
110. hilog.info(DOMAIN, TAG, BUNDLE + `ChildComponentA ${params.item} Reuse ${this.item}`);
111. this.item = params.item;
112. }

114. aboutToRecycle(): void {
115. hilog.info(DOMAIN, TAG, BUNDLE + `ChildComponentA ${this.item} Recycle`);
116. }

118. build() {
119. Column() {
120. Text(`Item ${this.item} Child Component A`)
121. .fontSize(20)
122. .margin({ left: 10 })
123. .fontColor(Color.Blue)
124. Grid() {
125. ForEach((new Array(20)).fill(''), (item: string, index: number) => {
126. GridItem() {
127. // 请开发者自行在src/main/resources/base/media路径下添加app.media.startIcon图片，否则运行时会因资源缺失而报错。
128. Image($r('app.media.startIcon'))
129. .height(20)
130. }
131. })
132. }
133. .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
134. .rowsTemplate('1fr 1fr 1fr 1fr')
135. .columnsGap(10)
136. .width('90%')
137. .height(160)
138. }
139. .margin({ left: 10, right: 10 })
140. .backgroundColor(0xFAEEE0)
141. }
142. }

144. @Reusable
145. @Component
146. struct ChildComponentB {
147. @State item: string = '';

149. aboutToReuse(params: ESObject) {
150. this.item = params.item;
151. }

153. build() {
154. Row() {
155. Text(`Item ${this.item} Child Component B`)
156. .fontSize(20)
157. .margin({ left: 10 })
158. .fontColor(Color.Red)
159. }.margin({ left: 10, right: 10 })
160. }
161. }

163. @Reusable
164. @Component
165. struct ChildComponentC {
166. @State item: string = '';

168. aboutToReuse(params: ESObject) {
169. this.item = params.item;
170. }

172. build() {
173. Row() {
174. Text(`Item ${this.item} Child Component C`)
175. .fontSize(20)
176. .margin({ left: 10 })
177. .fontColor(Color.Green)
178. }.margin({ left: 10, right: 10 })
179. }
180. }

182. @Reusable
183. @Component
184. struct ChildComponentD {
185. @State item: string = '';

187. aboutToReuse(params: ESObject) {
188. this.item = params.item;
189. }

191. build() {
192. Row() {
193. Text(`Item ${this.item} Child Component D`)
194. .fontSize(20)
195. .margin({ left: 10 })
196. .fontColor(Color.Orange)
197. }.margin({ left: 10, right: 10 })
198. }
199. }
```

[ReusableForComposite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ReusableComponent/entry/src/main/ets/pages/ReusableForComposite.ets#L16-L216)
