---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-gettarget
title: getTarget接口：获取状态管理框架代理前的原始对象
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 辅助接口 > getTarget接口：获取状态管理框架代理前的原始对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8558b28dfcf8aa9de08d5b88573c327e052a6f5250e2be4f5da8d2e4cda9c147
---

为了获取状态管理框架代理前的原始对象，开发者可以使用[getTarget接口](../harmonyos-references/js-apis-statemanagement.md#gettarget)。

在阅读本文档前，建议提前阅读：[@Observed](arkts-observed-and-objectlink.md)、[@ObservedV2](arkts-new-observedv2-and-trace.md)。

说明

从API version 12开始，开发者可以使用UIUtils中的getTarget接口获取状态管理框架代理前的原始对象。

## 概述

状态管理框架会对class、Date、Map、Set、Array类型的原始对象添加代理，用于观测属性变化与API调用。这一层代理会使得变量类型改变，在类型判断、NAPI调用等场景，会由于类型并非原始对象的类型产生预料之外的结果。

* 使用getTarget接口需要导入UIUtils工具。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  ```
* 状态管理V1中，会给@Observed装饰的类对象以及使用状态变量装饰器如[@State](arkts-state.md)装饰的class、Date、Map、Set、Array添加一层代理用于观测一层属性或API调用产生的变化。
* 状态管理V2中，会给使用状态变量装饰器如[@Trace](arkts-new-observedv2-and-trace.md)、[@Local](arkts-new-local.md)装饰的Date、Map、Set、Array添加一层代理用于观测API调用产生的变化。

使用getTarget接口可以获取这些代理对象的原始对象。

## 限制条件

* getTarget仅支持对象类型传参。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. let resNumber = UIUtils.getTarget(2); // 非对象类型入参，编译时报错
  3. let resObject = UIUtils.getTarget(2 as Object); // 非对象类型入参，绕过编译拦截，直接返回传入值，错误用法
  ```

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. @Observed
  3. class Info {
  4. public name: string = 'Tom';
  5. }
  6. let info: Info = new Info();
  7. let rawInfo: Info = UIUtils.getTarget(info); // 正确用法
  ```

  [ModelViewOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/model/ModelViewOne.ets#L15-L23)
* 更改getTarget获取的原始对象中的内容不会被观察到变化，也不会触发UI刷新。

  ```
  1. import { UIUtils } from '@kit.ArkUI';
  2. @Observed
  3. class Info {
  4. public name: string = 'Tom';
  5. }
  6. @Entry
  7. @Component
  8. struct GetTargetObject {
  9. @State info: Info = new Info();

  11. build() {
  12. Column() {
  13. Text(`info.name: ${this.info.name}`)
  14. Button('Change Proxy Object Properties')
  15. .onClick(() => {
  16. this.info.name = 'Alice'; // Text组件能够刷新
  17. })
  18. Button('Change Original Object Properties')
  19. .onClick(() => {
  20. let rawInfo: Info = UIUtils.getTarget(this.info);
  21. rawInfo.name = 'Bob'; // Text组件不能刷新
  22. })
  23. }
  24. }
  25. }
  ```

  [GetTargetObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetTargetObject.ets#L15-L41)

## 使用场景

### 获取状态管理V1代理前的原始对象

状态管理V1有两种场景会给对象增加代理：

【1】@Observed装饰的类实例。在创建@Observed装饰的类实例时，会给该实例添加代理。该过程发生在new对象的过程中，以下示例中，没有被@Observed装饰的类是不被代理的。

```
1. @Observed
2. class ObservedClass {
3. public name: string = 'Tom';
4. }
5. class NonObservedClass {
6. public name: string = 'Tom';
7. }
8. let observedClass: ObservedClass = new ObservedClass(); // 被代理
9. let nonObservedClass: NonObservedClass = new NonObservedClass(); // 不被代理
```

[GetTargetAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetTargetAgent.ets#L17-L27)

【2】状态变量装饰器装饰的复杂类型对象。使用@State、[@Prop](arkts-prop.md)等状态变量装饰器装饰Class、Map、Set、Date、Array时，会添加代理。若该对象已经是代理对象，则不会重复创建代理。

```
1. @Observed
2. class ObservedClassOne {
3. public name: string = 'Tom';
4. }
5. class NonObservedClassOne {
6. public name: string = 'Tom';
7. }
8. let observedClass: ObservedClassOne = new ObservedClassOne(); // 被代理
9. let nonObservedClass: NonObservedClassOne = new NonObservedClassOne(); // 不被代理
10. @Entry
11. @Component
12. struct GetTargetNoChange {
13. @State observedObject: ObservedClassOne = observedClass; // 已被代理数据不会重复创建代理
14. @State nonObservedObject: NonObservedClassOne = nonObservedClass; // 创建代理
15. @State numberList: number[] = [1, 2, 3]; // Array类型创建代理
16. @State sampleMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]); // Map类型创建代理
17. @State sampleSet: Set<number> = new Set([0, 1, 2, 3, 4]); // Set类型创建代理
18. @State sampleDate: Date = new Date(); // Date类型创建代理

