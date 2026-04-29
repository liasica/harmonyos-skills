---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-new-lifecycle
title: 自定义组件的生命周期（推荐）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件的生命周期（推荐）
category: harmonyos-references
scraped_at: 2026-04-29T13:52:54+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f5ec50f03261decf89141feabe228e132f1f5a6e50da1e1e5c50b1728675a656
---

自定义组件的生命周期回调函数用于通知用户该自定义组件的生命周期，这些回调函数是私有的，在运行时由开发框架在特定的时间进行调用，不能从应用程序中手动调用这些回调函数。

说明

* 本模块首批接口从API version 23开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @ComponentInit

PhonePC/2in1TabletTVWearable

ComponentInit: MethodDecorator

@ComponentInit装饰的函数在自定义组件初始化即将完成时执行。开发者可以在此时注册监听和修改变量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## @ComponentAppear

PhonePC/2in1TabletTVWearable

ComponentAppear: MethodDecorator

与aboutToAppear相似，@ComponentAppear装饰的函数在创建自定义组件的新实例后，在其build()函数执行前调用，不同的是，@ComponentAppear装饰的函数仅在自定义组件处于[CustomComponentLifecycleState](ts-custom-component-new-lifecycle.md#customcomponentlifecyclestate).INIT状态才会触发。允许在@ComponentAppear装饰的函数中改变状态变量，更改将在后续执行build()函数中生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## @ComponentBuilt

PhonePC/2in1TabletTVWearable

ComponentBuilt: MethodDecorator

@ComponentBuilt装饰的函数在自定义组件的build()函数首次执行后调用，即从CustomComponentLifecycleState.APPEARED到CustomComponentLifecycleState.BUILT的阶段触发。开发者可以在这个阶段实现埋点数据上报等不影响实际UI的功能。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## @ComponentDisappear

PhonePC/2in1TabletTVWearable

ComponentDisappear: MethodDecorator

@ComponentDisappear装饰的函数在自定义组件析构销毁时执行。不建议在此函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## @ComponentReuse

PhonePC/2in1TabletTVWearable

ComponentReuse: MethodDecorator

当可复用的自定义组件从缓存中重新添加到节点树时调用@ComponentReuse装饰的函数，即从CustomComponentLifecycleState.RECYCLED到CustomComponentLifecycleState.BUILT阶段触发，以接收组件的构造参数。最后，复用会递归遍历所有子组件，对每个完成复用的子组件，会调用子组件中@ComponentReuse装饰的函数。

说明

* 在状态管理V1的组件里，@ComponentReuse装饰的函数允许有一个入参或者无参。入参params建议为Record<string, Object | undefined | null>类型。
* 在状态管理V2的组件里，@ComponentReuse装饰的函数没有入参。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Record<string, Object | undefined | null> | 否 | 当params存在时，表示V1组件的复用回调。 |

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## @ComponentRecycle

PhonePC/2in1TabletTVWearable

ComponentRecycle: MethodDecorator

当组件被回收后触发，先执行应用程序中定义的必要回收操作，完成回收后调用此装饰器装饰的函数，即从CustomComponentLifecycleState.BUILT到CustomComponentLifecycleState.RECYCLED阶段触发。最后，回收会递归遍历所有子组件，对每个完成回收的子组件调用子组件中@ComponentRecycle装饰的函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

参见[生命周期使用示例](ts-custom-component-new-lifecycle.md#生命周期使用示例)。

## CustomComponentLifecycle

PhonePC/2in1TabletTVWearable

CustomComponentLifecycle用于监控自定义组件生命周期的变化，开发者可以通过[UIUtils.getLifecycle](js-apis-statemanagement.md#getlifecycle23)获取CustomComponentLifecycle实例。

### getCurrentState

PhonePC/2in1TabletTVWearable

getCurrentState(): CustomComponentLifecycleState

getCurrentState函数用于获得自定义组件当前的生命周期状态。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CustomComponentLifecycleState](ts-custom-component-new-lifecycle.md#customcomponentlifecyclestate) | 自定义组件当前的生命周期状态。 |

**示例：**

```
1. import { UIUtils, ComponentBuilt } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. @Entry
4. @Component
5. struct Index {
6. @ComponentBuilt
7. myBuilt() {
8. // CustomComponentLifecycle.getCurrentState用于获得自定义组件当前的生命周期状态
9. hilog.info(0x0000, 'testTag', 'Index Lifecycle is %{public}d', UIUtils.getLifecycle(this).getCurrentState());
10. }
11. build() {
12. Column() {
13. Text(`HelloWorld`)
14. }
15. .height('100%')
16. .width('100%')
17. }
18. }
```

### addObserver

PhonePC/2in1TabletTVWearable

addObserver(observer: CustomComponentLifecycleObserver): void

addObserver函数用于注册自定义组件生命周期监听器。当自定义组件的生命周期发生变化时，会触发监听器中相应的生命周期回调函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | [CustomComponentLifecycleObserver](ts-custom-component-new-lifecycle.md#customcomponentlifecycleobserver) | 是 | 监听自定义组件的监听器。 |

### removeObserver

PhonePC/2in1TabletTVWearable

removeObserver(observer: CustomComponentLifecycleObserver): void

removeObserver函数用于移除自定义组件生命周期监听器。解除注册后，即使自定义组件的生命周期状态发生变化，也不会触发监听器中相应的生命周期回调函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| observer | CustomComponentLifecycleObserver | 是 | 监听自定义组件的监听器。 |

## CustomComponentLifecycleObserver

PhonePC/2in1TabletTVWearable

用户注册自定义组件生命周期回调后，当该自定义组件的生命周期发生变化时，将触发监听器中相应的生命周期回调。

### aboutToAppear

PhonePC/2in1TabletTVWearable

aboutToAppear?(): void

aboutToAppear函数在创建自定义组件的新实例后，执行其build()函数之前执行。开发者可以在此阶段修改状态变量。其功能与[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)类似，但是在自定义组件状态机的约束下触发的。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

### onDidBuild

PhonePC/2in1TabletTVWearable

onDidBuild?(): void

onDidBuild函数在自定义组件的新实例构建完成后，执行其build()函数之后执行。开发者可以在此阶段实现一些不影响实际UI的功能，例如事件数据上报。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

### aboutToDisappear

PhonePC/2in1TabletTVWearable

aboutToDisappear?(): void

aboutToDisappear函数在自定义组件被销毁之前执行。不建议在aboutToDisappear函数中修改状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。其功能与[aboutToDisappear](ts-custom-component-lifecycle.md#abouttodisappear)类似，不同的是，CustomComponentLifecycleObserver中的aboutToDisappear函数受状态机约束，只有被监听的自定义组件状态向CustomComponentLifecycleState.DISAPPEARED转变前触发回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

### aboutToReuse

PhonePC/2in1TabletTVWearable

aboutToReuse?(params?: Record<string, Object | undefined | null>): void

当可复用的自定义组件从缓存中重新添加到节点树时调用aboutToReuse函数，以接收组件的构造参数。当params存在时，表示V1组件的复用回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Record<string, Object | undefined | null> | 否 | 当params存在时，表示V1组件的复用回调。 |

### aboutToRecycle

PhonePC/2in1TabletTVWearable

aboutToRecycle?(): void

当组件被回收后触发，先执行应用程序中定义的必要回收操作，完成回收后调用aboutToRecycle函数。随后该组件被冻结，以避免该组件处于回收池时进行UI更新。最后，aboutToRecycle函数会递归遍历所有子组件，对每个完成回收的组件调用aboutToRecycle函数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**示例：**

```
1. import { ComponentInit, ComponentDisappear, UIUtils, CustomComponentLifecycleObserver, CustomComponentLifecycle } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export class Message {
5. value: string | undefined;
6. constructor(value: string) {
7. this.value = value;
8. }
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State switch: boolean = true;

16. build() {
17. Column() {
18. Button('Hello')
19. .fontSize(30)
20. .fontWeight(FontWeight.Bold)
21. .onClick(() => {
22. this.switch = !this.switch;
23. })
24. if (this.switch) {
25. // 如果只有一个复用的组件，可以不用设置reuseId。
26. Child({ message: new Message('Child') })
27. .reuseId('Child')
28. }
29. }
30. .height('100%')
31. .width('100%')
32. }
33. }

35. @Reusable
36. @Component
37. struct Child {
38. @State message: Message = new Message('AboutToReuse');
39. @State label: string = 'HelloWorld';
40. @ComponentInit
41. myInit(): void {
42. registerObserver(UIUtils.getLifecycle(this));
43. }
44. @ComponentDisappear
45. myDisappear(): void {
46. unRegisterObserver(UIUtils.getLifecycle(this));
47. }
48. build() {
49. Column() {
50. Text(this.message.value)
51. .fontSize(30)
52. }
53. }
54. }

56. export class MyObserver implements CustomComponentLifecycleObserver {
57. // 重写CustomComponentLifecycleObserver中的生命周期事件。
58. aboutToAppear() {
59. hilog.info(0x0000, 'testTag', 'MyObserver aboutToAppear');
60. }
61. onDidBuild() {
62. hilog.info(0x0000, 'testTag', 'MyObserver onDidBuild');
63. }
64. aboutToReuse(params?: Record<string, Object | undefined | null>) {
65. // params存在时，为V1的复用；
66. hilog.info(0x0000, 'testTag', 'MyObserver aboutToReuse');
67. }
68. aboutToRecycle() {
69. hilog.info(0x0000, 'testTag', 'MyObserver aboutToRecycle');
70. }
71. aboutToDisappear() {
72. hilog.info(0x0000, 'testTag', 'MyObserver aboutToDisappear');
73. }
74. }

76. // 创建Observer对象
77. const observer = new MyObserver();

79. export function registerObserver(lifeCycle: CustomComponentLifecycle) {
80. // 向lifeCycle注册监听
81. lifeCycle.addObserver(observer);
82. }

84. export function unRegisterObserver(lifeCycle: CustomComponentLifecycle) {
85. // 向lifeCycle取消注册监听
86. lifeCycle.removeObserver(observer);
87. }
```

## CustomComponentLifecycleState

PhonePC/2in1TabletTVWearable

自定义组件当前的生命周期状态。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INIT | 0 | 初始化状态。 |
| APPEARED | 1 | 准备展开状态。 |
| BUILT | 2 | 已展开状态。 |
| RECYCLED | 3 | 回收状态。 |
| DISAPPEARED | 4 | 删除状态。 |

**示例：**

```
1. import { CustomComponentLifecycleState, ComponentBuilt } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. @ComponentBuilt
8. myBuilt() {
9. // CustomComponentLifecycleState.BUILT代表自定义组件为已展开状态
10. hilog.info(0x0000, 'testTag', 'Index Lifecycle is %{public}d', CustomComponentLifecycleState.BUILT);
11. }
12. build() {
13. Column() {
14. Text(`HelloWorld`)
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

## 生命周期使用示例

PhonePC/2in1TabletTVWearable

本示例展示了生命周期回调函数的部分使用场景：

1. 自定义组件Child的创建触发@ComponentInit、@ComponentAppear，Child执行build()后，触发@ComponentBuilt。
2. 更改this.switch为false，回收Child子组件触发@ComponentRecycle；更改this.switch为true，复用Child子组件触发@ComponentReuse。
3. 退出应用，在自定义组件Child销毁前，触发@ComponentDisappear。

```
1. import { ComponentInit, ComponentAppear, ComponentBuilt, ComponentDisappear, ComponentReuse, ComponentRecycle } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export class Message {
5. value: string | undefined;
6. constructor(value: string) {
7. this.value = value;
8. }
9. }
10. @Entry
11. @Component
12. struct Index {
13. @State switch: boolean = true;
14. build() {
15. Column() {
16. Button('Hello')
17. .fontSize(30)
18. .fontWeight(FontWeight.Bold)
19. .onClick(() => {
20. this.switch = !this.switch;
21. })
22. if (this.switch) {
23. // 如果只有一个复用的组件，可以不用设置reuseId。
24. Child({ message: new Message('Child') })
25. .reuseId('Child')
26. }
27. }
28. .height('100%')
29. .width('100%')
30. }
31. }

33. @Reusable
34. @Component
35. struct Child {
36. @State message: Message = new Message('Child');
37. @State label: string = 'HelloWorld';
38. @State switch: boolean = true;
39. @ComponentInit
40. myInit() {
41. // 自定义组件创建完毕后，触发myInit方法
42. hilog.info(0x0000, 'testTag', 'Child myInit');
43. }
44. @ComponentAppear
45. myAppear() {
46. this.label = 'myAppear'
47. hilog.info(0x0000, 'testTag', 'Child myAppear');
48. }
49. @ComponentBuilt
50. myBuilt() {
51. this.label = 'myBuilt'
52. hilog.info(0x0000, 'testTag', 'Child myBuilt');
53. }
54. @ComponentRecycle
55. myRecycle() {
56. this.label = 'myRecycle'
57. hilog.info(0x0000, 'testTag', 'Child myRecycle');
58. }
59. @ComponentDisappear
60. myDisappear() {
61. this.label = 'myDisappear'
62. hilog.info(0x0000, 'testTag', 'Child myDisappear');
63. }
64. @ComponentReuse
65. myReuse() {
66. this.label = 'myReuse'
67. hilog.info(0x0000, 'testTag', 'Child myReuse');
68. }
69. build() {
70. Column() {
71. Text(this.message.value)
72. .fontSize(30)
73. }
74. .borderWidth(1)
75. .height(100)
76. }
77. }
```
