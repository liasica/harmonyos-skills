---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-component
title: 组件内状态管理常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理常见问题 > 组件内状态管理常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bffc8b1b21bbfef6c777b77718b834eb93263d7188ddf32550ad3e377d0da4ae
---

在ArkUI应用开发中，组件内状态管理的合理使用直接影响应用的性能和开发效率。然而，开发者在实践中常因更新机制理解不足，导致组件行为异常或渲染效率下降。本文将介绍组件内状态管理的常见问题与解决方案。

## build函数中更改状态变量导致appfreeze

不允许在build里改变状态变量，状态管理框架会在运行时报出Error级别日志。通过事件回调或异步回调更新状态变量，例如在onClick中修改@State，是允许的。

下面的示例，渲染的流程是：

1. 创建Index自定义组件。
2. 执行Index的build方法：

   * 创建Column组件。
   * 创建Text组件。创建Text组件的过程中，触发this.count++。
   * count的改变再次触发Text组件的刷新。
   * 刷新过程中组件不会再标脏自己。
   * Text最终显示为2。

```
1. @Entry
2. @Component
3. struct Index {
4. @State count: number = 1;

6. build() {
7. Column() {
8. // 应避免直接在Text组件内改变count的值
9. Text(`${this.count++}`)
10. .width(50)
11. .height(50)
12. }
13. }
14. }
```

[StateProblemNotUpdateInBuildError01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemNotUpdateInBuildError01.ets#L16-L31)

在首次创建的过程中，Text组件被多渲染了一次，最终显示为2。

框架识别到在build里改变状态变量会打error日志，error日志为：

```
1. FIX THIS APPLICATION ERROR: @Component 'Index': State variable 'count' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
```

在上述示例中，Text组件多渲染了一次。这个错误行为不会造成严重的后果，所以许多开发者忽略了这个日志。

但是，此行为是严重错误的，随着工程的复杂度升级，隐患将逐渐增大。见下一个例子。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: number = 20;

6. build() {
7. Column() {
8. Text(`${this.message++}`)
9. Text(`${this.message++}`)
10. }
11. .height('100%')
12. .width('100%')
13. }
14. }
```

[StateProblemNotUpdateInBuildError02.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemNotUpdateInBuildError02.ets#L16-L31)

上面示例的渲染过程为：

1. 创建第一个Text组件，触发this.message改变，[标脏](arkts-state-management-glossary.md#标脏mark-dirty)第一个Text组件。
2. 创建第二个Text组件，触发this.message改变，标脏两个Text组件。
3. 下一帧到来时，刷新脏系统组件。
4. 刷新第一个Text组件，触发this.message改变，不会标脏自己，仅标脏第二个Text组件。
5. 刷新第二个Text组件，触发this.message改变，不会标脏自己，仅标脏第一个Text组件。
6. 上述4、5步骤循环。
7. 系统长时间无响应，appfreeze。

因此，在build方法中改变状态变量是完全错误的。当发现“FIX THIS APPLICATION ERROR: @Component ... has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!”日志时，即使当前没有带来严重后果，也应该警惕并修改错误写法。

## 注册回调中更改状态变量未解注册导致内存泄漏

开发者可以在[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)中注册箭头函数，以此改变组件中的状态变量。

注意

需要在[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)中将注册的函数置空，以避免箭头函数捕获自定义组件的this实例，导致自定义组件无法被释放，从而造成内存泄漏。

```
1. import { common } from '@kit.AbilityKit';

3. class Model {
4. private callback: (() => void) | undefined = () => {
5. };

7. add(callback: () => void): void {
8. this.callback = callback;
9. }

11. delete(): void {
12. this.callback = undefined;
13. }

15. call(): void {
16. if (this.callback) {
17. this.callback();
18. }
19. }
20. }

22. let model: Model = new Model();

24. @Entry
25. @Component
26. struct Test {
27. @State count: number = 10;
28. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

30. aboutToAppear(): void {
31. model.add(() => {
32. this.count++;
33. })
34. }

36. build() {
37. Column() {
38. // 请在resources\base\element\string.json文件中配置name为'state_countvalue_text1' ，value为非空字符串的资源
39. Text(resource.resourceToString($r('app.string.state_countvalue_text1')) + `${this.count}`)
40. Button('change')
41. .onClick(() => {
42. model.call();
43. })
44. }
45. }

47. aboutToDisappear(): void {
48. model.delete();
49. }
50. }
```

[StateProblemUnregisterStateCallback.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemUnregisterStateCallback.ets#L16-L67)

此外，也可以使用 LocalStorage在[自定义组件外改变状态变量](arkts-localstorage.md#自定义组件外改变状态变量)。

## 使用a.b(this.object)形式调用，不会触发UI刷新

在build方法内，当@State装饰的变量是Object类型，且通过a.b(this.object)形式调用时，b方法内传入的是this.object的原始对象，修改其属性，无法触发UI刷新。如下例中，通过静态方法Balloon.increaseVolume或者this.reduceVolume修改balloon的volume时，UI不会刷新。

【反例】

```
1. class Balloon {
2. public volume: number;

4. constructor(volume: number) {
5. this.volume = volume;
6. }

8. static increaseVolume(balloon: Balloon) {
9. balloon.volume += 2;
10. }
11. }

