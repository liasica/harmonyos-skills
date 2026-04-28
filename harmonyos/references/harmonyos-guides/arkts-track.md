---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-track
title: @Track装饰器：class对象属性级更新
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e40b0b6e20cf5f2058629d4f04f242073124491d5c340434b8dd06403ef9f4d4
---

@Track应用于class对象的属性级更新。@Track装饰的属性变化时，只会触发该属性关联的UI更新。

在阅读本文档之前，建议开发者对状态管理基本观察能力有基本的了解。建议提前阅读：[@State](arkts-state.md)。

说明

从API version 11开始，该装饰器支持在ArkTS卡片中使用。

从API version 12开始，该装饰器支持在元服务中使用。

## 概述

@Track是class对象的属性装饰器。当一个class对象是状态变量时，@Track装饰的属性发生变化，只会触发该属性关联的UI更新；如果class类中使用了@Track装饰器，则未被@Track装饰器装饰的属性不能在UI中使用，如果使用，会发生运行时报错。

## class属性级更新说明

状态管理V1中@State等装饰器默认支持观察第一层属性的变化，第一层属性的变化虽然可以触发更新，但无法做到类属性级的观察，下面的例子就展示了这一限制：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN_NUMBER: number = 0XFF00;
3. const TAG: string = '[Sample_StateTrack]';
4. class Info {
5. public name: string = 'Jack';
6. public age: number = 12;
7. }

9. @Entry
10. @Component
11. struct Index {
12. @State info: Info = new Info();

14. // 借助getFontSize的日志打印，可以分辨哪个组件触发了渲染
15. getFontSize(id: number): number {
16. hilog.info(DOMAIN_NUMBER, TAG, `Component ${id} render`);
17. return 30;
18. }

20. build() {
21. Column() {
22. Text(`name: ${this.info.name}`)
23. .fontSize(this.getFontSize(1))
24. Text(`age: ${this.info.age}`)
25. .fontSize(this.getFontSize(2))

27. // 点击当前Button，可以发现当前虽然仅改变了name属性
28. // 但是依旧会触发两个Text的刷新
29. // Text(`age: ${this.info.age}`)是冗余刷新
30. Button('change name').onClick(() => {
31. this.info.name = 'Jane';
32. })

34. // 点击当前Button，可以发现当前虽然仅改变了age属性
35. // 但是依旧会触发两个Text的刷新
36. // Text(`name: ${this.info.name}`)是冗余刷新
37. Button('change age').onClick(() => {
38. this.info.age++;
39. })
40. }
41. .height('100%')
42. .width('100%')
43. }
44. }
```

[StateTrackClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateTrack/entry/src/main/ets/pages/stateTrack/StateTrackClass.ets#L15-L60)

说明

当UI刷新时，会执行组件的属性设置方法，利用这一机制可以通过观察getFontSize方法是否被调用来判断当前组件是否刷新。

* UI首次渲染完成，观察到输出如下日志：

  ```
  1. Component 1 render
  2. Component 2 render
  ```
* 当点击Button('change name')时，即使只修改了info.name，观察日志发现两个Text组件仍会重新渲染。组件Text(`age: ${this.info.age}`)并未使用name属性，但仍因为info.name的改变而刷新，因此这次刷新是冗余的。日志输出如下：

  ```
  1. Component 1 render
  2. Component 2 render
  ```
* 同理，点击Button('change age')，也会触发Text(`name: ${this.info.name}`)的刷新。日志输出如下：

  ```
  1. Component 1 render
  2. Component 2 render
  ```

造成上述冗余刷新的根本原因是：状态管理V1中@State等装饰器无法精准观察类属性的访问与变更。为了实现类对象属性的精准观察，引入@Track装饰器。

## 装饰器说明

| @Track变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无 |
| 可装饰的变量 | class对象的非静态成员属性。@Track不支持观察Function类型的数据变化，修改@Track装饰的Function类型的数据，UI不会刷新。 |

## 观察变化和行为表现

当一个class对象是状态变量时，@Track装饰的属性发生变化，该属性关联的UI触发更新。

说明

当class对象中没有一个属性被标记@Track，行为与原先保持不变。@Track没有深度观测的功能。

使用@Track装饰器可以避免冗余刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN_NUMBER: number = 0XFF00;
3. const TAG: string = '[Sample_StateTrack]';

5. class LogTrack {
6. @Track public str1: string;
7. @Track public str2: string;

9. constructor(str1: string) {
10. this.str1 = str1;
11. this.str2 = 'World';
12. }
13. }

15. class LogNotTrack {
16. public str1: string;
17. public str2: string;

19. constructor(str1: string) {
20. this.str1 = str1;
21. this.str2 = 'World';
22. }
23. }

25. @Entry
26. @Component
27. struct AddLog {
28. @State logTrack: LogTrack = new LogTrack('Hello');
29. @State logNotTrack: LogNotTrack = new LogNotTrack('Hello');

31. isRender(index: number) {
32. hilog.info(DOMAIN_NUMBER, TAG, `Text ${index} is rendered`);
33. return 50;
34. }

36. build() {
37. Row() {
38. Column() {
39. Text(this.logTrack.str1) // Text1
40. .id('str1')
41. .fontSize(this.isRender(1))
42. .fontWeight(FontWeight.Bold)
43. Text(this.logTrack.str2) // Text2
44. .fontSize(this.isRender(2))
45. .fontWeight(FontWeight.Bold)
46. Button('change logTrack.str1')
47. .id('str2')
48. .onClick(() => {
49. this.logTrack.str1 = 'Bye';
50. })
51. Text(this.logNotTrack.str1) // Text3
52. .fontSize(this.isRender(3))
53. .fontWeight(FontWeight.Bold)
54. Text(this.logNotTrack.str2) // Text4
55. .fontSize(this.isRender(4))
56. .fontWeight(FontWeight.Bold)
57. Button('change logNotTrack.str1')
58. .onClick(() => {
59. this.logNotTrack.str1 = 'Bye';
60. })
61. }
62. .width('100%')
63. }
64. .height('100%')
65. }
66. }
```

