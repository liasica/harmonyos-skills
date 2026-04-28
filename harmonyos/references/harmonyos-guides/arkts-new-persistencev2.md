---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2
title: PersistenceV2: 持久化存储UI状态
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理应用拥有的状态 > PersistenceV2: 持久化存储UI状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6b7f7e485edf29311bb5c45e348879021b577999318b097d92120829f9f44e47
---

为了增强状态管理框架对持久化存储UI的能力，开发者可以使用PersistenceV2存储持久化的数据。

PersistenceV2是应用程序中的可选单例对象。此对象的作用是持久化存储UI相关的数据，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

PersistenceV2提供状态变量持久化能力，开发者可以通过connect或者globalConnect绑定同一个key，在状态变量变化和应用冷启动时，实现持久化能力。

在阅读本文档前，建议提前阅读：[@ComponentV2](arkts-create-custom-components.md#componentv2)，[@ObservedV2和@Trace](arkts-new-observedv2-and-trace.md)，配合阅读：[PersistenceV2-API文档](../harmonyos-references/js-apis-statemanagement.md#persistencev2)。

说明

PersistenceV2从API version 12开始支持。

globalConnect从API version 18开始支持，行为和connect保持一致，唯一的区别为connect的底层存储路径为module级别的路径，而globalConnect的底层存储路径为应用级别，详细区别见使用场景[在不同的module中使用connect和globalConnect](arkts-new-persistencev2.md#在不同的module中使用connect和globalconnect)。

globalConnect从API version 23开始支持[集合类型](arkts-new-persistencev2.md#globalconnect支持集合的类型)（Array、Map、Set、Date、collections.Array、collections.Map、collections.Set）的持久化，支持在UI线程持久化@Sendable类型的数据持久化，支持持久化循环引用的对象，支持持久化单个key超过8k的数据。目前建议开发者使用API version 23的新增的globalConnect接口。

## 概述

PersistenceV2是在应用UI启动时会被创建的单例。它的目的是提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。数据通过唯一的键值字符串访问。不同于AppStorageV2，PersistenceV2还将最新数据存储在设备磁盘上（持久化）。这意味着，应用退出再次启动后，依然能保存选定的结果。

对于与PersistenceV2关联的[@ObservedV2](arkts-new-observedv2-and-trace.md)对象，该对象的[@Trace](arkts-new-observedv2-and-trace.md)属性的变化，会触发**整个关联对象的自动持久化**；非[@Trace](arkts-new-observedv2-and-trace.md)属性的变化则不会，如有必要，可调用PersistenceV2 API手动持久化。请注意：被PersistenceV2持久化的类属性必须要有初值，否则不支持持久化。

PersistenceV2可以和UI组件同步，且可以在应用业务逻辑中被访问。

PersistenceV2支持应用的[主线程](thread-model-stage.md)内多个UIAbility实例间的状态共享。

PersistenceV2继承自[AppStorageV2](../harmonyos-references/js-apis-statemanagement.md#appstoragev2)，支持通过[connect](../harmonyos-references/js-apis-statemanagement.md#connect)创建或获取存储的数据。

## 使用说明

* globalConnect：创建或获取存储的数据。

  说明

  1、关联[@Observed](arkts-observed-and-objectlink.md)对象时，由于该类型的name属性未定义，需要指定key或者自定义name属性。

  2、 globalConnect为应用级别存储，对于一个key，整个应用在对应加密分区只有一份存储路径。使用PersistenceV2的connect存储的数据路径为module级别，即哪个module调用了connect，数据副本存入对应module的持久化文件中。如果多个module使用相同的key，则数据为最先使用connect的module，并且PersistenceV2中的数据也会存入最先使用connect的module里。因为存储路径在应用第一个ability启动时就已确定，为该ability所属的module。如果一个ability调用了connect，并且该ability能被不同的module拉起， 那么ability存在多少种启动方式，就会有多少份数据副本，因此，建议开发者使用globalConnect代替connect接口。
* remove：删除指定key的存储数据。删除PersistenceV2中不存在的key会报警告。
* keys：返回所有PersistenceV2中的key。包括module级别存储路径和应用级别存储路径中的所有key。
* save：手动持久化数据。
* notifyOnError：响应序列化或反序列化失败的回调。将数据存入磁盘时，需要对数据进行序列化；当某个key序列化失败时，错误是不可预知的；可调用该接口捕获异常。

以上接口详细描述请参考[状态管理API指南](../harmonyos-references/js-apis-statemanagement.md)。

## 使用限制

1、需要配合UI使用（UI线程），不能在其他线程使用。在API version 23以前，不支持@Sendable。

* 从API version 23开始，提供globalConnect接口，支持在UI线程持久化@Sendable装饰的类对象，其成员属性的类型需为基础内置类型（string、number和boolean）。

2、在API version 23以前，不支持collections.Set、collections.Map等类型。

* 从API version 23开始， 提供globalConnect接口，支持[collections.Set](../harmonyos-references/arkts-apis-arkts-collections-set.md)、[collections.Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)和[collections.Array](../harmonyos-references/arkts-apis-arkts-collections-array.md)。collections.Set、collections.Map和collections.Array本身无法观察，在globalConnect接口使用defaultCreator时，需要使用[UIUtils.makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)，才能在值变化时自动保存，如果不使用，开发者需要手动调用[PersistenceV2.save(key)](../harmonyos-references/js-apis-statemanagement.md#save)保存变化的数据。

  如下是新增接口globalConnect支持collections.Array的示例代码:

  ```
  1. import { PersistenceV2, UIUtils } from '@kit.ArkUI';
  2. import { collections } from '@kit.ArkTS';

  4. @Entry
  5. @ComponentV2
  6. struct Page1 {
  7. // 支持直接持久化collections.Array的类型
  8. @Local array: collections.Array<number> = PersistenceV2.globalConnect({
  9. // 定义持久化的数据类型
  10. type: collections.Array<number>,
  11. // 定义默认构造器，返回时需要调用makeObserved，才能实现自动持久化
  12. defaultCreator: () => UIUtils.makeObserved(new collections.Array<number>(1,2))
  13. })!;
  14. // 基于collections.Array构建Repeat的数据源
  15. toArray<T>(array: collections.Array<T>): Array<T> {
  16. const result = new Array<T>();
  17. array.forEach((item: T) => result.push(item));
  18. return result;
  19. }

  21. build() {
  22. Column({ space: 10 }) {
  23. Column({ space: 0 }) {
  24. Repeat(this.toArray(this.array))
  25. .each(ri => {
  26. Row() {
  27. Text(`Item: `)
  28. Text(`${ri.item}`)
  29. }
  30. })
  31. .key((item: number, index: number) => `${index} - ${item}`)
  32. }
  33. Divider().width('100%')
  34. // 点击'array.push(0)'，重启应用，Repeat数组项是：1, 2, 0
  35. Button('array.push(0)')
  36. .onClick(() => {
  37. this.array.push(Math.round(0));
  38. })
  39. .fontSize(24)
  40. // 点击'array.pop()'，重启应用，Repeat数组项是：1, 2
  41. Button('array.pop()')
  42. .onClick(() => {
  43. this.array.pop();
  44. })
  45. .fontSize(24)
  46. // 点击'array.splice(0)'，重启应用，Repeat数组项为空
  47. Button('array.splice(0)')
  48. .onClick(() => {
  49. this.array.splice(0);
  50. })
  51. .fontSize(24)
  52. // 点击'splice(1, 0, random)'，重启应用：Repeat组件再次显示相同的数组项
  53. Button('array.splice(1, 0, random)')
  54. .onClick(() => {
  55. this.array.splice(1, 0, Math.round(100*Math.random()));
  56. })
  57. .fontSize(24)
  58. // 点击'array.splice(0, 2, random, random)'，前两个数组项目被替换，记录下来
  59. // 重启应用：Repeat组件再次显示数组项
  60. Button('array.splice(0, 2, random, random)')
  61. .onClick(() => {
  62. this.array.splice(2, 2, Math.round(100*Math.random()), Math.round(100*Math.random()));
  63. })
  64. .fontSize(24)
  65. // 点击'array.sort', 对数组项升序排列，重启应用，Repeat组件展示升序数组
  66. Button('array.sort')
  67. .onClick(() => {
  68. this.array.sort((a, b) => a -b);
  69. })
  70. .fontSize(24)
  71. // 点击'array.reverse', 对数组项降序排列，重启应用，Repeat组件展示降序数组
  72. Button('array.reverse')
  73. .onClick(() => {
  74. this.array.reverse();
  75. })
  76. .fontSize(24)
  77. }
  78. .width('100%')
  79. }
  80. }
  ```
* globalConnect在持久化多个相同[集合类型](arkts-new-persistencev2.md#globalconnect支持集合的类型)时，需要提供不同的key来区分持久化数据。

  如下展示开发者持久化相同的Array<number>类型的部分示例代码片段：

  ```
  1. @Entry
  2. @ComponentV2
  3. struct Page1 {
  4. // 持久化相同容器类型的数据，建议开发者使用不同的key来区分持久化数据
  5. @Local arr1: Array<number> = PersistenceV2.globalConnect({
  6. type: Array<number>,
  7. key: 'arr1',
  8. defaultCreator: () => UIUtils.makeObserved(new Array<number>()),
  9. })!;

  11. @Local arr2: Array<number> = PersistenceV2.globalConnect({
  12. type: Array<number>,
  13. key: 'arr2',
  14. defaultCreator: () => UIUtils.makeObserved(new Array<number>()),
  15. })!;
  16. // ...
  17. }
  ```

3、不支持非built-in类型，如[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)、NativePointer、[ArrayList](../harmonyos-references/js-apis-arraylist.md)等Native类型。

4、在API version 23以前，单个key支持数据大小约8k，过大会导致持久化失败。

* 在API version 23开始，解除单个key只能持久化8K数据的限制，读取和写入持久化存储的数据会在UI线程中同步进行，但开发者需要注意，不建议开发者在UI线程存储大量的持久化数据，会导致界面卡顿。

5、在API version 23以前，持久化的数据必须是class对象，不支持容器类型（如Array、Set、Map），不支持built-in的构造对象（如String、Number），不支持持久化基本类型（如string、number、boolean）。如果需要持久化非class对象，建议使用[Preferences](preferences-guidelines.md)进行数据持久化。

* 在API version 23开始，支持持久化Class类型和容器类型（Array、Set、Map，Date）。支持built-in的构造对象类型（如String、Number）及基本类型（如string、number、boolean）作为class属性的持久化（String、Number是不可变的数据对象，没法直接作为[顶层数据类型](arkts-new-persistencev2.md#globalconnect顶层持久化数据类型及非顶层数据类型)进行持久化）。对于不支持的类型，会抛出运行时报错，从API version 23开始，将返回错误码[140103](../harmonyos-references/errorcode-statemanagement.md#section140103-appstoragev2和persistencev2使用不支持的数据类型)。

  如下为新增globalConnect支持Array<ClassA>类型的持久化示例：

  ```
  1. import { PersistenceV2, UIUtils } from '@kit.ArkUI';

  3. @ObservedV2
  4. class ClassA {
  5. @Trace public propA: string = '';
  6. @Trace public propB: string = '';

  8. public report(): string {
  9. return `${this.propA} - ${this.propB}`;
  10. }
  11. }

  13. @Entry
  14. @ComponentV2
  15. struct Comp {
  16. // 持久化顶层数据类型为Array<ClassA>的数据
  17. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
  18. type: Array<ClassA>,
  19. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
  20. // 添加defaultSubCreator，通知状态管理框架如何创建数组项
  21. // 另外持久化的数据需要加上makeObserved，因为JSON对象本身没有观察能力，自动持久化会失败
  22. defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
  23. })!;

  25. build() {
  26. Column() {
  27. Repeat(this.arr)
  28. .each(ri => {
  29. Row() {
  30. Text(`propA '${ri.item.propA}'`)
  31. Text(`propB '${ri.item.propB}'`)
  32. Text(`report?.() '${ri.item.report?.()}'`)
  33. }
  34. })
  35. // 点击'add item',显示`propA 'a' propB 'b'report?.'a' - 'b'`, 杀掉应用，再次进入，会显示上次的结果
  36. Button('add item')
  37. .onClick(() => {
  38. let temp: ClassA = new ClassA();
  39. temp.propA = 'a';
  40. temp.propB = 'b';
  41. this.arr.push(temp);
  42. })
  43. }
  44. }
  45. }
  ```

  如下为globalConnect支持Date类型的持久化示例：

  ```
  1. import { PersistenceV2, UIUtils } from '@kit.ArkUI';

  3. @Entry
  4. @ComponentV2
  5. struct Page1 {
  6. // 支持直接持久化Date类型的数据
  7. @Local date: Date = PersistenceV2.globalConnect({
  8. type: Date,
  9. defaultCreator: () => UIUtils.makeObserved(new Date())
  10. })!;

  12. build() {
  13. Column({ space: 40 }) {
  14. Text(`date: ${this.date.toISOString()}`)
  15. .fontSize(24)
  16. // 点击'date.setTime( Date.now() )', 杀掉应用，进入应用后，显示日期
  17. Button('date.setTime( Date.now() )')
  18. .onClick(() => {
  19. this.date.setTime(Date.now());
  20. })
  21. .fontSize(24)
  22. }
  23. .width('100%')
  24. }
  25. }
  ```

  如下为globalConnect支持Number类型作为class子属性的持久化示例：

  ```
  1. import { PersistenceV2 } from '@kit.ArkUI';

  3. @ObservedV2 class NumberClass {
  4. // Number类型不是顶层持久化数据类型，只能支持非顶层数据类型的持久化
  5. @Trace public value: Number = new Number(Infinity);
  6. }

  8. @Entry
  9. @ComponentV2
  10. struct Page1 {
  11. // Number类型只能作为NumberClass的子属性去持久化
  12. @Local number: NumberClass = PersistenceV2.globalConnect({
  13. type: NumberClass,
  14. defaultCreator: () => new NumberClass()
  15. })!;
  16. output: string[] = [];

  18. aboutToAppear(): void {
  19. this.output.push(`this.number.value: ${this.number.value}, is instanceof Number ${this.number.value instanceof Number}`);
  20. this.number.value = new Number(-this.number.value);
  21. }

  23. build() {
  24. Column() {
  25. Row() {
  26. // 第一次打开应用，界面显示'this.number.value: Infinity, is instanceof Number true'
  27. // 第二次打开应用，界面显示'this.number.value: -Infinity, is instanceof Number true'
  28. Text(this.output.join('\n\n'))
  29. .fontSize(24)
  30. }
  31. }
  32. .width('100%')
  33. }
  34. }
  ```

6、在API version 23以前，不支持循环引用对象的持久化。

* 在API version 23开始，提供globalConnect接口支持循环引用的对象持久化。

  如下为globalConnect支持循环引用的对象的持久化示例：

  ```
  1. import { PersistenceV2 } from '@kit.ArkUI';

  3. @ObservedV2
  4. class ClassA {
  5. @Trace public value: string = 'a';
  6. @Trace public refB: ClassB | undefined;
  7. }

  9. @ObservedV2
  10. class ClassB {
  11. @Trace public value: string = 'b';
  12. @Trace public refA: ClassA | undefined;
  13. }

  15. @ObservedV2
  16. class ClassC {
  17. @Trace public value: string = 'c';
  18. @Trace public objA: ClassA = new ClassA();
  19. @Trace public objB: ClassB = new ClassB();

  21. // ClassC是循环引用对象
  22. constructor() {
  23. this.objA.refB = this.objB;
  24. this.objB.refA = this.objA;
  25. }
  26. }

  28. @Entry
  29. @ComponentV2
  30. struct Page1 {
  31. @Local test: ClassC = PersistenceV2.globalConnect({
  32. type: ClassC,
  33. defaultCreator: () => new ClassC()
  34. })!;
  35. output: string[] = [];

  37. aboutToAppear(): void {
  38. const refAValue = this.test.objA?.refB?.refA?.value;
  39. const refBValue = this.test.objB?.refA?.refB?.value;
  40. this.output.push(`${refAValue}, ${refBValue}`);
  41. this.test.objA.value += 'a';
  42. this.test.objB.value += 'b';
  43. }

  45. build() {
  46. Column() {
  47. Row() {
  48. // 第一次打开应用，界面显示'a, b'
  49. // 第二次打开应用，界面显示'aa, bb'
  50. Text(this.output.join('\n\n'))
  51. .fontSize(24)
  52. }
  53. }
  54. .width('100%')
  55. }
  56. }
  ```

7、只有[@Trace](arkts-new-observedv2-and-trace.md)的数据改变会触发自动持久化，如V1状态变量、[@Observed](arkts-observed-and-objectlink.md)对象、普通数据的改变不会触发持久化。

8、connect和globalConnect不建议混用，如果混用，key不能一样，否则应用crash，从API version 23开始，将返回错误码[140105](../harmonyos-references/errorcode-statemanagement.md#section140105-persistencev2混用connect和globalconnect并使用相同的key)。

9、PersistenceV2必须与UI实例关联，持久化操作需在UI实例初始化完成后调用（即[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)回调触发后）。

```
1. // EntryAbility.ets
2. // 以下为代码片段，需要开发者自己在EntryAbility.ets中补全
3. import { PersistenceV2 } from '@kit.ArkUI';

5. // 在EntryAbility外部定义class
6. @ObservedV2
7. class Storage {
8. @Trace isPersist: boolean = false;
9. }

11. // 在onWindowStageCreate的loadContent回调中调用PersistenceV2
12. onWindowStageCreate(windowStage: window.WindowStage): void {
13. windowStage.loadContent('pages/Index', (err) => {
14. if (err.code) {
15. return;
16. }
17. PersistenceV2.connect(Storage, () => new Storage());
18. });
19. }
```

10、如果开发者对数据持久化能力有较强的诉求，例如持久化时机，建议使用[Preferences](preferences-guidelines.md)进行数据持久化。注意：不允许混用PersistenceV2和Preferences，因为Preferences存储的数据不会有状态变量信息，反序列化的数据不能触发PersistenceV2的自动化存储。

11、当开发者使用globalConnect持久化数据，从磁盘读取数据时，需要保证key数据在持久化前后类型一致。从API version 23开始，将返回错误码[140107](../harmonyos-references/errorcode-statemanagement.md#section140107-appstoragev2和persistencev2数据类型不匹配)。

12、globalConnect仅支持设置EL1-EL5加密级别，否则会抛出运行时异常，从API version 23开始，将返回错误码[140106](../harmonyos-references/errorcode-statemanagement.md#section140106-使用persistencev2存储数据到不支持的加密级别)，示例见[使用globalConnect存储数据](arkts-new-persistencev2.md#使用globalconnect存储数据)。

## globalConnect支持的类型

### globalConnect顶层持久化数据类型及非顶层数据类型

在API version 23以前，持久化的顶层数据类型必须是用户自定义的class对象，不支持容器类型（如Array、Set、Map，Date）。在API version 23开始，持久化的顶层数据类型可以是用户自定义的class，也可以是容器类型。非顶层数据类型，是指定义在用户自定义class属性的类型。

如下示例中，Array<ClassA>是顶层持久化数据类型, 可作为globalConnect的直接返回值类型，collections.Map是CollectionMapClass类中属性的类型，属于非顶层持久化的数据类型。

```
1. class ClassA {
2. propA: number;

4. }
5. @Sendable
6. class CollectionMapClass {
7. // 用户自定义的class中属性类型为collections.Map，非顶层持久化数据类型
8. value = new collections.Map<number, number>([]);
9. }

11. @ComponentV2
12. struct Page1 {
13. // 顶层持久化数据类型为Array<ClassA>
14. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
15. type: Array<ClassA>,
16. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
17. // 添加defaultSubCreator，通知状态管理框架如何创建数组项
18. // 另外持久化后的数据需要加上makeObserved，否则会持久化失败
19. defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
20. })!;

22. // 顶层持久化数据类型为用户自定义的class，collections.Map为非顶层持久化数据类型
23. collectionMap: CollectionMapClass = PersistenceV2.globalConnect({
24. type: CollectionMapClass,
25. defaultCreator: () => new CollectionMapClass()
26. })!
27. // ...
28. }
```

### globalConnect用户自定义class对象属性支持的类型

用户自定义class对象的属性可以使用以下类型：boolean、number、string、undefined、null、Object、Date、Number、Boolean、String以及自定义类class。还支持以下集合类型：Array、Map、Set。

```
1. // 观察类的@Trace属性支持上述所有类型
2. @ObservedV2
3. class ClassA {
4. // VType是上述列举的类型
5. @Trace propA: VType;
6. }

8. @ComponentV2 struct Comp {
9. @Local obsObj : ClassA = PersistenceV2.globalConnect({
10. type: ClassA,
11. defaultCreator: () => new ClassA()
12. })
13. // ...
14. }
```

用户自定义class类型的属性必须使用@Type装饰器装饰，且其class属性值必须严格为@Type中指定类的实例。

```
1. class ClassA {
2. // ...
3. }
4. class PersistClass {
5. @Type(ClassA)
6. propA: ClassA = new ClassA();
7. }
```

### globalConnect支持集合的类型

集合类型是指Array<V>、Map<K, V>、Set<V>、collections.Array<V>、collections.Map<K, V>、collections.Set<V>。

其中，Map<K, V>和collections.Map<k, V>中的key值类型（K）是指string或number类型。

Array<V>、Map<K, V>和 Set<V>中，V的类型包括：boolean、number、string、Date、Number、Boolean、String、interface类型和class类型。

collections.Array<V>、collections.Map<K, V>、collections.Set<V>要求V的类型必须是@Sendable类型的数据（boolean、number、string类型）。

如下展示globalConnect持久化Array<ClassA>的示例：

```
1. import { PersistenceV2,  UIUtils } from '@kit.ArkUI';

3. class ClassA {
4. public propA: number = 0;
5. public classAToString() : string {
6. return this.propA.toString()
7. }
8. }

10. @Entry
11. @ComponentV2
12. struct Page1 {
13. @Local arr: Array<ClassA> = PersistenceV2.globalConnect({
14. type: Array<ClassA>,
15. defaultCreator: () => UIUtils.makeObserved(new Array<ClassA>()),
16. // 添加defaultSubCreator，通知状态管理框架如何创建ClassA对象
17. // 另外持久化后的数据需要加上makeObserved，否则会持久化失败
18. defaultSubCreator: () => UIUtils.makeObserved(new ClassA())
19. })!;

21. build() {
22. Column({ space: 10 }) {
23. Column({ space: 0 }) {
24. Repeat(this.arr)
25. .each(ri => {
26. Row() {
27. Text(`Item: `)
28. Text(ri.item.classAToString ? ri.item.classAToString(): `classAToString() missing from object, propA: ${ri.item.propA}`)
29. }
30. })
31. .key((item: ClassA, index: number) => `${index} - ${item.propA}`)
32. }

34. Divider().width('100%')
35. // 点击'array.push(0)'，重启应用，Repeat数组项是：1, 2, 0
36. Button('array.push(0)')
37. .onClick(() => {
38. let temp = new ClassA();
39. temp.propA = 0;
40. this.arr.push(UIUtils.makeObserved(temp));
41. })
42. .fontSize(24)
43. // 点击'array.pop()'，重启应用，Repeat数组项是：1, 2
44. Button('array.pop()')
45. .onClick(() => {
46. this.arr.pop();
47. })
48. .fontSize(24)
49. // 点击'array.splice(0)'，重启应用，Repeat数组项为空
50. Button('array.splice(0)')
51. .onClick(() => {
52. this.arr.splice(0);
53. })
54. .fontSize(24)
55. // 点击'splice(1, 0, random)'，重启应用：Repeat组件再次显示相同的数组项
56. Button('array.splice(1, 0, random)')
57. .onClick(() => {
58. let temp = new ClassA();
59. temp.propA = Math.round(100 * Math.random());
60. this.arr.splice(1, 0, UIUtils.makeObserved(temp));
61. })
62. .fontSize(24)
63. // 点击'array.splice(0, 2, random, random)'，前两个数组项目被替换，记录下来
64. // 重启应用：Repeat组件再次显示数组项
65. Button('array.splice(0, 2, random, random)')
66. .onClick(() => {
67. let tempA = new ClassA();
68. tempA.propA = Math.round(100 * Math.random());
69. this.arr.splice(2, 2,
70. UIUtils.makeObserved(tempA),
71. UIUtils.makeObserved(tempA));
72. })
73. .fontSize(24)
74. // 点击'array.sort', 对数组项升序排列，重启应用，Repeat组件展示升序数组
75. Button('array.sort')
76. .onClick(() => {
77. this.arr.sort((tempA, tempB)=> tempA.propA - tempB.propA);
78. })
79. .fontSize(24)
80. // 点击'array.reverse', 对数组项降序排列，重启应用，Repeat组件展示降序数组
81. Button('array.reverse')
82. .onClick(() => {
83. this.arr.reverse();
84. })
85. .fontSize(24)
86. }
87. .width('100%')
88. }
89. }
```

## 使用场景

### 在两个页面之间存储数据

数据页面

```
1. // Sample.ets
2. import { Type } from '@kit.ArkUI';

4. // 数据中心
5. @ObservedV2
6. class SampleChild {
7. @Trace public p1: number = 0;
8. public p2: number = 10;
9. }

11. @ObservedV2
12. export class Sample {
13. // 对于复杂对象需要@Type修饰，确保序列化成功
14. @Type(SampleChild)
15. @Trace public f: SampleChild = new SampleChild();
16. }
```

[Sample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/Sample.ets#L16-L34)

页面1

```
1. // Page1.ets
2. import { PersistenceV2 } from '@kit.ArkUI';
3. import { Sample } from '../Sample';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0x0000;

8. // 接受序列化失败的回调
9. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
10. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
11. });

13. @Entry
14. @ComponentV2
15. struct Page1 {
16. // 在PersistenceV2中创建一个key为Sample的键值对（如果存在，则返回PersistenceV2中的数据），并且和prop关联
17. // 对于需要换connect对象的prop属性，需要加@Local修饰（不建议对属性换connect的对象）
18. @Local prop: Sample = PersistenceV2.connect(Sample, () => new Sample())!;
19. pageStack: NavPathStack = new NavPathStack();

21. build() {
22. Navigation(this.pageStack) {
23. Column() {
24. Button('Go to page2')
25. .onClick(() => {
26. this.pageStack.pushPathByName('Page2', null);
27. })

29. Button('Page1 connect the key Sample')
30. .onClick(() => {
31. // 在PersistenceV2中创建一个key为Sample的键值对（如果存在，则返回PersistenceV2中的数据），并且和prop关联
32. // 不建议对prop属性换connect的对象
33. this.prop = PersistenceV2.connect(Sample, 'Sample', () => new Sample())!;
34. })

36. Button('Page1 remove the key Sample')
37. .onClick(() => {
38. // 从PersistenceV2中删除后，prop将不会再与key为Sample的值关联
39. PersistenceV2.remove(Sample);
40. })

42. Button('Page1 save the key Sample')
43. .onClick(() => {
44. // 如果处于connect状态，持久化key为Sample的键值对
45. PersistenceV2.save(Sample);
46. })

48. Text(`Page1 add 1 to prop.p1: ${this.prop.f.p1}`)
49. .fontSize(30)
50. .onClick(() => {
51. this.prop.f.p1++;
52. })

54. Text(`Page1 add 1 to prop.p2: ${this.prop.f.p2}`)
55. .fontSize(30)
56. .onClick(() => {
57. // 页面不刷新，但是p2的值改变了
58. this.prop.f.p2++;
59. })

61. // 获取当前PersistenceV2里面的所有key
62. Text(`all keys in PersistenceV2: ${PersistenceV2.keys()}`)
63. .fontSize(30)
64. }
65. }
66. }
67. }
```

[Page1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/page/Page1.ets#L16-L84)

页面2

```
1. // Page2.ets
2. import { PersistenceV2 } from '@kit.ArkUI';
3. import { Sample } from '../Sample';

5. @Builder
6. export function Page2Builder() {
7. Page2()
8. }

10. @ComponentV2
11. struct Page2 {
12. // 在PersistenceV2中创建一个key为Sample的键值对（如果存在，则返回PersistenceV2中的数据），并且和prop关联
13. // 对于需要换connect对象的prop属性，需要加@Local修饰（不建议对属性换connect的对象）
14. @Local prop: Sample = PersistenceV2.connect(Sample, () => new Sample())!;
15. pathStack: NavPathStack = new NavPathStack();

17. build() {
18. NavDestination() {
19. Column() {
20. Button('Page2 connect the key Sample1')
21. .onClick(() => {
22. // 在PersistenceV2中创建一个key为Sample1的键值对（如果存在，则返回PersistenceV2中的数据），并且和prop关联
23. // 不建议对prop属性换connect的对象
24. this.prop = PersistenceV2.connect(Sample, 'Sample1', () => new Sample())!;
25. })

27. Text(`Page2 add 1 to prop.p1: ${this.prop.f.p1}`)
28. .fontSize(30)
29. .onClick(() => {
30. this.prop.f.p1++;
31. })

33. Text(`Page2 add 1 to prop.p2: ${this.prop.f.p2}`)
34. .fontSize(30)
35. .onClick(() => {
36. // 页面不刷新，但是p2的值改变了；只有重新初始化才会改变
37. this.prop.f.p2++;
38. })

40. // 获取当前PersistenceV2里面的所有key
41. Text(`all keys in PersistenceV2: ${PersistenceV2.keys()}`)
42. .fontSize(30)
43. }
44. }
45. .onReady((context: NavDestinationContext) => {
46. this.pathStack = context.pathStack;
47. })
48. }
49. }
```

[Page2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/page/Page2.ets#L16-L66)

使用Navigation时，需要添加配置系统路由表文件src/main/resources/base/profile/route\_map.json，并替换pageSourceFile为Page2页面的路径，并且在module.json5中添加："routerMap": "$profile:route\_map"。

```
1. {
2. "routerMap": [
3. {
4. "name": "Page2",
5. "pageSourceFile": "src/main/ets/pages/Page2.ets",
6. "buildFunction": "Page2Builder",
7. "data": {
8. "description" : "PersistenceV2 example"
9. }
10. }
11. ]
12. }
```

### 使用globalConnect存储数据

```
1. import { PersistenceV2, Type, ConnectOptions } from '@kit.ArkUI';
2. import { contextConstant } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;
6. // 接受序列化失败的回调
7. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
8. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
9. });

11. @ObservedV2
12. class SampleChild {
13. @Trace public childId: number = 0;
14. public groupId: number = 1;
15. }

17. @ObservedV2
18. export class SampleGlobalConnect {
19. // 对于复杂对象需要@Type修饰，确保序列化成功
20. @Type(SampleChild)
21. @Trace public father: SampleChild = new SampleChild();
22. }

24. @Entry
25. @ComponentV2
26. struct Page1 {
27. @Local refresh: number = 0;
28. // key不传入尝试用为type的name作为key，加密参数不传入默认加密等级为EL2
29. @Local p: SampleGlobalConnect =
30. PersistenceV2.globalConnect({ type: SampleGlobalConnect, defaultCreator: () => new SampleGlobalConnect() })!;
31. // 使用key:global1连接，传入加密等级为EL1
32. @Local p1: SampleGlobalConnect = PersistenceV2.globalConnect({
33. type: SampleGlobalConnect,
34. key: 'global1',
35. defaultCreator: () => new SampleGlobalConnect(),
36. areaMode: contextConstant.AreaMode.EL1
37. })!;
38. // 使用key:global2连接，使用构造函数形式，加密参数不传入默认加密等级为EL2
39. options: ConnectOptions<SampleGlobalConnect> =
40. { type: SampleGlobalConnect, key: 'global2', defaultCreator: () => new SampleGlobalConnect() };
41. @Local p2: SampleGlobalConnect = PersistenceV2.globalConnect(this.options)!;
42. // 使用key:global3连接，直接写加密数值，范围只能在0-4，否则运行会crash,例如加密设置为EL3
43. @Local p3: SampleGlobalConnect = PersistenceV2.globalConnect({
44. type: SampleGlobalConnect,
45. key: 'global3',
46. defaultCreator: () => new SampleGlobalConnect(),
47. areaMode: 3
48. })!;

50. build() {
51. Column() {
52. // 显示数据
53. // 被@Trace修饰的数据可以自动持久化进磁盘
54. Text('Key SampleGlobalConnect: ' + this.p.father.childId.toString())
55. .onClick(() => {
56. this.p.father.childId += 1;
57. })
58. .fontSize(25)
59. .fontColor(Color.Red)
60. Text('Key global1: ' + this.p1.father.childId.toString())
61. .onClick(() => {
62. this.p1.father.childId += 1;
63. })
64. .fontSize(25)
65. .fontColor(Color.Red)
66. Text('Key global2: ' + this.p2.father.childId.toString())
67. .onClick(() => {
68. this.p2.father.childId += 1;
69. })
70. .fontSize(25)
71. .fontColor(Color.Red)
72. Text('Key global3: ' + this.p3.father.childId.toString())
73. .onClick(() => {
74. this.p3.father.childId += 1;
75. })
76. .fontSize(25)
77. .fontColor(Color.Red)
78. // keys接口
79. // keys本身不会刷新，需要借助状态变量刷新
80. Text('Persist keys: ' + PersistenceV2.keys().toString() + ' refresh: ' + this.refresh)
81. .onClick(() => {
82. this.refresh += 1;
83. })
84. .fontSize(25)

86. // remove接口
87. Text('Remove key SampleGlobalConnect: ' + 'refresh: ' + this.refresh)
88. .onClick(() => {
89. // 删除这个key，会导致和p失去联系，之后即使reconnect，p也无法存储
90. PersistenceV2.remove(SampleGlobalConnect);
91. this.refresh += 1;
92. })
93. .fontSize(25)
94. Text('Remove key global1: ' + 'refresh: ' + this.refresh)
95. .onClick(() => {
96. // 删除这个key，会导致和p1失去联系，之后即使reconnect，p1也无法存储
97. PersistenceV2.remove('global1');
98. this.refresh += 1;
99. })
100. .fontSize(25)
101. Text('Remove key global2: ' + 'refresh: ' + this.refresh)
102. .onClick(() => {
103. // 删除这个key，会导致和p2失去联系，之后即使reconnect，p2也无法存储
104. PersistenceV2.remove('global2');
105. this.refresh += 1;
106. })
107. .fontSize(25)
108. Text('Remove key global3: ' + 'refresh: ' + this.refresh)
109. .onClick(() => {
110. // 删除这个key，会导致和p3失去联系，之后即使reconnect，p3也无法存储
111. PersistenceV2.remove('global3');
112. this.refresh += 1;
113. })
114. .fontSize(25)
115. // reConnect
116. // 重新连接也无法和之前的状态变量建立联系，因此无法保存数据
117. Text('ReConnect key global2: ' + 'refresh: ' + this.refresh)
118. .onClick(() => {
119. // 此时会重新存储一个key为global2的变量，但该变量与p2无关
120. PersistenceV2.globalConnect(this.options);
121. this.refresh += 1;
122. })
123. .fontSize(25)

125. // save接口
126. Text('not save key SampleGlobalConnect: ' + this.p.father.groupId.toString() + ' refresh: ' + this.refresh)
127. .onClick(() => {
128. // 未被@Trace保存的对象无法自动存储
129. this.p.father.groupId += 1;
130. this.refresh += 1;
131. })
132. .fontSize(25)
133. Text('save key SampleGlobalConnect: ' + this.p.father.groupId.toString() + ' refresh: ' + this.refresh)
134. .onClick(() => {
135. // 未被@Trace保存的对象无法自动存储，需要调用save存储
136. this.p.father.groupId += 1;
137. PersistenceV2.save(SampleGlobalConnect);
138. this.refresh += 1;
139. })
140. .fontSize(25)
141. }
142. .width('100%')
143. }
144. }
```

[PersistenceV2GlobalConnect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/PersistenceV2GlobalConnect.ets#L15-L160)

### 在不同的module中使用connect和globalConnect

**connect的存储路径需要注意以下两点：**

1、connect使用module级别的存储路径，以最先启动的module的路径作为存储路径，从内存回写磁盘时会回写到第一个连接该module的路径。应用如果之后先从另一个module启动，则会以新module的路径作为存储路径。

2、当不同module使用相同的key时，哪个module先启动，数据就为哪个module中保存的键值对，回写到对应的module中。

**globalConnect的存储路径需要注意：**

globalConnect虽然是应用级别的路径，但是可以设置不同的加密分区，不同加密分区即代表不同的存储路径。connect不支持设置加密分区，但是module自身切换加密级别时，module存储路径也会切换成对应加密分区路径。

示例代码如下：开发者需要在项目基础上，新建一个module，并按照示例代码跳转到新module中。

```
1. // 模块1
2. import { PersistenceV2, Type } from '@kit.ArkUI';
3. import { common, Want } from '@kit.AbilityKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { contextConstant } from '@kit.AbilityKit';

7. const DOMAIN = 0x0000;

9. // 接受序列化失败的回调
10. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
11. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
12. });

14. @ObservedV2
15. class SampleChild {
16. @Trace public childId: number = 0;
17. public groupId: number = 1;
18. }

20. @ObservedV2
21. export class Sample {
22. // 对于复杂对象需要@Type修饰，确保序列化成功
23. @Type(SampleChild)
24. @Trace public father: SampleChild = new SampleChild();
25. }

27. @Entry
28. @ComponentV2
29. struct Page1 {
30. @Local refresh: number = 0;
31. // 使用key:globalConnect1连接，传入加密等级为EL1
32. @Local p1: Sample =
33. PersistenceV2.globalConnect({
34. type: Sample,
35. key: 'globalConnect1',
36. defaultCreator: () => new Sample(),
37. areaMode: contextConstant.AreaMode.EL1
38. })!;
39. // 使用key:connect2连接，使用构造函数形式，加密参数不传入默认加密等级为EL2
40. @Local p2: Sample = PersistenceV2.connect(Sample, 'connect2', () => new Sample())!;
41. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

43. build() {
44. Column() {
45. // 显示数据
46. Text('Key globalConnect1: ' + this.p1.father.childId.toString())
47. .onClick(() => {
48. this.p1.father.childId += 1;
49. })
50. .fontSize(25)
51. .fontColor(Color.Red)
52. Text('Key connect2: ' + this.p2.father.childId.toString())
53. .onClick(() => {
54. this.p2.father.childId += 1;
55. })
56. .fontSize(25)
57. .fontColor(Color.Red)

59. // 跳转
60. Button('Jump to newModule')
61. .onClick(() => { // 不同module之间使用，建议使用globalConnect
62. let want: Want = {
63. deviceId: '', // deviceId为空代表本设备
64. bundleName: 'com.samples.paradigmstatemanagement', // 在app.json5中查看
65. moduleName: 'demo', // 在需要跳转的module的module.json5中查看，非必选参数
66. abilityName: 'NewModuleAbility', // 跳转启动的ability，在需要跳转的module的module.json5中查看
67. uri: 'src/main/ets/pages/Index'
68. };
69. // context为调用方UIAbility的UIAbilityContext
70. this.context.startAbility(want).then(() => {
71. hilog.info(DOMAIN, 'testTag', '%{public}s', 'start ability success');
72. }).catch((err: Error) => {
73. hilog.error(DOMAIN, 'testTag', '%{public}s',
74. `start ability failed. code is ${err.name}, message is ${err.message}`);
75. });
76. })
77. }
78. .width('100%')
79. .borderWidth(3)
80. .borderColor(Color.Blue)
81. .margin({ top: 5, bottom: 5 })
82. }
83. }
```

[PersistenceV2ModuleConnectStorage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/PersistenceV2ModuleConnectStorage1.ets#L16-L100)

```
1. // 模块2
2. import { PersistenceV2, Type } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { contextConstant } from '@kit.AbilityKit';

6. const DOMAIN = 0x0000;
7. // 接受序列化失败的回调
8. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
9. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
10. });

12. @ObservedV2
13. class SampleChild {
14. @Trace public childId: number = 0;
15. public groupId: number = 1;
16. }

18. @ObservedV2
19. export class Sample {
20. // 对于复杂对象需要@Type修饰，确保序列化成功
21. @Type(SampleChild)
22. @Trace public father: SampleChild = new SampleChild();
23. }

25. @Entry
26. @ComponentV2
27. struct Page1 {
28. @Local a: number = 0;
29. // 使用key:globalConnect1连接，传入加密等级为EL1
30. @Local p1: Sample =
31. PersistenceV2.globalConnect({ type: Sample, key: 'globalConnect1', defaultCreator: () => new Sample(), areaMode: contextConstant.AreaMode.EL1 })!;
32. // 使用key:connect2连接，使用构造函数形式，加密参数不传入默认加密等级为EL2
33. @Local p2: Sample = PersistenceV2.connect(Sample, 'connect2', () => new Sample())!;

35. build() {
36. Column() {
37. // 显示数据
38. Text('Key globalConnect1: ' + this.p1.father.childId.toString())
39. .onClick(() => {
40. this.p1.father.childId += 1;
41. })
42. .fontSize(25)
43. .fontColor(Color.Red)
44. Text('Key connect2: ' + this.p2.father.childId.toString())
45. .onClick(() => {
46. this.p2.father.childId += 1;
47. })
48. .fontSize(25)
49. .fontColor(Color.Red)
50. }
51. .width('100%')
52. }
53. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/demo/src/main/ets/pages/Index.ets#L16-L70)

当开发者对newModule使用不同启动方式会有以下现象：

* 开发者直接启动newModule，分别修改globalConnect1和connect2绑定的变量，例如将childId都改成5。
* 应用退出并清空后台，启动模块entry，通过跳转按键启动newModule，会发现globalConnect1值为5，而connect2值为0未修改。
* globalConnect为应用级别存储，对于一个key，整个应用在对应加密分区只有一份存储路径；connect为module级别的存储路径，会因为module的启动方式不同而在各自的加密分区对应不同的存储路径。

## 使用建议

建议开发者使用新接口globalConnect创建和获取数据。globalConnect的存储规格和内存规格一致，对于应用只有一份，并且支持设置加密级别，不需要去切换ability的加密才能设置数据的加密级别。当然如果开发者应用不涉及多模块，保持使用connect也不会有影响。

### connect向globalConnect迁移实现

```
1. // 使用connect存储数据
2. import { PersistenceV2, Type } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. // 接受序列化失败的回调
8. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
9. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
10. });

12. @ObservedV2
13. class SampleChild {
14. @Trace public childId: number = 0;
15. public groupId: number = 1;
16. }

18. @ObservedV2
19. export class Sample {
20. // 对于复杂对象需要@Type修饰，确保序列化成功
21. @Type(SampleChild)
22. @Trace public father: SampleChild = new SampleChild();
23. }

25. @Entry
26. @ComponentV2
27. struct Page1 {
28. @Local refresh: number = 0;
29. // 使用key:connect3存储
30. @Local p: Sample = PersistenceV2.connect(Sample, 'connect3', () => new Sample())!;

32. build() {
33. Column({ space: 5 }) {
34. // 显示数据
35. Text('Key connect3: ' + this.p.father.childId.toString())
36. .onClick(() => {
37. this.p.father.childId += 1;
38. })
39. .fontSize(25)
40. .fontColor(Color.Red)

42. // save接口
43. // 未被@Trace装饰的变量需要借助状态变量refresh才能刷新
44. Text('save key connect3: ' + this.p.father.groupId.toString() + ' refresh:' + this.refresh)
45. .onClick(() => {
46. // 未被@Trace保存的对象无法自动存储，需要调用save存储
47. this.p.father.groupId += 1;
48. PersistenceV2.save('connect3');
49. this.refresh += 1;
50. })
51. .fontSize(25)
52. }
53. .width('100%')
54. }
55. }
```

[PersistenceV2ConnectMigration1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/PersistenceV2ConnectMigration1.ets#L16-L72)

```
1. // 迁移到globalConnect
2. import { PersistenceV2, Type } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const DOMAIN = 0x0000;

7. // 接受序列化失败的回调
8. PersistenceV2.notifyOnError((key: string, reason: string, msg: string) => {
9. hilog.error(DOMAIN, 'testTag', '%{public}s', `error key: ${key}, reason: ${reason}, message: ${msg}`);
10. });

12. @ObservedV2
13. class SampleChild {
14. @Trace public childId: number = 0;
15. public groupId: number = 1;
16. }

18. @ObservedV2
19. export class Sample {
20. // 对于复杂对象需要@Type修饰，确保序列化成功
21. @Type(SampleChild)
22. @Trace public father: SampleChild = new SampleChild();
23. }

25. // 用于判断是否完成数据迁移的辅助数据
26. @ObservedV2
27. class StorageState {
28. @Trace public isCompleteMoving: boolean = false;
29. }

31. function move() {
32. let movingState = PersistenceV2.globalConnect({ type: StorageState, defaultCreator: () => new StorageState() })!;
33. if (!movingState.isCompleteMoving) {
34. let p: Sample = PersistenceV2.connect(Sample, 'connect3', () => new Sample())!;
35. PersistenceV2.remove('connect3');
36. let p1 = PersistenceV2.globalConnect({ type: Sample, key: 'connect4', defaultCreator: () => p })!; // 使用默认构造函数也可以
37. // 赋值数据，@Trace修饰的会自动保存
38. p1.father = p.father;
39. // 将迁移标志设置为true
40. movingState.isCompleteMoving = true;
41. }
42. }

44. move();

46. @Entry
47. @ComponentV2
48. struct Page1 {
49. @Local refresh: number = 0;
50. // 使用key:connect4存入数据
51. @Local p: Sample =
52. PersistenceV2.globalConnect({ type: Sample, key: 'connect4', defaultCreator: () => new Sample() })!;

54. build() {
55. Column({ space: 5 }) {
56. // 显示数据
57. Text('Key connect4: ' + this.p.father.childId.toString())
58. .onClick(() => {
59. this.p.father.childId += 1;
60. })
61. .fontSize(25)
62. .fontColor(Color.Red)

64. // save接口
65. // 未被@Trace装饰的变量需要借助状态变量refresh才能刷新
66. Text('save key connect4: ' + this.p.father.groupId.toString() + ' refresh:' + this.refresh)
67. .onClick(() => {
68. // 未被@Trace保存的对象无法自动存储，需要调用save存储
69. this.p.father.groupId += 1;
70. PersistenceV2.save('connect4');
71. this.refresh += 1;
72. })
73. .fontSize(25)
74. }
75. .width('100%')
76. }
77. }
```

[PersistenceV2ConnectMigration2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/persistenceV2/PersistenceV2ConnectMigration2.ets#L16-L94)

connect向globalConnect迁移，需要将key绑定的value赋值给globalConnect进行存储，之后当自定义组件使用globalConnect连接时，globalConnect绑定的数据即为之前使用connect保存的数据，开发者可以自定义move函数，并将其放在合适位置迁移即可。
