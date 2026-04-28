---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch
title: @Watch装饰器：状态变量更改通知
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @Watch装饰器：状态变量更改通知
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1654841265985a7420435dc9657912f5aeb09e0c5b55a065c38c8162cc160900
---

@Watch应用于对状态变量的监听。如果开发者需要关注某个状态变量的值是否改变，可以使用@Watch为状态变量设置回调函数。

@Watch提供了状态变量的监听能力，@Watch仅能监听到可以观察到的变化。

在阅读本文档前，建议开发者对状态管理基本观察能力有基本的了解。建议提前阅读：[@State](arkts-state.md)。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 概述

@Watch用于监听状态变量的变化，当状态变量变化时，@Watch的回调方法将被调用。@Watch在ArkUI框架内部判断数值有无更新使用的是严格相等（===），遵循严格相等规范。当严格相等判断的结果是false（即不相等）的情况下，就会触发@Watch的回调。

## 装饰器说明

| @Watch补充变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 必填。常量字符串，字符串需要有引号。是(string) => void自定义成员函数的方法的引用。 |
| 可装饰的自定义组件变量 | 可监听所有装饰器装饰的状态变量。不允许监听常规变量。 |
| 装饰器的顺序 | 装饰器顺序不影响实际功能，开发者可以根据自己的需要决定装饰器顺序的先后。建议[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Link](arkts-link.md)等装饰器在@Watch装饰器之前，以保持整体风格的一致。 |
| @Watch触发时机 | 使用@Watch来监听状态变量变化时，回调触发时间是变量真正变化、被赋值的时间。详细示例请参考使用场景中的[@Watch的触发时机](arkts-watch.md#watch的触发时机)。 |

## 语法说明

| 类型 | 说明 |
| --- | --- |
| (changedPropertyName? : string) => void | 该函数是自定义组件的成员函数，changedPropertyName是被watch的属性名。  在多个状态变量绑定同一个@Watch的回调方法的时候，可以通过changedPropertyName进行不同的逻辑处理  将属性名作为字符串输入参数，不返回任何内容。 |

## 观察变化和行为表现

1. 当观察到状态变量的变化（包括双向绑定的[AppStorage](arkts-appstorage.md)和[LocalStorage](arkts-localstorage.md)中对应的key发生的变化）的时候，对应的@Watch的回调方法将被触发；
2. @Watch方法在自定义组件的属性变更之后同步执行；
3. 如果在@Watch的方法里改变了其他的状态变量，也会引起状态变更和@Watch的执行；
4. 在第一次初始化的时候，@Watch装饰的方法不会被调用，即认为初始化不是状态变量的改变。只有在后续状态改变时，才会调用@Watch回调方法。

## 限制条件

* 建议开发者避免无限循环。循环可能是因为在@Watch的回调方法里直接或者间接地修改了同一个状态变量引起的。为了避免循环的产生，建议不要在@Watch的回调方法里修改当前装饰的状态变量；
* 开发者应关注性能，属性值更新函数会延迟组件的重新渲染（具体请见上面的行为表现），因此，回调函数应仅执行快速运算；
* 不建议在@Watch函数中调用async await，因为@Watch设计的用途是为了快速的计算，异步行为可能会导致重新渲染速度的性能问题。
* @Watch参数为必选，且参数类型必须是string，否则编译期会报错。不建议开发者传入undefined，传入后编译不会报错，相当于传入“undefined”。

```
1. // 错误写法，编译报错
2. @State @Watch() num: number = 10;
3. @State @Watch(change) num: number = 10;

5. // 正确写法
6. @State @Watch('change') num: number = 10;
7. change() {
8. console.info(`xxx`);
9. }
```

* @Watch内的参数必须是声明的方法名，否则编译期会报错。

```
1. // 错误写法，没有对应名称的函数，编译报错
2. @State @Watch('change') num: number = 10;
3. onChange() {
4. console.info(`xxx`);
5. }

7. // 正确写法
8. @State @Watch('change') num: number = 10;
9. change() {
10. console.info(`xxx`);
11. }
```

* 常规变量不能被@Watch装饰，否则编译期会报错。

```
1. // 错误写法
2. @Watch('change') num: number = 10;
3. change() {
4. console.info(`xxx`);
5. }

7. // 正确写法
8. @State @Watch('change') num: number = 10;
9. change() {
10. console.info(`xxx`);
11. }
```

## 使用场景

### @Watch和自定义组件更新

以下示例展示组件更新和@Watch的处理步骤。count在CountModifier中由@State装饰，在TotalView中由@Prop装饰。

```
1. @Component
2. struct TotalView {
3. @Prop @Watch('onCountUpdated') count: number = 0;
4. @State total: number = 0;

6. // @Watch 回调
7. onCountUpdated(propName: string): void {
8. this.total += this.count;
9. }

11. build() {
12. Text(`Total: ${this.total}`)
13. }
14. }

16. @Entry
17. @Component
18. struct CountModifier {
19. @State count: number = 0;

21. build() {
22. Column() {
23. Button('add to basket')
24. .onClick(() => {
25. this.count++;
26. })
27. TotalView({ count: this.count })
28. }
29. }
30. }
```

[CountModifier.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Watch/entry/src/main/ets/pages/CountModifier.ets#L15-L47)

处理步骤：

1. CountModifier自定义组件的Button.onClick点击事件自增count。
2. 由于@State count变量更改，子组件TotalView中的@Prop被更新，其@Watch('onCountUpdated')方法被调用，更新了子组件TotalView 中的total变量。
3. 子组件TotalView中的Text重新渲染。

### @Watch与@Link组合使用

以下示例说明了如何在子组件中观察@Link变量。

```
1. class PurchaseItem {
2. public static nextId: number = 0;
3. public id: number;
4. public price: number;

6. constructor(price: number) {
7. this.id = PurchaseItem.nextId++;
8. this.price = price;
9. }
10. }

12. @Component
13. struct BasketViewer {
14. @Link @Watch('onBasketUpdated') shopBasket: PurchaseItem[];
15. @State totalPurchase: number = 0;

17. updateTotal(): number {
18. let total = this.shopBasket.reduce((sum, i) => sum + i.price, 0);
19. // 超过100欧元可享受折扣
20. if (total >= 100) {
21. total = 0.9 * total;
22. }
23. return total;
24. }

26. // @Watch 回调
27. onBasketUpdated(propName: string): void {
28. this.totalPurchase = this.updateTotal();
29. }

31. build() {
32. Column() {
33. ForEach(this.shopBasket,
34. (item: PurchaseItem) => {
35. Text(`Price: ${item.price.toFixed(2)} €`)
36. },
37. (item: PurchaseItem) => item.id.toString()
38. )
39. Text(`Total: ${this.totalPurchase.toFixed(2)} €`)
40. }
41. }
42. }

44. @Entry
45. @Component
46. struct BasketModifier {
47. @State shopBasket: PurchaseItem[] = [];

49. build() {
50. Column() {
51. Button('Add to basket')
52. .onClick(() => {
53. this.shopBasket.push(new PurchaseItem(Math.round(100 * Math.random())));
54. })
55. BasketViewer({ shopBasket: $shopBasket })
56. }
57. }
58. }
```

[BasketModifier.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Watch/entry/src/main/ets/pages/BasketModifier.ets#L15-L75)

处理步骤如下：

1. BasketModifier组件的Button.onClick向BasketModifier shopBasket中添加条目；
2. @Link装饰的BasketViewer shopBasket值发生变化；
3. 状态管理框架调用@Watch函数BasketViewer onBasketUpdated 更新BasketViewer TotalPurchase的值；
4. @Link shopBasket的改变，新增了数组项，ForEach组件会执行item Builder，渲染构建新的Item项；@State totalPurchase改变，对应的Text组件也重新渲染；重新渲染是异步发生的。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/LIAfxm4ORECUXrALjfZqVg/zh-cn_image_0000002552797960.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233904Z&HW-CC-Expire=86400&HW-CC-Sign=7DBAAECB26574A06813E769D924FD3D7D7839B9EFD6AE431463656FA56B1D906)

### @Watch的触发时机

为了展示@Watch回调触发时间是根据状态变量真正变化的时间，本示例在子组件中同时使用@Link和[@ObjectLink](arkts-observed-and-objectlink.md)装饰器，分别观察不同的状态对象。通过在父组件中更改状态变量并观察@Watch回调的先后顺序，来表明@Watch触发的时机与赋值、同步的关系。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { common } from '@kit.AbilityKit';

4. @Observed
5. class Task {
6. public isFinished: boolean = false;

8. constructor(isFinished: boolean) {
9. this.isFinished = isFinished;
10. }
11. }

13. const DOMAIN = 0x0000;

15. @Entry
16. @Component
17. struct ParentComponent {
18. @State @Watch('onTaskAChanged') taskA: Task = new Task(false);
19. @State @Watch('onTaskBChanged') taskB: Task = new Task(false);
20. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
21. // 请将$r('app.string.watch_text5')替换为实际资源文件，在本示例中该资源文件的value值为"父组件任务A状态:"
22. @State type1: string = this.context!.resourceManager.getStringSync($r('app.string.watch_text5').id);
23. // 请将$r('app.string.watch_text6')替换为实际资源文件，在本示例中该资源文件的value值为"父组件任务B状态:"
24. @State type2: string = this.context!.resourceManager.getStringSync($r('app.string.watch_text6').id);

26. onTaskAChanged(changedPropertyName: string): void {
27. // 请将$r('app.string.watch_text12')替换为实际资源文件，在本示例中该资源文件的value值为"观测到父组件任务属性变化:"
28. hilog.info(DOMAIN, this.getUIContext()
29. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text12').id), changedPropertyName);
30. }

32. onTaskBChanged(changedPropertyName: string): void {
33. // 请将$r('app.string.watch_text12')替换为实际资源文件，在本示例中该资源文件的value值为"观测到父组件任务属性变化:"
34. hilog.info(DOMAIN, this.getUIContext()
35. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text12').id), changedPropertyName);
36. }

38. build() {
39. Column() {
40. // 请将$r('app.string.watch_text7')替换为实际资源文件，在本示例中该资源文件的value值为"已完成"
41. // 请将$r('app.string.watch_text8')替换为实际资源文件，在本示例中该资源文件的value值为"未完成"
42. Text(`${this.type1} ${this.taskA.isFinished ? this.getUIContext()
43. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text7').id) :
44. this.getUIContext()
45. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text8').id)}`)
46. Text(`${this.type2} ${this.taskB.isFinished ? this.getUIContext()
47. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text7').id) :
48. this.getUIContext()
49. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text8').id)}`)
50. ChildComponent({ taskA: this.taskA, taskB: this.taskB })
51. // 请将$r('app.string.watch_text9')替换为实际资源文件，在本示例中该资源文件的value值为"切换任务状态"
52. Button(this.getUIContext()
53. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text9').id))
54. .onClick(() => {
55. this.taskB = new Task(!this.taskB.isFinished);
56. this.taskA = new Task(!this.taskA.isFinished);
57. })
58. }
59. }
60. }

62. @Component
63. struct ChildComponent {
64. @ObjectLink @Watch('onObjectLinkTaskChanged') taskB: Task;
65. @Link @Watch('onLinkTaskChanged') taskA: Task;
66. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
67. // 请将$r('app.string.watch_text10')替换为实际资源文件，在本示例中该资源文件的value值为"子组件任务A状态:"
68. @State type1: string = this.context!.resourceManager.getStringSync($r('app.string.watch_text10').id);
69. // 请将$r('app.string.watch_text11')替换为实际资源文件，在本示例中该资源文件的value值为"子组件任务B状态:"
70. @State type2: string = this.context!.resourceManager.getStringSync($r('app.string.watch_text11').id);

72. onObjectLinkTaskChanged(changedPropertyName: string): void {
73. // 请将$r('app.string.watch_text13')替换为实际资源文件，在本示例中该资源文件的value值为"观测到子组件@ObjectLink关联的任务属性变化:"
74. hilog.info(DOMAIN, this.getUIContext()
75. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text13').id), changedPropertyName);
76. }

78. onLinkTaskChanged(changedPropertyName: string): void {
79. // 请将$r('app.string.watch_text14')替换为实际资源文件，在本示例中该资源文件的value值为"观测到子组件@Link关联的任务属性变化:"
80. hilog.info(DOMAIN, this.getUIContext()
81. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text14').id), changedPropertyName);
82. }

84. build() {
85. Column() {
86. // 请将$r('app.string.watch_text7')替换为实际资源文件，在本示例中该资源文件的value值为"已完成"
87. // 请将$r('app.string.watch_text8')替换为实际资源文件，在本示例中该资源文件的value值为"未完成"
88. Text(`${this.type1} ${this.taskA.isFinished ? this.getUIContext()
89. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text7').id) :
90. this.getUIContext()
91. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text8').id)}`)
92. Text(`${this.type2} ${this.taskB.isFinished ? this.getUIContext()
93. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text7').id) :
94. this.getUIContext()
95. .getHostContext()!.resourceManager.getStringSync($r('app.string.watch_text8').id)}`)
96. }
97. }
98. }
```

[ParentComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Watch/entry/src/main/ets/pages/ParentComponent.ets#L19-L97)

处理步骤如下：

1. 当点击按钮切换任务状态时，父组件首先更新了被@ObjectLink关联的taskB，然后更新了被@Link关联的taskA。
2. 观察到日志依次显示：

   ```
   1. 观测到父组件任务属性变化: taskB
   2. 观测到父组件任务属性变化: taskA
   3. 观测到子组件@Link关联的任务属性变化: taskA
   4. 观测到子组件@ObjectLink关联的任务属性变化: taskB
   ```
3. 通过日志可以看到，父组件的回调顺序和修改顺序一致，而子组件中@Link和@ObjectLink的回调触发顺序与父组件中变量更新的顺序不同。这是因为父组件的变量更新是即时的，但子组件中@Link和@ObjectLink获取更新数据的时机不同。@Link的状态更新是同步的，状态变化会立刻触发@Watch回调。而@ObjectLink的更新依赖于父组件的同步，当父组件刷新并将更新后的变量传递给子组件时，@Watch回调才会触发，因此触发顺序略晚于@Link。
4. 这是符合预期的行为，展示了@Watch回调的触发时机是根据状态变量真正变化的时间。因为@Link直接同步，而@ObjectLink需要等父组件更新子组件变量。类似地，@Prop也可能表现出与@ObjectLink类似的行为，其回调触发时间也会略晚。

### 使用changedPropertyName进行不同的逻辑处理

以下示例说明了如何在@Watch函数中使用changedPropertyName进行不同的逻辑处理。

```
1. @Entry
2. @Component
3. struct UsePropertyName {
4. @State @Watch('countUpdated') apple: number = 0;
5. @State @Watch('countUpdated') cabbage: number = 0;
6. @State fruit: number = 0;

8. // @Watch 回调
9. countUpdated(propName: string): void {
10. if (propName === 'apple') {
11. this.fruit = this.apple;
12. }
13. }

15. build() {
16. Column() {
17. Text(`Number of apples: ${this.apple.toString()}`).fontSize(30)
18. Text(`Number of cabbages: ${this.cabbage.toString()}`).fontSize(30)
19. Text(`Total number of fruits: ${this.fruit.toString()}`).fontSize(30)
20. Button('Add apples')
21. .onClick(() => {
22. this.apple++;
23. })
24. Button('Add cabbages')
25. .onClick(() => {
26. this.cabbage++;
27. })
28. }
29. }
30. }
```

[UsePropertyName.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Watch/entry/src/main/ets/pages/UsePropertyName.ets#L15-L47)

处理步骤如下：

1. 点击Button('Add apples')时，apple的值发生变化。
2. 状态管理框架调用@Watch函数countUpdated，发生变化的状态变量名为apple，满足if逻辑条件，fruit的值被改变。
3. 绑定了apple，fruit状态变量的Text重新渲染。
4. 点击Button('Add cabbages')时，cabbage的值发生变化。
5. 状态管理框架调用@Watch函数countUpdated，发生变化的状态变量名为cabbage，不满足if逻辑条件，fruit的值不发生变化。
6. 绑定了cabbage状态变量的Text重新渲染。