13. @Entry
14. @Component
15. struct Index {
16. @State balloon: Balloon = new Balloon(10);

18. reduceVolume(balloon: Balloon) {
19. balloon.volume -= 1;
20. }

22. build() {
23. Column({ space: 8 }) {
24. Text(`The volume of the balloon is ${this.balloon.volume} cubic centimeters.`)
25. .fontSize(30)
26. Button(`increaseVolume`)
27. .onClick(() => {
28. // 通过静态方法调用，无法触发UI刷新
29. Balloon.increaseVolume(this.balloon);
30. })
31. Button(`reduceVolume`)
32. .onClick(() => {
33. // 使用this通过自定义组件内部方法调用，无法触发UI刷新
34. this.reduceVolume(this.balloon);
35. })
36. }
37. .width('100%')
38. .height('100%')
39. }
40. }
```

[StateProblemABCallUiRefreshOpposite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemABCallUiRefreshOpposite.ets#L16-L57)

状态变量观察类属性变化是通过代理捕获其变化的，当使用a.b(this.object)调用时，框架会将代理对象转换为原始对象。修改原始对象属性，无法观察，因此UI不会刷新。开发者可以使用如下方法修改：

1. 先将this.balloon赋值给临时变量。
2. 再使用临时变量完成原本的调用逻辑。

   具体见正例。

【正例】

```
1. class Balloon {
2. public volume: number;

4. constructor(volume: number) {
5. this.volume = volume;
6. }

8. static increaseVolume(balloon: Balloon) {
9. balloon.volume += 2;
10. }
11. }

