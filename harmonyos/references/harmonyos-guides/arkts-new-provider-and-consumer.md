---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-provider-and-consumer
title: @Provider装饰器和@Consumer装饰器：跨组件层级双向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Provider装饰器和@Consumer装饰器：跨组件层级双向同步
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:18+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5a6b10a65e4abbaf69c92613df6099aafcab363fbd1409e5460140d26c719a1b
---

@Provider和@Consumer用于跨组件层级数据双向同步，可以使得开发者不用拘泥于组件层级。

@Provider和@Consumer属于状态管理V2装饰器，所以只能在@ComponentV2中才能使用，在@Component中使用会编译报错。

@Provider和@Consumer提供了跨组件层级数据双向同步的能力。在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)。常见问题请参考[组件内状态变量常见问题](arkts-state-management-faq-inner-component.md)。

说明

@Provider和@Consumer装饰器从API version 12开始支持。

从API version 12开始，@Provider和@Consumer装饰器支持在元服务中使用。

从API version 23开始，通过配置[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)的[BuildOptions](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)参数enableProvideConsumeCrossing为true，使得@Provider和@Consumer支持跨[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)双向同步。在BuilderNode挂载到自定义组件节点树之后，@Consumer会重新获取最近的@Provider数据，与之建立双向同步关系。具体可见[@Consumer在跨BuilderNode场景下和@Provider建立双向同步](arkts-new-provider-and-consumer.md#consumer在跨buildernode场景下和provider建立双向同步过程)。

从API version 23开始，@Provider和@Consumer装饰器支持在ArkTS卡片中使用。

## 概述

@Provider，即数据提供方，其所有的子组件都可以通过@Consumer绑定相同的key来获取@Provider提供的数据。

@Consumer，即数据消费方，可以通过绑定同样的key获取其最近父节点的@Provider的数据，当查找不到@Provider的数据时，使用本地默认值。图示如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/pgeMax3wSMmcKF_qcPdxmA/zh-cn_image_0000002558764108.png?HW-CC-KV=V1&HW-CC-Date=20260429T052717Z&HW-CC-Expire=86400&HW-CC-Sign=421FCE7D2B38F44265544509E720EC67C428F27F3D1B9FCE65F41907438253AD)

@Provider和@Consumer装饰的数据类型需要一致。

开发者在使用@Provider和@Consumer时要注意：

* @Provider和@Consumer强依赖自定义组件层级，@Consumer会因为所在组件的父组件不同，而被初始化为不同的值。
* @Provider和@Consumer相当于把组件粘合在一起了，从组件独立角度考虑，应减少使用@Provider和@Consumer。

## @Provider和@Consumer vs @Provide和@Consume能力对比

在状态管理V1版本中，提供跨组件层级双向的装饰器为[@Provide和@Consume](arkts-provide-and-consume.md)，当前文档介绍的是状态管理V2装饰器@Provider和@Consumer。虽然两者名字和功能类似，但在特性上还存在一些差异。

如果开发者不了解状态管理V1中的@Provide和@Consume，可以直接跳过本节。

| 能力 | V2装饰器@Provider和@Consumer | V1装饰器@Provide和@Consume |
| --- | --- | --- |
| @Consume(r) | 必须本地初始化，当找不到@Provider时使用本地默认值。 | API version 20以前，@Consume禁止本地初始化，当找不到对应@Provide的时候，会抛出异常；从API version 20开始，@Consume支持设置默认值，如果没有设置默认值，且找不到对应@Provide时，会抛出异常。 |
| 支持类型 | 支持function。 | 不支持function。 |
| 观察能力 | 仅能观察自身赋值变化，如果要观察嵌套场景，配合[@Trace](arkts-new-observedv2-and-trace.md)一起使用。 | 观察第一层变化，如果要观察嵌套场景，配合[@Observed和@ObjectLink](arkts-observed-and-objectlink.md)一起使用。 |
| alias和属性名 | alias是唯一匹配的key，缺省时默认属性名为alias。 | alias和属性名都为key，优先匹配alias，匹配不到可以匹配属性名。 |
| @Provide(r) 从父组件初始化 | 不允许。 | 允许。 |
| @Provide(r)支持重载 | 默认开启，即@Provider可以重名，@Consumer向上查找最近的@Provider。 | 默认关闭，即在组件树上不允许有同名@Provide。如果需要重载，则需要配置allowOverride。 |

