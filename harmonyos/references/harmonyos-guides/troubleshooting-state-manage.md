---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/troubleshooting-state-manage
title: 状态变量改变不触发组件刷新问题常用定位方法
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理常见问题 > 状态变量改变不触发组件刷新问题常用定位方法
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42a71135d9b4661bacb40b443a5b336455a912d7e1515577f5ba3717624c1e51
---

在声明式UI编程框架中，状态管理的主要职责是：当状态变量改变时，触发其关联组件的刷新。所以在使用状态变量的过程中，最常见的问题就是组件不刷新。本文主要针对开发者在使用状态变量时遇到的不刷新问题，阐述以下两个方面。

* 如何定位状态变量不刷新的问题。
* 不刷新问题常见案例。

## 定位状态变量不刷新问题的主要方法

状态变量触发UI刷新主要分为两步：

* 收集依赖：收集状态变量关联组件ID。
* 触发更新：标记需要更新的节点，触发需要更新的节点的更新。

这部分的原理在本篇文档中仅做简要说明，详情见[状态管理原理介绍](arkts-state-management-introduce.md)。基于上面的状态变量触发UI刷新的流程，在定位不刷新问题时，可以分为以下五步来定位。

### 第一步：状态变量收集依赖

基于状态管理的更新流程，状态变量触发UI组件更新的前提是，当前状态变量已经收集到UI组件的依赖，具体来说也就是在组件初始化的过程，触发了状态变量的“读”操作。

检查状态变量是否收集到组件的ID可通过以下工具：

