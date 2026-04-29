---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-lifecycle
title: 自定义组件生命周期
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件生命周期
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e377094ccaadab73fdeaa287ce73d58949754016ea237f87ff75355ec40d9779
---

自定义组件生命周期，即用[@Component](arkts-create-custom-components.md#component)或[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件的生命周期，提供以下生命周期接口：

* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)：组件即将出现时回调该接口，具体时机为在创建自定义组件的新实例后，在执行其build函数之前执行。
* [onDidBuild](../harmonyos-references/ts-custom-component-lifecycle.md#ondidbuild12)：在组件首次渲染触发的build函数执行完成之后回调该接口，后续组件重新渲染将不回调该接口。开发者可以在这个阶段实现埋点数据上报等不影响实际UI的功能。
* [aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)：aboutToDisappear函数在自定义组件析构销毁之前执行。不允许在aboutToDisappear函数中改变状态变量，特别是[@Link变量](arkts-link.md)的修改可能会导致应用程序行为不稳定。

说明

页面生命周期及其相关内容参考[页面路由](arkts-routing.md#生命周期)。

自定义组件生命周期流程如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/2iwq94k_Qz23KHvyohDimw/zh-cn_image_0000002558764044.png?HW-CC-KV=V1&HW-CC-Date=20260429T052701Z&HW-CC-Expire=86400&HW-CC-Sign=E4D88A8D7A92265BF0AE4331D086F804A184FC9DA6B7B6C0F56CFC57B12FC86D)

根据上面的流程图，接下来从自定义组件的初始创建、重新渲染和删除来详细说明。

## 自定义组件的创建和渲染流程

1. 自定义组件的创建：自定义组件的实例由ArkUI框架创建。
2. 初始化自定义组件的成员变量：通过本地默认值或者构造方法传递参数来初始化自定义组件的成员变量，初始化顺序为成员变量的定义顺序。
3. 如果开发者定义了aboutToAppear，则执行build方法之前执行该方法。
4. 在首次渲染的时候，执行build方法渲染系统组件，如果子组件为自定义组件，则创建自定义组件的实例。在首次渲染的过程中，框架会记录状态变量和组件的映射关系，当状态变量改变时，驱动其相关的组件刷新。
5. 如果开发者定义了onDidBuild，则执行build方法之后执行该方法。

## 自定义组件重新渲染

当触发事件（比如点击）改变状态变量时，或者[LocalStorage](arkts-localstorage.md) / [AppStorage](arkts-appstorage.md)中的属性更改，并导致绑定的状态变量更改其值时：

1. 框架观察到变化，启动重新渲染。
2. 根据框架记录的状态变量和组件的映射关系，仅刷新发生变化的状态变量所关联的组件，实现最小化更新。

## 自定义组件的删除

例如if组件的分支改变或ForEach循环渲染中数组的个数改变，组件将被移除：

1. 在删除组件之前，将调用其aboutToDisappear生命周期函数，标记着该节点将要被销毁。ArkUI的节点删除机制是：后端节点直接从组件树上摘下，后端节点被销毁，对前端节点解引用，前端节点已经没有引用时，将被Ark虚拟机垃圾回收。
2. 自定义组件和它的变量将被删除，如果组件有同步的变量（如[@Link](arkts-link.md)、[@Prop](arkts-prop.md)、[@StorageLink](arkts-appstorage.md#storagelink)），将从[同步源](arkts-state-management-glossary.md#数据源同步源data-source)上取消注册。

不建议在生命周期aboutToDisappear中使用async await。如果在此生命周期中使用异步操作（如 Promise 或回调方法），自定义组件将被保留在Promise的闭包中，直到回调方法执行完毕，这会阻止自定义组件的垃圾回收。

## 自定义组件嵌套使用与示例

通过以下示例，来详细说明自定义组件在嵌套使用时，自定义组件生命周期的调用时序：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Parent {
6. @State showChild: boolean = true;
7. @State btnColor: string = '#FF007DFF';

9. // 组件生命周期
10. aboutToAppear() {
11. hilog.info(0x0000, 'testTag', 'Parent aboutToAppear');
12. }

14. // 组件生命周期
15. onDidBuild() {
16. hilog.info(0x0000, 'testTag', 'Parent onDidBuild');
17. }

19. // 组件生命周期
20. aboutToDisappear() {
21. hilog.info(0x0000, 'testTag', 'Parent aboutToDisappear');
22. }

24. build() {
25. Column() {
26. // this.showChild为true，创建Child子组件，执行Child aboutToAppear和Child onDidBuild。
27. if (this.showChild) {
28. Child()
29. }
30. Button(this.showChild ? 'delete Child' : 'add Child')
31. .margin(20)
32. .backgroundColor(this.btnColor)
33. .onClick(() => {
34. // 更改this.showChild为false，删除Child子组件，执行Child aboutToDisappear。
35. // 更改this.showChild为true，添加Child子组件，执行Child aboutToAppear和Child onDidBuild。
36. this.showChild = !this.showChild;
37. })
38. }
39. }
40. }

42. @Component
43. struct Child {
44. @State title: string = 'Hello World';

46. // 组件生命周期
47. aboutToDisappear() {
48. hilog.info(0x0000, 'testTag', 'Child aboutToDisappear');
49. }

51. // 组件生命周期
52. onDidBuild() {
53. hilog.info(0x0000, 'testTag', 'Child onDidBuild');
54. }

56. // 组件生命周期
57. aboutToAppear() {
58. hilog.info(0x0000, 'testTag', 'Child aboutToAppear');
59. }

61. build() {
62. Text(this.title)
63. .fontSize(50)
64. .margin(20)
65. .onClick(() => {
66. this.title = 'Hello ArkUI';
67. })
68. }
69. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomLifecycle/entry/src/main/ets/pages/parent/Index.ets#L16-L86)

以上示例中，Index页面包含两个自定义组件，一个是Parent，一个是Child，Parent及其子组件Child分别声明了各自的自定义组件生命周期函数（aboutToAppear / onDidBuild / aboutToDisappear）。

* 应用冷启动的初始化流程为：Parent aboutToAppear --> Parent build --> Parent onDidBuild --> Child aboutToAppear --> Child build --> Child onDidBuild。此处体现了自定义组件懒展开特性，即Parent执行完onDidBuild之后才会执行Child组件的aboutToAppear。日志输出信息如下：

```
1. Parent aboutToAppear
2. Parent onDidBuild
3. Child aboutToAppear
4. Child onDidBuild
```

* 点击Button按钮，更改showChild为false，删除Child组件，执行Child aboutToDisappear方法。
* 如果直接退出应用，则会触发以下生命周期：Parent aboutToDisappear --> Child aboutToDisappear，此处体现了自定义组件删除顺序也是从父到子。日志输出信息如下：

```
1. Parent aboutToDisappear
2. Child aboutToDisappear
```

* 最小化应用或者应用进入后台，当前Index页面未被销毁，所以并不会执行组件的aboutToDisappear。
* 如果showChild的默认值为false，则应用冷启动的初始化流程为：Parent aboutToAppear --> Parent build --> Parent onDidBuild。日志输出信息如下：

```
1. Parent aboutToAppear
2. Parent onDidBuild
```

* 如果showChild的默认值为false，直接退出应用，则只执行Parent aboutToDisappear方法。
* 如果showChild的默认值为false，此时点击Button按钮，更改showChild为true，添加Child组件，添加流程为：Child aboutToAppear --> Child build --> Child onDidBuild。日志输出信息如下：

```
1. Child aboutToAppear
2. Child onDidBuild
```

当showChild为默认值true时，该示例的生命周期流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/mYDQaGX2QkqJiakU_T7k2Q/zh-cn_image_0000002558604388.png?HW-CC-KV=V1&HW-CC-Date=20260429T052701Z&HW-CC-Expire=86400&HW-CC-Sign=567B6AA1E84A7567016D3F7514A904EB16E0E277414A756572A1B996F185B167)