[StateTrackClass2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateTrack/entry/src/main/ets/pages/stateTrack/StateTrackClass2.ets#L15-L82)

在上面的示例中：

1. 类LogTrack中的属性均被@Track装饰器装饰，点击按钮"change logTrack.str1"，此时Text1刷新，Text2不刷新，只有一条日志输出，避免了冗余刷新。

   ```
   1. Text 1 is rendered
   ```
2. 类logNotTrack中的属性均未被@Track装饰器装饰，点击按钮"change logNotTrack.str1"，此时Text3、Text4均会刷新，有两条日志输出，存在冗余刷新。

   ```
   1. Text 3 is rendered
   2. Text 4 is rendered
   ```

## 限制条件

* 如果class类中使用了@Track装饰器，那么该class类中非@Track装饰的属性不能在@Component UI中使用，包括不能绑定在组件上、不能用于初始化子组件，错误的使用将导致运行时报错，从API version 23开始，将返回错误码[140110](../harmonyos-references/errorcode-statemanagement.md#section140110-在ui中使用非track装饰的属性发生运行时报错)，详见[在UI中使用非@Track装饰的属性发生运行时报错](arkts-track.md#在ui中使用非track装饰的属性发生运行时报错)；可以在非UI中使用非@Track装饰的属性，如事件回调函数中、生命周期函数中等。
* API version 19及以后，@Track使用在[@ComponentV2](arkts-create-custom-components.md#componentv2)的UI中，不会引起运行时报错，但依旧不会刷新，详见[@Observed+@Track装饰的class（V1->V2）](arkts-v1-v2-mixusage.md#传递class类型v1-v2)、[@Observed+@Track装饰的class（V2->V1）](arkts-v1-v2-mixusage.md#传递class类型v2-v1)。
* 建议开发者不要混用包含@Track的class对象和不包含@Track的class对象，如联合类型中、类继承中等，容易在UI中误用非@Track装饰的属性，导致运行时报错。

## 使用场景

### @Track和自定义组件更新

以下示例展示组件更新和@Track的处理步骤。对象log是@State装饰的状态变量，logInfo是@Track装饰的成员属性，其余成员属性都是非@Track装饰的，而且也不准备在UI中更新它们的值。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN_NUMBER: number = 0XFF00;
3. const TAG: string = '[Sample_StateTrack]';
4. class Log {
5. @Track public logInfo: string;
6. public owner: string;
7. public id: number;
8. public time: Date;
9. public location: string;
10. public reason: string;

12. constructor(logInfo: string) {
13. this.logInfo = logInfo;
14. this.owner = 'OH';
15. this.id = 0;
16. this.time = new Date();
17. this.location = 'CN';
18. this.reason = 'NULL';
19. }
20. }

22. @Entry
23. @Component
24. struct AddLog {
25. @State log: Log = new Log('origin info.');

27. build() {
28. Row() {
29. Column() {
30. Text(this.log.logInfo)
31. .fontSize(50)
32. .fontWeight(FontWeight.Bold)
33. .onClick(() => {
34. // 没有被@Track装饰的属性可以在点击事件中使用。
35. hilog.info(DOMAIN_NUMBER, TAG, 'owner: ' + this.log.owner +
36. ' id: ' + this.log.id +
37. ' time: ' + this.log.time +
38. ' location: ' + this.log.location +
39. ' reason: ' + this.log.reason);
40. this.log.time = new Date();
41. this.log.id++;
42. this.log.logInfo += ' info.';
43. })
44. }
45. .width('100%')
46. }
47. .height('100%')
48. }
49. }
```

[StateTrackClass3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StateTrack/entry/src/main/ets/pages/stateTrack/StateTrackClass3.ets#L15-L65)

处理步骤：

1. AddLog自定义组件的Text.onClick点击事件自增字符串' info.'。
2. 由于@State log变量的@Track属性logInfo更改，Text重新渲染。

## 常见问题

### 在UI中使用非@Track装饰的属性发生运行时报错

在UI中使用非@Track装饰的属性，运行时会报错，从API version 23开始，将返回错误码140110。需要给age也添加@Track装饰器。

```
1. class Person {
2. // id被@Track装饰
3. @Track id: number;
4. // age未被@Track装饰
5. age: number;

7. constructor(id: number, age: number) {
8. this.id = id;
9. this.age = age;
10. }
11. }

13. @Entry
14. @Component
15. struct Parent {
16. @State parent: Person = new Person(2, 30);

18. build() {
19. // 没有被@Track装饰的属性不可以在UI中使用，运行时会报错
20. Text(`Parent id is: ${this.parent.id} and Parent age is: ${this.parent.age}`)
21. }
22. }
```