20. build() {
21. Column() {
22. Text(`this.observedObject === observedClass: ${this.observedObject === observedClass}`) // true
23. Text(`this.nonObservedObject === nonObservedClass: ${this.nonObservedObject === nonObservedClass}`) // false
24. }
25. }
26. }
```

[GetTargetNoChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetTargetNoChange.ets#L15-L42)

使用UIUtils.getTarget接口可以获取代理前的原始对象。

```
1. import { UIUtils } from '@kit.ArkUI';
2. @Observed
3. class ObservedClass {
4. public name: string = 'Tom';
5. }
6. class NonObservedClass {
7. public name: string = 'Tom';
8. }
9. let observedClass: ObservedClass = new ObservedClass(); // 被代理
10. let nonObservedClass: NonObservedClass = new NonObservedClass(); // 不被代理
11. let globalNumberList: number[] = [1, 2, 3]; // 不被代理
12. let globalSampleMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]); // 不被代理
13. let globalSampleSet: Set<number> = new Set([0, 1, 2, 3, 4]); // 不被代理
14. let globalSampleDate: Date = new Date(); // 不被代理
15. @Entry
16. @Component
17. struct GetTargetAgent {
18. @State observedObject: ObservedClass = observedClass; // 已被代理数据不会重复创建代理
19. @State nonObservedObject: NonObservedClass = nonObservedClass; // 创建代理
20. @State numberList: number[] = globalNumberList; // Array类型创建代理
21. @State sampleMap: Map<number, string> = globalSampleMap; // Map类型创建代理
22. @State sampleSet: Set<number> = globalSampleSet; // Set类型创建代理
23. @State sampleDate: Date = globalSampleDate; // Date类型创建代理

25. build() {
26. Column() {
27. Text(`this.observedObject === observedClass: ${this.observedObject ===
28. observedClass}`) // true
29. Text(`UIUtils.getTarget(this.nonObservedObject) === nonObservedClass: ${UIUtils.getTarget(this.nonObservedObject) ===
30. nonObservedClass}`) // true
31. Text(`UIUtils.getTarget(this.numberList) === globalNumberList: ${UIUtils.getTarget(this.numberList) ===
32. globalNumberList}`) // true
33. Text(`UIUtils.getTarget(this.sampleMap) === globalSampleMap: ${UIUtils.getTarget(this.sampleMap) ===
34. globalSampleMap}`) // true
35. Text(`UIUtils.getTarget(this.sampleSet) === globalSampleSet: ${UIUtils.getTarget(this.sampleSet) ===
36. globalSampleSet}`) // true
37. Text(`UIUtils.getTarget(this.sampleDate) === globalSampleDate: ${UIUtils.getTarget(this.sampleDate) ===
38. globalSampleDate}`) // true
39. }
40. }
41. }
```

[GetTargetAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetTargetAgent.ets#L15-L59)

### 获取状态管理V2代理前的原始对象

状态管理V2会给状态变量装饰器如@Trace、@Local装饰的Map、Set、Date、Array添加一层代理。和V1不同的是，状态管理V2不会对类对象实例进行代理。

```
1. @ObservedV2
2. class ObservedClassTwo {
3. @Trace public name: string = 'Tom';
4. }
5. let globalObservedObject: ObservedClassTwo = new ObservedClassTwo(); // 不被代理
6. let globalNumberList: number[] = [1, 2, 3]; // 不被代理
7. let globalSampleMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]); // 不被代理
8. let globalSampleSet: Set<number> = new Set([0, 1, 2, 3, 4]); // 不被代理
9. let globalSampleDate: Date = new Date(); // 不被代理
10. @Entry
11. @ComponentV2
12. struct GetAgentObject {
13. @Local observedObject: ObservedClassTwo = globalObservedObject; // V2中对象不被代理
14. @Local numberList: number[] = globalNumberList; // Array类型创建代理
15. @Local sampleMap: Map<number, string> = globalSampleMap; // Map类型创建代理
16. @Local sampleSet: Set<number> = globalSampleSet; // Set类型创建代理
17. @Local sampleDate: Date = globalSampleDate; // Date类型创建代理

19. build() {
20. Column() {
21. Text(`this.observedObject === globalObservedObject ${this.observedObject === globalObservedObject}`) // true
22. Text(`this.numberList === globalNumberList ${this.numberList === globalNumberList}`) // false
23. }
24. }
25. }
```

[GetAgentObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetAgentObject.ets#L15-L41)

使用UIUtils.getTarget接口可以获取代理前的原始对象。

```
1. import { UIUtils } from '@kit.ArkUI';
2. @ObservedV2
3. class ObservedClassThree {
4. @Trace public name: string = 'Tom';
5. }
6. let globalObservedObject: ObservedClassThree = new ObservedClassThree(); // 不被代理
7. let globalNumberList: number[] = [1, 2, 3]; // 不被代理
8. let globalSampleMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]); // 不被代理
9. let globalSampleSet: Set<number> = new Set([0, 1, 2, 3, 4]); // 不被代理
10. let globalSampleDate: Date = new Date(); // 不被代理
11. @Entry
12. @ComponentV2
13. struct GetBeforeAgent {
14. @Local observedObject: ObservedClassThree = globalObservedObject; // V2中对象不被代理
15. @Local numberList: number[] = globalNumberList; // Array类型创建代理
16. @Local sampleMap: Map<number, string> = globalSampleMap; // Map类型创建代理
17. @Local sampleSet: Set<number> = globalSampleSet; // Set类型创建代理
18. @Local sampleDate: Date = globalSampleDate; // Date类型创建代理

20. build() {
21. Column() {
22. Text(`this.observedObject === globalObservedObject ${this.observedObject ===
23. globalObservedObject}`) // true
24. Text(`UIUtils.getTarget(this.numberList) === globalNumberList: ${UIUtils.getTarget(this.numberList) ===
25. globalNumberList}`) // true
26. Text(`UIUtils.getTarget(this.sampleMap) === globalSampleMap: ${UIUtils.getTarget(this.sampleMap) ===
27. globalSampleMap}`) // true
28. Text(`UIUtils.getTarget(this.sampleSet) === globalSampleSet: ${UIUtils.getTarget(this.sampleSet) ===
29. globalSampleSet}`) // true
30. Text(`UIUtils.getTarget(this.sampleDate) === globalSampleDate: ${UIUtils.getTarget(this.sampleDate) ===
31. globalSampleDate}`) // true
32. }
33. }
34. }
```

[GetBeforeAgent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/View/GetBeforeAgent.ets#L15-L50)

状态管理V2装饰器会为装饰的变量生成getter和setter方法，同时为原有变量名添加"\_\_ob\_"的前缀。出于性能考虑，getTarget接口不会对V2装饰器生成的前缀进行处理，因此向getTarget接口传入@ObservedV2装饰的类对象实例时，返回的对象依旧为对象本身，且被@Trace装饰的属性名仍有"\_\_ob\_"前缀。

该前缀会导致某些NAPI接口无法按预期处理对象的属性，以下面的对象为例，目前已知影响的NAPI接口如下：

```
1. @ObservedV2
2. class Info {
3. @Trace public name: string = 'Tom';
4. @Trace public age: number = 24;
5. }
6. let info: Info = new Info(); // NAPI接口传入info实例
```

[ModelViewTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NewGettarget/entry/src/main/ets/model/ModelViewTwo.ets#L15-L22)

| 影响接口名 | 影响结果 |
| --- | --- |
| [napi\_get\_property\_names](use-napi-about-property.md#napi_get_property_names) | 返回值为"\_\_ob\_name"，"\_\_ob\_age"。 |
| [napi\_set\_property](use-napi-about-property.md#napi_set_property) | 使用"name"，"\_\_ob\_name"均能赋值成功。 |
| [napi\_get\_property](use-napi-about-property.md#napi_get_property) | 使用"name"，"\_\_ob\_name"均能获取到值。 |
| [napi\_has\_property](use-napi-about-property.md#napi_has_property) | 使用"name"，"\_\_ob\_name"均返回true。 |
| [napi\_delete\_property](use-napi-about-property.md#napi_delete_property) | 删除属性时需要加上"\_\_ob\_"前缀才能删除成功。 |
| [napi\_has\_own\_property](use-napi-about-property.md#napi_has_own_property) | 使用"name"，"\_\_ob\_name"均返回true。 |
| [napi\_set\_named\_property](use-napi-about-property.md#napi_set_named_property) | 使用"name"，"\_\_ob\_name"均能赋值成功。 |
| [napi\_get\_named\_property](use-napi-about-property.md#napi_get_named_property) | 使用"name"，"\_\_ob\_name"均能获取到值。 |
| [napi\_has\_named\_property](use-napi-about-property.md#napi_has_named_property) | 使用"name"，"\_\_ob\_name"均返回true。 |
