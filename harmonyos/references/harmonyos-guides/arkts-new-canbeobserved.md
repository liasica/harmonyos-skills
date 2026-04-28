---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-canbeobserved
title: canBeObserved接口：判断对象是否可被观察
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 辅助接口 > canBeObserved接口：判断对象是否可被观察
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:64dca6c4f980642527b4fdbb57b66e54989b7603c3f7b0cc60a48c8f5585c67b
---

为了判断对象是否为可被观察对象和获取对象关联的组件信息，开发者可以使用[canBeObserved接口](../harmonyos-references/js-apis-statemanagement.md#canbeobserved23)。

在使用该接口前，建议开发者对状态管理框架有基本的了解。提前阅读：[状态管理概述](arkts-state-management-overview.md)。

说明

从API version 23开始，开发者可以使用UIUtils中的canBeObserved接口判断数据对象是否为可观察对象。

## 概述

在开发和调试过程中，开发者会遇到修改对象的值后UI页面不刷新的问题（详见[状态管理常见问题](arkts-state-management-faq.md)），在复杂业务中排查此类问题尤为不便。为此，提供了canBeObserved接口帮助开发者定位和分析问题。开发者使用该接口不仅可以判断对象是否为可被观察的对象，还能获取对象关联的组件信息。

使用canBeObserved接口需要导入UIUtils工具。

```
1. import { UIUtils } from '@kit.ArkUI';
```

## 限制条件

canBeObserved仅支持非空的对象类型传参。如果传入undefined或null，isObserved返回false。如果传入非Object类型，则会编译报错。

```
1. import { UIUtils } from '@kit.ArkUI';

3. let res1 = UIUtils.canBeObserved(2); // 非法类型入参，错误用法，编译报错
4. let res2 = UIUtils.canBeObserved(undefined); // 非法类型入参，错误用法，isObserved返回false
5. let res3 = UIUtils.canBeObserved(null); // 非法类型入参，错误用法，isObserved返回false

7. class User {
8. name?: string;
9. }

11. let result: ObservedResult = UIUtils.canBeObserved(new User()); // 正确用法
```

## 对象可被观察场景

可被观察对象调用canBeObserved接口，返回的[ObservedResult](../harmonyos-references/js-apis-statemanagement.md#observedresult23)结果对象中reason的值包含以下情况：

| reason值 | 说明 |
| --- | --- |
| The object data is decorated with @Observed or wrapped by makeV1Observed | 对象被[@Observed](arkts-observed-and-objectlink.md)装饰器装饰或对象是使用[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)方法包装得到的，详见[V1组件对象可被观察场景](arkts-new-canbeobserved.md#v1组件对象可被观察场景) 。 |
| The object data is decorated with V2 @ObservedV2 and @Trace | 对象和对象属性被[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)装饰器装饰，详见[V2组件对象可被观察场景](arkts-new-canbeobserved.md#v2组件对象可被观察场景) 。 |
| The object data is wrapped by V2's makeObserved | 对象是使用[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)方法包装得到的，详见[V2组件对象可被观察场景](arkts-new-canbeobserved.md#v2组件对象可被观察场景) 。 |
| The object data is built-in type proxy data (Array/Map/Set/Date) decorated with @Trace | Array、Set、Map、Date类型数据对象被状态管理V2装饰器装饰或作为对象属性被[@Trace](arkts-new-observedv2-and-trace.md)装饰器装饰，详见[V2组件对象可被观察场景](arkts-new-canbeobserved.md#v2组件对象可被观察场景) 。 |
| The V1 Observed object data is wrapped by enableV2Compatibility and used in @ComponentV2 | V1组件和V2组件混用时，对象是使用[enableV2Compatibility](arkts-v1-v2-mixusage.md#enablev2compatibility)方法包装得到的，详见[V1组件和V2组件混用对象可被观察场景](arkts-new-canbeobserved.md#v1组件和v2组件混用对象可被观察场景) 。 |

需要注意，上述情况reason的值结尾如果有but not used in UI或but not used in @ComponentV2则表示：对象虽然是可被观察的，但是没有被UI组件所使用，因此改变对象值的时候也无法刷新UI。

### V1组件对象可被观察场景

在V1组件中，可被观察对象场景如下：

* 组件内被状态管理V1装饰器装饰的对象（包括Array、Set、Map、Date类型数据对象）。
* 被[@Observed](arkts-observed-and-objectlink.md)装饰器装饰的对象。
* 使用[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)方法包装的对象。

其中状态管理V1装饰器指的是：[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Link](arkts-link.md)、[@ObjectLink](arkts-observed-and-objectlink.md)、[@StorageLink](arkts-appstorage.md#storagelink)、[@StorageProp](arkts-appstorage.md#storageprop)、[@LocalStorageLink](arkts-localstorage.md#localstoragelink)、[@LocalStorageProp](arkts-localstorage.md#localstorageprop)、[@Provide](arkts-provide-and-consume.md)、[@Consume](arkts-provide-and-consume.md)。

被[@Observed](arkts-observed-and-objectlink.md)装饰的对象和使用[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)包装的对象，如果在组件内没有状态管理V1装饰器装饰，调用canBeObserved接口返回结果如下：

```
1. {
2. // 被@Observed装饰的对象和使用makeV1Observed方法包装的对象，是可被观察的对象
3. "isObserved": true,
4. // 如果在组件内没有状态管理V1装饰器装饰，reason会返回：没有被UI组件使用，也就不会刷新UI
5. // V1组件刷新依赖的是状态管理V1装饰器
6. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed, but not used in UI",
7. // 收集不到状态管理装饰器
8. "decoratorInfo": []
9. }
```

**组件内被状态管理V1装饰器装饰的对象**

以下介绍组件中使用[@State](arkts-state.md)装饰器装饰对象，使其变成可被观察对象的使用场景。

示例代码：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG = 'CanBeObserved';

6. class StateUser {
7. public name?: string;
8. public age?: number;

10. constructor(name?: string, age?: number) {
11. this.name = name ?? '';
12. this.age = age ?? 0;
13. }

15. // 在对象中提供判断该对象是否为可被观察对象的方法
16. test(): void {
17. hilog.info(0x00, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this))}`);
18. }
19. }

21. @Entry
22. @Component
23. struct V1State {
24. // V1组件中使用@State装饰对象时，会将该对象变成可被观察对象
25. @State stateUser: StateUser = new StateUser('James', 33);

27. build() {
28. Column({ space: 20 }) {
29. // 组件使用了可被观察对象的属性
30. Text('user name: ' + this.stateUser.name)
31. // 组件使用了可被观察对象的属性
32. Text('user age: ' + this.stateUser.age)
33. Button('test')
34. .onClick(() => {
35. // 开发者可以在任意页面中使用接口来判断当前对象是否为可被观察对象，并且可被获取对象关联的组件信息
36. this.stateUser.test();
37. })

39. }
40. .height('100%')
41. .width('100%')
42. .justifyContent(FlexAlign.Center)
43. .alignItems(HorizontalAlign.Center)
44. }
45. }
```

返回结果：

```
1. {
2. // 对象是可被观察的
3. "isObserved": true,
4. // V1组件中被状态管理装饰器装饰的对象是可被观察的
5. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
6. // 收集对象的装饰器信息
7. "decoratorInfo": [{
8. // 装饰器的名称
9. "decoratorName": "@State",
10. // 装饰器装饰的属性名称
11. "stateVariableName": "stateUser",
12. // 装饰器所在的组件名称
13. "owningComponentOrClassName": "V1State",
14. // 装饰器所在的组件id
15. "owningComponentId": 4,
16. // 对象关联的组件信息
17. "dependentInfo": [{
18. // 组件名称
19. "elementName": "Text",
20. // 组件id
21. "elementId": 6
22. }, {
23. "elementName": "Text",
24. "elementId": 7
25. }]
26. }]
27. }
```

**被@Observed装饰器装饰的对象**

以下介绍对象使用[@Observed](arkts-observed-and-objectlink.md)装饰器装饰，且对象属性使用[@Track](arkts-track.md)装饰器装饰的使用场景。

示例代码：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG = 'CanBeObserved';

6. @Observed
7. class TrackUser {
8. @Track
9. public name?: string;
10. @Track
11. public age?: number;

13. constructor(name?: string, age?: number) {
14. this.name = name ?? '';
15. this.age = age ?? 0;
16. }

18. // 在对象中提供判断该对象是否为可被观察对象的方法
19. test(): void {
20. hilog.info(0x00, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this))}`);
21. }
22. }

24. @Entry
25. @Component
26. struct V1Track {
27. @State trackUser: TrackUser = new TrackUser('Robert', 25);

29. build() {
30. Column({ space: 20 }) {
31. TrackChild({ trackUser: this.trackUser })
32. Button('test')
33. .onClick(() => {
34. // 开发者可以在任意页面中使用接口来判断当前对象是否为可被观察对象，并且可被获取对象关联的组件信息
35. this.trackUser.test();
36. })
37. }
38. .height('100%')
39. .width('100%')
40. .justifyContent(FlexAlign.Center)
41. .alignItems(HorizontalAlign.Center)
42. }
43. }

45. @Component
46. struct TrackChild {
47. @ObjectLink trackUser: TrackUser;

49. build() {
50. Column() {
51. // 组件中使用可被观察对象的属性
52. Text('user name: ' + this.trackUser.name)
53. // 组件中使用可被观察对象的属性
54. Text('user age: ' + this.trackUser.age)
55. }
56. }
57. }
```

对象属性使用[@Track](arkts-track.md)装饰器时，其装饰器信息的收集规格与V2组件装饰器收集规格一致，可参考[V2组件对象可被观察场景](arkts-new-canbeobserved.md#v2组件对象可被观察场景)。

返回结果：

```
1. {
2. // 对象可被观察
3. "isObserved": true,
4. // 使用@Observed装饰器装饰的对象是可被观察对象
5. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
6. // 对象属性使用了@Track装饰器，装饰器信息收集规格与V2组件的收集规格一致
7. "decoratorInfo": [{
8. // 对象属性使用了@Track装饰时，装饰器名称固定为@Track
9. "decoratorName": "@Track",
10. // 对象属性使用了@Track装饰时，stateVariableName表示被@Track装饰是的属性名称
11. "stateVariableName": "name",
12. // 对象属性使用了@Track装饰时，owningComponentOrClassName表示类的名称
13. "owningComponentOrClassName": "TrackUser",
14. // owningComponentOrClassName为类名称时，owningComponentId固定返回-1
15. "owningComponentId": -1,
16. // 对象的name属性关联的组件信息
17. "dependentInfo": [{
18. "elementName": "Text",
19. "elementId": 10
20. }]
21. }, {
22. "decoratorName": "@Track",
23. "stateVariableName": "age",
24. "owningComponentOrClassName": "TrackUser",
25. "owningComponentId": -1,
26. // 对象的age属性关联的组件信息
27. "dependentInfo": [{
28. "elementName": "Text",
29. "elementId": 11
30. }]
31. }]
32. }
```

### V2组件对象可被观察场景

V2组件中，对象可被观察场景如下：

* 被[@ObservedV2](arkts-new-observedv2-and-trace.md)装饰器装饰的对象。
* 被状态管理V2装饰器装饰的Array、Set、Map、Date类型数据对象。
* 使用[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)方法包装的对象。

其中状态管理V2装饰器指的是：[@Local](arkts-new-local.md)、[@Param](arkts-new-param.md)、[@Provider](arkts-new-provider-and-consumer.md)、[@Consumer](arkts-new-provider-and-consumer.md)。

V2组件收集装饰器的规格与V1组件不同，V2组件收集装饰器信息时，是按照对象的@Trace装饰的属性进行分类收集的。以下面的TestClass为例，@Trace将以属性为单位展示关联组件的信息：

```
1. // 定义Class
2. @ObservedV2
3. class TestClass {
4. @Trace a?: string;
5. @Trace b?: string;
6. @Trace c?: string;
7. }
```

```
1. // 返回结果分析
2. {
3. // 对象是可被观察的
4. "isObserved": true,
5. "reason": "The object data is decorated with V2 @ObservedV2 and @Trace",
6. // 装饰器信息是按照@Trace装饰的属性进行分类收集
7. "decoratorInfo": [{
8. "decoratorName": "@Trace",
9. // 对象中@Trace属性的名称
10. "stateVariableName": "a",
11. // 对象的类名称
12. "owningComponentOrClassName": "TestClass",
13. // owningComponentId固定返回-1
14. "owningComponentId": -1,
15. // 同一个@Trace属性关联的组件信息集合在一起
16. "dependentInfo": [{
17. "elementId": 5,
18. "elementName": "Text"
19. }]
20. },{
21. "decoratorName": "@Trace",
22. "stateVariableName": "b",
23. "owningComponentOrClassName": "TestClass",
24. "owningComponentId": -1,
25. // 同一个@Trace属性关联的组件信息集合在一起
26. "dependentInfo": [{
27. "elementId": 6,
28. "elementName": "Text"
29. }]
30. },{
31. "decoratorName": "@Trace",
32. "stateVariableName": "c",
33. "owningComponentOrClassName": "TestClass",
34. "owningComponentId": -1,
35. // 同一个@Trace属性关联的组件信息集合在一起
36. "dependentInfo": [{
37. "elementId": 7,
38. "elementName": "Text"
39. }]
40. }]
41. }
```

**被@ObservedV2装饰器装饰的对象**

以下介绍V2组件中使用[@ObservedV2](arkts-new-observedv2-and-trace.md)装饰器装饰对象的使用场景。

示例代码：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG = 'CanBeObserved';

6. @ObservedV2
7. class LocalUser {
8. @Trace
9. public name?: string;
10. @Trace
11. public age?: number;

13. constructor(name?: string, age?: number) {
14. this.name = name ?? '';
15. this.age = age ?? 0;
16. }

18. // 在对象中提供判断该对象是否为可被观察对象的方法
19. test(): void {
20. hilog.info(0x00, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this))}`);
21. }
22. }

24. @Entry
25. @ComponentV2
26. struct V2Local {
27. @Local localUser: LocalUser = new LocalUser('Michael', 29);

29. build() {
30. Column({ space: 20 }) {
31. Text('index ' + this.localUser.name)
32. Text('index ' + this.localUser.age)
33. Button('test')
34. .onClick(() => {
35. // 开发者可以在任意页面中使用接口来判断当前对象是否为可被观察对象
36. this.localUser.test();
37. })
38. }
39. .height('100%')
40. .width('100%')
41. .justifyContent(FlexAlign.Center)
42. .alignItems(HorizontalAlign.Center)
43. }
44. }
```

返回结果：

```
1. {
2. // 对象是可被观察的
3. "isObserved": true,
4. // @ObservedV2装饰的对象是可被观察的
5. "reason": "The object data is decorated with V2 @ObservedV2 and @Trace",
6. // 对象上装饰器信息，按@Trace装饰的属性分类收集
7. "decoratorInfo": [{
8. // 装饰器名称固定为@Trace
9. "decoratorName": "@Trace",
10. // @Trace装饰的属性名称
11. "stateVariableName": "name",
12. // 对象类名称
13. "owningComponentOrClassName": "LocalUser",
14. // owningComponentId固定返回-1
15. "owningComponentId": -1,
16. // 对象的name属性关联的组件信息
17. "dependentInfo": [{
18. "elementId": 6,
19. "elementName": "Text"
20. }]
21. }, {
22. "decoratorName": "@Trace",
23. "stateVariableName": "age",
24. "owningComponentOrClassName": "LocalUser",
25. "owningComponentId": -1,
26. // 对象的age属性关联的组件信息
27. "dependentInfo": [{
28. "elementId": 7,
29. "elementName": "Text"
30. }]
31. }]
32. }
```

### V1组件和V2组件混用对象可被观察场景

V1组件和V2组件混用的场景中，要使对象能在V1组件和V2组件保持同步刷新，则需要在V1组件中使用[enableV2Compatibility](arkts-v1-v2-mixusage.md#enablev2compatibility)方法将V1组件的可被观察对象包装后传入V2组件。

代码示例：

```
1. import { UIUtils } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG = 'CanBeObserved';

6. class CompatibilityUser {
7. public name?: string;
8. public age?: number;

10. constructor(name?: string, age?: number) {
11. this.name = name ?? '';
12. this.age = age ?? 0;
13. }

15. // 在对象中提供判断该对象是否为可被观察对象的方法
16. test(): void {
17. hilog.info(0x00, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this))}`);
18. }
19. }

21. @Entry
22. @Component
23. struct V1AndV2Compatibility {
24. // 被enableV2Compatibility转换的V1对象必须是可被观察的V1对象
25. @State temp: CompatibilityUser = new CompatibilityUser('Thomas', 43);
26. @State compatibilityUser: CompatibilityUser = UIUtils.enableV2Compatibility(this.temp);

28. build() {
29. Column({ space: 20 }) {
30. Text('V1 name: ' + this.compatibilityUser.name)
31. Text('V1 age: ' + this.compatibilityUser.age)

33. V2Child({ compatibilityUser: this.compatibilityUser })

35. Button('test')
36. .onClick(() => {
37. // 开发者可以在任意页面中使用接口来判断当前对象是否为可被观察对象
38. this.compatibilityUser.test();
39. })
40. }
41. .height('100%')
42. .width('100%')
43. .justifyContent(FlexAlign.Center)
44. .alignItems(HorizontalAlign.Center)
45. }
46. }

48. @ComponentV2
49. export struct V2Child {
50. @Param compatibilityUser: CompatibilityUser = new CompatibilityUser();

52. build() {
53. Column() {
54. Text('V2Child name ' + this.compatibilityUser.name)
55. Text('V2Child age ' + this.compatibilityUser.age)
56. }
57. }
58. }
```

返回结果：

```
1. {
2. // 对象是可被观察的
3. "isObserved": true,
4. // 通过enableV2Compatibility方法转换的对象也是可被观察的
5. "reason": "The V1 Observed object data is wrapped by enableV2Compatibility and used in @ComponentV2",
6. // 装饰器信息，V1组件和V2组件分别收集
7. "decoratorInfo": [{
8. "decoratorName": "@State",
9. "stateVariableName": "temp",
10. "owningComponentOrClassName": "V1AndV2Compatibility",
11. "owningComponentId": 4,
12. "dependentInfo": []
13. }, {
14. "decoratorName": "@State",
15. "stateVariableName": "compatibilityUser",
16. "owningComponentOrClassName": "V1AndV2Compatibility",
17. "owningComponentId": 4,
18. "dependentInfo": [{
19. "elementName": "Text",
20. "elementId": 6
21. }, {
22. "elementName": "Text",
23. "elementId": 7
24. }, {
25. "elementName": "V2Child",
26. "elementId": 8
27. }]
28. }, {
29. // V2组件的decoratorName名称固定EnableV2Compatible
30. "decoratorName": "EnableV2Compatible",
31. // V2组件按对象属性分类收集
32. "stateVariableName": "name",
33. "owningComponentOrClassName": "CompatibilityUser",
34. "owningComponentId": -1,
35. // 对象name属性在V2组件中关联的组件信息
36. "dependentInfo": [{
37. "elementId": 12,
38. "elementName": "Text"
39. }]
40. }, {
41. "decoratorName": "EnableV2Compatible",
42. "stateVariableName": "age",
43. "owningComponentOrClassName": "CompatibilityUser",
44. "owningComponentId": -1,
45. // 对象age属性在V2组件中关联的组件信息
46. "dependentInfo": [{
47. "elementId": 13,
48. "elementName": "Text"
49. }]
50. }]
51. }
```

## 状态管理常见不刷新问题分析

在[状态管理常见问题](arkts-state-management-faq.md)的案例中介绍了常见的状态管理对象不刷新UI或者页面性能不达标的问题，以下介绍如何使用canBeObserved接口来帮助开发者分析和定位问题原因。

### a.b(this.object)案例分析

在[a.b(this.object)](arkts-state-management-faq-inner-component.md#使用abthisobject形式调用不会触发ui刷新)案例的反例中，由于b的入参传入的是this.object的原始对象，原始对象是不可被观察的，所以导致UI无法刷新。开发者可以在修改属性前调用canBeObserved接口判断入参对象是否可被观察。

在反例中提供了两个修改对象属性的方法，在修改属性前先使用canBeObserved接口判断对象是否可被观察，代码如下：

```
1. static increaseVolume(balloon: Balloon) {
2. // 修改属性前，通过canBeObserved来判断入参balloon对象是否可被观察
3. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(balloon))}`);
4. balloon.volume += 2;
5. }
```

```
1. reduceVolume(balloon: Balloon) {
2. // 修改属性前，通过canBeObserved来判断入参balloon对象是否可被观察
3. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(balloon))}`);
4. balloon.volume -= 1;
5. }
```

两个方法调用canBeObserved接口返回结果一样（如下所示），表示两个方法接收的入参都是不可被观察对象，所以UI无法刷新。

```
1. {
2. // 不可被观察
3. "isObserved": false,
4. // 原因：不是可被观察对象
5. "reason": "The object data is not an observable object",
6. // 装饰器信息为空
7. "decoratorInfo": []
8. }
```

在正例中修改属性方法前判断对象是否可被观察，代码如下：

```
1. static increaseVolume(balloon: Balloon) {
2. // 修改属性前，通过canBeObserved来判断入参balloon对象是否可被观察
3. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(balloon))}`);
4. balloon.volume += 2;
5. }
```

```
1. reduceVolume(balloon: Balloon) {
2. // 修改属性前，通过canBeObserved来判断入参balloon对象是否可被观察
3. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(balloon))}`);
4. balloon.volume -= 1;
5. }
```

两个方法调用canBeObserved接口返回结果一样（如下所示），表示两个方法接收的入参都是都是可被观察对象，且被UI组件所使用，UI可以正常刷新。

```
1. {
2. "isObserved": true,
3. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
4. "decoratorInfo": [{
5. "decoratorName": "@State",
6. "stateVariableName": "balloon",
7. "owningComponentOrClassName": "Index",
8. "owningComponentId": 4,
9. "dependentInfo": [{
10. "elementName": "Text",
11. "elementId": 6
12. }]
13. }]
14. }
```

### 状态变量关联的组件数过多导致性能下降案例分析

在[状态变量关联的组件数过多导致性能下降](arkts-state-management-faq-inner-component.md#状态变量关联的组件数过多导致性能下降)案例中提供了HiDumper工具来查看状态变量关联的组件，若组件关联过多，则页面性能下降。开发者也可以使用canBeObserved接口在业务代码中获取状态管理对象关联的组件，根据接口返回结果优化业务代码。

在反例中通过move按钮修改this.translateObj对象的属性，可以在修改属性前先调用canBeObserved接口来获取对象关联的组件信息，代码如下：

```
1. Button('move')
2. .translate({
3. x: this.translateObj.translateX
4. })
5. .onClick(() => {
6. this.getUIContext().animateTo({
7. duration: 50
8. }, () => {
9. // 在修改状态变量之前，调用canBeObserved接口获取状态变量关联的组件
10. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(this.translateObj))}`);
11. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150;
12. });
13. })
```

返回结果：

```
1. // 反例的获取结果，对象关联5个组件
2. {
3. "isObserved": true,
4. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
5. "decoratorInfo": [{
6. "decoratorName": "@State",
7. "stateVariableName": "translateObj",
8. "owningComponentOrClassName": "Page",
9. "owningComponentId": 4,
10. "dependentInfo": [{
11. "elementName": "Title",
12. "elementId": 6
13. }, {
14. "elementName": "Stack",
15. "elementId": 7
16. }, {
17. "elementName": "Button",
18. "elementId": 8
19. }]
20. }, {
21. "decoratorName": "@ObjectLink",
22. "stateVariableName": "translateObj",
23. "owningComponentOrClassName": "Title",
24. "owningComponentId": 6,
25. "dependentInfo": [{
26. "elementName": "Image",
27. "elementId": 11
28. }, {
29. "elementName": "Text",
30. "elementId": 12
31. }]
32. }]
33. }
```

在正例中修改对象的属性前也调用canBeObserved接口获取状态变量关联的组件，代码如下：

```
1. Button('move')
2. .onClick(() => {
3. this.getUIContext().animateTo({
4. duration: 50
5. }, () => {
6. // 在修改状态变量之前，调用canBeObserved接口获取状态变量关联的组件
7. hilog.info(0x00, 'test_log', `res: ${JSON.stringify(UIUtils.canBeObserved(this.translateObj))}`);
8. this.translateObj.translateX = (this.translateObj.translateX + 50) % 150;
9. });
10. })
```

返回结果：

```
1. // 正例的获取结果，对象关联1个组件
2. {
3. "isObserved": true,
4. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
5. "decoratorInfo": [{
6. "decoratorName": "@State",
7. "stateVariableName": "translateObj",
8. "owningComponentOrClassName": "Page1",
9. "owningComponentId": 4,
10. "dependentInfo": [{
11. "elementName": "Column",
12. "elementId": 5
13. }]
14. }]
15. }
```

对比可知：正例中对象关联的组件数量少于反例中对象关联的组件数量，从而实现性能提升。

### ForEach和对象数组结合使用导致UI不刷新案例分析

在[ForEach和对象数组结合使用导致UI不刷新](arkts-state-management-faq-inner-component.md#foreach和对象数组结合使用导致ui不刷新)案例中，使用canBeObserved接口获取判断对象是否是可被观察的。

在反例的onClick方法中，修改对象属性前先调用canBeObserved接口判断this.styleList[i]对象是否可被观察，代码如下：

```
1. Text('Font Size List')
2. .fontSize(50)
3. .onClick(() => {
4. for (let i = 0; i < this.styleList.length; i++) {
5. // 此处想要修改的是this.styleList[i]对象的fontSize属性
6. // 修改之前调用canBeObserved接口获取this.styleList[i]对象关联的组件信息
7. hilog.info(DOMAIN_NUMBER, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this.styleList[i]))}`);
8. this.styleList[i].fontSize++;
9. }
10. hilog.info(DOMAIN_NUMBER, TAG, 'change font size');
11. })
```

返回结果如下，虽然this.styleList[i]（也就是TextStyles对象）被[@Observed](arkts-observed-and-objectlink.md)装饰器装饰，是可被观察的，但没有被UI组件所使用，所以UI组件不刷新。

```
1. {
2. // 对象是可被观察的
3. "isObserved": true,
4. // @Observed装饰的对象是可被观察的
5. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed, but not used in UI",
6. // 收集的装饰器信息为空
7. "decoratorInfo": []
8. }
```

在正例中同样先判断对象是否可被观察，代码如下：

```
1. Text('Font Size List')
2. .fontSize(50)
3. .onClick(() => {
4. for (let i = 0; i < this.styleList.length; i++) {
5. // 此处想要修改的是this.styleList[i]对象的fontSize属性
6. // 修改之前调用canBeObserved接口获取this.styleList[i]对象关联的组件信息
7. hilog.info(DOMAIN_NUMBER, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this.styleList[i]))}`);
8. this.styleList[i].fontSize++;
9. }
10. hilog.info(DOMAIN_NUMBER, TAG, 'change font size');
11. })
```

返回结果如下，可知this.styleList[i]是可被观察对象，且有关联的UI组件，能正常刷新UI组件。

```
1. {
2. "isObserved": true,
3. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
4. "decoratorInfo": [{
5. "decoratorName": "@ObjectLink",
6. "stateVariableName": "textStyle",
7. "owningComponentOrClassName": "TextComponent",
8. "owningComponentId": 147,
9. "dependentInfo": [{
10. "elementName": "Text",
11. "elementId": 148
12. }]
13. }]
14. }
```

### 数据重置导致UI不刷新使用场景

在[数据重置导致UI不刷新使用场景](arkts-state-management-faq-inner-class.md#数据重置导致ui不刷新)案例中，使用canBeObserved接口定位UI不刷新原因。

在反例的X按钮修改对象属性前先调用canBeObserved接口判断对象是否可被观察，代码如下：

```
1. Button('X')
2. .backgroundColor(Color.Red)
3. .onClick(() => {
4. let index = this.childList.findIndex((item) => {
5. return item.count === this.child.count;
6. });
7. if (index !== -1) {
8. // 在删除数组元素之前，调用canBeObserved接口判断this.childList是否是一个可被观察对象
9. hilog.info(DOMAIN_NUMBER, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this.childList))}`);
10. this.childList.splice(index, 1);
11. }
12. })
13. .margin({
14. left: 200,
15. right: 30
16. })
```

在点击Recover按钮后，再次点击X按钮，数组元素不会删除，调用canBeObserved接口返回的结果发现，Recover之后的this.childList数组已经不是可被观察的了。

```
1. {
2. "isObserved": false,
3. "reason": "The object data is not an observable object",
4. "decoratorInfo": []
5. }
```

在正例中修改元素属性前判断对象是否可被观察，代码如下：

```
1. Button('X')
2. .backgroundColor(Color.Red)
3. .onClick(() => {
4. let index = this.childList.findIndex((item) => {
5. return item.count === this.child.count;
6. });
7. if (index !== -1) {
8. // 在删除数组元素之前，调用canBeObserved接口判断this.childList是否是一个可被观察对象
9. hilog.info(DOMAIN_NUMBER, TAG, `res: ${JSON.stringify(UIUtils.canBeObserved(this.childList))}`);
10. this.childList.splice(index, 1);
11. }
12. })
13. .margin({
14. left: 200,
15. right: 30
16. })
```

返回结果中关键信息如下，可知this.childList数组是可被观察的，且有关联的UI组件，能正常刷新UI组件。

```
1. {
2. "isObserved": true,
3. "reason": "The object data is decorated with @Observed or wrapped by makeV1Observed",
4. "decoratorInfo": [{
5. "decoratorName": "@ObjectLink",
6. "stateVariableName": "childList",
7. "owningComponentOrClassName": "CompList",
8. "owningComponentId": 8,
9. "dependentInfo": [{
10. "elementName": "ForEach",
11. "elementId": 16
12. }]
13. },
14. ...
15. // 以下结果省略
16. ]
17. }
```
