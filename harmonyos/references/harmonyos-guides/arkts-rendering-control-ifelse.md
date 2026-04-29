---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse
title: if/else：条件渲染
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式渲染控制 > if/else：条件渲染
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:33+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8bf49de19b5d3583c736bf1f0750a31fd5601d943f82587c00efbf0a7af83c16
---

ArkTS提供了渲染控制能力。条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。

说明

从API version 9开始，该接口支持在ArkTS卡片中使用。

## 使用规则

* 支持if、else和else if语句。
* if和else if后的条件语句可以使用状态变量或常规变量（状态变量的值改变时会实时渲染UI，而常规变量的值改变则不会）。
* 允许在容器组件内使用，通过条件渲染语句构建不同的子组件。
* 条件渲染语句在涉及到组件的父子关系时是“透明”的，父组件和子组件之间的条件渲染语句不影响父组件关于子组件使用的限制。例如，某些容器组件限制子组件的类型或数量。将条件渲染语句用于这些组件内时，这些限制同样适用于条件渲染语句内创建的组件。具体而言，[Grid](../harmonyos-references/ts-container-grid.md)容器组件的子组件仅支持[GridItem](../harmonyos-references/ts-container-griditem.md)组件。在Grid内使用条件渲染语句时，条件渲染语句内仅允许使用GridItem组件。
* 每个分支内部的构建函数必须遵循构建函数的规则，并创建一个或多个组件。无法创建组件的空构建函数会产生语法错误。关于构建函数的规则，请参考：[基本语法概述](arkts-basic-syntax-overview.md)、[声明式UI描述](arkts-declarative-ui-description.md)。

## 更新机制

当if、else if后跟随的状态判断中使用的状态变量值变化时，条件渲染语句会进行更新，更新步骤如下：

1. 评估if和else if的状态判断条件，如果分支没有变化，无需执行以下步骤。如果分支有变化，则执行2、3步骤。
2. 移除此前构建的所有子组件。
3. 执行新分支的构造函数，将生成的子组件添加到if父容器中。如果缺少适用的else分支，则不创建任何内容。

条件可以包含Typescript表达式。构造函数中的表达式不得更改应用程序状态。

## 使用场景

### 使用if进行条件渲染

```
1. @Entry
2. @Component
3. struct IfExample {
4. @State count: number = 0;

6. build() {
7. Column() {
8. Text(`count=${this.count}`)

10. if (this.count > 0) {
11. Text(`count is positive`)
12. .fontColor(Color.Green)
13. }

15. Button('increase count')
16. .onClick(() => {
17. this.count++;
18. })

20. Button('decrease count')
21. .onClick(() => {
22. this.count--;
23. })
24. }
25. }
26. }
```