13. @Entry
14. @Component
15. struct Index {
16. @State balloon: Balloon = new Balloon(10);

18. reduceVolume(balloon: Balloon) {
19. balloon.volume -= 1;
20. }

22. build() {
23. Column({ space: 8 }) {
24. Text(`The volume of the balloon is ${this.balloon.volume} cubic centimeters.`)
25. .fontSize(30)
26. Button(`increaseVolume`)
27. .onClick(() => {
28. // 通过赋值给临时变量保留Proxy代理
29. let balloon1 = this.balloon;
30. Balloon.increaseVolume(balloon1);
31. })
32. Button(`reduceVolume`)
33. .onClick(() => {
34. // 通过赋值给临时变量保留Proxy代理
35. let balloon2 = this.balloon;
36. this.reduceVolume(balloon2);
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

[StateProblemABCallUiRefreshPositive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemABCallUiRefreshPositive.ets#L16-L59)

## 复杂类型常量重复赋值给状态变量触发不必要的刷新

### 状态管理V1

在状态管理V1中，会给被@Observed装饰的类对象以及使用状态变量装饰器如@State装饰的Class、Date、Map、Set、Array类型的对象添加一层代理，用于观测一层属性或API调用产生的变化。当复杂类型常量重复赋值给状态变量时，可能会由于加了代理而判断为新旧值不相等，导致不必要的刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. class DataObj {
4. public name: string = 'default name';

6. constructor(name: string) {
7. this.name = name;
8. }
9. }

11. @Entry
12. @Component
13. struct Index {
14. list: DataObj[] = [new DataObj('a'), new DataObj('b'), new DataObj('c')];
15. @State dataObjFromList: DataObj = this.list[0];

17. build() {
18. Column() {
19. ConsumerChild({ dataObj: this.dataObjFromList })
20. Button('change to self').onClick(() => {
21. this.dataObjFromList = this.list[0];
22. })
23. }
24. }
25. }

27. @Component
28. struct ConsumerChild {
29. @Link @Watch('onDataObjChange') dataObj: DataObj;

31. onDataObjChange() {
32. hilog.info(0xFF00, 'testTag', '%{public}s', 'dataObj changed');
33. }

35. getContent() {
36. hilog.info(0xFF00, 'testTag', '%{public}s', `this.dataObj.name change: ${this.dataObj.name}`);
37. return this.dataObj.name;
38. }

40. build() {
41. Column() {
42. Text(this.getContent()).fontSize(30)
43. }
44. }
45. }
```

[StateProblemComplexConstantRepeatRefresh.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemComplexConstantRepeatRefresh.ets#L15-L61)

以上示例每次点击Button('change to self')，把相同的类实例赋值给一个Class类型的状态变量，会触发刷新并输出this.dataObj.name change: a日志。这是因为当再次赋值list[0]时，dataObjFromList已经是Proxy类型，而list[0]是Object类型，因此判断两者不相等，会触发赋值和刷新。

为了避免这种不必要的赋值和刷新，可以通过用@Observed装饰类，或者使用[UIUtils.getTarget()](arkts-new-gettarget.md)获取原始对象，提前进行新旧值的判断，如果相同则不执行赋值。

方法一：增加@Observed

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Observed
4. class DataObj {
5. public name: string = 'default name';

7. constructor(name: string) {
8. this.name = name;
9. }
10. }

12. @Entry
13. @Component
14. struct Index {
15. list: DataObj[] = [new DataObj('a'), new DataObj('b'), new DataObj('c')];
16. @State dataObjFromList: DataObj = this.list[0];

18. build() {
19. Column() {
20. ConsumerChild({ dataObj: this.dataObjFromList })
21. Button('change to self').onClick(() => {
22. this.dataObjFromList = this.list[0];
23. })
24. }
25. }
26. }

28. @Component
29. struct ConsumerChild {
30. @Link @Watch('onDataObjChange') dataObj: DataObj;

32. onDataObjChange() {
33. hilog.info(0xFF00, 'testTag', '%{public}s', 'dataObj changed');
34. }

36. build() {
37. Column() {
38. Text(this.dataObj.name).fontSize(30)
39. }
40. }
41. }
```

[StateProblemComplexSolution01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemComplexSolution01.ets#L15-L57)

以上示例，给对应的类增加了@Observed装饰器后，list[0]已经是Proxy类型了，这样再次赋值时，相同的对象，就不会触发刷新。

方法二：使用[UIUtils.getTarget()](arkts-new-gettarget.md)获取原始对象

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class DataObj {
5. public name: string = 'default name';

7. constructor(name: string) {
8. this.name = name;
9. }
10. }

12. @Entry
13. @Component
14. struct Index {
15. list: DataObj[] = [new DataObj('a'), new DataObj('b'), new DataObj('c')];
16. @State dataObjFromList: DataObj = this.list[0];

18. build() {
19. Column() {
20. ConsumerChild({ dataObj: this.dataObjFromList })
21. Button('change to self').onClick(() => {
22. // 获取原始对象来和新值做对比
23. if (UIUtils.getTarget(this.dataObjFromList) !== this.list[0]) {
24. this.dataObjFromList = this.list[0];
25. }
26. })
27. }
28. }
29. }

31. @Component
32. struct ConsumerChild {
33. @Link @Watch('onDataObjChange') dataObj: DataObj;

35. onDataObjChange() {
36. hilog.info(0xFF00, 'testTag', '%{public}s', 'dataObj changed');
37. }

39. build() {
40. Column() {
41. Text(this.dataObj.name).fontSize(30)
42. }
43. }
44. }
```

[StateProblemComplexSolution02.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemComplexSolution02.ets#L16-L61)

以上示例，在赋值前，使用getTarget获取了对应状态变量的原始对象，经过对比后，如果和当前对象一样，就不赋值，不触发刷新。

### 状态管理V2

在状态管理V2中，会给使用状态变量装饰器如@Trace、@Local装饰的Date、Map、Set、Array添加一层代理用于观测API调用产生的变化。当复杂类型常量重复赋值给状态变量时，可能会由于加了代理而判断为新旧值不相等，导致不必要的刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @ComponentV2
5. struct Index {
6. list: string[][] = [['a'], ['b'], ['c']];
7. @Local dataObjFromList: string[] = this.list[0];

9. @Monitor('dataObjFromList')
10. onStrChange(monitor: IMonitor) {
11. hilog.info(0xFF00, 'testTag', '%{public}s', 'dataObjFromList has changed');
12. }

14. build() {
15. Column() {
16. Button('change to self').onClick(() => {
17. // 新值和本地初始化的值相同
18. this.dataObjFromList = this.list[0];
19. })
20. }
21. }
22. }
```

[LocalQuestionSparkUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionSparkUpdate.ets#L15-L38)

以上示例每次点击Button('change to self')，把相同的Array类型常量赋值给一个Array类型的状态变量，都会触发刷新。这是因为当再次赋值list[0]时，dataObjFromList已经是Proxy类型，而list[0]是Array类型。由于类型不相等，会触发赋值和刷新。

为了避免这种不必要的赋值和刷新，可以使用[UIUtils.getTarget()](arkts-new-gettarget.md)获取原始对象提前进行新旧值的判断，当两者相同时不执行赋值。

使用UIUtils.getTarget()方法示例。

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. @Entry
7. @ComponentV2
8. struct Index {
9. list: string[][] = [['a'], ['b'], ['c']];
10. @Local dataObjFromList: string[] = this.list[0];

12. @Monitor('dataObjFromList')
13. onStrChange(monitor: IMonitor) {
14. hilog.info(DOMAIN, 'testTag', '%{public}s', 'dataObjFromList has changed');
15. }

17. build() {
18. Column() {
19. Button('change to self').onClick(() => {
20. // 获取原始对象来和新值做对比
21. if (UIUtils.getTarget(this.dataObjFromList) !== this.list[0]) {
22. this.dataObjFromList = this.list[0];
23. }
24. })
25. }
26. }
27. }
```

[LocalQuestionUIUtils.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/local/LocalQuestionUIUtils.ets#L17-L45)

## 子组件无需修改状态变量时，使用@Prop导致不必要的深拷贝

在应用开发中，父组件常向子组件传值。如果子组件不需要修改该状态变量，子组件使用[@Prop](arkts-prop.md)装饰器会增加组件创建时间并影响性能，此时建议改用[@ObjectLink](arkts-observed-and-objectlink.md)。

【反例】

```
1. @Observed
2. class DeepReMyClass {
3. public num: number = 0;

5. constructor(num: number) {
6. this.num = num;
7. }
8. }

10. @Component
11. struct DeepRePropChild {
12. @Prop testClass: DeepReMyClass; // @Prop装饰状态变量会深拷贝。

14. build() {
15. Text(`PropChild testNum ${this.testClass.num}`)
16. }
17. }

19. @Entry
20. @Component
21. struct DeepReParent {
22. @State testClass: DeepReMyClass[] = [new DeepReMyClass(1)];

24. build() {
25. Column() {
26. Text(`DeepReParent testNum ${this.testClass[0].num}`)
27. .onClick(() => {
28. this.testClass[0].num += 1;
29. })

31. // DeepRePropChild没有改变@Prop testClass: DeepReMyClass的值，所以这时最优的选择是使用@ObjectLink。
32. DeepRePropChild({ testClass: this.testClass[0] })
33. }
34. }
35. }
```

[DeepCopyReverse.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/DeepCopyReverse.ets#L16-L52)

在以上示例中，DeepRePropChild组件没有改变@Prop testClass: MyClass的值，因此使用@ObjectLink更为合适。因为@Prop会深拷贝数据带来性能开销，所以@ObjectLink是比@Prop更优的选择。

【正例】

```
1. @Observed
2. class MyClass {
3. public num: number = 0;

5. constructor(num: number) {
6. this.num = num;
7. }
8. }

10. @Component
11. struct PropChild {
12. @ObjectLink testClass: MyClass; // @ObjectLink装饰状态变量不会深拷贝。

14. build() {
15. Text(`PropChild testNum ${this.testClass.num}`)
16. }
17. }

19. @Entry
20. @Component
21. struct Parent {
22. @State testClass: MyClass[] = [new MyClass(1)];

24. build() {
25. Column() {
26. Text(`Parent testNum ${this.testClass[0].num}`)
27. .onClick(() => {
28. this.testClass[0].num += 1;
29. })

31. // 当子组件不需要本地修改状态时，应优先使用@ObjectLink，因为@Prop会执行深拷贝并带来性能开销，此时@ObjectLink是比@Link和@Prop更优的选择。
32. PropChild({ testClass: this.testClass[0] })
33. }
34. }
35. }
```

[DeepCopyCorrect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/DeepCopyCorrect.ets#L16-L52)

## 状态变量关联的组件数过多导致性能下降

建议每个状态变量关联的组件数少于20个。精准控制状态变量关联的组件数量可减少不必要的组件刷新，提升刷新效率。有时开发者会将同一状态变量绑定于多个同级组件属性，状态变化时将导致这些组件同步更新，产生不必要的刷新，当组件复杂度较高时会显著影响整体性能。相反，将该状态变量绑定在这些组件的父组件上，可以减少需要刷新的组件数，提高性能。在应用开发中，可以通过HiDumper查看状态变量关联的组件数。具体可参考[状态变量组件定位工具实践](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/performance/state_variable_dfx_pratice.md)。

【反例】

```
1. @Observed
2. class Translate {
3. public translateX: number = 20;
4. }

6. @Component
7. struct Title {
8. @ObjectLink translateObj: Translate;

10. build() {
11. Row() {
12. // $r('app.media.background')需要替换为开发者所需的资源文件。
13. Image($r('app.media.background'))
14. .width(50)
15. .height(50)
16. .translate({
17. x: this.translateObj.translateX // this.translateObj.translateX 绑定在Image和Text组件上。
18. })
19. Text('Title')
20. .fontSize(20)
21. .translate({
22. x: this.translateObj.translateX
23. })
24. }
25. }
26. }

28. @Entry
29. @Component
30. struct Page {
31. @State translateObj: Translate = new Translate();

33. build() {
34. Column() {
35. Title({
36. translateObj: this.translateObj
37. })
38. Stack() {
39. }
40. .backgroundColor('black')
41. .width(200)
42. .height(400)
43. .translate({
44. x: this.translateObj.translateX // this.translateObj.translateX 绑定在Stack和Button组件上。
45. })
46. Button('move')
47. .translate({
48. x: this.translateObj.translateX
49. })
50. .onClick(() => {
51. this.getUIContext().animateTo({
52. duration: 50
53. }, () => {
54. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150;
55. });
56. })
57. }
58. }
59. }
```

[PreciseControlCounterexamples.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/PreciseControlCounterexamples.ets#L16-L76)

在上面的示例中，状态变量this.translateObj.translateX被用在多个同级的子组件下，当this.translateObj.translateX变化时，会导致所有关联它的组件一起刷新，但实际上由于这些组件的变化是相同的，因此可以将这个属性绑定到他们共同的父组件上，来实现减少组件的刷新数量。经过分析，所有子组件均位于Page组件的Column下，因此将所有子组件相同的translate属性统一到Column上，来实现精准控制状态变量关联的组件数。

【正例】

```
1. @Observed
2. class PageTranslate {
3. public translateX: number = 20;
4. }

6. @Component
7. struct PageTitle {
8. build() {
9. Row() {
10. // $r('app.media.background')需要替换为开发者所需的图像资源文件。
11. Image($r('app.media.background'))
12. .width(50)
13. .height(50)
14. Text('Title')
15. .fontSize(20)
16. }
17. }
18. }

20. @Entry
21. @Component
22. struct Page1 {
23. @State translateObj: PageTranslate = new PageTranslate();

25. build() {
26. Column() {
27. PageTitle()
28. Stack() {
29. }
30. .backgroundColor('black')
31. .width(200)
32. .height(400)
33. Button('move')
34. .onClick(() => {
35. this.getUIContext().animateTo({
36. duration: 50
37. }, () => {
38. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150;
39. });
40. })
41. }
42. .translate({
43. // 子组件Stack和Button设置了同一个translate属性，可以统一到Column上设置。
44. x: this.translateObj.translateX
45. })
46. }
47. }
```

[PreciseControlPositiveCases.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/PreciseControlPositiveCases.ets#L16-L64)

## 在for、while等循环逻辑中频繁读取状态变量导致性能下降

在应用开发中，应避免在循环逻辑中频繁读取状态变量，而是应该放在循环外面读取。

【反例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '';

8. build() {
9. Column() {
10. Button('Click to print log')
11. .onClick(() => {
12. for (let i = 0; i < 10; i++) {
13. hilog.info(0x0000, 'TAG', '%{public}s', this.message);
14. }
15. })
16. .width('90%')
17. .backgroundColor(Color.Blue)
18. .fontColor(Color.White)
19. .margin({
20. top: 10
21. })
22. }
23. .justifyContent(FlexAlign.Start)
24. .alignItems(HorizontalAlign.Center)
25. .margin({
26. top: 15
27. })
28. }
29. }
```

[LoopStateInefficient.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/LoopStateInefficient.ets#L16-L46)

【正例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '';

8. build() {
9. Column() {
10. Button('Click to print log')
11. .onClick(() => {
12. let logMessage: string = this.message;
13. for (let i = 0; i < 10; i++) {
14. hilog.info(0x0000, 'TAG', '%{public}s', logMessage);
15. }
16. })
17. .width('90%')
18. .backgroundColor(Color.Blue)
19. .fontColor(Color.White)
20. .margin({
21. top: 10
22. })
23. }
24. .justifyContent(FlexAlign.Start)
25. .alignItems(HorizontalAlign.Center)
26. .margin({
27. top: 15
28. })
29. }
30. }
```

[LoopStateOptimized.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/LoopStateOptimized.ets#L16-L47)

## 频繁修改状态变量导致性能下降

在应用开发中，应尽量减少对状态变量的直接赋值，通过临时变量完成数据计算操作。

状态变量发生变化时，ArkUI会查询依赖该状态变量的组件并执行该组件的更新方法，完成组件渲染。通过使用临时变量的计算代替直接操作状态变量，可以使ArkUI仅在最后一次状态变量变更时查询并渲染组件，减少不必要的操作，从而提高应用性能。状态变量行为可参考[@State装饰器：组件内状态](arkts-state.md)。

【反例】

```
1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '';

8. appendMsg(newMsg: string) {
9. // 性能打点
10. hiTraceMeter.startTrace('StateVariable', 1);
11. this.message += newMsg;
12. this.message += ';';
13. this.message += '<br/>';
14. hiTraceMeter.finishTrace('StateVariable', 1);
15. }

17. build() {
18. Column() {
19. Button('Click to print log')
20. .onClick(() => {
21. this.appendMsg('Operating state variable');
22. })
23. .width('90%')
24. .backgroundColor(Color.Blue)
25. .fontColor(Color.White)
26. .margin({
27. top: 10
28. })
29. }
30. .justifyContent(FlexAlign.Start)
31. .alignItems(HorizontalAlign.Center)
32. .margin({
33. top: 15
34. })
35. }
36. }
```

[CalculationDirectState.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/CalculationDirectState.ets#L16-L53)

直接操作状态变量，三次触发计算函数，运行[耗时](ui-inspector-profiler.md#trace调试能力)结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/oNwHCx9zQ16kKbqAE4b67w/zh-cn_image_0000002552797984.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=2B6FCCA14F177E218F32BC3C8FC94B0294BE2CF737805801FA17FA831039DD20)

【正例】

```
1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '';

8. appendMsg(newMsg: string) {
9. // 性能打点。
10. hiTraceMeter.startTrace('TemporaryVariable', 2);
11. let message = this.message;
12. message += newMsg;
13. message += ';';
14. message += '<br/>';
15. this.message = message;
16. hiTraceMeter.finishTrace('TemporaryVariable', 2);
17. }

19. build() {
20. Column() {
21. Button('Click to print log')
22. .onClick(() => {
23. this.appendMsg('Operating temporary variable');
24. })
25. .width('90%')
26. .backgroundColor(Color.Blue)
27. .fontColor(Color.White)
28. .margin({
29. top: 10
30. })
31. }
32. .justifyContent(FlexAlign.Start)
33. .alignItems(HorizontalAlign.Center)
34. .margin({
35. top: 15
36. })
37. }
38. }
```

[CalculationTempVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateManagement/entry/src/main/ets/pages/CalculationTempVariable.ets#L16-L55)

使用临时变量取代状态变量的计算，三次触发计算函数，运行耗时结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/OoE5qQjaTkWQGNsO3YV7uA/zh-cn_image_0000002583437679.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=8F491B2521CB1D5F6A2490F56FD533354AE7D525570EACB65DA9051A6DBE8DFC)

【总结】

| **计算方式** | **耗时(局限不同设备和场景，数据仅供参考)** | **说明** |
| --- | --- | --- |
| 直接操作状态变量 | 1.01ms | 增加了ArkUI不必要的查询和渲染行为，导致性能劣化。 |
| 使用临时变量计算 | 0.63ms | 减少了ArkUI不必要的行为，优化性能。 |

## 使用LazyForEach的重建机制刷新UI导致性能下降

开发过程中通常会将[LazyForEach](arkts-rendering-control-lazyforeach.md)和状态变量结合起来使用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: StringData[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): StringData {
15. return this.originDataArray[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. hilog.info(DOMAIN_NUMBER, TAG, 'add listener');
21. this.listeners.push(listener);
22. }
23. }

25. unregisterDataChangeListener(listener: DataChangeListener): void {
26. const pos = this.listeners.indexOf(listener);
27. if (pos >= 0) {
28. hilog.info(DOMAIN_NUMBER, TAG, 'remove listener');
29. this.listeners.splice(pos, 1);
30. }
31. }

33. notifyDataReload(): void {
34. this.listeners.forEach(listener => {
35. listener.onDataReloaded();
36. })
37. }

39. notifyDataAdd(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataAdd(index);
42. })
43. }

45. notifyDataChange(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataChange(index);
48. })
49. }

51. notifyDataDelete(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataDelete(index);
54. })
55. }

57. notifyDataMove(from: number, to: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataMove(from, to);
60. })
61. }
62. }

64. class MyDataSource extends BasicDataSource {
65. private dataArray: StringData[] = [];

67. public totalCount(): number {
68. return this.dataArray.length;
69. }

71. public getData(index: number): StringData {
72. return this.dataArray[index];
73. }

75. public addData(index: number, data: StringData): void {
76. this.dataArray.splice(index, 0, data);
77. this.notifyDataAdd(index);
78. }

80. public pushData(data: StringData): void {
81. this.dataArray.push(data);
82. this.notifyDataAdd(this.dataArray.length - 1);
83. }

85. public reloadData(): void {
86. this.notifyDataReload();
87. }
88. }

90. class StringData {
91. public message: string;
92. public imgSrc: Resource;

94. constructor(message: string, imgSrc: Resource) {
95. this.message = message;
96. this.imgSrc = imgSrc;
97. }
98. }

100. @Entry
101. @Component
102. struct MyComponent {
103. private data: MyDataSource = new MyDataSource();

105. aboutToAppear() {
106. for (let i = 0; i <= 9; i++) {
107. // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
108. this.data.pushData(new StringData(`Click to add ${i}`, $r('app.media.icon')));
109. }
110. }

112. build() {
113. List({ space: 3 }) {
114. LazyForEach(this.data, (item: StringData, index: number) => {
115. ListItem() {
116. Column() {
117. Text(item.message).fontSize(20)
118. .onAppear(() => {
119. hilog.info(DOMAIN_NUMBER, TAG, 'text appear:' + item.message);
120. })
121. Image(item.imgSrc)
122. .width(100)
123. .height(100)
124. .onAppear(() => {
125. hilog.info(DOMAIN_NUMBER, TAG, 'image appear');
126. })
127. }.margin({ left: 10, right: 10 })
128. }
129. .onClick(() => {
130. item.message += '0';
131. this.data.reloadData();
132. })
133. }, (item: StringData, index: number) => JSON.stringify(item))
134. }.cachedCount(5)
135. }
136. }
```

[StateArrayLazy.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayLazy.ets#L15-L152)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/_4uZneqPRXqeyoecP6RMhQ/zh-cn_image_0000002552957634.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=E51B43DD59B03EC16AED68847A50F83AE80931597C45FFE7F540E93006BA09E2)

可以观察到在点击更改message之后，图片“闪烁”了一下，同时输出了组件的onAppear日志，这说明组件进行了重建。这是因为在更改message之后，导致LazyForEach中这一项的key值发生了变化，使得LazyForEach在reloadData的时候将这一项ListItem进行了重建。Text组件仅仅更改显示的内容却发生了重建，而不是更新。而尽管Image组件没有需要重新绘制的内容，但是因为触发LazyForEach的重建，会使得同样位于ListItem下的Image组件重新创建。

当前LazyForEach与状态变量都能触发UI的刷新，两者的性能开销是不一样的。使用LazyForEach刷新会对组件进行重建，如果包含了多个组件，则会产生比较大的性能开销。使用状态变量刷新会对组件进行刷新，具体到状态变量关联的组件上，相对于LazyForEach的重建来说，范围更小更精确。因此，推荐使用状态变量来触发LazyForEach中的组件刷新，这就需要使用自定义组件。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. class BasicDataSource implements IDataSource {
7. private listeners: DataChangeListener[] = [];
8. private originDataArray: StringData[] = [];

10. public totalCount(): number {
11. return 0;
12. }

14. public getData(index: number): StringData {
15. return this.originDataArray[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. hilog.info(DOMAIN_NUMBER, TAG, 'add listener');
21. this.listeners.push(listener);
22. }
23. }

25. unregisterDataChangeListener(listener: DataChangeListener): void {
26. const pos = this.listeners.indexOf(listener);
27. if (pos >= 0) {
28. hilog.info(DOMAIN_NUMBER, TAG, 'remove listener');
29. this.listeners.splice(pos, 1);
30. }
31. }

33. notifyDataReload(): void {
34. this.listeners.forEach(listener => {
35. listener.onDataReloaded();
36. })
37. }

39. notifyDataAdd(index: number): void {
40. this.listeners.forEach(listener => {
41. listener.onDataAdd(index);
42. })
43. }

45. notifyDataChange(index: number): void {
46. this.listeners.forEach(listener => {
47. listener.onDataChange(index);
48. })
49. }

51. notifyDataDelete(index: number): void {
52. this.listeners.forEach(listener => {
53. listener.onDataDelete(index);
54. })
55. }

57. notifyDataMove(from: number, to: number): void {
58. this.listeners.forEach(listener => {
59. listener.onDataMove(from, to);
60. })
61. }
62. }

64. class MyDataSource extends BasicDataSource {
65. private dataArray: StringData[] = [];

67. public totalCount(): number {
68. return this.dataArray.length;
69. }

71. public getData(index: number): StringData {
72. return this.dataArray[index];
73. }

75. public addData(index: number, data: StringData): void {
76. this.dataArray.splice(index, 0, data);
77. this.notifyDataAdd(index);
78. }

80. public pushData(data: StringData): void {
81. this.dataArray.push(data);
82. this.notifyDataAdd(this.dataArray.length - 1);
83. }
84. }

86. @Observed
87. class StringData {
88. @Track public message: string;
89. @Track public imgSrc: Resource;

91. constructor(message: string, imgSrc: Resource) {
92. this.message = message;
93. this.imgSrc = imgSrc;
94. }
95. }

97. @Entry
98. @Component
99. struct MyComponent {
100. @State data: MyDataSource = new MyDataSource();

102. aboutToAppear() {
103. for (let i = 0; i <= 9; i++) {
104. // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
105. this.data.pushData(new StringData(`Click to add ${i}`, $r('app.media.icon')));
106. }
107. }

109. build() {
110. List({ space: 3 }) {
111. LazyForEach(this.data, (item: StringData, index: number) => {
112. ListItem() {
113. ChildComponent({ data: item })
114. }
115. .onClick(() => {
116. item.message += '0';
117. })
118. }, (item: StringData, index: number) => index.toString())
119. }.cachedCount(5)
120. }
121. }

123. @Component
124. struct ChildComponent {
125. @ObjectLink data: StringData;

127. build() {
128. Column() {
129. Text(this.data.message).fontSize(20)
130. .onAppear(() => {
131. hilog.info(DOMAIN_NUMBER, TAG, 'text appear:' + this.data.message);
132. })
133. Image(this.data.imgSrc)
134. .width(100)
135. .height(100)
136. }.margin({ left: 10, right: 10 })
137. }
138. }
```

[StateArrayLazy2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayLazy2.ets#L15-L154)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Tru0Vn1FRFyVhR0-TwqGzQ/zh-cn_image_0000002583477635.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=99A6B4A245AA31AE065DCD8CCCAA5DDE3825D7690544B9336F78C09EE410F99B)

可以观察到UI能够正常刷新，图片没有“闪烁”，且没有输出日志信息，说明没有对Text组件和Image组件进行重建。

这是因为使用自定义组件之后，可以通过@Observed和@ObjectLink配合去直接更改自定义组件内的状态变量实现刷新，而不需要利用LazyForEach进行重建。使用[@Track装饰器](arkts-track.md)分别装饰StringData类型中的message和imgSrc属性可以使更新范围进一步缩小到指定的Text组件。

## ForEach和对象数组结合使用导致UI不刷新

开发过程中经常会使用对象数组和[ForEach](arkts-rendering-control-foreach.md)结合起来使用，但是写法不当的话会出现UI不刷新的情况。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class StyleList extends Array<TextStyles> {
8. }

10. @Observed
11. class TextStyles {
12. public fontSize: number;

14. constructor(fontSize: number) {
15. this.fontSize = fontSize;
16. }
17. }

19. @Entry
20. @Component
21. struct Page {
22. @State styleList: StyleList = new StyleList();

24. aboutToAppear() {
25. for (let i = 15; i < 50; i++) {
26. this.styleList.push(new TextStyles(i));
27. }
28. }

30. build() {
31. Column() {
32. Text('Font Size List')
33. .fontSize(50)
34. .onClick(() => {
35. for (let i = 0; i < this.styleList.length; i++) {
36. this.styleList[i].fontSize++;
37. }
38. hilog.info(DOMAIN_NUMBER, TAG, 'change font size');
39. })
40. List() {
41. ForEach(this.styleList, (item: TextStyles) => {
42. ListItem() {
43. Text('Hello World')
44. .fontSize(item.fontSize)
45. }
46. })
47. }
48. }
49. }
50. }
```

[StateArrayForeach.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayForeach.ets#L15-L66)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/TSh4Hdm7S_GMEkNiDBizBg/zh-cn_image_0000002552797986.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=3995B37C603B248158CA1D81A0BD10B37F18E41F628BCAE3BAF680E7EF002F8A)

由于ForEach中生成的item是一个常量，因此当点击改变item中的内容时，没有办法观测到UI刷新，尽管日志表明item的值已改变（这体现在打印了“change font size”的日志）。因此，需要使用自定义组件，配合@ObjectLink来实现观测的能力。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class StyleList extends Array<TextStyles> {
8. }

10. @Observed
11. class TextStyles {
12. public fontSize: number;

14. constructor(fontSize: number) {
15. this.fontSize = fontSize;
16. }
17. }

19. @Component
20. struct TextComponent {
21. @ObjectLink textStyle: TextStyles;

23. build() {
24. Text('Hello World')
25. .fontSize(this.textStyle.fontSize)
26. }
27. }

29. @Entry
30. @Component
31. struct Page {
32. @State styleList: StyleList = new StyleList();

34. aboutToAppear() {
35. for (let i = 15; i < 50; i++) {
36. this.styleList.push(new TextStyles(i));
37. }
38. }

40. build() {
41. Column() {
42. Text('Font Size List')
43. .fontSize(50)
44. .onClick(() => {
45. for (let i = 0; i < this.styleList.length; i++) {
46. this.styleList[i].fontSize++;
47. }
48. hilog.info(DOMAIN_NUMBER, TAG, 'change font size');
49. })
50. List() {
51. ForEach(this.styleList, (item: TextStyles) => {
52. ListItem() {
53. TextComponent({ textStyle: item })
54. }
55. })
56. }
57. }
58. }
59. }
```

[StateArrayForeach2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayForeach2.ets#L15-L75)

上述代码的运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/EUtxGULBQYCFycBtCd-dng/zh-cn_image_0000002583437681.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=361F274D44E9B2D2F3256EDD61A72EACFDE87A198006D7E1D7B2E5955CA7F8FF)

使用@ObjectLink接受传入的item后，使得TextComponent组件内的textStyle变量具有了被观测的能力。在父组件更改styleList中的值时，由于@ObjectLink是引用传递，所以会观测到styleList每一个数据项的地址指向的对应item的fontSize的值被改变，因此触发UI的刷新。

这是一个较为实用的使用状态管理进行刷新的开发方式。