## 装饰器说明

### 基本规则

@Provider语法：

@Provider(aliasName?: string) varName : varType = initValue

| @Provider属性装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | aliasName?: string，别名，缺省时默认为属性名。 |
| 支持类型 | 自定义组件中成员变量。属性的类型可以为number、string、boolean、class、[Array](arkts-new-provider-and-consumer.md#装饰array类型变量)、[Date](arkts-new-provider-and-consumer.md#装饰date类型变量)、[Map](arkts-new-provider-and-consumer.md#装饰map类型变量)、[Set](arkts-new-provider-and-consumer.md#装饰set类型变量)等类型。支持装饰[箭头函数](arkts-new-provider-and-consumer.md#provider和consumer装饰回调事件用于组件之间完成行为抽象)。 |
| 从父组件初始化 | 禁止。 |
| 本地初始化 | 必须本地初始化。 |
| 观察能力 | 能力等同于@Trace。变化会同步给对应的@Consumer。 |

@Consumer语法：

@Consumer(aliasName?: string) varName : varType = initValue

| @Consumer属性装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | aliasName?: string，别名，缺省时默认为属性名，向上查找最近的@Provider。 |
| 可装饰的变量 | 自定义组件中成员变量。属性的类型可以为number、string、boolean、class、Array、Date、Map、Set等类型。支持装饰箭头函数。 |
| 从父组件初始化 | 禁止。 |
| 本地初始化 | 必须本地初始化。 |
| 观察能力 | 能力等同于@Trace。变化会同步给对应的@Provider。 |

### aliasName和属性名

@Provider和@Consumer接受可选参数aliasName，没有配置参数时，使用属性名作为默认的aliasName。

说明

aliasName是用于@Provider和@Consumer进行匹配的唯一指定key。

以下三个例子可清楚介绍@Provider和@Consumer如何使用aliasName进行查找匹配。

```
1. @ComponentV2
2. struct Parent {
3. // 未定义aliasName, 使用属性名'str'作为aliasName
4. @Provider() str: string = 'hello';
5. }

7. @ComponentV2
8. struct Child {
9. // 定义aliasName为'str'，使用aliasName去寻找
10. // 能够在Parent组件上找到, 使用@Provider的值'hello'
11. @Consumer('str') str: string = 'world';
12. }
```

```
1. @ComponentV2
2. struct Parent {
3. // 定义aliasName为'alias'
4. @Provider('alias') str: string = 'hello';
5. }

7. @ComponentV2
8. struct Child {
9. // 定义aliasName为 'alias'，找到@Provider并获得值'hello'
10. @Consumer('alias') str: string = 'world';
11. }
```

```
1. @ComponentV2
2. struct Parent {
3. // 定义aliasName为'alias'
4. @Provider('alias') str: string = 'hello';
5. }

7. @ComponentV2
8. struct Child {
9. // 未定义aliasName，使用属性名'str'作为aliasName
10. // 没有找到对应的@Provider，使用本地值'world'
11. @Consumer() str: string = 'world';
12. }
```

## 变量传递

| 传递规则 | 说明 |
| --- | --- |
| 从父组件初始化 | @Provider和@Consumer装饰的变量仅允许本地初始化，不允许从外部传入初始化。 |
| 初始化子组件 | @Provider和@Consumer装饰的变量可以初始化子组件中@Param装饰的变量。 |

## 使用限制

1. @Provider和@Consumer为自定义组件的属性装饰器，只能装饰自定义组件内的属性，不能装饰class的属性。
2. @Provider和@Consumer为状态管理V2装饰器，只能在@ComponentV2中使用，不能在@Component中使用。
3. @Provider和@Consumer只支持本地初始化，不支持外部传入初始化。

## 使用场景

### @Provider和@Consumer双向同步

**建立双向绑定**

1. 自定义组件Parent和Child初始化：
   * Child中@Consumer() str: string = 'world'向上查找，查找到Parent中声明的@Provider() str: string = 'hello'。
   * @Consumer() str: string = 'world'初始化为其查找到的@Provider的值，即'hello'。
   * 两者建立双向同步关系。
2. 点击Parent中的按钮，改变@Provider装饰的str，通知其对应的@Consumer，对应UI刷新。
3. 点击Child中的按钮，改变@Consumer装饰的str，通知其对应的@Provider，对应UI刷新。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() str: string = 'hello';

6. build() {
7. Column() {
8. Button(this.str)
9. .onClick(() => {
10. this.str += '0';
11. })
12. Child()
13. }
14. }
15. }

