---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2
title: AppStorageV2: 应用全局UI状态存储
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理应用拥有的状态 > AppStorageV2: 应用全局UI状态存储
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e02b7a0a153e9e9951aecd7d2f3ea6d730972267d5fb65e7e5ee4c39280900bd
---

为了增强状态管理框架对应用全局UI状态变量的共享能力，开发者可以使用AppStorageV2存储应用全局UI的状态变量数据。

AppStorageV2提供应用级全局共享状态变量的能力，开发者可以通过connect绑定同一个key，进行跨ability的数据共享。

在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)，[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)，配合阅读：[AppStorageV2-API文档](../harmonyos-references/js-apis-statemanagement.md#appstoragev2)。

说明

AppStorageV2从API version 12开始支持。

## 概述

AppStorageV2是在应用UI启动时会被创建的单例。它用于提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorageV2将在应用运行过程保留其数据。数据通过唯一的键字符串值访问。需要注意的是，AppStorage与AppStorageV2之间的数据互不共享。

AppStorageV2可以修改connect的返回值，实现与UI组件的同步。

AppStorageV2支持应用的[主线程](thread-model-stage.md)内多个UIAbility实例间的状态共享。

## 使用说明

* connect：创建或获取存储的数据。

说明

1、若未指定key，使用第二个参数作为默认构造器；否则使用第三个参数作为默认构造器（第二个参数非法也使用第三个参数作为默认构造器）。

2、确保数据已经存储在AppStorageV2中，可省略默认构造器，获取存储的数据；否则必须指定默认构造器，不指定将导致应用异常。

3、同一个key，connect不同类型的数据会导致应用异常，应用需要确保类型匹配。

4、key建议使用有意义的值，可由字母、数字、下划线组成，长度不超过255，使用非法字符或空字符的行为是未定义的。

5、关联[@Observed](arkts-observed-and-objectlink.md)对象时，由于该类型的name属性未定义，需要指定key或者自定义name属性。

* remove：删除指定key的存储数据。

说明

删除AppStorageV2中不存在的key会报警告。

* keys：返回所有AppStorageV2中的key。

以上接口详细描述请参考状态管理API文档中的[AppStorageV2](../harmonyos-references/js-apis-statemanagement.md#appstoragev2)。

## 使用限制

1、只支持class类型，否则会抛出运行时报错，从API version 23开始，将返回错误码[140103](../harmonyos-references/errorcode-statemanagement.md#section140103-appstoragev2和persistencev2使用不支持的数据类型)。

2、需要配合UI使用（UI线程），不能在其他线程使用，如不支持[@Sendable](arkts-sendable.md)。

3、不支持[collections.Set](../harmonyos-references/arkts-apis-arkts-collections-set.md)、[collections.Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)等类型。

4、不支持非built-in类型，如[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)、NativePointer、[ArrayList](../harmonyos-references/js-apis-arraylist.md)等Native类型。

5、不支持存储基本类型，如string、number、boolean等。注意：不支持存储基本类型意味着connect接口传入的类型不能是基本类型，但connect传入的class中可以包含基本类型。

## 使用场景

### 使用AppStorageV2

AppStorageV2使用connect接口即可实现对AppStorageV2中数据的修改和同步，如果修改的数据被@Trace装饰，该数据的修改会同步更新UI。需要注意的是，使用remove接口只会将数据从AppStorageV2中删除，不影响组件中已创建的数据，详见以下示例代码：

```
1. import { AppStorageV2 } from '@kit.ArkUI';

3. @ObservedV2
4. class Message {
5. @Trace public userID: number;
6. public userName: string;

8. constructor(userID?: number, userName?: string) {
9. this.userID = userID ?? 1;
10. this.userName = userName ?? 'Jack';
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct Index {
17. // 使用connect在AppStorageV2中创建一个key为Message的对象
18. // 修改connect的返回值即可同步回AppStorageV2
19. @Local message: Message = AppStorageV2.connect<Message>(Message, () => new Message())!;

21. build() {
22. Column() {
23. // 修改@Trace装饰的类属性，UI能同步刷新
24. Button(`Index userID: ${this.message.userID}`)
25. .onClick(() => {
26. this.message.userID += 1;
27. })
28. // 修改非@Trace装饰的类属性，UI不会同步刷新，但修改的类属性已同步回AppStorageV2
29. Button(`Index userName: ${this.message.userName}`)
30. .onClick(() => {
31. this.message.userName += 'suf';
32. })
33. // remove key Message, 会从AppStorageV2中删除key为Message的对象
34. // remove之后，修改父组件的userId，子组件能同步变化，因为remove只是从AppStorageV2删除，不会影响组件中已存在的数据
35. Button('remove key: Message')
36. .onClick(() => {
37. AppStorageV2.remove<Message>(Message);
38. })
39. // connect key Message, 会从AppStorageV2中添加key为Message的对象
40. // remove之后，重新添加，修改父子组件的userID，可以发现数据已经不同步，子组件重新connect之后，数据一致
41. Button('connect key: Message')
42. .onClick(() => {
43. this.message = AppStorageV2.connect<Message>(Message, () => new Message(5, 'Rose'))!;
44. })
45. Divider()
46. Child()
47. }
48. .width('100%')
49. .height('100%')
50. }
51. }

53. @ComponentV2
54. struct Child {
55. // 使用connect在AppStorageV2中取出一个key为Message的对象，已在父组件中创建
56. @Local message: Message = AppStorageV2.connect<Message>(Message, () => new Message())!;
57. @Local name: string = this.message.userName;

59. build() {
60. Column() {
61. // 修改@Trace装饰的类属性，UI同步刷新，父组件能感知该变化
62. Button(`Child userID: ${this.message.userID}`)
63. .onClick(() => {
64. this.message.userID += 5;
65. })
66. // 修改父组件中的userName属性，点击name可以同步父组件的类属性修改
67. Button(`Child name: ${this.name}`)
68. .onClick(() => {
69. this.name = this.message.userName;
70. })
71. // remove key Message, 会从AppStorageV2中删除key为Message的对象
72. Button('remove key: Message')
73. .onClick(() => {
74. AppStorageV2.remove<Message>(Message);
75. })
76. // connect key Message, 会从AppStorageV2中添加key为Message的对象
77. Button('connect key: Message')
78. .onClick(() => {
79. this.message = AppStorageV2.connect<Message>(Message, () => new Message(10, 'Lucy'))!;
80. })
81. }
82. .width('100%')
83. .height('100%')
84. }
85. }
```

[AppStorageV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorageV2/entry/src/main/ets/pages/AppStorageV2.ets#L15-L103)

### 在两个页面之间存储数据

数据页面

```
1. // 数据中心
2. // Sample.ets
3. @ObservedV2
4. export class Sample {
5. @Trace public p1: number = 0;
6. public p2: number = 10;
7. }
```

[Sample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorageV2/entry/src/main/ets/pages/Sample.ets#L15-L23)

页面1

```
1. import { AppStorageV2 } from '@kit.ArkUI';
2. import { Sample } from './Sample';

4. @Entry
5. @ComponentV2
6. struct PageOne {
7. // 在AppStorageV2中创建一个key为Sample的键值对（如果存在，则返回AppStorageV2中的数据），并且和prop关联
8. @Local prop: Sample = AppStorageV2.connect(Sample, () => new Sample())!;
9. pageStack: NavPathStack = new NavPathStack();

11. build() {
12. Navigation(this.pageStack) {
13. Column() {
14. Button('Go to pageTwo')
15. .onClick(() => {
16. this.pageStack.pushPathByName('PageTwo', null);
17. })

19. Button('PageOne connect the key Sample')
20. .onClick(() => {
21. // 在AppStorageV2中创建一个key为Sample的键值对（如果存在，则返回AppStorageV2中的数据），并且和prop关联
22. this.prop = AppStorageV2.connect(Sample, 'Sample', () => new Sample())!;
23. })

25. Button('PageOne remove the key Sample')
26. .onClick(() => {
27. // 从AppStorageV2中删除后，prop将不会再与key为Sample的值关联
28. AppStorageV2.remove(Sample);
29. })

31. Text(`PageOne add 1 to prop.p1: ${this.prop.p1}`)
32. .fontSize(30)
33. .onClick(() => {
34. this.prop.p1++;
35. })

37. Text(`PageOne add 1 to prop.p2: ${this.prop.p2}`)
38. .fontSize(30)
39. .onClick(() => {
40. // 页面不刷新，但是p2的值改变了
41. this.prop.p2++;
42. })

44. // 获取当前AppStorageV2里面的所有key
45. Text(`all keys in AppStorage: ${AppStorageV2.keys()}`)
46. .fontSize(30)
47. }
48. }
49. }
50. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorageV2/entry/src/main/ets/pages/PageOne.ets#L15-L66)

页面2

```
1. import { AppStorageV2 } from '@kit.ArkUI';
2. import { Sample } from './Sample';

4. @Builder
5. export function PageTwoBuilder() {
6. PageTwo()
7. }

9. @ComponentV2
10. struct PageTwo {
11. // 在AppStorageV2中创建一个key为Sample的键值对（如果存在，则返回AppStorageV2中的数据），并且和prop关联
12. @Local prop: Sample = AppStorageV2.connect(Sample, () => new Sample())!;
13. pathStack: NavPathStack = new NavPathStack();

15. build() {
16. NavDestination() {
17. Column() {
18. Button('PageTwo connect the key Sample1')
19. .onClick(() => {
20. // 在AppStorageV2中创建一个key为Sample1的键值对（如果存在，则返回AppStorageV2中的数据），并且和prop关联
21. this.prop = AppStorageV2.connect(Sample, 'Sample1', () => new Sample())!;
22. })

24. Text(`PageTwo add 1 to prop.p1: ${this.prop.p1}`)
25. .fontSize(30)
26. .onClick(() => {
27. this.prop.p1++;
28. })

30. Text(`PageTwo add 1 to prop.p2: ${this.prop.p2}`)
31. .fontSize(30)
32. .onClick(() => {
33. // 页面不刷新，但是p2的值改变了；只有重新初始化才会改变
34. this.prop.p2++;
35. })

37. // 获取当前AppStorageV2里面的所有key
38. Text(`all keys in AppStorage: ${AppStorageV2.keys()}`)
39. .fontSize(30)
40. }
41. }
42. .onReady((context: NavDestinationContext) => {
43. this.pathStack = context.pathStack;
44. })
45. }
46. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/AppStorageV2/entry/src/main/ets/pages/PageTwo.ets#L15-L62)

使用Navigation时，需要添加配置系统路由表文件src/main/resources/base/profile/route\_map.json，并替换pageSourceFile为PageTwo页面的路径，并且在module.json5中添加："routerMap": "$profile:route\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "PageTwo",
5. "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
6. "buildFunction": "PageTwoBuilder",
7. "data": {
8. "description" : "AppStorageV2 example"
9. }
10. }
11. ]
12. }
```