* 使用DevEco Studio的ArkUI Inspector。具体使用方法见[状态管理Inspector调试能力](ui-inspector-profiler.md#状态管理inspector调试能力)。
* 使用[hidumper](hidumper.md)工具。具体使用方法见[状态管理hidumper能力](ui-inspector-profiler.md#状态管理hidumper能力)。

### 第二步：状态变量发生改变

在给状态变量赋值时，状态管理框架会检查当前被赋值的状态变量的值是否有变化，如果没有变化，则会直接返回，不做任何操作。最简单的排查手段是分别打印修改状态变量前后的值，检查是否有变化。如以下示例。

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. build() {
7. Column() {
8. Text(this.message)
9. .onClick(() => {
10. console.info(`message set before ${this.message}`);
11. this.message = 'Welcome';
12. console.info(`message set after ${this.message}`);
13. })
14. }
15. }
16. }
```

观察日志输出this.message前后发生改变，日志输出如下：

```
1. message set before Hello World
2. message set after Welcome
```

### 第三步：状态变量的赋值是否可被观察

**状态管理V1**

在状态管理V1中，若开发者确认赋值前后值已发生变化却未能触发UI刷新，应检查当前赋值操作是否可被观察（从API version 23开始，开发者可以使用[canBeObserved](arkts-new-canbeobserved.md)接口来判断对象是否可被观察）。示例如下。

在下面的示例中，开发者对this.inner.value的赋值无法触发Text(`Child: inner value: ${this.inner.value}`)组件的刷新，在遇到这个问题时，应该从以下方面排查当前赋值操作是否是可被观察。

* [@Watch](arkts-watch.md)的监听函数是否执行。
* 如果状态变量为复杂类型且需要观察其属性的赋值变化，开发者还可以通过[getTarget](arkts-new-gettarget.md)来判断当前变量是否可观察。
* 使用DevEco Studio的Profiler工具观察此次赋值是否有状态变量变化的上报，具体使用方法见[状态管理profiler调优能力](ui-inspector-profiler.md#状态管理profiler调优能力)。

```
1. import { UIUtils } from '@kit.ArkUI';

3. class Outer {
4. value: string = 'outer';
5. inner: Inner = new Inner();
6. }

8. class Inner {
9. value: string = 'inner';
10. }

12. @Entry
13. @Component
14. struct Index {
15. @State outer: Outer = new Outer();

17. build() {
18. Column() {
19. Text(`Index: outer value: ${this.outer.value}`)
20. Child({ inner: this.outer.inner })
21. }
22. }
23. }

25. @Component
26. struct Child {
27. // 写法错误：@ObjectLink初始化的变量不是@Observed装饰的类的实例
28. // 状态管理会打印error日志提醒开发者：
29. // FIX THIS APPLICATION ERROR: @ObjectLink inner owned by @Component Child set/init (method setValueInternal): assigned value is not be decorated by @Observed. Value changes will not be observed and UI will not update.
30. @ObjectLink @Watch('onChange') inner: Inner;

32. aboutToAppear(): void {
33. // 通过getTarget获取状态变量的原始对象，如果两者相等，即原始对象和该对象是同一个对象，则其不是一个可观察的数据
34. // 如果两者不相等，则其为可观察的对象
35. // 因为Inner缺少@Observed装饰器装饰，所以下面日志输出为：
36. // inner is not observed object
37. console.info(`inner is ${UIUtils.getTarget(this.inner) === this.inner ? 'not observed object' :
38. 'observed object'}`);
39. }

41. onChange() {
42. console.info(`inner property has been changed ${this.inner.value}`);
43. }

45. build() {
46. Column() {
47. Text(`Child: inner value: ${this.inner.value}`)
48. .onClick(() => {
49. this.inner.value += '!';
50. })
51. }
52. }
53. }
```

在上面的示例中，Inner没有被[@Observed](arkts-observed-and-objectlink.md)装饰，所以其属性value的赋值无法被观察：

* @Watch('onChange')函数没有执行。
* 日志提示inner is not observed object。
* ArkUI State泳道没有状态变量变化的上报信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FrKDD2VlQPuMhRpFYkOFqQ/zh-cn_image_0000002552957640.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=070BF0955E835B83C8A322BBD836403143E5B7E12AB345C222FC2BF3D590DDB6)

需要注意，并非所有的类对象都需要被@Observed装饰。[@State](arkts-state.md)装饰器会默认对复杂对象包装第一层代理，而对嵌套对象，则需要在内层对象的类声明上增加@Observed装饰。

正确示例：

```
1. import { UIUtils } from '@kit.ArkUI';

3. class Outer {
4. value: string = 'outer';
5. inner: Inner = new Inner();
6. }

8. @Observed
9. class Inner {
10. value: string = 'inner';
11. }

13. @Entry
14. @Component
15. struct Index {
16. @State outer: Outer = new Outer();

18. build() {
19. Column() {
20. Text(`Index: outer value: ${this.outer.value}`)
21. Child({ inner: this.outer.inner })
22. }
23. }
24. }

26. @Component
27. struct Child {
28. @ObjectLink @Watch('onChange') inner: Inner;

30. aboutToAppear(): void {
31. // 日志输出：inner is observed object
32. console.info(`inner is ${UIUtils.getTarget(this.inner) === this.inner ? 'not observed object' :
33. 'observed object'}`);
34. }

36. onChange() {
37. console.info(`inner property has been changed ${this.inner.value}`)
38. }

40. build() {
41. Column() {
42. Text(`Child: inner value: ${this.inner.value}`)
43. .onClick(() => {
44. this.inner.value += '!';
45. })
46. }
47. }
48. }
```

在正确的示例中：

* @Watch监听函数被正常触发。
* 日志提示inner is observed object。
* ArkUI State泳道有状态变量变化的上报信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/-c9FHYUVQlKKr6BLxVP0bw/zh-cn_image_0000002583477641.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=0C9FE3B5ABE7137F4381FB712E9ABC386A30A324609877D54BF6A9C4191F7694)

**状态管理V2**

状态管理V2中，对复杂对象的观察分以下两种情况：

* 普通类：

  与状态管理V1不同，在状态管理V2观察普通类时，框架不会为其实例创建代理对象，因此无法通过getTarget来判断其是否为代理对象。开发者可以通过以下方式判断：

  + 通过检查要观察的属性是否是[@Trace](arkts-new-observedv2-and-trace.md)装饰。
  + 观察ArkUI State泳道是否有状态变量变化信息上报，具体使用方法见[状态管理profiler调优能力](ui-inspector-profiler.md#状态管理profiler调优能力)。
* 内置类型（Built-in Types）：

  在状态管理V2中，Array、Map、Set会包装代理对象，开发者可以通过调用getTarget来判断当前类型是否为代理数据。

具体示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. @ObservedV2
4. class Info {
5. @Trace value: string = 'info';
6. @Trace numberArr: number[] = [];
7. count: number = 0;

9. constructor(val: string) {
10. this.value = val;
11. this.numberArr = [0, 1, 2];
12. }
13. }

15. @Entry
16. @ComponentV2
17. struct Index {
18. info: Info = new Info('info');

20. aboutToAppear(): void {
21. // 日志输出：this.info.numberArr is observed array
22. console.info(`this.info.numberArr is ${UIUtils.getTarget(this.info.numberArr) === this.info.numberArr ?
23. 'not observed array' :
24. 'observed array'}`);
25. }

27. build() {
28. Column() {
29. Text(`Index: info value: ${this.info.value}`)
30. Text(`Index: info numberArr length: ${this.info.numberArr.length}`)
31. Text(`Index: info count: ${this.info.count}`)

33. Button('change info property').onClick(() => {
34. this.info.value = 'new info';
35. this.info.numberArr.push(3);
36. this.info.count++;
37. })
38. }
39. }
40. }
```

基于上面的示例，观察ArkUI State泳道，有两次状态变量的变化上报，即this.info.value和this.info.numberArr。count不是@Trace装饰的，所以不会被观察到变化，也不会在Profiler上报状态变量的变化。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/sVYF6AqZR1qLqbFhxLkhxA/zh-cn_image_0000002552797992.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=60D624BC688FDA2270A05E95B19B349D282183FA60694940CE9F1A7F95CFFA6E)