17. @ComponentV2
18. struct Child {
19. // @Consumer装饰的属性str和Parent组件中@Provider装饰的属性str名称相同，因此建立了双向绑定关系
20. @Consumer() str: string = 'world';

22. build() {
23. Column() {
24. Button(this.str)
25. .onClick(() => {
26. this.str += '0';
27. })
28. }
29. }
30. }
```

[TwowayBinding.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/TwowayBinding.ets#L16-L47)

**未建立双向绑定**

下面的例子中，@Provider和@Consumer由于aliasName值不同，无法建立双向同步关系。

1. 自定义组件Parent和Child初始化：
   * Child中@Consumer() str: string = 'world'向上查找，未查找到其数据提供方@Provider。
   * @Consumer() str: string = 'world'使用其本地默认值为'world'。
   * 两者未建立双向同步关系。
2. 点击Parent中的按钮，改变@Provider装饰的str1，仅刷新@Provider关联的Button组件。
3. 点击Child中的按钮，改变@Consumer装饰的str，仅刷新@Consumer关联的Button组件。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() str1: string = 'hello';

6. build() {
7. Column() {
8. Button(this.str1)
9. .onClick(() => {
10. this.str1 += '0';
11. })
12. Child()
13. }
14. }
15. }

17. @ComponentV2
18. struct Child {
19. // @Consumer装饰的属性str和Parent组件中@Provider装饰的属性str1名称不同，无法建立双向绑定关系
20. @Consumer() str: string = 'world';

22. build() {
23. Column() {
24. Button(this.str)
25. .onClick(() => {
26. this.str += '0';
27. })
28. }
29. }
30. }
```

