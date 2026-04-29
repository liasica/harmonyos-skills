---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved
title: makeObserved接口：将非观察数据变为可观察数据
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 辅助接口 > makeObserved接口：将非观察数据变为可观察数据
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:22+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:1cc7aa27370a24b820ecba9f2cbea316edd14a47e788a563a9e3a89b980cfbb8
---

为了将普通不可观察数据变为可观察数据，开发者可以使用[makeObserved接口](../harmonyos-references/js-apis-statemanagement.md#makeobserved)。

makeObserved可以在@Trace无法标记的情况下使用。在阅读本文档前，建议提前阅读：[@Trace](arkts-new-observedv2-and-trace.md)。

说明

从API version 12开始，开发者可以使用UIUtils中的makeObserved接口将普通不可观察数据变为可观察数据。

## 概述

* 状态管理框架已提供[@ObservedV2/@Trace](arkts-new-observedv2-and-trace.md)用于观察类属性变化，makeObserved接口提供主要应用于@ObservedV2/@Trace无法涵盖的场景：

  + class的定义在三方包中：开发者无法手动对class中需要观察的属性加上@Trace标签，可以使用makeObserved使得当前对象可以被观察。
  + 当前类的成员属性不能被修改：因为@Trace观察类属性会动态修改类的属性，这个行为在[@Sendable](arkts-sendable.md#sendable装饰器)装饰的class中是不被允许的，此时可以使用makeObserved。
  + interface或者JSON.parse返回的匿名对象：这类场景往往没有明确的class声明，开发者无法使用@Trace标记当前属性可以被观察，此时可以使用makeObserved。
* 使用makeObserved接口需要导入UIUtils。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  ```

## 限制条件

* makeObserved仅支持非空的对象类型传参。

  + 不支持undefined和null：返回自身，不做任何处理。
  + 非Object类型：编译拦截报错。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. let res1 = UIUtils.makeObserved(2); // 非法类型入参，错误用法，编译报错
  3. let res2 = UIUtils.makeObserved(undefined); // 非法类型入参，错误用法，返回自身，res2 === undefined
  4. let res3 = UIUtils.makeObserved(null); // 非法类型入参，错误用法，返回自身，res3 === null

  6. class Info {
  7. id: number = 0;
  8. }
  9. let rawInfo: Info = UIUtils.makeObserved(new Info()); // 正确用法
  ```
* makeObserved不支持传入被[@ObservedV2](arkts-new-observedv2-and-trace.md)、[@Observed](arkts-observed-and-objectlink.md)装饰的类的实例和被makeObserved封装过的代理数据。为了防止数据被双重代理，makeObserved发现入参为上述情况时则直接返回，不做处理。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. @ObservedV2
  3. class Info {
  4. @Trace id: number = 0;
  5. }
  6. // 错误用法：makeObserved发现传入的实例是@ObservedV2装饰的类的实例，则返回传入对象自身
  7. let observedInfo: Info = UIUtils.makeObserved(new Info());

  9. class Info2 {
  10. id: number = 0;
  11. }
  12. // 正确用法：传入对象既不是@ObservedV2/@Observed装饰的类的实例，也不是makeObserved封装过的代理数据
  13. // 返回可观察数据
  14. let observedInfo1: Info2 = UIUtils.makeObserved(new Info2());
  15. // 错误用法：传入对象为makeObserved封装过的代理数据，此次makeObserved不做处理
  16. let observedInfo2: Info2 = UIUtils.makeObserved(observedInfo1);
  ```
* makeObserved可以用在[@Component](arkts-create-custom-components.md#component)装饰的自定义组件中，但不能和状态管理V1的状态变量装饰器配合使用，如果一起使用，则会抛出运行时异常。

  ```
  1. // 错误写法，运行时异常
  2. @State message: Info = UIUtils.makeObserved(new Info(20));
  ```

  注意：下面message2的写法不会抛异常。原因是：

  + this.message是[@State](arkts-state.md)装饰的，其实现等同于@Observed。
  + UIUtils.makeObserved的入参如果是@Observed装饰的class的实例，会直接返回自身。

  因此message2的初始值不是makeObserved返回的代理对象，而是@State装饰的this.message。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. class Person {
  3. public age: number = 10;
  4. }
  5. class Info {
  6. public id: number = 0;
  7. public person: Person = new Person();
  8. }
  9. @Entry
  10. @Component
  11. struct Page1 {
  12. @State message: Info = new Info();
  13. @State message2: Info = UIUtils.makeObserved(this.message); // 不会抛异常
  14. build() {
  15. Column() {
  16. Text(`${this.message2.person.age}`)
  17. .onClick(() => {
  18. // UI不会刷新，因为State只能观察到第一层的变化
  19. this.message2.person.age++;
  20. })
  21. }
  22. }
  23. }
  ```

  [Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page1.ets#L15-L39)

### makeObserved仅对入参对象进行深度观察

* message被[@Local](arkts-new-local.md)装饰，本身具有观察自身赋值的能力。其初始值为makeObserved的返回值，具有深度观察能力。需要注意，makeObserved仅对message进行深度观察，而message自身赋值的变化，则是由@Local观察的。
* 点击change id可以触发UI刷新。
* 点击change Info，将this.message重新赋值为不可观察数据后，再次点击change id，无法触发UI刷新。
* 再次点击change Info1，将this.message重新赋值为可观察数据，再次点击change id，可以触发UI刷新。

```
1. import { UIUtils } from '@kit.ArkUI';
2. class Info {
3. public id: number = 0;
4. constructor(id: number) {
5. this.id = id;
6. }
7. }
8. @Entry
9. @ComponentV2
10. struct Page2 {
11. // message初始化为makeObserved的返回值，具有深度观察能力
12. @Local message: Info = UIUtils.makeObserved(new Info(20));
13. build() {
14. Column() {
15. Button(`change id`).onClick(() => {
16. this.message.id++;
17. })
18. Button(`change Info ${this.message.id}`).onClick(() => {
19. this.message = new Info(30);
20. })
21. Button(`change Info1 ${this.message.id}`).onClick(() => {
22. this.message = UIUtils.makeObserved(new Info(30));
23. })
24. }
25. }
26. }
```

## 支持类型和观察变化

### 支持类型

* 支持未被[@Observed](arkts-observed-and-objectlink.md)或[@ObservedV2](arkts-new-observedv2-and-trace.md)装饰的类。
* 支持Array、Map、Set和Date。
* 支持[collections.Array](../harmonyos-references/arkts-apis-arkts-collections-array.md), [collections.Set](../harmonyos-references/arkts-apis-arkts-collections-set.md)和[collections.Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)。
* JSON.parse返回的Object。
* @Sendable装饰的类。

### 观察变化

* makeObserved传入内置类型或collections类型的实例时，可以观测其API带来的变化：

  | 类型 | 可观测变化的API |
  | --- | --- |
  | Array | push、pop、shift、unshift、splice、copyWithin、fill、reverse、sort |
  | collections.Array | push、pop、shift、unshift、splice、fill、reverse、sort、shrinkTo、extendTo |
  | Map/collections.Map | set、clear、delete |
  | Set/collections.Set | add、clear、delete |
  | Date | setFullYear、setMonth、setDate、setHours、setMinutes、setSeconds、setMilliseconds、setTime、setUTCFullYear、setUTCMonth、setUTCDate、setUTCHours、setUTCMinutes、setUTCSeconds、setUTCMilliseconds |

## 使用场景

### makeObserved和@Sendable装饰的class配合使用

[@Sendable](arkts-sendable.md)主要是为了处理应用场景中的并发任务。将makeObserved和@Sendable配合使用，可以满足一般应用开发中，在子线程做大数据处理，在UI线程做ViewModel的显示和观察数据的需求。@Sendable具体内容可参考[并发任务文档](multi-thread-concurrency-overview.md)。

本章节将说明下面的场景：

* makeObserved在传入@Sendable类型的数据后有观察能力，且其变化可以触发UI刷新。
* 从子线程中获取一个整体数据，然后对UI线程的可观察数据做整体替换。
* 从子线程获取的数据重新执行makeObserved，将数据变为可观察数据。
* 将数据从主线程传递回子线程时，仅传递不可观察的数据。makeObserved的返回值不可直接传给子线程。

例子如下：

```
1. @Sendable
2. export class SendableData  {
3. public name: string = 'Tom';
4. public age: number = 20;
5. public gender: number = 1;
6. // ....更多其他属性
7. public likes: number = 1;
8. public follow: boolean = false;
9. }
```

[modelView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/Model/modelView.ets#L15-L25)

```
1. import { taskpool } from '@kit.ArkTS';
2. import { SendableData } from '../Model/modelView';
3. import { UIUtils } from '@kit.ArkUI';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Concurrent
7. function threadGetData(param: string): SendableData {
8. const DOMAIN = 0xF811;
9. const TAG = '[Sample_MakeObserved]';
10. // 在子线程处理数据
11. let ret = new SendableData();
12. hilog.info(DOMAIN, TAG, `Concurrent threadGetData, param ${param}`);
13. ret.name = param + '-o';
14. ret.age = Math.floor(Math.random() * 40);
15. ret.likes = Math.floor(Math.random() * 100);
16. return ret;
17. }

19. @Entry
20. @ComponentV2
21. struct Page3 {
22. // 通过makeObserved给普通对象或是SendableData对象添加可观察能力
23. @Local send: SendableData = UIUtils.makeObserved(new SendableData());

25. build() {
26. Column() {
27. Text(this.send.name)
28. Button('change name').onClick(() => {
29. // ok 可以观察到属性的改变
30. this.send.name += '0';
31. })

33. Button('task').onClick(() => {
34. // 将待执行的函数放入taskpool内部任务队列等待，等待分发到工作线程执行。
35. taskpool.execute(threadGetData, this.send.name).then(val => {
36. // 和@Local一起使用，可以观察this.send的变化
37. this.send = UIUtils.makeObserved(val as SendableData);
38. })
39. })
40. }
41. }
42. }
```

需要注意：数据的构建和处理可以在子线程中完成，但有观察能力的数据不能传给子线程，只有在主线程里才可以操作可观察的数据。所以上述例子中只是将this.send的属性name传给子线程操作。

### makeObserved和collections.Array/Set/Map配合使用

collections提供ArkTS容器集，可用于并发场景下的高性能数据传递。详情见[@arkts.collections (ArkTS容器集)](../harmonyos-references/arkts-apis-arkts-collections.md)相关文档。

makeObserved可以在ArkUI中导入可观察的collections容器，但makeObserved不能和状态管理V1的状态变量装饰器如@State和[@Prop](arkts-prop.md)等配合使用，否则会抛出运行时异常。

**collections.Array**

collections.Array可以触发UI刷新的API有：

* 改变数组长度：push、pop、shift、unshift、splice、shrinkTo、extendTo
* 改变数组项本身：sort、fill

其他API不会改变原始数组，所以不会触发UI刷新。

```
1. import { collections } from '@kit.ArkTS';
2. import { UIUtils } from '@kit.ArkUI';

4. @Sendable
5. class Info {
6. public id: number = 0;
7. public name: string = 'cc';

9. constructor(id: number) {
10. this.id = id;
11. }
12. }

15. @Entry
16. @ComponentV2
17. struct Page4 {
18. scroller: Scroller = new Scroller();
19. @Local arrCollect: collections.Array<Info> =
20. UIUtils.makeObserved(new collections.Array<Info>(new Info(1), new Info(2)));

22. build() {
23. Column() {
24. // ForEach接口仅支持Array<any>，不支持collections.Array<any>。
25. // 但ForEach的实现用到的Array的API，collections.Array都有提供。所以可以使用as类型断言Array。
26. // 需要注意断言并不会改变原本的数据类型。
27. ForEach(this.arrCollect as object as Array<Info>, (item: Info) => {
28. Text(`${item.id}`)
29. .margin(5)
30. .onClick(() => {
31. item.id++;
32. })
33. }, (item: Info, index) => item.id.toString() + index.toString())
34. Divider()
35. .color('blue')
36. .margin(5)
37. if (this.arrCollect.length > 0) {
38. Text(`the first one ${this.arrCollect[0].id}`)
39. .margin(5)
40. Text(`the last one ${this.arrCollect[this.arrCollect.length - 1].id}`)
41. .margin(5)
42. }
43. Divider()
44. .color('blue')
45. .margin(5)

47. // 改变数据长度的API
48. Scroll(this.scroller) {
49. Column({ space: 10 }) {
50. // push: 新增新元素
51. Button('push')
52. .width('50%')
53. .onClick(() => {
54. this.arrCollect.push(new Info(30));
55. })
56. // pop: 删除最后一个
57. Button('pop')
58. .width('50%')
59. .onClick(() => {
60. this.arrCollect.pop();
61. })
62. // shift: 删除第一个
63. Button('shift')
64. .width('50%')
65. .onClick(() => {
66. this.arrCollect.shift();
67. })
68. // unshift: 在数组的开头插入新项
69. Button('unshift')
70. .width('50%')
71. .onClick(() => {
72. this.arrCollect.unshift(new Info(50));
73. })
74. // splice: 从数组的指定位置删除元素
75. Button('splice')
76. .width('50%')
77. .onClick(() => {
78. this.arrCollect.splice(1);
79. })

81. // shrinkTo: 将数组长度缩小到给定的长度
82. Button('shrinkTo')
83. .width('50%')
84. .onClick(() => {
85. this.arrCollect.shrinkTo(1);
86. })
87. // extendTo: 将数组长度扩展到给定的长度
88. Button('extendTo')
89. .width('50%')
90. .onClick(() => {
91. this.arrCollect.extendTo(6, new Info(20));
92. })

94. Divider()
95. .color('blue')

97. // 改变数组item本身
98. // sort：从大到小排序
99. Button('sort')
100. .width('50%')
101. .onClick(() => {
102. this.arrCollect.sort((a: Info, b: Info) => b.id - a.id);
103. })
104. // fill: 用值填充指定部分
105. Button('fill')
106. .width('50%')
107. .onClick(() => {
108. this.arrCollect.fill(new Info(5), 0, 2);
109. })

111. // 不会改变数组本身的API
112. // slice：返回新的数组，根据start end对原数组的拷贝，不会改变原数组，所以直接调用slice不会触发UI刷新
113. // 可以构建用例为返回的浅拷贝的数据赋值给this.arrCollect,需要注意这里依然要调用makeObserved，否则this.arrCollect被普通变量赋值后，会丧失观察能力
114. Button('slice')
115. .width('50%')
116. .onClick(() => {
117. this.arrCollect = UIUtils.makeObserved(this.arrCollect.slice(0, 1));
118. })
119. // map：原理同上
120. Button('map')
121. .width('50%')
122. .onClick(() => {
123. this.arrCollect = UIUtils.makeObserved(this.arrCollect.map((value) => {
124. value.id += 10;
125. return value;
126. }))
127. })
128. // filter：原理同上
129. Button('filter')
130. .width('50%')
131. .onClick(() => {
132. this.arrCollect = UIUtils.makeObserved(this.arrCollect.filter((value: Info) => value.id % 2 === 0));
133. })
134. // concat：原理同上
135. Button('concat')
136. .width('50%')
137. .onClick(() => {
138. let array1 = new collections.Array(new Info(100))
139. this.arrCollect = UIUtils.makeObserved(this.arrCollect.concat(array1));
140. })
141. }
142. .height('200%')
143. }
144. .height('100%')
145. }
146. .height('100%')
147. .width('100%')
148. }
149. }
```

[Page4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page4.ets#L15-L167)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/G_WJ4-MyQmuOybwH_X5KaQ/zh-cn_image_0000002589243917.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052720Z&HW-CC-Expire=86400&HW-CC-Sign=B7A7715AE9B9F8FE408AFCEF597A6EAFDEB58A253C886FE97AC09429086C0C38)

**collections.Map**

collections.Map可以触发UI刷新的API有：set、clear、delete。

```
1. import { collections } from '@kit.ArkTS';
2. import { UIUtils } from '@kit.ArkUI';

4. @Sendable
5. class Info {
6. public id: number = 0;

8. constructor(id: number) {
9. this.id = id;
10. }
11. }

14. @Entry
15. @ComponentV2
16. struct Page5 {
17. mapCollect: collections.Map<string, Info> =
18. UIUtils.makeObserved(new collections.Map<string, Info>([['a', new Info(10)], ['b', new Info(20)]]));

20. build() {
21. Column() {
22. // this.mapCollect.keys()返回迭代器。Foreach不支持迭代器，所以要Array.from浅拷贝生成数据。
23. ForEach(Array.from(this.mapCollect.keys()), (item: string) => {
24. Text(`${this.mapCollect.get(item)?.id}`)
25. .margin(5)
26. .onClick(() => {
27. let value: Info | undefined = this.mapCollect.get(item);
28. if (value) {
29. value.id++;
30. }
31. })
32. }, (item: string, index) => item + index.toString())

34. // set c
35. Button('set c')
36. .width('50%')
37. .margin(5)
38. .onClick(() => {
39. this.mapCollect.set('c', new Info(30));
40. })
41. // delete c
42. Button('delete c')
43. .width('50%')
44. .margin(5)
45. .onClick(() => {
46. if (this.mapCollect.has('c')) {
47. this.mapCollect.delete('c');
48. }
49. })
50. // clear
51. Button('clear')
52. .width('50%')
53. .margin(5)
54. .onClick(() => {
55. this.mapCollect.clear();
56. })
57. }
58. .height('100%')
59. .width('100%')
60. }
61. }
```

[Page5.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page5.ets#L15-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/5hK686PARh-KcGGYM_dnDA/zh-cn_image_0000002558764110.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052720Z&HW-CC-Expire=86400&HW-CC-Sign=DC84FA4433471D53942FCEA3F7002289F332ADFFBFBB9F32AEE8F0F437A0CE1E)

**collections.Set**

collections.Set可以触发UI刷新的API有：add、clear、delete。

```
1. import { collections } from '@kit.ArkTS';
2. import { UIUtils } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0xF811;
6. const TAG = '[Sample_MakeObserved]';

8. @Sendable
9. class Info {
10. public id: number = 0;

12. constructor(id: number) {
13. this.id = id;
14. }
15. }

18. @Entry
19. @ComponentV2
20. struct Page6 {
21. set: collections.Set<Info> = UIUtils.makeObserved(new collections.Set<Info>([new Info(10), new Info(20)]));

23. build() {
24. Column() {
25. // 因为ForEach不支持迭代器，所以需要使用Array.from浅拷贝生成数组。
26. // 但是浅拷贝生成的新的数组没有观察能力，为了ForEach组件在访问item的时候是可观察的数据，所以需要重新调用makeObserved。
27. ForEach((UIUtils.makeObserved(Array.from(this.set.values()))), (item: Info) => {
28. Text(`${item.id}`)
29. .margin(5)
30. .onClick(() => {
31. item.id++;
32. })
33. }, (item: Info, index) => item.id + index.toString())

35. Button('add')
36. .margin(5)
37. .width('50%')
38. .onClick(() => {
39. this.set.add(new Info(30));
40. hilog.info(DOMAIN, TAG, ('size:' + this.set.size));
41. })
42. Button('delete')
43. .margin(5)
44. .width('50%')
45. .onClick(() => {
46. let iterator = this.set.keys();
47. this.set.delete(iterator.next().value);
48. })
49. Button('clear')
50. .margin(5)
51. .width('50%')
52. .onClick(() => {
53. this.set.clear();
54. })
55. }
56. .height('100%')
57. .width('100%')
58. }
59. }
```

[Page6.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page6.ets#L15-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8_0P4sggTTml3gtUmnVzNQ/zh-cn_image_0000002558604454.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052720Z&HW-CC-Expire=86400&HW-CC-Sign=627BD2F82EAA966592F6A1EC91819D6D341D6F5C6F20ACBD7690F771C3DD854C)

### makeObserved的入参为JSON.parse的返回值

JSON.parse返回Object，无法使用@Trace装饰其属性，可以使用makeObserved使其变为可观察数据。

```
1. import { JSON } from '@kit.ArkTS';
2. import { UIUtils } from '@kit.ArkUI';

4. class Info {
5. public id: number = 0;

7. constructor(id: number) {
8. this.id = id;
9. }
10. }

12. let test: Record<string, number> = { 'a': 123 };
13. let testJsonStr: string = JSON.stringify(test);
14. let test2: Record<string, Info> = { 'a': new Info(20) };
15. let test2JsonStr: string = JSON.stringify(test2);

17. @Entry
18. @ComponentV2
19. struct Page7 {
20. // JSON.parse返回的Object用makeObserved转为可观察数据
21. message: Record<string, number> =
22. UIUtils.makeObserved<Record<string, number>>(JSON.parse(testJsonStr) as Record<string, number>);
23. message2: Record<string, Info> =
24. UIUtils.makeObserved<Record<string, Info>>(JSON.parse(test2JsonStr) as Record<string, Info>);

26. build() {
27. Column() {
28. Text(`${this.message.a}`)
29. .id('textId1')
30. .fontSize(50)
31. .onClick(() => {
32. this.message.a++;
33. })
34. Text(`${this.message2.a.id}`)
35. .id('textId2')
36. .fontSize(50)
37. .onClick(() => {
38. this.message2.a.id++;
39. })
40. }
41. .height('100%')
42. .width('100%')
43. }
44. }
```

[Page7.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page7.ets#L15-L59)

### makeObserved和V2装饰器配合使用

makeObserved可以和V2的装饰器一起使用。对于[@Monitor](arkts-new-monitor.md)和[@Computed](arkts-new-computed.md)，因为makeObserved传入@Observed或ObservedV2装饰的类实例会返回其自身，所以@Monitor或者@Computed不能定义在class中，只能定义在自定义组件里。

例子如下：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0xF811;
5. const TAG = '[Sample_MakeObserved]';

7. class Info {
8. public id: number = 0;
9. public age: number = 20;

11. constructor(id: number) {
12. this.id = id;
13. }
14. }

16. @Entry
17. @ComponentV2
18. struct Page8 {
19. @Local message: Info = UIUtils.makeObserved(new Info(20));

21. // 当message.id发生变化时，触发该函数调用
22. @Monitor('message.id')
23. onStrChange(monitor: IMonitor) {
24. hilog.info(DOMAIN, TAG, `name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
25. }

27. // 当message.id和message.age发生变化，需要重新计算时，触发该函数调用
28. @Computed
29. get ageId() {
30. hilog.info(DOMAIN, TAG, '---------Computed----------');
31. return this.message.id + ' ' + this.message.age;
32. }

34. build() {
35. Column() {
36. Text(`id: ${this.message.id}`)
37. .id('textIdMessage')
38. .fontSize(30)
39. .margin(5)
40. .onClick(() => {
41. this.message.id++;
42. })
43. Text(`age: ${this.message.age}`)
44. .id('textAgeMessageAge')
45. .fontSize(30)
46. .margin(5)
47. .onClick(() => {
48. this.message.age++;
49. })
50. Text(`Computed age + id: ${this.ageId}`)
51. .fontSize(30)
52. .margin(5)
53. Button('change Info')
54. .id('buttonChangeInfo')
55. .fontSize(30)
56. .margin(5)
57. .onClick(() => {
58. // 返回类实例本身，并赋值给message，触发@Computed和@Monitor
59. this.message = UIUtils.makeObserved(new Info(200));
60. })
61. Child({ message: this.message })
62. }
63. .height('100%')
64. .width('100%')
65. }
66. }

68. @ComponentV2
69. struct Child {
70. @Param @Require message: Info;

72. build() {
73. Text(`Child id: ${this.message.id}`)
74. .fontSize(30)
75. .margin(5)
76. }
77. }
```

[Page8.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page8.ets#L15-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/DS8iqAjCTlGN3qgdcqy17w/zh-cn_image_0000002589323979.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052720Z&HW-CC-Expire=86400&HW-CC-Sign=821B0CA9FC6807884D1E995591E1645D3D2B782820B3556CDD17757D6451317B)

### makeObserved在@Component内使用

makeObserved不能和V1的状态变量装饰器一起使用，但可以在@Component装饰的自定义组件里使用。

```
1. import { UIUtils } from '@kit.ArkUI';
2. class Info {
3. public id: number = 0;

5. constructor(id: number) {
6. this.id = id;
7. }
8. }

11. @Entry
12. @Component
13. struct Page9 {
14. // 如果和@State一起使用会抛出运行时异常
15. message: Info = UIUtils.makeObserved(new Info(20));

17. build() {
18. RelativeContainer() {
19. Text(`${this.message.id}`)
20. .id('textNumber')
21. .onClick(() => {
22. this.message.id++;
23. })
24. }
25. .height('100%')
26. .width('100%')
27. }
28. }
```

[Page9.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MakeObserved/entry/src/main/ets/View/Page9.ets#L15-L44)

## 常见问题

### getTarget后的数据可以正常赋值，但是无法触发UI刷新

[getTarget](arkts-new-gettarget.md)可以获取状态管理框架代理前的原始对象。

makeObserved封装的观察对象，可以通过getTarget获取到其原始对象，对原始对象的赋值不会触发UI刷新。

如下面例子：

1. 先点击第一个Text组件，通过getTarget获取其原始对象，此时修改原始对象的属性不会触发UI刷新，但数据会正常赋值。
2. 再点击第二个Text组件，此时修改this.observedObj的属性会触发UI刷新，Text显示21。

```
1. import { UIUtils } from '@kit.ArkUI';
2. class Info {
3. public id: number = 0;
4. }

6. @Entry
7. @Component
8. struct Page10 {
9. observedObj: Info = UIUtils.makeObserved(new Info());
10. build() {
11. Column() {
12. Text(`${this.observedObj.id}`)
13. .id('textobservedObj1')
14. .fontSize(50)
15. .onClick(() => {
16. // 通过getTarget获取其原始对象，将this.observedObj赋值为不可观察的数据
17. let rawObj: Info= UIUtils.getTarget(this.observedObj);
18. // 不会触发UI刷新，但数据会正常赋值
19. rawObj.id = 20;
20. })

22. Text(`${this.observedObj.id}`)
23. .id('textobservedObj2')
24. .fontSize(50)
25. .onClick(() => {
26. // 触发UI刷新，Text显示21
27. this.observedObj.id++;
28. })
29. }
30. }
31. }
```