### 第四步：数据源和被同步的对象是否有关联关系

状态管理中，数据源会通过双向或单向机制通知同步对象。如果开发者遇到数据源改变，但其同步对象没有被通知的情况，可以按下面的方式排查。

**状态管理V1**

状态管理V1存在下面两类同步方式：

* 同步对象(sync peer)：如@State和[@Link](arkts-link.md)、[@Provide](arkts-provide-and-consume.md)和[@Consume](arkts-provide-and-consume.md)。开发者可以通过DevEco Studio的ArkUI Inspector来查看数据源和同步对象之间是否存在同步关系，具体见[状态管理Inspector调试能力](ui-inspector-profiler.md#状态管理inspector调试能力)。
* 依赖其所属组件的更新函数：如@State通知@Prop变化、@State通知@ObjectLink变化。开发者可以使用断点调试工具，或者[getHash接口](../harmonyos-references/js-apis-util.md#utilgethash12)来判断数据源和同步对象是否为同一个对象的引用(hashcode并不固定，以开发者自己打印的为准)。

**状态管理V2**

状态管理V2没有同步对象(sync peer)的概念。[@Local](arkts-new-local.md)和[@Param](arkts-new-param.md)的同步方式是依赖@Param组件所属组件的更新函数。

这类问题中，常见的场景是和[ForEach](arkts-rendering-control-foreach.md)和[LazyForEach](arkts-rendering-control-lazyforeach.md)联用导致数据源和其同步对象断链。如以下示例。

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { util } from '@kit.ArkTS';

4. @Observed
5. class Info {
6. value: string = 'info';
7. }

9. @Entry
10. @Component
11. struct Index {
12. @State infos: Info[] = [new Info()];

14. build() {
15. Column() {
16. // 第一步：点击该Button
17. // 触发ForEach的刷新，ForEach对比前后key值没有改变，没有触发Child的更新，所以@ObjectLink info还是指向之前的Info的实例
18. // 出现@State infos和@ObjectLink info断链
19. Button('change first item value').onClick(() => {
20. this.infos[0] = new Info();
21. })

23. // 第二步：点击该Button，@ObjectLink info的@Watch的函数没有被触发
24. // 日志打印：this.infos[0] hashcode: 993656661
25. // this.infos[0]和@ObjectLink info不是同一个对象的引用，@State无法通知@ObjectLink刷新
26. Button('change first item value').onClick(() => {
27. this.infos[0].value += '1';
28. console.info(`this.infos[0] hashcode: ${util.getHash(this.infos[0])}`);
29. })
30. ForEach(this.infos, (item: Info) => {
31. Child({ info: item })
32. })
33. }
34. }
35. }

37. @Component
38. struct Child {
39. @ObjectLink @Watch('onChange') info: Info;

41. aboutToAppear(): void {
42. // 日志输出:
43. // info is observed object, hashcode: 1806047025
44. // hashcode并不固定，根据开发者自己打印的为准
45. console.info(`info is ${UIUtils.getTarget(this.info) === this.info ? 'not observed object' :
46. 'observed object'}, hashcode: ${util.getHash(this.info)}`);
47. }

49. onChange() {
50. console.info(`info property has been changed ${this.info.value}`);
51. }

53. build() {
54. Column() {
55. Text(`Child: info value: ${this.info.value}`)
56. .onClick(() => {
57. this.info.value += '2';
58. })
59. }
60. }
61. }
```

正确示例：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { util } from '@kit.ArkTS';

4. @Observed
5. class Info {
6. value: string = 'info';
7. }

9. @Entry
10. @Component
11. struct Index {
12. @State infos: Info[] = [new Info()];

14. build() {
15. Column() {
16. // 第一步：点击该Button
17. // 触发ForEach的刷新，ForEach对比前后key值改变，触发Child的重建，@ObjectLink info指向新的Info的实例
18. Button('change first item value').onClick(() => {
19. this.infos[0] = new Info();
20. })

22. // 第二步：点击该Button，@ObjectLink info的@Watch的函数被触发
23. // 日志打印：this.infos[0] hashcode: 358024053
24. Button('change first item value').onClick(() => {
25. this.infos[0].value += '1';
26. console.info(`this.infos[0] hashcode: ${util.getHash(this.infos[0])}`);
27. })

29. ForEach(this.infos, (item: Info) => {
30. Child({ info: item })
31. }, (item: Info) => {
32. // 随机数key值
33. return item.value + Math.random().toString();
34. })
35. }
36. }
37. }

39. @Component
40. struct Child {
41. @ObjectLink @Watch('onChange') info: Info;

43. aboutToAppear(): void {
44. // 日志输出:
45. // 首次创建： info is observed object, hashcode: 2026693567
46. // 点击Button('change first item value')，触发Child重建：info is observed object, hashcode: 358024053
47. console.info(`info is ${UIUtils.getTarget(this.info) === this.info ? 'not observed object' :
48. 'observed object'}, hashcode: ${util.getHash(this.info)}`);
49. }

51. onChange() {
52. console.info(`info property has been changed ${this.info.value}`);
53. }

55. build() {
56. Column() {
57. Text(`Child: info value: ${this.info.value}`)
58. .onClick(() => {
59. this.info.value += '2';
60. })
61. }
62. }
63. }
```

### 第五步：是否执行组件的更新函数

在检查了前四步后，如果发现UI依旧没有刷新，这就要检查最后一步，没有刷新的组件是否执行了更新函数。

这类问题常发生于，开发者在组件的同步回调里改变了状态变量，导致当前正在刷新的组件再次被加入到了待刷新的组件列表里，从而使状态管理框架忽略了这个组件的刷新。以[Image组件](../harmonyos-references/ts-basic-components-image.md)的[onComplete](../harmonyos-references/ts-basic-components-image.md#oncomplete)接口为例。

开发者可以通过封装获取组件属性方法来观察当前组件是否发生重新渲染。如下面示例：

```
1. @Entry
2. @Component
3. struct Page {
4. @State widthValue: number = 100;
5. @State flag: boolean = true;

7. // 封装getHeightValue方法观察Image是否发生重新渲染
8. getHeightValue(): number {
9. console.info('Image render');
10. return 500;
11. }

13. build() {
14. Column() {
15. Image(this.flag ? $r('app.media.startIcon') : $r('app.media.background'))
16. .width(this.widthValue)
17. .height(this.getHeightValue())
18. .backgroundColor(Color.Pink)
19. .onComplete((event) => {
20. this.widthValue = 200;
21. console.info(`Image onComplete ${this.widthValue} load status: ${event?.loadingStatus}`);
22. })

24. Button('change resource').onClick(() => {
25. // 第一步：改变flag，使得两个Resource变量都进入Image组件的缓存
26. // 第三步：再次改变Image的Resource，此时onComplete为同步回调
27. // onComplete的回调中同步修改widthValue为200
28. // 打印状态管理的错误日志：FIX THIS APPLICATION ERROR: @Component 'Page: State variable 'widthValue' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
29. // 没有打印Image render日志，Image宽度没有发生改变
30. this.flag = !this.flag;
31. })

33. Button('change widthValue').onClick(() => {
34. // 第二步：改变image宽度为100
35. this.widthValue = 100;
36. })
37. }
38. .height('100%')
39. .width('100%')
40. }
41. }
```

第三步点击Button('change resource')后，输出日志如下：

```
1. Image render
2. FIX THIS APPLICATION ERROR: @Component 'Page: State variable 'widthValue' has changed during render! It's illegal to change @Component state while build (initial render or re-render) is on-going. Application error!
3. Image onComplete 200 load status: 0
4. Image onComplete 200 load status: 1
```

可以看到在onComplete改变状态变量widthValue后，没有触发Image render日志，这次状态变量的改变没有触发Image组件的刷新。

正确示例：

可以将组件的同步回调中对状态变量的赋值通过setTimeout转换为异步执行，示例如下。

```
1. @Entry
2. @Component
3. struct Page {
4. @State widthValue: number = 100;
5. @State flag: boolean = true;

7. getHeightValue(): number {
8. console.info('Image render');
9. return 500;
10. }

12. build() {
13. Column() {
14. Image(this.flag ? $r('app.media.startIcon') : $r('app.media.background'))
15. .width(this.widthValue)
16. .height(this.getHeightValue())
17. .backgroundColor(Color.Pink)
18. .onComplete((event) => {
19. setTimeout(() =>{
20. this.widthValue = 200;
21. console.info(`Image onComplete ${this.widthValue} load status: ${event?.loadingStatus}`);
22. });
23. })

25. Button('change resource').onClick(() => {
26. // 第一步：改变flag，使得两个Resource变量都进入Image组件的缓存
27. // 第三步：再次改变Image的Resource，此时onComplete为同步回调
28. // onComplete的回调中异步修改widthValue为200
29. // Image宽度刷新为200
30. this.flag = !this.flag;
31. })

33. Button('change widthValue').onClick(() => {
34. // 第二步：改变image宽度为100
35. this.widthValue = 100;
36. })
37. }
38. .height('100%')
39. .width('100%')
40. }
41. }
```

第三步点击Button('change resource')后，输出日志如下：

```
1. Image render
2. Image onComplete 200 load status: 0
3. Image onComplete 200 load status: 1
4. Image render
```

可以看到在onComplete内的setTimeout改变状态变量widthValue后，触发Image render日志，Image宽度刷新为200。

## 总结

基于上述流程与示例，可以总结出定位不刷新问题的核心思路如下。

* 状态变量是否收集到了需要触发刷新组件的ID。
* 状态变量的赋值是否为可观察的变化。
* 需要刷新的组件是否执行了更新函数。

开发者在遇到不刷新的问题的时候，可以依据上面的定位流程，或者带着这三点疑问来排查代码，提高定位问题的效率。
