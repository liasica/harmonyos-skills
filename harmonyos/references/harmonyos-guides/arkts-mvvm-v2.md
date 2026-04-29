---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm-v2
title: MVVM模式（V2）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > MVVM模式（V2）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:11+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1f96e6ae6899ccf8377da94df14950830a21cc947e6128362179ed541caeb22e
---

## 概述

在应用开发中，UI的更新需要随着数据状态的变化进行实时同步，而这种同步往往决定了应用程序的性能和用户体验。为了解决数据与UI同步的复杂性，ArkUI采用了Model-View-ViewModel（MVVM）架构模式。MVVM将应用分为Model、View和ViewModel三个核心部分，实现数据、视图与逻辑的分离。通过这种模式，UI可以随着状态的变化自动更新，无需手动处理，从而高效管理数据和视图的绑定与更新。

* Model：存储和管理应用数据及业务逻辑，不直接与用户界面交互。通常从后端接口获取数据，是应用程序的数据基础，确保数据的一致性和完整性。
* View：负责用户界面展示数据并与用户交互，不包含任何业务逻辑。它通过绑定ViewModel层提供的数据来动态更新UI。
* ViewModel：负责管理UI状态和交互逻辑。作为连接Model和View的桥梁，ViewModel监控Model数据的变化，通知View更新UI，同时处理用户交互事件并转换为数据操作。

## 通过状态管理V2版本实现ViewModel

在MVVM模式中，ViewModel负责管理数据状态，并在数据变化时自动更新视图。ArkUI的状态管理V2版本提供了丰富的装饰器和工具，帮助开发者在自定义组件之间共享数据，确保数据变化自动同步到UI。常用的状态管理装饰器包括[@Local](arkts-new-local.md)、[@Param](arkts-new-param.md)、[@Event](arkts-new-event.md)、[@ObservedV2、@Trace](arkts-new-observedv2-and-trace.md)等等。此外，V2还提供了[AppStorageV2](arkts-new-appstoragev2.md)和[PersistenceV2](arkts-new-persistencev2.md)作为全局状态存储工具，用于应用间的状态共享和持久化存储。

本节将通过一个简单的todolist示例，逐步引入和使用状态管理V2的装饰器及工具，从基础的静态任务列表开始，逐步扩展功能。每个步骤都基于上一步扩展，帮助开发者循序渐进地理解并掌握各个装饰器的使用方法。

### 基础示例

首先，从静态待办事项列表开始。在示例1中，任务是静态的，没有状态变化和动态交互。

**示例1**

```
1. // src/main/ets/pages/BasicPage.ets
2. @Entry
3. @ComponentV2
4. struct TodoList {
5. build() {
6. Column() {
7. Text('To do')
8. .fontSize(40)
9. .margin({ bottom: 10 })
10. Text('task1')
11. Text('task2')
12. Text('task3')
13. }
14. }
15. }
```

[BasicPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/BasicPage.ets#L17-L33)

### 添加@Local，实现对组件内部状态观测

完成静态待办列表展示后，为了让用户能够更改任务的完成状态，需要使待办事项能够响应交互并动态更新显示。为此，引入@Local装饰器管理组件内部的状态。被@Local装饰的变量发生变化时，触发绑定的UI组件刷新。

在示例2中，新增@Local装饰的isFinish属性代表任务是否完成。两个图标finished.png和unfinished.png用于展示任务完成或未完成的状态。点击待办事项时，isFinish状态切换，更新图标和文本删除线的效果。

**示例2**

```
1. // src/main/ets/pages/LocalPage.ets
2. @Entry
3. @ComponentV2
4. struct TodoList {
5. @Local isFinish: boolean = false;

7. build() {
8. Column() {
9. Text('To do')
10. .fontSize(40)
11. .margin({ bottom: 10 })
12. Row() {
13. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
14. Image(this.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
15. .width(28)
16. .height(28)
17. Text('task1')
18. .decoration({ type: this.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
19. }
20. .onClick(() => this.isFinish = !this.isFinish)
21. }
22. }
23. }
```

[LocalPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/LocalPage.ets#L17-L41)

### 添加@Param，实现组件接收外部输入

实现任务本地状态切换后，为增强待办事项列表的灵活性，需要能够动态设置每个任务的名称，而不是固定在代码中。引入@Param装饰器后，子组件被装饰的变量可以接收父组件传入的值，实现单向数据同步。@Param默认只读，使用@Param [@Once](arkts-new-once.md)可在子组件中对传入的值进行本地更新。

在示例3中，每个待办事项抽象为TaskItem组件。@Param修饰的taskName属性从父组件TodoList传入任务名称，使TaskItem组件灵活且可复用，能够接收并渲染不同的任务名称。@Param @Once装饰的isFinish属性接收初始值后，可在子组件内更新。

**示例3**

```
1. // src/main/ets/pages/ParamPage.ets
2. @ComponentV2
3. struct TaskItem {
4. @Param taskName: string = '';
5. @Param @Once isFinish: boolean = false;

7. build() {
8. Row() {
9. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
10. Image(this.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
11. .width(28)
12. .height(28)
13. Text(this.taskName)
14. .decoration({ type: this.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
15. }
16. .onClick(() => this.isFinish = !this.isFinish)
17. }
18. }

20. @Entry
21. @ComponentV2
22. struct TodoList {
23. build() {
24. Column() {
25. Text('To do')
26. .fontSize(40)
27. .margin({ bottom: 10 })
28. TaskItem({ taskName: 'Task 1', isFinish: false })
29. TaskItem({ taskName: 'Task 2', isFinish: false })
30. TaskItem({ taskName: 'Task 3', isFinish: false })
31. }
32. }
33. }
```

[ParamPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/ParamPage.ets#L17-L51)

### 添加@Event，实现组件对外输出

实现任务名称动态设置后，任务列表内容固定。为了实现任务列表的动态扩展，需要增加任务项的添加和删除功能。为此，引入@Event装饰器，用于子组件向父组件输出数据。

在示例4中，每个TaskItem增加了删除按钮，同时任务列表底部增加了添加新任务的功能。点击子组件TaskItem的“删除”按钮时，deleteTask事件会被触发并传递给父组件TodoList，父组件响应并移除任务。通过使用@Param和@Event，子组件不仅能接收父组件的数据，还能将事件传递回父组件，实现数据双向同步。

**示例4**

```
1. // src/main/ets/pages/EventPage.ets
2. @ComponentV2
3. struct TaskItem {
4. @Param taskName: string = '';
5. @Param @Once isFinish: boolean = false;
6. @Event deleteTask: () => void = () => {};

8. build() {
9. Row() {
10. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
11. Image(this.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
12. .width(28)
13. .height(28)
14. Text(this.taskName)
15. .decoration({ type: this.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
16. Button('Delete')
17. .onClick(() => {
18. this.deleteTask();
19. })
20. }
21. .onClick(() => {
22. this.isFinish = !this.isFinish;
23. })
24. }
25. }

27. @Entry
28. @ComponentV2
29. struct TodoList {
30. @Local tasks: string[] = ['task1', 'task2', 'task3'];
31. @Local newTaskName: string = '';

33. build() {
34. Column() {
35. Text('To do')
36. .fontSize(40)
37. .margin({ bottom: 10 })
38. ForEach(this.tasks, (task: string) => {
39. TaskItem({
40. taskName: task,
41. isFinish: false,
42. deleteTask: () => {
43. this.tasks.splice(this.tasks.indexOf(task), 1);
44. }
45. })
46. })
47. Row() {
48. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
49. .onChange((value) => {
50. this.newTaskName = value;
51. })
52. .width('70%')
53. Button('+')
54. .onClick(() => {
55. this.tasks.push(this.newTaskName);
56. this.newTaskName = '';
57. })
58. }
59. }
60. }
61. }
```

[EventPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/EventPage.ets#L17-L79)

### 添加Repeat，实现子组件复用

添加任务增删功能后，任务列表项增加，需要高效渲染多个结构相同的子组件，提高界面性能。引入[Repeat](arkts-new-rendering-control-repeat.md)组件，优化任务列表渲染。

Repeat支持两种场景：懒加载场景和非懒加载场景。

* 懒加载场景适用于大量数据的场景，在滚动类容器中按需加载组件，极大节省内存和提升渲染效率。
* 非懒加载场景适用于数据量较小的场景，一次性渲染所有组件，并在数据变化时仅更新需要变化的部分，避免整体重新渲染。

在示例5中，由于任务量较少，使用Repeat非懒加载场景。新建任务数组tasks，并使用Repeat方法迭代数组中的每一项，动态生成并复用TaskItem组件。任务增删时，这种方式能高效复用已有组件，避免重复渲染，提高界面响应速度和性能。这种机制有效地提高了代码的复用性和渲染效率。

**示例5**

```
1. // src/main/ets/pages/RepeatPage.ets
2. @ComponentV2
3. struct TaskItem {
4. @Param taskName: string = '';
5. @Param @Once isFinish: boolean = false;
6. @Event deleteTask: () => void = () => {};

8. build() {
9. Row() {
10. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
11. Image(this.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
12. .width(28)
13. .height(28)
14. Text(this.taskName)
15. .decoration({ type: this.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
16. Button('Delete')
17. .onClick(() => {
18. this.deleteTask();
19. })
20. }
21. .onClick(() => {
22. this.isFinish = !this.isFinish;
23. })
24. }
25. }

27. @Entry
28. @ComponentV2
29. struct TodoList {
30. @Local tasks: string[] = ['task1', 'task2', 'task3'];
31. @Local newTaskName: string = '';

33. build() {
34. Column() {
35. Text('To do')
36. .fontSize(40)
37. .margin({ bottom: 10 })
38. Repeat<string>(this.tasks)
39. .each((obj: RepeatItem<string>) => {
40. TaskItem({
41. taskName: obj.item,
42. isFinish: false,
43. deleteTask: () => {
44. this.tasks.splice(this.tasks.indexOf(obj.item), 1);
45. }
46. })
47. })
48. Row() {
49. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
50. .onChange((value) => {
51. this.newTaskName = value;
52. })
53. .width('70%')
54. Button('+')
55. .onClick(() => {
56. this.tasks.push(this.newTaskName);
57. this.newTaskName = '';
58. })
59. }
60. }
61. }
62. }
```

[RepeatPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/RepeatPage.ets#L17-L80)

### 添加@ObservedV2，@Trace，实现类属性观测变化

实现多个功能后，任务列表管理变得复杂。为了有效处理任务数据的变化，特别是在多层嵌套结构中，需要确保属性变化能够被深度观测并自动更新UI。为此，引入了@ObservedV2和@Trace装饰器。与仅能观测对象及其第一层变化的@Local不同，@ObservedV2和@Trace适用于多层嵌套和继承等复杂场景。在@ObservedV2装饰的类中，@Trace装饰的属性变化时，会触发绑定的UI组件刷新。

在示例6中，任务（Task）被抽象为一个类，并用@ObservedV2标记该类，用@Trace标记isFinish属性。TodoList组件嵌套了TaskItem，TaskItem又嵌套了Task。在最外层的TodoList中，添加了"全部完成"和"全部未完成"的按钮，每次点击这些按钮都会直接更新最内层Task类的isFinish属性。@ObservedV2和@Trace确保可以观察到对应isFinish UI组件的刷新，从而实现了对嵌套类属性的深度观测。

**示例6**

```
1. // src/main/ets/pages/ObservedV2TracePage.ets
2. @ObservedV2
3. class Task {
4. public taskName: string = '';
5. @Trace public isFinish: boolean = false;

7. constructor(taskName: string, isFinish: boolean) {
8. this.taskName = taskName;
9. this.isFinish = isFinish;
10. }
11. }

13. @ComponentV2
14. struct TaskItem {
15. @Param task: Task = new Task('', false);
16. @Event deleteTask: () => void = () => {};

18. build() {
19. Row() {
20. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
21. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
22. .width(28)
23. .height(28)
24. Text(this.task.taskName)
25. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
26. Button('Delete')
27. .onClick(() => {
28. this.deleteTask();
29. })
30. }
31. .onClick(() => {
32. this.task.isFinish = !this.task.isFinish;
33. })
34. }
35. }

37. @Entry
38. @ComponentV2
39. struct TodoList {
40. @Local tasks: Task[] = [
41. new Task('task1', false),
42. new Task('task2', false),
43. new Task('task3', false),
44. ];
45. @Local newTaskName: string = '';

47. finishAll(ifFinish: boolean) {
48. for (let task of this.tasks) {
49. task.isFinish = ifFinish;
50. }
51. }

53. build() {
54. Column() {
55. Text('To do')
56. .fontSize(40)
57. .margin({ bottom: 10 })
58. Repeat<Task>(this.tasks)
59. .each((obj: RepeatItem<Task>) => {
60. TaskItem({
61. task: obj.item,
62. deleteTask: () => {
63. this.tasks.splice(this.tasks.indexOf(obj.item), 1);
64. }
65. })
66. })
67. Row() {
68. Button('All Completed')
69. .onClick(() => {
70. this.finishAll(true);
71. })
72. Button('All Not Completed')
73. .onClick(() => {
74. this.finishAll(false);
75. })
76. }
77. Row() {
78. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
79. .onChange((value) => {
80. this.newTaskName = value;
81. })
82. .width('70%')
83. Button('+')
84. .onClick(() => {
85. this.tasks.push(new Task(this.newTaskName, false));
86. this.newTaskName = '';
87. })
88. }
89. }
90. }
91. }
```

[ObservedV2TracePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/ObservedV2TracePage.ets#L17-L109)

### 添加@Monitor，@Computed，实现监听状态变量和计算属性

在当前任务列表功能基础上，为了提升体验，可以增加一些额外的功能，如任务状态变化的监听和未完成任务数量的动态计算。为此，引入[@Monitor](arkts-new-monitor.md)和[@Computed](arkts-new-computed.md)装饰器。@Monitor用于深度监听状态变量，在属性变化时触发自定义回调方法。@Computed用于装饰getter方法，检测被计算的属性变化。被计算的值变化时，仅计算一次，减少重复计算开销。

在示例7中，使用@Monitor装饰器深度监听TaskItem中task的isFinish属性。当任务完成状态变化时，触发onTaskFinished回调，记录任务完成状态的变化。同时，新增对todolist中未完成任务数量的记录。使用@Computed装饰器定义tasksUnfinished，每当任务状态变化时自动重新计算。通过这两个装饰器，实现了状态变量的深度监听和高效的计算属性。

**示例7**

```
1. // src/main/ets/pages/MonitorComputedPage.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @ObservedV2
5. class Task {
6. public taskName: string = '';
7. @Trace public isFinish: boolean = false;

9. constructor(taskName: string, isFinish: boolean) {
10. this.taskName = taskName;
11. this.isFinish = isFinish;
12. }
13. }

15. @ComponentV2
16. struct TaskItem {
17. @Param task: Task = new Task('', false);
18. @Event deleteTask: () => void = () => {};

20. @Monitor('task.isFinish')
21. onTaskFinished(mon: IMonitor) {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'Task ' + this.task.taskName + ' completion status changed from ' + mon.value()?.before + ' to ' + mon.value()?.now);
23. }

25. build() {
26. Row() {
27. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
28. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
29. .width(28)
30. .height(28)
31. Text(this.task.taskName)
32. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
33. Button('Delete')
34. .onClick(() => {
35. this.deleteTask();
36. })
37. }
38. .onClick(() => {
39. this.task.isFinish = !this.task.isFinish;
40. })
41. }
42. }

44. @Entry
45. @ComponentV2
46. struct TodoList {
47. @Local tasks: Task[] = [
48. new Task('task1', false),
49. new Task('task2', false),
50. new Task('task3', false),
51. ];
52. @Local newTaskName: string = '';

54. finishAll(ifFinish: boolean) {
55. for (let task of this.tasks) {
56. task.isFinish = ifFinish;
57. }
58. }

60. @Computed
61. get tasksUnfinished(): number {
62. return this.tasks.filter(task => !task.isFinish).length;
63. }

65. build() {
66. Column() {
67. Text('To do')
68. .fontSize(40)
69. .margin({ bottom: 10 })
70. Text('Unfinished task' + `：${this.tasksUnfinished}`)
71. Repeat<Task>(this.tasks)
72. .each((obj: RepeatItem<Task>) => {
73. TaskItem({
74. task: obj.item,
75. deleteTask: () => {
76. this.tasks.splice(this.tasks.indexOf(obj.item), 1);
77. }
78. })
79. })
80. Row() {
81. Button('All Completed')
82. .onClick(() => {
83. this.finishAll(true);
84. })
85. Button('All Not Completed')
86. .onClick(() => {
87. this.finishAll(false);
88. })
89. }
90. Row() {
91. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
92. .onChange((value) => {
93. this.newTaskName = value;
94. })
95. .width('70%')
96. Button('+')
97. .onClick(() => {
98. this.tasks.push(new Task(this.newTaskName, false));
99. this.newTaskName = '';
100. })
101. }
102. }
103. }
104. }
```

[MonitorComputedPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/MonitorComputedPage.ets#L16-L121)

### 添加AppStorageV2，实现应用全局UI状态存储

随着待办事项功能的增强，应用涉及多个页面或功能模块时，需要在这些页面之间共享全局状态。例如：在待办事项应用中，新增一个设置页面与主界面联动。为实现跨页面的状态共享，引入AppStorageV2，用于在多个UIAbility实例之间存储和共享应用的全局状态。

在这个示例中，新增了一个Ability，SettingAbility，用于加载设置页面SettingPage。SettingPage包含了一个Setting类，其中的showCompletedTask属性用于控制是否显示已完成的任务。用户可以通过一个开关切换该选项。两个Ability通过AppStorageV2共享设置数据，键为 "Setting"，对应的数据为Setting类。第一次通过connect连接Setting时，如果不存在存储的数据，会创建一个showCompletedTask默认为true的Setting实例。后续用户在设置页面修改设置后，主页面会根据这一设置更新任务列表的显示。通过AppStorageV2，实现了跨Ability、跨页面的数据共享。

**示例8**

```
1. // src/main/ets/pages/AppStorageV2Page.ets
2. import { AppStorageV2 } from '@kit.ArkUI';
3. import { common, Want } from '@kit.AbilityKit';
4. import { Setting } from './SettingPage';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. @ObservedV2
8. class Task {
9. public taskName: string = '';
10. @Trace public isFinish: boolean = false;

12. constructor(taskName: string, isFinish: boolean) {
13. this.taskName = taskName;
14. this.isFinish = isFinish;
15. }
16. }

18. @ComponentV2
19. struct TaskItem {
20. @Param task: Task = new Task('', false);
21. @Event deleteTask: () => void = () => {};

23. @Monitor('task.isFinish')
24. onTaskFinished(mon: IMonitor) {
25. hilog.info(0x0000, 'testTag', '%{public}s', 'Task ' + this.task.taskName + ' completion status changed from ' + mon.value()?.before + ' to ' + mon.value()?.now);
26. }

28. build() {
29. Row() {
30. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
31. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
32. .width(28)
33. .height(28)
34. Text(this.task.taskName)
35. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
36. Button('Delete')
37. .onClick(() => {
38. this.deleteTask();
39. })
40. }
41. .onClick(() => {
42. this.task.isFinish = !this.task.isFinish;
43. })
44. }
45. }

47. @Entry
48. @ComponentV2
49. struct TodoList {
50. @Local tasks: Task[] = [
51. new Task('task1', false),
52. new Task('task2', false),
53. new Task('task3', false),
54. ];
55. @Local newTaskName: string = '';
56. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
57. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

59. finishAll(ifFinish: boolean) {
60. for (let task of this.tasks) {
61. task.isFinish = ifFinish;
62. }
63. }

65. @Computed
66. get tasksUnfinished(): number {
67. return this.tasks.filter(task => !task.isFinish).length;
68. }

70. build() {
71. Column() {
72. Text('To do')
73. .fontSize(40)
74. .margin({ bottom: 10 })
75. Text('Unfinished task' + `：${this.tasksUnfinished}`)
76. Repeat<Task>(this.tasks.filter(task => this.setting.showCompletedTask || !task.isFinish))
77. .each((obj: RepeatItem<Task>) => {
78. TaskItem({
79. task: obj.item,
80. deleteTask: () => {
81. this.tasks.splice(this.tasks.indexOf(obj.item), 1);
82. }
83. })
84. })
85. Row() {
86. Button('All Completed')
87. .onClick(() => {
88. this.finishAll(true);
89. })
90. Button('All Not Completed')
91. .onClick(() => {
92. this.finishAll(false);
93. })
94. Button('Setting')
95. .onClick(() => {
96. let wantInfo: Want = {
97. deviceId: '', // deviceId为空表示本设备。
98. bundleName: 'com.samples.statemgmtv2mvvm', // 替换成AppScope/app.json5里的bundleName。
99. abilityName: 'SettingAbility',
100. };
101. this.context.startAbility(wantInfo);
102. })
103. }
104. Row() {
105. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
106. .onChange((value) => {
107. this.newTaskName = value;
108. })
109. .width('70%')
110. Button('+')
111. .onClick(() => {
112. this.tasks.push(new Task(this.newTaskName, false));
113. this.newTaskName = '';
114. })
115. }
116. }
117. }
118. }
```

[AppStorageV2Page.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/AppStorageV2Page.ets#L17-L136)

```
1. // src/main/ets/pages/SettingPage.ets
2. import { AppStorageV2 } from '@kit.ArkUI';
3. import { common } from '@kit.AbilityKit';

5. @ObservedV2
6. export class Setting {
7. @Trace public showCompletedTask: boolean = true;
8. }

10. @Entry
11. @ComponentV2
12. struct SettingPage {
13. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
14. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

16. build() {
17. Column() {
18. Text('Setting')
19. .fontSize(40)
20. .margin({ bottom: 10 })
21. Row() {
22. Text('Show completed tasks')
23. Toggle({ type: ToggleType.Switch, isOn: this.setting.showCompletedTask })
24. .onChange((isOn) => {
25. this.setting.showCompletedTask = isOn;
26. })
27. }
28. Button('Back to To do')
29. .onClick(() => {
30. this.context.terminateSelf();
31. })
32. .margin({ top: 10 })
33. }
34. .alignItems(HorizontalAlign.Start)
35. }
36. }
```

[SettingPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/SettingPage.ets#L17-L54)

### 添加PersistenceV2，实现持久化UI状态存储

为了确保用户重新打开应用时能看到之前的任务状态，建议使用PersistenceV2进行数据持久化存储。PersistenceV2可将数据保存在设备磁盘上，与AppStorageV2的运行时内存相比，它能确保数据在应用关闭后再次启动时保持不变。

在示例9中，创建了一个TaskList类，用于通过PersistenceV2持久化存储所有任务信息，键为"TaskList"，数据对应TaskList类。第一次通过connect连接TaskList时，如果没有数据，会创建一个默认tasks数组为空的新TaskList实例。在aboutToAppear生命周期函数中，连接到PersistenceV2的TaskList，若无存储任务数据，会从本地文件defaultTasks.json中加载任务并存储到PersistenceV2中。此后，每个任务的完成状态都会同步到PersistenceV2中。这样，即使应用关闭后再次打开，所有任务数据依旧保持不变，实现了持久化的应用状态存储功能。

**示例9**

```
1. // src/main/ets/pages/PersistenceV2Page.ets
2. import { AppStorageV2, PersistenceV2, Type } from '@kit.ArkUI';
3. import { common, Want } from '@kit.AbilityKit';
4. import { Setting } from './SettingPage';
5. import { util } from '@kit.ArkTS';
6. import { hilog } from '@kit.PerformanceAnalysisKit';

8. @ObservedV2
9. class Task {
10. // 未实现构造函数，因为@Type当前不支持带参数的构造函数。
11. @Trace public taskName: string = 'Todo';
12. @Trace public isFinish: boolean = false;
13. }

15. @ObservedV2
16. class TaskList {
17. // 对于复杂对象需要@Type修饰，确保序列化成功。
18. @Type(Task)
19. @Trace public tasks: Task[] = [];

21. constructor(tasks: Task[]) {
22. this.tasks = tasks;
23. }

25. async loadTasks(context: common.UIAbilityContext) {
26. let getJson = await context.resourceManager.getRawFileContent('defaultTasks.json');
27. let textDecoderOptions: util.TextDecoderOptions = { ignoreBOM: true };
28. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
29. let result = textDecoder.decodeToString(getJson);
30. this.tasks = JSON.parse(result).map((task: Task) => {
31. let newTask = new Task();
32. newTask.taskName = task.taskName;
33. newTask.isFinish = task.isFinish;
34. return newTask;
35. });
36. }
37. }

39. @ComponentV2
40. struct TaskItem {
41. @Param task: Task = new Task();
42. @Event deleteTask: () => void = () => {};

44. @Monitor('task.isFinish')
45. onTaskFinished(mon: IMonitor) {
46. hilog.info(0x0000, 'testTag', '%{public}s', 'Task ' + this.task.taskName + ' completion status changed from ' + mon.value()?.before + ' to ' + mon.value()?.now);
47. }

49. build() {
50. Row() {
51. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
52. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
53. .width(28)
54. .height(28)
55. Text(this.task.taskName)
56. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
57. Button('Delete')
58. .onClick(() => {
59. this.deleteTask();
60. })
61. }
62. .onClick(() => {
63. this.task.isFinish = !this.task.isFinish;
64. })
65. }
66. }

68. @Entry
69. @ComponentV2
70. struct TodoList {
71. @Local taskList: TaskList = new TaskList([]);
72. @Local newTaskName: string = '';
73. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
74. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

76. async aboutToAppear() {
77. this.taskList = PersistenceV2.connect(TaskList, 'TaskList', () => new TaskList([]))!;
78. if (this.taskList.tasks.length === 0) {
79. await this.taskList.loadTasks(this.context);
80. }
81. }

83. finishAll(ifFinish: boolean) {
84. for (let task of this.taskList.tasks) {
85. task.isFinish = ifFinish;
86. }
87. }

89. @Computed
90. get tasksUnfinished(): number {
91. return this.taskList.tasks.filter(task => !task.isFinish).length;
92. }

94. build() {
95. Column() {
96. Text('To do')
97. .fontSize(40)
98. .margin({ bottom: 10 })
99. Text('Unfinished task' + `：${this.tasksUnfinished}`)
100. Repeat<Task>(this.taskList.tasks.filter(task => this.setting.showCompletedTask || !task.isFinish))
101. .each((obj: RepeatItem<Task>) => {
102. TaskItem({
103. task: obj.item,
104. deleteTask: () => {
105. this.taskList.tasks.splice(this.taskList.tasks.indexOf(obj.item), 1);
106. }
107. })
108. })
109. Row() {
110. Button('All Completed')
111. .onClick(() => {
112. this.finishAll(true);
113. })
114. Button('All Not Completed')
115. .onClick(() => {
116. this.finishAll(false);
117. })
118. Button('Setting')
119. .onClick(() => {
120. let wantInfo: Want = {
121. deviceId: '', // deviceId为空表示本设备。
122. bundleName: 'com.samples.statemgmtv2mvvm', // 替换成AppScope/app.json5里的bundleName。
123. abilityName: 'SettingAbility',
124. };
125. this.context.startAbility(wantInfo);
126. })
127. }
128. Row() {
129. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
130. .onChange((value) => {
131. this.newTaskName = value;
132. })
133. .width('70%')
134. Button('+')
135. .onClick(() => {
136. let newTask = new Task();
137. newTask.taskName = this.newTaskName;
138. this.taskList.tasks.push(newTask);
139. this.newTaskName = '';
140. })
141. }
142. }
143. }
144. }
```

[PersistenceV2Page.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/PersistenceV2Page.ets#L17-L162)

JSON文件存放在src/main/resources/rawfile/defaultTasks.json路径下。

```
1. [
2. {"taskName": "学习ArkTS开发", "isFinish": false},
3. {"taskName": "健身", "isFinish": false},
4. {"taskName": "买水果", "isFinish": true},
5. {"taskName": "取快递", "isFinish": true},
6. {"taskName": "刷题", "isFinish": true}
7. ]
```

### 添加@Builder，实现自定义构建函数

随着应用功能逐步扩展，代码中的某些UI元素开始重复，不仅增加了代码量，也让维护变得复杂。为解决此问题，建议使用@Builder装饰器，将重复的UI组件抽象为独立的构建方法，便于复用和代码模块化。

在示例10中，通过使用@Builder定义的ActionButton方法，实现了按钮文字、样式和点击事件的统一管理，提高了代码的简洁性和可维护性。同时优化了界面组件的布局和样式，包括间距、颜色和尺寸等视觉元素，最终呈现出一个功能完善且界面简洁美观的待办事项应用。

**示例10**

```
1. // src/main/ets/pages/BuilderPage.ets
2. import { AppStorageV2, PersistenceV2, Type } from '@kit.ArkUI';
3. import { common, Want } from '@kit.AbilityKit';
4. import { Setting } from './SettingPage';
5. import { util } from '@kit.ArkTS';
6. import { hilog } from '@kit.PerformanceAnalysisKit';

8. @ObservedV2
9. class Task {
10. // 未实现构造函数，因为@Type当前不支持带参数的构造函数。
11. @Trace public taskName: string = 'Todo';
12. @Trace public isFinish: boolean = false;
13. }

15. @Builder
16. function actionButton(text: string | Resource, onClick: () => void) {
17. Button(text, { buttonStyle: ButtonStyleMode.NORMAL })
18. .onClick(onClick)
19. .margin({
20. left: 10,
21. right: 10,
22. top: 5,
23. bottom: 5
24. })
25. }

27. @ObservedV2
28. class TaskList {
29. // 对于复杂对象需要@Type修饰，确保序列化成功。
30. @Type(Task)
31. @Trace public tasks: Task[] = [];

33. constructor(tasks: Task[]) {
34. this.tasks = tasks;
35. }

37. async loadTasks(context: common.UIAbilityContext) {
38. let getJson = await context.resourceManager.getRawFileContent('defaultTasks.json');
39. let textDecoderOptions: util.TextDecoderOptions = { ignoreBOM: true };
40. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
41. let result = textDecoder.decodeToString(getJson);
42. this.tasks = JSON.parse(result).map((task: Task) => {
43. let newTask = new Task();
44. newTask.taskName = task.taskName;
45. newTask.isFinish = task.isFinish;
46. return newTask;
47. });
48. }
49. }

51. @ComponentV2
52. struct TaskItem {
53. @Param task: Task = new Task();
54. @Event deleteTask: () => void = () => {};

56. @Monitor('task.isFinish')
57. onTaskFinished(mon: IMonitor) {
58. hilog.info(0x0000, 'testTag', '%{public}s', 'Task ' + this.task.taskName + ' completion status changed from ' + mon.value()?.before + ' to ' + mon.value()?.now);
59. }

61. build() {
62. Row() {
63. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
64. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
65. .width(28)
66. .height(28)
67. .margin({ left: 15, right: 10 })
68. Text(this.task.taskName)
69. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
70. .fontSize(18)
71. actionButton('Delete', () => {
72. this.deleteTask();
73. })
74. }
75. .height('7%')
76. .width('90%')
77. .backgroundColor('#90f1f3f5')
78. .borderRadius(25)
79. .onClick(() => {
80. this.task.isFinish = !this.task.isFinish;
81. })
82. }
83. }

85. @Entry
86. @ComponentV2
87. struct TodoList {
88. @Local taskList: TaskList = PersistenceV2.connect(TaskList, 'TaskList', () => new TaskList([]))!;
89. @Local newTaskName: string = '';
90. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
91. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

93. async aboutToAppear() {
94. if (this.taskList.tasks.length === 0) {
95. await this.taskList.loadTasks(this.context);
96. }
97. }

99. finishAll(ifFinish: boolean) {
100. for (let task of this.taskList.tasks) {
101. task.isFinish = ifFinish;
102. }
103. }

105. @Computed
106. get tasksUnfinished(): number {
107. return this.taskList.tasks.filter(task => !task.isFinish).length;
108. }

110. build() {
111. Column() {
112. Text('To do')
113. .fontSize(40)
114. .margin(10)
115. Text('Unfinished task' + `：${this.tasksUnfinished}`)
116. .margin({ left: 10, bottom: 10 })
117. Repeat<Task>(this.taskList.tasks.filter(task => this.setting.showCompletedTask || !task.isFinish))
118. .each((obj: RepeatItem<Task>) => {
119. TaskItem({
120. task: obj.item,
121. deleteTask: () => {
122. this.taskList.tasks.splice(this.taskList.tasks.indexOf(obj.item), 1);
123. }
124. })
125. .margin(5)
126. })
127. Row() {
128. actionButton('All Completed', (): void => this.finishAll(true))
129. actionButton('All Not Completed', (): void => this.finishAll(false))
130. actionButton('Setting', (): void => {
131. let wantInfo: Want = {
132. deviceId: '', // deviceId为空表示本设备。
133. bundleName: 'com.samples.statemgmtv2mvvm', // 替换成AppScope/app.json5里的bundleName。
134. abilityName: 'SettingAbility',
135. };
136. this.context.startAbility(wantInfo);
137. })
138. }
139. .margin({ top: 10, bottom: 5 })
140. Row() {
141. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
142. .onChange((value) => {
143. this.newTaskName = value;
144. })
145. .width('70%')
146. actionButton('+', (): void => {
147. let newTask = new Task();
148. newTask.taskName = this.newTaskName;
149. this.taskList.tasks.push(newTask);
150. this.newTaskName = '';
151. })
152. }
153. }
154. .height('100%')
155. .width('100%')
156. .alignItems(HorizontalAlign.Start)
157. .margin({ left: 15 })
158. }
159. }
```

[BuilderPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/BuilderPage.ets#L17-L177)

### 效果图展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/ZKxkHgGaRd-5wFKcK1_RIA/zh-cn_image_0000002589243893.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052709Z&HW-CC-Expire=86400&HW-CC-Sign=FCF1A395954CC5C6091505F44445A6D9A9F04FDE729719C8E12D6658646B226E)

## 重构代码以符合MVVM架构

前面的例子通过使用一系列的状态管理装饰器，实现了todolist中的数据同步与UI更新。然而，随着应用功能的复杂化，代码的结构变得难以维护，Model、View和ViewModel的职责没有完全分离，存在耦合。为了更好地组织代码和提升可维护性，使用MVVM模式重构代码，进一步将数据层（Model）、逻辑层（ViewModel）和展示层（View）分离。

### 重构后的代码结构

```
1. /src
2. ├── /main
3. │   ├── /ets
4. │   │   ├── /entryability
5. │   │   ├── /model
6. │   │   │   ├── TaskListModel.ets
7. │   │   │   └── TaskModel.ets
8. │   │   ├── /pages
9. │   │   │   ├── SettingPage.ets
10. │   │   │   └── TodoListPage.ets
11. │   │   ├── /settingability
12. │   │   ├── /view
13. │   │   │   ├── BottomView.ets
14. │   │   │   ├── ListView.ets
15. │   │   │   └── TitleView.ets
16. │   │   ├── /viewmodel
17. │   │   │   ├── TaskListViewModel.ets
18. │   │   │   └── TaskViewModel.ets
19. │   └── /resources
20. │       ├── ...
21. ├─── ...
```

### Model层

Model层负责管理应用的数据及其业务逻辑，通常与后端或数据存储进行交互。在todolist应用中，Model层的主要职责是存储任务数据、加载任务列表，并提供数据操作的接口，而不直接涉及UI展示。

* TaskModel：单个任务的基本数据结构，包含任务名称和完成状态。

  ```
  1. export default class TaskModel {
  2. public taskName: string = 'Todo';
  3. public isFinish: boolean = false;
  4. }
  ```

  [TaskModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/model/TaskModel.ets#L18-L23)
* TaskListModel：任务的集合，提供从本地加载任务数据的功能。

  ```
  1. import { common } from '@kit.AbilityKit';
  2. import { util } from '@kit.ArkTS';
  3. import TaskModel from './TaskModel';
  4. import { hilog } from '@kit.PerformanceAnalysisKit';

  6. const DOMAIN = 0x0000;

  8. // Model层：TaskListModel负责加载任务列表
  9. export default class TaskListModel {
  10. public tasks: TaskModel[] = [];

  12. constructor(tasks: TaskModel[]) {
  13. this.tasks = tasks;
  14. }

  16. async loadTasks(context: common.UIAbilityContext) {
  17. try {
  18. let getJson = await context.resourceManager.getRawFileContent('defaultTasks.json');
  19. let textDecoderOptions: util.TextDecoderOptions = { ignoreBOM: true };
  20. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
  21. let result = textDecoder.decodeToString(getJson);
  22. this.tasks = JSON.parse(result).map((task: TaskModel) => {
  23. let newTask = new TaskModel();
  24. newTask.taskName = task.taskName;
  25. newTask.isFinish = task.isFinish;
  26. return newTask;
  27. });
  28. } catch (e) {
  29. hilog.error(DOMAIN, 'testTag', 'Failed to getRawFileContent', JSON.stringify(e) ?? '');
  30. }
  31. }
  32. }
  ```

  [TaskListModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/model/TaskListModel.ets#L18-L43)

### ViewModel层

ViewModel层管理UI状态和业务逻辑，连接Model和View。通过监控Model数据变化，处理应用逻辑，将数据同步到View层，从而实现UI的自动更新。使用ViewModel实现数据与视图解耦，提高代码可读性和可维护性。

* TaskViewModel：封装单个任务的数据和状态变更逻辑，通过状态装饰器监控数据的变化。

  ```
  1. // src/main/ets/viewmodel/TaskViewModel.ets
  2. import TaskModel from '../model/TaskModel';

  4. @ObservedV2
  5. export default class TaskViewModel {
  6. @Trace public taskName: string = 'Todo';
  7. @Trace public isFinish: boolean = false;

  9. updateTask(task: TaskModel) {
  10. this.taskName = task.taskName;
  11. this.isFinish = task.isFinish;
  12. }

  14. updateIsFinish(): void {
  15. this.isFinish = !this.isFinish;
  16. }
  17. }
  ```

  [TaskViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/viewmodel/TaskViewModel.ets#L17-L35)
* TaskListViewModel：封装了任务列表以及管理功能，包括加载任务、批量更新任务状态，以及添加和删除任务。

  ```
  1. // src/main/ets/viewmodel/TaskListViewModel.ets
  2. import { common } from '@kit.AbilityKit';
  3. import { Type } from '@kit.ArkUI';
  4. import TaskListModel from '../model/TaskListModel';
  5. import TaskViewModel from './TaskViewModel';

  7. @ObservedV2
  8. export default class TaskListViewModel {
  9. @Type(TaskViewModel)
  10. @Trace public tasks: TaskViewModel[] = [];

  12. async loadTasks(context: common.UIAbilityContext) {
  13. let taskList = new TaskListModel([]);
  14. await taskList.loadTasks(context);
  15. for (let task of taskList.tasks) {
  16. let taskViewModel = new TaskViewModel();
  17. taskViewModel.updateTask(task);
  18. this.tasks.push(taskViewModel);
  19. }
  20. }

  22. finishAll(ifFinish: boolean): void {
  23. for (let task of this.tasks) {
  24. task.isFinish = ifFinish;
  25. }
  26. }

  28. addTask(newTask: TaskViewModel): void {
  29. this.tasks.push(newTask);
  30. }

  32. removeTask(removedTask: TaskViewModel): void {
  33. this.tasks.splice(this.tasks.indexOf(removedTask), 1);
  34. }
  35. }
  ```

  [TaskListViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/viewmodel/TaskListViewModel.ets#L17-L53)

### View层

View层负责应用程序的UI展示和与用户的交互。它只关注如何渲染用户界面和展示数据，不包含业务逻辑。所有的数据状态和逻辑都来自ViewModel层，View层通过接收ViewModel传递的状态数据进行渲染，确保视图和数据分离。

* TitleView：负责展示应用的标题和未完成任务的统计信息。

  ```
  1. // src/main/ets/view/TitleView.ets
  2. @ComponentV2
  3. export default struct TitleView {
  4. @Param tasksUnfinished: number = 0;

  6. build() {
  7. Column() {
  8. Text('To do')
  9. .fontSize(40)
  10. .margin(10)
  11. Text(`All Not Completed：${this.tasksUnfinished}`)
  12. .margin({ left: 10, bottom: 10 })
  13. }
  14. }
  15. }
  ```

  [TitleView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/view/TitleView.ets#L17-L33)
* ListView：负责展示任务列表，并根据Setting中的设置筛选是否显示已完成的任务。它依赖于TaskListViewModel来获取任务数据，并通过TaskItem组件进行渲染，包括任务的名称、完成状态以及删除按钮。通过TaskViewModel和TaskListViewModel实现用户的交互，如切换任务完成状态和删除任务。

  ```
  1. // src/main/ets/view/ListView.ets
  2. import TaskViewModel from '../viewmodel/TaskViewModel';
  3. import TaskListViewModel from '../viewmodel/TaskListViewModel';
  4. import { Setting } from '../pages/SettingPage';
  5. import { ActionButton } from './BottomView';
  6. import { hilog } from '@kit.PerformanceAnalysisKit';

  8. @ComponentV2
  9. struct TaskItem {
  10. @Param task: TaskViewModel = new TaskViewModel();
  11. @Event deleteTask: () => void = () => {};

  13. @Monitor('task.isFinish')
  14. onTaskFinished(mon: IMonitor) {
  15. hilog.info(0x0000, 'testTag', '%{public}s', 'Task ' + this.task.taskName + ' completion status changed from ' + mon.value()?.before + ' to ' + mon.value()?.now);
  16. }

  18. build() {
  19. Row() {
  20. // 请开发者自行在src/main/resources/base/media路径下添加finished.png和unfinished.png两张图片，否则运行时会因资源缺失而报错。
  21. Image(this.task.isFinish ? $r('app.media.finished') : $r('app.media.unfinished'))
  22. .width(28)
  23. .height(28)
  24. .margin({ left: 15, right: 10 })
  25. Text(this.task.taskName)
  26. .decoration({ type: this.task.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
  27. .fontSize(18)
  28. ActionButton('Delete', () => this.deleteTask());
  29. }
  30. .height('7%')
  31. .width('90%')
  32. .backgroundColor('#90f1f3f5')
  33. .borderRadius(25)
  34. .onClick(() => this.task.updateIsFinish())
  35. }
  36. }

  38. @ComponentV2
  39. export default struct ListView {
  40. @Param taskList: TaskListViewModel = new TaskListViewModel();
  41. @Param setting: Setting = new Setting();

  43. build() {
  44. Repeat<TaskViewModel>(this.taskList.tasks.filter(task => this.setting.showCompletedTask || !task.isFinish))
  45. .each((obj: RepeatItem<TaskViewModel>) => {
  46. TaskItem({
  47. task: obj.item,
  48. deleteTask: () => this.taskList.removeTask(obj.item)
  49. }).margin(5)
  50. })
  51. }
  52. }
  ```

  [ListView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/view/ListView.ets#L17-L69)
* BottomView：负责提供与任务操作相关的按钮和输入框，如"全部完成"、"全部未完成"，"设置"三个按钮，以及添加新任务的输入框。点击"全部完成"和"全部未完成"时，通过TaskListViewModel更改所有任务的状态。点击"设置"按钮时，会导航到SettingAbility的设置页面。添加新任务时，通过TaskListViewModel新增任务到任务列表中。

  ```
  1. // src/main/ets/view/BottomView.ets
  2. import { common, Want } from '@kit.AbilityKit';
  3. import TaskViewModel from '../viewmodel/TaskViewModel';
  4. import TaskListViewModel from '../viewmodel/TaskListViewModel';

  6. @Builder
  7. export function ActionButton(text: string | Resource, onClick: () => void) {
  8. Button(text, { buttonStyle: ButtonStyleMode.NORMAL })
  9. .onClick(onClick)
  10. .margin({
  11. left: 10,
  12. right: 10,
  13. top: 5,
  14. bottom: 5
  15. })
  16. }

  18. @ComponentV2
  19. export default struct BottomView {
  20. @Param taskList: TaskListViewModel = new TaskListViewModel();
  21. @Local newTaskName: string = '';
  22. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  24. build() {
  25. Column() {
  26. Row() {
  27. ActionButton('All Completed', (): void => this.taskList.finishAll(true))
  28. ActionButton('All Not Completed', (): void => this.taskList.finishAll(false))
  29. }
  30. .margin({ top: 10 })

  32. Row() {
  33. ActionButton('Setting', (): void => {
  34. let wantInfo: Want = {
  35. deviceId: '', // deviceId为空表示本设备。
  36. bundleName: 'com.samples.statemgmtv2mvvm', // 替换成AppScope/app.json5里的bundleName。
  37. abilityName: 'SettingAbility',
  38. };
  39. this.context.startAbility(wantInfo);
  40. })
  41. }
  42. .margin({ bottom: 5 })

  44. Row() {
  45. TextInput({ placeholder: 'Add new tasks', text: this.newTaskName })
  46. .onChange((value) => this.newTaskName = value)
  47. .width('70%')
  48. ActionButton('+', (): void => {
  49. let newTask = new TaskViewModel();
  50. newTask.taskName = this.newTaskName;
  51. this.taskList.addTask(newTask);
  52. this.newTaskName = '';
  53. })
  54. }
  55. }
  56. }
  57. }
  ```

  [BottomView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/view/BottomView.ets#L17-L67)
* TodoListPage：todolist的主页面，包含以上的三个View组件（TitleView、ListView、BottomView），用于统一展示待办事项的各个部分，管理任务列表和用户设置。TodoListPage负责从ViewModel中获取数据，并将数据传递给各个子View组件进行渲染，通过PersistenceV2持久化任务数据，确保数据在应用重启后仍能保持一致。

  ```
  1. // src/main/ets/pages/TodoListPage.ets
  2. import TaskListViewModel from '../viewmodel/TaskListViewModel';
  3. import { common } from '@kit.AbilityKit';
  4. import { AppStorageV2, PersistenceV2 } from '@kit.ArkUI';
  5. import { Setting } from '../pages/SettingPage';
  6. import TitleView from '../view/TitleView';
  7. import ListView from '../view/ListView';
  8. import BottomView from '../view/BottomView';

  10. @Entry
  11. @ComponentV2
  12. struct TodoList {
  13. @Local taskList: TaskListViewModel = PersistenceV2.connect(TaskListViewModel, 'TaskList', () => new TaskListViewModel())!;
  14. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
  15. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  17. async aboutToAppear() {
  18. if (this.taskList.tasks.length === 0) {
  19. await this.taskList.loadTasks(this.context);
  20. }
  21. }

  23. @Computed
  24. get tasksUnfinished(): number {
  25. return this.taskList.tasks.filter(task => !task.isFinish).length;
  26. }

  28. build() {
  29. Column() {
  30. TitleView({ tasksUnfinished: this.tasksUnfinished })
  31. ListView({ taskList: this.taskList, setting: this.setting });
  32. BottomView({ taskList: this.taskList });
  33. }
  34. .height('100%')
  35. .width('100%')
  36. .alignItems(HorizontalAlign.Start)
  37. .margin({ left: 15 })
  38. }
  39. }
  ```

  [TodoListPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/TodoListPage.ets#L17-L57)
* SettingPage：设置页面，负责管理是否显示已完成任务的设置。通过AppStorageV2应用全局存储用户的设置，用户通过Toggle开关切换showCompletedTask状态。

  ```
  1. // src/main/ets/pages/SettingPage.ets
  2. import { AppStorageV2 } from '@kit.ArkUI';
  3. import { common } from '@kit.AbilityKit';

  5. @ObservedV2
  6. export class Setting {
  7. @Trace public showCompletedTask: boolean = true;
  8. }

  10. @Entry
  11. @ComponentV2
  12. struct SettingPage {
  13. @Local setting: Setting = AppStorageV2.connect(Setting, 'Setting', () => new Setting())!;
  14. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  16. build(){
  17. Column(){
  18. Text('Setting')
  19. .fontSize(40)
  20. .margin({ bottom: 10 })
  21. Row() {
  22. Text('Show completed tasks')
  23. Toggle({ type: ToggleType.Switch, isOn:this.setting.showCompletedTask })
  24. .onChange((isOn) => {
  25. this.setting.showCompletedTask = isOn;
  26. })
  27. }
  28. Button('Back to To do')
  29. .onClick(()=>this.context.terminateSelf())
  30. .margin({ top: 10 })
  31. }
  32. .alignItems(HorizontalAlign.Start)
  33. }
  34. }
  ```

  [SettingPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateMgmtV2MVVM/entry/src/main/ets/pages/SettingPage.ets#L17-L54)

## 总结

本指南通过待办事项应用示例，引入状态管理V2装饰器，并通过代码重构实现MVVM架构。最终将数据、业务逻辑和视图展示分层处理，使得代码结构更加清晰且易于维护。开发者通过正确应用Model、View和ViewModel分层结构，能够更好地理解和应用MVVM模式，进而在实际项目中提升开发效率、保证代码质量，并优化数据与UI的同步机制，简化整体开发流程。

## 代码示例

[完整源码](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/StateMgmtV2MVVM/entry)