[IfRendering.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingIf/IfRendering.ets#L16-L43)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/rvdtQ32HSkSMAE-RjQrUyw/zh-cn_image_0000002589324001.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=E26F34D1528109B1FBE522A71576C403D424FAA9022442DEFA1C9FF6B4E5C9AE)

if语句的每个分支都包含一个构建函数。此类构建函数必须创建一个或多个子组件。在初始渲染时，if语句会执行构建函数，并将生成的子组件添加到其父组件中。

每当if或else if条件语句中使用的状态变量发生变化时，条件语句都会更新并重新评估新的条件值。如果条件值评估发生了变化，这意味着需要构建另一个条件分支。此时ArkUI框架将：

1. 移除所有以前渲染的（早期分支的）组件。
2. 执行新分支的构造函数，将生成的子组件添加到其父组件中。

在以上示例中，当count从0增至1时，if (this.count > 0)更新为true，执行该分支的构造函数，创建一个[Text](../harmonyos-references/ts-basic-components-text.md)组件并添加到父组件Column中。如果后续count更改为0，则Text组件将从[Column](../harmonyos-references/ts-container-column.md)组件中删除。由于没有else分支，因此不会执行新的构造函数。

### if ... else ...语句和子组件状态

以下示例包含if ... else ...语句与拥有[@State](arkts-state.md)装饰变量的子组件。

```
1. @Component
2. struct CounterView {
3. @State counter: number = 0;
4. label: string = 'unknown';

6. build() {
7. Column({ space: 20 }) {
8. Text(`${this.label}`)
9. Button(`counter ${this.counter} +1`)
10. .onClick(() => {
11. this.counter += 1;
12. })
13. }
14. .margin(10)
15. .padding(10)
16. .border({ width: 1 })
17. }
18. }

20. @Entry
21. @Component
22. struct MainView {
23. @State toggle: boolean = true;

25. build() {
26. Column() {
27. if (this.toggle) {
28. CounterView({ label: 'CounterView #positive' });
29. } else {
30. CounterView({ label: 'CounterView #negative' });
31. }
32. Button(`toggle ${this.toggle}`)
33. .onClick(() => {
34. this.toggle = !this.toggle;
35. })
36. }
37. .width('100%')
38. .justifyContent(FlexAlign.Center)
39. }
40. }
```

[IfElseRendering.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingIf/IfElseRendering.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/bW_p9ijgQriVwaaw6U-XTA/zh-cn_image_0000002589243941.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=496382BFE153EC9FE36900852B8092797AA00BAF689457BBAAF0B562FC709A63)

**初次渲染**：创建CounterView子组件（label为 'CounterView #positive'），其状态变量counter初始值为0。

**修改CounterView的counter状态变量**：CounterView子组件（label为 'CounterView #positive'）重新渲染并保留状态变量值。

**修改MainView.toggle状态变量为false**：MainView父组件内的if语句将更新，并进行以下处理：

1. 删除旧的CounterView子组件（label为 'CounterView #positive'）。
2. 创建新的CounterView子组件（label为 'CounterView #negative'），其状态变量counter初始值为0。

说明

CounterView（label为 'CounterView #positive'）和CounterView（label为 'CounterView #negative'）是同一自定义组件的两个不同实例。if分支的更改，不会更新现有子组件，也不会保留状态。

以下示例展示了条件更改时，若需要保留counter值所做的修改。

```
1. @Component
2. struct KeepCounterView {
3. @Link counter: number;
4. label: string = 'unknown';

6. build() {
7. Column({ space: 20 }) {
8. Text(`${this.label}`)
9. .fontSize(20)
10. Button(`counter ${this.counter} +1`)
11. .onClick(() => {
12. this.counter += 1;
13. })
14. }
15. .margin(10)
16. .padding(10)
17. .border({ width: 1 })
18. }
19. }

21. @Entry
22. @Component
23. struct KeepMainView {
24. @State toggle: boolean = true;
25. @State counter: number = 0;

27. build() {
28. Column() {
29. if (this.toggle) {
30. KeepCounterView({ counter: $counter, label: 'CounterView #positive' });
31. } else {
32. KeepCounterView({ counter: $counter, label: 'CounterView #negative' });
33. }
34. Button(`toggle ${this.toggle}`)
35. .onClick(() => {
36. this.toggle = !this.toggle;
37. })
38. }
39. .width('100%')
40. .justifyContent(FlexAlign.Center)
41. }
42. }
```

[KeepCounter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingIf/KeepCounter.ets#L16-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/xDfvdfMNS2muuqA7at0lqw/zh-cn_image_0000002558764134.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=D1B47048606B70644DAEAC16B01D74515215AC2E8EB622862A85F6E17B7C67FA)

此处，@State counter变量归父组件所有。因此，当KeepCounterView组件实例被删除时，该变量不会被销毁。KeepCounterView组件通过[@Link](arkts-link.md)装饰器引用状态。状态必须从子级移动到其父级（或父级的父级），以避免在条件内容或重复内容被销毁时丢失状态。

### 嵌套if语句

嵌套条件语句不会影响父组件的相关规则。

```
1. @Entry
2. @Component
3. struct NestedIf {
4. @State toggle: boolean = false;
5. @State toggleColor: boolean = false;

7. build() {
8. Column({ space: 20 }) {
9. Text('Before')
10. .fontSize(15)
11. if (this.toggle) {
12. Text('Top True, positive 1 top')
13. .backgroundColor('#aaffaa').fontSize(20)
14. // 内部if语句
15. if (this.toggleColor) {
16. Text('Top True, Nested True, positive COLOR  Nested ')
17. .backgroundColor('#00aaaa').fontSize(15)
18. } else {
19. Text('Top True, Nested False, Negative COLOR  Nested ')
20. .backgroundColor('#aaaaff').fontSize(15)
21. }
22. } else {
23. Text('Top false, negative top level').fontSize(20)
24. .backgroundColor('#ffaaaa')
25. if (this.toggleColor) {
26. Text('positive COLOR  Nested ')
27. .backgroundColor('#00aaaa').fontSize(15)
28. } else {
29. Text('Negative COLOR  Nested ')
30. .backgroundColor('#aaaaff').fontSize(15)
31. }
32. }
33. Text('After')
34. .fontSize(15)
35. Button('Toggle Outer')
36. .onClick(() => {
37. this.toggle = !this.toggle;
38. })
39. Button('Toggle Inner')
40. .onClick(() => {
41. this.toggleColor = !this.toggleColor;
42. })
43. }
44. .width('100%')
45. .justifyContent(FlexAlign.Center)
46. }
47. }
```

[NestedIf.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingIf/NestedIf.ets#L16-L64)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/_e-BtywpToWA_DrIsXPxuA/zh-cn_image_0000002558604478.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=23BD907B8BE2BA33D6DB03AE0009E913DCAA1A92B06B41E68BAD83A8D2A79479)