[NoTwowayBinding.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/NoTwowayBinding.ets#L16-L47)

### 装饰Array类型变量

当装饰的对象是Array时，可以观察到Array整体的赋值，同时可以通过调用Array的接口push, pop, shift, unshift, splice, copyWithin, fill, reverse, sort更新Array中的数据。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() count: number[] = [1, 2, 3];

6. build() {
7. Row() {
8. Column() {
9. ForEach(this.count, (item: number) => {
10. Text(`parent: ${item}`).fontSize(30)
11. Divider()
12. })
13. // count被@Provider装饰，可以被观察到Array整体的赋值以及调用Array接口带来的变化
14. Button('push').onClick(() => {
15. this.count.push(111);
16. })
17. Button('reverse').onClick(() => {
18. this.count.reverse();
19. })
20. Button('fill').onClick(() => {
21. this.count.fill(6);
22. })
23. Child()
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }

31. @ComponentV2
32. struct Child {
33. @Consumer() count: number[] = [9, 8, 7];

35. build() {
36. Column() {
37. ForEach(this.count, (item: number) => {
38. Text(`child: ${item}`).fontSize(30)
39. Divider()
40. })
41. // count被@Consumer装饰，可以被观察到Array整体的赋值以及调用Array接口带来的变化
42. Button('push').onClick(() => {
43. this.count.push(222);
44. })
45. Button('reverse').onClick(() => {
46. this.count.reverse();
47. })
48. Button('fill').onClick(() => {
49. this.count.fill(8);
50. })
51. }
52. .width('100%')
53. }
54. }
```

[DecorativeArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeArray.ets#L16-L69)

### 装饰Date类型变量

当装饰Date类型变量时，可以观察到数据源对Date整体的赋值，以及调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds带来的变化。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() selectedDate: Date = new Date('2021-08-08');

6. build() {
7. Column() {
8. Text(`parent: ${this.selectedDate}`)
9. // selectedDate被@Provider装饰，可以被观察到Date整体的赋值以及调用Date接口带来的变化
10. Button('update the new date')
11. .onClick(() => {
12. this.selectedDate = new Date('2023-07-07');
13. })
14. Button('increase the year by 1')
15. .onClick(() => {
16. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
17. })
18. Button('increase the month by 1')
19. .onClick(() => {
20. this.selectedDate.setMonth(this.selectedDate.getMonth() + 1);
21. })
22. Button('increase the day by 1')
23. .onClick(() => {
24. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
25. })
26. Child()
27. }
28. }
29. }

31. @ComponentV2
32. struct Child {
33. @Consumer() selectedDate: Date = new Date('2022-07-07');

35. build() {
36. Column() {
37. Text(`child: ${this.selectedDate}`)
38. // selectedDate被@Consumer装饰，可以被观察到Date整体的赋值以及调用Date接口带来的变化
39. Button('update the new date')
40. .onClick(() => {
41. this.selectedDate = new Date('2025-01-01');
42. })
43. Button('increase the year by 1')
44. .onClick(() => {
45. this.selectedDate.setFullYear(this.selectedDate.getFullYear() + 1);
46. })
47. Button('increase the month by 1')
48. .onClick(() => {
49. this.selectedDate.setMonth(this.selectedDate.getMonth() + 1);
50. })
51. Button('increase the day by 1')
52. .onClick(() => {
53. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
54. })
55. }
56. }
57. }
```

[DecorativeDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeDate.ets#L16-L72)

### 装饰Map类型变量

当装饰Map类型变量时，可以观察到数据源对Map整体的赋值，以及调用Map的接口set, clear, delete带来的变化。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);

6. build() {
7. Column() {
8. Text('Parent').fontSize(30)
9. ForEach(Array.from(this.message.entries()), (item: [number, string]) => {
10. Text(`${item[0]}`).fontSize(30)
11. Text(`${item[1]}`).fontSize(30)
12. Divider()
13. })
14. // message被@Provider装饰，可以被观察到Map整体的赋值以及调用Map接口带来的变化
15. Button('init map').onClick(() => {
16. this.message = new Map([[0, 'aa'], [1, 'bb'], [3, 'cc']]);
17. })
18. Button('set new one').onClick(() => {
19. this.message.set(4, 'd');
20. })
21. Button('clear').onClick(() => {
22. this.message.clear();
23. })
24. Button('replace the first one').onClick(() => {
25. this.message.set(0, 'a~');
26. })
27. Button('delete the first one').onClick(() => {
28. this.message.delete(0);
29. })
30. Child()
31. }
32. }
33. }

35. @ComponentV2
36. struct Child {
37. @Consumer() message: Map<number, string> = new Map([[0, 'd'], [1, 'e'], [3, 'f']]);

39. build() {
40. Column() {
41. Text('Child').fontSize(30)
42. ForEach(Array.from(this.message.entries()), (item: [number, string]) => {
43. Text(`${item[0]}`).fontSize(30)
44. Text(`${item[1]}`).fontSize(30)
45. Divider()
46. })
47. // message被@Consumer装饰，可以被观察到Map整体的赋值以及调用Map接口带来的变化
48. Button('init map').onClick(() => {
49. this.message = new Map([[0, 'dd'], [1, 'ee'], [3, 'ff']]);
50. })
51. Button('set new one').onClick(() => {
52. this.message.set(4, 'g');
53. })
54. Button('clear').onClick(() => {
55. this.message.clear();
56. })
57. Button('replace the first one').onClick(() => {
58. this.message.set(0, 'a*');
59. })
60. Button('delete the first one').onClick(() => {
61. this.message.delete(0);
62. })
63. }
64. }
65. }
```

[DecorativeMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeMap.ets#L16-L80)

### 装饰Set类型变量

当装饰Set类型变量时，可以观察到数据源对Set整体的赋值，以及调用Set的接口 add, clear, delete带来的变化。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Provider() message: Set<number> = new Set([1, 2, 3, 4]);

6. build() {
7. Column() {
8. Text('Parent').fontSize(30)
9. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
10. Text(`${item[0]}`).fontSize(30)
11. Divider()
12. })
13. // message被@Provider装饰，可以被观察到Set整体的赋值以及调用Set接口带来的变化
14. Button('init set').onClick(() => {
15. this.message = new Set([1, 2, 3, 4]);
16. })
17. Button('set new one').onClick(() => {
18. this.message.add(5);
19. })
20. Button('clear').onClick(() => {
21. this.message.clear();
22. })
23. Button('delete the first one').onClick(() => {
24. this.message.delete(1);
25. })
26. Child()
27. }
28. }
29. }

31. @ComponentV2
32. struct Child {
33. @Consumer() message: Set<number> = new Set([1, 2, 3, 4, 5, 6]);

35. build() {
36. Column() {
37. Text('Child').fontSize(30)
38. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
39. Text(`${item[0]}`).fontSize(30)
40. Divider()
41. })
42. // message被@Consumer装饰，可以被观察到Set整体的赋值以及调用Set接口带来的变化
43. Button('init set').onClick(() => {
44. this.message = new Set([1, 2, 3, 4, 5, 6]);
45. })
46. Button('set new one').onClick(() => {
47. this.message.add(7);
48. })
49. Button('clear').onClick(() => {
50. this.message.clear();
51. })
52. Button('delete the first one').onClick(() => {
53. this.message.delete(1);
54. })
55. }
56. }
57. }
```

[DecorativeSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeSet.ets#L16-L72)

### @Provider和@Consumer装饰回调事件用于组件之间完成行为抽象

当需要在父组件中向子组件注册回调函数时，可以使用@Provider和@Consumer装饰回调方法来实现。

在拖拽场景中，若需将子组件的拖拽起始位置信息同步给父组件，可参考以下示例。

```
1. @Entry
2. @ComponentV2
3. struct Parent {
4. @Local childX: number = 0;
5. @Local childY: number = 1;
6. @Provider() onDrag: (x: number, y: number) => void = (x: number, y: number) => {
7. console.info(`onDrag event at x=${x} y:${y}`);
8. this.childX = x;
9. this.childY = y;
10. }

12. build() {
13. Column() {
14. Text(`child position x: ${this.childX}, y: ${this.childY}`)
15. Child()
16. }
17. }
18. }

20. @ComponentV2
21. struct Child {
22. @Consumer() onDrag: (x: number, y: number) => void = (x: number, y: number) => {};

24. build() {
25. Button('changed')
26. .draggable(true)
27. .onDragStart((event: DragEvent) => {
28. // 当前预览器上不支持通用拖拽事件
29. this.onDrag(event.getDisplayX(), event.getDisplayY());
30. })
31. }
32. }
```

[DragDrop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DragDrop.ets#L16-L49)

### @Provider和@Consumer装饰复杂类型，配合@Trace一起使用

1. @Provider和@Consumer只能观察到数据本身的变化。如果需要观察其装饰的复杂数据类型的属性变化，可以配合@Trace一起使用，也可以使用[makeObserved](arkts-new-makeobserved.md)将非可观察数据变为可观察数据。
2. 装饰内置类型：Array、Map、Set、Date时，可以观察到某些API的变化，观察能力同[@Trace](arkts-new-observedv2-and-trace.md#观察变化)。

```
1. @ObservedV2
2. class User {
3. // 复杂数据类型的属性被@Trace装饰，可以被观察到属性变化
4. @Trace public name: string;
5. @Trace public age: number;

7. constructor(name: string, age: number) {
8. this.name = name;
9. this.age = age;
10. }
11. }
12. const data: User[] = [new User('Json', 10), new User('Eric', 15)];
13. @Entry
14. @ComponentV2
15. struct Parent {
16. @Provider('data') users: User[] = data;

18. build() {
19. Column() {
20. Child()
21. Button('add new user')
22. .onClick(() => {
23. this.users.push(new User('Molly', 18));
24. })
25. Button('age++')
26. .onClick(() => {
27. this.users[0].age++;
28. })
29. Button('change name')
30. .onClick(() => {
31. this.users[0].name = 'Shelly';
32. })
33. }
34. }
35. }

37. @ComponentV2
38. struct Child {
39. @Consumer('data') users: User[] = [];

41. build() {
42. Column() {
43. ForEach(this.users, (item: User) => {
44. Column() {
45. Text(`name: ${item.name}`).fontSize(30)
46. Text(`age: ${item.age}`).fontSize(30)
47. Divider()
48. }
49. })
50. }
51. }
52. }
```

[DecorativeComplex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeComplex.ets#L16-L68)

### @Provider重名时，@Consumer向上查找其最近的@Provider

@Provider可以在组件树上重名，@Consumer会向上查找其最近父节点的@Provider的数据。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Provider() val: number = 10;

6. build() {
7. Column() {
8. Parent()
9. }
10. }
11. }

13. @ComponentV2
14. struct Parent {
15. @Provider() val: number = 20;
16. @Consumer('val') val2: number = 0; // 10

18. build() {
19. Column() {
20. Text(`${this.val2}`)
21. Child()
22. }
23. }
24. }

26. @ComponentV2
27. struct Child {
28. @Consumer() val: number = 0; // 20

30. build() {
31. Column() {
32. Text(`${this.val}`)
33. }
34. }
35. }
```

[ProviderSame.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/ProviderSame.ets#L16-L52)

上面的例子中：

* Parent中的@Consumer向上查找，查找到Index中定义的@Provider() val: number = 10，初始化为10。
* Child中的@Consumer向上查找，查找到Parent中定义的@Provider() val: number = 20后停止，初始化为20。

### @Provider和@Consumer初始化@Param

@Provider和@Consumer装饰的变量可以初始化子组件中@Param装饰的变量。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Provider() val: number = 10;

6. build() {
7. Column() {
8. Text(`Index @Provider val: ${this.val}`).fontSize(30)
9. // @Provider装饰的变量val可以初始化@Param装饰的变量val2
10. Parent({ val2: this.val })
11. }
12. }
13. }

15. @ComponentV2
16. struct Parent {
17. @Consumer() val: number = 0;
18. @Require @Param val2: number;

20. build() {
21. Column() {
22. Text(`Parent @Consumer val: ${this.val}`).fontSize(30)
23. Button('change val').onClick(() => {
24. this.val++;
25. })
26. Text(`Parent @Param val2: ${this.val2}`).fontSize(30)
27. // @Consumer装饰的变量val可以初始化@Param装饰的变量val
28. Child({ val: this.val })
29. }.border({ width: 2, color: Color.Green })
30. }
31. }

33. @ComponentV2
34. struct Child {
35. @Require @Param val: number;

37. build() {
38. Column() {
39. Text(`Child @Param val ${this.val}`).fontSize(30)
40. }.border({ width: 2, color: Color.Pink })
41. }
42. }
```

[DecorativeInitialized.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/DecorativeInitialized.ets#L16-L57)

上面的例子中：

* Index中@Provider装饰的变量val与Parent中@Consumer装饰的变量val建立双向数据绑定。Parent中@Param装饰的变量val2接收Index中数据源val的数据，并同步其变化。Child中@Param装饰的变量val接收Parent中数据源val的数据，并同步其变化。
* 点击Parent中的按钮，触发@Consumer() val的变化，变化同步给Index中的@Provider() val和Child中的@Param val，对应UI刷新。
* Index中@Provider() val的变化同步给Parent中的@Param val2，对应UI刷新。

### @Consumer在跨BuilderNode场景下和@Provider建立双向同步过程

说明

从API version 23开始，支持跨BuilderNode配对@Provider和@Consumer。

下面给出一个示例，实现如下功能：

1. BuilderNode通过[全局自定义构建函数](arkts-builder.md#全局自定义构建函数)构建组件树，组件树的根[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点可通过[getFrameNode](../harmonyos-references/js-apis-arkui-buildernode.md#getframenode)获取，该节点可直接由[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)返回并挂载于[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)节点下。
2. 挂载到自定义组件节点树时，BuilderNode会通过addBuilderNode方法挂载在自定义组件下，此时BuilderNode节点下的@Consumer会向上查找@Provider，根据key的匹配规则找到最近的@Provider后，会和@Provider建立双向同步关系。如果找不到配对的@Provider，则@Consumer仍使用默认值。
3. 建立双向同步的关系后，如果@Provider装饰变量的值和@Consumer的默认值不同，则会回调@Consumer的@Monitor方法，以及与@Consumer有同步关系的变量的@Monitor方法，例如：@Consumer通知其子组件中的@Param触发@Monitor方法。
4. BuilderNode从组件树卸载后，@Consumer会再次试图查找对应的@Provider，如果发现从组件树卸载后无法再找到之前配对的@Provider，则断开和@Provider的双向同步关系，@Consumer装饰的变量恢复成默认值。
5. @Consumer断开和@Provider的连接，恢复成默认值时，会判断@Consumer装饰变量的值相对于从@Provider变为@Consumer的默认值是否有变化，如果有变化，则会回调@Consumer的@Monitor方法以及与该@Consumer存在同步关系的变量的@Monitor方法。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. TestRemove()
6. }

8. let globalBuilderNode: BuilderNode<[]> | null = null;

10. class TextNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;
12. private uiContext: UIContext | null = null;

14. constructor() {
15. super();
16. }

18. makeNode(context: UIContext): FrameNode | null {
19. this.rootNode = new FrameNode(context);
20. this.uiContext = context;
21. return this.rootNode;
22. }

24. addBuilderNode(): void {
25. if (globalBuilderNode === null && this.uiContext) {
26. globalBuilderNode = new BuilderNode(this.uiContext);
27. // 构建BuilderNode，TestRemove作为子组件
28. globalBuilderNode.build(wrapBuilder<[]>(buildText), undefined, { enableProvideConsumeCrossing: true });
29. }
30. if (this.rootNode && globalBuilderNode) {
31. this.rootNode.appendChild(globalBuilderNode.getFrameNode());
32. }
33. }

35. removeBuilderNode(): void {
36. if (this.rootNode && globalBuilderNode) {
37. this.rootNode.removeChild(globalBuilderNode.getFrameNode());
38. }
39. }

41. disposeNode(): void {
42. if (this.rootNode && globalBuilderNode) {
43. globalBuilderNode.dispose();
44. }
45. }
46. }

48. @Entry
49. @ComponentV2
50. struct RemoChildDisconnectProvider {
51. @Provider() content: string = 'Index: hello world';
52. @Monitor('content')
53. providerWatch() {
54. console.info(`Provider change ${this.content}`);
55. }

57. controllerIndex: TextNodeController = new TextNodeController();

59. build() {
60. Column({ space: 8 }) {
61. Text(`Provider: ${this.content}`)

63. // 添加BuilderNode，@Consumer与@Provider建立双向同步
64. Button('add child')
65. .onClick(() => {
66. this.controllerIndex.addBuilderNode();
67. })

69. // 移除BuilderNode，@Consumer与@Provider断开连接，恢复默认值
70. Button('remove child')
71. .onClick(() => {
72. this.controllerIndex.removeBuilderNode();
73. })

75. // 释放BuilderNode的子节点TestRemove，随后该子节点销毁，触发子节点的aboutToDisappear回调
76. Button('dispose child')
77. .onClick(() => {
78. this.controllerIndex.disposeNode();
79. })

81. // @Provider/@Consumer双向同步更新
82. Button('change Provider')
83. .onClick(() => {
84. this.content += 'Pro';
85. })
86. NodeContainer(this.controllerIndex)
87. }
88. .width('100%')
89. .height('100%')
90. }
91. }

93. @ComponentV2
94. struct TestRemove {
95. @Consumer() content: string = 'default value';
96. @Monitor('content')
97. consumerWatch() {
98. console.info(`Consumer change ${this.content}`);
99. }

101. aboutToDisappear() {
102. console.info(`TestRemove aboutToDisappear`);
103. }

105. build() {
106. Column() {
107. Text('Consumer ' + this.content)

109. // @Provider和@Consumer绑定的Text组件刷新，并回调@Provider和@Consumer的@Monitor方法
110. Button('change cc')
111. .onClick(() => {
112. this.content += 'cc';
113. })
114. }
115. }
116. }
```

[BuilderNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ProviderConsumer/entry/src/main/ets/homePage/BuilderNode.ets#L15-L132)

上面的例子中：

* 点击add Child，TestRemove中@Consumer向上找到最近的RemoChildDisconnectProvider中的@Provider，将@Consumer从默认值更新为@Provider的值，并回调@Consumer的@Monitor方法。
* @Provider和@Consumer配对后，建立双向同步关系。点击change Provider和Text(change cc)，@Provider和@Consumer绑定的Text组件刷新，并回调@Provider和@Consumer的@Monitor方法。
* 点击remove Child，BuilderNode子节点从组件树卸载，TestRemove中的@Consumer和RemoChildDisconnectProvider中的@Provider断开连接，TestRemove中的@Consumer恢复成默认值，并回调@Consumer的@Monitor方法。
* 点击dispose Child，释放BuilderNode下的子节点TestRemove，随后该子节点销毁，执行aboutToDisappear回调。
