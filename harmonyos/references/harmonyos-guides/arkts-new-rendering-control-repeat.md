---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat
title: Repeat：可复用的循环渲染
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式渲染控制 > Repeat：可复用的循环渲染
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e330d8d67cb526f23feb351bd7d2e613b7d7b950b9e43ab233c5a31e15d91b2
---

说明

* Repeat从API version 12开始支持。
* 本文档仅为开发指南。组件接口规范见[Repeat API参数说明](../harmonyos-references/ts-rendering-control-repeat.md)。
* 由于不同设备屏幕宽高不同，本指南内的示例的实际效果和截图有偏差。

## 概述

Repeat基于数组类型数据来进行循环渲染，一般与滚动容器组件配合使用。

Repeat根据容器组件的**显示区域和预加载区域**加载子组件。当容器滑动/数组改变时，Repeat会根据父容器组件的布局过程重新计算显示区域和预加载区域范围，并管理列表子组件节点的创建与销毁。Repeat通过组件节点更新/复用从而优化性能表现，详细描述见[节点更新/复用能力说明](arkts-new-rendering-control-repeat.md#节点更新复用能力说明)。

本文档依次介绍了Repeat的[基础特性](arkts-new-rendering-control-repeat.md#基础特性)、[高级特性](arkts-new-rendering-control-repeat.md#高级特性)、[常见使用场景](arkts-new-rendering-control-repeat.md#常见使用场景)和[常见问题](arkts-new-rendering-control-repeat.md#常见问题)，开发者可以按需阅读。在[子组件生成规则](arkts-new-rendering-control-repeat.md#子组件生成规则)小节中，给出了简单的示例，可以帮助开发者快速上手Repeat的使用。

说明

Repeat与[LazyForEach](arkts-rendering-control-lazyforeach.md)组件的区别：

* Repeat直接监听状态变量的变化，而LazyForEach需要开发者实现[IDataSource](../harmonyos-references/ts-rendering-control-lazyforeach.md#idatasource)接口，手动管理子组件内容/索引的修改。
* Repeat还增强了节点复用能力，提高了长列表滑动和数据更新的渲染性能。
* Repeat增加了渲染模板（template）的能力，在同一个数组中，根据开发者自定义的模板类型（template type）渲染不同的子组件。

相较于LazyForEach，Repeat用法更加简单，渲染性能更好，建议开发者优先使用Repeat。

## 使用限制

* Repeat必须在滚动类容器组件内使用，仅有[List](../harmonyos-references/ts-container-list.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)以及[WaterFlow](../harmonyos-references/ts-container-waterflow.md)组件支持Repeat懒加载场景。

  循环渲染只允许创建一个子组件，子组件应当是允许包含在容器组件中的子组件。例如：Repeat与[List](../harmonyos-references/ts-container-list.md)组件配合使用时，子组件必须为[ListItem](../harmonyos-references/ts-container-listitem.md)组件。
* Repeat[懒加载模式](arkts-new-rendering-control-repeat.md#懒加载能力说明)不支持与[状态管理（V1）](arkts-state-management-overview.md#状态管理v1)配合使用，否则会导致渲染异常。
* Repeat当前不支持动画效果。
* 滚动容器组件内只能包含一个Repeat。以List为例，不建议同时包含ListItem、ForEach、LazyForEach，不建议同时包含多个Repeat。
* 当Repeat与自定义组件或[@Builder](arkts-builder.md)函数混用时，必须将RepeatItem类型整体进行传参，组件才能监听到数据变化。详见[与@Builder混用时状态变量未刷新](arkts-new-rendering-control-repeat.md#与builder混用时状态变量未刷新)。
* Repeat子组件复用时不会触发[aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)、[aboutToReuse](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoreuse10)生命周期。

说明

Repeat功能依赖数组属性的动态修改。如果数组对象被密封（sealed）或冻结（frozen），将导致Repeat部分功能失效，因为密封操作会禁止对象扩展属性并锁定现有属性的配置。

常见触发场景：

1）可观察数据的转换：使用[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)将普通数组（如[collections.Array](../harmonyos-references/arkts-apis-arkts-collections-array.md)）转换为可观察数据时，某些实现会自动密封数组。

2）主动对象保护：显式调用Object.seal()或Object.freeze()防止数组被修改。

## 基础特性

### 子组件生成规则

Repeat通过[.each()](../harmonyos-references/ts-rendering-control-repeat.md#each)和[.template()](../harmonyos-references/ts-rendering-control-repeat.md#template)属性定义子组件生成规则。每个子组件必须有且仅有一个根节点。当Repeat仅包含一种类型的子组件时，可使用.each()属性定义子组件的生成规则。当Repeat包含多种类型的子组件时，可使用.template()属性分别定义不同类型子组件的生成规则。

**单一类型子组件**

.each()适用于只需要循环渲染一种子组件的场景。下列示例代码使用Repeat组件进行简单的循环渲染。

```
1. // 在List容器组件中使用Repeat
2. @Entry
3. @ComponentV2
4. // 推荐使用V2装饰器
5. struct RepeatExample {
6. @Local dataArr: Array<string> = []; // 数据源

8. aboutToAppear(): void {
9. for (let i = 0; i < 50; i++) {
10. this.dataArr.push(`data_${i}`); // 为数组添加一些数据
11. }
12. }

14. build() {
15. Column() {
16. List() {
17. Repeat<string>(this.dataArr)
18. .each((ri: RepeatItem<string>) => {
19. ListItem() {
20. Text('each_' + ri.item).fontSize(30)
21. }
22. })
23. .virtualScroll({ totalCount: this.dataArr.length }) // 打开懒加载，totalCount为期望加载的数据长度
24. }
25. .cachedCount(2) // 容器组件的预加载区域大小
26. .height('70%')
27. .border({ width: 1 }) // 边框
28. }
29. }
30. }
```

[RepeatExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatExample.ets#L16-L46)

运行后界面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/6xf21IyFSbedkQqnrudOxw/zh-cn_image_0000002552798014.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=5CEFFA97A8F2DF4B623CB13DB03D6BFF1F7FE0DCCFFAB712EBAC04614E044B6C)

**多种类型子组件**

Repeat提供渲染模板（template）能力，可以在同一个数据源中渲染多种子组件。每个数据项会根据[.templateId()](../harmonyos-references/ts-rendering-control-repeat.md#templateid)得到template type，从而渲染type对应的.template()中的子组件。

说明

* .template()需要在[懒加载模式](arkts-new-rendering-control-repeat.md#懒加载能力说明)下使用。
* .each()等价于template type为空字符串的.template()。
* 当多个template type相同时（包括template type为空字符串），Repeat仅生效最新定义的.each()或.template()。
* 如果.templateId()缺省，或templateId()计算得到的template type不存在，则template type取默认值空字符串。
* 只有相同template type的节点可以互相复用。

下列示例代码中使用Repeat组件进行循环渲染，并使用了多个渲染模板。

```
1. // 在List容器组件中使用Repeat
2. @Entry
3. @ComponentV2 // 推荐使用V2装饰器
4. struct RepeatExampleWithTemplates {
5. @Local dataArr: Array<string> = []; // 数据源

7. aboutToAppear(): void {
8. for (let i = 0; i < 50; i++) {
9. this.dataArr.push(`data_${i}`); // 为数组添加一些数据
10. }
11. }

13. build() {
14. Column() {
15. List() {
16. Repeat<string>(this.dataArr)
17. .each((ri: RepeatItem<string>) => { // 默认渲染模板
18. ListItem() {
19. Text('each_' + ri.item).fontSize(30).fontColor('rgb(161,10,33)') // 文本颜色为红色
20. }
21. })
22. .key((item: string, index: number): string => JSON.stringify(item)) // 键值生成函数
23. .virtualScroll({ totalCount: this.dataArr.length }) // 打开懒加载，totalCount为期望加载的数据长度
24. .templateId((item: string, index: number): string => { // 根据返回值寻找对应的模板子组件进行渲染
25. return index <= 4 ? 'A' : (index <= 10 ? 'B' : ''); // 前5个节点模板为A，接下来的5个为B，其余为默认模板
26. })
27. .template('A', (ri: RepeatItem<string>) => { // 'A'模板
28. ListItem() {
29. Text('A_' + ri.item).fontSize(30).fontColor('rgb(23,169,141)') // 文本颜色为绿色
30. }
31. }, { cachedCount: 3 }) // 'A'模板的缓存列表容量为3
32. .template('B', (ri: RepeatItem<string>) => { // 'B'模板
33. ListItem() {
34. Text('B_' + ri.item).fontSize(30).fontColor('rgb(39,135,217)') // 文本颜色为蓝色
35. }
36. }, { cachedCount: 4 }) // 'B'模板的缓存列表容量为4
37. }
38. .cachedCount(2) // 容器组件的预加载区域大小
39. .height('70%')
40. .border({ width: 1 }) // 边框
41. }
42. }
43. }
```

[RepeatExample2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatExample2.ets#L16-L60)

运行后界面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/t2_fer1GQ2CtLZm5Hs620A/zh-cn_image_0000002583437709.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=193BE11AD5FE228E1F91459FAAB6D5E3CD926C22A9E1EEF2005BF5472BECC880)

### 键值生成规则

Repeat的[.key()](../harmonyos-references/ts-rendering-control-repeat.md#key)属性为每个子组件生成一个键值。Repeat通过键值识别数组增加、删除哪些数据以及哪些数据改变了位置（索引）。

当.key()缺省时，Repeat会生成新的随机键值。当发现有重复key时，Repeat会在已有键值的基础上递归生成新的键值，直到没有重复键值。

说明

* 键值（key）与索引（index）的区别：键值是数据项的唯一标识符，Repeat根据键值是否发生变化判断数据项是否更新；索引只标识数据项在数组中的位置。
* 在[懒加载模式](arkts-new-rendering-control-repeat.md#懒加载能力说明)下，Repeat也会通过状态管理机制监听数据本身的变化，从而实现高效的更新。

键值生成函数.key()的使用限制：

* 即使数组发生变化，开发者也必须保证键值key唯一。
* 每次执行.key()函数时，使用相同的数据项作为输入，输出必须是一致的。
* 允许在.key()中使用index，但不建议开发者这样做。因为在数据项移动时索引index发生变化的同时key值也会改变，导致Repeat认为数据发生变化，从而触发子组件重新渲染，降低性能表现。
* 推荐将简单类型数组转换为类对象数组，并添加一个readonly id属性，在构造函数中初始化唯一值。

键值生成示例：

```
1. @ObservedV2
2. class ExampleData {
3. @Trace str: string;
4. num: number;

6. constructor(s: string, n: number) {
7. this.str = s;
8. this.num = n;
9. }
10. }

12. @Entry
13. @ComponentV2
14. struct Index {
15. @Local exampleList: Array<ExampleData> = [];

17. aboutToAppear(): void {
18. for (let i = 0; i < 20; i++) {
19. this.exampleList.push(new ExampleData(`data${i}`, i));
20. }
21. }

23. build() {
24. Column() {
25. List({ space: 10 }) {
26. Repeat(this.exampleList)
27. .each((obj: RepeatItem<ExampleData>) => {
28. ListItem() {
29. Text(obj.item.str).fontSize(50)
30. }
31. })
32. .key(item => item.str) // UI显示刷新与属性str相关，建议在键值生成函数中设置其为返回值，此处键值生成与index无关
33. }
34. }
35. }
36. }
```

在上述示例代码中，使用.key()定义键值生成函数，各子组件的键值为item元素的str属性值。

### 懒加载能力说明

Repeat加载子节点具有懒加载和全量加载两种模式。开发者可通过设置[.virtualScroll()](../harmonyos-references/ts-rendering-control-repeat.md#virtualscroll)属性选择合适的加载模式。对于长列表场景，懒加载模式支持按需加载子组件，建议开发者优先使用懒加载模式。

**懒加载模式**

使用Repeat的.virtualScroll()属性，即可使能懒加载能力。在懒加载模式下，Repeat根据当前的容器组件显示区域和预加载区域范围，按需加载子组件。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/wOqnjztpSsyIhD5snLLIng/zh-cn_image_0000002552957664.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=2C49220A1743D85DEC44973DFD0519EE57CA0BA8C7BDC769127F96B9E55D9B32)

说明

* 懒加载模式需要和滚动容器组件[List](../harmonyos-references/ts-container-list.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)或[WaterFlow](../harmonyos-references/ts-container-waterflow.md)配合使用。
* 懒加载模式需要和[状态管理（V2）](arkts-state-management-overview.md#状态管理v2)配合使用。
* 键值变化或数据变化均会触发页面刷新。

**全量加载模式**

当关闭Repeat的.virtualScroll()属性时（即省略该属性），Repeat在初始化页面时加载列表中的所有子组件，适合**短数据列表/组件全部加载**的场景。对于**长数据列表（数据长度大于30）**，如果关闭懒加载，Repeat会一次性加载全量子组件，此操作耗时长，不建议使用。

说明

* 渲染模板特性（template）不可用。
* 不受滚动容器组件的限制，可以在任意场景使用。
* 支持与[状态管理（V1）](arkts-state-management-overview.md#状态管理v1)配合使用。
* 页面刷新取决于键值变化：如果更新前后键值相同，即使数据改变，页面也不会刷新。

### 节点更新/复用能力说明

Repeat具有节点复用能力。Repeat子组件从组件树中移除时，会被存入缓存池中。后续创建新子组件时，会优先复用池中的节点。懒加载模式和全量加载模式下的复用流程细节存在差异，下文中将分别进行说明。

Repeat组件默认开启节点复用功能。从API version 18开始，在懒加载模式下，可以通过配置reusable字段选择是否启用复用功能。为了提高渲染性能，建议开发者保持节点复用。代码示例见[VirtualScrollOptions](../harmonyos-references/ts-rendering-control-repeat.md#virtualscrolloptions)。

从API version 18开始，Repeat支持懒加载模式下[缓存池自定义组件冻结](arkts-custom-components-freezev2.md#repeat)。

说明

Repeat子组件的节点操作分为四种：节点创建、节点更新、节点复用、节点销毁。其中，节点更新和节点复用的区别为：

* 节点更新：节点不销毁，状态变量驱动节点属性更新。
* 节点复用：旧节点不销毁，存储在空闲节点缓存池；需要创建新节点时，直接从缓存池中获取可复用的旧节点，并做相应的节点属性更新。

Repeat节点复用时，不会触发子组件的[aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)和[aboutToReuse](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoreuse10)生命周期。

**懒加载模式下的节点更新/复用**

在懒加载模式下，当**滚动容器组件滑动/数组改变**时，Repeat将失效的子组件节点（离开容器组件的显示区域和预加载区域）加入空闲节点缓存池中，即断开组件节点与页面组件树的连接但不销毁节点。在需要生成新的组件时，对缓存池里的组件节点进行复用。

下面通过**首次渲染**后典型的**滑动场景**和**数据更新场景**示例来展示Repeat子组件的渲染逻辑。

1. 首次渲染。

   定义长度为20的数组，数组前5项的template type为aa，渲染浅蓝色组件，其余项为bb，渲染橙色组件。aa缓存池容量为3，bb缓存池容量为4。容器组件的预加载区域大小为2。为了便于理解，在aa和bb缓存池中分别加入一个和两个空闲节点。

   首次渲染时列表的节点状态如下图所示（template type在图中简写为ttype）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/fyMeV1NEQly1IwNkUkhOAQ/zh-cn_image_0000002583477665.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=7530E2D7C33C7D34C1B1D50209FFB3A2BC2112405276C275E860F5ED8DC455BC)
2. 滑动场景。

   将列表向下滑动一个节点的距离，Repeat会复用缓存池中的节点。

   1）index=10的节点进入预加载区域，计算出其template type为bb。由于bb缓存池非空，Repeat会从bb缓存池中取出一个空闲节点进行复用，更新其节点属性（数据item和索引index），该子组件中涉及数据item和索引index的其他孙子组件会根据[状态管理（V2）](arkts-state-management-overview.md#状态管理v2)的规则做同步更新。

   2）index=0的节点滑出了预加载区域。当UI主线程空闲时，会检查aa缓存池是否已满，此时aa缓存池未满，将该节点加入到对应的缓存池中。

   3）其余节点仍在容器显示区域和预加载区域范围，均只更新索引index。如果对应template type的缓存池已满，Repeat会在UI主线程空闲时销毁掉多余的节点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/9sL9sPEETgCp3OzLfpZRVQ/zh-cn_image_0000002552798016.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=217330F6338326DD32C63CA7C44AB6ADB78A3E9EA004F40D48E9C6D4713150E0)
3. 数据更新场景。

   在上一小节的基础上做如下的数组更新操作，删除index=4的节点，修改节点数据07为new。

   1）删除index=4的节点后，节点05前移。根据template type的计算规则，新的05节点的template type变为aa，直接复用旧的04节点，更新数据item和索引index，并且将旧的05节点加入bb缓存池。

   2）后面的列表节点前移，新进入预加载区域的节点11会复用bb缓存池中的空闲节点，其他节点均只更新索引index。

   3）对于节点数据从07变为new的情况，页面监听到数据源变化将会触发重新渲染。Repeat数据更新触发重新渲染的逻辑是比较当前索引处节点数据item是否变化，以此判断是否进行UI刷新，仅改变键值不改变item的情况不会触发刷新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/0WHMRVmTRfSVSWsFEjuIgg/zh-cn_image_0000002583437711.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=939FCD4CC296F462C09003E5A3F4F6F4628698A3A17373B4F332EC3483E61771)

**全量加载模式下的节点更新/复用**

在全量加载模式下，页面首次渲染时，Repeat子组件全部创建。数组发生改变后，Repeat对子组件节点的处理分为以下几个步骤：

首先，遍历旧数组键值。如果新数组中没有该键值，将其加入键值集合deletedKeys。

其次，遍历新数组键值。依次判断以下条件，进行符合条件的操作：

1. 若在旧数组中能找到相同键值，直接使用对应的子组件节点，并更新索引index。
2. 若deletedKeys非空，按照先进后出的顺序，更新该集合中的键值所对应的节点。
3. 若deletedKeys为空，则表示没有可以更新的节点，需要创建新节点。

最后，如果新数组键值遍历结束后，deletedKeys非空，则销毁集合中的键值所对应的节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/y95n-bcEQDuemQHMakM2wA/zh-cn_image_0000002552957666.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=8B051566A7D1DC5017B58F76E357E979E6932F3A6C09D29950F0150954D6BFCC)

以下图中的数组变化为例，图中的item\_X表示数据项的键值key。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/v2wHo8nORXerNGEsH4BvoQ/zh-cn_image_0000002583477667.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=5793026E9F914C35DF72F183B562F59AFD4AF0058926880662D3E9EE22907A50)

根据上述判断逻辑：item\_0没有变化，item\_1和item\_2只更新了索引，item\_n1和item\_n2分别由item\_4和item\_3进行节点更新获得，item\_n3为新创建的节点。

说明

Repeat全量加载模式与[ForEach](arkts-rendering-control-foreach.md)组件的区别：

* 针对特定数组更新场景的渲染性能进行了优化。
* 将子组件的内容/索引管理职责转移至框架层面。

**示例：**

以下示例演示了全量加载模式下的节点更新。

```
1. @Entry
2. @ComponentV2
3. struct NodeUpdateMechanism {
4. @Local simpleList: Array<string> = ['one', 'two', 'three'];

6. build() {
7. Row() {
8. Column() {
9. Text('Click to change the value of the third array item')
10. .fontSize(24)
11. .fontColor(Color.Red)
12. .onClick(() => {
13. this.simpleList[2] = 'new three';
14. })

16. Repeat<string>(this.simpleList)
17. .each((obj: RepeatItem<string>)=>{
18. ChildItem({ item: obj.item })
19. .margin({top: 20})
20. })
21. .key((item: string) => item)
22. }
23. .justifyContent(FlexAlign.Center)
24. .width('100%')
25. .height('100%')
26. }
27. .height('100%')
28. .backgroundColor(0xF1F3F5)
29. }
30. }

32. @ComponentV2
33. struct ChildItem {
34. @Param @Require item: string;

36. build() {
37. Text(this.item)
38. .fontSize(30)
39. }
40. }
```

[NodeUpdateMechanism.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/NodeUpdateMechanism.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/y4Vv60GOTHG-VcGjnSouoA/zh-cn_image_0000002583437691.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=CA08902A875FF908D704CCB51238FB6049E1CFB887E26191FE19E2EA9E8EDAD6)

点击红色字体，第三个数据项发生变化（直接使用旧的组件节点，仅刷新数据）。

**节点复用情况查看**

查看节点是否为复用可以使用[DevEco Testing](deveco-testing.md)工具进行查看，进入DevEco Testing工具后，选择实用工具，界面如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/iV-S8t-5S2eYHRzMgbSAfA/zh-cn_image_0000002552798018.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=CFCD97A905D583F4F39472775044C77D6F4630491AE2AC2452F04A890596ADE3)

在实用工具中选择UIViewer，该工具可以获取设备快照、控件树信息及控件节点属性，在右侧的控件树中选择Repeat子节点，右下方的节点属性会显示节点ID等信息，可以通过节点ID是否相同，判断组件复用或者新建的情况。

## 高级特性

除循环渲染、懒加载、组件复用等能力外，Repeat还提供了数据精准懒加载、拖拽排序、数据前插保持等高级特性，开发者可按需使用。

### 数据精准懒加载

当数据源总长度较长，或数据项加载耗时较长时，可使用Repeat数据精准懒加载特性，避免在初始化时加载所有数据。Repeat数据精准懒加载特性从API version 19开始支持。

开发者可以设置.virtualScroll()的totalCount属性值或onTotalCount自定义方法用于计算期望加载的数据项总数，设置onLazyLoading属性实现数据精准懒加载，实现在节点首次渲染时加载对应的数据。详细说明和注意事项见[VirtualScrollOptions](../harmonyos-references/ts-rendering-control-repeat.md#virtualscrolloptions)。

**示例1**

数据源总长度较长，在首次渲染、滑动屏幕、跳转显示区域时，动态加载对应区域内的数据。

```
1. @Entry
2. @ComponentV2
3. struct RepeatLazyLoadingLongData {
4. // 假设数据源总长度较长，为1000。初始数组未提供数据。
5. @Local arr: Array<string> = [];
6. scroller: Scroller = new Scroller();

8. build() {
9. Column({ space: 5 }) {
10. // 初始显示位置为index = 100，数据可通过懒加载自动获取。
11. List({ scroller: this.scroller, space: 5, initialIndex: 100 }) {
12. Repeat(this.arr)
13. .virtualScroll({
14. // 期望的数据源总长度为1000。
15. onTotalCount: () => {
16. return 1000;
17. },
18. // 实现数据懒加载。
19. onLazyLoading: (index: number) => {
20. this.arr[index] = index.toString();
21. }
22. })
23. .each((obj: RepeatItem<string>) => {
24. ListItem() {
25. Row({ space: 5 }) {
26. Text(`${obj.index}: Item_${obj.item}`)
27. }
28. }
29. .height(50)
30. })
31. }
32. .height('80%')
33. .border({ width: 1 })

35. // 显示位置跳转至index = 500，数据可通过懒加载自动获取。
36. Button('ScrollToIndex 500')
37. .onClick(() => {
38. this.scroller.scrollToIndex(500);
39. })
40. }
41. }
42. }
```

[RepeatLazyLoading1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatLazyLoading1.ets#L16-L51)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/eW6oFnkmQ3OtGdEnpGqfLA/zh-cn_image_0000002583437713.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=875891CAF54E68D576FC74871099DADD35437CBEEC191F69E55414C0276033AF)

**示例2**

数据加载耗时长，在onLazyLoading方法中，首先为数据项创建占位符，再通过异步任务加载数据。

```
1. @Entry
2. @ComponentV2
3. struct RepeatLazyLoadingSync {
4. @Local arr: Array<string> = [];

6. build() {
7. Column({ space: 5 }) {
8. List({ space: 5 }) {
9. Repeat(this.arr)
10. .virtualScroll({
11. onTotalCount: () => {
12. return 100;
13. },
14. // 实现数据懒加载。
15. onLazyLoading: (index: number) => {
16. // 创建占位符。
17. this.arr[index] = '';
18. // 模拟高耗时加载过程，通过异步任务加载数据。
19. setTimeout(() => {
20. this.arr[index] = index.toString();
21. }, 1000);
22. }
23. })
24. .each((obj: RepeatItem<string>) => {
25. ListItem() {
26. Row({ space: 5 }) {
27. Text(`${obj.index}: Item_${obj.item}`)
28. }
29. }
30. .height(50)
31. })
32. }
33. .height('100%')
34. .border({ width: 1 })
35. }
36. }
37. }
```

[RepeatLazyLoading2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatLazyLoading2.ets#L16-L49)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4SpZyplvRVK2wp7z7s9-Hg/zh-cn_image_0000002552957668.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=037EF1AA0F6496E7D5B044BDD692BBBDD5BF1BD65B4FDAF8225B063AB76DBA0D)

**示例3**

使用数据懒加载，并配合设置onTotalCount: () => { return this.arr.length + 1; }，可实现数据无限懒加载。

说明

* 此场景下，开发者需要提供首屏显示所需的初始数据，并建议设置父容器组件cachedCount > 0，否则将会导致渲染异常。
* 若与Swiper-Loop模式同时使用，停留在index = 0处时，将导致onLazyLoading方法被持续触发，建议避免与Swiper-Loop模式同时使用。
* 开发者需要关注内存消耗情况，避免因数据持续加载而导致内存过量消耗。

```
1. @Entry
2. @ComponentV2
3. struct RepeatLazyLoadingInfinite {
4. @Local arr: Array<string> = [];

6. // 提供首屏显示所需的初始数据。
7. aboutToAppear(): void {
8. for (let i = 0; i < 15; i++) {
9. this.arr.push(i.toString());
10. }
11. }

13. build() {
14. Column({ space: 5 }) {
15. List({ space: 5 }) {
16. Repeat(this.arr)
17. .virtualScroll({
18. // 数据无限懒加载。
19. onTotalCount: () => {
20. return this.arr.length + 1;
21. },
22. onLazyLoading: (index: number) => {
23. this.arr[index] = index.toString();
24. }
25. })
26. .each((obj: RepeatItem<string>) => {
27. ListItem() {
28. Row({ space: 5 }) {
29. Text(`${obj.index}: Item_${obj.item}`)
30. }
31. }
32. .height(50)
33. })
34. }
35. .height('100%')
36. .border({ width: 1 })
37. // 建议设置cachedCount > 0。
38. .cachedCount(1)
39. }
40. }
41. }
```

[RepeatLazyLoading3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatLazyLoading3.ets#L16-L52)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/PbcYtL3-RxqsfGK2Tqw1AA/zh-cn_image_0000002583477669.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=E5D4B12C6CF35FBAEA18E23E592B870B61D99CFA2AB8BF68BFB44D30B1371667)

### 拖拽排序

当Repeat在[List](../harmonyos-references/ts-container-list.md)组件下使用，并且设置了[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)事件，Repeat每次迭代都生成一个[ListItem](../harmonyos-references/ts-container-listitem.md)时，可以使能拖拽排序。Repeat拖拽排序特性从API version 19开始支持。

说明

* 拖拽排序离手后，如果数据位置发生变化，则会触发onMove事件，上报数据移动原始索引号和目标索引号。

  在onMove事件中，需要根据上报的起始索引号和目标索引号修改数据源。数据源修改前后，要保持每个数据的键值不变，只是顺序发生变化，才能保证落位动画正常执行。
* 拖拽排序过程中，在离手之前，不允许修改数据源。

示例代码：

```
1. @Entry
2. @ComponentV2
3. struct RepeatVirtualScrollOnMove {
4. @Local simpleList: Array<string> = [];

6. aboutToAppear(): void {
7. for (let i = 0; i < 100; i++) {
8. this.simpleList.push(`${i}`);
9. }
10. }

12. build() {
13. Column() {
14. List() {
15. Repeat<string>(this.simpleList)
16. // 通过设置onMove，使能拖拽排序。
17. .onMove((from: number, to: number) => {
18. let temp = this.simpleList.splice(from, 1);
19. this.simpleList.splice(to, 0, temp[0]);
20. })
21. .each((obj: RepeatItem<string>) => {
22. ListItem() {
23. Text(obj.item)
24. .fontSize(16)
25. .textAlign(TextAlign.Center)
26. .size({ height: 100, width: '100%' })
27. }.margin(10)
28. .borderRadius(10)
29. .backgroundColor('#FFFFFFFF')
30. })
31. .key((item: string, index: number) => {
32. return item;
33. })
34. .virtualScroll({ totalCount: this.simpleList.length })
35. }
36. .border({ width: 1 })
37. .backgroundColor('#FFDCDCDC')
38. .width('100%')
39. .height('100%')
40. }
41. }
42. }
```

[RepeatVirtualScrollOnMove.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatVirtualScrollOnMove.ets#L16-L59)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/k5lyvN6XTKqeSsZbgKGPeg/zh-cn_image_0000002552798020.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=560AEA5957072CD97AE71D96216F6F3F4A6F10F4131A363464F1CA3F57FCEC63)

### 数据前插保持

数据前插保持，即在列表显示区域之前插入或删除数据后，保持显示区域子组件的滚动位置不变。

从API version 20开始，仅当父容器组件为[List](../harmonyos-references/ts-container-list.md)且[maintainVisibleContentPosition](../harmonyos-references/ts-container-list.md#maintainvisiblecontentposition12)属性设置为true后，在List显示区域之前插入或删除数据时保持List显示区域子组件位置不变。

**示例代码**

```
1. @Entry
2. @ComponentV2
3. struct PreInsertDemo {
4. @Local simpleList: Array<string> = [];
5. private cnt: number = 1;

7. aboutToAppear(): void {
8. for (let i = 0; i < 30; i++) {
9. this.simpleList.push(`Hello ${this.cnt++}`);
10. }
11. }

13. build() {
14. Column() {
15. Row() {
16. Button(`insert #5`)
17. .onClick(() => {
18. this.simpleList.splice(5, 0, `Hello ${this.cnt++}`);
19. })
20. Button(`delete #0`)
21. .onClick(() => {
22. this.simpleList.splice(0, 1);
23. })
24. }

26. List({ initialIndex: 5 }) {
27. Repeat<string>(this.simpleList)
28. .each((obj: RepeatItem<string>) => {
29. ListItem() {
30. Row() {
31. Text(`index: ${obj.index}  `)
32. .fontSize(16)
33. .fontColor('#70707070')
34. .textAlign(TextAlign.End)
35. .size({ height: 100, width: '40%' })
36. Text(`item: ${obj.item}`)
37. .fontSize(16)
38. .textAlign(TextAlign.Start)
39. .size({ height: 100, width: '60%' })
40. }
41. }.margin(10)
42. .borderRadius(10)
43. .backgroundColor('#FFFFFFFF')
44. })
45. .key((item: string, index: number) => item)
46. .virtualScroll({ totalCount: this.simpleList.length })
47. }
48. .maintainVisibleContentPosition(true) // 启用前插保持
49. .border({ width: 1 })
50. .backgroundColor('#FFDCDCDC')
51. .width('100%')
52. .height('100%')
53. }
54. }
55. }
```

[PreInsert.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/PreInsert.ets#L16-L72)

示例中，通过点击按钮在显示区域上方插入或删除数据时，显示区域的节点仅index发生改变，对应数据项不变。

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/CVYq1xy1To2s0SXaslVrXg/zh-cn_image_0000002583437715.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=821404FBA3FF38C53DD3CB91858987C5804D92AE391AC5C07B676456FE891C0A)

## 常见使用场景

### 数据展示&操作

下面的代码示例展示了Repeat修改数组的常见操作，包括**插入数据、修改数据、删除数据、交换数据**。点击下拉框选择索引index值，点击相应的按钮即可操作数据项，依次点击两个不同的数据项可以进行交换。

```
1. @ObservedV2
2. class Repeat006Clazz {
3. @Trace public message: string = '';

5. constructor(message: string) {
6. this.message = message;
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct RepeatVirtualScroll {
13. @Local simpleList: Array<Repeat006Clazz> = [];
14. private exchange: number[] = [];
15. private counter: number = 0;
16. @Local selectOptions: SelectOption[] = [];
17. @Local selectIdx: number = 0;

19. @Monitor('simpleList')
20. reloadSelectOptions(): void {
21. this.selectOptions = [];
22. for (let i = 0; i < this.simpleList.length; ++i) {
23. this.selectOptions.push({ value: i.toString() });
24. }
25. if (this.selectIdx >= this.simpleList.length) {
26. this.selectIdx = this.simpleList.length - 1;
27. }
28. }

30. aboutToAppear(): void {
31. for (let i = 0; i < 100; i++) {
32. this.simpleList.push(new Repeat006Clazz(`item_${i}`));
33. }
34. this.reloadSelectOptions();
35. }

37. handleExchange(idx: number): void { // 点击交换子组件
38. this.exchange.push(idx);
39. if (this.exchange.length === 2) {
40. let _a = this.exchange[0];
41. let _b = this.exchange[1];
42. let temp: Repeat006Clazz = this.simpleList[_a];
43. this.simpleList[_a] = this.simpleList[_b];
44. this.simpleList[_b] = temp;
45. this.exchange = [];
46. }
47. }

49. build() {
50. Column({ space: 10 }) {
51. Text('virtualScroll each()&template() 2t')
52. .fontSize(15)
53. .fontColor(Color.Gray)
54. Text('Select an index and press the button to update data.')
55. .fontSize(15)
56. .fontColor(Color.Gray)

58. Select(this.selectOptions)
59. .selected(this.selectIdx)
60. .value(this.selectIdx.toString())
61. .key('selectIdx')
62. .onSelect((index: number) => {
63. this.selectIdx = index;
64. })
65. Row({ space: 5 }) {
66. Button('Add No.' + this.selectIdx)
67. .onClick(() => {
68. this.simpleList.splice(this.selectIdx, 0, new Repeat006Clazz(`${this.counter++}_add_item`));
69. this.reloadSelectOptions();
70. })
71. Button('Modify No.' + this.selectIdx)
72. .onClick(() => {
73. this.simpleList.splice(this.selectIdx, 1, new Repeat006Clazz(`${this.counter++}_modify_item`));
74. })
75. Button('Del No.' + this.selectIdx)
76. .onClick(() => {
77. this.simpleList.splice(this.selectIdx, 1);
78. this.reloadSelectOptions();
79. })
80. }
81. Button('Update array length to 5')
82. .onClick(() => {
83. this.simpleList = this.simpleList.slice(0, 5);
84. this.reloadSelectOptions();
85. })

87. Text('Click on two items to exchange')
88. .fontSize(15)
89. .fontColor(Color.Gray)

91. List({ space: 10 }) {
92. Repeat<Repeat006Clazz>(this.simpleList)
93. .each((obj: RepeatItem<Repeat006Clazz>) => {
94. ListItem() {
95. Text(`[each] index${obj.index}: ${obj.item.message}`)
96. .fontSize(25)
97. .onClick(() => {
98. this.handleExchange(obj.index);
99. })
100. }
101. })
102. .key((item: Repeat006Clazz, index: number) => {
103. return item.message;
104. })
105. .virtualScroll({ totalCount: this.simpleList.length })
106. .templateId((item: Repeat006Clazz, index: number) => {
107. return (index % 2 === 0) ? 'odd' : 'even';
108. })
109. .template('odd', (ri) => {
110. Text(`[odd] index${ri.index}: ${ri.item.message}`)
111. .fontSize(25)
112. .fontColor(Color.Blue)
113. .onClick(() => {
114. this.handleExchange(ri.index);
115. })
116. }, { cachedCount: 3 })
117. .template('even', (ri) => {
118. Text(`[even] index${ri.index}: ${ri.item.message}`)
119. .fontSize(25)
120. .fontColor(Color.Green)
121. .onClick(() => {
122. this.handleExchange(ri.index);
123. })
124. }, { cachedCount: 1 })
125. }
126. .cachedCount(2)
127. .border({ width: 1 })
128. .width('95%')
129. .height('40%')
130. }
131. .justifyContent(FlexAlign.Center)
132. .width('100%')
133. .height('100%')
134. }
135. }
```

[RepeatVirtualScroll2T.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatVirtualScroll2T.ets#L16-L152)

该示例代码展示了100项自定义类RepeatClazz的message字符串属性，[List](../harmonyos-references/ts-container-list.md)组件的[cachedCount](../harmonyos-references/ts-container-list.md#cachedcount)属性设为2，模板'odd'和'even'的空闲节点缓存池大小分别设为3和1。运行后界面如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/aNxizZ6vQLekJ2CcXjzkcw/zh-cn_image_0000002552957670.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=8609957724604E3A4D2AFE4A93DBD88385B270B1AA64210AD04B0FFADD6D69EF)

### Repeat嵌套

Repeat支持嵌套使用，示例代码如下：

```
1. // Repeat嵌套
2. @Entry
3. @ComponentV2
4. struct NestedRepeat {
5. @Local outerList: string[] = [];
6. @Local innerList: number[] = [];

8. aboutToAppear(): void {
9. for (let i = 0; i < 20; i++) {
10. this.outerList.push(i.toString());
11. this.innerList.push(i);
12. }
13. }

15. build() {
16. Column({ space: 20 }) {
17. Text('Nested Repeat with virtualScroll')
18. .fontSize(15)
19. .fontColor(Color.Gray)
20. List() {
21. Repeat<string>(this.outerList)
22. .each((obj) => {
23. ListItem() {
24. Column() {
25. Text('outerList item: ' + obj.item)
26. .fontSize(30)
27. List() {
28. Repeat<number>(this.innerList)
29. .each((subObj) => {
30. ListItem() {
31. Text('innerList item: ' + subObj.item)
32. .fontSize(20)
33. }
34. })
35. .key((item) => 'innerList_' + item)
36. .virtualScroll()
37. }
38. .width('80%')
39. .border({ width: 1 })
40. .backgroundColor(Color.Orange)
41. }
42. .height('30%')
43. .backgroundColor(Color.Pink)
44. }
45. .border({ width: 1 })
46. })
47. .key((item) => 'outerList_' + item)
48. .virtualScroll()
49. }
50. .width('80%')
51. .border({ width: 1 })
52. }
53. .justifyContent(FlexAlign.Center)
54. .width('90%')
55. .height('80%')
56. }
57. }
```

[NestedRepeat.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/NestedRepeat.ets#L16-L74)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/JmUyT_pmT0meJ0fS7uTJgg/zh-cn_image_0000002583477671.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=79171643617567C250C1A0E9FD80C01638DCA191C87F2C18AE3105AB5B64C45C)

### 父容器组件应用场景

本节展示Repeat与滚动容器组件的常见应用场景。

**与List组合使用**

在[List](../harmonyos-references/ts-container-list.md)容器组件中使用Repeat，示例代码如下：

```
1. class DemoListItemInfo {
2. public name: string;
3. public icon: Resource;

5. constructor(name: string, icon: Resource) {
6. this.name = name;
7. this.icon = icon;
8. }
9. }

11. @Entry
12. @ComponentV2
13. struct DemoList {
14. @Local videoList: Array<DemoListItemInfo> = [];

16. aboutToAppear(): void {
17. for (let i = 0; i < 10; i++) {
18. // 此处app.media.listItem0、app.media.listItem1、app.media.listItem2仅作示例，请开发者自行替换
19. this.videoList.push(new DemoListItemInfo('Video' + i,
20. i % 3 == 0 ? $r('app.media.listItem0') :
21. i % 3 == 1 ? $r('app.media.listItem1') : $r('app.media.listItem2')));
22. }
23. }

25. @Builder
26. itemEnd(index: number) {
27. Button('Delete')
28. .backgroundColor(Color.Red)
29. .onClick(() => {
30. this.videoList.splice(index, 1);
31. })
32. }

34. build() {
35. Column({ space: 10 }) {
36. Text('List Contains the Repeat Component')
37. .fontSize(15)
38. .fontColor(Color.Gray)

40. List({ space: 5 }) {
41. Repeat<DemoListItemInfo>(this.videoList)
42. .each((obj: RepeatItem<DemoListItemInfo>) => {
43. ListItem() {
44. Column() {
45. Image(obj.item.icon)
46. .width('80%')
47. .margin(10)
48. Text(obj.item.name)
49. .fontSize(20)
50. }
51. }
52. .swipeAction({
53. end: {
54. builder: () => {
55. this.itemEnd(obj.index);
56. }
57. }
58. })
59. .onAppear(() => {
60. })
61. })
62. .key((item: DemoListItemInfo) => item.name)
63. .virtualScroll()
64. }
65. .cachedCount(2)
66. .height('90%')
67. .border({ width: 1 })
68. .listDirection(Axis.Vertical)
69. .alignListItem(ListItemAlign.Center)
70. .divider({
71. strokeWidth: 1,
72. startMargin: 60,
73. endMargin: 60,
74. color: '#ffe9f0f0'
75. })

77. Row({ space: 10 }) {
78. Button('Delete No.1')
79. .onClick(() => {
80. this.videoList.splice(0, 1);
81. })
82. Button('Delete No.5')
83. .onClick(() => {
84. this.videoList.splice(4, 1);
85. })
86. }
87. }
88. .width('100%')
89. .height('100%')
90. .justifyContent(FlexAlign.Center)
91. }
92. }
```

[DemoList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/DemoList.ets#L16-L109)

右滑并点击按钮，或点击底部按钮，可删除视频卡片：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/8qyltyOVRmWij5KtBqqFNg/zh-cn_image_0000002552798022.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=67D840A347F3ADD9DEA8ED4B4F591C428ABF425FF3A09E37328696FE3FC151CD)

**与Grid组合使用**

在[Grid](../harmonyos-references/ts-container-grid.md)容器组件中使用Repeat，示例如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const TAG = '[Sample_RenderingControl]';
3. const DOMAIN = 0xF811;

5. class DemoGridItemInfo {
6. public name: string;
7. public icon: Resource;

9. constructor(name: string, icon: Resource) {
10. this.name = name;
11. this.icon = icon;
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct DemoGrid {
18. @Local itemList: Array<DemoGridItemInfo> = [];
19. @Local isRefreshing: boolean = false;
20. private layoutOptions: GridLayoutOptions = {
21. regularSize: [1, 1],
22. irregularIndexes: [10]
23. };
24. private gridScroller: Scroller = new Scroller();
25. private num: number = 0;

27. aboutToAppear(): void {
28. for (let i = 0; i < 10; i++) {
29. // 此处app.media.gridItem0、app.media.gridItem1、app.media.gridItem2仅作示例，请开发者自行替换
30. this.itemList.push(new DemoGridItemInfo('Video' + i,
31. i % 3 == 0 ? $r('app.media.gridItem0') :
32. i % 3 == 1 ? $r('app.media.gridItem1') : $r('app.media.gridItem2')));
33. }
34. }

36. build() {
37. Column({ space: 10 }) {
38. Text('Grid Contains the Repeat Component')
39. .fontSize(15)
40. .fontColor(Color.Gray)

42. Refresh({ refreshing: $$this.isRefreshing }) {
43. Grid(this.gridScroller, this.layoutOptions) {
44. Repeat<DemoGridItemInfo>(this.itemList)
45. .each((obj: RepeatItem<DemoGridItemInfo>) => {
46. if (obj.index === 10 ) {
47. GridItem() {
48. Text('Last viewed here. Touch to refresh.')
49. .fontSize(20)
50. }
51. .height(30)
52. .border({ width: 1 })
53. .onClick(() => {
54. this.gridScroller.scrollToIndex(0);
55. this.isRefreshing = true;
56. })
57. .onAppear(() => {
58. hilog.info(DOMAIN, TAG, 'AceTag', obj.item.name);
59. })
60. } else {
61. GridItem() {
62. Column() {
63. Image(obj.item.icon)
64. .width('100%')
65. .height(80)
66. .objectFit(ImageFit.Cover)
67. .borderRadius({ topLeft: 16, topRight: 16 })
68. Text(obj.item.name)
69. .fontSize(15)
70. .height(20)
71. }
72. }
73. .height(100)
74. .borderRadius(16)
75. .backgroundColor(Color.White)
76. .onAppear(() => {
77. hilog.info(DOMAIN, TAG, 'AceTag', obj.item.name);
78. })
79. }
80. })
81. .key((item: DemoGridItemInfo) => item.name)
82. .virtualScroll()
83. }
84. .columnsTemplate('repeat(auto-fit, 150)')
85. .cachedCount(4)
86. .rowsGap(15)
87. .columnsGap(10)
88. .height('100%')
89. .padding(10)
90. .backgroundColor('#F1F3F5')
91. }
92. .onRefreshing(() => {
93. setTimeout(() => {
94. this.itemList.splice(10, 1);
95. this.itemList.unshift(new DemoGridItemInfo('refresh', $r('app.media.gridItem0'))); // 此处app.media.gridItem0仅作示例，请开发者自行替换
96. for (let i = 0; i < 10; i++) {
97. // 此处app.media.gridItem0、app.media.gridItem1、app.media.gridItem2仅作示例，请开发者自行替换
98. this.itemList.unshift(new DemoGridItemInfo('New video' + this.num,
99. i % 3 == 0 ? $r('app.media.gridItem0') :
100. i % 3 == 1 ? $r('app.media.gridItem1') : $r('app.media.gridItem2')));
101. this.num++;
102. }
103. this.isRefreshing = false;
104. }, 1000);
105. })
106. .refreshOffset(64)
107. .pullToRefresh(true)
108. .width('100%')
109. .height('85%')

111. Button('Refresh')
112. .onClick(() => {
113. this.gridScroller.scrollToIndex(0);
114. this.isRefreshing = true;
115. })
116. }
117. .width('100%')
118. .height('100%')
119. .justifyContent(FlexAlign.Center)
120. }
121. }
```

[DemoGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/DemoGrid.ets#L16-L138)

下拉屏幕，或点击刷新按钮，或点击“先前浏览至此，点击刷新”，可加载新的视频内容：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MzzgYmTBRMOSMFqivcoJyQ/zh-cn_image_0000002583437717.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=2A1C5FC35ED7B3E69D1BED2EAF3397D05B4739F67C1F9ECC1F627C9E78FAF0BD)

**与Swiper组合使用**

在[Swiper](../harmonyos-references/ts-container-swiper.md)容器组件中使用Repeat，示例如下：

```
1. const remotePictures: string[] = [
2. 'common/image/image1.png', // 请填写具体的图片地址
3. 'common/image/image2.png',
4. 'common/image/image3.png',
5. ];

7. @ObservedV2
8. class DemoSwiperItemInfo {
9. public id: string;
10. @Trace public url: string = 'default';

12. constructor(id: string) {
13. this.id = id;
14. }
15. }

17. @Entry
18. @ComponentV2
19. struct DemoSwiper {
20. @Local pics: Array<DemoSwiperItemInfo> = [];

22. aboutToAppear(): void {
23. for (let i = 0; i < 3; i++) {
24. this.pics.push(new DemoSwiperItemInfo('pic' + i));
25. }
26. setTimeout(() => {
27. this.pics[0].url = remotePictures[0];
28. }, 1000);
29. }

31. build() {
32. Column() {
33. Text('Swiper Contains the Repeat Component')
34. .fontSize(15)
35. .fontColor(Color.Gray)

37. Stack() {
38. Text('Loading...')
39. .fontSize(15)
40. .fontColor(Color.Gray)
41. Swiper() {
42. Repeat(this.pics)
43. .each((obj: RepeatItem<DemoSwiperItemInfo>) => {
44. Image(obj.item.url)
45. .onAppear(() => {
46. })
47. })
48. .key((item: DemoSwiperItemInfo) => item.id)
49. .virtualScroll()
50. }
51. .cachedCount(9)
52. .height('50%')
53. .loop(false)
54. .indicator(true)
55. .onChange((index) => {
56. setTimeout(() => {
57. this.pics[index].url = remotePictures[index];
58. }, 1000);
59. })
60. }
61. .width('100%')
62. .height('100%')
63. .backgroundColor(Color.Black)
64. }
65. }
66. }
```

[DemoSwiper.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/DemoSwiper.ets#L16-L83)

定时1秒后加载图片，模拟网络延迟：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/zeDjR3-JRNmUGeiRHMp5Nw/zh-cn_image_0000002552957672.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=CD1E59BF1E56482EE03EC26C48B4396CE0E015C9817BD5CFF2FE6F601A21F90A)

## 常见问题

### 显示区域外增删数据时保持滚动位置不变

下面的场景示例中，滚动列表显示区域外的增删数据操作将影响[List](../harmonyos-references/ts-container-list.md)列表滚动条停留的位置：

在List组件中声明Repeat组件，实现key值生成逻辑和each逻辑（如下示例代码），点击按钮“insert”，在屏幕显示的第一个元素前面插入一个元素，列表显示区域数据向下滚动。

```
1. // 定义一个类，标记为可观察的
2. // 类中自定义一个数组，标记为可追踪的
3. @ObservedV2
4. class ArrayHolder {
5. @Trace public arr: Array<number> = [];

7. // constructor，用于初始化数组个数
8. constructor(count: number) {
9. for (let i = 0; i < count; i++) {
10. this.arr.push(i);
11. }
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct RepeatTemplateSingle {
18. @Local arrayHolder: ArrayHolder = new ArrayHolder(100);
19. @Local totalCount: number = this.arrayHolder.arr.length;
20. scroller: Scroller = new Scroller();

22. build() {
23. Column({ space: 5 }) {
24. List({ space: 20, initialIndex: 19, scroller: this.scroller }) {
25. Repeat(this.arrayHolder.arr)
26. .virtualScroll({ totalCount: this.totalCount })
27. .templateId((item, index) => {
28. return 'number';
29. })
30. .template('number', (r) => {
31. ListItem() {
32. Text(r.index! + ':' + r.item + 'Reuse');
33. }
34. })
35. .each((r) => {
36. ListItem() {
37. Text(r.index! + ':' + r.item + 'eachMessage');
38. }
39. })
40. }
41. .height('30%')

43. Button(`insert totalCount ${this.totalCount}`)
44. .height(60)
45. .onClick(() => {
46. // 插入元素，元素位置为屏幕显示的前一个元素
47. this.arrayHolder.arr.splice(18, 0, this.totalCount);
48. this.totalCount = this.arrayHolder.arr.length;
49. })
50. }
51. .width('100%')
52. .margin({ top: 5 })
53. }
54. }
```

[RepeatTemplateSingle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatTemplateSingle.ets#L16-L71)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/jXQn8fCpTXSuV78-2M_skQ/zh-cn_image_0000002583477673.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=B1DB358A26BB03C575903C8DAB843AABFEF391735CA71594D8DD7C913C40FCFC)

以下为修正后的示例：

在部分场景中，我们不希望显示区域外的数据源增删操作或高度变化影响屏幕中[List](../harmonyos-references/ts-container-list.md)列表Scroller停留的位置，可以通过List组件的[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)事件对列表滚动动作进行监听，当列表发生滚动时，获取列表滚动位置。使用Scroller组件的[scrollToIndex](../harmonyos-references/ts-container-scroll.md#scrolltoindex)特性，滑动到指定index位置，实现屏幕外的数据源增加/删除数据时，Scroller停留的位置不变的效果。

示例代码仅对增加数据的情况进行展示。

说明

Repeat从API version 20开始支持[数据前插保持](arkts-new-rendering-control-repeat.md#数据前插保持)，该功能特性可通过简单配置List组件的属性实现相同的效果。

```
1. // 定义一个类，标记为可观察的
2. // 类中自定义一个数组，标记为可追踪的
3. @ObservedV2
4. class ArrayHolderLocal {
5. @Trace public arr: Array<number> = [];

7. // constructor，用于初始化数组个数
8. constructor(count: number) {
9. for (let i = 0; i < count; i++) {
10. this.arr.push(i);
11. }
12. }
13. }
14. @Entry
15. @ComponentV2
16. struct RepeatSingle {
17. @Local arrayHolder: ArrayHolderLocal = new ArrayHolderLocal(100);
18. @Local totalCount: number = this.arrayHolder.arr.length;
19. scroller: Scroller = new Scroller();

21. private start: number = 1;
22. private end: number = 1;

24. build() {
25. Column({ space: 5 }) {
26. List({ space: 20, initialIndex: 19, scroller: this.scroller }) {
27. Repeat(this.arrayHolder.arr)
28. .virtualScroll({ totalCount: this.totalCount })
29. .templateId((item, index) => {
30. return 'number';
31. })
32. .template('number', (r) => {
33. ListItem() {
34. Text(r.index! + ':' + r.item + 'Reuse')
35. }
36. })
37. .each((r) => {
38. ListItem() {
39. Text(r.index! + ':' + r.item + 'eachMessage')
40. }
41. })
42. }
43. .onScrollIndex((start, end) => {
44. this.start = start;
45. this.end = end;
46. })
47. .height('30%')

49. Button(`insert totalCount ${this.totalCount}`)
50. .height(60)
51. .onClick(() => {
52. // 插入元素，元素位置为屏幕显示的前一个元素
53. this.arrayHolder.arr.splice(18, 0, this.totalCount);
54. let rect = this.scroller.getItemRect(this.start); // 获取子组件的大小位置
55. this.scroller.scrollToIndex(this.start + 1); // 滑动到指定index
56. this.scroller.scrollBy(0, -rect.y); // 滑动指定距离
57. this.totalCount = this.arrayHolder.arr.length;
58. })
59. }
60. .width('100%')
61. .margin({ top: 5 })
62. }
63. }
```

[RepeatTemplateSingle1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/RepeatTemplateSingle1.ets#L16-L80)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xU-oEaPbTfmg4HBlzNEQ9A/zh-cn_image_0000002552798024.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=56707C2384D35B6603C6CE612DA75AFACAE74F8A10EF95BF26E5D968DFD7CAA3)

### totalCount值大于数据源长度

当数据源总长度很大时，会使用懒加载的方式先加载一部分数据，为了使Repeat显示正确的滚动条样式，需要将数据总长度赋值给totalCount，即数据源全部加载完成前，totalCount大于array.length。

totalCount > array.length时，在父组件容器滚动过程中，应用需要保证列表即将滑动到数据源末尾时请求后续数据，开发者需要对数据请求的错误场景（如网络延迟）进行保护操作，直到数据源全部加载完成，否则列表滑动的过程中会出现滚动效果异常。

上述规范可以通过实现父组件[List](../harmonyos-references/ts-container-list.md)/[Grid](../harmonyos-references/ts-container-grid.md)的[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)属性的回调函数完成。示例代码如下：

说明

Repeat从API version 19开始支持[数据精准懒加载](arkts-new-rendering-control-repeat.md#数据精准懒加载)，该功能特性可通过配置onLazyLoading回调函数动态加载对应区域内的数据。

```
1. @ObservedV2
2. class VehicleData {
3. @Trace public name: string;
4. @Trace public price: number;

6. constructor(name: string, price: number) {
7. this.name = name;
8. this.price = price;
9. }
10. }

12. @ObservedV2
13. class VehicleDB {
14. public vehicleItems: VehicleData[] = [];

16. constructor() {
17. // 数组初始化大小 20
18. for (let i = 1; i <= 20; i++) {
19. this.vehicleItems.push(new VehicleData(`Vehicle${i}`, i));
20. }
21. }
22. }

24. @Entry
25. @ComponentV2
26. struct EntryCompSucc {
27. @Local vehicleItems: VehicleData[] = new VehicleDB().vehicleItems;
28. @Local listChildrenSize: ChildrenMainSize = new ChildrenMainSize(60);
29. @Local totalCount: number = this.vehicleItems.length;
30. scroller: Scroller = new Scroller();

32. build() {
33. Column({ space: 3 }) {
34. List({ scroller: this.scroller }) {
35. Repeat(this.vehicleItems)
36. .virtualScroll({ totalCount: 50 }) // 数组预期长度 50
37. .templateId(() => 'default')
38. .template('default', (ri) => {
39. ListItem() {
40. Column() {
41. Text(`${ri.item.name} + ${ri.index}`)
42. .width('90%')
43. .height(this.listChildrenSize.childDefaultSize)
44. .backgroundColor(0xFFA07A)
45. .textAlign(TextAlign.Center)
46. .fontSize(20)
47. .fontWeight(FontWeight.Bold)
48. }
49. }.border({ width: 1 })
50. }, { cachedCount: 5 })
51. .each((ri) => {
52. ListItem() {
53. Text('Wrong: ' + `${ri.item.name} + ${ri.index}`)
54. .width('90%')
55. .height(this.listChildrenSize.childDefaultSize)
56. .backgroundColor(0xFFA07A)
57. .textAlign(TextAlign.Center)
58. .fontSize(20)
59. .fontWeight(FontWeight.Bold)
60. }.border({ width: 1 })
61. })
62. .key((item, index) => `${index}:${item}`)
63. }
64. .height('50%')
65. .margin({ top: 20 })
66. .childrenMainSize(this.listChildrenSize)
67. .alignListItem(ListItemAlign.Center)
68. .onScrollIndex((start, end) => {
69. // 数据懒加载
70. if (this.vehicleItems.length < 50) {
71. for (let i = 0; i < 10; i++) {
72. if (this.vehicleItems.length < 50) {
73. this.vehicleItems.push(new VehicleData('Vehicle_loaded', i));
74. }
75. }
76. }
77. })
78. }
79. }
80. }
```

[EntryCompSucc.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingRepeat/EntryCompSucc.ets#L16-L97)

示例代码运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/wv-DV7HSR-mU1rVAwWMUrA/zh-cn_image_0000002583437719.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=EE03F2DF1256040A7105181FE7F51F5741313EA62A86A7DCCC03CE9F7AABC6C3)

### 与@Builder混用时状态变量未刷新

当Repeat与[@Builder](arkts-builder.md)混用时，如果只传递RepeatItem.item或RepeatItem.index，参数值的改变不会引起@Builder函数内的UI刷新。推荐使用[按引用传递](arkts-builder.md#按引用传递参数)，即将RepeatItem类型整体进行传参，组件才能监听到数据变化。除此之外，从API version 20开始，开发者可以通过使用[UIUtils.makeBinding()](../harmonyos-references/js-apis-statemanagement.md#makebinding20)函数、[Binding类](../harmonyos-references/js-apis-statemanagement.md#bindingt20)和[MutableBinding类](../harmonyos-references/js-apis-statemanagement.md#mutablebindingt20)实现@Builder函数中状态变量的刷新。

示例代码如下：

```
1. import { UIUtils, Binding } from '@kit.ArkUI';

3. @Entry
4. @ComponentV2
5. struct RepeatBuilderPage {
6. @Local simpleList: Array<number> = [];

8. aboutToAppear(): void {
9. for (let i = 0; i < 100; i++) {
10. this.simpleList.push(i);
11. }
12. }

14. @Builder
15. buildItem1(bindingData: Binding<number>) { // 使用Binding类/MutableBinding类接收传参，通过value属性访问值。
16. Text('[Binding] item: ' + bindingData.value)
17. .fontSize(20)
18. }

20. @Builder
21. buildItem2(ri: RepeatItem<number>) {
22. Text('[RepeatItem] item: ' + ri.item)
23. .fontSize(20)
24. }

26. @Builder
27. buildItem3(data: number) {
28. Text('[number] item: ' + data)
29. .fontSize(20).fontColor(Color.Red)
30. }

32. build() {
33. Column({ space: 10 }) {
34. List({ space: 20 }) {
35. Repeat<number>(this.simpleList)
36. .each((ri) => {
37. ListItem() {
38. Column({ space: 2 }) {
39. this.buildItem1(UIUtils.makeBinding<number>(() => ri.item)) // 使用UIUtils.makeBinding()函数实现@Builder函数中状态变量的刷新。
40. this.buildItem2(ri) // 按引用传递，状态变量的改变会引起@Builder函数内的UI刷新。
41. this.buildItem3(ri.item) // 反例。按值传递，状态变量的改变不会引起@Builder函数内的UI刷新。
42. }
43. }.border({ width: 1 })
44. }).virtualScroll()
45. }
46. .cachedCount(1)
47. .border({ width: 1 })
48. .width('70%')
49. .height('60%')
50. .alignListItem(ListItemAlign.Center)

52. Button('click to change data.').onClick(() => {
53. this.simpleList[0] = 10000; // 修改第一项数据为10000。
54. })
55. }
56. .width('100%').height('100%')
57. .justifyContent(FlexAlign.Center)
58. }
59. }
```

@Builder传参方式依次为makeBinding()、地址传递和值传递，界面展示如下图，进入页面后点击按钮改变数据。在@Builder构造函数中使用值传递传参不会引起函数内的UI刷新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/z8q-YwX1SI6pzAT8OS8-BQ/zh-cn_image_0000002552957674.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=6809F6916FA64A0016A027DBC8BF3F227B4D43B338EFAB054DD3E95A8789D9B3)

### expandSafeArea属性失效

在API version 18之前，Repeat子组件声明expandSafeArea属性，子组件无法扩展至全屏；从API version 18开始，子组件声明expandSafeArea属性可正常扩展至全屏展示。
